---
layout: default
title: Voclosporin
parent: 僅模型預測 (L5)
nav_order: 473
evidence_level: L5
indication_count: 10
---

# Voclosporin
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

Using the data-report skill approach (execute-before-report), I'll work strictly from the JSON evidence pack provided — no external data was fetched, so I'm treating every field as-is rather than supplementing from memory.

A few data-quality notes before the report: `drug.original_indications` is empty and `original_moa` is `[Data Gap]`, so no specific original indication is documented in this pack. The evidence pack's own literature/rationale text (not the `original_moa` field) does establish that voclosporin is a calcineurin-inhibitor immunosuppressant — I've used that only where it's explicitly sourced from the pack's literature/rationale content, and flagged everywhere else that data is missing, per the "no fabrication" rule.

---

# Voclosporin: From Immunosuppressive Therapy to Primary Release Disorder of Platelets

## One-Sentence Summary

> Voclosporin is a calcineurin-inhibitor immunosuppressant (class-mate of cyclosporine and tacrolimus); no specific original approved indication is documented in this evidence pack, and the drug is **not currently marketed in Denmark**.
> The TxGNN model's top-ranked prediction links it to **Primary Release Disorder of Platelets**, with a **95.4% prediction score**, but **zero supporting clinical trials and zero literature**, and the model's own mechanistic rationale states this link is biologically implausible.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (no `original_indications` on file; drug not yet marketed in Denmark) |
| Predicted New Indication | Primary release disorder of platelets |
| TxGNN Prediction Score | 95.42% |
| Evidence Level | L5 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for voclosporin is not available at the drug level in this evidence pack (`original_moa: [Data Gap]`). However, the literature and rationale entries attached to other candidate indications in this same pack indicate that voclosporin belongs to the **calcineurin-inhibitor (CNI)** class, alongside cyclosporine and tacrolimus. According to a review captured in this pack (PMID 41361657), CNIs act by inhibiting the calcium-dependent phosphatase calcineurin, blocking dephosphorylation/nuclear translocation of NFAT, and suppressing IL-2 transcription — thereby impairing T-cell activation. This is standard immunosuppressant pharmacology, not a validated original indication for voclosporin specifically.

For the model's top-ranked prediction — **primary release disorder of platelets** — the evidence pack's own mechanistic assessment is explicitly negative: this is a **hereditary defect in platelet dense-granule secretion**, a structural/genetic platelet disorder with pathophysiology unrelated to T-cell activation or the calcineurin pathway. The pack states plainly that "目前無任何臨床或文獻證據支持" (no clinical or literature evidence currently supports this) and classifies the association as a prediction-only artifact that "未達可驗證假說門檻" (has not reached the threshold of a testable hypothesis).

In short: the TxGNN similarity score (95.4%) is high, but the accompanying rationale — generated from the same evidence pack — does not corroborate a plausible biological mechanism. A high embedding-similarity score without mechanistic or empirical support should be interpreted cautiously; it may reflect graph-clustering effects among platelet-related disease nodes rather than a genuine pharmacological relationship.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Denmark Market Information

Voclosporin currently has **no marketing authorisation on file in Denmark** (`market_status`: Not marketed; `total_licenses`: 0). No Laegemiddelstyrelsen national authorisation or EMA centralised authorisation record is present in this evidence pack.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

*(Note: this evidence pack's own data-gap log flags the missing label/warning data — item DG001, "TFDA 仿單警語/禁忌" — as a **Blocking** severity gap, meaning this candidate cannot yet proceed to the safety-review stage (S1) until label data is retrieved.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- Evidence level is **L5** — model prediction only, with no clinical trials, no literature, and no observational data supporting a link between voclosporin and primary release disorder of platelets.
- The evidence pack's own mechanistic rationale explicitly contradicts biological plausibility: platelet dense-granule secretion defects are not known to involve the calcineurin/T-cell activation pathway that voclosporin targets.
- Two data gaps block further progression: **DG001** (Danish/EU SmPC warnings and contraindications — Blocking, prevents entry to safety-review stage S1) and **DG002** (confirmed mechanism of action — High, needed for mechanistic validation).

**To proceed, the following is needed:**
- Retrieve the approved SmPC (Danish/EU label) for voclosporin to resolve DG001 before any safety review can begin
- Confirm mechanism of action via DrugBank or primary pharmacology sources to resolve DG002
- Any preclinical or mechanistic literature directly linking calcineurin inhibition to platelet dense-granule release would be required before this candidate could move beyond Hold
- **For consideration**: this same evidence pack contains a lower-ranked but better-supported candidate — **dermatitis** (TxGNN score 94.2%, evidence level L3, decision stage S1 "Research Question") — backed by 2 literature reviews (PMID 37307993, PMID 41361657) discussing off-label dermatologic use of systemic calcineurin inhibitors including voclosporin. That candidate has a coherent class-effect mechanistic rationale and may warrant prioritized follow-up ahead of the top-ranked but mechanistically unsupported platelet-disorder prediction.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

