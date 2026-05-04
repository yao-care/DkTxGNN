---
layout: default
title: Avanafil
parent: 僅模型預測 (L5)
nav_order: 50
evidence_level: L5
indication_count: 0
---

# Avanafil
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

# Avanafil: No TxGNN Repurposing Predictions Generated

## One-Sentence Summary

Avanafil (DB06237) is a selective phosphodiesterase type 5 (PDE5) inhibitor known internationally for the treatment of erectile dysfunction, marketed as Stendra and Spedra in various markets.
The TxGNN pipeline did not generate any repurposing predictions for this drug in the current run (v4, data cut-off: 4 April 2026).
Two unresolved data gaps — missing mechanism of action and missing safety data — prevent completion of the standard repurposing evaluation; **this report therefore functions as a data gap assessment rather than a full repurposing recommendation.**

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Erectile dysfunction (sourced from general pharmacological knowledge; not recorded in current Evidence Pack) |
| Predicted New Indication | No predictions available |
| TxGNN Prediction Score | Not applicable |
| Evidence Level | L5 — pipeline produced no candidates |
| Denmark Market Status | Not found in source database |
| Number of Marketing Authorisations | 0 (in source database) |
| Recommended Decision | Hold |

> **⚠ Important caveat on market status:** The source data underlying this Evidence Pack originates from a Taiwan regulatory database. Avanafil is authorised in the European Union under the centralised procedure as **Spedra (EU/1/13/841)** for erectile dysfunction in adult men. Danish healthcare professionals should verify the current status directly with the Danish Medicines Agency (Lægemiddelstyrelsen) or the EMA product database, as the "not found" entry is likely an artefact of the source database scope, not an accurate reflection of Danish market availability.

---

## Why No Prediction Was Generated

The TxGNN model did not return any repurposing candidates for avanafil in this run. Two potential explanations should be investigated before concluding that no repurposing signal exists:

1. **Knowledge-graph mapping gap.** If avanafil was not successfully mapped to a DrugBank or disease node in the knowledge graph, no candidate edges can be scored. The query log confirms that the DrugBank lookup returned one result (success), but upstream mapping into the TxGNN graph node set may still be incomplete.

2. **Absent indication data.** The `original_indications` field is empty in the Evidence Pack. TxGNN's graph-based scoring partly relies on existing approved indication edges. Without a seed indication node, some inference pathways may be suppressed.

**What is known from pharmacology:** Avanafil selectively inhibits cyclic GMP-specific PDE5, promoting smooth muscle relaxation and vasodilation via the nitric oxide–cGMP pathway. This mechanism has been explored beyond erectile dysfunction in drug classes including pulmonary arterial hypertension (sildenafil, tadalafil) and Raynaud's phenomenon. Whether avanafil's higher PDE5 selectivity and shorter half-life translate into a distinct repurposing profile relative to first-generation PDE5 inhibitors remains an open research question — but this cannot be assessed until the pipeline data gaps are resolved.

---

## Safety Considerations

Safety data are absent from the current Evidence Pack. Please refer to the approved Summary of Product Characteristics (SmPC) for **Spedra (avanafil)** for complete prescribing information. Key areas to review include:

- **Absolute contraindications:** Concomitant use with any form of organic nitrate or nitric oxide donor (risk of severe hypotension)
- **Cardiovascular precautions:** Risk assessment for patients with underlying cardiovascular disease prior to prescribing
- **Drug interactions:** Avanafil is metabolised primarily by CYP3A4; strong CYP3A4 inhibitors (e.g., ketoconazole, ritonavir) significantly increase avanafil exposure
- **Visual/auditory adverse effects:** Consistent with the PDE5 inhibitor class

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN pipeline returned no repurposing candidates, and two data gaps — absent safety data (severity: Blocking) and absent mechanism of action (severity: High) — prevent the evaluation from advancing through the standard S1 screening gate.

**To proceed, the following is needed:**

- [ ] **Resolve DG002 (MOA):** Query the DrugBank API for DB06237 to retrieve pharmacology, mechanism of action, and drug category classifications
- [ ] **Resolve DG001 (Safety):** Obtain the Spedra SmPC from the EMA product database or Lægemiddelstyrelsen to populate warnings and contraindications
- [ ] **Investigate TxGNN mapping:** Verify whether avanafil (DB06237) is correctly mapped to a node in the TxGNN knowledge graph (`data/external/drugbank_vocab.csv`); if absent, add manually and re-run the prediction pipeline
- [ ] **Confirm Denmark market status:** Cross-reference Spedra EU/1/13/841 against Lægemiddelstyrelsen's register to correct the Evidence Pack market status field before generating the final report
- [ ] **Re-run Evidence Pack generation** after all data gaps are resolved, targeting Evidence Pack v5 or later

---

*This report is generated for research purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before any therapeutic application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

