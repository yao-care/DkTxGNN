---
layout: default
title: Zanamivir
parent: 僅模型預測 (L5)
nav_order: 476
evidence_level: L5
indication_count: 10
---

# Zanamivir
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

Using the report as directly specified by the prompt (this is a self-contained content-generation task with explicit formatting instructions already provided, so I'm following those instructions directly rather than invoking a separate skill).

I reviewed the evidence pack in detail: notably, all `predicted_indications` entries here carry **negative** mechanistic assessments (`decision_stage: S0`, `recommendation: Hold`, `evidence_level: L5`), and the only literature hits (for "disorder of tyrosine metabolism") are flagged in the pack itself as a knowledge-graph false positive (papers about oseltamivir/zanamivir resistance mutations, not about metabolic disease). I've written the report to reflect this honestly rather than forcing a positive narrative.

---

# Zanamivir: From Influenza to Pyelonephritis

## One-Sentence Summary

Zanamivir is an antiviral neuraminidase inhibitor internationally approved for the treatment and prevention of influenza A and B.
The TxGNN model's top-ranked prediction proposes possible relevance to **Pyelonephritis**, but this is a **model-only (L5)** signal —
there are **no supporting clinical trials and no supporting literature**, and the evidence pack's own mechanistic review finds no credible pharmacological basis for the link.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in Danish licence data (no marketing authorisations on file); Zanamivir is internationally indicated for Influenza A/B treatment and prophylaxis |
| Predicted New Indication | Pyelonephritis |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L5 |
| Denmark Market Status | Not Marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Formal mechanism-of-action data was not available in this evidence pack (drug-level data gap, marked High severity in the source metadata). Based on established pharmacology, Zanamivir is an inhaled neuraminidase inhibitor that blocks the influenza virus surface glycoprotein neuraminidase, preventing release of new viral particles from infected respiratory epithelial cells. Its approved use is narrowly confined to influenza A and B.

The model's top-ranked new indication, **Pyelonephritis**, is a bacterial upper urinary tract infection. There is no overlap between bacterial infection pathophysiology and viral neuraminidase inhibition, and no antibacterial activity has been documented for zanamivir. The evidence pack's own mechanistic-link assessment for this candidate concludes explicitly that there is no credible pharmacological connection.

The remaining model-flagged candidates — disorders of tyrosine and phenylalanine metabolism, tetrahydrobiopterin-responsive phenylketonuria, and teratogenic Pierre Robin syndrome — are all congenital metabolic or craniofacial developmental disorders, none of which have any known biochemical relationship to neuraminidase inhibition. Notably, the three literature citations retrieved under "disorder of tyrosine metabolism" all concern oseltamivir/zanamivir antiviral-**resistance mutations** (e.g., the H275Y / H274Y neuraminidase substitutions) — the mutation nomenclature happens to reference a tyrosine/histidine substitution, which appears to have triggered a spurious text-matching link in the knowledge graph rather than reflecting genuine therapeutic relevance. This is best interpreted as a **knowledge-graph false positive** rather than supporting evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for the top-ranked candidate indication (Pyelonephritis).

*(Note: 3 publications were retrieved under a lower-ranked candidate, "disorder of tyrosine metabolism," but on review these concern antiviral resistance mutation nomenclature, not the metabolic disorder itself — see rationale above.)*

---

## Denmark Market Information

No marketing authorisations are currently on file for Zanamivir in Denmark (Market Status: **Not Marketed**; Total Licences: **0**). This drug does not currently have a registered presence in the Danish market.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All predicted indications for Zanamivir in this evidence pack are supported only at the model-prediction level (L5), with no clinical trials and no genuinely relevant literature. The top candidate (Pyelonephritis) and all other candidates lack any credible mechanistic rationale connecting an antiviral neuraminidase inhibitor to their respective disease biology, and one literature signal was identified as a knowledge-graph false positive.

**To proceed, the following is needed:**
- Confirmed mechanism-of-action data for Zanamivir (DrugBank API query — currently a data gap)
- SmPC/product label warnings and contraindications (Danish Medicines Agency source — currently a blocking data gap for safety screening)
- Independent (non-TxGNN-triggered) hypothesis generation or targeted literature/trial search specific to Pyelonephritis before any further evaluation
- Reassessment of whether these candidates should remain in the active pipeline, given the absence of a plausible mechanistic basis
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

