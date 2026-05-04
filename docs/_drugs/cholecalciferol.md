---
layout: default
title: Cholecalciferol
parent: 僅模型預測 (L5)
nav_order: 109
evidence_level: L5
indication_count: 10
---

# Cholecalciferol
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

# Cholecalciferol: From Vitamin D Deficiency to Familial Isolated Hypoparathyroidism Due to Impaired PTH Secretion

---

## One-Sentence Summary

Cholecalciferol (Vitamin D3) is a fat-soluble secosteroid vitamin widely used to prevent and treat vitamin D deficiency, supporting calcium homeostasis, bone mineralisation, and musculoskeletal health.
The TxGNN model predicts it may be effective for **Familial Isolated Hypoparathyroidism Due to Impaired PTH Secretion**, with a prediction score of **99.79%**.
Currently, **no clinical trials** and **no publications** specifically address this drug–indication combination, yielding an evidence level of **L5** (model prediction only).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not formally registered in Denmark; used internationally for vitamin D deficiency, rickets, and disorders of calcium and phosphorus metabolism |
| Predicted New Indication | Familial isolated hypoparathyroidism due to impaired PTH secretion |
| TxGNN Prediction Score | 99.79% |
| Evidence Level | L5 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this dataset. Based on established pharmacological knowledge, cholecalciferol (Vitamin D3) is the natural precursor to the active hormone calcitriol (1,25-dihydroxyvitamin D). It undergoes two sequential hydroxylation steps: first in the liver (producing 25-hydroxyvitamin D, or calcidiol) and then in the kidney (producing 1,25-dihydroxyvitamin D, or calcitriol). Calcitriol acts through the vitamin D receptor (VDR) to promote intestinal calcium absorption, enhance renal tubular calcium reabsorption, and support bone mineralisation.

Familial isolated hypoparathyroidism due to impaired PTH secretion is characterised by insufficient PTH output, resulting in hypocalcaemia and hyperphosphataemia. Under normal physiology, PTH stimulates renal 1α-hydroxylase activity, driving the conversion of calcidiol to the active calcitriol. When PTH is deficient, this activation step is impaired. Cholecalciferol's downstream metabolite, calcitriol, can in principle partially compensate for PTH absence by directly promoting intestinal calcium absorption and renal calcium retention via VDR signalling, offering some degree of symptomatic correction of hypocalcaemia.

However, the mechanistic link is indirect and limited. Cholecalciferol is a distal precursor, and its conversion to calcitriol is itself dependent on PTH-driven 1α-hydroxylase activity — the same step that is compromised in this condition. In clinical practice, active vitamin D analogues such as calcitriol or alfacalcidol, which bypass the impaired renal hydroxylation step entirely, are the established standard of care for hypoparathyroidism. Cholecalciferol's relevance here is therefore mechanistically plausible but substantially weakened by poor conversion efficiency in a low-PTH environment, making it a supportive rather than primary therapeutic candidate.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Denmark Market Information

Cholecalciferol is not currently registered as a prescription medicinal product by the Danish Medicines Agency (Laegemiddelstyrelsen). No national or centralised (EMA) marketing authorisations are on file in Denmark. Cholecalciferol is available in Denmark as a non-prescription dietary supplement or vitamin preparation, which falls outside the scope of standard medicinal product registration.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model assigns a high prediction score based on mechanistic pathway proximity (VDR-mediated calcium homeostasis), but there is no supporting clinical trial or published literature evidence for cholecalciferol specifically in familial isolated hypoparathyroidism due to impaired PTH secretion. The core mechanistic limitation — impaired cholecalciferol-to-calcitriol conversion in a low-PTH state — means that active vitamin D analogues are clinically preferred, and direct evidence for cholecalciferol in this rare genetic condition is entirely absent.

**To proceed, the following is needed:**
- Retrieval of detailed MOA data from DrugBank (DB00169) to confirm the mechanistic rationale formally
- A targeted literature search for case reports or mechanistic studies evaluating cholecalciferol (not only active analogues) in PTH-deficient settings
- Pharmacokinetic/pharmacodynamic modelling of calcitriol conversion rates achievable under low-PTH conditions with high-dose cholecalciferol supplementation
- Consultation with Danish endocrinology/rare disease specialists to assess whether any patients with this condition are currently managed with cholecalciferol off-label
- Review of EMA/Laegemiddelstyrelsen product information for calcitriol and alfacalcidol to assess regulatory precedent for active-vitamin-D use in this indication and inform any future application strategy

> **Note for reviewers:** Among all TxGNN predictions for this drug, **hypophosphatemic rickets** (TxGNN score 99.20%, evidence level L3) has substantially stronger supporting evidence — including 1 completed Phase 3 RCT with active vitamin D as a comparator arm and multiple clinical series. If this repurposing programme progresses to a higher-priority review, hypophosphatemic rickets may represent a more actionable near-term candidate than the top-ranked familial hypoparathyroidism prediction.

---

*This report is generated for research reference purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

