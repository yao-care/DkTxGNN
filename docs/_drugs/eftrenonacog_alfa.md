---
layout: default
title: Eftrenonacog Alfa
parent: 僅模型預測 (L5)
nav_order: 157
evidence_level: L5
indication_count: 10
---

# Eftrenonacog Alfa
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

# Eftrenonacog alfa: From Haemophilia B to Pseudo-von Willebrand Disease

## One-Sentence Summary

Eftrenonacog alfa is a recombinant coagulation Factor IX Fc fusion protein, approved in multiple markets for the treatment and prophylaxis of bleeding in Haemophilia B (congenital Factor IX deficiency). The TxGNN model predicts it may have utility in **pseudo-von Willebrand disease**, with a prediction confidence of **99.48%**; however, **no clinical trials and no published literature** currently support this specific repurposing direction. The mechanistic connection is considered weak, and the overall evidence is limited to model prediction alone.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Haemophilia B (congenital Factor IX deficiency) — treatment and prophylaxis of bleeding episodes |
| Predicted New Indication | Pseudo-von Willebrand disease |
| TxGNN Prediction Score | 99.48% |
| Evidence Level | L5 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack (DrugBank query pending). Based on established pharmacological knowledge, Eftrenonacog alfa (brand name: Alprolix) is a recombinant fusion protein combining coagulation Factor IX with the Fc region of human IgG1. It replaces deficient or absent endogenous Factor IX, enabling the intrinsic coagulation pathway to function via assembly of the tenase complex (FIXa + FVIIIa). The Fc fusion extends its half-life, allowing less frequent dosing compared to standard Factor IX products.

Pseudo-von Willebrand disease (Pseudo-vWD) is a gain-of-function disorder of platelet glycoprotein Ibα (GPIbα), which exhibits abnormally high affinity for von Willebrand factor (vWF). This leads to spontaneous platelet-vWF binding, progressive depletion of high-molecular-weight vWF multimers, and a clinical phenotype resembling type 2B vWD. The fundamental defect lies in the **platelet-vWF interaction**, not in coagulation factor levels. Eftrenonacog alfa, acting via the FIXa/FVIIIa tenase complex, can theoretically augment downstream thrombin generation, which may provide indirect haemostatic benefit after a bleeding event has commenced. However, this does not address the primary pathophysiological mechanism of Pseudo-vWD.

The mechanistic overlap between Eftrenonacog alfa's established indication (Haemophilia B) and Pseudo-vWD is thus very limited. Both involve haemostatic dysfunction and bleeding risk, but the underlying pathways are distinct. Unlike bypass therapies such as recombinant FVIIa (which can partially compensate for platelet-dependent haemostatic defects by directly activating FX on platelet surfaces), Factor IX supplementation occupies a more distal and uncertain role in the context of platelet-vWF axis disorders. This prediction is better understood as a graph-topology association within the TxGNN knowledge graph than as a direct pharmacological hypothesis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Eftrenonacog alfa in pseudo-von Willebrand disease.

---

## Literature Evidence

Currently no related literature available for Eftrenonacog alfa in pseudo-von Willebrand disease.

---

## Denmark Market Information

Eftrenonacog alfa currently holds **no marketing authorisations** in Denmark, either via the Danish Medicines Agency (Lægemiddelstyrelsen) national pathway or the centralised EMA procedure. The drug is not marketed in Denmark as of the data cut-off date (2026-04-05).

> **Note for reviewers:** Eftrenonacog alfa (Alprolix) holds EMA centralised marketing authorisation (EU/1/15/990) and FDA approval for Haemophilia B in other markets, but this authorisation does not extend to Denmark based on current data. Verification against the current EMA EPAR database is recommended.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information. No drug interaction data, warnings, or contraindications were retrievable from the current Evidence Pack for this candidate.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model assigns a high prediction score (99.48%) to the Eftrenonacog alfa → Pseudo-vWD association, but this reflects knowledge graph topology rather than established clinical utility. The mechanistic link is weak: Pseudo-vWD is driven by a gain-of-function platelet GPIbα defect causing vWF depletion, and Factor IX supplementation does not address this primary lesion. With zero supporting clinical trials, zero publications, and no Denmark regulatory footprint, the evidence base is insufficient to advance this candidate.

**To proceed, the following is needed:**

- **Mechanism of action data**: Retrieve full DrugBank MOA and pharmacodynamic profile for Eftrenonacog alfa to formally assess mechanistic plausibility
- **Safety data**: Obtain the current SmPC (EMA EPAR EU/1/15/990) to complete contraindication and warning assessment
- **Preclinical rationale**: Commission a structured literature review on Factor IX pathway contributions in GPIbα-related platelet disorders before advancing to hypothesis testing
- **Expert consultation**: Seek input from a clinical haematologist specialising in rare platelet disorders to evaluate whether any clinical subpopulation (e.g., Pseudo-vWD patients with concurrent bleeding refractory to standard therapy) could represent a plausible investigational niche
- **EMA authorisation status confirmation**: Verify current Denmark/EMA marketing authorisation status directly against the EMA product database and Lægemiddelstyrelsen register

> *This report is for research reference purposes only and does not constitute medical advice. All drug repurposing candidates require prospective clinical validation before any clinical application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

