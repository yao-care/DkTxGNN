---
layout: default
title: Travoprost
parent: 僅模型預測 (L5)
nav_order: 448
evidence_level: L5
indication_count: 10
---

# Travoprost
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

# Travoprost: From Glaucoma/Ocular Hypertension to Visceral Calciphylaxis

## One-Sentence Summary

Travoprost is a prostaglandin F2α analogue used to lower intraocular pressure in glaucoma and ocular hypertension (mechanism and trial context reconstructed from the evidence pack, as structured MOA/indication fields were not populated). The TxGNN model predicts it may be effective for **Visceral Calciphylaxis**, but this prediction is currently supported by **no clinical trials** and **no published literature** — it is a pure model signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Glaucoma / Ocular Hypertension (reconstructed from trial evidence; not present in structured regulatory data) |
| Predicted New Indication | Visceral Calciphylaxis |
| TxGNN Prediction Score | 99.9998% |
| Evidence Level | L5 |
| Denmark Market Status | Not Marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in structured form. Based on information embedded in the evidence pack's clinical trial records and rationale notes, Travoprost is a prostaglandin F2α analogue (prodrug, hydrolyzed to its active acid form) that selectively agonizes the FP prostanoid receptor, lowering intraocular pressure by increasing uveoscleral outflow — its established use is in open-angle glaucoma and ocular hypertension.

Visceral calciphylaxis is a small-vessel calcification disorder leading to ischemic tissue necrosis, involving vascular smooth muscle calcification and coagulation abnormalities. According to the repurposing rationale supplied with this candidate, **there is no known physiological link** between this pathway and Travoprost's FP-receptor/IOP-lowering mechanism.

This candidate ranks #1 by TxGNN score, but the model's own supporting rationale explicitly states the association is unsupported by any clinical trial or literature evidence — it reflects a high embedding-similarity signal only, not a mechanistically or clinically grounded hypothesis.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This is an L5-evidence candidate — a model prediction with no supporting clinical trials, no literature, and no established mechanistic link between Travoprost's FP-receptor pathway and calciphylaxis pathophysiology. The drug is also not currently marketed in Denmark, and safety labeling data needed for even a preliminary safety screen is missing (blocking data gap).

**To proceed, the following is needed:**
- Confirmed mechanism of action (MOA) data from DrugBank or SmPC
- Danish/EU product labeling (warnings, contraindications) to clear the current blocking data gap (DG001)
- Preclinical or mechanistic studies linking prostaglandin FP-receptor activity to vascular calcification pathways
- If pursued, an initial preclinical/in vitro feasibility study before any clinical evidence generation, given the complete absence of supporting data

*Note: Among the other candidates in this evidence pack, "vascular disease" (rank 9–10, L4) has substantially more evidence (15 clinical trials, 20 publications) but that evidence is graded low-relevance (Grade C) — the trials are glaucoma/IOP studies incidentally involving Travoprost, not vascular-disease treatment trials. It may warrant separate evaluation but was not the top-ranked candidate and is outside the scope of this report.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

