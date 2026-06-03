# Evidence Matrix Guide

Use this guide to check whether a narrative is supported.

| Narrative claim type | Minimum evidence | Stronger evidence | Safer wording when evidence is limited |
|---|---|---|---|
| Challenges an assumption | Show the assumption in prior work and demonstrate failure cases | Stress tests across datasets/conditions; theoretical analysis | “questions the robustness of X under…” |
| Solves a field bottleneck | Show bottleneck matters and current methods fail | Evaluation targeted at the bottleneck; user/clinical/field relevance | “addresses one important aspect of…” |
| Reveals a mechanism | Ablation or analysis linking component to outcome | Causal intervention, theory, replicated mechanism tests | “is consistent with the interpretation that…” |
| Provides a general principle | Evidence across multiple settings or conditions | Theory plus cross-domain validation | “suggests a design principle for…” |
| Improves performance | Strong baselines and fair evaluation | Statistical testing, external validation, resource analysis | “improves over tested baselines on…” |
| Improves robustness | Distribution shift or perturbation tests | Real-world external validation | “is more robust in the tested shift settings…” |
| Enables a field/resource | Quality, coverage, reproducibility, baseline tasks | Community adoption, new discoveries enabled | “provides an enabling resource for…” |
| Has practical impact | Evaluation connected to practical constraints | Prospective, field, clinical, or deployment evidence | “has potential practical relevance for…” |

## Claim wording ladder
Use stronger verbs only when evidence supports them:

1. **Observes / reports** — descriptive evidence.
2. **Suggests / indicates** — plausible but not definitive evidence.
3. **Shows / demonstrates** — direct empirical or theoretical support.
4. **Establishes / proves** — rigorous proof or very strong evidence; use rarely.
5. **Generalizes** — requires validation beyond the original setting.

## Boundary checklist
For each major claim, identify:
- Population, domain, dataset, or system covered.
- Conditions where it holds.
- Conditions where it fails or is untested.
- Whether evidence is empirical, theoretical, qualitative, or speculative.
- Whether causal language is justified.
