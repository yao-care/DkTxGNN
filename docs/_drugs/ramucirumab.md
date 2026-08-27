---
layout: default
title: Ramucirumab
parent: 僅模型預測 (L5)
nav_order: 365
evidence_level: L5
indication_count: 10
---

# Ramucirumab
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

# Ramucirumab: From Advanced Solid Tumours to Uterine Ligament Adenocarcinoma

## One-Sentence Summary

Ramucirumab is an anti-VEGFR2 monoclonal antibody whose antitumour effect through blockade of tumour angiogenesis is established in gastric cancer, NSCLC, hepatocellular carcinoma and colorectal cancer (per the mechanistic rationale in this evidence pack; not independently confirmed via structured indication data in this pack). The TxGNN model predicts it may be effective for **uterine ligament adenocarcinoma**, but currently **0 clinical trials** and **0 publications** support this specific direction — this is a model-prediction-only signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not confirmed in this evidence pack (structured field empty); mechanistic rationale references established use in gastric cancer, NSCLC, hepatocellular carcinoma and colorectal cancer |
| Predicted New Indication | Uterine ligament adenocarcinoma |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L5 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

The `original_moa` field for Ramucirumab is not populated in this evidence pack (flagged as a High-severity data gap, DG002 — pending DrugBank API lookup). However, the repurposing rationale attached to the top prediction describes Ramucirumab as an anti-VEGFR2 monoclonal antibody that inhibits tumour angiogenesis, a mechanism already validated across multiple solid tumours including gastric cancer, NSCLC, hepatocellular carcinoma and colorectal cancer.

Uterine ligament adenocarcinoma is a rare gynaecological malignancy. The mechanistic link proposed here is a broad extrapolation from anti-angiogenic activity in other solid tumours, rather than a disease-specific finding — the evidence pack explicitly notes there is no direct data on VEGFR2 expression or angiogenesis-dependence in this specific tumour type, so the connection "cannot be established as a specific link" beyond general class-level plausibility.

Because there are no clinical trials or publications testing Ramucirumab in this indication, the mechanistic argument currently stands alone as the entire evidentiary basis for the prediction.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Denmark Market Information

Ramucirumab currently has **no marketing authorisations on record** in this evidence pack (`total_licenses: 0`, `market_status: 未上市` / Not marketed). No licence table can be produced.

---

## Cytotoxicity

Ramucirumab is an antineoplastic monoclonal antibody (anti-VEGFR2, anti-angiogenic class), so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (anti-VEGFR2 monoclonal antibody, antiangiogenic) |
| Myelosuppression Risk | Please refer to the Summary of Product Characteristics (SmPC) warnings and precautions |
| Emetogenicity Classification | Please refer to the Summary of Product Characteristics (SmPC) warnings and precautions |
| Monitoring Items | Please refer to the Summary of Product Characteristics (SmPC) warnings and precautions |
| Handling Protection | Please refer to the Summary of Product Characteristics (SmPC) warnings and precautions |

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information. Note: the evidence pack flags a **Blocking**-severity data gap (DG001) — TFDA/SmPC-level warnings and contraindications are not yet available, which by itself prevents this candidate from entering the S1 safety pre-assessment stage.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- Evidence level is L5 (model prediction only) — there are zero clinical trials and zero publications supporting Ramucirumab in uterine ligament adenocarcinoma, and the mechanistic link is a generic class-level extrapolation rather than a disease-specific finding. Combined with a Blocking-severity safety data gap, the candidate cannot proceed further at this time.

**To proceed, the following is needed:**
- TFDA/SmPC-sourced warnings and contraindications (DG001, Blocking) — required before any S1 safety pre-assessment
- Confirmed mechanism of action from DrugBank (DG002)
- Disease-specific supporting evidence (preclinical, case reports, or trials) for VEGFR2/angiogenesis relevance in uterine ligament adenocarcinoma specifically, given its rarity and the lack of any registered studies
- Clarification of Ramucirumab's confirmed original indication(s), since the structured `original_indications` field in this pack is currently empty
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

