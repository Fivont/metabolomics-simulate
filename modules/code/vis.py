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


def generate_interactive_dashboard(history_list, filename="metabolic_dynamics.html"):
    df = pd.DataFrame(history_list)
    time_steps = df['time'].values
    
    # 1. 定义模块在画布上的坐标 (自定义拓扑结构)
    # 模拟：酒精代谢 -> 乙醛 -> 乙酸/乙酰辅酶A -> 能量代谢 -> 脂代谢
    nodes = {
        "Ethanol_Mod": [1, 3, "酒精分解(ADH)"],
        "Acetaldehyde_Mod": [1.6, 3, "乙醛清除(ALDH)"],
        "Acetate_Mod": [2.2, 3, "乙酸→乙酰辅酶A"],
        # "Glycolysis_Mod": [2.8, 4, "糖酵解"],
        # "TCA_Mod": [3.4, 3, "能量中心(TCA)"],
        # "Lipid_Mod": [4.0, 2, "脂代谢"],
        # "Urea_Mod": [2.8, 2, "尿素循环"]
    }
    
    df['act_ethanol'] = pd.concat([_get_series(df, 'rate_ethanol_ADH'), _get_series(df, 'rate_acetaldehyde_ALDH')], axis=1).max(axis=1)
    df['act_energy'] = pd.concat([_get_series(df, 'rate_oxidativePhosphorylation'), _get_series(df, 'rate_cytosolicATPase_load')], axis=1).max(axis=1)
    df['act_lipid'] = pd.concat([_get_series(df, 'rate_betaOxidation'), _get_series(df, 'rate_fattyAcidSynthesis')], axis=1).max(axis=1)

    # 2. 初始化画布 (1行3列：模块/浓度/速率)
    fig = make_subplots(
        rows=1, cols=3,
        column_widths=[0.32, 0.43, 0.25],
        specs=[[{"type": "scatter"}, {"type": "scatter"}, {"type": "scatter"}]],
        subplot_titles=("反应模块激活状态 (颜色深浅=速率)", "代谢物浓度实时曲线", "乙醇代谢反应速率")
    )

    # 3. 创建动画帧
    frames = []
    for t_idx in range(len(time_steps)):
        current_t = time_steps[t_idx]
        curr_df = df.iloc[t_idx]
        
        # --- 左图：模块散点 (拓扑模拟) ---
        node_x = [v[0] for v in nodes.values()]
        node_y = [v[1] for v in nodes.values()]
        node_text = [v[2] for v in nodes.values()]
        
        # 计算颜色强度 (根据当前帧速率)
        # 归一化处理，假设速率 5.0 为极值
        colors = [
            float(curr_df.get('act_ethanol', 0.0)) * 50,
            float(curr_df.get('rate_acetaldehyde_ALDH', 0.0)) * 60,
            float(curr_df.get('rate_acetate_to_acetylcoa', 0.0)) * 80,
            float(curr_df.get('rate_hexokinase_or_glucokinase', 0.0)) * 40,
            float(curr_df.get('act_energy', 0.0)) * 20,
            float(curr_df.get('act_lipid', 0.0)) * 30,
            float(curr_df.get('rate_cps1_Ammonia_to_CarbamoylPhosphate', 0.0)) * 100
        ]
        
        # --- 右图：曲线同步 (显示到当前时间点的所有数据) ---
        history_so_far = df.iloc[:t_idx+1]
        
        frame = go.Frame(
            data=[
                # 帧中的散点图 (左)
                go.Scatter(
                    x=node_x, y=node_y, mode="markers+text",
                    text=node_text, textposition="top center",
                    marker=dict(size=[30+c for c in colors], color=colors,
                                colorscale="Reds", showscale=False, cmin=0, cmax=220,
                                line=dict(width=2, color='DarkSlateGrey'))
                ),
                # 帧中的折线图 (右 - 血糖)
                # go.Scatter(x=history_so_far['time'], y=history_so_far['glucose'], name="Glucose", line=dict(color="royalblue")),
                # 帧中的折线图 (右 - 酒精)
                go.Scatter(x=history_so_far['time'], y=history_so_far['ethanol'], name="Ethanol", line=dict(color="orange")),
                # 帧中的折线图 (右 - 乙醛)
                go.Scatter(x=history_so_far['time'], y=history_so_far['acetaldehyde'], name="Acetaldehyde", line=dict(color="red")),
                # 帧中的折线图 (右 - 乙酸/乙酰辅酶A/NADH/NAD+)
                go.Scatter(x=history_so_far['time'], y=_get_series(history_so_far, 'acetate'), name="Acetate", line=dict(color="brown")),
                go.Scatter(x=history_so_far['time'], y=_get_series(history_so_far, 'acetyl_coa'), name="Acetyl-CoA", line=dict(color="green")),
                go.Scatter(x=history_so_far['time'], y=_get_series(history_so_far, 'nadh'), name="NADH", line=dict(color="purple")),
                go.Scatter(x=history_so_far['time'], y=_get_series(history_so_far, 'nad_plus'), name="NAD+", line=dict(color="pink")),
                # 速率曲线 (第三列)
                go.Scatter(x=history_so_far['time'], y=_get_series(history_so_far, 'rate_ethanol_ADH'), name="rate_ADH", line=dict(color="orange")),
                go.Scatter(x=history_so_far['time'], y=_get_series(history_so_far, 'rate_acetaldehyde_ALDH'), name="rate_ALDH", line=dict(color="red")),
                go.Scatter(x=history_so_far['time'], y=_get_series(history_so_far, 'rate_acetate_to_acetylcoa'), name="rate_Acetate→Acetyl-CoA", line=dict(color="brown")),
            ],
            name=str(current_t),
            traces=list(range(0, 11))  # 对应初始 data 的索引
        )
        frames.append(frame)

    # 4. 添加初始状态 (第0帧)
    fig.add_trace(frames[0].data[0], row=1, col=1)
    for i in range(1, 7):
        fig.add_trace(frames[0].data[i], row=1, col=2)
    for i in range(7, 10):
        fig.add_trace(frames[0].data[i], row=1, col=3)

    # 5. 配置播放器 (Slider & Buttons)
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

    # 设置坐标轴范围固定，防止动画闪烁
    fig.update_xaxes(range=[0.5, 4.5], row=1, col=1, showgrid=False, zeroline=False, visible=False)
    fig.update_yaxes(range=[1.5, 4.5], row=1, col=1, showgrid=False, zeroline=False, visible=False)
    fig.update_xaxes(title="Time", range=[0, max(time_steps)], row=1, col=2)
    conc_max = pd.concat([_get_series(df, 'ethanol'), _get_series(df, 'acetaldehyde'), _get_series(df, 'acetate'), _get_series(df, 'acetyl_coa'), _get_series(df, 'nadh'), _get_series(df, 'nad_plus')], axis=1).values.max()
    fig.update_yaxes(title="Concentration", range=[0, float(conc_max) * 1.1 if np.isfinite(conc_max) else 1.0], row=1, col=2)
    fig.update_xaxes(title="Time", range=[0, max(time_steps)], row=1, col=3)
    rate_max = pd.concat([_get_series(df, 'rate_ethanol_ADH'), _get_series(df, 'rate_acetaldehyde_ALDH'), _get_series(df, 'rate_acetate_to_acetylcoa')], axis=1).values.max()
    fig.update_yaxes(title="Rate", range=[0, float(rate_max) * 1.1 if np.isfinite(rate_max) else 1.0], row=1, col=3)

    fig.frames = frames
    outdir = os.path.dirname(filename) or "."
    os.makedirs(outdir, exist_ok=True)
    fig.write_html(filename)
    print(f"交互式动态报告已生成: {filename}")


if __name__ == "__main__":
    env = MetabolicEnvironment()
    def inject(e: MetabolicEnvironment, t: int):
        if 10 <= t <= 15:
            e.setMetabolite("ethanol", e.getMetabolite("ethanol") + 0.5) # 模拟持续吸收
    system = LiverMetabolismSystem(env)
    minutes = 60 * 8
    for tt in range(minutes):
        hour = tt / 60.0
        inject(env, tt)
        system.step(hour)
    generate_interactive_dashboard(env.history, filename="../results-html/interactive_alcohol.html")
