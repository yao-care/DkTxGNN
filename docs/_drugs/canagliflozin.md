---
layout: default
title: Canagliflozin
parent: 僅模型預測 (L5)
nav_order: 85
evidence_level: L5
indication_count: 0
---

# Canagliflozin
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

# Canagliflozin: Drug Repurposing Candidate Evaluation — Evidence Pack Incomplete

## One-Sentence Summary

Canagliflozin (DrugBank: DB08907) is a sodium-glucose cotransporter 2 (SGLT2) inhibitor with established use in type 2 diabetes mellitus and cardiovascular/renal protection.
However, the current Evidence Pack contains **no TxGNN predicted indications**, and key data fields including mechanism of action, safety warnings, and regulatory approval records are absent.
A complete evaluation cannot be performed at this stage; a **Hold** decision is warranted until the data gaps are resolved.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not recorded in Evidence Pack (known from literature: Type 2 diabetes mellitus) |
| Predicted New Indication | None — TxGNN output not present in this Evidence Pack |
| TxGNN Prediction Score | Not available |
| Evidence Level | L5 (model prediction data absent; no supporting studies linked in pack) |
| Denmark Market Status | Not marketed (per Evidence Pack) |
| Number of Marketing Authorisations | 0 (per Evidence Pack) |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

No TxGNN predicted indication is included in this Evidence Pack, so a formal mechanistic rationale linking the original indication to a new target indication cannot be constructed.

Based on publicly available pharmacological knowledge, canagliflozin belongs to the SGLT2 inhibitor class. It acts in the renal proximal tubule by blocking sodium-glucose cotransporter 2, thereby reducing glucose reabsorption and increasing urinary glucose excretion. Beyond glycaemic control, SGLT2 inhibitors have demonstrated natriuretic and haemodynamic effects with implications for heart failure and chronic kidney disease — areas that have attracted significant repurposing interest.

Until the TxGNN prediction pipeline is re-run and the Evidence Pack is regenerated with a valid `predicted_indications` array, no mechanistic association analysis can be formally completed for this candidate.

---

## Clinical Trial Evidence

Currently no related clinical trial evidence is linked in this Evidence Pack.

> **Note:** This reflects the absence of data in the `predicted_indications` field, not necessarily the absence of real-world trial activity for canagliflozin. Once a target indication is identified by the TxGNN model, a dedicated evidence query should be executed against ClinicalTrials.gov and the EU Clinical Trials Register (EudraCT / CTIS).

---

## Literature Evidence

Currently no related literature is linked in this Evidence Pack.

> **Note:** As above, this is a consequence of missing `predicted_indications` data, not a reflection of the overall published literature for canagliflozin.

---

## Denmark Market Information

Per the Evidence Pack, canagliflozin has **0 marketing authorisations** and is recorded as **not marketed**.

> **Important caveat for reviewers:** This Evidence Pack was generated from a regulatory data source that may not reflect the current Danish/EMA registration status. Canagliflozin-containing products (e.g., Invokana, Vokanamet) hold EMA centralised marketing authorisations that are valid in Denmark. Reviewers are strongly advised to verify the current status directly via:
> - [EMA product page](https://www.ema.europa.eu/en/medicines/human/EPAR/invokana)
> - [Laegemiddelstyrelsen (DKMA) product database](https://laegemiddelstyrelsen.dk/)

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for full safety information, as no safety data is present in this Evidence Pack.

> The following data gaps have been flagged as requiring resolution before any safety-based evaluation can proceed:
> - **TFDA labelling warnings and contraindications** (Severity: Blocking) — prevents entry into safety screening Stage 1
> - **Mechanism of action data** (Severity: High) — prevents mechanistic relevance analysis

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Evidence Pack for canagliflozin (DB08907) is critically incomplete: no TxGNN predicted indications are present, mechanism of action data is absent, and all safety fields are empty. Without a predicted target indication, no evidence-based repurposing evaluation can be conducted, and no recommendation regarding clinical development can be made.

**To proceed, the following is needed:**

- [ ] **Re-run TxGNN prediction pipeline** for DB08907 to populate `predicted_indications` — this is the single most important blocker
- [ ] **Retrieve mechanism of action data** from DrugBank API for DB08907 (Data Gap DG002, severity: High)
- [ ] **Retrieve SmPC safety data** including warnings and contraindications from the Danish/EMA label (Data Gap DG001, severity: Blocking)
- [ ] **Verify Denmark market status** against the EMA centralised authorisation database and the DKMA product register, as the Evidence Pack value of "not marketed" appears inconsistent with known EMA approvals
- [ ] **Re-generate the Evidence Pack** with complete inputs before scheduling a formal evaluation review

---

*This report was generated from Evidence Pack `TW-DB08907-multi` (v4, data cutoff 2026-04-04). Due to critical data gaps, this document serves as a triage record only and does not constitute a complete drug repurposing evaluation. All findings are for research reference only and do not constitute medical advice. Any repurposing candidate requires clinical validation before application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

