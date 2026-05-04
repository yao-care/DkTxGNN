---
layout: default
title: Albutrepenonacog Alfa
parent: 僅模型預測 (L5)
nav_order: 20
evidence_level: L5
indication_count: 10
---

# Albutrepenonacog Alfa
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

# Albutrepenonacog Alfa: From Haemophilia B to Pseudo-von Willebrand Disease

## One-Sentence Summary

Albutrepenonacog alfa (Idelvion®) is a recombinant Factor IX–albumin fusion protein originally developed for the prophylaxis and treatment of bleeding in Haemophilia B (congenital Factor IX deficiency).
The TxGNN model predicts it may be effective for **Pseudo-von Willebrand Disease (Platelet-type VWD)**, with a prediction score of **99.94%**; however, **no clinical trials and no published literature** currently support this direction, and mechanistic analysis indicates a fundamental mismatch between the drug's mode of action and the pathophysiology of the predicted indication.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Haemophilia B — prophylaxis and treatment of bleeding episodes due to congenital Factor IX deficiency |
| Predicted New Indication | Pseudo-von Willebrand Disease (Platelet-type VWD) |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L5 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Albutrepenonacog alfa is a recombinant human coagulation Factor IX (FIX) fused to human albumin (rFIX-FP). The albumin fusion substantially extends the plasma half-life of FIX compared with standard Factor IX concentrates. Its pharmacological action lies entirely within the **intrinsic coagulation pathway**: once activated to FIXa, it assembles the intrinsic tenase complex (FIXa–FVIIIa) on phospholipid membrane surfaces, driving Factor Xa generation, thrombin formation, and ultimately fibrin clot stabilisation. This mechanism is specific to correcting the secondary haemostasis defect found in Haemophilia B.

Pseudo-von Willebrand Disease (also known as Platelet-type VWD or GP1BA-related VWD) represents an entirely distinct pathophysiology. It is caused by a gain-of-function mutation in the platelet glycoprotein **GPIbα**, which results in spontaneous, abnormal binding of GPIbα to von Willebrand Factor (vWF). This depletes circulating vWF multimers and platelets, impairing primary haemostasis. The established treatment is **platelet transfusion** (to supply normal GPIbα), not coagulation factor replacement. Factor IX supplementation plays no role in restoring vWF levels, normalising platelet counts, or correcting GPIbα receptor function.

The TxGNN model's high confidence score most likely reflects **topological similarity within the underlying knowledge graph** — both Haemophilia B and pseudo-von Willebrand disease share "haemorrhagic disorder" and "coagulation abnormality" nodes — rather than any genuine mechanistic or therapeutic link. This case illustrates a recognised limitation of graph-based prediction models: phenotypic clustering can inflate confidence scores without capturing the disease-specific molecular pathophysiology. The prediction should be interpreted with significant caution.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

*Systematic searches of ClinicalTrials.gov and WHO ICTRP conducted on 26 March 2026 returned no results for albutrepenonacog alfa in pseudo-von Willebrand disease.*

---

## Literature Evidence

Currently no related literature available.

*PubMed searches conducted on 26 March 2026 returned no publications linking albutrepenonacog alfa to pseudo-von Willebrand disease.*

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction is driven by knowledge graph topological proximity within the "bleeding disorder" phenotype cluster rather than by mechanistic relevance; pseudo-von Willebrand disease is a primary haemostasis disorder requiring platelet transfusion, and Factor IX replacement has no theoretical basis, no clinical precedent, and no supporting evidence in this condition.

**Summary of all TxGNN-predicted indications for Albutrepenonacog Alfa:**

| Rank | Predicted Disease | TxGNN Score | Mechanistic Assessment | Decision |
|------|------------------|------------|----------------------|---------|
| 1 | Pseudo-von Willebrand Disease | 99.94% | **Mismatch** — GPIbα gain-of-function platelet disorder; FIX has no mechanistic role | Hold |
| 2 | Primary Release Disorder of Platelets | 99.94% | **Mismatch** — Dense/α-granule secretion defect; coagulation factor supplementation has no basis | Hold |
| 3 | Glanzmann Thrombasthenia | 99.92% | **Weak** — Bypass therapy concept misapplied; rFVIIa (not FIX) is the established bypass agent for GPIIb/IIIa deficiency | Hold |
| 4 | Scott Syndrome | 99.63% | **Partial plausibility** — FIX complex assembly theoretically impaired; however no clinical evidence exists and the disease affects fewer than 30 patients globally | Hold |
| 5 | Bleeding Diathesis due to Collagen Receptor Defect | 99.28% | **Mismatch** — Primary haemostasis defect (GPVI/α2β1); coagulation factors cannot correct platelet–collagen adhesion failure | Hold |

**To proceed with any re-evaluation, the following would be required:**

- Detailed mechanism of action data and pharmacodynamic profile from DrugBank and primary literature
- Confirmation of Danish marketing authorisation status (note: Idelvion® holds EMA centralised authorisation EU/1/16/1073 for Haemophilia B; local availability and reimbursement status in Denmark should be verified with Laegemiddelstyrelsen separately)
- For **Scott syndrome** specifically — the most mechanistically arguable of the five predictions — expert haematology opinion and a targeted literature review on FIX activity in phosphatidylserine externalisation defects would be the minimum prerequisite before any further steps
- Preclinical or case-report-level evidence demonstrating FIX activity in platelet-related bleeding models (currently entirely absent across all five predicted indications)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

