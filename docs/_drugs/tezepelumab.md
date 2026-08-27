---
layout: default
title: Tezepelumab
parent: 僅模型預測 (L5)
nav_order: 428
evidence_level: L5
indication_count: 10
---

# Tezepelumab
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

# Tezepelumab: From Severe Asthma to Diabetic Cataract

## One-Sentence Summary

Tezepelumab is an anti-TSLP monoclonal antibody; its established indication is Type 2 inflammation-driven severe asthma, though formal Danish label data on this original indication is currently unavailable. The TxGNN model predicts possible efficacy for **Diabetic Cataract**, but this prediction is currently supported by **0 clinical trials** and **0 publications**, and the evidence pack's own mechanistic review flags it as a likely false-positive graph artifact rather than a biologically grounded signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Severe asthma (Type 2 inflammation-driven) — per model rationale; formal Danish label text unavailable (data gap) |
| Predicted New Indication | Diabetic Cataract |
| TxGNN Prediction Score | 98.40% |
| Evidence Level | L5 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this evidence pack (data gap, High severity). Based on the mechanistic notes accompanying the prediction, Tezepelumab is an anti-TSLP (thymic stromal lymphopoietin) monoclonal antibody, with its proven efficacy limited to Type 2 inflammation-driven severe asthma.

There is no known direct biological pathway connecting TSLP signalling to cataract pathophysiology, which involves lens protein denaturation, oxidative stress, and the polyol pathway. The evidence pack's own repurposing rationale explicitly characterizes this high score (0.984) as likely arising from an indirect knowledge-graph connection through a shared "diabetes" node, rather than from a genuine pharmacological mechanism — i.e., the model itself flags this as a probable false positive.

Given the absence of both a plausible mechanistic link and any supporting clinical or literature evidence, this prediction should be treated as exploratory only and not as a basis for further mechanistic or clinical investment at this time.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Denmark Market Information

Tezepelumab currently holds no marketing authorisations in Denmark (0 licenses on record; market status: Not marketed).

---

## Safety Considerations

Please refer to the approved EU Summary of Product Characteristics (SmPC), as this product does not currently hold a Danish marketing authorisation and no drug interaction, warning, or contraindication data is available in this evidence pack. Note also that Danish-specific label/warning data (e.g., equivalent to TFDA label warnings) is flagged as a **Blocking** data gap, meaning a formal safety pre-screen cannot yet be completed for this candidate.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no clinical or literature evidence supporting this indication, and the evidence pack's own mechanistic analysis identifies the prediction as a likely knowledge-graph artifact rather than a biologically plausible signal. The drug is also not marketed in Denmark, and a blocking safety data gap prevents any initial safety screening.

**To proceed, the following is needed:**
- Danish/EU label safety data (warnings, contraindications) to resolve the blocking data gap
- Confirmed mechanism of action via DrugBank or manufacturer SmPC
- Independent mechanistic or preclinical evidence linking TSLP/Type 2 inflammation pathways to cataract pathophysiology, before pursuing clinical trial or literature searches further
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

