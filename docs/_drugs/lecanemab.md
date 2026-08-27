---
layout: default
title: Lecanemab
parent: 僅模型預測 (L5)
nav_order: 258
evidence_level: L5
indication_count: 10
---

# Lecanemab
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

# Lecanemab: From Alzheimer's Disease to Diabetic Cataract

## One-Sentence Summary

Lecanemab is a monoclonal antibody targeting amyloid-beta protofibrils, originally developed for Alzheimer's disease. The TxGNN model predicts it may be effective for **diabetic cataract**, but currently **0 clinical trials** and **0 publications** support this direction — the prediction rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Alzheimer's disease (amyloid-beta clearance; not recorded as a formal Danish-approved indication text since the drug is not marketed here) |
| Predicted New Indication | Diabetic cataract |
| TxGNN Prediction Score | 98.48% |
| Evidence Level | L5 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

A formal, structured mechanism-of-action record is not available in DrugBank for this entry. However, the model's own rationale describes the mechanism: Lecanemab is a humanized monoclonal antibody that binds soluble amyloid-beta (Aβ) protofibrils, promoting their clearance from the brain — its established role is reducing Aβ aggregate burden in Alzheimer's disease.

The link to diabetic cataract is conceptual rather than direct. Diabetic cataract pathology involves lens crystallin proteins that misfold and aggregate under oxidative stress and glycation, clouding the lens. Both conditions therefore involve "protein misfolding and aggregation," which is likely what drove the similarity signal in TxGNN's knowledge-graph embeddings.

This conceptual overlap does not translate into a plausible clinical mechanism. Lecanemab's antibody epitope is specific to the Aβ peptide, structurally unrelated to lens crystallins, so target engagement in the lens is unlikely. Furthermore, Lecanemab is a large-molecule biologic with no established route to cross the blood-aqueous or blood-retinal barrier and reach the lens; no ocular formulation or delivery pathway exists. This should be read as a knowledge-graph similarity-driven hypothesis, not a mechanistically supported prediction.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Denmark Market Information

Lecanemab currently has no marketing authorisation in Denmark (market status: not marketed; 0 authorisations on record).

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information. No drug-drug interaction data were found in the queried sources.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a TxGNN similarity score (L5, decision stage S0) with no clinical trials, no literature, and a biologically weak mechanistic rationale — a large-molecule antibody with no plausible route to the lens.

**To proceed, the following is needed:**
- Verified mechanism-of-action data for Lecanemab (DrugBank API or manufacturer SmPC)
- Danish/EU product label (SmPC) with warnings, contraindications, and DDI data once available
- Preclinical evidence of ocular biodistribution or target engagement before any further evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

