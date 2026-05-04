---
layout: default
title: Daratumumab
parent: 僅模型預測 (L5)
nav_order: 129
evidence_level: L5
indication_count: 0
---

# Daratumumab
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

# Daratumumab: No Repurposing Predictions Generated — Evaluation Pending

## One-Sentence Summary

Daratumumab (DB09331) is a CD38-targeting monoclonal antibody used in the treatment of multiple myeloma, registered by the EMA under the brand name Darzalex.
The TxGNN prediction pipeline **did not generate any repurposing predictions** for this drug in the current evaluation cycle, as critical input data — including the mechanism of action and original indication fields — were absent from the Evidence Pack.
**No clinical trial or literature evidence could therefore be retrieved or assessed**, and a formal repurposing evaluation cannot be completed at this stage.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not recorded in Evidence Pack |
| Predicted New Indication | None generated |
| TxGNN Prediction Score | Not available |
| Evidence Level | Not assessable (L5 floor not reached — no prediction output) |
| Denmark Market Status | Not registered per Evidence Pack data |
| Number of Marketing Authorisations | 0 (per Evidence Pack) |
| Recommended Decision | **Hold** |

> ⚠️ **Data integrity note:** The Evidence Pack records 0 Danish marketing authorisations and "not marketed" status. This is inconsistent with the publicly known EMA centralised authorisation for Darzalex (daratumumab) for multiple myeloma, which is valid across all EU/EEA member states including Denmark. The regulatory data source should be verified before relying on this field.

---

## Why No Predictions Were Generated

The TxGNN model requires two inputs to generate repurposing candidates: (1) a validated DrugBank ID matched to the knowledge graph, and (2) at least one mapped approved indication from which the model infers mechanistic similarity. For daratumumab (DB09331), the Evidence Pack confirms a successful DrugBank query but records **no original indications** in the `original_indications` field. Without a source indication node, the model cannot traverse the knowledge graph to identify candidate target diseases, and no prediction score is output.

Additionally, the mechanism of action (MOA) field is absent. MOA data is used downstream to contextualise and prioritise candidates; its absence means that even manual prioritisation of any future model output would be impaired.

From general pharmacological knowledge, daratumumab binds CD38 — a glycoprotein highly expressed on plasma cells — and induces tumour cell death through antibody-dependent cellular cytotoxicity (ADCC), complement-dependent cytotoxicity (CDC), and apoptosis. Its approved use in multiple myeloma is well-established and biologically coherent. Once the Evidence Pack is remediated (see Next Steps), the TxGNN model may generate predictions for haematological malignancies and potentially other CD38-expressing conditions, such as systemic lupus erythematosus or AL amyloidosis — both areas of active clinical investigation globally.

---

## Cytotoxicity

Daratumumab is classified as an antineoplastic agent (targeted immunotherapy / monoclonal antibody) based on its approved therapeutic use in multiple myeloma.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted immunotherapy — anti-CD38 IgG1κ monoclonal antibody (not conventional cytotoxic) |
| Myelosuppression Risk | Moderate to High — infusion-related reactions, neutropenia, thrombocytopenia, and anaemia are commonly reported in product labelling |
| Emetogenicity Classification | Low (monoclonal antibodies carry minimal direct emetogenic potential) |
| Monitoring Items | Full blood count (CBC with differential) prior to each cycle; renal function; immunoglobulin levels; hepatitis B screening before initiation |
| Handling Protection | Standard aseptic handling for parenteral biologics; no cytotoxic-drug special waste classification required, but institutional biohazard protocols for monoclonal antibodies apply |

> Please refer to the approved SmPC for Darzalex for full prescribing, handling, and monitoring guidance.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for Darzalex for full safety information, including infusion-related reaction management, immunisation precautions, and interference with serum protein electrophoresis assays (daratumumab is a known source of false-positive M-protein results).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Evidence Pack for daratumumab (DB09331) is critically incomplete — no original indication data, no mechanism of action, and no TxGNN repurposing predictions were generated. A meaningful repurposing evaluation cannot be conducted on the basis of available data alone, and proceeding to clinical feasibility assessment would be premature.

**To proceed, the following is needed:**

- **[Blocking — DG001]** Retrieve the SmPC / product information for Darzalex from the EMA product database or the Danish Medicines Agency (Lægemiddelstyrelsen) to extract approved indications, key warnings, and contraindications
- **[High — DG002]** Query the DrugBank API for DB09331 to populate the MOA field; this is required for the knowledge graph prediction step and for mechanistic plausibility analysis
- **Re-run TxGNN pipeline** once `original_indications` and `original_moa` are populated in the Evidence Pack
- **Correct the regulatory data** — verify Denmark / EMA marketing authorisation status against the EMA EPAR database (Darzalex EU/1/16/1101); the current "not marketed" flag appears to reflect a data source gap rather than actual market absence
- **Supplementary search** — once predictions are generated, collect clinical trial data from ClinicalTrials.gov and EudraCT / EU Clinical Trials Register for any emerging indications (e.g., AL amyloidosis, POEMS syndrome, lupus nephritis) to assess evidence level

---

*This report is generated for research purposes only and does not constitute medical advice. All repurposing candidates require clinical validation before any therapeutic application. Report generated: 2026-04-05 | Evidence Pack version: v4 | Candidate ID: TW-DB09331-multi.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

