---
layout: default
title: Riociguat
parent: 僅模型預測 (L5)
nav_order: 379
evidence_level: L5
indication_count: 10
---

# Riociguat
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

# Riociguat: From Pulmonary Arterial Hypertension to Ambras Type Hypertrichosis Universalis Congenita

## One-Sentence Summary

Riociguat is a soluble guanylate cyclase (sGC) stimulator, referenced in this evidence pack's own mechanistic annotations as being used for pulmonary arterial hypertension (PAH) and chronic thromboembolic pulmonary hypertension (CTEPH) — though this cannot be formally verified, as the drug's original indication and mechanism of action are flagged as data gaps in this pack. The TxGNN model's top prediction is **Ambras Type Hypertrichosis Universalis Congenita**, a rare congenital hair-growth disorder, but this prediction is currently supported by **0 clinical trials** and **0 publications**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not confirmed in this evidence pack (referenced only informally as PAH/CTEPH in internal rationale notes — see Data Gaps) |
| Predicted New Indication | Ambras Type Hypertrichosis Universalis Congenita |
| TxGNN Prediction Score | 94.92% |
| Evidence Level | L5 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for Riociguat is not available in this evidence pack (flagged as a High-severity data gap, DG002). Internal rationale annotations attached to lower-ranked candidates in this same pack note that Riociguat is pharmacologically known as an sGC stimulator that raises intracellular cGMP, producing vascular smooth muscle relaxation — the basis for its established use in PAH/CTEPH. This information is unverified pending formal MOA confirmation via DrugBank.

For the top-ranked prediction, Ambras type hypertrichosis universalis congenita, there is no plausible pathophysiological link to this vascular sGC/cGMP mechanism. This is a rare congenital hair-growth syndrome with a genetic basis unrelated to vascular smooth muscle signalling. The prediction reflects a high TxGNN model score only, with no corroborating mechanistic, clinical, or literature signal.

It is also worth noting that the ten predicted indications returned in this pack collapse to five unique diseases, each duplicated. All five (hypertrichosis-type disorders, an odontal/periodontal malformation syndrome, and Dandy-Walker malformation syndrome) are rare congenital or structural syndromes with no established connection to sGC/cGMP vascular pharmacology, and all are scored L5/Hold in the underlying data.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

*Note: A lower-ranked candidate in this same evidence pack ("malformation syndrome with odontal and/or periodontal component," rank 3–4) returned 20 PubMed hits, but manual review found these to be general periodontology reviews with no mention of Riociguat or sGC stimulators — assessed as keyword co-occurrence noise rather than drug-specific evidence, and is not counted toward the top-ranked candidate above.*

## Denmark Market Information

No marketing authorisations for Riociguat are currently registered in this evidence pack. Market status: Not marketed (0 licenses on file).

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication has no mechanistic rationale, no clinical trial evidence, and no literature support — only a raw TxGNN model score. Combined with an unresolved blocking data gap (product label/warnings, DG001) and an unverified mechanism of action (DG002), this candidate does not meet the threshold to advance past initial screening.

**To proceed, the following is needed:**
- Danish/EU SmPC or product labelling data (warnings, contraindications) — currently blocking (DG001)
- MOA verification via DrugBank API — currently high-priority gap (DG002)
- Confirmation of Riociguat's original approved indication and regulatory status in Denmark/EU
- If further pursued, a targeted literature and mechanistic search specific to hypertrichosis pathophysiology, rather than relying on automated model score alone
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

