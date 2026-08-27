---
layout: default
title: Pegvisomant
parent: 僅模型預測 (L5)
nav_order: 340
evidence_level: L5
indication_count: 10
---

# Pegvisomant
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

# Pegvisomant: From Acromegaly to Borderline Ovarian Serous Tumor

## One-Sentence Summary

> Pegvisomant (DrugBank DB00082) is a recombinant growth hormone (GH) receptor antagonist originally developed to treat **acromegaly** by blocking GH-driven IGF-1 production.
> The TxGNN model predicts a possible effect on **Borderline Ovarian Serous Tumor**, with a prediction score of **98.63%**, but **no clinical trials and no literature** currently support this specific link — this is a pure knowledge-graph prediction.

> **Note on data provenance:** The evidence pack's own `original_moa` and `original_indications` fields are flagged as data gaps (DG002). The "Acromegaly" original indication and GH-receptor-antagonist mechanism stated above come from established public drug information (Pegvisomant/Somavert), not from the source pack, and should be confirmed against the official SmPC before use.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acromegaly (growth hormone excess) — *not present in source pack; based on established drug information, pending confirmation* |
| Predicted New Indication | Borderline Ovarian Serous Tumor |
| TxGNN Prediction Score | 98.63% |
| Evidence Level | L5 (model prediction only — no clinical trials, no literature) |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed, source-verified mechanism of action data is not available in the evidence pack (flagged as a High-severity data gap, DG002). Based on the rationale attached to this prediction, Pegvisomant is understood to act as a **GH receptor antagonist**, reducing IGF-1 production — the mechanism underlying its established use in acromegaly.

The proposed link to Borderline Ovarian Serous Tumor rests on general oncology background knowledge that the GH/IGF-1 axis can contribute to proliferative signaling in some ovarian epithelial tumors, so a GH receptor antagonist could theoretically slow IGF-1-driven tumor growth. However, the evidence pack explicitly characterizes this as an **indirect, mechanism-only inference**: there is no trial or publication that directly connects Pegvisomant to this specific tumor type, and the high TxGNN score cannot distinguish a genuine biological signal from a knowledge-graph clustering effect.

This caution is reinforced by the fact that four of the top ten predictions from this run are ovarian tumor subtypes (borderline serous tumor, rete ovarii cystadenoma, papillary cystadenoma, and malignant Brenner tumor) with nearly identical scores (0.9856–0.9863), suggesting the model is grouping these diseases together in embedding space rather than producing an individually validated signal for any one of them. A fifth top-10 prediction — pyelonephritis, a bacterial infection with no known mechanistic link to GH receptor blockade — is flagged in the pack itself as a likely false-positive artifact and is not considered further in this report.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Denmark Market Information

Pegvisomant currently holds **no marketing authorisations** in Denmark (market status: Not marketed; 0 licenses on record in the source pack). No Laegemiddelstyrelsen or centralised EMA authorisation data is available to summarize dosage form or approved indication text for this market.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

*(Note: This is not merely a placeholder — key warnings, contraindications, and drug interaction data are marked as a Blocking-severity data gap, DG001, meaning this candidate cannot currently enter the S1 safety pre-assessment stage.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- Evidence Level is L5 — the prediction is supported only by the TxGNN model, with zero clinical trials and zero publications specific to this indication.
- The prediction sits within a cluster of near-identical scores across multiple unrelated ovarian tumor subtypes, raising concern that it reflects structural similarity in the knowledge graph rather than a validated pharmacological signal.
- A Blocking-severity data gap (missing Danish/EU SmPC warnings and contraindications) means this candidate cannot yet proceed to safety pre-assessment (S1), independent of the efficacy question.
- Pegvisomant is not currently marketed in Denmark (0 authorisations), which adds a regulatory/access barrier on top of the evidentiary one.

**To proceed, the following is needed:**
- Official SmPC (warnings, contraindications, drug interactions) to clear the Blocking data gap (DG001) and allow safety pre-assessment
- Confirmed, source-verified mechanism of action and original indication documentation (DG002)
- Preclinical or mechanistic studies specifically examining the GH/IGF-1 axis in borderline ovarian serous tumors, rather than general oncology background reasoning
- Any first clinical or case-level evidence connecting Pegvisomant to this indication before further resource investment
- Reassessment of the other clustered ovarian-tumor predictions as a group, since they may represent one underlying (unconfirmed) hypothesis rather than four independent signals
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

