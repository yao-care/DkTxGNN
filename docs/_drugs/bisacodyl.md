---
layout: default
title: Bisacodyl
parent: 僅模型預測 (L5)
nav_order: 67
evidence_level: L5
indication_count: 0
---

# Bisacodyl
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

# Bisacodyl: Evidence Pack Incomplete — No TxGNN Repurposing Predictions Available

## One-Sentence Summary

Bisacodyl (DB09020) is a stimulant laxative established in clinical practice for the short-term treatment of constipation and bowel preparation prior to colonoscopy or surgery. The current Evidence Pack contains **no TxGNN-predicted new indications**, and three critical data categories — mechanism of action, Danish regulatory records, and safety profile — are absent. This report documents the data state as of 2026-04-04 and cannot progress to a full repurposing evaluation without remediation of the identified gaps.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available — no Danish marketing authorisation records in current dataset |
| Predicted New Indication | None — TxGNN predictions absent from this Evidence Pack |
| TxGNN Prediction Score | N/A |
| Evidence Level | N/A |
| Denmark Market Status | Not marketed (per current data; likely a data collection gap — see note below) |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

This section cannot be completed as the `predicted_indications` array in the Evidence Pack is empty. No TxGNN repurposing candidate has been generated for Bisacodyl in this pipeline run. The most probable causes are: (1) Bisacodyl was not successfully mapped to a DrugBank node in the TxGNN knowledge graph, (2) the prediction step was not executed for this compound, or (3) Bisacodyl falls below the model's scoring threshold for all disease nodes.

Detailed mechanism of action data is not available in this Evidence Pack (Data Gap DG002). Based on established pharmacological knowledge, Bisacodyl is a diphenylmethane derivative that acts directly on the colonic mucosa: it stimulates enteric nerve endings, accelerates peristalsis, and promotes luminal fluid accumulation by altering electrolyte transport in colonocytes. This locally-acting mechanism is distinct from systemic drug targets commonly explored in repurposing research, which may limit TxGNN's ability to generate knowledge-graph-based predictions.

To unlock a repurposing evaluation, the DrugBank record for DB09020 must be retrieved to populate the MOA and pharmacological target fields, and the TxGNN prediction pipeline must be re-executed with a confirmed DrugBank node mapping.

---

## Denmark Market Information

No marketing authorisations are currently recorded in the dataset for Bisacodyl. This almost certainly reflects a **data collection gap** rather than genuine absence from the Danish market: Bisacodyl is a widely available over-the-counter (OTC) laxative sold across the EU and would ordinarily appear in the Danish Medicines Agency (Lægemiddelstyrelsen) register. The following reconciliation steps are required before market status can be reported:

- Query the Lægemiddelstyrelsen product register directly for Bisacodyl and its brand equivalents (e.g., *Dulcolax*, *Toilax*)
- Check the EMA centralised authorisation database, noting that Bisacodyl is a non-prescription product and may be registered nationally rather than centrally
- Update `taiwan_regulatory` (Denmark regulatory) fields accordingly before re-running this Evidence Pack

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

> **Note:** Safety data — including key warnings, contraindications, and drug interaction data — are absent from this Evidence Pack (Data Gap DG001, severity: Blocking). The Danish SmPC PDF should be retrieved from the Lægemiddelstyrelsen website and parsed before any clinical or regulatory decision is made.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Evidence Pack for Bisacodyl (DB09020) is critically incomplete across all three evaluation pillars — predictive, regulatory, and safety — making a drug repurposing assessment impossible at this stage. Proceeding without remediation would produce a report with no actionable content for healthcare professionals.

**To proceed, the following is needed:**

- **Re-run TxGNN predictions** for DB09020 after confirming the correct DrugBank node mapping; verify whether Bisacodyl appears in `data/external/drugbank_vocab.csv`
- **Retrieve DrugBank record** via the DrugBank API to populate mechanism of action, pharmacological targets, and toxicity data (Data Gap DG002 — severity: High)
- **Retrieve Danish SmPC** from Lægemiddelstyrelsen to obtain approved indications, boxed warnings, contraindications, and drug interactions (Data Gap DG001 — severity: Blocking)
- **Reconcile market status** against the Lægemiddelstyrelsen national product register and EMA database; update `total_licenses` and `licenses[]` accordingly
- **Re-generate Evidence Pack** (targeting version v5) once all blocking gaps are resolved, then re-trigger the full report pipeline
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

