---
layout: default
title: Sparsentan
parent: 僅模型預測 (L5)
nav_order: 407
evidence_level: L5
indication_count: 10
---

# Sparsentan
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

# Sparsentan: From an Unconfirmed Original Indication to Alopecia

## One-Sentence Summary

Sparsentan (DrugBank DB12548) is a dual endothelin type A (ETA) / angiotensin II type 1 (AT1) receptor antagonist; its original approved indication is not documented in the current evidence pack. The TxGNN model predicts a possible signal for **Alopecia**, but this prediction is currently supported by **0 clinical trials** and **0 publications**, and the model's own mechanistic rationale characterizes the drug–disease link as speculative rather than validated.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no marketing authorisation or approved indication text in the current evidence pack |
| Predicted New Indication | Alopecia |
| TxGNN Prediction Score | 94.52% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Denmark Market Status | Not Marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action documentation is not available in the current evidence pack (flagged as a High-severity data gap, DG002). Based on the mechanistic rationale accompanying this prediction, Sparsentan is known to act as a dual ETA (endothelin receptor type A) and AT1 (angiotensin II type 1 receptor) antagonist.

The renin-angiotensin system (RAS) and endothelin signalling have been reported, in scattered exploratory studies, to play local paracrine roles in follicular microvascular supply and hair cycle regulation. However, the evidence pack's own assessment explicitly notes that the causal link between systemic ETA/AT1 blockade and alopecia treatment is weak and speculative — this is **not** a validated mechanism, and the high TxGNN score should not be read as mechanistic confirmation.

It is also worth noting that this candidate list contains several related but questionable signals: two entries for hereditary/structural hair-loss conditions (congenital hypotrichosis milia, hypotrichosis simplex of the scalp) that the rationale attributes to likely knowledge-graph clustering artifacts rather than genuine pharmacological relevance, and an angioedema signal that the rationale flags as a possible **inverted safety signal** (RAS-blocking drugs are a known clinical risk factor for angioedema, not a treatment) rather than a therapeutic opportunity. This context reinforces that the Alopecia signal should be treated as a low-confidence, model-only hypothesis at this stage.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Denmark Market Information

Sparsentan currently has no marketing authorisations registered in Denmark (0 licenses on file; market status: Not Marketed).

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

*Note: A Blocking-severity data gap (DG001) has been identified — local product label warnings/contraindications have not yet been retrieved, which prevents a formal safety pre-assessment (S1 stage) for this candidate.*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate is supported only by a TxGNN model score (L5 evidence level), with no clinical trials, literature, or Danish market presence to corroborate it. The evidence pack's own mechanistic rationale describes the drug–disease link as speculative rather than established, and a Blocking-severity data gap (missing product label/safety data) prevents even an initial safety screen.

**To proceed, the following is needed:**
- Retrieval of the approved product label / SmPC warnings and contraindications (resolves DG001, currently blocking)
- Confirmation of detailed mechanism-of-action data via DrugBank or primary literature (resolves DG002)
- Preclinical or mechanistic studies specifically examining RAS/endothelin signalling in hair follicle biology
- Any clinical trial or case-level data evaluating Sparsentan (or the ETA/AT1 dual-antagonist class) in alopecia, to move this candidate beyond a model-only (L5) evidence level
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

