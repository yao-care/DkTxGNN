---
layout: default
title: Ripretinib
parent: 僅模型預測 (L5)
nav_order: 380
evidence_level: L5
indication_count: 10
---

# Ripretinib
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

# Ripretinib: From Original Indication (Data Pending) to Multiple Endocrine Neoplasia

## One-Sentence Summary

> Ripretinib (DrugBank DB14840) is not currently marketed in Denmark, and its original approved indication is not available in this evidence pack.
> The TxGNN model's top-ranked prediction is **Multiple Endocrine Neoplasia (MEN)**, with a prediction score of **98.84%**,
> but this is supported by **0 clinical trials** and **0 publications**, and the model's own rationale flags a weak mechanistic link.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | No data available (not registered in Denmark; no original indication text provided) |
| Predicted New Indication | Multiple Endocrine Neoplasia |
| TxGNN Prediction Score | 98.84% |
| Evidence Level | L5 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for ripretinib is not available in this evidence pack (marked as a data gap, severity: High). What is available is the model's own rationale text, which identifies ripretinib as a **switch-control KIT/PDGFRA tyrosine kinase inhibitor**.

Multiple Endocrine Neoplasia (particularly MEN2) is primarily driven by **RET** mutations, not KIT/PDGFRA — a different receptor tyrosine kinase branch. The evidence pack's own rationale for this prediction explicitly states there is no direct target overlap between ripretinib's known pharmacology and MEN's driver gene, and that the prediction is based purely on TxGNN knowledge-graph embedding similarity, with no supporting trial or literature evidence.

Notably, several other TxGNN-ranked candidates for this drug (malignant catarrh, infectious bovine rhinotracheitis) are **veterinary/bovine diseases**, not human indications — suggesting disease-ontology noise in the underlying knowledge graph for this candidate. This further lowers confidence that the raw ranking reflects a biologically meaningful signal for ripretinib specifically, and reinforces treating the MEN prediction as hypothesis-generating only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Denmark Market Information

Ripretinib is not currently marketed in Denmark. No marketing authorisations (national or centralised/EMA) are on record in this evidence pack.

---

## Cytotoxicity

Ripretinib is characterized in the evidence pack's rationale as a KIT/PDGFRA switch-control tyrosine kinase inhibitor, consistent with a targeted (non-classical-cytotoxic) small-molecule anticancer agent.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (KIT/PDGFRA tyrosine kinase inhibitor) |
| Myelosuppression Risk | Please refer to the Summary of Product Characteristics (SmPC) warnings and precautions |
| Emetogenicity Classification | Please refer to the Summary of Product Characteristics (SmPC) warnings and precautions |
| Monitoring Items | Please refer to the Summary of Product Characteristics (SmPC) warnings and precautions |
| Handling Protection | Please refer to the Summary of Product Characteristics (SmPC) warnings and precautions |

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information. Note: regulatory warnings/contraindications data (e.g. TFDA/SmPC labelling) are flagged as a **blocking data gap** in this evidence pack and must be obtained before any safety evaluation can proceed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top-ranked predicted indication (MEN) has zero clinical trial or literature support, an evidence level of L5 (model prediction only), and the model's own rationale identifies a weak/unconfirmed mechanistic link (RET-driven disease vs. a KIT/PDGFRA-targeted drug). The drug is also not currently marketed in Denmark, and core safety labelling data is missing (blocking gap).

**To proceed, the following is needed:**
- Ripretinib's official mechanism of action and original approved indication (currently a data gap)
- Danish/EU SmPC warnings, contraindications, and precautions (currently a blocking data gap — required before any safety evaluation)
- Independent mechanistic or preclinical validation of a RET/KIT-PDGFRA connection before pursuing MEN as a repurposing hypothesis
- Re-screening of the full TxGNN candidate list for this drug to filter out non-human (veterinary) disease entries before further evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

