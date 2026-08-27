---
layout: default
title: Ocrelizumab
parent: 僅模型預測 (L5)
nav_order: 317
evidence_level: L5
indication_count: 10
---

# Ocrelizumab
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

# Ocrelizumab: From Multiple Sclerosis to HER2 Positive Breast Carcinoma

## One-Sentence Summary

> Ocrelizumab is an anti-CD20 monoclonal antibody whose established use is B-lymphocyte depletion in multiple sclerosis.
> The TxGNN model predicts it may be effective for **HER2 Positive Breast Carcinoma**,
> but currently **0 clinical trials** and **0 publications** support this specific prediction, and the model's own rationale flags the score as likely a knowledge-graph embedding artefact rather than a genuine mechanistic signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Multiple Sclerosis (per mechanistic rationale in the evidence pack; no formal Danish licence text is available — see Denmark Market Information) |
| Predicted New Indication | HER2 Positive Breast Carcinoma |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the current evidence pack (flagged as a High-severity data gap). Based on the repurposing rationale generated alongside the prediction, Ocrelizumab is an anti-CD20 monoclonal antibody that depletes B lymphocytes and is established for multiple sclerosis.

The evidence pack's own mechanistic assessment is explicitly skeptical of this prediction: it states that CD20/B-cell depletion has no known intersection with the HER2/ERBB2 signalling pathway that drives HER2-positive breast carcinoma, and no mechanistic literature links B-cell depletion to direct suppression of HER2-driven tumours. The assessment concludes that the high TxGNN score more likely reflects knowledge-graph embedding similarity than a real biological mechanism.

This concern is reinforced by the pattern across all five unique predicted diseases in this candidate set (HER2-positive breast carcinoma, normal breast-like subtype, PR-positive breast cancer, luminal A/B breast tumour, PR-negative breast cancer): none has a plausible mechanistic link to CD20/B-cell depletion, and the one indication that did return literature hits (luminal A/B, 19 PubMed records) was found on review to consist entirely of off-topic papers (B-cell biology, hepatitis B vaccines, HLA-B serology) — apparent false positives from a keyword "B" match rather than substantive evidence. Given this, the mechanistic case for repurposing Ocrelizumab toward any of these breast cancer subtypes is currently unsupported.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Denmark Market Information

No marketing authorisation is currently registered for Ocrelizumab in Denmark (0 licences on file in this evidence pack).

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication has a very high TxGNN score but zero supporting clinical trials or literature, and the evidence pack's own mechanistic analysis concludes the score likely reflects an embedding artefact rather than true biological plausibility — the same pattern holds across all candidate breast cancer subtypes in this set, including one indication where the retrieved literature turned out to be an unrelated keyword-matching artefact.

**To proceed, the following is needed:**
- Confirmed mechanism of action (MOA) data for Ocrelizumab (currently a data gap)
- Danish/EU SmPC warnings, contraindications, and drug interaction data (currently a blocking data gap)
- Independent preclinical or mechanistic evidence connecting CD20/B-cell depletion to HER2-driven tumour biology before further evaluation is warranted
- Re-query of literature and trial databases using disambiguated search terms to rule out further keyword-matching noise in this candidate set
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

