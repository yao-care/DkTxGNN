---
layout: default
title: Sargramostim
parent: 僅模型預測 (L5)
nav_order: 392
evidence_level: L5
indication_count: 10
---

# Sargramostim
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

# Sargramostim: From Unspecified Original Indication to Drug-induced Osteoporosis

## One-Sentence Summary

Sargramostim's original approved indication is not recorded in the current evidence pack, and no marketing authorisation exists in Denmark today. The TxGNN model predicts a possible signal for **Drug-induced Osteoporosis**, but this is currently **model prediction only** — **0 clinical trials** and **0 publications** support this specific direction, and the drug's own rationale narrative flags a possible contradictory mechanism.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in current evidence pack |
| Predicted New Indication | Drug-induced Osteoporosis |
| TxGNN Prediction Score | 98.99% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for Sargramostim is not available in this evidence pack. Sargramostim is known generically as a recombinant GM-CSF (granulocyte-macrophage colony-stimulating factor) product, and this identity is reflected in the model's own rationale text rather than in structured MOA data.

The rationale supplied alongside the prediction is explicitly cautious rather than supportive: GM-CSF is understood to modulate bone-marrow stromal cells and osteoclast differentiation, which gives it a theoretical, indirect connection to bone metabolism. However, the same rationale notes that some literature suggests GM-CSF may instead **promote** osteoclast activity — meaning the direction of effect is unclear and could plausibly work *against* an osteoporosis indication rather than for it.

Given this, the mechanistic case here should be read as a hypothesis-generating signal only, not as a coherent pharmacological argument for repurposing. It does not currently rise to a level that would support clinical exploration without further mechanistic and safety data.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Denmark Market Information

Sargramostim currently holds no marketing authorisation in Denmark (0 registered licenses; market status: Not marketed). No Laegemiddelstyrelsen or EMA centralised authorisation data is available in this evidence pack.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information. No drug-drug interaction records were found in the current query (query status: not found, 0 interactions).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate is supported only by an L5 model prediction — there are no clinical trials or literature specific to Sargramostim in drug-induced osteoporosis, and the drug's own mechanistic rationale raises the possibility that GM-CSF could worsen rather than improve osteoclast-driven bone loss. Combined with the absence of any Danish marketing authorisation, there is no basis to advance this candidate at this time.

**To proceed, the following is needed:**
- Danish/EU SmPC warnings and contraindications for Sargramostim (currently a blocking data gap — required before any safety pre-screen)
- Verified mechanism of action data from DrugBank or equivalent source
- Primary literature or preclinical data directly addressing GM-CSF's effect on osteoclast activity and bone density, to resolve the directional uncertainty noted in the rationale
- Confirmation of original approved indication(s), to properly assess similarity/rationale between old and new use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

