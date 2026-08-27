---
layout: default
title: Inotersen
parent: 僅模型預測 (L5)
nav_order: 232
evidence_level: L5
indication_count: 10
---

# Inotersen
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

Using the Evidence Pack provided, here is the drug repurposing evaluation report.

---

# Inotersen: From Hereditary Transthyretin Amyloidosis (hATTR) to Acute Intermittent Porphyria

## One-Sentence Summary

Inotersen is a liver-targeted antisense oligonucleotide (ASO) approved for hereditary transthyretin-mediated (hATTR) amyloidosis, where it reduces amyloidogenic transthyretin (TTR) protein production. TxGNN predicts a possible effect in **Acute Intermittent Porphyria (AIP)**, but this signal is currently supported by **0 clinical trials** and only **1 indirect literature reference** — and the evidence pack's own mechanistic analysis flags the biological link as implausible.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hereditary transthyretin-mediated (hATTR) amyloidosis *(from evidence-pack background text; not present in the formal `original_indications` registry field — see Data Gap DG002)* |
| Predicted New Indication | Acute Intermittent Porphyria |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L4 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the structured registry (Data Gap DG002, High severity). Based on background information contained in the evidence pack, Inotersen is an antisense oligonucleotide that binds TTR mRNA in the liver, lowering circulating TTR protein and thereby reducing amyloid fibril deposition — the basis for its approval in hATTR amyloidosis.

The evidence pack's own mechanistic rationale, however, argues **against** a plausible link to Acute Intermittent Porphyria. AIP is caused by dysregulation of the heme biosynthesis pathway (ALAS1/PBGD-HMBS deficiency), leading to accumulation of δ-ALA and porphyrin precursors. A therapy already exists for this exact mechanism — Givosiran, an RNAi drug that specifically silences hepatic ALAS1 mRNA. Inotersen's target (TTR) shares no known molecular pathway with heme biosynthesis or porphyrin metabolism.

The rationale text concludes that the very high TxGNN score most likely reflects a **structural similarity cluster in the knowledge graph** — "liver-targeted oligonucleotide therapies for rare hereditary metabolic/neurological disease" — rather than a genuine drug-target-disease mechanistic connection. The single supporting publication (PMID 30847674) is a general review of neuromuscular disease therapeutics that discusses ASO/RNAi drugs for hATTR amyloidosis broadly; it does not address Inotersen's use in AIP specifically, and is classified in the evidence pack as indirect, non-specific evidence.

**In short: this is a low-confidence, model-only signal that internal mechanistic review considers unlikely to reflect true pharmacological relevance.**

---

## Clinical Trial Evidence

Currently no related clinical trials registered. (ClinicalTrials.gov and WHO ICTRP searches for Inotersen + Acute Intermittent Porphyria both returned 0 results, per query log.)

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30847674](https://pubmed.ncbi.nlm.nih.gov/30847674/) | 2019 | Review | Neurological Sciences | General review of therapeutic advances in genetic neuromuscular/peripheral neuropathy disorders, including ASO/RNAi drugs used for hATTR amyloidosis; does **not** discuss Inotersen use in Acute Intermittent Porphyria — classified as indirect, non-specific evidence. |

---

## Denmark Market Information

Inotersen currently has **no marketing authorisation on file** for Denmark (`market_status: 未上市` / Not marketed; `total_licenses: 0`). No national (Laegemiddelstyrelsen) or centralised (EMA) authorisation records were available in this evidence pack.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

*Note: Key warnings, contraindications, and drug-interaction data were all flagged as unavailable in this evidence pack. Retrieval of TFDA/SmPC-level warnings and contraindications is recorded as a **Blocking data gap (DG001)** — without it, this candidate cannot proceed to the S1 safety pre-assessment stage.*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The prediction rests solely on a TxGNN similarity score, with zero clinical trials and only one indirect (non-disease-specific) literature reference.
- The evidence pack's own mechanistic review considers the TTR–AIP biological link implausible, attributing the high score to knowledge-graph structural clustering rather than a genuine pharmacological relationship — a validated, mechanism-specific RNAi therapy (Givosiran/ALAS1) already exists for AIP.
- Inotersen is not currently marketed in Denmark, and mandatory safety data (SmPC warnings/contraindications) are missing — a Blocking data gap (DG001) that prevents advancement past the current S0 screening stage.

**To proceed, the following is needed:**
- Resolve Blocking data gap DG001: obtain TFDA/SmPC warnings and contraindications before any safety pre-assessment (S1) can begin
- Resolve High-severity data gap DG002: obtain confirmed mechanism-of-action data from DrugBank/manufacturer to properly assess mechanistic plausibility
- Independent expert (hepatology/porphyria specialist) review of whether any indirect TTR–heme pathway interaction could exist, given the current mechanistic assessment argues against it
- Ongoing monitoring for any future preclinical or clinical evidence specific to Inotersen in porphyria, before reconsidering this candidate
- Confirmation of Danish/EU regulatory pathway and route-of-administration compatibility should market status change
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

