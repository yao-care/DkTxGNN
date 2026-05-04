---
layout: default
title: Migalastat
parent: 僅模型預測 (L5)
nav_order: 235
evidence_level: L5
indication_count: 10
---

# Migalastat
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

# Migalastat: From Fabry Disease to Idiopathic Copper-Associated Cirrhosis

## One-Sentence Summary

Migalastat (Galafold) is an oral pharmacological chaperone approved for Fabry disease — a rare lysosomal storage disorder caused by mutations in the *GLA* gene encoding alpha-galactosidase A.
The TxGNN model predicts it may be effective for **Idiopathic Copper-Associated Cirrhosis**, with a prediction score of **98.85%**.
However, **no clinical trials and no published literature** currently support this direction, and mechanistic analysis suggests the link is very weak.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Fabry disease (alpha-galactosidase A deficiency, GLA amenable mutations) |
| Predicted New Indication | Idiopathic copper-associated cirrhosis |
| TxGNN Prediction Score | 98.85% |
| Evidence Level | L5 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known information, Migalastat is an oral pharmacological chaperone that selectively binds to and stabilises misfolded alpha-galactosidase A (GLA) in patients with amenable *GLA* mutations. By restoring proper lysosomal trafficking of GLA, it reduces the pathological accumulation of globotriaosylceramide (Gb3) and related glycosphingolipids in vascular endothelium, cardiomyocytes, and podocytes — the hallmark lesion of Fabry disease.

The predicted indication, idiopathic copper-associated cirrhosis, involves a fundamentally different metabolic pathway. Copper homeostasis is primarily regulated by ATP7B (the Wilson disease copper transporter) and related proteins such as COMMD1 and ATOX1; none of these intersect directly with the GLA/Gb3 lysosomal pathway. While lysosomal dysfunction can theoretically influence intracellular metal trafficking through LAMP2-related mechanisms, there is no published evidence that Migalastat exerts any effect on copper metabolism or hepatic copper accumulation.

The most likely explanation for the high TxGNN score is a **graph clustering artefact**: the TxGNN knowledge graph may have grouped "hepatic lysosomal storage disease" as a shared hub node, causing Migalastat to score highly against copper-related liver conditions despite there being no biologically plausible treatment rationale. All five unique predicted indications in this pack share the same score (98.85%) and the same evidence profile (zero trials, zero publications), which further supports this interpretation of systematic over-prediction in the rare liver disease subgraph.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for any of the predicted indications.

---

## Literature Evidence

Currently no related literature available for any of the predicted indications.

---

## Denmark Market Information

Migalastat (Galafold) currently holds **no national marketing authorisations** recorded in the Danish Medicines Agency (Lægemiddelstyrelsen) database, and the drug is listed as not marketed in Denmark at the time of this report (data cut-off: 2026-04-04).

> **Note for reviewers:** Galafold received a European Medicines Agency (EMA) centralised marketing authorisation (EU/1/16/1085) for Fabry disease in May 2016. If this EMA authorisation is not reflected in the source data, the regulatory status should be verified directly via the [EMA Product page](https://www.ema.europa.eu/en/medicines/human/EPAR/galafold) and the [Lægemiddelstyrelsen product database](https://produktresume.dk/) before drawing conclusions about Danish market availability.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

> Safety data — including key warnings, contraindications, and drug–drug interactions — were not available in this Evidence Pack and were not retrieved from TFDA/DrugBank sources at the time of data collection (2026-03-24). Before any clinical use, consult the current Galafold SmPC available through the EMA or the national medicines agency.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model assigns a high score (98.85%) to all predicted indications, but this appears to reflect a knowledge-graph clustering effect rather than genuine pharmacological plausibility. There is no clinical trial evidence, no supporting literature, no established mechanistic link between GLA-targeted pharmacological chaperoning and copper metabolism or hepatic vascular pathology, and Migalastat has no current marketing authorisation recorded in Denmark. With an L5 evidence level and a weak mechanistic rationale across all five predicted disease areas, advancing this candidate is not justified at this stage.

**To proceed, the following is needed:**

- **Mechanistic data**: Retrieve and review full Migalastat MOA from DrugBank (DB05018) and primary literature to formally rule out any indirect copper-handling or lysosomal-hepatic link.
- **Regulatory clarification**: Confirm whether the EMA centralised authorisation (EU/1/16/1085) is active and valid for Denmark, and obtain the current SmPC with full safety data.
- **TxGNN model audit**: Investigate why all top-10 predictions share an identical score (0.9885) and map to rare hepatic conditions. This likely reflects a subgraph-level bias and should be flagged to the model maintenance team for recalibration.
- **Broader indication search**: Reassess Migalastat candidates outside the hepatic rare-disease subgraph — for example, Fabry-adjacent indications (nephropathy, cardiomyopathy, cerebrovascular disease) where the GLA/Gb3 mechanistic link is well established and clinical trial evidence may exist.
- **Safety assessment**: Complete the blocking data gap (DG001) by downloading and parsing the SmPC/prescribing information from the EMA or a reference regulatory authority before any repurposing safety evaluation can proceed.

---

*This report is for research purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before therapeutic application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

