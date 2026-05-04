---
layout: default
title: Florfenicol
parent: 僅模型預測 (L5)
nav_order: 192
evidence_level: L5
indication_count: 10
---

# Florfenicol
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

# Florfenicol: From Veterinary Bacterial Infections to Interventricular Septum Aneurysm

## One-Sentence Summary

Florfenicol is a fluorinated chloramphenicol-class antibiotic developed exclusively for veterinary use, with no approved indications in human medicine.
The TxGNN model predicts it may be effective for **Interventricular Septum Aneurysm** with a score of 94.31%;
however, **no clinical trials and no published literature** currently support this direction, making this a model-only prediction at evidence level L5.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Veterinary bacterial infections (not approved for human use) |
| Predicted New Indication | Interventricular Septum Aneurysm |
| TxGNN Prediction Score | 94.31% |
| Evidence Level | L5 |
| Denmark Market Status | Not Marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known pharmacological information, Florfenicol is a fluorinated derivative of chloramphenicol — a broad-spectrum antibiotic that works by inhibiting bacterial protein synthesis (binding to the 50S ribosomal subunit). It is used in veterinary medicine to treat bacterial infections in fish, cattle, and swine, and has never been approved for use in humans in any jurisdiction.

Interventricular septum aneurysm (VSA) is a structural cardiac defect — either congenital or acquired — involving localised bulging of the ventricular septal wall. There is no established mechanistic link between protein synthesis inhibition (the antibiotic mode of action) and cardiac structural repair, remodelling, or fibrosis prevention. The TxGNN model likely inferred this association through indirect knowledge graph pathways connecting bacterial infection to cardiac involvement (e.g., infectious endocarditis → cardiac structural damage → antibiotic therapy), rather than any direct pharmacological mechanism.

It should be noted that the same prediction score (0.9431) appears duplicated across both rank 1 and rank 2 entries for the same disease, suggesting a data pipeline issue rather than independent evidence. The mechanistic plausibility of Florfenicol in any human cardiac condition is currently unsupported, and the veterinary-only regulatory history creates an additional barrier to human repurposing.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Denmark Market Information

Florfenicol holds no marketing authorisations in Denmark. The drug is not registered with the Danish Medicines Agency (Lægemiddelstyrelsen) and has no EMA centralised authorisation for human use. It is classified as a veterinary medicinal product outside the scope of human pharmaceutical regulation.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

> **Note:** No human-use safety data (warnings, contraindications, or drug interactions) were retrieved for Florfenicol, consistent with its status as a veterinary-only compound. Any human safety assessment would need to be constructed de novo from veterinary data and chloramphenicol-class extrapolation before further evaluation could proceed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate scores L5 (model prediction only) with zero supporting clinical trials or published literature, and the drug itself has no human regulatory history in any country. The mechanistic connection between a bacterial protein synthesis inhibitor and a structural cardiac defect is not pharmacologically supported, and the identical duplicate scores across indication ranks suggest a data quality concern in the current pipeline output.

**To proceed, the following would be needed:**

- **Establish basic human pharmacology:** Florfenicol has no human PK/PD data. Preclinical toxicology and first-in-human data would be required before any repurposing programme could be initiated.
- **Clarify mechanism of action relevance:** A credible mechanistic hypothesis linking chloramphenicol-class activity to interventricular septum pathophysiology must be established (e.g., anti-inflammatory or anti-fibrotic properties demonstrated in cardiac tissue models).
- **Resolve duplicate prediction entries:** Ranks 1 and 2 are identical; the pipeline should deduplicate disease entries before scoring.
- **Retrieve full MOA data from DrugBank:** DrugBank query was recorded as successful but MOA was not populated in the Evidence Pack — this should be retrieved to support any mechanistic analysis.
- **Regulatory pathway assessment:** A formal assessment of whether Florfenicol could enter human clinical development (e.g., under EMA's repurposing framework) would be required given its veterinary-only history.
- **No further evidence search is recommended** until the mechanistic hypothesis is strengthened; additional database queries at this stage are unlikely to yield new results.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

