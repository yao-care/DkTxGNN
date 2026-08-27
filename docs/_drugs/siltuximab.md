---
layout: default
title: Siltuximab
parent: 僅模型預測 (L5)
nav_order: 399
evidence_level: L5
indication_count: 10
---

# Siltuximab
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

# Siltuximab: From Multicentric Castleman Disease to Extracutaneous Mastocytoma

## One-Sentence Summary

> Siltuximab is an anti-interleukin-6 (IL-6) monoclonal antibody approved for multicentric Castleman disease (MCD).
> The TxGNN model predicts it may be effective for **Extracutaneous Mastocytoma**,
> but this prediction is currently supported by **0 clinical trials** and **0 publications** — it rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Multicentric Castleman Disease (MCD) — referenced in evidence pack rationale text; not present in formal license data |
| Predicted New Indication | Extracutaneous Mastocytoma |
| TxGNN Prediction Score | 99.64% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not formally recorded for Siltuximab in this evidence pack (drug-level MOA field is a data gap). However, supporting trial documentation elsewhere in the pack describes Siltuximab as a recombinant chimeric (human-murine) anti-IL-6 monoclonal antibody, administered by intravenous infusion, and notes it is approved for multicentric Castleman disease — a lymphoproliferative disorder driven in part by IL-6 signalling.

For the top-ranked predicted indication, extracutaneous mastocytoma, the evidence pack's own mechanistic assessment is explicitly skeptical: mastocytoma pathology is driven primarily by KIT mutations and mast cell proliferation, a pathway with only weak, unsubstantiated overlap with IL-6 inhibition. No clinical or literature evidence accompanies this prediction — it is a high TxGNN score without independent corroboration.

By contrast, other candidates further down the same prediction list — notably Kaposi's sarcoma (rank 9–10, score 99.28%) — have a more coherent mechanistic story (shared HHV-8/KSHV viral driver with MCD, IL-6 implicated in tumor microenvironment) and at least one supporting literature reference, though still no direct clinical evidence. This suggests the overall repurposing signal for Siltuximab is stronger for virally-driven, IL-6-associated conditions than for the top-ranked mastocytoma prediction itself.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Denmark Market Information

Siltuximab currently holds no marketing authorisation in Denmark (0 registered products; market status: not marketed).

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information. Note: label-level warnings/contraindications and a formal DDI screen for Siltuximab are flagged as outstanding, blocking data gaps in this evidence pack (no source could yet be queried for warnings, contraindications, or drug interactions).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication (extracutaneous mastocytoma) has no clinical trial or literature support and a mechanistic link the evidence pack itself describes as weak — this is a pure L5 model score, insufficient to advance.

**To proceed, the following is needed:**
- Formal mechanism-of-action documentation for Siltuximab (currently a data gap)
- Danish/EU label warnings and contraindications (blocking gap — required before any S1 safety screen)
- A completed drug-interaction query (current status: not found)
- Independent preclinical or mechanistic rationale connecting IL-6 inhibition to mast cell tumor biology before pursuing mastocytoma further
- If pursuing the IL-6/viral-driven signal instead, prioritize the Kaposi's sarcoma candidate (L4, Research Question stage) for deeper literature review, since it currently has the pack's only literature support
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

