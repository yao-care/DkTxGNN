---
layout: default
title: Tralokinumab
parent: 僅模型預測 (L5)
nav_order: 444
evidence_level: L5
indication_count: 10
---

# Tralokinumab
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

# Tralokinumab: From Atopic Dermatitis to Diabetic Cataract

## One-Sentence Summary

Tralokinumab is an anti-IL-13 monoclonal antibody, originally used to treat atopic dermatitis. The TxGNN model predicts it may be effective for **Diabetic Cataract**, with a prediction score of **98.69%**, but currently **no clinical trials and no published literature** support this direction — the signal is driven purely by knowledge-graph topology.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Atopic dermatitis (per internal mechanistic note; not confirmed via formal regulatory data — original indication field and licenses are empty in this evidence pack) |
| Predicted New Indication | Diabetic Cataract |
| TxGNN Prediction Score | 98.69% |
| Evidence Level | L5 (model prediction only, no clinical trials or literature) |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a Blocking/High-severity data gap). Based on the limited information available, Tralokinumab is an anti-IL-13 monoclonal antibody whose efficacy has been established in atopic dermatitis, an IL-13/Th2-driven inflammatory condition.

A hypothesized — but unconfirmed — mechanistic bridge exists between IL-13/Th2 signaling and diabetes-related tissue damage: TGF-β/fibrosis pathways have been proposed in the literature as potentially relevant to lens epithelial pathology. However, there is no direct molecular evidence that IL-13 inhibition affects cataract formation or lens metabolism.

Several of the other top-ranked predicted indications (tetanic cataract, craniostenosis cataract) involve mechanisms — electrolyte disturbance, developmental/skeletal gene abnormalities — that have no known biological relationship to IL-13 signaling at all. This suggests the prediction is being driven largely by network topology/similarity in the knowledge graph rather than an established pharmacological rationale, which is consistent with the L5 evidence level assigned.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Denmark Market Information

Currently no marketing authorisations registered in Denmark (market status: Not marketed; 0 licenses on file).

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication is supported by TxGNN score alone (Evidence Level L5), with zero clinical trials, zero literature, no confirmed mechanism of action, and no Danish market presence. There is currently no basis to advance this candidate beyond hypothesis generation.

**To proceed, the following is needed:**
- Mechanism of action (MOA) data for Tralokinumab (currently a Blocking-severity data gap)
- Danish/EU Summary of Product Characteristics (SmPC) — warnings, contraindications, drug interactions
- Preclinical or mechanistic studies establishing a biological link between IL-13 inhibition and cataract/lens pathology
- Confirmation of original approved indication(s) and any existing Danish or EU marketing authorisation status
- Resolution of duplicate/overlapping predicted indications (several ranked candidates are the same or closely related cataract subtypes) before further prioritization
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

