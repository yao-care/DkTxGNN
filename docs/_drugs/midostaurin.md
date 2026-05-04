---
layout: default
title: Midostaurin
parent: 僅模型預測 (L5)
nav_order: 234
evidence_level: L5
indication_count: 0
---

# Midostaurin
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

# Midostaurin (DB06595): Drug Repurposing Assessment — TxGNN Prediction Data Unavailable

---

## One-Sentence Summary

Midostaurin (Rydapt®) is a multi-targeted kinase inhibitor with established antineoplastic activity, notably approved in the EU for FLT3-mutated acute myeloid leukaemia and advanced systemic mastocytosis.
The current Evidence Pack contains **no TxGNN repurposing predictions** for this compound, and two critical data fields — mechanism of action and national prescribing information — are missing.
**A complete drug repurposing evaluation cannot be conducted at this time; a Hold decision is recommended pending data remediation.**

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | FLT3-mutated AML; advanced systemic mastocytosis *(sourced from general pharmaceutical knowledge — absent from Evidence Pack)* |
| Predicted New Indication | Not available — TxGNN pipeline returned no candidates |
| TxGNN Prediction Score | Not available |
| Evidence Level | Not determinable |
| Denmark Market Status | Not found in Laegemiddelstyrelsen national registry |
| Number of Marketing Authorisations | 0 (national registry query) |
| Recommended Decision | **Hold** |

---

## Why No Prediction Is Available

The Evidence Pack for midostaurin (DB06595) contains an empty `predicted_indications` array, meaning the TxGNN pipeline did not return any repurposing candidates as of the data cutoff (2026-04-04). Two upstream data gaps most likely caused this failure:

**Missing mechanism of action (MOA).** The DrugBank query returned a result record (query log ID 2, status: success), yet the `original_moa` field was not populated. Without a pharmacological mechanism profile, the TxGNN graph model lacks the node features needed to score drug–disease links reliably.

**Missing regulatory prescribing information.** The Laegemiddelstyrelsen registry query returned zero licences. Notably, midostaurin holds an EMA centralised marketing authorisation (Rydapt®, EU/1/17/1213, granted June 2017) for use in Denmark and other EU member states. The national registry query appears not to have captured this centralised pathway, leaving indication vocabulary unmapped. This directly limits disease-node alignment in the knowledge graph and may have suppressed candidate generation.

Until these gaps are resolved, any repurposing hypothesis for midostaurin would rest on the model's structural graph inference alone, without pharmacological or regulatory context — which is insufficient for a clinical evaluation.

---

## Denmark Market Information

The Evidence Pack reports zero marketing authorisations via the Laegemiddelstyrelsen national registry. Based on publicly available pharmaceutical records, Rydapt® (midostaurin 25 mg hard capsules, Novartis) holds an EMA centralised authorisation accessible in Denmark; however, this must be formally verified before the next pipeline run.

| Note | Detail |
|------|--------|
| National registry result | 0 licences retrieved |
| Expected EMA authorisation | EU/1/17/1213 (Rydapt® — requires verification) |
| Recommended action | Query EMA EPAR database directly; confirm product is on the Danish formulary and retrieve the approved indication text for disease mapping |

---

## Cytotoxicity

Midostaurin is classified as an antineoplastic agent on the basis of its approved indications (AML, systemic mastocytosis) and its mechanism of action as a multi-targeted protein kinase inhibitor. The section below is based on general pharmaceutical knowledge, as the Evidence Pack did not supply drug-level safety data; all entries should be verified against the current SmPC before clinical use.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — multi-targeted protein kinase inhibitor (FLT3, KIT, PDGFR, PKC isoforms, VEGFR-2) |
| Myelosuppression Risk | High when used in AML induction regimens (febrile neutropenia, anaemia, thrombocytopenia are well-characterised in combination with cytarabine/daunorubicin) |
| Emetogenicity Classification | Low to moderate |
| Monitoring Items | Full blood count with differential, liver function tests (ALT/AST/bilirubin), renal function, QTc interval, pulmonary function (interstitial lung disease risk) |
| Handling Protection | Must follow cytotoxic drug handling regulations per local pharmacy guidelines |

---

## Safety Considerations

The Evidence Pack did not contain safety warnings, contraindications, or drug interaction data for midostaurin. Please refer to the approved Summary of Product Characteristics (SmPC) for all safety information before any clinical or research use.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Evidence Pack is critically incomplete — no TxGNN repurposing predictions were generated, and the two data gaps classified as Blocking/High severity (prescribing information and MOA) directly prevent both the prediction pipeline from functioning and the safety screening from proceeding. Generating a repurposing recommendation under these conditions would not be clinically responsible.

**To proceed, the following is needed:**

1. **Investigate empty prediction output** — Determine whether the pipeline failed silently (e.g., DrugBank ID DB06595 not matched to a KG node, or all scores below the reporting threshold). Review `run_kg_prediction.py` logs for midostaurin.
2. **Retrieve MOA data (DG002)** — Query the DrugBank API for DB06595 pharmacology, mechanism of action, and drug categories. The query log confirms a successful DrugBank hit exists; the MOA field must be extracted and populated.
3. **Retrieve national prescribing information (DG001)** — Download and parse the Rydapt® SmPC from either the EMA EPAR database (EU/1/17/1213) or the Laegemiddelstyrelsen product portal to populate warnings, contraindications, and approved indication text.
4. **Re-align disease vocabulary** — Once the approved indication text is available, re-run disease mapping to ensure AML and mastocytosis nodes are correctly linked in the knowledge graph.
5. **Re-generate Evidence Pack** — After resolving all data gaps, re-execute the full evidence collection pipeline and regenerate this report. A complete evaluation with TxGNN predictions, clinical trial evidence, and safety screening should then be possible.

---

*This report is intended for research purposes only and does not constitute medical advice. All repurposing candidates require clinical validation before any therapeutic application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

