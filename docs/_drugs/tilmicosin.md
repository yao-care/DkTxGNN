---
layout: default
title: Tilmicosin
parent: 僅模型預測 (L5)
nav_order: 435
evidence_level: L5
indication_count: 10
---

# Tilmicosin
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

# Tilmicosin: From Veterinary Respiratory Infections to Jeune Syndrome with Situs Inversus

## One-Sentence Summary

Tilmicosin is a macrolide antibiotic used exclusively in veterinary medicine (cattle, sheep, pig respiratory infections) and has no approved human indication in Denmark. The TxGNN model predicts a possible link to **Jeune syndrome with situs inversus**, but this prediction is supported by **0 clinical trials** and **0 publications** — it is a pure model-topology signal with no biological plausibility.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not applicable to human medicine — Tilmicosin is a veterinary-only macrolide antibiotic for respiratory infections in cattle, sheep, and pigs; no approved human indication or Danish marketing authorisation exists |
| Predicted New Indication | Jeune syndrome with situs inversus |
| TxGNN Prediction Score | 97.24% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for this candidate (flagged as a blocking data gap). Based on known information, Tilmicosin is a 16-membered macrolide antibiotic approved only for veterinary use, acting by binding the bacterial 50S ribosomal subunit to inhibit protein synthesis — a purely antibacterial mechanism.

Jeune syndrome with situs inversus is a rare genetic skeletal ciliopathy. There is no known mechanistic pathway connecting a bacterial protein-synthesis inhibitor to ciliary/skeletal developmental disease, and the evidence pack explicitly confirms this: the model score reflects only topological similarity in the knowledge graph, with no supporting clinical trial or literature evidence of any kind. The same absence of mechanistic and evidentiary support applies to the other top-ranked predictions in this pack (interventricular septum aneurysm, partial 22q deletion, Pierre Robin syndrome) — none have a plausible pharmacological rationale.

Notably, the only substantial literature signal found anywhere in this evidence pack relates to a lower-ranked candidate, "heart disease" (score 97.19%), where 20 PubMed records were retrieved. However, all of them describe Tilmicosin-**induced cardiotoxicity** (acute cardiotoxicity, left ventricular dysfunction, arrhythmia) in animal models and accidental human exposures — i.e., evidence of harm, not therapeutic benefit. This reinforces that the model's high similarity scores in this case are not indicative of genuine repurposing potential.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

**Additional signal from literature review:** Although not tied to the top-ranked predicted indication, 20 published studies retrieved for a related candidate ("heart disease") consistently describe Tilmicosin-induced cardiotoxicity in animals and accidental human exposure (including a 2025 case report of cardiac effects after accidental ingestion). This is a known class-related cardiac safety signal for macrolide antibiotics and should be treated as a risk flag, not a therapeutic lead.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Tilmicosin has no Danish marketing authorisation and no approved human indication, and every predicted new indication in this evidence pack — including the top-ranked Jeune syndrome/situs inversus prediction — is Evidence Level L5 with no clinical trial or literature support. The only substantial literature found for a related candidate points to cardiotoxicity risk rather than efficacy.

**To proceed, the following is needed:**
- Confirmation of whether Tilmicosin has any pathway toward human-use development (currently veterinary-only)
- Mechanism of action (MOA) data from DrugBank
- TFDA/SmPC warning and contraindication data (currently a blocking data gap)
- Independent mechanistic or preclinical rationale connecting this drug class to the predicted indication before any further evaluation stage is considered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

