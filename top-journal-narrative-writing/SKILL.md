---
name: top-journal-narrative-writing
description: Diagnoses and rewrites academic manuscript framing for top-journal style narrative; use for 顶刊叙事, 论文写作, abstract/introduction/cover letter/reviewer-response work involving problem framing, contribution positioning, assumption challenges, mechanism explanation, evidence-boundary checks, and defensible novelty claims.
---

# Top-Journal Narrative Writing

## Purpose
Help transform a manuscript from “we did X and improved Y” into a defensible scholarly narrative: **important problem → unresolved gap or questionable assumption → precise contribution → evidence → mechanism/explanation → boundary and broader implication**.

Use this skill for academic papers, grant-like manuscript framing, abstracts, introductions, discussion sections, cover letters, and reviewer-response narratives.

## Non-negotiable rules
1. Do not invent novelty, mechanisms, datasets, experiments, citations, or implications.
2. Never claim “top-journal ready” unless the evidence, novelty, scope, and writing all support it; instead state what is strong, weak, or missing.
3. Separate **narrative framing** from **scientific substance**. Better framing can reveal contribution; it cannot replace contribution.
4. Every upgraded story must pass the triad: **claim — evidence — boundary**.
5. Prefer the strongest defensible narrative over the grandest-sounding narrative.
6. Flag overclaiming, causal language without causal evidence, and broad generalization from a narrow setting.

## Required input to ask for or infer
When information is missing, proceed with explicit assumptions rather than blocking, unless the user asks for a final manuscript rewrite. Useful inputs:
- Field and target journal or journal tier.
- Current title, abstract, introduction, or draft contribution bullets.
- What was actually done: method/theory/data/experiment/application.
- Main empirical/theoretical evidence.
- Baselines, ablations, robustness tests, external validation, or qualitative evidence.
- Known limitations and what cannot be claimed.

## Core workflow

### Step 1 — Extract the factual contribution
Summarize only what the manuscript actually supports:
- Research object:
- Existing dominant view/method/assumption:
- Concrete gap or failure mode:
- New contribution:
- Main evidence:
- Scope and limitations:

### Step 2 — Diagnose the current story
Classify the draft’s current narrative pattern:
- Incremental improvement: “A has a limitation; we add B.”
- Method-first: “We propose method X.”
- Application-only: “We apply X to Y.”
- Result-only: “We achieve higher scores.”
- Isolated contribution: “This works here.”
- Other pattern:

State why the current framing may feel ordinary to reviewers.

### Step 3 — Generate alternative narrative angles
Create 3–5 candidate framings. For each candidate, use this format:

```markdown
### Narrative option: [short name]
**Core sentence:** [One sentence: field assumes/needs X, but Y; this work shows/proposes Z.]
**Best fit when:** [conditions]
**Evidence required:** [minimum evidence needed]
**What to avoid:** [overclaiming risk]
**Likely title style:** [title pattern]
**Intro opening logic:** [3-step opening]
```

Use these canonical upgrades when appropriate:
1. **Improvement → assumption challenge**: move from “we improve A” to “we test and relax an assumption behind A.”
2. **Method-driven → problem-driven**: make the painful unresolved problem the protagonist; method is the response.
3. **Application → principle**: extract a transferable mechanism, condition, rule, or design principle from the application.
4. **Result → explanation**: explain why the result occurs using ablations, mechanism tests, theory, or error analysis.
5. **Isolated work → connection**: connect the contribution to broader debates, tasks, fields, or theoretical questions.
6. **Benchmark gain → reliability/generalization**: when gains are modest, frame around robustness, distribution shift, interpretability, cost, safety, or deployment constraints if evidence supports it.
7. **Tool/dataset → field-enabling resource**: for resources, frame around what questions become answerable, not just what was collected.

For detailed angle criteria, consult `references/NARRATIVE_ANGLES.md`.

### Step 4 — Build the evidence matrix
For the strongest 1–2 narratives, produce a claim-evidence-boundary table:

```markdown
| Claim | Evidence already available | Evidence still needed | Safe wording | Unsafe wording |
|---|---|---|---|---|
```

Use `references/EVIDENCE_MATRIX.md` for required evidence by claim type.

### Step 5 — Select the strongest defensible narrative
Rank options by:
- Importance of the problem.
- Novelty of the conceptual move.
- Strength of evidence.
- Generality without overclaiming.
- Reviewer plausibility.
- Fit to target journal and audience.

Recommend one primary narrative and one backup narrative.

### Step 6 — Rewrite key manuscript elements
When asked to rewrite, provide one or more of:
- Title alternatives.
- Abstract in structured logic: background → gap → approach → evidence → insight → implication.
- Introduction outline: broad problem → field bottleneck → hidden assumption/gap → our contribution → evidence → implications.
- Contribution bullets.
- Discussion/limitation paragraph.
- Cover-letter pitch.
- Reviewer-facing response framing.

Use `templates/OUTPUT_TEMPLATE.md` for a compact output format.

### Step 7 — Skeptical reviewer check
End with a short “reviewer risk audit”:
- What would a skeptical reviewer challenge first?
- Which claim is under-evidenced?
- Which sentence may sound inflated?
- What experiment/analysis/wording would reduce risk?

## Style guidelines
- Write in the language used by the user unless asked otherwise.
- Prefer clear, precise academic prose over promotional language.
- Use “we show/provide evidence/suggest” when evidence is empirical but not causal.
- Use “generalizes to” only with external validation; otherwise use “may extend to” or “suggests relevance for.”
- Preserve technical accuracy and field terminology.
- Do not add citations unless sources are supplied or web/library access is explicitly available.

## Compact response template
```markdown
## 1. Overall judgment
[Reasonable / overclaimed / missing evidence / best potential framing]

## 2. Current narrative diagnosis
[What the manuscript currently sounds like and why]

## 3. Candidate narratives
[3–5 options with core sentence, evidence required, risks]

## 4. Best narrative
[Primary narrative + backup]

## 5. Rewrite draft
[Title / abstract / intro outline / contribution bullets as requested]

## 6. Reviewer risk audit
[Main overclaim risks and evidence gaps]
```
