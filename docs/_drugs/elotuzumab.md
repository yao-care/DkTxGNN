---
layout: default
title: Elotuzumab
parent: 僅模型預測 (L5)
nav_order: 160
evidence_level: L5
indication_count: 0
---

# Elotuzumab
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

# Elotuzumab: Multiple Myeloma — TxGNN Predictions Not Available

## One-Sentence Summary

Elotuzumab (Empliciti) is a SLAMF7-targeting immunotherapy monoclonal antibody approved for the treatment of relapsed or refractory multiple myeloma in combination with lenalidomide or pomalidomide plus dexamethasone.
The current Evidence Pack (v4, candidate `TW-DB06317-multi`) contains **no TxGNN-predicted new indications** for this drug, and two critical data gaps — mechanism of action detail and regulatory safety data — remain unresolved.
A repurposing assessment **cannot be completed** with the information currently available; the recommended action is to hold pending data remediation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Multiple myeloma (relapsed/refractory) — in combination with lenalidomide + dexamethasone or pomalidomide + dexamethasone |
| Predicted New Indication | Not available — no TxGNN predictions in current Evidence Pack |
| TxGNN Prediction Score | Not available |
| Evidence Level | Unable to determine — no prediction output generated |
| Denmark Market Status | Not registered in queried national database |
| Number of Marketing Authorisations | 0 (queried national database); EMA centralised authorisation exists separately |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

*This section normally provides mechanistic rationale for a TxGNN-predicted new indication. Because no predictions are available in this Evidence Pack, it instead documents the current state of knowledge about the drug to support future analysis.*

Elotuzumab is a humanised IgG1 monoclonal antibody that targets **SLAMF7** (Signaling Lymphocytic Activation Molecule Family member 7, also known as CS1/CRACC/CD319) — a glycoprotein highly expressed on multiple myeloma cells and natural killer (NK) cells. Its dual mechanism of action combines direct antibody-dependent cellular cytotoxicity (ADCC) through NK cell activation with direct opsonisation of malignant plasma cells, establishing it as a clinically validated immunotherapy in the multiple myeloma space.

The DrugBank query for DB06317 returned a successful result, confirming the drug record exists. However, detailed mechanism of action data was flagged as a **High-severity data gap** (DG002), meaning the structured MOA fields required for the mechanistic plausibility analysis were not populated. Separately, the regulatory safety data query — covering contraindications and package insert warnings — was flagged as a **Blocking-severity data gap** (DG001), preventing the standard safety pre-screen from being completed.

Without TxGNN prediction output, a formal repurposing hypothesis cannot be evaluated at this stage. From a biological standpoint, SLAMF7 expression has been reported in certain other haematological malignancies beyond myeloma (including some NK/T-cell lymphomas and Waldenström macroglobulinaemia), suggesting that repurposing potential may exist. Realising this potential, however, requires the model to produce ranked predictions and confidence scores before a structured assessment can proceed.

---

## Denmark Market Information

No national marketing authorisations were found in the queried regulatory database (0 records; market status: not registered).

> **Important note for Danish prescribers:** Elotuzumab is authorised in the European Union under the **EMA centralised procedure** as **Empliciti** (Bristol-Myers Squibb / AbbVie), approved since 2016. This centralised authorisation is valid in all EU/EEA member states including Denmark. The absence of records in the locally queried database reflects the data pipeline's coverage, not a lack of legal authorisation. The EMA SmPC for Empliciti is the authoritative safety reference document.

---

## Cytotoxicity

Elotuzumab is used exclusively in the treatment of multiple myeloma, a haematological malignancy. The cytotoxicity section applies.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted immunotherapy — SLAMF7-directed humanised IgG1 monoclonal antibody |
| Myelosuppression Risk | Low for elotuzumab as a single agent; **Moderate to High** in standard combination regimens (lenalidomide + dexamethasone or pomalidomide + dexamethasone) due to the partner drugs |
| Emetogenicity Classification | Low |
| Monitoring Items | CBC with differential (to monitor for lenalidomide/pomalidomide-associated neutropenia and thrombocytopenia), liver function tests, infusion-related reaction monitoring (fever, chills, hypertension — most common during first infusion), lymphocyte counts |
| Handling Protection | Elotuzumab itself does not require cytotoxic handling precautions; combination partners **lenalidomide and pomalidomide** are teratogenic IMiDs subject to strict Pregnancy Prevention Programmes (PPP) — prescribers must comply with REVLIMID/IMNOVID REMS-equivalent EU risk management requirements |

---

## Safety Considerations

Both safety data fields (key warnings and contraindications) are flagged as unresolved data gaps in the current Evidence Pack, and no drug–drug interaction records were returned from the DDI query.

> Please refer to the approved Summary of Product Characteristics (SmPC) for **Empliciti** (available via the EMA product page) for complete safety information, including infusion reaction management, infection risk, secondary malignancy monitoring, and embryo-foetal toxicity guidance specific to combination regimens.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Evidence Pack for Elotuzumab (DB06317) is currently incomplete in two critical areas: no TxGNN prediction output was generated, and both the mechanism of action detail and regulatory safety data are absent. Without a predicted indication to evaluate and without a safety pre-screen, a repurposing assessment cannot meet the minimum evidence threshold required to move forward.

**To proceed, the following is needed:**

- **TxGNN prediction output (Critical):** Re-run the TxGNN model for DrugBank ID DB06317 to generate ranked predicted indications with confidence scores. Verify whether the `multi` suffix in the candidate ID (`TW-DB06317-multi`) indicates a known pipeline processing issue.
- **Mechanism of action data (High priority — DG002):** Retrieve the structured MOA from the DrugBank API for DB06317, including pharmacological action, target proteins, and pathway associations.
- **Regulatory safety data (Blocking — DG001):** Download and parse the EMA SmPC for Empliciti to populate warnings, contraindications, and special population guidance (renal/hepatic impairment, pregnancy).
- **EMA authorisation cross-reference:** Map the EMA centralised marketing authorisation number for Empliciti into the Denmark market information section to provide an accurate regulatory landscape for Danish prescribers.
- **DDI data supplement:** Retrieve drug–drug interaction data for elotuzumab in the context of its standard combination partners (lenalidomide, pomalidomide, dexamethasone, bortezomib) from a validated DDI resource (e.g., DrugBank interactions, SFINX, or Lexi-Interact).
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

