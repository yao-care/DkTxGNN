---
layout: default
title: Bortezomib
parent: 僅模型預測 (L5)
nav_order: 71
evidence_level: L5
indication_count: 0
---

# Bortezomib
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

# Bortezomib: Drug Repurposing Evaluation — Insufficient Evidence Pack for Candidate Analysis

## One-Sentence Summary

Bortezomib is a proteasome inhibitor approved internationally for multiple myeloma and mantle cell lymphoma. The current Evidence Pack contains **no TxGNN-predicted new indications** and carries two critical data gaps — a Blocking-severity gap in safety data (DG001) and a High-severity gap in mechanism of action (DG002) — making a complete repurposing evaluation impossible at this stage. This report documents the current state and the remediation steps required before evaluation can proceed.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Multiple myeloma and mantle cell lymphoma (internationally approved; not registered in Danish data) |
| Predicted New Indication | Not available — no predictions present in current Evidence Pack |
| TxGNN Prediction Score | Not available |
| Evidence Level | Not evaluable |
| Denmark Market Status | Not found in local database (0 marketing authorisations) |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | **Hold** |

> ⚠️ **Data Note:** Bortezomib is marketed as **Velcade** under an EMA centralised marketing authorisation valid across the EU/EEA, including Denmark. The zero-licence result likely reflects a gap in the local Laegemiddelstyrelsen database query rather than actual non-availability. This should be verified against the EMA product database before drawing conclusions about Danish market status.

---

## Mechanism of Action (Background Information)

> The Evidence Pack flags mechanism of action as a data gap (DG002, severity: High). The following is based on published literature and DrugBank, not from the Evidence Pack itself.

Bortezomib is a **reversible inhibitor of the 26S proteasome chymotrypsin-like activity**. The 26S proteasome is responsible for degrading ubiquitinated proteins that regulate the cell cycle, apoptosis, and transcription factor signalling (notably NF-κB). By blocking this degradation pathway, bortezomib causes accumulation of pro-apoptotic factors and cell cycle arrest, selectively exploiting the high proteasome dependence of malignant plasma cells.

This mechanistic profile is the basis for its proven efficacy in **multiple myeloma** — and has been the subject of research into other haematologic malignancies and even solid tumours where proteasome pathway activity is dysregulated.

Because predicted indications are absent from this Evidence Pack, the applicability of this mechanism to any new indication cannot be formally assessed at this time.

---

## Cytotoxicity

Bortezomib meets the inclusion criteria for this section: it is a targeted antineoplastic agent used in haematologic malignancies.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — Proteasome inhibitor |
| Myelosuppression Risk | **High** — thrombocytopenia is the dose-limiting toxicity; Grade 3/4 thrombocytopenia occurs in approximately 30% of patients. Neutropenia is also common. Platelet counts typically nadir around Day 11 of each cycle and recover by Day 21. |
| Emetogenicity Classification | Low |
| Monitoring Items | Full blood count (FBC) with differential and platelet count prior to each dose cycle, liver function tests (LFTs), renal function (eGFR), serum electrolytes (potassium, sodium, calcium), peripheral neuropathy assessment at each visit |
| Handling Protection | Must be handled following cytotoxic drug handling regulations. **Critical safety alert:** Bortezomib must **never** be administered intrathecally — intrathecal administration is fatal. Subcutaneous administration is preferred over intravenous to reduce peripheral neuropathy incidence. |

---

## Safety Considerations

The Evidence Pack has a **Blocking-severity** data gap (DG001) in TFDA/SmPC safety warnings and contraindications. No DDI data was retrieved.

Please refer to the approved **Summary of Product Characteristics (SmPC)** for full safety information.

Based on published literature, the following safety areas warrant particular attention pending formal SmPC review:

- **Peripheral neuropathy:** A significant and potentially dose-limiting toxicity. Pre-existing neuropathy is a relative contraindication. Subcutaneous administration substantially reduces this risk.
- **Thrombocytopenia:** Patients with platelet counts below threshold should not receive treatment; full blood count monitoring is mandatory before each cycle.
- **Orthostatic hypotension:** Patients should be monitored for dizziness and syncope, particularly those on antihypertensive therapy.
- **Cardiac events:** Cases of congestive heart failure and QT prolongation have been reported; baseline cardiac assessment is advisable.
- **Intrathecal fatality risk:** This must be prominently communicated to all clinical staff involved in preparation and administration.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Evidence Pack contains no TxGNN-predicted new indications, which is the primary input required to initiate a repurposing evaluation. In addition, two data gaps — one Blocking (safety data) and one High-severity (MOA) — prevent the mandatory safety pre-screening step (S1) from being completed. No recommendation for or against a repurposing candidate can be made until these gaps are resolved.

**To proceed, the following is needed:**

1. **Re-run TxGNN prediction pipeline** for Bortezomib (DrugBank ID: DB00188) to generate predicted indication candidates with scores — this is the foundational missing input.
2. **Resolve DG001 (Blocking):** Download and parse the TFDA/EMA SmPC PDF to extract warnings, contraindications, and special populations data.
3. **Resolve DG002 (High):** Query DrugBank API for full MOA, pharmacodynamics, and drug categories for DB00188.
4. **Verify Danish market status:** Cross-check the EMA centralised authorisation database for Velcade to confirm EMA-authorised availability in Denmark and retrieve the correct Marketing Authorisation numbers for the Denmark Market Information table.
5. **Re-run DDI query:** The DDI query returned `not_found`; retry with alternative spellings or DrugBank ID to confirm whether there are genuine absence of interactions or a query failure.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

