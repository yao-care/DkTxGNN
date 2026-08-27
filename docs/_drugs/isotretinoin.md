---
layout: default
title: Isotretinoin
parent: 僅模型預測 (L5)
nav_order: 247
evidence_level: L5
indication_count: 4
---

# Isotretinoin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Isotretinoin: From Unknown Indication to Malignant Renovascular Hypertension

## One-Sentence Summary

Isotretinoin (DB00982) is a systemic retinoid whose original approved indication is not documented in the current Evidence Pack.
The TxGNN model predicts a possible link to **Malignant Renovascular Hypertension** (score 99.01%),
but **no clinical trials and no literature** currently support this prediction — it rests on the knowledge-graph signal alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in Evidence Pack (data gap — no licenses or original_indications on file) |
| Predicted New Indication | Malignant Renovascular Hypertension |
| TxGNN Prediction Score | 99.01% |
| Evidence Level | L5 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available for isotretinoin in this Evidence Pack. Based on general pharmacological knowledge referenced in the underlying rationale data, isotretinoin is a vitamin A acid (retinoid) derivative that acts primarily on retinoic acid receptors and sebaceous gland tissue — a pathway not obviously connected to renovascular or hypertensive renal pathology.

No mechanistic, preclinical, or clinical evidence in the Evidence Pack establishes a biological pathway between retinoid signalling and malignant renovascular hypertension or malignant hypertensive renal disease. The TxGNN score of 0.99 reflects a strong knowledge-graph link prediction only — it should not be interpreted as mechanistic or clinical evidence.

It should also be noted that the model surfaced two closely related renal-hypertensive diseases (malignant renovascular hypertension and malignant hypertensive renal disease) at the identical score, each appearing twice in the ranked list — consistent with related graph nodes rather than independent corroborating signals.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Denmark Market Information

Isotretinoin currently has no marketing authorisations on file and is **not marketed** in Denmark. No product, dosage form, or approved indication data is available to report.

## Safety Considerations

Safety and warning data (key warnings, contraindications, drug interactions) could not be retrieved for isotretinoin — this is flagged as a **Blocking** data gap in the Evidence Pack, preventing initial safety screening (S1). Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no clinical, literature, or mechanistic evidence connecting isotretinoin to malignant renovascular hypertension or malignant hypertensive renal disease — only a model-derived score is available. Combined with the absence of Denmark market authorisation and a Blocking safety-data gap, the evidence base is insufficient to advance this candidate.

**To proceed, the following is needed:**
- Original indication and mechanism of action (MOA) data (DrugBank)
- SmPC warnings, contraindications, and drug interaction data (Laegemiddelstyrelsen / TFDA) — currently Blocking
- Preclinical or mechanistic rationale linking retinoid pathways to renal-vascular hypertension
- Confirmation of whether the duplicate-scored candidates (malignant renovascular hypertension vs. malignant hypertensive renal disease) represent distinct or overlapping signals before further evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

