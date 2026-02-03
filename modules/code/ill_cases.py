import os
from typing import Callable, Dict, List, Tuple, Any
import pandas as pd
import matplotlib.pyplot as plt
from simulate import MetabolicEnvironment, LiverMetabolismSystem


def _run(env: MetabolicEnvironment, minutes: int, inject: Callable[[MetabolicEnvironment, int], None] = None) -> Tuple[pd.DataFrame, List[Dict]]:
    system = LiverMetabolismSystem(env)
    for tt in range(minutes):
        hour = tt / 60.0
        if inject:
            inject(env, tt)
        system.step(hour)
    df = pd.DataFrame(env.history)
    return df, []


def _plot_pair(df_left: pd.DataFrame, df_right: pd.DataFrame, columns: List[str], title_left: str, title_right: str, outfile: str) -> None:
    try:
        plt.rcParams["font.sans-serif"] = ["SimHei", "DejaVu Sans", "Arial"]
    except:
        pass
    plt.rcParams["axes.unicode_minus"] = False
    fig, axes = plt.subplots(1, 2, figsize=(14, 6), sharey=False)
    cmap = plt.get_cmap("tab20")
    available_left = [c for c in columns if c in df_left.columns]
    available_right = [c for c in columns if c in df_right.columns]
    for i, col in enumerate(available_left):
        axes[0].plot(df_left["time"], df_left[col], label=col, linewidth=2, color=cmap(i % cmap.N))
    axes[0].set_title(title_left)
    axes[0].set_xlabel("时间 (小时)")
    axes[0].set_ylabel("浓度/水平")
    if len(available_left) > 0:
        axes[0].legend(loc="best", fontsize=9, ncol=2)
    for i, col in enumerate(available_right):
        axes[1].plot(df_right["time"], df_right[col], label=col, linewidth=2, color=cmap(i % cmap.N))
    axes[1].set_title(title_right)
    axes[1].set_xlabel("时间 (小时)")
    axes[1].set_ylabel("浓度/水平")
    if len(available_right) > 0:
        axes[1].legend(loc="best", fontsize=9, ncol=2)
    outdir = os.path.dirname(outfile) or "."
    os.makedirs(outdir, exist_ok=True)
    plt.tight_layout()
    plt.savefig(outfile, bbox_inches="tight")
    plt.close()


def _plot_pair_rates(df_left: pd.DataFrame, df_right: pd.DataFrame, rate_columns: List[str], title_left: str, title_right: str, outfile: str) -> None:
    try:
        plt.rcParams["font.sans-serif"] = ["SimHei", "DejaVu Sans", "Arial"]
    except:
        pass
    plt.rcParams["axes.unicode_minus"] = False
    cols = [c for c in rate_columns if c in df_left.columns or c in df_right.columns]
    if len(cols) == 0:
        outdir = os.path.dirname(outfile) or "."
        os.makedirs(outdir, exist_ok=True)
        fig, _ = plt.subplots(1, 1, figsize=(8, 4))
        fig.suptitle("无可用速率数据")
        plt.savefig(outfile, bbox_inches="tight")
        plt.close()
        return
    fig, axes = plt.subplots(len(cols), 2, figsize=(14, 3.5 * len(cols)), sharey=False)
    if len(cols) == 1:
        axes = [axes]
    for i, col in enumerate(cols):
        ax_left, ax_right = axes[i]
        if col in df_left.columns:
            ax_left.plot(df_left["time"], df_left[col], linewidth=2)
        ax_left.set_title(f"{title_left} - {col}")
        ax_left.set_xlabel("时间 (小时)")
        ax_left.set_ylabel("反应速率")
        if col in df_right.columns:
            ax_right.plot(df_right["time"], df_right[col], linewidth=2)
        ax_right.set_title(f"{title_right} - {col}")
        ax_right.set_xlabel("时间 (小时)")
        ax_right.set_ylabel("反应速率")
    outdir = os.path.dirname(outfile) or "."
    os.makedirs(outdir, exist_ok=True)
    plt.tight_layout()
    plt.savefig(outfile, bbox_inches="tight")
    plt.close()


def case_nafld_abnormal() -> Tuple[pd.DataFrame, List[Dict]]:
    env = MetabolicEnvironment()

    def inject(e: MetabolicEnvironment, t: int):
        e.setParameter("is_postprandial", True)
        g = e.getMetabolite("glucose")
        e.setMetabolite("glucose", max(g, 180.0))

    return _run(env, minutes=360, inject=inject)


def case_nafld_normal() -> Tuple[pd.DataFrame, List[Dict]]:
    env = MetabolicEnvironment()

    def inject(e: MetabolicEnvironment, t: int):
        if 20 <= t < 60 or 180 <= t < 220:
            e.setParameter("is_postprandial", True)
            e.setMetabolite("glucose", e.getMetabolite("glucose") + 5.0)
        else:
            e.setParameter("is_postprandial", False)

    return _run(env, minutes=360, inject=inject)


def case_dka_abnormal() -> Tuple[pd.DataFrame, List[Dict]]:
    env = MetabolicEnvironment()
    env.setParameter("insulin_degrading_enzyme_activity", 50.0)
    env.setParameter("insulin_sensitivity", 1.0)

    def inject(e: MetabolicEnvironment, t: int):
        e.setParameter("is_postprandial", False)
        e.setMetabolite("glucose", max(e.getMetabolite("glucose"), 180.0))

    return _run(env, minutes=360, inject=inject)


def case_dka_normal() -> Tuple[pd.DataFrame, List[Dict]]:
    env = MetabolicEnvironment()

    def inject(e: MetabolicEnvironment, t: int):
        if 30 <= t < 120:
            e.setParameter("is_postprandial", True)
            e.setMetabolite("glucose", e.getMetabolite("glucose") + 4.0)
        else:
            e.setParameter("is_postprandial", False)

    return _run(env, minutes=360, inject=inject)


def case_acetaldehyde_abnormal() -> Tuple[pd.DataFrame, List[Dict]]:
    env = MetabolicEnvironment()
    env.setParameter("liver_function", 0.2)

    def inject(e: MetabolicEnvironment, t: int):
        if t == 10:
            e.setMetabolite("ethanol", e.getMetabolite("ethanol") + 8.0)
        if t >= 30:
            e.setMetabolite("nad_plus", max(e.getMetabolite("nad_plus") - 0.5, 1.0))

    return _run(env, minutes=240, inject=inject)


def case_acetaldehyde_normal() -> Tuple[pd.DataFrame, List[Dict]]:
    env = MetabolicEnvironment()
    env.setParameter("liver_function", 1.0)

    def inject(e: MetabolicEnvironment, t: int):
        if t == 10:
            e.setMetabolite("ethanol", e.getMetabolite("ethanol") + 5.0)

    return _run(env, minutes=240, inject=inject)


def case_hepatic_encephalopathy_abnormal() -> Tuple[pd.DataFrame, List[Dict]]:
    env = MetabolicEnvironment()
    env.setParameter("liver_function", 0.2)

    def inject(e: MetabolicEnvironment, t: int):
        e.setMetabolite("atp", min(e.getMetabolite("atp"), 10.0))
        if t % 30 == 0 and t <= 180:
            e.setMetabolite("amino_acid", e.getMetabolite("amino_acid") + 3.0)

    return _run(env, minutes=240, inject=inject)


def case_hepatic_encephalopathy_normal() -> Tuple[pd.DataFrame, List[Dict]]:
    env = MetabolicEnvironment()
    env.setParameter("liver_function", 1.0)

    def inject(e: MetabolicEnvironment, t: int):
        if t % 60 == 0 and t <= 180:
            e.setMetabolite("amino_acid", e.getMetabolite("amino_acid") + 1.0)

    return _run(env, minutes=240, inject=inject)


def _write_events(path: str, events: List[Dict]) -> None:
    outdir = os.path.dirname(path) or "."
    os.makedirs(outdir, exist_ok=True)
    df = pd.DataFrame(events, columns=["time", "name", "status"])
    df.to_csv(path, index=False)


def run_and_plot_all() -> Dict[str, str]:
    os.makedirs("../results-ill", exist_ok=True)
    df_nafld_abn, ev_nafld_abn = case_nafld_abnormal()
    df_nafld_ctl, ev_nafld_ctl = case_nafld_normal()
    _plot_pair(
        df_nafld_abn,
        df_nafld_ctl,
        ["glucose", "fatty_acid", "triglycerides", "insulin"],
        "NAFLD 异常输入",
        "NAFLD 正常对照",
        "../results-ill/nafld_pair.png",
    )
    _write_events("../results-ill/nafld_events_abnormal.csv", ev_nafld_abn)
    _write_events("../results-ill/nafld_events_normal.csv", ev_nafld_ctl)
    rate_cols = [
        "rate_hexokinase_or_glucokinase",
        "rate_glycolysis_middle_steps",
        "rate_betaOxidation",
        "rate_fattyAcidSynthesis",
        "rate_ketogenesis",
        "rate_oxidativePhosphorylation",
        "rate_glycogenSynthaseStep",
        "rate_glycogenPhosphorylaseStep",
        "rate_deNovoLipogenesis",
    ]
    _plot_pair_rates(
        df_nafld_abn,
        df_nafld_ctl,
        rate_cols,
        "NAFLD 异常输入 主要反应速率",
        "NAFLD 正常对照 主要反应速率",
        "../results-ill/nafld_rates_pair.png",
    )
    df_dka_abn, ev_dka_abn = case_dka_abnormal()
    df_dka_ctl, ev_dka_ctl = case_dka_normal()
    _plot_pair(
        df_dka_abn,
        df_dka_ctl,
        ["glucose", "ketone_body", "insulin", "fatty_acid"],
        "DKA 异常输入",
        "DKA 正常对照",
        "../results-ill/dka_pair.png",
    )
    _write_events("../results-ill/dka_events_abnormal.csv", ev_dka_abn)
    _write_events("../results-ill/dka_events_normal.csv", ev_dka_ctl)
    _plot_pair_rates(
        df_dka_abn,
        df_dka_ctl,
        rate_cols,
        "DKA 异常输入 主要反应速率",
        "DKA 正常对照 主要反应速率",
        "../results-ill/dka_rates_pair.png",
    )
    df_acet_abn, ev_acet_abn = case_acetaldehyde_abnormal()
    df_acet_ctl, ev_acet_ctl = case_acetaldehyde_normal()
    _plot_pair(
        df_acet_abn,
        df_acet_ctl,
        ["ethanol", "acetaldehyde", "acetate", "nadh", "nad_plus"],
        "乙醛蓄积 异常输入",
        "乙醛蓄积 正常对照",
        "../results-ill/acetaldehyde_pair.png",
    )
    _write_events("../results-ill/acetaldehyde_events_abnormal.csv", ev_acet_abn)
    _write_events("../results-ill/acetaldehyde_events_normal.csv", ev_acet_ctl)
    _plot_pair_rates(
        df_acet_abn,
        df_acet_ctl,
        rate_cols,
        "乙醛蓄积 异常输入 主要反应速率",
        "乙醛蓄积 正常对照 主要反应速率",
        "../results-ill/acetaldehyde_rates_pair.png",
    )
    df_he_abn, ev_he_abn = case_hepatic_encephalopathy_abnormal()
    df_he_ctl, ev_he_ctl = case_hepatic_encephalopathy_normal()
    _plot_pair(
        df_he_abn,
        df_he_ctl,
        ["ammonia", "urea", "amino_acid"],
        "肝性脑病 异常输入",
        "肝性脑病 正常对照",
        "../results-ill/hepatic_encephalopathy_pair.png",
    )
    _write_events("../results-ill/hepatic_encephalopathy_events_abnormal.csv", ev_he_abn)
    _write_events("../results-ill/hepatic_encephalopathy_events_normal.csv", ev_he_ctl)
    _plot_pair_rates(
        df_he_abn,
        df_he_ctl,
        rate_cols,
        "肝性脑病 异常输入 主要反应速率",
        "肝性脑病 正常对照 主要反应速率",
        "../results-ill/hepatic_encephalopathy_rates_pair.png",
    )
    return {
        "NAFLD": "../results-ill/nafld_pair.png",
        "NAFLD_EVENTS_ABNORMAL": "../results-ill/nafld_events_abnormal.csv",
        "NAFLD_EVENTS_NORMAL": "../results-ill/nafld_events_normal.csv",
        "NAFLD_RATES": "../results-ill/nafld_rates_pair.png",
        "DKA": "../results-ill/dka_pair.png",
        "DKA_EVENTS_ABNORMAL": "../results-ill/dka_events_abnormal.csv",
        "DKA_EVENTS_NORMAL": "../results-ill/dka_events_normal.csv",
        "DKA_RATES": "../results-ill/dka_rates_pair.png",
        "Acetaldehyde": "../results-ill/acetaldehyde_pair.png",
        "Acetaldehyde_EVENTS_ABNORMAL": "../results-ill/acetaldehyde_events_abnormal.csv",
        "Acetaldehyde_EVENTS_NORMAL": "../results-ill/acetaldehyde_events_normal.csv",
        "Acetaldehyde_RATES": "../results-ill/acetaldehyde_rates_pair.png",
        "HepaticEncephalopathy": "../results-ill/hepatic_encephalopathy_pair.png",
        "HepaticEncephalopathy_EVENTS_ABNORMAL": "../results-ill/hepatic_encephalopathy_events_abnormal.csv",
        "HepaticEncephalopathy_EVENTS_NORMAL": "../results-ill/hepatic_encephalopathy_events_normal.csv",
        "HepaticEncephalopathy_RATES": "../results-ill/hepatic_encephalopathy_rates_pair.png",
    }


if __name__ == "__main__":
    paths = run_and_plot_all()
    print(paths)
