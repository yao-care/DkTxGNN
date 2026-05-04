---
layout: default
title: Blinatumomab
parent: 僅模型預測 (L5)
nav_order: 70
evidence_level: L5
indication_count: 0
---

# Blinatumomab
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

# Blinatumomab: Preliminary Assessment — TxGNN Prediction Data Unavailable

## One-Sentence Summary

Blinatumomab (Blincyto) is a first-in-class bispecific T-cell engager (BiTE) antibody approved for relapsed or refractory B-cell precursor acute lymphoblastic leukaemia (ALL), which works by redirecting a patient's own T cells to destroy CD19-expressing cancer cells. No TxGNN drug repurposing predictions are currently available for this candidate — the `predicted_indications` field in the Evidence Pack is empty — meaning a full repurposing evaluation cannot be completed at this stage. This report documents the current data status, flags critical gaps, and recommends a **Hold** pending re-execution of the prediction pipeline.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Relapsed/refractory B-cell precursor acute lymphoblastic leukaemia (ALL) |
| Predicted New Indication | Not available — TxGNN prediction pending |
| TxGNN Prediction Score | Not available |
| Evidence Level | Not determinable |
| Denmark Market Status | Not recorded (0 authorisations in data pack — see note below) |
| Number of Marketing Authorisations | 0 (per data pack; likely a data retrieval gap — see note) |
| Recommended Decision | **Hold** |

> **⚠️ Data note on market status:** Blinatumomab is marketed as **Blincyto** under EMA centralised authorisation **EU/1/15/1047**, which is valid in all EU/EEA member states including Denmark. The zero-licence result in this Evidence Pack likely reflects a gap in the data retrieval pipeline rather than true absence from the Danish market. Manual verification against the Lægemiddelstyrelsen register and EMA EPAR is recommended.

---

## Drug Background and Known Mechanistic Profile

Although no TxGNN predictions are available, the following background is provided to support prioritisation decisions.

Blinatumomab belongs to the bispecific T-cell engager (BiTE) class of immunotherapies. It simultaneously binds **CD19** on B-lineage tumour cells and **CD3ε** on cytotoxic T cells, forming an artificial immunological synapse that activates T cells — independently of MHC presentation — and triggers serial lysis of CD19+ target cells. This mechanism is structurally distinct from conventional chemotherapy and monoclonal antibodies, making it potentially applicable across a range of CD19-expressing haematological malignancies beyond ALL.

Current EMA-approved indications for Blincyto include:
- Relapsed or refractory (R/R) Philadelphia chromosome-negative (Ph–) B-cell precursor ALL in adults and paediatric patients
- MRD-positive (minimal residual disease) B-cell precursor ALL in adults

The drug's mechanism of action data was flagged as a **High-severity data gap (DG002)** in the Evidence Pack. Retrieval from the DrugBank API (DB09052) is required before mechanistic rationale analysis can be completed formally.

---

## Cytotoxicity

Blinatumomab is classified as an antineoplastic agent (immunotherapy). This section is included as the drug carries the oncology indication profile and specific toxicity management requirements that differ from standard systemic chemotherapy.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted immunotherapy — Bispecific T-cell Engager (BiTE antibody); not a conventional cytotoxic agent |
| Myelosuppression Risk | Moderate to High — febrile neutropenia, anaemia, and thrombocytopenia are commonly reported; attributable partly to underlying disease and partly to immune activation |
| Emetogenicity Classification | Low — nausea may occur but is not primarily emetogenic; standard antiemetic prophylaxis not routinely required |
| Monitoring Items | Full blood count with differential (frequent during cycles 1–2), liver function tests, neurological status (daily during hospitalisation phase), signs of cytokine release syndrome (CRS) and immune effector cell-associated neurotoxicity syndrome (ICANS) |
| Handling Protection | Administered as a continuous IV infusion via ambulatory pump (up to 4 weeks); follows institutional biologic/monoclonal antibody handling guidelines — not classified as a traditional hazardous cytotoxic, but local institutional policies apply |

---

## Safety Considerations

Structured safety data (warnings, contraindications, drug interactions) were not returned by the data pipeline for this Evidence Pack. Please refer to the approved Summary of Product Characteristics (SmPC) for Blincyto, available via the [EMA product page for EU/1/15/1047](https://www.ema.europa.eu/en/medicines/human/EPAR/blincyto), with particular attention to:

- **Cytokine Release Syndrome (CRS):** Requires stepwise dose escalation, mandatory hospitalisation for the first 9 days of cycles 1 and 2, and a documented CRS management protocol including corticosteroids and tocilizumab.
- **Neurological toxicity (ICANS/encephalopathy):** Seizures, speech disorders, and impaired consciousness have been reported; treatment interruption criteria are defined in the SmPC.
- **Infection risk:** Opportunistic infections including PML (progressive multifocal leukoencephalopathy) have been reported.
- **Tumour lysis syndrome:** Pre-treatment hydration and uric acid management are recommended.
- **Preparation and administration:** Requires specific IV bag preparation with stabiliser solution; errors in preparation carry serious risk.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Evidence Pack contains no TxGNN-predicted indications for blinatumomab, making it impossible to conduct a repurposing evaluation. Without a target indication, neither clinical evidence retrieval nor a benefit–risk assessment can be performed in a meaningful way.

**To proceed, the following is needed:**

- **[Critical]** Re-run the TxGNN prediction pipeline for `DB09052` (blinatumomab) and populate `predicted_indications` — this is a blocking prerequisite for any repurposing assessment.
- **[High]** Retrieve mechanism of action and pharmacology data from the DrugBank API for `DB09052` to enable mechanistic rationale analysis.
- **[Blocking]** Retrieve the Danish SmPC / safety data: warnings, contraindications, and drug interaction profile.
- **[Recommended]** Manually verify Danish marketing authorisation status against the Lægemiddelstyrelsen register and cross-reference with the EMA EPAR for Blincyto (EU/1/15/1047) to correct the apparent data retrieval gap showing 0 licences.
- Once a complete Evidence Pack (v5+) is available with populated `predicted_indications`, re-issue this report following the standard evaluation framework.

---

> *This report is generated for research purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before any therapeutic application. This page includes a YMYL disclaimer: information presented here is preliminary and must not be used to inform clinical decision-making.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

