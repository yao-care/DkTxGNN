---
layout: default
title: Mecasermin
parent: 僅模型預測 (L5)
nav_order: 280
evidence_level: L5
indication_count: 10
---

# Mecasermin
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

# Mecasermin: From Severe Primary IGF-1 Deficiency to Monosomy X

## One-Sentence Summary

Mecasermin (Increlex) is a recombinant human insulin-like growth factor-1 (rhIGF-1), originally used to treat growth failure in children with severe primary IGF-1 deficiency or growth hormone gene deletion.
The TxGNN model predicts it may be effective for **Monosomy X** (Turner syndrome), a chromosomal condition characterised by short stature and impaired growth.
Currently, **no clinical trials and no publications** specifically linking mecasermin to this indication have been identified; this prediction is supported by model scoring alone.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Severe primary IGF-1 deficiency / growth failure in children (known approved use; not registered in Denmark) |
| Predicted New Indication | Monosomy X (Turner syndrome) |
| TxGNN Prediction Score | 99.59% |
| Evidence Level | L5 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known pharmacological information, mecasermin is a recombinant analogue of endogenous human IGF-1 (insulin-like growth factor-1). It acts as an agonist at the IGF-1 receptor (IGF1R), directly stimulating longitudinal bone growth, skeletal muscle development, and cellular proliferation — bypassing the need for upstream growth hormone (GH) signalling. It is approved internationally (e.g. by EMA as Increlex) for children who either lack IGF-1 production entirely or who cannot respond to GH.

Monosomy X, commonly known as Turner syndrome (45,X karyotype), is defined by the complete or partial absence of one X chromosome in females. Short stature is the most consistent and clinically significant feature, arising from a combination of haploinsufficiency of the SHOX gene (short stature homeobox gene on the X chromosome) and relative GH-IGF-1 axis dysregulation. Girls with Turner syndrome typically have low-normal to mildly reduced IGF-1 levels despite normal or elevated GH secretion — a pattern suggesting partial GH insensitivity at the tissue level.

Given this biological context, the TxGNN model's high prediction score is mechanistically plausible: supplying exogenous rhIGF-1 could potentially augment growth signalling downstream of the GH-IGF-1 axis in a population where the axis is partially dysfunctional. Standard care for Turner syndrome already relies on supraphysiological GH doses to partially compensate for SHOX haploinsufficiency; mecasermin could theoretically offer complementary or alternative IGF-1 replacement. However, no formal clinical evidence exists to support this specific application, and the fundamental genetic cause of Turner syndrome remains unaddressed by IGF-1 therapy.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Denmark Market Information

Mecasermin is not currently registered or marketed in Denmark. No national (Laegemiddelstyrelsen) or centralised (EMA) marketing authorisations are on record for this product within the Danish market at the time of this report.

> **Note for clinicians:** Mecasermin (Increlex) holds a centralised EMA marketing authorisation valid across the EU/EEA for severe primary IGF-1 deficiency. Named-patient or compassionate-use access pathways via Laegemiddelstyrelsen may be applicable if clinical need arises; contact Laegemiddelstyrelsen for guidance on special-purpose authorisation (særlig tilladelse).

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

> No drug interaction data, key warnings, or contraindication data are available in the current Evidence Pack. Before any clinical consideration, the full Increlex SmPC (available via the EMA product page) should be reviewed, with particular attention to known risks including hypoglycaemia, intracranial hypertension, and lymphoid tissue hypertrophy.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests entirely on TxGNN model scoring (L5 evidence); no clinical trials or publications have been identified to support the use of mecasermin specifically in monosomy X. While the mechanistic hypothesis — IGF-1 supplementation in a condition characterised by partial GH-IGF-1 axis dysfunction — is biologically coherent, it is not supported by empirical data at this stage.

**To proceed, the following is needed:**

- **Formal MOA documentation**: Obtain confirmed mechanism of action data from DrugBank or the Increlex SmPC to replace the current data gap.
- **Targeted literature review**: Conduct a structured PubMed/EMBASE search for mecasermin or IGF-1 therapy in Turner syndrome (monosomy X), including any case reports, compassionate-use series, or pilot studies not captured by the current automated query.
- **Clinical trial landscape scan**: Expand ClinicalTrials.gov search to include broader terms (e.g. "IGF-1" + "Turner syndrome", "rhIGF-1" + "45,X") beyond the current exact-match query.
- **Comparison with standard of care**: Assess whether mecasermin offers any advantage over established GH therapy (already approved and widely used in Turner syndrome in Denmark), and whether combination IGF-1 + GH protocols have been explored.
- **Safety data retrieval**: Download and parse the Increlex SmPC (TFDA and EMA versions) to populate the warnings, contraindications, and drug interaction fields before any clinical evaluation proceeds.
- **Regulatory pathway assessment**: If evidence is identified, consult Laegemiddelstyrelsen regarding compassionate-use or named-patient access given the absence of a Danish marketing authorisation.

---

*This report is generated for research reference only and does not constitute medical advice. All drug repurposing candidates require clinical validation before application. Report version: v4 | Data cut-off: 2026-04-04.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

