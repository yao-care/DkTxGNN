---
layout: default
title: Cisplatin
parent: 僅模型預測 (L5)
nav_order: 113
evidence_level: L5
indication_count: 0
---

# Cisplatin
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

# Cisplatin: Drug Repurposing Evaluation — No TxGNN Predictions Available

## One-Sentence Summary

Cisplatin (DB00515) is a well-established platinum-based cytotoxic chemotherapy agent, recognised as a cornerstone treatment for numerous solid tumours worldwide.
The TxGNN model did not generate any repurposing predictions for this candidate in the current evidence pack (v4, data cutoff 2026-04-05), as critical input data — including mechanism of action and regulatory indication records — were not successfully retrieved.
This report summarises the current data status and identifies the remediation steps required before a formal repurposing evaluation can proceed.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not retrieved — regulatory indication records are absent from the current evidence pack |
| Predicted New Indication | Not available — TxGNN model returned no predictions |
| TxGNN Prediction Score | Not available |
| Evidence Level | Not determinable |
| Denmark Market Status | Not marketed (0 authorisations found in current dataset) |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | **Hold** |

---

## Why No Prediction Is Available

The TxGNN prediction pipeline requires two foundational inputs to function: a mapped DrugBank identifier and at least one regulatory indication record. For this candidate, the DrugBank query returned a successful match (DB00515), but all downstream inputs failed:

- **Mechanism of action (MOA):** Not retrieved from DrugBank. This is a high-severity gap and directly prevents the mechanistic relevance analysis that underpins the model's candidate scoring.
- **Approved indication records:** Zero entries were found in the Denmark regulatory dataset. Cisplatin is a globally established platinum-based chemotherapy; the absence of any authorisation record almost certainly reflects a data retrieval failure rather than a genuine absence from the Danish market. The EMA-centralised authorisation for cisplatin-containing products should be verifiable through the Laegemiddelstyrelsen product database.
- **Safety warnings and contraindications:** Not retrieved from the regulatory source, preventing the S1 safety pre-screening step.

Until these three gaps are resolved, no mechanistic rationale or evidence evaluation can be formally assessed.

---

## Cytotoxicity

Based on DrugBank classification (DB00515) and established pharmacological class, Cisplatin is unambiguously an antineoplastic cytotoxic agent belonging to the platinum coordination compounds.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — Platinum coordination compound |
| Myelosuppression Risk | High — leucopenia, thrombocytopenia, and anaemia are well-documented dose-limiting toxicities |
| Emetogenicity Classification | High — cisplatin is classified as highly emetogenic; prophylactic antiemetic therapy (5-HT₃ antagonist + NK₁ antagonist + dexamethasone) is mandatory |
| Monitoring Items | Full blood count (with differential), serum creatinine and eGFR (nephrotoxicity is a primary dose-limiting toxicity), serum electrolytes (Mg²⁺, K⁺, Na⁺, Ca²⁺), audiometry (ototoxicity monitoring), urinalysis |
| Handling Protection | Must be handled in accordance with cytotoxic drug handling regulations; requires appropriate personal protective equipment, dedicated preparation area (laminar flow cabinet), and cytotoxic waste disposal procedures |

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model could not generate repurposing predictions for Cisplatin because the two blocking data gaps — missing mechanism of action data and the absence of any regulatory indication record — prevented the pipeline from producing a scoreable candidate. No evidence table or mechanistic assessment can be completed in the current state.

**To proceed, the following is needed:**

- **[Blocking]** Retrieve approved indication, warning, and contraindication data by downloading and parsing the SmPC PDF from the Danish Medicines Agency (Laegemiddelstyrelsen) — required for S1 safety pre-screening
- **[High]** Query the DrugBank API directly for DB00515 to obtain the mechanism of action — required for mechanistic relevance analysis
- **[High]** Verify Denmark market status: Cisplatin has long been available as a standard chemotherapy across the EU; the zero-authorisation result should be investigated as a likely data retrieval issue before any regulatory conclusion is drawn
- **[Follow-up]** Re-run the full TxGNN prediction pipeline once complete input data is available, and re-issue this evidence pack
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

