---
layout: default
title: Silodosin
parent: 僅模型預測 (L5)
nav_order: 398
evidence_level: L5
indication_count: 10
---

# Silodosin
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

# Silodosin: From Benign Prostatic Hyperplasia to Ambras Type Hypertrichosis Universalis Congenita

## One-Sentence Summary

Silodosin is a highly selective α1A-adrenergic receptor antagonist, clinically established for benign prostatic hyperplasia (BPH) and associated lower urinary tract symptoms. The TxGNN model predicts it may be effective for **Ambras Type Hypertrichosis Universalis Congenita**, a rare congenital hair-growth disorder, but this prediction is currently supported by **0 clinical trials** and **0 publications**. The drug's own repurposing rationale flags this association as a likely knowledge-graph false positive rather than a genuine mechanistic signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Benign prostatic hyperplasia (BPH) / lower urinary tract symptoms (based on known drug class; not confirmed in this Evidence Pack) |
| Predicted New Indication | Ambras Type Hypertrichosis Universalis Congenita |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 (model prediction only) |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a High-severity data gap, DG002). Based on known information, silodosin is a highly selective α1A-adrenergic receptor antagonist used to relax smooth muscle in the prostate and bladder neck, improving urinary flow in BPH.

Ambras type hypertrichosis universalis congenita is a rare autosomal-dominant disorder linked to chromosomal rearrangements near 8q22 and dysregulation of the EDA2R-AR gene region, affecting hair follicle growth control. There is no established physiological or pharmacological pathway connecting α1A-adrenergic receptor blockade to hair follicle regulation.

The Evidence Pack's own repurposing rationale is explicit on this point: with no mechanistic hypothesis, no clinical trials, and no literature support — only a high TxGNN score — this association should be treated as a **likely knowledge-graph noise / data-sparsity false positive**, not a credible repurposing lead. This assessment applies consistently across all five distinct candidate diseases surfaced by this run (hypertrichosis-related conditions, a dental/periodontal malformation syndrome, and Dandy-Walker malformation syndrome) — none show a plausible mechanistic link to α1A-selective antagonism.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Denmark Market Information

Silodosin currently has no marketing authorisation registered in Denmark (0 authorisations; market status: Not marketed). No product/dosage-form data is available in this Evidence Pack.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information. Note: retrieval of Danish label warnings and contraindications (DG001) is currently a **Blocking** data gap — it must be resolved before any initial safety screening (S1) can proceed.

---

## Other Candidate Indications (Same Run)

For transparency, four additional distinct predicted indications were generated in the same batch, all with comparably high TxGNN scores but no supporting evidence and the same "Hold" recommendation:

| Predicted Indication | TxGNN Score | Evidence Level | Supporting Data |
|---|---|---|---|
| Hypertrichosis (disease) | 99.99% | L5 | None |
| Malformation syndrome with odontal and/or periodontal component | 99.99% | L4 | 20 publications (all generic periodontitis literature, none mentioning silodosin or α1-antagonists — string-match artifact, not drug-specific evidence) |
| Syndrome with a Dandy-Walker malformation as major feature | 99.98% | L5 | None |
| Isolated genetic hair shaft abnormality | 99.98% | L5 | None |

None of these candidates present a credible mechanistic or evidentiary basis for repurposing.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- All five candidate indications are supported only by high TxGNN scores (L5, or L4 with irrelevant literature), with no clinical trials, no disease-specific publications, and no plausible mechanistic pathway connecting silodosin's α1A-adrenergic antagonism to any of the predicted conditions. This pattern is consistent with a knowledge-graph false positive.
- A Blocking data gap (DG001: missing Danish/EU label warnings and contraindications) independently prevents even an initial safety screen (S1) from being started.

**To proceed, the following is needed:**
- Resolve DG001: obtain the official SmPC warnings/contraindications (Blocking)
- Resolve DG002: obtain confirmed mechanism of action and approved original indication data from DrugBank or an equivalent authoritative source
- If any of these five indications is to be pursued further, an independent mechanistic hypothesis (beyond TxGNN score) should be developed and validated before allocating evidence-collection resources
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

