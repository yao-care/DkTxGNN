---
layout: default
title: Nusinersen
parent: 僅模型預測 (L5)
nav_order: 313
evidence_level: L5
indication_count: 10
---

# Nusinersen
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

# Nusinersen: From Original Indication Not on File to Mixed Mineral Dust Pneumoconiosis

## One-Sentence Summary

Nusinersen's original approved indication is not recorded in this evidence pack (no license or MOA data available). The TxGNN model's top-ranked prediction is **Mixed Mineral Dust Pneumoconiosis**, but the prediction score (50%) sits at the model's non-discriminative baseline, and **0 clinical trials** and **0 publications** currently support this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in evidence pack (no marketing authorisation or label data on file) |
| Predicted New Indication | Mixed Mineral Dust Pneumoconiosis |
| TxGNN Prediction Score | 50.0% |
| Evidence Level | L5 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available for Nusinersen in this evidence pack, and no original indication is on file to compare against. Based on the model's own generated rationale, Nusinersen is understood to act as an antisense oligonucleotide targeting SMN2 pre-mRNA splicing (intron 7 / ISS-N1 region), administered intrathecally, with pharmacological activity confined to central nervous system motor neurons.

Mixed mineral dust pneumoconiosis is an inhalational lung disease driven by macrophage activation and TGF-β–mediated fibrotic/inflammatory pathways — a mechanism with no known overlap with SMN2 splicing regulation. The evidence pack's own mechanistic assessment concludes that a TxGNN score of 0.5 represents an essentially non-discriminative baseline value and does not constitute biological plausibility evidence.

It is also worth noting that all ten of the model's top-ranked predicted indications for this drug carry the identical score of 0.5, spanning unrelated disease areas (pneumoconiosis, rare genetic syndromes, mast cell disorders, food allergy syndromes, tendinopathy). This pattern indicates the model did not find a confidently discriminating signal for Nusinersen in this run, rather than identifying a specific high-confidence repurposing candidate.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Denmark Market Information

Nusinersen is **not marketed** in Denmark according to this evidence pack, and no marketing authorisations (national Laegemiddelstyrelsen or centralised EMA) are on file.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The TxGNN score (0.5) is at the model's non-discriminative baseline — shared identically across all ten top-ranked candidates — and is not corroborated by any clinical trial or literature evidence. There is also no established mechanistic link between Nusinersen's CNS-restricted splicing-modulation activity and mixed mineral dust pneumoconiosis.

**To proceed, the following is needed:**
- Original indication and label/MOA data for Nusinersen (currently a blocking/high-severity data gap)
- Danish/EU regulatory warnings and contraindications (SmPC) to enable a baseline safety review
- A re-run or re-ranking against a higher, more discriminative TxGNN score threshold before this candidate is considered for further evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

