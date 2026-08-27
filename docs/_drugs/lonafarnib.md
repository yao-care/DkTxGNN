---
layout: default
title: Lonafarnib
parent: 僅模型預測 (L5)
nav_order: 267
evidence_level: L5
indication_count: 10
---

# Lonafarnib
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

Using the report template directly — this is a document-generation task with the full spec already supplied, no additional skill applies.

A few data-quality notes before the report: `predicted_indications[0]` (rank 1, Leprosy) is the required subject per the template, but it carries **zero** supporting evidence (L5, model-score only) — its own `repurposing_rationale` explicitly states there is no mechanistic link. The evidence pack also has no `original_indications`, no `original_moa`, and no Danish licenses on file. I've reported these gaps transparently rather than filling them from outside knowledge, per the "no guessing / no data-gap fabrication" rules. I also flagged the higher-evidence rheumatoid arthritis candidate (rank 3, L4) in the conclusion since it's materially relevant to the recommendation.

---

# Lonafarnib: From Unspecified Original Indication to Leprosy

## One-Sentence Summary

> Lonafarnib's original approved indication is not documented in the available data (DrugBank ID DB06448; mechanism of action recorded as a data gap).
> The TxGNN model predicts possible effectiveness for **Leprosy**, with a prediction score of **99.14%**,
> but currently **zero clinical trials and zero publications** support this specific pairing — the prediction is model-score only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in available data |
| Predicted New Indication | Leprosy |
| TxGNN Prediction Score | 99.14% |
| Evidence Level | L5 (model prediction only, no clinical or literature support) |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data for Lonafarnib is not available in the current dataset (flagged as a High-severity data gap). Supporting rationale text elsewhere in the evidence pack identifies Lonafarnib as a farnesyltransferase (FTase) inhibitor, which blocks farnesylation of Ras and related proteins — but this description was supplied only as background context for other candidate indications, not as a validated MOA record for this drug.

For the top-ranked prediction, Leprosy, the evidence pack explicitly states there is **no known mechanistic connection** between farnesyltransferase inhibition and *Mycobacterium leprae* infection pathology. The prediction is derived solely from the TxGNN knowledge-graph score, with no corroborating clinical trials, literature, or biological rationale identified to date.

Because the original indication is also undocumented, it is not currently possible to assess pharmacological continuity between Lonafarnib's established use and Leprosy. This combination of an unsupported mechanistic link and the absence of any original-indication context is why the evidence level is scored at the lowest tier (L5) and the recommendation defaults to Hold.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Denmark Market Information

No marketing authorisations are currently registered for Lonafarnib in Denmark (market status: Not marketed; 0 licenses on file).

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

*(Danish label warnings/contraindications are recorded as a Blocking-severity data gap — this must be resolved before any safety pre-assessment (S1) can proceed. No drug-drug interaction data was found in the source query.)*

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (Leprosy) is supported only by a TxGNN graph score, with no clinical trials, no literature, and no plausible mechanistic link identified — evidence level L5 does not meet the threshold to advance past initial screening (S0).

**To proceed, the following is needed:**
- Danish/EU SmPC warnings and contraindications (Blocking data gap — required before any safety pre-assessment)
- Verified mechanism of action for Lonafarnib
- Documentation of Lonafarnib's original approved indication(s), to assess continuity with any new candidate
- If pursuing repurposing further, consider prioritizing the rheumatoid arthritis candidate instead (evidence level L4, one supporting mechanistic-pathway publication, though not drug-specific), rather than Leprosy which currently has no evidentiary support at all
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

