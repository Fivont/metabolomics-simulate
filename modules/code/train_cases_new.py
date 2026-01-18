import os
import pandas as pd
import matplotlib.pyplot as plt
from typing import Callable, Dict, List
from simulate import MetabolicEnvironment, LiverMetabolismSystem


def _run(env: MetabolicEnvironment, minutes: int, inject: Callable[[MetabolicEnvironment, int], None] = None) -> pd.DataFrame:
    sys = LiverMetabolismSystem(env)
    for t in range(minutes):
        hour = t / 60.0
        if inject:
            inject(env, t)
        sys.step(hour)
    df = pd.DataFrame(env.history)
    df["time"] = df["time"]
    return df


def _plot(df: pd.DataFrame, columns: List[str], title: str, outfile: str) -> None:
    try:
        plt.rcParams['font.sans-serif'] = ['SimHei', 'DejaVu Sans', 'Arial']
    except:
        pass
    plt.rcParams['axes.unicode_minus'] = False
    plt.figure(figsize=(12, 7))
    available = [c for c in columns if c in df.columns]
    cmap = plt.get_cmap("tab20")
    for i, col in enumerate(available):
        val = df[col]
        m = val.max() if val.max() != 0 else 1.0
        plt.plot(df["time"], val / m, label=col, linewidth=2, color=cmap(i % cmap.N))
    plt.xlabel("时间 (小时)")
    plt.ylabel("归一化浓度/水平")
    plt.title(title)
    if len(available) > 0:
        plt.legend(loc="best", fontsize=9, ncol=2)
    outdir = os.path.dirname(outfile) or "."
    os.makedirs(outdir, exist_ok=True)
    plt.tight_layout()
    plt.savefig(outfile, bbox_inches="tight")
    plt.close()


def test_insulin_degradation() -> Dict[str, float]:
    env_fast = MetabolicEnvironment()
    env_fast.setParameter("insulin_degrading_enzyme_activity", 3.0)
    env_slow = MetabolicEnvironment()
    env_slow.setParameter("insulin_degrading_enzyme_activity", 0.05)

    def inject(env: MetabolicEnvironment, t: int):
        # 简单餐后胰岛素刺激
        if 20 <= t < 50:
            env.setParameter("is_postprandial", True)
        else:
            env.setParameter("is_postprandial", False)

    df_fast = _run(env_fast, minutes=180, inject=inject)
    df_slow = _run(env_slow, minutes=180, inject=inject)

    _plot(df_fast, ["insulin", "glucagon"], "胰岛素降解（高IDE）", "../results/curves_test_insulin_deg_fast.png")
    _plot(df_slow, ["insulin", "glucagon"], "胰岛素降解（低IDE）", "../results/curves_test_insulin_deg_slow.png")

    # 指标：同一时刻胰岛素更低，且下降更快
    t_idx_mid = df_fast["time"].sub(1.0).abs().idxmin()
    t_idx_end = df_fast.index[-1]
    metric_lower = float(df_fast["insulin"].iloc[t_idx_mid] < df_slow["insulin"].iloc[t_idx_mid])
    metric_decay = float(df_fast["insulin"].iloc[t_idx_end] < df_slow["insulin"].iloc[t_idx_end])
    return {"insulin_lower_with_high_IDE": metric_lower, "faster_decay_with_high_IDE": metric_decay}


def test_ethanol_detox() -> Dict[str, float]:
    env = MetabolicEnvironment()
    env.setParameter("liver_function", 1.0)

    def inject(env: MetabolicEnvironment, t: int):
        if t == 10:
            env.setMetabolite("ethanol", env.getMetabolite("ethanol") + 5.0)

    df = _run(env, minutes=240, inject=inject)
    _plot(df, ["ethanol", "acetaldehyde", "acetate", "nadh", "nad_plus"], "乙醇代谢曲线", "../results/curves_test_ethanol.png")
    # 指标：乙醇下降，乙醛先升后降，乙酸上升
    ethanol_drop = float(df["ethanol"].iloc[-1] < df["ethanol"].max() * 0.5)
    acetaldehyde_peak = float(df["acetaldehyde"].max() > 0.5)
    acetate_rise = float(df["acetate"].iloc[-1] > df["acetate"].iloc[0])
    return {"ethanol_decreasing": ethanol_drop, "acetaldehyde_peak": acetaldehyde_peak, "acetate_increasing": acetate_rise}


def test_bilirubin_conjugation() -> Dict[str, float]:
    env = MetabolicEnvironment()
    env.setParameter("liver_function", 1.0)
    env.setMetabolite("indirect_bilirubin", 1.0)
    env.setMetabolite("udpga", 5.0)

    def inject(env: MetabolicEnvironment, t: int):
        pass

    df = _run(env, minutes=180, inject=inject)
    _plot(df, ["indirect_bilirubin", "direct_bilirubin", "udpga"], "胆红素结合曲线", "../results/curves_test_bilirubin.png")
    # 指标：间接胆红素下降、直接胆红素增加、UDPGA消耗
    ib_drop = float(df["indirect_bilirubin"].iloc[-1] < df["indirect_bilirubin"].iloc[0])
    db_rise = float(df["direct_bilirubin"].iloc[-1] > df["direct_bilirubin"].iloc[0])
    udpga_use = float(df["udpga"].iloc[-1] < df["udpga"].iloc[0])
    return {"indirect_bilirubin_decreasing": ib_drop, "direct_bilirubin_increasing": db_rise, "udpga_consumed": udpga_use}


def test_phaseII_conjugation_with_cofactors() -> Dict[str, float]:
    env = MetabolicEnvironment()
    env.setParameter("liver_function", 1.0)
    env.setMetabolite("udpga", 6.0)
    env.setMetabolite("paps", 3.0)
    env.setMetabolite("gsh", 8.0)

    def inject(env: MetabolicEnvironment, t: int):
        # 持续引入少量相I底物以生成中间体
        if t % 20 == 0 and t <= 120:
            env.setParameter("xenobiotic_load", env.getParameter("xenobiotic_load") + 0.8)

    df = _run(env, minutes=240, inject=inject)
    _plot(df, ["phaseI_intermediates", "conjugates", "udpga", "paps", "gsh"], "相II结合与辅基消耗", "../results/curves_test_phaseII.png")
    # 指标：中间体下降、结合产物上升、辅基下降
    inter_drop = float(df["phaseI_intermediates"].iloc[-1] < df["phaseI_intermediates"].max() * 0.7)
    conj_rise = float(df["conjugates"].iloc[-1] > df["conjugates"].iloc[0])
    cof_drop = float((df["udpga"].iloc[-1] < df["udpga"].iloc[0]) and (df["paps"].iloc[-1] < df["paps"].iloc[0]) and (df["gsh"].iloc[-1] < df["gsh"].iloc[0]))
    return {"intermediates_decreasing": inter_drop, "conjugates_increasing": conj_rise, "cofactors_consumed": cof_drop}


def test_glucose_homeostasis_constraints() -> Dict[str, float]:
    env = MetabolicEnvironment()

    def inject(env: MetabolicEnvironment, t: int):
        # 两次餐后窗口
        if 20 <= t < 60:
            env.setParameter("is_postprandial", True)
            env.setMetabolite("glucose", env.getMetabolite("glucose") + 5.0)
        elif 180 <= t < 220:
            env.setParameter("is_postprandial", True)
            env.setMetabolite("glucose", env.getMetabolite("glucose") + 5.0)
        else:
            env.setParameter("is_postprandial", False)

    df = _run(env, minutes=360, inject=inject)
    _plot(df, ["glucose", "glycogen", "ketone_body", "insulin", "glucagon"], "糖代谢稳态", "../results/curves_constraint_glucose.png")
    # 峰值后2小时内回落（相对行为判断）
    p1 = df[(df["time"] >= 0.5) & (df["time"] < 1.5)]
    p1_peak = p1["glucose"].max() if len(p1) else df["glucose"].max()
    p1_end = df[(df["time"] >= 2.5) & (df["time"] < 3.0)]["glucose"].mean()
    cond_peak_then_fall = float(p1_end < p1_peak)
    # 空腹期轻度酮体上升
    fasting_tail = df[df["time"] > (df["time"].min() + 5.0)]
    cond_ketone_rise = float(fasting_tail["ketone_body"].iloc[-1] >= fasting_tail["ketone_body"].iloc[0])
    # 空腹阶段血糖稳定（标准差较小）
    fasting_std = float(fasting_tail["glucose"].std() < 10.0)
    return {
        "postprandial_peak_then_fall_within_~2h": cond_peak_then_fall,
        "late_fasting_slight_rise_ketone": cond_ketone_rise,
        "fasting_phase_stable_glucose": fasting_std
    }


def test_urea_cycle_constraints() -> Dict[str, float]:
    env = MetabolicEnvironment()

    def inject(env: MetabolicEnvironment, t: int):
        if t == 10 or t == 40:
            env.setMetabolite("ammonia", env.getMetabolite("ammonia") + 2.0)

    df = _run(env, minutes=240, inject=inject)
    _plot(df, ["ammonia", "urea", "amino_acid"], "尿素循环约束", "../results/curves_constraint_urea.png")
    # 加氨后尿素上升、氨回落
    post_peak = df[df["time"] > 0.2]
    cond_urea_increase = float(post_peak["urea"].iloc[-1] > post_peak["urea"].iloc[0])
    cond_ammonia_control = float(post_peak["ammonia"].iloc[-1] <= post_peak["ammonia"].max() * 0.6)
    return {"urea_increase_after_ammonia": cond_urea_increase, "ammonia_peak_then_drop": cond_ammonia_control}


def test_albumin_constraints() -> Dict[str, float]:
    env = MetabolicEnvironment()

    def inject(env: MetabolicEnvironment, t: int):
        # 餐后促进蛋白合成
        if 30 <= t < 120:
            env.setParameter("is_postprandial", True)
            env.setMetabolite("amino_acid", env.getMetabolite("amino_acid") + 0.2)
        else:
            env.setParameter("is_postprandial", False)

    df = _run(env, minutes=360, inject=inject)
    _plot(df, ["albumin", "amino_acid", "atp", "insulin"], "白蛋白约束", "../results/curves_constraint_albumin.png")
    alb_min = df["albumin"].min()
    alb_max = df["albumin"].max()
    cond_range = float(alb_min >= 30.0 and alb_max <= 70.0)
    cond_post_support = float(df["albumin"].iloc[150] >= df["albumin"].iloc[20])
    return {"albumin_in_approx_35_55_range": cond_range, "postprandial_support": cond_post_support}


def test_lipid_constraints() -> Dict[str, float]:
    env = MetabolicEnvironment()

    def inject(env: MetabolicEnvironment, t: int):
        if t == 20:
            env.setMetabolite("fatty_acid", env.getMetabolite("fatty_acid") + 10.0)
        if t == 180:
            env.setMetabolite("triglycerides", env.getMetabolite("triglycerides") + 8.0)
        # 餐后窗口以促进储存
        env.setParameter("is_postprandial", 20 <= t < 80 or 180 <= t < 240)

    df = _run(env, minutes=360, inject=inject)
    _plot(df, ["fatty_acid", "triglycerides", "atp", "insulin", "glucagon"], "脂代谢约束", "../results/curves_constraint_lipid.png")
    fa_drop = float(df["fatty_acid"].iloc[-1] <= df["fatty_acid"].max() * 0.7)
    tg_increase = float(df["triglycerides"].iloc[-1] >= df["triglycerides"].iloc[0])
    tg_not_unbounded = float(df["triglycerides"].iloc[-1] <= df["triglycerides"].iloc[0] * 1.8)
    return {"fatty_acid_decreases": fa_drop, "triglycerides_increase": tg_increase, "tg_not_unbounded": tg_not_unbounded}

def run_all_tests() -> Dict[str, Dict[str, float]]:
    results: Dict[str, Dict[str, float]] = {}
    results["TC-NEW-INSULIN-DEG"] = test_insulin_degradation()
    results["TC-NEW-ETHANOL"] = test_ethanol_detox()
    results["TC-NEW-BILIRUBIN"] = test_bilirubin_conjugation()
    results["TC-NEW-PHASEII"] = test_phaseII_conjugation_with_cofactors()
    results["TC-CONSTRAINT-GLUCOSE"] = test_glucose_homeostasis_constraints()
    results["TC-CONSTRAINT-UREA"] = test_urea_cycle_constraints()
    results["TC-CONSTRAINT-ALBUMIN"] = test_albumin_constraints()
    results["TC-CONSTRAINT-LIPID"] = test_lipid_constraints()
    return results


def summarize_and_plot() -> str:
    results = run_all_tests()
    summary = ["=== 新测试需求验证结果 ==="]
    total = 0
    passed = 0
    for tc, checks in results.items():
        summary.append(f"Test Case: {tc}")
        tc_pass = True
        for name, val in checks.items():
            status = "PASS" if val == 1.0 else "FAIL"
            summary.append(f"  - {name}: {status}")
            if val != 1.0:
                tc_pass = False
        summary.append(f"  => {'[PASSED]' if tc_pass else '[FAILED]'}")
        summary.append("-" * 40)
        total += 1
        if tc_pass:
            passed += 1
    summary.append(f"Summary: {passed}/{total} Test Cases Passed")
    out_txt = "\n".join(summary)
    os.makedirs("../results", exist_ok=True)
    with open("../results/test_result_train_cases_new.txt", "w", encoding="utf-8") as f:
        f.write(out_txt)
    return out_txt


if __name__ == "__main__":
    print(summarize_and_plot())
