---
layout: default
title: Selpercatinib
parent: 僅模型預測 (L5)
nav_order: 397
evidence_level: L5
indication_count: 10
---

# Selpercatinib
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

# Selpercatinib: From RET Fusion-Positive Cancer to Pulmonary Hypertension

## One-Sentence Summary

Selpercatinib is a selective RET kinase inhibitor whose established use — per the supporting literature in this evidence pack — is in RET fusion-positive non-small-cell lung cancer and related RET-altered tumours. The TxGNN model's top prediction is **Pulmonary Hypertension** (score 99.18%), but the only two supporting publications describe treatment-related *systemic* hypertension as an adverse event, not efficacy against pulmonary hypertension as a disease — with **0 clinical trials** and no efficacy literature currently backing this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (no Danish licence on file); literature context indicates RET fusion-positive NSCLC/RET-altered cancers |
| Predicted New Indication | Pulmonary Hypertension |
| TxGNN Prediction Score | 99.18% |
| Evidence Level | L4 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this evidence pack (flagged as a High-severity data gap). Based on the supporting literature, Selpercatinib is a highly selective RET kinase inhibitor, and treatment-related hypertension (elevated blood pressure) is a documented adverse event of RET inhibitor therapy.

However, this is a drug-safety signal for *systemic* hypertension, not mechanistic evidence for treating *pulmonary* hypertension as a disease. Neither of the two supporting publications studies Selpercatinib's efficacy in pulmonary hypertension: one is a pharmacovigilance comparison of adverse-event profiles between pralsetinib and selpercatinib (FDA FAERS data), and the other is a retrospective real-world analysis of selpercatinib in RET fusion-positive NSCLC. The most likely explanation is that TxGNN's embedding space has conflated "hypertension" (an adverse-event term) with "pulmonary hypertension" (the predicted disease target) — a term-overlap artifact rather than a genuine repurposing signal.

The remaining predicted indications in this evidence pack (migraine disorder, migraine with brainstem aura, kyphoscoliotic heart disease) are rated L5 (model prediction only) and rely on either purely theoretical GDNF-RET pathway reasoning with no supporting studies, or literature that is off-target (epilepsy genetics research retrieved via keyword overlap with "migraine/aura"), further reinforcing that this candidate is not yet ready to progress past a data-driven hypothesis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39372206](https://pubmed.ncbi.nlm.nih.gov/39372206/) | 2024 | Cohort (real-world pharmacovigilance) | Frontiers in Pharmacology | Compares adverse-event profiles of pralsetinib vs. selpercatinib using FDA FAERS data; does not evaluate efficacy in pulmonary hypertension |
| [34178121](https://pubmed.ncbi.nlm.nih.gov/34178121/) | 2021 | Cohort (retrospective) | Therapeutic Advances in Medical Oncology | Real-world (SIREN) analysis of selpercatinib in RET fusion-positive NSCLC via an access program; unrelated to pulmonary hypertension |

---

## Denmark Market Information

Currently no Danish marketing authorisations on file (market status: Not marketed).

---

## Cytotoxicity

Selpercatinib is an oncology-indicated targeted therapy (based on RET fusion-positive NSCLC context in the literature above), so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (selective RET kinase inhibitor) |
| Myelosuppression Risk | No myelosuppression data available in this evidence pack — please refer to the Summary of Product Characteristics (SmPC) |
| Emetogenicity Classification | No data available in this evidence pack — please refer to the SmPC |
| Monitoring Items | Blood pressure (treatment-related hypertension is a documented class-effect adverse event per the pharmacovigilance literature above); liver function; please refer to the SmPC for a complete monitoring panel |
| Handling Protection | No data available in this evidence pack — please refer to the SmPC and applicable cytotoxic/targeted-agent handling regulations |

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information. Note: TFDA/Danish label warnings and contraindications are recorded as a **Blocking** data gap (DG001) — this must be resolved before any safety pre-screening (S1) can proceed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top-ranked prediction (Pulmonary Hypertension) is supported only by two pharmacovigilance/real-world papers that do not address pulmonary hypertension efficacy — the association most likely reflects a term-overlap artifact (systemic hypertension AE vs. pulmonary hypertension disease) rather than a genuine mechanistic signal. There are no clinical trials, and the drug is not marketed in Denmark. A Blocking data gap (missing label warnings/contraindications) also prevents any safety pre-screening at this stage.

**To proceed, the following is needed:**
- TFDA/Danish SmPC warnings and contraindications (DG001, Blocking)
- Confirmed mechanism of action data from DrugBank (DG002)
- A dedicated mechanistic or preclinical study on RET signalling in pulmonary vascular remodeling, to distinguish a true repurposing signal from the AE-term confound identified above
- Re-evaluation of lower-ranked candidates (migraine, kyphoscoliotic heart disease) only if independent, on-topic literature or trial evidence emerges
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

