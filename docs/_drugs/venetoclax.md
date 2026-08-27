---
layout: default
title: Venetoclax
parent: 僅模型預測 (L5)
nav_order: 467
evidence_level: L5
indication_count: 10
---

# Venetoclax
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

# Venetoclax: From Established CLL/AML Indications to IGHV-Mutated CLL/SLL

## One-Sentence Summary

Venetoclax is an orally administered BCL-2 inhibitor with internationally established use in chronic lymphocytic leukemia (CLL) and acute myeloid leukemia (AML). The TxGNN model's top-ranked prediction for this candidate is **IGHV-mutated chronic lymphocytic leukemia/small lymphocytic lymphoma (CLL/SLL)** — a molecularly defined subgroup within venetoclax's existing disease class — with a prediction score of **99.55%**, but this specific ranked entry returned **no directly linked clinical trials or publications** in the current evidence pack. Substantially more trial and literature support exists for other venetoclax entries in the same candidate bundle (Hodgkin's/non-Hodgkin's lymphoma, myeloid leukemia, CML blast phase).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (no Danish licenses on file). Based on established pharmacological knowledge, venetoclax's internationally approved indications are CLL/SLL and AML. |
| Predicted New Indication | Chronic lymphocytic leukemia/small lymphocytic lymphoma with immunoglobulin heavy chain variable-region gene somatic hypermutation (IGHV-mutated CLL/SLL) |
| TxGNN Prediction Score | 99.55% |
| Evidence Level | L5 (model prediction only — no clinical trials or literature directly linked to this ranked entry) |
| Denmark Market Status | Not marketed (未上市) |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this evidence pack (flagged as a High-severity data gap). Based on established pharmacological knowledge, venetoclax is a selective, orally administered small-molecule inhibitor of BCL-2 (B-cell lymphoma 2), a protein that promotes malignant cell survival by blocking apoptosis. By binding BCL-2 and displacing pro-apoptotic proteins, venetoclax restores the intrinsic apoptotic pathway in malignant B-lymphocytes and myeloid blasts.

BCL-2 dependency is a shared biological feature across B-cell malignancies (CLL/SLL, Hodgkin's and non-Hodgkin's lymphomas) and myeloid malignancies (AML, CML blast phase), which is consistent with why this candidate bundle's predictions converge broadly on hematologic malignancies. The specific top-ranked prediction — an IGHV-mutation-defined CLL/SLL subgroup — represents a molecular refinement within venetoclax's already-established disease class rather than a mechanistically distant new indication.

Notably, although the top-ranked entry itself has no trials or publications indexed in this evidence pack, closely related entries within the same candidate bundle are extensively supported, including the pivotal MURANO trial (venetoclax-rituximab in relapsed/refractory CLL, PMID [40009494](https://pubmed.ncbi.nlm.nih.gov/40009494/)) and multiple completed Phase 3 studies in lymphoma and leukemia. This supports the general mechanistic plausibility of BCL-2 inhibition in this disease class, even though evidence specific to the IGHV-mutated subgroup was not separately retrieved by the searches recorded in this pack.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Denmark Market Information

Venetoclax is **not currently marketed in Denmark**; the Laegemiddelstyrelsen dataset in this evidence pack lists zero marketing authorisations for this drug.

## Cytotoxicity

Venetoclax is an antineoplastic agent (BCL-2 inhibitor, indicated for leukemia/lymphoma), so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (selective BCL-2 inhibitor) |
| Myelosuppression Risk | Please refer to the Summary of Product Characteristics (SmPC) warnings and precautions |
| Emetogenicity Classification | Please refer to the Summary of Product Characteristics (SmPC) warnings and precautions |
| Monitoring Items | Please refer to the Summary of Product Characteristics (SmPC) warnings and precautions |
| Handling Protection | Please refer to the Summary of Product Characteristics (SmPC) warnings and precautions |

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Venetoclax is not marketed in Denmark (zero authorisations on file), a Blocking-severity data gap prevents any safety initial evaluation (TFDA/SmPC warnings and contraindications are missing), and the top-ranked predicted indication itself has no directly linked clinical trial or literature evidence in this pack (Evidence Level L5).

**To proceed, the following is needed:**
- Obtain the official SmPC / product label (via EMA centralised procedure or manufacturer, since not yet authorised in Denmark) to close the blocking safety data gap
- Confirm original approved indications and mechanism of action via DrugBank/EMA to close the MOA data gap
- Run a targeted evidence search specific to the IGHV-mutated CLL/SLL molecular subgroup, since current searches returned zero trials/literature for this exact ranked entry
- Consider evaluating the more evidence-rich related entries in this candidate bundle (venetoclax in Hodgkin's/non-Hodgkin's lymphoma combination regimens, myeloid leukemia, and CML blast phase), which show substantially stronger trial and literature support
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

