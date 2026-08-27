---
layout: default
title: Risdiplam
parent: 僅模型預測 (L5)
nav_order: 382
evidence_level: L5
indication_count: 10
---

# Risdiplam
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

# Risdiplam: From Spinal Muscular Atrophy to Acne (TxGNN Top-Ranked Prediction)

## One-Sentence Summary

Risdiplam is an SMN2 pre-mRNA splicing modulator used to treat spinal muscular atrophy (SMA); detailed mechanism-of-action data is formally recorded as a data gap in this evidence pack.
The TxGNN model's top prediction is **Acne (disease)** with a **99.45%** score, but this is a pure model-prediction case: **0 clinical trials** and **0 publications** support any of the five predicted indications, and the pack's own mechanistic review flags the high scores as likely artifacts of knowledge-graph hub bias rather than genuine biological signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Spinal Muscular Atrophy (SMA) — referenced in evidence pack rationale; formal MOA record is a data gap |
| Predicted New Indication | Acne (disease) |
| TxGNN Prediction Score | 99.45% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (formally recorded as a data gap, DG002). Based on the information available in this evidence pack, Risdiplam is known as an SMN2 pre-mRNA splicing modulator, increasing functional SMN protein in motor neurons for the treatment of spinal muscular atrophy — a mechanism centered on neuromuscular biology.

None of the five TxGNN-predicted indications in this pack (acne, drug-induced osteoporosis, elevated plasma zinc, common wart, metastatic melanoma) have an established mechanistic connection to SMN2 splicing modulation. The evidence pack's own rationale is explicit about this: it attributes the uniformly high TxGNN scores (97–99%) to likely **hub-disease bias** in the knowledge graph — i.e., these diseases may simply be highly-connected nodes that receive elevated scores across many drugs, rather than genuine drug-disease biology.

Given the absence of MOA data, the absence of any supporting clinical trials or literature, and the model's own flagged concern about hub bias, this candidate set should be treated as exploratory model output only, not as a mechanistically supported repurposing hypothesis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Denmark Market Information

Risdiplam currently holds no marketing authorisations in Denmark (0 licenses on record; market status: Not marketed). No product/dosage-form/indication data is available to tabulate.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

*(Note: TFDA/label warnings and contraindications are recorded as a **Blocking** data gap (DG001) — this prevents a formal Stage 1 safety pre-assessment.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All five predicted indications sit at decision stage S0 with evidence level L5 — model prediction only, with zero clinical trials, zero publications, and no plausible mechanistic link identified. A blocking data gap on label warnings/contraindications additionally prevents any safety pre-assessment.

**To proceed, the following is needed:**
- TFDA/regulatory label warnings and contraindications (blocking gap, required before any S1 safety review)
- Confirmed mechanism of action (MOA) data from DrugBank or primary literature
- Independent verification of whether the high TxGNN scores reflect genuine signal or knowledge-graph hub bias (e.g., compare score distribution against known hub diseases)
- Any preclinical or case-level evidence connecting SMN2 splicing modulation to the predicted indications before further investment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

