import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from typing import Dict, List


# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei'] # 或者 'Microsoft YaHei'
# 解决负号 '-' 显示为方块的问题
plt.rcParams['axes.unicode_minus'] = False


# ==========================================
# ENV-1: 代谢环境模块 (Global State)
# ==========================================
class MetabolicEnvironment:
    def __init__(self):
        # 代谢物池 (Metabolites)
        self.metabolites = {
            "glucose": 100.0, "glycogen": 500.0, "fatty_acid": 50.0,
            "glycerol": 10.0, "amino_acid": 30.0, "ammonia": 0.5,
            "urea": 10.0, "cholesterol": 20.0, "bile_acid": 5.0,
            "atp": 100.0, "adp": 20.0, "nad_plus": 50.0, "nadh": 10.0,
            "acetyl_coa": 5.0, "ketone_body": 1.0, "lactate": 5.0,
            "oxygen": 100.0, "albumin": 40.0, "clotting_factor": 10.0
        }
        # 信号分子 (Signals)
        self.signals = {
            "insulin": 1.0, "glucagon": 1.0, "epinephrine": 0.1,
            "cortisol": 0.1, "inflammation": 0.0, "sympath_nerve": 1.0
        }
        # 记录历史用于可视化
        self.history = []

    def update_history(self, t):
        record = {**self.metabolites, **self.signals, "time": t}
        self.history.append(record)

# ==========================================
# 代谢功能模块实现 (REQ-1 to REQ-5)
# ==========================================
class LiverMetabolismSystem:
    def __init__(self, env: MetabolicEnvironment):
        self.env = env

    def step(self):
        m = self.env.metabolites
        s = self.env.signals

        # --- REQ-5: 激素-神经-免疫调控 (控制逻辑) ---
        # REQ-5-1 & 5-2: 根据当前血糖调节激素分泌(简化逻辑)
        s['insulin'] = 1.0 / (1.0 + np.exp(-0.1 * (m['glucose'] - 110)))
        s['glucagon'] = 1.0 / (1.0 + np.exp(0.1 * (m['glucose'] - 90)))
        # REQ-5-3: 代谢重编程控制 (炎症影响)
        metabolic_rate_mod = 1.0 - (s['inflammation'] * 0.5)

        # --- REQ-1: 营养代谢 ---
        # REQ-1-1: 碳水代谢
        # REQ-1-1-1: 糖原合成
        if s['insulin'] > 0.5 and m['glucose'] > 100 and m['atp'] > 20:
            rate = 0.5 * s['insulin']
            m['glucose'] -= rate; m['atp'] -= rate * 0.1; m['glycogen'] += rate; m['adp'] += rate * 0.1
        
        # REQ-1-1-2: 糖原分解
        if (s['glucagon'] > 0.6 or s['epinephrine'] > 0.5) and m['glycogen'] > 10:
            rate = 0.6 * max(s['glucagon'], s['epinephrine'])
            m['glycogen'] -= rate; m['glucose'] += rate

        # REQ-1-1-3: 糖异生
        if s['glucagon'] > 0.7 and m['atp'] > 30:
            rate = 0.2 * s['glucagon']
            m['lactate'] -= rate; m['glycerol'] -= rate; m['amino_acid'] -= rate
            m['glucose'] += rate; m['atp'] -= rate * 2; m['adp'] += rate * 2

        # REQ-1-2: 脂类代谢
        # REQ-1-2-1: 脂肪酸合成
        if s['insulin'] > 0.7 and m['acetyl_coa'] > 2:
            rate = 0.1 * s['insulin']
            m['acetyl_coa'] -= rate; m['atp'] -= rate; m['fatty_acid'] += rate
        
        # REQ-1-2-2: 脂肪酸分解 (Beta-oxidation)
        if s['glucagon'] > 0.5 and m['fatty_acid'] > 5:
            rate = 0.3 * s['glucagon']
            m['fatty_acid'] -= rate; m['nad_plus'] -= rate; m['nadh'] += rate; m['acetyl_coa'] += rate

        # REQ-1-4-2: 酮体生成
        if m['glucose'] < 70 and m['acetyl_coa'] > 5:
            rate = 0.2
            m['acetyl_coa'] -= rate; m['ketone_body'] += rate

        # REQ-1-3: 氨基酸代谢
        # REQ-1-3-1 & 1-3-2: 分解与合成
        if m['amino_acid'] > 40: # 摄入过量
            rate = 0.2
            m['amino_acid'] -= rate; m['ammonia'] += rate # 产生氨
        
        # REQ-4: 氮处理与尿素循环
        # REQ-4-1: 尿素循环
        if m['ammonia'] > 0.1 and m['atp'] > 10:
            rate = 0.4 * m['ammonia']
            m['ammonia'] -= rate; m['atp'] -= rate; m['urea'] += rate

        # REQ-1-4-1: 有氧呼吸与ATP生成 (维持细胞运转)
        if m['oxygen'] > 20:
            resp_rate = 0.5
            m['glucose'] -= resp_rate * 0.1; m['fatty_acid'] -= resp_rate * 0.05
            m['atp'] += 2.0; m['oxygen'] -= 1.0

        # REQ-2: 解毒 (生物转化)
        # REQ-2-1 & 2-2: 氧化与结合
        drug_toxin = 5.0 # 模拟外部毒素输入
        if m['oxygen'] > 10 and m['glucose'] > 50:
            rate = 0.1
            m['glucose'] -= rate * 0.1 # 消耗能量用于解毒

        # REQ-3: 合成与分泌
        # REQ-3-1: 胆汁酸合成
        if m['cholesterol'] > 10:
            rate = 0.05
            m['cholesterol'] -= rate; m['bile_acid'] += rate
        # REQ-3-2 & 3-3: 血浆蛋白与凝血因子
        if m['amino_acid'] > 10:
            m['albumin'] += 0.02; m['clotting_factor'] += 0.01; m['amino_acid'] -= 0.03

# ==========================================
# 仿真运行与可视化
# ==========================================
def run_simulation(steps=200):
    env = MetabolicEnvironment()
    system = LiverMetabolismSystem(env)
    
    for t in range(steps):
        # 模拟外部干扰：在第50步进食（血糖升高），在第150步应激（肾上腺素升高）
        if 50 <= t <= 60:
            env.metabolites['glucose'] += 15.0
            env.metabolites['amino_acid'] += 5.0
        if t > 150:
            env.signals['epinephrine'] = 2.0
        # if t == 151:
        #     env.signals['epinephrine'] = 0.1

        system.step()
        env.update_history(t)
    
    return pd.DataFrame(env.history)

def visualize(df):
    plt.figure(figsize=(14, 8))
    
    # 选取关键指标进行可视化
    targets = ['glucose', 'glycogen', 'insulin', 'glucagon', 'atp', 'fatty_acid', 'urea', 'ketone_body']
    
    for column in targets:
        # 对信号和代谢物进行归一化处理以便同图观察趋势
        norm_val = df[column] / df[column].max()
        plt.plot(df['time'], norm_val, label=column, linewidth=2)

    plt.title("Human Metabolic & Regulatory System Simulation (Liver Flux)", fontsize=15)
    plt.xlabel("Time Steps", fontsize=12)
    plt.ylabel("Normalized Concentration / Level", fontsize=12)
    plt.legend(loc='upper right', bbox_to_anchor=(1.15, 1))
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()
    plt.savefig('metabolite_curves.png')

if __name__ == "__main__":
    simulation_data = run_simulation(200)
    visualize(simulation_data)
