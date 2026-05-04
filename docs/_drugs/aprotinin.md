---
layout: default
title: Aprotinin
parent: 僅模型預測 (L5)
nav_order: 44
evidence_level: L5
indication_count: 0
---

# Aprotinin
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

# Aprotinin: No Repurposing Predictions Available for Evaluation

---

## One-Sentence Summary

Aprotinin is a serine protease inhibitor (Kunitz-type, bovine-derived) historically used as an antifibrinolytic agent to reduce perioperative blood loss in cardiac surgery.
The current Evidence Pack contains **no TxGNN repurposing predictions** for this compound, and aprotinin holds no marketing authorisations in Denmark.
Without prediction data, clinical trial evidence, or literature evidence in the pack, a standard repurposing assessment cannot be completed at this stage.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Antifibrinolytic; reduction of perioperative blood loss in cardiac surgery (not registered in Denmark) |
| Predicted New Indication | None generated |
| TxGNN Prediction Score | Not available |
| Evidence Level | L5 — model prediction pipeline produced no output |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | **Hold** |

---

## Why No Predictions Were Generated

Aprotinin (DrugBank DB06692) is a 58-amino-acid serine protease inhibitor derived from bovine lung tissue. It inhibits trypsin, plasmin, and plasma kallikrein, thereby attenuating the fibrinolytic cascade and contact-phase activation that contribute to coagulopathy during cardiopulmonary bypass surgery. Marketed under the brand name Trasylol, it was once the most widely used antifibrinolytic in high-risk cardiac procedures.

Aprotinin was voluntarily suspended from most markets in 2007–2008 after the Canadian BART trial (Blood conservation using Antifibrinolytics in a Randomized Trial) demonstrated a significantly higher 30-day mortality compared with the lysine analogues tranexamic acid and aminocaproic acid. The European Medicines Agency subsequently reinstated a restricted authorisation in 2012, limiting use to adult patients undergoing isolated coronary artery bypass graft (CABG) surgery when other antifibrinolytics are not suitable, under close haemodynamic monitoring.

The absence of TxGNN predictions in this Evidence Pack most likely reflects one of the following:

1. **Knowledge graph gap** — Aprotinin may not be represented as a node in the TxGNN drug–disease graph, or its DrugBank ID was not matched to a graph entity.
2. **Below-threshold scores** — All candidate disease scores fell below the model's reporting threshold.
3. **Upstream data gap** — Missing mechanism-of-action data (flagged as data gap DG002) may have impaired graph embedding quality, suppressing prediction output.

The query log confirms that a DrugBank query returned a successful result (`result_status: success`, `result_count: 1`), indicating the compound was identified, yet no predictions were propagated downstream.

---

## Denmark Market Information

Aprotinin currently holds no marketing authorisations in Denmark and is classified as not marketed. Historically, Trasylol received EMA centralised authorisation, which was suspended in 2007 and partially reinstated in 2012 under a restricted indication for isolated CABG surgery. Any clinical use in Denmark today would require a named-patient or compassionate-use authorisation from Lægemiddelstyrelsen, subject to risk–benefit documentation and institutional approval.

---

## Safety Considerations

No structured safety data (warnings, contraindications, or drug interactions) are available in this Evidence Pack. Based on published EMA and FDA documentation, clinicians should be aware of the following key concerns before any use:

- **Mortality risk**: Increased 30-day all-cause mortality versus lysine analogues, established in the BART trial.
- **Serious organ injury**: Elevated risk of acute renal failure, myocardial infarction, and stroke in cardiac surgery patients.
- **Hypersensitivity / anaphylaxis**: Risk is substantially increased on re-exposure (prior aprotinin use within 12 months is a documented risk factor); a 10,000 KIU test dose and pre-medication protocol are required.
- **Re-exposure interval**: A minimum 12-month interval between exposures is recommended per SmPC.

Please refer to the approved Summary of Product Characteristics (SmPC) for Trasylol and the EMA product information for complete and current safety guidance.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN pipeline produced no repurposing predictions for aprotinin, the drug is not authorised in Denmark, and critical input data (MOA, approved indications, safety profile) are absent from the Evidence Pack. There is no candidate indication to evaluate at this stage.

**To proceed, the following is needed:**

- **Resolve the prediction gap**: Verify whether aprotinin (DB06692) exists as a node in the TxGNN knowledge graph; if absent, request graph inclusion before re-running the pipeline.
- **Retrieve MOA data**: Query the DrugBank API for DB06692 to obtain full pharmacology data (Data Gap DG002 — severity: High).
- **Retrieve safety profile**: Download the Trasylol SmPC from the EMA product database and parse warnings and contraindications (Data Gap DG001 — severity: Blocking).
- **Clarify EU regulatory status**: Confirm current authorisation status of Trasylol with Lægemiddelstyrelsen or via the EMA product database, given the complex suspension–reinstatement history.
- **Re-run TxGNN**: Once graph membership and MOA data are confirmed, re-run the prediction pipeline and generate a new Evidence Pack.
- **If predictions are generated**: Proceed to evidence collection (ClinicalTrials.gov, PubMed) for the top-ranked indication and re-issue this report at a higher evidence level.

---

> **Disclaimer**: This report is generated for research reference purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before application. This document does not replace the approved Summary of Product Characteristics or clinical judgement.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

