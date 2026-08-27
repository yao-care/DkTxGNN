---
layout: default
title: Praziquantel
parent: 僅模型預測 (L5)
nav_order: 357
evidence_level: L5
indication_count: 10
---

# Praziquantel
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

# Praziquantel: From Schistosomiasis to Uterine Corpus Epithelioid Leiomyosarcoma

## One-Sentence Summary

Praziquantel is a classic antiparasitic agent used to treat schistosomiasis and other trematode/cestode (fluke and tapeworm) infections. The TxGNN model's top-ranked prediction points to **Uterine Corpus Epithelioid Leiomyosarcoma**, but this signal is currently supported by **0 clinical trials** and **0 publications**, with no established mechanistic rationale.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Schistosomiasis and other trematode/cestode (parasitic worm) infections |
| Predicted New Indication | Uterine Corpus Epithelioid Leiomyosarcoma |
| TxGNN Prediction Score | 97.28% |
| Evidence Level | L5 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for Praziquantel is a documented data gap in this evidence pack. Based on established pharmacology, Praziquantel increases calcium-ion permeability across the tegument and musculature of platyhelminths (flukes and tapeworms), causing spastic paralysis and tegmental disruption that exposes the parasite to host immune clearance. This mechanism is specific to flatworm neuromuscular/tegmental biology.

There is no known mechanistic overlap between this platyhelminth-specific calcium-channel/tegument effect and the pathogenic pathways implicated in uterine leiomyosarcoma (e.g., TP53, RB1 mutation, MDM2 pathway dysregulation). The repurposing rationale for this candidate explicitly states no plausible biological hypothesis could be constructed.

Importantly, the 97.28% TxGNN score is not corroborated by any clinical trial or literature evidence for this specific indication (0/0). This gap between a high model score and a complete absence of supporting evidence suggests the score likely reflects knowledge-graph topology (e.g., indirect node proximity) rather than a validated pharmacological signal — consistent with its L5 evidence classification and Hold recommendation.

*Note: among this drug's 10 model-ranked candidates, Plasmodium falciparum malaria (rank 3, score 97.22%) is a separate signal actually backed by clinical trial and literature data (L3, "Research Question" stage) — see Conclusion for a note on this alternate candidate.*

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Denmark Market Information

Praziquantel currently holds no marketing authorisation in Denmark (0 licenses on record; market status: Not marketed).

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (Uterine Corpus Epithelioid Leiomyosarcoma) is supported only by a TxGNN model score, with no clinical trials, no literature, and no plausible mechanistic hypothesis (L5). The drug is also not currently marketed in Denmark and lacks the basic MOA and SmPC safety data needed to begin a formal safety review.

**To proceed, the following is needed:**
- Mechanism of action data via DrugBank API (data gap DG002, High priority)
- SmPC warnings/contraindications from the responsible regulatory source (data gap DG001, Blocking)
- Preclinical/mechanistic studies exploring any plausible activity against uterine leiomyosarcoma before further evidence-gathering is warranted
- If pursuing antiparasitic repurposing signals for this drug, separately evaluate the Plasmodium falciparum malaria candidate (rank 3, L3, "Research Question" stage), which has actual supporting trial and literature data unlike the current top-ranked candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

