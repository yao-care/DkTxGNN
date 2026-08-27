---
layout: default
title: Nemolizumab
parent: 僅模型預測 (L5)
nav_order: 307
evidence_level: L5
indication_count: 10
---

# Nemolizumab
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

# Nemolizumab: From Atopic Dermatitis/Prurigo Nodularis to Diabetic Cataract

## One-Sentence Summary

Nemolizumab is an anti-IL-31 receptor A (IL-31RA) monoclonal antibody, described in the evidence pack's mechanistic notes as approved for pruritus and inflammation in atopic dermatitis and prurigo nodularis (a formal, registry-sourced original indication is not on file). The TxGNN model predicts it may be effective for **Diabetic Cataract**, but this prediction is currently supported by **0 clinical trials** and **0 publications**, and the evidence pack's own mechanistic analysis states there is no known biological link between IL-31 signaling and diabetic lens pathology.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Atopic dermatitis / Prurigo nodularis (stated in the repurposing rationale text; not confirmed via a formal Danish registry entry — see note below) |
| Predicted New Indication | Diabetic Cataract |
| TxGNN Prediction Score | 98.55% |
| Evidence Level | L5 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

*Note: `taiwan_regulatory.licenses` is empty and `drug.original_indications` is unpopulated, so the original indication above is taken from the drug's mechanistic description rather than a Danish Medicines Agency registry entry.*

## Why is This Prediction Reasonable?

Nemolizumab blocks IL-31 signaling through IL-31RA, a pathway central to pruritus (itch) and inflammation in atopic dermatitis and prurigo nodularis. This is a neuroimmune/inflammatory mechanism, not a metabolic or ocular one.

Diabetic cataract, by contrast, is driven by lens-specific metabolic pathology — osmotic damage from the polyol (sorbitol) pathway, oxidative stress, and accumulation of advanced glycation end-products (AGEs). The evidence pack's own repurposing rationale is explicit that no published or mechanistic connection exists between IL-31/IL-31RA blockade and these lens-damage processes.

Given this, the prediction appears to be an artifact of TxGNN's knowledge-graph embedding similarity rather than a biologically grounded hypothesis. The high prediction score (98.55%) reflects graph-level pattern similarity, not pharmacological plausibility, and the same score is shared across multiple unrelated cataract subtypes (diabetic, tetanic, craniostenosis-associated, immature, mature), which further suggests the model is clustering on the general "cataract" disease node rather than a diabetes-specific mechanism.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Denmark Market Information

Nemolizumab currently has **no marketing authorisation** in Denmark (market status: Not marketed; 0 licenses on file), so no national or centralised (EMA) authorisation details are available to report.

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information. Danish label warnings, contraindications, and drug-interaction data are not yet available in this evidence pack (flagged as a **Blocking** data gap — see Next Steps).

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high, but there is zero clinical trial or literature support, and the evidence pack's own mechanistic analysis explicitly finds no biological link between the drug's approved mechanism (IL-31RA blockade) and diabetic cataract pathology. Combined with the absence of Danish market authorisation and missing SmPC safety data, this candidate does not meet the bar for further evaluation at this time.

**To proceed, the following is needed:**
- SmPC warnings/contraindications data (currently a Blocking gap — required before any S1 safety screening)
- Confirmed, registry-sourced original indication and MOA (currently marked as a data gap)
- Independent preclinical or mechanistic evidence linking IL-31/IL-31RA signaling to lens/cataract pathology, before this candidate is considered for further evidence collection
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

