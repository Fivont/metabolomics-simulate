# 详细代谢反应规格

## 模块 A：营养物质代谢（核心能量转换）

### 糖类代谢

#### 糖类转运与摄取 (Carbohydrate Transport and Uptake)

##### 步骤 ID: GLY-11
**1. 反应名称**: 葡萄糖转运蛋白 (Glucose Transporter)
**2. 化学方程式**: Glucose(blood) ⇌ Glucose(cytosol)
**3. 核心酶信息**: GLUT2 (SLC2A2), 肝脏特异性葡萄糖转运蛋白，基因型: SLC2A2
**4. 动力学与调控**: 
   - 反应机制: 被动易化扩散，通过构象变化机制转运葡萄糖
   - 速率方程: v = (Vmax_forward[Glucose]blood - Vmax_backward[Glucose]cytosol) / (1 + [Glucose]blood/Km_forward + [Glucose]cytosol/Km_backward)
   - 动力学参数: 
     * Km_forward(Glucose) ~15-20 mM (外向内转运)
     * Km_backward(Glucose) ~15-20 mM (内向外运)
     * Vmax ~100-200 nmol/min/mg protein
     * 转运效率: 高容量低亲和力系统
   - 抑制类型: 无特异性抑制剂
   - 激活剂: 
     * 胰岛素 (转录水平上调)
     * 葡萄糖 (底物诱导表达)
   - 抑制剂: 
     * 果糖 (竞争性抑制，Ki ~50-100 mM)
     * 山梨醇 (竞争性抑制，Ki ~100-200 mM)
   - 转运机制: 被动易化扩散，不消耗ATP
   - 双向转运逻辑: 血糖高时(>10 mM)肝脏摄取, 血糖低时(<5 mM)肝脏释放葡萄糖
   - 膜定位: 基底膜 (Basolateral membrane)
   - 转录调控: 
     * 胰岛素: 上调SLC2A2基因表达
     * 胰高血糖素: 下调SLC2A2基因表达
     * 糖皮质激素: 上调SLC2A2基因表达
   - 翻译后修饰: 
     * 磷酸化: 蛋白激酶C (PKC) 磷酸化可降低转运活性
     * 糖基化: N-糖基化对转运活性至关重要
**5. 能量与热力学**: ΔG°' ≈ 0 kJ/mol (可逆)
**6. 生理意义**: 肝脏作为血糖缓冲器，高血糖时摄取储存，低血糖时释放维持血糖稳定
**7. 病理结局**: 
   - GLUT2 缺陷: Fanconi-Bickel 综合征，糖原储积病 XI 型
   - GLUT2 过表达: 可能导致脂肪肝（过量葡萄糖摄取）
   - GLUT2 活性降低: 胰岛素抵抗，2型糖尿病风险增加

##### 步骤 ID: GLY-12
**1. 反应名称**: 丙酮酸转运蛋白 (Pyruvate Transporter)
**2. 化学方程式**: Pyruvate(cytosol) ⇌ Pyruvate(mitochondria)
**3. 核心酶信息**: MPC (Mitochondrial Pyruvate Carrier), MPC1/MPC2 异源二聚体，基因型: MPC1, MPC2
**4. 动力学与调控**: 
   - 反应机制: 质子共转运机制，每转运1分子丙酮酸同时转运1个质子进入线粒体
   - 速率方程: v = (Vmax_forward[Pyruvate]cytosol[H+]cytosol - Vmax_backward[Pyruvate]mito[H+]mito) / (1 + [Pyruvate]cytosol/Km_forward + [Pyruvate]mito/Km_backward + Ki(UK5099)[UK5099])
   - 动力学参数: 
     * Km_forward(Pyruvate) ~0.1-0.5 mM (胞浆到线粒体)
     * Km_backward(Pyruvate) ~0.5-1.0 mM (线粒体到胞浆)
     * Vmax ~50-100 nmol/min/mg protein
     * 质子依赖性: 转运速率与ΔpH呈正相关
   - 抑制类型: 
     * UK5099: 竞争性抑制剂 (与丙酮酸竞争结合位点)，Ki ~0.01-0.05 μM
     * α-氰基-4-羟基肉桂酸: 竞争性抑制剂，Ki ~0.1-0.5 μM
   - 激活剂: 
     * 胰岛素 (转录水平上调MPC表达)
     * 丙酮酸 (底物诱导表达)
     * Mg2+ (促进异源二聚体形成)
   - 抑制剂: 
     * UK5099 (特异性抑制剂)
     * α-氰基-4-羟基肉桂酸 (经典抑制剂)
     * 棕榈酰-CoA (非竞争性抑制，Ki ~0.1-0.5 mM)
     * 过氧化脂质 (氧化应激抑制)
   - 转运机制: 质子共转运，依赖膜电位
   - 膜定位: 线粒体内膜 (Inner mitochondrial membrane)
   - 转录调控: 
     * 胰岛素: 上调MPC1/MPC2基因表达
     * 胰高血糖素: 下调MPC1/MPC2基因表达
     * 甲状腺激素: 上调MPC1/MPC2基因表达
   - 翻译后修饰: 
     * 磷酸化: AMPK 磷酸化可增强转运活性
     * 乙酰化: SIRT3 去乙酰化可增强转运活性
   - 异源二聚体调控: MPC1/MPC2 比例对转运活性至关重要
**5. 能量与热力学**: ΔG°' ≈ +5 kJ/mol (可逆，需要质子梯度)
**6. 生理意义**: 将胞浆丙酮酸运入线粒体进行 TCA 循环或糖异生
**7. 病理结局**: 
   - MPC 缺陷: 丙酮酸脱氢酶缺乏，乳酸酸中毒
   - MPC 抑制: 糖异生受阻，低血糖风险
   - MPC 过表达: 可能导致线粒体丙酮酸过载，活性氧生成增加

##### 步骤 ID: GLY-13
**1. 反应名称**: 丙酮酸脱氢酶复合体 (Pyruvate Dehydrogenase Complex)
**2. 化学方程式**: 1.0 Pyruvate + 1.0 CoA-SH + 1.0 NAD+ → 1.0 Acetyl-CoA + 1.0 NADH + 1.0 CO2 + 1.0 H+
**3. 核心酶信息**: PDH 复合体 (E1: PDHA1/PDHB, E2: DLAT, E3: DLD)，基因型: PDHA1, PDHB, DLAT, DLD
**4. 动力学与调控**: 
   - 反应机制: 多酶复合体顺序反应机制
   - 反应序列: 1) E1 (丙酮酸脱氢酶) 催化丙酮酸脱羧，形成羟乙基-TPP中间物 2) 羟乙基转移到E2 (二氢硫辛酰胺转乙酰酶) 的硫辛酰胺辅因子上 3) E2 将乙酰基转移给CoA，生成乙酰-CoA 4) E3 (二氢硫辛酰胺脱氢酶) 重新氧化硫辛酰胺，将电子转移给FAD，再转移给NAD+
   - 速率方程: v = Vmax[Pyruvate][CoA-SH][NAD+] / (K1[CoA-SH][NAD+] + K2[Pyruvate][NAD+] + K3[Pyruvate][CoA-SH] + [Pyruvate][CoA-SH][NAD+] + Ki(ATP)[ATP] + Ki(Acetyl-CoA)[Acetyl-CoA] + Ki(NADH)[NADH])
   - 动力学参数: 
     * Km(Pyruvate) ~0.05-0.1 mM
     * Km(CoA-SH) ~0.01-0.05 mM
     * Km(NAD+) ~0.05-0.1 mM
     * Vmax ~100-200 μmol/min/mg protein
   - 抑制类型: 
     * ATP: 非竞争性抑制剂，Ki ~0.1-0.5 mM
     * Acetyl-CoA: 竞争性抑制剂 (与CoA-SH竞争结合位点)，Ki ~0.01-0.05 mM
     * NADH: 竞争性抑制剂 (与NAD+竞争结合位点)，Ki ~0.01-0.05 mM
   - 激活剂: 
     * Ca2+ (别构激活，降低Km值)
     * Insulin (通过激活丙酮酸脱氢酶磷酸酶(PDP)促进去磷酸化激活)
     * AMP (别构激活，与ATP竞争)
   - 抑制剂: 
     * 丙酮酸脱氢酶激酶 (PDK) 磷酸化抑制 (E1亚基Ser-293, Ser-300, Ser-305磷酸化)
     * 乙酰-CoA (产物抑制)
     * NADH (产物抑制)
     * ATP (能量状态抑制)
   - 空间定位: 线粒体基质 (Mitochondrial matrix)
   - 辅因子: TPP (E1), 硫辛酰胺 (E2), FAD (E3), Mg2+
   - 磷酸化调控: 
     * 磷酸化状态: E1亚基磷酸化 → 复合体失活
     * 去磷酸化状态: E1亚基去磷酸化 → 复合体激活
     * PDK同工酶: PDK1-4，不同组织表达不同，对效应物敏感性不同
     * PDP同工酶: PDP1-2，催化去磷酸化激活
**5. 能量与热力学**: ΔG°' ≈ -35 kJ/mol (不可逆)
**6. 生理意义**: 连接糖酵解和 TCA 循环的关键步骤，将丙酮酸转化为乙酰-CoA
**7. 病理结局**: 
   - PDH 缺陷: 乳酸酸中毒，神经发育迟缓
   - PDH 过度抑制 (如 PDK 过表达): Warburg 效应，肿瘤代谢特征

##### 步骤 ID: GLY-14
**1. 反应名称**: 乳酸脱氢酶 (Lactate Dehydrogenase)
**2. 化学方程式**: 1.0 Pyruvate + 1.0 NADH + 1.0 H+ ⇌ 1.0 Lactate + 1.0 NAD+
**3. 核心酶信息**: LDH (Lactate Dehydrogenase), LDHA (M亚基) 和 LDHB (H亚基)，基因型: LDHA, LDHB
**4. 动力学与调控**: 
   - 反应机制: 有序双底物反应机制，先结合NADH/NAD+，再结合丙酮酸/乳酸
   - 速率方程: v = (Vmax_forward[Pyruvate][NADH] - Vmax_backward[Lactate][NAD+]) / (1 + [Pyruvate]Km_pyr + [NADH]Km_nadh + [Lactate]Km_lac + [NAD+]Km_nad + Ki(Oxamate)[Oxamate])
   - 平衡常数 (Keq): 同工酶条件下相同，由底物/产物及细胞环境决定
   - 动力学参数 (LDHA, M亚基): 
     * Km(Pyruvate) ~0.5-1.0 mM
     * Km(NADH) ~0.01-0.05 mM
     * Km(Lactate) ~5-10 mM
     * Km(NAD+) ~0.1-0.5 mM
     * Vmax ~1000-2000 μmol/min/mg protein
   - 动力学参数 (LDHB, H亚基): 
     * Km(Pyruvate) ~0.05-0.1 mM
     * Km(NADH) ~0.005-0.02 mM
     * Km(Lactate) ~0.5-1.0 mM
     * Km(NAD+) ~0.05-0.1 mM
     * Vmax ~500-1000 μmol/min/mg protein
   - 抑制类型: 
     * Oxamate: 竞争性抑制剂 (与丙酮酸竞争结合位点)，Ki ~0.1-0.5 mM
     * 草酰乙酸: 竞争性抑制剂 (与丙酮酸竞争结合位点)，Ki ~0.01-0.05 mM
     * 丙酮酸: 底物抑制 (高浓度抑制)，Ki ~5-10 mM
   - 激活剂: 无特异性离子激活剂需求
   - 抑制剂: 
     * Oxamate (经典抑制剂)
     * 草酰乙酸 (代谢物抑制剂)
     * 丙酮酸 (高浓度底物抑制)
   - 同工酶差异: 
     * LDHA (M亚基): 倾向丙酮酸→乳酸 (厌氧代谢)，高Km值，对丙酮酸亲和力低
     * LDHB (H亚基): 倾向乳酸→丙酮酸 (有氧代谢)，低Km值，对丙酮酸亲和力高
     * LDHC (C亚基): 睾丸特异性，动力学特性介于LDHA和LDHB之间
     * 同工酶组合: LDHA4 (M4), LDHA3B1, LDHA2B2, LDHA1B3, LDHB4 (H4)
   - 膜定位: 胞浆 (Cytosol)
   - 辅因子: NAD+/NADH
   - 转录调控: 
     * 缺氧诱导因子-1α (HIF-1α): 上调LDHA基因表达
     * 胰岛素: 上调LDHB基因表达
     * 胰高血糖素: 上调LDHA基因表达
   - 翻译后修饰: 
     * 磷酸化: 蛋白激酶A (PKA) 磷酸化可降低LDH活性
     * 乙酰化: SIRT1去乙酰化可增强LDH活性
     * 硝基化: 一氧化氮 (NO) 诱导的硝基化可抑制LDH活性
   - 代谢调控: 
     * NAD+/NADH 比率: 调控反应方向，低比率促进乳酸生成
     * 丙酮酸/乳酸比率: 调控反应方向
     * 氧气浓度: 低氧促进LDHA表达和乳酸生成
**5. 能量与热力学**: ΔG°' ≈ -25 kJ/mol (可逆)
**6. 生理意义**: 在缺氧或高强度运动时再生 NAD+，维持糖酵解进行；在有氧条件下将乳酸转化为丙酮酸进入TCA循环
**7. 病理结局**: 
   - LDHA 过表达: Warburg 效应，肿瘤代谢特征，乳酸堆积
   - LDHB 缺陷: 心肌功能障碍，运动不耐受
   - LDH 缺陷: 运动不耐受，肌红蛋白尿症，代谢性酸中毒
   - 乳酸酸中毒: LDH 活性异常或组织缺氧导致

#### 果糖代谢 (Fructose Metabolism)

##### 步骤 ID: GLY-15
**1. 反应名称**: 肝脏果糖摄取 (Hepatic Fructose Uptake)
**2. 化学方程式**: Fructose(blood) ⇌ Fructose(cytosol)
**3. 核心酶信息**: GLUT2 (SLC2A2)，肝细胞主要果糖/葡萄糖/半乳糖双向转运体；补充：小肠上皮细胞顶膜表达GLUT5 (SLC2A5) 专一性果糖转运
**4. 动力学与调控**: 
   - 反应机制: 被动易化扩散，通过构象变化机制转运果糖
   - 速率方程: v = (Vmax_forward[Fructose]blood - Vmax_backward[Fructose]cytosol) / (1 + [Fructose]blood/Km_forward + [Fructose]cytosol/Km_backward)
   - 动力学参数: 
     * Km_forward(Fructose) ~10-20 mM (GLUT2)
     * Km_backward(Fructose) ~10-20 mM (GLUT2)
     * Vmax ~50-100 nmol/min/mg protein
   - 抑制类型: 无特异性抑制剂
   - 激活剂: 底物诱导表达
   - 膜定位: 基底膜 (Basolateral membrane, 肝细胞)
   - 补充信息（GLUT5）: 顶膜定位（小肠）；对果糖高度特异，葡萄糖不被GLUT5识别；小分子抑制剂MSNBA；代谢类似物/竞争剂2,5-AM
**5. 能量与热力学**: ΔG°' ≈ 0 kJ/mol (可逆)
**6. 生理意义**: 正常条件下肝脏主要通过GLUT2摄取果糖；GLUT5负责小肠对膳食果糖的吸收
**7. 病理结局**: 
   - 小肠GLUT5 缺陷: 果糖吸收不良
   - 肝脏GLUT2 异常: 可能影响肝脏果糖摄取

##### 步骤 ID: GLY-16
**1. 反应名称**: 果糖激酶 (Fructokinase)
**2. 化学方程式**: 1.0 Fructose + 1.0 ATP → 1.0 Fructose-1-Phosphate + 1.0 ADP + 1.0 H+
**3. 核心酶信息**: 果糖激酶 (KHK), EC 2.7.1.3，基因型: KHK；同工酶：KHK-C（肝脏/肾/肠道，高亲和力，低Km ~0.5 mM），KHK-A（广泛表达，低亲和力，高Km ~6-10 mM）
**4. 动力学与调控**: 
   - 反应机制: 磷酸转移反应，将ATP的磷酸基团转移到果糖的C1位
   - 速率方程: v = Vmax[Fructose][ATP] / (Km(Fructose)[ATP] + Km(ATP)[Fructose] + [Fructose][ATP])
   - 动力学参数: 
     * Km(Fructose) 取决于同工酶：KHK-C ~0.5 mM；KHK-A ~6-10 mM
     * Km(ATP) ~0.1-0.5 mM
     * Vmax ~50-100 μmol/min/mg protein
   - 抑制类型: 无强变构调控
   - 激活剂: 无强变构激活剂
   - 抑制剂: 无强抑制剂
   - 膜定位: 胞浆 (Cytosol)
**5. 能量与热力学**: ATP消耗: -1, ΔG°' ≈ -15.9 kJ/mol (不可逆)
**6. 生理意义**: 果糖代谢的第一步，将果糖磷酸化为果糖-1-磷酸；肝脏高表达KHK-C以高效代谢血液中的果糖；在病理条件下存在KHK-C → KHK-A表达转换
**7. 病理结局**: 
   - KHK 缺陷: 原发性果糖尿症（通常良性）
   - 遗传性果糖不耐受症 (HFI): 由 ALDOB 缺乏导致，F-1-P 堆积

##### 步骤 ID: GLY-17
**1. 反应名称**: 醛缩酶B (Aldolase B)
**2. 化学方程式**: 1.0 Fructose-1-Phosphate → 1.0 Glyceraldehyde + 1.0 Dihydroxyacetone Phosphate
**3. 核心酶信息**: 醛缩酶B (ALDOB), EC 4.1.2.13, 肝脏特异性，基因型: ALDOB
**4. 动力学与调控**: 
   - 反应机制: 醛缩反应，通过形成Schiff碱中间物
   - 速率方程: v = Vmax[Fructose-1-Phosphate] / (Km(Fructose-1-Phosphate) + [Fructose-1-Phosphate])
   - 动力学参数: 
     * Km(Fructose-1-Phosphate) ~0.5-1.0 mM
     * Vmax ~50-100 μmol/min/mg protein
   - 抑制类型: 无强变构调控
   - 激活剂: 无强变构激活剂
   - 抑制剂: 无强抑制剂
   - 膜定位: 胞浆 (Cytosol)
**5. 能量与热力学**: ΔG°' ≈ +22.8 kJ/mol (可逆)
**6. 生理意义**: 将果糖-1-磷酸裂解为甘油醛和二羟基丙酮磷酸，进入糖酵解途径
**7. 病理结局**: 
   - ALDOB 缺陷: 遗传性果糖不耐受症 (HFI)，果糖-1-磷酸堆积
   - ALDOB 活性不足: 果糖代谢障碍

##### 步骤 ID: GLY-18
**1. 反应名称**: 甘油醛激酶 (Glyceraldehyde Kinase)
**2. 化学方程式**: 1.0 Glyceraldehyde + 1.0 ATP → 1.0 Glyceraldehyde-3-Phosphate + 1.0 ADP + 1.0 H+
**3. 核心酶信息**: 甘油醛激酶 (GK), EC 2.7.1.16, 基因型: GK
**4. 动力学与调控**: 
   - 反应机制: 磷酸转移反应，将ATP的磷酸基团转移到甘油醛的C3位
   - 速率方程: v = Vmax[Glyceraldehyde][ATP] / (Km(Glyceraldehyde)[ATP] + Km(ATP)[Glyceraldehyde] + [Glyceraldehyde][ATP])
   - 动力学参数: 
     * Km(Glyceraldehyde) ~0.1-0.5 mM
     * Km(ATP) ~0.1-0.5 mM
     * Vmax ~50-100 μmol/min/mg protein
   - 抑制类型: 无强变构调控
   - 激活剂: 无强变构激活剂
   - 抑制剂: 无强抑制剂
   - 膜定位: 胞浆 (Cytosol)
**5. 能量与热力学**: ATP消耗: -1, ΔG°' ≈ -18.8 kJ/mol (不可逆)
**6. 生理意义**: 将甘油醛磷酸化为甘油醛-3-磷酸，进入糖酵解途径
**7. 病理结局**: 
   - GK 缺陷: 甘油醛代谢障碍，可能影响果糖代谢

#### 半乳糖代谢 (Galactose Metabolism)

##### 步骤 ID: GLY-19
**1. 反应名称**: 半乳糖转运蛋白 (Galactose Transporter)
**2. 化学方程式**: Galactose(blood) ⇌ Galactose(cytosol)
**3. 核心酶信息**: GLUT2 (SLC2A2)，肝脏双向转运葡萄糖/半乳糖；补充：肠上皮SGLT1 (SLC5A1) 参与半乳糖与Na+共转运，负责肠腔吸收
**4. 动力学与调控**: 
   - 反应机制: 被动易化扩散，通过构象变化机制转运半乳糖
   - 速率方程: v = (Vmax_forward[Galactose]blood - Vmax_backward[Galactose]cytosol) / (1 + [Galactose]blood/Km_forward + [Galactose]cytosol/Km_backward)
   - 动力学参数: 
     * Km_forward(Galactose) ~10-15 mM
     * Km_backward(Galactose) ~10-15 mM
     * Vmax ~80-150 nmol/min/mg protein
   - 抑制类型: 无特异性抑制剂
   - 激活剂: 半乳糖 (底物诱导表达)
   - 抑制剂: 葡萄糖 (竞争性抑制，Ki ~15-20 mM)
   - 膜定位: 基底膜 (Basolateral membrane)
**5. 能量与热力学**: ΔG°' ≈ 0 kJ/mol (可逆)
**6. 生理意义**: 肝脏摄取半乳糖进行代谢，是半乳糖代谢的主要场所
**7. 病理结局**: 
   - GLUT2 缺陷: 半乳糖吸收和代谢障碍，Fanconi-Bickel 综合征（糖原累积病 XI 型）

##### 步骤 ID: GLY-20
**1. 反应名称**: 半乳糖激酶 (Galactokinase)
**2. 化学方程式**: 1.0 Galactose + 1.0 ATP → 1.0 Galactose-1-Phosphate + 1.0 ADP + 1.0 H+
**3. 核心酶信息**: 半乳糖激酶 (GALK1), EC 2.7.1.6, 基因型: GALK1
**4. 动力学与调控**: 
   - 反应机制: 磷酸转移反应，将ATP的磷酸基团转移到半乳糖的C1位
   - 速率方程: v = Vmax[Galactose][ATP] / (Km(Galactose)[ATP] + Km(ATP)[Galactose] + [Galactose][ATP])
   - 动力学参数: 
     * Km(Galactose) ~0.5-1.0 mM
     * Km(ATP) ~0.1-0.5 mM
     * Vmax ~20-50 μmol/min/mg protein
   - 抑制类型: 无强变构调控
   - 激活剂: 无强变构激活剂
   - 抑制剂: 无强抑制剂
   - 膜定位: 胞浆 (Cytosol)
**5. 能量与热力学**: ATP消耗: -1, ΔG°' ≈ -16.9 kJ/mol (不可逆)
**6. 生理意义**: 半乳糖代谢的第一步，将半乳糖磷酸化为半乳糖-1-磷酸
**7. 病理结局**: 
   - GALK1 缺陷: 半乳糖血症 II 型，半乳糖堆积导致白内障

##### 步骤 ID: GLY-21
**1. 反应名称**: 尿苷二磷酸葡萄糖-半乳糖-1-磷酸尿苷转移酶 (GALT)
**2. 化学方程式**: 1.0 Galactose-1-Phosphate + 1.0 UDP-Glucose → 1.0 Glucose-1-Phosphate + 1.0 UDP-Galactose
**3. 核心酶信息**: GALT (UDP-Glucose:Galactose-1-Phosphate Uridylyltransferase), EC 2.7.7.12, 基因型: GALT
**4. 动力学与调控**: 
   - 反应机制: 双底物转移反应，将UDP基团从UDP-葡萄糖转移到半乳糖-1-磷酸
   - 速率方程: v = Vmax[Galactose-1-Phosphate][UDP-Glucose] / (Km(Galactose-1-Phosphate)[UDP-Glucose] + Km(UDP-Glucose)[Galactose-1-Phosphate] + [Galactose-1-Phosphate][UDP-Glucose])
   - 动力学参数: 
     * Km(Galactose-1-Phosphate) ~0.05-0.1 mM
     * Km(UDP-Glucose) ~0.05-0.1 mM
     * Vmax ~20-50 μmol/min/mg protein
   - 抑制类型: 无强变构调控
   - 激活剂: 无强变构激活剂
   - 抑制剂: 无强抑制剂
   - 膜定位: 胞浆 (Cytosol)
**5. 能量与热力学**: ΔG°' ≈ 0 kJ/mol (可逆)
**6. 生理意义**: 半乳糖代谢的关键步骤，将半乳糖-1-磷酸转化为葡萄糖-1-磷酸
**7. 病理结局**: 
   - GALT 缺陷: 半乳糖血症 I 型，半乳糖-1-磷酸堆积，导致肝损伤和白内障

##### 步骤 ID: GLY-22
**1. 反应名称**: UDP-半乳糖-4-表异构酶 (GALE)
**2. 化学方程式**: 1.0 UDP-Galactose → 1.0 UDP-Glucose
**3. 核心酶信息**: GALE (UDP-Galactose-4-Epimerase), EC 5.1.3.2, 基因型: GALE
**4. 动力学与调控**: 
   - 反应机制: 氧化-还原异构化反应，通过4-酮中间物
   - 速率方程: v = Vmax[UDP-Galactose] / (Km(UDP-Galactose) + [UDP-Galactose])
   - 动力学参数: 
     * Km(UDP-Galactose) ~0.1-0.5 mM
     * Vmax ~20-50 μmol/min/mg protein
   - 抑制类型: 无强变构调控
   - 激活剂: 无强变构激活剂
   - 抑制剂: 无强抑制剂
   - 膜定位: 胞浆 (Cytosol)
   - 辅因子: NAD+ (作为辅酶参与氧化-还原反应)
**5. 能量与热力学**: ΔG°' ≈ 0 kJ/mol (可逆)
**6. 生理意义**: 将UDP-半乳糖转化为UDP-葡萄糖，完成半乳糖代谢循环
**7. 病理结局**: 
   - GALE 缺陷: 半乳糖血症 III 型，半乳糖代谢障碍

#### 糖原代谢 (Glycogen Metabolism)

##### 步骤 ID: GLY-23
**1. 反应名称**: 糖原合成酶 (Glycogen Synthase)
**2. 化学方程式**: 1.0 UDP-Glucose + (Glucose)n → 1.0 (Glucose)n+1 + 1.0 UDP
**3. 核心酶信息**: 糖原合成酶 (GYS), EC 2.4.1.11, 肝脏特异性: GYS2，基因型: GYS2
**4. 动力学与调控**: 
   - 反应机制: 糖基转移反应，将UDP-葡萄糖的葡萄糖残基转移到糖原引物
   - 速率方程: v = Vmax[UDP-Glucose][Glycogen] / (Km(UDP-Glucose)[Glycogen] + Km(Glycogen)[UDP-Glucose] + [UDP-Glucose][Glycogen] + Ki(UDP)[UDP])
   - 动力学参数: 
     * Km(UDP-Glucose) ~0.5-1.0 mM
     * Km(Glycogen) ~0.1-0.5 mg/mL
     * Vmax ~50-100 μmol/min/mg protein
   - 抑制类型: 
     * UDP: 竞争性抑制剂 (与UDP-葡萄糖竞争结合位点)，Ki ~0.5-1.0 mM
   - 激活剂: 
     * 葡萄糖-6-磷酸 (别构激活剂)
     * 胰岛素 (通过去磷酸化激活)
   - 抑制剂: 
     * 胰高血糖素 (通过磷酸化抑制)
     * AMPK (通过磷酸化抑制)
   - 磷酸化调控: 
     * 磷酸化状态: 多个丝氨酸残基磷酸化 → 酶活性降低
     * 去磷酸化状态: 去磷酸化 → 酶活性增加
   - 膜定位: 胞浆 (Cytosol)
**5. 能量与热力学**: ΔG°' ≈ -13.4 kJ/mol (可逆)
**6. 生理意义**: 糖原合成的关键酶，将葡萄糖残基添加到糖原分子
**7. 病理结局**: 
   - GYS2 缺陷: 糖原储积病 0 型，糖原合成障碍
   - GYS2 过表达: 可能导致糖原过度合成

##### 步骤 ID: GLY-24
**1. 反应名称**: 糖原磷酸化酶 (Glycogen Phosphorylase)
**2. 化学方程式**: 1.0 (Glucose)n + 1.0 Pi → 1.0 (Glucose)n-1 + 1.0 Glucose-1-Phosphate
**3. 核心酶信息**: 糖原磷酸化酶 (PYGL), EC 2.4.1.1, 肝脏特异性: PYGL，基因型: PYGL
**4. 动力学与调控**: 
   - 反应机制: 磷酸解反应，从糖原非还原端切除葡萄糖残基
   - 速率方程: v = Vmax[Glycogen][Pi] / (Km(Glycogen)[Pi] + Km(Pi)[Glycogen] + [Glycogen][Pi] + Kact[AMP])
   - 动力学参数: 
     * Km(Glycogen) ~0.1-0.5 mg/mL
     * Km(Pi) ~1.0-5.0 mM
     * Vmax ~50-100 μmol/min/mg protein
   - 激活剂: 
     * AMP (别构激活剂)
     * 胰高血糖素 (通过磷酸化激活)
     * Ca2+ (别构激活剂)
   - 抑制剂: 
     * ATP (别构抑制剂)
     * 葡萄糖-6-磷酸 (别构抑制剂)
     * 葡萄糖 (别构抑制剂)
     * 胰岛素 (通过去磷酸化抑制)
   - 磷酸化调控: 
     * 磷酸化状态: Ser-14磷酸化 → 酶活性增加
     * 去磷酸化状态: 去磷酸化 → 酶活性降低
   - 膜定位: 胞浆 (Cytosol)
**5. 能量与热力学**: ΔG°' ≈ +3.1 kJ/mol (可逆)
**6. 生理意义**: 糖原分解的关键酶，从糖原分子释放葡萄糖-1-磷酸
**7. 病理结局**: 
   - PYGL 缺陷: 糖原储积病 VI 型 (Hers病)，糖原分解障碍
   - PYGL 过表达: 可能导致糖原过度分解

##### 步骤 ID: GLY-25
**1. 反应名称**: 磷酸葡萄糖变位酶 (Phosphoglucomutase)
**2. 化学方程式**: 1.0 Glucose-1-Phosphate → 1.0 Glucose-6-Phosphate
**3. 核心酶信息**: 磷酸葡萄糖变位酶 (PGM1), EC 5.4.2.2, 基因型: PGM1
**4. 动力学与调控**: 
   - 反应机制: 磷酸转移反应，通过磷酸化酶中间物
   - 速率方程: v = Vmax[Glucose-1-Phosphate] / (Km(Glucose-1-Phosphate) + [Glucose-1-Phosphate])
   - 动力学参数: 
     * Km(Glucose-1-Phosphate) ~0.1-0.5 mM
     * Km(Glucose-6-Phosphate) ~0.1-0.5 mM (反向反应)
     * Vmax ~200-500 μmol/min/mg protein
   - 抑制类型: 无强变构调控
   - 激活剂: 
     * 葡萄糖-1,6-二磷酸 (必需激活剂，作为磷酸供体)
   - 抑制剂: 无强抑制剂
   - 膜定位: 胞浆 (Cytosol)
**5. 能量与热力学**: ΔG°' ≈ 0 kJ/mol (可逆)
**6. 生理意义**: 连接糖原代谢和糖酵解/糖异生的关键酶，将葡萄糖-1-磷酸转化为葡萄糖-6-磷酸
**7. 病理结局**: 
   - PGM1 缺陷: 磷酸葡萄糖变位酶缺乏症，糖原代谢障碍

#### 戊糖磷酸途径 (Pentose Phosphate Pathway)

##### 步骤 ID: GLY-26
**1. 反应名称**: 葡萄糖-6-磷酸脱氢酶 (G6PD)
**2. 化学方程式**: 1.0 Glucose-6-Phosphate + 1.0 NADP+ → 1.0 6-Phosphogluconolactone + 1.0 NADPH + 1.0 H+
**3. 核心酶信息**: G6PD (Glucose-6-Phosphate Dehydrogenase), EC 1.1.1.49, 基因型: G6PD
**4. 动力学与调控**: 
   - 反应机制: 氧化反应，将葡萄糖-6-磷酸脱氢为6-磷酸葡萄糖酸内酯
   - 速率方程: v = Vmax[Glucose-6-Phosphate][NADP+] / (Km(Glucose-6-Phosphate)[NADP+] + Km(NADP+)[Glucose-6-Phosphate] + [Glucose-6-Phosphate][NADP+] + Ki(NADPH)[NADPH])
   - 动力学参数: 
     * Km(Glucose-6-Phosphate) ~0.1-0.5 mM
     * Km(NADP+) ~0.01-0.05 mM
     * Vmax ~50-100 μmol/min/mg protein
   - 抑制类型: 
     * NADPH: 竞争性抑制剂 (与NADP+竞争结合位点)，Ki ~0.01-0.05 mM
   - 激活剂: 
     * NADP+ (底物激活)
     * 胰岛素 (转录水平上调)
   - 抑制剂: 
     * NADPH (产物抑制)
     * 胰高血糖素 (转录水平下调)
   - 膜定位: 胞浆 (Cytosol)
**5. 能量与热力学**: NADPH生成: +1, ΔG°' ≈ -17.6 kJ/mol (不可逆)
**6. 生理意义**: 戊糖磷酸途径的限速酶，产生NADPH和6-磷酸葡萄糖酸内酯
**7. 病理结局**: 
   - G6PD 缺陷: 蚕豆病，氧化应激敏感性增加，溶血性贫血
   - G6PD 活性不足: NADPH生成减少，抗氧化能力下降

##### 步骤 ID: GLY-27
**1. 反应名称**: 6-磷酸葡萄糖酸内酯酶 (6PGL)
**2. 化学方程式**: 1.0 6-Phosphogluconolactone + 1.0 H2O → 1.0 6-Phosphogluconate + 1.0 H+
**3. 核心酶信息**: 6PGL (6-Phosphogluconolactonase), EC 3.1.1.31, 基因型: PGLS
**4. 动力学与调控**: 
   - 反应机制: 水解反应，将6-磷酸葡萄糖酸内酯水解为6-磷酸葡萄糖酸
   - 速率方程: v = Vmax[6-Phosphogluconolactone] / (Km(6-Phosphogluconolactone) + [6-Phosphogluconolactone])
   - 动力学参数: 
     * Km(6-Phosphogluconolactone) ~0.1-0.5 mM
     * Vmax ~100-200 μmol/min/mg protein
   - 抑制类型: 无强变构调控
   - 激活剂: 无强变构激活剂
   - 抑制剂: 无强抑制剂
   - 膜定位: 胞浆 (Cytosol)
**5. 能量与热力学**: ΔG°' ≈ -16.7 kJ/mol (不可逆)
**6. 生理意义**: 戊糖磷酸途径的第二步，将6-磷酸葡萄糖酸内酯转化为6-磷酸葡萄糖酸
**7. 病理结局**: 
   - PGLS 缺陷: 戊糖磷酸途径障碍，NADPH生成减少

##### 步骤 ID: GLY-28
**1. 反应名称**: 6-磷酸葡萄糖酸脱氢酶 (6PGD)
**2. 化学方程式**: 1.0 6-Phosphogluconate + 1.0 NADP+ → 1.0 Ribulose-5-Phosphate + 1.0 CO2 + 1.0 NADPH + 1.0 H+
**3. 核心酶信息**: 6PGD (6-Phosphogluconate Dehydrogenase), EC 1.1.1.44, 基因型: 6PGD
**4. 动力学与调控**: 
   - 反应机制: 氧化脱羧反应，将6-磷酸葡萄糖酸氧化脱羧为核酮糖-5-磷酸
   - 速率方程: v = Vmax[6-Phosphogluconate][NADP+] / (Km(6-Phosphogluconate)[NADP+] + Km(NADP+)[6-Phosphogluconate] + [6-Phosphogluconate][NADP+] + Ki(NADPH)[NADPH])
   - 动力学参数: 
     * Km(6-Phosphogluconate) ~0.1-0.5 mM
     * Km(NADP+) ~0.01-0.05 mM
     * Vmax ~50-100 μmol/min/mg protein
   - 抑制类型: 
     * NADPH: 竞争性抑制剂 (与NADP+竞争结合位点)，Ki ~0.01-0.05 mM
   - 激活剂: 
     * NADP+ (底物激活)
   - 抑制剂: 
     * NADPH (产物抑制)
   - 膜定位: 胞浆 (Cytosol)
**5. 能量与热力学**: NADPH生成: +1, CO2生成: +1, ΔG°' ≈ -14.3 kJ/mol (不可逆)
**6. 生理意义**: 戊糖磷酸途径的第三步，产生更多NADPH和核酮糖-5-磷酸
**7. 病理结局**: 
   - 6PGD 缺陷: 戊糖磷酸途径障碍，NADPH生成减少

##### 步骤 ID: GLY-29
**1. 反应名称**: 核糖-5-磷酸异构酶 (RPIA)
**2. 化学方程式**: 1.0 Ribulose-5-Phosphate → 1.0 Ribose-5-Phosphate
**3. 核心酶信息**: RPIA (Ribose-5-Phosphate Isomerase A), EC 5.3.1.6, 基因型: RPIA
**4. 动力学与调控**: 
   - 反应机制: 异构化反应，将核酮糖-5-磷酸转化为核糖-5-磷酸
   - 速率方程: v = Vmax[Ribulose-5-Phosphate] / (Km(Ribulose-5-Phosphate) + [Ribulose-5-Phosphate])
   - 动力学参数: 
     * Km(Ribulose-5-Phosphate) ~0.5-1.0 mM
     * Vmax ~100-200 μmol/min/mg protein
   - 抑制类型: 无强变构调控
   - 激活剂: 无强变构激活剂
   - 抑制剂: 无强抑制剂
   - 膜定位: 胞浆 (Cytosol)
**5. 能量与热力学**: ΔG°' ≈ -2.1 kJ/mol (可逆)
**6. 生理意义**: 戊糖磷酸途径的非氧化阶段，产生核糖-5-磷酸用于核苷酸合成
**7. 病理结局**: 
   - RPIA 缺陷: 核糖-5-磷酸生成障碍，可能影响核苷酸合成

#### 糖酵解 (Glycolysis)

##### 步骤 ID: GLY-01
**1. 反应名称**: 葡萄糖磷酸化 (Glucose Phosphorylation)
**2. 化学方程式**: 1.0 Glucose + 1.0 ATP → 1.0 Glucose-6-Phosphate + 1.0 ADP + 1.0 H+
**3. 核心酶信息**: 己糖激酶 IV (Glucokinase), EC 2.7.1.2, 肝脏特异性 (高Km)
**4. 动力学与调控**: 
   - 反应机制: 具有协同性的单体酶，表现出Sigmoidal动力学
   - 协同效应: 无传统的多聚体协同性，但通过构象变化表现出类似的Sigmoidal动力学，是肝脏葡萄糖感知的关键
   - 速率方程: v = Vmax[Glucose]^n / (K0.5^n + [Glucose]^n)，其中K0.5为半饱和浓度，n为表观Hill系数
   - 动力学参数: 
     * Km(Glucose) ~8-10 mM (表观Km)
     * K0.5(Glucose) ~5-7 mM (半饱和浓度)
     * Vmax ~50-100 μmol/min/mg protein
     * 表观Hill系数 (n) ≈ 1.5-2.0
   - 激活剂: 
     * Insulin (转录水平，增加酶表达)
     * Glucose (底物激活，正协同效应)
   - 抑制剂: 
     * GKRP (葡萄糖激酶调节蛋白，非竞争性抑制，与酶结合形成无活性复合物)
     * Fructose-6-Phosphate (别构抑制剂，非竞争性)
   - 葡萄糖感知: Sigmoidal动力学使酶活性对血糖浓度变化敏感，在生理血糖范围内(4-10 mM)表现出开关式响应
**5. 能量与热力学**: ATP消耗: -1, ΔG°' ≈ -16.7 kJ/mol (不可逆)

##### 步骤 ID: GLY-02
**1. 反应名称**: 葡萄糖-6-磷酸异构化 (Glucose-6-Phosphate Isomerization)
**2. 化学方程式**: 1.0 Glucose-6-Phosphate → 1.0 Fructose-6-Phosphate
**3. 核心酶信息**: 磷酸葡萄糖异构酶 (Phosphoglucose Isomerase), EC 5.3.1.9
**4. 动力学与调控**: 
   - 反应机制: 酸-碱催化的异构化反应，通过烯二醇中间物
   - 反应序列: 1) 酶的组氨酸残基作为碱催化剂，提取葡萄糖-6-磷酸的C2质子 2) 形成烯二醇中间物 3) 酶的谷氨酸残基作为酸催化剂，将质子转移到C1 4) 形成果糖-6-磷酸
   - 速率方程: v = Vmax[Glucose-6-Phosphate] / (Km(Glucose-6-Phosphate) + [Glucose-6-Phosphate])
   - 动力学参数: 
     * Km(Glucose-6-Phosphate) ~0.5-1.0 mM
     * Km(Fructose-6-Phosphate) ~0.5-1.0 mM (反向反应)
     * Vmax ~500-1000 μmol/min/mg protein
   - 抑制类型: 无强变构调控，产物抑制较弱
   - 激活剂: 无强变构激活剂
   - 抑制剂: 无强抑制剂
   - 膜定位: 胞浆 (Cytosol)
   - 辅因子: 无，但需要Mg2+作为结构稳定剂
**5. 能量与热力学**: ΔG°' ≈ +1.7 kJ/mol (可逆)

##### 步骤 ID: GLY-03
**1. 反应名称**: 果糖-6-磷酸磷酸化 (Fructose-6-Phosphate Phosphorylation)
**2. 化学方程式**: 1.0 Fructose-6-Phosphate + 1.0 ATP → 1.0 Fructose-1,6-Bisphosphate + 1.0 ADP + 1.0 H+
**3. 核心酶信息**: 磷酸果糖激酶-1 (Phosphofructokinase-1), EC 2.7.1.11, 糖酵解限速酶
**4. 动力学与调控**: 
   - 反应机制: 别构调节的多聚体酶 (四聚体)
   - 协同效应: 具有正协同性，Hill系数 (n) ≈ 2.5-3.0，表现出开关效应
   - 速率方程: v = Vmax[Fructose-6-Phosphate]^n / (K0.5^n + [Fructose-6-Phosphate]^n)，其中K0.5为半饱和浓度
   - 动力学参数: 
     * Km(Fructose-6-Phosphate) ~0.1-0.5 mM
     * K0.5(Fructose-6-Phosphate) ~0.2-0.6 mM (在生理条件下)
     * Vmax ~200-400 μmol/min/mg protein
   - 激活剂: 
     * AMP (别构激活，与ATP竞争结合位点)
     * Fructose-2,6-Bisphosphate (强力别构激活剂，降低K0.5)
   - 抑制剂: 
     * ATP (别构抑制剂，竞争性抑制AMP结合)
     * Citrate (别构抑制剂，非竞争性)
   - 开关效应: 对AMP/ATP比率变化极其敏感，当ATP水平高时抑制，AMP水平高时激活
**5. 能量与热力学**: ATP消耗: -1, ΔG°' ≈ -14.2 kJ/mol (不可逆)

##### 步骤 ID: GLY-04
**1. 反应名称**: 果糖-1,6-二磷酸裂解 (Fructose-1,6-Bisphosphate Cleavage)
**2. 化学方程式**: 1.0 Fructose-1,6-Bisphosphate → 1.0 Glyceraldehyde-3-Phosphate + 1.0 Dihydroxyacetone Phosphate
**3. 核心酶信息**: 醛缩酶 (Aldolase), EC 4.1.2.13
**4. 动力学与调控**: 
   - 反应机制: 醛缩反应，通过形成Schiff碱中间物
   - 反应序列: 1) 酶的赖氨酸残基与果糖-1,6-二磷酸的羰基形成Schiff碱 2) C3-C4键断裂，形成甘油醛-3-磷酸和酶结合的二羟基丙酮磷酸 3) 酶结合的二羟基丙酮磷酸解离，形成游离的二羟基丙酮磷酸
   - 速率方程: v = Vmax[Fructose-1,6-Bisphosphate] / (Km(Fructose-1,6-Bisphosphate) + [Fructose-1,6-Bisphosphate])
   - 动力学参数: 
     * Km(Fructose-1,6-Bisphosphate) ~0.1-0.5 mM
     * Vmax ~200-400 μmol/min/mg protein
   - 抑制类型: 无强变构调控，产物抑制较弱
   - 激活剂: 无强变构激活剂
   - 抑制剂: 无强抑制剂
   - 膜定位: 胞浆 (Cytosol)
   - 辅因子: 无，但需要Mg2+作为结构稳定剂
**5. 能量与热力学**: ΔG°' ≈ +23.8 kJ/mol (可逆，平衡偏向底物)

##### 步骤 ID: GLY-05
**1. 反应名称**: 磷酸丙糖异构化 (Triose Phosphate Isomerization)
**2. 化学方程式**: 1.0 Dihydroxyacetone Phosphate → 1.0 Glyceraldehyde-3-Phosphate
**3. 核心酶信息**: 磷酸丙糖异构酶 (Triose Phosphate Isomerase), EC 5.3.1.1
**4. 动力学与调控**: 
   - 反应机制: 酸-碱催化的异构化反应，通过烯二醇中间物
   - 反应序列: 1) 酶的组氨酸残基作为碱催化剂，提取二羟基丙酮磷酸的C1质子 2) 形成烯二醇中间物 3) 酶的谷氨酸残基作为酸催化剂，将质子转移到C2 4) 形成甘油醛-3-磷酸
   - 速率方程: v = Vmax[Dihydroxyacetone Phosphate] / (Km(Dihydroxyacetone Phosphate) + [Dihydroxyacetone Phosphate])
   - 动力学参数: 
     * Km(Dihydroxyacetone Phosphate) ~0.5-1.0 mM
     * Km(Glyceraldehyde-3-Phosphate) ~0.5-1.0 mM (反向反应)
     * Vmax ~1000-2000 μmol/min/mg protein (催化效率极高)
   - 抑制类型: 无强变构调控，产物抑制较弱
   - 激活剂: 无强变构激活剂
   - 抑制剂: 无强抑制剂
   - 膜定位: 胞浆 (Cytosol)
   - 辅因子: 无，但需要Mg2+作为结构稳定剂
**5. 能量与热力学**: ΔG°' ≈ +7.5 kJ/mol (可逆，平衡偏向DHAP)

##### 步骤 ID: GLY-06
**1. 反应名称**: 甘油醛-3-磷酸氧化磷酸化 (Glyceraldehyde-3-Phosphate Oxidative Phosphorylation)
**2. 化学方程式**: 1.0 Glyceraldehyde-3-Phosphate + 1.0 NAD+ + 1.0 Pi → 1.0 1,3-Bisphosphoglycerate + 1.0 NADH + 1.0 H+
**3. 核心酶信息**: 甘油醛-3-磷酸脱氢酶 (Glyceraldehyde-3-Phosphate Dehydrogenase), EC 1.2.1.12
**4. 动力学与调控**: 
   - 反应机制: 氧化-磷酸化偶联反应，通过硫酯中间物
   - 反应序列: 1) 甘油醛-3-磷酸与酶的半胱氨酸残基形成硫酯中间物 2) 同时将电子转移给NAD+，生成NADH 3) 无机磷酸攻击硫酯键，形成1,3-二磷酸甘油酸 4) 产物解离
   - 速率方程: v = Vmax[Glyceraldehyde-3-Phosphate][Pi][NAD+] / (K1[Pi][NAD+] + K2[Glyceraldehyde-3-Phosphate][NAD+] + K3[Glyceraldehyde-3-Phosphate][Pi] + [Glyceraldehyde-3-Phosphate][Pi][NAD+] + Ki(NADH)[NADH])
   - 动力学参数: 
     * Km(Glyceraldehyde-3-Phosphate) ~0.1-0.5 mM
     * Km(Pi) ~0.5-1.0 mM
     * Km(NAD+) ~0.05-0.1 mM
     * Vmax ~200-400 μmol/min/mg protein
   - 抑制类型: 
     * NADH: 竞争性抑制剂 (与NAD+竞争结合位点)，Ki ~0.01-0.05 mM
   - 激活剂: 无强变构激活剂
   - 抑制剂: 
     * NADH/NAD+ 比值高 (氧化还原状态抑制)
     * 碘乙酸 (不可逆抑制剂，与活性位点半胱氨酸反应)
   - 膜定位: 胞浆 (Cytosol)
   - 辅因子: NAD+/NADH
**5. 能量与热力学**: ΔG°' ≈ +6.3 kJ/mol (可逆)

##### 步骤 ID: GLY-07
**1. 反应名称**: 1,3-二磷酸甘油酸底物水平磷酸化 (1,3-Bisphosphoglycerate Substrate-Level Phosphorylation)
**2. 化学方程式**: 1.0 1,3-Bisphosphoglycerate + 1.0 ADP → 1.0 3-Phosphoglycerate + 1.0 ATP
**3. 核心酶信息**: 磷酸甘油酸激酶 (Phosphoglycerate Kinase), EC 2.7.2.3
**4. 动力学与调控**: 
   - 反应机制: 底物水平磷酸化反应，通过乒乓机制
   - 反应序列: 1) 1,3-二磷酸甘油酸与酶结合，将磷酸基团转移到酶的组氨酸残基 2) ADP与酶结合 3) 磷酸基团从酶转移到ADP，生成ATP 4) 3-磷酸甘油酸和ATP解离
   - 速率方程: v = Vmax[1,3-Bisphosphoglycerate][ADP] / (Km(1,3-Bisphosphoglycerate)[ADP] + Km(ADP)[1,3-Bisphosphoglycerate] + [1,3-Bisphosphoglycerate][ADP] + Ki(ATP)[ATP])
   - 动力学参数: 
     * Km(1,3-Bisphosphoglycerate) ~0.1-0.5 mM
     * Km(ADP) ~0.1-0.5 mM
     * Vmax ~500-1000 μmol/min/mg protein
   - 抑制类型: 
     * ATP: 竞争性抑制剂 (与ADP竞争结合位点)，Ki ~0.1-0.5 mM
   - 激活剂: 无强变构激活剂
   - 抑制剂: ATP (产物抑制)
   - 膜定位: 胞浆 (Cytosol)
   - 辅因子: 无，但需要Mg2+作为结构稳定剂
**5. 能量与热力学**: ATP生成: +1, ΔG°' ≈ -18.5 kJ/mol (可逆)

##### 步骤 ID: GLY-08
**1. 反应名称**: 3-磷酸甘油酸变位 (3-Phosphoglycerate Mutase Reaction)
**2. 化学方程式**: 1.0 3-Phosphoglycerate → 1.0 2-Phosphoglycerate
**3. 核心酶信息**: 磷酸甘油酸变位酶 (Phosphoglycerate Mutase), EC 5.4.2.1
**4. 动力学与调控**: 
   - 反应机制: 磷酸转移反应，通过双底物乒乓机制
   - 反应序列: 1) 2,3-二磷酸甘油酸作为辅因子，将磷酸基团转移到酶的组氨酸残基 2) 3-磷酸甘油酸与酶结合，接收磷酸基团生成2,3-二磷酸甘油酸中间物 3) 中间物将C3的磷酸基团转移到酶，生成2-磷酸甘油酸 4) 产物解离，酶恢复磷酸化状态
   - 速率方程: v = Vmax[3-Phosphoglycerate] / (Km(3-Phosphoglycerate) + [3-Phosphoglycerate])
   - 动力学参数: 
     * Km(3-Phosphoglycerate) ~0.5-1.0 mM
     * Km(2-Phosphoglycerate) ~0.5-1.0 mM (反向反应)
     * Vmax ~500-1000 μmol/min/mg protein
   - 抑制类型: 无强变构调控，产物抑制较弱
   - 激活剂: 无强变构激活剂
   - 抑制剂: 无强抑制剂
   - 膜定位: 胞浆 (Cytosol)
   - 辅因子: 2,3-二磷酸甘油酸 (必需的磷酸供体/受体)
**5. 能量与热力学**: ΔG°' ≈ +4.4 kJ/mol (可逆)

##### 步骤 ID: GLY-09
**1. 反应名称**: 2-磷酸甘油酸脱水 (2-Phosphoglycerate Dehydration)
**2. 化学方程式**: 1.0 2-Phosphoglycerate → 1.0 Phosphoenolpyruvate + 1.0 H2O
**3. 核心酶信息**: 烯醇化酶 (Enolase), EC 4.2.1.11
**4. 动力学与调控**: 
   - 反应机制: 脱水反应，通过形成烯二醇中间物
   - 反应序列: 1) 2-磷酸甘油酸与酶结合，Mg2+作为辅因子稳定负电荷 2) 酶催化脱水，形成磷酸烯醇式丙酮酸 3) 产物解离
   - 速率方程: v = Vmax[2-Phosphoglycerate] / (Km(2-Phosphoglycerate) + [2-Phosphoglycerate])
   - 动力学参数: 
     * Km(2-Phosphoglycerate) ~0.1-0.5 mM
     * Vmax ~500-1000 μmol/min/mg protein
   - 抑制类型: 无强变构调控，产物抑制较弱
   - 激活剂: 无强变构激活剂
   - 抑制剂: 无强抑制剂
   - 膜定位: 胞浆 (Cytosol)
   - 辅因子: Mg2+ (必需，稳定反应中间物的负电荷)
**5. 能量与热力学**: ΔG°' ≈ +7.5 kJ/mol (可逆)

##### 步骤 ID: GLY-10
**1. 反应名称**: 磷酸烯醇式丙酮酸底物水平磷酸化 (Phosphoenolpyruvate Substrate-Level Phosphorylation)
**2. 化学方程式**: 1.0 Phosphoenolpyruvate + 1.0 ADP + 1.0 H+ → 1.0 Pyruvate + 1.0 ATP
**3. 核心酶信息**: 丙酮酸激酶 (Pyruvate Kinase), EC 2.7.1.40, 肝脏特异性L型同工酶
**4. 动力学与调控**: 
   - 反应机制: 底物水平磷酸化反应，通过烯醇式-酮式互变
   - 反应序列: 1) 磷酸烯醇式丙酮酸与酶结合，Mg2+作为辅因子 2) ADP与酶结合 3) 磷酸基团转移，同时烯醇式丙酮酸转化为酮式丙酮酸 4) 丙酮酸和ATP解离
   - 速率方程: v = Vmax[Phosphoenolpyruvate][ADP] / (Km(Phosphoenolpyruvate)[ADP] + Km(ADP)[Phosphoenolpyruvate] + [Phosphoenolpyruvate][ADP] + Ki(ATP)[ATP] + Ki(Alanine)[Alanine] + Kact[Fructose-1,6-Bisphosphate])
   - 动力学参数: 
     * Km(Phosphoenolpyruvate) ~0.1-0.5 mM
     * Km(ADP) ~0.1-0.5 mM
     * Vmax ~200-400 μmol/min/mg protein
   - 抑制类型: 
     * ATP: 非竞争性抑制剂，Ki ~0.5-1.0 mM
     * Alanine: 非竞争性抑制剂，Ki ~0.5-1.0 mM
   - 激活剂: 
     * Fructose-1,6-Bisphosphate (别构激活剂，降低Km值)
     * Mg2+ (必需辅因子)
     * K+ (激活剂)
   - 抑制剂: 
     * ATP (能量状态抑制)
     * Alanine (糖异生信号抑制)
     * 胰高血糖素 (通过cAMP-PKA通路磷酸化抑制)
   - 膜定位: 胞浆 (Cytosol)
   - 辅因子: Mg2+ (必需)
   - 磷酸化调控: 
     * 磷酸化状态: Ser-12磷酸化 → 酶活性降低
     * 去磷酸化状态: 去磷酸化 → 酶活性恢复
     * 调控逻辑: 饱食时胰岛素促进去磷酸化激活，饥饿时胰高血糖素促进磷酸化抑制
**5. 能量与热力学**: ATP生成: +1, ΔG°' ≈ -31.4 kJ/mol (不可逆)

#### 糖异生 (Gluconeogenesis)

##### 步骤 ID: GNG-01
**1. 反应名称**: 丙酮酸羧化酶反应 (Pyruvate Carboxylase Reaction)
**2. 化学方程式**: 1.0 Pyruvate + 1.0 HCO3- + 1.0 ATP → 1.0 Oxaloacetate + 1.0 ADP + 1.0 Pi + 1.0 H+
**3. 核心酶信息**: 丙酮酸羧化酶 (Pyruvate Carboxylase, PC), EC 6.4.1.1, 需要生物素作为辅因子
**4. 动力学与调控**: 
   - 反应机制: 生物素依赖性羧化反应，分两步进行
   - 反应序列: 1) ATP活化HCO3-，形成羧基磷酸中间体 2) 羧基转移到生物素辅因子 3) 羧基从生物素转移到丙酮酸，生成草酰乙酸
   - 速率方程: v = Vmax[Pyruvate][HCO3-][ATP] / (Km(Pyruvate)[HCO3-][ATP] + Km(HCO3-)[Pyruvate][ATP] + Km(ATP)[Pyruvate][HCO3-] + [Pyruvate][HCO3-][ATP] + Kact[Acetyl-CoA])
   - 动力学参数: 
     * Km(Pyruvate) ~0.1-0.5 mM
     * Km(HCO3-) ~1.0-5.0 mM
     * Km(ATP) ~0.1-0.5 mM
     * Vmax ~50-100 μmol/min/mg protein
   - 抑制类型: 产物抑制 (草酰乙酸)
   - 激活剂: 
     * Acetyl-CoA (别构激活剂，必需激活剂，降低Km值)
     * Mg2+ (必需辅因子)
     * 生物素 (必需辅因子)
   - 抑制剂: 无强变构抑制剂
   - 非磷酸化修饰: 乙酰化 (Acetylation)
   - 乙酰化位点: Lys-288, Lys-292, Lys-382
   - 乙酰化效应: PC被乙酰化时活性降低50-70%
   - 去乙酰化酶: SIRT3 (线粒体去乙酰化酶)
   - 去乙酰化条件: 饥饿状态下NAD+升高 → SIRT3激活 → PC去乙酰化 → 活性恢复
   - 营养状态逻辑: 
     * 饱食状态: 高乙酰-CoA → PC乙酰化 → 糖异生抑制
     * 饥饿状态: 高NAD+ → SIRT3激活 → PC去乙酰化 → 糖异生激活
   - 膜定位: 线粒体基质 (Mitochondrial matrix)
**5. 能量与热力学**: ATP消耗: -1, ΔG°' ≈ -0.8 kJ/mol (不可逆)
**6. 生理意义**: 糖异生的第一步，将丙酮酸转化为草酰乙酸
**7. PTM调控意义**: 乙酰化作为营养状态传感器，饱食时抑制糖异生，饥饿时激活糖异生

##### 步骤 ID: GNG-02
**1. 反应名称**: 磷酸烯醇式丙酮酸羧激酶反应 (Phosphoenolpyruvate Carboxykinase Reaction)
**2. 化学方程式**: 1.0 Oxaloacetate + 1.0 GTP → 1.0 Phosphoenolpyruvate + 1.0 CO2 + 1.0 GDP
**3. 核心酶信息**: 磷酸烯醇式丙酮酸羧激酶 (Phosphoenolpyruvate Carboxykinase, PEPCK), EC 4.1.1.32
**4. 动力学与调控**: 
   - 反应机制: GTP依赖性脱羧反应
   - 反应序列: 1) 草酰乙酸与酶结合 2) GTP水解提供能量 3) 草酰乙酸脱羧，形成磷酸烯醇式丙酮酸 4) 产物解离
   - 速率方程: v = Vmax[Oxaloacetate][GTP] / (Km(Oxaloacetate)[GTP] + Km(GTP)[Oxaloacetate] + [Oxaloacetate][GTP])
   - 动力学参数: 
     * Km(Oxaloacetate) ~0.01-0.05 mM
     * Km(GTP) ~0.01-0.05 mM
     * Vmax ~50-100 μmol/min/mg protein
   - 抑制类型: 无强变构调控
   - 激活剂: 
     * Mg2+ (必需辅因子)
     * Mn2+ (激活剂)
   - 抑制剂: 无强变构抑制剂
   - 转录调节: 胰高血糖素/Cortisol 上调, Insulin 下调
   - 非磷酸化修饰: 乙酰化 (Acetylation)
   - 乙酰化位点: Lys-70, Lys-71, Lys-285
   - 乙酰化效应: PEPCK被乙酰化时活性降低60-80%
   - 去乙酰化酶: SIRT1 (核/胞浆去乙酰化酶)
   - 去乙酰化条件: 饥饿状态下NAD+升高 → SIRT1激活 → PEPCK去乙酰化 → 活性恢复
   - 营养状态逻辑: 
     * 饱食状态: 高乙酰-CoA → PEPCK乙酰化 → 糖异生抑制
     * 饥饿状态: 高NAD+ → SIRT1激活 → PEPCK去乙酰化 → 糖异生激活
   - 膜定位: 胞浆 (GNG-02) 和线粒体 (另一种同工酶)
   - 辅因子: Mg2+ (必需)
**5. 能量与热力学**: GTP消耗: -1, ΔG°' ≈ +2.9 kJ/mol (不可逆)
**6. 生理意义**: 糖异生的限速步骤，将草酰乙酸转化为磷酸烯醇式丙酮酸
**7. PTM调控意义**: 乙酰化作为营养状态传感器，饱食时抑制糖异生，饥饿时激活糖异生

##### 步骤 ID: GNG-03
**1. 反应名称**: 果糖-1,6-二磷酸酶反应 (Fructose-1,6-bisphosphatase Reaction)
**2. 化学方程式**: 1.0 Fructose-1,6-Bisphosphate + 1.0 H2O → 1.0 Fructose-6-Phosphate + 1.0 Pi
**3. 核心酶信息**: 果糖-1,6-二磷酸酶 (Fructose-1,6-bisphosphatase), EC 3.1.3.11
**4. 动力学与调控**: 
   - 反应机制: 水解反应，特异性水解C1位的磷酸酯键
   - 反应序列: 1) 果糖-1,6-二磷酸与酶结合 2) 酶催化C1位磷酸酯键水解 3) 释放果糖-6-磷酸和无机磷酸
   - 速率方程: v = Vmax[Fructose-1,6-Bisphosphate] / (Km(Fructose-1,6-Bisphosphate) + [Fructose-1,6-Bisphosphate] + Ki(Fructose-2,6-Bisphosphate)[Fructose-2,6-Bisphosphate] + Ki(AMP)[AMP])
   - 动力学参数: 
     * Km(Fructose-1,6-Bisphosphate) ~0.1-0.5 mM
     * Vmax ~100-200 μmol/min/mg protein
   - 抑制类型: 
     * Fructose-2,6-Bisphosphate: 竞争性抑制剂，Ki ~0.001-0.01 mM
     * AMP: 非竞争性抑制剂，Ki ~0.1-0.5 mM
   - 激活剂: 
     * Mg2+ (必需辅因子)
     * Citrate (别构激活剂)
   - 抑制剂: 
     * Fructose-2,6-Bisphosphate (强力抑制剂，糖酵解/糖异生的关键调控物)
     * AMP (能量状态抑制剂)
     * ATP (轻微激活剂，与AMP竞争)
   - 膜定位: 胞浆 (Cytosol)
   - 辅因子: Mg2+ (必需)
**5. 能量与热力学**: ΔG°' ≈ -8.6 kJ/mol (不可逆)

##### 步骤 ID: GNG-04
**1. 反应名称**: 葡萄糖-6-磷酸酶反应 (Glucose-6-phosphatase Reaction)
**2. 化学方程式**: 1.0 Glucose-6-Phosphate + 1.0 H2O → 1.0 Glucose + 1.0 Pi
**3. 核心酶信息**: 葡萄糖-6-磷酸酶 (Glucose-6-phosphatase), EC 3.1.3.9, 位于内质网膜
**4. 动力学与调控**: 
   - 反应机制: 水解反应，位于内质网膜上的多酶复合体
   - 反应序列: 1) 葡萄糖-6-磷酸从胞浆转运到内质网腔 2) 葡萄糖-6-磷酸酶催化磷酸酯键水解 3) 葡萄糖和无机磷酸转运回胞浆
   - 速率方程: v = Vmax[Glucose-6-Phosphate] / (Km(Glucose-6-Phosphate) + [Glucose-6-Phosphate])
   - 动力学参数: 
     * Km(Glucose-6-Phosphate) ~1.0-5.0 mM
     * Vmax ~50-100 μmol/min/mg protein
   - 抑制类型: 无强变构调控
   - 激活剂: 
     * Mg2+ (必需辅因子)
   - 抑制剂: 无强变构抑制剂
   - 转录调节: 胰高血糖素/Cortisol 上调, Insulin 下调
   - 膜定位: 内质网膜 (Endoplasmic reticulum membrane)
   - 辅因子: Mg2+ (必需)
   - 复合体组成: 葡萄糖-6-磷酸酶催化亚基 (G6PC) 和转运蛋白 (G6PT)
**5. 能量与热力学**: ΔG°' ≈ -13.8 kJ/mol (不可逆)

### 非磷酸化修饰网络 (Non-Canonical PTMs)

#### 乙酰化-能量感应 (Acetylation - Energy Sensing)

##### 步骤 ID: PTM-ACET-01
**1. 反应名称**: SIRT1去乙酰化PGC-1α (SIRT1 Deacetylation of PGC-1α)
**2. 化学方程式**: 
   - 饱食状态: PGC-1α-Acetyl + 高乙酰-CoA → PGC-1α-Acetyl (持续乙酰化)
   - 饥饿状态: PGC-1α-Acetyl + 高NAD+ + SIRT1 → PGC-1α + Acetyl-NAD+ + 去乙酰化PGC-1α
**3. 核心酶信息**: 
   - SIRT1 (Sirtuin 1), EC 3.5.1.98, NAD+依赖性去乙酰化酶
   - PGC-1α (过氧化物酶体增殖物激活受体γ共激活因子-1α), 转录共激活因子
**4. 动力学与调控**: 
   - SIRT1 Km(NAD+) ~0.1-0.5 mM
   - 激活条件: 饥饿状态下NAD+升高 (> 0.5 mM) → SIRT1激活
   - 抑制条件: 饱食状态下NADH升高 → NAD+/NADH比率下降 → SIRT1活性降低
   - 乙酰化位点: PGC-1α的多个赖氨酸位点 (Lys-224, Lys-313, Lys-738等)
   - 去乙酰化效应: PGC-1α去乙酰化后活性增加3-5倍
**5. 能量与热力学**: NAD+消耗: -1 (去乙酰化反应), ΔG°' ≈ -15 kJ/mol (不可逆)
**6. 功能说明**: 
   - 饥饿状态: 高NAD+ → SIRT1激活 → PGC-1α去乙酰化 → PGC-1α活性增加
   - PGC-1α激活 → 促进线粒体增生和生物合成
   - 线粒体增生 → 增强脂肪酸氧化和糖异生能力
**7. 生理意义**: 
   - 饥饿时的适应性反应，增强肝脏的能量产生能力
   - 通过PGC-1α去乙酰化调控线粒体数量和功能
   - 连接营养状态（NAD+水平）与代谢适应（线粒体增生）
**8. PTM调控意义**: 
   - 乙酰化作为营养状态的分子开关
   - 饱食时：PGC-1α乙酰化 → 线粒体增生抑制 → 节能模式
   - 饥饿时：PGC-1α去乙酰化 → 线粒体增生激活 → 产能模式

##### 步骤 ID: PTM-ACET-02
**1. 反应名称**: 乙酰化修饰的糖异生酶调控 (Acetylation Regulation of Gluconeogenic Enzymes)
**2. 化学方程式**: 
   - 饱食状态: PC/PEPCK + 高乙酰-CoA + GCN5 → PC/PEPCK-Acetyl + CoA-SH
   - 饥饿状态: PC/PEPCK-Acetyl + 高NAD+ + SIRT3/SIRT1 → PC/PEPCK + Acetyl-NAD+
**3. 核心酶信息**: 
   - GCN5 (组蛋白乙酰转移酶5), EC 2.3.1.48, 乙酰转移酶
   - SIRT3 (Sirtuin 3), EC 3.5.1.98, 线粒体去乙酰化酶
   - SIRT1 (Sirtuin 1), EC 3.5.1.98, 核/胞浆去乙酰化酶
**4. 动力学与调控**: 
   - GCN5 Km(乙酰-CoA) ~0.1-0.5 mM
   - 激活条件: 饱食状态下乙酰-CoA升高 (> 0.5 mM) → GCN5激活
   - 抑制条件: 饥饿状态下NAD+升高 → SIRT3/SIRT1激活 → 去乙酰化
   - 乙酰化效应: PC/PEPCK被乙酰化时活性降低50-80%
   - 去乙酰化效应: PC/PEPCK去乙酰化时活性恢复到正常水平
**5. 能量与热力学**: 
   - 乙酰化: 无直接能量消耗
   - 去乙酰化: NAD+消耗 -1, ΔG°' ≈ -15 kJ/mol (不可逆)
**6. 功能说明**: 
   - 饱食状态: 高乙酰-CoA → PC/PEPCK乙酰化 → 糖异生抑制
   - 饥饿状态: 高NAD+ → SIRT3/SIRT1激活 → PC/PEPCK去乙酰化 → 糖异生激活
**7. 生理意义**: 
   - 乙酰化作为营养状态的精细调控机制
   - 饱食时抑制糖异生，避免不必要的葡萄糖合成
   - 饥饿时激活糖异生，维持血糖稳定
**8. PTM调控意义**: 
   - 乙酰化修饰提供比转录调控更快速的酶活性调节
   - 连接营养状态（乙酰-CoA/NAD+比率）与代谢适应（糖异生活性）

#### 糖原合成与分解 (Glycogen Metabolism)

##### 步骤 ID: GLG-01
**1. 反应名称**: 糖原合成 (Glycogen Synthesis)
**2. 化学方程式**: 1.0 UDP-Glucose + (Glycogen)n → (Glycogen)n+1 + 1.0 UDP
**3. 核心酶信息**: 糖原合酶 (Glycogen Synthase), EC 2.4.1.11, 糖原合成限速酶
**4. 动力学与调控**: Km(UDP-Glucose) ~0.1-0.5 mM; 激活剂: Glucose-6-Phosphate; 共价修饰: Insulin 激活(去磷酸化), 胰高血糖素/肾上腺素 抑制(磷酸化)
**5. 能量与热力学**: ΔG°' ≈ -13.4 kJ/mol (可逆)

##### 步骤 ID: GLG-02
**1. 反应名称**: 糖原分解 (Glycogenolysis)
**2. 化学方程式**: (Glycogen)n + 1.0 Pi → (Glycogen)n-1 + 1.0 Glucose-1-Phosphate
**3. 核心酶信息**: 糖原磷酸化酶 (Glycogen Phosphorylase), EC 2.4.1.1, 糖原分解限速酶
**4. 动力学与调控**: Km(Glycogen) ~0.1-0.5 mM; 激活剂: AMP; 抑制剂: Glucose; 共价修饰: 胰高血糖素/肾上腺素 激活(磷酸化), Insulin 抑制(去磷酸化)
**5. 能量与热力学**: ΔG°' ≈ +3.1 kJ/mol (可逆)

##### 步骤 ID: GLG-03
**1. 反应名称**: 葡萄糖-1-磷酸转位 (Glucose-1-Phosphate Mutase Reaction)
**2. 化学方程式**: 1.0 Glucose-1-Phosphate → 1.0 Glucose-6-Phosphate
**3. 核心酶信息**: 磷酸葡萄糖变位酶 (Phosphoglucomutase), EC 5.4.2.2
**4. 动力学与调控**: Km(Glucose-1-Phosphate) ~0.1-0.5 mM; 需要葡萄糖-1,6-二磷酸作为辅因子
**5. 能量与热力学**: ΔG°' ≈ +7.3 kJ/mol (可逆)

##### 步骤 ID: GLG-04
**1. 反应名称**: UDP-葡萄糖焦磷酸化酶反应 (UDP-Glucose Pyrophosphorylase Reaction)
**2. 化学方程式**: 1.0 Glucose-1-Phosphate + 1.0 UTP → 1.0 UDP-Glucose + 1.0 PPi
**3. 核心酶信息**: UDP-葡萄糖焦磷酸化酶 (UDP-Glucose Pyrophosphorylase), EC 2.7.7.9
**4. 动力学与调控**: Km(Glucose-1-Phosphate) ~0.1-0.5 mM; Km(UTP) ~0.1-0.5 mM
**5. 能量与热力学**: ΔG°' ≈ 0 kJ/mol (可逆，因PPi水解而正向进行)

##### 步骤 ID: GLG-05
**1. 反应名称**: 糖原分支酶反应 (Glycogen Branching Enzyme Reaction)
**2. 化学方程式**: (Glycogen linear chain) → (Glycogen branched chain)
**3. 核心酶信息**: 糖原分支酶 (Glycogen Branching Enzyme), EC 2.4.1.18
**4. 动力学与调控**: 无强变构调控
**5. 能量与热力学**: ΔG°' ≈ 0 kJ/mol (可逆)

##### 步骤 ID: GLG-06
**1. 反应名称**: 糖原脱支酶反应 (Glycogen Debranching Enzyme Reaction)
**2. 化学方程式**: (Glycogen branched chain) → (Glycogen linear chain) + 1.0 Glucose
**3. 核心酶信息**: 糖原脱支酶 (Glycogen Debranching Enzyme), EC 3.2.1.33
**4. 动力学与调控**: 无强变构调控
**5. 能量与热力学**: ΔG°' ≈ -15 kJ/mol (可逆)

##### 步骤 ID: GLG-07
**1. 反应名称**: 磷酸葡萄糖变位酶反应 (Phosphoglucomutase Reaction)
**2. 化学方程式**: 1.0 Glucose-6-Phosphate → 1.0 Glucose-1-Phosphate
**3. 核心酶信息**: 磷酸葡萄糖变位酶 (Phosphoglucomutase), EC 5.4.2.2
**4. 动力学与调控**: Km(Glucose-6-Phosphate) ~0.1-0.5 mM; 需要葡萄糖-1,6-二磷酸作为辅因子
**5. 能量与热力学**: ΔG°' ≈ -7.3 kJ/mol (可逆)

##### 步骤 ID: GLG-08
**1. 反应名称**: 葡萄糖-6-磷酸转葡萄糖 (Glucose-6-Phosphatase Reaction)
**2. 化学方程式**: 1.0 Glucose-6-Phosphate + 1.0 H2O → 1.0 Glucose + 1.0 Pi
**3. 核心酶信息**: 葡萄糖-6-磷酸酶 (Glucose-6-phosphatase), EC 3.1.3.9
**4. 动力学与调控**: Km(Glucose-6-Phosphate) ~1.0-5.0 mM; 转录调节: 胰高血糖素/Cortisol 上调, Insulin 下调
**5. 能量与热力学**: ΔG°' ≈ -13.8 kJ/mol (不可逆)

#### 磷酸戊糖途径 (Pentose Phosphate Pathway, PPP)

##### 步骤 ID: PPP-01
**1. 反应名称**: 葡萄糖-6-磷酸脱氢酶反应 (Glucose-6-Phosphate Dehydrogenase Reaction)
**2. 化学方程式**: 1.0 Glucose-6-Phosphate + 1.0 NADP+ → 1.0 6-Phosphogluconolactone + 1.0 NADPH + 1.0 H+
**3. 核心酶信息**: 葡萄糖-6-磷酸脱氢酶 (Glucose-6-Phosphate Dehydrogenase), EC 1.1.1.49, PPP限速酶
**4. 动力学与调控**: Km(Glucose-6-Phosphate) ~0.1-0.5 mM; 激活剂: NADP+; 抑制剂: NADPH
**5. 能量与热力学**: ΔG°' ≈ -17.7 kJ/mol (不可逆)

##### 步骤 ID: PPP-02
**1. 反应名称**: 6-磷酸葡萄糖酸内酯酶反应 (6-Phosphogluconolactonase Reaction)
**2. 化学方程式**: 1.0 6-Phosphogluconolactone + 1.0 H2O → 1.0 6-Phosphogluconate + 1.0 H+
**3. 核心酶信息**: 6-磷酸葡萄糖酸内酯酶 (6-Phosphogluconolactonase), EC 3.1.1.31
**4. 动力学与调控**: Km(6-Phosphogluconolactone) ~0.1-0.5 mM; 无强变构调控
**5. 能量与热力学**: ΔG°' ≈ -16.3 kJ/mol (不可逆)

##### 步骤 ID: PPP-03
**1. 反应名称**: 6-磷酸葡萄糖酸脱氢酶反应 (6-Phosphogluconate Dehydrogenase Reaction)
**2. 化学方程式**: 1.0 6-Phosphogluconate + 1.0 NADP+ → 1.0 Ribulose-5-Phosphate + 1.0 CO2 + 1.0 NADPH + 1.0 H+
**3. 核心酶信息**: 6-磷酸葡萄糖酸脱氢酶 (6-Phosphogluconate Dehydrogenase), EC 1.1.1.44
**4. 动力学与调控**: Km(6-Phosphogluconate) ~0.1-0.5 mM; 激活剂: NADP+; 抑制剂: NADPH
**5. 能量与热力学**: ΔG°' ≈ -12.5 kJ/mol (不可逆)

##### 步骤 ID: PPP-04
**1. 反应名称**: 核糖-5-磷酸异构酶反应 (Ribose-5-Phosphate Isomerase Reaction)
**2. 化学方程式**: 1.0 Ribulose-5-Phosphate → 1.0 Ribose-5-Phosphate
**3. 核心酶信息**: 核糖-5-磷酸异构酶 (Ribose-5-Phosphate Isomerase), EC 5.3.1.6
**4. 动力学与调控**: Km(Ribulose-5-Phosphate) ~0.1-0.5 mM; 无强变构调控
**5. 能量与热力学**: ΔG°' ≈ +2.5 kJ/mol (可逆)

##### 步骤 ID: PPP-05
**1. 反应名称**: 木酮糖-5-磷酸差向异构酶反应 (Xylulose-5-Phosphate Epimerase Reaction)
**2. 化学方程式**: 1.0 Ribulose-5-Phosphate → 1.0 Xylulose-5-Phosphate
**3. 核心酶信息**: 木酮糖-5-磷酸差向异构酶 (Xylulose-5-Phosphate Epimerase), EC 5.1.3.1
**4. 动力学与调控**: Km(Ribulose-5-Phosphate) ~0.1-0.5 mM; 无强变构调控
**5. 能量与热力学**: ΔG°' ≈ -1.7 kJ/mol (可逆)

##### 步骤 ID: PPP-06
**1. 反应名称**: 转酮醇酶反应 (Transketolase Reaction)
**2. 化学方程式**: 1.0 Xylulose-5-Phosphate + 1.0 Ribose-5-Phosphate → 1.0 Glyceraldehyde-3-Phosphate + 1.0 Sedoheptulose-7-Phosphate
**3. 核心酶信息**: 转酮醇酶 (Transketolase), EC 2.2.1.1, 需要TPP作为辅因子
**4. 动力学与调控**: Km(Xylulose-5-Phosphate) ~0.1-0.5 mM; Km(Ribose-5-Phosphate) ~0.1-0.5 mM
**5. 能量与热力学**: ΔG°' ≈ +0.4 kJ/mol (可逆)

##### 步骤 ID: PPP-07
**1. 反应名称**: 转醛醇酶反应 (Transaldolase Reaction)
**2. 化学方程式**: 1.0 Sedoheptulose-7-Phosphate + 1.0 Glyceraldehyde-3-Phosphate → 1.0 Erythrose-4-Phosphate + 1.0 Fructose-6-Phosphate
**3. 核心酶信息**: 转醛醇酶 (Transaldolase), EC 2.2.1.2
**4. 动力学与调控**: Km(Sedoheptulose-7-Phosphate) ~0.1-0.5 mM; Km(Glyceraldehyde-3-Phosphate) ~0.1-0.5 mM
**5. 能量与热力学**: ΔG°' ≈ -2.4 kJ/mol (可逆)

##### 步骤 ID: PPP-08
**1. 反应名称**: 转酮醇酶反应 (Transketolase Reaction)
**2. 化学方程式**: 1.0 Xylulose-5-Phosphate + 1.0 Erythrose-4-Phosphate → 1.0 Glyceraldehyde-3-Phosphate + 1.0 Fructose-6-Phosphate
**3. 核心酶信息**: 转酮醇酶 (Transketolase), EC 2.2.1.1, 需要TPP作为辅因子
**4. 动力学与调控**: Km(Xylulose-5-Phosphate) ~0.1-0.5 mM; Km(Erythrose-4-Phosphate) ~0.1-0.5 mM
**5. 能量与热力学**: ΔG°' ≈ -1.3 kJ/mol (可逆)

##### 步骤 ID: PPP-09
**1. 反应名称**: TPP 从头合成 (Thiamine Pyrophosphokinase Reaction)
**2. 化学方程式**: 1.0 Thiamine (维生素B1) + 1.0 ATP → 1.0 TPP (硫胺素焦磷酸) + 1.0 AMP
**3. 核心酶信息**: 硫胺素焦磷酸激酶 (TPK1), EC 2.7.6.2，基因型: TPK1
**4. 动力学与调控**: 
   - Km(Thiamine) ~0.01-0.05 mM
   - 激活剂: Mg2+, ATP
   - 抑制剂: 硫胺素类似物 (如 oxythiamine)
   - 膜定位: 胞浆 (Cytosol)
**5. 能量与热力学**: ATP 消耗: -1, ΔG°' ≈ -30 kJ/mol (不可逆)
**6. 生理意义**: 从头合成转酮醇酶必需的 TPP 辅因子，维持 PPP 氧化分支功能
**7. 病理结局**: 
   - 维生素 B1 缺乏: TPP 合成不足 → 转酮醇酶活性下降 → PPP 受阻 → NADPH 生成减少 → 氧化应激
   - 硫胺素缺乏症: 脚气病，Wernicke-Korsakoff 综合征

##### 步骤 ID: PPP-10
**1. 反应名称**: NADPH 氧化还原平衡 (NADPH Redox Balance)
**2. 化学方程式**: 1.0 NADPH + 1.0 H+ + 1.0 GSSG → 1.0 NADP+ + 2.0 GSH
**3. 核心酶信息**: 谷胱甘肽还原酶 (Glutathione Reductase), EC 1.8.1.7，基因型: GSR
**4. 动力学与调控**: 
   - Km(NADPH) ~0.01-0.05 mM
   - 激活剂: FAD (辅因子)
   - 抑制剂: 高浓度 GSH (产物抑制)
   - 膜定位: 胞浆 (Cytosol)
**5. 能量与热力学**: ΔG°' ≈ -20 kJ/mol (可逆)
**6. 生理意义**: 将 NADPH 的还原力转移到 GSH，维持细胞抗氧化能力
**7. 病理结局**: 
   - GSR 缺陷: GSH 再生受阻 → 氧化应激 → 溶血性贫血
   - NADPH 耗尽: 无法再生 GSH → 细胞氧化损伤 → 凋亡

##### 步骤 ID: PPP-11
**1. 反应名称**: PRPP 合成 (PRPP Synthetase)
**2. 化学方程式**: 1.0 Ribose-5-Phosphate + 1.0 ATP → 1.0 PRPP (5-磷酸核糖-1-焦磷酸) + 1.0 AMP
**3. 核心酶信息**: 磷酸核糖焦磷酸合成酶 (PRPP Synthetase), EC 2.7.6.1，基因型: PRPS1, PRPS2
**4. 动力学与调控**: 
   - Km(Ribose-5-Phosphate) ~0.05-0.1 mM
   - 激活剂: Mg2+, Pi
   - 抑制剂: ADP, GDP (产物抑制)
   - 膜定位: 胞浆 (Cytosol)
**5. 能量与热力学**: ATP 消耗: -1, ΔG°' ≈ -30 kJ/mol (不可逆)
**6. 生理意义**: 生成 PRPP，作为嘌呤/嘧啶从头合成的关键前体，连接 PPP 和核酸合成
**7. 病理结局**: 
   - PRPS1 过表达: Lesch-Nyhan 综合征，痛风，神经发育异常
   - PRPS1 缺陷: 免疫缺陷，生长迟缓

### 脂质代谢

#### 脂肪酸转运与摄取 (Fatty Acid Transport and Uptake)

##### 步骤 ID: LIP-11
**1. 反应名称**: 长链脂肪酸跨膜转运 (Long-Chain Fatty Acid Transmembrane Transport)
**2. 化学方程式**: Fatty Acid(blood) ⇌ Fatty Acid(cytosol)
**3. 核心酶信息**: CD36 / FATP 家族 / FABP 协助，基因型: CD36, SLC27A1-6
**4. 动力学与调控**: 
   - Km(Fatty Acid) ~0.1-0.5 mM
   - 转运机制: 被动/促进扩散 + 蛋白协助，不直接消耗ATP
   - 调控: 胰岛素促进CD36/FATP膜转位表达
   - 膜定位: 基底膜 (Basolateral membrane)
**5. 能量与热力学**: ΔG°' ≈ 0 kJ/mol (可逆)
**6. 生理意义**: 介导脂肪酸入胞；细胞内后续由Acyl-CoA synthetase活化（ATP→AMP+PPi）
**7. 病理结局**: 
   - CD36 过表达: 脂肪酸摄取过多 → 脂质堆积 → 脂肪肝
   - CD36 缺陷: 脂肪酸摄取减少 → 能量代谢异常

##### 步骤 ID: LIP-12
**1. 反应名称**: 肉碱循环 (Carnitine Cycle)
**2. 化学方程式**: 
   - 胞浆: Fatty Acyl-CoA + Carnitine → Fatty Acyl-Carnitine + CoA-SH
   - 线粒体: Fatty Acyl-Carnitine → Fatty Acyl-CoA + Carnitine
**3. 核心酶信息**: 
   - CPT1 (Carnitine Palmitoyltransferase I), EC 2.3.1.21，基因型: CPT1A, CPT1B
   - CACT (Carnitine Acylcarnitine Translocase), 基因型: SLC25A20
   - CPT2 (Carnitine Palmitoyltransferase II), EC 2.3.1.21，基因型: CPT2
**4. 动力学与调控**: 
   - CPT1 Km(Fatty Acyl-CoA) ~0.1-0.5 mM
   - 激活剂: 丙二酰-CoA (饥饿时降低)
   - 抑制剂: 丙二酰-CoA (饱食时升高，抑制 CPT1)
   - 膜定位: CPT1 (线粒体外膜), CACT (线粒体内膜), CPT2 (线粒体内膜)
**5. 能量与热力学**: ΔG°' ≈ 0 kJ/mol (可逆)
**6. 生理意义**: 将长链脂肪酸转运进入线粒体进行 β-氧化，是脂肪酸氧化的关键步骤
**7. 病理结局**: 
   - CPT1 缺陷: 肉碱棕榈酰转移酶 I 缺乏症，低酮性低血糖，肌肉无力
   - CPT1 抑制: 脂肪酸氧化受阻 → 脂质堆积 → 脂肪肝

#### 脂肪酸 β-氧化 (Fatty Acid β-Oxidation)

##### 步骤 ID: LIP-01
**1. 反应名称**: 脂肪酸活化 (Fatty Acid Activation)
**2. 化学方程式**: 1.0 Fatty Acid + 1.0 ATP + 1.0 CoA-SH → 1.0 Fatty Acyl-CoA + 1.0 AMP + 2.0 PPi
**3. 核心酶信息**: 脂酰-CoA合成酶 (Acyl-CoA Synthetase), EC 6.2.1.3
**4. 动力学与调控**: Km(Fatty Acid) ~0.1-0.5 mM; 需要Mg2+作为辅因子
**5. 能量与热力学**: ATP消耗: -2 (因2个PPi水解), ΔG°' ≈ -34 kJ/mol (不可逆)

##### 步骤 ID: LIP-02
**1. 反应名称**: 脂酰-CoA转运 (Fatty Acyl-CoA Transport)
**2. 化学方程式**: 1.0 Fatty Acyl-CoA (胞浆) + 1.0 Carnitine → 1.0 Fatty Acyl-Carnitine + 1.0 CoA-SH
**3. 核心酶信息**: 肉碱棕榈酰转移酶 I (Carnitine Palmitoyltransferase I), EC 2.3.1.21, 脂肪酸β-氧化限速酶
**4. 动力学与调控**: Km(Fatty Acyl-CoA) ~0.1-0.5 mM; 抑制剂: Malonyl-CoA
**5. 能量与热力学**: ΔG°' ≈ 0 kJ/mol (可逆)

##### 步骤 ID: LIP-03
**1. 反应名称**: 脂酰-CoA脱氢 (Fatty Acyl-CoA Dehydrogenation)
**2. 化学方程式**: 1.0 Fatty Acyl-CoA + 1.0 FAD → 1.0 Enoyl-CoA + 1.0 FADH2
**3. 核心酶信息**: 脂酰-CoA脱氢酶 (Acyl-CoA Dehydrogenase), EC 1.3.8.7
**4. 动力学与调控**: Km(Fatty Acyl-CoA) ~0.1-0.5 mM
**5. 能量与热力学**: ΔG°' ≈ -15 kJ/mol (可逆)

##### 步骤 ID: LIP-04
**1. 反应名称**: 烯酰-CoA水合 (Enoyl-CoA Hydration)
**2. 化学方程式**: 1.0 Enoyl-CoA + 1.0 H2O → 1.0 3-Hydroxyacyl-CoA
**3. 核心酶信息**: 烯酰-CoA水合酶 (Enoyl-CoA Hydratase), EC 4.2.1.17
**4. 动力学与调控**: Km(Enoyl-CoA) ~0.1-0.5 mM
**5. 能量与热力学**: ΔG°' ≈ -3 kJ/mol (可逆)

##### 步骤 ID: LIP-05
**1. 反应名称**: 3-羟基脂酰-CoA脱氢 (3-Hydroxyacyl-CoA Dehydrogenation)
**2. 化学方程式**: 1.0 3-Hydroxyacyl-CoA + 1.0 NAD+ → 1.0 3-Ketoacyl-CoA + 1.0 NADH + 1.0 H+
**3. 核心酶信息**: 3-羟基脂酰-CoA脱氢酶 (3-Hydroxyacyl-CoA Dehydrogenase), EC 1.1.1.35
**4. 动力学与调控**: Km(3-Hydroxyacyl-CoA) ~0.1-0.5 mM
**5. 能量与热力学**: ΔG°' ≈ -15 kJ/mol (可逆)

##### 步骤 ID: LIP-06
**1. 反应名称**: 硫解酶反应 (Thiolase Reaction)
**2. 化学方程式**: 1.0 3-Ketoacyl-CoA + 1.0 CoA-SH → 1.0 Acetyl-CoA + 1.0 Fatty Acyl-CoA (缩短2个碳原子)
**3. 核心酶信息**: β-酮硫解酶 (β-Ketothiolase), EC 2.3.1.16
**4. 动力学与调控**: Km(3-Ketoacyl-CoA) ~0.1-0.5 mM
**5. 能量与热力学**: ΔG°' ≈ -28 kJ/mol (可逆)

#### 脂肪酸合成 (Fatty Acid Synthesis)

##### 步骤 ID: LIP-07
**1. 反应名称**: 乙酰-CoA羧化 (Acetyl-CoA Carboxylation)
**2. 化学方程式**: 1.0 Acetyl-CoA + 1.0 HCO3- + 1.0 ATP → 1.0 Malonyl-CoA + 1.0 ADP + 1.0 Pi + 1.0 H+
**3. 核心酶信息**: 乙酰-CoA羧化酶 (Acetyl-CoA Carboxylase), EC 6.4.1.2, 脂肪酸合成限速酶
**4. 动力学与调控**: Km(Acetyl-CoA) ~0.1-0.5 mM; 激活剂: Citrate, Insulin; 抑制剂: Palmitoyl-CoA, Glucagon
**5. 能量与热力学**: ATP消耗: -1, ΔG°' ≈ -25 kJ/mol (不可逆)

##### 步骤 ID: LIP-08
**1. 反应名称**: 脂肪酸合酶反应 (Fatty Acid Synthase Reaction)
**2. 化学方程式**: 1.0 Acetyl-CoA + 7.0 Malonyl-CoA + 14.0 NADPH + 14.0 H+ → 1.0 Palmitate + 7.0 CO2 + 8.0 CoA-SH + 14.0 NADP+ + 6.0 H2O
**3. 核心酶信息**: 脂肪酸合酶 (Fatty Acid Synthase), EC 2.3.1.85
**4. 动力学与调控**: 激活剂: Insulin; 抑制剂: Glucagon, Palmitoyl-CoA
**5. 能量与热力学**: NADPH消耗: -14, ΔG°' ≈ -32 kJ/mol (不可逆)

#### 甘油三酯合成 (Triglyceride Synthesis)

##### 步骤 ID: LIP-09
**1. 反应名称**: 甘油磷酸化 (Glycerol Phosphorylation)
**2. 化学方程式**: 1.0 Glycerol + 1.0 ATP → 1.0 Glycerol-3-Phosphate + 1.0 ADP + 1.0 H+
**3. 核心酶信息**: 甘油激酶 (Glycerol Kinase), EC 2.7.1.30
**4. 动力学与调控**: Km(Glycerol) ~0.1-0.5 mM
**5. 能量与热力学**: ATP消耗: -1, ΔG°' ≈ -9 kJ/mol (不可逆)

##### 步骤 ID: LIP-10
**1. 反应名称**: 甘油三酯合成 (Triglyceride Synthesis)
**2. 化学方程式**: 1.0 Glycerol-3-Phosphate + 3.0 Fatty Acyl-CoA → 1.0 Triglyceride + 3.0 CoA-SH + 1.0 Pi
**3. 核心酶信息**: 甘油三酯合成酶 (Triglyceride Synthase), EC 2.3.1.20
**4. 动力学与调控**: 激活剂: Insulin; 抑制剂: Glucagon
**5. 能量与热力学**: ΔG°' ≈ -30 kJ/mol (不可逆)

#### 酮体生成 (Ketogenesis)

##### 步骤 ID: LIP-11
**1. 反应名称**: 乙酰-CoA缩合 (Acetyl-CoA Condensation)
**2. 化学方程式**: 2.0 Acetyl-CoA → 1.0 Acetoacetyl-CoA + 1.0 CoA-SH
**3. 核心酶信息**: 硫解酶 (Thiolase), EC 2.3.1.9
**4. 动力学与调控**: Km(Acetyl-CoA) ~0.1-0.5 mM; 激活剂: 高浓度乙酰-CoA
**5. 能量与热力学**: ΔG°' ≈ +7 kJ/mol (可逆，因产物消耗而正向进行)

##### 步骤 ID: LIP-12
**1. 反应名称**: HMG-CoA合成 (HMG-CoA Synthesis)
**2. 化学方程式**: 1.0 Acetoacetyl-CoA + 1.0 Acetyl-CoA + 1.0 H2O → 1.0 HMG-CoA + 1.0 CoA-SH
**3. 核心酶信息**: HMG-CoA合成酶 (HMG-CoA Synthase), EC 2.3.3.10, 酮体生成限速酶
**4. 动力学与调控**: Km(Acetoacetyl-CoA) ~0.1-0.5 mM
**5. 能量与热力学**: ΔG°' ≈ -16 kJ/mol (不可逆)

##### 步骤 ID: LIP-13
**1. 反应名称**: 酮体生成 (Ketone Body Formation)
**2. 化学方程式**: 1.0 HMG-CoA → 1.0 Acetoacetate + 1.0 Acetyl-CoA
**3. 核心酶信息**: HMG-CoA裂解酶 (HMG-CoA Lyase), EC 4.1.3.4
**4. 动力学与调控**: Km(HMG-CoA) ~0.1-0.5 mM
**5. 能量与热力学**: ΔG°' ≈ -3.5 kJ/mol (可逆)

##### 步骤 ID: LIP-14
**1. 反应名称**: β-羟丁酸生成 (β-Hydroxybutyrate Formation)
**2. 化学方程式**: 1.0 Acetoacetate + 1.0 NADH + 1.0 H+ → 1.0 β-Hydroxybutyrate + 1.0 NAD+
**3. 核心酶信息**: β-羟丁酸脱氢酶 (β-Hydroxybutyrate Dehydrogenase), EC 1.1.1.30
**4. 动力学与调控**: Km(Acetoacetate) ~0.1-0.5 mM
**5. 能量与热力学**: ΔG°' ≈ -25 kJ/mol (可逆)

#### 胆固醇合成 (Cholesterol Synthesis)

##### 步骤 ID: LIP-15
**1. 反应名称**: 甲羟戊酸生成 (Mevalonate Formation)
**2. 化学方程式**: 3.0 Acetyl-CoA + 2.0 NADPH + 2.0 H+ + 1.0 ATP → 1.0 Mevalonate + 3.0 CoA-SH + 2.0 NADP+ + 1.0 ADP + 1.0 Pi
**3. 核心酶信息**: HMG-CoA还原酶 (HMG-CoA Reductase), EC 1.1.1.34, 胆固醇合成限速酶
**4. 动力学与调控**: 激活剂: Insulin; 抑制剂: Glucagon, Cholesterol, Statins
**5. 能量与热力学**: ATP消耗: -1, NADPH消耗: -2, ΔG°' ≈ -18 kJ/mol (不可逆)

##### 步骤 ID: LIP-16
**1. 反应名称**: 胆固醇合成 (Cholesterol Synthesis)
**2. 化学方程式**: 1.0 Mevalonate → 1.0 Cholesterol (多步反应)
**3. 核心酶信息**: 多种酶参与
**4. 动力学与调控**: 复杂的反馈调控
**5. 能量与热力学**: 总ATP消耗: -18, 总NADPH消耗: -16

### 氨基酸基本代谢

#### 转氨基反应 (Transamination Reactions)

##### 步骤 ID: AA-01
**1. 反应名称**: 丙氨酸转氨基 (Alanine Transamination)
**2. 化学方程式**: 1.0 Alanine + 1.0 α-Ketoglutarate → 1.0 Pyruvate + 1.0 Glutamate
**3. 核心酶信息**: 丙氨酸转氨酶 (Alanine Aminotransferase), EC 2.6.1.2
**4. 动力学与调控**: Km(Alanine) ~0.5-1.0 mM; Km(α-Ketoglutarate) ~0.1-0.5 mM
**5. 能量与热力学**: ΔG°' ≈ 0 kJ/mol (可逆)

##### 步骤 ID: AA-02
**1. 反应名称**: 天冬氨酸转氨基 (Aspartate Transamination)
**2. 化学方程式**: 1.0 Aspartate + 1.0 α-Ketoglutarate → 1.0 Oxaloacetate + 1.0 Glutamate
**3. 核心酶信息**: 天冬氨酸转氨酶 (Aspartate Aminotransferase), EC 2.6.1.1
**4. 动力学与调控**: Km(Aspartate) ~0.5-1.0 mM; Km(α-Ketoglutarate) ~0.1-0.5 mM
**5. 能量与热力学**: ΔG°' ≈ 0 kJ/mol (可逆)

##### 步骤 ID: AA-03
**1. 反应名称**: 谷氨酸脱氢 (Glutamate Dehydrogenation)
**2. 化学方程式**: 1.0 Glutamate + 1.0 NAD+ + 1.0 H2O → 1.0 α-Ketoglutarate + 1.0 NH4+ + 1.0 NADH + 1.0 H+
**3. 核心酶信息**: 谷氨酸脱氢酶 (Glutamate Dehydrogenase), EC 1.4.1.3
**4. 动力学与调控**: Km(Glutamate) ~1.0-5.0 mM; 激活剂: ADP, GDP; 抑制剂: ATP, GTP
**5. 能量与热力学**: ΔG°' ≈ +30 kJ/mol (可逆，因产物消耗而正向进行)

#### 支链氨基酸代谢 (Branched-Chain Amino Acid Metabolism)

##### 步骤 ID: AA-04
**1. 反应名称**: 支链氨基酸转氨基 (BCAA Transamination)
**2. 化学方程式**: 1.0 BCAA (Valine/Isoleucine/Leucine) + 1.0 α-Ketoglutarate → 1.0 BCKA (支链α-酮酸) + 1.0 Glutamate
**3. 核心酶信息**: 支链氨基酸转氨酶 (Branched-Chain Amino Acid Aminotransferase), EC 2.6.1.42
**4. 动力学与调控**: Km(BCAA) ~0.5-1.0 mM
**5. 能量与热力学**: ΔG°' ≈ 0 kJ/mol (可逆)

##### 步骤 ID: AA-05
**1. 反应名称**: 支链α-酮酸脱氢 (BCKA Dehydrogenation)
**2. 化学方程式**: 1.0 BCKA + 1.0 CoA-SH + 1.0 NAD+ → 1.0 Branched-Chain Acyl-CoA + 1.0 CO2 + 1.0 NADH + 1.0 H+
**3. 核心酶信息**: 支链α-酮酸脱氢酶 (Branched-Chain α-Keto Acid Dehydrogenase), EC 1.2.4.4, 支链氨基酸代谢限速酶
**4. 动力学与调控**: Km(BCKA) ~0.1-0.5 mM; 激活剂: Mg2+; 抑制剂: 产物抑制
**5. 能量与热力学**: ΔG°' ≈ -30 kJ/mol (不可逆)

#### 谷氨酸代谢 (Glutamate Metabolism)

##### 步骤 ID: AA-06
**1. 反应名称**: 谷氨酰胺水解 (Glutamine Hydrolysis)
**2. 化学方程式**: 1.0 Glutamine + 1.0 H2O → 1.0 Glutamate + 1.0 NH4+
**3. 核心酶信息**: 谷氨酰胺酶 (Glutaminase), EC 3.5.1.2
**4. 动力学与调控**: 
   - Km(Glutamine) ~0.5-2.0 mM
   - 激活剂: ADP, Pi
   - 抑制剂: Glutamate, ATP
   - 空间定位: 线粒体基质 (Mitochondrial matrix)
**5. 能量与热力学**: ΔG°' ≈ -15 kJ/mol (不可逆)
**6. 生理意义**: 产生谷氨酸用于转氨基反应，同时释放氨用于尿素循环
**7. 病理结局**: 
   - 谷氨酰胺酶过表达: 氨生成过多 → 高氨血症 → 脑损伤
   - 谷氨酰胺酶缺陷: 谷氨酸生成不足 → 神经递质合成障碍

##### 步骤 ID: AA-07
**1. 反应名称**: 谷氨酸合成 (Glutamate Synthesis)
**2. 化学方程式**: 1.0 α-Ketoglutarate + 1.0 NH4+ + 1.0 NADPH + 1.0 H+ → 1.0 Glutamate + 1.0 NADP+ + 1.0 H2O
**3. 核心酶信息**: 谷氨酸脱氢酶 (Glutamate Dehydrogenase), EC 1.4.1.4
**4. 动力学与调控**: 
   - Km(α-Ketoglutarate) ~0.1-0.5 mM
   - Km(NH4+) ~1-5 mM
   - 激活剂: ADP, GDP (促进还原性氨化)
   - 抑制剂: ATP, GTP (促进氧化性脱氨)
   - 辅因子: NADP+/NADPH (还原性方向), NAD+/NADH (氧化性方向)
**5. 能量与热力学**: NADPH消耗: -1, ΔG°' ≈ -30 kJ/mol (不可逆)
**6. 生理意义**: 将氨固定到α-酮戊二酸上生成谷氨酸，是氨同化的关键反应
**7. 病理结局**: 
   - GDH 缺陷: 高氨血症，低血糖，神经发育迟缓
   - GDH 活性过高: 低氨血症，谷氨酸过量 → 兴奋性毒性

#### 天冬氨酸代谢 (Aspartate Metabolism)

##### 步骤 ID: AA-08
**1. 反应名称**: 天冬氨酸合成 (Aspartate Synthesis)
**2. 化学方程式**: 1.0 Oxaloacetate + 1.0 Glutamate + 1.0 ATP → 1.0 Aspartate + 1.0 α-Ketoglutarate + 1.0 ADP + 1.0 Pi
**3. 核心酶信息**: 天冬氨酸转氨酶 (Aspartate Aminotransferase), EC 2.6.1.1
**4. 动力学与调控**: 
   - Km(Oxaloacetate) ~0.05-0.1 mM
   - Km(Glutamate) ~0.5-1.0 mM
   - 平衡常数: Keq ≈ 1.0 (接近平衡)
   - 空间定位: 胞浆 (Cytosol) 和线粒体 (Mitochondria)
**5. 能量与热力学**: ΔG°' ≈ 0 kJ/mol (可逆)
**6. 生理意义**: 连接TCA循环和氨基酸代谢，为嘌呤/嘧啶合成提供天冬氨酸
**7. 病理结局**: 
   - AST 缺陷: 天冬氨酸生成不足 → 嘌呤/嘧啶合成障碍
   - AST 过表达: 天冬氨酸过量 → 可能影响神经递质平衡

#### 丝氨酸/甘氨酸代谢 (Serine/Glycine Metabolism)

##### 步骤 ID: AA-09
**1. 反应名称**: 丝氨酸合成 (Serine Synthesis)
**2. 化学方程式**: 1.0 3-Phosphoglycerate + 1.0 Glutamate + 1.0 NAD+ → 1.0 Serine + 1.0 α-Ketoglutarate + 1.0 NADH + 1.0 H+
**3. 核心酶信息**: 3-磷酸丝氨酸转氨酶 (Phosphoserine Aminotransferase), EC 2.6.1.52
**4. 动力学与调控**: 
   - Km(3-Phosphoglycerate) ~0.1-0.5 mM
   - 激活剂: ATP (通过上游酶)
   - 抑制剂: Serine (产物抑制)
**5. 能量与热力学**: NADH生成: +1, ΔG°' ≈ -10 kJ/mol (可逆)
**6. 生理意义**: 从糖酵解中间产物合成丝氨酸，为甘氨酸和胱氨酸合成提供前体
**7. 病理结局**: 
   - 丝氨酸合成缺陷: 神经发育异常，癫痫
   - 丝氨酸过量: 可能影响神经递质平衡

##### 步骤 ID: AA-10
**1. 反应名称**: 丝氨酸羟甲基转移 (Serine Hydroxymethyltransferase)
**2. 化学方程式**: 1.0 Serine + 1.0 THF → 1.0 Glycine + 1.0 5,10-Methylene-THF + 1.0 H2O
**3. 核心酶信息**: 丝氨酸羟甲基转移酶 (Serine Hydroxymethyltransferase), EC 2.1.2.1
**4. 动力学与调控**: 
   - Km(Serine) ~0.5-1.0 mM
   - 激活剂: PLP (磷酸吡哆醛，维生素B6)
   - 抑制剂: Glycine (产物抑制)
   - 空间定位: 胞浆 (Cytosol) 和线粒体 (Mitochondria)
**5. 能量与热力学**: ΔG°' ≈ -5 kJ/mol (可逆)
**6. 生理意义**: 连接丝氨酸和甘氨酸代谢，生成一碳单位用于核酸合成
**7. 病理结局**: 
   - SHMT 缺陷: 甘氨酸生成不足，一碳单位代谢障碍
   - SHMT 过表达: 甘氨酸过量 → 可能影响神经递质平衡

#### 甲硫氨酸代谢 (Methionine Metabolism)

##### 步骤 ID: AA-11
**1. 反应名称**: 甲硫氨酸活化 (Methionine Activation)
**2. 化学方程式**: 1.0 Methionine + 1.0 ATP → 1.0 S-Adenosylmethionine (SAM) + 1.0 PPi + 1.0 Pi
**3. 核心酶信息**: 甲硫氨酸腺苷转移酶 (Methionine Adenosyltransferase), EC 2.5.1.6
**4. 动力学与调控**: 
   - Km(Methionine) ~0.05-0.1 mM
   - 激活剂: Mg2+
   - 抑制剂: SAM (产物抑制)
   - 空间定位: 胞浆 (Cytosol)
**5. 能量与热力学**: ATP消耗: -1, ΔG°' ≈ -30 kJ/mol (不可逆)
**6. 生理意义**: 生成SAM作为甲基供体，参与甲基化反应
**7. 病理结局**: 
   - MAT 缺陷: 高甲硫氨酸血症，肝损伤
   - SAM 缺乏: 甲基化反应障碍 → DNA甲基化异常

##### 步骤 ID: AA-12
**1. 反应名称**: SAM 甲基转移 (SAM Methyl Transfer)
**2. 化学方程式**: 1.0 SAM + 1.0 Acceptor → 1.0 Methylated Acceptor + 1.0 SAH
**3. 核心酶信息**: 甲基转移酶 (Methyltransferase) 家族, EC 2.1.1.x
**4. 动力学与调控**: 
   - Km(SAM) ~0.01-0.05 mM
   - 激活剂: Mg2+
   - 抑制剂: SAH (产物抑制)
   - 底物: DNA, RNA, 蛋白质, 脂质, 小分子
**5. 能量与热力学**: ΔG°' ≈ -20 kJ/mol (不可逆)
**6. 生理意义**: SAM作为通用甲基供体，参与几乎所有甲基化反应
**7. 病理结局**: 
   - 甲基转移酶缺陷: 甲基化反应障碍 → 表观遗传异常
   - SAH 积累: 抑制甲基转移酶 → 甲基化反应受阻

#### 组氨酸代谢 (Histidine Metabolism)

##### 步骤 ID: AA-13
**1. 反应名称**: 组氨酸脱氨 (Histidine Deamination)
**2. 化学方程式**: 1.0 Histidine + 1.0 H2O → 1.0 Urocanate + 1.0 NH4+
**3. 核心酶信息**: 组氨酸氨裂解酶 (Histidine Ammonia-Lyase), EC 4.3.1.3
**4. 动力学与调控**: 
   - Km(Histidine) ~0.1-0.5 mM
   - 激活剂: PLP (磷酸吡哆醛，维生素B6)
   - 抑制剂: Urocanate (产物抑制)
   - 空间定位: 肝细胞胞浆 (Hepatocyte cytosol)
**5. 能量与热力学**: ΔG°' ≈ -15 kJ/mol (不可逆)
**6. 生理意义**: 组氨酸分解的第一步，生成尿刊酸
**7. 病理结局**: 
   - HAL 缺陷: 组氨酸尿症，智力发育迟缓
   - HAL 过表达: 尿刊酸积累 → 可能影响皮肤屏障功能

##### 步骤 ID: AA-14
**1. 反应名称**: 尿刊酸水合 (Urocanate Hydration)
**2. 化学方程式**: 1.0 Urocanate + 1.0 H2O → 1.0 4-Imidazolone-5-Propionate
**3. 核心酶信息**: 尿刊酸水合酶 (Urocanate Hydratase), EC 4.2.1.49
**4. 动力学与调控**: 
   - Km(Urocanate) ~0.1-0.5 mM
   - 无强变构调控
   - 空间定位: 肝细胞胞浆 (Hepatocyte cytosol)
**5. 能量与热力学**: ΔG°' ≈ -10 kJ/mol (不可逆)
**6. 生理意义**: 组氨酸代谢的中间步骤
**7. 病理结局**: 
   - UH 缺陷: 尿刊酸尿症，皮肤病变

#### 苯丙氨酸/酪氨酸代谢 (Phenylalanine/Tyrosine Metabolism)

##### 步骤 ID: AA-15
**1. 反应名称**: 苯丙氨酸羟化 (Phenylalanine Hydroxylation)
**2. 化学方程式**: 1.0 Phenylalanine + 1.0 BH4 + 1.0 O2 → 1.0 Tyrosine + 1.0 BH2 + 1.0 H2O
**3. 核心酶信息**: 苯丙氨酸羟化酶 (Phenylalanine Hydroxylase), EC 1.14.16.1
**4. 动力学与调控**: 
   - Km(Phenylalanine) ~0.1-0.5 mM
   - 激活剂: BH4 (四氢生物蝶呤)
   - 抑制剂: Tyrosine (产物抑制)
   - 空间定位: 肝细胞胞浆 (Hepatocyte cytosol)
**5. 能量与热力学**: ΔG°' ≈ -20 kJ/mol (不可逆)
**6. 生理意义**: 将必需氨基酸苯丙氨酸转化为酪氨酸，是苯丙氨酸代谢的主要途径
**7. 病理结局**: 
   - PAH 缺陷: 苯丙酮尿症 (PKU)，智力发育迟缓
   - PAH 活性不足: 苯丙氨酸积累 → 神经毒性

##### 步骤 ID: AA-16
**1. 反应名称**: 酪氨酸转氨基 (Tyrosine Transamination)
**2. 化学方程式**: 1.0 Tyrosine + 1.0 α-Ketoglutarate → 1.0 p-Hydroxyphenylpyruvate + 1.0 Glutamate
**3. 核心酶信息**: 酪氨酸转氨酶 (Tyrosine Aminotransferase), EC 2.6.1.5
**4. 动力学与调控**: 
   - Km(Tyrosine) ~0.1-0.5 mM
   - 激活剂: 胰高血糖素 (转录水平)
   - 抑制剂: 胰岛素 (转录水平)
   - 空间定位: 肝细胞胞浆 (Hepatocyte cytosol)
**5. 能量与热力学**: ΔG°' ≈ 0 kJ/mol (可逆)
**6. 生理意义**: 酪氨酸分解的第一步，生成对羟基苯丙酮酸
**7. 病理结局**: 
   - TAT 缺陷: 酪氨酸血症 II 型，智力发育迟缓
   - TAT 过表达: 酪氨酸分解过快 → 可能影响神经递质合成

#### 色氨酸代谢 (Tryptophan Metabolism)

##### 步骤 ID: AA-17
**1. 反应名称**: 色氨酸羟化 (Tryptophan Hydroxylation)
**2. 化学方程式**: 1.0 Tryptophan + 1.0 BH4 + 1.0 O2 → 1.0 5-Hydroxytryptophan + 1.0 BH2 + 1.0 H2O
**3. 核心酶信息**: 色氨酸羟化酶 (Tryptophan Hydroxylase), EC 1.14.16.4
**4. 动力学与调控**: 
   - Km(Tryptophan) ~0.05-0.1 mM
   - 激活剂: BH4 (四氢生物蝶呤)
   - 抑制剂: 5-Hydroxytryptophan (产物抑制)
   - 空间定位: 肝细胞胞浆 (Hepatocyte cytosol)
**5. 能量与热力学**: ΔG°' ≈ -20 kJ/mol (不可逆)
**6. 生理意义**: 色氨酸代谢的第一步，生成5-羟色氨酸
**7. 病理结局**: 
   - TPH 缺陷: 5-羟色胺合成不足 → 抑郁，睡眠障碍
   - TPH 过表达: 5-羟色胺过量 → 可能影响神经递质平衡

##### 步骤 ID: AA-18
**1. 反应名称**: 色氨酸-2,3-双加氧酶反应 (Tryptophan-2,3-Dioxygenase Reaction)
**2. 化学方程式**: 1.0 Tryptophan + 1.0 O2 → 1.0 N-Formylkynurenine
**3. 核心酶信息**: 色氨酸-2,3-双加氧酶 (Tryptophan-2,3-Dioxygenase), EC 1.13.11.11
**4. 动力学与调控**: 
   - Km(Tryptophan) ~0.1-0.5 mM
   - 激活剂: 肝素，皮质醇
   - 抑制剂: 色氨酸代谢产物
   - 空间定位: 肝细胞胞浆 (Hepatocyte cytosol)
**5. 能量与热力学**: ΔG°' ≈ -25 kJ/mol (不可逆)
**6. 生理意义**: 色氨酸分解的主要途径，生成犬尿氨酸
**7. 病理结局**: 
   - TDO 缺陷: 色氨酸积累 → 可能影响神经递质合成
   - TDO 过表达: 色氨酸分解过快 → 5-羟色胺合成不足

### TCA循环 (Tricarboxylic Acid Cycle)

#### TCA循环核心反应 (TCA Cycle Core Reactions)

##### 步骤 ID: TCA-01
**1. 反应名称**: 柠檬酸合酶反应 (Citrate Synthase Reaction)
**2. 化学方程式**: 1.0 Acetyl-CoA + 1.0 Oxaloacetate + 1.0 H2O → 1.0 Citrate + 1.0 CoA-SH + 1.0 H+
**3. 核心酶信息**: 柠檬酸合酶 (Citrate Synthase), EC 2.3.3.1, TCA循环限速酶
**4. 动力学与调控**: 
   - 反应机制: 有序双底物反应，先结合草酰乙酸，再结合乙酰-CoA
   - 速率方程: v = Vmax[Acetyl-CoA][Oxaloacetate] / (Km(Acetyl-CoA)[Oxaloacetate] + Km(Oxaloacetate)[Acetyl-CoA] + [Acetyl-CoA][Oxaloacetate] + Ki(CoA-SH)[CoA-SH] + Ki(NADH)[NADH])
   - 动力学参数: 
     * Km(Acetyl-CoA) ~0.01-0.05 mM
     * Km(Oxaloacetate) ~0.001-0.01 mM
     * Vmax ~100-200 μmol/min/mg protein
   - 抑制类型: 
     * CoA-SH: 竞争性抑制剂 (与乙酰-CoA竞争结合位点)，Ki ~0.01-0.05 mM
     * NADH: 非竞争性抑制剂，Ki ~0.01-0.05 mM
     * ATP: 非竞争性抑制剂，Ki ~0.1-0.5 mM
   - 激活剂: 无强变构激活剂
   - 抑制剂: 
     * NADH (氧化还原状态抑制)
     * ATP (能量状态抑制)
     * Succinyl-CoA (反馈抑制)
   - 空间定位: 线粒体基质 (Mitochondrial matrix)
   - 辅因子: 无
**5. 能量与热力学**: ΔG°' ≈ -32 kJ/mol (不可逆)
**6. 生理意义**: TCA循环的第一步，将乙酰-CoA和草酰乙酸缩合生成柠檬酸
**7. 病理结局**: 
   - 柠檬酸合酶缺陷: 能量代谢障碍，神经退行性疾病
   - 柠檬酸合酶过表达: 可能导致柠檬酸堆积

##### 步骤 ID: TCA-02
**1. 反应名称**: 顺乌头酸酶反应 (Aconitase Reaction)
**2. 化学方程式**: 1.0 Citrate → 1.0 Isocitrate
**3. 核心酶信息**: 顺乌头酸酶 (Aconitase), EC 4.2.1.3
**4. 动力学与调控**: 
   - 反应机制: 脱水-水合反应，通过顺乌头酸中间物
   - 速率方程: v = Vmax[Citrate] / (Km(Citrate) + [Citrate])
   - 动力学参数: 
     * Km(Citrate) ~0.1-0.5 mM
     * Vmax ~500-1000 μmol/min/mg protein
   - 抑制类型: 无强变构调控
   - 激活剂: Fe-S簇 (必需辅因子)
   - 抑制剂: 氟化物 (抑制Fe-S簇)
   - 空间定位: 线粒体基质 (Mitochondrial matrix)
   - 辅因子: Fe-S簇
**5. 能量与热力学**: ΔG°' ≈ +8 kJ/mol (可逆)
**6. 生理意义**: 将柠檬酸异构化为异柠檬酸，为下一步氧化脱羧做准备
**7. 病理结局**: 
   - 顺乌头酸酶缺陷: 柠檬酸堆积，能量代谢障碍
   - Fe-S簇损伤: 氧化应激，神经退行性疾病

##### 步骤 ID: TCA-03
**1. 反应名称**: 异柠檬酸脱氢酶反应 (Isocitrate Dehydrogenase Reaction)
**2. 化学方程式**: 1.0 Isocitrate + 1.0 NAD+ → 1.0 α-Ketoglutarate + 1.0 CO2 + 1.0 NADH + 1.0 H+
**3. 核心酶信息**: 异柠檬酸脱氢酶 (Isocitrate Dehydrogenase), EC 1.1.1.41, TCA循环限速酶
**4. 动力学与调控**: 
   - 反应机制: 氧化脱羧反应，先氧化后脱羧
   - 速率方程: v = Vmax[Isocitrate][NAD+] / (Km(Isocitrate)[NAD+] + Km(NAD+)[Isocitrate] + [Isocitrate][NAD+] + Ki(NADH)[NADH] + Ki(ATP)[ATP] + Kact[ADP])
   - 动力学参数: 
     * Km(Isocitrate) ~0.01-0.05 mM
     * Km(NAD+) ~0.01-0.05 mM
     * Vmax ~100-200 μmol/min/mg protein
   - 抑制类型: 
     * NADH: 竞争性抑制剂 (与NAD+竞争结合位点)，Ki ~0.01-0.05 mM
     * ATP: 非竞争性抑制剂，Ki ~0.1-0.5 mM
   - 激活剂: 
     * ADP (别构激活剂，降低Km值)
     * Ca2+ (别构激活剂)
     * Mg2+ (必需辅因子)
   - 抑制剂: 
     * NADH (氧化还原状态抑制)
     * ATP (能量状态抑制)
   - 空间定位: 线粒体基质 (Mitochondrial matrix)
   - 辅因子: NAD+, Mg2+
**5. 能量与热力学**: NADH生成: +1, CO2生成: +1, ΔG°' ≈ -17 kJ/mol (不可逆)
**6. 生理意义**: TCA循环的第一个氧化脱羧反应，生成NADH和α-酮戊二酸
**7. 病理结局**: 
   - 异柠檬酸脱氢酶缺陷: 能量代谢障碍，神经退行性疾病
   - 异柠檬酸脱氢酶突变: 癌症 (如IDH1/2突变)

##### 步骤 ID: TCA-04
**1. 反应名称**: α-酮戊二酸脱氢酶复合体反应 (α-Ketoglutarate Dehydrogenase Complex Reaction)
**2. 化学方程式**: 1.0 α-Ketoglutarate + 1.0 CoA-SH + 1.0 NAD+ → 1.0 Succinyl-CoA + 1.0 CO2 + 1.0 NADH + 1.0 H+
**3. 核心酶信息**: α-酮戊二酸脱氢酶复合体 (α-Ketoglutarate Dehydrogenase Complex), EC 1.2.4.2, TCA循环限速酶
**4. 动力学与调控**: 
   - 反应机制: 多酶复合体顺序反应，类似丙酮酸脱氢酶复合体
   - 反应序列: 1) E1催化α-酮戊二酸脱羧 2) E2将酰基转移给CoA 3) E3重新氧化辅因子并将电子转移给NAD+
   - 速率方程: v = Vmax[α-Ketoglutarate][CoA-SH][NAD+] / (K1[CoA-SH][NAD+] + K2[α-Ketoglutarate][NAD+] + K3[α-Ketoglutarate][CoA-SH] + [α-Ketoglutarate][CoA-SH][NAD+] + Ki(Succinyl-CoA)[Succinyl-CoA] + Ki(NADH)[NADH] + Ki(ATP)[ATP])
   - 动力学参数: 
     * Km(α-Ketoglutarate) ~0.01-0.05 mM
     * Km(CoA-SH) ~0.01-0.05 mM
     * Km(NAD+) ~0.01-0.05 mM
     * Vmax ~50-100 μmol/min/mg protein
   - 抑制类型: 
     * Succinyl-CoA: 竞争性抑制剂 (与CoA-SH竞争结合位点)，Ki ~0.01-0.05 mM
     * NADH: 竞争性抑制剂 (与NAD+竞争结合位点)，Ki ~0.01-0.05 mM
     * ATP: 非竞争性抑制剂，Ki ~0.1-0.5 mM
   - 激活剂: 
     * Ca2+ (别构激活剂)
     * Mg2+ (必需辅因子)
     * TPP (E1辅因子), 硫辛酰胺 (E2辅因子), FAD (E3辅因子)
   - 抑制剂: 
     * Succinyl-CoA (产物抑制)
     * NADH (产物抑制)
     * ATP (能量状态抑制)
   - 空间定位: 线粒体基质 (Mitochondrial matrix)
   - 辅因子: TPP, 硫辛酰胺, FAD, NAD+
**5. 能量与热力学**: NADH生成: +1, CO2生成: +1, ΔG°' ≈ -30 kJ/mol (不可逆)
**6. 生理意义**: TCA循环的第二个氧化脱羧反应，生成NADH和琥珀酰-CoA
**7. 病理结局**: 
   - α-酮戊二酸脱氢酶缺陷: 能量代谢障碍，神经退行性疾病
   - 硫胺素缺乏: 酶活性下降，脚气病

##### 步骤 ID: TCA-05
**1. 反应名称**: 琥珀酰-CoA合成酶反应 (Succinyl-CoA Synthetase Reaction)
**2. 化学方程式**: 1.0 Succinyl-CoA + 1.0 GDP + 1.0 Pi → 1.0 Succinate + 1.0 GTP + 1.0 CoA-SH
**3. 核心酶信息**: 琥珀酰-CoA合成酶 (Succinyl-CoA Synthetase), EC 6.2.1.5
**4. 动力学与调控**: 
   - 反应机制: 底物水平磷酸化反应，通过磷酸组氨酸中间物
   - 速率方程: v = Vmax[Succinyl-CoA][GDP][Pi] / (Km(Succinyl-CoA)[GDP][Pi] + Km(GDP)[Succinyl-CoA][Pi] + Km(Pi)[Succinyl-CoA][GDP] + [Succinyl-CoA][GDP][Pi])
   - 动力学参数: 
     * Km(Succinyl-CoA) ~0.01-0.05 mM
     * Km(GDP) ~0.01-0.05 mM
     * Km(Pi) ~0.1-0.5 mM
     * Vmax ~100-200 μmol/min/mg protein
   - 抑制类型: 无强变构调控
   - 激活剂: Mg2+ (必需辅因子)
   - 抑制剂: 无强抑制剂
   - 空间定位: 线粒体基质 (Mitochondrial matrix)
   - 辅因子: Mg2+
**5. 能量与热力学**: GTP生成: +1, ΔG°' ≈ -2 kJ/mol (可逆)
**6. 生理意义**: TCA循环中唯一的底物水平磷酸化反应，生成GTP
**7. 病理结局**: 
   - 琥珀酰-CoA合成酶缺陷: 能量代谢障碍，神经退行性疾病

##### 步骤 ID: TCA-06
**1. 反应名称**: 琥珀酸脱氢酶反应 (Succinate Dehydrogenase Reaction)
**2. 化学方程式**: 1.0 Succinate + 1.0 FAD → 1.0 Fumarate + 1.0 FADH2
**3. 核心酶信息**: 琥珀酸脱氢酶 (Succinate Dehydrogenase), EC 1.3.5.1, 电子传递链复合物II
**4. 动力学与调控**: 
   - 反应机制: 氧化反应，直接将电子转移到FAD
   - 速率方程: v = Vmax[Succinate] / (Km(Succinate) + [Succinate] + Ki(Malonate)[Malonate])
   - 动力学参数: 
     * Km(Succinate) ~0.1-0.5 mM
     * Vmax ~100-200 μmol/min/mg protein
   - 抑制类型: 
     * Malonate: 竞争性抑制剂 (与琥珀酸竞争结合位点)，Ki ~0.01-0.05 mM
   - 激活剂: FAD (必需辅因子), Fe-S簇
   - 抑制剂: Malonate (经典抑制剂)
   - 空间定位: 线粒体内膜 (Inner mitochondrial membrane)
   - 辅因子: FAD, Fe-S簇
**5. 能量与热力学**: FADH2生成: +1, ΔG°' ≈ 0 kJ/mol (可逆)
**6. 生理意义**: 连接TCA循环和电子传递链的唯一酶，将琥珀酸氧化为延胡索酸
**7. 病理结局**: 
   - 琥珀酸脱氢酶缺陷: 能量代谢障碍，肿瘤 (如副神经节瘤)
   - 复合物II功能障碍: 氧化磷酸化缺陷

##### 步骤 ID: TCA-07
**1. 反应名称**: 延胡索酸酶反应 (Fumarase Reaction)
**2. 化学方程式**: 1.0 Fumarate + 1.0 H2O → 1.0 L-Malate
**3. 核心酶信息**: 延胡索酸酶 (Fumarase), EC 4.2.1.2
**4. 动力学与调控**: 
   - 反应机制: 反式水合反应
   - 速率方程: v = Vmax[Fumarate] / (Km(Fumarate) + [Fumarate])
   - 动力学参数: 
     * Km(Fumarate) ~0.1-0.5 mM
     * Vmax ~500-1000 μmol/min/mg protein
   - 抑制类型: 无强变构调控
   - 激活剂: 无强变构激活剂
   - 抑制剂: 无强抑制剂
   - 空间定位: 线粒体基质 (Mitochondrial matrix)
   - 辅因子: 无
**5. 能量与热力学**: ΔG°' ≈ -4 kJ/mol (可逆)
**6. 生理意义**: 将延胡索酸水合为L-苹果酸，为最后一步氧化反应做准备
**7. 病理结局**: 
   - 延胡索酸酶缺陷: 延胡索酸堆积，能量代谢障碍
   - 延胡索酸酶突变: 肿瘤 (如遗传性平滑肌瘤病和肾细胞癌)

##### 步骤 ID: TCA-08
**1. 反应名称**: 苹果酸脱氢酶反应 (Malate Dehydrogenase Reaction)
**2. 化学方程式**: 1.0 L-Malate + 1.0 NAD+ → 1.0 Oxaloacetate + 1.0 NADH + 1.0 H+
**3. 核心酶信息**: 苹果酸脱氢酶 (Malate Dehydrogenase), EC 1.1.1.37
**4. 动力学与调控**: 
   - 反应机制: 氧化还原反应
   - 速率方程: v = Vmax[L-Malate][NAD+] / (Km(L-Malate)[NAD+] + Km(NAD+)[L-Malate] + [L-Malate][NAD+] + Ki(NADH)[NADH])
   - 动力学参数: 
     * Km(L-Malate) ~0.1-0.5 mM
     * Km(NAD+) ~0.01-0.05 mM
     * Vmax ~500-1000 μmol/min/mg protein
   - 抑制类型: 
     * NADH: 竞争性抑制剂 (与NAD+竞争结合位点)，Ki ~0.01-0.05 mM
   - 激活剂: 无强变构激活剂
   - 抑制剂: NADH (产物抑制)
   - 空间定位: 线粒体基质 (Mitochondrial matrix)
   - 辅因子: NAD+
**5. 能量与热力学**: NADH生成: +1, ΔG°' ≈ +29 kJ/mol (可逆，依赖草酰乙酸的快速消耗)
**6. 生理意义**: TCA循环的最后一步，将L-苹果酸氧化为草酰乙酸，完成循环
**7. 病理结局**: 
   - 苹果酸脱氢酶缺陷: 能量代谢障碍，神经退行性疾病

#### TCA循环回补反应 (TCA Cycle Anaplerosis)

##### 步骤 ID: TCA-Anap-01
**1. 反应名称**: 丙酮酸羧化 (Pyruvate Carboxylation)
**2. 化学方程式**: 1.0 Pyruvate + 1.0 HCO3- + 1.0 ATP → 1.0 Oxaloacetate + 1.0 ADP + 1.0 Pi + 1.0 H+
**3. 核心酶信息**: 丙酮酸羧化酶 (Pyruvate Carboxylase), EC 6.4.1.1
**4. 动力学与调控**: 
   - Km(Pyruvate) ~0.1-0.5 mM
   - 绝对激活剂: Acetyl-CoA (必须存在)
   - 抑制剂: ADP, ATP (能量状态调控)
   - 空间定位: 线粒体基质 (Mitochondrial matrix)
   - 辅因子: 生物素 (Biotin)
**5. 能量与热力学**: ATP消耗: -1, ΔG°' ≈ -0.8 kJ/mol (不可逆)
**6. 生理意义**: TCA循环的关键回补反应，维持草酰乙酸水平
**7. 病理结局**: 
   - PC 缺陷: 乳酸酸中毒，低血糖，神经发育迟缓
   - PC 活性不足: TCA循环中间产物不足 → 能量代谢障碍

##### 步骤 ID: TCA-Anap-02
**1. 反应名称**: 谷氨酸脱氨回补 (Glutamate Deamination Anaplerosis)
**2. 化学方程式**: 1.0 Glutamate + 1.0 NAD+ + 1.0 H2O → 1.0 α-Ketoglutarate + 1.0 NH4+ + 1.0 NADH + 1.0 H+
**3. 核心酶信息**: 谷氨酸脱氢酶 (Glutamate Dehydrogenase), EC 1.4.1.3
**4. 动力学与调控**: 
   - Km(Glutamate) ~1.0-5.0 mM
   - 激活剂: ADP, GDP (促进氧化性脱氨)
   - 抑制剂: ATP, GTP (促进还原性氨化)
   - 空间定位: 线粒体基质 (Mitochondrial matrix)
**5. 能量与热力学**: NADH生成: +1, ΔG°' ≈ +30 kJ/mol (可逆)
**6. 生理意义**: 将谷氨酸转化为α-酮戊二酸，回补TCA循环
**7. 病理结局**: 
   - GDH 缺陷: 高氨血症，低血糖
   - GDH 活性过高: 谷氨酸消耗过快 → 神经递质合成障碍

##### 步骤 ID: TCA-Anap-03
**1. 反应名称**: 天冬氨酸转氨基回补 (Aspartate Transamination Anaplerosis)
**2. 化学方程式**: 1.0 Aspartate + 1.0 α-Ketoglutarate → 1.0 Oxaloacetate + 1.0 Glutamate
**3. 核心酶信息**: 天冬氨酸转氨酶 (Aspartate Aminotransferase), EC 2.6.1.1
**4. 动力学与调控**: 
   - Km(Aspartate) ~0.5-1.0 mM
   - 平衡常数: Keq ≈ 1.0 (接近平衡)
   - 空间定位: 线粒体基质 (Mitochondrial matrix)
**5. 能量与热力学**: ΔG°' ≈ 0 kJ/mol (可逆)
**6. 生理意义**: 将天冬氨酸转化为草酰乙酸，回补TCA循环
**7. 病理结局**: 
   - AST 缺陷: 天冬氨酸代谢障碍 → 嘌呤/嘧啶合成障碍
   - AST 活性不足: TCA循环中间产物不足 → 能量代谢障碍

#### 氨基酸分解为TCA循环中间产物 (Amino Acid Catabolism to TCA Intermediates)

##### 步骤 ID: AA-Cat-01
**1. 反应名称**: 丙氨酸分解 (Alanine Catabolism)
**2. 化学方程式**: 1.0 Alanine + 1.0 α-Ketoglutarate → 1.0 Pyruvate + 1.0 Glutamate
**3. 核心酶信息**: 丙氨酸转氨酶 (Alanine Aminotransferase), EC 2.6.1.2
**4. 动力学与调控**: 
   - Km(Alanine) ~0.5-1.0 mM
   - 激活剂: 胰高血糖素 (转录水平)
   - 抑制剂: 胰岛素 (转录水平)
   - 空间定位: 肝细胞胞浆 (Hepatocyte cytosol)
**5. 能量与热力学**: ΔG°' ≈ 0 kJ/mol (可逆)
**6. 生理意义**: 丙氨酸-葡萄糖循环的一部分，将肌肉来源的丙氨酸转化为丙酮酸
**7. 病理结局**: 
   - ALT 缺陷: 丙氨酸代谢障碍 → 高丙氨酸血症
   - ALT 过表达: 丙氨酸分解过快 → 可能影响糖异生

##### 步骤 ID: AA-Cat-02
**1. 反应名称**: 异亮氨酸分解 (Isoleucine Catabolism)
**2. 化学方程式**: 1.0 Isoleucine → 1.0 Acetyl-CoA + 1.0 Succinyl-CoA (多步反应)
**3. 核心酶信息**: 支链氨基酸转氨酶 (BCAT), 支链α-酮酸脱氢酶 (BCKDH), 多种分解酶
**4. 动力学与调控**: 
   - Km(Isoleucine) ~0.1-0.5 mM
   - 激活剂: Mg2+
   - 抑制剂: 产物抑制
   - 空间定位: 线粒体基质 (Mitochondrial matrix)
**5. 能量与热力学**: 生成1个乙酰-CoA和1个琥珀酰-CoA，可进入TCA循环
**6. 生理意义**: 异亮氨酸是生酮兼生糖氨基酸，分解产物可进入TCA循环
**7. 病理结局**: 
   - 异亮氨酸代谢缺陷: 枫糖尿症，智力发育迟缓
   - 异亮氨酸过量: 可能影响能量代谢平衡

##### 步骤 ID: AA-Cat-03
**1. 反应名称**: 亮氨酸分解 (Leucine Catabolism)
**2. 化学方程式**: 1.0 Leucine → 1.0 Acetyl-CoA + 1.0 Acetoacetate (多步反应)
**3. 核心酶信息**: 支链氨基酸转氨酶 (BCAT), 支链α-酮酸脱氢酶 (BCKDH), 多种分解酶
**4. 动力学与调控**: 
   - Km(Leucine) ~0.1-0.5 mM
   - 激活剂: Mg2+
   - 抑制剂: 产物抑制
   - 空间定位: 线粒体基质 (Mitochondrial matrix)
**5. 能量与热力学**: 生成乙酰-CoA和乙酰乙酸，可生成酮体
**6. 生理意义**: 亮氨酸是纯生酮氨基酸，分解产物可生成酮体
**7. 病理结局**: 
   - 亮氨酸代谢缺陷: 枫糖尿症，智力发育迟缓
   - 亮氨酸过量: 可能促进蛋白质合成

##### 步骤 ID: AA-Cat-04
**1. 反应名称**: 缬氨酸分解 (Valine Catabolism)
**2. 化学方程式**: 1.0 Valine → 1.0 Succinyl-CoA (多步反应)
**3. 核心酶信息**: 支链氨基酸转氨酶 (BCAT), 支链α-酮酸脱氢酶 (BCKDH), 多种分解酶
**4. 动力学与调控**: 
   - Km(Valine) ~0.1-0.5 mM
   - 激活剂: Mg2+
   - 抑制剂: 产物抑制
   - 空间定位: 线粒体基质 (Mitochondrial matrix)
**5. 能量与热力学**: 生成琥珀酰-CoA，可进入TCA循环
**6. 生理意义**: 缬氨酸是生糖氨基酸，分解产物可进入TCA循环
**7. 病理结局**: 
   - 缬氨酸代谢缺陷: 枫糖尿症，智力发育迟缓
   - 缬氨酸过量: 可能影响能量代谢平衡

##### 步骤 ID: AA-Cat-05
**1. 反应名称**: 天冬酰胺分解 (Asparagine Catabolism)
**2. 化学方程式**: 1.0 Asparagine + 1.0 H2O → 1.0 Aspartate + 1.0 NH4+
**3. 核心酶信息**: 天冬酰胺酶 (Asparaginase), EC 3.5.1.1
**4. 动力学与调控**: 
   - Km(Asparagine) ~0.1-0.5 mM
   - 无强变构调控
   - 空间定位: 肝细胞胞浆 (Hepatocyte cytosol)
**5. 能量与热力学**: ΔG°' ≈ -15 kJ/mol (不可逆)
**6. 生理意义**: 天冬酰胺分解生成天冬氨酸，可进入TCA循环
**7. 病理结局**: 
   - 天冬酰胺酶缺陷: 天冬酰胺尿症
   - 天冬酰胺酶过表达: 天冬酰胺消耗过快 → 可能影响蛋白质合成

##### 步骤 ID: AA-Cat-06
**1. 反应名称**: 谷氨酰胺分解 (Glutamine Catabolism)
**2. 化学方程式**: 1.0 Glutamine + 1.0 H2O → 1.0 Glutamate + 1.0 NH4+
**3. 核心酶信息**: 谷氨酰胺酶 (Glutaminase), EC 3.5.1.2
**4. 动力学与调控**: 
   - Km(Glutamine) ~0.5-2.0 mM
   - 激活剂: ADP, Pi
   - 抑制剂: Glutamate, ATP
   - 空间定位: 线粒体基质 (Mitochondrial matrix)
**5. 能量与热力学**: ΔG°' ≈ -15 kJ/mol (不可逆)
**6. 生理意义**: 谷氨酰胺分解生成谷氨酸，可进入TCA循环
**7. 病理结局**: 
   - 谷氨酰胺酶缺陷: 谷氨酰胺尿症
   - 谷氨酰胺酶过表达: 氨生成过多 → 高氨血症

##### 步骤 ID: AA-Cat-07
**1. 反应名称**: 精氨酸分解 (Arginine Catabolism)
**2. 化学方程式**: 1.0 Arginine + 1.0 H2O → 1.0 Ornithine + 1.0 Urea
**3. 核心酶信息**: 精氨酸酶 (Arginase), EC 3.5.3.1
**4. 动力学与调控**: 
   - Km(Arginine) ~1-5 mM
   - 激活剂: Mn2+
   - 抑制剂: 产物抑制
   - 空间定位: 肝细胞胞浆 (Hepatocyte cytosol)
**5. 能量与热力学**: ΔG°' ≈ -20 kJ/mol (不可逆)
**6. 生理意义**: 精氨酸分解生成鸟氨酸和尿素，是尿素循环的最后一步
**7. 病理结局**: 
   - 精氨酸酶缺陷: 高精氨酸血症，智力发育迟缓
   - 精氨酸酶过表达: 精氨酸消耗过快 → 可能影响蛋白质合成

##### 步骤 ID: AA-Cat-08
**1. 反应名称**: 鸟氨酸分解 (Ornithine Catabolism)
**2. 化学方程式**: 1.0 Ornithine + 1.0 α-Ketoglutarate → 1.0 Glutamate-γ-Semialdehyde + 1.0 Glutamate
**3. 核心酶信息**: 鸟氨酸δ-氨基转移酶 (Ornithine δ-Aminotransferase), EC 2.6.1.13
**4. 动力学与调控**: 
   - Km(Ornithine) ~0.1-0.5 mM
   - 激活剂: PLP (磷酸吡哆醛，维生素B6)
   - 抑制剂: 产物抑制
   - 空间定位: 线粒体基质 (Mitochondrial matrix)
**5. 能量与热力学**: ΔG°' ≈ 0 kJ/mol (可逆)
**6. 生理意义**: 鸟氨酸分解生成谷氨酸-γ-半醛，可转化为脯氨酸
**7. 病理结局**: 
   - OAT 缺陷: 高鸟氨酸血症，眼部病变
   - OAT 过表达: 鸟氨酸消耗过快 → 可能影响尿素循环

##### 步骤 ID: AA-Cat-09
**1. 反应名称**: 脯氨酸分解 (Proline Catabolism)
**2. 化学方程式**: 1.0 Proline + 1.0 FAD + 1.0 H2O → 1.0 Δ1-Pyrroline-5-Carboxylate + 1.0 FADH2
**3. 核心酶信息**: 脯氨酸氧化酶 (Proline Oxidase), EC 1.5.3.8
**4. 动力学与调控**: 
   - Km(Proline) ~0.1-0.5 mM
   - 激活剂: FAD
   - 抑制剂: 产物抑制
   - 空间定位: 线粒体内膜 (Inner mitochondrial membrane)
**5. 能量与热力学**: FADH2生成: +1, ΔG°' ≈ -15 kJ/mol (不可逆)
**6. 生理意义**: 脯氨酸分解生成Δ1-吡咯啉-5-羧酸，可转化为谷氨酸
**7. 病理结局**: 
   - 脯氨酸氧化酶缺陷: 高脯氨酸血症 I 型
   - 脯氨酸氧化酶过表达: 脯氨酸消耗过快 → 可能影响胶原蛋白合成

##### 步骤 ID: AA-Cat-10
**1. 反应名称**: 赖氨酸分解 (Lysine Catabolism)
**2. 化学方程式**: 1.0 Lysine → 1.0 Acetyl-CoA (多步反应)
**3. 核心酶信息**: 赖氨酸酮戊二酸还原酶 (Lysine-Ketoglutarate Reductase), 多种分解酶
**4. 动力学与调控**: 
   - Km(Lysine) ~0.1-0.5 mM
   - 激活剂: NADPH
   - 抑制剂: 产物抑制
   - 空间定位: 线粒体基质 (Mitochondrial matrix)
**5. 能量与热力学**: 生成乙酰-CoA，可进入TCA循环
**6. 生理意义**: 赖氨酸是纯生酮氨基酸，分解产物可生成酮体
**7. 病理结局**: 
   - 赖氨酸代谢缺陷: 高赖氨酸血症，智力发育迟缓
   - 赖氨酸过量: 可能影响蛋白质合成平衡

##### 步骤 ID: AA-Cat-11
**1. 反应名称**: 苏氨酸分解 (Threonine Catabolism)
**2. 化学方程式**: 1.0 Threonine → 1.0 Succinyl-CoA (多步反应)
**3. 核心酶信息**: 苏氨酸脱氢酶 (Threonine Dehydrogenase), 多种分解酶
**4. 动力学与调控**: 
   - Km(Threonine) ~0.1-0.5 mM
   - 激活剂: NAD+
   - 抑制剂: 产物抑制
   - 空间定位: 线粒体基质 (Mitochondrial matrix)
**5. 能量与热力学**: 生成琥珀酰-CoA，可进入TCA循环
**6. 生理意义**: 苏氨酸是生糖氨基酸，分解产物可进入TCA循环
**7. 病理结局**: 
   - 苏氨酸代谢缺陷: 高苏氨酸血症
   - 苏氨酸过量: 可能影响能量代谢平衡

##### 步骤 ID: AA-Cat-12
**1. 反应名称**: 半胱氨酸分解 (Cysteine Catabolism)
**2. 化学方程式**: 1.0 Cysteine + 1.0 H2O → 1.0 Pyruvate + 1.0 NH4+ + 1.0 H2S
**3. 核心酶信息**: 半胱氨酸脱硫酶 (Cysteine Desulfurase), EC 2.8.1.7
**4. 动力学与调控**: 
   - Km(Cysteine) ~0.1-0.5 mM
   - 激活剂: PLP (磷酸吡哆醛，维生素B6)
   - 抑制剂: 产物抑制
   - 空间定位: 肝细胞胞浆 (Hepatocyte cytosol)
**5. 能量与热力学**: ΔG°' ≈ -20 kJ/mol (不可逆)
**6. 生理意义**: 半胱氨酸分解生成丙酮酸，可进入TCA循环
**7. 病理结局**: 
   - 半胱氨酸脱硫酶缺陷: 半胱氨酸尿症
   - 半胱氨酸脱硫酶过表达: H2S生成过多 → 可能影响线粒体功能

#### 非必需氨基酸合成 (Non-Essential Amino Acid Synthesis)

##### 步骤 ID: AA-Syn-01
**1. 反应名称**: 丙氨酸合成 (Alanine Synthesis)
**2. 化学方程式**: 1.0 Pyruvate + 1.0 Glutamate → 1.0 Alanine + 1.0 α-Ketoglutarate
**3. 核心酶信息**: 丙氨酸转氨酶 (Alanine Aminotransferase), EC 2.6.1.2
**4. 动力学与调控**: 
   - Km(Pyruvate) ~0.1-0.5 mM
   - 激活剂: 胰岛素 (转录水平)
   - 抑制剂: 胰高血糖素 (转录水平)
   - 空间定位: 肝细胞胞浆 (Hepatocyte cytosol)
**5. 能量与热力学**: ΔG°' ≈ 0 kJ/mol (可逆)
**6. 生理意义**: 从丙酮酸合成丙氨酸，是丙氨酸-葡萄糖循环的一部分
**7. 病理结局**: 
   - ALT 缺陷: 丙氨酸合成障碍 → 蛋白质合成障碍
   - ALT 过表达: 丙氨酸合成过多 → 可能影响糖代谢

##### 步骤 ID: AA-Syn-02
**1. 反应名称**: 天冬氨酸合成 (Aspartate Synthesis)
**2. 化学方程式**: 1.0 Oxaloacetate + 1.0 Glutamate → 1.0 Aspartate + 1.0 α-Ketoglutarate
**3. 核心酶信息**: 天冬氨酸转氨酶 (Aspartate Aminotransferase), EC 2.6.1.1
**4. 动力学与调控**: 
   - Km(Oxaloacetate) ~0.05-0.1 mM
   - 平衡常数: Keq ≈ 1.0 (接近平衡)
   - 空间定位: 肝细胞胞浆 (Hepatocyte cytosol)
**5. 能量与热力学**: ΔG°' ≈ 0 kJ/mol (可逆)
**6. 生理意义**: 从草酰乙酸合成天冬氨酸，为嘌呤/嘧啶合成提供前体
**7. 病理结局**: 
   - AST 缺陷: 天冬氨酸合成障碍 → 嘌呤/嘧啶合成障碍
   - AST 过表达: 天冬氨酸合成过多 → 可能影响TCA循环

##### 步骤 ID: AA-Syn-03
**1. 反应名称**: 谷氨酸合成 (Glutamate Synthesis)
**2. 化学方程式**: 1.0 α-Ketoglutarate + 1.0 NH4+ + 1.0 NADPH + 1.0 H+ → 1.0 Glutamate + 1.0 NADP+ + 1.0 H2O
**3. 核心酶信息**: 谷氨酸脱氢酶 (Glutamate Dehydrogenase), EC 1.4.1.4
**4. 动力学与调控**: 
   - Km(α-Ketoglutarate) ~0.1-0.5 mM
   - Km(NH4+) ~1-5 mM
   - 激活剂: ADP, GDP (促进还原性氨化)
   - 抑制剂: ATP, GTP (促进氧化性脱氨)
   - 辅因子: NADP+/NADPH (还原性方向)
**5. 能量与热力学**: NADPH消耗: -1, ΔG°' ≈ -30 kJ/mol (不可逆)
**6. 生理意义**: 将氨固定到α-酮戊二酸上生成谷氨酸，是氨同化的关键反应
**7. 病理结局**: 
   - GDH 缺陷: 谷氨酸合成障碍 → 高氨血症
   - GDH 活性过高: 谷氨酸合成过多 → 可能影响神经递质平衡

##### 步骤 ID: AA-Syn-04
**1. 反应名称**: 谷氨酰胺合成 (Glutamine Synthesis)
**2. 化学方程式**: 1.0 Glutamate + 1.0 NH4+ + 1.0 ATP → 1.0 Glutamine + 1.0 ADP + 1.0 Pi + 1.0 H+
**3. 核心酶信息**: 谷氨酰胺合成酶 (Glutamine Synthetase), EC 6.3.1.2
**4. 动力学与调控**: 
   - Km(Glutamate) ~1-5 mM
   - Km(NH4+) ~1-5 mM
   - 激活剂: α-Ketoglutarate
   - 抑制剂: 谷氨酰胺 (产物抑制)
   - 空间定位: 肝细胞胞浆 (Hepatocyte cytosol)
**5. 能量与热力学**: ATP消耗: -1, ΔG°' ≈ -16 kJ/mol (不可逆)
**6. 生理意义**: 将氨固定到谷氨酸上生成谷氨酰胺，是氨储存和运输的形式
**7. 病理结局**: 
   - GS 缺陷: 谷氨酰胺合成障碍 → 高氨血症
   - GS 过表达: 谷氨酰胺合成过多 → 可能影响氨代谢平衡

##### 步骤 ID: AA-Syn-05
**1. 反应名称**: 天冬酰胺合成 (Asparagine Synthesis)
**2. 化学方程式**: 1.0 Aspartate + 1.0 Glutamine + 1.0 ATP → 1.0 Asparagine + 1.0 Glutamate + 1.0 AMP + 1.0 PPi
**3. 核心酶信息**: 天冬酰胺合成酶 (Asparagine Synthetase), EC 6.3.5.4
**4. 动力学与调控**: 
   - Km(Aspartate) ~0.1-0.5 mM
   - 激活剂: Mg2+
   - 抑制剂: 天冬酰胺 (产物抑制)
   - 空间定位: 肝细胞胞浆 (Hepatocyte cytosol)
**5. 能量与热力学**: ATP消耗: -2 (因PPi水解), ΔG°' ≈ -30 kJ/mol (不可逆)
**6. 生理意义**: 从天冬氨酸合成天冬酰胺，为蛋白质合成提供前体
**7. 病理结局**: 
   - AS 缺陷: 天冬酰胺合成障碍 → 蛋白质合成障碍
   - AS 过表达: 天冬酰胺合成过多 → 可能影响氨基酸平衡

##### 步骤 ID: AA-Syn-06
**1. 反应名称**: 丝氨酸合成 (Serine Synthesis)
**2. 化学方程式**: 1.0 3-Phosphoglycerate + 1.0 Glutamate + 1.0 NAD+ → 1.0 Serine + 1.0 α-Ketoglutarate + 1.0 NADH + 1.0 H+
**3. 核心酶信息**: 3-磷酸丝氨酸转氨酶 (Phosphoserine Aminotransferase), EC 2.6.1.52
**4. 动力学与调控**: 
   - Km(3-Phosphoglycerate) ~0.1-0.5 mM
   - 激活剂: ATP (通过上游酶)
   - 抑制剂: 丝氨酸 (产物抑制)
   - 空间定位: 肝细胞胞浆 (Hepatocyte cytosol)
**5. 能量与热力学**: NADH生成: +1, ΔG°' ≈ -10 kJ/mol (可逆)
**6. 生理意义**: 从糖酵解中间产物合成丝氨酸，为甘氨酸和胱氨酸合成提供前体
**7. 病理结局**: 
   - PSAT 缺陷: 丝氨酸合成障碍 → 神经发育异常
   - PSAT 过表达: 丝氨酸合成过多 → 可能影响糖代谢

##### 步骤 ID: AA-Syn-07
**1. 反应名称**: 甘氨酸合成 (Glycine Synthesis)
**2. 化学方程式**: 1.0 Serine + 1.0 THF → 1.0 Glycine + 1.0 5,10-Methylene-THF + 1.0 H2O
**3. 核心酶信息**: 丝氨酸羟甲基转移酶 (Serine Hydroxymethyltransferase), EC 2.1.2.1
**4. 动力学与调控**: 
   - Km(Serine) ~0.5-1.0 mM
   - 激活剂: PLP (磷酸吡哆醛，维生素B6)
   - 抑制剂: 甘氨酸 (产物抑制)
   - 空间定位: 肝细胞胞浆 (Hepatocyte cytosol)
**5. 能量与热力学**: ΔG°' ≈ -5 kJ/mol (可逆)
**6. 生理意义**: 从丝氨酸合成甘氨酸，生成一碳单位用于核酸合成
**7. 病理结局**: 
   - SHMT 缺陷: 甘氨酸合成障碍 → 一碳单位代谢障碍
   - SHMT 过表达: 甘氨酸合成过多 → 可能影响神经递质平衡

##### 步骤 ID: AA-Syn-08
**1. 反应名称**: 半胱氨酸合成 (Cysteine Synthesis)
**2. 化学方程式**: 1.0 Serine + 1.0 Homocysteine → 1.0 Cystathionine + 1.0 H2O
**3. 核心酶信息**: 胱硫醚β-合酶 (Cystathionine β-Synthase), EC 4.2.1.22
**4. 动力学与调控**: 
   - Km(Serine) ~0.5-1.0 mM
   - Km(Homocysteine) ~0.1-0.5 mM
   - 激活剂: PLP (磷酸吡哆醛，维生素B6)
   - 抑制剂: 产物抑制
   - 空间定位: 肝细胞胞浆 (Hepatocyte cytosol)
**5. 能量与热力学**: ΔG°' ≈ -10 kJ/mol (不可逆)
**6. 生理意义**: 从丝氨酸和同型半胱氨酸合成胱硫醚，是半胱氨酸合成的前体
**7. 病理结局**: 
   - CBS 缺陷: 同型半胱氨酸尿症，血管疾病
   - CBS 过表达: 半胱氨酸合成过多 → 可能影响氧化还原平衡

##### 步骤 ID: AA-Syn-09
**1. 反应名称**: 胱硫醚裂解 (Cystathionine Cleavage)
**2. 化学方程式**: 1.0 Cystathionine + 1.0 H2O → 1.0 Cysteine + 1.0 α-Ketobutyrate + 1.0 NH4+
**3. 核心酶信息**: 胱硫醚γ-裂解酶 (Cystathionine γ-Lyase), EC 4.4.1.1
**4. 动力学与调控**: 
   - Km(Cystathionine) ~0.1-0.5 mM
   - 激活剂: PLP (磷酸吡哆醛，维生素B6)
   - 抑制剂: 产物抑制
   - 空间定位: 肝细胞胞浆 (Hepatocyte cytosol)
**5. 能量与热力学**: ΔG°' ≈ -15 kJ/mol (不可逆)
**6. 生理意义**: 胱硫醚裂解生成半胱氨酸和α-酮丁酸
**7. 病理结局**: 
   - CGL 缺陷: 半胱氨酸合成障碍 → 同型半胱氨酸尿症
   - CGL 过表达: 半胱氨酸合成过多 → 可能影响氧化还原平衡

##### 步骤 ID: AA-Syn-10
**1. 反应名称**: 酪氨酸合成 (Tyrosine Synthesis)
**2. 化学方程式**: 1.0 Phenylalanine + 1.0 BH4 + 1.0 O2 → 1.0 Tyrosine + 1.0 BH2 + 1.0 H2O
**3. 核心酶信息**: 苯丙氨酸羟化酶 (Phenylalanine Hydroxylase), EC 1.14.16.1
**4. 动力学与调控**: 
   - Km(Phenylalanine) ~0.1-0.5 mM
   - 激活剂: BH4 (四氢生物蝶呤)
   - 抑制剂: 酪氨酸 (产物抑制)
   - 空间定位: 肝细胞胞浆 (Hepatocyte cytosol)
**5. 能量与热力学**: ΔG°' ≈ -20 kJ/mol (不可逆)
**6. 生理意义**: 从必需氨基酸苯丙氨酸合成酪氨酸
**7. 病理结局**: 
   - PAH 缺陷: 酪氨酸合成障碍 → 苯丙酮尿症 (PKU)
   - PAH 活性不足: 苯丙氨酸积累 → 神经毒性

##### 步骤 ID: AA-Syn-11
**1. 反应名称**: 脯氨酸合成 (Proline Synthesis)
**2. 化学方程式**: 1.0 Glutamate + 1.0 ATP → 1.0 Glutamate-5-Semialdehyde + 1.0 ADP + 1.0 Pi
**3. 核心酶信息**: 谷氨酸-5-激酶 (Glutamate-5-Kinase), EC 2.7.2.11
**4. 动力学与调控**: 
   - Km(Glutamate) ~0.5-1.0 mM
   - 激活剂: Mg2+
   - 抑制剂: 产物抑制
   - 空间定位: 肝细胞胞浆 (Hepatocyte cytosol)
**5. 能量与热力学**: ATP消耗: -1, ΔG°' ≈ -30 kJ/mol (不可逆)
**6. 生理意义**: 从谷氨酸合成谷氨酸-5-半醛，是脯氨酸合成的第一步
**7. 病理结局**: 
   - G5K 缺陷: 脯氨酸合成障碍 → 蛋白质合成障碍
   - G5K 过表达: 脯氨酸合成过多 → 可能影响胶原蛋白合成

##### 步骤 ID: AA-Syn-12
**1. 反应名称**: 精氨酸合成 (Arginine Synthesis)
**2. 化学方程式**: 1.0 Ornithine + 1.0 Carbamoyl Phosphate → 1.0 Citrulline + 1.0 Pi
**3. 核心酶信息**: 鸟氨酸氨甲酰转移酶 (Ornithine Carbamoyltransferase), EC 2.1.3.3
**4. 动力学与调控**: 
   - Km(Ornithine) ~0.1-0.5 mM
   - 激活剂: Mg2+
   - 抑制剂: 产物抑制
   - 空间定位: 线粒体基质 (Mitochondrial matrix)
**5. 能量与热力学**: ΔG°' ≈ -20 kJ/mol (不可逆)
**6. 生理意义**: 从鸟氨酸合成瓜氨酸，是精氨酸合成的中间步骤
**7. 病理结局**: 
   - OTC 缺陷: 瓜氨酸合成障碍 → 高氨血症
   - OTC 过表达: 瓜氨酸合成过多 → 可能影响尿素循环

#### 核苷酸代谢 (Nucleotide Metabolism)

##### 步骤 ID: NUC-01
**1. 反应名称**: PRPP合成 (PRPP Synthesis)
**2. 化学方程式**: 1.0 Ribose-5-Phosphate + 1.0 ATP → 1.0 5-Phosphoribosyl-1-Pyrophosphate (PRPP) + 1.0 AMP
**3. 核心酶信息**: PRPP合成酶 (PRPP Synthetase), EC 2.7.6.1
**4. 动力学与调控**: 
   - Km(Ribose-5-Phosphate) ~0.05-0.1 mM
   - 激活剂: Pi (无机磷酸)
   - 抑制剂: ADP, GDP (产物抑制)
   - 空间定位: 胞浆 (Cytosol)
**5. 能量与热力学**: ATP消耗: -1, ΔG°' ≈ -30 kJ/mol (不可逆)
**6. 生理意义**: PRPP是核苷酸合成的前体，连接PPP和核苷酸代谢
**7. 病理结局**: 
   - PRPS 缺陷: Lesch-Nyhan 综合征，痛风
   - PRPS 过表达: PRPP合成过多 → 嘌呤合成增加 → 痛风

##### 步骤 ID: NUC-02
**1. 反应名称**: 嘌呤从头合成第一步 (De Novo Purine Synthesis Step 1)
**2. 化学方程式**: 1.0 PRPP + 1.0 Glutamine + 1.0 H2O → 1.0 5-Phosphoribosylamine + 1.0 Glutamate + 1.0 PPi
**3. 核心酶信息**: PRPP酰胺转移酶 (PRPP Amidotransferase), EC 2.4.2.14, 嘌呤合成限速酶
**4. 动力学与调控**: 
   - Km(PRPP) ~0.01-0.05 mM
   - 激活剂: PRPP (底物激活)
   - 抑制剂: AMP, GMP (终产物反馈抑制)
   - 空间定位: 胞浆 (Cytosol)
**5. 能量与热力学**: ATP消耗: -1 (因PPi水解), ΔG°' ≈ -40 kJ/mol (不可逆)
**6. 生理意义**: 嘌呤从头合成的第一步，是嘌呤合成的关键调控点
**7. 病理结局**: 
   - PRPPAT 缺陷: 嘌呤合成障碍 → 免疫缺陷
   - PRPPAT 活性过高: 嘌呤合成过多 → 痛风

##### 步骤 ID: NUC-03
**1. 反应名称**: 嘌呤从头合成 (De Novo Purine Synthesis)
**2. 化学方程式**: 1.0 PRPP + 1.0 Glutamine + 1.0 Glycine + 1.0 Aspartate + 1.0 CO2 + 2.0 Formyl-THF → 1.0 IMP + 1.0 Glutamate + 1.0 Fumarate + 2.0 THF + 1.0 PPi
**3. 核心酶信息**: 多种酶参与，PRPP酰胺转移酶为限速酶
**4. 动力学与调控**: 
   - 总ATP消耗: -5
   - 激活剂: PRPP
   - 抑制剂: AMP, GMP (终产物反馈抑制)
   - 空间定位: 胞浆 (Cytosol)
**5. 能量与热力学**: ATP消耗: -5, ΔG°' ≈ -150 kJ/mol (不可逆)
**6. 生理意义**: 从头合成嘌呤核苷酸，是DNA/RNA合成的基础
**7. 病理结局**: 
   - 嘌呤合成缺陷: 免疫缺陷，生长迟缓
   - 嘌呤合成过多: 痛风，肾结石

##### 步骤 ID: NUC-04
**1. 反应名称**: IMP转化为AMP (IMP to AMP Conversion)
**2. 化学方程式**: 1.0 IMP + 1.0 Aspartate + 1.0 GTP → 1.0 Adenylosuccinate + 1.0 GDP + 1.0 Pi
**3. 核心酶信息**: 腺苷酸代琥珀酸合成酶 (Adenylosuccinate Synthetase), EC 6.3.4.4
**4. 动力学与调控**: 
   - Km(IMP) ~0.01-0.05 mM
   - 激活剂: GTP
   - 抑制剂: AMP (终产物反馈抑制)
   - 空间定位: 胞浆 (Cytosol)
**5. 能量与热力学**: GTP消耗: -1, ΔG°' ≈ -30 kJ/mol (不可逆)
**6. 生理意义**: IMP转化为AMP，是嘌呤核苷酸合成的重要分支
**7. 病理结局**: 
   - ADSS 缺陷: AMP合成障碍 → 肌病，智力发育迟缓
   - ADSS 活性过高: AMP合成过多 → 可能影响能量代谢

##### 步骤 ID: NUC-05
**1. 反应名称**: IMP转化为GMP (IMP to GMP Conversion)
**2. 化学方程式**: 1.0 IMP + 1.0 NAD+ + 1.0 H2O → 1.0 Xanthosine-5'-Phosphate (XMP) + 1.0 NADH + 1.0 H+
**3. 核心酶信息**: IMP脱氢酶 (IMP Dehydrogenase), EC 1.1.1.205
**4. 动力学与调控**: 
   - Km(IMP) ~0.01-0.05 mM
   - 激活剂: NAD+
   - 抑制剂: GMP (终产物反馈抑制)
   - 空间定位: 胞浆 (Cytosol)
**5. 能量与热力学**: NADH生成: +1, ΔG°' ≈ -20 kJ/mol (不可逆)
**6. 生理意义**: IMP氧化为XMP，是GMP合成的中间步骤
**7. 病理结局**: 
   - IMPDH 缺陷: GMP合成障碍 → 免疫缺陷
   - IMPDH 活性过高: GMP合成过多 → 可能影响核苷酸平衡

##### 步骤 ID: NUC-06
**1. 反应名称**: 嘧啶从头合成第一步 (De Novo Pyrimidine Synthesis Step 1)
**2. 化学方程式**: 1.0 Carbamoyl Phosphate + 1.0 Aspartate → 1.0 Carbamoyl Aspartate + 1.0 Pi
**3. 核心酶信息**: 天冬氨酸转氨甲酰酶 (Aspartate Transcarbamoylase), EC 2.1.3.2
**4. 动力学与调控**: 
   - Km(Aspartate) ~0.1-0.5 mM
   - 激活剂: ATP
   - 抑制剂: CTP (终产物反馈抑制)
   - 空间定位: 胞浆 (Cytosol)
**5. 能量与热力学**: ΔG°' ≈ -20 kJ/mol (不可逆)
**6. 生理意义**: 嘧啶从头合成的第一步，是嘧啶合成的关键调控点
**7. 病理结局**: 
   - ATC 缺陷: 嘧啶合成障碍 → 免疫缺陷
   - ATC 活性过高: 嘧啶合成过多 → 可能影响核苷酸平衡

##### 步骤 ID: NUC-07
**1. 反应名称**: 嘧啶从头合成 (De Novo Pyrimidine Synthesis)
**2. 化学方程式**: 1.0 Carbamoyl Phosphate + 1.0 Aspartate + 1.0 PRPP → 1.0 UMP + 1.0 PPi + 1.0 Pi + 1.0 CO2
**3. 核心酶信息**: 多种酶参与，氨甲酰磷酸合成酶II为限速酶
**4. 动力学与调控**: 
   - 总ATP消耗: -2
   - 激活剂: PRPP
   - 抑制剂: UTP, CTP (终产物反馈抑制)
   - 空间定位: 胞浆 (Cytosol)
**5. 能量与热力学**: ATP消耗: -2, ΔG°' ≈ -60 kJ/mol (不可逆)
**6. 生理意义**: 从头合成嘧啶核苷酸，是DNA/RNA合成的基础
**7. 病理结局**: 
   - 嘧啶合成缺陷: 免疫缺陷，生长迟缓
   - 嘧啶合成过多: 可能影响核苷酸平衡

##### 步骤 ID: NUC-08
**1. 反应名称**: UMP磷酸化 (UMP Phosphorylation)
**2. 化学方程式**: 1.0 UMP + 1.0 ATP → 1.0 UDP + 1.0 ADP
**3. 核心酶信息**: UMP激酶 (UMP Kinase), EC 2.7.4.14
**4. 动力学与调控**: 
   - Km(UMP) ~0.01-0.05 mM
   - 激活剂: ATP
   - 抑制剂: UTP (终产物反馈抑制)
   - 空间定位: 胞浆 (Cytosol)
**5. 能量与热力学**: ATP消耗: -1, ΔG°' ≈ -30 kJ/mol (不可逆)
**6. 生理意义**: UMP磷酸化为UDP，是嘧啶核苷酸合成的重要步骤
**7. 病理结局**: 
   - UMPK 缺陷: UDP合成障碍 → 免疫缺陷
   - UMPK 活性过高: UDP合成过多 → 可能影响核苷酸平衡

##### 步骤 ID: NUC-09
**1. 反应名称**: UDP还原为dUDP (UDP to dUDP Reduction)
**2. 化学方程式**: 1.0 UDP + 1.0 NADPH + 1.0 H+ → 1.0 dUDP + 1.0 NADP+
**3. 核心酶信息**: 核糖核苷酸还原酶 (Ribonucleotide Reductase), EC 1.17.4.1
**4. 动力学与调控**: 
   - Km(UDP) ~0.01-0.05 mM
   - 激活剂: ATP, dATP (变构激活)
   - 抑制剂: dATP (高浓度时变构抑制)
   - 空间定位: 胞浆 (Cytosol)
**5. 能量与热力学**: NADPH消耗: -1, ΔG°' ≈ -30 kJ/mol (不可逆)
**6. 生理意义**: 将核糖核苷酸还原为脱氧核糖核苷酸，是DNA合成的基础
**7. 病理结局**: 
   - RNR 缺陷: DNA合成障碍 → 免疫缺陷，生长迟缓
   - RNR 活性过高: DNA合成过多 → 可能影响细胞周期

##### 步骤 ID: NUC-10
**1. 反应名称**: 嘌呤补救合成 (Purine Salvage Synthesis)
**2. 化学方程式**: 1.0 Hypoxanthine + 1.0 PRPP → 1.0 IMP + 1.0 PPi
**3. 核心酶信息**: 次黄嘌呤-鸟嘌呤磷酸核糖转移酶 (HGPRT), EC 2.4.2.8
**4. 动力学与调控**: 
   - Km(Hypoxanthine) ~0.01-0.05 mM
   - 激活剂: PRPP
   - 抑制剂: IMP, GMP (终产物反馈抑制)
   - 空间定位: 胞浆 (Cytosol)
**5. 能量与热力学**: ATP消耗: -1 (因PPi水解), ΔG°' ≈ -30 kJ/mol (不可逆)
**6. 生理意义**: 从游离嘌呤碱基合成嘌呤核苷酸，节省能量
**7. 病理结局**: 
   - HGPRT 缺陷: Lesch-Nyhan 综合征，痛风，自残行为
   - HGPRT 活性过高: 嘌呤补救合成过多 → 可能影响核苷酸平衡

#### 一碳代谢 (One-Carbon Metabolism)

##### 步骤 ID: 1C-01
**1. 反应名称**: 丝氨酸转羟甲基 (Serine Hydroxymethyltransferase)
**2. 化学方程式**: 1.0 Serine + 1.0 THF → 1.0 Glycine + 1.0 5,10-Methylene-THF + 1.0 H2O
**3. 核心酶信息**: 丝氨酸羟甲基转移酶 (Serine Hydroxymethyltransferase), EC 2.1.2.1
**4. 动力学与调控**: 
   - Km(Serine) ~0.5-1.0 mM
   - 激活剂: PLP (磷酸吡哆醛，维生素B6)
   - 抑制剂: Glycine (产物抑制)
   - 空间定位: 胞浆 (Cytosol) 和线粒体 (Mitochondria)
**5. 能量与热力学**: ΔG°' ≈ -5 kJ/mol (可逆)
**6. 生理意义**: 连接丝氨酸和甘氨酸代谢，生成一碳单位用于核酸合成
**7. 病理结局**: 
   - SHMT 缺陷: 一碳单位代谢障碍 → DNA合成异常
   - SHMT 过表达: 一碳单位生成过多 → 可能影响核苷酸平衡

##### 步骤 ID: 1C-02
**1. 反应名称**: 5,10-亚甲基-THF还原 (5,10-Methylene-THF Reduction)
**2. 化学方程式**: 1.0 5,10-Methylene-THF + 1.0 NADPH + 1.0 H+ → 1.0 5-Methyl-THF + 1.0 NADP+
**3. 核心酶信息**: 亚甲基四氢叶酸还原酶 (Methylene Tetrahydrofolate Reductase, MTHFR), EC 1.5.1.20
**4. 动力学与调控**: 
   - Km(5,10-Methylene-THF) ~0.01-0.05 mM
   - 激活剂: FAD (辅因子)
   - 抑制剂: SAM (变构抑制)
   - 空间定位: 胞浆 (Cytosol)
**5. 能量与热力学**: NADPH消耗: -1, ΔG°' ≈ -20 kJ/mol (不可逆)
**6. 生理意义**: 将5,10-亚甲基-THF还原为5-甲基-THF，是同型半胱氨酸甲基化的关键
**7. 病理结局**: 
   - MTHFR 缺陷: 高同型半胱氨酸血症，心血管疾病
   - MTHFR 多态性: 影响叶酸代谢，增加神经管缺陷风险

##### 步骤 ID: 1C-03
**1. 反应名称**: 同型半胱氨酸甲基化 (Homocysteine Methylation)
**2. 化学方程式**: 1.0 Homocysteine + 1.0 5-Methyl-THF → 1.0 Methionine + 1.0 THF
**3. 核心酶信息**: 甲硫氨酸合酶 (Methionine Synthase), EC 2.1.1.13
**4. 动力学与调控**: 
   - Km(Homocysteine) ~0.01-0.05 mM
   - 激活剂: 维生素B12 (钴胺素)
   - 抑制剂: SAM (产物抑制)
   - 空间定位: 胞浆 (Cytosol)
**5. 能量与热力学**: ΔG°' ≈ -30 kJ/mol (不可逆)
**6. 生理意义**: 将同型半胱氨酸甲基化为甲硫氨酸，降低同型半胱氨酸水平
**7. 病理结局**: 
   - MS 缺陷: 高同型半胱氨酸血症，巨幼红细胞性贫血
   - 维生素B12缺乏: 同型半胱氨酸升高 → 心血管疾病

##### 步骤 ID: 1C-04
**1. 反应名称**: 5,10-亚甲基-THF氧化 (5,10-Methylene-THF Oxidation)
**2. 化学方程式**: 1.0 5,10-Methylene-THF + 1.0 NADP+ → 1.0 5,10-Methenyl-THF + 1.0 NADPH + 1.0 H+
**3. 核心酶信息**: 亚甲基四氢叶酸脱氢酶 (Methylene Tetrahydrofolate Dehydrogenase), EC 1.5.1.5
**4. 动力学与调控**: 
   - Km(5,10-Methylene-THF) ~0.01-0.05 mM
   - 激活剂: NADP+
   - 抑制剂: 产物抑制
   - 空间定位: 胞浆 (Cytosol)
**5. 能量与热力学**: NADPH生成: +1, ΔG°' ≈ -10 kJ/mol (可逆)
**6. 生理意义**: 一碳单位氧化，连接不同氧化态的一碳单位
**7. 病理结局**: 
   - MTHFD 缺陷: 一碳单位代谢障碍 → DNA合成异常
   - MTHFD 活性过高: 一碳单位代谢紊乱 → 可能影响核苷酸平衡

##### 步骤 ID: 1C-05
**1. 反应名称**: 5,10-亚甲基-THF用于胸苷酸合成 (5,10-Methylene-THF for Thymidylate Synthesis)
**2. 化学方程式**: 1.0 dUMP + 1.0 5,10-Methylene-THF → 1.0 dTMP + 1.0 DHF
**3. 核心酶信息**: 胸苷酸合酶 (Thymidylate Synthase), EC 2.1.1.45
**4. 动力学与调控**: 
   - Km(dUMP) ~0.01-0.05 mM
   - 激活剂: 5,10-Methylene-THF
   - 抑制剂: 5-FU (5-氟尿嘧啶，化疗药物)
   - 空间定位: 胞浆 (Cytosol)
**5. 能量与热力学**: ΔG°' ≈ -30 kJ/mol (不可逆)
**6. 生理意义**: 将dUMP甲基化为dTMP，是DNA合成的关键步骤
**7. 病理结局**: 
   - TS 缺陷: dTMP合成障碍 → DNA合成异常
   - TS 过表达: dTMP合成过多 → 可能影响DNA复制

#### 辅酶代谢 (Coenzyme Metabolism)

##### 步骤 ID: COE-01
**1. 反应名称**: NAD+合成 (NAD+ Synthesis)
**2. 化学方程式**: 1.0 Nicotinamide + 1.0 PRPP → 1.0 Nicotinamide Mononucleotide (NMN) + 1.0 PPi
**3. 核心酶信息**: 烟酰胺磷酸核糖转移酶 (Nicotinamide Phosphoribosyltransferase, NAMPT), EC 2.4.2.12
**4. 动力学与调控**: 
   - Km(Nicotinamide) ~0.01-0.05 mM
   - 激活剂: PRPP
   - 抑制剂: FK866 (特异性抑制剂)
   - 空间定位: 胞浆 (Cytosol)
**5. 能量与热力学**: ATP消耗: -1 (因PPi水解), ΔG°' ≈ -30 kJ/mol (不可逆)
**6. 生理意义**: NAD+是氧化还原反应的关键辅酶，参与能量代谢和DNA修复
**7. 病理结局**: 
   - NAMPT 缺陷: NAD+合成障碍 → 能量代谢障碍
   - NAMPT 过表达: NAD+合成过多 → 可能影响氧化还原平衡

##### 步骤 ID: COE-02
**1. 反应名称**: NAD+磷酸化 (NAD+ Phosphorylation)
**2. 化学方程式**: 1.0 NMN + 1.0 ATP → 1.0 NAD+ + 1.0 PPi
**3. 核心酶信息**: NMN腺苷转移酶 (NMN Adenylyltransferase, NMNAT), EC 2.7.7.1
**4. 动力学与调控**: 
   - Km(NMN) ~0.01-0.05 mM
   - 激活剂: ATP
   - 抑制剂: 产物抑制
   - 空间定位: 胞浆 (Cytosol)
**5. 能量与热力学**: ATP消耗: -1 (因PPi水解), ΔG°' ≈ -30 kJ/mol (不可逆)
**6. 生理意义**: NMN磷酸化为NAD+，完成NAD+合成
**7. 病理结局**: 
   - NMNAT 缺陷: NAD+合成障碍 → 能量代谢障碍
   - NMNAT 过表达: NAD+合成过多 → 可能影响氧化还原平衡

##### 步骤 ID: COE-03
**1. 反应名称**: CoA合成 (CoA Synthesis)
**2. 化学方程式**: 1.0 Pantothenate + 1.0 Cysteine + 1.0 ATP → 1.0 4'-Phosphopantetheine + 1.0 ADP + 1.0 Pi
**3. 核心酶信息**: 泛酸激酶 (Pantothenate Kinase), EC 2.7.1.33
**4. 动力学与调控**: 
   - Km(Pantothenate) ~0.01-0.05 mM
   - 激活剂: ATP
   - 抑制剂: 泛酸激酶相关神经变性 (PKAN)
   - 空间定位: 胞浆 (Cytosol)
**5. 能量与热力学**: ATP消耗: -1, ΔG°' ≈ -30 kJ/mol (不可逆)
**6. 生理意义**: CoA是酰基转移反应的关键辅酶，参与TCA循环和脂肪酸代谢
**7. 病理结局**: 
   - PANK 缺陷: CoA合成障碍 → PKAN (泛酸激酶相关神经变性)
   - PANK 过表达: CoA合成过多 → 可能影响酰基代谢

##### 步骤 ID: COE-04
**1. 反应名称**: CoA去磷酸化 (CoA Dephosphorylation)
**2. 化学方程式**: 1.0 4'-Phosphopantetheine + 1.0 ATP → 1.0 Dephospho-CoA + 1.0 ADP + 1.0 Pi
**3. 核心酶信息**: 磷酸泛酰半胱氨酸脱羧酶 (Phosphopantothenoylcysteine Decarboxylase), EC 4.1.1.36
**4. 动力学与调控**: 
   - Km(4'-Phosphopantetheine) ~0.01-0.05 mM
   - 激活剂: ATP
   - 抑制剂: 产物抑制
   - 空间定位: 胞浆 (Cytosol)
**5. 能量与热力学**: ATP消耗: -1, ΔG°' ≈ -30 kJ/mol (不可逆)
**6. 生理意义**: CoA合成的中间步骤
**7. 病理结局**: 
   - PPCDC 缺陷: CoA合成障碍 → 能量代谢障碍
   - PPCDC 过表达: CoA合成过多 → 可能影响酰基代谢

### 营养物质转运系统 (Nutrient Transport Systems)

#### 葡萄糖摄取 (Glucose Uptake)

##### 步骤 ID: TRANS-01
**1. 反应名称**: 葡萄糖双向转运 (Glucose Facilitated Diffusion)
**2. 化学方程式**: Glucose(blood) ⇌ Glucose(cytosol)
**3. 核心酶信息**: GLUT2 / SLC2A2, 肝脏特异性葡萄糖转运体
**4. 动力学与调控**: Km(Glucose) ~15-20 mM (极高Km值); 双向转运逻辑: 血糖高时(>10 mM)肝脏摄取, 血糖低时(<5 mM)肝脏释放葡萄糖
**5. 能量与热力学**: 被动易化扩散, ΔG°' ≈ 0 kJ/mol (可逆)
**6. 生理意义**: 肝脏作为血糖缓冲器, 高血糖时摄取储存, 低血糖时释放维持血糖稳定

#### 脂肪酸摄取 (Fatty Acid Uptake)

##### 步骤 ID: TRANS-02
**1. 反应名称**: 长链脂肪酸跨膜转运 (Long-Chain Fatty Acid Transmembrane Transport)
**2. 化学方程式**: Fatty Acid(blood) ⇌ Fatty Acid(cytosol)
**3. 核心酶信息**: CD36 / FATP 家族 / FABP 协助
**4. 动力学与调控**: 胰岛素促进CD36/FATP膜表达，增强转运
**5. 能量与热力学**: ΔG°' ≈ 0 kJ/mol (可逆)
**6. 生理意义**: 转运本身不消耗ATP；脂肪酸活化由Acyl-CoA synthetase执行（ATP→AMP+PPi）

#### 线粒体穿梭系统 (Mitochondrial Shuttles)

##### 步骤 ID: SHT-01
**1. 反应名称**: 苹果酸-天冬氨酸穿梭 (Malate-Aspartate Shuttle)
**2. 化学方程式**: 
   - 胞浆: Oxaloacetate + NADH + H+ → Malate + NAD+
   - 线粒体: Malate + NAD+ → Oxaloacetate + NADH + H+
   - 辅助: Oxaloacetate + Glutamate ⇌ Aspartate + α-Ketoglutarate (通过线粒体膜)
**3. 核心酶信息**: 胞浆苹果酸脱氢酶 (cMDH), 线粒体苹果酸脱氢酶 (mMDH), 天冬氨酸氨基转移酶 (AST), 苹果酸-α-酮戊二酸转运体, 谷氨酸-天冬氨酸转运体
**4. 动力学与调控**: 高效NADH转运: 每分子胞浆NADH可生成~2.5 ATP (比甘油-3-磷酸穿梭更高效)
**5. 能量与热力学**: NADH转运, 线粒体内NADH氧化生成~2.5 ATP
**6. 生理意义**: 肝脏主要NADH穿梭系统, 将糖酵解产生的胞浆NADH运入线粒体进行氧化磷酸化

##### 步骤 ID: SHT-02
**1. 反应名称**: 柠檬酸-丙酮酸穿梭 (Citrate-Pyruvate Shuttle)
**2. 化学方程式**: 
   - 线粒体: Acetyl-CoA + Oxaloacetate + H2O → Citrate + CoA-SH
   - 线粒体膜转运: Citrate(mito) → Citrate(cyto)
   - 胞浆: Citrate + ATP + CoA-SH → Acetyl-CoA + Oxaloacetate + ADP + Pi
   - 胞浆: Oxaloacetate + NADH + H+ → Malate + NAD+
   - 胞浆: Malate + NADP+ → Pyruvate + CO2 + NADPH
   - 线粒体膜转运: Pyruvate(cyto) → Pyruvate(mito)
**3. 核心酶信息**: 柠檬酸合酶 (CS), ATP-柠檬酸裂解酶 (ACL), 苹果酸脱氢酶 (MDH), 苹果酸酶 (ME), 柠檬酸转运体, 丙酮酸转运体
**4. 动力学与调控**: 能量状态调控: 高ATP/柠檬酸 → 脂肪酸合成激活; 低ATP → TCA循环优先
**5. 能量与热力学**: ATP消耗: -1 (胞浆裂解柠檬酸), NADPH生成: +1 (苹果酸酶反应，NADP+为辅因子)
**6. 生理意义**: 将线粒体Acetyl-CoA运出胞浆用于脂肪酸合成, 同时生成NADPH供脂质合成使用

### 电子传递链微观拆解 (Micro-ETC)

#### 复合物 I (NADH脱氢酶)

##### 步骤 ID: ETC-01
**1. 反应名称**: NADH氧化与泛醌还原 (NADH Oxidation and Ubiquinone Reduction)
**2. 化学方程式**: 1.0 NADH + 1.0 H+ + 1.0 Q → 1.0 NAD+ + 1.0 QH2
**3. 核心酶信息**: 复合物 I (NADH:泛醌氧化还原酶), EC 1.6.5.3, 含FMN和Fe-S簇
**4. 动力学与调控**: 
   - 质子泵出: 4 H+ / NADH
   - ROS泄漏逻辑: 当膜电位过高(Δψm > 150 mV)或Q库饱和时, 电子从FMN或Fe-S簇泄漏至O2生成超氧化物(O2·-), 泄漏概率 ∝ Δψm × [QH2]/[Q]
   - 抑制剂: 鱼藤酮 (Rotenone), 杀粉蝶菌素A (Piericidin A)
**5. 能量与热力学**: ΔG°' ≈ -220 kJ/mol, 贡献~2.5 ATP
**6. 生理意义**: 电子传递链入口点之一, 是ROS主要泄漏位点

#### 复合物 II (琥珀酸脱氢酶)

##### 步骤 ID: ETC-02
**1. 反应名称**: 琥珀酸氧化与泛醌还原 (Succinate Oxidation and Ubiquinone Reduction)
**2. 化学方程式**: 1.0 Succinate + 1.0 Q → 1.0 Fumarate + 1.0 QH2
**3. 核心酶信息**: 复合物 II (琥珀酸脱氢酶), EC 1.3.5.1, TCA循环组成部分, 含FAD和Fe-S簇
**4. 动力学与调控**: 
   - 质子泵出: 0 H+ (不泵出质子)
   - ROS泄漏逻辑: 低泄漏风险, 但在反向电子传递(复合物II→I)时可产生大量ROS
   - 抑制剂: 丙二酸 (Malonate), 3-硝基丙酸 (3-Nitropropionic acid)
**5. 能量与热力学**: ΔG°' ≈ -150 kJ/mol, 贡献~1.5 ATP
**6. 生理意义**: 连接TCA循环和电子传递链的唯一酶, 不泵出质子

#### 复合物 III (泛醌-细胞色素c氧化还原酶)

##### 步骤 ID: ETC-03
**1. 反应名称**: 泛醇氧化与细胞色素c还原 (Ubiquinol Oxidation and Cytochrome c Reduction)
**2. 化学方程式**: 1.0 QH2 + 2.0 Cyt c(Fe3+) → 1.0 Q + 2.0 Cyt c(Fe2+) + 2.0 H+
**3. 核心酶信息**: 复合物 III (泛醌:细胞色素c氧化还原酶), EC 1.10.2.2, 含细胞色素b和c1, Rieske Fe-S簇
**4. 动力学与调控**: 
   - 质子泵出: 4 H+ / QH2 (通过Q循环机制)
   - ROS泄漏逻辑: 当Δψm过高或Q库饱和时, 半醌自由基(Q·-)在Qo位点泄漏电子至O2生成超氧化物, 泄漏概率 ∝ Δψm × [Q·-]
   - 抑制剂: 抗霉素A (Antimycin A), 粘噻唑醇 (Myxothiazol)
**5. 能量与热力学**: ΔG°' ≈ -100 kJ/mol, 贡献~1.5 ATP
**6. 生理意义**: Q循环机制实现质子泵出效率最大化, 是ROS重要泄漏位点

#### 复合物 IV (细胞色素c氧化酶)

##### 步骤 ID: ETC-04
**1. 反应名称**: 细胞色素c氧化与氧还原 (Cytochrome c Oxidation and Oxygen Reduction)
**2. 化学方程式**: 4.0 Cyt c(Fe2+) + 1.0 O2 + 8.0 H+ → 4.0 Cyt c(Fe3+) + 2.0 H2O + 4.0 H+
**3. 核心酶信息**: 复合物 IV (细胞色素c氧化酶), EC 1.9.3.1, 含血红素a和a3, CuA和CuB中心
**4. 动力学与调控**: 
   - 质子泵出: 2 H+ / O2 (化学质子) + 2 H+ / O2 (泵出质子) = 4 H+ / O2
   - ROS泄漏逻辑: 低泄漏风险, 但在缺氧或抑制剂存在时可产生少量超氧化物
   - 抑制剂: 氰化物 (Cyanide), 叠氮化物 (Azide), CO (一氧化碳)
**5. 能量与热力学**: ΔG°' ≈ -500 kJ/mol, 贡献~1.0 ATP
**6. 生理意义**: 电子传递链终点, 将电子传递给氧生成水, 是呼吸链限速步骤

#### 复合物 V (ATP合酶)

##### 步骤 ID: ETC-05
**1. 反应名称**: ATP合成 (ATP Synthesis)
**2. 化学方程式**: 1.0 ADP + 1.0 Pi + n H+(膜间隙) → 1.0 ATP + 1.0 H2O + n H+(基质)
**3. 核心酶信息**: 复合物 V (F1F0 ATP合酶), EC 3.6.3.14, 含F0质子通道和F1催化亚基
**4. 动力学与调控**: 
   - 质子动力势驱动: Δp = Δψm - 60ΔpH (mV), 需要至少4个质子通过F0合成1个ATP
   - ATP/ADP转运: 腺苷酸转运体 (ANT) 将ATP运出, ADP运入, 消耗1个质子
   - 磷酸转运: 磷酸转运体将Pi运入, 消耗1个质子
   - 总质子消耗: ~4 (ATP合成) + 1 (ANT) + 1 (Pi转运) = 6 H+ / ATP
   - 抑制剂: 寡霉素 (Oligomycin)
**5. 能量与热力学**: ΔG°' ≈ +30 kJ/mol (ATP合成), 由质子动力势驱动
**6. 生理意义**: 将电子传递链建立的质子动力势转化为ATP化学能, 是氧化磷酸化的最终步骤

### 脂质修饰精细化 (Lipid Modification)

#### 脂肪酸去饱和 (Fatty Acid Desaturation)

##### 步骤 ID: LIP-Desat
**1. 反应名称**: 硬脂酸去饱和 (Stearic Acid Desaturation)
**2. 化学方程式**: 1.0 C18:0 (硬脂酸) + 1.0 NADH + 1.0 H+ + 1.0 O2 → 1.0 C18:1 (油酸) + 1.0 NAD+ + 2.0 H2O
**3. 核心酶信息**: 硬脂酰-CoA去饱和酶1 (Stearoyl-CoA Desaturase 1, SCD1), EC 1.14.19.1, 含细胞色素b5还原酶和细胞色素b5
**4. 动力学与调控**: 
   - Km(C18:0-CoA) ~0.05-0.1 mM
   - 激活剂: 胰岛素 (转录水平), SREBP-1c (转录因子)
   - 抑制剂: PUFA (多不饱和脂肪酸), AMPK (能量感应)
   - NADH消耗: -1 (电子供体)
**5. 能量与热力学**: ΔG°' ≈ -50 kJ/mol (不可逆)
**6. 生理意义**: 将饱和脂肪酸(SFA)转化为单不饱和脂肪酸(MUFA), 降低脂毒性, 是膜脂流动性和脂滴形成的关键调节酶

#### 脂肪酸延长 (Fatty Acid Elongation)

##### 步骤 ID: LIP-Elong
**1. 反应名称**: 长链脂肪酸延长 (Long-Chain Fatty Acid Elongation)
**2. 化学方程式**: 1.0 C16:0-CoA (棕榈酰-CoA) + 1.0 Malonyl-CoA + 2.0 NADPH + 2.0 H+ → 1.0 C18:0-CoA (硬脂酰-CoA) + 1.0 CO2 + 1.0 CoA-SH + 2.0 NADP+
**3. 核心酶信息**: ELOVL (Elongation of Very Long Chain Fatty Acids) 家族, EC 2.3.1.x, 内质网膜结合酶复合体
**4. 动力学与调控**: 
   - ELOVL6特异性延长C16→C18
   - Km(Malonyl-CoA) ~0.1-0.5 mM
   - 激活剂: SREBP-1c (转录因子), 胰岛素
   - 抑制剂: AMPK (能量感应), PUFA
   - NADPH消耗: -2 (还原力)
**5. 能量与热力学**: ATP消耗: -1 (Malonyl-CoA合成), NADPH消耗: -2, ΔG°' ≈ -60 kJ/mol
**6. 生理意义**: 逐步延长脂肪酸碳链, ELOVL6调节C16/C18比例, 影响胰岛素敏感性和脂质代谢

## 模块 B：解毒与防御（化学加工厂）

### 异物摄取与外排 (Xenobiotic Transport)

#### 有机阴离子转运体 (OATP 家族)

##### 步骤 ID: XEN-01
**1. 反应名称**: OATP1B1 药物摄取 (OATP1B1 Drug Uptake)
**2. 化学方程式**: Drug(blood) + H+ → Drug(cytosol) + H+
**3. 核心酶信息**: OATP1B1 (SLCO1B1), EC 7.5.2.-, 肝脏特异性摄取转运体, 基因型: SLCO1B1
**4. 动力学与调控**: 
   - 反应机制: 次级主动转运，依赖 Na+/牛磺胆酸盐共转运产生的负膜电位
   - 速率方程: v = Vmax[Drug][H+] / (Km(Drug)[H+] + Km(H+)[Drug] + [Drug][H+])
   - 动力学参数: 
     * Km(阿托伐他汀) ~0.1-0.5 μM
     * Km(瑞舒伐他汀) ~0.01-0.1 μM
     * Km(胆红素) ~0.1-0.5 μM
     * Km(H+) ~10-100 nM (pH 依赖)
     * Vmax ~10-50 pmol/min/mg protein
   - 抑制剂: 环孢素 (Ki ~0.1-1 μM), 利福平 (Ki ~1-10 μM), 吉非贝齐 (Ki ~10-100 μM)
   - 基因多态性: SLCO1B1*5 (c.521T>C) 降低转运活性 ~50%
   - 膜定位: 肝细胞基底膜 (Basolateral membrane)
**5. 能量与热力学**: 继发性主动转运，依赖钠离子梯度，间接消耗 ATP
**6. 生理意义**: 肝脏摄取他汀类药物、胆红素和激素的主要转运体
**7. 病理结局**: 
   - SLCO1B1 缺陷: 高胆红素血症，他汀类药物摄取减少 → 肌病风险增加
   - OATP1B1 抑制: 药物相互作用 → 他汀类药物血药浓度升高

##### 步骤 ID: XEN-02
**1. 反应名称**: OATP1B3 药物摄取 (OATP1B3 Drug Uptake)
**2. 化学方程式**: Drug(blood) + H+ → Drug(cytosol) + H+
**3. 核心酶信息**: OATP1B3 (SLCO1B3), EC 7.5.2.-, 肝脏特异性摄取转运体, 基因型: SLCO1B3
**4. 动力学与调控**: 
   - 反应机制: 类似 OATP1B1，次级主动转运
   - 速率方程: v = Vmax[Drug][H+] / (Km(Drug)[H+] + Km(H+)[Drug] + [Drug][H+])
   - 动力学参数: 
     * Km(普伐他汀) ~0.1-0.5 μM
     * Km(甲氨蝶呤) ~1-10 μM
     * Km(胆红素) ~0.5-1.0 μM
     * Vmax ~5-25 pmol/min/mg protein
   - 抑制剂: 与 OATP1B1 类似，但对某些底物敏感性不同
   - 膜定位: 肝细胞基底膜 (Basolateral membrane)
**5. 能量与热力学**: 继发性主动转运，依赖钠离子梯度，间接消耗 ATP
**6. 生理意义**: 补充 OATP1B1 的功能，转运某些 OATP1B1 低亲和力底物

##### 步骤 ID: XEN-03
**1. 反应名称**: NTCP 胆酸盐摄取 (NTCP Bile Acid Uptake)
**2. 化学方程式**: Bile Acid(blood) + 2.0 Na+ → Bile Acid(cytosol) + 2.0 Na+
**3. 核心酶信息**: Na+/牛磺胆酸盐共转运蛋白 (NTCP, SLC10A1), EC 7.4.2.1, 肝脏特异性, 基因型: SLC10A1
**4. 动力学与调控**: 
   - 反应机制: Na+ 依赖性主动转运，2:1 Na+:胆酸盐 stoichiometry
   - 速率方程: v = Vmax[Bile Acid][Na+]^2 / (Km(Bile Acid)[Na+]^2 + Km(Na+)[Bile Acid] + [Bile Acid][Na+]^2)
   - 动力学参数: 
     * Km(牛磺胆酸) ~5-10 μM
     * Km(甘氨胆酸) ~10-20 μM
     * Km(Na+) ~5-15 mM
     * Vmax ~100-500 pmol/min/mg protein
   - 抑制剂: 环孢素, 利福平, 某些他汀类药物
   - 调控: 受 FXR 转录调控，胆汁酸反馈抑制
   - 膜定位: 肝细胞基底膜 (Basolateral membrane)
**5. 能量与热力学**: 原发性主动转运，直接依赖 Na+ 梯度，间接消耗 ATP
**6. 生理意义**: 肝脏摄取胆酸盐的主要转运体，维持胆汁酸肠肝循环
**7. 病理结局**: 
   - NTCP 缺陷: 胆汁酸吸收障碍 → 胆汁酸腹泻
   - NTCP 抑制: 药物性胆汁淤积

#### 多药耐药蛋白 (MDR1 & MRP 家族)

##### 步骤 ID: XEN-04
**1. 反应名称**: MDR1 药物外排 (MDR1 Drug Efflux)
**2. 化学方程式**: Drug(cytosol) + ATP → Drug(bile) + ADP + Pi
**3. 核心酶信息**: MDR1 (P-gp, ABCB1), EC 7.6.2.1, 基因型: ABCB1
**4. 动力学与调控**: 
   - 反应机制: ATP 驱动的药物外排泵，交替构象机制
   - 速率方程: v = Vmax[Drug][ATP] / (Km(Drug)[ATP] + Km(ATP)[Drug] + [Drug][ATP])
   - 动力学参数: 
     * Km(紫杉醇) ~1-10 μM
     * Km(地高辛) ~10-100 μM
     * Km(ATP) ~0.1-1 mM
     * Vmax ~10-50 pmol/min/mg protein
   - 诱导剂: 利福平 (通过 PXR), 苯巴比妥 (通过 CAR)
   - 抑制剂: 维拉帕米, 环孢素,  tariquidar
   - 基因多态性: ABCB1 3435C>T 影响表达水平
   - 膜定位: 肝细胞顶膜 (Apical membrane)
**5. 能量与热力学**: ATP 消耗: -1, ΔG°' ≈ -30 kJ/mol (不可逆)
**6. 生理意义**: 外排未结合的亲脂性药物，防止药物在细胞内蓄积
**7. 病理结局**: 
   - MDR1 过表达: 药物耐药性增加
   - MDR1 缺陷: 某些药物毒性增加

##### 步骤 ID: XEN-05
**1. 反应名称**: MRP2 结合物外排 (MRP2 Conjugate Efflux)
**2. 化学方程式**: Conjugate(cytosol) + ATP → Conjugate(bile) + ADP + Pi
**3. 核心酶信息**: MRP2 (ABCC2), EC 7.6.2.3, 基因型: ABCC2
**4. 动力学与调控**: 
   - 反应机制: ATP 驱动的有机阴离子外排泵
   - 速率方程: v = Vmax[Conjugate][ATP] / (Km(Conjugate)[ATP] + Km(ATP)[Conjugate] + [Conjugate][ATP])
   - 动力学参数: 
     * Km(胆红素葡萄糖醛酸苷) ~1-10 μM
     * Km(GSH 结合物) ~10-100 μM
     * Km(ATP) ~0.1-1 mM
     * Vmax ~5-25 pmol/min/mg protein
   - 诱导剂: 利福平, 苯巴比妥
   - 抑制剂: 环孢素, 某些非甾体抗炎药
   - 膜定位: 肝细胞顶膜 (Apical membrane)
**5. 能量与热力学**: ATP 消耗: -1, ΔG°' ≈ -30 kJ/mol (不可逆)
**6. 生理意义**: 外排结合型代谢产物、胆红素葡萄糖醛酸苷和谷胱甘肽结合物
**7. 病理结局**: 
   - MRP2 缺陷: Dubin-Johnson 综合征 →  conjugated 高胆红素血症
   - MRP2 抑制: 药物性胆汁淤积

##### 步骤 ID: XEN-06
**1. 反应名称**: BSEP 胆酸盐外排 (BSEP Bile Acid Efflux)
**2. 化学方程式**: Bile Acid(cytosol) + ATP → Bile Acid(bile) + ADP + Pi
**3. 核心酶信息**: 胆盐输出泵 (BSEP, ABCB11), EC 7.6.2.2, 肝脏特异性, 基因型: ABCB11
**4. 动力学与调控**: 
   - 反应机制: ATP 驱动的胆酸盐外排泵
   - 速率方程: v = Vmax[Bile Acid][ATP] / (Km(Bile Acid)[ATP] + Km(ATP)[Bile Acid] + [Bile Acid][ATP])
   - 动力学参数: 
     * Km(牛磺胆酸) ~0.5-5 μM
     * Km(甘氨胆酸) ~1-10 μM
     * Km(ATP) ~0.1-1 mM
     * Vmax ~50-250 pmol/min/mg protein
   - 抑制剂: 环孢素, 利福平, 某些他汀类药物, 雌二醇
   - 调控: 受 FXR 转录调控，胆汁酸反馈激活
   - 膜定位: 肝细胞顶膜 (Apical membrane)
**5. 能量与热力学**: ATP 消耗: -1, ΔG°' ≈ -30 kJ/mol (不可逆)
**6. 生理意义**: 肝脏分泌胆酸盐到胆汁的主要转运体
**7. 病理结局**: 
   - BSEP 缺陷: 进行性家族性肝内胆汁淤积症 2 型 (PFIC2)
   - BSEP 抑制: 药物性胆汁淤积

##### 步骤 ID: XEN-07
**1. 反应名称**: MATE1 阳离子外排 (MATE1 Cation Efflux)
**2. 化学方程式**: Cation(cytosol) + H+ → Cation(bile) + H+
**3. 核心酶信息**: 多药及毒素外排蛋白 1 (MATE1, SLC47A1), EC 7.4.2.-, 基因型: SLC47A1
**4. 动力学与调控**: 
   - 反应机制: H+ 交换的阳离子外排转运体
   - 速率方程: v = Vmax[Cation][H+] / (Km(Cation)[H+] + Km(H+)[Cation] + [Cation][H+])
   - 动力学参数: 
     * Km( metformin) ~10-100 μM
     * Km(西咪替丁) ~10-100 μM
     * Km(H+) ~10-100 nM (pH 依赖)
     * Vmax ~50-250 pmol/min/mg protein
   - 抑制剂: 三甲氧苄氨嘧啶, 奎尼丁
   - 膜定位: 肝细胞顶膜 (Apical membrane)
**5. 能量与热力学**: 继发性主动转运，依赖 H+ 梯度，间接消耗 ATP
**6. 生理意义**: 外排阳离子药物和内源性阳离子物质
**7. 病理结局**: 
   - MATE1 缺陷: 某些阳离子药物排泄减少 → 毒性增加



### 醇类代谢 (Alcohol Metabolism)

#### 乙醇脱氢酶系统 (Alcohol Dehydrogenase System)

##### 步骤 ID: DET-01
**1. 反应名称**: ADH1B 乙醇氧化 (ADH1B Ethanol Oxidation)
**2. 化学方程式**: 1.0 Ethanol + 1.0 NAD+ → 1.0 Acetaldehyde + 1.0 NADH + 1.0 H+
**3. 核心酶信息**: 乙醇脱氢酶 1B (ADH1B), EC 1.1.1.1, 肝脏特异性同工酶, 基因型: ADH1B
**4. 动力学与调控**: 
   - 反应机制: Ordered Bi-Bi 机制，NAD+ 先结合
   - 速率方程: v = Vmax[Ethanol][NAD+] / (Km(Ethanol)[NAD+] + Km(NAD+)[Ethanol] + [Ethanol][NAD+])
   - 动力学参数: 
     * Km(Ethanol) ~0.1-1 mM (高亲和力)
     * Km(NAD+) ~0.1-0.5 mM
     * Vmax ~100-500 μmol/min/mg protein
   - 抑制剂: 4-甲基吡唑 (4-MP), 甲醇, 乙二醇
   - 基因多态性: ADH1B*2 (Arg47His) 活性更高
   - 膜定位: 胞浆 (Cytosol)
**5. 能量与热力学**: ΔG°' ≈ -20 kJ/mol (可逆)
**6. 生理意义**: 肝脏主要的乙醇代谢酶，负责低浓度乙醇的氧化
**7. 病理结局**: 
   - ADH1B 缺陷: 乙醇代谢减慢 → 酒精敏感性增加
   - ADH1B 活性过高: 乙醛生成过快 → 酒精潮红综合征

##### 步骤 ID: DET-02
**1. 反应名称**: ADH1C 乙醇氧化 (ADH1C Ethanol Oxidation)
**2. 化学方程式**: 1.0 Ethanol + 1.0 NAD+ → 1.0 Acetaldehyde + 1.0 NADH + 1.0 H+
**3. 核心酶信息**: 乙醇脱氢酶 1C (ADH1C), EC 1.1.1.1, 肝脏特异性同工酶, 基因型: ADH1C
**4. 动力学与调控**: 
   - 反应机制: 类似 ADH1B
   - 速率方程: v = Vmax[Ethanol][NAD+] / (Km(Ethanol)[NAD+] + Km(NAD+)[Ethanol] + [Ethanol][NAD+])
   - 动力学参数: 
     * Km(Ethanol) ~1-5 mM
     * Km(NAD+) ~0.1-0.5 mM
     * Vmax ~50-250 μmol/min/mg protein
   - 基因多态性: ADH1C*1 和 ADH1C*2 活性不同
   - 膜定位: 胞浆 (Cytosol)
**5. 能量与热力学**: ΔG°' ≈ -20 kJ/mol (可逆)
**6. 生理意义**: 辅助 ADH1B 代谢乙醇

##### 步骤 ID: DET-03
**1. 反应名称**: MEOS 乙醇氧化 (MEOS Ethanol Oxidation)
**2. 化学方程式**: 1.0 Ethanol + 1.0 O2 + 1.0 NADPH + 1.0 H+ → 1.0 Acetaldehyde + 1.0 H2O + 1.0 NADP+
**3. 核心酶信息**: 微粒体乙醇氧化系统 (MEOS), 主要为 CYP2E1, EC 1.14.14.1, 基因型: CYP2E1
**4. 动力学与调控**: 
   - 反应机制: P450 单加氧酶反应
   - 速率方程: v = Vmax[Ethanol][NADPH] / (Km(Ethanol)[NADPH] + Km(NADPH)[Ethanol] + [Ethanol][NADPH])
   - 动力学参数: 
     * Km(Ethanol) ~10-50 mM (低亲和力，高浓度乙醇时活跃)
     * Km(NADPH) ~0.01-0.1 mM
     * Vmax ~10-50 μmol/min/mg protein
   - 诱导剂: 慢性乙醇暴露 (通过 ADH 产物诱导)
   - 抑制剂: 双硫仑, 酮康唑
   - 膜定位: 内质网膜 (Endoplasmic reticulum membrane)
**5. 能量与热力学**: NADPH消耗: -1, ΔG°' ≈ -30 kJ/mol (不可逆)
**6. 生理意义**: 高浓度乙醇时的主要代谢途径，慢性饮酒者的适应性反应
**7. 病理结局**: 
   - CYP2E1 诱导: 活性氧生成增加 → 氧化应激 → 肝损伤
   - CYP2E1 过表达: 药物代谢相互作用

#### 乙醛脱氢酶系统 (Acetaldehyde Dehydrogenase System)

##### 步骤 ID: DET-04
**1. 反应名称**: ALDH2 乙醛氧化 (ALDH2 Acetaldehyde Oxidation)
**2. 化学方程式**: 1.0 Acetaldehyde + 1.0 NAD+ + 1.0 H2O → 1.0 Acetate + 1.0 NADH + 2.0 H+
**3. 核心酶信息**: 乙醛脱氢酶 2 (ALDH2), EC 1.2.1.3, 线粒体酶, 基因型: ALDH2
**4. 动力学与调控**: 
   - 反应机制: Ordered Bi-Bi 机制
   - 速率方程: v = Vmax[Acetaldehyde][NAD+] / (Km(Acetaldehyde)[NAD+] + Km(NAD+)[Acetaldehyde] + [Acetaldehyde][NAD+])
   - 动力学参数: 
     * Km(Acetaldehyde) ~0.01-0.1 mM (高亲和力)
     * Km(NAD+) ~0.1-0.5 mM
     * Vmax ~200-1000 μmol/min/mg protein
   - 抑制剂: 双硫仑 (不可逆抑制), 氰化物
   - 基因多态性: ALDH2*2 (Glu504Lys) 活性极低
   - 膜定位: 线粒体 (Mitochondria)
**5. 能量与热力学**: ΔG°' ≈ -45 kJ/mol (不可逆)
**6. 生理意义**: 肝脏主要的乙醛代谢酶，负责乙醛的快速解毒
**7. 病理结局**: 
   - ALDH2 缺陷: 乙醛蓄积 → 酒精潮红综合征, 乙醛毒性
   - ALDH2 抑制: 双硫仑戒酒疗法的基础

##### 步骤 ID: DET-05
**1. 反应名称**: ALDH1A1 乙醛氧化 (ALDH1A1 Acetaldehyde Oxidation)
**2. 化学方程式**: 1.0 Acetaldehyde + 1.0 NAD+ + 1.0 H2O → 1.0 Acetate + 1.0 NADH + 2.0 H+
**3. 核心酶信息**: 乙醛脱氢酶 1A1 (ALDH1A1), EC 1.2.1.3, 胞浆酶, 基因型: ALDH1A1
**4. 动力学与调控**: 
   - 反应机制: 类似 ALDH2
   - 速率方程: v = Vmax[Acetaldehyde][NAD+] / (Km(Acetaldehyde)[NAD+] + Km(NAD+)[Acetaldehyde] + [Acetaldehyde][NAD+])
   - 动力学参数: 
     * Km(Acetaldehyde) ~1-10 mM (低亲和力)
     * Km(NAD+) ~0.1-0.5 mM
     * Vmax ~50-250 μmol/min/mg protein
   - 膜定位: 胞浆 (Cytosol)
**5. 能量与热力学**: ΔG°' ≈ -45 kJ/mol (不可逆)
**6. 生理意义**: 辅助 ALDH2 代谢乙醛，高浓度乙醛时活跃

#### 其他醇类代谢 (Other Alcohol Metabolism)

##### 步骤 ID: DET-06
**1. 反应名称**: 甲醇氧化 (Methanol Oxidation)
**2. 化学方程式**: 1.0 Methanol + 1.0 NAD+ → 1.0 Formaldehyde + 1.0 NADH + 1.0 H+
**3. 核心酶信息**: 乙醇脱氢酶 (ADH1B), EC 1.1.1.1
**4. 动力学与调控**: 
   - 速率方程: v = Vmax[Methanol][NAD+] / (Km(Methanol)[NAD+] + Km(NAD+)[Methanol] + [Methanol][NAD+])
   - 动力学参数: 
     * Km(Methanol) ~10-20 mM (比乙醇低亲和力)
     * Km(NAD+) ~0.1-0.5 mM
     * Vmax ~50-250 μmol/min/mg protein
   - 抑制剂: 4-甲基吡唑 (4-MP), 乙醇 (竞争性)
**5. 能量与热力学**: ΔG°' ≈ -15 kJ/mol (可逆)
**6. 病理结局**: 
   - 甲醇氧化产物: 甲醛 → 甲酸 → 酸中毒和视神经损伤

##### 步骤 ID: DET-07
**1. 反应名称**: 乙二醇氧化 (Ethylene Glycol Oxidation)
**2. 化学方程式**: 1.0 Ethylene Glycol + 1.0 NAD+ → 1.0 Glycoaldehyde + 1.0 NADH + 1.0 H+
**3. 核心酶信息**: 乙醇脱氢酶 (ADH1B), EC 1.1.1.1
**4. 动力学与调控**: 
   - 速率方程: v = Vmax[Ethylene Glycol][NAD+] / (Km(Ethylene Glycol)[NAD+] + Km(NAD+)[Ethylene Glycol] + [Ethylene Glycol][NAD+])
   - 动力学参数: 
     * Km(Ethylene Glycol) ~5-10 mM (比乙醇低亲和力)
     * Km(NAD+) ~0.1-0.5 mM
     * Vmax ~50-250 μmol/min/mg protein
   - 抑制剂: 4-甲基吡唑 (4-MP), 乙醇 (竞争性)
**5. 能量与热力学**: ΔG°' ≈ -18 kJ/mol (可逆)
**6. 病理结局**: 
   - 乙二醇氧化产物: 草酸 → 肾草酸钙结石和肾功能衰竭

##### 步骤 ID: DET-08
**1. 反应名称**: 丙醇氧化 (Propanol Oxidation)
**2. 化学方程式**: 1.0 Propanol + 1.0 NAD+ → 1.0 Propionaldehyde + 1.0 NADH + 1.0 H+
**3. 核心酶信息**: 乙醇脱氢酶 (ADH1B), EC 1.1.1.1
**4. 动力学与调控**: 
   - 速率方程: v = Vmax[Propanol][NAD+] / (Km(Propanol)[NAD+] + Km(NAD+)[Propanol] + [Propanol][NAD+])
   - 动力学参数: 
     * Km(Propanol) ~1-5 mM
     * Km(NAD+) ~0.1-0.5 mM
     * Vmax ~50-250 μmol/min/mg protein
**5. 能量与热力学**: ΔG°' ≈ -19 kJ/mol (可逆)

##### 步骤 ID: DET-09
**1. 反应名称**: 异丙醇氧化 (Isopropanol Oxidation)
**2. 化学方程式**: 1.0 Isopropanol + 1.0 NAD+ → 1.0 Acetone + 1.0 NADH + 1.0 H+
**3. 核心酶信息**: 乙醇脱氢酶 (ADH1B), EC 1.1.1.1
**4. 动力学与调控**: 
   - 速率方程: v = Vmax[Isopropanol][NAD+] / (Km(Isopropanol)[NAD+] + Km(NAD+)[Isopropanol] + [Isopropanol][NAD+])
   - 动力学参数: 
     * Km(Isopropanol) ~2-10 mM
     * Km(NAD+) ~0.1-0.5 mM
     * Vmax ~50-250 μmol/min/mg protein
**5. 能量与热力学**: ΔG°' ≈ -20 kJ/mol (可逆)
**6. 病理结局**: 
   - 异丙醇中毒: 丙酮蓄积 → 酮症

#### 醇类代谢的能量效应 (Energy Effects of Alcohol Metabolism)

##### 步骤 ID: DET-10
**1. 反应名称**: 乙醇代谢能量效应 (Energy Effects of Ethanol Metabolism)
**2. 化学方程式**: 
   - 乙醇氧化: 1.0 Ethanol → 1.0 Acetate (产生 2 NADH)
   - 乙酸活化: 1.0 Acetate + 1.0 CoA-SH + 1.0 ATP → 1.0 Acetyl-CoA + 1.0 AMP + 1.0 PPi
   - TCA 循环: 1.0 Acetyl-CoA → 2.0 CO2 (产生 3 NADH, 1 FADH2, 1 GTP)
**3. 核心酶信息**: 多酶系统协同作用
**4. 动力学与调控**: 
   - ATP 平衡: 每分子乙醇产生约 13-14 ATP
   - NADH/NAD+ 比值: 乙醇代谢增加 NADH/NAD+ 比值 → 抑制 TCA 循环和糖异生
   - 能量状态: 高能量状态下乙醇代谢减慢
**5. 能量与热力学**: 
   - 总 ATP 产生: +13-14 per ethanol
   - 净能量: 乙醇是高能量物质，但代谢产物抑制其他代谢
**6. 生理意义**: 
   - 能量产生: 乙醇可作为能量来源
   - 代谢抑制: 高 NADH/NAD+ 比值抑制糖异生 → 低血糖
   - 脂肪堆积: 抑制脂肪酸氧化 → 脂肪肝
**7. 病理结局**: 
   - 慢性乙醇代谢: 脂肪肝 → 酒精性肝炎 → 肝硬化
   - 急性乙醇中毒: 低血糖和中枢神经系统抑制

### 醇类代谢 (Alcohol Metabolism)

##### 步骤 ID: DET-01
**1. 反应名称**: 乙醇氧化 (Ethanol Oxidation)
**2. 化学方程式**: 1.0 Ethanol + 1.0 NAD+ → 1.0 Acetaldehyde + 1.0 NADH + 1.0 H+
**3. 核心酶信息**: 乙醇脱氢酶 (Alcohol Dehydrogenase), EC 1.1.1.1
**4. 动力学与调控**: Km(Ethanol) ~1-5 mM; 抑制剂: 甲醇、乙二醇
**5. 能量与热力学**: ΔG°' ≈ -20 kJ/mol (可逆)

##### 步骤 ID: DET-02
**1. 反应名称**: 乙醛氧化 (Acetaldehyde Oxidation)
**2. 化学方程式**: 1.0 Acetaldehyde + 1.0 NAD+ + 1.0 H2O → 1.0 Acetate + 1.0 NADH + 2.0 H+
**3. 核心酶信息**: 乙醛脱氢酶 (Acetaldehyde Dehydrogenase), EC 1.2.1.3
**4. 动力学与调控**: Km(Acetaldehyde) ~0.1-0.5 mM; 抑制剂: 双硫仑
**5. 能量与热力学**: ΔG°' ≈ -45 kJ/mol (不可逆)

##### 步骤 ID: DET-03
**1. 反应名称**: 甲醇氧化 (Methanol Oxidation)
**2. 化学方程式**: 1.0 Methanol + 1.0 NAD+ → 1.0 Formaldehyde + 1.0 NADH + 1.0 H+
**3. 核心酶信息**: 乙醇脱氢酶 (Alcohol Dehydrogenase), EC 1.1.1.1
**4. 动力学与调控**: Km(Methanol) ~10-20 mM (比乙醇低亲和力)
**5. 能量与热力学**: ΔG°' ≈ -15 kJ/mol (可逆)

##### 步骤 ID: DET-04
**1. 反应名称**: 乙二醇氧化 (Ethylene Glycol Oxidation)
**2. 化学方程式**: 1.0 Ethylene Glycol + 1.0 NAD+ → 1.0 Glycoaldehyde + 1.0 NADH + 1.0 H+
**3. 核心酶信息**: 乙醇脱氢酶 (Alcohol Dehydrogenase), EC 1.1.1.1
**4. 动力学与调控**: Km(Ethylene Glycol) ~5-10 mM (比乙醇低亲和力)
**5. 能量与热力学**: ΔG°' ≈ -18 kJ/mol (可逆)

### 药物/异物代谢 (P450系统)

#### 肝脏主要P450同工酶 (Major Hepatic P450 Isoforms)

##### 步骤 ID: DET-05
**1. 反应名称**: CYP3A4 氧化反应 (CYP3A4 Oxidation)
**2. 化学方程式**: 1.0 Substrate + 1.0 O2 + 1.0 NADPH + 1.0 H+ → 1.0 Oxidized Product + 1.0 H2O + 1.0 NADP+
**3. 核心酶信息**: 细胞色素P450 3A4 (CYP3A4), EC 1.14.13.97, 肝脏主要P450酶, 基因型: CYP3A4
**4. 动力学与调控**: 
   - 反应机制: P450 单加氧酶反应，包含底物结合、O2 活化、电子转移等步骤
   - 速率方程: v = Vmax[Substrate][NADPH] / (Km(Substrate)[NADPH] + Km(NADPH)[Substrate] + [Substrate][NADPH])
   - 动力学参数: 
     * Km(咪达唑仑) ~0.5-5 μM
     * Km(辛伐他汀) ~1-10 μM
     * Km(环孢素) ~1-5 μM
     * Km(NADPH) ~0.01-0.1 mM
     * Vmax ~10-50 pmol/min/pmol CYP
   - 底物: 占临床药物代谢的 ~50%，包括他汀类、钙通道阻滞剂、大环内酯类抗生素等
   - 诱导剂: 利福平 (通过 PXR), 苯巴比妥 (通过 CAR)
   - 抑制剂: 酮康唑, 红霉素, 葡萄柚汁 (呋喃香豆素)
   - 基因多态性: CYP3A4*22 活性降低
   - 膜定位: 内质网膜 (Endoplasmic reticulum membrane)
**5. 能量与热力学**: NADPH消耗: -1, ΔG°' ≈ -20 kJ/mol (不可逆)
**6. 生理意义**: 肝脏最重要的药物代谢酶，参与多种内源性物质 (如类固醇激素) 的代谢
**7. 病理结局**: 
   - CYP3A4 诱导: 药物代谢加快 → 药效降低
   - CYP3A4 抑制: 药物蓄积 → 毒性增加

##### 步骤 ID: DET-06
**1. 反应名称**: CYP2C9 氧化反应 (CYP2C9 Oxidation)
**2. 化学方程式**: 1.0 Substrate + 1.0 O2 + 1.0 NADPH + 1.0 H+ → 1.0 Oxidized Product + 1.0 H2O + 1.0 NADP+
**3. 核心酶信息**: 细胞色素P450 2C9 (CYP2C9), EC 1.14.13.80, 肝脏重要P450酶, 基因型: CYP2C9
**4. 动力学与调控**: 
   - 反应机制: 类似 CYP3A4
   - 速率方程: v = Vmax[Substrate][NADPH] / (Km(Substrate)[NADPH] + Km(NADPH)[Substrate] + [Substrate][NADPH])
   - 动力学参数: 
     * Km(华法林) ~1-5 μM
     * Km(布洛芬) ~10-50 μM
     * Km(甲苯磺丁脲) ~50-200 μM
     * Vmax ~5-25 pmol/min/pmol CYP
   - 底物: 非甾体抗炎药、抗凝血药、口服降糖药等
   - 诱导剂: 利福平, 苯巴比妥
   - 抑制剂: 氟康唑, 磺胺类药物
   - 基因多态性: CYP2C9*2 和 *3 活性降低
**5. 能量与热力学**: NADPH消耗: -1, ΔG°' ≈ -20 kJ/mol (不可逆)
**6. 生理意义**: 参与多种临床重要药物的代谢
**7. 病理结局**: 
   - CYP2C9 缺陷: 华法林代谢减慢 → 出血风险增加

##### 步骤 ID: DET-07
**1. 反应名称**: CYP2C19 氧化反应 (CYP2C19 Oxidation)
**2. 化学方程式**: 1.0 Substrate + 1.0 O2 + 1.0 NADPH + 1.0 H+ → 1.0 Oxidized Product + 1.0 H2O + 1.0 NADP+
**3. 核心酶信息**: 细胞色素P450 2C19 (CYP2C19), EC 1.14.13.40, 肝脏重要P450酶, 基因型: CYP2C19
**4. 动力学与调控**: 
   - 反应机制: 类似 CYP3A4
   - 速率方程: v = Vmax[Substrate][NADPH] / (Km(Substrate)[NADPH] + Km(NADPH)[Substrate] + [Substrate][NADPH])
   - 动力学参数: 
     * Km(奥美拉唑) ~1-10 μM
     * Km(氯吡格雷) ~5-20 μM
     * Km(丙戊酸) ~100-500 μM
     * Vmax ~5-25 pmol/min/pmol CYP
   - 底物: 质子泵抑制剂、抗血小板药、抗癫痫药等
   - 诱导剂: 利福平, 苯巴比妥
   - 抑制剂: 氟伏沙明, 酮康唑
   - 基因多态性: CYP2C19*2 和 *3 为弱代谢型，*17 为超快代谢型
**5. 能量与热力学**: NADPH消耗: -1, ΔG°' ≈ -20 kJ/mol (不可逆)
**6. 生理意义**: 参与多种临床重要药物的代谢
**7. 病理结局**: 
   - CYP2C19 缺陷: 氯吡格雷活化减少 → 心血管事件风险增加

##### 步骤 ID: DET-08
**1. 反应名称**: CYP2D6 氧化反应 (CYP2D6 Oxidation)
**2. 化学方程式**: 1.0 Substrate + 1.0 O2 + 1.0 NADPH + 1.0 H+ → 1.0 Oxidized Product + 1.0 H2O + 1.0 NADP+
**3. 核心酶信息**: 细胞色素P450 2D6 (CYP2D6), EC 1.14.14.1, 肝脏重要P450酶, 基因型: CYP2D6
**4. 动力学与调控**: 
   - 反应机制: 类似 CYP3A4，但对底物结构要求严格
   - 速率方程: v = Vmax[Substrate][NADPH] / (Km(Substrate)[NADPH] + Km(NADPH)[Substrate] + [Substrate][NADPH])
   - 动力学参数: 
     * Km(地昔帕明) ~0.1-1 μM
     * Km(氟西汀) ~1-10 μM
     * Km(可待因) ~10-50 μM
     * Vmax ~5-25 pmol/min/pmol CYP
   - 底物: 占临床药物代谢的 ~25%，包括抗抑郁药、抗精神病药、阿片类药物等
   - 诱导剂: 无强诱导剂
   - 抑制剂: 帕罗西汀, 氟西汀, 奎尼丁
   - 基因多态性: 高度多态，从无功能到超功能等位基因
**5. 能量与热力学**: NADPH消耗: -1, ΔG°' ≈ -20 kJ/mol (不可逆)
**6. 生理意义**: 参与多种中枢神经系统药物的代谢
**7. 病理结局**: 
   - CYP2D6 缺陷: 可待因无法转化为吗啡 → 镇痛效果降低
   - CYP2D6 超功能: 某些药物代谢过快 → 药效降低

##### 步骤 ID: DET-09
**1. 反应名称**: CYP1A2 氧化反应 (CYP1A2 Oxidation)
**2. 化学方程式**: 1.0 Substrate + 1.0 O2 + 1.0 NADPH + 1.0 H+ → 1.0 Oxidized Product + 1.0 H2O + 1.0 NADP+
**3. 核心酶信息**: 细胞色素P450 1A2 (CYP1A2), EC 1.14.14.1, 肝脏重要P450酶, 基因型: CYP1A2
**4. 动力学与调控**: 
   - 反应机制: 类似 CYP3A4
   - 速率方程: v = Vmax[Substrate][NADPH] / (Km(Substrate)[NADPH] + Km(NADPH)[Substrate] + [Substrate][NADPH])
   - 动力学参数: 
     * Km(咖啡因) ~50-200 μM
     * Km(茶碱) ~10-50 μM
     * Km(对乙酰氨基酚) ~100-500 μM
     * Vmax ~10-50 pmol/min/pmol CYP
   - 底物: 咖啡因、茶碱、某些抗精神病药等
   - 诱导剂: 烟草烟雾 (多环芳烃), 烧煮肉类 (杂环胺)
   - 抑制剂: 氟伏沙明, 喹诺酮类抗生素
   - 基因多态性: CYP1A2*1F 活性增加
**5. 能量与热力学**: NADPH消耗: -1, ΔG°' ≈ -20 kJ/mol (不可逆)
**6. 生理意义**: 参与咖啡因等食物成分和某些药物的代谢
**7. 病理结局**: 
   - CYP1A2 诱导: 茶碱代谢加快 → 药效降低
   - CYP1A2 抑制: 茶碱蓄积 → 毒性增加

##### 步骤 ID: DET-10
**1. 反应名称**: CYP2E1 氧化反应 (CYP2E1 Oxidation)
**2. 化学方程式**: 1.0 Substrate + 1.0 O2 + 1.0 NADPH + 1.0 H+ → 1.0 Oxidized Product + 1.0 H2O + 1.0 NADP+
**3. 核心酶信息**: 细胞色素P450 2E1 (CYP2E1), EC 1.14.13.13, 肝脏重要P450酶, 基因型: CYP2E1
**4. 动力学与调控**: 
   - 反应机制: 类似 CYP3A4
   - 速率方程: v = Vmax[Substrate][NADPH] / (Km(Substrate)[NADPH] + Km(NADPH)[Substrate] + [Substrate][NADPH])
   - 动力学参数: 
     * Km(乙醇) ~10-50 mM (高浓度时)
     * Km(对乙酰氨基酚) ~500-1000 μM
     * Km(氯仿) ~1-10 μM
     * Vmax ~5-25 pmol/min/pmol CYP
   - 底物: 乙醇、对乙酰氨基酚 (产生 NAPQI)、多种有机溶剂等
   - 诱导剂: 乙醇 (慢性), 异烟肼
   - 抑制剂: 双硫仑, 酮康唑
   - 膜定位: 内质网膜 (Endoplasmic reticulum membrane)
**5. 能量与热力学**: NADPH消耗: -1, ΔG°' ≈ -20 kJ/mol (不可逆)
**6. 生理意义**: 参与乙醇和多种毒物的代谢
**7. 病理结局**: 
   - CYP2E1 诱导: 活性氧生成增加 → 氧化应激 → 肝损伤
   - 对乙酰氨基酚过量: NAPQI 生成增加 → 肝坏死

#### P450 酶系统的电子传递链 (P450 Electron Transfer Chain)

##### 步骤 ID: DET-11
**1. 反应名称**: P450 还原酶反应 (P450 Reductase Reaction)
**2. 化学方程式**: 1.0 NADPH + 1.0 Cyt P450 (Fe3+) → 1.0 NADP+ + 1.0 Cyt P450 (Fe2+)
**3. 核心酶信息**: NADPH-细胞色素P450还原酶 (CPR), EC 1.6.2.4
**4. 动力学与调控**: 
   - 反应机制: 包含 FAD 和 FMN 两个辅基的电子传递
   - 速率方程: v = Vmax[NADPH][P450] / (Km(NADPH)[P450] + Km(P450)[NADPH] + [NADPH][P450])
   - 动力学参数: 
     * Km(NADPH) ~0.01-0.1 mM
     * Km(P450) ~0.1-1 μM
     * Vmax ~100-500 nmol/min/mg protein
   - 调控: CPR 为所有 P450 酶提供电子，是限速步骤之一
   - 膜定位: 内质网膜 (Endoplasmic reticulum membrane)
**5. 能量与热力学**: NADPH消耗: -1, ΔG°' ≈ -10 kJ/mol (可逆)
**6. 生理意义**: P450 酶系统的电子供体，对所有 P450 反应至关重要
**7. 病理结局**: 
   - CPR 缺陷: 所有 P450 酶活性降低 → 药物代谢障碍

#### P450 酶的诱导与抑制网络 (P450 Induction and Inhibition Network)

##### 步骤 ID: DET-12
**1. 反应名称**: P450 酶调控网络 (P450 Regulatory Network)
**2. 化学方程式**: 
   - 诱导: Inducer + Nuclear Receptor → 转录激活 → P450 mRNA → P450 蛋白
   - 抑制: Inhibitor + P450 → 酶活性降低
**3. 核心酶信息**: 多系统协同作用
**4. 动力学与调控**: 
   - 核受体调控: PXR (NR1I2)、CAR (NR1I3)、AhR 等
   - 诱导时间: 数小时到数天
   - 抑制类型: 竞争性、非竞争性、机制性抑制
   - 药物相互作用: 多种药物可通过诱导或抑制 P450 酶影响其他药物的代谢
**5. 能量与热力学**: 诱导过程消耗 ATP (转录和翻译)
**6. 生理意义**: 肝脏对药物和异物的适应性反应
**7. 病理结局**: 
   - 药物相互作用: 可导致药效降低或毒性增加
   - 慢性诱导: 可能增加某些致癌物的活化

### II相代谢 (Phase II Conjugation)

#### 葡糖醛酸结合 (Glucuronidation)

##### 步骤 ID: TOX-Conj-01
**1. 反应名称**: 葡糖醛酸结合 (Glucuronidation)
**2. 化学方程式**: 1.0 Substrate + 1.0 UDP-Glucuronic Acid → 1.0 Glucuronide Conjugate + 1.0 UDP
**3. 核心酶信息**: UDP-葡萄糖醛酸转移酶 (UGT) 家族, EC 2.4.1.17, 肝脏特异性同工酶: UGT1A1, UGT2B7, 基因型: UGT1A1, UGT2B7
**4. 动力学与调控**: 
   - 速率方程: v = Vmax[Substrate][UDP-GA] / (Km(Substrate)[UDP-GA] + Km(UDP-GA)[Substrate] + [Substrate][UDP-GA])
   - 动力学参数: 
     * UGT1A1 Km(胆红素) ~0.1-0.5 μM
     * UGT1A1 Km(对乙酰氨基酚) ~100-500 μM
     * UGT2B7 Km(吗啡) ~10-50 μM
     * Vmax ~10-50 pmol/min/mg protein
   - 抑制类型: 
     * 底物竞争: 多种底物可竞争同一UGT同工酶
     * 产物抑制: 葡糖醛酸结合物可抑制UGT活性
   - 激活剂: 
     * 某些药物 (如利福平) 可通过PXR诱导UGT表达
     * Nrf2激活可诱导UGT表达
   - 抑制剂: 
     * 某些药物 (如丙磺舒) 可抑制UGT活性
   - 膜定位: 内质网膜 (Endoplasmic reticulum membrane)
**5. 能量与热力学**: 
   - UDP-GA 合成消耗 ATP: 间接消耗 1 ATP
   - ΔG°' ≈ -15 kJ/mol (不可逆)
**6. 功能说明**: 将亲脂性底物转化为水溶性葡糖醛酸结合物，便于通过胆汁或尿液排出
**7. 生理意义**: 肝脏主要的解毒途径之一，参与胆红素、药物、激素等的代谢
**8. 病理结局**: 
   - UGT1A1缺陷: 克里格勒-纳贾尔综合征 (Crigler-Najjar syndrome)，未结合胆红素升高
   - UGT1A1变异: 吉尔伯特综合征 (Gilbert syndrome)，轻度未结合胆红素升高
   - UGT抑制: 药物代谢减慢，药物蓄积，毒性增加

#### 硫酸结合 (Sulfation)

##### 步骤 ID: TOX-Conj-02
**1. 反应名称**: 硫酸结合 (Sulfation)
**2. 化学方程式**: 1.0 Substrate + 1.0 PAPS (3'-磷酸腺苷-5'-磷酸硫酸) → 1.0 Sulfate Conjugate + 1.0 PAP (3'-磷酸腺苷-5'-磷酸)
**3. 核心酶信息**: 硫酸转移酶 (SULT) 家族, EC 2.8.2.x, 肝脏特异性同工酶: SULT1A1, SULT2A1, 基因型: SULT1A1, SULT2A1
**4. 动力学与调控**: 
   - 速率方程: v = Vmax[Substrate][PAPS] / (Km(Substrate)[PAPS] + Km(PAPS)[Substrate] + [Substrate][PAPS])
   - 动力学参数: 
     * SULT1A1 Km(对硝基酚) ~1-10 μM
     * SULT1A1 Km(雌二醇) ~0.1-1 μM
     * SULT2A1 Km(脱氢表雄酮) ~0.1-1 μM
     * Vmax ~5-20 pmol/min/mg protein
   - 抑制类型: 
     * PAP: 产物抑制剂 (非竞争性)，Ki ~0.1-1 μM
     * 底物竞争: 多种底物可竞争同一SULT同工酶
   - 激活剂: 
     * 某些激素可诱导SULT表达
   - 抑制剂: 
     * PAP (产物反馈抑制)
     * 某些药物可抑制SULT活性
   - 膜定位: 胞浆 (Cytosol)
**5. 能量与热力学**: 
   - PAPS 合成消耗 2 ATP
   - ΔG°' ≈ -20 kJ/mol (不可逆)
**6. 功能说明**: 将底物与硫酸根结合，增加水溶性和排泄性，是许多药物的主要代谢途径
**7. 生理意义**: 参与酚类、醇类、胺类化合物和激素的代谢
**8. 病理结局**: 
   - SULT缺陷: 某些药物代谢减慢，药物蓄积，毒性增加
   - PAPS合成障碍: 硫酸结合能力下降，影响药物和内源性物质的代谢

#### 谷胱甘肽结合 (GSH Conjugation)

##### 步骤 ID: TOX-Conj-03
**1. 反应名称**: 谷胱甘肽结合 (GSH Conjugation)
**2. 化学方程式**: 1.0 Substrate + 1.0 GSH (谷胱甘肽) → 1.0 GSH Conjugate
**3. 核心酶信息**: 谷胱甘肽S-转移酶 (GST) 家族, EC 2.5.1.18, 肝脏特异性同工酶: GSTα, GSTπ, 基因型: GSTA1, GSTP1
**4. 动力学与调控**: 
   - 速率方程: v = Vmax[Substrate][GSH] / (Km(Substrate)[GSH] + Km(GSH)[Substrate] + [Substrate][GSH])
   - 动力学参数: 
     * GSTα Km(NAPQI) ~10-100 μM
     * GSTπ Km(1-氯-2,4-二硝基苯) ~100-500 μM
     * Km(GSH) ~0.5-5 mM
     * Vmax ~50-200 pmol/min/mg protein
   - 抑制类型: 
     * 底物竞争: 多种底物可竞争同一GST同工酶
   - 激活剂: 
     * Nrf2激活可诱导GST表达
     * 某些药物可诱导GST表达
   - 抑制剂: 
     * 某些药物可抑制GST活性
   - 膜定位: 胞浆 (Cytosol)
**5. 能量与热力学**: 
   - GSH 合成消耗 ATP: 间接消耗 1 ATP
   - ΔG°' ≈ -10 kJ/mol (不可逆)
**6. 功能说明**: 是 NAPQI 等活性中间体的最终归宿，防止其与细胞大分子结合造成损伤
**7. 生理意义**: 肝脏重要的解毒途径，保护细胞免受亲电子化合物和活性氧的损伤
**8. 病理结局**: 
   - GST缺陷: 对亲电子化合物和活性氧的敏感性增加，易发生氧化损伤
   - GSH耗尽: 氧化应激增加，可能导致细胞凋亡或坏死
**9. 逻辑门**: 若 GSH 耗尽，则触发氧化应激报警，可能导致细胞凋亡或坏死

#### 乙酰化 (Acetylation)

##### 步骤 ID: TOX-Conj-04
**1. 反应名称**: 乙酰化 (Acetylation)
**2. 化学方程式**: 1.0 Substrate + 1.0 Acetyl-CoA → 1.0 Acetylated Conjugate + 1.0 CoA-SH
**3. 核心酶信息**: N-乙酰转移酶 (NAT) 家族, EC 2.3.1.5, 肝脏特异性同工酶: NAT2, 基因型: NAT2
**4. 动力学与调控**: 
   - 速率方程: v = Vmax[Substrate][Acetyl-CoA] / (Km(Substrate)[Acetyl-CoA] + Km(Acetyl-CoA)[Substrate] + [Substrate][Acetyl-CoA])
   - 动力学参数: 
     * NAT2 Km(异烟肼) ~100-500 μM
     * NAT2 Km(磺胺类药物) ~50-200 μM
     * Vmax ~5-20 pmol/min/mg protein
   - 抑制类型: 
     * 底物竞争: 多种底物可竞争同一NAT同工酶
   - 激活剂: 
     * 某些药物可诱导NAT表达
   - 抑制剂: 
     * 某些药物可抑制NAT活性
   - 膜定位: 胞浆 (Cytosol)
**5. 能量与热力学**: 
   - 间接消耗 ATP (Acetyl-CoA 合成)
   - ΔG°' ≈ -10 kJ/mol (不可逆)
**6. 功能说明**: 将底物与乙酰基结合，改变底物的水溶性和生物活性
**7. 生理意义**: 参与胺类药物和内源性物质的代谢
**8. 病理结局**: 
   - NAT2慢乙酰化型: 异烟肼代谢减慢，周围神经炎风险增加
   - NAT2快乙酰化型: 某些药物代谢加快，可能降低药效

#### 甲基化 (Methylation)

##### 步骤 ID: TOX-Conj-05
**1. 反应名称**: 甲基化 (Methylation)
**2. 化学方程式**: 1.0 Substrate + 1.0 S-Adenosylmethionine (SAM) → 1.0 Methylated Conjugate + 1.0 S-Adenosylhomocysteine (SAH)
**3. 核心酶信息**: 儿茶酚-O-甲基转移酶 (COMT) 和其他甲基转移酶, EC 2.1.1.6, 肝脏特异性: COMT, 基因型: COMT
**4. 动力学与调控**: 
   - 速率方程: v = Vmax[Substrate][SAM] / (Km(Substrate)[SAM] + Km(SAM)[Substrate] + [Substrate][SAM] + Ki(SAH)[SAH])
   - 动力学参数: 
     * COMT Km(多巴胺) ~1-10 μM
     * COMT Km(SAM) ~10-50 μM
     * Vmax ~10-50 pmol/min/mg protein
   - 抑制类型: 
     * SAH: 产物抑制剂 (非竞争性)，Ki ~1-10 μM
   - 激活剂: 
     * 某些药物可诱导甲基转移酶表达
   - 抑制剂: 
     * SAH (产物反馈抑制)
     * 某些药物可抑制甲基转移酶活性
   - 膜定位: 胞浆 (Cytosol)
**5. 能量与热力学**: 
   - SAM 合成消耗 ATP: 间接消耗 1 ATP
   - ΔG°' ≈ -5 kJ/mol (可逆)
**6. 功能说明**: 将底物与甲基结合，改变底物的水溶性和生物活性
**7. 生理意义**: 参与儿茶酚胺、药物和内源性物质的代谢
**8. 病理结局**: 
   - 甲基转移酶缺陷: 某些药物代谢减慢，药物蓄积，毒性增加
   - SAM合成障碍: 甲基化能力下降，影响药物和内源性物质的代谢

#### 氨基酸结合 (Amino Acid Conjugation)

##### 步骤 ID: TOX-Conj-06
**1. 反应名称**: 甘氨酸结合 (Glycine Conjugation)
**2. 化学方程式**: 1.0 Benzoic Acid + 1.0 CoA-SH + 1.0 ATP → 1.0 Benzoyl-CoA + 1.0 AMP + 1.0 PPi; 1.0 Benzoyl-CoA + 1.0 Glycine → 1.0 Hippuric Acid + 1.0 CoA-SH
**3. 核心酶信息**: 酰基辅酶A合成酶和甘氨酸N-酰基转移酶, EC 6.2.1.2, EC 2.3.1.13, 肝脏特异性: 甘氨酸N-酰基转移酶, 基因型: GLYAT
**4. 动力学与调控**: 
   - 速率方程: v = Vmax[Benzoic Acid][CoA-SH][ATP][Glycine] / (K1[CoA-SH][ATP][Glycine] + K2[Benzoic Acid][ATP][Glycine] + K3[Benzoic Acid][CoA-SH][Glycine] + K4[Benzoic Acid][CoA-SH][ATP] + [Benzoic Acid][CoA-SH][ATP][Glycine])
   - 动力学参数: 
     * Km(苯甲酸) ~100-500 μM
     * Km(甘氨酸) ~1-5 mM
     * Vmax ~5-20 pmol/min/mg protein
   - 抑制类型: 
     * 底物竞争: 多种底物可竞争同一酶
   - 激活剂: 
     * 某些药物可诱导酶表达
   - 抑制剂: 
     * 某些药物可抑制酶活性
   - 膜定位: 线粒体 (Mitochondria)
**5. 能量与热力学**: 
   - ATP 消耗: -1
   - ΔG°' ≈ -20 kJ/mol (不可逆)
**6. 功能说明**: 将底物与甘氨酸结合，增加水溶性和排泄性
**7. 生理意义**: 参与苯甲酸等化合物的代谢
**8. 病理结局**: 
   - 甘氨酸结合缺陷: 苯甲酸代谢减慢，可能导致毒性增加
   - 甘氨酸缺乏: 甘氨酸结合能力下降，影响相关化合物的代谢


**1. 反应名称**: 葡糖醛酸结合 (Glucuronidation)
**2. 化学方程式**: 1.0 Substrate + 1.0 UDP-Glucuronic Acid → 1.0 Glucuronide Conjugate + 1.0 UDP
**3. 核心酶信息**: UDP-葡萄糖醛酸转移酶 (UGT) 家族, EC 2.4.1.17, 如 UGT1A1 (胆红素特异性)
**4. 动力学与调控**: 
   - 依赖UDP-GA的供应: UDP-GA 由 UDP-Glucose 氧化生成
   - 竞争关系: 与糖原合成竞争 UDP-Glucose 原料，高糖状态下糖原合成增加可减少葡糖醛酸结合
   - 底物: 胆红素、药物、激素、内源性代谢物
   - 诱导剂: 某些药物 (如利福平) 可诱导 UGT 表达
**5. 能量与热力学**: 
   - UDP-GA 合成消耗 ATP: 间接消耗 1 ATP
   - ΔG°' ≈ -15 kJ/mol (不可逆)
**6. 功能说明**: 将亲脂性底物转化为水溶性葡糖醛酸结合物，便于通过胆汁或尿液排出

#### 硫酸结合 (Sulfation)

##### 步骤 ID: TOX-Conj-02
**1. 反应名称**: 硫酸结合 (Sulfation)
**2. 化学方程式**: 1.0 Substrate + 1.0 PAPS (3'-磷酸腺苷-5'-磷酸硫酸) → 1.0 Sulfate Conjugate + 1.0 PAP (3'-磷酸腺苷-5'-磷酸)
**3. 核心酶信息**: 硫酸转移酶 (SULT) 家族, EC 2.8.2.x, 如 SULT1A1
**4. 动力学与调控**: 
   - PAPS 消耗: PAPS 是硫酸基的活性供体
   - PAPS 合成: 由 ATP 和硫酸盐合成，需要 2 个 ATP
   - 底物: 酚类、醇类、胺类化合物、某些激素
   - 限制因素: 受半胱氨酸水平限制（硫酸盐来源）
**5. 能量与热力学**: 
   - PAPS 合成消耗 2 ATP
   - ΔG°' ≈ -20 kJ/mol (不可逆)
**6. 功能说明**: 将底物与硫酸根结合，增加水溶性和排泄性，是许多药物的主要代谢途径

#### 谷胱甘肽结合 (GSH Conjugation)

##### 步骤 ID: TOX-Conj-03
**1. 反应名称**: 谷胱甘肽结合 (GSH Conjugation)
**2. 化学方程式**: 1.0 Substrate + 1.0 GSH (谷胱甘肽) → 1.0 GSH Conjugate
**3. 核心酶信息**: 谷胱甘肽S-转移酶 (GST) 家族, EC 2.5.1.18, 如 GSTπ, GSTα
**4. 动力学与调控**: 
   - GSH 消耗: 不可逆地消耗 GSH
   - GSH 合成: 需要谷氨酸、半胱氨酸和甘氨酸，消耗 ATP
   - 底物: 亲电子化合物、活性氧中间体 (如 NAPQI)
   - 限制因素: 受 GSH 水平限制
**5. 能量与热力学**: 
   - GSH 合成消耗 ATP: 间接消耗 1 ATP
   - ΔG°' ≈ -10 kJ/mol (不可逆)
**6. 功能说明**: 是 NAPQI 等活性中间体的最终归宿，防止其与细胞大分子结合造成损伤
**7. 逻辑门**: 若 GSH 耗尽，则触发氧化应激报警，可能导致细胞凋亡或坏死

### 药代动力学闭环 (PK Closed Loop)

##### 步骤 ID: PK-01
**1. 反应名称**: 药物代谢闭环 (Drug Metabolism Closed Loop)
**2. 化学方程式**: 
   - 摄取: Drug(blood) → Drug(cytosol) [OATP]
   - 氧化: Drug(cytosol) → Oxidized Drug(cytosol) [P450]
   - 结合: Oxidized Drug(cytosol) + Co-factor → Conjugate(cytosol) [Phase II]
   - 外排: Conjugate(cytosol) → Conjugate(bile/blood) [MDR1/MRP]
**3. 核心酶信息**: 多酶系统协同作用
**4. 动力学与调控**: 
   - 限速步骤: 通常是 P450 氧化或转运过程
   - ATP 依赖: 外排泵直接消耗 ATP，结合反应间接消耗 ATP
   - 底物竞争: 多种药物可竞争同一酶或转运体
**5. 能量与热力学**: 
   - 总 ATP 消耗: 每分子药物约消耗 2-4 ATP
   - 效率: 高能量状态下代谢效率高，ATP 耗尽时代谢受阻
**6. 生理意义**: 构建完整的‘进 -> 氧化 -> 结合 -> 出’药代动力学闭环，确保药物和毒物的有效清除
**7. 逻辑门**: 
   - ATP 耗尽: 毒物堆积 → 细胞坏死
   - GSH 耗尽: 氧化应激 → 细胞凋亡
   - 转运体抑制: 药物相互作用 → 不良反应

### 内源性废物处理 (Bilirubin Metabolism)

##### 步骤 ID: DET-07
**1. 反应名称**: 血红素降解 (Heme Degradation)
**2. 化学方程式**: 1.0 Heme + 3.0 O2 + 3.0 NADPH + 3.0 H+ → 1.0 Biliverdin + 1.0 CO + 1.0 Fe2+ + 3.0 NADP+ + 3.0 H2O
**3. 核心酶信息**: 血红素氧合酶 (Heme Oxygenase), EC 1.14.14.18, 肝脏特异性同工酶: HO-1 (诱导型), HO-2 (组成型), 基因型: HMOX1, HMOX2
**4. 动力学与调控**: 
   - 速率方程: v = Vmax[Heme][O2][NADPH] / (K1[O2][NADPH] + K2[Heme][NADPH] + K3[Heme][O2] + [Heme][O2][NADPH])
   - 动力学参数: 
     * Km(Heme) ~0.1-0.5 μM
     * Km(O2) ~10-50 μM
     * Km(NADPH) ~0.01-0.05 mM
     * Vmax ~10-50 pmol/min/mg protein
   - 抑制类型: 无强变构调控
   - 激活剂: 
     * 氧化应激 (HO-1诱导剂)
     * 重金属离子 (HO-1诱导剂)
     * 血红素 (HO-1诱导剂)
   - 抑制剂: 
     * 锌原卟啉 (ZnPP，HO抑制剂)
     * 锡原卟啉 (SnPP，HO抑制剂)
   - 膜定位: 内质网膜 (Endoplasmic reticulum membrane)
**5. 能量与热力学**: NADPH消耗: -3, ΔG°' ≈ -50 kJ/mol (不可逆)
**6. 生理意义**: 降解血红素，生成胆绿素，是胆红素合成的第一步
**7. 病理结局**: 
   - HO-1过表达: 胆红素生成增加 → 高胆红素血症
   - HO-1缺乏: 血红素堆积 → 溶血性贫血

##### 步骤 ID: DET-08
**1. 反应名称**: 胆红素生成 (Bilirubin Formation)
**2. 化学方程式**: 1.0 Biliverdin + 1.0 NADPH + 1.0 H+ → 1.0 Bilirubin + 1.0 NADP+
**3. 核心酶信息**: 胆绿素还原酶 (Biliverdin Reductase), EC 1.3.1.24, 肝脏特异性: BLVRA, BLVRB, 基因型: BLVRA, BLVRB
**4. 动力学与调控**: 
   - 速率方程: v = Vmax[Biliverdin][NADPH] / (Km(Biliverdin)[NADPH] + Km(NADPH)[Biliverdin] + [Biliverdin][NADPH])
   - 动力学参数: 
     * Km(Biliverdin) ~0.1-0.5 μM
     * Km(NADPH) ~0.01-0.05 mM
     * Vmax ~10-50 pmol/min/mg protein
   - 抑制类型: 无强变构调控
   - 激活剂: 
     * 某些氧化应激条件可诱导BLVR表达
   - 抑制剂: 
     * 某些重金属离子
   - 膜定位: 胞浆 (Cytosol)
**5. 能量与热力学**: NADPH消耗: -1, ΔG°' ≈ -25 kJ/mol (不可逆)
**6. 生理意义**: 将胆绿素还原为胆红素，是胆红素合成的第二步
**7. 病理结局**: 
   - BLVR缺陷: 胆绿素堆积 → 胆绿素血症
   - BLVR缺乏: 可能导致新生儿黄疸

##### 步骤 ID: DET-09
**1. 反应名称**: 胆红素结合 (Bilirubin Conjugation)
**2. 化学方程式**: 1.0 Bilirubin + 2.0 UDP-Glucuronic Acid → 1.0 Bilirubin Diglucuronide + 2.0 UDP
**3. 核心酶信息**: UDP-葡萄糖醛酸转移酶 1A1 (UDP-Glucuronosyltransferase 1A1), EC 2.4.1.17, 肝脏特异性: UGT1A1, 基因型: UGT1A1
**4. 动力学与调控**: 
   - 速率方程: v = Vmax[Bilirubin][UDP-GA] / (Km(Bilirubin)[UDP-GA] + Km(UDP-GA)[Bilirubin] + [Bilirubin][UDP-GA])
   - 动力学参数: 
     * Km(Bilirubin) ~0.1-0.5 μM
     * Km(UDP-GA) ~0.1-0.5 mM
     * Vmax ~10-50 pmol/min/mg protein
   - 抑制类型: 
     * 底物竞争: 多种底物可竞争UGT1A1
   - 激活剂: 
     * 某些药物 (如利福平) 可通过PXR诱导UGT1A1表达
     * Nrf2激活可诱导UGT1A1表达
   - 抑制剂: 
     * 某些药物 (如丙磺舒) 可抑制UGT1A1活性
   - 膜定位: 内质网膜 (Endoplasmic reticulum membrane)
**5. 能量与热力学**: ΔG°' ≈ -30 kJ/mol (不可逆)
**6. 生理意义**: 将胆红素与葡糖醛酸结合，增加水溶性，便于通过胆汁排出
**7. 病理结局**: 
   - UGT1A1缺陷: 克里格勒-纳贾尔综合征 (Crigler-Najjar syndrome)，未结合胆红素升高
   - UGT1A1变异: 吉尔伯特综合征 (Gilbert syndrome)，轻度未结合胆红素升高
   - UGT1A1抑制: 胆红素代谢减慢 → 高胆红素血症

### 氧化应激防御 (Oxidative Stress Defense)

##### 步骤 ID: DET-10
**1. 反应名称**: 超氧化物歧化 (Superoxide Dismutation)
**2. 化学方程式**: 2.0 O2- + 2.0 H+ → 1.0 O2 + 1.0 H2O2
**3. 核心酶信息**: 超氧化物歧化酶 (Superoxide Dismutase), EC 1.15.1.1, 肝脏特异性同工酶: SOD1 (Cu/Zn-SOD, 胞浆), SOD2 (Mn-SOD, 线粒体), 基因型: SOD1, SOD2
**4. 动力学与调控**: 
   - 速率方程: v = Vmax[O2-] / (Km(O2-) + [O2-])
   - 动力学参数: 
     * SOD1 Km(O2-) ~1-5 μM
     * SOD2 Km(O2-) ~1-5 μM
     * Vmax ~10-50 μmol/min/mg protein
   - 抑制类型: 无强变构调控
   - 激活剂: 
     * 某些金属离子可激活SOD活性
   - 抑制剂: 
     * 氰化物 (Cu/Zn-SOD抑制剂)
     * 过氧化氢 (高浓度时抑制)
   - 膜定位: 胞浆 (SOD1), 线粒体基质 (SOD2)
**5. 能量与热力学**: ΔG°' ≈ -100 kJ/mol (不可逆)
**6. 生理意义**: 清除超氧阴离子，防止氧化应激
**7. 病理结局**: 
   - SOD缺陷: 超氧阴离子堆积 → 氧化应激 → 细胞损伤
   - SOD过表达: 可能干扰正常的氧化还原平衡

##### 步骤 ID: DET-11
**1. 反应名称**: 过氧化氢分解 (Hydrogen Peroxide Decomposition)
**2. 化学方程式**: 2.0 H2O2 → 2.0 H2O + 1.0 O2
**3. 核心酶信息**: 过氧化氢酶 (Catalase), EC 1.11.1.6, 肝脏特异性: CAT, 基因型: CAT
**4. 动力学与调控**: 
   - 速率方程: v = Vmax[H2O2] / (Km(H2O2) + [H2O2])
   - 动力学参数: 
     * Km(H2O2) ~10-20 mM
     * Vmax ~100-500 μmol/min/mg protein
   - 抑制类型: 无强变构调控
   - 激活剂: 
     * 某些金属离子可激活过氧化氢酶活性
   - 抑制剂: 
     * 氰化物
     * 叠氮化物
     * 3-AT (3-氨基-1,2,4-三唑)
   - 膜定位: 过氧化物酶体 (Peroxisome)
**5. 能量与热力学**: ΔG°' ≈ -90 kJ/mol (不可逆)
**6. 生理意义**: 清除过氧化氢，防止氧化应激
**7. 病理结局**: 
   - 过氧化氢酶缺陷: 过氧化氢堆积 → 氧化应激 → 细胞损伤
   - 过氧化氢酶缺乏: 可能导致某些遗传性疾病

##### 步骤 ID: DET-12
**1. 反应名称**: 谷胱甘肽还原 (Glutathione Reduction)
**2. 化学方程式**: 1.0 GSSG + 1.0 NADPH + 1.0 H+ → 2.0 GSH + 1.0 NADP+
**3. 核心酶信息**: 谷胱甘肽还原酶 (Glutathione Reductase), EC 1.8.1.7, 肝脏特异性: GSR, 基因型: GSR
**4. 动力学与调控**: 
   - 速率方程: v = Vmax[GSSG][NADPH] / (Km(GSSG)[NADPH] + Km(NADPH)[GSSG] + [GSSG][NADPH])
   - 动力学参数: 
     * Km(GSSG) ~0.1-0.5 mM
     * Km(NADPH) ~0.01-0.05 mM
     * Vmax ~10-50 μmol/min/mg protein
   - 抑制类型: 
     * NADP+: 产物抑制剂 (竞争性)，Ki ~0.01-0.05 mM
   - 激活剂: 
     * 某些氧化应激条件可诱导GSR表达
   - 抑制剂: 
     * NADP+ (产物反馈抑制)
     * 某些重金属离子
   - 膜定位: 胞浆 (Cytosol)
**5. 能量与热力学**: NADPH消耗: -1, ΔG°' ≈ -20 kJ/mol (不可逆)
**6. 生理意义**: 再生还原型谷胱甘肽，维持细胞抗氧化能力
**7. 病理结局**: 
   - GSR缺陷: GSH再生障碍 → 氧化应激 → 细胞损伤
   - GSR缺乏: 可能导致溶血性贫血

##### 步骤 ID: DET-13
**1. 反应名称**: 谷胱甘肽过氧化物酶反应 (Glutathione Peroxidase Reaction)
**2. 化学方程式**: 2.0 GSH + 1.0 H2O2 → 1.0 GSSG + 2.0 H2O
**3. 核心酶信息**: 谷胱甘肽过氧化物酶 (Glutathione Peroxidase), EC 1.11.1.9, 肝脏特异性同工酶: GPx1 (胞浆), GPx4 (线粒体), 基因型: GPX1, GPX4
**4. 动力学与调控**: 
   - 速率方程: v = Vmax[H2O2][GSH] / (Km(H2O2)[GSH] + Km(GSH)[H2O2] + [H2O2][GSH])
   - 动力学参数: 
     * Km(H2O2) ~0.1-0.5 mM
     * Km(GSH) ~1-5 mM
     * Vmax ~10-50 μmol/min/mg protein
   - 抑制类型: 无强变构调控
   - 激活剂: 
     * 硒是必需辅因子
     * Nrf2激活可诱导GPx表达
   - 抑制剂: 
     * 汞离子
     * 金离子
     * 叠氮化物
   - 膜定位: 胞浆 (GPx1), 线粒体 (GPx4)
**5. 能量与热力学**: ΔG°' ≈ -30 kJ/mol (不可逆)
**6. 生理意义**: 清除过氧化氢，保护细胞免受氧化损伤
**7. 病理结局**: 
   - GPx缺陷: 过氧化氢堆积 → 氧化应激 → 细胞损伤
   - GPx缺乏: 可能导致心血管疾病和癌症风险增加

## 线粒体穿梭系统 (Mitochondrial Shuttles)

### 苹果酸-天冬氨酸穿梭 (Malate-Aspartate Shuttle)

##### 步骤 ID: SHT-01
**1. 反应名称**: 苹果酸-天冬氨酸穿梭 (Malate-Aspartate Shuttle)
**2. 化学方程式**: 胞浆: 1.0 NADH + 1.0 Oxaloacetate → 1.0 Malate + 1.0 NAD+; 线粒体内: 1.0 Malate + 1.0 NAD+ → 1.0 Oxaloacetate + 1.0 NADH; 跨膜: 1.0 Malate (胞浆) ↔ 1.0 Malate (线粒体); 1.0 Aspartate (线粒体) ↔ 1.0 Glutamate (胞浆)
**3. 核心酶信息**: 胞浆苹果酸脱氢酶 (cMDH), 线粒体苹果酸脱氢酶 (mMDH), 天冬氨酸转氨酶 (AST)
**4. 动力学与调控**: 受线粒体膜两侧质子梯度影响，梯度高时穿梭受阻; 受[NADH]/[NAD+]比值调控
**5. 能量与热力学**: 无直接能量消耗，ΔG°' ≈ 0 kJ/mol (可逆)
**6. 功能说明**: 将胞浆糖酵解产生的NADH转运进线粒体，参与氧化磷酸化产生ATP

### 柠檬酸-丙酮酸循环 (Citrate-Pyruvate Shuttle)

##### 步骤 ID: SHT-02
**1. 反应名称**: 柠檬酸-丙酮酸循环 (Citrate-Pyruvate Shuttle)
**2. 化学方程式**: 线粒体内: 1.0 Acetyl-CoA + 1.0 Oxaloacetate + 1.0 H2O → 1.0 Citrate + 1.0 CoA-SH; 跨膜: 1.0 Citrate (线粒体) ↔ 1.0 Malate (胞浆); 胞浆: 1.0 Citrate + 1.0 ATP + 1.0 CoA-SH → 1.0 Acetyl-CoA + 1.0 Oxaloacetate + 1.0 ADP + 1.0 Pi + 1.0 H+; 1.0 Malate → 1.0 Pyruvate + 1.0 NADPH
**3. 核心酶信息**: 柠檬酸合酶, 柠檬酸载体, ATP-柠檬酸裂解酶 (ACLY), 苹果酸酶
**4. 动力学与调控**: ACLY是限速酶; 激活剂: Insulin; 抑制剂: Glucagon
**5. 能量与热力学**: ATP消耗: -1, NADPH生成: +1, ΔG°' ≈ -8 kJ/mol (不可逆)
**6. 功能说明**: 将线粒体内的Acetyl-CoA转运到胞浆，用于脂肪合成

### 甘油-3-磷酸穿梭 (Glycerol-3-Phosphate Shuttle)

##### 步骤 ID: SHT-03
**1. 反应名称**: 甘油-3-磷酸穿梭 (Glycerol-3-Phosphate Shuttle)
**2. 化学方程式**: 胞浆: 1.0 DHAP + 1.0 NADH + 1.0 H+ → 1.0 Glycerol-3-Phosphate + 1.0 NAD+; 线粒体内: 1.0 Glycerol-3-Phosphate + 1.0 FAD → 1.0 DHAP + 1.0 FADH2
**3. 核心酶信息**: 胞浆甘油-3-磷酸脱氢酶 (cGPDH), 线粒体甘油-3-磷酸脱氢酶 (mGPDH)
**4. 动力学与调控**: 无强变构调控
**5. 能量与热力学**: 无直接能量消耗，ΔG°' ≈ 0 kJ/mol (可逆)
**6. 功能说明**: 将胞浆NADH转运进线粒体，产生FADH2参与氧化磷酸化

### 金属解毒与螯合 (Metal Detoxification and Chelation)

##### 步骤 ID: MET-01
**1. 反应名称**: 金属硫蛋白合成 (Metallothionein Synthesis)
**2. 化学方程式**: 多种氨基酸 → 1.0 Metallothionein + 多个 H2O
**3. 核心酶信息**: 核糖体、多种合成酶，基因型: MT1, MT2
**4. 动力学与调控**: 
   - 速率方程: v = Vmax[Amino Acids] / (Km(Amino Acids) + [Amino Acids])
   - 动力学参数: 
     * Km(氨基酸) ~0.1-1 mM
     * Vmax ~5-20 nmol/min/mg protein
   - 激活剂: 
     * 重金属离子 (Cd2+, Hg2+, Zn2+, Cu2+)
     * 氧化应激
     * 葡萄糖皮质激素
   - 抑制剂: 
     * 蛋白质合成抑制剂
     * 某些药物
   - 转录调控: 金属反应元件 (MRE) 介导的转录激活
   - 膜定位: 胞浆 (Cytosol)
**5. 能量与热力学**: ATP 消耗: -4 per peptide bond
**6. 生理意义**: 金属硫蛋白富含半胱氨酸，能螯合重金属离子，防止其与细胞大分子结合造成损伤
**7. 病理结局**: 
   - 金属硫蛋白过表达: 重金属中毒的保护机制，但可能干扰必需金属离子的稳态
   - 金属硫蛋白缺乏: 重金属敏感性增加，易发生重金属中毒

##### 步骤 ID: MET-02
**1. 反应名称**: 谷胱甘肽-金属螯合 (Glutathione-Metal Chelation)
**2. 化学方程式**: 1.0 Metal2+ + 2.0 GSH → 1.0 Metal-(GS)2 复合物
**3. 核心酶信息**: 非酶促反应，但可被谷胱甘肽S-转移酶 (GST) 催化，基因型: GSTA1, GSTP1
**4. 动力学与调控**: 
   - 速率方程: v = k[Metal2+][GSH]^2 (二级反应)
   - 动力学参数: 
     * k ~10-100 M^-2 s^-1
     * 依赖 GSH 浓度: GSH > 5 mM 时螯合效率高
     * 金属亲和力: Hg2+ > Cd2+ > Pb2+ > Zn2+ > Cu2+
   - 激活剂: 
     * GST 可催化某些金属的螯合反应
   - 抑制剂: 
     * GSH 耗尽
     * 某些药物可抑制GST活性
   - 膜定位: 胞浆 (Cytosol)
**5. 能量与热力学**: ΔG°' ≈ -50 kJ/mol (不可逆)
**6. 生理意义**: GSH 通过巯基与重金属离子形成稳定复合物，促进其外排
**7. 病理结局**: 
   - GSH 耗尽: 重金属离子与蛋白质巯基结合 → 酶失活 → 细胞损伤
   - 重金属中毒: GSH 消耗 → 氧化应激 → 细胞凋亡

##### 步骤 ID: MET-03
**1. 反应名称**: 金属-谷胱甘肽复合物外排 (Metal-Glutathione Complex Efflux)
**2. 化学方程式**: 1.0 Metal-(GS)2 (胞浆) + ATP → 1.0 Metal-(GS)2 (胆汁/血液) + ADP + Pi
**3. 核心酶信息**: MRP 家族 (ABCC), 特别是 MRP1, MRP2, 基因型: ABCC1, ABCC2
**4. 动力学与调控**: 
   - 速率方程: v = Vmax[Metal-(GS)2][ATP] / (Km(Metal-(GS)2)[ATP] + Km(ATP)[Metal-(GS)2] + [Metal-(GS)2][ATP])
   - 动力学参数: 
     * Km(Metal-(GS)2) ~1-10 μM
     * Km(ATP) ~0.1-1 mM
     * Vmax ~10-50 pmol/min/mg protein
   - ATP 消耗: -1 (直接消耗 ATP)
   - 底物: 金属-谷胱甘肽复合物、药物-谷胱甘肽复合物
   - 激活剂: 
     * 某些药物 (如利福平) 可诱导 MRP 表达
     * Nrf2激活可诱导MRP表达
   - 抑制剂: 
     * 某些药物 (如 MK-571) 可抑制 MRP 活性
     * ATP 耗尽
   - 膜定位: 顶膜 (Apical membrane, MRP2) 或基底膜 (Basolateral membrane, MRP1)
**5. 能量与热力学**: ATP 消耗: -1, ΔG°' ≈ -30 kJ/mol (不可逆)
**6. 生理意义**: 将金属-谷胱甘肽复合物泵出到胆汁或血液，完成重金属解毒的最后步骤
**7. 病理结局**: 
   - MRP 缺陷: 金属-谷胱甘肽复合物在胞内堆积 → 重金属中毒
   - MRP 过表达: 可能导致药物外排增加，降低药效
   - Dubin-Johnson综合征: MRP2缺陷 → 结合胆红素外排障碍

##### 步骤 ID: MET-04
**1. 反应名称**: 铜蓝蛋白合成 (Ceruloplasmin Synthesis)
**2. 化学方程式**: 1.0 Apoceruloplasmin + 6.0 Cu2+ → 1.0 Ceruloplasmin
**3. 核心酶信息**: 铜蓝蛋白 (Ceruloplasmin), EC 1.16.3.1, 肝脏特异性: CP, 基因型: CP
**4. 动力学与调控**: 
   - 速率方程: v = Vmax[Apoceruloplasmin][Cu2+] / (Km(Apoceruloplasmin)[Cu2+] + Km(Cu2+)[Apoceruloplasmin] + [Apoceruloplasmin][Cu2+])
   - 动力学参数: 
     * Km(Apoceruloplasmin) ~0.1-1 μM
     * Km(Cu2+) ~1-10 μM
     * Vmax ~1-5 pmol/min/mg protein
   - 激活剂: 
     * 铜离子 (诱导CP表达)
     * 某些炎症因子
   - 抑制剂: 
     * 铜缺乏
     * 某些药物
   - 膜定位: 分泌到血液 (Secreted to blood)
**5. 能量与热力学**: ATP 消耗: -1 (蛋白质合成)
**6. 生理意义**: 铜蓝蛋白是主要的铜转运蛋白，参与铜的代谢和铁的氧化
**7. 病理结局**: 
   - CP缺陷: 铜代谢障碍 → Wilson病 (铜堆积)
   - CP缺乏: 可能导致铁代谢异常

##### 步骤 ID: MET-05
**1. 反应名称**: 铁蛋白合成 (Ferritin Synthesis)
**2. 化学方程式**: 1.0 Apoferritin + 24.0 Fe2+ + 12.0 O2 → 1.0 Ferritin (Fe3+ core)
**3. 核心酶信息**: 铁蛋白 (Ferritin), 肝脏特异性: FTH1 (重链), FTL1 (轻链), 基因型: FTH1, FTL1
**4. 动力学与调控**: 
   - 速率方程: v = Vmax[Apoferritin][Fe2+] / (Km(Apoferritin)[Fe2+] + Km(Fe2+)[Apoferritin] + [Apoferritin][Fe2+])
   - 动力学参数: 
     * Km(Apoferritin) ~0.1-1 μM
     * Km(Fe2+) ~10-100 μM
     * Vmax ~10-50 pmol/min/mg protein
   - 激活剂: 
     * 铁离子 (诱导铁蛋白表达)
     * 氧化应激
   - 抑制剂: 
     * 铁缺乏
     * 某些药物
   - 膜定位: 胞浆 (Cytosol)
**5. 能量与热力学**: ATP 消耗: -1 (蛋白质合成)
**6. 生理意义**: 铁蛋白储存铁离子，防止铁催化的氧化应激
**7. 病理结局**: 
   - 铁蛋白缺陷: 铁离子堆积 → 氧化应激 → 细胞损伤
   - 铁蛋白过表达: 可能导致铁缺乏

### 药物代谢酶诱导与抑制 (Drug Metabolism Enzyme Induction and Inhibition)

##### 步骤 ID: IND-01
**1. 反应名称**: P450 酶诱导 (P450 Enzyme Induction)
**2. 化学方程式**: 1.0 Inducer + PXR/CAR (核受体) → 激活的 PXR/CAR → P450 mRNA → P450 蛋白
**3. 核心酶信息**: 
   - 孕烷 X 受体 (PXR, NR1I2), 核受体
   - 组成型雄烷受体 (CAR, NR1I3), 核受体
   - 细胞色素 P450 酶 (CYP3A4, CYP2B6, CYP2C9 等)
**4. 动力学与调控**: 
   - 速率方程: v = Vmax[Inducer][PXR/CAR] / (Km(Inducer)[PXR/CAR] + Km(PXR/CAR)[Inducer] + [Inducer][PXR/CAR])
   - 动力学参数: 
     * Km(利福平) ~0.1-1 μM
     * Km(苯巴比妥) ~10-100 μM
     * Vmax ~1-10 pmol/min/mg protein (mRNA合成)
   - 触发: 外源性化合物 (如利福平、苯巴比妥) 持续暴露 > 24 小时
   - 激活剂: 
     * 利福平 (PXR 激动剂)
     * 苯巴比妥 (CAR 激动剂)
   - 抑制剂: 
     * 酮康唑 (PXR 拮抗剂)
   - 时间尺度: 基因转录和翻译需要数天
   - 膜定位: 核内 (Nuclear receptors)
**5. 能量与热力学**: 不需要直接能量输入 (ATP 消耗在转录和翻译过程中)
**6. 生理意义**: 长期暴露于外源性化合物时，肝脏适应性增加解毒能力
**7. 病理结局**: 
   - P450 酶诱导: 药物代谢加快 → 药效降低 → 需要增加剂量
   - P450 酶诱导: 活性代谢物生成增加 → 毒性增加
   - 药物相互作用: 诱导剂可降低其他药物的疗效

##### 步骤 ID: IND-02
**1. 反应名称**: P450 酶抑制 (P450 Enzyme Inhibition)
**2. 化学方程式**: 1.0 Inhibitor + P450 (活性) → P450-Inhibitor 复合物 (无活性)
**3. 核心酶信息**: 细胞色素 P450 酶 (CYP3A4, CYP2D6, CYP2C19 等)
**4. 动力学与调控**: 
   - 速率方程 (竞争性抑制): v = Vmax[Substrate] / (Km(1 + [Inhibitor]/Ki) + [Substrate])
   - 速率方程 (非竞争性抑制): v = Vmax[Substrate] / ((Km + [Substrate])(1 + [Inhibitor]/Ki))
   - 动力学参数: 
     * Ki(酮康唑, CYP3A4) ~0.1-1 μM
     * Ki(西咪替丁, CYP3A4) ~10-100 μM
     * Ki(红霉素, CYP3A4, 机制性) ~0.1-1 μM
   - 抑制类型: 
     * 竞争性抑制 (如酮康唑)
     * 非竞争性抑制 (如西咪替丁)
     * 机制性抑制 (如红霉素)
   - 可逆性: 竞争性/非竞争性抑制可逆，机制性抑制不可逆
   - 膜定位: 内质网膜 (Endoplasmic reticulum membrane)
**5. 能量与热力学**: ΔG°' ≈ -30 kJ/mol (不可逆)
**6. 生理意义**: 某些药物可抑制 P450 酶活性，影响其他药物的代谢
**7. 病理结局**: 
   - P450 酶抑制: 药物代谢减慢 → 药物蓄积 → 毒性增加
   - 药物相互作用: 抑制剂可增加其他药物的毒性和不良反应
   - 机制性抑制: P450 酶失活 → 需要数天才能恢复

### 氧化应激信号通路 (Oxidative Stress Signaling Pathways)

##### 步骤 ID: OXS-01
**1. 反应名称**: Nrf2 激活 (Nrf2 Activation)
**2. 化学方程式**: 
   - 基础状态: Nrf2 + Keap1 → Nrf2-Keap1 复合物 → Nrf2 泛素化 → Nrf2 降解
   - 氧化应激: ROS + Keap1 (氧化) → Keap1 构象改变 → Nrf2 释放 → Nrf2 核转位
   - 转录激活: Nrf2 + ARE (抗氧化反应元件) → 抗氧化酶 mRNA → 抗氧化酶蛋白
**3. 核心酶信息**: 
   - 核因子 E2 相关因子 2 (Nrf2, NFE2L2), 转录因子
   - Kelch 样 ECH 相关蛋白 1 (Keap1), Nrf2 负调控因子
   - 泛素-蛋白酶体系统 (Ubiquitin-Proteasome System)
**4. 动力学与调控**: 
   - 速率方程 (基础状态): v = Vmax[Nrf2][Keap1] / (Km(Nrf2)[Keap1] + Km(Keap1)[Nrf2] + [Nrf2][Keap1])
   - 速率方程 (氧化应激): v = Vmax[ROS][Keap1] / (Km(ROS)[Keap1] + Km(Keap1)[ROS] + [ROS][Keap1])
   - 动力学参数: 
     * Km(ROS) ~0.5-2 μM
     * Km(Nrf2) ~0.1-0.5 μM
     * Vmax ~1-10 pmol/min/mg protein (mRNA合成)
   - 触发: ROS > 1 μM 或亲电子化合物 > 10 μM
   - 激活剂: 
     * 叔丁基对苯二酚 (tBHQ)
     * 莱菔硫烷 (Sulforaphane)
   - 抑制剂: 
     * Keap1 过表达
   - 时间尺度: 基因转录需要数小时
   - 膜定位: 胞浆 (Cytosol, Keap1) 和核内 (Nrf2)
**5. 能量与热力学**: 不需要直接能量输入 (ATP 消耗在转录和翻译过程中)
**6. 功能说明**: 
   - 上调 SOD (超氧化物歧化酶): 增加 Vmax，促进 O2- 歧化
   - 上调 Catalase (过氧化氢酶): 增加 Vmax，促进 H2O2 分解
   - 上调 GPx (谷胱甘肽过氧化物酶): 增加 Vmax，促进 H2O2 还原
   - 上调 GSR (谷胱甘肽还原酶): 增加 Vmax，促进 GSH 再生
   - 上调 HO-1 (血红素加氧酶-1): 增加 Vmax，促进血红素降解和抗氧化
   - 上调 NQO1 (NAD(P)H 醌氧化还原酶 1): 增加 Vmax，促进醌类化合物还原
**7. 生理意义**: 氧化应激时的适应性反应，增强细胞的抗氧化能力
**8. 病理结局**: 
   - Nrf2 缺陷: 氧化应激敏感性增加 → 易发生氧化损伤相关疾病
   - Nrf2 过度激活: 可能促进肿瘤细胞存活，降低化疗效果

##### 步骤 ID: OXS-02
**1. 反应名称**: NF-κB 激活 (NF-κB Activation)
**2. 化学方程式**: 
   - 基础状态: NF-κB + IκB → NF-κB-IκB 复合物 (无活性)
   - 氧化应激: ROS + IKK (IκB 激酶) → IKK 激活 → IκB 磷酸化 → IκB 泛素化 → IκB 降解
   - 转录激活: NF-κB 核转位 + κB 位点 → 炎症因子 mRNA → 炎症因子蛋白
**3. 核心酶信息**: 
   - 核因子 κB (NF-κB), 转录因子
   - IκB (NF-κB 抑制因子), 负调控因子
   - IKK (IκB 激酶), 激酶复合体
   - 泛素-蛋白酶体系统 (Ubiquitin-Proteasome System)
**4. 动力学与调控**: 
   - 速率方程 (IKK激活): v = Vmax[ROS][IKK] / (Km(ROS)[IKK] + Km(IKK)[ROS] + [ROS][IKK])
   - 速率方程 (IκB磷酸化): v = Vmax[IκB][IKK] / (Km(IκB)[IKK] + Km(IKK)[IκB] + [IκB][IKK])
   - 动力学参数: 
     * Km(ROS) ~0.5-2 μM
     * Km(IκB) ~0.1-0.5 μM
     * Vmax ~1-10 pmol/min/mg protein (mRNA合成)
   - 触发: ROS > 1 μM 或 TNF-α > 0.1 nM
   - 激活剂: 
     * TNF-α
     * IL-1β
     * LPS
   - 抑制剂: 
     * 抗氧化剂 (如 NAC)
     * IKK 抑制剂 (如 BMS-345541)
   - 时间尺度: 基因转录需要数小时
   - 膜定位: 胞浆 (Cytosol, NF-κB-IκB) 和核内 (NF-κB)
**5. 能量与热力学**: 不需要直接能量输入 (ATP 消耗在转录和翻译过程中)
**6. 功能说明**: 
   - 上调 TNF-α: 增加 Vmax，促进炎症反应
   - 上调 IL-6: 增加 Vmax，促进炎症反应
   - 上调 IL-1β: 增加 Vmax，促进炎症反应
   - 上调 COX-2 (环氧化酶-2): 增加 Vmax，促进前列腺素合成
   - 上调 iNOS (诱导型一氧化氮合酶): 增加 Vmax，促进 NO 生成
**7. 生理意义**: 氧化应激和炎症反应的关键信号通路，协调炎症和免疫反应
**8. 病理结局**: 
   - NF-κB 过度激活: 慢性炎症 → 肝纤维化 → 肝硬化
   - NF-κB 抑制: 免疫功能下降 → 易感染

### 线粒体质量控制 (Mitochondrial Quality Control)

##### 步骤 ID: MIT-01
**1. 反应名称**: 线粒体自噬 (Mitophagy)
**2. 化学方程式**: 
   - 触发: 线粒体膜电位 (ΔΨm) 下降 + ROS 升高
   - 标记: PINK1 在受损线粒体上积累 → Parkin 招募 → Parkin 泛素化线粒体外膜蛋白
   - 吞噬: 自噬体形成 + 标记的线粒体 → 自噬体-线粒体复合物 → 溶酶体融合 → 线粒体降解
**3. 核心酶信息**: 
   - PTEN 诱导激酶 1 (PINK1), 丝氨酸/苏氨酸激酶
   - Parkin (PARK2), E3 泛素连接酶
   - 自噬相关蛋白 (ATG5, ATG7, LC3 等)
   - 溶酶体酶 (Lysosomal enzymes)
**4. 动力学与调控**: 
   - 触发条件: ΔΨm < 100 mV 或 ROS > 5 μM
   - 激活剂: 线粒体解偶联剂 (如 FCCC), ROS 诱导剂
   - 抑制剂: Mdivi-1 (线粒体分裂抑制剂), 3-MA (自噬抑制剂)
   - 时间尺度: 线粒体标记需要数小时，吞噬和降解需要数小时到数天
   - 膜定位: 线粒体外膜 (PINK1, Parkin), 胞浆 (自噬体), 溶酶体 (降解)
**5. 能量与热力学**: ATP 消耗: -2 (用于自噬体形成和溶酶体融合)
**6. 生理意义**: 清除受损线粒体，维持线粒体质量，防止 ROS 生成和细胞凋亡
**7. 病理结局**: 
   - 线粒体自噬缺陷: 受损线粒体堆积 → ROS 升高 → 氧化应激 → 细胞凋亡
   - 线粒体自噬过度: 正常线粒体被清除 → 能量产生下降 → 细胞功能障碍
   - 帕金森病: PINK1/Parkin 突变 → 线粒体自噬缺陷 → 神经元死亡

##### 步骤 ID: MIT-02
**1. 反应名称**: 线粒体生物合成 (Mitochondrial Biogenesis)
**2. 化学方程式**: 
   - 触发: 能量需求增加 + PGC-1α 激活
   - 转录激活: PGC-1α + NRF-1/NRF-2 + TFAM → mtDNA 复制 + 线粒体蛋白合成
   - 组装: 线粒体蛋白 + 线粒体膜脂质 → 新线粒体
**3. 核心酶信息**: 
   - 过氧化物酶体增殖物激活受体 γ 共激活因子 1α (PGC-1α), 转录共激活因子
   - 核呼吸因子 1/2 (NRF-1/NRF-2), 转录因子
   - 线粒体转录因子 A (TFAM), mtDNA 转录因子
   - 线粒体 DNA 聚合酶 γ (POLG), mtDNA 复制酶
**4. 动力学与调控**: 
   - 触发: 能量需求增加 (如运动、寒冷) 或 AMPK 激活
   - 激活剂: AMPK, SIRT1, CaMK
   - 抑制剂: 高血糖, 高脂饮食
   - 时间尺度: 基因转录和翻译需要数天，新线粒体形成需要数天到数周
   - 膜定位: 核内 (PGC-1α, NRF-1/2), 线粒体 (TFAM, POLG)
**5. 能量与热力学**: ATP 消耗: -10 (用于 mtDNA 复制、蛋白质合成和膜脂质合成)
**6. 生理意义**: 增加线粒体数量和功能，提高能量产生能力，适应能量需求增加
**7. 病理结局**: 
   - 线粒体生物合成缺陷: 线粒体数量减少 → 能量产生下降 → 代谢性疾病
   - 线粒体生物合成过度: 可能增加 ROS 生成 → 氧化应激

### 蛋白质质量控制 (Protein Quality Control)

##### 步骤 ID: PQC-01
**1. 反应名称**: 未折叠蛋白反应 (Unfolded Protein Response, UPR)
**2. 化学方程式**: 
   - 触发: 内质网 (ER) 内未折叠蛋白积累
   - 传感器激活: IRE1α, PERK, ATF6 激活
   - 转录激活: XBP1, ATF4, ATF6(N) → 分子伴侣 mRNA → 分子伴侣蛋白
   - 结果: 分子伴侣 (如 BiP, GRP94) 表达增加 → 蛋白质折叠能力增强
**3. 核心酶信息**: 
   - 肌醇需求酶 1α (IRE1α), 内质网应激传感器
   - PKR 样内质网激酶 (PERK), 内质网应激传感器
   - 活化转录因子 6 (ATF6), 内质网应激传感器
   - X 盒结合蛋白 1 (XBP1), 转录因子
   - 活化转录因子 4 (ATF4), 转录因子
**4. 动力学与调控**: 
   - 触发条件: 未折叠蛋白 > 正常水平的 2 倍
   - 激活剂: 衣霉素 (Tunicamycin), 毒胡萝卜素 (Thapsigargin)
   - 抑制剂: 4μ8C (IRE1α 抑制剂), GSK2606414 (PERK 抑制剂)
   - 时间尺度: 传感器激活需要数分钟，基因转录需要数小时
   - 膜定位: 内质网膜 (IRE1α, PERK, ATF6), 核内 (XBP1, ATF4, ATF6)
**5. 能量与热力学**: 不需要直接能量输入 (ATP 消耗在转录和翻译过程中)
**6. 功能说明**: 
   - 上调 BiP (免疫球蛋白重链结合蛋白): 增加 Vmax，促进蛋白质折叠
   - 上调 GRP94 (葡萄糖调节蛋白 94): 增加 Vmax，促进蛋白质折叠
   - 上调 CHOP (C/EBP 同源蛋白): 增加 Vmax，促进细胞凋亡 (应激持续时)
   - 上调 ERO1 (内质网氧化还原酶 1): 增加 Vmax，促进蛋白质二硫键形成
**7. 生理意义**: 内质网应激时的适应性反应，增强蛋白质折叠能力，维持蛋白质稳态
**8. 病理结局**: 
   - UPR 缺陷: 未折叠蛋白积累 → 内质网应激 → 细胞凋亡
   - UPR 过度激活: CHOP 介导的细胞凋亡 → 肝损伤
   - 脂肪肝: 内质网应激 → UPR 激活 → 脂质合成增加

##### 步骤 ID: PQC-02
**1. 反应名称**: 泛素-蛋白酶体系统 (Ubiquitin-Proteasome System, UPS)
**2. 化学方程式**: 
   - 泛素化: 1.0 Misfolded Protein + n Ubiquitin + ATP → 1.0 Ubiquitinated Protein + n ADP + n Pi
   - 降解: 1.0 Ubiquitinated Protein → 1.0 Degraded Protein + n Ubiquitin
**3. 核心酶信息**: 
   - E1 泛素激活酶 (Ubiquitin-activating enzyme), EC 6.2.1.45
   - E2 泛素结合酶 (Ubiquitin-conjugating enzyme), EC 2.3.2.23
   - E3 泛素连接酶 (Ubiquitin ligase), 多种
   - 26S 蛋白酶体 (26S Proteasome), 蛋白质降解复合体
**4. 动力学与调控**: 
   - E1 Km(Ubiquitin) ~0.01-0.05 mM
   - ATP 消耗: -1 per ubiquitin (泛素化步骤)
   - 激活剂: 氧化应激, 热休克
   - 抑制剂: MG-132 (蛋白酶体抑制剂), 乳胞素 (Lactacystin)
   - 膜定位: 胞浆 (Cytosol)
**5. 能量与热力学**: ATP 消耗: -4 per protein (泛素化), ΔG°' ≈ -50 kJ/mol (不可逆)
**6. 生理意义**: 降解错误折叠或损伤的蛋白质，维持蛋白质稳态
**7. 病理结局**: 
   - UPS 缺陷: 错误折叠蛋白积累 → 蛋白质聚集 → 细胞功能障碍
   - UPS 过度激活: 正常蛋白质被降解 → 细胞功能下降
   - 神经退行性疾病: UPS 功能障碍 → 蛋白质聚集 → 神经元死亡

### 氨基酸代谢 (Amino Acid Metabolism)

#### 支链氨基酸代谢 (Branched-Chain Amino Acid Metabolism)

##### 步骤 ID: AAM-01
**1. 反应名称**: 支链氨基酸转氨酶 (BCAT)
**2. 化学方程式**: 1.0 Leucine + 1.0 α-Ketoglutarate → 1.0 α-Ketoisocaproate + 1.0 Glutamate
**3. 核心酶信息**: BCAT (Branched-Chain Amino Acid Transaminase), EC 2.6.1.42, 肝脏特异性: BCAT2 (线粒体), 基因型: BCAT2
**4. 动力学与调控**: 
   - 反应机制: Ping-Pong Bi-Bi 机制，类似其他转氨酶
   - 速率方程: v = Vmax[Leucine][α-Ketoglutarate] / (Km(Leucine)[α-Ketoglutarate] + Km(α-Ketoglutarate)[Leucine] + [Leucine][α-Ketoglutarate])
   - 动力学参数: 
     * Km(Leucine) ~0.1-0.5 mM
     * Km(Isoleucine) ~0.1-0.5 mM
     * Km(Valine) ~0.5-1.0 mM
     * Km(α-Ketoglutarate) ~0.1-0.5 mM
     * Vmax ~20-50 μmol/min/mg protein
   - 抑制类型: 无强变构调控
   - 激活剂: 无强变构激活剂
   - 抑制剂: 无强抑制剂
   - 膜定位: 线粒体基质 (Mitochondrial matrix)
**5. 能量与热力学**: ΔG°' ≈ 0 kJ/mol (可逆)
**6. 生理意义**: 支链氨基酸代谢的第一步，将支链氨基酸转氨为相应的α-酮酸
**7. 病理结局**: 
   - BCAT2 缺陷: 支链氨基酸代谢障碍，可能导致枫糖尿病

##### 步骤 ID: AAM-02
**1. 反应名称**: 支链α-酮酸脱氢酶复合体 (BCKDH)
**2. 化学方程式**: 1.0 α-Ketoisocaproate + 1.0 CoA-SH + 1.0 NAD+ → 1.0 Isovaleryl-CoA + 1.0 NADH + 1.0 CO2 + 1.0 H+
**3. 核心酶信息**: BCKDH 复合体 (E1: BCKDHA/BCKDHB, E2: DBT, E3: DLD), 基因型: BCKDHA, BCKDHB, DBT, DLD
**4. 动力学与调控**: 
   - 反应机制: 多酶复合体顺序反应机制，类似丙酮酸脱氢酶复合体
   - 速率方程: v = Vmax[α-Ketoisocaproate][CoA-SH][NAD+] / (K1[CoA-SH][NAD+] + K2[α-Ketoisocaproate][NAD+] + K3[α-Ketoisocaproate][CoA-SH] + [α-Ketoisocaproate][CoA-SH][NAD+] + Ki(Isovaleryl-CoA)[Isovaleryl-CoA] + Ki(NADH)[NADH])
   - 动力学参数: 
     * Km(α-Ketoisocaproate) ~0.05-0.1 mM
     * Km(CoA-SH) ~0.01-0.05 mM
     * Km(NAD+) ~0.05-0.1 mM
     * Vmax ~10-20 μmol/min/mg protein
   - 抑制类型: 
     * Isovaleryl-CoA: 竞争性抑制剂 (与CoA-SH竞争结合位点)，Ki ~0.01-0.05 mM
     * NADH: 竞争性抑制剂 (与NAD+竞争结合位点)，Ki ~0.01-0.05 mM
   - 激活剂: 
     * 胰岛素 (通过去磷酸化激活)
     * Ca2+ (别构激活剂)
   - 抑制剂: 
     * 胰高血糖素 (通过磷酸化抑制)
     * 产物抑制
   - 膜定位: 线粒体基质 (Mitochondrial matrix)
**5. 能量与热力学**: NADH生成: +1, CO2生成: +1, ΔG°' ≈ -30 kJ/mol (不可逆)
**6. 生理意义**: 支链氨基酸代谢的关键步骤，将支链α-酮酸氧化脱羧为相应的酰基辅酶A
**7. 病理结局**: 
   - BCKDH 缺陷: 枫糖尿病 (MSUD)，支链α-酮酸堆积

#### 芳香族氨基酸代谢 (Aromatic Amino Acid Metabolism)

##### 步骤 ID: AAM-03
**1. 反应名称**: 苯丙氨酸羟化酶 (PAH)
**2. 化学方程式**: 1.0 Phenylalanine + 1.0 O2 + 1.0 Tetrahydrobiopterin → 1.0 Tyrosine + 1.0 Dihydrobiopterin + 1.0 H2O
**3. 核心酶信息**: PAH (Phenylalanine Hydroxylase), EC 1.14.16.1, 肝脏特异性，基因型: PAH
**4. 动力学与调控**: 
   - 反应机制: 混合功能氧化反应，需要四氢生物蝶呤作为辅酶
   - 速率方程: v = Vmax[Phenylalanine][Tetrahydrobiopterin][O2] / (K1[Tetrahydrobiopterin][O2] + K2[Phenylalanine][O2] + K3[Phenylalanine][Tetrahydrobiopterin] + [Phenylalanine][Tetrahydrobiopterin][O2])
   - 动力学参数: 
     * Km(Phenylalanine) ~0.1-0.5 mM
     * Km(Tetrahydrobiopterin) ~0.01-0.05 mM
     * Vmax ~5-10 μmol/min/mg protein
   - 抑制类型: 无强变构调控
   - 激活剂: 
     * 苯丙氨酸 (别构激活剂)
     * 胰岛素 (转录水平上调)
   - 抑制剂: 
     * 胰高血糖素 (转录水平下调)
   - 膜定位: 胞浆 (Cytosol)
**5. 能量与热力学**: ΔG°' ≈ -15 kJ/mol (不可逆)
**6. 生理意义**: 苯丙氨酸代谢的关键步骤，将苯丙氨酸羟化为酪氨酸
**7. 病理结局**: 
   - PAH 缺陷: 苯丙酮尿症 (PKU)，苯丙氨酸堆积

##### 步骤 ID: AAM-04
**1. 反应名称**: 酪氨酸转氨酶 (TAT)
**2. 化学方程式**: 1.0 Tyrosine + 1.0 α-Ketoglutarate → 1.0 p-Hydroxyphenylpyruvate + 1.0 Glutamate
**3. 核心酶信息**: TAT (Tyrosine Aminotransferase), EC 2.6.1.5, 肝脏特异性，基因型: TAT
**4. 动力学与调控**: 
   - 反应机制: Ping-Pong Bi-Bi 机制，类似其他转氨酶
   - 速率方程: v = Vmax[Tyrosine][α-Ketoglutarate] / (Km(Tyrosine)[α-Ketoglutarate] + Km(α-Ketoglutarate)[Tyrosine] + [Tyrosine][α-Ketoglutarate])
   - 动力学参数: 
     * Km(Tyrosine) ~0.1-0.5 mM
     * Km(α-Ketoglutarate) ~0.1-0.5 mM
     * Vmax ~10-20 μmol/min/mg protein
   - 抑制类型: 无强变构调控
   - 激活剂: 
     * 糖皮质激素 (转录水平上调)
     * 胰高血糖素 (转录水平上调)
   - 抑制剂: 
     * 胰岛素 (转录水平下调)
   - 膜定位: 胞浆 (Cytosol)
**5. 能量与热力学**: ΔG°' ≈ 0 kJ/mol (可逆)
**6. 生理意义**: 酪氨酸代谢的第一步，将酪氨酸转氨为p-羟基苯丙酮酸
**7. 病理结局**: 
   - TAT 缺陷: 酪氨酸代谢障碍，可能导致酪氨酸血症

##### 步骤 ID: AAM-05
**1. 反应名称**: p-羟基苯丙酮酸双加氧酶 (HPPD)
**2. 化学方程式**: 1.0 p-Hydroxyphenylpyruvate + 1.0 O2 → 1.0 Homogentisate + 1.0 CO2
**3. 核心酶信息**: HPPD (p-Hydroxyphenylpyruvate Dioxygenase), EC 1.13.11.27, 肝脏特异性，基因型: HPPD
**4. 动力学与调控**: 
   - 反应机制: 双加氧反应，将p-羟基苯丙酮酸氧化为尿黑酸
   - 速率方程: v = Vmax[p-Hydroxyphenylpyruvate][O2] / (Km(p-Hydroxyphenylpyruvate)[O2] + Km(O2)[p-Hydroxyphenylpyruvate] + [p-Hydroxyphenylpyruvate][O2])
   - 动力学参数: 
     * Km(p-Hydroxyphenylpyruvate) ~0.05-0.1 mM
     * Km(O2) ~0.1-0.5 mM
     * Vmax ~10-20 μmol/min/mg protein
   - 抑制类型: 无强变构调控
   - 激活剂: 无强变构激活剂
   - 抑制剂: 
     * 硝磺草酮 (除草剂，特异性抑制剂)
   - 膜定位: 胞浆 (Cytosol)
**5. 能量与热力学**: CO2生成: +1, ΔG°' ≈ -20 kJ/mol (不可逆)
**6. 生理意义**: 酪氨酸代谢的关键步骤，将p-羟基苯丙酮酸氧化为尿黑酸
**7. 病理结局**: 
   - HPPD 缺陷: 酪氨酸血症 I 型，p-羟基苯丙酮酸堆积

#### 含硫氨基酸代谢 (Sulfur-Containing Amino Acid Metabolism)

##### 步骤 ID: AAM-06
**1. 反应名称**: 甲硫氨酸腺苷转移酶 (MAT)
**2. 化学方程式**: 1.0 Methionine + 1.0 ATP → 1.0 S-Adenosylmethionine (SAM) + 1.0 PPi + 1.0 Pi
**3. 核心酶信息**: MAT (Methionine Adenosyltransferase), EC 2.5.1.6, 肝脏特异性: MAT1A，基因型: MAT1A
**4. 动力学与调控**: 
   - 反应机制: 多步反应，将甲硫氨酸与ATP缩合生成S-腺苷甲硫氨酸
   - 速率方程: v = Vmax[Methionine][ATP] / (Km(Methionine)[ATP] + Km(ATP)[Methionine] + [Methionine][ATP])
   - 动力学参数: 
     * Km(Methionine) ~0.1-0.5 mM
     * Km(ATP) ~0.1-0.5 mM
     * Vmax ~20-50 μmol/min/mg protein
   - 抑制类型: 
     * SAM: 反馈抑制剂 (非竞争性)，Ki ~0.01-0.05 mM
   - 激活剂: 无强变构激活剂
   - 抑制剂: 
     * SAM (产物反馈抑制)
   - 膜定位: 胞浆 (Cytosol)
**5. 能量与热力学**: ATP消耗: -1, ΔG°' ≈ -30 kJ/mol (不可逆)
**6. 生理意义**: 甲硫氨酸代谢的关键步骤，生成S-腺苷甲硫氨酸作为甲基供体
**7. 病理结局**: 
   - MAT1A 缺陷: 遗传性高甲硫氨酸血症，甲硫氨酸堆积

##### 步骤 ID: AAM-07
**1. 反应名称**: 胱硫醚β-合成酶 (CBS)
**2. 化学方程式**: 1.0 Homocysteine + 1.0 Serine → 1.0 Cystathionine + 1.0 H2O
**3. 核心酶信息**: CBS (Cystathionine β-Synthase), EC 4.2.1.22, 肝脏特异性，基因型: CBS
**4. 动力学与调控**: 
   - 反应机制: β-替换反应，将同型半胱氨酸与丝氨酸缩合生成胱硫醚
   - 速率方程: v = Vmax[Homocysteine][Serine] / (Km(Homocysteine)[Serine] + Km(Serine)[Homocysteine] + [Homocysteine][Serine] + Kact[S-Adenosylmethionine])
   - 动力学参数: 
     * Km(Homocysteine) ~0.1-0.5 mM
     * Km(Serine) ~1.0-5.0 mM
     * Vmax ~10-20 μmol/min/mg protein
   - 抑制类型: 无强变构调控
   - 激活剂: 
     * S-Adenosylmethionine (别构激活剂)
     * Pyridoxal 5'-phosphate (PLP，必需辅因子)
   - 抑制剂: 无强抑制剂
   - 膜定位: 胞浆 (Cytosol)
**5. 能量与热力学**: ΔG°' ≈ +10 kJ/mol (可逆)
**6. 生理意义**: 同型半胱氨酸代谢的关键步骤，将同型半胱氨酸转化为胱硫醚
**7. 病理结局**: 
   - CBS 缺陷: 高同型半胱氨酸血症，可能导致心血管疾病

### 脂类代谢 (Lipid Metabolism)

#### 脂肪酸合成 (Fatty Acid Synthesis)

##### 步骤 ID: LIP-01
**1. 反应名称**: 乙酰-CoA羧化酶 (ACC)
**2. 化学方程式**: 1.0 Acetyl-CoA + 1.0 HCO3- + 1.0 ATP → 1.0 Malonyl-CoA + 1.0 ADP + 1.0 Pi + 1.0 H+
**3. 核心酶信息**: ACC (Acetyl-CoA Carboxylase), EC 6.4.1.2, 肝脏特异性: ACC1，基因型: ACACA
**4. 动力学与调控**: 
   - 反应机制: 生物素依赖性羧化反应，分两步进行
   - 速率方程: v = Vmax[Acetyl-CoA][HCO3-][ATP] / (Km(Acetyl-CoA)[HCO3-][ATP] + Km(HCO3-)[Acetyl-CoA][ATP] + Km(ATP)[Acetyl-CoA][HCO3-] + [Acetyl-CoA][HCO3-][ATP] + Ki(Palmitoyl-CoA)[Palmitoyl-CoA])
   - 动力学参数: 
     * Km(Acetyl-CoA) ~0.1-0.5 mM
     * Km(HCO3-) ~1.0-5.0 mM
     * Km(ATP) ~0.1-0.5 mM
     * Vmax ~10-20 μmol/min/mg protein
   - 抑制类型: 
     * Palmitoyl-CoA: 别构抑制剂，Ki ~0.01-0.05 mM
   - 激活剂: 
     * Citrate (别构激活剂)
     * 胰岛素 (通过去磷酸化激活)
   - 抑制剂: 
     * Palmitoyl-CoA (产物反馈抑制)
     * 胰高血糖素 (通过磷酸化抑制)
     * AMPK (通过磷酸化抑制)
   - 膜定位: 胞浆 (Cytosol)
**5. 能量与热力学**: ATP消耗: -1, ΔG°' ≈ -5.7 kJ/mol (不可逆)
**6. 生理意义**: 脂肪酸合成的限速步骤，将乙酰-CoA羧化为丙二酰-CoA
**7. 病理结局**: 
   - ACC1 缺陷: 脂肪酸合成障碍，可能导致脂质营养不良

##### 步骤 ID: LIP-02
**1. 反应名称**: 脂肪酸合酶 (FASN)
**2. 化学方程式**: 8.0 Malonyl-CoA + 14.0 NADPH + 14.0 H+ + 1.0 Acetyl-CoA → 1.0 Palmitate + 8.0 CoA-SH + 14.0 NADP+ + 7.0 H2O
**3. 核心酶信息**: FASN (Fatty Acid Synthase), EC 2.3.1.85, 肝脏特异性，基因型: FASN
**4. 动力学与调控**: 
   - 反应机制: 多酶复合体反应，通过酰基载体蛋白 (ACP) 传递酰基
   - 速率方程: v = Vmax[Malonyl-CoA][Acetyl-CoA][NADPH] / (K1[Acetyl-CoA][NADPH] + K2[Malonyl-CoA][NADPH] + K3[Malonyl-CoA][Acetyl-CoA] + [Malonyl-CoA][Acetyl-CoA][NADPH])
   - 动力学参数: 
     * Km(Malonyl-CoA) ~0.05-0.1 mM
     * Km(Acetyl-CoA) ~0.05-0.1 mM
     * Km(NADPH) ~0.1-0.5 mM
     * Vmax ~5-10 μmol/min/mg protein
   - 抑制类型: 无强变构调控
   - 激活剂: 
     * 胰岛素 (转录水平上调)
   - 抑制剂: 
     * 胰高血糖素 (转录水平下调)
     * 脂肪酸合成抑制剂 (如 C75)
   - 膜定位: 胞浆 (Cytosol)
**5. 能量与热力学**: NADPH消耗: -14, ΔG°' ≈ -100 kJ/mol (不可逆)
**6. 生理意义**: 脂肪酸合成的关键酶，将丙二酰-CoA和乙酰-CoA合成为棕榈酸
**7. 病理结局**: 
   - FASN 缺陷: 脂肪酸合成障碍，可能导致脂质营养不良

#### 脂肪酸氧化 (Fatty Acid Oxidation)

##### 步骤 ID: LIP-03
**1. 反应名称**: 肉碱棕榈酰转移酶 I (CPT1)
**2. 化学方程式**: 1.0 Palmitoyl-CoA + 1.0 Carnitine → 1.0 Palmitoyl-Carnitine + 1.0 CoA-SH
**3. 核心酶信息**: CPT1 (Carnitine Palmitoyltransferase I), EC 2.3.1.21, 肝脏特异性: CPT1A，基因型: CPT1A
**4. 动力学与调控**: 
   - 反应机制: 酰基转移反应，将脂肪酸从CoA转移到肉碱
   - 速率方程: v = Vmax[Palmitoyl-CoA][Carnitine] / (Km(Palmitoyl-CoA)[Carnitine] + Km(Carnitine)[Palmitoyl-CoA] + [Palmitoyl-CoA][Carnitine] + Ki(Malonyl-CoA)[Malonyl-CoA])
   - 动力学参数: 
     * Km(Palmitoyl-CoA) ~0.01-0.05 mM
     * Km(Carnitine) ~0.1-0.5 mM
     * Vmax ~20-50 μmol/min/mg protein
   - 抑制类型: 
     * Malonyl-CoA: 竞争性抑制剂 (与棕榈酰-CoA竞争结合位点)，Ki ~0.01-0.05 mM
   - 激活剂: 
     * 胰高血糖素 (通过降低Malonyl-CoA水平激活)
     * AMPK (通过磷酸化ACC降低Malonyl-CoA水平)
   - 抑制剂: 
     * Malonyl-CoA (脂肪酸合成的产物，抑制脂肪酸氧化)
     * 丙二酰-CoA类似物 (如 Etomoxir)
   - 膜定位: 线粒体外膜 (Outer mitochondrial membrane)
**5. 能量与热力学**: ΔG°' ≈ 0 kJ/mol (可逆)
**6. 生理意义**: 长链脂肪酸氧化的限速步骤，将长链脂肪酸转运进入线粒体
**7. 病理结局**: 
   - CPT1A 缺陷: 长链脂肪酸氧化障碍，可能导致低血糖和肝损伤

##### 步骤 ID: LIP-04
**1. 反应名称**: 肉碱棕榈酰转移酶 II (CPT2)
**2. 化学方程式**: 1.0 Palmitoyl-Carnitine + 1.0 CoA-SH → 1.0 Palmitoyl-CoA + 1.0 Carnitine
**3. 核心酶信息**: CPT2 (Carnitine Palmitoyltransferase II), EC 2.3.1.21, 基因型: CPT2
**4. 动力学与调控**: 
   - 反应机制: 酰基转移反应，将脂肪酸从肉碱转移回CoA
   - 速率方程: v = Vmax[Palmitoyl-Carnitine][CoA-SH] / (Km(Palmitoyl-Carnitine)[CoA-SH] + Km(CoA-SH)[Palmitoyl-Carnitine] + [Palmitoyl-Carnitine][CoA-SH])
   - 动力学参数: 
     * Km(Palmitoyl-Carnitine) ~0.01-0.05 mM
     * Km(CoA-SH) ~0.01-0.05 mM
     * Vmax ~50-100 μmol/min/mg protein
   - 抑制类型: 无强变构调控
   - 激活剂: 无强变构激活剂
   - 抑制剂: 无强抑制剂
   - 膜定位: 线粒体内膜 (Inner mitochondrial membrane)
**5. 能量与热力学**: ΔG°' ≈ 0 kJ/mol (可逆)
**6. 生理意义**: 长链脂肪酸氧化的关键步骤，将长链脂肪酸从肉碱转移回CoA
**7. 病理结局**: 
   - CPT2 缺陷: 长链脂肪酸氧化障碍，可能导致横纹肌溶解和肝损伤

##### 步骤 ID: LIP-05
**1. 反应名称**: 酰基辅酶A脱氢酶 (ACAD)
**2. 化学方程式**: 1.0 Palmitoyl-CoA + 1.0 FAD → 1.0 trans-Δ2-Enoyl-CoA + 1.0 FADH2
**3. 核心酶信息**: ACAD (Acyl-CoA Dehydrogenase), EC 1.3.8.7, 肝脏特异性: VLCAD (ACADVL)，基因型: ACADVL
**4. 动力学与调控**: 
   - 反应机制: 氧化反应，将脂肪酸的α,β-碳脱氢
   - 速率方程: v = Vmax[Palmitoyl-CoA][FAD] / (Km(Palmitoyl-CoA)[FAD] + Km(FAD)[Palmitoyl-CoA] + [Palmitoyl-CoA][FAD])
   - 动力学参数: 
     * Km(Palmitoyl-CoA) ~0.01-0.05 mM
     * Km(FAD) ~0.01-0.05 mM
     * Vmax ~50-100 μmol/min/mg protein
   - 抑制类型: 无强变构调控
   - 激活剂: 无强变构激活剂
   - 抑制剂: 无强抑制剂
   - 膜定位: 线粒体基质 (Mitochondrial matrix)
**5. 能量与热力学**: FADH2生成: +1, ΔG°' ≈ 0 kJ/mol (可逆)
**6. 生理意义**: β-氧化的第一步，将脂肪酸脱氢为相应的烯酰-CoA
**7. 病理结局**: 
   - ACADVL 缺陷: 长链脂肪酸氧化障碍，可能导致低血糖和肝损伤

## 模块 C：氮代谢与尿素循环（排毒中心）

### 氨的转运 (Ammonia Transport)

##### 步骤 ID: NIT-01
**1. 反应名称**: 丙氨酸-葡萄糖循环 (Alanine-Glucose Cycle)
**2. 化学方程式**: 1.0 Pyruvate + 1.0 NH4+ + 1.0 NADH + 1.0 H+ → 1.0 Alanine + 1.0 NAD+ + 1.0 H2O
**3. 核心酶信息**: 丙氨酸转氨酶 (Alanine Aminotransferase, ALT), EC 2.6.1.2, 基因型: GPT (肝细胞浆), GPT2 (肌肉)
**4. 动力学与调控**: 
   - 反应机制: Ping-Pong Bi-Bi 机制
   - 反应序列: 1) 酶 (E) 首先结合丙酮酸 → 形成酶-底物复合物 2) 释放丙氨酸，酶转化为 E-NH2 中间态 3) E-NH2 结合 α-酮戊二酸 → 形成第二复合物 4) 释放谷氨酸，酶 (E) 再生
   - 速率方程: v = Vmax[Pyruvate][NH4+] / (Km(Pyruvate)[NH4+] + Km(NH4+)[Pyruvate] + [Pyruvate][NH4+])
   - 动力学参数: 
     * Km(Pyruvate) ~0.1-0.5 mM
     * Km(NH4+) ~1-5 mM
     * Vmax ~50-100 μmol/min/mg protein
   - 抑制类型: 
     * 丙氨酸: 竞争性抑制剂 (与丙酮酸竞争结合位点), Ki ~0.5-1.0 mM
     * 谷氨酸: 竞争性抑制剂 (与 NH4+ 竞争结合位点), Ki ~0.5-1.0 mM
   - 激活剂: 
     * 胰岛素 (转录水平上调)
     * 丙酮酸 (底物诱导)
   - 抑制剂: 
     * 胰高血糖素 (转录水平下调)
     * 丙氨酸 (产物抑制)
   - 膜定位: 肝细胞浆 (Hepatocyte cytosol)
**5. 能量与热力学**: ΔG°' ≈ -10 kJ/mol (可逆)
**6. 生理意义**: 将肌肉中的氨以丙氨酸形式转运到肝脏，同时将肝脏的葡萄糖转运到肌肉，维持血糖稳定
**7. 病理结局**: 
   - ALT 缺陷: 氨转运障碍 → 血氨升高
   - ALT 活性降低: 丙氨酸-葡萄糖循环效率下降 → 肌肉能量代谢障碍
   - 肝功能衰竭: ALT 释放到血液 → 血清 ALT 升高 (临床诊断指标)

##### 步骤 ID: NIT-02
**1. 反应名称**: 谷氨酰胺合成 (Glutamine Synthesis)
**2. 化学方程式**: 1.0 Glutamate + 1.0 NH4+ + 1.0 ATP → 1.0 Glutamine + 1.0 ADP + 1.0 Pi + 1.0 H+
**3. 核心酶信息**: 谷氨酰胺合成酶 (Glutamine Synthetase, GS), EC 6.3.1.2, 基因型: GLUL
**4. 动力学与调控**: 
   - 反应机制: Ordered Bi-Ter 机制，ATP 先结合
   - 反应序列: 1) 酶结合 ATP → 形成酶-ATP 复合物 2) 结合谷氨酸 → 形成 γ-谷氨酰磷酸中间物 3) 结合 NH4+ → 形成谷氨酰胺 4) 释放产物
   - 速率方程: v = Vmax[Glutamate][NH4+][ATP] / (K1[NH4+][ATP] + K2[Glutamate][ATP] + K3[Glutamate][NH4+] + [Glutamate][NH4+][ATP] + Ki(Glutamine)[Glutamine])
   - 动力学参数: 
     * Km(Glutamate) ~1-5 mM
     * Km(NH4+) ~1-5 mM
     * Km(ATP) ~0.1-0.5 mM
     * Vmax ~10-20 μmol/min/mg protein
   - 抑制类型: 
     * 谷氨酰胺: 反馈抑制剂，Ki ~0.1-0.5 mM
     * AMP: 竞争性抑制剂，Ki ~0.5-1.0 mM
   - 激活剂: 
     * α-Ketoglutarate (别构激活剂)
     * Pi (别构激活剂)
   - 抑制剂: 
     * 谷氨酰胺 (产物抑制)
     * AMP (能量状态抑制)
   - 分区分布: Zone 3 Exclusive (小叶中心区，仅约7%的肝细胞)
   - 梯度逻辑: Activity = Base_Activity × Low_Oxygen_Gradient × NH4+_Gradient
   - 空间约束: 仅在Zone 3的少数细胞中表达，Zone 1-2几乎无活性
   - 膜定位: 肝细胞浆 (Hepatocyte cytosol)
**5. 能量与热力学**: ATP消耗: -1, ΔG°' ≈ -16 kJ/mol (不可逆)
**6. 生理意义**: 两级氨清除系统的第二级，捕获Zone 1漏掉的氨，为其他组织提供氮源
**7. 分区意义**: Zone 3的GS活性确保从Zone 1-2逃逸的氨被捕获，防止氨进入中心静脉
**8. 病理结局**: 
   - GS 缺陷: 氨捕获障碍 → 血氨升高 → 肝性脑病
   - GS 活性降低: 谷氨酰胺合成减少 → 其他组织氮源不足
   - GS 过表达: 可能导致谷氨酸消耗过多 → 神经递质合成障碍

### 尿素循环 (Urea Cycle)

##### 步骤 ID: NIT-03
**1. 反应名称**: 氨甲酰磷酸合成 (Carbamoyl Phosphate Synthesis)
**2. 化学方程式**: 1.0 NH4+ + 1.0 HCO3- + 2.0 ATP → 1.0 Carbamoyl Phosphate + 2.0 ADP + 1.0 Pi + 2.0 H+
**3. 核心酶信息**: 氨甲酰磷酸合成酶 I (Carbamoyl Phosphate Synthetase I, CPS1), EC 6.3.4.16, 尿素循环限速酶, 基因型: CPS1
**4. 动力学与调控**: 
   - 反应机制: Ordered Ter-Ter 机制，NAG 作为别构激活剂
   - 反应序列: 1) 酶结合 NAG (别构激活) 2) 结合 HCO3- 和 ATP → 形成羧基磷酸中间物 3) 结合 NH4+ → 形成氨甲酰磷酸 4) 释放产物
   - 速率方程: v = Vmax[NH4+][HCO3-][ATP] / (K1[HCO3-][ATP] + K2[NH4+][ATP] + K3[NH4+][HCO3-] + [NH4+][HCO3-][ATP] + Ki(Carbamoyl Phosphate)[Carbamoyl Phosphate])
   - 动力学参数: 
     * Km(NH4+) ~1-5 mM
     * Km(HCO3-) ~1-5 mM
     * Km(ATP) ~0.1-0.5 mM
     * Vmax ~5-10 μmol/min/mg protein
   - 抑制类型: 
     * 氨甲酰磷酸: 产物抑制剂，Ki ~0.1-0.5 mM
     * UTP: 反馈抑制剂，Ki ~0.1-0.5 mM
   - 激活剂: 
     * N-Acetylglutamate (NAG, 别构激活剂), Ka ~0.01-0.05 mM
     * Mg2+ (必需辅因子)
   - 抑制剂: 
     * 氨甲酰磷酸 (产物抑制)
     * UTP (反馈抑制)
     * 琥珀酰化修饰 (TCA循环受阻时)
   - 分区分布: Zone 1 Dominant (门静脉周围区)
   - 梯度逻辑: Activity = Base_Activity × Oxygen_Gradient(High) × NAG_Gradient
   - 空间约束: 仅在Zone 1-2表达，Zone 3几乎无活性
   - 膜定位: 线粒体基质 (Mitochondrial matrix)
   - 转录调控: 
     * 糖皮质激素: 上调 CPS1 基因表达
     * 胰岛素: 上调 CPS1 基因表达
     * 胰高血糖素: 上调 CPS1 基因表达
**5. 能量与热力学**: ATP消耗: -2, ΔG°' ≈ -32 kJ/mol (不可逆)
**6. 生理意义**: 尿素循环的第一步和限速步骤，Zone 1的高氧环境有利于氨的氧化
**7. 分区意义**: Zone 1的高CPS1活性确保从门静脉进入的氨被快速清除，防止氨中毒
**8. 病理结局**: 
   - CPS1 缺陷: 先天性高氨血症 I 型，血氨显著升高 → 脑病
   - CPS1 活性降低: 氨清除能力下降 → 高氨血症
   - CPS1 琥珀酰化: TCA循环受阻 → 尿素循环抑制 → 血氨升高

##### 步骤 ID: NIT-04
**1. 反应名称**: 瓜氨酸合成 (Citrulline Synthesis)
**2. 化学方程式**: 1.0 Carbamoyl Phosphate + 1.0 Ornithine → 1.0 Citrulline + 1.0 Pi
**3. 核心酶信息**: 鸟氨酸氨甲酰转移酶 (Ornithine Carbamoyltransferase, OTC), EC 2.1.3.3, 基因型: OTC
**4. 动力学与调控**: 
   - 反应机制: Ordered Bi-Bi 机制，氨甲酰磷酸先结合
   - 反应序列: 1) 酶结合氨甲酰磷酸 → 形成酶-底物复合物 2) 结合鸟氨酸 → 形成瓜氨酸 3) 释放 Pi 4) 释放瓜氨酸
   - 速率方程: v = Vmax[Carbamoyl Phosphate][Ornithine] / (Km(Carbamoyl Phosphate)[Ornithine] + Km(Ornithine)[Carbamoyl Phosphate] + [Carbamoyl Phosphate][Ornithine])
   - 动力学参数: 
     * Km(Carbamoyl Phosphate) ~0.1-0.5 mM
     * Km(Ornithine) ~0.1-0.5 mM
     * Vmax ~10-20 μmol/min/mg protein
   - 抑制类型: 
     * 瓜氨酸: 产物抑制剂，Ki ~0.5-1.0 mM
     * Pi: 竞争性抑制剂，Ki ~1-5 mM
   - 激活剂: 
     * Mg2+ (必需辅因子)
     * K+ (别构激活剂)
   - 抑制剂: 
     * 瓜氨酸 (产物抑制)
     * Pi (产物抑制)
   - 分区分布: Zone 1 Dominant (门静脉周围区)
   - 梯度逻辑: Activity = Base_Activity × Oxygen_Gradient(High)
   - 空间约束: 主要在Zone 1-2表达，Zone 3活性极低
   - 膜定位: 线粒体基质 (Mitochondrial matrix)
   - 转录调控: 
     * 糖皮质激素: 上调 OTC 基因表达
     * 胰岛素: 上调 OTC 基因表达
**5. 能量与热力学**: ΔG°' ≈ -20 kJ/mol (不可逆)
**6. 生理意义**: 尿素循环的第二步，将氨甲酰磷酸与鸟氨酸结合生成瓜氨酸
**7. 分区意义**: Zone 1的高OTC活性与CPS1协同，确保氨的快速清除
**8. 病理结局**: 
   - OTC 缺陷: 先天性高氨血症 II 型，血氨升高 → 脑病
   - OTC 活性降低: 尿素循环效率下降 → 高氨血症
   - OTC 过表达: 可能导致鸟氨酸消耗过多 → 精氨酸合成减少

##### 步骤 ID: NIT-05
**1. 反应名称**: 精氨琥珀酸合成 (Argininosuccinate Synthesis)
**2. 化学方程式**: 1.0 Citrulline + 1.0 Aspartate + 1.0 ATP → 1.0 Argininosuccinate + 1.0 AMP + 2.0 PPi
**3. 核心酶信息**: 精氨琥珀酸合成酶 (Argininosuccinate Synthetase, ASS), EC 6.3.4.5, 基因型: ASS1
**4. 动力学与调控**: 
   - 反应机制: Ordered Ter-Ter 机制，ATP 先结合
   - 反应序列: 1) 酶结合 ATP → 形成酶-ATP 复合物 2) 结合瓜氨酸 → 形成瓜氨酰-AMP 中间物 3) 结合天冬氨酸 → 形成精氨琥珀酸 4) 释放 PPi 和 AMP
   - 速率方程: v = Vmax[Citrulline][Aspartate][ATP] / (K1[Aspartate][ATP] + K2[Citrulline][ATP] + K3[Citrulline][Aspartate] + [Citrulline][Aspartate][ATP] + Ki(Argininosuccinate)[Argininosuccinate])
   - 动力学参数: 
     * Km(Citrulline) ~0.1-0.5 mM
     * Km(Aspartate) ~1-5 mM
     * Km(ATP) ~0.1-0.5 mM
     * Vmax ~5-10 μmol/min/mg protein
   - 抑制类型: 
     * 精氨琥珀酸: 产物抑制剂，Ki ~0.1-0.5 mM
     * AMP: 竞争性抑制剂，Ki ~0.5-1.0 mM
   - 激活剂: 
     * Mg2+ (必需辅因子)
     * K+ (别构激活剂)
   - 抑制剂: 
     * 精氨琥珀酸 (产物抑制)
     * AMP (能量状态抑制)
   - 分区分布: Zone 1 Dominant (门静脉周围区)
   - 梯度逻辑: Activity = Base_Activity × Oxygen_Gradient(High) × Aspartate_Gradient
   - 空间约束: 主要在Zone 1-2表达，Zone 3活性极低
   - 膜定位: 肝细胞浆 (Hepatocyte cytosol)
   - 转录调控: 
     * 糖皮质激素: 上调 ASS1 基因表达
     * 胰岛素: 上调 ASS1 基因表达
**5. 能量与热力学**: ATP消耗: -2 (因2个PPi水解), ΔG°' ≈ -10 kJ/mol (不可逆)
**6. 生理意义**: 尿素循环的第三步，将瓜氨酸与天冬氨酸结合生成精氨琥珀酸
**7. 分区意义**: Zone 1的高ASS活性确保尿素循环的高效进行
**8. 病理结局**: 
   - ASS1 缺陷: 先天性高氨血症 III 型，精氨琥珀酸合成障碍 → 血氨升高
   - ASS1 活性降低: 尿素循环效率下降 → 高氨血症
   - ASS1 过表达: 可能导致天冬氨酸消耗过多 → 其他代谢途径受影响

##### 步骤 ID: NIT-06
**1. 反应名称**: 精氨琥珀酸裂解 (Argininosuccinate Cleavage)
**2. 化学方程式**: 1.0 Argininosuccinate → 1.0 Arginine + 1.0 Fumarate
**3. 核心酶信息**: 精氨琥珀酸裂解酶 (Argininosuccinate Lyase, ASL), EC 4.3.2.1, 基因型: ASL
**4. 动力学与调控**: 
   - 反应机制: 单底物裂解机制
   - 反应序列: 1) 酶结合精氨琥珀酸 → 形成酶-底物复合物 2) 底物分子内重排 → 形成精氨酸和延胡索酸 3) 释放产物
   - 速率方程: v = Vmax[Argininosuccinate] / (Km(Argininosuccinate) + [Argininosuccinate] + Ki(Arginine)[Arginine] + Ki(Fumarate)[Fumarate])
   - 动力学参数: 
     * Km(Argininosuccinate) ~0.1-0.5 mM
     * Vmax ~10-20 μmol/min/mg protein
   - 抑制类型: 
     * 精氨酸: 产物抑制剂，Ki ~0.5-1.0 mM
     * 延胡索酸: 产物抑制剂，Ki ~1-5 mM
   - 激活剂: 
     * Mg2+ (必需辅因子)
     * K+ (别构激活剂)
   - 抑制剂: 
     * 精氨酸 (产物抑制)
     * 延胡索酸 (产物抑制)
   - 分区分布: Zone 1 Dominant (门静脉周围区)
   - 梯度逻辑: Activity = Base_Activity × Oxygen_Gradient(High)
   - 空间约束: 主要在Zone 1-2表达，Zone 3活性极低
   - 膜定位: 肝细胞浆 (Hepatocyte cytosol)
   - 转录调控: 
     * 糖皮质激素: 上调 ASL 基因表达
     * 胰岛素: 上调 ASL 基因表达
**5. 能量与热力学**: ΔG°' ≈ -5 kJ/mol (可逆)
**6. 生理意义**: 尿素循环的第四步，将精氨琥珀酸裂解为精氨酸和延胡索酸，延胡索酸可进入TCA循环
**7. 分区意义**: Zone 1的高ASL活性维持尿素循环的连续性
**8. 病理结局**: 
   - ASL 缺陷: 精氨琥珀酸血症，精氨琥珀酸堆积 → 高氨血症, 神经损伤
   - ASL 活性降低: 尿素循环效率下降 → 高氨血症
   - ASL 过表达: 可能导致精氨酸过度生成 → 一氧化氮合成增加

##### 步骤 ID: NIT-07
**1. 反应名称**: 精氨酸水解 (Arginine Hydrolysis)
**2. 化学方程式**: 1.0 Arginine + 1.0 H2O → 1.0 Urea + 1.0 Ornithine
**3. 核心酶信息**: 精氨酸酶 (Arginase, ARG), EC 3.5.3.1, 基因型: ARG1 (肝脏), ARG2 (肾脏)
**4. 动力学与调控**: 
   - 反应机制: Ordered Bi-Bi 机制，精氨酸先结合
   - 反应序列: 1) 酶结合精氨酸 → 形成酶-底物复合物 2) 结合 H2O → 形成鸟氨酸和尿素 3) 释放尿素 4) 释放鸟氨酸
   - 速率方程: v = Vmax[Arginine] / (Km(Arginine) + [Arginine] + Ki(Urea)[Urea] + Ki(Ornithine)[Ornithine])
   - 动力学参数: 
     * Km(Arginine) ~1-5 mM
     * Vmax ~20-40 μmol/min/mg protein
   - 抑制类型: 
     * 尿素: 产物抑制剂，Ki ~5-10 mM
     * 鸟氨酸: 产物抑制剂，Ki ~1-5 mM
     * Nω-羟基-L-精氨酸: 竞争性抑制剂，Ki ~0.1-0.5 mM
   - 激活剂: 
     * Mn2+ (必需辅因子)
     * Co2+ (替代辅因子)
     * K+ (别构激活剂)
   - 抑制剂: 
     * 尿素 (产物抑制)
     * 鸟氨酸 (产物抑制)
     * Nω-羟基-L-精氨酸 (NOS 中间物)
   - 分区分布: Zone 1 Dominant (门静脉周围区)
   - 梯度逻辑: Activity = Base_Activity × Oxygen_Gradient(High)
   - 空间约束: 主要在Zone 1-2表达，Zone 3活性极低
   - 膜定位: 肝细胞浆 (Hepatocyte cytosol)
   - 转录调控: 
     * 糖皮质激素: 上调 ARG1 基因表达
     * 胰岛素: 上调 ARG1 基因表达
     * 胰高血糖素: 上调 ARG1 基因表达
**5. 能量与热力学**: ΔG°' ≈ -20 kJ/mol (不可逆)
**6. 生理意义**: 尿素循环的最后一步，将精氨酸水解为尿素和鸟氨酸，鸟氨酸可重新参与尿素循环
**7. 分区意义**: Zone 1的高ARG活性确保尿素在门静脉周围区生成并释放到血液中
**8. 病理结局**: 
   - ARG1 缺陷: 先天性高氨血症 IV 型，精氨酸堆积 → 高氨血症, 神经损伤
   - ARG1 活性降低: 尿素循环效率下降 → 高氨血症
   - ARG1 过表达: 可能导致精氨酸消耗过多 → 一氧化氮合成减少

### 两级氨清除系统 (Two-Stage Ammonia Clearance System)

#### 系统概述

肝脏通过空间分区的两级系统高效清除氨，防止氨中毒：

1. **第一级清除 (Primary Clearance - Zone 1)**: 
   - 位置: 门静脉周围区 (Zone 1)
   - 主要酶: CPS1, OTC, ASS, ASL, ARG (尿素循环全套酶)
   - 功能: 将从门静脉进入的高浓度氨快速转化为尿素
   - 效率: 清除约85-90%的氨

2. **第二级清除 (Secondary Clearance - Zone 3)**:
   - 位置: 小叶中心区 (Zone 3)
   - 主要酶: 谷氨酰胺合成酶 (GS)
   - 功能: 捕获从Zone 1-2逃逸的氨
   - 效率: 清除剩余10-15%的氨

#### 分区协同机制

##### 步骤 ID: NIT-08
**1. 反应名称**: 氨的跨分区转运 (Ammonia Trans-Zonal Transport)
**2. 化学方程式**: 
   - Zone 1: NH4+ (高浓度) → 尿素循环 → Urea (释放到血液)
   - Zone 1-2: NH4+ (中等浓度) → 扩散到Zone 3
   - Zone 3: NH4+ (低浓度) + Glutamate → Glutamine (释放到血液)
**3. 核心酶信息**: 
   - Zone 1: CPS1, OTC, ASS, ASL, ARG
   - Zone 3: GS
**4. 动力学与调控**: 
   - Zone 1氨清除率: Vmax ≈ 5-10 μmol/min/g liver
   - Zone 3氨捕获率: Vmax ≈ 0.5-1 μmol/min/g liver
   - 分区梯度: NH4+浓度从Zone 1 (50-100 μM) 递减到Zone 3 (5-10 μM)
   - 氧气梯度: Zone 1 (高氧, 60-80 mmHg) → Zone 3 (低氧, 10-30 mmHg)
   - pH梯度: Zone 1 (pH 7.4-7.5) → Zone 3 (pH 7.2-7.3)
   - 扩散系数: NH4+在肝细胞间的扩散系数 ~1×10^-5 cm²/s
   - 时间尺度: 氨从Zone 1扩散到Zone 3需要数分钟
   - 调控机制: 
     * 缺氧诱导因子 (HIF-1α): 在低氧条件下上调GS表达
     * 糖皮质激素: 上调尿素循环酶表达
     * 胰岛素: 上调尿素循环酶和GS表达
**5. 能量与热力学**: 
   - Zone 1: ATP消耗 -2 per NH4+ (尿素循环)
   - Zone 3: ATP消耗 -1 per NH4+ (谷氨酰胺合成)
   - 总能量消耗: -2.1 per NH4+ (考虑90%通过尿素循环，10%通过谷氨酰胺合成)
**6. 生理意义**: 
   - 确保血液中氨浓度维持在安全水平 (< 50 μM)
   - 防止氨进入中心静脉造成系统性氨中毒
   - 提供谷氨酰胺作为其他组织的氮源
   - 适应不同的代谢状态和氨负荷
**7. 分区意义**: 
   - Zone 1的高氧环境有利于氨的氧化和尿素合成
   - Zone 3的低氧环境适合谷氨酰胺合成
   - 两级系统确保即使第一级清除效率下降，第二级也能提供保护
   - 空间分隔避免了酶之间的相互干扰
**8. 协同机制**: 
   - 底物分配: 高氨负荷时优先通过尿素循环处理
   - 反馈调节: 谷氨酰胺可抑制尿素循环酶活性
   - 代偿机制: Zone 3的GS活性可在Zone 1受损时上调
   - 激素协调: 胰高血糖素促进尿素循环，胰岛素促进谷氨酰胺合成

#### 病理状态下的分区异常

##### 步骤 ID: NIT-09
**1. 反应名称**: 肝性脑病中的氨清除障碍 (Ammonia Clearance Impairment in Hepatic Encephalopathy)
**2. 化学方程式**: 
   - 正常状态: NH4+ (门静脉) → Zone 1清除 (85%) + Zone 3清除 (15%) → 血液NH4+ < 50 μM
   - 肝损伤状态: NH4+ (门静脉) → Zone 1清除 (↓30-50%) + Zone 3清除 (↓50%) → 血液NH4+ > 200 μM
**3. 核心酶信息**: 
   - 受损酶: CPS1, OTC, ASS, ASL, ARG, GS
**4. 动力学与调控**: 
   - 触发: 急性肝衰竭、肝硬化、门体分流
   - 分区影响: Zone 1酶活性下降更显著，Zone 3相对保留
   - 氧气梯度改变: Zone 1氧分压下降 → 尿素循环效率降低
   - 酶活性变化: 
     * CPS1活性: ↓60-80%
     * OTC活性: ↓40-60%
     * ASS活性: ↓40-60%
     * ASL活性: ↓40-60%
     * ARG活性: ↓40-60%
     * GS活性: ↓20-40% (相对保留)
   - 血氨动力学: 血氨浓度与肝损伤程度呈正相关
   - 时间尺度: 急性肝衰竭时血氨可在数小时内升高
**5. 能量与热力学**: 
   - ATP供应不足，氨清除能量需求无法满足
   - 线粒体功能障碍 → 能量产生下降
   - 氧化磷酸化解偶联 → 能量利用效率降低
**6. 生理意义**: 
   - 氨清除能力下降 → 血氨升高 → 脑毒性
   - 谷氨酰胺合成代偿性增加 → 脑内谷氨酰胺堆积 → 脑水肿
   - 血脑屏障通透性增加 → 氨更易进入脑内
   - 神经递质失衡 → 兴奋性毒性
**7. 分区意义**: 
   - Zone 1的尿素循环受损是肝性脑病的主要原因
   - Zone 3的谷氨酰胺合成成为主要的氨清除途径
   - 但Zone 3的清除能力有限，无法完全代偿Zone 1的损失
   - 肝窦内皮细胞损伤 → 氨扩散障碍
**8. 治疗靶点**: 
   - 降氨药物: 乳果糖、拉克替醇
   - 肠道清洁: 减少肠道氨产生
   - 支链氨基酸: 改善氨基酸失衡
   - 肝移植: 终末期肝病的根治方法

#### 琥珀酰化-线粒体压力 (Succinylation - Mitochondrial Stress)

##### 步骤 ID: PTM-SUCC-01
**1. 反应名称**: CPS1琥珀酰化修饰 (CPS1 Succinylation)
**2. 化学方程式**: 
   - 正常状态: CPS1 + NH4+ + HCO3- + ATP → Carbamoyl Phosphate + ADP + Pi
   - TCA受阻状态: CPS1 + Succinyl-CoA + KAT2 → CPS1-Succinyl + CoA-SH
   - 去琥珀酰化: CPS1-Succinyl + SIRT5 → CPS1 + Succinyl-NAD+
**3. 核心酶信息**: 
   - CPS1 (氨甲酰磷酸合成酶 I), EC 6.3.4.16, 尿素循环限速酶, 基因型: CPS1
   - KAT2 (赖氨酸琥珀酰转移酶2), EC 2.3.1.247, 琥珀酰转移酶, 基因型: KAT2
   - SIRT5 (Sirtuin 5), EC 3.5.1.98, 线粒体去琥珀酰化酶, 基因型: SIRT5
**4. 动力学与调控**: 
   - CPS1 Km(NH4+) ~1-5 mM
   - KAT2 Km(Succinyl-CoA) ~0.1-0.5 mM
   - SIRT5 Km(NAD+) ~0.1-0.5 mM
   - 激活剂: N-Acetylglutamate (NAG)
   - 琥珀酰化位点: CPS1的Lys-1290, Lys-1292, Lys-1295（活性中心附近）
   - 琥珀酰化效应: CPS1被琥珀酰化时活性降低70-90%
   - 琥珀酰化条件: TCA循环受阻 → Succinyl-CoA堆积 (> 0.5 mM) → KAT2激活 → CPS1琥珀酰化
   - 去琥珀酰化条件: TCA循环恢复 → Succinyl-CoA下降 → SIRT5激活 → CPS1去琥珀酰化
   - 修饰动力学: 琥珀酰化/去琥珀酰化循环时间常数 ~1-5分钟
**5. 能量与热力学**: 
   - CPS1反应: ATP消耗 -2, ΔG°' ≈ -32 kJ/mol (不可逆)
   - 琥珀酰化: 无直接能量消耗
   - 去琥珀酰化: NAD+消耗 -1, ΔG°' ≈ -15 kJ/mol (不可逆)
**6. 功能说明**: 
   - TCA循环受阻: Succinyl-CoA堆积 → CPS1琥珀酰化 → 尿素循环抑制
   - 尿素循环抑制: 氨清除能力下降 → 血氨升高
   - 去琥珀酰化: TCA循环恢复 → SIRT5激活 → CPS1去琥珀酰化 → 尿素循环恢复
   - 级联效应: CPS1琥珀酰化 → 尿素循环抑制 → 节省ATP → 优先满足TCA循环需求
**7. 生理意义**: 
   - 代谢压力感应机制，TCA循环受阻时抑制尿素循环
   - 防止在能量不足时进行高耗能的尿素合成
   - TCA循环恢复后快速恢复尿素循环功能
   - 协调尿素循环与TCA循环的能量分配
**8. PTM调控意义**: 
   - 琥珀酰化作为线粒体代谢压力的传感器
   - 连接TCA循环状态（Succinyl-CoA水平）与尿素循环活性（CPS1活性）
   - 代谢压力导致高血氨的分子机制
   - 提供比转录调控更快速的代谢适应机制
**9. 病理意义**: 
   - 缺血再灌注损伤: 能量耗竭 → Succinyl-CoA堆积 → CPS1琥珀酰化 → 血氨升高
   - 肝硬化: 线粒体功能障碍 → TCA循环受阻 → CPS1琥珀酰化 → 肝性脑病
   - 遗传性高氨血症: CPS1突变 → 琥珀酰化敏感性改变 → 酶活性异常
**10. 治疗靶点**: 
   - SIRT5激活剂: 促进CPS1去琥珀酰化 → 恢复尿素循环功能
   - 琥珀酰化抑制剂: 抑制KAT2活性 → 减少CPS1琥珀酰化
   - 能量代谢改善: 恢复TCA循环功能 → 降低Succinyl-CoA水平

##### 步骤 ID: PTM-SUCC-02
**1. 反应名称**: 线粒体酶琥珀酰化调控 (Succinylation Regulation of Mitochondrial Enzymes)
**2. 化学方程式**: 
   - 正常状态: 线粒体酶 + 底物 → 产物
   - TCA受阻状态: 线粒体酶 + Succinyl-CoA + KAT2 → 线粒体酶-Succinyl + CoA-SH
   - 去琥珀酰化: 线粒体酶-Succinyl + SIRT5 → 线粒体酶 + Succinyl-NAD+
**3. 核心酶信息**: 
   - KAT2 (赖氨酸琥珀酰转移酶2), EC 2.3.1.247, 琥珀酰转移酶, 基因型: KAT2
   - SIRT5 (Sirtuin 5), EC 3.5.1.98, 线粒体去琥珀酰化酶, 基因型: SIRT5
   - 受影响酶: CPS1, SDH, IDH, GDH等多种线粒体酶
**4. 动力学与调控**: 
   - KAT2 Km(Succinyl-CoA) ~0.1-0.5 mM
   - SIRT5 Km(NAD+) ~0.1-0.5 mM
   - 激活条件: TCA循环受阻 → Succinyl-CoA升高 (> 0.5 mM) → KAT2激活
   - 抑制条件: TCA循环恢复 → Succinyl-CoA下降 → SIRT5激活 → 去琥珀酰化
   - 琥珀酰化效应: 多种线粒体酶被琥珀酰化时活性降低50-90%
   - 去琥珀酰化效应: 线粒体酶去琥珀酰化时活性恢复到正常水平
   - 修饰动力学: 琥珀酰化/去琥珀酰化循环时间常数 ~1-5分钟
**5. 能量与热力学**: 
   - 琥珀酰化: 无直接能量消耗
   - 去琥珀酰化: NAD+消耗 -1, ΔG°' ≈ -15 kJ/mol (不可逆)
**6. 功能说明**: 
   - TCA循环受阻: Succinyl-CoA堆积 → 多种线粒体酶琥珀酰化 → 线粒体代谢整体抑制
   - 代谢抑制: 降低能量消耗，适应代谢压力
   - 去琥珀酰化: TCA循环恢复 → SIRT5激活 → 线粒体酶去琥珀酰化 → 代谢恢复
   - 级联效应: 线粒体酶琥珀酰化 → 代谢重编程 → 优先满足核心能量需求 → 促进细胞存活
   - 协同调控: 琥珀酰化同时影响多个代谢途径 → 实现代谢网络的协调响应
**7. 生理意义**: 
   - 线粒体代谢压力的适应性反应
   - 通过琥珀酰化修饰快速调节线粒体酶活性
   - 防止在能量不足时进行高耗能的代谢过程
   - 增强细胞代谢灵活性，应对不同生理状态
   - 作为细胞应激响应的重要组成部分，协调代谢与能量需求
**8. PTM调控意义**: 
   - 琥珀酰化作为线粒体代谢状态的精细调控机制
   - 连接代谢压力（Succinyl-CoA堆积）与代谢适应（酶活性调节）
   - 提供比转录调控更快速的代谢响应
**9. 病理意义**: 
   - 线粒体疾病: 琥珀酰化/去琥珀酰化失衡 → 线粒体酶活性异常 → 能量代谢障碍
   - 神经退行性疾病: 线粒体功能障碍 → 琥珀酰化过度 → 神经元能量不足 → 细胞死亡
   - 代谢综合征: 胰岛素抵抗 → 线粒体琥珀酰化异常 → 糖脂代谢紊乱
**10. 治疗靶点**: 
   - SIRT5激活剂: 促进线粒体酶去琥珀酰化 → 恢复线粒体功能
   - 琥珀酰化抑制剂: 抑制KAT2活性 → 减少过度琥珀酰化
   - 线粒体保护剂: 改善线粒体功能 → 恢复琥珀酰化/去琥珀酰化平衡

### 核苷酸代谢 (Nucleotide Metabolism)

##### 步骤 ID: NIT-08
**1. 反应名称**: 嘌呤合成 (Purine Synthesis)
**2. 化学方程式**: 多种前体 → 1.0 IMP (肌苷酸) (多步反应)
**3. 核心酶信息**: 
   - 限速酶: PRPP酰胺转移酶 (PRPP Amidotransferase), EC 2.4.2.14, 基因型: PPAT
   - 其他关键酶: 甲酰基转移酶 (Formyltransferase), 次黄嘌呤核苷酸脱氢酶 (IMP Dehydrogenase)
**4. 动力学与调控**: 
   - PRPP酰胺转移酶 Km(PRPP) ~0.1-0.5 mM
   - PRPP酰胺转移酶 Km(Gln) ~1-5 mM
   - 激活剂: PRPP (磷酸核糖焦磷酸)
   - 抑制剂: 
     * IMP, AMP, GMP (反馈抑制)
     * ATP, GTP (别构抑制)
   - 转录调控: 
     * c-Myc: 上调 PPAT 基因表达
     * p53: 下调 PPAT 基因表达
     * 生长因子: 上调嘌呤合成酶表达
**5. 能量与热力学**: 
   - 总ATP消耗: -5
   - ΔG°' ≈ -10 kJ/mol (总体不可逆)
**6. 生理意义**: 
   - 合成嘌呤核苷酸，为DNA/RNA合成提供原料
   - 维持细胞能量状态 (ATP, GTP)
   - 参与信号转导 (cAMP, cGMP)
**7. 病理结局**: 
   - 嘌呤合成过度: 痛风，尿酸生成过多 → 关节炎症
   - 嘌呤合成不足: 免疫缺陷，DNA合成障碍 → 反复感染
   - PPAT 突变: 嘌呤核苷酸合成障碍 → 发育迟缓，贫血

##### 步骤 ID: NIT-09
**1. 反应名称**: 嘧啶合成 (Pyrimidine Synthesis)
**2. 化学方程式**: 多种前体 → 1.0 UMP (尿苷酸) (多步反应)
**3. 核心酶信息**: 
   - 限速酶: 氨甲酰磷酸合成酶 II (Carbamoyl Phosphate Synthetase II), EC 6.3.5.5, 基因型: CAD
   - 其他关键酶: 天冬氨酸转氨甲酰酶 (Aspartate Transcarbamylase), 二氢乳清酸脱氢酶 (Dihydroorotate Dehydrogenase)
**4. 动力学与调控**: 
   - CAD Km(Glutamine) ~1-5 mM
   - CAD Km(CO2) ~1-5 mM
   - CAD Km(ATP) ~0.1-0.5 mM
   - 激活剂: PRPP (磷酸核糖焦磷酸)
   - 抑制剂: 
     * UMP, UDP, UTP (反馈抑制)
     * CTP (别构抑制)
   - 转录调控: 
     * E2F: 上调 CAD 基因表达
     * p53: 下调 CAD 基因表达
     * 生长因子: 上调嘧啶合成酶表达
**5. 能量与热力学**: 
   - 总ATP消耗: -2
   - ΔG°' ≈ -5 kJ/mol (总体不可逆)
**6. 生理意义**: 
   - 合成嘧啶核苷酸，为DNA/RNA合成提供原料
   - 维持细胞能量状态 (UTP, CTP)
   - 参与磷脂合成 (CTP)
**7. 病理结局**: 
   - 嘧啶合成过度: 肿瘤细胞增殖，DNA合成加速 → 癌症进展
   - 嘧啶合成不足: 免疫缺陷，DNA合成障碍 → 反复感染
   - CAD 突变: 嘧啶核苷酸合成障碍 → 发育迟缓，贫血
   - 二氢乳清酸脱氢酶缺陷: 遗传性乳清酸尿症，嘧啶合成障碍 → 高尿酸尿，贫血

##### 步骤 ID: NIT-10
**1. 反应名称**: 嘌呤降解 (Purine Degradation)
**2. 化学方程式**: 1.0 Purine Nucleotide → 1.0 Uric Acid (多步反应)
**3. 核心酶信息**: 
   - 关键酶: 黄嘌呤氧化酶 (Xanthine Oxidase), EC 1.17.3.2, 基因型: XDH
   - 其他酶: 核苷酸磷酸化酶 (Nucleoside Phosphorylase), 嘌呤核苷磷酸化酶 (Purine Nucleoside Phosphorylase)
**4. 动力学与调控**: 
   - 黄嘌呤氧化酶 Km(Xanthine) ~0.01-0.1 mM
   - 黄嘌呤氧化酶 Km(O2) ~0.1-0.5 mM
   - 激活剂: 次黄嘌呤，黄嘌呤
   - 抑制剂: 
     * 别嘌呤醇 (竞争性抑制剂)
     * 氧嘌呤醇 (非竞争性抑制剂)
   - 转录调控: 
     * NF-κB: 上调 XDH 基因表达
     * 氧化应激: 上调 XDH 基因表达
**5. 能量与热力学**: 
   - ΔG°' ≈ -20 kJ/mol (不可逆)
   - 产生 ROS (活性氧物种)
**6. 生理意义**: 
   - 降解多余的嘌呤核苷酸，避免堆积
   - 生成尿酸，作为抗氧化剂
   - 维持嘌呤核苷酸池的平衡
**7. 病理结局**: 
   - 嘌呤降解过度: 痛风，尿酸生成过多 → 关节炎症
   - 嘌呤降解不足: 免疫缺陷，嘌呤核苷酸堆积 → 反复感染
   - XDH 突变: 黄嘌呤尿症，尿酸生成减少 → 肾结石
   - 嘌呤核苷磷酸化酶缺陷: 免疫缺陷，T细胞功能障碍 → 重症联合免疫缺陷

##### 步骤 ID: NIT-11
**1. 反应名称**: 嘧啶降解 (Pyrimidine Degradation)
**2. 化学方程式**: 1.0 Pyrimidine Nucleotide → 1.0 β-Alanine + 1.0 NH4+ + 1.0 CO2 (多步反应)
**3. 核心酶信息**: 
   - 关键酶: 二氢嘧啶脱氢酶 (Dihydropyrimidine Dehydrogenase), EC 1.3.1.2, 基因型: DPYD
   - 其他酶: 二氢嘧啶酶 (Dihydropyrimidinase), β-脲基丙酸酶 (β-Ureidopropionase)
**4. 动力学与调控**: 
   - DPYD Km(Thymine) ~0.01-0.1 mM
   - DPYD Km(Uracil) ~0.01-0.1 mM
   - 激活剂: NADPH
   - 抑制剂: 5-氟尿嘧啶 (竞争性抑制剂)
   - 转录调控: 
     * PPARα: 上调 DPYD 基因表达
     * 氧化应激: 下调 DPYD 基因表达
**5. 能量与热力学**: 
   - ΔG°' ≈ -15 kJ/mol (不可逆)
   - 消耗 NADPH
**6. 生理意义**: 
   - 降解多余的嘧啶核苷酸，避免堆积
   - 生成 β-丙氨酸，参与辅酶A合成
   - 生成氨，参与尿素循环
   - 维持嘧啶核苷酸池的平衡
**7. 病理结局**: 
   - 嘧啶降解过度: 肿瘤细胞代谢，嘧啶消耗过多 → 化疗敏感性增加
   - 嘧啶降解不足: 嘧啶核苷酸堆积 → 毒性反应
   - DPYD 突变: 5-氟尿嘧啶代谢障碍 → 化疗严重毒性
   - 二氢嘧啶酶缺陷: 二氢嘧啶尿症，嘧啶降解障碍 → 神经系统症状
   - β-脲基丙酸酶缺陷: β-脲基丙酸尿症，嘧啶降解障碍 → 神经系统症状

### 氨基酸代谢 (Amino Acid Metabolism)

#### 支链氨基酸代谢 (Branched-Chain Amino Acid Metabolism)

##### 步骤 ID: AA-BCAA-01
**1. 反应名称**: 支链氨基酸转氨 (Branched-Chain Amino Acid Transamination)
**2. 化学方程式**: 1.0 BCAA (Leu/Ile/Val) + 1.0 α-Ketoglutarate → 1.0 BCKA (相应酮酸) + 1.0 Glutamate
**3. 核心酶信息**: 支链氨基酸转氨酶 (Branched-Chain Aminotransferase, BCAT), EC 2.6.1.42, 基因型: BCAT1 (胞浆), BCAT2 (线粒体)
**4. 动力学与调控**: 
   - Km(BCAA) ~0.1-0.5 mM
   - 激活剂: 胰岛素 (转录水平)
   - 抑制剂: 胰高血糖素 (转录水平)
   - 膜定位: 胞浆 (BCAT1) 和线粒体 (BCAT2)
**5. 能量与热力学**: ΔG°' ≈ 0 kJ/mol (可逆)
**6. 生理意义**: 支链氨基酸代谢的第一步，将支链氨基酸转化为相应的酮酸
**7. 病理结局**: 
   - BCAT 缺陷: 枫糖尿症，支链氨基酸及其酮酸堆积 → 神经损伤
   - BCAT 过表达: 支链氨基酸分解加快 → 蛋白质合成障碍

##### 步骤 ID: AA-BCAA-02
**1. 反应名称**: 支链α-酮酸脱氢 (Branched-Chain α-Ketoacid Dehydrogenation)
**2. 化学方程式**: 1.0 BCKA + 1.0 CoA-SH + 1.0 NAD+ → 1.0 Acyl-CoA (相应酰基-CoA) + 1.0 CO2 + 1.0 NADH
**3. 核心酶信息**: 支链α-酮酸脱氢酶复合体 (Branched-Chain α-Ketoacid Dehydrogenase Complex, BCKDC), EC 1.2.4.4, 基因型: BCKDHA, BCKDHB, DBT
**4. 动力学与调控**: 
   - Km(BCKA) ~0.01-0.05 mM
   - 激活剂: Ca2+, 磷酸化 (去磷酸化激活)
   - 抑制剂: BCKDK (支链α-酮酸脱氢酶激酶) 磷酸化抑制, NADH, 产物抑制
   - 膜定位: 线粒体基质 (Mitochondrial matrix)
   - 辅因子: TPP (E1), 硫辛酰胺 (E2), FAD (E3)
**5. 能量与热力学**: ΔG°' ≈ -30 kJ/mol (不可逆)
**6. 生理意义**: 支链氨基酸代谢的限速步骤，将支链酮酸氧化脱羧生成酰基-CoA
**7. 病理结局**: 
   - BCKDC 缺陷: 枫糖尿症，支链酮酸堆积 → 代谢性酸中毒, 神经损伤
   - BCKDC 过度抑制: 支链氨基酸分解受阻 → 肌肉萎缩

#### 芳香族氨基酸代谢 (Aromatic Amino Acid Metabolism)

##### 步骤 ID: AA-ARO-01
**1. 反应名称**: 苯丙氨酸羟化 (Phenylalanine Hydroxylation)
**2. 化学方程式**: 1.0 Phenylalanine + 1.0 O2 + 1.0 BH4 (四氢生物蝶呤) → 1.0 Tyrosine + 1.0 H2O + 1.0 BH2 (二氢生物蝶呤)
**3. 核心酶信息**: 苯丙氨酸羟化酶 (Phenylalanine Hydroxylase, PAH), EC 1.14.16.1, 基因型: PAH
**4. 动力学与调控**: 
   - Km(Phenylalanine) ~0.1-0.5 mM
   - 激活剂: BH4 (辅因子), 苯丙氨酸 (底物激活)
   - 抑制剂: BH2 (产物抑制), 苯丙氨酸类似物
   - 膜定位: 肝细胞胞浆 (Hepatocyte cytosol)
   - 辅因子: BH4, Fe2+
**5. 能量与热力学**: ΔG°' ≈ -20 kJ/mol (不可逆)
**6. 生理意义**: 苯丙氨酸代谢的主要途径，将苯丙氨酸转化为酪氨酸
**7. 病理结局**: 
   - PAH 缺陷: 苯丙酮尿症 (PKU), 苯丙氨酸堆积 → 智力障碍
   - PAH 活性降低: 苯丙氨酸水平升高 → 神经毒性

##### 步骤 ID: AA-ARO-02
**1. 反应名称**: 酪氨酸转氨 (Tyrosine Transamination)
**2. 化学方程式**: 1.0 Tyrosine + 1.0 α-Ketoglutarate → 1.0 p-Hydroxyphenylpyruvate + 1.0 Glutamate
**3. 核心酶信息**: 酪氨酸转氨酶 (Tyrosine Aminotransferase, TAT), EC 2.6.1.5, 基因型: TAT
**4. 动力学与调控**: 
   - Km(Tyrosine) ~0.1-0.5 mM
   - 激活剂: 胰高血糖素, 糖皮质激素 (转录水平)
   - 抑制剂: 胰岛素 (转录水平)
   - 膜定位: 肝细胞胞浆 (Hepatocyte cytosol)
**5. 能量与热力学**: ΔG°' ≈ 0 kJ/mol (可逆)
**6. 生理意义**: 酪氨酸代谢的第一步，将酪氨酸转化为对羟基苯丙酮酸
**7. 病理结局**: 
   - TAT 缺陷: 酪氨酸血症 II 型, 酪氨酸堆积 → 眼部皮肤损伤
   - TAT 过表达: 酪氨酸分解加快 → 黑色素合成减少

##### 步骤 ID: AA-ARO-03
**1. 反应名称**: 色氨酸羟化 (Tryptophan Hydroxylation)
**2. 化学方程式**: 1.0 Tryptophan + 1.0 O2 + 1.0 BH4 → 1.0 5-Hydroxytryptophan + 1.0 H2O + 1.0 BH2
**3. 核心酶信息**: 色氨酸羟化酶 (Tryptophan Hydroxylase, TPH), EC 1.14.16.4, 基因型: TPH1, TPH2
**4. 动力学与调控**: 
   - Km(Tryptophan) ~0.01-0.05 mM
   - 激活剂: BH4 (辅因子), Ca2+/钙调蛋白
   - 抑制剂: p-Chlorophenylalanine (特异性抑制剂)
   - 膜定位: 肝细胞胞浆 (TPH1) 和神经元 (TPH2)
   - 辅因子: BH4, Fe2+
**5. 能量与热力学**: ΔG°' ≈ -20 kJ/mol (不可逆)
**6. 生理意义**: 色氨酸代谢的第一步，将色氨酸转化为5-羟色氨酸，是5-羟色胺合成的前体
**7. 病理结局**: 
   - TPH 缺陷: 5-羟色胺合成障碍 → 抑郁症, 睡眠障碍
   - TPH 活性降低: 5-羟色胺水平下降 → 情绪障碍

#### 含硫氨基酸代谢 (Sulfur-Containing Amino Acid Metabolism)

##### 步骤 ID: AA-SUL-01
**1. 反应名称**: 蛋氨酸腺苷转移 (Methionine Adenosyltransferase)
**2. 化学方程式**: 1.0 Methionine + 1.0 ATP → 1.0 S-Adenosylmethionine (SAM) + 1.0 PPi + 1.0 Pi
**3. 核心酶信息**: 蛋氨酸腺苷转移酶 (Methionine Adenosyltransferase, MAT), EC 2.5.1.6, 基因型: MAT1A (肝脏), MAT2A (其他组织)
**4. 动力学与调控**: 
   - Km(Methionine) ~0.01-0.05 mM
   - 激活剂: 蛋氨酸 (底物激活)
   - 抑制剂: SAM (产物抑制), S-腺苷同型半胱氨酸 (SAH)
   - 膜定位: 肝细胞胞浆 (Hepatocyte cytosol)
**5. 能量与热力学**: ATP 消耗: -2 (因PPi水解), ΔG°' ≈ -40 kJ/mol (不可逆)
**6. 生理意义**: SAM 是主要的甲基供体，参与甲基化反应
**7. 病理结局**: 
   - MAT 缺陷: 高蛋氨酸血症, SAM 合成障碍 → 甲基化反应受阻
   - MAT 活性降低: SAM 水平下降 → 肝损伤, 脂肪肝

##### 步骤 ID: AA-SUL-02
**1. 反应名称**: 同型半胱氨酸合成 (Homocysteine Synthesis)
**2. 化学方程式**: 1.0 SAM + Methyl Acceptor → 1.0 SAH (S-腺苷同型半胱氨酸) + Methylated Product
**3. 核心酶信息**: 甲基转移酶 (Methyltransferases), 多种
**4. 动力学与调控**: 
   - Km(SAM) ~0.01-0.05 mM
   - 激活剂: 底物特异性
   - 抑制剂: SAH (产物抑制)
   - 膜定位: 胞浆 (Cytosol)
**5. 能量与热力学**: ΔG°' ≈ -20 kJ/mol (不可逆)
**6. 生理意义**: SAM 甲基化后生成 SAH，SAH 水解生成同型半胱氨酸
**7. 病理结局**: 
   - 甲基转移酶缺陷: SAH 堆积 → 同型半胱氨酸升高 → 心血管疾病风险增加
   - SAH 水解酶缺陷: SAH 堆积 → 甲基化反应受阻

##### 步骤 ID: AA-SUL-03
**1. 反应名称**: 同型半胱氨酸再甲基化 (Homocysteine Remethylation)
**2. 化学方程式**: 1.0 Homocysteine + 1.0 N5-Methyl-THF → 1.0 Methionine + 1.0 THF
**3. 核心酶信息**: 甲硫氨酸合酶 (Methionine Synthase, MS), EC 2.1.1.13, 基因型: MTR
**4. 动力学与调控**: 
   - Km(Homocysteine) ~0.01-0.05 mM
   - 激活剂: 维生素B12 (辅因子), SAM (别构激活)
   - 抑制剂: N2O (氧化维生素B12), 同型半胱氨酸类似物
   - 膜定位: 胞浆 (Cytosol)
   - 辅因子: 维生素B12 (甲基钴胺素)
**5. 能量与热力学**: ΔG°' ≈ -15 kJ/mol (可逆)
**6. 生理意义**: 同型半胱氨酸再甲基化生成蛋氨酸，维持蛋氨酸循环
**7. 病理结局**: 
   - MS 缺陷: 高同型半胱氨酸血症 → 心血管疾病风险增加, 神经管缺陷
   - 维生素B12 缺乏: MS 活性降低 → 同型半胱氨酸升高 → 巨幼红细胞贫血

##### 步骤 ID: AA-SUL-04
**1. 反应名称**: 同型半胱氨酸转硫 (Homocysteine Transsulfuration)
**2. 化学方程式**: 1.0 Homocysteine + 1.0 Serine → 1.0 Cystathionine + 1.0 H2O
**3. 核心酶信息**: 胱硫醚β-合酶 (Cystathionine β-Synthase, CBS), EC 4.2.1.22, 基因型: CBS
**4. 动力学与调控**: 
   - Km(Homocysteine) ~0.1-0.5 mM
   - 激活剂: 维生素B6 (辅因子), SAM (别构激活)
   - 抑制剂: 同型半胱氨酸类似物, 丙炔甘氨酸
   - 膜定位: 胞浆 (Cytosol)
   - 辅因子: 维生素B6 (磷酸吡哆醛)
**5. 能量与热力学**: ΔG°' ≈ -10 kJ/mol (可逆)
**6. 生理意义**: 同型半胱氨酸转硫途径，生成胱硫醚，最终合成半胱氨酸
**7. 病理结局**: 
   - CBS 缺陷: 同型半胱氨酸尿症, 同型半胱氨酸堆积 → 血栓形成, 晶状体脱位
   - CBS 活性降低: 同型半胱氨酸升高 → 心血管疾病风险增加

##### 步骤 ID: AA-SUL-05
**1. 反应名称**: 胱硫醚裂解 (Cystathionine Cleavage)
**2. 化学方程式**: 1.0 Cystathionine + 1.0 H2O → 1.0 Cysteine + 1.0 α-Ketobutyrate + 1.0 NH4+
**3. 核心酶信息**: 胱硫醚γ-裂解酶 (Cystathionine γ-Lyase, CGL), EC 4.4.1.1, 基因型: CTH
**4. 动力学与调控**: 
   - Km(Cystathionine) ~0.1-0.5 mM
   - 激活剂: 维生素B6 (辅因子)
   - 抑制剂: 丙炔甘氨酸, 氨基乙氧基乙烯基甘氨酸
   - 膜定位: 胞浆 (Cytosol)
   - 辅因子: 维生素B6 (磷酸吡哆醛)
**5. 能量与热力学**: ΔG°' ≈ -15 kJ/mol (不可逆)
**6. 生理意义**: 胱硫醚裂解生成半胱氨酸和α-酮丁酸，是半胱氨酸合成的关键步骤
**7. 病理结局**: 
   - CGL 缺陷: 半胱氨酸合成障碍 → 谷胱甘肽合成减少 → 氧化应激
   - CGL 活性降低: 半胱氨酸水平下降 → 蛋白质合成障碍

### 一碳代谢 (One-Carbon Metabolism)

##### 步骤 ID: OCM-01
**1. 反应名称**: 丝氨酸羟甲基转移 (Serine Hydroxymethyltransferase)
**2. 化学方程式**: 1.0 Serine + 1.0 THF → 1.0 Glycine + 1.0 N5,N10-Methylene-THF + 1.0 H2O
**3. 核心酶信息**: 丝氨酸羟甲基转移酶 (Serine Hydroxymethyltransferase, SHMT), EC 2.1.2.1, 基因型: SHMT1 (胞浆), SHMT2 (线粒体)
**4. 动力学与调控**: 
   - Km(Serine) ~0.1-0.5 mM
   - 激活剂: 甘氨酸 (产物激活)
   - 抑制剂: 丝氨酸类似物
   - 膜定位: 胞浆 (SHMT1) 和线粒体 (SHMT2)
   - 辅因子: 维生素B6 (磷酸吡哆醛), THF
**5. 能量与热力学**: ΔG°' ≈ -5 kJ/mol (可逆)
**6. 生理意义**: 一碳代谢的关键反应，生成甘氨酸和N5,N10-亚甲基-THF，为核苷酸合成提供一碳单位
**7. 病理结局**: 
   - SHMT 缺陷: 甘氨酸合成障碍, 一碳单位生成减少 → 核苷酸合成障碍
   - SHMT 活性降低: 核苷酸合成受阻 → 细胞增殖障碍

##### 步骤 ID: OCM-02
**1. 反应名称**: 亚甲基-THF还原 (Methylene-THF Reductase)
**2. 化学方程式**: 1.0 N5,N10-Methylene-THF + 1.0 NADPH + 1.0 H+ → 1.0 N5-Methyl-THF + 1.0 NADP+
**3. 核心酶信息**: 亚甲基四氢叶酸还原酶 (Methylenetetrahydrofolate Reductase, MTHFR), EC 1.5.1.20, 基因型: MTHFR
**4. 动力学与调控**: 
   - Km(N5,N10-Methylene-THF) ~0.01-0.05 mM
   - 激活剂: SAM (别构激活)
   - 抑制剂: SAH (产物抑制), FAD 缺乏
   - 膜定位: 胞浆 (Cytosol)
   - 辅因子: FAD, NADPH
**5. 能量与热力学**: NADPH 消耗: -1, ΔG°' ≈ -20 kJ/mol (不可逆)
**6. 生理意义**: 将N5,N10-亚甲基-THF还原为N5-甲基-THF，为同型半胱氨酸再甲基化提供甲基
**7. 病理结局**: 
   - MTHFR 缺陷: 高同型半胱氨酸血症 → 心血管疾病风险增加, 神经管缺陷
   - MTHFR 多态性 (C677T): 酶活性降低 → 同型半胱氨酸升高 → 疾病风险增加

##### 步骤 ID: OCM-03
**1. 反应名称**: 甲酰-THF合成 (Formyl-THF Synthesis)
**2. 化学方程式**: 1.0 N5,N10-Methenyl-THF + 1.0 H2O → 1.0 N10-Formyl-THF + 1.0 H+
**3. 核心酶信息**: 亚甲基四氢叶酸脱氢酶 (Methylenetetrahydrofolate Dehydrogenase, MTHFD), EC 1.5.1.5, 基因型: MTHFD1 (胞浆), MTHFD2 (线粒体)
**4. 动力学与调控**: 
   - Km(N5,N10-Methenyl-THF) ~0.01-0.05 mM
   - 激活剂: NADP+
   - 抑制剂: 甲氨蝶呤 (MTX)
   - 膜定位: 胞浆 (MTHFD1) 和线粒体 (MTHFD2)
   - 辅因子: NADP+, THF
**5. 能量与热力学**: ΔG°' ≈ -10 kJ/mol (可逆)
**6. 生理意义**: 生成N10-甲酰-THF，为嘌呤合成提供一碳单位
**7. 病理结局**: 
   - MTHFD 缺陷: 嘌呤合成障碍 → DNA合成受阻 → 细胞增殖障碍
   - MTHFD 活性降低: 嘌呤合成减少 → 免疫缺陷

### 氨基酸分解代谢 (Amino Acid Catabolism)

##### 步骤 ID: AAC-01
**1. 反应名称**: 丙氨酸转氨 (Alanine Transamination)
**2. 化学方程式**: 1.0 Alanine + 1.0 α-Ketoglutarate → 1.0 Pyruvate + 1.0 Glutamate
**3. 核心酶信息**: 丙氨酸转氨酶 (Alanine Aminotransferase, ALT), EC 2.6.1.2, 基因型: GPT
**4. 动力学与调控**: 
   - 反应机制: Ping-Pong Bi-Bi 机制
   - 反应序列: 1) 酶 (E) 首先结合丙氨酸 → 形成酶-底物复合物 2) 释放丙酮酸，酶转化为 E-NH2 中间态 3) E-NH2 结合 α-酮戊二酸 → 形成第二复合物 4) 释放谷氨酸，酶 (E) 再生
   - 速率方程: v = Vmax[Alanine][α-Ketoglutarate] / (Km(Alanine)[α-Ketoglutarate] + Km(α-Ketoglutarate)[Alanine] + [Alanine][α-Ketoglutarate])
   - 动力学参数: 
     * Km(Alanine) ~0.1-0.5 mM
     * Km(α-Ketoglutarate) ~0.1-0.3 mM
     * Vmax ~100-200 μmol/min/mg protein
   - 抑制类型: 
     * 丙酮酸: 竞争性抑制剂 (与丙氨酸竞争结合位点), Ki ~0.2-0.5 mM
     * 谷氨酸: 竞争性抑制剂 (与 α-酮戊二酸竞争结合位点), Ki ~0.3-0.8 mM
   - 激活剂: 胰岛素 (转录水平)
   - 抑制剂: 胰高血糖素 (转录水平)
   - 膜定位: 肝细胞胞浆 (Hepatocyte cytosol)
   - 辅因子: 维生素B6 (磷酸吡哆醛)
**5. 能量与热力学**: ΔG°' ≈ 0 kJ/mol (可逆)
**6. 生理意义**: 丙氨酸-葡萄糖循环的关键反应，将丙氨酸转化为丙酮酸，为糖异生提供底物
**7. 病理结局**: 
   - ALT 缺陷: 丙氨酸代谢障碍 → 丙氨酸堆积 → 蛋白质合成障碍
   - ALT 升高: 肝细胞损伤标志 → 肝炎, 肝硬化

##### 步骤 ID: AAC-02
**1. 反应名称**: 天冬氨酸转氨 (Aspartate Transamination)
**2. 化学方程式**: 1.0 Aspartate + 1.0 α-Ketoglutarate → 1.0 Oxaloacetate + 1.0 Glutamate
**3. 核心酶信息**: 天冬氨酸转氨酶 (Aspartate Aminotransferase, AST), EC 2.6.1.1, 基因型: GOT1 (胞浆), GOT2 (线粒体)
**4. 动力学与调控**: 
   - 反应机制: Ping-Pong Bi-Bi 机制
   - 反应序列: 1) 酶 (E) 首先结合天冬氨酸 → 形成酶-底物复合物 2) 释放草酰乙酸，酶转化为 E-NH2 中间态 3) E-NH2 结合 α-酮戊二酸 → 形成第二复合物 4) 释放谷氨酸，酶 (E) 再生
   - 速率方程: v = Vmax[Aspartate][α-Ketoglutarate] / (Km(Aspartate)[α-Ketoglutarate] + Km(α-Ketoglutarate)[Aspartate] + [Aspartate][α-Ketoglutarate])
   - 动力学参数: 
     * Km(Aspartate) ~0.1-0.5 mM
     * Km(α-Ketoglutarate) ~0.1-0.3 mM
     * Vmax ~150-250 μmol/min/mg protein
   - 抑制类型: 
     * 草酰乙酸: 竞争性抑制剂 (与天冬氨酸竞争结合位点), Ki ~0.1-0.4 mM
     * 谷氨酸: 竞争性抑制剂 (与 α-酮戊二酸竞争结合位点), Ki ~0.2-0.7 mM
   - 激活剂: 胰岛素 (转录水平)
   - 抑制剂: 胰高血糖素 (转录水平)
   - 膜定位: 胞浆 (GOT1) 和线粒体 (GOT2)
   - 辅因子: 维生素B6 (磷酸吡哆醛)
**5. 能量与热力学**: ΔG°' ≈ 0 kJ/mol (可逆)
**6. 生理意义**: 天冬氨酸代谢的关键反应，将天冬氨酸转化为草酰乙酸，为尿素循环提供底物
**7. 病理结局**: 
   - AST 缺陷: 天冬氨酸代谢障碍 → 尿素循环受阻 → 高氨血症
   - AST 升高: 肝细胞损伤标志 → 肝炎, 肝硬化

##### 步骤 ID: AAC-03
**1. 反应名称**: 谷氨酸脱氢 (Glutamate Dehydrogenation)
**2. 化学方程式**: 1.0 Glutamate + 1.0 NAD+ + 1.0 H2O → 1.0 α-Ketoglutarate + 1.0 NH4+ + 1.0 NADH
**3. 核心酶信息**: 谷氨酸脱氢酶 (Glutamate Dehydrogenase, GDH), EC 1.4.1.3, 基因型: GLUD1 (肝脏), GLUD2 (脑)
**4. 动力学与调控**: 
   - Km(Glutamate) ~0.5-1.0 mM
   - 激活剂: ADP (别构激活), Leucine (别构激活)
   - 抑制剂: GTP (别构抑制), ATP (别构抑制)
   - 膜定位: 线粒体基质 (Mitochondrial matrix)
   - 辅因子: NAD+ 或 NADP+
**5. 能量与热力学**: ΔG°' ≈ -10 kJ/mol (可逆)
**6. 生理意义**: 谷氨酸氧化脱氨，生成α-酮戊二酸和氨，是氨的主要来源之一
**7. 病理结局**: 
   - GDH 缺陷: 高氨血症, 谷氨酸堆积 → 神经毒性
   - GDH 过度激活: 谷氨酸分解加快 → 神经递质合成障碍

##### 步骤 ID: AAC-04
**1. 反应名称**: 谷氨酰胺酶 (Glutaminase)
**2. 化学方程式**: 1.0 Glutamine + 1.0 H2O → 1.0 Glutamate + 1.0 NH4+
**3. 核心酶信息**: 谷氨酰胺酶 (Glutaminase, GLS), EC 3.5.1.2, 基因型: GLS1 (肾脏型), GLS2 (肝脏型)
**4. 动力学与调控**: 
   - Km(Glutamine) ~0.5-1.0 mM
   - 激活剂: 磷酸盐 (Pi)
   - 抑制剂: 6-Diazo-5-oxo-L-norleucine (DON)
   - 膜定位: 线粒体基质 (Mitochondrial matrix)
**5. 能量与热力学**: ΔG°' ≈ -15 kJ/mol (不可逆)
**6. 生理意义**: 谷氨酰胺水解生成谷氨酸和氨，是氨的主要来源之一
**7. 病理结局**: 
   - GLS 缺陷: 谷氨酰胺堆积 → 高氨血症
   - GLS 过度激活: 谷氨酰胺分解加快 → 氨生成过多 → 肝性脑病

## 模块 D：合成与分泌（物资输出站）

### 胆汁酸合成 (Bile Acid Synthesis)

##### 步骤 ID: BILE-SYN-01
**1. 反应名称**: 胆固醇7α-羟化 (Cholesterol 7α-Hydroxylation)
**2. 化学方程式**: 1.0 Cholesterol + 1.0 NADPH + 1.0 O2 → 1.0 7α-Hydroxycholesterol + 1.0 NADP+ + 1.0 H2O
**3. 核心酶信息**: 胆固醇7α-羟化酶 (Cholesterol 7α-Hydroxylase, CYP7A1), EC 1.14.13.17, 基因型: CYP7A1
**4. 动力学与调控**: 
   - Km(Cholesterol) ~0.01-0.05 mM
   - Km(NADPH) ~0.01-0.05 mM
   - Vmax ~5-10 pmol/min/mg protein
   - 调控: 
     * 受 FXR (Farnesoid X Receptor) 负反馈调节，胆汁酸高时抑制 CYP7A1 表达
     * 受 LRH-1 (Liver Receptor Homolog-1) 正调控
     * 受胰岛素抑制，胰高血糖素激活
   - 膜定位: 内质网 (Endoplasmic Reticulum)
**5. 能量与热力学**: NADPH 消耗: -1, ΔG°' ≈ -20 kJ/mol (不可逆)
**6. 生理意义**: 胆汁酸合成的限速步骤，将胆固醇转化为7α-羟基胆固醇
**7. 病理结局**: 
   - CYP7A1 缺陷: 胆汁酸合成减少 → 胆固醇积累 → 胆结石, 高胆固醇血症
   - CYP7A1 过度激活: 胆汁酸合成增加 → 胆汁酸腹泻
**8. 治疗靶点**: 
   - FXR 激动剂: 抑制 CYP7A1 活性，减少胆汁酸合成
   - 他汀类药物: 降低胆固醇合成，减少胆汁酸前体

##### 步骤 ID: BILE-SYN-02
**1. 反应名称**: 胆汁酸侧链氧化 (Bile Acid Side Chain Oxidation)
**2. 化学方程式**: 1.0 7α-Hydroxycholesterol + 多个 NADPH + 多个 O2 → 1.0 Chenodeoxycholic Acid + 多个 NADP+ + 多个 H2O
**3. 核心酶信息**: 固醇27-羟化酶 (Sterol 27-Hydroxylase, CYP27A1), EC 1.14.15.15, 基因型: CYP27A1
**4. 动力学与调控**: 
   - Km(7α-Hydroxycholesterol) ~0.01-0.05 mM
   - Vmax ~10-20 pmol/min/mg protein
   - 调控: 受胆汁酸水平反馈调节
   - 膜定位: 线粒体 (Mitochondria)
**5. 能量与热力学**: 多个 NADPH 消耗, ΔG°' ≈ -50 kJ/mol (不可逆)
**6. 生理意义**: 氧化胆固醇侧链，生成初级胆汁酸
**7. 病理结局**: 
   - CYP27A1 缺陷:  cerebrotendinous xanthomatosis (CTX), 胆固醇积累 → 黄色瘤, 神经系统损害
**8. 治疗靶点**: 
   - 鹅去氧胆酸: 补充外源性胆汁酸

##### 步骤 ID: BILE-SYN-03
**1. 反应名称**: 胆汁酸结合 (Bile Acid Conjugation)
**2. 化学方程式**: 1.0 Chenodeoxycholic Acid + 1.0 Glycine/Taurine + 1.0 ATP → 1.0 Glycocholic Acid/Taurocholic Acid + 1.0 AMP + 1.0 PPi
**3. 核心酶信息**: 胆汁酸-CoA连接酶 (Bile Acid-CoA Ligase, SLC27A5), EC 6.2.1.7, 基因型: SLC27A5; 胆汁酸-CoA:氨基酸N-酰基转移酶 (Bile Acid-CoA:Amino Acid N-Acyltransferase, BAAT), EC 2.3.1.65, 基因型: BAAT
**4. 动力学与调控**: 
   - Km(Chenodeoxycholic Acid) ~0.01-0.05 mM
   - Vmax ~50-100 pmol/min/mg protein
   - 调控: 受胆汁酸合成速率调节
   - 膜定位: 胞浆 (SLC27A5) 和 peroxisome (BAAT)
**5. 能量与热力学**: ATP 消耗: -1, ΔG°' ≈ -30 kJ/mol (不可逆)
**6. 生理意义**: 胆汁酸与甘氨酸或牛磺酸结合，增加水溶性，促进分泌
**7. 病理结局**: 
   - BAAT 缺陷: 未结合胆汁酸积累 → 胆汁酸毒性增加
**8. 治疗靶点**: 
   - 牛磺酸补充: 促进胆汁酸结合

### 胆汁分泌泵系统 (Bile Secretion System)

#### 胆汁盐外排泵 (BSEP)

##### 步骤 ID: BILE-01
**1. 反应名称**: 胆汁盐外排 (Bile Salt Export)
**2. 化学方程式**: 1.0 Conjugated Bile Acid(cytosol) + ATP → 1.0 Conjugated Bile Acid(bile) + ADP + Pi
**3. 核心酶信息**: BSEP (Bile Salt Export Pump, ABCB11), ATP 结合盒转运体, 基因型: ABCB11
**4. 动力学与调控**: 
   - ATP 消耗: -1 (直接消耗 ATP)
   - Km(Conjugated Bile Acid) ~0.1-0.5 mM
   - Vmax ~100-200 pmol/min/mg protein
   - 调控: 
     * 受 FXR (Farnesoid X Receptor) 核受体调控，FXR 激活时 BSEP 表达上调
     * 受 PXR (Pregnane X Receptor) 调控，PXR 激活时 BSEP 表达上调
   - 抑制剂: 
     * 某些药物 (如环孢素、利福平) 可抑制 BSEP 活性
     * 胆汁酸浓度过高时的反馈抑制
   - 膜定位: 肝细胞胆小管膜 (Canalicular membrane)
**5. 能量与热力学**: ATP 消耗: -1, ΔG°' ≈ -30 kJ/mol (不可逆)
**6. 生理意义**: 是胆汁流形成的限速步骤，将结合型胆汁酸泵入胆汁，维持胆汁酸稳态
**7. 病理结局**: 
   - ABCB11 突变: 进行性家族性肝内胆汁淤积症 2 型 (PFIC2)，胆汁酸排泄障碍 → 胆汁淤积, 肝损伤
   - BSEP 抑制: 药物性胆汁淤积，胆汁酸堆积 → 肝损伤
   - BSEP 表达下调: 肝硬化，胆汁酸排泄能力下降 → 黄疸
**8. 治疗靶点**: 
   - FXR 激动剂: 奥贝胆酸，上调 BSEP 表达
   - 胆汁酸螯合剂: 考来烯胺，减少肠道胆汁酸吸收
   - 肝移植: 终末期 PFIC2 的根治方法
**9. 逻辑门**: 若 BSEP 被抑制或表达下调，胆汁酸在肝细胞内堆积 → 胆汁淤积 → 肝损伤

#### 胆固醇外排泵 (ABCG5/8)

##### 步骤 ID: BILE-02
**1. 反应名称**: 胆固醇外排 (Cholesterol Export)
**2. 化学方程式**: 1.0 Cholesterol(cytosol) + ATP → 1.0 Cholesterol(bile) + ADP + Pi
**3. 核心酶信息**: ABCG5/8 (ATP Binding Cassette Subfamily G Member 5/8), 异源二聚体转运体, 基因型: ABCG5, ABCG8
**4. 动力学与调控**: 
   - ATP 消耗: -1 (直接消耗 ATP)
   - Km(Cholesterol) ~0.1-0.5 mM
   - Vmax ~50-100 pmol/min/mg protein
   - 调控: 
     * 受 LXR (Liver X Receptor) 核受体调控，LXR 激活时 ABCG5/8 表达上调
     * 受 FXR 调控，FXR 激活时 ABCG5/8 表达上调
   - 底物: 胆固醇、植物固醇
   - 抑制剂: 某些药物 (如依折麦布) 可抑制 ABCG5/8 活性
   - 膜定位: 肝细胞胆小管膜 (Canalicular membrane)
**5. 能量与热力学**: ATP 消耗: -1, ΔG°' ≈ -30 kJ/mol (不可逆)
**6. 生理意义**: 将胆固醇和植物固醇泵入胆汁，是胆固醇排泄的主要途径
**7. 病理结局**: 
   - ABCG5/8 突变: 谷固醇血症，植物固醇吸收增加 → 动脉粥样硬化风险增加
   - ABCG5/8 表达下调: 胆固醇排泄减少 → 高胆固醇血症, 脂肪肝
   - ABCG5/8 功能缺陷: 脂质沉积 → 肝细胞损伤
**8. 治疗靶点**: 
   - LXR 激动剂: 上调 ABCG5/8 表达
   - 植物固醇限制: 减少肠道植物固醇吸收
   - 他汀类药物: 降低胆固醇合成
**9. 逻辑门**: 若 ABCG5/8 功能缺陷，胆固醇在肝细胞内堆积 → 脂质沉积 → 脂肪肝

#### 胆汁酸重吸收 (NTCP)

##### 步骤 ID: BILE-03
**1. 反应名称**: 胆汁酸重吸收 (Bile Acid Reabsorption)
**2. 化学方程式**: 1.0 Conjugated Bile Acid(blood) + Na+ → 1.0 Conjugated Bile Acid(cytosol) + Na+
**3. 核心酶信息**: NTCP (Na+-Taurocholate Cotransporting Polypeptide, SLC10A1), 基底膜侧胆汁酸转运体, 基因型: SLC10A1
**4. 动力学与调控**: 
   - 继发性主动转运，依赖钠离子梯度
   - Km(Conjugated Bile Acid) ~0.01-0.1 mM
   - Vmax ~100-200 pmol/min/mg protein
   - 底物: 结合型胆汁酸
   - 调控: 
     * 受 FXR 核受体调控，FXR 激活时 NTCP 表达下调
     * 受 HNF4α (Hepatocyte Nuclear Factor 4α) 调控，HNF4α 激活时 NTCP 表达上调
     * 受 PXR 调控，PXR 激活时 NTCP 表达下调
   - 抑制剂: 某些药物 (如环孢素、利福平) 可抑制 NTCP 活性
   - 膜定位: 肝细胞基底膜 (Basolateral membrane)
**5. 能量与热力学**: 间接消耗 ATP (维持钠离子梯度), ΔG°' ≈ -20 kJ/mol
**6. 生理意义**: 肠肝循环的回收站，从门静脉血液中回收胆汁酸，减少胆汁酸合成需求
**7. 病理结局**: 
   - SLC10A1 突变: 进行性家族性肝内胆汁淤积症 1 型 (PFIC1)，胆汁酸重吸收障碍 → 胆汁酸合成增加
   - NTCP 抑制: 药物性胆汁酸重吸收障碍 → 胆汁酸丢失增加
   - NTCP 表达下调: 肝硬化，胆汁酸重吸收能力下降 → 胆汁酸合成增加
**8. 治疗靶点**: 
   - HNF4α 激动剂: 上调 NTCP 表达
   - 胆汁酸替代治疗: 补充外源性胆汁酸
**9. 逻辑门**: 若 NTCP 被抑制，胆汁酸回收减少 → 肝脏需要合成更多胆汁酸 → 增加胆固醇消耗

### 胆固醇生物合成 (Cholesterol Biosynthesis)

##### 步骤 ID: CHOL-01
**1. 反应名称**: 甲羟戊酸生成 (Mevalonate Formation)
**2. 化学方程式**: 3.0 Acetyl-CoA + 2.0 NADPH + 2.0 H+ + 1.0 ATP → 1.0 Mevalonate + 3.0 CoA-SH + 2.0 NADP+ + 1.0 ADP + 1.0 Pi
**3. 核心酶信息**: HMG-CoA还原酶 (HMG-CoA Reductase, HMGCR), EC 1.1.1.34, 胆固醇合成限速酶, 基因型: HMGCR
**4. 动力学与调控**: 
   - Km(HMG-CoA) ~0.01-0.05 mM
   - Km(NADPH) ~0.01-0.05 mM
   - Vmax ~100-200 nmol/min/mg protein
   - 受[Cholesterol]产物的负反馈调节
   - 受[AMPK]磷酸化抑制
   - 受[Insulin]诱导激活
   - 抑制剂: Statins (他汀类药物, 竞争性抑制剂, Ki ~0.1-1.0 nM)
   - 非磷酸化修饰: 泛素化 (Ubiquitination)
   - 泛素化位点: HMGCR的多个赖氨酸位点 (Lys-248, Lys-352等)
   - 泛素化效应: HMGCR被泛素化时被标记为降解
   - 泛素连接酶: gp78 (E3泛素连接酶), HRD1 (E3泛素连接酶)
   - 泛素化条件: 胆固醇高 (> 5 mM) → Insig1/2激活 → gp78/HRD1激活 → HMGCR泛素化
   - 去泛素化条件: 胆固醇正常 (< 3 mM) → Insig1/2抑制 → HMGCR去泛素化 → 稳定
   - 半衰期调节: 
     * 胆固醇高: HMGCR泛素化 → 蛋白酶体降解 → 半衰期缩短至30-60分钟
     * 胆固醇正常: HMGCR去泛素化 → 蛋白稳定 → 半衰期延长至4-6小时
   - 转录调控: 
     * SREBP-2 (Sterol Regulatory Element-Binding Protein 2): 上调 HMGCR 基因表达
     * LXR: 下调 HMGCR 基因表达
     * 胰岛素: 上调 HMGCR 基因表达
     * 胰高血糖素: 下调 HMGCR 基因表达
   - 膜定位: 内质网 (Endoplasmic Reticulum)
**5. 能量与热力学**: ATP消耗: -1, NADPH消耗: -2, ΔG°' ≈ -18 kJ/mol (不可逆)
**6. 空间定位**: 胞浆内质网 (Endoplasmic Reticulum)
**7. 生理意义**: 胆固醇合成的限速步骤，受胆固醇水平的精细调控
**8. PTM调控意义**: 
   - 泛素化作为胆固醇水平的快速调控机制
   - 胆固醇高时：HMGCR泛素化 → 蛋白降解 → 胆固醇合成抑制
   - 胆固醇正常时：HMGCR去泛素化 → 蛋白稳定 → 胆固醇合成恢复
   - 通过半衰期调节实现胆固醇合成的快速响应
**9. 病理结局**: 
   - HMGCR 过度激活: 胆固醇合成增加 → 高胆固醇血症, 动脉粥样硬化
   - HMGCR 缺陷: 胆固醇合成减少 → 发育迟缓, 脂溶性维生素缺乏
   - HMGCR 突变: 对他汀类药物敏感性改变 → 药物疗效差异
**10. 治疗靶点**: 
   - 他汀类药物: 抑制 HMGCR 活性，降低胆固醇合成
   - PCSK9 抑制剂: 增加 LDL 受体表达，促进胆固醇清除
   - 依折麦布: 抑制肠道胆固醇吸收

##### 步骤 ID: CHOL-02
**1. 反应名称**: 甲羟戊酸磷酸化 (Mevalonate Phosphorylation)
**2. 化学方程式**: 1.0 Mevalonate + 2.0 ATP → 1.0 Mevalonate-5-Pyrophosphate + 2.0 ADP
**3. 核心酶信息**: 甲羟戊酸激酶 (Mevalonate Kinase, MVK), EC 2.7.1.36, 基因型: MVK; 磷酸甲羟戊酸激酶 (Phosphomevalonate Kinase, PMK), EC 2.7.4.2, 基因型: PMVK
**4. 动力学与调控**: 
   - MVK Km(Mevalonate) ~0.05-0.1 mM
   - MVK Km(ATP) ~0.1-0.5 mM
   - MVK Vmax ~200-400 nmol/min/mg protein
   - PMK Km(Mevalonate-5-P) ~0.01-0.05 mM
   - PMK Km(ATP) ~0.1-0.5 mM
   - PMK Vmax ~200-400 nmol/min/mg protein
   - 抑制剂: 高浓度产物反馈抑制
   - 调控: 
     * 受 SREBP-2 调控，SREBP-2 激活时 MVK 和 PMVK 表达上调
     * 受胰岛素调控，胰岛素激活时 MVK 和 PMVK 表达上调
   - 膜定位: 胞浆 (Cytosol)
**5. 能量与热力学**: ATP 消耗: -2, ΔG°' ≈ -40 kJ/mol (不可逆)
**6. 生理意义**: 甲羟戊酸磷酸化是胆固醇合成的第二步，为后续反应提供活性中间产物
**7. 病理结局**: 
   - MVK 缺陷: 甲羟戊酸激酶缺乏症，胆固醇合成减少 → 发育迟缓, 反复感染
   - PMVK 缺陷: 磷酸甲羟戊酸激酶缺乏症，胆固醇合成减少 → 发育迟缓, 脂溶性维生素缺乏
**8. 治疗靶点**: 
   - 补充胆固醇: 缓解胆固醇合成缺陷症状
   - 补充脂溶性维生素: 缓解维生素缺乏症状

##### 步骤 ID: CHOL-03
**1. 反应名称**: 异戊烯焦磷酸合成 (Isopentenyl Pyrophosphate Synthesis)
**2. 化学方程式**: 1.0 Mevalonate-5-Pyrophosphate → 1.0 Isopentenyl Pyrophosphate (IPP) + CO2
**3. 核心酶信息**: 甲羟戊酸焦磷酸脱羧酶 (Mevalonate Pyrophosphate Decarboxylase, MVD), EC 4.1.1.33, 基因型: MVD
**4. 动力学与调控**: 
   - Km(Mevalonate-5-Pyrophosphate) ~0.01-0.05 mM
   - Vmax ~150-300 nmol/min/mg protein
   - 调控: 
     * 受 SREBP-2 调控，SREBP-2 激活时 MVD 表达上调
     * 受胰岛素调控，胰岛素激活时 MVD 表达上调
   - 膜定位: 胞浆 (Cytosol)
**5. 能量与热力学**: ΔG°' ≈ -20 kJ/mol (不可逆)
**6. 生理意义**: 甲羟戊酸焦磷酸脱羧生成异戊烯焦磷酸 (IPP)，是胆固醇合成的关键中间步骤
**7. 病理结局**: 
   - MVD 缺陷: 异戊烯焦磷酸合成减少 → 胆固醇合成障碍 → 发育迟缓, 脂溶性维生素缺乏
**8. 治疗靶点**: 
   - 补充胆固醇: 缓解胆固醇合成缺陷症状
   - 补充脂溶性维生素: 缓解维生素缺乏症状

##### 步骤 ID: CHOL-04
**1. 反应名称**: 异戊烯焦磷酸异构化 (IPP Isomerization)
**2. 化学方程式**: 1.0 IPP ⇌ 1.0 Dimethylallyl Pyrophosphate (DMAPP)
**3. 核心酶信息**: 异戊烯焦磷酸异构酶 (Isopentenyl Pyrophosphate Isomerase, IDI), EC 5.3.3.2, 基因型: IDI1
**4. 动力学与调控**: 
   - Km(IPP) ~0.01-0.05 mM
   - Km(DMAPP) ~0.01-0.05 mM
   - Vmax ~200-400 nmol/min/mg protein
   - 平衡偏向 IPP:DMAPP ≈ 6:1
   - 调控: 
     * 受 SREBP-2 调控，SREBP-2 激活时 IDI1 表达上调
     * 受胰岛素调控，胰岛素激活时 IDI1 表达上调
   - 膜定位: 胞浆 (Cytosol)
**5. 能量与热力学**: ΔG°' ≈ +5 kJ/mol (可逆)
**6. 生理意义**: 将 IPP 异构化为 DMAPP，为后续的萜类合成提供底物
**7. 病理结局**: 
   - IDI1 缺陷: DMAPP 合成减少 → 胆固醇合成障碍 → 发育迟缓, 脂溶性维生素缺乏
**8. 治疗靶点**: 
   - 补充胆固醇: 缓解胆固醇合成缺陷症状
   - 补充脂溶性维生素: 缓解维生素缺乏症状

##### 步骤 ID: CHOL-05
**1. 反应名称**: 法尼基焦磷酸合成 (Farnesyl Pyrophosphate Synthesis)
**2. 化学方程式**: 1.0 DMAPP + 2.0 IPP → 1.0 Farnesyl Pyrophosphate (FPP)
**3. 核心酶信息**: 法尼基焦磷酸合酶 (Farnesyl Pyrophosphate Synthase, FDPS), EC 2.5.1.10, 基因型: FDPS
**4. 动力学与调控**: 
   - Km(IPP) ~0.01-0.05 mM
   - Km(DMAPP) ~0.01-0.05 mM
   - Vmax ~150-300 nmol/min/mg protein
   - 抑制剂: 双膦酸盐类 (Bisphosphonates, 竞争性抑制剂, Ki ~0.1-1.0 μM)
   - 调控: 
     * 受 SREBP-2 调控，SREBP-2 激活时 FDPS 表达上调
     * 受胰岛素调控，胰岛素激活时 FDPS 表达上调
   - 膜定位: 内质网 (Endoplasmic Reticulum)
**5. 能量与热力学**: ΔG°' ≈ -30 kJ/mol (不可逆)
**6. 生理意义**: 合成法尼基焦磷酸 (FPP)，是胆固醇合成和其他萜类化合物合成的关键中间产物
**7. 病理结局**: 
   - FDPS 过度激活: 胆固醇合成增加 → 高胆固醇血症, 动脉粥样硬化
   - FDPS 缺陷: 胆固醇合成减少 → 发育迟缓, 脂溶性维生素缺乏
**8. 治疗靶点**: 
   - 双膦酸盐类药物: 抑制 FDPS 活性，用于治疗骨质疏松和骨转移瘤
   - 他汀类药物: 抑制上游 HMGCR 活性，降低胆固醇合成

##### 步骤 ID: CHOL-06
**1. 反应名称**: 鲨烯合成 (Squalene Synthesis)
**2. 化学方程式**: 2.0 FPP → 1.0 Squalene + 2.0 PPi
**3. 核心酶信息**: 鲨烯合酶 (Squalene Synthase, FDFT1), EC 2.5.1.21, 基因型: FDFT1
**4. 动力学与调控**: 
   - Km(FPP) ~0.01-0.05 mM
   - Vmax ~100-200 nmol/min/mg protein
   - 抑制剂: 某些他汀类药物, 鲨烯合酶抑制剂 (如 zaragozic acid)
   - 调控: 
     * 受 SREBP-2 调控，SREBP-2 激活时 FDFT1 表达上调
     * 受胰岛素调控，胰岛素激活时 FDFT1 表达上调
   - 膜定位: 内质网 (Endoplasmic Reticulum)
**5. 能量与热力学**: ΔG°' ≈ -25 kJ/mol (不可逆)
**6. 生理意义**: 将 FPP 转化为鲨烯，是胆固醇合成的关键步骤
**7. 病理结局**: 
   - FDFT1 过度激活: 胆固醇合成增加 → 高胆固醇血症, 动脉粥样硬化
   - FDFT1 缺陷: 胆固醇合成减少 → 发育迟缓, 脂溶性维生素缺乏
**8. 治疗靶点**: 
   - 鲨烯合酶抑制剂: 抑制 FDFT1 活性，降低胆固醇合成
   - 他汀类药物: 抑制上游 HMGCR 活性，降低胆固醇合成

##### 步骤 ID: CHOL-07
**1. 反应名称**: 鲨烯环化 (Squalene Cyclization)
**2. 化学方程式**: 1.0 Squalene + 3.0 O2 → 1.0 Lanosterol + 3.0 H2O
**3. 核心酶信息**: 鲨烯环氧酶 (Squalene Monooxygenase, SQLE), EC 1.14.14.17, 基因型: SQLE; 羊毛甾醇合成酶 (Lanosterol Synthase, LSS), EC 5.4.99.7, 基因型: LSS
**4. 动力学与调控**: 
   - SQLE Km(Squalene) ~0.01-0.05 mM
   - SQLE Km(NADPH) ~0.01-0.05 mM
   - SQLE Vmax ~50-100 nmol/min/mg protein
   - LSS Km(2,3-Oxidosqualene) ~0.01-0.05 mM
   - LSS Vmax ~50-100 nmol/min/mg protein
   - 抑制剂: 特比萘芬 (Terbinafine, 抑制 SQLE), 唑类抗真菌药物 (抑制 LSS)
   - 调控: 
     * 受 SREBP-2 调控，SREBP-2 激活时 SQLE 和 LSS 表达上调
     * 受胰岛素调控，胰岛素激活时 SQLE 和 LSS 表达上调
   - 膜定位: 内质网 (Endoplasmic Reticulum)
**5. 能量与热力学**: NADPH 消耗: -3, ΔG°' ≈ -50 kJ/mol (不可逆)
**6. 生理意义**: 将鲨烯环化为羊毛甾醇，是胆固醇合成的关键步骤
**7. 病理结局**: 
   - SQLE/LSS 过度激活: 胆固醇合成增加 → 高胆固醇血症, 动脉粥样硬化
   - SQLE/LSS 缺陷: 胆固醇合成减少 → 发育迟缓, 脂溶性维生素缺乏
**8. 治疗靶点**: 
   - 特比萘芬: 抑制 SQLE 活性，用于治疗真菌感染
   - 唑类抗真菌药物: 抑制 LSS 活性，用于治疗真菌感染
   - 他汀类药物: 抑制上游 HMGCR 活性，降低胆固醇合成

##### 步骤 ID: CHOL-08
**1. 反应名称**: 胆固醇合成 (Cholesterol Synthesis)
**2. 化学方程式**: 1.0 Lanosterol → 1.0 Cholesterol (多步反应)
**3. 核心酶信息**: 多种固醇修饰酶，包括 C-14 还原酶 (DHCR14, EC 1.3.1.70, 基因型: DHCR14)、C-8 异构酶 (EBP, EC 5.3.3.5, 基因型: EBP)、C-5 去饱和酶 (SC5D, EC 1.14.13.152, 基因型: SC5D)、7-脱氢胆固醇还原酶 (DHCR7, EC 1.3.1.21, 基因型: DHCR7) 等
**4. 动力学与调控**: 
   - 代表性酶动力学: 
     * DHCR7 Km(7-Dehydrocholesterol) ~0.01-0.05 mM
     * DHCR7 Vmax ~20-50 nmol/min/mg protein
   - 调控: 
     * 受 SREBP-2 调控，SREBP-2 激活时固醇修饰酶表达上调
     * 受胆固醇水平反馈调节，胆固醇高时抑制相关酶表达
     * 受胰岛素调控，胰岛素激活时相关酶表达上调
   - 膜定位: 内质网 (Endoplasmic Reticulum)
**5. 能量与热力学**: 总 NADPH 消耗: -2, ΔG°' ≈ -40 kJ/mol (不可逆)
**6. 生理意义**: 从羊毛甾醇到胆固醇的多步修饰，是胆固醇合成的最终阶段
**7. 病理结局**: 
   - DHCR7 缺陷: 7-脱氢胆固醇积累 → 史密斯-莱姆利-奥皮茨综合征 (SLOS)
   - EBP 缺陷: 固醇代谢障碍 → 康拉迪病 (Conradi-Hünermann-Happle syndrome)
   - 胆固醇合成缺陷: 发育迟缓, 脂溶性维生素缺乏, 神经系统异常
**8. 治疗靶点**: 
   - 补充胆固醇: 缓解胆固醇合成缺陷症状
   - 补充脂溶性维生素: 缓解维生素缺乏症状

##### 步骤 ID: CHOL-09
**1. 反应名称**: 辅酶 Q10 合成 (Coenzyme Q10 Synthesis)
**2. 化学方程式**: 1.0 FPP + 10.0 IPP + 其他前体 → 1.0 CoQ10
**3. 核心酶信息**: 辅酶 Q 合成酶复合体 (CoQ Synthase Complex)
**4. 动力学与调控**: 依赖 FPP 和 IPP 供应
**5. 能量与热力学**: 间接消耗 ATP 和 NADPH
**6. 生理意义**: CoQ10 是电子传递链必需的电子载体，若胆固醇合成被抑制，CoQ10 也会缺乏 → 线粒体功能障碍

##### 步骤 ID: CHOL-10
**1. 反应名称**: 多萜醇合成 (Dolichol Synthesis)
**2. 化学方程式**: 1.0 FPP + n IPP → 1.0 Dolichol (n ≈ 14-18)
**3. 核心酶信息**: 多萜醇合酶 (Dolichol Synthase)
**4. 动力学与调控**: 依赖 FPP 和 IPP 供应
**5. 能量与热力学**: 间接消耗 ATP 和 NADPH
**6. 生理意义**: Dolichol 是糖蛋白合成必需的脂质载体，若胆固醇合成被抑制，Dolichol 也会缺乏 → 糖蛋白合成障碍

### 酮体生成分支 (Ketogenesis)

##### 步骤 ID: CHOL-04
**1. 反应名称**: 酮体生成 (Ketone Body Formation)
**2. 化学方程式**: 2.0 Acetyl-CoA → 1.0 Acetoacetate + 1.0 CoA-SH
**3. 核心酶信息**: 线粒体HMG-CoA合酶 (mHMGCS), HMG-CoA裂解酶
**4. 动力学与调控**: 激活剂: 高浓度乙酰-CoA, 长链脂酰-CoA; 抑制剂: Insulin
**5. 能量与热力学**: ΔG°' ≈ -16 kJ/mol (不可逆)
**6. 空间定位**: 线粒体HMG-CoA用于酮体生成

### 血浆蛋白合成 (Plasma Protein Synthesis)

##### 步骤 ID: SEC-01
**1. 反应名称**: 白蛋白合成 (Albumin Synthesis)
**2. 化学方程式**: 多种氨基酸 → 1.0 Albumin + 多个 H2O
**3. 核心酶信息**: 核糖体、多种合成酶
**4. 动力学与调控**: 受营养状态和激素调控，Insulin 促进合成
**5. 能量与热力学**: 总ATP消耗: -4 per peptide bond

##### 步骤 ID: SEC-02
**1. 反应名称**: 凝血因子合成 (Coagulation Factor Synthesis)
**2. 化学方程式**: 多种氨基酸 → 1.0 Coagulation Factor + 多个 H2O
**3. 核心酶信息**: 核糖体、多种合成酶
**4. 动力学与调控**: 受维生素 K 调控，肝脏特异性合成
**5. 能量与热力学**: 总ATP消耗: -4 per peptide bond

### 药物代谢 (Drug Metabolism)

##### 步骤 ID: DRUG-01
**1. 反应名称**: 细胞色素P450氧化 (Cytochrome P450 Oxidation)
**2. 化学方程式**: 1.0 药物 + 1.0 NADPH + 1.0 O2 → 1.0 氧化代谢物 + 1.0 NADP+ + 1.0 H2O
**3. 核心酶信息**: 细胞色素P450酶系 (Cytochrome P450, CYP), 主要包括 CYP1A2, CYP2C9, CYP2C19, CYP2D6, CYP3A4 等, 基因型: 对应CYP基因
**4. 动力学与调控**: 
   - Km(药物) ~0.1-10 mM (依药物而异)
   - Vmax ~10-100 pmol/min/mg protein
   - 调控: 
     * 受 PXR (Pregnane X Receptor) 和 CAR (Constitutive Androstane Receptor) 诱导
     * 受某些药物的抑制 (如酮康唑抑制 CYP3A4)
   - 膜定位: 内质网 (Endoplasmic Reticulum)
**5. 能量与热力学**: NADPH 消耗: -1, ΔG°' ≈ -20 kJ/mol (不可逆)
**6. 生理意义**: 第一相药物代谢反应，增加药物水溶性，促进排泄
**7. 病理结局**: 
   - CYP 遗传多态性: 药物代谢速率差异 → 药物疗效和毒性变化
   - CYP 诱导: 药物代谢加快 → 治疗失败
   - CYP 抑制: 药物代谢减慢 → 药物积累中毒
**8. 治疗靶点**: 
   - 避免 CYP 抑制剂和诱导剂的联合使用
   - 根据 CYP 基因型调整药物剂量

##### 步骤 ID: DRUG-02
**1. 反应名称**: 葡萄糖醛酸结合 (Glucuronidation)
**2. 化学方程式**: 1.0 药物 + 1.0 UDP-Glucuronic Acid → 1.0 葡萄糖醛酸结合物 + 1.0 UDP
**3. 核心酶信息**: UDP-葡萄糖醛酸转移酶 (UDP-Glucuronosyltransferase, UGT), EC 2.4.1.17, 主要包括 UGT1A1, UGT2B7 等, 基因型: 对应UGT基因
**4. 动力学与调控**: 
   - Km(药物) ~0.1-5 mM (依药物而异)
   - Km(UDP-Glucuronic Acid) ~0.1-1 mM
   - Vmax ~50-200 pmol/min/mg protein
   - 调控: 受 PXR 和 CAR 诱导
   - 膜定位: 内质网 (Endoplasmic Reticulum)
**5. 能量与热力学**: ΔG°' ≈ -15 kJ/mol (不可逆)
**6. 生理意义**: 第二相药物代谢反应，增加药物水溶性，促进排泄
**7. 病理结局**: 
   - UGT1A1 缺陷: 胆红素葡萄糖醛酸结合障碍 → 吉尔伯特综合征, 克里格勒-纳贾尔综合征
   - UGT 诱导: 药物代谢加快 → 治疗失败
**8. 治疗靶点**: 
   - 避免 UGT 诱导剂的联合使用
   - 根据 UGT 基因型调整药物剂量

##### 步骤 ID: DRUG-03
**1. 反应名称**: 硫酸结合 (Sulfation)
**2. 化学方程式**: 1.0 药物 + 1.0 PAPS (3'-Phosphoadenosine-5'-Phosphosulfate) → 1.0 硫酸结合物 + 1.0 PAP (3'-Phosphoadenosine-5'-Phosphate)
**3. 核心酶信息**: 硫酸转移酶 (Sulfotransferase, SULT), EC 2.8.2.1, 主要包括 SULT1A1, SULT2A1 等, 基因型: 对应SULT基因
**4. 动力学与调控**: 
   - Km(药物) ~0.01-1 mM (依药物而异)
   - Km(PAPS) ~0.01-0.1 mM
   - Vmax ~20-100 pmol/min/mg protein
   - 调控: 受激素和药物诱导
   - 膜定位: 胞浆 (Cytosol)
**5. 能量与热力学**: ΔG°' ≈ -20 kJ/mol (不可逆)
**6. 生理意义**: 第二相药物代谢反应，增加药物水溶性，促进排泄
**7. 病理结局**: 
   - SULT 缺陷: 药物代谢减慢 → 药物积累中毒
   - SULT 多态性: 药物代谢速率差异
**8. 治疗靶点**: 
   - 根据 SULT 基因型调整药物剂量

##### 步骤 ID: DRUG-04
**1. 反应名称**: 谷胱甘肽结合 (Glutathione Conjugation)
**2. 化学方程式**: 1.0 亲电药物 + 1.0 GSH (Glutathione) → 1.0 谷胱甘肽结合物
**3. 核心酶信息**: 谷胱甘肽S-转移酶 (Glutathione S-Transferase, GST), EC 2.5.1.18, 主要包括 GSTα, GSTμ, GSTπ 等, 基因型: 对应GST基因
**4. 动力学与调控**: 
   - Km(药物) ~0.01-1 mM (依药物而异)
   - Km(GSH) ~0.1-1 mM
   - Vmax ~50-200 pmol/min/mg protein
   - 调控: 受氧化应激诱导
   - 膜定位: 胞浆 (Cytosol) 和线粒体
**5. 能量与热力学**: ΔG°' ≈ -10 kJ/mol (不可逆)
**6. 生理意义**: 解毒反应，保护细胞免受亲电物质损伤
**7. 病理结局**: 
   - GST 缺陷: 解毒能力下降 → 药物毒性增加, 癌症风险增加
   - GST 多态性: 解毒能力差异
**8. 治疗靶点**: 
   - 补充谷胱甘肽前体 (如N-乙酰半胱氨酸) 增强解毒能力

### 胆红素代谢 (Bilirubin Metabolism)

##### 步骤 ID: BILIRUBIN-01
**1. 反应名称**: 胆红素摄取 (Bilirubin Uptake)
**2. 化学方程式**: 1.0 Bilirubin(blood) → 1.0 Bilirubin(cytosol)
**3. 核心酶信息**: 有机阴离子转运多肽 (Organic Anion Transporting Polypeptides, OATP), 主要包括 OATP1B1, OATP1B3, 基因型: SLCO1B1, SLCO1B3
**4. 动力学与调控**: 
   - Km(Bilirubin) ~0.01-0.1 mM
   - Vmax ~50-100 pmol/min/mg protein
   - 调控: 受核受体调控
   - 膜定位: 肝细胞基底膜 (Basolateral membrane)
**5. 能量与热力学**: 间接消耗 ATP (维持膜电位), ΔG°' ≈ -10 kJ/mol
**6. 生理意义**: 从血液中摄取胆红素，为后续代谢做准备
**7. 病理结局**: 
   - OATP 缺陷: 胆红素摄取障碍 → 高胆红素血症
   - OATP 抑制: 药物性高胆红素血症
**8. 治疗靶点**: 
   - 避免使用 OATP 抑制剂

##### 步骤 ID: BILIRUBIN-02
**1. 反应名称**: 胆红素葡萄糖醛酸结合 (Bilirubin Glucuronidation)
**2. 化学方程式**: 1.0 Bilirubin + 2.0 UDP-Glucuronic Acid → 1.0 Bilirubin Diglucuronide + 2.0 UDP
**3. 核心酶信息**: UDP-葡萄糖醛酸转移酶 1A1 (UGT1A1), EC 2.4.1.17, 基因型: UGT1A1
**4. 动力学与调控**: 
   - Km(Bilirubin) ~0.01-0.05 mM
   - Km(UDP-Glucuronic Acid) ~0.1-1 mM
   - Vmax ~10-50 pmol/min/mg protein
   - 调控: 受 PXR 和 CAR 诱导
   - 膜定位: 内质网 (Endoplasmic Reticulum)
**5. 能量与热力学**: ΔG°' ≈ -30 kJ/mol (不可逆)
**6. 生理意义**: 胆红素代谢的关键步骤，增加胆红素水溶性，促进排泄
**7. 病理结局**: 
   - UGT1A1 缺陷: 克里格勒-纳贾尔综合征 (严重) 或吉尔伯特综合征 (轻度), 非结合胆红素升高
   - UGT1A1 抑制: 药物性高胆红素血症
**8. 治疗靶点**: 
   - 苯巴比妥: 诱导 UGT1A1 表达
   - 光疗: 促进胆红素异构化

##### 步骤 ID: BILIRUBIN-03
**1. 反应名称**: 胆红素排泄 (Bilirubin Excretion)
**2. 化学方程式**: 1.0 Bilirubin Diglucuronide(cytosol) + ATP → 1.0 Bilirubin Diglucuronide(bile) + ADP + Pi
**3. 核心酶信息**: 多药耐药相关蛋白 2 (Multidrug Resistance-Associated Protein 2, MRP2), ABCC2, 基因型: ABCC2
**4. 动力学与调控**: 
   - Km(Bilirubin Diglucuronide) ~0.01-0.1 mM
   - Vmax ~50-100 pmol/min/mg protein
   - 调控: 受核受体调控
   - 膜定位: 肝细胞胆小管膜 (Canalicular membrane)
**5. 能量与热力学**: ATP 消耗: -1, ΔG°' ≈ -30 kJ/mol (不可逆)
**6. 生理意义**: 将结合胆红素泵入胆汁，随粪便排出
**7. 病理结局**: 
   - MRP2 缺陷:  Dubin-Johnson 综合征, 结合胆红素升高
   - MRP2 抑制: 药物性胆汁淤积
**8. 治疗靶点**: 
   - 避免使用 MRP2 抑制剂

### 脂蛋白组装 (Lipoprotein Assembly)

#### VLDL 组装 (VLDL Assembly)

##### 步骤 ID: SEC-03
**1. 反应名称**: ApoB 脂化 (ApoB Lipidation)
**2. 化学方程式**: 1.0 ApoB-100 + n Triglyceride + m Cholesterol + 其他脂质 → 1.0 Lipidated ApoB
**3. 核心酶信息**: 微粒体甘油三酯转移蛋白 (Microsomal Triglyceride Transfer Protein, MTP), EC 2.3.1.155
**4. 动力学与调控**: 
   - MTP Km(Triglyceride) ~0.1-0.5 mM
   - 激活剂: Insulin (通过 PI3K/Akt 通路)
   - 抑制剂: Glucagon, MTP 抑制剂 (如 lomitapide)
   - 底物: ApoB-100, 甘油三酯, 胆固醇, 磷脂
**5. 能量与热力学**: ATP 消耗: -1 (用于脂质合成), ΔG°' ≈ -20 kJ/mol
**6. 生理意义**: 将脂质装载到 ApoB 上，是 VLDL 组装的关键步骤
**7. 逻辑门**: 
   - 若 MTP 被抑制或 ApoB 缺乏，甘油三酯将滞留形成脂滴 → 脂肪肝
   - 若 ApoB 脂化不足，未脂化的 ApoB 被蛋白酶体降解 → VLDL 分泌减少

##### 步骤 ID: SEC-04
**1. 反应名称**: VLDL 成熟 (VLDL Maturation)
**2. 化学方程式**: 1.0 Lipidated ApoB + 其他载脂蛋白 (ApoC, ApoE) → 1.0 Mature VLDL
**3. 核心酶信息**: 多种载脂蛋白组装因子
**4. 动力学与调控**: 受细胞内脂质含量和激素调控
**5. 能量与热力学**: ATP 消耗: -1 (用于载脂蛋白合成和转运)
**6. 生理意义**: 添加 ApoC 和 ApoE，使 VLDL 具备完整功能

##### 步骤 ID: SEC-05
**1. 反应名称**: VLDL 分泌 (VLDL Secretion)
**2. 化学方程式**: 1.0 Mature VLDL (胞内) + ATP → 1.0 Mature VLDL (血浆) + ADP + Pi
**3. 核心酶信息**: 多种转运蛋白，包括 COPII 囊泡
**4. 动力学与调控**: 
   - ATP 消耗: -1 (直接消耗 ATP)
   - 调控: 受细胞内脂质含量、胰岛素水平调控
   - 抑制剂: 某些药物可抑制 VLDL 分泌
**5. 能量与热力学**: ATP 消耗: -1, ΔG°' ≈ -30 kJ/mol (不可逆)
**6. 生理意义**: 将 VLDL 分泌到血浆，运输甘油三酯到外周组织
**7. 逻辑门**: 
   - 若 VLDL 分泌受阻，甘油三酯在肝细胞内堆积 → 脂肪肝
   - 若 VLDL 分泌过多，血浆甘油三酯升高 → 高甘油三酯血症

### 胆汁酸代谢 (Bile Acid Metabolism)

##### 步骤 ID: SEC-05
**1. 反应名称**: 胆汁酸初级合成 (Primary Bile Acid Synthesis)
**2. 化学方程式**: 1.0 Cholesterol → 1.0 Cholic Acid / Chenodeoxycholic Acid (多步反应)
**3. 核心酶信息**: 胆固醇7α-羟化酶 (Cholesterol 7α-Hydroxylase), EC 1.14.13.17, 胆汁酸合成限速酶
**4. 动力学与调控**: Km(Cholesterol) ~0.1-0.5 mM; 激活剂: Insulin; 抑制剂: Bile Acids (反馈抑制)
**5. 能量与热力学**: 总NADPH消耗: -3, 总O2消耗: -3

##### 步骤 ID: SEC-06
**1. 反应名称**: 胆汁酸结合 (Bile Acid Conjugation)
**2. 化学方程式**: 1.0 Bile Acid + 1.0 Glycine / Taurine → 1.0 Conjugated Bile Acid
**3. 核心酶信息**: 胆汁酸-CoA连接酶 (Bile Acid-CoA Ligase), EC 6.2.1.7
**4. 动力学与调控**: Km(Bile Acid) ~0.1-0.5 mM
**5. 能量与热力学**: ATP消耗: -1, ΔG°' ≈ -20 kJ/mol (不可逆)

##### 步骤 ID: SEC-07
**1. 反应名称**: 胆汁酸分泌 (Bile Acid Secretion)
**2. 化学方程式**: 1.0 Conjugated Bile Acid (胞内) → 1.0 Conjugated Bile Acid (胆汁)
**3. 核心酶信息**: 胆汁酸转运蛋白 (Bile Acid Transporters)
**4. 动力学与调控**: 受胆汁酸浓度调控
**5. 能量与热力学**: 需要ATP供能

### 糖蛋白合成 (Glycoprotein Synthesis)

##### 步骤 ID: GLYCO-01
**1. 反应名称**: 多萜醇磷酸化 (Dolichol Phosphorylation)
**2. 化学方程式**: 1.0 Dolichol + 1.0 CTP → 1.0 Dolichol-P + 1.0 CDP
**3. 核心酶信息**: 多萜醇激酶 (Dolichol Kinase, DOLK), EC 2.7.1.108, 基因型: DOLK
**4. 动力学与调控**: 
   - Km(Dolichol) ~0.1-0.5 mM
   - 激活剂: CTP, Mg2+
   - 抑制剂: 多萜醇类似物
   - 膜定位: 内质网膜 (Endoplasmic reticulum membrane)
**5. 能量与热力学**: CTP 消耗: -1, ΔG°' ≈ -30 kJ/mol (不可逆)
**6. 生理意义**: 多萜醇磷酸化生成 Dolichol-P，作为糖基转移的脂质载体
**7. 病理结局**: 
   - DOLK 缺陷: CDG-Ie 型先天性糖基化障碍, 糖蛋白合成减少 → 多系统疾病
   - DOLK 活性降低: 糖蛋白合成受阻 → 免疫功能下降

##### 步骤 ID: GLYCO-02
**1. 反应名称**: 寡糖链组装 (Oligosaccharide Chain Assembly)
**2. 化学方程式**: 1.0 Dolichol-P + 2.0 N-Acetylglucosamine + 9.0 Mannose + 3.0 Glucose → 1.0 Dolichol-P-P-寡糖 + 多个 UDP/GDP
**3. 核心酶信息**: 多种糖基转移酶，包括 ALG1, ALG2, ALG3 等
**4. 动力学与调控**: 
   - 依赖 Dolichol-P 供应
   - 依赖核苷酸糖前体: UDP-GlcNAc, GDP-Man, UDP-Glc
   - 膜定位: 内质网膜 (Endoplasmic reticulum membrane)
**5. 能量与热力学**: 
   - 核苷酸糖合成消耗 ATP: 间接消耗 12 ATP
   - ΔG°' ≈ -40 kJ/mol (不可逆)
**6. 生理意义**: 在 Dolichol-P 上组装寡糖链，为蛋白质 N-糖基化做准备
**7. 病理结局**: 
   - ALG 缺陷: 多种类型的先天性糖基化障碍, 糖蛋白合成异常 → 多系统疾病
   - 核苷酸糖前体缺乏: 糖基化障碍 → 蛋白质功能异常

##### 步骤 ID: GLYCO-03
**1. 反应名称**: 蛋白质N-糖基化 (Protein N-Glycosylation)
**2. 化学方程式**: 1.0 Dolichol-P-P-寡糖 + 1.0 Protein (Asn-X-Ser/Thr) → 1.0 Glycoprotein + 1.0 Dolichol-P-P
**3. 核心酶信息**: 寡糖转移酶复合体 (Oligosaccharyltransferase Complex, OST), EC 2.4.99.18, 基因型: STT3A, STT3B
**4. 动力学与调控**: 
   - 底物: 新合成的蛋白质，含 Asn-X-Ser/Thr 序列
   - 激活剂: 钙离子
   - 抑制剂: tunicamycin (抑制 Dolichol-P 合成)
   - 膜定位: 内质网膜 (Endoplasmic reticulum membrane)
**5. 能量与热力学**: ΔG°' ≈ -20 kJ/mol (不可逆)
**6. 生理意义**: 将寡糖链转移到新合成的蛋白质上，是糖蛋白合成的关键步骤
**7. 病理结局**: 
   - OST 缺陷: CDG-Ih 型先天性糖基化障碍, 糖蛋白合成减少 → 多系统疾病
   - N-糖基化障碍: 蛋白质折叠异常 → 内质网应激

##### 步骤 ID: GLYCO-04
**1. 反应名称**: 糖蛋白成熟 (Glycoprotein Maturation)
**2. 化学方程式**: 1.0 高甘露糖型糖蛋白 → 1.0 复杂型糖蛋白 (多步反应)
**3. 核心酶信息**: 多种糖苷酶和糖基转移酶，包括 ERGIC-53, Golgi 糖苷酶
**4. 动力学与调控**: 
   - 步骤: 去甘露糖 → 加 N-乙酰葡萄糖胺 → 加半乳糖 → 加唾液酸
   - 依赖 Golgi 酸性环境
   - 膜定位: 内质网-高尔基体中间腔室 (ERGIC) 和高尔基体 (Golgi apparatus)
**5. 能量与热力学**: 间接消耗 ATP (维持酸性环境)
**6. 生理意义**: 糖蛋白的寡糖链加工成熟，影响蛋白质的稳定性、折叠和功能
**7. 病理结局**: 
   - 糖基转移酶缺陷: 糖蛋白成熟障碍 → 蛋白质功能异常
   - 高尔基体功能障碍: 糖蛋白分泌受阻 → 多系统疾病

### 脂质合成 (Lipid Synthesis)

#### 磷脂合成 (Phospholipid Synthesis)

##### 步骤 ID: LIPID-01
**1. 反应名称**: 磷脂酸合成 (Phosphatidic Acid Synthesis)
**2. 化学方程式**: 1.0 Glycerol-3-Phosphate + 2.0 Fatty Acyl-CoA → 1.0 Phosphatidic Acid + 2.0 CoA-SH
**3. 核心酶信息**: 甘油-3-磷酸酰基转移酶 (Glycerol-3-Phosphate Acyltransferase, GPAT), EC 2.3.1.15, 基因型: GPAT1, GPAT2
**4. 动力学与调控**: 
   - Km(Glycerol-3-Phosphate) ~0.1-0.5 mM
   - 激活剂: 胰岛素 (转录水平)
   - 抑制剂: 胰高血糖素 (转录水平)
   - 膜定位: 内质网膜 (Endoplasmic reticulum membrane)
**5. 能量与热力学**: 间接消耗 ATP (脂肪酸活化)
**6. 生理意义**: 磷脂合成的第一步，生成磷脂酸
**7. 病理结局**: 
   - GPAT 缺陷: 磷脂合成减少 → 膜结构异常
   - GPAT 过度激活: 脂质合成增加 → 脂肪肝

##### 步骤 ID: LIPID-02
**1. 反应名称**: 磷脂酰胆碱合成 (Phosphatidylcholine Synthesis)
**2. 化学方程式**: 1.0 Phosphatidic Acid + 1.0 CDP-Choline → 1.0 Phosphatidylcholine + 1.0 CMP
**3. 核心酶信息**: 胆碱磷酸胞苷转移酶 (Choline Phosphotransferase, CPT), EC 2.7.8.2, 基因型: CHPT1
**4. 动力学与调控**: 
   - Km(CDP-Choline) ~0.1-0.5 mM
   - 激活剂: 胰岛素 (转录水平)
   - 抑制剂: 胰高血糖素 (转录水平)
   - 膜定位: 内质网膜 (Endoplasmic reticulum membrane)
**5. 能量与热力学**: CTP 消耗: -1 (CDP-Choline 合成), ΔG°' ≈ -30 kJ/mol (不可逆)
**6. 生理意义**: 合成磷脂酰胆碱，是细胞膜的主要成分
**7. 病理结局**: 
   - CHPT1 缺陷: 磷脂酰胆碱合成减少 → 膜结构异常
   - 磷脂酰胆碱缺乏: 脂肪肝, 肝功能障碍

##### 步骤 ID: LIPID-03
**1. 反应名称**: 磷脂酰乙醇胺合成 (Phosphatidylethanolamine Synthesis)
**2. 化学方程式**: 1.0 Phosphatidic Acid + 1.0 CDP-Ethanolamine → 1.0 Phosphatidylethanolamine + 1.0 CMP
**3. 核心酶信息**: 乙醇胺磷酸胞苷转移酶 (Ethanolamine Phosphotransferase, EPT), EC 2.7.8.1, 基因型: CEPT1
**4. 动力学与调控**: 
   - Km(CDP-Ethanolamine) ~0.1-0.5 mM
   - 激活剂: 胰岛素 (转录水平)
   - 抑制剂: 胰高血糖素 (转录水平)
   - 膜定位: 内质网膜 (Endoplasmic reticulum membrane)
**5. 能量与热力学**: CTP 消耗: -1 (CDP-Ethanolamine 合成), ΔG°' ≈ -30 kJ/mol (不可逆)
**6. 生理意义**: 合成磷脂酰乙醇胺，是细胞膜的重要成分
**7. 病理结局**: 
   - CEPT1 缺陷: 磷脂酰乙醇胺合成减少 → 膜结构异常
   - 磷脂酰乙醇胺缺乏: 神经退行性疾病, 肝功能障碍

#### 鞘脂合成 (Sphingolipid Synthesis)

##### 步骤 ID: LIPID-04
**1. 反应名称**: 丝氨酸棕榈酰转移 (Serine Palmitoyltransferase)
**2. 化学方程式**: 1.0 Serine + 1.0 Palmitoyl-CoA → 1.0 3-Ketosphinganine + 1.0 CoA-SH + 1.0 CO2
**3. 核心酶信息**: 丝氨酸棕榈酰转移酶 (Serine Palmitoyltransferase, SPT), EC 2.3.1.50, 基因型: SPTLC1, SPTLC2
**4. 动力学与调控**: 
   - Km(Serine) ~0.1-0.5 mM
   - Km(Palmitoyl-CoA) ~0.01-0.05 mM
   - 激活剂: 胰岛素 (转录水平)
   - 抑制剂: 胰高血糖素 (转录水平)
   - 膜定位: 内质网膜 (Endoplasmic reticulum membrane)
   - 辅因子: 磷酸吡哆醛 (维生素B6)
**5. 能量与热力学**: ΔG°' ≈ -20 kJ/mol (不可逆)
**6. 生理意义**: 鞘脂合成的限速步骤，生成 3-Ketosphinganine
**7. 病理结局**: 
   - SPT 缺陷: 遗传性感觉和自主神经病 1 型, 鞘脂合成减少 → 神经损伤
   - SPT 过度激活: 鞘脂合成增加 → 细胞凋亡

##### 步骤 ID: LIPID-05
**1. 反应名称**: 神经酰胺合成 (Ceramide Synthesis)
**2. 化学方程式**: 1.0 3-Ketosphinganine → 1.0 Sphinganine → 1.0 Dihydroceramide → 1.0 Ceramide (多步反应)
**3. 核心酶信息**: 多种酶，包括 3-酮二氢鞘氨醇还原酶、二氢神经酰胺合酶、二氢神经酰胺去饱和酶
**4. 动力学与调控**: 
   - 依赖 3-Ketosphinganine 供应
   - 激活剂: 胰岛素 (转录水平)
   - 抑制剂: 胰高血糖素 (转录水平)
   - 膜定位: 内质网膜 (Endoplasmic reticulum membrane)
**5. 能量与热力学**: 间接消耗 NADPH (还原反应)
**6. 生理意义**: 合成神经酰胺，是鞘脂的前体，参与细胞信号传导
**7. 病理结局**: 
   - 神经酰胺合成障碍: 鞘脂代谢异常 → 神经退行性疾病
   - 神经酰胺堆积: 细胞凋亡增加 → 肝损伤

### 类固醇激素合成 (Steroid Hormone Synthesis)

##### 步骤 ID: STEROID-01
**1. 反应名称**: 胆固醇侧链裂解 (Cholesterol Side-Chain Cleavage)
**2. 化学方程式**: 1.0 Cholesterol + 3.0 NADPH + 3.0 H+ + 3.0 O2 → 1.0 Pregnenolone + 1.0 Isocaproaldehyde + 3.0 NADP+ + 3.0 H2O
**3. 核心酶信息**: 胆固醇侧链裂解酶 (Cholesterol Side-Chain Cleavage Enzyme, CYP11A1), EC 1.14.15.6, 基因型: CYP11A1
**4. 动力学与调控**: 
   - Km(Cholesterol) ~0.1-0.5 mM
   - 激活剂: ACTH (通过 cAMP/PKA 通路)
   - 抑制剂: 胆固醇转运抑制剂
   - 膜定位: 线粒体内膜 (Inner mitochondrial membrane)
   - 辅因子: NADPH, P450 还原酶
**5. 能量与热力学**: NADPH 消耗: -3, ΔG°' ≈ -80 kJ/mol (不可逆)
**6. 生理意义**: 类固醇激素合成的限速步骤，将胆固醇转化为孕烯醇酮
**7. 病理结局**: 
   - CYP11A1 缺陷: 先天性肾上腺皮质增生症, 类固醇激素合成减少 → 肾上腺功能不全
   - CYP11A1 活性降低: 激素合成受阻 → 内分泌紊乱

##### 步骤 ID: STEROID-02
**1. 反应名称**: 皮质醇合成 (Cortisol Synthesis)
**2. 化学方程式**: 1.0 Pregnenolone → 1.0 Progesterone → 1.0 17α-Hydroxyprogesterone → 1.0 11-Deoxycortisol → 1.0 Cortisol (多步反应)
**3. 核心酶信息**: 多种细胞色素 P450 酶，包括 CYP17A1, CYP21A2, CYP11B1
**4. 动力学与调控**: 
   - 依赖 Pregnenolone 供应
   - 激活剂: ACTH (转录和翻译水平)
   - 抑制剂: 皮质醇 (负反馈抑制)
   - 膜定位: 内质网膜 (Endoplasmic reticulum membrane)
**5. 能量与热力学**: 间接消耗 NADPH (羟化反应)
**6. 生理意义**: 合成皮质醇，参与应激反应和糖代谢调节
**7. 病理结局**: 
   - 酶缺陷: 各种类型的先天性肾上腺皮质增生症, 皮质醇合成减少 → 肾上腺功能不全
   - 皮质醇合成过多: Cushing 综合征, 代谢紊乱

### 维生素代谢 (Vitamin Metabolism)

#### 维生素 A 代谢 (Vitamin A Metabolism)

##### 步骤 ID: VIT-01
**1. 反应名称**: 视黄醇酯化 (Retinol Esterification)
**2. 化学方程式**: 1.0 Retinol + 1.0 Fatty Acyl-CoA → 1.0 Retinyl Ester + 1.0 CoA-SH
**3. 核心酶信息**: 卵磷脂:视黄醇酰基转移酶 (Lecithin:Retinol Acyltransferase, LRAT), EC 2.3.1.135, 基因型: LRAT
**4. 动力学与调控**: 
   - Km(Retinol) ~0.01-0.05 mM
   - 激活剂: 胰岛素 (转录水平)
   - 抑制剂: 胰高血糖素 (转录水平)
   - 膜定位: 内质网膜 (Endoplasmic reticulum membrane)
**5. 能量与热力学**: 间接消耗 ATP (脂肪酸活化)
**6. 生理意义**: 视黄醇酯化生成视黄酯，储存维生素 A
**7. 病理结局**: 
   - LRAT 缺陷: 早发性严重视网膜营养不良, 维生素 A 储存减少 → 夜盲症
   - LRAT 活性降低: 维生素 A 利用障碍 → 视力损害

##### 步骤 ID: VIT-02
**1. 反应名称**: 视黄酸合成 (Retinoic Acid Synthesis)
**2. 化学方程式**: 1.0 Retinol → 1.0 Retinal → 1.0 Retinoic Acid
**3. 核心酶信息**: 视黄醇脱氢酶 (Retinol Dehydrogenase, RDH), EC 1.1.1.105; 视黄醛脱氢酶 (Retinal Dehydrogenase, RALDH), EC 1.2.1.36
**4. 动力学与调控**: 
   - Km(Retinol) ~0.01-0.05 mM
   - 激活剂: 维生素 A 缺乏
   - 抑制剂: 视黄酸 (负反馈抑制)
   - 膜定位: 内质网膜 (Endoplasmic reticulum membrane)
**5. 能量与热力学**: 间接消耗 NAD+ (氧化反应)
**6. 生理意义**: 视黄酸是维生素 A 的活性形式，参与基因转录调控
**7. 病理结局**: 
   - 视黄酸合成障碍: 维生素 A 缺乏症, 生长发育迟缓, 免疫功能下降
   - 视黄酸过多: 维生素 A 中毒, 肝损伤

#### 维生素 D 代谢 (Vitamin D Metabolism)

##### 步骤 ID: VIT-03
**1. 反应名称**: 25-羟维生素 D 合成 (25-Hydroxyvitamin D Synthesis)
**2. 化学方程式**: 1.0 Vitamin D3 + 1.0 NADPH + 1.0 H+ + 1.0 O2 → 1.0 25-Hydroxyvitamin D3 + 1.0 NADP+ + 1.0 H2O
**3. 核心酶信息**: 25-羟化酶 (CYP2R1), EC 1.14.15.18, 基因型: CYP2R1
**4. 动力学与调控**: 
   - Km(Vitamin D3) ~0.01-0.05 mM
   - 激活剂: 维生素 D 缺乏
   - 抑制剂: 25-Hydroxyvitamin D3 (负反馈抑制)
   - 膜定位: 内质网膜 (Endoplasmic reticulum membrane)
   - 辅因子: NADPH, P450 还原酶
**5. 能量与热力学**: NADPH 消耗: -1, ΔG°' ≈ -20 kJ/mol (不可逆)
**6. 生理意义**: 维生素 D 代谢的第一步，生成 25-Hydroxyvitamin D3
**7. 病理结局**: 
   - CYP2R1 缺陷: 维生素 D 依赖性佝偻病 1B 型, 维生素 D 活化障碍 → 佝偻病
   - CYP2R1 活性降低: 维生素 D 利用障碍 → 骨代谢异常

##### 步骤 ID: VIT-04
**1. 反应名称**: 1,25-二羟维生素 D 合成 (1,25-Dihydroxyvitamin D Synthesis)
**2. 化学方程式**: 1.0 25-Hydroxyvitamin D3 + 1.0 NADPH + 1.0 H+ + 1.0 O2 → 1.0 1,25-Dihydroxyvitamin D3 + 1.0 NADP+ + 1.0 H2O
**3. 核心酶信息**: 1α-羟化酶 (CYP27B1), EC 1.14.15.16, 基因型: CYP27B1
**4. 动力学与调控**: 
   - Km(25-Hydroxyvitamin D3) ~0.01-0.05 mM
   - 激活剂: PTH (甲状旁腺激素), 低血钙
   - 抑制剂: 1,25-Dihydroxyvitamin D3 (负反馈抑制), FGF23
   - 膜定位: 线粒体内膜 (Inner mitochondrial membrane)
   - 辅因子: NADPH, P450 还原酶
**5. 能量与热力学**: NADPH 消耗: -1, ΔG°' ≈ -20 kJ/mol (不可逆)
**6. 生理意义**: 维生素 D 代谢的限速步骤，生成活性形式 1,25-Dihydroxyvitamin D3
**7. 病理结局**: 
   - CYP27B1 缺陷: 维生素 D 依赖性佝偻病 1A 型, 活性维生素 D 合成减少 → 佝偻病
   - CYP27B1 过度激活: 活性维生素 D 过多 → 高钙血症

## 模块 E：信号调控系统（指挥部）

### 激素感应 (Hormone Sensing)

##### 步骤 ID: SIG-01
**1. 反应名称**: 胰岛素信号通路 (Insulin Signaling Pathway)
**2. 化学方程式**: 1.0 Insulin + 1.0 Insulin Receptor → 1.0 Activated Insulin Receptor
**3. 核心酶信息**: 胰岛素受体 (Insulin Receptor), EC 2.7.10.1
**4. 动力学与调控**: Km(Insulin) ~0.1-1.0 nM; 激活下游PI3K/Akt通路
**5. 能量与热力学**: 不需要直接能量输入

##### 步骤 ID: SIG-02
**1. 反应名称**: 胰高血糖素信号通路 (Glucagon Signaling Pathway)
**2. 化学方程式**: 1.0 Glucagon + 1.0 Glucagon Receptor → 1.0 Activated Glucagon Receptor
**3. 核心酶信息**: 胰高血糖素受体 (Glucagon Receptor), G蛋白偶联受体
**4. 动力学与调控**: Km(Glucagon) ~1-10 nM; 激活下游cAMP/PKA通路
**5. 能量与热力学**: 不需要直接能量输入

##### 步骤 ID: SIG-03
**1. 反应名称**: 肾上腺素信号通路 (Epinephrine Signaling Pathway)
**2. 化学方程式**: 1.0 Epinephrine + 1.0 β-Adrenergic Receptor → 1.0 Activated β-Adrenergic Receptor
**3. 核心酶信息**: β-肾上腺素受体 (β-Adrenergic Receptor), G蛋白偶联受体
**4. 动力学与调控**: Km(Epinephrine) ~1-10 nM; 激活下游cAMP/PKA通路
**5. 能量与热力学**: 不需要直接能量输入

### 能量状态感应 (Energy Status Sensing)

##### 步骤 ID: SIG-04
**1. 反应名称**: AMPK激活 (AMPK Activation)
**2. 化学方程式**: 1.0 AMP + 1.0 AMPK (无活性) → 1.0 AMPK (活性) + 1.0 ADP
**3. 核心酶信息**: AMP激活的蛋白激酶 (AMP-Activated Protein Kinase), EC 2.7.11.31
**4. 动力学与调控**: 激活剂: AMP, ADP; 抑制剂: ATP
**5. 能量与热力学**: 不需要直接能量输入

##### 步骤 ID: SIG-05
**1. 反应名称**: mTOR激活 (mTOR Activation)
**2. 化学方程式**: 1.0 ATP + 1.0 mTOR (无活性) → 1.0 mTOR (活性) + 1.0 ADP
**3. 核心酶信息**: 哺乳动物雷帕霉素靶蛋白 (Mammalian Target of Rapamycin), EC 2.7.11.1
**4. 动力学与调控**: 激活剂: Insulin, 氨基酸, 高ATP/AMP比率
**5. 能量与热力学**: ATP消耗: -1

### 细胞命运判决 (Cell Fate Decisions)

#### 凋亡 (Apoptosis)

##### 步骤 ID: FAT-01
**1. 反应名称**: 线粒体凋亡通路 (Mitochondrial Apoptosis Pathway)
**2. 化学方程式**: 
   - 触发: Cyt c (线粒体) → Cyt c (胞浆) [膜通透性增加]
   - 级联: Cyt c + Apaf-1 + ATP → Apoptosome
   - 执行: Apoptosome + Pro-caspase-9 → Caspase-9 (活性)
   - 执行: Caspase-9 + Pro-caspase-3 → Caspase-3 (活性)
   - 结果: Caspase-3 + 细胞成分 → 凋亡小体
**3. 核心酶信息**: 
   - 线粒体通透性转换孔 (MPTP)
   - 凋亡蛋白酶激活因子-1 (Apaf-1)
   - Caspase-9, Caspase-3
**4. 动力学与调控**: 
   - 触发条件: Cyt c 释放 + ATP 尚存 (> 1 mM)
   - 激活剂: ROS, DNA 损伤, 毒物
   - 抑制剂: Bcl-2, Bcl-xL (抗凋亡蛋白)
**5. 能量与热力学**: ATP 消耗: -1 (用于凋亡小体形成), ΔG°' ≈ -50 kJ/mol (不可逆)
**6. 生理意义**: 程序性细胞死亡，有序清除受损细胞，不引发炎症反应
**7. 逻辑门**: 
   - 若 ATP > 1 mM 且 Cyt c 释放 → 凋亡 (有序死亡)
   - 若 ATP < 1 mM 且 Cyt c 释放 → 坏死 (无序死亡)

#### 坏死 (Necrosis)

##### 步骤 ID: FAT-02
**1. 反应名称**: 能量耗尽性坏死 (Energy Depletion Necrosis)
**2. 化学方程式**: 
   - 触发: ATP < 0.1 mM + ROS 爆表 (> 10 μM)
   - 膜破裂: 细胞膜完整性丧失 → 细胞内容物外泄
   - 炎症: DAMPs (Damage-Associated Molecular Patterns) 释放 → 免疫细胞激活
**3. 核心酶信息**: 
   - 无特定酶，是能量耗尽的被动过程
   - 涉及离子泵失效 (Na+/K+-ATPase, Ca2+-ATPase)
**4. 动力学与调控**: 
   - 触发条件: ROS 爆表 + ATP 耗尽 (< 0.1 mM)
   - 机制: 无法维持离子泵 → 细胞肿胀 → 膜破裂
   - 促进因素: 氧化应激, 线粒体功能障碍, 毒物堆积
**5. 能量与热力学**: 无能量消耗 (被动过程), ΔG°' ≈ 0 kJ/mol
**6. 生理意义**: 无序细胞死亡，释放炎症因子 (DAMPs)，引发免疫反应和周围组织损伤
**7. 逻辑门**: 
   - 若 ATP < 0.1 mM 且 ROS > 10 μM → 坏死 (无序死亡)
   - 后果: 膜破裂 → DAMPs 释放 → 免疫反应 → 肝损伤加重
   - 预防: 维持 ATP 水平，控制 ROS 生成

### 炎症信号 (Inflammatory Signaling)

##### 步骤 ID: SIG-06
**1. 反应名称**: TNF-α信号通路 (TNF-α Signaling Pathway)
**2. 化学方程式**: 1.0 TNF-α + 1.0 TNF Receptor → 1.0 Activated TNF Receptor
**3. 核心酶信息**: TNF受体 (TNF Receptor), 死亡受体家族
**4. 动力学与调控**: Km(TNF-α) ~0.1-1.0 nM; 激活下游NF-κB通路
**5. 能量与热力学**: 不需要直接能量输入

##### 步骤 ID: SIG-07
**1. 反应名称**: IL-6信号通路 (IL-6 Signaling Pathway)
**2. 化学方程式**: 1.0 IL-6 + 1.0 IL-6 Receptor → 1.0 Activated IL-6 Receptor
**3. 核心酶信息**: IL-6受体 (IL-6 Receptor), 细胞因子受体家族
**4. 动力学与调控**: Km(IL-6) ~0.1-1.0 nM; 激活下游JAK/STAT通路
**5. 能量与热力学**: 不需要直接能量输入

##### 步骤 ID: SIG-08
**1. 反应名称**: 急性期反应蛋白合成 (Acute Phase Protein Synthesis)
**2. 化学方程式**: 多种氨基酸 → 1.0 Acute Phase Protein + 多个 H2O
**3. 核心酶信息**: 核糖体、多种合成酶
**4. 动力学与调控**: 受TNF-α、IL-6调控
**5. 能量与热力学**: 总ATP消耗: -4 per peptide bond

### 核受体信号通路 (Nuclear Receptor Signaling)

##### 步骤 ID: NUC-01
**1. 反应名称**: FXR信号通路 (Farnesoid X Receptor Signaling)
**2. 化学方程式**: 1.0 胆汁酸 + 1.0 FXR (胞浆) → 1.0 FXR-胆汁酸复合物 (核内) → 1.0 激活的转录复合物
**3. 核心酶信息**: 法尼醇X受体 (Farnesoid X Receptor, NR1H4), 基因型: NR1H4
**4. 动力学与调控**: 
   - Km(胆汁酸) ~0.1-1.0 μM
   - 配体: 鹅去氧胆酸、熊去氧胆酸等
   - 调控: 激活下游靶基因如 BSEP, SHP, FGF19
   - 膜定位: 胞浆和细胞核
**5. 能量与热力学**: 不需要直接能量输入
**6. 生理意义**: 调控胆汁酸稳态、胆固醇代谢和糖代谢
**7. 病理结局**: 
   - FXR 缺陷: 胆汁酸代谢紊乱 → 胆汁淤积, 脂肪肝
   - FXR 激活不足: 胆固醇代谢异常 → 高胆固醇血症
**8. 治疗靶点**: 
   - FXR 激动剂: 奥贝胆酸，治疗原发性胆汁性胆管炎

##### 步骤 ID: NUC-02
**1. 反应名称**: LXR信号通路 (Liver X Receptor Signaling)
**2. 化学方程式**: 1.0 氧化固醇 + 1.0 LXR (胞浆) → 1.0 LXR-氧化固醇复合物 (核内) → 1.0 激活的转录复合物
**3. 核心酶信息**: 肝脏X受体 (Liver X Receptor, NR1H2/3), 基因型: NR1H2, NR1H3
**4. 动力学与调控**: 
   - Km(氧化固醇) ~0.1-1.0 μM
   - 配体: 22(R)-羟胆固醇、24(S)-羟胆固醇等
   - 调控: 激活下游靶基因如 ABCA1, ABCG1, SREBP-1c
   - 膜定位: 胞浆和细胞核
**5. 能量与热力学**: 不需要直接能量输入
**6. 生理意义**: 调控胆固醇逆向转运、脂肪酸合成和炎症反应
**7. 病理结局**: 
   - LXR 缺陷: 胆固醇代谢紊乱 → 动脉粥样硬化, 脂肪肝
   - LXR 过度激活: 脂肪酸合成增加 → 脂肪肝
**8. 治疗靶点**: 
   - LXR 激动剂: 调控胆固醇代谢，治疗动脉粥样硬化

##### 步骤 ID: NUC-03
**1. 反应名称**: PPARα信号通路 (Peroxisome Proliferator-Activated Receptor α Signaling)
**2. 化学方程式**: 1.0 脂肪酸/药物 + 1.0 PPARα (胞浆) → 1.0 PPARα-配体复合物 (核内) → 1.0 激活的转录复合物
**3. 核心酶信息**: 过氧化物酶体增殖物激活受体α (Peroxisome Proliferator-Activated Receptor α, NR1C1), 基因型: PPARA
**4. 动力学与调控**: 
   - Km(脂肪酸) ~0.1-1.0 μM
   - 配体: 脂肪酸、贝特类药物等
   - 调控: 激活下游靶基因如 CPT1A, ACOX1, PPARGC1A
   - 膜定位: 胞浆和细胞核
**5. 能量与热力学**: 不需要直接能量输入
**6. 生理意义**: 调控脂肪酸氧化、酮体生成和能量代谢
**7. 病理结局**: 
   - PPARα 缺陷: 脂肪酸氧化障碍 → 脂肪肝, 高甘油三酯血症
   - PPARα 过度激活: 脂肪酸氧化增加 → 能量消耗过多
**8. 治疗靶点**: 
   - PPARα 激动剂: 贝特类药物，治疗高甘油三酯血症

### 氧化应激信号通路 (Oxidative Stress Signaling)

##### 步骤 ID: OX-01
**1. 反应名称**: Nrf2信号通路 (Nuclear Factor Erythroid 2-Related Factor 2 Signaling)
**2. 化学方程式**: 1.0 ROS + 1.0 Keap1-Nrf2 复合物 (胞浆) → 1.0 Nrf2 (游离) → 1.0 Nrf2 (核内) → 1.0 激活的转录复合物
**3. 核心酶信息**: 核因子 erythroid 2 相关因子 2 (Nuclear Factor Erythroid 2-Related Factor 2), 基因型: NFE2L2
**4. 动力学与调控**: 
   - 激活剂: ROS, 亲电物质, 某些药物 (如二甲双胍)
   - 抑制剂: Keap1 (正常状态下抑制Nrf2)
   - 调控: 激活下游靶基因如 NQO1, HO-1, GCL
   - 膜定位: 胞浆和细胞核
**5. 能量与热力学**: 不需要直接能量输入
**6. 生理意义**: 调控抗氧化酶表达，保护细胞免受氧化应激损伤
**7. 病理结局**: 
   - Nrf2 缺陷: 抗氧化能力下降 → 氧化应激损伤, 肝脏疾病
   - Nrf2 过度激活: 可能促进某些肿瘤生长
**8. 治疗靶点**: 
   - Nrf2 激活剂: 叔丁基对苯二酚 (tBHQ)、萝卜硫素，治疗氧化应激相关疾病

### 自噬信号通路 (Autophagy Signaling)

##### 步骤 ID: AUT-01
**1. 反应名称**: 自噬起始 (Autophagy Initiation)
**2. 化学方程式**: 1.0 能量应激/营养缺乏 + 1.0 ULK1 复合物 → 1.0 激活的 ULK1 复合物 → 1.0 自噬前体结构
**3. 核心酶信息**: ULK1 复合物 (Unc-51 Like Autophagy Activating Kinase 1 Complex), 基因型: ULK1
**4. 动力学与调控**: 
   - 激活剂: AMPK (直接磷酸化激活), 营养缺乏
   - 抑制剂: mTOR (直接磷酸化抑制)
   - 时间尺度: 分钟级反应
**5. 能量与热力学**: ATP 消耗: -1 (ULK1 激活需磷酸化)
**6. 生理意义**: 启动自噬过程，清除受损细胞器和蛋白质 aggregates
**7. 病理结局**: 
   - 自噬缺陷: 蛋白质和细胞器积累 → 肝细胞损伤, 脂肪肝
   - 自噬过度: 细胞成分过度降解 → 细胞死亡
**8. 治疗靶点**: 
   - 自噬诱导剂: 雷帕霉素、二甲双胍，治疗肝脏疾病

### 肝脏再生信号通路 (Liver Regeneration Signaling)

##### 步骤 ID: REGEN-01
**1. 反应名称**: HGF/c-Met信号通路 (Hepatocyte Growth Factor/c-Met Signaling)
**2. 化学方程式**: 1.0 HGF + 1.0 c-Met 受体 → 1.0 激活的 c-Met 受体 → 1.0 激活的下游信号
**3. 核心酶信息**: 肝细胞生长因子受体 (c-Met), EC 2.7.10.1, 基因型: MET
**4. 动力学与调控**: 
   - Km(HGF) ~0.1-1.0 nM
   - 激活剂: HGF (由肝脏星状细胞分泌)
   - 调控: 激活下游信号如 ERK, PI3K/Akt, STAT3
   - 时间尺度: 分钟到小时级反应
**5. 能量与热力学**: ATP 消耗: -1 (受体自身磷酸化)
**6. 生理意义**: 调控肝细胞增殖、迁移和存活，促进肝脏再生
**7. 病理结局**: 
   - c-Met 缺陷: 肝脏再生能力下降 → 肝衰竭
   - c-Met 过度激活: 可能促进肝细胞癌发生
**8. 治疗靶点**: 
   - HGF 模拟物: 促进肝脏再生
   - c-Met 抑制剂: 治疗肝细胞癌

### 内质网应激信号通路 (Endoplasmic Reticulum Stress Signaling)

##### 步骤 ID: ER-01
**1. 反应名称**: 未折叠蛋白反应 (Unfolded Protein Response, UPR)
**2. 化学方程式**: 1.0 未折叠蛋白积累 (内质网) → 1.0 激活的 UPR 传感器 (IRE1α, PERK, ATF6) → 1.0 激活的下游信号
**3. 核心酶信息**: 
   - IRE1α (Inositol-Requiring Enzyme 1α), 基因型: ERN1
   - PERK (Protein Kinase R-Like Endoplasmic Reticulum Kinase), 基因型: EIF2AK3
   - ATF6 (Activating Transcription Factor 6), 基因型: ATF6
**4. 动力学与调控**: 
   - 激活剂: 未折叠蛋白积累、钙离子失衡、氧化应激
   - 调控: 
     * IRE1α 通路: 激活 XBP1 转录因子
     * PERK 通路: 抑制蛋白质合成，激活 ATF4
     * ATF6 通路: 激活 ER 应激相关基因
   - 时间尺度: 分钟到小时级反应
**5. 能量与热力学**: ATP 消耗: -1 (激酶激活)
**6. 生理意义**: 缓解内质网应激，恢复蛋白质折叠 homeostasis
**7. 病理结局**: 
   - UPR 缺陷: 内质网应激无法缓解 → 细胞凋亡, 肝脏疾病
   - UPR 过度激活: 持续 ER 应激 → 慢性炎症, 肝硬化
**8. 治疗靶点**: 
   - ER 应激抑制剂: 牛磺熊去氧胆酸 (TUDCA)，治疗内质网应激相关疾病

### 激酶级联反应 (Kinase Cascades)

#### MAPK 通路 (丝裂原活化蛋白激酶通路)

##### 步骤 ID: KIN-01
**1. 反应名称**: ERK1/2 激活 (ERK1/2 Activation)
**2. 化学方程式**: 
   - 受体激活: Growth Factor + RTK → 激活的 RTK
   - 级联激活: 激活的 RTK → Grb2 → SOS → Ras-GTP
   - 级联激活: Ras-GTP + Raf → 激活的 Raf
   - 级联激活: 激活的 Raf + MEK1/2 → 激活的 MEK1/2
   - 级联激活: 激活的 MEK1/2 + ERK1/2 → 激活的 ERK1/2
**3. 核心酶信息**: 
   - Raf (EC 2.7.11.1), MEK1/2 (EC 2.7.12.2), ERK1/2 (EC 2.7.11.1)
**4. 动力学与调控**: 
   - 激活剂: EGF, IGF-1, 胰岛素
   - 抑制剂: U0126 (MEK抑制剂), PD98059 (MEK抑制剂)
   - 时间尺度: 毫秒到分钟级反应
**5. 能量与热力学**: ATP消耗: -2 (Raf和MEK激活各需1分子ATP)
**6. 功能说明**: 
   - 调控细胞增殖、分化和存活
   - 上调 c-Fos、c-Jun 等转录因子
   - 参与肝脏再生和修复过程
**7. 生理意义**: 生长因子刺激下的细胞响应，促进肝脏组织修复

##### 步骤 ID: KIN-02
**1. 反应名称**: JNK 激活 (JNK Activation)
**2. 化学方程式**: 
   - 应激刺激 → 激活的 MKK4/7
   - 激活的 MKK4/7 + JNK → 激活的 JNK
**3. 核心酶信息**: 
   - MKK4/7 (EC 2.7.12.2), JNK (EC 2.7.11.1)
**4. 动力学与调控**: 
   - 激活剂: 应激刺激 (ROS, 渗透压变化, 细胞因子)
   - 抑制剂: SP600125 (JNK抑制剂)
   - 时间尺度: 分钟级反应
**5. 能量与热力学**: ATP消耗: -1 (MKK激活需1分子ATP)
**6. 功能说明**: 
   - 调控细胞应激响应和凋亡
   - 参与炎症信号通路
   - 影响肝脏损伤和修复
**7. 生理意义**: 细胞应激状态下的适应性反应，在肝脏损伤中起重要作用

#### PI3K/Akt 通路

##### 步骤 ID: KIN-03
**1. 反应名称**: PI3K/Akt 激活 (PI3K/Akt Activation)
**2. 化学方程式**: 
   - 受体激活: Insulin + Insulin Receptor → 激活的 Insulin Receptor
   - 级联激活: 激活的 Insulin Receptor → IRS → PI3K
   - 级联激活: PI3K + PIP2 → PIP3
   - 级联激活: PIP3 + PDK1 + Akt → 激活的 Akt
**3. 核心酶信息**: 
   - PI3K (EC 2.7.1.137), PDK1 (EC 2.7.11.1), Akt (EC 2.7.11.1)
**4. 动力学与调控**: 
   - 激活剂: 胰岛素、IGF-1
   - 抑制剂: Wortmannin (PI3K抑制剂), LY294002 (PI3K抑制剂)
   - 时间尺度: 秒到分钟级反应
**5. 能量与热力学**: ATP消耗: -2 (PI3K和Akt激活各需1分子ATP)
**6. 功能说明**: 
   - 调控细胞生长、存活和代谢
   - 促进糖原合成和蛋白质合成
   - 抑制细胞凋亡
**7. 生理意义**: 胰岛素信号的主要传导通路，在肝脏代谢调节中起核心作用

#### AMPK 通路

##### 步骤 ID: KIN-04
**1. 反应名称**: AMPK 激活 (AMPK Activation)
**2. 化学方程式**: 
   - 能量应激: AMP/ATP 比率升高 → LKB1 激活
   - 级联激活: LKB1 + AMPK → 激活的 AMPK
   - 或: CaMKKβ + Ca²⁺ → 激活的 CaMKKβ
   - 级联激活: 激活的 CaMKKβ + AMPK → 激活的 AMPK
**3. 核心酶信息**: 
   - LKB1 (EC 2.7.11.1), CaMKKβ (EC 2.7.11.17), AMPK (EC 2.7.11.31)
**4. 动力学与调控**: 
   - 激活剂: 高AMP/ATP比率, 运动, 二甲双胍
   - 抑制剂: Compound C (AMPK抑制剂)
   - 时间尺度: 分钟级反应
**5. 能量与热力学**: ATP消耗: -1 (AMPK激活需1分子ATP)
**6. 功能说明**: 
   - 调控能量代谢，促进脂肪酸氧化
   - 抑制蛋白质合成和脂肪酸合成
   - 增强胰岛素敏感性
**7. 生理意义**: 细胞能量状态的关键传感器，在能量应激时维持代谢平衡

### 信号通路交叉对话 (Signaling Cross-talk)

#### 胰岛素-mTOR-AMPK 相互作用

##### 步骤 ID: CROS-01
**1. 反应名称**: 胰岛素-mTOR 激活轴 (Insulin-mTOR Activation Axis)
**2. 化学方程式**: 
   - 胰岛素信号: Insulin → 激活的 Insulin Receptor → 激活的 PI3K/Akt
   - mTOR 激活: 激活的 Akt + TSC2 → 抑制的 TSC2
   - mTOR 激活: 抑制的 TSC2 + Rheb-GTP → 激活的 mTORC1
**3. 核心酶信息**: 
   - Akt (EC 2.7.11.1), TSC2, Rheb, mTORC1 (EC 2.7.11.1)
**4. 动力学与调控**: 
   - 激活剂: 胰岛素、氨基酸、生长因子
   - 抑制剂: rapamycin (mTOR抑制剂), Torin1 (mTOR抑制剂)
   - 时间尺度: 分钟级反应
**5. 能量与热力学**: ATP消耗: -1 (Akt磷酸化TSC2)
**6. 功能说明**: 
   - 促进蛋白质合成和细胞生长
   - 抑制自噬
   - 调控脂质合成
**7. 生理意义**: 营养充足时促进细胞生长和合成代谢，是胰岛素信号的重要下游效应器

##### 步骤 ID: CROS-02
**1. 反应名称**: AMPK-mTOR 抑制轴 (AMPK-mTOR Inhibition Axis)
**2. 化学方程式**: 
   - 能量应激: 高AMP/ATP比率 → 激活的 AMPK
   - mTOR 抑制: 激活的 AMPK + TSC2 → 激活的 TSC2
   - mTOR 抑制: 激活的 TSC2 + Rheb-GTP → 抑制的 mTORC1
   - 或: 激活的 AMPK + raptor → 抑制的 mTORC1
**3. 核心酶信息**: 
   - AMPK (EC 2.7.11.31), TSC2, raptor, mTORC1
**4. 动力学与调控**: 
   - 激活剂: 能量应激、二甲双胍、运动
   - 抑制剂: Compound C (AMPK抑制剂)
   - 时间尺度: 分钟级反应
**5. 能量与热力学**: ATP消耗: -1 (AMPK磷酸化TSC2或raptor)
**6. 功能说明**: 
   - 抑制蛋白质合成和细胞生长
   - 促进自噬
   - 调控能量代谢
**7. 生理意义**: 能量不足时抑制合成代谢，促进分解代谢，维持能量平衡

##### 步骤 ID: CROS-03
**1. 反应名称**: 胰岛素-AMPK 相互调节 (Insulin-AMPK Mutual Regulation)
**2. 化学方程式**: 
   - 短期效应: 胰岛素 → 激活的 Akt → 抑制的 AMPK
   - 长期效应: 胰岛素抵抗 → 激活的 JNK/IKK → 抑制的 IRS → 抑制的 PI3K/Akt → 激活的 AMPK
**3. 核心酶信息**: 
   - Akt (EC 2.7.11.1), AMPK (EC 2.7.11.31), JNK (EC 2.7.11.1), IKK (EC 2.7.11.1)
**4. 动力学与调控**: 
   - 短期: 胰岛素抑制AMPK活性
   - 长期: 胰岛素抵抗时AMPK活性增加
   - 时间尺度: 短期(分钟级)到长期(小时/天级)
**5. 能量与热力学**: 短期: ATP消耗 -1 (Akt磷酸化AMPK)
**6. 功能说明**: 
   - 短期: 胰岛素促进合成代谢，抑制分解代谢
   - 长期: 胰岛素抵抗时AMPK试图恢复代谢平衡
**7. 生理意义**: 细胞根据胰岛素信号和能量状态动态调整代谢策略

#### 炎症-代谢信号交叉对话

##### 步骤 ID: CROS-04
**1. 反应名称**: NF-κB-AMPK 相互作用 (NF-κB-AMPK Interaction)
**2. 化学方程式**: 
   - 炎症激活: TNF-α → 激活的 IKK → 激活的 NF-κB
   - 炎症抑制: 激活的 AMPK → 抑制的 IKK → 抑制的 NF-κB
   - 代谢影响: 激活的 NF-κB → 抑制的 AMPK → 代谢紊乱
**3. 核心酶信息**: 
   - IKK (EC 2.7.11.1), NF-κB, AMPK (EC 2.7.11.31)
**4. 动力学与调控**: 
   - 激活剂: 细胞因子、LPS
   - 抑制剂: 抗炎药物、AMPK激活剂
   - 时间尺度: 分钟到小时级反应
**5. 能量与热力学**: 无直接能量消耗
**6. 功能说明**: 
   - 炎症状态下抑制AMPK活性，导致代谢紊乱
   - AMPK激活可减轻炎症反应
**7. 生理意义**: 炎症与代谢之间的双向调节，在脂肪肝和胰岛素抵抗中起重要作用

### 病理状态下的信号调控异常 (Pathological Signaling Dysregulation)

#### 脂肪肝 (Fatty Liver Disease)

##### 步骤 ID: PATH-01
**1. 反应名称**: 脂肪肝中的胰岛素抵抗信号 (Insulin Resistance Signaling in Fatty Liver)
**2. 化学方程式**: 
   - 脂毒性: 过量FFA → 激活的 JNK/IKK → 抑制的 IRS
   - 胰岛素抵抗: 抑制的 IRS → 抑制的 PI3K/Akt → 激活的 GSK3β
   - 糖代谢异常: 激活的 GSK3β → 抑制的 glycogen synthase → 糖原合成减少
**3. 核心酶信息**: 
   - JNK (EC 2.7.11.1), IKK (EC 2.7.11.1), IRS, PI3K (EC 2.7.1.137), Akt (EC 2.7.11.1), GSK3β (EC 2.7.11.26)
**4. 动力学与调控**: 
   - 触发: FFA > 1.0 mM
   - 促进因素: 氧化应激、炎症细胞因子
   - 时间尺度: 小时到天级反应
**5. 能量与热力学**: 无直接能量消耗
**6. 功能说明**: 
   - 胰岛素信号传导受阻
   - 糖原合成减少，糖异生增加
   - 脂质合成持续激活
**7. 病理意义**: 脂肪肝进展为非酒精性脂肪肝炎(NASH)的关键机制

##### 步骤 ID: PATH-02
**1. 反应名称**: 脂肪肝中的mTOR过度激活 (mTOR Hyperactivation in Fatty Liver)
**2. 化学方程式**: 
   - 营养过剩: 高胰岛素 + 高氨基酸 → 过度激活的 mTORC1
   - 自噬抑制: 过度激活的 mTORC1 → 抑制的自噬
   - 脂质堆积: 抑制的自噬 + 增强的脂质合成 → 脂肪肝加重
**3. 核心酶信息**: 
   - mTORC1 (EC 2.7.11.1), ULK1 (EC 2.7.11.1)
**4. 动力学与调控**: 
   - 触发: 胰岛素 > 10 nM 且 氨基酸 > 正常水平2倍
   - 促进因素: 高碳水化合物饮食
   - 时间尺度: 天到周级反应
**5. 能量与热力学**: ATP消耗增加
**6. 功能说明**: 
   - 蛋白质合成增加
   - 自噬清除功能下降
   - 脂质代谢紊乱
**7. 病理意义**: 脂肪肝进展和胰岛素抵抗加重的重要因素

#### 药物性肝损伤 (Drug-Induced Liver Injury)

##### 步骤 ID: PATH-03
**1. 反应名称**: 药物代谢激活的氧化应激信号 (Oxidative Stress Signaling in DILI)
**2. 化学方程式**: 
   - 药物代谢: 药物 + CYP450 → 活性代谢物
   - 氧化应激: 活性代谢物 → ROS 生成增加
   - 应激信号: 增加的 ROS → 激活的 JNK/p38 → 激活的 ASK1
   - 细胞损伤: 激活的 ASK1 → 激活的 caspases → 细胞凋亡/坏死
**3. 核心酶信息**: 
   - CYP450 酶系, ASK1 (EC 2.7.11.1), JNK (EC 2.7.11.1), p38 (EC 2.7.11.24), caspases
**4. 动力学与调控**: 
   - 触发: 药物浓度 > 治疗窗口
   - 促进因素: 药物代谢酶多态性、线粒体功能障碍
   - 时间尺度: 小时到天级反应
**5. 能量与热力学**: 无直接能量消耗，但ROS消耗抗氧化物质
**6. 功能说明**: 
   - 细胞氧化还原状态失衡
   - 线粒体功能损伤
   - 细胞死亡途径激活
**7. 病理意义**: 药物性肝损伤的主要发病机制之一

##### 步骤 ID: PATH-04
**1. 反应名称**: 药物性肝损伤中的炎症信号激活 (Inflammatory Signaling Activation in DILI)
**2. 化学方程式**: 
   - 细胞损伤: 药物/活性代谢物 → 肝细胞损伤
   - DAMPs释放: 肝细胞损伤 → DAMPs 释放
   - 炎症激活: DAMPs + 肝Kupffer细胞 → 激活的 Kupffer细胞
   - 细胞因子释放: 激活的 Kupffer细胞 → TNF-α + IL-6 + IL-1β
   - 炎症放大: TNF-α + IL-6 + IL-1β → 进一步肝细胞损伤
**3. 核心酶信息**: 
   - Kupffer细胞中的多种炎症信号酶
**4. 动力学与调控**: 
   - 触发: 肝细胞损伤 > 阈值
   - 促进因素: 先天免疫激活
   - 时间尺度: 天级反应
**5. 能量与热力学**: 无直接能量消耗
**6. 功能说明**: 
   - 先天免疫系统激活
   - 炎症细胞因子风暴
   - 肝细胞损伤放大
**7. 病理意义**: 药物性肝损伤从肝细胞损伤进展为肝衰竭的关键机制

#### 胆汁淤积 (Cholestasis)

##### 步骤 ID: PATH-05
**1. 反应名称**: 胆汁淤积中的FXR信号抑制 (FXR Signaling Suppression in Cholestasis)
**2. 化学方程式**: 
   - 胆汁酸淤积: 胆汁酸排泄障碍 → 胆汁酸堆积
   - 膜损伤: 堆积的胆汁酸 → 细胞膜损伤 → 细胞内胆汁酸增加
   - FXR抑制: 过高浓度胆汁酸 → 抑制的 FXR 核转位
   - 胆汁酸合成失控: 抑制的 FXR → 激活的 CYP7A1 → 胆汁酸合成持续
**3. 核心酶信息**: 
   - FXR, CYP7A1 (EC 1.14.13.11)
**4. 动力学与调控**: 
   - 触发: 胆汁酸 > 100 μM
   - 促进因素: BSEP基因突变、药物抑制BSEP
   - 时间尺度: 天级反应
**5. 能量与热力学**: 无直接能量消耗
**6. 功能说明**: 
   - 胆汁酸负反馈调节失效
   - 胆汁酸合成持续激活
   - 肝细胞损伤加重
**7. 病理意义**: 胆汁淤积性肝病进展的关键机制

### 慢速适应性网络 (Nuclear Receptors)

#### PPAR-α (过氧化物酶体增殖物激活受体 α)

##### 步骤 ID: REG-Nucl-01
**1. 反应名称**: PPAR-α 激活 (PPAR-α Activation)
**2. 化学方程式**: 
   - 配体结合: FFA (游离脂肪酸) + PPAR-α (胞浆) → PPAR-α-FFA 复合物
   - 核转位: PPAR-α-FFA 复合物 → PPAR-α-FFA (核内)
   - DNA 结合: PPAR-α-FFA + RXR + PPRE → 转录激活复合物
   - 基因转录: 转录激活复合物 + DNA → mRNA (靶基因) + 转录激活复合物
**3. 核心酶信息**: 
   - 过氧化物酶体增殖物激活受体 α (PPAR-α), 核受体
   - 视黄酸 X 受体 (RXR), 辅助受体
**4. 动力学与调控**: 
   - 触发: 游离脂肪酸 (FFA) 升高 (> 0.5 mM)
   - 激活剂: Fibrates (贝特类药物), GW7647 (合成激动剂)
   - 抑制剂: GW6471 (拮抗剂)
   - 时间尺度: 基因转录需要数小时到数天
**5. 能量与热力学**: 不需要直接能量输入 (ATP 消耗在转录和翻译过程中)
**6. 功能说明**: 
   - 上调 CPT1 (肉碱棕榈酰转移酶 1): 增加 Vmax，促进脂肪酸 β-氧化
   - 上调 HMGCS2 (线粒体 HMG-CoA 合酶): 增加 Vmax，促进酮体生成
   - 上调 ACOX1 (过氧化物酶体酰基辅酶 A 氧化酶): 增加 Vmax，促进过氧化物酶体 β-氧化
   - 上调 UCP2 (解偶联蛋白 2): 增加 Vmax，降低 ROS 生成
**7. 生理意义**: 长期饥饿或生酮饮食下，肝脏适应机制，增强燃烧脂肪能力
**8. 逻辑门**: 
   - 若 FFA > 0.5 mM 持续 > 6 小时 → PPAR-α 激活 → 脂肪酸氧化基因上调
   - 适应结果: 肝脏从糖代谢转向脂代谢，维持能量供应

#### LXR (肝 X 受体)

##### 步骤 ID: REG-Nucl-02
**1. 反应名称**: LXR 激活 (LXR Activation)
**2. 化学方程式**: 
   - 配体结合: 氧化胆固醇衍生物 + LXR (胞浆) → LXR-配体复合物
   - 核转位: LXR-配体复合物 → LXR-配体 (核内)
   - DNA 结合: LXR-配体 + RXR + LXRE → 转录激活复合物
   - 基因转录: 转录激活复合物 + DNA → mRNA (靶基因) + 转录激活复合物
**3. 核心酶信息**: 
   - 肝 X 受体 (LXR), 核受体 (LXRα 和 LXRβ)
   - 视黄酸 X 受体 (RXR), 辅助受体
**4. 动力学与调控**: 
   - 触发: 氧化胆固醇衍生物 (> 10 μM)
   - 激活剂: GW3965 (合成激动剂), T0901317 (合成激动剂)
   - 抑制剂: GSK2033 (拮抗剂)
   - 时间尺度: 基因转录需要数小时到数天
**5. 能量与热力学**: 不需要直接能量输入 (ATP 消耗在转录和翻译过程中)
**6. 功能说明**: 
   - 上调 SREBP-1c (固醇调节元件结合蛋白 1c): 增加 Vmax，促进脂肪酸和胆固醇合成
   - 上调 ABCG5/8 (胆固醇外排泵): 增加 Vmax，促进胆固醇排泄
   - 上调 PLTP (磷脂转运蛋白): 增加 Vmax，促进 HDL 形成
   - 上调 FAS (脂肪酸合酶): 增加 Vmax，促进脂肪酸合成
**7. 生理意义**: 高脂饮食下，肝脏适应机制，促进胆固醇排泄和脂肪合成
**8. 逻辑门**: 
   - 若氧化胆固醇 > 10 μM 持续 > 6 小时 → LXR 激活 → 脂肪合成基因上调
   - 适应结果: 增加胆固醇排泄，但可能诱发脂肪肝

#### FXR (法尼醇 X 受体)

##### 步骤 ID: REG-Nucl-03
**1. 反应名称**: FXR 激活 (FXR Activation)
**2. 化学方程式**: 
   - 配体结合: 胆汁酸 + FXR (胞浆) → FXR-胆汁酸复合物
   - 核转位: FXR-胆汁酸复合物 → FXR-胆汁酸 (核内)
   - DNA 结合: FXR-胆汁酸 + RXR + FXRE → 转录激活复合物
   - 基因转录: 转录激活复合物 + DNA → mRNA (靶基因) + 转录激活复合物
   - 抑制转录: SHP + CYP7A1 启动子 → CYP7A1 转录抑制
**3. 核心酶信息**: 
   - 法尼醇 X 受体 (FXR), 核受体
   - 视黄酸 X 受体 (RXR), 辅助受体
   - SHP (小异二聚体伴侣), 转录抑制因子
**4. 动力学与调控**: 
   - 触发: 胆汁酸 (> 50 μM)
   - 激活剂: GW4064 (合成激动剂), Obeticholic acid (OCA)
   - 抑制剂: Guggulsterone (拮抗剂)
   - 时间尺度: 基因转录需要数小时到数天
**5. 能量与热力学**: 不需要直接能量输入 (ATP 消耗在转录和翻译过程中)
**6. 功能说明**: 
   - 抑制 CYP7A1 (胆固醇 7α-羟化酶): 降低 Vmax，停止胆汁酸合成
   - 上调 BSEP (胆汁盐外排泵): 增加 Vmax，促进胆汁酸排泄
   - 下调 NTCP (胆汁酸重吸收泵): 降低 Vmax，减少胆汁酸回收
   - 上调 SHP (转录抑制因子): 抑制胆汁酸合成基因
**7. 生理意义**: 胆汁酸的负反馈调节机制，防止胆汁淤积
**8. 逻辑门**: 
   - 若胆汁酸 > 50 μM 持续 > 6 小时 → FXR 激活 → 胆汁酸合成抑制
   - 适应结果: 停止合成胆汁酸，促进胆汁酸排泄，防止胆汁淤积

#### CAR (组成型雄烷受体)

##### 步骤 ID: REG-Nucl-04
**1. 反应名称**: CAR 激活 (CAR Activation)
**2. 化学方程式**: 
   - 配体结合: 药物/异种物 + CAR (胞浆) → CAR-配体复合物
   - 核转位: CAR-配体复合物 → CAR-配体 (核内)
   - DNA 结合: CAR-配体 + RXR + DR4/ER6 → 转录激活复合物
   - 基因转录: 转录激活复合物 + DNA → mRNA (靶基因) + 转录激活复合物
**3. 核心酶信息**: 
   - 组成型雄烷受体 (Constitutive Androstane Receptor, CAR), 核受体
   - 视黄酸 X 受体 (RXR), 辅助受体
**4. 动力学与调控**: 
   - 触发: 药物/异种物 (> 1 μM)
   - 激活剂: Phenobarbital (苯巴比妥), CITCO (合成激动剂)
   - 抑制剂: Androstanol (雄烷醇), PK11195
   - 时间尺度: 基因转录需要数小时到数天
**5. 能量与热力学**: 不需要直接能量输入 (ATP 消耗在转录和翻译过程中)
**6. 功能说明**: 
   - 上调 CYP2B6 (细胞色素 P450 2B6): 增加 Vmax，促进药物代谢
   - 上调 CYP3A4 (细胞色素 P450 3A4): 增加 Vmax，促进药物代谢
   - 上调 UGT1A1 (尿苷二磷酸葡萄糖醛酸转移酶): 增加 Vmax，促进药物结合代谢
   - 上调 SULT1A1 (磺基转移酶): 增加 Vmax，促进药物结合代谢
**7. 生理意义**: 药物和异种物的适应性反应，增强肝脏解毒能力
**8. 逻辑门**: 
   - 若药物/异种物 > 1 μM 持续 > 6 小时 → CAR 激活 → 药物代谢基因上调
   - 适应结果: 增强药物代谢能力，减少药物毒性，但可能导致药物相互作用

#### PXR (孕烷 X 受体)

##### 步骤 ID: REG-Nucl-05
**1. 反应名称**: PXR 激活 (PXR Activation)
**2. 化学方程式**: 
   - 配体结合: 药物/类固醇 + PXR (胞浆) → PXR-配体复合物
   - 核转位: PXR-配体复合物 → PXR-配体 (核内)
   - DNA 结合: PXR-配体 + RXR + DR3/DR4 → 转录激活复合物
   - 基因转录: 转录激活复合物 + DNA → mRNA (靶基因) + 转录激活复合物
**3. 核心酶信息**: 
   - 孕烷 X 受体 (Pregnane X Receptor, PXR), 核受体
   - 视黄酸 X 受体 (RXR), 辅助受体
**4. 动力学与调控**: 
   - 触发: 药物/类固醇 (> 1 μM)
   - 激活剂: Rifampicin (利福平), SR12813 (合成激动剂)
   - 抑制剂: SPA70 (拮抗剂), Ketoconazole (酮康唑)
   - 时间尺度: 基因转录需要数小时到数天
**5. 能量与热力学**: 不需要直接能量输入 (ATP 消耗在转录和翻译过程中)
**6. 功能说明**: 
   - 上调 CYP3A4 (细胞色素 P450 3A4): 增加 Vmax，促进药物代谢
   - 上调 MDR1 (多药耐药蛋白 1): 增加 Vmax，促进药物外排
   - 上调 MRP2 (多药耐药相关蛋白 2): 增加 Vmax，促进药物外排
   - 上调 GST (谷胱甘肽 S-转移酶): 增加 Vmax，促进药物结合代谢
**7. 生理意义**: 药物和类固醇的适应性反应，保护肝脏免受毒性物质损害
**8. 逻辑门**: 
   - 若药物/类固醇 > 1 μM 持续 > 6 小时 → PXR 激活 → 药物代谢和外排基因上调
   - 适应结果: 增强药物代谢和外排能力，减少药物毒性，但可能导致药物疗效降低
