---
layout: default
title: Amoxicillin
parent: 僅模型預測 (L5)
nav_order: 34
evidence_level: L5
indication_count: 10
---

# Amoxicillin
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

# Amoxicillin: From Bacterial Infections to Polyclonal Hyperviscosity Syndrome

## One-Sentence Summary

Amoxicillin is a broad-spectrum beta-lactam antibiotic widely used to treat bacterial infections caused by susceptible Gram-positive and Gram-negative organisms.
The TxGNN model predicts it may have a role in **Polyclonal Hyperviscosity Syndrome**, with **0 clinical trials** and **0 publications** currently supporting this direction.
The mechanistic connection is indirect and speculative, and the evidence is insufficient to move beyond a model-level prediction at this stage.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Bacterial infections (broad-spectrum antibiotic; indication data not captured in current dataset) |
| Predicted New Indication | Polyclonal Hyperviscosity Syndrome |
| TxGNN Prediction Score | 99.63% |
| Evidence Level | L5 |
| Denmark Market Status | Not Marketed (0 authorisations on record) |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Detailed mechanism of action data is not available in the current dataset. Based on well-established pharmacological knowledge, Amoxicillin is a beta-lactam antibiotic that inhibits bacterial cell wall synthesis by covalently binding to penicillin-binding proteins (PBPs). This interferes with the final cross-linking step of peptidoglycan biosynthesis, leading to osmotic instability and bacterial cell lysis. It is active against a broad range of susceptible organisms including *Streptococcus*, *Haemophilus influenzae*, *E. coli*, and *Helicobacter pylori*.

Polyclonal hyperviscosity syndrome is caused by the excessive production of polyclonal immunoglobulins, typically arising in the setting of chronic infection, systemic autoimmune disease, or B-cell dysregulation — not a malignant clone, as seen in Waldenström's macroglobulinaemia. The proposed indirect mechanistic link is that a persistent bacterial infection (e.g., subacute bacterial endocarditis) may continuously drive polyclonal immunoglobulin production through chronic antigen stimulation. Eradicating the underlying infection with antibiotics such as Amoxicillin could theoretically reduce this antigen-driven stimulus and allow immunoglobulin levels and blood viscosity to normalise.

However, this is a multi-step, indirect inference rather than a direct pharmacological mechanism. Amoxicillin has no known direct effect on immunoglobulin synthesis, plasma cell activity, or blood viscosity. The TxGNN knowledge graph likely captured an epidemiological co-occurrence between bacterial infection and hyperviscosity rather than a true drug–disease therapeutic relationship. Biological plausibility is considered low, and this prediction should not be interpreted as evidence of efficacy.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Denmark Market Information

Based on data available from the Laegemiddelstyrelsen (Danish Medicines Agency), Amoxicillin currently has no recorded marketing authorisations in this dataset.

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|-------------------------------|-------------|-------------|---------------------|
| — | — | — | No authorisations on record |

> **Note for clinicians:** Amoxicillin is one of the most widely prescribed antibiotics globally and is available in numerous formulations across European markets. The absence of records in this dataset likely reflects a data pipeline gap rather than a true absence of registration. Current authorisation status and approved products should be verified directly via the [Laegemiddelstyrelsen product database](https://www.laegemiddelstyrelsen.dk) or the [EMA medicines database](https://www.ema.europa.eu/en/medicines).

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All TxGNN predictions for Amoxicillin are rated L5 (model prediction only), with zero supporting clinical trials or published literature across all five predicted indications. The mechanistic link between Amoxicillin's antibacterial action and polyclonal hyperviscosity syndrome relies on an indirect, multi-step chain of reasoning with no direct pharmacological basis, making this prediction insufficient to justify further development at this time.

**To proceed, the following is needed:**

- **Mechanism of action data**: Retrieve full MOA and drug category information from DrugBank (DB01060) to enable proper mechanistic evaluation
- **Safety profile**: Obtain complete key warnings, contraindications, and drug–drug interactions from the approved SmPC or Laegemiddelstyrelsen records
- **Denmark market verification**: Confirm current Danish market status and available product authorisations directly via Laegemiddelstyrelsen or EMA
- **Supporting literature**: Conduct a broader literature review for any case reports or epidemiological studies linking antibiotic use to changes in immunoglobulin levels or blood viscosity
- **Biological plausibility assessment**: Before advancing, an independent expert review of the mechanistic rationale is strongly recommended; the other four predicted indications (hyperamylasemia, congenital analbuminemia, blood group incompatibility, premalignant haematological disease) also lack biological plausibility for Amoxicillin and should not be prioritised

---

> ⚠️ **Disclaimer:** This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before any clinical application. All content should be evaluated in the context of current clinical guidelines and individual patient circumstances.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

