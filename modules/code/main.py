import sys
import os
import pandas as pd
import matplotlib.pyplot as plt
from simulate import MetabolicEnvironment, LiverMetabolismSystem

def simulate_24h() -> pd.DataFrame:
    env = MetabolicEnvironment()
    system = LiverMetabolismSystem(env)
    
    UNITS_PER_HOUR = 30
    DAY_UNITS = 24 * UNITS_PER_HOUR
    start_t = 7 * UNITS_PER_HOUR
    total_units = DAY_UNITS + 1
    
    for t in range(start_t, start_t + total_units):
        hour = (t - start_t) / UNITS_PER_HOUR
        
        if t == 8 * UNITS_PER_HOUR:
            env.setMetabolite("glucose", env.getMetabolite("glucose") + 30.0)
            env.setMetabolite("amino_acid", env.getMetabolite("amino_acid") + 5.0)
            env.setMetabolite("triglycerides", env.getMetabolite("triglycerides") + 5.0)
        
        elif t == 12 * UNITS_PER_HOUR:
            env.setMetabolite("glucose", env.getMetabolite("glucose") + 40.0)
            env.setMetabolite("amino_acid", env.getMetabolite("amino_acid") + 7.0)
            env.setMetabolite("triglycerides", env.getMetabolite("triglycerides") + 8.0)
            
        elif t == 18 * UNITS_PER_HOUR:
            env.setMetabolite("glucose", env.getMetabolite("glucose") + 35.0)
            env.setMetabolite("amino_acid", env.getMetabolite("amino_acid") + 6.0)
            env.setMetabolite("triglycerides", env.getMetabolite("triglycerides") + 7.0)

        is_postprandial = False
        if (8 * UNITS_PER_HOUR) <= t < (10 * UNITS_PER_HOUR):
            is_postprandial = True
        elif (12 * UNITS_PER_HOUR) <= t < (15 * UNITS_PER_HOUR):
            is_postprandial = True
        elif (18 * UNITS_PER_HOUR) <= t < (22 * UNITS_PER_HOUR):
            is_postprandial = True
            
        env.setParameter("is_postprandial", is_postprandial)
        
        system.step(hour)
        
    df = pd.DataFrame(env.history)
    df["time"] = df["time"] + 7.0
    df["time_abs"] = df["time"]
    return df

def run_simulation_train_cases() -> pd.DataFrame:
    return simulate_24h()

def visualize(df: pd.DataFrame, output_path: str = "metabolite_curves_train_cases.png") -> None:
    # Try to set a font that supports Chinese characters, fallback to default if not found
    try:
        plt.rcParams['font.sans-serif'] = ['SimHei', 'DejaVu Sans', 'Arial']
    except:
        pass
    plt.rcParams['axes.unicode_minus'] = False
    
    plt.figure(figsize=(14, 8))
    targets = [
        "glucose","glycogen","insulin","glucagon","atp","fatty_acid","triglycerides",
        "urea","ketone_body","albumin","clotting_factor","bile_acid","phaseI_intermediates","conjugates","ethanol","nadh","nad_plus","lactate"
    ]
    
    # Check which targets are actually in df
    available_targets = [t for t in targets if t in df.columns]
    
    cmap = plt.get_cmap("tab20")
    colors = [cmap(i % cmap.N) for i in range(len(available_targets))]
    
    for i, column in enumerate(available_targets):
        val = df[column]
        m = val.max() if val.max() != 0 else 1.0
        # Normalize for visualization
        plt.plot(df["time"], val / m, label=column, linewidth=2, color=colors[i])
        
    plt.xlabel("时间 (Clock Time: 7:00 start)")
    plt.ylabel("归一化浓度/水平")
    
    # Mark meal times
    plt.axvline(x=8.0, color='gray', linestyle='--', alpha=0.5, label='Breakfast (8:00)')
    plt.axvline(x=12.0, color='gray', linestyle='--', alpha=0.5, label='Lunch (12:00)')
    plt.axvline(x=18.0, color='gray', linestyle='--', alpha=0.5, label='Dinner (18:00)')
    
    plt.legend(loc="upper right", bbox_to_anchor=(1.2, 1))
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(output_path)
    # plt.show() # Commented out for non-interactive environments

def save_csv(df: pd.DataFrame, path: str = "simulation_result_train_cases.csv") -> None:
    # Ensure directory exists
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    df.to_csv(path, index=False)

if __name__ == "__main__":
    print("Running Train Cases Simulation...")
    df = run_simulation_train_cases()
    df["scenario"] = "train_cases_24h"
    
    # Save to modules/results as in main.py reference or project root?
    # User said "参考main.py中的...保存过程csv"
    # main.py saves to "../results/simulation_result.csv" (relative to modules/code/main.py)
    # Our script is in root (simulate/), so modules/results/ is ./modules/results/
    
    output_path = "../results/simulation_result_train_cases.csv"
    save_csv(df, output_path)
    print(f"Simulation saved to {output_path}")
    
    fig_path = "../results/metabolite_curves_train_cases.png"
    visualize(df, fig_path)
    print(f"Visualization saved to {fig_path}")
