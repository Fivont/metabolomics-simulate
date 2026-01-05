import pandas as pd
import numpy as np

def analyze_trend(series, time, threshold=0.02):
    """
    分析时间序列的趋势。
    返回分段列表，每一段包含起始时间、结束时间、起始值、结束值和趋势类型。
    """
    if len(series) < 2:
        return []

    # 1. 平滑处理以减少噪声
    smoothed = series.rolling(window=5, center=True, min_periods=1).mean()
    
    # 2. 寻找局部极值点 (拐点)
    # diff(sign(diff(x))) 在峰值为 -2, 谷值为 +2
    diffs = np.diff(smoothed)
    signs = np.sign(diffs)
    sign_diffs = np.diff(signs)
    
    # 找出符号变化的点 (索引需要+1因为做了两次diff)
    extrema_indices = np.where(sign_diffs != 0)[0] + 1
    
    # 总是包含起点和终点
    indices = [0] + list(extrema_indices) + [len(series)-1]
    indices = sorted(list(set(indices)))
    
    # 3. 过滤微小的波动
    # 如果某段的变化幅度小于总体范围的 threshold，则尝试合并
    data_range = series.max() - series.min()
    if data_range == 0:
         return [{
            "start_time": time.iloc[0],
            "end_time": time.iloc[-1],
            "start_val": series.iloc[0],
            "end_val": series.iloc[-1],
            "trend": "平稳"
        }]

    filtered_indices = [indices[0]]
    for i in range(1, len(indices)):
        prev_idx = filtered_indices[-1]
        curr_idx = indices[i]
        
        # 检查这一段的幅度
        val_diff = abs(smoothed.iloc[curr_idx] - smoothed.iloc[prev_idx])
        
        # 如果是最后一点，或者变化幅度足够大
        if i == len(indices) - 1 or val_diff > data_range * threshold:
            filtered_indices.append(curr_idx)
    
    # 4. 生成分段描述
    segments = []
    for i in range(len(filtered_indices) - 1):
        start_idx = filtered_indices[i]
        end_idx = filtered_indices[i+1]
        
        start_val = series.iloc[start_idx]
        end_val = series.iloc[end_idx]
        
        diff = end_val - start_val
        
        # 定义趋势
        if diff > data_range * 0.01:
            trend = "上升"
        elif diff < -data_range * 0.01:
            trend = "下降"
        else:
            trend = "平稳"
            
        segments.append({
            "start_time": time.iloc[start_idx],
            "end_time": time.iloc[end_idx],
            "start_val": start_val,
            "end_val": end_val,
            "trend": trend
        })
        
    return segments

def summarize_metabolism(csv_path, output_path='metabolite_summary_train_cases.md'):
    df = pd.read_csv(csv_path)
    summary = []
    
    # 确定时间轴
    if 'time' in df.columns:
        time_col = df['time']
    else:
        time_col = pd.Series(range(len(df)))
        
    for col in df.columns:
        if col in ['scenario', 'time']: continue
        
        # 基础统计
        start_val = df[col].iloc[0]
        end_val = df[col].iloc[-1]
        max_val = df[col].max()
        min_val = df[col].min()
        
        # 趋势分析
        segments = analyze_trend(df[col], time_col)
        
        # 构建描述
        col_summary = f"### {col}\n"
        col_summary += f"- 概览: 起始 {start_val:.2f}, 结束 {end_val:.2f}, 范围 [{min_val:.2f}, {max_val:.2f}]\n"
        
        if segments:
            col_summary += f"- 详细趋势:\n"
            for i, seg in enumerate(segments):
                change = seg['end_val'] - seg['start_val']
                col_summary += f"  {i+1}. 时间 {seg['start_time']:.2f} -> {seg['end_time']:.2f}: {seg['trend']} (从 {seg['start_val']:.2f} 到 {seg['end_val']:.2f})\n"
            
            # 关键转折点
            if len(segments) > 1:
                col_summary += f"- 关键转折点:\n"
                for i in range(len(segments) - 1):
                    t_point = segments[i]['end_time']
                    prev_trend = segments[i]['trend']
                    next_trend = segments[i+1]['trend']
                    if prev_trend != next_trend:
                        col_summary += f"  - 时间 {t_point:.2f}: 趋势由 {prev_trend} 转变为 {next_trend}\n"
        
        summary.append(col_summary)

    # 保存到Markdown文件
    summary = "\n".join(summary)
    print(summary)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(summary)
    
    return summary


if __name__ == "__main__":
    csv_path = "../results/simulation_result_train_cases.csv"
    txt_path = "../results/metabolite_summary_train_cases.md"
    try:
        summarize_metabolism(csv_path, txt_path)
    except Exception as e:
        print(f"Error: {e}")
