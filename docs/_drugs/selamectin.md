---
layout: default
title: Selamectin
parent: 僅模型預測 (L5)
nav_order: 394
evidence_level: L5
indication_count: 10
---

# Selamectin
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

# Selamectin: From Veterinary Antiparasitic Use to Candidiasis

## One-Sentence Summary

Selamectin is an avermectin-class macrocyclic lactone approved exclusively as a veterinary antiparasitic (fleas, mites, heartworm prevention in dogs and cats) — it has no approved human indication and no marketing authorisation in Denmark. The TxGNN model predicts potential efficacy for **Candidiasis**, but this prediction is currently supported by **0 clinical trials** and **0 publications**, and is based purely on knowledge-graph topology rather than any known antifungal mechanism.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not established for human use — approved only as a veterinary antiparasitic (ecto-/endoparasite control in companion animals); no human indication data available |
| Predicted New Indication | Candidiasis |
| TxGNN Prediction Score | 98.43% |
| Evidence Level | L5 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available (MOA marked as a data gap). Based on the information that is available, Selamectin is an avermectin-class macrocyclic lactone whose known pharmacology activates invertebrate glutamate-gated chloride channels — a mechanism specific to arthropod and nematode nervous systems. It has no documented antifungal activity pathway.

There is no established mechanistic or clinical relationship between Selamectin's approved veterinary antiparasitic use and human candidiasis (a fungal infection). The evidence pack's own rationale is explicit on this point: the high TxGNN score (0.984) reflects graph-topological similarity within the knowledge graph rather than any pharmacological plausibility.

Because Selamectin has never been studied in humans — it has no human PK/PD data, no human safety database, and toxicology is limited to veterinary/animal studies — mechanistic extrapolation to candidiasis cannot currently be supported.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Denmark Market Information

Selamectin holds no marketing authorisation in Denmark (0 licenses on file); the product is not currently registered with Lægemiddelstyrelsen or centrally through the EMA.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information. No key warnings, contraindications, or drug interaction data are currently available for this candidate.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The candidiasis prediction has zero supporting clinical trials or literature, no plausible mechanism of action, no human safety data, and the drug is not registered in Denmark — evidence is insufficient to proceed beyond model-prediction stage (L5/S0).

**To proceed, the following is needed:**
- Confirmed mechanism of action (MOA) data from DrugBank or primary literature
- Any preclinical (in vitro/in vivo) antifungal activity data for Selamectin
- Human pharmacokinetic and safety/toxicology data, given the drug has no prior human exposure history
- TFDA/EMA/SmPC-level warnings and contraindications before any S1 safety screening can begin

**Data quality note:** Among the other TxGNN candidates in this pack, the "heart disease" prediction (rank 9–10, L4) is supported only by veterinary literature on *heartworm disease* (Dirofilaria immitis infection) — an apparent keyword-matching artifact ("heartworm disease" → "heart disease"), not evidence of activity against human cardiac disease. This should not be read as supporting evidence for a cardiovascular indication.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

