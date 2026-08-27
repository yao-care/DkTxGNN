---
layout: default
title: Sumatriptan
parent: 僅模型預測 (L5)
nav_order: 409
evidence_level: L5
indication_count: 2
---

# Sumatriptan
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Sumatriptan: From Migraine to Migraine with Brainstem Aura

## One-Sentence Summary

Sumatriptan is a 5-HT1B/1D receptor agonist with an established role in the acute treatment of migraine. The TxGNN model predicts a strong association with **Migraine with Brainstem Aura**, but this signal is currently supported only by mechanistic and observational literature (**18 publications, 0 clinical trials**) — and this migraine subtype is conventionally regarded as a relative/absolute contraindication for triptans, so the finding requires careful safety review before any further action.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Migraine (acute treatment) — based on established pharmacology; no Danish licence data is available for this drug |
| Predicted New Indication | Migraine with Brainstem Aura |
| TxGNN Prediction Score | 99.74% |
| Evidence Level | L4 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, sumatriptan is a selective 5-HT1B/1D receptor agonist that constricts cranial blood vessels and inhibits vasoactive neuropeptide release from perivascular trigeminal axons, a mechanism well established for treating acute migraine.

Migraine with brainstem aura (formerly "basilar-type migraine") is a subtype within the broader migraine spectrum, which is why TxGNN's knowledge-graph model links it strongly to sumatriptan — the drug's original indication and this predicted indication share the same disease family and receptor biology.

However, this mechanistic similarity cuts both ways: because sumatriptan's vasoconstrictive action could theoretically affect brainstem circulation, most clinical guidelines list migraine with brainstem aura as a relative or absolute **contraindication** for triptans rather than an approved use. The high TxGNN score reflects general "sumatriptan–migraine" relatedness in the knowledge graph, not a validated safety profile for this specific aura subtype — the mechanistic and safety signals point in opposite directions, which is why this candidate requires a safety-first review rather than a straightforward efficacy assessment.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23657930](https://pubmed.ncbi.nlm.nih.gov/23657930/) | 2014 | RCT | Phytotherapy Research | Double-blind RCT comparing ginger powder to sumatriptan for acute migraine ablation |
| [25600718](https://pubmed.ncbi.nlm.nih.gov/25600718/) | 2015 | Guideline/Evidence Assessment | Headache | American Headache Society evidence review of acute migraine pharmacotherapies, including triptans |
| [25841032](https://pubmed.ncbi.nlm.nih.gov/25841032/) | 2015 | Cohort/Comparative | Neurology | Sumatriptan shows **reduced efficacy in migraine with aura vs. without aura** — directly relevant caution for this subtype |
| [1313746](https://pubmed.ncbi.nlm.nih.gov/1313746/) | 1992 | RCT | Cephalalgia | Double-blind, placebo-controlled trial of oral sumatriptan 200mg in acute migraine with aura |
| [33567890](https://pubmed.ncbi.nlm.nih.gov/33567890/) | 2021 | RCT | Cephalalgia | Randomised trial: early sumatriptan treatment prevents PACAP38-induced migraine attacks |
| [31135819](https://pubmed.ncbi.nlm.nih.gov/31135819/) | 2019 | Mechanistic/Imaging Study | JAMA Neurology | PET imaging study of central 5-HT1B receptor binding during sumatriptan treatment |
| [38307660](https://pubmed.ncbi.nlm.nih.gov/38307660/) | 2024 | Review | Handbook of Clinical Neurology | Overview of status migrainosus, a recognized complication across migraine (with/without aura) |
| [8536293](https://pubmed.ncbi.nlm.nih.gov/8536293/) | 1995 | Review | Cephalalgia | Critical review of clinical experience with sumatriptan in migraine and cluster headache management |
| [27910087](https://pubmed.ncbi.nlm.nih.gov/27910087/) | 2017 | Review | Headache | Review of menstrual migraine treatment options |
| [37123778](https://pubmed.ncbi.nlm.nih.gov/37123778/) | 2023 | Review | Cureus | Review of migraine management approaches in pregnancy and breastfeeding |

---

## Denmark Market Information

Sumatriptan currently has no marketing authorisation on record with the Laegemiddelstyrelsen (Danish Medicines Agency) in the dataset used for this analysis (0 licences); market status is recorded as **Not marketed**.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

**Important note:** although formal warning/contraindication data was not retrievable for this analysis, published literature (e.g., PMID 25841032) and general triptan-class labelling conventionally treat migraine with brainstem aura as a **contraindicated or high-caution use** for triptans due to theoretical cerebrovascular vasoconstriction risk. This should be explicitly verified against the SmPC before any clinical consideration.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score reflects general sumatriptan–migraine relatedness rather than validated evidence for this specific aura subtype. No clinical trials support this indication, evidence level is L4 (mechanistic/literature only), and the predicted indication conflicts with the conventional contraindication profile of triptans in brainstem-type migraine — safety concerns must be resolved before this can advance.

**To proceed, the following is needed:**
- SmPC warnings/contraindications for sumatriptan (Blocking data gap — required before any S1 safety screening)
- Verified mechanism of action data to support or refute the mechanistic rationale
- A dedicated safety/contraindication review specifically addressing brainstem aura and triptan vasoconstriction risk
- If pursued, a marketing authorisation pathway with the Laegemiddelstyrelsen, as none currently exists
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

