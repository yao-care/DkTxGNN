---
layout: default
title: Teplizumab
parent: 僅模型預測 (L5)
nav_order: 425
evidence_level: L5
indication_count: 10
---

# Teplizumab
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

# Teplizumab: From Type 1 Diabetes Progression Delay to Diabetic Cataract

## One-Sentence Summary

Teplizumab is an anti-CD3 monoclonal antibody used to delay progression of Type 1 diabetes through T-cell immune modulation. The TxGNN model predicts a possible link to **Diabetic Cataract**, but currently **no clinical trials and no literature** support this direction, and the model's own rationale flags the connection as biologically weak.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in this evidence pack (no approved label text on file) |
| Predicted New Indication | Diabetic Cataract |
| TxGNN Prediction Score | 98.38% |
| Evidence Level | L5 (model prediction only) |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is marked as a data gap in this evidence pack. Based on the repurposing rationale that accompanies the prediction, Teplizumab is an anti-CD3 monoclonal antibody that modulates T-cell activity to delay the autoimmune destruction underlying Type 1 diabetes.

Diabetic cataract, by contrast, is a structural lens pathology driven by protein denaturation and osmotic imbalance (e.g., sorbitol accumulation, oxidative stress) — not an autoimmune process. The evidence pack's own mechanistic assessment states there is **no known direct biochemical pathway** connecting Teplizumab's immune-modulating action to cataract pathogenesis.

The pack explicitly interprets the high TxGNN score as likely arising from **indirect graph proximity** — both diseases sharing a "diabetes" node in the knowledge graph — rather than a genuine mechanistic hypothesis. This applies to all ten ranked candidates in this evidence pack, which are various cataract subtypes (diabetic, immature, mature, tetanic, craniostenosis-associated) clustered around the same diabetes node. The assessment for tetanic and craniostenosis-associated cataract subtypes is particularly clear on this point, since those are linked to calcium/parathyroid or developmental causes with no plausible connection to T-cell modulation at all.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Denmark Market Information

Teplizumab is currently **not marketed** in Denmark; no marketing authorisations (national or centralised/EMA) are on file in this evidence pack.

## Safety Considerations

No safety data (warnings, contraindications, or drug interactions) is currently available in this evidence pack, and as Teplizumab is not marketed in Denmark, no approved Summary of Product Characteristics (SmPC) exists yet to consult.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests solely on a TxGNN graph-similarity score (L5) with zero supporting clinical trials or literature, and the accompanying mechanistic assessment itself concludes the drug–disease link is likely a knowledge-graph artifact rather than genuine biological plausibility.

**To proceed, the following is needed:**
- Confirmed original indication and approved label text (currently blocking — no source data available)
- Verified mechanism of action data from DrugBank or another authoritative source
- Independent literature or preclinical search specifically for any T-cell/immune involvement in diabetic cataract pathogenesis
- Regulatory label/warning and contraindication data before any safety evaluation can begin
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

