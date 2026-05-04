---
layout: default
title: Encorafenib
parent: 僅模型預測 (L5)
nav_order: 163
evidence_level: L5
indication_count: 0
---

# Encorafenib
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

# Encorafenib: Evaluation Incomplete — No Repurposing Predictions Generated

## One-Sentence Summary

Encorafenib (DB11718) is a selective BRAF kinase inhibitor used in oncology.
This Evidence Pack **could not generate repurposing predictions**, as critical inputs — including the original approved indication, mechanism of action, and Danish regulatory records — were not successfully retrieved.
This report documents the current data gaps and outlines the remediation steps required before a full evaluation can proceed.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not retrieved in this Evidence Pack |
| Predicted New Indication | None — TxGNN produced no output |
| TxGNN Prediction Score | N/A |
| Evidence Level | Cannot be assessed |
| Denmark Market Status | Not marketed (per data retrieved) |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | **Hold** |

---

## Context: Why No Prediction Was Generated

No repurposing prediction was generated for Encorafenib in this Evidence Pack. The `predicted_indications` array is empty, and both the original indication and mechanism of action were flagged as data gaps — the two most critical inputs for the TxGNN prediction pipeline.

From publicly available sources, Encorafenib is known to be a selective **Class VI BRAF kinase inhibitor** (brand name Braftovi), approved in combination with binimetinib for BRAF V600E/K-mutant unresectable or metastatic melanoma, and in combination with cetuximab for BRAF V600E-mutant metastatic colorectal cancer. These details were not captured in the Evidence Pack and therefore could not serve as TxGNN input. Until `original_indications` and `original_moa` are populated, the model has insufficient context to score and rank repurposing candidates.

Two data gaps are currently blocking progress:

| Gap ID | Item | Severity | Impact |
|--------|------|----------|--------|
| DG001 | Regulatory warnings and contraindications (SmPC) | **Blocking** | Prevents safety pre-screening |
| DG002 | Mechanism of action (MOA) | **High** | Prevents mechanistic relevance analysis and TxGNN input |

---

## Denmark Market Information

No marketing authorisations for Encorafenib were retrieved from the Danish regulatory database.

> **Important note:** Encorafenib (Braftovi) holds a centralised EMA marketing authorisation (EU/1/18/1314) that is valid across all EU/EEA member states including Denmark. The current `market_status: Not marketed` most likely reflects a **retrieval gap in the Evidence Pack pipeline** rather than an actual absence from the Danish market. It is strongly recommended to verify the current status directly via the [EMA product database](https://www.ema.europa.eu/en/medicines/human/EPAR/braftovi) or Laegemiddelstyrelsen before drawing any regulatory conclusions.

---

## Cytotoxicity

Encorafenib is an antineoplastic agent. The following is based on publicly available product information, as no DrugBank toxicity data was included in this Evidence Pack.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — Selective BRAF kinase inhibitor (Class VI RAF inhibitor) |
| Myelosuppression Risk | Low to moderate; anaemia and neutropenia have been reported, but haematological toxicity is less pronounced than with conventional cytotoxic chemotherapy |
| Emetogenicity Classification | Low to moderate (oral targeted therapy) |
| Monitoring Items | Full blood count (CBC with differential), liver function (ALT, AST, bilirubin), renal function, dermatological assessment (squamous cell carcinoma risk), ECG (QTc interval), ophthalmological evaluation |
| Handling Protection | Please refer to the SmPC — standard oral cytotoxic handling precautions apply; avoid crushing or splitting capsules |

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for complete safety information.

No safety data (warnings, contraindications, or drug interactions) was retrieved in this Evidence Pack. Gap DG001 is classified **Blocking** and must be resolved before any safety pre-screening can be completed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Evidence Pack for Encorafenib is incomplete — no original indications, mechanism of action, repurposing predictions, or safety data were retrieved. A meaningful drug repurposing evaluation cannot be completed in the current state.

**To proceed, the following is needed:**

- **Resolve DG001 (Blocking):** Retrieve regulatory warnings and contraindications from the approved SmPC — access via the [EMA EPAR for Braftovi](https://www.ema.europa.eu/en/medicines/human/EPAR/braftovi) or Laegemiddelstyrelsen
- **Resolve DG002 (High):** Query the DrugBank API for DB11718 to retrieve the mechanism of action
- **Populate `original_indications`:** Add confirmed approved indications (BRAF V600-mutant melanoma; BRAF V600E-mutant metastatic colorectal cancer) to enable TxGNN input mapping
- **Re-run the TxGNN prediction pipeline** once all inputs are complete
- **Verify Danish market status:** Confirm EMA centralised authorisation coverage — the `market_status: Not marketed` result is likely a pipeline retrieval issue
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

