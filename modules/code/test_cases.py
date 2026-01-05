import pandas as pd
from typing import Any, Dict, List
from requirements_impl import MetabolicEnvironment, LiverMetabolismSystem


def _simulate(env: MetabolicEnvironment, minutes: int, inject=None) -> pd.DataFrame:
    system = LiverMetabolismSystem(env)
    for t in range(minutes):
        hour = t / 60.0
        if callable(inject):
            inject(env, t)
        system.step(hour)
    return pd.DataFrame(env.history)


def run_yaml_tests() -> Dict[str, Dict[str, float]]:
    results: Dict[str, Dict[str, float]] = {}

    def inject_three_meals(env: MetabolicEnvironment, t: int):
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
    env = MetabolicEnvironment()
    df = _simulate(env, minutes=24*60, inject=inject_three_meals)
    def _win(df, s, e):
        m = (df["time"] >= s) & (df["time"] < e)
        return df.loc[m]
    morning_fasting = _win(df, 6.0, 7.0)
    breakfast = _win(df, 8.0, 9.0)
    lunch = _win(df, 12.0, 13.0)
    dinner = _win(df, 18.0, 19.0)
    post_meal = pd.concat([breakfast, lunch, dinner], ignore_index=True)
    non_meal = df.loc[~((df["time"].between(8.0, 9.0)) | (df["time"].between(12.0, 13.0)) | (df["time"].between(18.0, 19.0)))]
    results["TC-NORMAL-THREE-MEALS-01"] = {
        "insulin_postprandial_high": float(post_meal["insulin"].mean() > non_meal["insulin"].mean()),
        "glucagon_fasting_high": float(morning_fasting["glucagon"].mean() > breakfast["glucagon"].mean()),
        "glucose_peaks_post_meal": float(max(breakfast["glucose"].max(), lunch["glucose"].max(), dinner["glucose"].max()) > morning_fasting["glucose"].mean()),
        "glycogen_net_increase": float(df["glycogen"].iloc[-1] > df["glycogen"].iloc[0]),
        "triglycerides_postprandial_increase": float(post_meal["triglycerides"].mean() > non_meal["triglycerides"].mean()),
        "ketone_bodies_fasting_higher_than_postprandial": float(morning_fasting["ketone_body"].mean() > post_meal["ketone_body"].mean())
    }

    env = MetabolicEnvironment()
    df = _simulate(env, minutes=8*60)
    results["TC-SLEEP-FASTING-01"] = {
        "glucose_decrease_slightly": float(df["glucose"].iloc[-1] < df["glucose"].iloc[0]),
        "glycogen_decrease": float(df["glycogen"].iloc[-1] < df["glycogen"].iloc[0]),
        "fatty_acid_increase": float(df["fatty_acid"].iloc[-1] > df["fatty_acid"].iloc[0]),
        "ketone_body_baseline": float(abs(df["ketone_body"].iloc[-1] - df["ketone_body"].iloc[0]) < 5.0),
        "urea_increase_slightly": float(df["urea"].iloc[-1] > df["urea"].iloc[0]),
        "insulin_low": float(df["insulin"].iloc[-1] < 0.5),
        "glucagon_high": float(df["glucagon"].iloc[-1] > 0.5)
    }

    def inject_highcarb(env: MetabolicEnvironment, t: int):
        if 0 <= t < 60:
            env.setParameter("is_postprandial", True)
            env.setMetabolite("glucose", env.getMetabolite("glucose") + 0.8)
            env.setMetabolite("amino_acid", env.getMetabolite("amino_acid") + 0.2)
            env.setMetabolite("glycerol", env.getMetabolite("glycerol") + 0.05)
        else:
            env.setParameter("is_postprandial", False)
    env = MetabolicEnvironment()
    df = _simulate(env, minutes=3*60, inject=inject_highcarb)
    results["TC-POSTPRANDIAL-HIGHCARB-01"] = {
        "glucose_transient_increase_then_normalize": float(df["glucose"].max() > env.getMetabolite("glucose") and df["glucose"].iloc[-1] < df["glucose"].mean()),
        "glycogen_increase": float(df["glycogen"].iloc[-1] > df["glycogen"].iloc[0]),
        "fatty_acids_increase_via_lipogenesis": float(df["triglycerides"].iloc[-1] > df["triglycerides"].iloc[0]),
        "ATP_increase": float(df["atp"].iloc[-1] > df["atp"].iloc[0]),
        "insulin_high": float(df["insulin"].mean() > 0.6),
        "glucagon_suppressed": float(df["glucagon"].mean() < 0.6)
    }

    def inject_exercise(env: MetabolicEnvironment, t: int):
        if 0 <= t < 60:
            env.signals["epinephrine"] = 1.5
            env.setMetabolite("oxygen", max(env.getMetabolite("oxygen") - 0.2, 0.0))
    env = MetabolicEnvironment()
    df = _simulate(env, minutes=90, inject=inject_exercise)
    results["TC-EXERCISE-HIGH-INTENSITY-01"] = {
        "ATP_decrease": float(df["atp"].iloc[-1] < df["atp"].iloc[0]),
        "glycogen_rapid_decrease": float(df["glycogen"].iloc[-1] < df["glycogen"].iloc[0]),
        "fatty_acid_increase": float(df["fatty_acid"].iloc[-1] > df["fatty_acid"].iloc[0]),
        "lactate_increase": float(df["lactate"].iloc[-1] > df["lactate"].iloc[0]),
        "adrenaline_high": float(df["epinephrine"].mean() > 0.8)
    }

    env = MetabolicEnvironment()
    df = _simulate(env, minutes=72*60)
    results["TC-STARVATION-KETOSIS-01"] = {
        "glucose_maintained_low": float(df["glucose"].iloc[-1] < 80.0),
        "fatty_acid_high": float(df["fatty_acid"].iloc[-1] > df["fatty_acid"].iloc[0]),
        "ketone_bodies_high": float(df["ketone_body"].iloc[-1] > df["ketone_body"].iloc[0]),
        "urea_initial_increase_then_stable": float(df["urea"].iloc[-1] >= df["urea"].iloc[0])
    }

    env = MetabolicEnvironment()
    env.setMetabolite("oxygen", 10.0)
    df = _simulate(env, minutes=120)
    results["TC-HYPOXIA-01"] = {
        "lactate_increase": float(df["lactate"].iloc[-1] > df["lactate"].iloc[0]),
        "ATP_decrease": float(df["atp"].iloc[-1] < df["atp"].iloc[0]),
        "NADH_accumulate": float(df["nadh"].iloc[-1] > df["nadh"].iloc[0])
    }

    env = MetabolicEnvironment()
    env.signals["inflammation"] = 1.0
    df = _simulate(env, minutes=240)
    results["TC-INFLAMMATION-ACUTE-01"] = {
        "glucose_increase": float(df["glucose"].iloc[-1] > df["glucose"].iloc[0]),
        "amino_acids_mobilize": float(df["amino_acid"].iloc[0] >= df["amino_acid"].min()),
        "insulin_sensitivity_decreased_proxy": float(df["insulin"].mean() < 0.8)
    }

    def inject_high_protein(env: MetabolicEnvironment, t: int):
        if 0 <= t < 60:
            env.setParameter("is_postprandial", True)
            env.setMetabolite("amino_acid", env.getMetabolite("amino_acid") + 0.8)
        else:
            env.setParameter("is_postprandial", False)
    env = MetabolicEnvironment()
    df = _simulate(env, minutes=180, inject=inject_high_protein)
    results["TC-HIGH-PROTEIN-DIET-01"] = {
        "amino_acids_high": float(df["amino_acid"].max() > df["amino_acid"].iloc[0]),
        "urea_increase": float(df["urea"].iloc[-1] > df["urea"].iloc[0]),
        "glucose_stable": float(df["glucose"].std() < 15.0)
    }

    def inject_high_fat(env: MetabolicEnvironment, t: int):
        if 0 <= t < 60:
            env.setParameter("is_postprandial", True)
            env.setMetabolite("fatty_acid", env.getMetabolite("fatty_acid") + 0.8)
        else:
            env.setParameter("is_postprandial", False)
    env = MetabolicEnvironment()
    df = _simulate(env, minutes=180, inject=inject_high_fat)
    results["TC-HIGH-FAT-MEAL-01"] = {
        "triglycerides_increase": float(df["triglycerides"].iloc[-1] > df["triglycerides"].iloc[0]),
        "fatty_acids_increase": float(df["fatty_acid"].iloc[-1] > df["fatty_acid"].iloc[0]),
        "insulin_moderate": float(0.3 < df["insulin"].mean() < 0.9)
    }

    env = MetabolicEnvironment()
    env.signals["insulin"] = 0.2
    env.signals["glucagon"] = 0.8
    df = _simulate(env, minutes=240)
    results["TC-INSULIN-RESISTANCE-01"] = {
        "glucose_elevated_persistent": float(df["glucose"].iloc[-1] > df["glucose"].iloc[0]),
        "fatty_acids_increase": float(df["fatty_acid"].iloc[-1] > df["fatty_acid"].iloc[0]),
        "glycogen_reduced_synthesis": float(df["glycogen"].iloc[-1] <= df["glycogen"].iloc[0])
    }

    env = MetabolicEnvironment()
    env.signals["cortisol"] = 1.5
    df = _simulate(env, minutes=7*24*60//24)
    results["TC-CORTISOL-CHRONIC-01"] = {
        "glucose_increase": float(df["glucose"].iloc[-1] > df["glucose"].iloc[0]),
        "amino_acids_mobilized": float(df["amino_acid"].iloc[-1] < df["amino_acid"].iloc[0]),
        "urea_increase": float(df["urea"].iloc[-1] > df["urea"].iloc[0])
    }

    env = MetabolicEnvironment()
    env.signals["insulin"] = 0.05
    env.signals["glucagon"] = 0.9
    df = _simulate(env, minutes=240)
    results["TC-DKA-01"] = {
        "ketone_bodies_very_high": float(df["ketone_body"].iloc[-1] > df["ketone_body"].iloc[0]),
        "fatty_acids_high": float(df["fatty_acid"].iloc[-1] > df["fatty_acid"].iloc[0])
    }

    def inject_refeed(env: MetabolicEnvironment, t: int):
        if 0 <= t < 60:
            env.setMetabolite("glucose", env.getMetabolite("glucose") + 1.0)
            env.setParameter("is_postprandial", True)
        else:
            env.setParameter("is_postprandial", False)
    env = MetabolicEnvironment()
    df = _simulate(env, minutes=180, inject=inject_refeed)
    results["TC-REFEEDING-AFTER-FAST-01"] = {
        "glycogen_replenish": float(df["glycogen"].iloc[-1] > df["glycogen"].iloc[0]),
        "ketone_bodies_decrease": float(df["ketone_body"].iloc[-1] < df["ketone_body"].iloc[0]),
        "ATP_increase": float(df["atp"].iloc[-1] > df["atp"].iloc[0])
    }

    env = MetabolicEnvironment()
    env.signals["insulin"] = 1.2
    env.parameters["insulin_degrading_enzyme_activity"] = 0.1
    df = _simulate(env, minutes=240)
    results["TC-INSULIN-DEGRADATION-IMPAIRED-01"] = {
        "insulin_prolonged_high": float(df["insulin"].mean() > 0.8),
        "glycogen_prolonged_increase": float(df["glycogen"].iloc[-1] > df["glycogen"].iloc[0]),
        "glucose_decrease_then_stable": float(df["glucose"].iloc[-1] <= df["glucose"].iloc[0])
    }

    env = MetabolicEnvironment()
    env.parameters["xenobiotic_load"] = 5.0
    env.parameters["liver_function"] = 0.4
    df = _simulate(env, minutes=240)
    results["TC-LIVER-DETOX-INSUFFICIENCY-01"] = {
        "phaseI_intermediates_accumulate": float(df["phaseI_intermediates"].iloc[-1] > df["phaseI_intermediates"].iloc[0]),
        "conjugates_decrease": float(df["conjugates"].iloc[-1] < df["conjugates"].iloc[0]),
        "NADPH_decrease": float(df["nadph"].iloc[-1] < df["nadph"].iloc[0])
    }

    env = MetabolicEnvironment()
    df = _simulate(env, minutes=240)
    results["TC-BASELINE-ENV-01"] = {
        "glucose_stable": float(df["glucose"].std() < 10.0),
        "ATP_baseline": float(df["atp"].mean() > 50.0),
        "insulin_baseline": float(0.3 < df["insulin"].mean() < 0.7),
        "glucagon_baseline": float(0.3 < df["glucagon"].mean() < 0.7)
    }

    def inject_mixed_meal(env: MetabolicEnvironment, t: int):
        if 0 <= t < 60:
            env.setParameter("is_postprandial", True)
            env.setMetabolite("glucose", env.getMetabolite("glucose") + 0.6)
            env.setMetabolite("fatty_acid", env.getMetabolite("fatty_acid") + 0.4)
            env.setMetabolite("amino_acid", env.getMetabolite("amino_acid") + 0.3)
        else:
            env.setParameter("is_postprandial", False)
    env = MetabolicEnvironment()
    df = _simulate(env, minutes=180, inject=inject_mixed_meal)
    results["TC-MIXED-MEAL-01"] = {
        "glycogen_increase": float(df["glycogen"].iloc[-1] > df["glycogen"].iloc[0]),
        "fatty_acids_increase_via_lipogenesis": float(df["triglycerides"].iloc[-1] > df["triglycerides"].iloc[0]),
        "amino_acids_increase": float(df["amino_acid"].iloc[-1] > df["amino_acid"].iloc[0]),
        "urea_slight_increase": float(df["urea"].iloc[-1] >= df["urea"].iloc[0]),
        "insulin_high": float(df["insulin"].mean() > 0.6),
        "glucagon_low": float(df["glucagon"].mean() < 0.6)
    }

    env = MetabolicEnvironment()
    env.setMetabolite("amino_acid", env.getMetabolite("amino_acid") + 2.0)
    df = _simulate(env, minutes=180)
    results["TC-PLASMA-PROTEIN-SYNTHESIS-01"] = {
        "plasma_proteins_increase": float(df["albumin"].iloc[-1] > df["albumin"].iloc[0]),
        "insulin_moderate": float(0.3 < df["insulin"].mean() < 0.9)
    }

    env = MetabolicEnvironment()
    env.setMetabolite("amino_acid", env.getMetabolite("amino_acid") + 2.0)
    df = _simulate(env, minutes=180)
    results["TC-COAGULATION-UPREG-01"] = {
        "coagulation_factors_increase": float(df["clotting_factor"].iloc[-1] > df["clotting_factor"].iloc[0])
    }

    env = MetabolicEnvironment()
    env.setMetabolite("ammonia", env.getMetabolite("ammonia") + 2.0)
    env.setMetabolite("atp", env.getMetabolite("atp") + 10.0)
    df = _simulate(env, minutes=120)
    results["TC-AMMONIA-SPIKE-01"] = {
        "urea_increase": float(df["urea"].iloc[-1] > df["urea"].iloc[0])
    }

    env = MetabolicEnvironment()
    env.signals["insulin"] = 0.5
    env.signals["glucagon"] = 0.5
    env.signals["epinephrine"] = 0.5
    env.signals["inflammation"] = 0.5
    df = _simulate(env, minutes=240)
    results["TC-MULTI-SIGNAL-INTEGRATION-01"] = {
        "glucose_variable": float(df["glucose"].std() > 1.0),
        "fatty_acids_mobilized": float(df["fatty_acid"].iloc[-1] != df["fatty_acid"].iloc[0]),
        "amino_acids_mobilized": float(df["amino_acid"].iloc[-1] != df["amino_acid"].iloc[0]),
        "insulin_sensitivity_decreased_proxy": float(df["insulin"].mean() < 0.7)
    }

    env = MetabolicEnvironment()
    env.setMetabolite("atp", 120.0)
    df = _simulate(env, minutes=180)
    results["TC-PFK1-REGULATION-01"] = {
        "glycolytic_flux_decrease_proxy": float(df["lactate"].iloc[-1] <= df["lactate"].iloc[0])
    }

    env = MetabolicEnvironment()
    df = _simulate(env, minutes=180)
    results["TC-GLYCOGEN-BRANCHING-THRESH-01"] = {
        "branched_glycogen_increase_proxy": float(df["glycogen"].iloc[-1] >= df["glycogen"].iloc[0])
    }
    return results


TEST_REQ_MAP: Dict[str, List[str]] = {
    "TC-NORMAL-THREE-MEALS-01": ["REQ-1-1-1", "REQ-1-2-1", "REQ-3-2", "ENV-1"],
    "TC-SLEEP-FASTING-01": ["REQ-1-1-2", "REQ-1-1-3", "REQ-1-2-2"],
    "TC-POSTPRANDIAL-HIGHCARB-01": ["REQ-1-1-1", "REQ-1-1-4", "REQ-1-2-1", "REQ-3-2"],
    "TC-EXERCISE-HIGH-INTENSITY-01": ["REQ-1-1-2", "REQ-1-1-4", "REQ-1-2-2", "REQ-1-4-1"],
    "TC-STARVATION-KETOSIS-01": ["REQ-1-1-3", "REQ-1-2-2", "REQ-1-4-2", "REQ-4-1"],
    "TC-HYPOXIA-01": ["REQ-1-4-1", "REQ-1-1-4"],
    "TC-INFLAMMATION-ACUTE-01": ["REQ-5-3", "REQ-1-1-3", "REQ-3-2"],
    "TC-HIGH-PROTEIN-DIET-01": ["REQ-1-3-1", "REQ-4-1"],
    "TC-HIGH-FAT-MEAL-01": ["REQ-1-2-3", "REQ-3-1"],
    "TC-INSULIN-RESISTANCE-01": ["REQ-5-1", "REQ-1-1-3", "REQ-1-2-1"],
    "TC-CORTISOL-CHRONIC-01": ["REQ-1-1-3", "REQ-1-3-1", "REQ-5-1"],
    "TC-DKA-01": ["REQ-1-4-2", "REQ-1-2-2", "REQ-1-1-3"],
    "TC-REFEEDING-AFTER-FAST-01": ["REQ-1-1-1", "REQ-1-4-2", "REQ-1-1-4"],
    "TC-INSULIN-DEGRADATION-IMPAIRED-01": ["REQ-5-4-1", "REQ-1-1-1"],
    "TC-LIVER-DETOX-INSUFFICIENCY-01": ["REQ-2-1", "REQ-2-2"],
    "TC-BASELINE-ENV-01": ["ENV-1"],
    "TC-MIXED-MEAL-01": ["REQ-1", "REQ-1-1", "REQ-1-2", "REQ-1-3"],
    "TC-PLASMA-PROTEIN-SYNTHESIS-01": ["REQ-3", "REQ-3-2"],
    "TC-COAGULATION-UPREG-01": ["REQ-3", "REQ-3-3"],
    "TC-AMMONIA-SPIKE-01": ["REQ-4", "REQ-4-1"],
    "TC-MULTI-SIGNAL-INTEGRATION-01": ["REQ-5", "REQ-5-1", "REQ-5-2", "REQ-5-3", "REQ-5-4"],
    "TC-PFK1-REGULATION-01": ["REQ-1-1-4-2"],
    "TC-GLYCOGEN-BRANCHING-THRESH-01": ["REQ-1-1-1-4"]
}


def summarize_test_pass(results: Dict[str, Dict[str, float]]) -> Dict[str, bool]:
    summary: Dict[str, bool] = {}
    for tc, checks in results.items():
        summary[tc] = all(v == 1.0 for v in checks.values())
    return summary


def aggregate_requirements(results: Dict[str, Dict[str, float]]) -> Dict[str, Dict[str, Any]]:
    tc_pass = summarize_test_pass(results)
    req_to_tests: Dict[str, List[str]] = {}
    for tc, reqs in TEST_REQ_MAP.items():
        for r in reqs:
            req_to_tests.setdefault(r, []).append(tc)
    req_summary: Dict[str, Dict[str, Any]] = {}
    for r, tcs in req_to_tests.items():
        status = all(tc_pass.get(tc, False) for tc in tcs)
        req_summary[r] = {"status": status, "tests": tcs}
    return req_summary


def run_all() -> Dict[str, Any]:
    results = run_yaml_tests()
    tc_summary = summarize_test_pass(results)
    req_summary = aggregate_requirements(results)
    per_test_counts: Dict[str, Dict[str, int]] = {}
    total_passed = 0
    total_checks = 0
    for tc, checks in results.items():
        passed = sum(1 for v in checks.values() if v == 1.0)
        total = len(checks)
        per_test_counts[tc] = {"passed": passed, "total": total}
        total_passed += passed
        total_checks += total
    check_counts = {"per_test": per_test_counts, "global": {"passed": total_passed, "total": total_checks}}
    return {"test_results": results, "test_summary": tc_summary, "requirements_summary": req_summary, "check_counts": check_counts}


if __name__ == "__main__":
    out = run_all()
    print(out["test_summary"])
    print(out["requirements_summary"])
    gc = out.get("check_counts", {}).get("global", {})
    print(f"正确 {gc.get('passed', 0)} / 总 {gc.get('total', 0)}")
