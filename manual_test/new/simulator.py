import numpy as np
from typing import Dict, List, Optional
import matplotlib.pyplot as plt

# ==========================================
# 1. 基础物质定义 (Atom Layer)
# ==========================================
class Metabolite:
    def __init__(self, name: str, initial_conc: float):
        self.name = name
        self.conc = initial_conc

    def update(self, delta: float):
        # 确保浓度不为负
        self.conc = max(0.0, self.conc + delta)

# ==========================================
# 2. 反应定义 (Reaction Layer)
# ==========================================
class Reaction:
    def __init__(self, name: str, stoichiometry: Dict[str, float], key_enzyme: str):
        self.name = name
        # 计量比，例如 {"glucose": -1.0, "pyruvate": 2.0} 表示消耗1分糖生成2分丙酮酸
        self.stoichiometry = stoichiometry
        self.key_enzyme = key_enzyme

    def get_deltas(self, rate: float) -> Dict[str, float]:
        """根据给定的速率计算各物质的变化量"""
        return {m: coeff * rate for m, coeff in self.stoichiometry.items()}

# ==========================================
# 3. 代谢模块 (Pathway Layer)
# ==========================================
class NutrientMetabolism:
    def __init__(self):
        self.reactions = [
            Reaction("Glycolysis", {"glucose": -1.0, "atp": 2.0, "pyruvate": 2.0, "nadh": 2.0}, "PFK-1"),
            Reaction("Gluconeogenesis", {"pyruvate": -2.0, "atp": -6.0, "glucose": 1.0}, "PEPCK/FBPase-1"),
            Reaction("Glycogenesis", {"glucose": -1.0, "atp": -1.0, "glycogen": 1.0}, "Glycogen Synthase"),
            Reaction("Glycogenolysis", {"glycogen": -1.0, "glucose": 1.0}, "Glycogen Phosphorylase"),
            Reaction("PPP", {"glucose": -1.0, "nadph": 2.0, "ribose_5p": 1.0}, "G6PD"),
            Reaction("AnaerobicRespiration", {"pyruvate": -1.0, "lactate": 1.0, "nadh": -1.0}, "LDH"),
            Reaction("PyruvateOxidation", {"pyruvate": -1.0, "acetyl_coa": 1.0, "nadh": 1.0}, "PDH"),
            Reaction("TCA_OxPhos", {"acetyl_coa": -1.0, "nadh": -3.0, "atp": 10.0}, "TCA/ETC"),
            Reaction("FattyAcidSynthesis", {"acetyl_coa": -2.0, "nadph": -4.0, "atp": -1.0, "fatty_acid": 1.0}, "ACC/FAS"),
            Reaction("BetaOxidation", {"fatty_acid": -1.0, "acetyl_coa": 1.0, "nadh": 1.0}, "CPT-1"),
            Reaction("Ketogenesis", {"acetyl_coa": -2.0, "ketone_bodies": 1.0}, "mHMGCS"),
            Reaction("TriglycerideSynthesis", {"fatty_acid": -3.0, "glycerol_3p": -1.0, "triglyceride": 1.0}, "DGAT"),
            Reaction("CholesterolSynthesis", {"acetyl_coa": -2.0, "nadph": -2.0, "cholesterol": 1.0}, "HMGCR"),
            Reaction("VLDLAssembly", {"triglyceride": -1.0, "cholesterol": -1.0, "vldl": 1.0}, "MTP"),
            Reaction("BileAcidSynthesis", {"cholesterol": -1.0, "nadph": -1.0, "bile_acid": 1.0}, "CYP7A1"),
            Reaction("Transamination", {"amino_acids": -1.0, "glutamate": 1.0}, "ALT/AST"),
            Reaction("GlutamateDehydrogenase", {"glutamate": -1.0, "ammonia": 1.0, "alpha_ketoglutarate": 1.0, "nadh": 1.0}, "GDH"),
            Reaction("UreaCycle", {"ammonia": -2.0, "atp": -2.0, "urea": 1.0}, "CPS-I/OTC/ASS"),
            Reaction("GlucoseAlanineCycle", {"alanine": -1.0, "pyruvate": 1.0, "glucose": 1.0}, "ALT"),
            Reaction("AlbuminSynthesis", {"amino_acids": -10.0, "atp": -5.0, "albumin": 1.0}, "Ribosome/mTOR"),
            Reaction("GlutamineSynthesis", {"ammonia": -1.0, "glutamate": -1.0, "glutamine": 1.0}, "GS"),
        ]
        self.reaction_names = [r.name for r in self.reactions]

    def get_reaction_count(self):
        return len(self.reactions)

# ==========================================
# 4. 模拟引擎 (Engine Layer)
# ==========================================
class MetabolicSimulator:
    def __init__(self):
        # 初始化代谢池
        self.pool = {
            "glucose": Metabolite("Glucose", 90.0),     # 葡萄糖
            "glycogen": Metabolite("Glycogen", 400.0),  # 糖原
            "pyruvate": Metabolite("Pyruvate", 5.0),    # 丙酮酸
            "lactate": Metabolite("Lactate", 5.0),      # 乳酸
            "atp": Metabolite("ATP", 100.0),            # ATP
            "nadh": Metabolite("NADH", 10.0),           # NADH
            "nadph": Metabolite("NADPH", 20.0),         # NADPH 
            "ribose_5p": Metabolite("Ribose-5P", 1.0),  # 核糖-5-磷酸
            "acetyl_coa": Metabolite("Acetyl-CoA", 5.0),
            "fatty_acid": Metabolite("FattyAcid", 20.0),
            "ketone_bodies": Metabolite("KetoneBodies", 0.0),
            "glycerol_3p": Metabolite("Glycerol-3P", 5.0),
            "triglyceride": Metabolite("Triglyceride", 50.0),
            "cholesterol": Metabolite("Cholesterol", 10.0),
            "vldl": Metabolite("VLDL", 0.0),
            "bile_acid": Metabolite("BileAcid", 5.0),
            "amino_acids": Metabolite("AminoAcids", 50.0),
            "glutamate": Metabolite("Glutamate", 5.0),
            "alpha_ketoglutarate": Metabolite("Alpha-Ketoglutarate", 5.0),
            "ammonia": Metabolite("Ammonia", 5.0),
            "urea": Metabolite("Urea", 0.0),
            "alanine": Metabolite("Alanine", 5.0),
            "albumin": Metabolite("Albumin", 0.0),
            "glutamine": Metabolite("Glutamine", 5.0)
        }
        self.pathway = NutrientMetabolism()
        self.history = []
        self.shortage_log = [] # 记录每一步的底物缺失量，用于 Loss


    def apply_step(self, rate_vector: np.ndarray, dt: float = 1.0):
        step_shortage = 0.0
        pending_deltas = {name: 0.0 for name in self.pool.keys()}

        # 1. 预计算所有变化
        for i, rate in enumerate(rate_vector):
            reaction = self.pathway.reactions[i]
            deltas = reaction.get_deltas(rate * dt)
            for m_name, delta in deltas.items():
                if m_name in pending_deltas:
                    pending_deltas[m_name] += delta

        # 2. 检查底物可用性并更新 (关键：检测异常)
        for m_name, delta in pending_deltas.items():
            current_val = self.pool[m_name].conc
            if current_val + delta < 0:
                # 记录缺失量：预测要求的消耗量 - 实际能提供的量
                shortage = abs(current_val + delta)
                step_shortage += shortage
                self.pool[m_name].conc = 0.0 # 强制设为0
            else:
                self.pool[m_name].conc += delta

        return step_shortage


    def run_simulation(self, rate_matrix: np.ndarray):
        """
        rate_matrix: T x N 的矩阵
        """
        T = rate_matrix.shape[0]
        for t in range(T):
            step_shortage = self.apply_step(rate_matrix[t])
            self.shortage_log.append(step_shortage)
            # 记录快照
            snapshot = {name: m.conc for name, m in self.pool.items()}
            self.history.append(snapshot)
        return self.history
    
    
    def plot_results(self, save_path='curve.png'):
        steps = range(len(self.history))
        metabolites = self.history[0].keys()

        # 绘制主代谢物曲线
        plt.subplot(1, 2, 1)
        for m in metabolites:
            data = [h[m] for h in self.history]
            plt.plot(steps, data, label=m, linewidth=2)
        plt.title("Metabolite Concentration Over Time")
        plt.xlabel("Time Step")
        plt.ylabel("Concentration")
        plt.legend()
        plt.grid(True, alpha=0.3)

        # 绘制 Shortage Loss 曲线
        plt.subplot(1, 2, 2)
        plt.bar(range(len(self.shortage_log)), self.shortage_log, color='red', alpha=0.6)
        plt.title("Shortage Penalty (Loss Indicator)")
        plt.xlabel("Time Step")
        plt.ylabel("Shortage Magnitude")
        plt.grid(True, axis='y', linestyle='--')

        plt.tight_layout()
        plt.show()
        plt.savefig(save_path)




if __name__ == "__main__":
    sim = MetabolicSimulator()
    T = 10
    N = sim.pathway.get_reaction_count()
    
    # 模拟一个预测出来的速率矩阵 (T*N)
    # 假设预测网络输出：糖酵解速率为10.0，其余为0
    sample_rates = np.zeros((T, N))
    sample_rates[:, 0] = 10.0  # Glycolysis active
    
    results = sim.run_simulation(sample_rates)
    sim.plot_results()
    
    print(f"{'Step':<5} | {'Glucose':<10} | {'Pyruvate':<10} | {'ATP':<10}")
    for i, res in enumerate(results):
        print(f"{i:<5} | {res['glucose']:<10.2f} | {res['pyruvate']:<10.2f} | {res['atp']:<10.2f}")
