---
layout: default
title: Trimethoprim
parent: 僅模型預測 (L5)
nav_order: 453
evidence_level: L5
indication_count: 4
---

# Trimethoprim
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Trimethoprim: From Antibacterial Therapy to Punctate Epithelial Keratoconjunctivitis

## One-Sentence Summary

Trimethoprim is an antibacterial agent (dihydrofolate reductase inhibitor); detailed original indication and mechanism-of-action records are not available in the current evidence pack, and the drug is not currently marketed in Denmark. The TxGNN model predicts a possible link to **punctate epithelial keratoconjunctivitis**, with a high prediction score but **zero supporting clinical trials or literature**, and the evidence pack's own mechanistic review flags this prediction as biologically implausible.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (no Danish licences on file); per the pack's own mechanistic notes, trimethoprim is classed as an antibacterial (DHFR inhibitor) |
| Predicted New Indication | Punctate epithelial keratoconjunctivitis |
| TxGNN Prediction Score | 99.57% |
| Evidence Level | L5 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (data gap). Based on the information available in this evidence pack, trimethoprim is classified as an antibacterial agent that inhibits dihydrofolate reductase (DHFR), giving it activity against a range of bacterial pathogens but **no activity against viruses**.

Punctate epithelial keratoconjunctivitis is most commonly caused by viral infection (e.g., adenovirus), rather than by bacteria. This creates a direct mismatch between trimethoprim's mechanism and the predominant etiology of the predicted indication.

The TxGNN model's high score (99.57%) most likely reflects graph proximity to related ocular/conjunctival disease categories rather than a genuine mechanistic or clinical link — the score is not corroborated by any clinical trial or published literature identified for this drug-indication pair. On mechanistic grounds alone, this prediction does not appear applicable.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Denmark Market Information

No marketing authorisations are on file for trimethoprim in Denmark (Laegemiddelstyrelsen) in this evidence pack; market status is recorded as "Not marketed" with 0 authorisations.

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score with no clinical trial or literature evidence (L5), and the evidence pack's own mechanistic analysis indicates trimethoprim (an antibacterial) is unlikely to be effective against punctate epithelial keratoconjunctivitis, which is predominantly viral in origin.

**To proceed, the following is needed:**
- Confirmed mechanism-of-action data from DrugBank (currently a blocking-adjacent data gap)
- Danish SmPC / warnings and contraindications data (currently unavailable)
- Independent clinical or preclinical evidence specifically addressing this drug-indication pair before reconsidering beyond Hold
- Re-evaluation against alternative, better-evidenced predicted indications for this drug, if available in future evidence pack updates
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

