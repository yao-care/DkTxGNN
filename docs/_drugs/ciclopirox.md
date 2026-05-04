---
layout: default
title: Ciclopirox
parent: 僅模型預測 (L5)
nav_order: 110
evidence_level: L5
indication_count: 0
---

# Ciclopirox
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

# Ciclopirox: No TxGNN Prediction Available — Insufficient Data for Repurposing Assessment

## One-Sentence Summary

Ciclopirox (DrugBank: DB01188) is a broad-spectrum antifungal agent primarily used topically for dermatomycoses and onychomycosis.
**No TxGNN repurposing prediction is available** for this candidate in the current Evidence Pack, as the `predicted_indications` array is empty.
Without a model-generated target indication or supporting evidence, a full repurposing evaluation cannot be completed at this stage.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Fungal skin and nail infections (dermatomycoses, onychomycosis) — based on general pharmacological knowledge; no TFDA/SmPC data loaded |
| Predicted New Indication | Not available — no TxGNN prediction generated |
| TxGNN Prediction Score | Not available |
| Evidence Level | L5 (no supporting studies identified in this pack) |
| Denmark Market Status | Not marketed (no authorisations registered with Laegemiddelstyrelsen) |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | **Hold** |

---

## Why No Prediction Is Available

The Evidence Pack for this candidate (TW-DB01188-multi, v4) was generated with two confirmed data gaps that together prevent a complete analysis:

1. **Missing mechanism of action (MOA) data** — DrugBank query returned a record (query ID 2, status: success), but MOA was not extracted into the pack. Ciclopirox is known to act by chelating polyvalent metal cations (Fe³⁺, Al³⁺) that are essential cofactors for fungal cytochrome-dependent enzymes, thereby disrupting DNA repair, cell respiration, and cell division. However, this information has not been formally validated and loaded into the pipeline.

2. **No TFDA/regulatory label data** — The TFDA Summary of Product Characteristics (SmPC), including approved indications and contraindications, was not retrieved (data gap DG001, severity: Blocking). This is a prerequisite for the Safety Stage 1 screening.

Without these two inputs, the TxGNN knowledge-graph matching and disease-mapping steps could not produce a ranked prediction list, resulting in an empty `predicted_indications` field.

---

## Denmark Market Information

Ciclopirox currently holds **no marketing authorisations** with the Danish Medicines Agency (Laegemiddelstyrelsen) and is not listed as a marketed product in Denmark. Neither a national authorisation nor a centralised EMA authorisation has been identified for this substance.

> Note: Ciclopirox is marketed in several other EU/EEA countries (e.g., Germany, France) under brand names such as **Batrafen** and **Mycoster**, primarily as topical formulations (cream, solution, nail lacquer). A centralised or mutual-recognition procedure application may be a pathway if a Danish indication is pursued.

---

## Safety Considerations

Both key warnings and contraindications were listed as data gaps in this Evidence Pack. No drug–drug interaction records were found in the DDI query (query ID 1, status: not\_found).

> Please refer to the approved Summary of Product Characteristics (SmPC) — available from the EMA product database or national agencies where ciclopirox is authorised — for full safety information including contraindications, warnings, and drug interactions.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Evidence Pack is structurally incomplete — both the TxGNN predicted indication and the regulatory safety data are missing, making it impossible to assess repurposing feasibility or safety profile at this stage.

**To proceed, the following is needed:**

- [ ] **Retrieve TFDA SmPC / EMA SmPC**: Download and parse the approved product label to extract indications, contraindications, and key warnings (resolves data gap DG001 — Blocking)
- [ ] **Load MOA from DrugBank API**: The DrugBank query was successful (result\_count: 1); re-run the extraction step to populate `original_moa` (resolves data gap DG002 — High)
- [ ] **Re-run TxGNN prediction pipeline**: Once MOA and indication data are loaded, re-execute the knowledge-graph and deep-learning prediction steps to generate `predicted_indications`
- [ ] **Confirm Denmark regulatory pathway**: Although ciclopirox is not currently marketed in Denmark, assess whether an existing EMA centralised authorisation or mutual-recognition procedure can serve as the basis for a Danish application
- [ ] **Re-generate Evidence Pack**: After the above steps, generate a new pack (v5+) for full L1–L5 evidence assessment and final Go/Hold/Proceed with Guardrails decision
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

