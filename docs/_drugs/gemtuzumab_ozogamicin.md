---
layout: default
title: Gemtuzumab Ozogamicin
parent: 僅模型預測 (L5)
nav_order: 208
evidence_level: L5
indication_count: 0
---

# Gemtuzumab Ozogamicin
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

---

# Gemtuzumab Ozogamicin: Repurposing Evaluation Blocked — Data Gaps Require Resolution

---

## One-Sentence Summary

Gemtuzumab ozogamicin (DrugBank ID: DB00056) was identified in the pipeline but could not be evaluated for drug repurposing in this cycle.
The TxGNN model generated **no predicted indications**, as two upstream data gaps — missing regulatory label data and missing mechanism of action — prevented the prediction pipeline from running.
This report documents the gaps and defines the remediation steps required before evaluation can proceed.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available |
| Predicted New Indication | No prediction generated |
| TxGNN Prediction Score | Not available |
| Evidence Level | L5 — model prediction only, no supporting studies |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | **Hold** |

---

## Why Could No Prediction Be Generated?

The TxGNN repurposing pipeline requires two inputs to function: a confirmed mechanism of action (to locate the drug node in the knowledge graph) and at least one approved indication (to establish the drug's existing disease associations).

For gemtuzumab ozogamicin, both inputs are absent from the current Evidence Pack. The MOA field was not populated from DrugBank (DG002), and no original indication records were retrieved (DG001 — no regulatory label). Without these anchors, the knowledge graph cannot place the drug in its correct therapeutic context, and the prediction model cannot produce meaningful output.

From the INN suffix convention, "-ozogamicin" designates a calicheamicin-conjugated antibody-drug conjugate (ADC). This naming convention places gemtuzumab ozogamicin within the cytotoxic antineoplastic class. However, this structural inference alone is not sufficient to drive the TxGNN prediction — confirmed indication and MOA data must be loaded first. Once those data gaps are resolved, the pipeline should be re-run.

---

## Cytotoxicity

> This section is included because the INN suffix "-ozogamicin" identifies this agent as a calicheamicin-conjugated antibody-drug conjugate — a known cytotoxic antineoplastic class.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Antibody-drug conjugate (ADC) — calicheamicin conjugate (inferred from INN suffix; confirmation from DrugBank/SmPC required) |
| Myelosuppression Risk | Please refer to the approved Summary of Product Characteristics (SmPC) — calicheamicin ADCs are typically associated with significant haematological toxicity |
| Emetogenicity Classification | Please refer to the SmPC |
| Monitoring Items | Please refer to the SmPC — typically includes complete blood count (CBC with differential), liver function tests, and hepatic veno-occlusive disease surveillance |
| Handling Protection | Must follow cytotoxic drug handling regulations — treat as cytotoxic until SmPC confirms otherwise |

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

No key warnings, contraindications, or drug interaction data were available in this Evidence Pack. All safety fields returned as gaps (DG001). Retrieving the regulatory label is classified as a **Blocking** data gap before any safety screening can begin.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Two data gaps — one classified as Blocking (DG001: regulatory label) and one as High severity (DG002: MOA) — prevent the TxGNN prediction pipeline from generating any output. Until these are resolved, no repurposing signal can be evaluated and no safety screening can be completed.

**To proceed, the following is needed:**

- **[DG001 — Blocking]** Retrieve the product label (SmPC) from the Danish Medicines Agency (Laegemiddelstyrelsen) or the EMA centralised database. Note: gemtuzumab ozogamicin may hold a centralised EMA authorisation (Mylotarg®, Pfizer); the 0-licence result in the current Evidence Pack should be verified against the EMA product register before concluding the drug is absent from the Danish market.
- **[DG002 — High]** Query the DrugBank API (DB00056) to populate the mechanism of action field — specifically the antibody target and the cytotoxic payload linkage.
- **Re-run prediction pipeline** after both fields are populated, and generate a new Evidence Pack version.
- **Confirm market status** by cross-checking Laegemiddelstyrelsen and the EMA EPAR database for any active or historical centralised marketing authorisations covering Denmark.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

