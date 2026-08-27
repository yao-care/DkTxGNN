---
layout: default
title: Vildagliptin
parent: 僅模型預測 (L5)
nav_order: 471
evidence_level: L5
indication_count: 10
---

# Vildagliptin
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

# Vildagliptin: From Type 2 Diabetes Mellitus to Classic Stiff Person Syndrome

## One-Sentence Summary

Vildagliptin is a dipeptidyl peptidase-4 (DPP-4) inhibitor, a drug class internationally used for glycaemic control in type 2 diabetes mellitus. The TxGNN model predicts it may be effective for **Classic Stiff Person Syndrome**, but this direction is currently supported only by the model's similarity score — **no clinical trials and no literature** have been identified. The proposed mechanistic link is also considered weak by the model's own rationale text.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 diabetes mellitus (glycaemic control) — general knowledge of the DPP-4 inhibitor class; not present in the supplied regulatory dataset |
| Predicted New Indication | Classic Stiff Person Syndrome |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L5 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack (flagged as a High-severity data gap). Based on general pharmacological knowledge, vildagliptin belongs to the DPP-4 inhibitor class, which raises endogenous incretin (GLP-1/GIP) concentrations to improve glycaemic control; its efficacy in type 2 diabetes has been established in that context.

Classic Stiff Person Syndrome, by contrast, is an autoimmune neurological disorder in which anti-GAD65 antibodies impair GABAergic neurotransmission, producing muscle rigidity and spasm. There is no established overlap between the incretin/glucose-metabolism pathway and GABAergic neurotransmission or anti-GAD65-mediated autoimmunity.

While DPP-4 (CD26) does have a recognised role in T-cell immune regulation, there is currently no evidence that DPP-4 inhibition modulates anti-GAD65 autoimmune activity or restores GABAergic signalling deficits. The model's own repurposing rationale characterizes this as a likely indirect association arising from shared knowledge-graph nodes (e.g. "diabetic neuropathy") rather than a genuine mechanistic link, and explicitly describes the mechanistic evidence as weak.

It is also worth noting that TxGNN's top 10 candidates for this drug contain only five distinct diseases, each duplicated (classic stiff person syndrome, focal stiff limb syndrome, thiamine-responsive dysfunction syndrome, opsismodysplasia, and drug-induced localized lipodystrophy), all at similarly high but essentially undifferentiated scores (~99.8–99.9%) and all rated L5/Hold. This pattern is consistent with a model-level signal rather than a curated, disease-specific hypothesis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Denmark Market Information

Vildagliptin currently holds **no marketing authorisation in Denmark** — the supplied dataset lists 0 licenses and a market status of "Not marketed." No national (Lægemiddelstyrelsen) or centralised (EMA) authorisation records were available for this product in the evidence pack.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

*Note: The evidence pack flags retrieval of the product's warnings/contraindications label text as a Blocking data gap (DG001), meaning this candidate cannot yet proceed to a formal safety (S1) assessment.*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- Evidence level is L5 — the association rests solely on the TxGNN similarity score, with zero supporting clinical trials or literature identified across all 10 predicted disease candidates for this drug.
- The proposed mechanistic link between DPP-4/incretin pharmacology and anti-GAD65-mediated autoimmune GABAergic dysfunction is explicitly assessed as weak, likely reflecting an indirect knowledge-graph association rather than a plausible biological hypothesis.
- A Blocking data gap (missing SmPC warnings/contraindications) prevents this candidate from entering even the initial safety screening stage (S1).
- The drug is not currently marketed in Denmark, so there is no existing local safety or utilisation experience to draw on.

**To proceed, the following is needed:**
- Danish/EU product label (SmPC) with full warnings, contraindications, and drug interaction data — required to clear the Blocking data gap before any safety review
- Confirmed mechanism of action (DrugBank or primary literature) to properly evaluate mechanistic plausibility
- Independent literature or preclinical evidence connecting DPP-4 inhibition to GAD65-mediated autoimmune neurological disease, if this hypothesis is to be pursued further
- Clarification of why TxGNN returned duplicate/near-identical top candidates, to rule out a model or pipeline artifact before committing further evaluation resources to this candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

