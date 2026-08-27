---
layout: default
title: Ketoprofen
parent: 僅模型預測 (L5)
nav_order: 252
evidence_level: L5
indication_count: 10
---

# Ketoprofen
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

Using the report structure directly (this is a content-generation task per the provided template, not a coding task — no other skill applies).

# Ketoprofen: From Pain and Inflammation to Acromesomelic Dysplasia, Hunter-Thompson Type

## One-Sentence Summary

Ketoprofen is a non-selective COX-1/COX-2 inhibitor used for pain, inflammation, and fever. The TxGNN model predicts it may be effective for **Acromesomelic Dysplasia, Hunter-Thompson Type**, a rare skeletal developmental disorder, but this prediction is currently supported by **no clinical trials and no published literature**, and the model's own rationale flags the mechanistic link as biologically implausible.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — Ketoprofen holds no marketing authorisation in Denmark, so no Danish-approved indication text exists in this Evidence Pack |
| Predicted New Indication | Acromesomelic Dysplasia, Hunter-Thompson Type |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for this candidate is not available in the Evidence Pack (marked as a Data Gap). Based on the mechanistic notes accompanying the prediction, Ketoprofen is a non-selective COX-1/COX-2 inhibitor with anti-inflammatory, analgesic, and antipyretic activity — a well-established NSAID pharmacology.

However, the predicted indication, Acromesomelic Dysplasia, Hunter-Thompson Type, is a rare genetic skeletal dysplasia caused by *GDF5* mutations, with a pathophysiology centered on bone/cartilage developmental signaling rather than inflammation. The Evidence Pack's own repurposing rationale explicitly states that there is **no known pathological link** between the COX/prostaglandin pathway and this disorder, and that the high TxGNN score most likely reflects graph-embedding similarity rather than a biologically grounded mechanism.

This pattern repeats across the other top-ranked candidates in this pack (brachyolmia-amelogenesis imperfecta syndrome, myosclerosis, brachyolmia, and colobomatous microphthalmia-rhizomelic dysplasia syndrome) — all are rare congenital/developmental or fibrotic disorders for which the accompanying rationale text states the mechanistic connection to NSAID pharmacology is weak or absent. This is a case where the model score is high but the biological plausibility narrative is explicitly negative; it should not be read as a validated repurposing hypothesis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Denmark Market Information

Ketoprofen currently has no marketing authorisations registered in this Evidence Pack (0 licenses; market status: Not marketed). No product-level dosage form or indication data is available for Denmark.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information. Note: the underlying data pack flags TFDA/regulatory label warnings and contraindications as a **Blocking** data gap (DG001) — this must be resolved before any safety pre-assessment (S1) can proceed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate has no clinical trial or literature evidence (L5, model prediction only), no Danish marketing authorisation to anchor safety/dosing, and the mechanistic rationale supplied with the prediction itself states the biological link to Ketoprofen's COX-inhibitory pharmacology is weak or absent. There is no basis to advance past the S0 screening stage.

**To proceed, the following is needed:**
- TFDA/SmPC-sourced warnings and contraindications (currently a Blocking data gap)
- Confirmed mechanism of action (MOA) data from DrugBank or equivalent source
- An independent, disease-specific biological plausibility assessment for Acromesomelic Dysplasia, Hunter-Thompson Type (given the model's own rationale is skeptical)
- Any preclinical or case-level evidence connecting NSAID pharmacology to *GDF5*-related skeletal dysplasias, should such data emerge
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

