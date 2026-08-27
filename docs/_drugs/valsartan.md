---
layout: default
title: Valsartan
parent: 僅模型預測 (L5)
nav_order: 463
evidence_level: L5
indication_count: 10
---

# Valsartan
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

# Valsartan: From Hypertension to Malignant Hypertensive Renal Disease

## One-Sentence Summary

Valsartan is an angiotensin II receptor blocker (ARB) originally used to treat hypertension.
The TxGNN model predicts it may be effective for **malignant hypertensive renal disease**,
with a prediction score of **99.97%**, but currently only **1 indirect publication** supports this direction — no clinical trials have been identified.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (ARB class); specific licensed indication text not available in this evidence pack |
| Predicted New Indication | Malignant hypertensive renal disease |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L4 |
| Denmark Market Status | Not marketed (per evidence pack) |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for this evidence pack is flagged as a data gap. Based on known pharmacology, valsartan is an angiotensin II type 1 (AT1) receptor blocker used to treat hypertension; mechanistically, RAAS (renin-angiotensin-aldosterone system) blockade could plausibly extend to blood-pressure-driven renal injury states.

The predicted indication, malignant hypertensive renal disease, overlaps mechanistically with renal blood-pressure regulation and RAAS overactivation — AT1 blockade could theoretically reduce intraglomerular pressure and slow renal damage. However, the only supporting literature (PMID 24368192) studies **avosentan**, an endothelin receptor antagonist, not valsartan itself. This is cross-drug-class indirect evidence — mechanistically relevant, but not direct evidence for valsartan.

Notably, a closely related predicted indication in this same evidence pack, *malignant renovascular hypertension* (tied top TxGNN score), is supported by more directly relevant evidence: PMID 11560862 shows that AT1 receptor blockade prevents lethal malignant hypertension and protects the kidney in an animal model — an on-target class effect consistent with valsartan's known mechanism, though the study is dated (2001) and presumed preclinical rather than a human trial. This strengthens the overall mechanistic plausibility of AT1 blockade in malignant hypertensive/renovascular disease states, even though direct valsartan-specific evidence for either indication is still lacking.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24368192](https://pubmed.ncbi.nlm.nih.gov/24368192/) | 2014 | Review (indirect, other drug class) | Pharmacological Research | Avosentan (an endothelin receptor antagonist, not valsartan) protected against hypertensive nephropathy in a transgenic rat model at doses avoiding fluid retention — indirect mechanistic support for RAAS/blood-pressure-mediated renal protection. |

## Denmark Market Information

No Danish marketing authorisation is on file in this evidence pack (market status: Not marketed, 0 licenses recorded).

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (malignant hypertensive renal disease) is supported only by a single indirect, cross-drug-class publication (avosentan, not valsartan) with no clinical trial evidence — an evidence level of L4. In addition, the evidence pack records no current Danish marketing authorisation for valsartan and flags a **Blocking** data gap on TFDA/SmPC safety labeling (DG001), which prevents progression to the S1 safety-evaluation stage.

**To proceed, the following is needed:**
- TFDA/Danish SmPC safety label data (warnings, contraindications) — currently a Blocking data gap (DG001)
- Detailed mechanism-of-action (MOA) documentation for valsartan — currently a High-severity data gap (DG002)
- Direct (ideally human) evidence for valsartan specifically in malignant hypertensive renal disease or the closely related malignant renovascular hypertension, since current supporting literature is either indirect (different drug class) or older preclinical/animal data
- Verification of valsartan's actual Danish marketing/licensing status, since the evidence pack shows 0 licenses despite valsartan being a long-established ARB
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

