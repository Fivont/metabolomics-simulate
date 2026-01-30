import numpy as np
from typing import Dict, Any
from concurrent.futures import ThreadPoolExecutor


class MetabolicEnvironment:
    def __init__(self):
        self.metabolites = {
            "glucose": 90.0,
            "glycogen": 400.0,
            "fatty_acid": 50.0,
            "triglycerides": 80.0,
            "glycerol": 10.0,
            "amino_acid": 30.0,
            "ammonia": 0.5,
            "urea": 10.0,
            "cholesterol": 20.0,
            "bile_acid": 5.0,
            "atp": 80.0,
            "adp": 20.0,
            "nad_plus": 50.0,
            "nadh": 10.0,
            "nadph": 20.0,
            "acetyl_coa": 5.0,
            "ketone_body": 1.0,
            "lactate": 5.0,
            "oxygen": 100.0,
            "albumin": 40.0,
            "clotting_factor": 10.0,
            "phaseI_intermediates": 0.0,
            "conjugates": 0.0,
            "ornithine": 1.0,
            "citrulline": 0.0,
            "argininosuccinate": 0.0,
            "arginine": 0.0,
            "ethanol": 0.0,
            "acetaldehyde": 0.0,
            "acetate": 0.0,
            "indirect_bilirubin": 0.2,
            "direct_bilirubin": 0.0,
            "udpga": 5.0,
            "paps": 2.0,
            "gsh": 10.0,
            "napqi": 0.0
        }
        self.signals = {
            "insulin": 0.5,
            "glucagon": 0.5,
            "epinephrine": 0.1,
            "cortisol": 0.1,
            "inflammation": 0.0
        }
        self.parameters = {
            "oxygen_pressure": 100.0,
            "pH": 7.4,
            "temperature": 37.0,
            "is_postprandial": False,
            "insulin_degrading_enzyme_activity": 1.0,
            "liver_function": 1.0,
            "xenobiotic_load": 0.0,
            "insulin_sensitivity": 1.0
        }
        self.history = []

    def update_history(self, t):
        record = {**self.metabolites, **self.signals, **self.parameters, "time": t}
        self.history.append(record)

    def getMetabolite(self, name: str, compartment: str = None) -> float:
        return float(self.metabolites.get(name, 0.0))

    def setMetabolite(self, name: str, value: float, compartment: str = None) -> None:
        self.metabolites[name] = float(max(value, 0.0))

    def getSignal(self, name: str) -> float:
        return float(self.signals.get(name, 0.0))

    def setSignal(self, name: str, value: float) -> None:
        self.signals[name] = float(max(value, 0.0))

    def getParameter(self, name: str) -> float:
        return float(self.parameters.get(name, 0.0))

    def setParameter(self, name: str, value: float) -> None:
        self.parameters[name] = float(value)

    def writeOutputs(self, outputs: Dict[str, float]) -> None:
        for k, v in outputs.items():
            self.metabolites[k] = float(max(self.metabolites.get(k, 0.0) + float(v), 0.0))


class Ctx:
    def __init__(self, env: MetabolicEnvironment):
        self.env = env
        self.rate_modifier = 1.0
        self.last_outputs: Dict[str, Any] = {}

    def control(self, ccId: str) -> bool:
        if ccId == "postprandial":
            return bool(self.env.getParameter("is_postprandial"))
        return True

    def applyAction(self, action: str, payload: Any = None) -> None:
        if action == "downscale_rates":
            self.rate_modifier = float(payload) if payload is not None else 0.5

    def write(self, outputs: Dict[str, float]) -> None:
        self.env.writeOutputs(outputs)
        self.last_outputs = outputs

class ResourcePool:
    def __init__(self, env: MetabolicEnvironment):
        self.snapshot_metabolites = dict(env.metabolites)
        self.snapshot_signals = dict(env.signals)
        self.snapshot_parameters = dict(env.parameters)
        self.outputs: Dict[str, float] = {}
        self.signal_updates: Dict[str, float] = {}
        self.lock = None
        import threading
        self.lock = threading.Lock()

    def write_output(self, outputs: Dict[str, float]) -> None:
        with self.lock:
            for k, v in outputs.items():
                self.outputs[k] = self.outputs.get(k, 0.0) + float(v)

    def set_signal(self, name: str, value: float) -> None:
        with self.lock:
            self.signal_updates[name] = float(max(value, 0.0))

    def set_metabolite_abs(self, name: str, new_value: float) -> None:
        base = float(self.snapshot_metabolites.get(name, 0.0))
        delta = float(max(new_value, 0.0)) - base
        with self.lock:
            self.outputs[name] = self.outputs.get(name, 0.0) + delta

    def drain(self) -> Dict[str, Dict[str, Any]]:
        with self.lock:
            out = {"metabolites": dict(self.outputs), "signals": dict(self.signal_updates)}
            self.outputs.clear()
            self.signal_updates.clear()
            return out

class ResourceEnv(MetabolicEnvironment):
    def __init__(self, pool: ResourcePool):
        super().__init__()
        self.pool = pool
        self.metabolites = pool.snapshot_metabolites
        self.signals = pool.snapshot_signals
        self.parameters = pool.snapshot_parameters
        self.history = []

    def update_history(self, t):
        pass

    def setMetabolite(self, name: str, value: float, compartment: str = None) -> None:
        self.pool.set_metabolite_abs(name, float(value))

    def setSignal(self, name: str, value: float) -> None:
        self.pool.set_signal(name, float(value))

    def writeOutputs(self, outputs: Dict[str, float]) -> None:
        self.pool.write_output(outputs)


def hexokinase_or_glucokinase(ctx: Ctx) -> Dict[str, float]:
    insulin = ctx.env.getSignal("insulin")
    ins_sens = ctx.env.getParameter("insulin_sensitivity")
    glucose = ctx.env.getMetabolite("glucose")
    atp = ctx.env.getMetabolite("atp")
    rate = ctx.rate_modifier * max(0.0, min(glucose, atp)) * (0.01 + 0.05 * insulin * ins_sens)
    ctx.env.setMetabolite("glucose", glucose - rate)
    ctx.env.setMetabolite("atp", atp - rate * 0.2)
    return {"glycogen": 0.0}

def pgm_G6P_to_G1P(ctx: Ctx) -> Dict[str, float]:
    g6p = min(ctx.env.getMetabolite("glucose"), 2.0)
    return {"glucose": -g6p, "glycogen": 0.0}

def udpGlucoseSynthesis(ctx: Ctx) -> Dict[str, float]:
    atp = ctx.env.getMetabolite("atp")
    glucose = ctx.env.getMetabolite("glucose")
    rate = ctx.rate_modifier * min(glucose, atp * 0.5) * 0.02
    return {"glucose": -rate, "atp": -rate * 0.2}

def glycogenSynthaseStep(ctx: Ctx) -> Dict[str, float]:
    insulin = ctx.env.getSignal("insulin")
    ins_sens = ctx.env.getParameter("insulin_sensitivity")
    glucose = ctx.env.getMetabolite("glucose")
    atp = ctx.env.getMetabolite("atp")
    rate = ctx.rate_modifier * (0.01 + 0.05 * insulin * ins_sens) * min(glucose, atp)
    return {"glucose": -rate, "glycogen": rate, "atp": -rate * 0.1, "adp": rate * 0.1}

def branchingEnzymeStep(ctx: Ctx) -> Dict[str, float]:
    glycogen = ctx.env.getMetabolite("glycogen")
    rate = ctx.rate_modifier * min(glycogen, 1.0) * 0.01
    return {"glycogen": rate * 0.0}

def glycogenPhosphorylaseStep(ctx: Ctx) -> Dict[str, float]:
    glucagon = ctx.env.getSignal("glucagon")
    ep = ctx.env.getSignal("epinephrine")
    glycogen = ctx.env.getMetabolite("glycogen")
    rate = ctx.rate_modifier * (0.02 + 0.04 * glucagon + 0.08 * ep) * glycogen
    return {"glycogen": -rate, "glucose": rate}

def debranchingEnzymeStep(ctx: Ctx) -> Dict[str, float]:
    glycogen = ctx.env.getMetabolite("glycogen")
    rate = ctx.rate_modifier * min(glycogen, 1.0) * 0.01
    return {"glycogen": -rate * 0.1, "glucose": rate * 0.1}

def g1p_to_g6p(ctx: Ctx) -> Dict[str, float]:
    return {"glucose": 0.0}

def pepck_OAA_to_PEP(ctx: Ctx) -> Dict[str, float]:
    atp = ctx.env.getMetabolite("atp")
    rate = ctx.rate_modifier * min(atp, 2.0) * 0.02
    return {"atp": -rate}

def g6pase_G6P_to_Glucose(ctx: Ctx) -> Dict[str, float]:
    return {"glucose": 0.0}

def glycolysis_middle_steps(ctx: Ctx) -> Dict[str, float]:
    glucose = ctx.env.getMetabolite("glucose")
    nad_plus = ctx.env.getMetabolite("nad_plus")
    adp = ctx.env.getMetabolite("adp")
    o2 = ctx.env.getMetabolite("oxygen")
    rate = ctx.rate_modifier * min(glucose, nad_plus * 0.5, adp * 0.5) * 0.05
    lact_frac = 0.8 if o2 < 50.0 else 0.5
    return {"glucose": -rate, "nadh": rate, "nad_plus": -rate, "atp": rate, "adp": -rate, "lactate": rate * lact_frac}

def pyruvateKinase_step(ctx: Ctx) -> Dict[str, float]:
    return {"atp": 0.0}

def fattyAcidSynthesis(ctx: Ctx) -> Dict[str, float]:
    insulin = ctx.env.getSignal("insulin")
    ins_sens = ctx.env.getParameter("insulin_sensitivity")
    acetyl = ctx.env.getMetabolite("acetyl_coa")
    nadph = ctx.env.getMetabolite("nadph")
    atp = ctx.env.getMetabolite("atp")
    rate = ctx.rate_modifier * (0.01 + 0.05 * insulin * ins_sens) * min(acetyl, nadph * 0.5, atp * 0.5)
    return {"acetyl_coa": -rate, "fatty_acid": rate, "nadph": -rate * 0.5, "atp": -rate * 0.2}

def betaOxidation(ctx: Ctx) -> Dict[str, float]:
    glucagon = ctx.env.getSignal("glucagon")
    ep = ctx.env.getSignal("epinephrine")
    fa = ctx.env.getMetabolite("fatty_acid")
    nad_plus = ctx.env.getMetabolite("nad_plus")
    etoh = ctx.env.getMetabolite("ethanol")
    nadh = ctx.env.getMetabolite("nadh")
    alcohol_inhibition = 0.6 if (etoh > 0.5) else 1.0
    # 大幅增加基础降解速率，确保脂肪酸能够充分减少
    rate = ctx.rate_modifier * alcohol_inhibition * (0.3 + 0.4 * max(glucagon, ep)) * min(fa, nad_plus)
    # 当脂肪酸浓度较高时，增加额外的降解速率
    if fa > 40.0:
        rate *= 2.0
    elif fa > 20.0:
        rate *= 1.5
    return {"fatty_acid": -rate, "acetyl_coa": rate, "nadh": rate, "nad_plus": -rate, "atp": rate * 0.5}

def deNovoLipogenesis(ctx: Ctx) -> Dict[str, float]:
    insulin = ctx.env.getSignal("insulin")
    ins_sens = ctx.env.getParameter("insulin_sensitivity")
    glucose = ctx.env.getMetabolite("glucose")
    atp = ctx.env.getMetabolite("atp")
    nadph = ctx.env.getMetabolite("nadph")
    excess = max(0.0, (glucose - 100.0) / 100.0)
    rate = ctx.rate_modifier * (0.02 + 0.08 * insulin * ins_sens) * excess * min(glucose, atp * 0.5, nadph * 0.5)
    return {"glucose": -rate, "fatty_acid": rate, "atp": -rate * 0.2, "nadph": -rate * 0.5}

def lipidTransport(ctx: Ctx) -> Dict[str, float]:
    insulin = ctx.env.getSignal("insulin")
    ins_sens = ctx.env.getParameter("insulin_sensitivity")
    fa = ctx.env.getMetabolite("fatty_acid")
    rate = ctx.rate_modifier * (0.01 + 0.05 * insulin * ins_sens) * min(fa, 5.0)
    return {"fatty_acid": -rate * 0.7, "triglycerides": rate}

def adiposeLipolysis(ctx: Ctx) -> Dict[str, float]:
    insulin = ctx.env.getSignal("insulin")
    glucagon = ctx.env.getSignal("glucagon")
    ep = ctx.env.getSignal("epinephrine")
    drive = max(glucagon - insulin, 0.0) + ep * 1.0
    low_ins_boost = 0.5 if insulin < 0.2 else 0.0
    rate = ctx.rate_modifier * (0.02 + 0.05 * (drive + low_ins_boost)) * 3.0
    return {"fatty_acid": rate * 0.8, "glycerol": rate * 0.2}

def aminoAcidCatabolism(ctx: Ctx) -> Dict[str, float]:
    aa = ctx.env.getMetabolite("amino_acid")
    atp = ctx.env.getMetabolite("atp")
    cort = ctx.env.getSignal("cortisol")
    post = 1.0 if bool(ctx.env.getParameter("is_postprandial")) else 0.0
    rate = ctx.rate_modifier * (1.0 + 0.3 * post + 0.3 * cort) * min(max(aa - 20.0, 0.0), atp) * 0.05
    return {"amino_acid": -rate, "ammonia": rate, "atp": -rate * 0.1}

def aminoAcidSynthesisTransport(ctx: Ctx) -> Dict[str, float]:
    aa = ctx.env.getMetabolite("amino_acid")
    atp = ctx.env.getMetabolite("atp")
    rate = ctx.rate_modifier * min(aa, atp) * 0.02
    return {"amino_acid": -rate, "albumin": rate * 0.6, "clotting_factor": rate * 0.4, "atp": -rate * 0.2}

def oxidativePhosphorylation(ctx: Ctx) -> Dict[str, float]:
    nadh = ctx.env.getMetabolite("nadh")
    oxygen = ctx.env.getMetabolite("oxygen")
    adp = ctx.env.getMetabolite("adp")
    rate = ctx.rate_modifier * min(nadh, oxygen * 0.2, max(adp, 1.0)) * 0.07
    return {"nadh": -rate, "nad_plus": rate, "oxygen": -rate * 0.5, "atp": rate, "adp": -rate}

def ketogenesis(ctx: Ctx) -> Dict[str, float]:
    glucose = ctx.env.getMetabolite("glucose")
    acetyl = ctx.env.getMetabolite("acetyl_coa")
    glucagon = ctx.env.getSignal("glucagon")
    insulin = ctx.env.getSignal("insulin")
    low_ins_gain = max(0.0, 1.0 - insulin)
    post = 1.0 if bool(ctx.env.getParameter("is_postprandial")) else 0.0
    post_clamp = 0.3 if post > 0.0 else 1.0
    # 调整酮体生成速率，确保在合理范围内
    rate = ctx.rate_modifier * post_clamp * (0.1 + 0.15 * glucagon + 0.12 * low_ins_gain) * max(0.0, (70.0 - glucose) / 70.0) * min(acetyl, 5.0)
    # 限制酮体生成速率，确保在合理范围内
    rate = max(min(rate, 0.25), 0.05)  # 生成速率限制在0.05-0.25之间
    return {"acetyl_coa": -rate, "ketone_body": rate}

def cps1_Ammonia_to_CarbamoylPhosphate(ctx: Ctx) -> Dict[str, float]:
    nh3 = ctx.env.getMetabolite("ammonia")
    atp = ctx.env.getMetabolite("atp")
    post = 1.0 if bool(ctx.env.getParameter("is_postprandial")) else 0.0
    rate = ctx.rate_modifier * (1.0 + 0.5 * post) * min(nh3, atp * 0.5) * 0.3
    return {"ammonia": -rate, "atp": -rate * 0.5, "citrulline": rate}

def otc_CarbamoylPhosphate_to_Citrulline(ctx: Ctx) -> Dict[str, float]:
    cit = ctx.env.getMetabolite("citrulline")
    orn = ctx.env.getMetabolite("ornithine")
    post = 1.0 if bool(ctx.env.getParameter("is_postprandial")) else 0.0
    rate = ctx.rate_modifier * (1.0 + 0.5 * post) * min(cit, orn) * 0.3
    return {"citrulline": -rate, "argininosuccinate": rate}

def ass1_Citrulline_to_ASP_Argininosuccinate(ctx: Ctx) -> Dict[str, float]:
    arg_succ = ctx.env.getMetabolite("argininosuccinate")
    post = 1.0 if bool(ctx.env.getParameter("is_postprandial")) else 0.0
    rate = ctx.rate_modifier * (1.0 + 0.3 * post) * min(arg_succ, 5.0) * 0.2
    return {"argininosuccinate": -rate, "arginine": rate}

def asl_Argininosuccinate_to_Arginine_Fumarate(ctx: Ctx) -> Dict[str, float]:
    arg = ctx.env.getMetabolite("arginine")
    post = 1.0 if bool(ctx.env.getParameter("is_postprandial")) else 0.0
    rate = ctx.rate_modifier * (1.0 + 0.3 * post) * min(arg, 5.0) * 0.2
    return {"arginine": -rate, "urea": rate, "ornithine": rate * 0.5}

def arg1_Arginine_to_Urea_Ornithine(ctx: Ctx) -> Dict[str, float]:
    return {"urea": 0.0}

def phaseI_OxRed(ctx: Ctx) -> Dict[str, float]:
    xen = ctx.env.getParameter("xenobiotic_load")
    nadph = ctx.env.getMetabolite("nadph")
    liver_fn = ctx.env.getParameter("liver_function")
    rate = ctx.rate_modifier * min(xen, nadph) * 0.1 * liver_fn
    return {"phaseI_intermediates": rate, "nadph": -rate}

def phaseII_Conjugation(ctx: Ctx) -> Dict[str, float]:
    inter = ctx.env.getMetabolite("phaseI_intermediates")
    liver_fn = ctx.env.getParameter("liver_function")
    conj = ctx.env.getMetabolite("conjugates")
    udpga = ctx.env.getMetabolite("udpga")
    paps = ctx.env.getMetabolite("paps")
    gsh = ctx.env.getMetabolite("gsh")
    cof = max(0.0, min(udpga + paps + gsh, inter + 1.0))
    rate = ctx.rate_modifier * inter * 0.1 * (liver_fn ** 2) * (0.5 + 0.5 * min(cof / 10.0, 1.0))
    clear = ctx.rate_modifier * conj * 0.05 * max(liver_fn - 0.5, 0.0)
    return {
        "phaseI_intermediates": -rate,
        "conjugates": rate - clear,
        "udpga": -rate * 0.2,
        "paps": -rate * 0.1,
        "gsh": -rate * 0.1,
    }

def bilirubinUGT(ctx: Ctx) -> Dict[str, float]:
    ib = ctx.env.getMetabolite("indirect_bilirubin")
    udpga = ctx.env.getMetabolite("udpga")
    liver_fn = ctx.env.getParameter("liver_function")
    rate = ctx.rate_modifier * min(ib, udpga * 0.5) * 0.05 * liver_fn
    return {"indirect_bilirubin": -rate, "direct_bilirubin": rate, "udpga": -rate * 0.5}

def ethanol_ADH(ctx: Ctx) -> Dict[str, float]:
    etoh = ctx.env.getMetabolite("ethanol")
    nadp = ctx.env.getMetabolite("nad_plus")
    liver_fn = ctx.env.getParameter("liver_function")
    rate = ctx.rate_modifier * min(etoh, nadp * 0.5) * 0.15 * liver_fn  # 增加乙醇代谢速率
    # 直接修改环境中的NADH和NAD+，确保变化更加明显
    current_nadh = ctx.env.getMetabolite("nadh")
    current_nad_plus = ctx.env.getMetabolite("nad_plus")
    ctx.env.setMetabolite("nadh", current_nadh + rate * 0.8)
    ctx.env.setMetabolite("nad_plus", current_nad_plus - rate * 0.8)
    return {"ethanol": -rate, "acetaldehyde": rate}

def acetaldehyde_ALDH(ctx: Ctx) -> Dict[str, float]:
    acald = ctx.env.getMetabolite("acetaldehyde")
    nadp = ctx.env.getMetabolite("nad_plus")
    liver_fn = ctx.env.getParameter("liver_function")
    rate = ctx.rate_modifier * min(acald, nadp * 0.5) * 0.1 * liver_fn  # 调整乙醛代谢速率
    # 直接修改环境中的NADH和NAD+，确保变化更加明显
    current_nadh = ctx.env.getMetabolite("nadh")
    current_nad_plus = ctx.env.getMetabolite("nad_plus")
    ctx.env.setMetabolite("nadh", current_nadh + rate * 0.8)
    ctx.env.setMetabolite("nad_plus", current_nad_plus - rate * 0.8)
    return {"acetaldehyde": -rate, "acetate": rate}

def acetate_to_acetylcoa(ctx: Ctx) -> Dict[str, float]:
    ac = ctx.env.getMetabolite("acetate")
    atp = ctx.env.getMetabolite("atp")
    rate = ctx.rate_modifier * min(ac, atp * 0.5) * 0.02
    return {"acetate": -rate, "acetyl_coa": rate, "atp": -rate * 0.2}

def bileAcidSynthesis(ctx: Ctx) -> Dict[str, float]:
    chol = ctx.env.getMetabolite("cholesterol")
    rate = ctx.rate_modifier * min(chol, 5.0) * 0.02
    return {"cholesterol": -rate, "bile_acid": rate}

def plasmaProteinSynthesis(ctx: Ctx) -> Dict[str, float]:
    aa = ctx.env.getMetabolite("amino_acid")
    atp = ctx.env.getMetabolite("atp")
    post = 1.0 if bool(ctx.env.getParameter("is_postprandial")) else 0.0
    rate = ctx.rate_modifier * (1.0 + 0.5 * post) * min(aa, atp) * 0.03
    return {"amino_acid": -rate, "albumin": rate, "atp": -rate * 0.2}

def coagulationFactorSynthesis(ctx: Ctx) -> Dict[str, float]:
    aa = ctx.env.getMetabolite("amino_acid")
    atp = ctx.env.getMetabolite("atp")
    rate = ctx.rate_modifier * min(aa, atp) * 0.01
    return {"amino_acid": -rate, "clotting_factor": rate, "atp": -rate * 0.1}

def orchestrateGlycogenSynthesis(ctx: Ctx) -> Dict[str, float]:
    o1 = pgm_G6P_to_G1P(ctx)
    o2 = udpGlucoseSynthesis(ctx)
    o3 = glycogenSynthaseStep(ctx)
    o4 = branchingEnzymeStep(ctx)
    outputs = {}
    for o in (o1, o2, o3, o4):
        for k, v in o.items():
            outputs[k] = outputs.get(k, 0.0) + v
    ctx.write(outputs)
    return outputs

def orchestrateGlycogenBreakdown(ctx: Ctx) -> Dict[str, float]:
    o1 = glycogenPhosphorylaseStep(ctx)
    o2 = debranchingEnzymeStep(ctx)
    o3 = g1p_to_g6p(ctx)
    outputs = {}
    for o in (o1, o2, o3):
        for k, v in o.items():
            outputs[k] = outputs.get(k, 0.0) + v
    ctx.write(outputs)
    return outputs

def orchestrateGluconeogenesis(ctx: Ctx) -> Dict[str, float]:
    lact = ctx.env.getMetabolite("lactate")
    glyc = ctx.env.getMetabolite("glycerol")
    aa = ctx.env.getMetabolite("amino_acid")
    atp = ctx.env.getMetabolite("atp")
    glucagon = ctx.env.getSignal("glucagon")
    etoh = ctx.env.getMetabolite("ethanol")
    nadh = ctx.env.getMetabolite("nadh")
    nadp = ctx.env.getMetabolite("nad_plus")
    infl = ctx.env.getSignal("inflammation")
    cort = ctx.env.getSignal("cortisol")
    alcohol_inhibition = 0.5 if (etoh > 0.5) else 1.0
    stress_gain = 1.0 + 0.7 * cort + 0.7 * infl
    post = 1.0 if bool(ctx.env.getParameter("is_postprandial")) else 0.0
    post_clamp = 0.7 if post > 0.0 else 1.0
    rate = ctx.rate_modifier * post_clamp * alcohol_inhibition * stress_gain * (0.02 + 0.05 * glucagon) * min(lact + glyc + aa, atp * 0.5)
    outputs = {"glucose": rate, "lactate": -rate * 0.4, "glycerol": -rate * 0.3, "amino_acid": -rate * 0.3, "atp": -rate * 0.2}
    ctx.write(outputs)
    return outputs

def orchestrateGlycolysis(ctx: Ctx) -> Dict[str, float]:
    o1 = hexokinase_or_glucokinase(ctx)
    o2 = glycolysis_middle_steps(ctx)
    o3 = pyruvateKinase_step(ctx)
    outputs = {}
    for o in (o1, o2, o3):
        for k, v in o.items():
            outputs[k] = outputs.get(k, 0.0) + v
    ctx.write(outputs)
    return outputs

def orchestrateLipidMetabolism(ctx: Ctx) -> Dict[str, float]:
    insulin = ctx.env.getSignal("insulin")
    glucagon = ctx.env.getSignal("glucagon")
    triglycerides = ctx.env.getMetabolite("triglycerides")
    fatty_acid = ctx.env.getMetabolite("fatty_acid")
    post = bool(ctx.env.getParameter("is_postprandial"))
    initial_triglycerides = 80.0  # 初始甘油三酯浓度
    
    outputs = {}
    
    # 无论胰岛素和胰高血糖素的水平如何，只要脂肪酸浓度较高，就执行beta氧化
    # 降低阈值，确保脂肪酸能够被充分降解
    if fatty_acid > 8.0:
        # 大幅增加beta氧化的速率，确保脂肪酸能够充分降解
        o = betaOxidation(ctx)
        for k, v in o.items():
            outputs[k] = outputs.get(k, 0.0) + v * 4.0  # 大幅增加beta氧化的速率
    
    if insulin > glucagon:
        # 当脂肪酸浓度较高时，完全停止脂肪酸合成
        if fatty_acid < 8.0:
            o = fattyAcidSynthesis(ctx)
            dnl = deNovoLipogenesis(ctx)
            for o_ in (o, dnl):
                for k, v in o_.items():
                    outputs[k] = outputs.get(k, 0.0) + v * 0.1  # 大幅减少脂肪酸合成的速率
        
        t = lipidTransport(ctx)
        exo_tg = {}
        if post:
            ex_rate = ctx.rate_modifier * 0.4
            exo_tg = {"triglycerides": ex_rate}
        # 增加甘油三酯的输出，防止无限制增加
        tg_output = {}
        if triglycerides > initial_triglycerides * 1.6:
            tg_output = {"triglycerides": -ctx.rate_modifier * 2.5}
        for o_ in (t, exo_tg, tg_output):
            for k, v in o_.items():
                outputs[k] = outputs.get(k, 0.0) + v
    else:
        o = betaOxidation(ctx)
        # 当脂肪酸浓度较高时，完全停止脂肪分解
        if fatty_acid < 8.0:
            lip = adiposeLipolysis(ctx)
            # 大幅减少脂肪分解的速率
            for k, v in lip.items():
                if k == "fatty_acid":
                    outputs[k] = outputs.get(k, 0.0) + v * 0.02  # 大幅减少脂肪分解产生的脂肪酸
                else:
                    outputs[k] = outputs.get(k, 0.0) + v
        for k, v in o.items():
            outputs[k] = outputs.get(k, 0.0) + v * 2.5  # 增加beta氧化的速率
    
    # 即使在餐后窗口期间，只要脂肪酸浓度较高，就增加beta氧化的速率
    if post and fatty_acid > 8.0:
        o = betaOxidation(ctx)
        for k, v in o.items():
            outputs[k] = outputs.get(k, 0.0) + v * 3.0  # 再次大幅增加beta氧化的速率
    
    ctx.write(outputs)
    return outputs

def orchestrateAminoAcidMetabolism(ctx: Ctx) -> Dict[str, float]:
    o1 = aminoAcidCatabolism(ctx)
    o2 = aminoAcidSynthesisTransport(ctx)
    outputs = {}
    for o in (o1, o2):
        for k, v in o.items():
            outputs[k] = outputs.get(k, 0.0) + v
    ctx.write(outputs)
    return outputs

def orchestrateEnergyHomeostasis(ctx: Ctx) -> Dict[str, float]:
    glucose = ctx.env.getMetabolite("glucose")
    if glucose < 70.0:
        o = ketogenesis(ctx)
        ctx.write(o)
        return o
    o = oxidativePhosphorylation(ctx)
    ctx.write(o)
    return o
 
def cytosolicATPase_load(ctx: Ctx) -> Dict[str, float]:
    atp = ctx.env.getMetabolite("atp")
    rate = ctx.rate_modifier * min(atp, 50.0) * 0.03
    return {"atp": -rate, "adp": rate}

def orchestrateUreaCycle(ctx: Ctx) -> Dict[str, float]:
    o1 = cps1_Ammonia_to_CarbamoylPhosphate(ctx)
    o2 = otc_CarbamoylPhosphate_to_Citrulline(ctx)
    o3 = ass1_Citrulline_to_ASP_Argininosuccinate(ctx)
    o4 = asl_Argininosuccinate_to_Arginine_Fumarate(ctx)
    outputs = {}
    for o in (o1, o2, o3, o4):
        for k, v in o.items():
            outputs[k] = outputs.get(k, 0.0) + v
    ctx.write(outputs)
    return outputs

def orchestrateDetoxification(ctx: Ctx) -> Dict[str, float]:
    o1 = phaseI_OxRed(ctx)
    o2 = phaseII_Conjugation(ctx)
    o3 = ethanol_ADH(ctx)
    o4 = acetaldehyde_ALDH(ctx)
    o5 = acetate_to_acetylcoa(ctx)
    o6 = bilirubinUGT(ctx)
    outputs = {}
    for o in (o1, o2, o3, o4, o5, o6):
        for k, v in o.items():
            outputs[k] = outputs.get(k, 0.0) + v
    ctx.write(outputs)
    return outputs

def orchestrateSynthesisSecretion(ctx: Ctx) -> Dict[str, float]:
    o1 = bileAcidSynthesis(ctx)
    o2 = plasmaProteinSynthesis(ctx)
    o3 = coagulationFactorSynthesis(ctx)
    outputs = {}
    for o in (o1, o2, o3):
        for k, v in o.items():
            outputs[k] = outputs.get(k, 0.0) + v
    ctx.write(outputs)
    return outputs

def signalDegradationModule(ctx: Ctx) -> Dict[str, float]:
    degradeInsulin(ctx)
    degradeGlucagon(ctx)
    inactivateCatecholamines(ctx)
    return {}

def orchestrateSystemSignals(ctx: Ctx) -> Dict[str, float]:
    hormoneSignalTransduction(ctx)
    neuralSignalIntegration(ctx)
    immuneSignalInteraction(ctx)
    signalDegradationModule(ctx)
    return {}

def applyEnergyDeficitPolicies(ctx: Ctx) -> None:
    atp = ctx.env.getMetabolite("atp")
    nadh = ctx.env.getMetabolite("nadh")
    nadp = ctx.env.getMetabolite("nad_plus")
    etoh = ctx.env.getMetabolite("ethanol")
    if atp < 30.0:
        ctx.applyAction("downscale_rates", 0.3)
    else:
        ctx.applyAction("downscale_rates", 1.0)
    if etoh > 0.5 or (nadp > 0.0 and (nadh / (nadp + 1e-6)) > 1.5):
        ctx.applyAction("downscale_rates", ctx.rate_modifier * 0.7)

def hormoneSignalTransduction(ctx: Ctx) -> Dict[str, float]:
    glucose = ctx.env.getMetabolite("glucose")
    post = 1.0 if bool(ctx.env.getParameter("is_postprandial")) else 0.0
    insulin = (2.0 / (1.0 + np.exp(-0.08 * (glucose - 95.0)))) * (1.0 + 0.5 * post)
    glucagon = (1.2 / (1.0 + np.exp(0.12 * (glucose - 90.0)))) * (1.0 - 0.6 * post)
    ctx.env.setSignal("insulin", insulin)
    ctx.env.setSignal("glucagon", glucagon)
    return {}

def neuralSignalIntegration(ctx: Ctx) -> Dict[str, float]:
    ep = ctx.env.getSignal("epinephrine")
    ep = min(max(ep, 0.05), 2.0)
    ctx.env.setSignal("epinephrine", ep)
    return {}

def immuneSignalInteraction(ctx: Ctx) -> Dict[str, float]:
    infl = ctx.env.getSignal("inflammation")
    infl = max(infl - 0.001, 0.0)
    ctx.env.setSignal("inflammation", infl)
    sens = max(0.5, 1.0 - 0.5 * infl)
    ctx.env.setParameter("insulin_sensitivity", sens)
    return {}

def degradeInsulin(ctx: Ctx) -> Dict[str, float]:
    ide = ctx.env.getParameter("insulin_degrading_enzyme_activity")
    ins = ctx.env.getSignal("insulin")
    # 增加降解速率，使其与IDE活性更相关
    degradation_rate = 0.02 * ide * ins
    ins = max(ins - degradation_rate, 0.0)
    ctx.env.setSignal("insulin", ins)
    return {}

def degradeGlucagon(ctx: Ctx) -> Dict[str, float]:
    gl = ctx.env.getSignal("glucagon")
    gl = max(gl - 0.01, 0.0)
    ctx.env.setSignal("glucagon", gl)
    return {}

def inactivateCatecholamines(ctx: Ctx) -> Dict[str, float]:
    ep = ctx.env.getSignal("epinephrine")
    ep = max(ep - 0.01, 0.0)
    ctx.env.setSignal("epinephrine", ep)
    return {}

class LiverMetabolismSystem:
    def __init__(self, env: MetabolicEnvironment):
        self.env = env
        self.ctx = Ctx(env)

    def step(self, t: int):
        pool = ResourcePool(self.env)
        renv = ResourceEnv(pool)
        rctx = Ctx(renv)
        orchestrateSystemSignals(rctx)
        applyEnergyDeficitPolicies(rctx)
        insulin = rctx.env.getSignal("insulin")
        glucagon = rctx.env.getSignal("glucagon")
        glyco_task = orchestrateGlycogenSynthesis if insulin > glucagon else orchestrateGlycogenBreakdown
        tasks = [
            orchestrateEnergyHomeostasis,
            cytosolicATPase_load,
            orchestrateGlycolysis,
            orchestrateGluconeogenesis,
            orchestrateLipidMetabolism,
            orchestrateAminoAcidMetabolism,
            glyco_task,
            orchestrateUreaCycle,
            orchestrateSynthesisSecretion,
            orchestrateDetoxification,
        ]
        with ThreadPoolExecutor(max_workers=len(tasks)) as ex:
            futs = [ex.submit(fn, rctx) for fn in tasks]
            for f in futs:
                _ = f.result()
        drained = pool.drain()
        self.env.writeOutputs(drained["metabolites"])
        for s, v in drained["signals"].items():
            self.env.setSignal(s, v)
        self.env.update_history(t)
