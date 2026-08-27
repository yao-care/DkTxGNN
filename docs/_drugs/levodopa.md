---
layout: default
title: Levodopa
parent: 僅模型預測 (L5)
nav_order: 263
evidence_level: L5
indication_count: 2
---

# Levodopa
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Levodopa: From Parkinson's Disease to Rasmussen Subacute Encephalitis

## One-Sentence Summary

Levodopa (DrugBank DB01235) is the dopamine precursor foundational to Parkinson's disease therapy; no marketing-authorisation record for Denmark is present in this Evidence Pack, so registry-confirmed original indication data is currently unavailable. The TxGNN model predicts potential relevance to **Rasmussen subacute encephalitis**, but this prediction is currently supported by **0 clinical trials** and **0 publications**, and the drug is **not marketed in Denmark**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available from Danish registry data (drug not marketed in Denmark); generically known for Parkinson's disease |
| Predicted New Indication | Rasmussen Subacute Encephalitis |
| TxGNN Prediction Score | 99.06% |
| Evidence Level | L5 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this Evidence Pack (`original_moa: [Data Gap]`). Based on general pharmacological knowledge, levodopa is a dopamine precursor that is converted by DOPA decarboxylase into dopamine, and it is used clinically to replenish striatal dopamine deficiency (classically in Parkinson's disease).

Rasmussen subacute encephalitis is a chronic, typically unilateral, T-cell-mediated autoimmune/inflammatory encephalitis of childhood, presenting with drug-resistant epilepsy and progressive neurological decline. There is no established pathological link between this disease and dopaminergic signalling.

The model's high score (0.99) most likely reflects topological similarity within the knowledge graph — for example, shared proximity to other central-nervous-system and movement/seizure-related disease nodes — rather than a genuine mechanistic connection. Because the drug's own MOA record is missing, this rationale cannot be cross-validated against structured data, and the predicted link should be treated as speculative pending mechanistic and preclinical review.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Denmark Market Information

Currently no marketing authorisations registered in Denmark (market status: Not marketed).

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the TxGNN model score (Evidence Level L5), with no clinical trials, no literature, and no drug interaction data confirming feasibility; the drug also carries no current Danish marketing authorisation, and both the original MOA and safety/contraindication data are missing.

**To proceed, the following is needed:**
- Confirmed mechanism of action (MOA) data for levodopa from DrugBank or SmPC
- TFDA/Danish SmPC-sourced warnings and contraindications (currently blocking per data gap DG001)
- Preclinical or mechanistic studies establishing a plausible biological link to Rasmussen subacute encephalitis
- Ongoing monitoring for emerging clinical trial or publication evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

