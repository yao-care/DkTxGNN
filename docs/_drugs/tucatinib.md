---
layout: default
title: Tucatinib
parent: 僅模型預測 (L5)
nav_order: 456
evidence_level: L5
indication_count: 10
---

# Tucatinib
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

# Tucatinib: From HER2-Positive Breast Cancer to Migraine Disorder

## One-Sentence Summary

Tucatinib is an oral HER2-selective tyrosine kinase inhibitor, described in the sourced evidence as targeting the HER2 pathway used in oncology settings; no confirmed original indication is recorded in this evidence pack because the drug is not marketed in Denmark. The TxGNN model predicts it may be effective for **Migraine Disorder**, but this prediction is currently supported by **0 clinical trials** and **0 publications**, and the evidence pack's own mechanistic rationale states there is no known biological link between HER2 signalling and migraine pathophysiology (CGRP, trigeminovascular system, serotonin pathways).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in Danish license data (drug not marketed in Denmark); evidence-pack rationale text identifies Tucatinib as a HER2-selective TKI used in HER2-related oncology |
| Predicted New Indication | Migraine Disorder |
| TxGNN Prediction Score | 98.62% |
| Evidence Level | L5 (model prediction only, no clinical trials or literature) |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data (`original_moa`) is not available as a structured field. Based on information embedded in the evidence pack's own rationale text, Tucatinib is a HER2-selective tyrosine kinase inhibitor, a drug class used in oncology to block HER2-driven tumour signalling.

Migraine disorder's known pathophysiology involves CGRP release, the trigeminovascular system, and serotonergic pathways — none of which overlap with HER2 receptor signalling. The evidence pack explicitly states: *"無已知機轉關聯...無臨床或臨床前證據支持"* (no known mechanistic link; no clinical or preclinical evidence supports this association).

Given the absence of a plausible biological mechanism and the complete absence of supporting clinical trials or literature for this specific drug-disease pair, this prediction should be interpreted as a statistical association from the TxGNN model rather than a mechanistically grounded repurposing hypothesis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Denmark Market Information

Tucatinib is not currently marketed in Denmark. No marketing authorisations (national Laegemiddelstyrelsen or centralised EMA) were found in this evidence pack (`total_licenses: 0`).

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (HER2-selective tyrosine kinase inhibitor) |
| Myelosuppression Risk | Please refer to the Summary of Product Characteristics (SmPC) warnings and precautions |
| Emetogenicity Classification | Please refer to the Summary of Product Characteristics (SmPC) warnings and precautions |
| Monitoring Items | Please refer to the Summary of Product Characteristics (SmPC) warnings and precautions |
| Handling Protection | Please refer to the Summary of Product Characteristics (SmPC) warnings and precautions |

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information. No key warnings, contraindications, or drug-drug interaction data were available in this evidence pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN prediction score (98.62%), there is no supporting clinical trial or literature evidence for Tucatinib in migraine disorder, and the mechanistic rationale in the evidence pack itself finds no biological plausibility (HER2 pathway vs. CGRP/trigeminovascular/serotonergic pathways). This is a model-only (L5) prediction and does not meet the threshold to advance past initial screening.

Additionally, worth noting: among this drug's other top-ranked TxGNN predictions, the "multiple endocrine neoplasia" evidence (NCT04802759, NCT02892123) was flagged as keyword mismatch — those trials study zanidatamab, not Tucatinib — and the "pulmonary hypertension" prediction was flagged as a possible **safety signal rather than therapeutic benefit**, since tyrosine kinase inhibitors as a class (e.g., dasatinib) are known to induce pulmonary hypertension as an adverse effect. Both reinforce a cautious posture toward this candidate overall.

**To proceed, the following is needed:**
- TFDA/Danish SmPC warnings and contraindications (currently a Blocking data gap)
- Confirmed mechanism of action data via DrugBank API (currently a High-severity data gap)
- Any preclinical or mechanistic studies linking HER2 inhibition to migraine pathophysiology, if they exist
- Re-evaluation once genuine (non-keyword-mismatched) clinical or literature evidence becomes available
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

