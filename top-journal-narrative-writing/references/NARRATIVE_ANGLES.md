# Narrative Angle Reference

Use these cards to choose a defensible narrative angle. Do not force a grand angle if the evidence cannot support it.

## 1. Improvement → Assumption Challenge
**Use when:** the field relies on a method, metric, dataset condition, theoretical premise, or design convention that is not always valid.

**Core logic:**
- Prior work assumes X.
- X holds under conditions A but fails under conditions B.
- This work identifies the failure and proposes an approach that relaxes or replaces X.

**Evidence needed:**
- Clear documentation that X is an implicit or explicit assumption in prior work.
- Failure cases showing where X breaks.
- New method or analysis that does not depend on X, or depends on it less.
- Robustness or stress tests under non-ideal conditions.

**Red flags:**
- Calling something an “assumption” when it is only a minor design choice.
- Claiming the field is wrong without showing representative prior work.
- Overstating universality from one dataset or case.

## 2. Method-Driven → Problem-Driven
**Use when:** the real value is solving a painful bottleneck rather than introducing a technique.

**Core logic:**
- A high-value task depends on solving problem P.
- Existing approaches fail because of bottleneck B.
- The proposed method is designed around B and is validated on settings where B matters.

**Evidence needed:**
- Why P matters to the field or application.
- Why B is unresolved and consequential.
- Experiments or analysis specifically targeting B, not only global metrics.

**Red flags:**
- A dramatic problem opening followed by experiments that do not measure the problem.
- Treating convenience or speed as a major scientific bottleneck without evidence.

## 3. Application → Principle
**Use when:** a case study reveals a transferable rule, mechanism, constraint, or design principle.

**Core logic:**
- In setting Y, phenomenon Z appears.
- Analysis shows Z arises because of mechanism M or condition C.
- M/C suggests a broader principle beyond Y.

**Evidence needed:**
- Repeated observation across conditions, datasets, tasks, or cases.
- Mechanistic analysis or theory.
- Boundary conditions where the principle holds or fails.

**Red flags:**
- Rebranding a single successful application as a principle without cross-setting evidence.
- Using “universal” or “general” when only one domain was tested.

## 4. Result → Explanation
**Use when:** the manuscript has strong empirical gains but lacks insight.

**Core logic:**
- The method improves outcome O.
- The improvement comes mainly from component/mechanism M.
- M addresses a known failure mode F, explaining when and why the method works.

**Evidence needed:**
- Ablation studies.
- Error analysis.
- Sensitivity analysis.
- Mechanism-specific metrics.
- Qualitative examples when useful.

**Red flags:**
- Reporting scores without explaining sources of gain.
- Claiming mechanism from correlation alone.

## 5. Isolated Work → Connection
**Use when:** the work has implications for a broader question, task family, or debate.

**Core logic:**
- This work addresses a local problem.
- The core idea connects to broader issue Q.
- The findings suggest new directions or constraints for Q.

**Evidence needed:**
- A clearly stated conceptual bridge.
- At least some evidence that the bridge is not superficial.
- Conservative language when evidence is indirect.

**Red flags:**
- Ending with vague “future applications” unrelated to evidence.
- Listing many fields without explaining the shared mechanism.

## 6. Benchmark Gain → Reliability/Generalization
**Use when:** performance gains alone are modest but the method improves robustness, calibration, transfer, interpretability, cost, fairness, safety, or deployment reliability.

**Evidence needed:**
- Stress tests, distribution-shift tests, calibration curves, cost analysis, subgroup analysis, or deployment-style evaluation.
- Direct comparison against strong baselines.

**Red flags:**
- Claiming real-world relevance from standard benchmark gains only.

## 7. Dataset/Tool → Field-Enabling Resource
**Use when:** the contribution is a dataset, platform, benchmark, protocol, or tool.

**Core logic:**
- The field cannot answer question Q because resource R is missing.
- This work creates R with properties A/B/C.
- R enables new measurement, comparison, or discovery.

**Evidence needed:**
- Coverage, quality control, annotation reliability, benchmark tasks, baseline results, reproducibility, access details.
- Examples of new questions or analyses enabled by the resource.

**Red flags:**
- Treating size alone as importance.
- Ignoring bias, coverage limits, or data governance issues.
