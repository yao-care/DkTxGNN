---
layout: default
title: Urofollitropin
parent: 僅模型預測 (L5)
nav_order: 461
evidence_level: L5
indication_count: 10
---

# Urofollitropin
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

# Urofollitropin: From Fertility Treatment to Migraine Disorder

## One-Sentence Summary

Urofollitropin is a purified follicle-stimulating hormone (FSH) preparation used for ovulation induction and assisted reproductive technology (ART). The TxGNN model predicts it may be effective for **Migraine Disorder**, but this prediction is currently supported by **no clinical trials and no published literature**, and the drug is not marketed in Denmark.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Ovulation induction / assisted reproductive technology (based on known drug class; not documented in Danish licenses, as the drug is not marketed in Denmark) |
| Predicted New Indication | Migraine Disorder |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L5 (model prediction only, no clinical trials or literature identified) |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available for Urofollitropin (data gap). Based on known pharmacology, Urofollitropin is a purified FSH preparation used to stimulate follicular development for ovulation induction and ART; its efficacy in fertility treatment is well established, but no known mechanistic pathway connects gonadotropin signalling to the neurovascular/CGRP pathways implicated in migraine.

The evidence pack's own mechanistic assessment is explicitly skeptical of this prediction: it notes there is "no known mechanism linking FSH to migraine's neurovascular/CGRP pathway" and flags this as "highly suspicious of knowledge-graph co-occurrence bias" (e.g., an indirect association between menstrual migraine and gonadotropin activity being amplified by the graph structure rather than reflecting genuine biology).

This concern is reinforced by the broader prediction set: five mechanistically unrelated conditions — migraine disorder, migraine with brainstem aura, cauda equina syndrome, His bundle tachycardia, and restless legs syndrome — all score within a narrow band (99.68%–99.85%), each duplicated across two ranks. None of these conditions share a plausible pharmacological link to FSH, and none returned any supporting clinical trial or literature evidence. This pattern is more consistent with a non-specific scoring artifact than a validated repurposing signal.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Denmark Market Information

Urofollitropin is **not marketed** in Denmark — no marketing authorisations (national or centralised/EMA) are currently on record.

## Safety Considerations

Safety data (key warnings, contraindications, drug-drug interactions) could not be retrieved for this evaluation. This is flagged in the evidence pack as a **Blocking** data gap (DG001: SmPC warnings/contraindications), meaning the candidate cannot proceed past the initial safety screening stage (S1) until label data is obtained. Please refer to the approved Summary of Product Characteristics (SmPC) once available.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate has zero supporting clinical trial or literature evidence (Evidence Level L5), the drug is not marketed in Denmark, and a Blocking data gap prevents safety screening. The evidence pack's own mechanistic review flags the prediction as likely reflecting knowledge-graph co-occurrence bias rather than a genuine biological signal, given that multiple unrelated conditions score in the same narrow range with no differentiating evidence.

**To proceed, the following is needed:**
- SmPC warnings/contraindications (blocking gap — required before any safety screening)
- Detailed mechanism of action data for Urofollitropin (DrugBank/literature)
- A biologically plausible mechanistic hypothesis linking FSH to migraine pathophysiology, ideally supported by preclinical data
- At minimum, exploratory/observational evidence before considering advancement beyond model-prediction stage
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

