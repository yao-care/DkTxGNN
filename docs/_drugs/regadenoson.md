---
layout: default
title: Regadenoson
parent: 僅模型預測 (L5)
nav_order: 368
evidence_level: L5
indication_count: 8
---

# Regadenoson
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

# Regadenoson: From Pharmacologic Cardiac Stress Testing to Anaphylaxis

## One-Sentence Summary

Regadenoson is a selective A2A adenosine receptor agonist used clinically as a pharmacologic stress agent for cardiac perfusion imaging (not as a treatment for a disease indication). The TxGNN model predicts it may be effective for **Anaphylaxis**, but this is supported by only **1 clinical trial** (not actually testing this use) and **0 publications** — and the drug's own known adverse-effect profile suggests the signal likely points in the wrong direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not a treated disease — used as a pharmacologic stress agent for cardiac perfusion imaging (per evidence-pack mechanistic notes); the drug is not marketed in Denmark, so no approved indication text exists |
| Predicted New Indication | Anaphylaxis |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L5 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for regadenoson is not available in the evidence pack (flagged as a High-severity data gap). Based on the mechanistic notes that were captured, regadenoson is a selective **A2A adenosine receptor agonist**, used clinically to induce pharmacologic coronary vasodilation during myocardial perfusion stress imaging — it is a diagnostic tool, not a therapeutic agent for a disease indication.

Critically, the evidence pack's own analysis casts strong doubt on this prediction rather than supporting it. Regadenoson's known adverse-reaction profile includes flushing, dyspnea, and hypotension — pseudoallergic (anaphylactoid) reactions mediated by A2A/A3 receptor activation on mast cells and basophils. These are documented **risks of the drug**, not treatment effects. The most plausible explanation is that TxGNN learned a co-occurrence pattern between regadenoson and anaphylaxis-related terms from adverse-event data, and misclassified this as a therapeutic relationship — meaning the predicted mechanism likely runs in the **opposite direction** from what would be needed for repurposing.

The same caution applies to the other candidate indications returned for this drug (food-dependent exercise-induced anaphylaxis, esotropia, pseudoallergy) — none have any supporting clinical or mechanistic evidence, and two of them share the same "reversed adverse-event signal" concern as anaphylaxis. Separately, note that the ranked candidate list contains exact duplicate entries (ranks 1–2, 3–4, 5–6, 7–8 are each the same disease with identical scores and evidence) — this appears to be a data-pipeline artifact and should be corrected before further review.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06854458](https://clinicaltrials.gov/study/NCT06854458) | N/A | Recruiting | 1000 | Multicenter stress cardiac MRI perfusion imaging study; regadenoson is used only as a pharmacologic stress agent to simulate exercise for cardiac imaging. It does not evaluate regadenoson for treating anaphylaxis (relevance graded **C — low relevance** in the evidence pack). |

---

## Literature Evidence

Currently no related literature available.

---

## Denmark Market Information

Regadenoson is currently **not marketed** in Denmark — no national (Laegemiddelstyrelsen) or centralised (EMA) marketing authorisations were found in the evidence pack (0 licenses on record).

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for detailed safety information; structured warning, contraindication, and drug-interaction data were not available in this evidence pack (flagged as a Blocking data gap).

One point worth flagging for clinical review: the drug's known adverse-effect profile (flushing, dyspnea, hypotension, and pseudoallergic/anaphylactoid reactions via A2A/A3 receptor activation) overlaps directly with the predicted indication itself (anaphylaxis), which is the basis for treating this prediction with caution rather than as a genuine therapeutic signal.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- Evidence level is L5 (model prediction only) with no relevant clinical trials or literature; the single trial identified does not test regadenoson for anaphylaxis. The evidence pack's own mechanistic analysis suggests the TxGNN signal likely reflects a reversed adverse-event association rather than a genuine treatment effect, and the same concern applies to the drug's other candidate indications.

**To proceed, the following is needed:**
- Regadenoson SmPC warnings/contraindications (currently a Blocking data gap)
- Verified mechanism of action (MOA) data from DrugBank or another primary source
- Independent pharmacological review to confirm or rule out the "reversed signal" hypothesis before any further evaluation
- Correction of the duplicate entries in the predicted-indications list at the data pipeline level
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

