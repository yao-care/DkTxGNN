---
layout: default
title: Faricimab
parent: 僅模型預測 (L5)
nav_order: 186
evidence_level: L5
indication_count: 0
---

# Faricimab
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

# Faricimab: Drug Repurposing Evaluation Report

## One-Sentence Summary

Faricimab is a bispecific monoclonal antibody (targeting VEGF-A and Ang-2) approved internationally for neovascular age-related macular degeneration (nAMD) and diabetic macular oedema (DME), marketed as Vabysmo® by Roche.
The TxGNN model has **no predicted new indications** for this drug at present, and the evidence pack contains significant data gaps that prevent a full evaluation.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in evidence pack (internationally approved for nAMD and DME) |
| Predicted New Indication | **None** — no TxGNN predictions available |
| TxGNN Prediction Score | N/A |
| Evidence Level | **L5** (No prediction or supporting studies in this dataset) |
| Denmark Market Status | **Not marketed** |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | **Hold** |

> **Note:** Faricimab (Vabysmo®) holds a centralised EMA marketing authorisation (EU/1/22/1683) for nAMD and DME. The evidence pack's Denmark-specific licence records show 0 entries, which may reflect an incomplete data import rather than true absence from the Danish market. This should be verified against the Laegemiddelstyrelsen and EMA registers.

---

## Why is This Prediction Reasonable?

There is currently **no TxGNN-predicted new indication** for Faricimab, so a mechanistic plausibility assessment cannot be performed.

For background: Faricimab is the first bispecific antibody approved for intraocular use. It simultaneously inhibits vascular endothelial growth factor A (VEGF-A) and angiopoietin-2 (Ang-2), two key drivers of pathological angiogenesis and vascular instability. By targeting both pathways, it aims to achieve greater vascular stabilisation than anti-VEGF monotherapy alone. Its mechanism of action data was flagged as a data gap (DG002) in this evidence pack and should be retrieved from DrugBank for any future evaluation round.

Until the TxGNN knowledge graph generates candidate indications for Faricimab and supporting evidence is gathered, no mechanistic bridge to a new indication can be assessed.

---

## Clinical Trial Evidence

Currently no TxGNN-predicted indication exists for Faricimab; therefore, no indication-specific clinical trial search was performed.

---

## Literature Evidence

Currently no TxGNN-predicted indication exists for Faricimab; therefore, no indication-specific literature search was performed.

---

## Denmark Market Information

No marketing authorisations were recorded in the evidence pack.

> **Verification recommended:** Faricimab (Vabysmo®) received a centralised EMA marketing authorisation (EU/1/22/1683) in September 2022 for nAMD and DME. Danish availability should be confirmed with the Laegemiddelstyrelsen medicines database or the EMA Union Register.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

> The evidence pack flagged the following blocking data gaps:
> - **DG001 (Blocking):** Labelling warnings and contraindications are not yet available — these must be retrieved from the SmPC before any Stage 1 safety screening can proceed.
> - **DG002 (High):** Mechanism of action details are missing — to be queried from DrugBank.
>
> No drug–drug interactions were identified in the DDI database search (query date: 2026-03-26). This may reflect the intravitreal route of administration, which generally results in minimal systemic exposure.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No TxGNN-predicted new indications are available for Faricimab, and multiple critical data gaps (SmPC safety data, mechanism of action) remain unresolved. There is insufficient information to evaluate any repurposing opportunity at this time.

**To proceed, the following is needed:**
- **Resolve DG001:** Retrieve the full SmPC (warnings, contraindications, special populations) from the EMA or Laegemiddelstyrelsen — this is a blocking prerequisite for Stage 1 safety review
- **Resolve DG002:** Query DrugBank API for detailed mechanism of action, pharmacodynamics, and target information
- **Verify Denmark market status:** Confirm whether the EMA centralised authorisation (EU/1/22/1683) provides Danish market access and update the licence records accordingly
- **Re-run TxGNN prediction pipeline:** Once the drug is properly mapped in the knowledge graph with complete DrugBank data, re-execute the KG and DL prediction models to generate candidate indications
- **Populate original indications:** Record the EMA-approved indications (nAMD, DME) in the evidence pack to enable future mechanistic bridging analyses

---

*This report is for research purposes only and does not constitute medical advice. Any drug repurposing candidates require clinical validation before application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

