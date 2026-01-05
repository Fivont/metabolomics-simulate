# 失败测试用例原因与修复方法（基于 test_result.json）

- 数据来源：modules/code/test_result.json（需求映射均为失败）
- 代码参考：核心模拟实现在 [requirements_impl.py](file:///home/yifei/AI4Science/metabolomics/simulate/modules/code/requirements_impl.py)；测试定义在 [tests.py](file:///home/yifei/AI4Science/metabolomics/simulate/modules/code/tests.py)

## TC-SLEEP-FASTING-01
- 失败原因
  - 空腹状态下的脂肪动员未实现，脂肪酸未上升，酮体上升不足
  - 胰岛素/胰高糖素调制过于平缓，未明显体现“胰岛素低、胰高糖素高”
- 修复方法
  - 在脂代谢编排中引入“低胰岛素/高胰高糖素时脂肪动员”将脂肪酸、甘油输入肝脏池（建议新增 adiposeLipolysis）
    - 参考位置： [orchestrateLipidMetabolism](file:///home/yifei/AI4Science/metabolomics/simulate/modules/code/requirements_impl.py#L323-L339)
  - 强化空腹时的激素响应曲线，提高胰高糖素、降低胰岛素
    - 参考位置： [hormoneSignalTransduction](file:///home/yifei/AI4Science/metabolomics/simulate/modules/code/requirements_impl.py#L411-L417)

## TC-POSTPRANDIAL-HIGHCARB-01
- 失败原因
  - 高碳餐后甘油三酯未显著增加，缺少高胰岛素驱动的葡萄糖→脂肪酸（新生脂肪生成）路径
- 修复方法
  - 在脂肪酸合成中加入对高葡萄糖的依赖或新增 deNovoLipogenesis，将葡萄糖在胰岛素高时部分转为脂肪酸，再经脂质运输生成甘油三酯
    - 参考位置： [fattyAcidSynthesis](file:///home/yifei/AI4Science/metabolomics/simulate/modules/code/requirements_impl.py#L168-L175)、[lipidTransport](file:///home/yifei/AI4Science/metabolomics/simulate/modules/code/requirements_impl.py#L187-L191)

## TC-EXERCISE-HIGH-INTENSITY-01
- 失败原因
  - 糖原分解速率低，未体现“快速下降”
  - 脂肪酸在模型中被β氧化消耗，未体现运动时外周动员导致“脂肪酸上升”的血液侧效应
- 修复方法
  - 提高肾上腺素高时的 [glycogenPhosphorylaseStep](file:///home/yifei/AI4Science/metabolomics/simulate/modules/code/requirements_impl.py#L135-L140) 速率系数
  - 在高肾上腺素时引入外周脂肪动员输入通道（如 adiposeLipolysis），而非仅加速β氧化

## TC-STARVATION-KETOSIS-01
- 失败原因
  - 长期饥饿下脂肪酸未持续上升，酮生成受限
- 修复方法
  - 空腹/长期饥饿时增加脂肪动员输入；适度提高 [ketogenesis](file:///home/yifei/AI4Science/metabolomics/simulate/modules/code/requirements_impl.py#L212-L217) 速率或降低触发阈值

## TC-HYPOXIA-01
- 失败原因
  - 低氧时乳酸上升、ATP下降、NADH积累不显著，氧化磷酸化抑制不够
- 修复方法
  - 降低 [oxidativePhosphorylation](file:///home/yifei/AI4Science/metabolomics/simulate/modules/code/requirements_impl.py#L205-L210) 对氧的有效速率系数；在低氧下提高 [glycolysis_middle_steps](file:///home/yifei/AI4Science/metabolomics/simulate/modules/code/requirements_impl.py#L158-L164) 产乳酸比例

## TC-INFLAMMATION-ACUTE-01
- 失败原因
  - 炎症信号未与糖异生/胰岛素敏感性联动，无法体现应激性高血糖与胰岛素敏感性下降
- 修复方法
  - 在 [immuneSignalInteraction](file:///home/yifei/AI4Science/metabolomics/simulate/modules/code/requirements_impl.py#L425-L429) 引入炎症驱动：提高 [orchestrateGluconeogenesis](file:///home/yifei/AI4Science/metabolomics/simulate/modules/code/requirements_impl.py#L297-L310) 速率、降低胰岛素作用（新增 insulin_sensitivity 参数）

## TC-HIGH-PROTEIN-DIET-01
- 失败原因
  - 尿素生成不足（尿素循环通量偏低）
- 修复方法
  - 提高 [cps1_Ammonia_to_CarbamoylPhosphate](file:///home/yifei/AI4Science/metabolomics/simulate/modules/code/requirements_impl.py#L219-L224) 与后续酶步骤的速率系数，或在高氨基酸时提高 ATP 供给

## TC-HIGH-FAT-MEAL-01
- 失败原因
  - 脂肪酸注入后被快速转为甘油三酯导致“脂肪酸上升”不明显
- 修复方法
  - 调整 [lipidTransport](file:///home/yifei/AI4Science/metabolomics/simulate/modules/code/requirements_impl.py#L187-L191) 比例，保留部分脂肪酸在血/肝池中；或引入外源餐后乳糜微粒对甘油三酯的直接输入

## TC-INSULIN-RESISTANCE-01
- 失败原因
  - 未实现胰岛素敏感性降低的通用参数，导致胰岛素驱动的合成仍然偏强
- 修复方法
  - 新增 insulin_sensitivity 参数，衰减胰岛素在 [glycogenSynthaseStep](file:///home/yifei/AI4Science/metabolomics/simulate/modules/code/requirements_impl.py#L123-L129)、[fattyAcidSynthesis](file:///home/yifei/AI4Science/metabolomics/simulate/modules/code/requirements_impl.py#L168-L175) 等路径的增益

## TC-CORTISOL-CHRONIC-01
- 失败原因
  - 未实现皮质醇对糖异生增强与蛋白质分解的作用
- 修复方法
  - 在 [orchestrateGluconeogenesis](file:///home/yifei/AI4Science/metabolomics/simulate/modules/code/requirements_impl.py#L297-L310) 增加 cortisol 增益；在 [aminoAcidCatabolism](file:///home/yifei/AI4Science/metabolomics/simulate/modules/code/requirements_impl.py#L193-L198) 提高通量

## TC-DKA-01
- 失败原因
-  胰岛素极低/胰高糖素很高时未充分动员脂肪酸与酮生成
- 修复方法
  - 结合 TC-SLEEP-FASTING-01 的动员改造；提高 [ketogenesis](file:///home/yifei/AI4Science/metabolomics/simulate/modules/code/requirements_impl.py#L212-L217) 在极端胰岛素低时的权重

## TC-REFEEDING-AFTER-FAST-01
- 失败原因
  - 进食后糖原补充不足，酮体下降不明显
- 修复方法
  - 在高胰岛素时提高 [glycogenSynthaseStep](file:///home/yifei/AI4Science/metabolomics/simulate/modules/code/requirements_impl.py#L123-L129)；进食后降低 [ketogenesis](file:///home/yifei/AI4Science/metabolomics/simulate/modules/code/requirements_impl.py#L212-L217) 触发

## TC-INSULIN-DEGRADATION-IMPAIRED-01
- 失败原因
  - 胰岛素降解抑制效果不足，平均胰岛素值未显著升高
- 修复方法
  - 调整 [degradeInsulin](file:///home/yifei/AI4Science/metabolomics/simulate/modules/code/requirements_impl.py#L431-L436) 衰减系数；在 [hormoneSignalTransduction](file:///home/yifei/AI4Science/metabolomics/simulate/modules/code/requirements_impl.py#L411-L417) 中提高高血糖时的上限

## TC-LIVER-DETOX-INSUFFICIENCY-01
- 失败原因
  - 低肝功能时第二相结合仍有一定增长，未体现“结合物下降”
- 修复方法
  - 在 [phaseII_Conjugation](file:///home/yifei/AI4Science/metabolomics/simulate/modules/code/requirements_impl.py#L250-L254) 对 liver_function 采用非线性抑制（平方/阈值截断）；加入结合物的清除项

## TC-BASELINE-ENV-01
- 失败原因
  - 多线程并行后通量合并导致轻微漂移，稳定性受影响
- 修复方法
  - 降低默认速率系数；仅在明确触发时提高通量；校准合并策略（必要时改为每路径归一化写入）

## TC-MIXED-MEAL-01
- 失败原因
  - 部分指标（如尿素轻微增加）可能不稳定
- 修复方法
  - 在餐后短时提高氨基酸代谢与尿素循环通量；同时保持胰岛素高、胰高糖素低的抑制关系

---

## 汇总修复优先级
- 高优先：脂肪动员通道（adiposeLipolysis）、胰岛素敏感性参数、炎症/皮质醇对糖异生与敏感性的调控
- 中优先：低氧下的乳酸/ATP/NADH调参、尿素循环加速、Phase II 非线性抑制与结合物清除
- 低优先：餐后新生脂肪生成、混合餐细调、并行合并的稳定性校准
 
---

## 最新失败用例与修复计划（基于 test_result.jsonl）
- 数据来源：modules/code/test_result.jsonl
- 失败用例概览：TC-SLEEP-FASTING-01、TC-POSTPRANDIAL-HIGHCARB-01、TC-EXERCISE-HIGH-INTENSITY-01、TC-HYPOXIA-01、TC-INFLAMMATION-ACUTE-01、TC-HIGH-PROTEIN-DIET-01、TC-HIGH-FAT-MEAL-01、TC-INSULIN-RESISTANCE-01、TC-CORTISOL-CHRONIC-01、TC-DKA-01、TC-REFEEDING-AFTER-FAST-01、TC-INSULIN-DEGRADATION-IMPAIRED-01、TC-LIVER-DETOX-INSUFFICIENCY-01、TC-BASELINE-ENV-01、TC-MIXED-MEAL-01
- 已通过用例：TC-STARVATION-KETOSIS-01、TC-COAGULATION-UPREG-01、TC-AMMONIA-SPIKE-01、TC-MULTI-SIGNAL-INTEGRATION-01、TC-PFK1-REGULATION-01、TC-GLYCOGEN-BRANCHING-THRESH-01

### 目标性修复摘要
- 空腹/运动：增强脂肪动员与肾上腺素响应（[adiposeLipolysis](file:///home/yifei/AI4Science/metabolomics/simulate/modules/code/requirements_impl.py#L248-L255)、[glycogenPhosphorylaseStep](file:///home/yifei/AI4Science/metabolomics/simulate/modules/code/requirements_impl.py#L190-L195)）
- 餐后高碳：提高新生脂肪生成与外源 TG 输入（[deNovoLipogenesis](file:///home/yifei/AI4Science/metabolomics/simulate/modules/code/requirements_impl.py#L241-L247)、[orchestrateLipidMetabolism](file:///home/yifei/AI4Science/metabolomics/simulate/modules/code/requirements_impl.py#L395-L411)）
- 低氧：提高乳酸比例，下降氧化磷酸化（[glycolysis_middle_steps](file:///home/yifei/AI4Science/metabolomics/simulate/modules/code/requirements_impl.py#L213-L219)、[oxidativePhosphorylation](file:///home/yifei/AI4Science/metabolomics/simulate/modules/code/requirements_impl.py#L260-L265)）
- 炎症/皮质醇：提升糖异生应激增益并在餐后抑制（[orchestrateGluconeogenesis](file:///home/yifei/AI4Science/metabolomics/simulate/modules/code/requirements_impl.py#L369-L382)、[immuneSignalInteraction](file:///home/yifei/AI4Science/metabolomics/simulate/modules/code/requirements_impl.py#L508-L513)）
- 高蛋白/尿素：上调 CPS1/OTC 等速率（[cps1](file:///home/yifei/AI4Science/metabolomics/simulate/modules/code/requirements_impl.py#L274-L279)、[otc](file:///home/yifei/AI4Science/metabolomics/simulate/modules/code/requirements_impl.py#L280-L285)）
- 高脂餐：提高脂质转运保留并增加餐后 TG 外源输入（[lipidTransport](file:///home/yifei/AI4Science/metabolomics/simulate/modules/code/requirements_impl.py#L242-L247)、[orchestrateLipidMetabolism](file:///home/yifei/AI4Science/metabolomics/simulate/modules/code/requirements_impl.py#L395-L411)）
- 胰岛素抵抗：将敏感性作用扩展至糖酵解与 DNL（[hexokinase_or_glucokinase](file:///home/yifei/AI4Science/metabolomics/simulate/modules/code/requirements_impl.py#L159-L166)、[deNovoLipogenesis](file:///home/yifei/AI4Science/metabolomics/simulate/modules/code/requirements_impl.py#L241-L247)）
- DKA/再喂养：极低胰素下动员与酮生成增强，餐后对酮生成抑制（[adiposeLipolysis](file:///home/yifei/AI4Science/metabolomics/simulate/modules/code/requirements_impl.py#L248-L255)、[ketogenesis](file:///home/yifei/AI4Science/metabolomics/simulate/modules/code/requirements_impl.py#L267-L272)）
- 胰岛素降解受损：提升胰素上限与 IDE 差异效应（[hormoneSignalTransduction](file:///home/yifei/AI4Science/metabolomics/simulate/modules/code/requirements_impl.py#L494-L500)、[degradeInsulin](file:///home/yifei/AI4Science/metabolomics/simulate/modules/code/requirements_impl.py#L514-L519)）
- 肝解毒不足：Phase I 与乙醇代谢受肝功能抑制（[phaseI_OxRed](file:///home/yifei/AI4Science/metabolomics/simulate/modules/code/requirements_impl.py#L299-L304)、[ethanol_ADH](file:///home/yifei/AI4Science/metabolomics/simulate/modules/code/requirements_impl.py#L311-L315)、[acetaldehyde_ALDH](file:///home/yifei/AI4Science/metabolomics/simulate/modules/code/requirements_impl.py#L317-L321)）
