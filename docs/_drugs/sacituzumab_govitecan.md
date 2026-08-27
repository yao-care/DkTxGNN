---
layout: default
title: Sacituzumab Govitecan
parent: 僅模型預測 (L5)
nav_order: 391
evidence_level: L5
indication_count: 10
---

# Sacituzumab Govitecan
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

# Sacituzumab Govitecan: From Antineoplastic ADC Therapy to Drug-Induced Osteoporosis

## One-Sentence Summary

Sacituzumab govitecan is a Trop-2-targeted antibody-drug conjugate (ADC) used in antineoplastic therapy; the specific original oncology indication is not recorded in this evidence pack. The TxGNN model predicts it may be effective for **Drug-Induced Osteoporosis**, but this direction is currently supported by **0 clinical trials** and **0 publications**, and is a model-prediction-only signal (L5).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in this evidence pack (drug class: antineoplastic ADC; specific indication data missing) |
| Predicted New Indication | Drug-Induced Osteoporosis |
| TxGNN Prediction Score | 99.78% |
| Evidence Level | L5 (model prediction only — no clinical trials or literature found) |
| Denmark Market Status | Not marketed (未上市) |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not populated in the dedicated MOA field of this evidence pack, but the repurposing rationale attached to each candidate describes the mechanism: Sacituzumab govitecan is an antibody-drug conjugate directed against Trop-2, a cell-surface glycoprotein overexpressed on epithelial tumours, and it delivers SN-38 — the active topoisomerase I inhibitor metabolite of irinotecan — directly into tumour cells, where it causes DNA damage and cell death. This places the drug in the conventional cytotoxic chemotherapy class, delivered via an ADC targeting mechanism, and its established use is oncology-focused tumour cell killing.

Notably, the evidence pack's own mechanistic assessment for this candidate is explicitly skeptical rather than supportive: it states there is no known link between Trop-2/SN-38 cytotoxicity and bone remodeling pathways (osteoclast/osteoblast regulation), and further notes that cytotoxic chemotherapy agents are, if anything, a **known risk factor for causing** drug-induced bone loss — i.e., the mechanistic direction runs opposite to a therapeutic effect on osteoporosis. The same caveat applies to the other TxGNN-ranked candidates in this pack (severe nonproliferative diabetic retinopathy, diabetic retinopathy, diabetic cataract, cortical cataract, nuclear senile cataract): none have a plausible mechanistic connection to Trop-2/SN-38 cytotoxicity, and none are backed by any retrieved trial or literature evidence.

In short, this is a case where the TxGNN similarity score is high, but the underlying mechanistic rationale and evidentiary base are weak-to-contradictory. This should be weighted heavily in the decision below.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Denmark Market Information

Sacituzumab govitecan currently has **no marketing authorisation in Denmark** — 0 licenses on record (national Laegemiddelstyrelsen or centralised EU/EMA), and market status is listed as "Not marketed."

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Antibody-drug conjugate (ADC) with conventional cytotoxic payload (topoisomerase I inhibitor, SN-38) |
| Myelosuppression Risk | Not provided in this evidence pack (data gap DG001, TFDA/SmPC warning data pending); SN-38-class topoisomerase I inhibitor payloads are class-associated with neutropenia — confirm via SmPC once available |
| Emetogenicity Classification | Not provided in this evidence pack; refer to SmPC (SN-38-class agents are typically moderate-to-high emetogenic risk) |
| Monitoring Items | CBC with differential (neutrophil count), liver and renal function, infusion-reaction monitoring |
| Handling Protection | Yes — cytotoxic drug handling precautions required (ADC with cytotoxic payload) |

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The prediction is L5 (model score only) with zero corroborating clinical trials or literature, the drug has no Danish marketing authorisation, and the pack's own mechanistic analysis indicates the cytotoxic ADC mechanism is not plausibly linked to — and may work against — the predicted indication (drug-induced osteoporosis and the other candidate diseases).

**To proceed, the following is needed:**
- TFDA/SmPC label warnings and contraindications (data gap DG001, currently Blocking — required before any S1 safety screening)
- Confirmed original indication and mechanism-of-action data (data gap DG002)
- Independent mechanistic or preclinical evidence connecting Trop-2/SN-38 activity to bone metabolism before further evaluation is warranted
- Re-screening of clinical trial and literature databases as new evidence emerges
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

