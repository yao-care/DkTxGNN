---
layout: default
title: Insulin Lispro
parent: 僅模型預測 (L5)
nav_order: 237
evidence_level: L5
indication_count: 10
---

# Insulin Lispro
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

Using the provided report template directly — this is a single, self-contained report-generation task with no additional skill needed beyond the instructions already given.

# Insulin Lispro: From Diabetes Mellitus to Autoimmune Oophoritis

## One-Sentence Summary

Insulin lispro is a rapid-acting insulin analogue used to control blood glucose in diabetes mellitus. The TxGNN model's top prediction links it to **Autoimmune Oophoritis** with a very high similarity score, but **zero clinical trials and zero publications** currently support this link, and the model's own rationale suggests the connection reflects a shared autoimmune comorbidity pattern rather than a genuine drug-repurposing mechanism.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Diabetes Mellitus (insulin replacement therapy) — based on general drug knowledge; not confirmed by Danish licence data, as none is available in this evidence pack |
| Predicted New Indication | Autoimmune Oophoritis |
| TxGNN Prediction Score | 99.78% |
| Evidence Level | L5 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known general pharmacology, insulin lispro is a rapid-acting recombinant human insulin analogue; its efficacy in glycaemic control for diabetes mellitus is well established, but no MOA data in this evidence pack supports extrapolating a direct pharmacological effect on ovarian autoimmune disease.

The TxGNN rationale itself flags this prediction as a **comorbidity association rather than a treatment hypothesis**: autoimmune oophoritis and type 1 diabetes mellitus are both frequent components of Autoimmune Polyglandular Syndrome type 2 (APS-2), and likely share overlapping genetic susceptibility (e.g., HLA haplotypes). This shared-node pattern in the knowledge graph is plausible reason for the high similarity score, but there is no mechanistic evidence that insulin itself exerts a therapeutic effect on ovarian autoimmune inflammation.

It is also worth noting that TxGNN surfaced four other candidate diseases in the top 10 (thiamine-responsive dysfunction syndrome, classic stiff person syndrome, focal stiff limb syndrome, and opsismodysplasia) with very similar scores. Each carries the same underlying caveat in its rationale — the association arises from shared autoimmune, metabolic, or gene-pathway nodes (e.g., GAD65 autoimmunity, SLC19A2/insulin co-morbidity, or INPPL1–insulin-signalling pathway overlap) rather than a demonstrated treatment effect. This pattern suggests the current TxGNN output for insulin lispro should be read as a hypothesis-generation signal, not a repurposing candidate ready for evaluation.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Denmark Market Information

No marketing authorisation for insulin lispro is currently recorded in this evidence pack for the Danish market (Market status: Not marketed; 0 licences on file). This may reflect a genuine absence of local Laegemiddelstyrelsen/EMA registration, or it may reflect a data-collection gap — this should be verified directly against the Laegemiddelstyrelsen product register before any downstream decision.

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

*(Note: this evidence pack flags the absence of SmPC-derived warnings/contraindications as a **Blocking** data gap — see Conclusion below.)*

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests entirely on TxGNN's model score (L5 — no clinical trials, no literature, no observational data), and the accompanying mechanistic rationale explicitly characterizes the drug–disease link as a comorbidity/shared-node artifact rather than a plausible pharmacological repurposing hypothesis. There is currently no basis to advance this candidate beyond hypothesis-generation.

**To proceed, the following is needed:**
- SmPC warnings and contraindications for insulin lispro (currently a **Blocking** data gap — required before any safety pre-screening, per DG001)
- Verified mechanism of action data from DrugBank or another authoritative source (currently a **High**-severity data gap, per DG002)
- Confirmation of Danish/EU marketing authorisation status directly from Laegemiddelstyrelsen or the EMA register
- Independent mechanistic or preclinical evidence connecting insulin signalling to ovarian autoimmune pathology, beyond the comorbidity association identified by the knowledge graph
- If pursued further, expert endocrinology/reproductive-immunology input to assess biological plausibility before any trial-stage investment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

