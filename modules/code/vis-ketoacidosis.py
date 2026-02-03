import os
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from simulate import MetabolicEnvironment, LiverMetabolismSystem

def _get_series(df, col):
    if col in df.columns:
        return df[col]
    return pd.Series(0.0, index=df.index)

def generate_dka_dashboard(history_list, filename="dka_simulation.html"):
    df = pd.DataFrame(history_list)
    time_steps = df['time'].values
    
    # 1. Define nodes for DKA topology
    # Lipolysis -> Fatty Acid -> Beta-Oxidation -> Acetyl-CoA -> Ketogenesis -> Ketone Bodies
    #                                             |
    #                                             v
    #                                            TCA (Energy)
    nodes = {
        "Lipolysis_Mod": [1, 3, "脂肪分解(Lipolysis)"],
        "BetaOx_Mod": [2, 3, "β-氧化(Beta-Ox)"],
        "Ketogenesis_Mod": [3, 4, "酮体生成(Ketogenesis)"],
        "TCA_Mod": [3, 2, "TCA循环"],
        "Gluconeogenesis_Mod": [2, 1, "糖异生"]
    }
    
    # Calculate approximate pH based on ketone bodies (Simplified model)
    # Normal pH 7.4. Ketones are acidic.
    # Assume pH = 7.4 - k * ketone_body
    # DKA ketone levels can reach 10-20 mmol/L.
    # pH can drop to 7.0 or lower.
    # Let's say at 20 mmol/L ketones, pH is 6.9. Drop = 0.5.
    # k = 0.5 / 20 = 0.025
    df['simulated_pH'] = 7.4 - 0.025 * _get_series(df, 'ketone_body')
    
    # 2. Initialize Canvas
    fig = make_subplots(
        rows=1, cols=3,
        column_widths=[0.32, 0.43, 0.25],
        specs=[[{"type": "scatter"}, {"type": "scatter"}, {"type": "scatter"}]],
        subplot_titles=("代谢通量拓扑 (颜色深浅=速率)", "关键代谢物浓度 & pH", "关键反应速率")
    )

    # 3. Create Frames
    frames = []
    for t_idx in range(len(time_steps)):
        current_t = time_steps[t_idx]
        curr_df = df.iloc[t_idx]
        
        # Node coordinates
        node_x = [v[0] for v in nodes.values()]
        node_y = [v[1] for v in nodes.values()]
        node_text = [v[2] for v in nodes.values()]
        
        # Color intensity based on rates
        # Normalize arbitrarily for visualization
        def get_val(key):
            val = curr_df.get(key, 0.0)
            return 0.0 if pd.isna(val) else float(val)

        colors = [
            get_val('rate_adiposeLipolysis') * 50,
            get_val('rate_betaOxidation') * 50,
            get_val('rate_ketogenesis') * 100,
            get_val('rate_oxidativePhosphorylation') * 20,
            get_val('rate_orchestrateGluconeogenesis') * 100 
        ]
        
        # Gluconeogenesis might not have a single 'rate' recorded if it's an orchestrator
        # But simulate.py records "orchestrateGluconeogenesis" rate? 
        # Actually orchestrateGluconeogenesis calculates a rate and writes outputs. 
        # But wait, orchestrateGluconeogenesis in simulate.py doesn't call recordRate itself?
        # Let's check simulate.py... 
        # It calculates `rate = ...` then `outputs = ...`. It does NOT call `ctx.env.recordRate` for the orchestrator itself usually.
        # But `betaOxidation` DOES record rate.
        # `ketogenesis` DOES record rate.
        # `adiposeLipolysis` DOES record rate.
        # `oxidativePhosphorylation` DOES record rate.
        # `orchestrateGluconeogenesis`:
        # rate = ...
        # outputs = ...
        # It does NOT record "rate_orchestrateGluconeogenesis".
        # However, `vis.py` uses `rate_...` keys.
        # I should check if `orchestrateGluconeogenesis` records a rate. 
        # Looking at simulate.py code provided:
        # def orchestrateGluconeogenesis(ctx: Ctx) -> Dict[str, float]:
        #     ...
        #     rate = ...
        #     outputs = ...
        #     ctx.write(outputs)
        #     return outputs
        # It does NOT call recordRate. So 'rate_orchestrateGluconeogenesis' will be NaN/0.
        # I'll use 'glucose' production as proxy or just 0 for now.
        
        history_so_far = df.iloc[:t_idx+1]
        
        frame = go.Frame(
            data=[
                # Left: Topology
                go.Scatter(
                    x=node_x, y=node_y, mode="markers+text",
                    text=node_text, textposition="top center",
                    marker=dict(size=[30+c for c in colors], color=colors,
                                colorscale="Reds", showscale=False, cmin=0, cmax=100,
                                line=dict(width=2, color='DarkSlateGrey'))
                ),
                # Middle: Concentrations
                go.Scatter(x=history_so_far['time'], y=history_so_far['glucose'], name="Glucose", line=dict(color="royalblue")),
                go.Scatter(x=history_so_far['time'], y=history_so_far['fatty_acid'], name="Fatty Acid", line=dict(color="orange")),
                go.Scatter(x=history_so_far['time'], y=history_so_far['ketone_body'], name="Ketone Bodies", line=dict(color="red")),
                go.Scatter(x=history_so_far['time'], y=history_so_far['acetyl_coa'], name="Acetyl-CoA", line=dict(color="green")),
                go.Scatter(x=history_so_far['time'], y=history_so_far['simulated_pH'], name="Est. pH", line=dict(color="purple", dash='dot'), yaxis="y2"),
                
                # Right: Rates
                go.Scatter(x=history_so_far['time'], y=_get_series(history_so_far, 'rate_adiposeLipolysis'), name="Lipolysis Rate", line=dict(color="orange")),
                go.Scatter(x=history_so_far['time'], y=_get_series(history_so_far, 'rate_betaOxidation'), name="Beta-Ox Rate", line=dict(color="green")),
                go.Scatter(x=history_so_far['time'], y=_get_series(history_so_far, 'rate_ketogenesis'), name="Ketogenesis Rate", line=dict(color="red")),
            ],
            name=str(current_t),
            traces=[0, 1, 2, 3, 4, 5, 6, 7, 8]
        )
        frames.append(frame)

    # 4. Add Initial Traces
    for i in range(len(frames[0].data)):
        row = 1
        col = 1
        if i >= 1 and i <= 5: col = 2
        if i >= 6: col = 3
        fig.add_trace(frames[0].data[i], row=row, col=col)

    # 5. Layout
    fig.update_layout(
        template="plotly_dark",
        updatemenus=[{
            "type": "buttons",
            "buttons": [{
                "label": "Play",
                "method": "animate",
                "args": [None, {"frame": {"duration": 50, "redraw": True}, "fromcurrent": True}]
            }, {
                "label": "Pause",
                "method": "animate",
                "args": [[None], {"frame": {"duration": 0, "redraw": True}, "mode": "immediate"}]
            }]
        }],
        sliders=[{
            "steps": [{"args": [[f.name], {"frame": {"duration": 0, "redraw": True}, "mode": "immediate"}],
                       "label": f.name, "method": "animate"} for f in frames],
            "currentvalue": {"prefix": "Time: "}
        }]
    )
    
    # Secondary Y-axis for pH in middle plot
    fig.update_layout(
        yaxis2=dict(
            title="pH",
            overlaying="y",
            side="right",
            range=[6.8, 7.6],
            showgrid=False
        )
    )

    # Axis ranges
    fig.update_xaxes(range=[0.5, 4.5], row=1, col=1, visible=False)
    fig.update_yaxes(range=[0.5, 4.5], row=1, col=1, visible=False)
    
    fig.update_xaxes(title="Time (hours)", range=[0, max(time_steps)], row=1, col=2)
    # Concentration max
    conc_max = pd.concat([
        _get_series(df, 'glucose'), 
        _get_series(df, 'fatty_acid'), 
        _get_series(df, 'ketone_body')
    ], axis=1).values.max()
    fig.update_yaxes(title="Concentration (mmol/L)", range=[0, float(conc_max)*1.2 if np.isfinite(conc_max) else 10], row=1, col=2)
    
    fig.update_xaxes(title="Time (hours)", range=[0, max(time_steps)], row=1, col=3)
    # Rate max
    rate_max = pd.concat([
        _get_series(df, 'rate_adiposeLipolysis'), 
        _get_series(df, 'rate_betaOxidation'), 
        _get_series(df, 'rate_ketogenesis')
    ], axis=1).values.max()
    fig.update_yaxes(title="Rate (mmol/L/h)", range=[0, float(rate_max)*1.2 if np.isfinite(rate_max) else 1.0], row=1, col=3)

    fig.frames = frames
    outdir = os.path.dirname(filename) or "."
    os.makedirs(outdir, exist_ok=True)
    fig.write_html(filename)
    print(f"DKA Dashboard generated: {filename}")

def run_simulation(case_type="normal"):
    env = MetabolicEnvironment()
    system = LiverMetabolismSystem(env)
    
    if case_type == "dka":
        # DKA Simulation Setup
        print("Initializing DKA Case...")
        env.setSignal("insulin", 0.05) # Extremely low insulin
        env.setSignal("glucagon", 0.9) # High glucagon
        env.setMetabolite("glucose", 25.0) # High blood sugar (but cells can't use it)
        env.setMetabolite("fatty_acid", 2.0) # Elevated FA from lipolysis
        
        # In DKA, the body is flooded with FA, and Glucose is high but stuck
        # We need to ensure these conditions persist or evolve naturally
        
    else:
        # Normal Simulation Setup
        print("Initializing Normal Case...")
        env.setSignal("insulin", 0.5)
        env.setSignal("glucagon", 0.5)
        env.setMetabolite("glucose", 5.0)
        env.setMetabolite("fatty_acid", 0.5)
        
    # Run for 24 hours (1440 mins) to see accumulation
    hours = 24
    minutes = hours * 60
    
    for tt in range(minutes):
        hour = tt / 60.0
        
        # Maintain pathological conditions (simulating external body state)
        if case_type == "dka":
            # Continuous lipolysis influx from adipose tissue (external to liver model)
            # The model has 'adiposeLipolysis' function but it might be internal liver fat? 
            # Actually simulate.py's adiposeLipolysis increases fatty_acid.
            # But let's make sure we don't run out of "source".
            # Also maintain high glucose to simulate lack of uptake
            
            # Simple clamp or drift
            curr_glucose = env.getMetabolite("glucose")
            if curr_glucose < 20.0:
                env.setMetabolite("glucose", 20.0)
                
            # If insulin is low, adiposeLipolysis in simulate.py should fire.
            # Let's trust the system step.
            pass
            
        system.step(hour)
        
    return env.history

if __name__ == "__main__":
    # 1. Normal Case
    hist_normal = run_simulation("normal")
    generate_dka_dashboard(hist_normal, "../results-html/dka_normal.html")
    
    # 2. DKA Case
    hist_dka = run_simulation("dka")
    generate_dka_dashboard(hist_dka, "../results-html/dka_abnormal.html")
