---
layout: default
title: Asfotase Alfa
parent: 僅模型預測 (L5)
nav_order: 46
evidence_level: L5
indication_count: 10
---

# Asfotase Alfa
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

# Asfotase Alfa: From Hypophosphatasia to Mitochondrial Oxidative Phosphorylation Disorder

## One-Sentence Summary

Asfotase alfa (Strensiq) is a recombinant human tissue-nonspecific alkaline phosphatase (TNSALP) enzyme replacement therapy, approved for the treatment of hypophosphatasia (HPP) — a rare inherited metabolic bone disease caused by deficient TNSALP activity.
The TxGNN model predicts it may be effective for **Mitochondrial Oxidative Phosphorylation Disorder due to Nuclear DNA Anomalies** with a prediction score of **99.95%**; however, **no clinical trials or published literature** currently support this repurposing direction.
This prediction is considered a knowledge-graph topological inference only, with no mechanistic validation available at this time.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypophosphatasia (HPP) — inherited TNSALP enzyme deficiency causing impaired bone mineralisation |
| Predicted New Indication | Mitochondrial Oxidative Phosphorylation Disorder due to Nuclear DNA Anomalies |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L5 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the Evidence Pack. Based on contextual information embedded in the prediction rationale, Asfotase alfa is a recombinant fusion protein that replaces deficient TNSALP activity, hydrolysing its natural substrates: inorganic pyrophosphate (PPi), pyridoxal-5'-phosphate (PLP), and phosphoethanolamine (PEA). By reducing PPi accumulation — which acts as a potent inhibitor of mineralisation — the drug restores normal bone and tooth formation in HPP patients.

The mechanistic basis for a link to mitochondrial oxidative phosphorylation disorders is indirect at best. Phosphate metabolism broadly connects to bioenergetics, since ATP synthesis in mitochondria is fundamentally a phosphorylation process. It is conceivable that the TxGNN knowledge graph detected a topological association between "phosphate metabolism" and "energy metabolism" nodes, generating a high prediction score through this pathway. However, the nuclear DNA mutations that cause primary oxidative phosphorylation disorders (e.g. defects in electron transport chain Complex I–V subunits) are mechanistically distinct from TNSALP substrate accumulation. The substrates of Asfotase alfa (PPi, PEA, PLP) have no established direct interaction with mitochondrial respiratory chain complexes.

In summary, while the TxGNN score is strikingly high (99.95%), the current expert assessment is that this prediction reflects a knowledge-graph proximity artefact rather than a biologically actionable mechanistic link. No supporting preclinical data, animal models, or clinical observations have been identified to bridge these two disease areas.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Asfotase alfa in Mitochondrial Oxidative Phosphorylation Disorder due to Nuclear DNA Anomalies.

---

## Literature Evidence

Currently no related literature available for Asfotase alfa in Mitochondrial Oxidative Phosphorylation Disorder due to Nuclear DNA Anomalies.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All five predicted repurposing targets for Asfotase alfa are rated L5 (model prediction only), meaning there is no clinical trial, observational study, or peer-reviewed literature supporting any of these new indications. Furthermore, the mechanistic analysis for the top-ranked indication (mitochondrial oxidative phosphorylation disorder) identifies the high TxGNN score as likely arising from a graph topology association — specifically the broad link between phosphate metabolism and energy metabolism — rather than a direct pharmacological relationship. Asfotase alfa's known mechanism (TNSALP-mediated PPi hydrolysis to restore bone mineralisation) does not intersect with the primary pathophysiology of nuclear DNA-associated respiratory chain defects.

**To proceed, the following is needed:**

- **MOA validation**: Retrieve full mechanism of action data from DrugBank (DB09105) to confirm or exclude any secondary pathway interactions relevant to mitochondrial function.
- **Preclinical signal search**: Conduct a targeted literature review of TNSALP/ALP activity in mitochondrial disease models, including any reports of secondary mineralisation defects in mitochondrial disorder patients.
- **Danish regulatory status clarification**: Asfotase alfa (Strensiq) holds EMA centralised marketing authorisation for HPP in Europe; confirm whether a Danish marketing authorisation has lapsed or was never applied for, and update the regulatory record accordingly.
- **Safety data retrieval**: Download and parse the current SmPC (available via EMA) to populate key warnings, contraindications, and any relevant drug interaction data before any further evaluation stages are initiated.
- **KG artefact review**: Assess whether duplicated rank entries (ranks 1&2, 3&4, 5&6, 7&8, 9&10 all share identical disease names and scores) reflect a data pipeline issue that may have inflated the candidate list — this should be resolved before interpreting breadth of TxGNN predictions.

> ⚠️ **Disclaimer**: This report is for research reference purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before application. All predictions are generated by the TxGNN computational model and must be interpreted in the context of available mechanistic and clinical evidence.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

