import pandas as pd
import matplotlib.pyplot as plt
from simulate import MetabolicEnvironment, LiverMetabolismSystem

def run_simulation_day_normal(dt_min: int = 1) -> pd.DataFrame:
    env = MetabolicEnvironment()
    system = LiverMetabolismSystem(env)
    total_minutes = 24 * 60
    for t in range(0, total_minutes, dt_min):
        hour = t / 60.0
        env.setParameter("is_postprandial", False)
        if 8*60 <= t < 9*60:
            env.setParameter("is_postprandial", True)
            env.setMetabolite("glucose", env.getMetabolite("glucose") + 0.6)
            env.setMetabolite("amino_acid", env.getMetabolite("amino_acid") + 0.2)
            env.setMetabolite("glycerol", env.getMetabolite("glycerol") + 0.05)
        if 12*60 <= t < 13*60:
            env.setParameter("is_postprandial", True)
            env.setMetabolite("glucose", env.getMetabolite("glucose") + 0.8)
            env.setMetabolite("amino_acid", env.getMetabolite("amino_acid") + 0.25)
            env.setMetabolite("glycerol", env.getMetabolite("glycerol") + 0.08)
        if 18*60 <= t < 19*60:
            env.setParameter("is_postprandial", True)
            env.setMetabolite("glucose", env.getMetabolite("glucose") + 0.7)
            env.setMetabolite("amino_acid", env.getMetabolite("amino_acid") + 0.22)
            env.setMetabolite("glycerol", env.getMetabolite("glycerol") + 0.07)
        system.step(hour)
    return pd.DataFrame(env.history)

def visualize(df: pd.DataFrame) -> None:
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    
    plt.figure(figsize=(14, 8))
    targets = [
        "glucose","glycogen","insulin","glucagon","atp","fatty_acid","triglycerides",
        "urea","ketone_body","albumin","clotting_factor","bile_acid","phaseI_intermediates","conjugates","ethanol","nadh","nad_plus","lactate"
    ]
    cmap = plt.get_cmap("tab20")
    colors = [cmap(i % cmap.N) for i in range(len(targets))]
    for i, column in enumerate(targets):
        if column in df.columns:
            val = df[column]
            m = val.max() if val.max() != 0 else 1.0
            plt.plot(df["time"], val / m, label=column, linewidth=2, color=colors[i])
    plt.xlabel("时间（小时）")
    plt.ylabel("归一化浓度/水平")
    plt.legend(loc="upper right", bbox_to_anchor=(1.2, 1))
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig("metabolite_curves.png")
    plt.show()

def save_csv(df: pd.DataFrame, path: str = "simulation_result.csv") -> None:
    df.to_csv(path, index=False)

if __name__ == "__main__":
    df = run_simulation_day_normal()
    df["scenario"] = "normal_three_meals"
    save_csv(df, "../results/simulation_result.csv")
    visualize(df)
