---
layout: default
title: Obiltoxaximab
parent: 僅模型預測 (L5)
nav_order: 315
evidence_level: L5
indication_count: 10
---

# Obiltoxaximab
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

# Obiltoxaximab: From Inhalational Anthrax to Postinfectious Vasculitis

## One-Sentence Summary

> Obiltoxaximab (Anthim) is a monoclonal antibody originally developed to treat and prevent inhalational anthrax caused by *Bacillus anthracis* toxin exposure — this is evident from its own clinical trial history, as Denmark holds no marketing authorisation or approved indication text for this drug.
> The TxGNN model predicts it may be effective for **Postinfectious Vasculitis**, but currently **no clinical trials or publications** support this specific direction.
> This is a **model-prediction-only** signal (Evidence Level L5) with an explicitly weak mechanistic rationale — it should not be interpreted as a validated repurposing opportunity.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Inhalational anthrax (treatment/post-exposure prophylaxis) — based on the drug's own trial history; no Danish regulatory text exists |
| Predicted New Indication | Postinfectious vasculitis |
| TxGNN Prediction Score | 99.74% |
| Evidence Level | L5 (model prediction only, no supporting trials or literature) |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for Obiltoxaximab in this evidence pack. Based on known information, Obiltoxaximab is a monoclonal antibody that specifically binds and neutralises the Protective Antigen (PA) subunit of *Bacillus anthracis* toxin, blocking toxin entry into host cells. It is not a broad-spectrum antimicrobial or anti-inflammatory agent.

The evidence pack's own repurposing rationale for this prediction is explicit and should be taken at face value: there is **no known mechanistic link** between anthrax toxin neutralisation and the immune-complex/vascular inflammatory pathology underlying postinfectious vasculitis. The TxGNN score of 99.74% most likely reflects knowledge-graph embedding similarity (e.g., shared "post-infection" node proximity) rather than a biologically grounded hypothesis.

Given the absence of MOA confirmation, supporting trials, or literature, this prediction currently lacks the biological plausibility argument that would normally support further evaluation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

*(Note: four Phase 1/Phase 4 trials of obiltoxaximab exist in the evidence pack — NCT03088111, NCT01932242, NCT01929226, NCT00138411 — but these were conducted for anthrax toxin exposure/safety-PK purposes and are associated with the separate, low-relevance "post-bacterial disorder" prediction, not with postinfectious vasculitis. All were graded relevance "C" — keyword-matched, not disease-specific.)*

## Literature Evidence

Currently no related literature available.

## Denmark Market Information

Obiltoxaximab currently holds **no marketing authorisation in Denmark** (0 registered licenses, market status: Not marketed).

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

*(Key warnings, contraindications, and drug-drug interaction data are currently unavailable for this drug — this is flagged as a blocking data gap (DG001) in the evidence pack and must be resolved before any safety evaluation.)*

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests solely on a TxGNN similarity score with no supporting clinical trials, no literature, no confirmed mechanism of action, and an explicitly acknowledged lack of biological plausibility. The drug is also not marketed in Denmark, so no local regulatory or safety infrastructure currently exists to support evaluation.

**To proceed, the following is needed:**
- Confirmed mechanism-of-action data (currently a data gap)
- SmPC-based safety information: warnings, contraindications, and drug interactions (currently a blocking data gap, DG001)
- Preclinical or mechanistic studies establishing biological plausibility for postinfectious vasculitis
- Any future clinical trial or case-report evidence specific to this indication, should it emerge
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

