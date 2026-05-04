---
layout: default
title: Escitalopram
parent: 僅模型預測 (L5)
nav_order: 175
evidence_level: L5
indication_count: 0
---

# Escitalopram
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

# Escitalopram: Drug Repurposing Evaluation — Insufficient Data for Prediction

## One-Sentence Summary

Escitalopram is a well-established selective serotonin reuptake inhibitor (SSRI) widely used internationally for major depressive disorder and generalised anxiety disorder. The TxGNN model has **not generated any repurposing predictions** for this compound, and the evidence pack contains **no clinical trial or literature evidence** for novel indications. This report documents the current data gaps that must be resolved before a repurposing evaluation can proceed.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in this evidence pack (see note below) |
| Predicted New Indication | **None** — no TxGNN predictions available |
| TxGNN Prediction Score | N/A |
| Evidence Level | **L5** (No predictions or supporting studies) |
| Denmark Market Status | Not marketed (未上市) |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | **Hold** |

> **Note on Original Indication:** Although the evidence pack does not list original indications, escitalopram is internationally recognised as an SSRI approved for major depressive disorder (MDD) and generalised anxiety disorder (GAD). In the EU, escitalopram is authorised under multiple national marketing authorisations (e.g., Cipralex®) for depression, panic disorder, social anxiety disorder, generalised anxiety disorder, and obsessive-compulsive disorder.

---

## Why is This Prediction Reasonable?

No TxGNN repurposing prediction has been generated for escitalopram. Therefore, a mechanistic rationale for a new indication cannot be assessed at this time.

Currently, detailed mechanism of action data is not available in this evidence pack. Based on publicly known information, escitalopram is the S-enantiomer of citalopram and functions as a highly selective serotonin reuptake inhibitor (SSRI). It blocks the serotonin transporter (SERT), increasing serotonergic neurotransmission. This mechanism underlies its established efficacy in depressive and anxiety disorders.

The absence of TxGNN predictions may indicate that escitalopram's DrugBank ID (DB01175) was not successfully mapped into the knowledge graph, or that the model did not identify any novel disease associations scoring above the relevance threshold. Further investigation into the mapping pipeline is recommended.

---

## Clinical Trial Evidence

Currently no predicted indications exist, therefore no related clinical trials have been identified for a repurposing context.

---

## Literature Evidence

Currently no predicted indications exist, therefore no related literature has been identified for a repurposing context.

---

## Denmark Market Information

No marketing authorisations for escitalopram were found in the current dataset.

> **Note:** This likely reflects a data gap rather than true absence. Escitalopram is widely available across the EU. Cipralex® (escitalopram oxalate) is authorised via national procedures in Denmark through the Laegemiddelstyrelsen, and generic formulations are also available. The evidence pack's regulatory data module may need to be updated with Danish or EMA marketing authorisation records.

---

## Safety Considerations

> Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.
>
> For Danish prescribers, the SmPC for Cipralex® (escitalopram) is available via the Laegemiddelstyrelsen's product database or the EMA website. Key safety considerations for escitalopram generally include:
> - QT prolongation risk (dose-dependent)
> - Serotonin syndrome risk when combined with other serotonergic agents
> - Suicidality risk in young adults (black box warning in some jurisdictions)
> - Withdrawal symptoms on abrupt discontinuation

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence pack contains no TxGNN predictions, no regulatory data for Denmark, and no safety information. Without a predicted new indication, there is no basis to evaluate a repurposing opportunity. This candidate cannot advance until fundamental data gaps are resolved.

**To proceed, the following is needed:**

1. **Resolve DrugBank/KG mapping issue** — Verify that DB01175 (escitalopram) is correctly mapped into the TxGNN knowledge graph and that predictions can be generated
2. **Populate Denmark regulatory data** — Import marketing authorisation records from the Laegemiddelstyrelsen and/or EMA centralised procedure database (escitalopram is widely authorised in Denmark)
3. **Obtain mechanism of action (MOA) data** — Query DrugBank API for complete pharmacological profile (DG002)
4. **Obtain SmPC safety data** — Extract warnings, contraindications, and drug interactions from the Danish-approved SmPC (DG001)
5. **Re-run the TxGNN prediction pipeline** once the above data gaps are filled, and regenerate the evidence pack

---

*This report is for research purposes only and does not constitute medical advice. Any drug repurposing candidates require clinical validation before application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

