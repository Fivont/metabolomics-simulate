# 模拟接口：生物反应函数说明

本文件登记 modules/code/simulate.py 中代表生物反应（含代谢、转运、合成、解毒及信号过程）的函数，提供自然语言名称、功能简述与主要规则。每项均附源码位置以便跳转。

## 代谢反应与转运

- 名称: 葡萄糖磷酸化（己糖激酶/葡萄糖激酶）
  - 源函数: [hexokinase_or_glucokinase](file:///home/yifei/AI4Science/metabolomics/simulate/modules/code/simulate.py#L166-L174)
  - 简述: 胰岛素与敏感性调节的葡萄糖利用与ATP消耗的起始步。
  - 规则: 速率随胰岛素×敏感性与底物最小值增大；消耗少量ATP。

- 名称: G6P→G1P 变位（PGM）
  - 源函数: [pgm_G6P_to_G1P](file:///home/yifei/AI4Science/metabolomics/simulate/modules/code/simulate.py#L176-L179)
  - 简述: 将葡萄糖-6-磷酸转为葡萄糖-1-磷酸，为糖原合成做准备。
  - 规则: 受可用葡萄糖上限约束，按比例转化。

- 名称: UDP-葡萄糖合成
  - 源函数: [udpGlucoseSynthesis](file:///home/yifei/AI4Science/metabolomics/simulate/modules/code/simulate.py#L180-L185)
  - 简述: 生成UDP-葡萄糖，伴随ATP消耗。
  - 规则: 受葡萄糖与ATP共同限制，低比例消耗ATP。

- 名称: 糖原合成酶反应
  - 源函数: [glycogenSynthaseStep](file:///home/yifei/AI4Science/metabolomics/simulate/modules/code/simulate.py#L186-L193)
  - 简述: 在胰岛素信号驱动下合成糖原。
  - 规则: 速率与胰岛素×敏感性相关；消耗少量ATP并生成等量ADP。

- 名称: 糖原分支酶反应
  - 源函数: [branchingEnzymeStep](file:///home/yifei/AI4Science/metabolomics/simulate/modules/code/simulate.py#L194-L197)
  - 简述: 增加糖原分支结构的步骤。
  - 规则: 受糖原水平与速率修饰限制，影响较小。

- 名称: 糖原磷酸化酶反应
  - 源函数: [glycogenPhosphorylaseStep](file:///home/yifei/AI4Science/metabolomics/simulate/modules/code/simulate.py#L199-L205)
  - 简述: 在胰高血糖素/肾上腺素作用下分解糖原并释放葡萄糖。
  - 规则: 速率与胰高血糖素、肾上腺素水平成正相关。

- 名称: 去分支酶反应
  - 源函数: [debranchingEnzymeStep](file:///home/yifei/AI4Science/metabolomics/simulate/modules/code/simulate.py#L206-L210)
  - 简述: 去除糖原分支并产生少量葡萄糖。
  - 规则: 受糖原水平与速率修饰限制。

- 名称: G1P→G6P 转化
  - 源函数: [g1p_to_g6p](file:///home/yifei/AI4Science/metabolomics/simulate/modules/code/simulate.py#L211-L213)
  - 简述: 将G1P转回G6P的占位转换。
  - 规则: 当前实现不改变代谢物总量。

- 名称: PEPCK 草酰乙酸→PEP
  - 源函数: [pepck_OAA_to_PEP](file:///home/yifei/AI4Science/metabolomics/simulate/modules/code/simulate.py#L214-L218)
  - 简述: 糖异生关键步，ATP参与的羧基转移与脱羧。
  - 规则: 受ATP水平与速率修饰限制，消耗ATP。

- 名称: G6P酶生成葡萄糖
  - 源函数: [g6pase_G6P_to_Glucose](file:///home/yifei/AI4Science/metabolomics/simulate/modules/code/simulate.py#L219-L221)
  - 简述: 糖异生/糖原分解末端释放葡萄糖。
  - 规则: 当前实现为占位，不变更量。

- 名称: 糖酵解中间步
  - 源函数: [glycolysis_middle_steps](file:///home/yifei/AI4Science/metabolomics/simulate/modules/code/simulate.py#L222-L230)
  - 简述: 耦合NAD+/ADP的糖酵解主干，部分流向乳酸。
  - 规则: 受葡萄糖、NAD+、ADP限制；低氧时乳酸比例上升。

- 名称: 丙酮酸激酶反应
  - 源函数: [pyruvateKinase_step](file:///home/yifei/AI4Science/metabolomics/simulate/modules/code/simulate.py#L231-L233)
  - 简述: PEP→丙酮酸与ATP生成的末端步。
  - 规则: 当前实现为占位。

- 名称: 脂肪酸合成
  - 源函数: [fattyAcidSynthesis](file:///home/yifei/AI4Science/metabolomics/simulate/modules/code/simulate.py#L234-L242)
  - 简述: 胰岛素驱动下以乙酰-CoA与NADPH生成脂肪酸。
  - 规则: 受胰岛素×敏感性与底物限制；消耗NADPH与ATP。

- 名称: 脂肪酸β-氧化
  - 源函数: [betaOxidation](file:///home/yifei/AI4Science/metabolomics/simulate/modules/code/simulate.py#L243-L259)
  - 简述: 脂肪酸分解为乙酰-CoA并生成NADH、ATP。
  - 规则: 受胰高血糖素/肾上腺素促进；酒精抑制；高脂肪酸时提高速率。

- 名称: 新生脂肪生成（DNL）
  - 源函数: [deNovoLipogenesis](file:///home/yifei/AI4Science/metabolomics/simulate/modules/code/simulate.py#L260-L269)
  - 简述: 高糖时将葡萄糖转化为脂肪酸。
  - 规则: 受胰岛素×敏感性及“过量葡萄糖”驱动；消耗ATP与NADPH。

- 名称: 脂质转运/装载
  - 源函数: [lipidTransport](file:///home/yifei/AI4Science/metabolomics/simulate/modules/code/simulate.py#L270-L276)
  - 简述: 将脂肪酸转为三酯并输出。
  - 规则: 胰岛素×敏感性促进；受脂肪酸可用量限制。

- 名称: 脂肪组织脂解
  - 源函数: [adiposeLipolysis](file:///home/yifei/AI4Science/metabolomics/simulate/modules/code/simulate.py#L277-L285)
  - 简述: 释放脂肪酸与甘油。
  - 规则: 胰高血糖素/肾上腺素增强；低胰岛素时额外提升。

- 名称: 氨基酸分解
  - 源函数: [aminoAcidCatabolism](file:///home/yifei/AI4Science/metabolomics/simulate/modules/code/simulate.py#L286-L293)
  - 简述: 生成氨与消耗ATP。
  - 规则: 受进食状态与皮质醇影响；底物与ATP限制。

- 名称: 氨基酸合成与转运（蛋白）
  - 源函数: [aminoAcidSynthesisTransport](file:///home/yifei/AI4Science/metabolomics/simulate/modules/code/simulate.py#L294-L299)
  - 简述: 合成白蛋白与凝血因子。
  - 规则: 受氨基酸与ATP双底物限制；按比例分配产物。

- 名称: 氧化磷酸化
  - 源函数: [oxidativePhosphorylation](file:///home/yifei/AI4Science/metabolomics/simulate/modules/code/simulate.py#L300-L306)
  - 简述: NADH与氧驱动ATP生成。
  - 规则: 受NADH、氧与ADP限制；NADH→NAD+，ATP↑ADP↓。

- 名称: 酮体生成
  - 源函数: [ketogenesis](file:///home/yifei/AI4Science/metabolomics/simulate/modules/code/simulate.py#L307-L320)
  - 简述: 低糖/高胰高血糖素时由乙酰-CoA生成酮体。
  - 规则: 进食状态限制；胰岛素低时增强；速率加以上下限约束。

- 名称: CPS1 氨→氨甲酰磷酸
  - 源函数: [cps1_Ammonia_to_CarbamoylPhosphate](file:///home/yifei/AI4Science/metabolomics/simulate/modules/code/simulate.py#L321-L327)
  - 简述: 尿素循环起始步，消耗ATP生成瓜氨酸前体。
  - 规则: 进食状态提升；受氨与ATP限制。

- 名称: OTC 合成瓜氨酸
  - 源函数: [otc_CarbamoylPhosphate_to_Citrulline](file:///home/yifei/AI4Science/metabolomics/simulate/modules/code/simulate.py#L328-L334)
  - 简述: 由氨甲酰磷酸与鸟氨酸生成瓜氨酸。
  - 规则: 受底物最小值限制；进食状态提升。

- 名称: ASS1 生成精氨酸代琥珀酸
  - 源函数: [ass1_Citrulline_to_ASP_Argininosuccinate](file:///home/yifei/AI4Science/metabolomics/simulate/modules/code/simulate.py#L335-L340)
  - 简述: 尿素循环中间步。
  - 规则: 受底物与进食状态限制。

- 名称: ASL 生成精氨酸与延胡索酸
  - 源函数: [asl_Argininosuccinate_to_Arginine_Fumarate](file:///home/yifei/AI4Science/metabolomics/simulate/modules/code/simulate.py#L341-L346)
  - 简述: 尿素循环后段，生成尿素前体与再生鸟氨酸。
  - 规则: 受底物与进食状态限制；副产物比例固定。

- 名称: ARG1 精氨酸→尿素/鸟氨酸
  - 源函数: [arg1_Arginine_to_Urea_Ornithine](file:///home/yifei/AI4Science/metabolomics/simulate/modules/code/simulate.py#L347-L349)
  - 简述: 尿素循环末端步（占位）。
  - 规则: 当前实现不改变量。

- 名称: Ⅰ相氧化还原（药物代谢）
  - 源函数: [phaseI_OxRed](file:///home/yifei/AI4Science/metabolomics/simulate/modules/code/simulate.py#L350-L355)
  - 简述: 依赖NADPH与肝功能将外源物氧化为中间体。
  - 规则: 受外源负荷、NADPH、肝功能限制。

- 名称: Ⅱ相结合反应
  - 源函数: [phaseII_Conjugation](file:///home/yifei/AI4Science/metabolomics/simulate/modules/code/simulate.py#L357-L373)
  - 简述: 使用UDPGA/PAPS/GSH与肝功能完成结合与清除。
  - 规则: 受中间体与辅基可用性、肝功能平方项影响；持续清除积累的结合物。

- 名称: 胆红素葡糖醛酸化（UGT）
  - 源函数: [bilirubinUGT](file:///home/yifei/AI4Science/metabolomics/simulate/modules/code/simulate.py#L375-L381)
  - 简述: 将间接胆红素转为直接胆红素，消耗UDPGA。
  - 规则: 受底物与肝功能限制。

- 名称: 酒精脱氢酶（ADH）
  - 源函数: [ethanol_ADH](file:///home/yifei/AI4Science/metabolomics/simulate/modules/code/simulate.py#L382-L393)
  - 简述: 乙醇→乙醛并驱动NAD+→NADH。
  - 规则: 受乙醇、NAD+与肝功能限制；直接调整NADH/NAD+。

- 名称: 醛脱氢酶（ALDH）
  - 源函数: [acetaldehyde_ALDH](file:///home/yifei/AI4Science/metabolomics/simulate/modules/code/simulate.py#L394-L405)
  - 简述: 乙醛→乙酸并驱动NAD+→NADH。
  - 规则: 受乙醛、NAD+与肝功能限制；直接调整NADH/NAD+。

- 名称: 乙酸→乙酰-CoA 合成
  - 源函数: [acetate_to_acetylcoa](file:///home/yifei/AI4Science/metabolomics/simulate/modules/code/simulate.py#L406-L411)
  - 简述: 乙酸活化生成乙酰-CoA，消耗ATP。
  - 规则: 受乙酸与ATP限制。

- 名称: 胆汁酸合成
  - 源函数: [bileAcidSynthesis](file:///home/yifei/AI4Science/metabolomics/simulate/modules/code/simulate.py#L412-L415)
  - 简述: 由胆固醇生成胆汁酸。
  - 规则: 受胆固醇与速率修饰限制。

- 名称: 血浆蛋白合成
  - 源函数: [plasmaProteinSynthesis](file:///home/yifei/AI4Science/metabolomics/simulate/modules/code/simulate.py#L417-L423)
  - 简述: 以氨基酸与ATP合成白蛋白。
  - 规则: 进食状态提升；双底物限制。

- 名称: 凝血因子合成
  - 源函数: [coagulationFactorSynthesis](file:///home/yifei/AI4Science/metabolomics/simulate/modules/code/simulate.py#L424-L429)
  - 简述: 以氨基酸与ATP生成凝血因子。
  - 规则: 双底物限制；ATP消耗较低。

- 名称: 胞浆 ATPase 负荷
  - 源函数: [cytosolicATPase_load](file:///home/yifei/AI4Science/metabolomics/simulate/modules/code/simulate.py#L566-L569)
  - 简述: 非特异ATP水解负荷，转化为ADP。
  - 规则: 受ATP水平与速率修饰限制。

## 信号与调控

- 名称: 系统信号编排
  - 源函数: [orchestrateSystemSignals](file:///home/yifei/AI4Science/metabolomics/simulate/modules/code/simulate.py#L614-L619)
  - 简述: 调用激素、神经、免疫信号模块及降解模块。
  - 规则: 编排调用，不直接产生代谢物变化。

- 名称: 能量赤字策略
  - 源函数: [applyEnergyDeficitPolicies](file:///home/yifei/AI4Science/metabolomics/simulate/modules/code/simulate.py#L621-L632)
  - 简述: 根据ATP与NADH/NAD+状态下调全局速率。
  - 规则: 动态调整 ctx.rate_modifier。

- 名称: 激素信号转导（胰岛素/胰高血糖素）
  - 源函数: [hormoneSignalTransduction](file:///home/yifei/AI4Science/metabolomics/simulate/modules/code/simulate.py#L633-L640)
  - 简述: 依据血糖与进食状态生成胰岛素/胰高血糖素信号。
  - 规则: 采用Sigmoid响应；进食时胰岛素增强、胰高血糖素抑制。

- 名称: 神经信号整合（肾上腺素）
  - 源函数: [neuralSignalIntegration](file:///home/yifei/AI4Science/metabolomics/simulate/modules/code/simulate.py#L642-L646)
  - 简述: 规范化肾上腺素范围并写回信号。
  - 规则: 限幅到生理区间。

- 名称: 免疫信号交互（炎症）
  - 源函数: [immuneSignalInteraction](file:///home/yifei/AI4Science/metabolomics/simulate/modules/code/simulate.py#L648-L654)
  - 简述: 缓慢衰减炎症水平并下调胰岛素敏感性。
  - 规则: 炎症越高，敏感性越低（下限0.5）。

- 名称: 胰岛素降解（IDE）
  - 源函数: [degradeInsulin](file:///home/yifei/AI4Science/metabolomics/simulate/modules/code/simulate.py#L656-L663)
  - 简述: IDE活性驱动胰岛素清除。
  - 规则: 降解速率∝IDE×胰岛素。

- 名称: 胰高血糖素降解
  - 源函数: [degradeGlucagon](file:///home/yifei/AI4Science/metabolomics/simulate/modules/code/simulate.py#L665-L669)
  - 简述: 基础速率清除胰高血糖素。
  - 规则: 固定幅度衰减。

- 名称: 儿茶酚胺失活
  - 源函数: [inactivateCatecholamines](file:///home/yifei/AI4Science/metabolomics/simulate/modules/code/simulate.py#L671-L675)
  - 简述: 基础速率清除肾上腺素。
  - 规则: 固定幅度衰减。

## 流程编排（组合调用）

- 名称: 糖原合成编排
  - 源函数: [orchestrateGlycogenSynthesis](file:///home/yifei/AI4Science/metabolomics/simulate/modules/code/simulate.py#L430-L441)
  - 简述: 组合PGM、UDP-Glc、GS与分支酶输出净变化。
  - 规则: 聚合各子反应的产出写入环境。

- 名称: 糖原分解编排
  - 源函数: [orchestrateGlycogenBreakdown](file:///home/yifei/AI4Science/metabolomics/simulate/modules/code/simulate.py#L442-L451)
  - 简述: 组合GP、去分支与G1P→G6P。
  - 规则: 聚合并写入环境。

- 名称: 糖异生编排
  - 源函数: [orchestrateGluconeogenesis](file:///home/yifei/AI4Science/metabolomics/simulate/modules/code/simulate.py#L453-L471)
  - 简述: 汇总乳酸/甘油/氨基酸供体生成葡萄糖。
  - 规则: 酒精抑制；炎症/皮质醇促进；进食状态限幅。

- 名称: 糖酵解编排
  - 源函数: [orchestrateGlycolysis](file:///home/yifei/AI4Science/metabolomics/simulate/modules/code/simulate.py#L473-L482)
  - 简述: 组合GK/HK、中间步与PK。
  - 规则: 聚合并写入环境。

- 名称: 脂质代谢编排
  - 源函数: [orchestrateLipidMetabolism](file:///home/yifei/AI4Science/metabolomics/simulate/modules/code/simulate.py#L484-L544)
  - 简述: 条件调用β氧化/合成/DNL/转运，并限幅TG。
  - 规则: 高脂肪酸优先β氧化；餐后与激素状态影响路径选择与强度。

- 名称: 氨基酸代谢编排
  - 源函数: [orchestrateAminoAcidMetabolism](file:///home/yifei/AI4Science/metabolomics/simulate/modules/code/simulate.py#L546-L554)
  - 简述: 组合分解与合成/转运。
  - 规则: 聚合并写入环境。

- 名称: 能量稳态编排
  - 源函数: [orchestrateEnergyHomeostasis](file:///home/yifei/AI4Science/metabolomics/simulate/modules/code/simulate.py#L556-L564)
  - 简述: 低糖时走酮体生成，否则走氧化磷酸化。
  - 规则: 基于葡萄糖阈值切换路径。

- 名称: 尿素循环编排
  - 源函数: [orchestrateUreaCycle](file:///home/yifei/AI4Science/metabolomics/simulate/modules/code/simulate.py#L571-L581)
  - 简述: 组合CPS1/OTC/ASS1/ASL输出净变化。
  - 规则: 聚合并写入环境。

- 名称: 解毒过程编排
  - 源函数: [orchestrateDetoxification](file:///home/yifei/AI4Science/metabolomics/simulate/modules/code/simulate.py#L583-L595)
  - 简述: 汇总Ⅰ相/Ⅱ相、酒精代谢与UGT及乙酸活化。
  - 规则: 聚合并写入环境。

- 名称: 合成与分泌编排
  - 源函数: [orchestrateSynthesisSecretion](file:///home/yifei/AI4Science/metabolomics/simulate/modules/code/simulate.py#L597-L606)
  - 简述: 胆汁酸、血浆蛋白与凝血因子生成的合计输出。
  - 规则: 聚合并写入环境。
