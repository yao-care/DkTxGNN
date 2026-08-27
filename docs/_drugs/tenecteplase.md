---
layout: default
title: Tenecteplase
parent: 僅模型預測 (L5)
nav_order: 424
evidence_level: L5
indication_count: 10
---

# Tenecteplase
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Tenecteplase: From Undocumented Original Indication to Posterolateral Myocardial Infarction

## One-Sentence Summary

Tenecteplase (DB00031) is a recombinant tissue plasminogen activator (TNK-tPA); its originally approved indication is not documented in this evidence pack, and it currently holds **no marketing authorisation in Denmark**. The TxGNN model's top-ranked prediction is **posterolateral myocardial infarction**, with a **99.87%** prediction score, but this specific candidate is supported by **zero clinical trials and zero literature** in the evidence pack — it rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented — `taiwan_regulatory.licenses` is empty (no Danish MA on file) and `original_indications` was not populated in this pack |
| Predicted New Indication | Posterolateral Myocardial Infarction |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L5 (model prediction only, no supporting trials or literature) |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a High-severity data gap, DG002). Based on the drug's known pharmacological class, tenecteplase is a genetically engineered variant of tissue plasminogen activator (TNK-tPA) that catalyzes the conversion of plasminogen to plasmin, dissolving fibrin clots.

Posterolateral myocardial infarction is an anatomical-location subtype of myocardial infarction, a condition for which thrombolytic agents in this class are mechanistically relevant. The evidence pack's own rationale for this candidate states: this subtype "is theoretically consistent with tenecteplase's standard thrombolytic mechanism, but no trial or literature in this dataset directly supports it — only the TxGNN score exists — and it substantially overlaps with myocardial infarction as a general condition, raising the possibility that this is an ontology-level duplicate rather than a genuinely novel indication."

In other words, the mechanistic plausibility is high, but that plausibility likely reflects tenecteplase's already-established relevance to myocardial infarction generally, rather than new evidence specific to the posterolateral subtype. This is why the evidence pack itself scores this candidate L5 and recommends **Hold**.

*Note for context: within the same evidence pack, a different candidate — **coronary stenosis** (rank 9/10) — has materially stronger support, including a completed Phase 2 RCT (NCT00604695, low-dose intracoronary tenecteplase during primary PCI) and 12 literature hits, reaching evidence level L2 with a "Proceed with Guardrails" recommendation. That candidate may warrant separate evaluation.*

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Denmark Market Information

Tenecteplase currently holds no marketing authorisation in Denmark — `total_licenses` is 0 and no license records are on file in this evidence pack.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information. (Key warnings, contraindications, and drug-interaction data are all marked as data gaps in this evidence pack; the DDI query itself returned "not found.")

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate has no direct clinical-trial or literature support in the evidence pack — only a TxGNN model score — and the predicted indication is anatomically nested within myocardial infarction, a condition already closely tied to tenecteplase's known thrombolytic mechanism. This raises meaningful risk that the "new indication" is an ontology artifact rather than a genuine repurposing opportunity, so it does not meet the bar to proceed.

**To proceed, the following is needed:**
- Original indication and mechanism-of-action data (DG002 remediation, via DrugBank API), to establish whether this candidate is truly distinct from tenecteplase's existing use
- TFDA/SmPC label, warnings, and contraindications (DG001 remediation, currently Blocking) before any S1 safety review can begin
- Targeted literature/trial search specific to "posterolateral myocardial infarction" (as opposed to myocardial infarction generally) to determine if this subtype has been studied independently
- If pursuing repurposing work on this drug, consider prioritizing the **coronary stenosis** candidate instead, which already has L2-level evidence including a completed Phase 2 RCT
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

