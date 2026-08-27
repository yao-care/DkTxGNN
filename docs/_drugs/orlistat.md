---
layout: default
title: Orlistat
parent: 僅模型預測 (L5)
nav_order: 322
evidence_level: L5
indication_count: 2
---

# Orlistat
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Orlistat: From Weight Management to Hypervitaminosis

## One-Sentence Summary

Orlistat is a gastric/pancreatic lipase inhibitor generally used for weight management in obesity (Denmark-specific approved indication text is not available since the drug is not currently marketed there). The TxGNN model predicts a possible link to **Hypervitaminosis**, but this is currently a **model prediction only, with no supporting clinical trials or literature**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Weight management / obesity (based on general pharmacological knowledge of orlistat; no Danish-specific approved indication text is available) |
| Predicted New Indication | Hypervitaminosis |
| TxGNN Prediction Score | 99.42% |
| Evidence Level | L5 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed, structured mechanism-of-action data for orlistat is currently a data gap (DG002) in this evidence pack. Based on general pharmacological knowledge, orlistat inhibits gastric and pancreatic lipase, blocking hydrolysis of dietary triglycerides and thereby reducing intestinal absorption of dietary fat along with the fat-soluble vitamins A, D, E, and K.

This mechanism is the basis for the TxGNN association with hypervitaminosis: reduced absorption of fat-soluble vitamins could, in theory, lower vitamin overload in patients with hypervitaminosis A or D, which is directionally consistent with the model's high score (0.994).

However, this link requires careful clinical scrutiny before it can be considered a genuine repurposing opportunity. Chronic orlistat use is clinically well known to *cause* fat-soluble vitamin **deficiency** (hypovitaminosis) as an adverse effect, not to treat vitamin excess. The directionality of the proposed benefit therefore conflicts with orlistat's established safety profile, and this discrepancy has not been resolved by any clinical or literature evidence in this evidence pack — it remains a purely mechanistic hypothesis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Denmark Market Information

Orlistat is not currently marketed in Denmark, and no marketing authorisations (national or centralised/EMA) are recorded in this evidence pack.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This prediction is supported only by a mechanistic hypothesis (Evidence Level L5) with no clinical trials or literature, and the proposed direction of effect conflicts with orlistat's known adverse effect of causing fat-soluble vitamin deficiency. The drug is also not currently marketed in Denmark.

**To proceed, the following is needed:**
- TFDA/SmPC-equivalent warnings and contraindications data (currently a Blocking data gap, DG001) to enable an initial safety assessment
- Formal, structured mechanism-of-action data (DG002)
- Clinical or preclinical evidence directly addressing the hypervitaminosis hypothesis, and resolution of the directional conflict with orlistat's known vitamin-deficiency effect
- Confirmation of Denmark market/regulatory pathway status before any further evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

