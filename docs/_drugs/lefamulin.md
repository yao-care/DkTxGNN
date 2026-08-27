---
layout: default
title: Lefamulin
parent: 僅模型預測 (L5)
nav_order: 259
evidence_level: L5
indication_count: 10
---

# Lefamulin
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

# Lefamulin: From Bacterial Infection to Diffuse Cutaneous Leishmaniasis

## One-Sentence Summary

Lefamulin is a pleuromutilin-class antibiotic; the evidence pack does not document its specific original approved indication, and detailed mechanism-of-action data is also unavailable.
The TxGNN model predicts it may be effective for **diffuse cutaneous leishmaniasis**, but this is currently a **pure model prediction with zero supporting clinical trials or publications**, and the underlying evidence pack itself notes no known mechanistic link between the drug and this parasitic disease.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in evidence pack (only DrugBank input received; original indication field empty) |
| Predicted New Indication | Diffuse Cutaneous Leishmaniasis |
| TxGNN Prediction Score | 99.24% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Denmark Market Status | Not Marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for the original indication. Based on what is known, Lefamulin is a **pleuromutilin-class antibiotic** that inhibits bacterial ribosomal 50S subunit protein synthesis — this is a well-established antibacterial mechanism, not related to antiparasitic activity.

The evidence pack's own mechanistic assessment for this candidate is explicit: there is **no known direct mechanistic relationship** between Lefamulin's ribosomal-inhibition activity and the parasitology of *Leishmania* infection. The prediction reflects a knowledge-graph link identified by TxGNN, rather than a biologically grounded hypothesis.

Given the combination of a high TxGNN score with an explicitly stated absence of mechanistic plausibility, zero clinical trials, and zero literature, this candidate should be interpreted as a low-confidence, exploratory signal only — not as a scientifically supported repurposing hypothesis at this time.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Denmark Market Information

Lefamulin is currently **not marketed** in Denmark, and no marketing authorisations (national or centralised/EMA) are on file in this evidence pack.

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information. No drug interaction data was found for Lefamulin in the queried database (query status: not found).

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a TxGNN model score, with no clinical trials, no literature, and the evidence pack's own rationale confirms no known mechanistic link to the predicted indication. The drug is also not currently marketed in Denmark. This does not meet the threshold to advance past initial screening.

**To proceed, the following is needed:**
- Product label (SmPC) warnings and contraindications — currently missing, and blocking entry into the initial safety assessment stage (S1)
- Verified mechanism of action (MOA) data, to properly assess mechanistic relevance to any new indication
- Independent pharmacological or preclinical rationale connecting Lefamulin to antiparasitic activity, before further evidence collection is warranted
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

