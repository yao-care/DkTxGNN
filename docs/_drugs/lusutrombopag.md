---
layout: default
title: Lusutrombopag
parent: 僅模型預測 (L5)
nav_order: 273
evidence_level: L5
indication_count: 10
---

# Lusutrombopag
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

# Lusutrombopag: From [Original Indication Not Available] to Hereditary Thrombocytopenia with Normal Platelets

## One-Sentence Summary

Lusutrombopag (DrugBank DB13125) is a TPO receptor (MPL) agonist; its original approved indication is not recorded in this evidence pack, and the drug is not currently marketed in Denmark. The TxGNN model predicts a possible link to **hereditary thrombocytopenia with normal platelets**, but this prediction is supported by **0 clinical trials** and **0 publications**, and the underlying mechanistic rationale itself flags a likely mismatch (see below).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in evidence pack (no Danish licence text; `original_moa` also flagged as data gap) |
| Predicted New Indication | Hereditary thrombocytopenia with normal platelets |
| TxGNN Prediction Score | 99.995% |
| Evidence Level | L5 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed original-indication and formal MOA data are not populated in this evidence pack (flagged as data gaps DG001 and DG002). Based on the mechanistic description captured in the model's own rationale text, Lusutrombopag is a **thrombopoietin (TPO) receptor (MPL) agonist**: it stimulates proliferation and differentiation of bone-marrow megakaryocytes to increase circulating platelet **count**. This class of drug is typically used where thrombocytopenia results from insufficient platelet production.

The predicted indication, "hereditary thrombocytopenia with normal platelets," is problematic on its face — the disease name itself specifies **normal platelet counts**, meaning the underlying pathology is not one of insufficient platelet production but rather a hereditary platelet functional/structural abnormality. A TPO-RA's mechanism of *increasing platelet quantity* has no clear counterpart in a condition where platelet count is already normal, so the mechanistic link is weak.

The same caveat applies to the other top-ranked candidates in this evidence pack: "marcothrombocytopenia with mitral valve insufficiency," "dense granule disease," and "platelet storage pool deficiency" are all functional/structural platelet disorders rather than production disorders, and "transient neonatal thrombocytopenia" is a self-limiting condition with no established paediatric safety data for this drug. All were scored L5/Hold internally, consistent with high TxGNN similarity scores but low biological plausibility — likely reflecting knowledge-graph co-occurrence (shared "platelet" and "thrombocytopenia" terminology) rather than causal mechanism.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Denmark Market Information

Lusutrombopag is not currently marketed in Denmark (0 marketing authorisations on record; market status: "未上市" / not marketed).

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information. No key warnings, contraindications, or drug-drug interaction data are currently available in the evidence pack (DDI query returned "not found").

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The predicted indication's own definition (normal platelet count) is mechanistically inconsistent with a TPO-receptor agonist's platelet-count-raising action, and this pattern repeats across the other top-ranked candidates in this pack.
- There is zero clinical trial or literature support (L5 — model prediction only), the drug is not marketed in Denmark, and safety data (warnings, contraindications, DDI) are entirely unavailable — including a Blocking-severity gap (DG001) that prevents any S1 safety pre-assessment.

**To proceed, the following is needed:**
- Danish/EU SmPC warnings and contraindications (DG001, Blocking)
- Confirmed mechanism of action via DrugBank or primary literature (DG002, High)
- Clinical/haematology specialist review of the mechanistic mismatch between TPO-RA action and the platelet-functional (not production) disorders predicted here
- Original approved indication text, to properly frame drug-to-candidate similarity
- If pursued further, targeted literature/registry search specifically for TPO-RA use in hereditary platelet functional disorders, since standard clinical-trial/PubMed searches returned no hits
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

