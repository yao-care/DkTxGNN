---
layout: default
title: Relugolix
parent: 僅模型預測 (L5)
nav_order: 370
evidence_level: L5
indication_count: 10
---

# Relugolix
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

# Relugolix: From Advanced Prostate Cancer to Nephrogenic Syndrome of Inappropriate Antidiuresis

## One-Sentence Summary

Relugolix (DrugBank DB11853) is an oral GnRH receptor antagonist whose established use is in hormone-sensitive conditions such as advanced prostate cancer and uterine fibroids/endometriosis. The TxGNN model predicts it may be effective for **Nephrogenic Syndrome of Inappropriate Antidiuresis (NSIAD)**, but this prediction is currently supported by **no registered clinical trials and no published literature** — it is a model-only signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (no licence record on file); externally known class use is advanced prostate cancer and hormone-dependent gynaecological conditions |
| Predicted New Indication | Nephrogenic Syndrome of Inappropriate Antidiuresis |
| TxGNN Prediction Score | 96.13% |
| Evidence Level | L5 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for Relugolix in this evidence pack. Based on known pharmacology, Relugolix is an oral **GnRH (gonadotropin-releasing hormone) receptor antagonist** — the same drug class referenced elsewhere in this dataset's mechanistic rationale for other candidate indications (e.g., its suppression of the gonadal hormone axis). Its established efficacy is built on suppressing sex-hormone production, which is mechanistically distinct from the pathophysiology of NSIAD.

NSIAD is a rare, typically congenital disorder caused by **gain-of-function mutations in the vasopressin V2 receptor**, leading to inappropriate free-water retention independent of gonadal hormone signaling. No direct or indirect mechanistic pathway connecting GnRH receptor antagonism to V2 receptor–driven water retention is documented in this evidence pack — the `repurposing_rationale.mechanistic_link` field for this indication is explicitly marked as not yet analyzed ("pending").

Given the absence of a substantiated mechanistic link, corroborating trials, or literature, this prediction should be treated as an early-stage hypothesis generated purely from the TxGNN knowledge-graph embedding, not as a pharmacologically validated signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

*(Query log confirms ClinicalTrials.gov and ICTRP searches for "Relugolix" + "nephrogenic syndrome of inappropriate antidiuresis" returned zero results as of 2026-03-24.)*

---

## Literature Evidence

Currently no related literature available.

*(PubMed search for "Relugolix" + "nephrogenic syndrome of inappropriate antidiuresis" returned zero results as of 2026-03-24.)*

---

## Denmark Market Information

Relugolix currently holds no marketing authorisation in Denmark (0 licences on file; market status: Not marketed). No national (Lægemiddelstyrelsen) or centralised (EMA) authorisation data is available in this evidence pack.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

*(Note: key warnings, contraindications, and drug–drug interaction data are all unrecorded in this evidence pack. This is flagged as a Blocking-severity data gap — see Conclusion below.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The prediction rests on TxGNN model output alone (Evidence Level L5), with zero clinical trials, zero literature, and no documented mechanistic pathway linking GnRH antagonism to NSIAD pathophysiology.
- Relugolix is not marketed in Denmark and has no on-file safety/label data, so no safety baseline exists to support even exploratory use.

**To proceed, the following is needed:**
- SmPC warnings, contraindications, and interaction data (Blocking data gap — required before any S1 safety screening can occur)
- Mechanism of action (MOA) documentation from DrugBank or equivalent source
- A pharmacological or preclinical rationale specifically linking GnRH receptor antagonism to vasopressin V2 receptor–mediated water retention
- Confirmation of original approved indication(s) and existing real-world safety experience, given no original indication data is currently on file
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

