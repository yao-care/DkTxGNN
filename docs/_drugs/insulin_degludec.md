---
layout: default
title: Insulin Degludec
parent: 僅模型預測 (L5)
nav_order: 235
evidence_level: L5
indication_count: 10
---

# Insulin Degludec
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

# Insulin Degludec: Confirming Established Basal Insulin Therapy in Type 1 Diabetes Mellitus

## One-Sentence Summary

Insulin degludec is a long-acting basal insulin analogue whose detailed mechanism-of-action documentation is currently a data gap in this evidence pack. The TxGNN model predicts high relevance for **Type 1 Diabetes Mellitus (T1DM)**, supported by **50 clinical trials** and **20 publications** — however, this is the drug's own well-established, label-type indication rather than a novel repurposing hypothesis, so this case should be read as a **market-entry/registration review**, not a mechanism-discovery finding.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available from Danish licence data (0 licences on file); internationally, insulin degludec is an approved basal insulin used for diabetes mellitus management |
| Predicted New Indication | Type 1 Diabetes Mellitus |
| TxGNN Prediction Score | 99.44% |
| Evidence Level | L1 |
| Denmark Market Status | Not Marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data is not available in this evidence pack (flagged as a High-severity data gap). Based on known pharmacological class information, insulin degludec is an ultra-long-acting basal insulin analogue that forms soluble multihexamers after subcutaneous injection, which are slowly and continuously released into the bloodstream — producing a flat, stable glucose-lowering profile with a duration of action exceeding 42 hours and low day-to-day variability compared with earlier basal insulin analogues (glargine, detemir).

Importantly, the analysts who produced this candidate flag an important caveat that must be communicated clearly: **Type 1 Diabetes Mellitus is not a novel repurposing target for insulin degludec — it is the drug's core, label-type indication.** T1DM results from autoimmune destruction of pancreatic beta cells, leading to absolute insulin deficiency; exogenous basal-bolus insulin replacement (of which insulin degludec is a standard component) is the established standard of care. The TxGNN model's very high score (99.44%) reflects that the model has correctly recovered an already well-established pharmacological relationship from the knowledge graph, rather than surfacing new biological insight.

Mechanistically, this "prediction" is therefore trivially reasonable — it is direct pharmacological replacement therapy, not an indirect or hypothesis-generating association. The practical question for this evidence pack is not "does insulin degludec work in T1DM" (this is already extensively proven, see evidence below), but rather **whether/when the product will obtain Danish marketing authorisation**, since Denmark currently shows "Not Marketed" status with zero registered licences.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02030600](https://clinicaltrials.gov/study/NCT02030600) | Phase 3 | Completed | 721 | SWITCH 2: double-blind, cross-over comparison of insulin degludec vs. insulin glargine (safety/efficacy) — population: Type 2 diabetes |
| [NCT01513473](https://clinicaltrials.gov/study/NCT01513473) | Phase 3 | Completed | 350 | BEGIN™ Young 1: multinational, randomised, parallel trial of insulin degludec vs. detemir in children/adolescents with Type 1 diabetes on basal-bolus regimen |
| [NCT02392117](https://clinicaltrials.gov/study/NCT02392117) | N/A (non-interventional) | Completed | 1,262 | Multi-centre, prospective, real-world safety and effectiveness study of Tresiba® (insulin degludec) in Type 1 and Type 2 diabetes |
| [NCT04196231](https://clinicaltrials.gov/study/NCT04196231) | Phase 4 | Completed | 258 | BEYOND: open-label, three-arm RCT on durability of glycaemic control with basal insulin/GLP-1RA or SGLT-2i vs. basal-bolus insulin — population: Type 2 diabetes |
| [NCT06199505](https://clinicaltrials.gov/study/NCT06199505) | Phase 2 | Completed | 153 | Comparison of GZR101 vs. insulin degludec/insulin aspart in Type 2 diabetes inadequately controlled on OADs/insulin |
| [NCT03938740](https://clinicaltrials.gov/study/NCT03938740) | Phase 2 | Completed | 61 | Randomised, open-label comparison of insulin dosing algorithms (HDV-insulin lispro vs. insulin degludec) in Type 1 diabetes |
| [NCT01773798](https://clinicaltrials.gov/study/NCT01773798) | Phase 1 | Completed | 33 | PK/PD study of insulin degludec/insulin aspart 15 in Type 1 diabetes |
| [NCT02670915](https://clinicaltrials.gov/study/NCT02670915) | Phase 3 | Completed | 834 | Efficacy/safety of faster-acting insulin aspart vs. NovoRapid®, both in combination with insulin degludec, in children/adolescents with Type 1 diabetes (comparator focus — indirect relevance) |
| [NCT05103306](https://clinicaltrials.gov/study/NCT05103306) | N/A | Unknown | 300 | Real-world comparison of empagliflozin-based quadruple oral therapy vs. basal insulin-based combination therapy in Type 2 diabetes (indirect relevance) |
| [NCT01467414](https://clinicaltrials.gov/study/NCT01467414) | Phase 1 | Terminated | 1 | PD study of insulin degludec in Japanese subjects with Type 2 diabetes — terminated, minimal completed enrollment (low relevance) |

*Note: 50 clinical trials referencing insulin degludec and diabetes were identified in total; the 10 most relevant (by assigned evidence grade) are shown above. Several listed trials studied Type 2 diabetes populations or used insulin degludec as a comparator rather than the primary study drug — flagged accordingly.*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39270686](https://pubmed.ncbi.nlm.nih.gov/39270686/) | 2024 | RCT | Lancet | QWINT-5: once-weekly insulin efsitora alfa vs. once-daily insulin degludec in adults with Type 1 diabetes — non-inferiority trial |
| [37863084](https://pubmed.ncbi.nlm.nih.gov/37863084/) | 2023 | RCT | Lancet | ONWARDS 6: once-weekly insulin icodec vs. once-daily insulin degludec as part of basal-bolus regimen in Type 1 diabetes |
| [36623517](https://pubmed.ncbi.nlm.nih.gov/36623517/) | 2023 | RCT | Lancet Diabetes & Endocrinology | EXPECT: insulin degludec vs. detemir (both with aspart) in pregnant women with Type 1 diabetes — non-inferiority trial |
| [36763996](https://pubmed.ncbi.nlm.nih.gov/36763996/) | 2022 | Meta-analysis/Review | Clinical Therapeutics | Systematic review/meta-analysis comparing efficacy and tolerability of insulin degludec vs. other long-acting basal insulin analogues in T1DM/T2DM |
| [38679838](https://pubmed.ncbi.nlm.nih.gov/38679838/) | 2024 | Review (trial design) | Diabetes, Obesity & Metabolism | Design and rationale of the QWINT phase 3 programme (efsitora vs. degludec) |
| [36106652](https://pubmed.ncbi.nlm.nih.gov/36106652/) | 2023 | Review (trial design) | Diabetes, Obesity & Metabolism | Design and rationale of the ONWARDS 1-6 phase 3a programme (icodec vs. degludec) |
| [37290466](https://pubmed.ncbi.nlm.nih.gov/37290466/) | 2023 | Review | Lancet Diabetes & Endocrinology | Management of Type 1 diabetes in pregnancy, incl. basal insulin choice and glycaemic targets |
| [31055056](https://pubmed.ncbi.nlm.nih.gov/31055056/) | 2020 | Review | Diabetes & Metabolism | Current status of insulin degludec in Type 1 and Type 2 diabetes based on randomized and observational trials |
| [25143741](https://pubmed.ncbi.nlm.nih.gov/25143741/) | 2014 | Review | Vascular Health and Risk Management | Insulin degludec/insulin aspart combination for treatment of Type 1 and Type 2 diabetes |
| [23890782](https://pubmed.ncbi.nlm.nih.gov/23890782/) | 2014 | Review | Endocrinología y Nutrición | Advances in clinical research on degludec as ultra-long-acting basal insulin in Type 1 and Type 2 diabetes |

*Note: 20 publications were identified in total for this indication; the 10 with completed relevance classification are shown, prioritised RCT > meta-analysis/review > narrative review.*

---

## Denmark Market Information

No marketing authorisation for insulin degludec is currently on file in this evidence pack for the Danish market (**Market status: Not Marketed; 0 registered licences**). No product name, dosage form, or approved indication text is available from the Laegemiddelstyrelsen (Danish Medicines Agency) or EMA centralised registration data provided. This should be independently verified against the current Laegemiddelstyrelsen and EMA product registers, since insulin degludec (marketed elsewhere as Tresiba®/Ryzodeg®/Xultophy®) may hold live EU centralised authorisations not captured in this pack.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information. No key warnings, contraindications, or drug-drug interaction data were available in this evidence pack (drug interaction query: not found, 0 results). **This is flagged as a Blocking-severity data gap** — the absence of label-derived warnings/contraindications means a preliminary safety assessment (S1) cannot currently be completed for this candidate.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Extensive Phase 3 clinical trial and RCT literature evidence (Evidence Level L1) supports insulin degludec's efficacy and safety in Type 1 diabetes mellitus. However, this reflects confirmation of an already well-established indication rather than a novel repurposing signal, and Denmark currently has no active marketing authorisation on file — so "guardrails" here specifically means: treat this as a regulatory/market-access question, not a scientific-validation question, and do not proceed to any safety sign-off until the blocking data gap below is closed.

**To proceed, the following is needed:**
- **[Blocking]** Danish/EU-approved product label (SmPC) — warnings, precautions, and contraindications must be obtained before any S1 safety evaluation can be completed.
- **[High priority]** Verified mechanism-of-action documentation from DrugBank or the manufacturer's SmPC.
- Confirmation of current Danish/EU marketing authorisation status directly from Laegemiddelstyrelsen and the EMA register (this evidence pack shows 0 licences, which should be cross-checked as it may reflect a data completeness gap rather than true absence of any EU authorisation).
- Clarification with the originating analysis team on why "Type 1 Diabetes Mellitus" — the drug's core label indication — was classified as a *predicted new* indication, to ensure this candidate is correctly triaged as a market-access case rather than mixed into genuine repurposing-hypothesis review queues.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

