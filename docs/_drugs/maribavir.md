---
layout: default
title: Maribavir
parent: 僅模型預測 (L5)
nav_order: 223
evidence_level: L5
indication_count: 0
---

# Maribavir
{: .fs-9 }

證據等級: **L5** | 預測適應症: **0** 個
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

# Maribavir: Drug Repurposing Assessment — Evidence Pack Incomplete

## One-Sentence Summary

Maribavir (DrugBank ID: DB06234) is a first-in-class antiviral agent known from publicly available sources to target cytomegalovirus (CMV) UL97 kinase, approved in the USA (Livtencity®) for post-transplant CMV infection refractory to prior therapy. The current Evidence Pack contains **no TxGNN-predicted repurposing indications**, and three critical data fields — original indications, mechanism of action, and safety information — are absent or unresolved. **A full drug repurposing evaluation cannot be completed at this stage** until the identified data gaps are remediated.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not recorded in evidence pack |
| Predicted New Indication | None — `predicted_indications` array is empty |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 — no predictions available |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | **Hold** |

---

## Why a Full Evaluation Cannot Proceed

The Evidence Pack contains two blocking and one high-severity data gaps that together prevent any repurposing evaluation from being completed:

**No TxGNN-predicted indications (Blocking).** The `predicted_indications` array is empty. This is the foundational input for any drug repurposing report — without at least one model-predicted target indication, there is no repurposing hypothesis to evaluate, no evidence to assess, and no go/no-go recommendation to make for a specific new use.

**Missing safety data (Blocking).** All key warnings and contraindications are unresolved. Safety pre-screening is a mandatory step before any repurposing pathway can advance. This gap alone would prevent the report from reaching a clinical recommendation even if predictions were available.

**Missing mechanism of action (High severity).** Mechanistic plausibility is a core pillar of repurposing evaluation. Without MOA data, it is impossible to assess whether Maribavir's pharmacology is applicable to any candidate indication.

---

## Denmark Market Information

Maribavir is **not currently marketed in Denmark** according to the evidence pack. There are no active marketing authorisations recorded with Laegemiddelstyrelsen (the Danish Medicines Agency) or via the EMA centralised procedure.

> **Important verification needed:** Maribavir (Livtencity®, Takeda) received EMA centralised marketing authorisation for the treatment of post-transplant CMV infection in adults. If a valid EU authorisation exists, it should appear in the Denmark regulatory section. The absence of records here is likely a data collection gap rather than a true absence of authorisation. This must be verified directly via the [EMA Product Database](https://www.ema.europa.eu/en/medicines) before any regulatory assessment is made.

---

## Safety Considerations

All safety data fields in the evidence pack are unresolved. No safety summary can be generated from the current data.

> Please refer to the approved Summary of Product Characteristics (SmPC) for safety information. The SmPC for Livtencity® is available via the EMA website.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Evidence Pack is incomplete and does not contain the minimum required inputs for a drug repurposing evaluation. The TxGNN prediction pipeline has not produced results for this candidate, and all safety data are missing. No clinical recommendation of any kind can be made until these gaps are resolved.

**To proceed, the following is needed:**

- [ ] **Re-run TxGNN prediction pipeline** for Maribavir (DB06234) to populate `predicted_indications` — this is the single most critical step
- [ ] **Retrieve mechanism of action from DrugBank API** (DB06234) to resolve data gap DG002
- [ ] **Download and parse the SmPC** from the EMA product database to resolve data gap DG001 (warnings, contraindications, interactions)
- [ ] **Verify EMA centralised authorisation status** for Livtencity® and update the Denmark regulatory section accordingly
- [ ] **Re-generate the Evidence Pack (v5)** once the above gaps are resolved, then proceed with full evaluation

---

> ⚠️ **Disclaimer:** This report is for research purposes only and does not constitute medical advice. Any drug repurposing candidate identified by TxGNN requires clinical validation before application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

