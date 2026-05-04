---
layout: default
title: Gabapentin
parent: 僅模型預測 (L5)
nav_order: 198
evidence_level: L5
indication_count: 0
---

# Gabapentin
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

# Gabapentin: Evidence Pack Incomplete — Repurposing Evaluation Pending

## One-Sentence Summary

Gabapentin (DB00996) is a drug with confirmed DrugBank records, but this Evidence Pack contains **no TxGNN predicted indications**, making a standard repurposing evaluation impossible at this time.
Key data gaps — including original indications, mechanism of action, Denmark market status, and safety data — must be resolved before any evaluation can proceed.
A **Hold** decision is recommended until the pipeline is corrected and predictions are generated.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not captured in this Evidence Pack |
| Predicted New Indication | No predictions generated |
| TxGNN Prediction Score | Not available |
| Evidence Level | Not assessable |
| Denmark Market Status | Not available (data pipeline error suspected) |
| Number of Marketing Authorisations | 0 (likely incomplete — see below) |
| Recommended Decision | **Hold** |

---

## Why This Evaluation Cannot Proceed

The Evidence Pack for Gabapentin (DB00996) is missing three categories of data that are each individually sufficient to block evaluation:

**1. No TxGNN predicted indications**
The `predicted_indications` array is empty. A repurposing evaluation requires at least one prediction target. Without it, there is no disease context against which clinical trials or literature can be assessed. This is the most critical blocker.

**2. Original indication and mechanism of action unavailable**
Both `original_indications` and `original_moa` are absent from this Evidence Pack. The data pipeline flagged MOA as a high-severity gap (DG002) and recommended retrieval from DrugBank — notably, the DrugBank query on 2026-03-26 returned status `success` with 1 result, suggesting the data exists in DrugBank but was not transferred into this Evidence Pack.

**3. Denmark market status appears to be a pipeline error**
The Evidence Pack reports `market_status: "未上市"` (not marketed) with 0 licences. Gabapentin has been authorised in the EU for many years; a result of zero licences strongly suggests a connection failure to the Lægemiddelstyrelsen or EMA data source rather than a genuine absence of authorisations. This must be verified before any regulatory assessment is made.

---

## Denmark Market Information

No marketing authorisation records were retrieved in this Evidence Pack. Manual verification with the Danish Medicines Agency (Lægemiddelstyrelsen) or the EMA product database is required before this field can be populated.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Evidence Pack is missing its most essential input — TxGNN predicted indications — and cannot support any structured repurposing evaluation. All downstream sections (clinical trial evidence, literature evidence, mechanism analysis, safety review) depend on a prediction target being present.

**To proceed, the following is needed:**

- **Re-run TxGNN prediction pipeline** for Gabapentin (DB00996) to generate `predicted_indications`; confirm whether the empty result reflects a true model output or a pipeline execution failure
- **Retrieve MOA and original indications from DrugBank** — the 2026-03-26 DrugBank query returned success; the data should be extracted and populated into the Evidence Pack
- **Verify Denmark regulatory data** — check the Lægemiddelstyrelsen / EMA data connection; the "0 licences" result is inconsistent with known EU regulatory history for this drug
- **Resolve DG001 (TFDA warnings/contraindications)** — download and parse the applicable SmPC PDF to populate safety fields before any clinical assessment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

