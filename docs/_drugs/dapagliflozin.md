---
layout: default
title: Dapagliflozin
parent: 僅模型預測 (L5)
nav_order: 127
evidence_level: L5
indication_count: 0
---

# Dapagliflozin
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

# Dapagliflozin: Repurposing Candidate Assessment — Evidence Pack Incomplete

## One-Sentence Summary

Dapagliflozin (Forxiga®) is a selective SGLT2 inhibitor with approved indications for Type 2 Diabetes Mellitus, Heart Failure, and Chronic Kidney Disease across the EU, including Denmark. The TxGNN model has **not generated any repurposing predictions** for this drug in the current Evidence Pack, as the predicted indications list is empty. A **Hold** decision is required until the pipeline is re-executed with complete input data.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Type 2 Diabetes Mellitus; Heart Failure; Chronic Kidney Disease *(sourced from general knowledge — not present in Evidence Pack)* |
| Predicted New Indication | Not available — TxGNN prediction was not executed |
| TxGNN Prediction Score | Not available |
| Evidence Level | L5 — No prediction or supporting studies retrieved |
| Denmark Market Status | Data not retrieved *(see note below)* |
| Number of Marketing Authorisations | 0 *(data retrieval failed — see note below)* |
| Recommended Decision | **Hold** |

> **⚠️ Note on Denmark Market Data:** The Evidence Pack reports zero marketing authorisations and "not marketed" status. This almost certainly reflects a **data retrieval failure**, not actual market absence. Dapagliflozin is centrally authorised in the EU under **Forxiga® (EU/1/12/795)** by AstraZeneca, with full validity in Denmark. The regulatory data pipeline should be re-executed against the EMA product database and the Danish Medicines Agency (Laegemiddelstyrelsen) register.

---

## Why is This Prediction Reasonable?

No TxGNN repurposing prediction has been generated for dapagliflozin in this Evidence Pack, so the standard mechanistic rationale for a specific new indication cannot be provided.

From established pharmacological knowledge: Dapagliflozin selectively inhibits **sodium-glucose cotransporter 2 (SGLT2)** in the renal proximal tubule, blocking approximately 90% of filtered glucose reabsorption and driving urinary glucose excretion. Beyond glycaemic control, SGLT2 inhibition reduces tubuloglomerular feedback, lowers intraglomerular pressure, and decreases proximal tubular sodium reabsorption — mechanisms that translate into renoprotection independent of blood glucose. The resulting natriuresis and plasma volume contraction reduce cardiac preload and afterload, explaining the drug's cardiovascular benefits in heart failure.

These pleiotropic effects — metabolic, haemodynamic, anti-inflammatory, and anti-fibrotic — make dapagliflozin a mechanistically rich candidate for repurposing research. Current investigational areas include non-alcoholic steatohepatitis (NASH/MAFLD), polycystic ovary syndrome (PCOS), hyperuricaemia, and sleep-disordered breathing. However, **no TxGNN model output is available in this Evidence Pack** to support a structured repurposing analysis, and no indication-specific evidence tables can be presented.

---

## Clinical Trial Evidence

No TxGNN-predicted indication is present in this Evidence Pack. Indication-specific clinical trial retrieval was not performed.

> Currently no related clinical trial evidence is linked to a repurposing target for this candidate.

---

## Literature Evidence

No TxGNN-predicted indication is present in this Evidence Pack. Indication-specific literature retrieval was not performed.

> Currently no related literature is linked to a repurposing target for this candidate.

---

## Denmark Market Information

No marketing authorisation records were retrieved for Denmark in this Evidence Pack.

**Known regulatory context (from general knowledge):** Dapagliflozin is marketed in Denmark as **Forxiga®** under EMA centralised authorisation **EU/1/12/795** (AstraZeneca). The SmPC and EPAR are publicly available via the EMA website. The data pipeline should re-fetch this authorisation and any national records from Laegemiddelstyrelsen.

---

## Safety Considerations

No safety data was successfully retrieved in this Evidence Pack — key warnings and contraindications were not populated, and no drug–drug interaction records were found.

> Please refer to the approved Summary of Product Characteristics (SmPC) for safety information. The Forxiga SmPC (EU/1/12/795) is available at [https://www.ema.europa.eu](https://www.ema.europa.eu).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This Evidence Pack is critically incomplete — the TxGNN model produced no repurposing predictions, regulatory data for Denmark was not retrieved, and all safety fields are empty. No meaningful clinical assessment can be made on this basis.

**To proceed, the following is needed:**

- **Re-execute TxGNN prediction** for Dapagliflozin (DB06292) to generate `predicted_indications` with candidate diseases, scores, clinical trials, and literature
- **Re-fetch EMA/Danish regulatory data**: retrieve Forxiga® EU/1/12/795 authorisation details, approved indications, and current market status from Laegemiddelstyrelsen
- **Retrieve complete SmPC safety data**: key warnings, contraindications, special populations (renal impairment, pregnancy, elderly), and drug interaction profile — particularly with diuretics, insulin, and other antidiabetic agents
- **Obtain DrugBank MOA data** for DB06292 to populate the mechanism of action field
- **Re-run the full Evidence Pack pipeline** (v5 or later) with all data sources confirmed as active inputs, not just `drugbank`
- Once a valid predicted indication is identified, commission a structured clinical and regulatory feasibility review with Danish hospital pharmacy and endocrinology input
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

