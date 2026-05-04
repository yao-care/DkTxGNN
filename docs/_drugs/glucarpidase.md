---
layout: default
title: Glucarpidase
parent: 僅模型預測 (L5)
nav_order: 210
evidence_level: L5
indication_count: 10
---

# Glucarpidase
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

# Glucarpidase: From Methotrexate Toxicity Rescue to Diabetic Cataract

## One-Sentence Summary

Glucarpidase is a carboxypeptidase enzyme used as a rescue agent in acute methotrexate (MTX) overdose, acting by rapidly hydrolysing circulating MTX to inactive metabolites.
The TxGNN model predicts it may be effective for **Diabetic Cataract**,
however **no clinical trials and no publications** currently support this direction — the prediction is based solely on knowledge graph inference.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Methotrexate overdose / toxic plasma MTX concentration rescue |
| Predicted New Indication | Diabetic Cataract |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L5 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Glucarpidase (also known as carboxypeptidase G2) is a recombinant bacterial enzyme that cleaves the glutamate tail of methotrexate and its toxic polyglutamate metabolites, rapidly reducing plasma MTX levels. It is approved as an emergency rescue therapy in patients with delayed MTX clearance due to renal impairment, where toxic MTX concentrations carry risk of severe myelosuppression, mucositis, and end-organ damage.

The proposed link to diabetic cataract is mechanistically indirect. Diabetic cataract is driven by activation of the polyol pathway (aldose reductase), accumulation of advanced glycation end-products (AGEs), and oxidative stress — none of which involve MTX metabolism or carboxypeptidase activity. The TxGNN model likely generated this high score through a multi-hop knowledge graph path: **folate metabolism → elevated homocysteine → vascular and metabolic injury → diabetic ocular complications**. While hyperhomocysteinaemia is an established risk factor for diabetic microangiopathy, Glucarpidase is an acute-rescue enzyme, not a folate supplement or homocysteine-lowering agent, so this graph path does not constitute a valid therapeutic rationale.

It is worth noting that the top 10 predictions are dominated by multiple cataract subtypes sharing identical scores (0.998330), which is a recognised cluster artefact in knowledge graph models — nodes belonging to the same disease cluster receive uniform high scores regardless of drug-specific mechanistic relevance. This further reduces confidence in the biological plausibility of the prediction.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Denmark Market Information

Glucarpidase is not registered with the Danish Medicines Agency (Lægemiddelstyrelsen) and holds no national or centralised (EMA) marketing authorisation in Denmark. No product listing is available.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction score is high (99.85%), but this appears to reflect a knowledge graph cluster artefact rather than a genuine pharmacological hypothesis — there is no mechanistic link between Glucarpidase's MTX-hydrolysing activity and the pathophysiology of diabetic cataract. With zero supporting clinical trials, zero publications, no Danish marketing authorisation, and no available safety data, there is currently no basis to advance this candidate.

**To proceed, the following is needed:**

- Confirmation of a plausible mechanistic hypothesis connecting Glucarpidase (or MTX pathway modulation) to lens epithelial cell protection in hyperglycaemic conditions
- Independent literature review to determine whether any folate-cycle–homocysteine–lens opacity connection has been explored experimentally
- Full mechanism of action (MOA) data from DrugBank to enable a rigorous mechanistic analysis
- Safety profile and contraindication data (TFDA/EMA SmPC) before any further evaluation
- Re-examination of whether the high prediction score reflects genuine signal or knowledge graph cluster noise (deduplication and score recalibration recommended)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

