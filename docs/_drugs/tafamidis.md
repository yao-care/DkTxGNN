---
layout: default
title: Tafamidis
parent: 僅模型預測 (L5)
nav_order: 414
evidence_level: L5
indication_count: 10
---

# Tafamidis
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

# Tafamidis: From Transthyretin Amyloidosis to Primary Release Disorder of Platelets

## One-Sentence Summary

Tafamidis is a transthyretin (TTR) stabiliser whose established clinical use is in transthyretin amyloidosis (ATTR-CM/ATTR-PN) — this drug is currently **not marketed in Denmark**, and formal mechanism-of-action and label data are unavailable in this evidence pack. The TxGNN model's top-ranked prediction is **Primary Release Disorder of Platelets**, but this prediction is supported by **0 clinical trials and 0 publications**, and no biologically plausible mechanistic link has been identified between TTR stabilisation and platelet granule-release physiology.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Transthyretin amyloidosis (ATTR-CM/ATTR-PN) — inferred from trial/literature context in this pack; not confirmed via a Danish label, as the drug has no marketing authorisation on file |
| Predicted New Indication | Primary Release Disorder of Platelets |
| TxGNN Prediction Score | 89.27% |
| Evidence Level | L5 (model prediction only, no trials or literature) |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in this evidence pack (flagged as a High-severity data gap). What is known — drawn from trial and literature context elsewhere in this pack — is that tafamidis works by binding transthyretin and stabilising its tetrameric form, preventing dissociation and amyloid fibril formation; this is the basis for its established role in transthyretin amyloid cardiomyopathy and polyneuropathy.

Primary release disorder of platelets is a distinct condition involving defective granule release from platelets during activation — a mechanism governed by platelet signalling and secretory pathways, not by transthyretin folding or amyloidogenesis. No known biological pathway connects TTR stabilisation to platelet granule release, and the evidence pack's own rationale for this candidate explicitly states there is no known mechanistic link.

This prediction should therefore be read as a pure graph-embedding similarity output from TxGNN rather than a mechanistically or clinically grounded hypothesis. Notably, a lower-ranked candidate in this same run — "primary amyloidosis" (rank 9, TxGNN score 85.0%) — is supported by 17 clinical trials and 20 publications, consistent with tafamidis's already-known clinical use. That contrast reinforces that the rank-1 platelet-disorder prediction reviewed here currently lacks the supporting evidence needed to act on.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Denmark Market Information

Tafamidis has no marketing authorisation on record in Denmark (market status: Not marketed; 0 authorisations). No product/dosage-form/indication data is available to tabulate.

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- Zero clinical trials and zero publications support tafamidis in primary release disorder of platelets, and no known mechanistic link exists between TTR stabilisation and platelet granule-release pathology. Evidence level is L5 (model prediction only), decision stage S0 — the lowest confidence tier in this framework.

**To proceed, the following is needed:**
- TFDA/SmPC label warnings and contraindications (currently a Blocking data gap — required before any S1 safety screen can begin)
- Confirmed mechanism-of-action data for tafamidis (High-severity data gap)
- Preclinical or mechanistic studies establishing biological plausibility between TTR stabilisation and platelet granule release
- Confirmation of Danish/EU marketing authorisation status before any regulatory pathway can be scoped
- If pursuing repurposing, prioritise the "primary amyloidosis" candidate instead, given its existing 17-trial/20-publication evidence base consistent with tafamidis's known clinical use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

