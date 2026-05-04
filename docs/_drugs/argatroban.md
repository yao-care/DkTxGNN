---
layout: default
title: Argatroban
parent: 僅模型預測 (L5)
nav_order: 45
evidence_level: L5
indication_count: 0
---

# Argatroban
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

# Argatroban: Drug Repurposing Evaluation — TxGNN Prediction Not Available

## One-Sentence Summary

Argatroban is a synthetic direct thrombin inhibitor used intravenously for the prophylaxis and treatment of thrombosis in patients with heparin-induced thrombocytopenia (HIT).
The current Evidence Pack contains **no TxGNN repurposing predictions** for this drug, and critical data including mechanism of action, safety warnings, and contraindications are all absent.
**A complete repurposing evaluation cannot be produced at this time; this report summarises the data gaps and required next steps.**

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Thrombosis prophylaxis/treatment in heparin-induced thrombocytopenia (HIT) *(from general knowledge; no regulatory record in dataset)* |
| Predicted New Indication | Not available — TxGNN returned no candidates |
| TxGNN Prediction Score | Not available |
| Evidence Level | Not assessable |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | **Hold** |

---

## Why This Evaluation Cannot Proceed

The Evidence Pack for Argatroban (DrugBank ID: DB00278) has two critical structural problems that prevent a standard repurposing evaluation.

**First, the TxGNN prediction pipeline returned zero repurposing candidates.** This is the foundational output the entire report structure depends on. Without at least one predicted indication and an associated score, it is not possible to assess mechanistic plausibility, search for supporting clinical trials, or rate evidence strength.

**Second, all drug-level safety data are absent.** Warnings, contraindications, and drug–drug interactions were either not retrieved or not found during the query run on 26 March 2026. For an anticoagulant drug — a class with a narrow therapeutic window and clinically significant bleeding risk — proceeding without safety data would be irresponsible.

From general pharmacological knowledge, Argatroban is a direct, reversible thrombin inhibitor. It binds the active site of thrombin and blocks thrombin-catalysed reactions including fibrin formation, platelet activation, and activation of coagulation factors V, VIII, and XIII. Unlike heparin, it does not require antithrombin as a cofactor, which makes it the agent of choice when heparin use is contraindicated due to HIT. This mechanistic profile is relevant background for any future repurposing analysis, particularly in thrombotic or inflammatory contexts where thrombin plays a pathological role.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

> **Note for the assessor:** Argatroban (brand name *Argatra*) holds a centralised EMA marketing authorisation in the European Union. The EMA SmPC is publicly available at the European Medicines Agency product pages and should be used as the primary safety reference while the TFDA/Danish national data gap is resolved.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Evidence Pack is structurally incomplete — no TxGNN predictions were generated and all safety fields are missing — making it impossible to produce a valid repurposing evaluation or safety assessment. Proceeding to clinical consideration without this data would not meet the minimum evidence threshold.

**To proceed, the following is needed:**

- **[Blocking]** Re-run the TxGNN prediction pipeline for DB00278 and confirm Argatroban is present and correctly mapped in the knowledge graph; verify the drug–disease candidate list was not inadvertently filtered out
- **[High]** Retrieve mechanism of action (MOA) data via the DrugBank API for DB00278
- **[High]** Download and parse the EMA *Argatra* SmPC (or the Danish national product information if available) to populate warnings, contraindications, and special precautions
- **[Medium]** Verify Argatroban's registration status with the Danish Medicines Agency (Lægemiddelstyrelsen); note that centralised EMA-authorised products are legally available in all EU/EEA member states even without a national marketing authorisation record
- **[Follow-up]** Once TxGNN predictions are available, run standard clinical trial (ClinicalTrials.gov, EudraCT) and literature (PubMed) evidence collection for each candidate indication

---

*This report is generated for research purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before application. This document was produced under the TxGNN Drug Repurposing Research Programme (Evidence Pack v4, data cut-off: 2026-04-04).*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

