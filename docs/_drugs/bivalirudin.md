---
layout: default
title: Bivalirudin
parent: 僅模型預測 (L5)
nav_order: 69
evidence_level: L5
indication_count: 0
---

# Bivalirudin
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

# Bivalirudin: No Repurposing Candidates Identified by TxGNN

## One-Sentence Summary

Bivalirudin is a synthetic direct thrombin inhibitor (DTI) used as an anticoagulant, best known for its use during percutaneous coronary intervention (PCI) and in patients with, or at risk of, heparin-induced thrombocytopenia (HIT).
The current TxGNN analysis **did not generate any repurposing predictions** for this compound.
This evaluation is **incomplete** due to two critical data gaps — missing MOA data and absent Danish regulatory records — and a repurposing recommendation cannot be issued at this stage.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Anticoagulation during PCI; heparin-induced thrombocytopenia *(based on established pharmacological knowledge; no formal indication text retrieved from the Evidence Pack)* |
| Predicted New Indication | None identified |
| TxGNN Prediction Score | Not available |
| Evidence Level | Not evaluated |
| Denmark Market Status | Not marketed (0 authorisations on record) |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | **Hold** |

---

## Why No Prediction Was Generated

Bivalirudin (DrugBank ID: DB00006) is a 20-amino-acid synthetic peptide that reversibly and directly inhibits thrombin — both free and clot-bound — by binding simultaneously to the active catalytic site and the anion-binding exosite I. This bivalent binding profile distinguishes it from heparin and is the basis of its anticoagulant use in cardiovascular settings.

Despite this well-characterised pharmacological profile, the TxGNN knowledge-graph pipeline returned **no repurposing candidates** in this run. Two factors are likely responsible:

1. **Missing MOA data in the Evidence Pack.** The `original_moa` field is marked as a data gap (severity: High). Without a structured mechanism-of-action record linked to the knowledge graph, TxGNN's graph-traversal and disease-similarity modules cannot anchor the drug to downstream biological targets and pathways that would otherwise surface novel indications.

2. **No Danish regulatory linkage.** The Evidence Pack contains zero approved indications and zero marketing authorisations for Denmark. The drug-indication edges that ordinarily seed TxGNN's scoring are therefore absent, which further constrains prediction coverage.

> **Note:** Bivalirudin is centrally authorised in Europe under the brand name **Angiox** (EMA/H/C/000562). The absence of Danish national records in this Evidence Pack may reflect a data-collection gap rather than a genuine lack of availability. This should be verified against the EMA product database and the Danish Medicines Agency (Lægemiddelstyrelsen) register before concluding that the product is truly unavailable in Denmark.

---

## Safety Considerations

All safety fields (key warnings, contraindications, drug–drug interactions) are absent from the current Evidence Pack.

> Please refer to the approved Summary of Product Characteristics (SmPC) for Angiox — available via the [EMA product page](https://www.ema.europa.eu/en/medicines/human/EPAR/angiox) — for full safety information, including bleeding risk, renal dose adjustments, and interactions with other anticoagulants or antiplatelets.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model produced no repurposing predictions for Bivalirudin in this evaluation cycle, and two blocking or high-severity data gaps prevent a meaningful mechanistic or regulatory assessment from being completed. No evidence review can be performed without a target indication to anchor it.

**To proceed, the following is needed:**

- **Resolve DG002 (High) — MOA data:** Query the DrugBank API for DB00006 to retrieve structured mechanism-of-action, target, and pathway data. This is essential for TxGNN graph-based scoring and for the mechanistic rationale section.
- **Resolve DG001 (Blocking) — Danish regulatory / SmPC data:** Cross-check the EMA centralised authorisation database and Lægemiddelstyrelsen product register for Bivalirudin / Angiox. Download the current SmPC PDF to extract approved indications, warnings, and contraindications.
- **Re-run TxGNN pipeline:** Once the MOA and indication data are populated, re-execute the knowledge-graph prediction step. With bivalent thrombin inhibition as the core mechanism, candidate indications in thrombotic, inflammatory, or complement-pathway disorders may emerge.
- **Verify Denmark market availability:** Confirm whether Angiox is commercially available via EMA centralised authorisation and whether it is reimbursed under the Danish national formulary, independent of a national MA number.

---

*This report is generated for research purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before any therapeutic application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

