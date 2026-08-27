---
layout: default
title: Pegvaliase
parent: 僅模型預測 (L5)
nav_order: 339
evidence_level: L5
indication_count: 10
---

# Pegvaliase
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

# Pegvaliase: From Phenylketonuria (PKU) to Diabetic Retinopathy

## One-Sentence Summary

Pegvaliase is a PEGylated phenylalanine ammonia-lyase enzyme substitution therapy, used to lower blood phenylalanine levels in patients with phenylketonuria (PKU).
The TxGNN model predicts it may be effective for **Diabetic Retinopathy**, with a very high prediction score (**99.17%**) but **0 clinical trials** and **0 publications** currently supporting this direction — and the model's own mechanistic assessment argues against a real pharmacological link.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Phenylketonuria (PKU) — enzyme substitution therapy (per DrugBank; no Danish licence/SmPC on file to confirm wording) |
| Predicted New Indication | Diabetic Retinopathy |
| TxGNN Prediction Score | 99.17% |
| Evidence Level | L5 (model prediction only — no clinical trials or literature identified) |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for Pegvaliase is not available at the drug level (flagged as a data gap in the Evidence Pack). Based on the available information, Pegvaliase is a PEGylated phenylalanine ammonia-lyase that breaks down blood phenylalanine; its efficacy in PKU is well established, but this mechanism has no known biological overlap with the pathophysiology of diabetic retinopathy (retinal microvascular damage, VEGF-driven neovascularisation, polyol/sorbitol pathway activation).

The Evidence Pack's own mechanistic review is explicit about this gap: it states that phenylalanine metabolism has "no known association" with retinal microvascular disease, and that the same conclusion holds for the related cataract predictions surfaced elsewhere in this candidate set (diabetic cataract, nuclear senile cataract, cortical cataract), none of which involve phenylalanine or PAL enzyme activity in their known pathophysiology.

Because of this, the Evidence Pack's assessment is that the very high TxGNN score (99.17%) most likely reflects **structural similarity between metabolic-disease nodes in the underlying knowledge graph**, rather than a genuine pharmacological connection. In other words, this prediction should be treated as hypothesis-generating only, not as a mechanistically grounded signal.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Denmark Market Information

Pegvaliase currently has no marketing authorisation on file in Denmark (0 licences; market status: **Not marketed**). No national (Laegemiddelstyrelsen) or centralised (EMA) authorisation data is available to summarise here.

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no clinical trial or literature evidence for Pegvaliase in diabetic retinopathy, and the Evidence Pack's own mechanistic analysis concludes the prediction likely reflects a knowledge-graph artefact rather than a real pharmacological link. The drug is also not currently marketed in Denmark, so there is no regulatory or clinical use context to build on locally.

**To proceed, the following is needed:**
- Confirmed mechanism of action (MOA) data for Pegvaliase and an independent assessment of any plausible pathway to diabetic retinopathy or cataract
- Danish/EU regulatory dossier or SmPC (key warnings, contraindications, drug interactions) — none currently on file
- Preclinical or in vitro evidence testing Pegvaliase in models relevant to retinal microvascular disease or lens pathology, before any clinical hypothesis is considered
- Re-evaluation once actual clinical trial or literature signals emerge, rather than acting on the TxGNN score alone
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

