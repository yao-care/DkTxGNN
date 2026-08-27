---
layout: default
title: Lorlatinib
parent: 僅模型預測 (L5)
nav_order: 270
evidence_level: L5
indication_count: 10
---

# Lorlatinib
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

# Lorlatinib: From ALK-Positive NSCLC to Gingival Fibromatosis

## One-Sentence Summary

Lorlatinib is a third-generation ALK/ROS1 tyrosine kinase inhibitor (TKI), originally developed for ALK-positive (and ROS1-positive) advanced non-small cell lung cancer (NSCLC). The TxGNN model's top-ranked prediction for this drug is **Gingival Fibromatosis**, but currently **no clinical trials** and **no publications** support this specific prediction — it is a pure computational signal (TxGNN score 99.81%) with no mechanistic corroboration.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | ALK-positive advanced Non-Small Cell Lung Cancer (NSCLC) — inferred from the evidence pack's rationale text; not confirmed via a formal Danish regulatory record in this pack |
| Predicted New Indication | Gingival Fibromatosis |
| TxGNN Prediction Score | 99.81% |
| Evidence Level | L5 (model prediction only, no clinical or literature support) |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in structured form (data gap). Based on the rationale embedded in this evidence pack, Lorlatinib is known to act as an ALK/ROS1 tyrosine kinase inhibitor, and its efficacy in ALK-positive NSCLC is well established.

For this top-ranked prediction, however, the pack's own analysis directly undermines the mechanistic case: gingival fibromatosis is pathologically driven by SOS1 gene mutations or connective-tissue fibrosis pathways, which have no known link to ALK/ROS1 signalling. TxGNN assigned a very high similarity score (99.81%), but there is no biological or clinical rationale connecting Lorlatinib's known pharmacology to this indication — this is a network-embedding artifact rather than a substantiated repurposing signal.

For transparency: this evidence pack also contains other candidate indications for Lorlatinib (lung hilum carcinoma, lung benign neoplasm) that carry actual literature. Those, too, warrant caution — lung hilum carcinoma is supported by only a single case report, and the 20 publications attached to "lung benign neoplasm" are, per the pack's own annotation, entirely about malignant ALK-positive NSCLC (Lorlatinib's already-approved indication), suggesting a disease-ontology mapping error in TxGNN rather than a genuine new-indication signal. None of this literature applies to the gingival fibromatosis prediction discussed here.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Denmark Market Information

Lorlatinib currently holds no marketing authorisation in Denmark (0 licenses on record); market status is "not marketed."

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (ALK/ROS1 tyrosine kinase inhibitor) |
| Myelosuppression Risk | Please refer to the Summary of Product Characteristics (SmPC) warnings and precautions |
| Emetogenicity Classification | Please refer to the Summary of Product Characteristics (SmPC) warnings and precautions |
| Monitoring Items | Please refer to the Summary of Product Characteristics (SmPC) warnings and precautions |
| Handling Protection | As an oral antineoplastic agent, handle per institutional hazardous-drug precautions; refer to SmPC for specific handling instructions |

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information. (No structured key warnings, contraindications, or drug-drug interaction data were retrievable for this evidence pack; local label warnings are flagged as a Blocking data gap.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (gingival fibromatosis) has no clinical trial or literature support and, per the pack's own mechanistic analysis, no plausible biological link to Lorlatinib's ALK/ROS1 pharmacology — this is an L5, model-only signal.

**To proceed, the following is needed:**
- Danish/local label warnings and contraindications (currently a Blocking data gap)
- Formal DrugBank mechanism-of-action data (currently a High-severity data gap)
- Preclinical or mechanistic evidence directly linking ALK/ROS1 inhibition to gingival fibromatosis pathology before this candidate can advance past S0
- Resolution of the apparent TxGNN disease-ontology mapping error affecting the "lung benign neoplasm" candidate in this same pack, before that candidate is separately evaluated
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

