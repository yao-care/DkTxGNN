---
layout: default
title: Insulin Detemir
parent: 僅模型預測 (L5)
nav_order: 236
evidence_level: L5
indication_count: 10
---

# Insulin Detemir
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Insulin Detemir: From an Undocumented Original Indication to Type 1 Diabetes Mellitus (Likely Existing-Use Case)

## One-Sentence Summary

Insulin detemir's original indication is not recorded in this evidence pack (data gap), but the drug is generically known as a long-acting basal insulin analogue. The TxGNN model predicts it may be effective for **Type 1 Diabetes Mellitus**, with **dozens of clinical trials** (many completed Phase 3 RCTs) and **substantial literature** currently supporting this direction — however, this is very likely an **already-approved existing indication** rather than a genuinely novel repurposing signal, and this must be verified before any "new indication" claim is made.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in this dataset — insulin detemir is generically a long-acting basal insulin, so this is likely an existing (not new) indication; requires verification |
| Predicted New Indication | Type 1 Diabetes Mellitus |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L1 |
| Denmark Market Status | Not Marketed (per this dataset — see caveat below) |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in this evidence pack (data gap DG002, severity: High). Generically, insulin detemir is a recombinant human insulin analogue modified at the B29 lysine residue with a C14 (myristic acid) fatty-acid chain, which allows reversible binding to serum albumin. This slows subcutaneous absorption and produces a protracted, relatively flat time-action profile compared with NPH insulin — the pharmacological basis for its use as a once- or twice-daily basal insulin. This is the same active substance marketed internationally under the brand name Levemir®.

Because the `original_indications` field in this dataset is empty, the system could not automatically confirm whether "type 1 diabetes mellitus" is already the drug's approved indication rather than a novel one. Long-acting basal insulin analogues of this class are, by design and by regulatory history, indicated for basal glycaemic control in both type 1 and type 2 diabetes. The extremely high TxGNN score (99.77%) combined with a very large body of completed Phase 3 randomised controlled trials most plausibly reflects a strong, already-established drug–disease relationship in the knowledge graph — **not** a novel mechanistic hypothesis.

The evidence pack's own repurposing rationale flags this directly: *"此案例的決策重點在於『引進/上市可行性』而非機轉新穎性…建議人工核實後移除或標註為『既有適應症之市場引進』而非典型 repurposing 候選"* (the decision focus here is market-entry feasibility, not mechanistic novelty; human review should reclassify this as "market introduction of an existing indication" rather than a typical repurposing candidate). This caveat should be resolved — by retrieving the drug's documented original indication from TFDA/DrugBank/SmPC — before this candidate is treated as a genuine old-drug-new-use opportunity.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03220425](https://clinicaltrials.gov/study/NCT03220425) | Phase 3 | Completed | 752 | 6-month efficacy/safety comparison of insulin detemir vs NPH insulin in T1DM basal-bolus regimen; large direct evidence base |
| [NCT01486940](https://clinicaltrials.gov/study/NCT01486940) | Phase 3 | Completed | 598 | Multinational RCT comparing detemir+aspart vs NPH+human soluble insulin in T1DM basal-bolus therapy |
| [NCT01513473](https://clinicaltrials.gov/study/NCT01513473) | Phase 3 | Completed | 350 | BEGIN™ Young 1: 26-week (+26-week extension) comparison of insulin degludec vs detemir in children/adolescents with T1DM |
| [NCT00447382](https://clinicaltrials.gov/study/NCT00447382) | Phase 3 | Completed | 330 | 12-month double-blind safety comparison of two detemir manufacturing processes in T1DM basal-bolus regimen |
| [NCT01709929](https://clinicaltrials.gov/study/NCT01709929) | Phase 3 | Completed | 2287 | Large multicentre, non-randomised safety study of insulin detemir in T1DM and T2DM |
| [NCT01461616](https://clinicaltrials.gov/study/NCT01461616) | Phase 3 | Completed | 19 | Open-label triple crossover trial comparing NPH, detemir and glargine on IGFBP-1/IGF-I in T1DM |
| [NCT00738153](https://clinicaltrials.gov/study/NCT00738153) | N/A (observational) | Completed | 798 | Observational study (Africa) evaluating efficacy and serious ADR incidence with Levemir® in T1DM and T2DM |
| [NCT00687284](https://clinicaltrials.gov/study/NCT00687284) | N/A (observational) | Completed | 2188 | Large European observational study of glycaemic control with Levemir® as initiation therapy |
| [NCT01271517](https://clinicaltrials.gov/study/NCT01271517) | Phase 4 | Unknown | 120 | RCT in newly diagnosed adolescents comparing NPH, glargine and detemir on metabolic control and GH/IGF-I axis |
| [NCT00595374](https://clinicaltrials.gov/study/NCT00595374) | Phase 3 | Completed | 114 | European RCT comparing detemir+aspart vs NPH+aspart in adults with T1DM |

*Note: dozens of additional Phase 1–4 trials (both RCTs and observational studies) exist in the evidence pack beyond this top-10 selection; the full set spans pregnancy, paediatric, and comparator (glargine/degludec) populations.*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36623517](https://pubmed.ncbi.nlm.nih.gov/36623517/) | 2023 | RCT | Lancet Diabetes Endocrinol | EXPECT trial: open-label, multinational non-inferiority RCT of degludec vs detemir (both + aspart) in pregnant women with T1DM |
| [36763996](https://pubmed.ncbi.nlm.nih.gov/36763996/) | 2022 | Systematic review/Meta-analysis | Clin Ther | Efficacy/tolerability of degludec vs other long-acting basal analogues (incl. detemir) in T1DM/T2DM |
| [29477399](https://pubmed.ncbi.nlm.nih.gov/29477399/) | 2018 | Systematic review/Network meta-analysis | Value Health | Comparative efficacy and safety of basal insulin regimens in adults with T1DM |
| [23110609](https://pubmed.ncbi.nlm.nih.gov/23110609/) | 2012 | Review | Drugs | Comprehensive review of insulin detemir's role as basal therapy in T1DM and T2DM |
| [21878861](https://pubmed.ncbi.nlm.nih.gov/21878861/) | 2011 | Systematic review/Meta-analysis | Pol Arch Med Wewn | Detemir vs NPH insulin in T1DM — glycaemic control outcomes |
| [17326333](https://pubmed.ncbi.nlm.nih.gov/17326333/) | 2006 | Review | Vasc Health Risk Manag | Mechanism and clinical use of detemir in T1DM and T2DM, including reduced hypoglycaemia risk |
| [15516157](https://pubmed.ncbi.nlm.nih.gov/15516157/) | 2004 | Review | Drugs | Early comprehensive review of detemir's pharmacology and use in T1DM/T2DM |
| [20539842](https://pubmed.ncbi.nlm.nih.gov/20539842/) | 2010 | Review | Vasc Health Risk Manag | Updated treatment review positioning detemir among basal insulin analogues |
| [36896906](https://pubmed.ncbi.nlm.nih.gov/36896906/) | 2024 | Review | Curr Diabetes Rev | Two-decade review of glargine in T1DM, with detemir as a key comparator |
| [18454569](https://pubmed.ncbi.nlm.nih.gov/18454569/) | 2008 | Review | Paediatr Drugs | Review of insulin analogue preparations, including detemir, in children/adolescents with T1DM |

---

## Denmark Market Information

No marketing authorisations for insulin detemir are recorded in this dataset (market status: **Not Marketed**, 0 licenses on file).

**Important caveat:** Insulin detemir (Levemir®) is an internationally marketed, EMA centrally-authorised product. A "0 licenses / not marketed" result in this evidence pack is inconsistent with its known global regulatory status and should be treated as a probable **data gap** rather than confirmation of true absence from the Danish market. This must be verified directly against the Laegemiddelstyrelsen register and the EMA centralised procedure database before any market-entry decision is finalised.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

**Critical outstanding gap:** TFDA/SmPC label warnings and contraindications could not be retrieved for this evaluation (data gap DG001, severity: **Blocking**). Per the evidence pack, this gap means the candidate **cannot proceed to the S1 safety initial-assessment stage** until label data is obtained. This alone is sufficient reason to hold the case regardless of the strength of the efficacy evidence above.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- A **Blocking**-severity data gap (missing TFDA/SmPC warnings and contraindications) prevents any safety initial assessment (S1), independent of how strong the efficacy evidence is.
- The predicted "new" indication (type 1 diabetes mellitus) is very likely an **already-approved, existing use** of insulin detemir rather than a genuine repurposing candidate; the case should be reclassified once the drug's documented original indication is confirmed.
- Separately, the model's other predictions for this drug (autoimmune oophoritis, opsismodysplasia, thiamine-responsive dysfunction syndrome, classic/focal stiff person syndrome) are all Evidence Level L5 with no supporting trials or literature, and are already correctly flagged "Hold" — these most likely reflect indirect knowledge-graph paths (shared autoimmune/comorbidity or insulin-signalling nodes) rather than plausible clinical hypotheses.

**To proceed, the following is needed:**
- Retrieve TFDA/Laegemiddelstyrelsen SmPC label (warnings, contraindications) to close the Blocking data gap and enable S1 safety assessment
- Retrieve confirmed mechanism-of-action and **original approved indication(s)** from DrugBank/regulatory sources to determine whether "type 1 diabetes mellitus" is genuinely novel or an existing use
- Verify actual Danish/EU marketing authorisation status for insulin detemir (Levemir®), since "0 licenses / not marketed" appears inconsistent with its known EMA-centralised approval
- If reclassified as an existing indication, redirect this evidence pack toward a market-access/pricing review rather than a repurposing evaluation
- If any of the lower-ranked rare-disease predictions are of separate interest, commission targeted literature/mechanistic searches before further action, as none currently have any supporting evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

