---
layout: default
title: Teprotumumab
parent: 僅模型預測 (L5)
nav_order: 427
evidence_level: L5
indication_count: 10
---

# Teprotumumab
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

# Teprotumumab: From Thyroid Eye Disease to Monosomy X

## One-Sentence Summary

Teprotumumab is an IGF-1R-blocking monoclonal antibody; supporting evidence in this dataset describes its mechanism as inhibition of orbital fibroblast activation, consistent with its known use in thyroid eye disease, though no official original indication is on file. The TxGNN model predicts a possible link to **Monosomy X (Turner syndrome)**, with a prediction score of 99.79%, but **0 clinical trials** and **0 publications** currently support this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — drug not marketed in Denmark; no approved indication text on file |
| Predicted New Indication | Monosomy X (Turner syndrome) |
| TxGNN Prediction Score | 99.79% |
| Evidence Level | L5 |
| Denmark Market Status | Not Marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for teprotumumab is flagged as a data gap in this pack, and no original indication is recorded. However, the evidence collected for other candidate diseases in this same batch describes teprotumumab as an IGF-1R antagonist that suppresses orbital fibroblast activation — the mechanism underlying its established use in thyroid eye disease (Graves' ophthalmopathy).

For the top-ranked candidate, Monosomy X, no mechanistic rationale was generated in this pack (marked "pending"), and no clinical trials, ICTRP records, or literature were found. A related candidate in the same batch, mixed gonadal dysgenesis, was explicitly reviewed and flagged as a likely false positive: IGF-1R blockade has no established role in chromosomal or gonadal developmental disorders, and any link to the growth axis is indirect. Because Monosomy X sits in the same disease-similarity neighborhood (Turner-syndrome-related conditions) within the knowledge graph, the same caution likely applies — this prediction is plausibly a knowledge-graph embedding artifact rather than a genuine mechanistic signal, but this has not yet been formally confirmed for this specific candidate.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Denmark Market Information

No marketing authorisations are recorded for this drug in Denmark (0 licenses on file; market status: Not Marketed).

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (Monosomy X) has no supporting clinical trials or literature (Evidence Level L5) and no completed mechanistic review, while structurally similar predictions in the same batch (e.g., mixed gonadal dysgenesis) were independently assessed as likely false positives. The drug is also not currently marketed in Denmark, so no local safety reference exists.

**To proceed, the following is needed:**
- Complete the pending mechanistic and decision-stage review specifically for Monosomy X
- Resolve the Blocking data gap: TFDA/EMA SmPC warnings and contraindications (DG001)
- Resolve the mechanism-of-action data gap to support relevance analysis (DG002)
- Identify any preclinical or mechanistic literature connecting the IGF-1R pathway to Turner syndrome physiology before further evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

