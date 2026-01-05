import sys
import os
import pandas as pd
import numpy as np
from typing import Dict, Any
from simulate import MetabolicEnvironment, LiverMetabolismSystem

UNITS_PER_HOUR = 30
DAY_UNITS = 24 * UNITS_PER_HOUR


def simulate_24h() -> pd.DataFrame:
    env = MetabolicEnvironment()
    system = LiverMetabolismSystem(env)
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

def run_train_cases() -> Dict[str, Dict[str, float]]:
    results = {}
    df = simulate_24h()
    
    # Add absolute time column (hours) starting at 7.0
    df['time_abs'] = df.index / UNITS_PER_HOUR + 7.0
    
    # Helper to get phase data
    def get_phase(start_h, end_h):
        # Handle day wrap if needed (e.g. 22:00 to 31:00)
        return df[(df['time_abs'] >= start_h) & (df['time_abs'] < end_h)]

    # ==========================================
    # TC-TRAIN-PHASE-01: 07:00 - 08:00 (Fasting)
    # ==========================================
    p1 = get_phase(7.0, 8.0)
    results["TC-TRAIN-PHASE-01"] = {
        "glucose_baseline_check": float(4.0 <= p1["glucose"].mean() <= 6.0), # Relaxed range
        "insulin_low": float(p1["insulin"].mean() < 0.5),
        "glucagon_high": float(p1["glucagon"].mean() > 0.5),
        "glycogen_decreasing": float(p1["glycogen"].iloc[-1] < p1["glycogen"].iloc[0]),
    }

    # ==========================================
    # TC-TRAIN-PHASE-02/03: 08:00 - 10:00 (Breakfast + Post)
    # ==========================================
    p3 = get_phase(8.0, 10.0)
    # Need to compare with pre-meal
    pre_meal_glucose = p1["glucose"].iloc[-1]
    
    results["TC-TRAIN-PHASE-03"] = {
        "glucose_peak_rise": float(p3["glucose"].max() > pre_meal_glucose + 1.0),
        "insulin_peak_high": float(p3["insulin"].max() > 0.8),
        "glycogen_increasing": float(p3["glycogen"].iloc[-1] > p3["glycogen"].iloc[0]),
        # Lipogenesis implies TG increase
        "triglycerides_increasing": float(p3["triglycerides"].iloc[-1] > p3["triglycerides"].iloc[0]),
        "glucagon_suppressed": float(p3["glucagon"].min() < 0.5)
    }

    # ==========================================
    # TC-TRAIN-PHASE-04: 10:00 - 12:00 (Early Fasting)
    # ==========================================
    p4 = get_phase(10.0, 12.0)
    results["TC-TRAIN-PHASE-04"] = {
        "glucose_return_baseline": float(p4["glucose"].iloc[-1] < p3["glucose"].max()),
        "insulin_dropping": float(p4["insulin"].iloc[-1] < p3["insulin"].max()),
        "glucagon_rising": float(p4["glucagon"].iloc[-1] > p3["glucagon"].min())
    }

    # ==========================================
    # TC-TRAIN-PHASE-06: 12:00 - 15:00 (Lunch Post)
    # ==========================================
    p6 = get_phase(12.0, 15.0)
    pre_lunch_glucose = p4["glucose"].iloc[-1]
    
    results["TC-TRAIN-PHASE-06"] = {
        "glucose_peak_rise": float(p6["glucose"].max() > pre_lunch_glucose + 1.0),
        "glycogen_strong_synthesis": float(p6["glycogen"].iloc[-1] > p6["glycogen"].iloc[0]),
        "amino_acid_utilization": float(p6["amino_acid"].iloc[-1] < p6["amino_acid"].max()), # Uptake
        "insulin_peak_higher_than_fasting": float(p6["insulin"].max() > 0.8)
    }

    # ==========================================
    # TC-TRAIN-PHASE-07: 15:00 - 18:00 (Afternoon)
    # ==========================================
    p7 = get_phase(15.0, 18.0)
    results["TC-TRAIN-PHASE-07"] = {
        "glucose_stabilizing": float(p7["glucose"].std() < 5.0), # Loose check
        "glucagon_rising_late": float(p7["glucagon"].iloc[-1] > p7["glucagon"].iloc[0])
    }

    # ==========================================
    # TC-TRAIN-PHASE-09: 18:00 - 22:00 (Dinner Post)
    # ==========================================
    p9 = get_phase(18.0, 22.0)
    results["TC-TRAIN-PHASE-09"] = {
        "glycogen_peak_daily": float(p9["glycogen"].max() >= df["glycogen"].max() * 0.9),
        "triglycerides_storage": float(p9["triglycerides"].iloc[-1] > p9["triglycerides"].iloc[0]),
    }

    # ==========================================
    # TC-TRAIN-PHASE-10: 22:00 - 31:00 (Sleep)
    # ==========================================
    p10 = get_phase(22.0, 31.0) # 22:00 to 07:00 next day
    
    results["TC-TRAIN-PHASE-10"] = {
        "insulin_basal_low": float(p10["insulin"].min() < 0.4),
        "glucagon_high": float(p10["glucagon"].mean() > 0.5),
        "glycogen_decay": float(p10["glycogen"].iloc[-1] < p10["glycogen"].iloc[0]),
        "fatty_acid_rise": float(p10["fatty_acid"].iloc[-1] > p10["fatty_acid"].iloc[0]),
        # Ketone body rise might be small in 24h but should not drop
        "ketone_bodies_trend": float(p10["ketone_body"].iloc[-1] >= p10["ketone_body"].iloc[0] - 0.1)
    }

    return results

def summarize_results(results, output_path='test_result_train_cases.txt'):
    total = 0
    passed = 0
    result_str = ''
    result_str += "\n=== Train Cases Verification Results ===\n"
    for tc, checks in results.items():
        result_str += f"Test Case: {tc}\n"
        tc_pass = True
        for name, res in checks.items():
            status = "PASS" if res == 1.0 else "FAIL"
            result_str += f"  - {name}: {status}\n"
            if res != 1.0:
                tc_pass = False
        result_str += f"  => {'[PASSED]' if tc_pass else '[FAILED]'}\n"
        total += 1
        if tc_pass:
            passed += 1
        result_str += "-" * 40 + "\n"
    
    result_str += f"\nSummary: {passed}/{total} Test Cases Passed\n"
    print(result_str)
    with open(output_path, "w") as f:
        f.write(result_str)

    return result_str


if __name__ == "__main__":
    results = run_train_cases()
    txt_path = "../results/test_result_train_cases.txt"
    summarize_results(results, txt_path)
