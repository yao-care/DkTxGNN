---
layout: default
title: Reteplase
parent: 僅模型預測 (L5)
nav_order: 373
evidence_level: L5
indication_count: 10
---

# Reteplase
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

# Reteplase: From Acute Myocardial Infarction (STEMI) to Posteroinferior Myocardial Infarction

## One-Sentence Summary

Reteplase is a recombinant tissue plasminogen activator (r-tPA variant) used as thrombolytic therapy for acute ST-elevation myocardial infarction (STEMI). The TxGNN model's top-ranked prediction, **Posteroinferior Myocardial Infarction**, is flagged by the evidence pack itself as an anatomical subtype of reteplase's *existing* MI indication rather than a genuine new indication, and it is supported by **0 clinical trials** and **0 publications**. A more substantive signal exists further down the candidate list — **Septal Myocardial Infarction** (rank 5–6) is backed by a completed Phase 3 RCT (n=2,461).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acute myocardial infarction (STEMI) — thrombolytic therapy (per repurposing-rationale text in the evidence pack; not confirmed against a Danish SmPC, as the product currently holds no Danish marketing authorisation) |
| Predicted New Indication | Posteroinferior Myocardial Infarction *(anatomical subtype of the existing indication — see caveat below)* |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L4 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action (MOA) data is not available for reteplase in this evidence pack [DG002]. Based on known pharmacology, reteplase is a third-generation recombinant plasminogen activator (an engineered tPA variant) that catalyses conversion of plasminogen to plasmin, dissolving fibrin clots in occluded coronary arteries — the basis of its approved use in acute MI/STEMI.

**Important caveat on the top-ranked candidate:** the evidence pack's own repurposing rationale states that "posteroinferior myocardial infarction" is not a true new indication. TxGNN's near-identical scores across ranks 1–4 (posteroinferior MI, posterolateral MI) reflect semantic overlap in the knowledge graph between MI anatomical subtypes and MI generally, not a novel mechanistic link. No independent trials or literature were found for these subtype-labelled terms. This should be treated as an **ontology artifact** — an extension of the existing indication rather than a repurposing candidate.

A more genuine signal appears at rank 5–6, **Septal Myocardial Infarction**, supported by a completed Phase 3, multicentre, double-blind, placebo-controlled RCT (NCT00046228, n=2,461) evaluating reteplase plus abciximab in acute MI — directly on-mechanism, and evaluated at decision stage S3 with a "Proceed with Guardrails" recommendation. Ranks 9–10 (**coronary stenosis**) are similarly supported by several observational/cohort studies (GUSTO-V, SPEED/GUSTO-4 pilot) consistent with reteplase's core fibrinolytic mechanism, though no trial is registered under that exact disease label.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for **Posteroinferior Myocardial Infarction** (the ranked #1 candidate).

*For reference, the strongest trial evidence in this evidence pack relates to Septal Myocardial Infarction (rank 5–6):*

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00046228](https://clinicaltrials.gov/study/NCT00046228) | Phase 3 | Completed | 2,461 | Multicentre, randomized, double-blind, placebo-controlled trial comparing reteplase + abciximab combination therapy vs. abciximab alone before primary PCI in acute MI. |

---

## Literature Evidence

Currently no related literature available for **Posteroinferior Myocardial Infarction** (the ranked #1 candidate).

---

## Denmark Market Information

Reteplase currently holds **0 marketing authorisations** in Denmark (`market_status: 未上市 / Not marketed`). No Laegemiddelstyrelsen national or EMA centralised licence records are present in this evidence pack.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information. Key warnings, contraindications, and drug-interaction data were not available in this evidence pack [DG001 — Blocking: TFDA/SmPC label text not yet retrieved].

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked candidate (Posteroinferior Myocardial Infarction) is an anatomical subtype of reteplase's existing approved indication rather than a novel repurposing signal, has zero supporting trials or literature, and is explicitly flagged in the evidence pack as a knowledge-graph ontology artifact. Combined with the blocking gap on Danish label/safety data (DG001) and missing MOA confirmation (DG002), this candidate cannot proceed past initial screening.

**To proceed, the following is needed:**
- Danish SmPC / regulatory label text (warnings, contraindications, DDI) — currently blocking (DG001)
- Confirmed mechanism of action data from DrugBank (DG002)
- A decision on whether MI anatomical-subtype predictions (ranks 1–4, 7–8) should be excluded from the candidate pipeline as ontology duplicates, or re-scored against the parent "myocardial infarction" indication
- If pursuing an evidence-backed candidate instead, **Septal Myocardial Infarction** (L1 evidence, Phase 3 RCT, "Proceed with Guardrails") and **Coronary Stenosis** (L3 evidence, multiple cohort studies) warrant separate evaluation as the more substantive repurposing signals in this evidence pack
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

