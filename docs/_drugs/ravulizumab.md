---
layout: default
title: Ravulizumab
parent: 僅模型預測 (L5)
nav_order: 367
evidence_level: L5
indication_count: 10
---

# Ravulizumab
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

# Ravulizumab: From Paroxysmal Nocturnal Hemoglobinuria to Autosomal Recessive Severe Congenital Neutropenia due to G6PC3 Deficiency

## One-Sentence Summary

Ravulizumab is a long-acting anti-complement C5 monoclonal antibody, originally approved for paroxysmal nocturnal hemoglobinuria (PNH), atypical hemolytic uremic syndrome (aHUS), generalized myasthenia gravis (gMG), and neuromyelitis optica spectrum disorder (NMOSD). The TxGNN model predicts it may be effective for **autosomal recessive severe congenital neutropenia due to G6PC3 deficiency**, but this prediction is currently supported by **0 clinical trials** and **0 publications**, and the evidence pack's own mechanistic review finds no established biological link between complement C5 inhibition and this disease.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | PNH, aHUS, gMG, NMOSD (approved indications per evidence-pack annotations; not sourced from a Danish label, as the product is not marketed in Denmark) |
| Predicted New Indication | Autosomal recessive severe congenital neutropenia due to G6PC3 deficiency |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L5 (model prediction only, no clinical or literature support) |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Ravulizumab binds complement protein C5 with high affinity, blocking its cleavage into C5a and C5b and thereby preventing formation of the membrane attack complex (MAC). Its approved indications — PNH, aHUS, gMG, and NMOSD — are all diseases driven by pathological terminal complement activation.

The predicted indication, G6PC3-deficient congenital neutropenia, has a fundamentally different pathophysiology: a defect in the glucose-6-phosphatase catalytic subunit that impairs neutrophil energy metabolism and triggers endoplasmic-reticulum stress, leading to increased neutrophil apoptosis. This is a metabolic/developmental disorder of granulopoiesis, not a complement-mediated disease, and the evidence pack explicitly states there is "no mechanistic overlap" between the two pathways.

Across all five distinct diseases in the top-10 predictions (G6PC3-deficient SCN, cyclic hematopoiesis, primary hyperoxaluria, severe congenital neutropenia, CXCR2-deficient SCN), the accompanying rationale text consistently characterizes the TxGNN score as likely reflecting graph-level node proximity — e.g., shared clustering with "inflammatory/hematologic disease" nodes — rather than a causal pharmacological relationship. The one partial exception is primary hyperoxaluria, where isolated case reports describe C5 inhibitors (e.g., eculizumab) being used to manage secondary thrombotic microangiopathy as a complication, not the primary oxalate metabolism defect itself. Taken together, the mechanistic case for this repurposing candidate is weak and currently unsupported by direct evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Denmark Market Information

Ravulizumab currently holds no marketing authorisation in Denmark (0 licenses on record; market status: Not marketed). No product/dosage-form/indication data is available to tabulate.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information. No Danish SmPC warnings, contraindications, or drug-interaction data are currently available in this evidence pack — this is flagged as a **Blocking** data gap (DG001) that prevents progression to initial safety assessment (S1).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All five distinct predicted indications carry L5 evidence (model prediction only), zero clinical trials, and zero literature; the evidence pack's own mechanistic analysis finds no credible pathway linking complement C5 inhibition to any of these diseases. Combined with the drug's non-marketed status in Denmark and a blocking gap on SmPC safety data, there is currently no basis to advance beyond model-prediction stage (S0).

**To proceed, the following is needed:**
- Danish/EU SmPC warnings, contraindications, and drug-interaction data (resolves DG001, blocking)
- Formal confirmation of original MOA and approved indications from DrugBank/EMA labeling (resolves DG002)
- Preclinical or mechanistic studies establishing a plausible link between complement C5 activity and neutrophil-maturation or oxalate-metabolism disorders before any clinical exploration is considered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

