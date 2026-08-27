---
layout: default
title: Tisagenlecleucel
parent: 僅模型預測 (L5)
nav_order: 437
evidence_level: L5
indication_count: 10
---

# Tisagenlecleucel
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

# Tisagenlecleucel: From CD19+ B-Cell Malignancies to Crohn's Colitis

## One-Sentence Summary

Tisagenlecleucel is a CD19-directed CAR-T cell therapy, originally developed for CD19-positive B-cell malignancies (B-ALL, DLBCL). The TxGNN model predicts a possible signal for **Crohn's colitis**, but this is currently a **purely computational prediction with no supporting clinical trials or published literature**, and mechanism-of-action and Danish safety data are not yet available.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not confirmed in Danish licensing data (product not marketed in Denmark); mechanistic notes describe original approval for CD19+ B-cell malignancies (B-ALL, DLBCL) |
| Predicted New Indication | Crohn's Colitis |
| TxGNN Prediction Score | 91.39% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for this evidence pack (flagged as a High-severity data gap). Based on the mechanistic notes accompanying the prediction, tisagenlecleucel is an autologous anti-CD19 chimeric antigen receptor (CAR) T-cell therapy, approved for CD19-positive B-cell malignancies such as B-cell acute lymphoblastic leukaemia (B-ALL) and diffuse large B-cell lymphoma (DLBCL).

The proposed link to Crohn's colitis rests on the theory that B cells contribute to pathology in some autoimmune and inflammatory bowel disease models, and that deep CD19+ B-cell depletion with CAR-T therapy has been explored in isolated case reports for other autoimmune conditions (e.g., systemic lupus erythematosus). However, there is **no direct evidence** linking gut inflammation in Crohn's disease to a CD19+ B-cell-driven mechanism, and this connection remains theoretical.

Importantly, this pairing carries meaningful safety uncertainty: CAR-T therapy is associated with risks such as cytokine release syndrome, and its safety profile in an inflammatory bowel disease population is entirely unstudied. The mechanistic link should be regarded as a hypothesis-generating signal only, not a validated therapeutic rationale.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Denmark Market Information

Tisagenlecleucel currently holds no marketing authorisation on file in this dataset (0 licenses; market status: Not marketed).

---

## Cytotoxicity (Antineoplastic Drugs Only)

| Item | Content |
|------|------|
| Cytotoxicity Classification | Immunotherapy (CD19-directed CAR-T cell therapy) — not a conventional cytotoxic agent |
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
The prediction is supported only by a TxGNN model score (L5, S0 decision stage) with zero corroborating clinical trials or literature, and the proposed mechanism is explicitly flagged as indirect and theoretical, with unknown safety in the target population. The product is also not currently marketed in Denmark, and core safety documentation (SmPC warnings/contraindications) is missing.

**To proceed, the following is needed:**
- TFDA/Danish SmPC warnings and contraindications (currently a Blocking data gap; required before any S1 safety review)
- Confirmed mechanism of action detail (High-priority data gap)
- Preclinical or early clinical evidence directly testing CD19+ B-cell depletion in inflammatory bowel disease models
- Clarification of Danish/EU marketing authorisation status for tisagenlecleucel
- Assessment of CAR-T-specific toxicity risk (e.g., cytokine release syndrome) in an IBD population before any further evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

