---
layout: default
title: Disulfiram
parent: 僅模型預測 (L5)
nav_order: 144
evidence_level: L5
indication_count: 0
---

# Disulfiram
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

# Disulfiram (DB00822): Drug Repurposing Evaluation — Incomplete Data Package

> ⚠️ **Notice:** This Evidence Pack contains critical data gaps. The TxGNN model returned **no predicted indications**, and regulatory, safety, and mechanism-of-action data are absent from the package. This report documents current findings and specifies the remediation steps required before a full repurposing evaluation can be conducted.

---

## One-Sentence Summary

Disulfiram (DrugBank: DB00822) is a well-established aldehyde dehydrogenase (ALDH) inhibitor, classically used for alcohol use disorder (aversion therapy).
However, the current Evidence Pack contains **no TxGNN-predicted indications**, **no approved product registrations in Denmark**, and **no machine-readable safety data**, making a standard repurposing evaluation impossible at this stage.
A **Hold** decision is recommended until the blocking data gaps are resolved.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Alcohol use disorder (aversion therapy) — from general pharmacological knowledge; no structured indication data in this package |
| Predicted New Indication | **Not available** — TxGNN returned no predictions for this candidate |
| TxGNN Prediction Score | Not available |
| Evidence Level | **L5** (model prediction only — and even this is absent; effectively unranked) |
| Denmark Market Status | **Not marketed** |
| Number of Marketing Authorisations | **0** |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

No predicted indication is available in this Evidence Pack, so no mechanistic bridge analysis can be performed at this time.

From established pharmacological knowledge, Disulfiram irreversibly inhibits **aldehyde dehydrogenase (ALDH)**, causing accumulation of acetaldehyde when ethanol is ingested, which produces the disulfiram-ethanol reaction used therapeutically in alcohol aversion therapy. Outside this classical role, ALDH inhibition and secondary copper-chelating activity have attracted research interest in oncology (particularly glioblastoma and breast cancer) and infectious disease contexts — however, none of this is reflected in the current Evidence Pack, and **no structured MOA data (DB002 — High severity)** is available to formally support such reasoning here.

Once the DrugBank API query is completed and `original_moa` is populated, a mechanistic analysis can be generated.

---

## Clinical Trial Evidence

No predicted indication is present in this Evidence Pack; therefore, no indication-specific clinical trial evidence can be extracted or tabulated.

Currently no related clinical trials registered under a TxGNN-predicted indication.

---

## Literature Evidence

Currently no related literature available under a TxGNN-predicted indication.

---

## Denmark Market Information

Disulfiram has **no marketing authorisations** registered in Denmark at the time of this data pull (2026-04-05).

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|-------------------------------|-------------|-------------|-------------------|
| — | — | — | No authorisations on record |

> **Note:** Disulfiram (brand name *Antabuse*) is registered in several EU member states and has EMA precedent. A separate manual search of the Danish Medicines Agency (Lægemiddelstyrelsen) product register and the EMA centralised database is recommended to confirm whether any parallel imports or exemption-based supplies exist.

---

## Safety Considerations

> Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

All safety fields in this Evidence Pack carry blocking data gaps:

- **Key Warnings**: Not available (DG001 — Blocking severity). Source: Danish SmPC / Lægemiddelstyrelsen product monograph.
- **Contraindications**: Not available (DG001 — Blocking severity).
- **Drug–Drug Interactions**: Query returned `not_found` (0 interactions). This likely reflects a query failure rather than the absence of interactions — Disulfiram is known to interact with warfarin, phenytoin, metronidazole, and several other agents.

Until DG001 is resolved, **no safety-based prescribing decisions should be made on the basis of this report**.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Evidence Pack is structurally incomplete — the TxGNN prediction pipeline returned no candidate indications, and both the regulatory and safety data layers are absent. There is no actionable repurposing signal to evaluate at this stage.

**To proceed, the following is needed:**

1. **[DG001 — Blocking]** Retrieve the Danish SmPC (or EMA SmPC if applicable) for Disulfiram; parse warnings, contraindications, and special precautions. *Source: Lægemiddelstyrelsen / EMA product monograph PDF.*
2. **[DG002 — High]** Query DrugBank API for DB00822 to populate `original_moa`, pharmacodynamics, and toxicity fields. *Source: DrugBank `https://go.drugbank.com/drugs/DB00822`.*
3. **[Prediction Gap — Critical]** Investigate why `predicted_indications` is empty:
   - Confirm that Disulfiram (DB00822) is present in the TxGNN knowledge graph node list (`data/node.csv`).
   - Re-run `scripts/run_kg_prediction.py` with explicit DrugBank ID lookup to verify pipeline completion.
   - If the drug is absent from the KG, add it as a seed node and re-predict.
4. **[DDI Gap — High]** Re-run the DDI query with alternative drug name variants (e.g., "disulfiram", "tetraethylthiuram disulfide") and confirm the `not_found` status is not a normalisation failure.
5. **[Market Status]** Cross-check with Lægemiddelstyrelsen's online product register and EMA's EPAR database to confirm zero-authorisation status and identify any compassionate-use or named-patient supply pathways currently active in Denmark.

---

*This report was generated from Evidence Pack `TW-DB00822-multi` (v4, data cutoff 2026-04-05). Results are for research reference only and do not constitute medical advice. All repurposing candidates require clinical validation before application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

