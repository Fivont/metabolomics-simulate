import simulate as sim
from typing import Dict, Any, Callable, List, Tuple
import pandas as pd


class TriggerCtx(sim.Ctx):
    def __init__(self, env: sim.MetabolicEnvironment):
        super().__init__(env)
        self.step_events: List[Dict[str, Any]] = []

    def record_event(self, name: str, status: str, detail: Dict[str, Any] = None) -> None:
        self.step_events.append({"name": name, "status": status, "detail": detail or {}})


def _glucose_stable(c: TriggerCtx) -> bool:
    g = c.env.getMetabolite("glucose")
    ins = c.env.getSignal("insulin")
    glg = c.env.getSignal("glucagon")
    return (85.0 <= g <= 110.0) and (abs(ins - glg) < 0.2)


def _glucose_severely_low(c: TriggerCtx) -> bool:
    return c.env.getMetabolite("glucose") < 65.0


def _reaction_list() -> List[Tuple[str, Callable[[TriggerCtx], Dict[str, float]], Callable[[TriggerCtx], bool]]]:
    return [
        ("hexokinase_or_glucokinase", sim.hexokinase_or_glucokinase, lambda c: min(c.env.getMetabolite("glucose"), c.env.getMetabolite("atp")) > 0.1),
        ("pgm_G6P_to_G1P", sim.pgm_G6P_to_G1P, lambda c: c.env.getMetabolite("glucose") > 1.0),
        ("udpGlucoseSynthesis", sim.udpGlucoseSynthesis, lambda c: c.env.getMetabolite("glucose") > 0.5 and c.env.getMetabolite("atp") > 0.5),
        ("glycogenSynthaseStep", sim.glycogenSynthaseStep, lambda c: (not _glucose_stable(c)) and c.env.getSignal("insulin") > c.env.getSignal("glucagon") and c.env.getMetabolite("glucose") > 1.0 and c.env.getMetabolite("atp") > 0.5),
        ("branchingEnzymeStep", sim.branchingEnzymeStep, lambda c: c.env.getMetabolite("glycogen") > 10.0),
        ("glycogenPhosphorylaseStep", sim.glycogenPhosphorylaseStep, lambda c: (not _glucose_stable(c)) and (c.env.getSignal("glucagon") > c.env.getSignal("insulin") or c.env.getSignal("epinephrine") > 0.1) and c.env.getMetabolite("glycogen") > 10.0),
        ("debranchingEnzymeStep", sim.debranchingEnzymeStep, lambda c: c.env.getMetabolite("glycogen") > 10.0),
        ("g1p_to_g6p", sim.g1p_to_g6p, lambda c: False),
        ("pepck_OAA_to_PEP", sim.pepck_OAA_to_PEP, lambda c: c.env.getMetabolite("atp") > 0.5),
        ("g6pase_G6P_to_Glucose", sim.g6pase_G6P_to_Glucose, lambda c: False),
        ("glycolysis_middle_steps", sim.glycolysis_middle_steps, lambda c: c.env.getMetabolite("glucose") > 1.0 and c.env.getMetabolite("nad_plus") > 0.5 and c.env.getMetabolite("adp") > 0.5),
        ("pyruvateKinase_step", sim.pyruvateKinase_step, lambda c: False),
        ("fattyAcidSynthesis", sim.fattyAcidSynthesis, lambda c: c.env.getSignal("insulin") > c.env.getSignal("glucagon") and c.env.getMetabolite("acetyl_coa") > 1.0 and c.env.getMetabolite("nadph") > 0.5 and c.env.getMetabolite("atp") > 0.5),
        ("betaOxidation", sim.betaOxidation, lambda c: _glucose_severely_low(c) and c.env.getMetabolite("fatty_acid") > 5.0 and c.env.getMetabolite("nad_plus") > 1.0),
        ("deNovoLipogenesis", sim.deNovoLipogenesis, lambda c: c.env.getMetabolite("glucose") > 100.0 and c.env.getSignal("insulin") >= c.env.getSignal("glucagon")),
        ("lipidTransport", sim.lipidTransport, lambda c: c.env.getSignal("insulin") > c.env.getSignal("glucagon") and c.env.getMetabolite("fatty_acid") > 1.0),
        ("adiposeLipolysis", sim.adiposeLipolysis, lambda c: c.env.getSignal("glucagon") > c.env.getSignal("insulin") or c.env.getSignal("epinephrine") > 0.2),
        ("aminoAcidCatabolism", sim.aminoAcidCatabolism, lambda c: c.env.getMetabolite("amino_acid") > 20.0 and c.env.getMetabolite("atp") > 0.5),
        ("aminoAcidSynthesisTransport", sim.aminoAcidSynthesisTransport, lambda c: c.env.getMetabolite("amino_acid") > 10.0 and c.env.getMetabolite("atp") > 0.5),
        ("oxidativePhosphorylation", sim.oxidativePhosphorylation, lambda c: c.env.getMetabolite("nadh") > 0.5 and c.env.getMetabolite("oxygen") > 10.0 and c.env.getMetabolite("adp") >= 1.0),
        ("ketogenesis", sim.ketogenesis, lambda c: c.env.getMetabolite("glucose") < 70.0 and c.env.getSignal("glucagon") >= c.env.getSignal("insulin")),
        ("cps1_Ammonia_to_CarbamoylPhosphate", sim.cps1_Ammonia_to_CarbamoylPhosphate, lambda c: c.env.getMetabolite("ammonia") > 0.5 and c.env.getMetabolite("atp") > 0.5),
        ("otc_CarbamoylPhosphate_to_Citrulline", sim.otc_CarbamoylPhosphate_to_Citrulline, lambda c: c.env.getMetabolite("citrulline") > 0.0 and c.env.getMetabolite("ornithine") > 0.0),
        ("ass1_Citrulline_to_ASP_Argininosuccinate", sim.ass1_Citrulline_to_ASP_Argininosuccinate, lambda c: c.env.getMetabolite("argininosuccinate") > 0.1),
        ("asl_Argininosuccinate_to_Arginine_Fumarate", sim.asl_Argininosuccinate_to_Arginine_Fumarate, lambda c: c.env.getMetabolite("arginine") > 0.1),
        ("arg1_Arginine_to_Urea_Ornithine", sim.arg1_Arginine_to_Urea_Ornithine, lambda c: c.env.getMetabolite("arginine") > 0.1),
        ("phaseI_OxRed", sim.phaseI_OxRed, lambda c: c.env.getParameter("xenobiotic_load") > 0.1 and c.env.getMetabolite("nadph") > 0.5 and c.env.getParameter("liver_function") > 0.2),
        ("phaseII_Conjugation", sim.phaseII_Conjugation, lambda c: c.env.getMetabolite("phaseI_intermediates") > 0.1 and c.env.getParameter("liver_function") > 0.2 and (c.env.getMetabolite("udpga") > 1.0 or c.env.getMetabolite("paps") > 1.0 or c.env.getMetabolite("gsh") > 1.0)),
        ("bilirubinUGT", sim.bilirubinUGT, lambda c: c.env.getMetabolite("indirect_bilirubin") > 0.1 and c.env.getMetabolite("udpga") > 0.5 and c.env.getParameter("liver_function") > 0.2),
        ("ethanol_ADH", sim.ethanol_ADH, lambda c: c.env.getMetabolite("ethanol") > 0.1 and c.env.getMetabolite("nad_plus") > 0.5 and c.env.getParameter("liver_function") > 0.2),
        ("acetaldehyde_ALDH", sim.acetaldehyde_ALDH, lambda c: c.env.getMetabolite("acetaldehyde") > 0.1 and c.env.getMetabolite("nad_plus") > 0.5 and c.env.getParameter("liver_function") > 0.2),
        ("acetate_to_acetylcoa", sim.acetate_to_acetylcoa, lambda c: c.env.getMetabolite("acetate") > 0.1 and c.env.getMetabolite("atp") > 0.5),
        ("bileAcidSynthesis", sim.bileAcidSynthesis, lambda c: c.env.getMetabolite("cholesterol") > 1.0),
        ("plasmaProteinSynthesis", sim.plasmaProteinSynthesis, lambda c: c.env.getMetabolite("amino_acid") > 10.0 and c.env.getMetabolite("atp") > 0.5),
        ("coagulationFactorSynthesis", sim.coagulationFactorSynthesis, lambda c: c.env.getMetabolite("amino_acid") > 10.0 and c.env.getMetabolite("atp") > 0.5),
        ("cytosolicATPase_load", sim.cytosolicATPase_load, lambda c: c.env.getMetabolite("atp") > 1.0),
    ]


class LiverMetabolismSystemTrigger:
    def __init__(self, env: sim.MetabolicEnvironment):
        self.env = env
        self.ctx = TriggerCtx(env)
        self.events_history: List[Dict[str, Any]] = []

    def step(self, t: int):
        self.ctx.step_events = []
        sim.orchestrateSystemSignals(self.ctx)
        sim.applyEnergyDeficitPolicies(self.ctx)
        reactions = _reaction_list()
        outputs: Dict[str, float] = {}
        for name, fn, pred in reactions:
            ok = bool(pred(self.ctx))
            if ok:
                res = fn(self.ctx)
                for k, v in res.items():
                    outputs[k] = outputs.get(k, 0.0) + float(v)
                self.ctx.record_event(name, "triggered", {})
            else:
                self.ctx.record_event(name, "stopped", {})
        self.env.writeOutputs(outputs)
        self.events_history.append({"time": t, "events": list(self.ctx.step_events)})
        self.env.update_history(t)


def run_with_trigger(env: sim.MetabolicEnvironment, minutes: int, inject: Callable[[sim.MetabolicEnvironment, int], None] = None) -> Tuple[pd.DataFrame, List[Dict[str, Any]]]:
    sys = LiverMetabolismSystemTrigger(env)
    for tt in range(minutes):
        hour = tt / 60.0
        if inject:
            inject(env, tt)
        sys.step(hour)
    df = pd.DataFrame(env.history)
    return df, sys.events_history
