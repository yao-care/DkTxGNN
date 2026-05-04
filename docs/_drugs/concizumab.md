---
layout: default
title: Concizumab
parent: 僅模型預測 (L5)
nav_order: 121
evidence_level: L5
indication_count: 10
---

# Concizumab
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

# Concizumab: From Haemophilia to Diabetic Cataract

## One-Sentence Summary

Concizumab is a humanised monoclonal antibody targeting Tissue Factor Pathway Inhibitor (TFPI), currently in clinical development for haemophilia A and B, where it restores thrombin generation by inhibiting the TFPI-mediated brake on coagulation.
The TxGNN model predicts it may be effective for **Diabetic Cataract**, with **0 clinical trials** and **0 publications** currently supporting this direction.
This prediction is rated **L5** (model prediction only) and carries a **Hold** recommendation pending mechanistic plausibility review and safety clarification.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Haemophilia A and B (investigational; no approved indication on record in Denmark) |
| Predicted New Indication | Diabetic Cataract |
| TxGNN Prediction Score | 98.27% |
| Evidence Level | L5 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the current Evidence Pack. Based on information embedded in the repurposing rationale fields, Concizumab is an anti-TFPI antibody that exerts a **procoagulant** effect — it blocks TFPI, thereby relieving the inhibition of the extrinsic coagulation pathway and restoring haemostasis in haemophilia patients.

Diabetic cataract is caused by an entirely distinct pathophysiological process: chronic hyperglycaemia drives sorbitol accumulation in the lens via the aldose reductase pathway, generates advanced glycation end-products (AGEs), and creates oxidative stress that progressively denatures lens crystallin proteins. **There is no established mechanistic link** between TFPI inhibition or coagulation pathway modulation and lens protein aggregation or oxidative damage.

The high TxGNN score (98.27%) most likely reflects a **graph-structural artefact**: the knowledge graph contains a densely connected "diabetes" comorbidity hub, and the model propagates signal indirectly from Concizumab → haemophilia → diabetes complications → diabetic cataract nodes, without this representing a direct pharmacological relationship. An additional concern is that Concizumab's procoagulant properties may be **unsafe** in diabetic patients, who already have elevated microvascular thrombotic risk; use could theoretically worsen retinal vein occlusion or other ocular microvascular complications.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Concizumab in any cataract indication.

---

## Literature Evidence

Currently no related literature available for Concizumab in any cataract indication.

---

## Denmark Market Information

Concizumab has no marketing authorisations in Denmark (neither national Laegemiddelstyrelsen nor centralised EMA authorisations). The drug is not currently marketed in Denmark.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) and the Investigator's Brochure (IB) for full safety information, as no labelled safety data were available in this Evidence Pack.

Based on the drug's pharmacological class, the following potential concerns are flagged for awareness:

- **Procoagulant risk in diabetic patients**: Concizumab enhances thrombin generation. Diabetic patients carry an intrinsically elevated thrombotic and hypercoagulable state; administration of an anti-TFPI antibody in this population may increase the risk of microvascular thrombotic events, including retinal vein occlusion.
- **Bleeding/thrombosis balance**: As an agent that shifts haemostasis toward coagulation, any use outside its intended haemophilia indication requires careful haematological risk assessment.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction score is high, but the mechanistic analysis indicates no plausible biological link between TFPI inhibition and cataract formation; the prediction is most likely a graph-structural false positive arising from shared diabetes comorbidity nodes in the knowledge graph. Furthermore, the procoagulant mechanism of Concizumab raises specific safety concerns in the target diabetic patient population, and there is a complete absence of supporting clinical or preclinical evidence (L5).

**To proceed, the following would be needed:**

- **Biological plausibility study**: Identification of any peer-reviewed hypothesis or preclinical data linking TFPI or coagulation pathway components to lens oxidative stress or crystallin aggregation — none currently exists.
- **MOA data retrieval**: Full DrugBank and published pharmacology data for Concizumab to confirm or exclude any off-target ocular mechanisms.
- **Safety assessment in diabetic population**: Dedicated coagulation risk modelling before any further evaluation in patients with diabetes mellitus.
- **Regulatory status clarification**: Confirm current clinical development phase and whether any EMA marketing authorisation application is planned, to assess the realistic pathway to a Danish repurposing study.
- **Re-evaluation of TxGNN output**: Given that ranks 1–10 are entirely occupied by cataract subtypes sharing near-identical scores (0.9816–0.9827), this cluster should be formally reviewed as a potential systematic model artefact before being taken forward as a repurposing signal.

> **Disclaimer:** This report is for research reference purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before any therapeutic application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

