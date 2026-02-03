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

def generate_nafld_dashboard(history_list, filename="nafld_simulation.html"):
    df = pd.DataFrame(history_list)
    time_steps = df['time'].values
    
    # 1. Define nodes for NAFLD topology
    # Glucose -> [DNL] -> Fatty Acid -> [Transport] -> Triglycerides
    #                               |
    #                               v
    #                            [BetaOx]
    nodes = {
        "Glucose_Mod": [1, 3, "葡萄糖(Glucose)"],
        "DNL_Mod": [2, 3, "新生脂生成(DNL)"],
        "FattyAcid_Mod": [3, 3, "脂肪酸(Fatty Acid)"],
        "Transport_Mod": [4, 3, "脂转运(Transport)"],
        "Triglyceride_Mod": [5, 3, "甘油三酯(TG)"],
        "BetaOx_Mod": [3, 2, "β-氧化(Beta-Ox)"]
    }
    
    # 2. Initialize Canvas
    fig = make_subplots(
        rows=1, cols=3,
        column_widths=[0.32, 0.43, 0.25],
        specs=[[{"type": "scatter"}, {"type": "scatter"}, {"type": "scatter"}]],
        subplot_titles=("代谢通量拓扑 (颜色深浅=速率)", "脂质积累曲线", "关键合成速率")
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
        
        # Helper to avoid NaN errors
        def get_val(key):
            val = curr_df.get(key, 0.0)
            return 0.0 if pd.isna(val) else float(val)
            
        # Color intensity
        colors = [
            get_val('glucose') * 2, # Glucose node intensity by concentration
            get_val('rate_deNovoLipogenesis') * 200,
            get_val('fatty_acid') * 20, # FA node intensity by concentration
            get_val('rate_lipidTransport') * 100,
            get_val('triglycerides') * 10, # TG node intensity by concentration
            get_val('rate_betaOxidation') * 50
        ]
        
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
                # Middle: Concentrations (Accumulation)
                go.Scatter(x=history_so_far['time'], y=history_so_far['glucose'], name="Glucose", line=dict(color="royalblue")),
                go.Scatter(x=history_so_far['time'], y=history_so_far['fatty_acid'], name="Fatty Acid", line=dict(color="orange")),
                go.Scatter(x=history_so_far['time'], y=history_so_far['triglycerides'], name="Triglycerides", line=dict(color="brown")),
                go.Scatter(x=history_so_far['time'], y=history_so_far['glycogen'], name="Glycogen", line=dict(color="green", dash='dot'), yaxis="y2"),
                
                # Right: Rates
                go.Scatter(x=history_so_far['time'], y=_get_series(history_so_far, 'rate_deNovoLipogenesis'), name="DNL Rate", line=dict(color="red")),
                go.Scatter(x=history_so_far['time'], y=_get_series(history_so_far, 'rate_fattyAcidSynthesis'), name="FA Synth Rate", line=dict(color="purple")),
                go.Scatter(x=history_so_far['time'], y=_get_series(history_so_far, 'rate_lipidTransport'), name="Transport Rate", line=dict(color="blue")),
                go.Scatter(x=history_so_far['time'], y=_get_series(history_so_far, 'rate_betaOxidation'), name="Beta-Ox Rate", line=dict(color="green")),
            ],
            name=str(current_t),
            traces=[0, 1, 2, 3, 4, 5, 6, 7, 8]
        )
        frames.append(frame)

    # 4. Add Initial Traces
    for i in range(len(frames[0].data)):
        row = 1
        col = 1
        if i >= 1 and i <= 4: col = 2
        if i >= 5: col = 3
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
    
    # Secondary Y-axis for Glycogen
    fig.update_layout(
        yaxis2=dict(
            title="Glycogen",
            overlaying="y",
            side="right",
            range=[0, 500],
            showgrid=False
        )
    )

    # Axis ranges
    fig.update_xaxes(range=[0.5, 5.5], row=1, col=1, visible=False)
    fig.update_yaxes(range=[1.5, 4.5], row=1, col=1, visible=False)
    
    fig.update_xaxes(title="Time (hours)", range=[0, max(time_steps)], row=1, col=2)
    # Concentration max
    conc_max = pd.concat([
        _get_series(df, 'glucose'), 
        _get_series(df, 'fatty_acid'), 
        _get_series(df, 'triglycerides')
    ], axis=1).values.max()
    fig.update_yaxes(title="Concentration (mmol/L)", range=[0, float(conc_max)*1.2 if np.isfinite(conc_max) else 10], row=1, col=2)
    
    fig.update_xaxes(title="Time (hours)", range=[0, max(time_steps)], row=1, col=3)
    # Rate max
    rate_max = pd.concat([
        _get_series(df, 'rate_deNovoLipogenesis'), 
        _get_series(df, 'rate_fattyAcidSynthesis'),
        _get_series(df, 'rate_lipidTransport')
    ], axis=1).values.max()
    fig.update_yaxes(title="Rate", range=[0, float(rate_max)*1.2 if np.isfinite(rate_max) else 1.0], row=1, col=3)

    fig.frames = frames
    outdir = os.path.dirname(filename) or "."
    os.makedirs(outdir, exist_ok=True)
    fig.write_html(filename)
    print(f"NAFLD Dashboard generated: {filename}")

def run_simulation(case_type="normal"):
    env = MetabolicEnvironment()
    system = LiverMetabolismSystem(env)
    
    if case_type == "nafld":
        # NAFLD Setup: High Sugar Diet + Insulin Resistance (or High Insulin)
        print("Initializing NAFLD Case...")
        env.setSignal("insulin", 0.8) # High insulin (hyperinsulinemia)
        env.setSignal("glucagon", 0.2)
        env.setParameter("insulin_sensitivity", 0.5) # Reduced sensitivity
        # Initial high glucose
        env.setMetabolite("glucose", 110.0) 
        
    else:
        # Normal Setup
        print("Initializing Normal Case...")
        env.setSignal("insulin", 0.5)
        env.setSignal("glucagon", 0.5)
        env.setMetabolite("glucose", 5.0)
        
    # Run for 48 hours to see accumulation
    hours = 48
    minutes = hours * 60
    
    for tt in range(minutes):
        hour = tt / 60.0
        
        # Feeding Logic
        if case_type == "nafld":
            # Continuous high sugar or frequent meals
            curr_g = env.getMetabolite("glucose")
            # Maintain high glucose > 100 to trigger DNL
            if curr_g < 110.0:
                 env.setMetabolite("glucose", 120.0)
        else:
            # Normal meals (every 6 hours)
            if tt % 360 == 0 and tt > 0:
                env.setMetabolite("glucose", env.getMetabolite("glucose") + 5.0)
            
        system.step(hour)
        
    return env.history

if __name__ == "__main__":
    # 1. Normal Case
    hist_normal = run_simulation("normal")
    generate_nafld_dashboard(hist_normal, "../results-html/nafld_normal.html")
    
    # 2. NAFLD Case
    hist_nafld = run_simulation("nafld")
    generate_nafld_dashboard(hist_nafld, "../results-html/nafld_abnormal.html")
