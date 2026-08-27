---
layout: default
title: Maraviroc
parent: 僅模型預測 (L5)
nav_order: 277
evidence_level: L5
indication_count: 10
---

# Maraviroc
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

# Maraviroc: From HIV-1 Infection to Multiple Endocrine Neoplasia

## One-Sentence Summary

Maraviroc is a CCR5 antagonist originally developed to block HIV-1 entry into CD4+ T cells for the treatment of HIV-1 infection. The TxGNN model assigns its highest score to **Multiple Endocrine Neoplasia**, but this prediction is supported by **0 clinical trials** and **0 publications**, and the evidence pack's own mechanistic assessment flags it as a likely false positive.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in Denmark market data; drug is a CCR5 antagonist historically indicated for HIV-1 infection |
| Predicted New Indication | Multiple Endocrine Neoplasia |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L5 (model prediction only, no clinical trials or literature) |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for Maraviroc is not available from the structured DrugBank field in this pack (marked as a data gap). Based on the repurposing rationale supplied alongside the predictions, Maraviroc acts as a CCR5 antagonist, blocking chemokine receptor CCR5 signalling and thereby preventing HIV entry into CD4+ T cells.

Multiple Endocrine Neoplasia (MEN) is driven by MEN1/RET gene mutations that cause endocrine tumour proliferation — a pathway with no established biological link to CCR5-mediated immune cell chemotaxis. The evidence pack's own mechanistic assessment explicitly characterizes this as **"a candidate with an extremely high prediction score but an implausible mechanism, most likely a false positive"** (原文: 屬預測分數極高但機轉不合理的假陽性候選).

In other words, the very high TxGNN score (99.82%) reflects a strong pattern match in the knowledge graph, not a validated pharmacological rationale. No clinical trials, registry entries, or peer-reviewed literature connect Maraviroc to MEN, and the drug's known immunomodulatory/antiviral mechanism does not translate mechanistically to endocrine tumorigenesis.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Denmark Market Information

Maraviroc is currently not marketed in Denmark (market status: Not marketed; 0 marketing authorisations on record), so no Danish product/authorisation data is available for this evaluation.

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top-ranked prediction (Multiple Endocrine Neoplasia) has no supporting clinical trials or literature (Evidence Level L5), and the evidence pack's own mechanistic review identifies it as a likely false positive with no plausible biological link between CCR5 antagonism and MEN1/RET-driven tumorigenesis.

**To proceed, the following is needed:**
- TFDA/SmPC label warnings and contraindications (currently a blocking data gap — required before any safety pre-assessment)
- Confirmed mechanism-of-action data from DrugBank (currently a data gap affecting mechanistic-link analysis)
- Preclinical or mechanistic studies specifically linking CCR5 signalling to MEN1/RET pathways, if this candidate is to be pursued further
- Independent confirmation that this is not a knowledge-graph artifact, given the pack's own flag of likely false-positive status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

