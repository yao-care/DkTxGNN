---
layout: default
title: Hypromellose
parent: 僅模型預測 (L5)
nav_order: 217
evidence_level: L5
indication_count: 10
---

# Hypromellose
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

# Hypromellose: From Pharmaceutical Excipient to Hepatic Veno-Occlusive Disease-Immunodeficiency Syndrome

## One-Sentence Summary

Hypromellose (hydroxypropyl methylcellulose, HPMC) is an inert semi-synthetic polymer with no established pharmacological therapeutic indication — it functions primarily as an excipient in pharmaceutical formulations (tablet coatings, ophthalmic lubricants, suspending agents).
The TxGNN model predicts it may be effective for **hepatic veno-occlusive disease-immunodeficiency syndrome** with a prediction score of **98.30%**, however **no supporting clinical trials or published literature** currently exist for this direction.
Given the complete absence of a plausible mechanism of action and zero clinical evidence, this prediction is assessed as a likely model artefact rather than a genuine therapeutic opportunity.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No established therapeutic indication (used as pharmaceutical excipient) |
| Predicted New Indication | Hepatic veno-occlusive disease-immunodeficiency syndrome |
| TxGNN Prediction Score | 98.30% |
| Evidence Level | L5 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for Hypromellose, as it is not classified as a pharmacologically active substance. Hypromellose is a semi-synthetic inert polymer derived from cellulose, used across pharmaceutical manufacturing as a film-coating agent for tablets (controlled-release formulations), a viscosity-modifying and lubricating agent in ophthalmic drops (artificial tears), and a suspending agent in oral liquid preparations. Its effects are entirely physical and physicochemical — film-forming, mucoadhesive, viscosity-modifying — with no known receptor binding, enzymatic inhibition, or biochemical signalling activity.

Hepatic veno-occlusive disease-immunodeficiency syndrome (VODI syndrome) is a rare autosomal recessive primary immunodeficiency disorder associated with mutations in genes such as *VPS13B* and *WIPF1*. The pathophysiology centres on defective immune signalling and hepatic sinusoidal endothelial injury, leading to progressive veno-occlusive disease and combined immunodeficiency. Effective pharmacological intervention in this condition requires agents capable of modulating immune cell development, endothelial protection, or fibrinolytic activation — none of which are properties attributable to an inert polymer excipient.

**There is no established or plausible mechanistic link between Hypromellose and any of the predicted indications.** The uniformly high TxGNN scores across all five top-ranked rare diseases most likely reflect a knowledge graph artefact: Hypromellose's ubiquitous co-occurrence with thousands of active drugs in formulation data may have artificially inflated its graph connectivity, producing spurious high-confidence predictions unrelated to pharmacological activity. This interpretation is strongly supported by the complete absence of any supporting clinical trials or literature across all queried indications.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Hypromellose is an inert pharmaceutical excipient with no known pharmacological activity; all five unique top-ranked TxGNN predictions involve rare genetic diseases for which no mechanistic connection to Hypromellose exists, and zero clinical or preclinical supporting evidence was identified across all evidence sources queried.

**To proceed, the following is needed:**

- **Pipeline audit**: Verify whether Hypromellose was correctly classified in the TxGNN input pipeline — known excipients and inactive ingredients should be excluded from repurposing candidate generation to prevent model artefacts
- **Knowledge graph review**: Investigate whether Hypromellose's high graph connectivity stems from co-formulation co-occurrence rather than pharmacological relationships, and apply appropriate edge filtering
- **Expert adjudication**: If any downstream investigation is warranted, obtain an independent pharmacology expert assessment of whether HPMC can exert any direct biological activity at physiologically relevant concentrations
- **No further evidence collection is recommended** at this stage for any of the predicted indications, as the foundational premise (pharmacological activity) has not been established
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

