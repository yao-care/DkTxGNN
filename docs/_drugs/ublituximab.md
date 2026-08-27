---
layout: default
title: Ublituximab
parent: 僅模型預測 (L5)
nav_order: 460
evidence_level: L5
indication_count: 10
---

# Ublituximab
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

# Ublituximab: From Multiple Sclerosis to Diabetic Cataract

## One-Sentence Summary

Ublituximab is a third-generation anti-CD20 monoclonal antibody, known to be approved for multiple sclerosis via B-cell depletion (Denmark-specific licensing data is not available in this evidence pack). The TxGNN model predicts it may be effective for **Diabetic Cataract**, but currently **0 clinical trials** and **0 publications** support this direction, and the evidence pack itself flags the prediction as a likely false positive.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Multiple Sclerosis (based on known drug classification; no Danish licence data available) |
| Predicted New Indication | Diabetic Cataract |
| TxGNN Prediction Score | 98.57% |
| Evidence Level | L5 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Ublituximab is a third-generation anti-CD20 monoclonal antibody. Its mechanism of action is B-cell depletion, and it is approved for the treatment of multiple sclerosis.

Diabetic cataract, by contrast, is primarily driven by non-enzymatic glycation of lens proteins, sorbitol (polyol pathway) accumulation, and oxidative stress leading to protein aggregation and lens opacification. There is no established mechanistic link between B-cell–mediated immune pathways and this lens pathology.

Given the very high TxGNN score (0.986) combined with the complete absence of supporting clinical trials or literature, the evidence pack itself assesses this as a likely **false positive arising from topological similarity in the knowledge-graph embedding space**, rather than a biologically grounded signal. The same caveat applies to the other cataract-subtype predictions in this evidence pack (mature, tetanic, craniostenosis, and immature cataract), none of which have a plausible mechanistic connection to anti-CD20 immunotherapy.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Denmark Market Information

Ublituximab is not currently marketed in Denmark, and no marketing authorisations (national or EMA centralised) are on record in this evidence pack.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high, but there are zero supporting clinical trials or publications, and the mechanistic rationale in this evidence pack itself identifies the signal as a probable embedding-space artefact rather than a biologically plausible link between anti-CD20 B-cell depletion and diabetic cataract pathology.

**To proceed, the following is needed:**
- Confirmed mechanism of action (MOA) data from DrugBank or the SmPC
- A biological plausibility review specifically addressing lens/ocular pathology pathways
- Danish/EU regulatory data (licences, indications) to establish original-indication baseline
- Preclinical or observational evidence before any further evaluation stage
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

