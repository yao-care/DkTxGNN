---
layout: default
title: Tafasitamab
parent: 僅模型預測 (L5)
nav_order: 415
evidence_level: L5
indication_count: 10
---

# Tafasitamab
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

# Tafasitamab: From Diffuse Large B-Cell Lymphoma to Drug-Induced Osteoporosis

## One-Sentence Summary

Tafasitamab is an anti-CD19 monoclonal antibody used (in combination with lenalidomide) for relapsed/refractory diffuse large B-cell lymphoma (DLBCL). The TxGNN model predicts it may be effective for **drug-induced osteoporosis**, but this direction is currently supported by **0 clinical trials** and **0 publications** — it is a model-generated hypothesis only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not registered in Denmark; per DrugBank, approved (with lenalidomide) for relapsed/refractory diffuse large B-cell lymphoma (DLBCL) |
| Predicted New Indication | Drug-induced osteoporosis |
| TxGNN Prediction Score | 98.71% |
| Evidence Level | L5 |
| Denmark Market Status | Not marketed (未上市) |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in a structured field. Based on the available rationale, Tafasitamab is a humanized, Fc-modified anti-CD19 monoclonal antibody that eliminates B-cells via ADCC, ADCP, CDC, and direct apoptosis induction. It is approved for use in combination with lenalidomide for relapsed/refractory DLBCL.

The theoretical link to drug-induced osteoporosis rests on the observation that B-cells can secrete RANKL, a driver of osteoclast activation, so B-cell depletion could in principle influence bone metabolism. However, drug-induced osteoporosis in clinical practice is typically caused by corticosteroids or cytotoxic chemotherapy, not by CD19-targeted immunotherapy — there is no established pathological connection between these mechanisms.

This means the prediction most likely reflects an indirect association at the embedding level of the knowledge graph, rather than a validated biological mechanism. No clinical or published evidence currently supports this link.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Denmark Market Information

Tafasitamab currently holds no marketing authorisation in Denmark (0 licenses on record); the drug is not marketed in this jurisdiction.

---

## Cytotoxicity

Tafasitamab is an antineoplastic agent (approved for DLBCL, a malignant lymphoma), so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted immunotherapy (anti-CD19, Fc-engineered monoclonal antibody; ADCC/ADCP/CDC-mediated) |
| Myelosuppression Risk | Please refer to the Summary of Product Characteristics (SmPC) warnings and precautions |
| Emetogenicity Classification | Please refer to the Summary of Product Characteristics (SmPC) warnings and precautions |
| Monitoring Items | Please refer to the Summary of Product Characteristics (SmPC) warnings and precautions |
| Handling Protection | Please refer to the Summary of Product Characteristics (SmPC) warnings and precautions |

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is based solely on TxGNN model scoring (L5) with no supporting clinical trials or literature, and the proposed mechanistic link to drug-induced osteoporosis is biologically weak and unvalidated. In addition, Denmark-specific regulatory and safety data (SmPC warnings/contraindications) are currently unavailable, blocking initial safety screening (S1).

**To proceed, the following is needed:**
- TFDA/Danish SmPC warnings, contraindications, and DDI data (currently blocking — DG001)
- Confirmed original indication and detailed mechanism of action documentation (DG002)
- Preclinical or mechanistic studies examining B-cell depletion and bone metabolism/RANKL pathway
- Any emerging case reports, registries, or trial signals specifically linking tafasitamab to bone density outcomes
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

