# Train Cases Simulation Failures & Analysis (Updated)

依据本次模拟输出：[metabolite_summary_train_cases.md](file:///home/yifei/AI4Science/metabolomics/simulate/modules/results/metabolite_summary_train_cases.md) 与 [test_result_train_cases.txt](file:///home/yifei/AI4Science/metabolomics/simulate/modules/results/test_result_train_cases.txt)，现有通过率为 1/7。结合期望描述 [train_cases.md](file:///home/yifei/AI4Science/metabolomics/simulate/modules/docs/train_cases.md) 更新失败原因与修正方案。

## 失败与偏差
- 清晨空腹期血糖显著下降，未维持基线；糖原无明显分解迹象。
- 早餐/午餐后血糖与胰岛素未形成明显峰值；胰高血糖素抑制不充分。
- 脂肪酸在全天显著累积；甘油三酯储存信号较弱。
- NAD+/ADP 逐步枯竭，阻滞氧化磷酸化，导致代谢链条失衡。

## 原因定位
- 步进任务未包含糖原合成/分解的编排，导致糖原始终不变。
- 餐食注入量过小，无法触发餐后血糖与胰岛素峰值。
- 激素传导仅依赖血糖阈值，未考虑餐后状态对胰岛素增强与胰高血糖素抑制。
- ADP 回补缺失，NAD+ 再生受阻，造成脂肪氧化与能量代谢受限。

## 已实施修正
- 在系统步进中按胰岛素/胰高血糖素关系动态加入糖原合成或分解。
- 提升餐食注入量（葡萄糖/氨基酸/甘油三酯）以形成合理餐后峰值。
- 调整激素传导：餐后增强胰岛素、抑制胰高血糖素；降低阈值以匹配生理范围。
- 增加细胞 ATP 负荷模块，回补 ADP，缓解 NAD+ 枯竭；放宽氧化磷酸化对 ADP 的硬阈值。
- 下调脂解速率常数；增强餐后外源性甘油三酯注入。

## 待验证与预期
- 空腹阶段血糖维持在合理基线，糖原缓慢下降；餐后血糖与胰岛素出现峰值，胰高血糖素被抑制。
- 午晚餐后甘油三酯储存增强，脂肪酸不再单调暴涨；夜间酮体适度上升。
- NAD+/ADP 维持在非零稳态，氧化磷酸化与脂肪氧化正常进行。

请重新运行训练用例模拟并生成最新的结果文件，用于进一步核验各阶段断言。
