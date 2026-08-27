---
layout: default
title: Pegfilgrastim
parent: 僅模型預測 (L5)
nav_order: 335
evidence_level: L5
indication_count: 4
---

# Pegfilgrastim
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

# Pegfilgrastim: From Original Indication Not Documented to Severe Nonproliferative Diabetic Retinopathy

## One-Sentence Summary

Pegfilgrastim (DrugBank DB00019) is a long-acting G-CSF analogue; its original approved indication is not documented in the current evidence pack.
The TxGNN model predicts a possible association with **Severe Nonproliferative Diabetic Retinopathy**,
but this prediction is currently supported by **0 clinical trials** and **0 publications** — it is a pure model output with no corroborating evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in evidence pack (no licenses or original_indications data available) |
| Predicted New Indication | Severe Nonproliferative Diabetic Retinopathy |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L5 |
| Denmark Market Status | Not Marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available for pegfilgrastim in this evidence pack (flagged as a High-severity data gap). Based on the TxGNN model's own rationale, pegfilgrastim is a pegylated G-CSF (granulocyte colony-stimulating factor) analogue whose known action is to stimulate bone marrow neutrophil production and mobilize CD34+ haematopoietic/endothelial progenitor cells into peripheral blood.

The model links this progenitor-mobilization mechanism to retinal vascular remodeling pathways. However, the rationale supplied alongside the prediction is notably cautionary rather than supportive: existing literature on G-CSF use for stem-cell mobilization has reported case-level signals of **worsening proliferative diabetic retinopathy or vitreous haemorrhage** — i.e., a potential risk of disease progression rather than a therapeutic benefit. For severe nonproliferative diabetic retinopathy specifically (a pre-neovascular stage), there is no mechanistic evidence in the pack supporting a treatment effect.

In short, the high TxGNN score reflects a graph-level association, not a validated or even directionally favourable pharmacological rationale — the available mechanistic reasoning points toward a possible safety concern that would need to be ruled out before any therapeutic exploration.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Denmark Market Information

Pegfilgrastim is currently **not marketed** in Denmark, and no marketing authorisations (national or centralised/EMA) are recorded in this evidence pack.

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This prediction rests solely on a TxGNN model score (Evidence Level L5) with zero supporting clinical trials or literature, no confirmed mechanism-of-action data, and no marketing presence in Denmark. The mechanistic rationale that does exist suggests a possible *risk* of retinopathy progression rather than benefit, which further argues against advancing this candidate without additional evidence.

**To proceed, the following is needed:**
- SmPC/label warnings and contraindications for pegfilgrastim (currently a Blocking data gap — required before any S1 safety screening)
- Confirmed mechanism of action and original approved indication(s) from DrugBank or regulatory source
- Preclinical or mechanistic evidence specifically addressing G-CSF effects on non-proliferative (pre-neovascular) diabetic retinopathy, given the existing signal of potential harm in proliferative disease
- Any case reports, registries, or pharmacovigilance data on retinal outcomes in patients receiving pegfilgrastim
- Reassessment of Denmark market/regulatory pathway, since the product currently has no authorisation on record
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

