---
layout: default
title: Epoprostenol
parent: 僅模型預測 (L5)
nav_order: 169
evidence_level: L5
indication_count: 0
---

# Epoprostenol
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

# Epoprostenol (DB01240): Pulmonary Arterial Hypertension — Evidence Pack Incomplete, Assessment Pending

---

## One-Sentence Summary

Epoprostenol (prostacyclin, PGI₂) is a synthetic vasodilator and platelet aggregation inhibitor classically used in the management of pulmonary arterial hypertension (PAH).
However, the current Evidence Pack contains **no TxGNN prediction output** and **no Denmark market authorisation records**, meaning a full drug repurposing evaluation cannot be completed at this stage.
This report documents the identified data gaps and recommends a structured remediation pathway before proceeding.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Pulmonary arterial hypertension (based on general pharmacological knowledge; not supplied in evidence pack) |
| Predicted New Indication | No prediction data available |
| TxGNN Prediction Score | No prediction data available |
| Evidence Level | Not assessable |
| Denmark Market Status | Not recorded (0 licences on file — likely a data collection gap; EU centralised authorisations exist) |
| Number of Marketing Authorisations | 0 (on file) |
| Recommended Decision | **Hold** — critical data gaps must be resolved first |

---

## Why This Report Cannot Be Completed Yet

The TxGNN model prediction pipeline did not return any repurposing candidates for Epoprostenol in this Evidence Pack (version v4, data cut-off 2026-04-05). Two high-severity data gaps have been formally logged:

| Gap ID | Category | Missing Item | Severity | Impact |
|--------|----------|-------------|----------|--------|
| DG001 | Drug Level | Danish Medicines Agency (Laegemiddelstyrelsen) / EMA approved warnings and contraindications | **Blocking** | Cannot complete S1 safety screening |
| DG002 | Drug Level | Mechanism of action (MOA) | **High** | Cannot perform mechanistic plausibility analysis for any predicted indication |

Until these gaps are resolved and the TxGNN pipeline is re-run with complete input data, a meaningful repurposing evaluation cannot be generated.

---

## Denmark Market Information

The evidence pack records **zero marketing authorisations** for Epoprostenol in Denmark. This is inconsistent with publicly known regulatory status: Epoprostenol is available in the EU under centralised EMA procedures (e.g., *Flolan*, *Veletri*), which automatically confer authorisation in all EU/EEA member states including Denmark.

**This strongly suggests a data collection failure rather than true absence from the Danish market.**

| Expected Authorisation | Product Name | Dosage Form | Note |
|------------------------|-------------|-------------|------|
| EMA centralised (verify via EMA EPAR database) | Flolan | Powder and solvent for solution for infusion | PAH — verify current status at ema.europa.eu |
| EMA centralised (verify via EMA EPAR database) | Veletri | Powder for solution for infusion | PAH — verify current status at ema.europa.eu |

> **Action required:** Query the [EMA Product Database](https://www.ema.europa.eu/en/medicines) and the [Laegemiddelstyrelsen produktresume database](https://www.laegemiddelstyrelsen.dk/) to retrieve current authorisation numbers, SmPC, and approved indications.

---

## Safety Considerations

No safety data was retrieved for this evidence pack. All key warnings, contraindications, and drug interaction fields are absent.

> Please refer to the approved Summary of Product Characteristics (SmPC) — available via the [EMA EPAR for Flolan](https://www.ema.europa.eu/en/medicines/human/EPAR/flolan) or [Veletri](https://www.ema.europa.eu/en/medicines/human/EPAR/veletri) — for complete safety information before any clinical assessment.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Evidence Pack for Epoprostenol is missing both the TxGNN prediction output and Denmark/EMA regulatory safety data, making it impossible to assess any repurposing hypothesis or evaluate risk–benefit at this stage.

**To proceed, the following is needed:**

1. **Re-run the TxGNN pipeline** for DB01240 and confirm that `predicted_indications` is populated with at least one candidate before generating a full report.
2. **Retrieve MOA data (DG002)** from DrugBank API (DrugBank ID: DB01240) — Epoprostenol is expected to act via prostacyclin receptor (IP receptor) agonism, leading to cAMP-mediated vasodilation and inhibition of platelet aggregation; confirm and populate `original_moa`.
3. **Retrieve SmPC warnings and contraindications (DG001)** from the EMA EPAR documents for Flolan/Veletri; parse and populate `safety.key_warnings` and `safety.contraindications`.
4. **Correct the Denmark regulatory record** by querying the EMA centralised authorisation database and the Laegemiddelstyrelsen produktresume register; update `taiwan_regulatory.market_status`, `total_licenses`, and `licenses[]`.
5. **Re-submit the completed Evidence Pack** to regenerate a full evaluation report with predicted indications, mechanistic rationale, clinical trial evidence, and a final Go / Proceed with Guardrails recommendation.

---

*This report is generated for research reference only and does not constitute medical advice. All drug repurposing candidates require clinical validation before any therapeutic application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

