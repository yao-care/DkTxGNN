---
layout: default
title: Iohexol
parent: 僅模型預測 (L5)
nav_order: 241
evidence_level: L5
indication_count: 10
---

# Iohexol
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

# Iohexol: From Radiographic Contrast Agent to Insomnia

## One-Sentence Summary

Iohexol is a non-ionic iodinated radiographic contrast agent used in diagnostic imaging procedures (e.g., myelography, angiography, phlebography). The TxGNN model predicts a possible association with **Insomnia**, but this is currently supported by **0 clinical trials** and **0 publications**, and the evidence pack itself flags the prediction as lacking pharmacological plausibility.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in Danish licensing data — Iohexol is not currently marketed in Denmark, so no approved indication text is available |
| Predicted New Indication | Insomnia |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L5 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for Iohexol in this evidence pack. Based on information contained in the supporting literature and trial records, Iohexol is a non-ionic, iodinated contrast medium used for radiographic and imaging procedures — it has no known central nervous system pharmacological activity and does not cross the blood-brain barrier to produce a sedative or hypnotic effect.

The evidence pack's own repurposing rationale is explicit on this point: there is **no known mechanism** linking Iohexol to insomnia treatment, and the high TxGNN score is assessed as likely reflecting a graph-relational artifact rather than a biologically grounded signal. No clinical trials or literature records exist for the drug–disease pair to counterbalance this concern.

For context, the same evidence pack also generated several other high-scoring predictions for Iohexol (anxiety, rheumatoid arthritis, antithrombin deficiency type 2, factor V excess). In each case, any clinical trials or literature that do exist use Iohexol only as a renal-clearance (GFR) measurement tool or diagnostic contrast agent within studies of unrelated interventions — not as a therapeutic agent for those conditions. This pattern reinforces that the current top prediction should be treated as a low-confidence model artifact rather than a credible repurposing lead.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Denmark Market Information

Iohexol currently holds no marketing authorisation in Denmark (market status: **Not marketed**, 0 licenses on record).

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The prediction score is high (99.87%), but it is unsupported by any clinical trial or literature evidence, and the drug's known pharmacology (a non-CNS-active iodinated contrast agent) provides no plausible mechanism for treating insomnia. This is consistent with the L5 evidence level and Hold recommendation already assigned in the source data.

**To proceed, the following is needed:**
- Confirmed mechanism of action (MOA) data for Iohexol (currently a data gap)
- TFDA/SmPC warnings and contraindications data — currently missing and flagged as a **blocking** gap for any safety pre-assessment
- Independent biological or preclinical rationale linking Iohexol to insomnia, since none currently exists
- Re-evaluation if new clinical trial or literature evidence emerges; absent that, this candidate should not advance beyond Hold
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

