---
layout: default
title: Pitolisant
parent: 僅模型預測 (L5)
nav_order: 353
evidence_level: L5
indication_count: 6
---

# Pitolisant
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Pitolisant: From Narcolepsy to Insomnia

## One-Sentence Summary

> Pitolisant is a selective histamine H3-receptor inverse agonist/antagonist, best documented in the literature for treating excessive daytime sleepiness in **narcolepsy** and residual sleepiness in obstructive sleep apnoea (OSA).
> The TxGNN model predicts it may be effective for **Insomnia**, but this is supported only by **1 unrelated, withdrawn clinical trial** and **8 publications**, none of which studied insomnia directly.
> The drug's pharmacological effect is wake-promoting, which is mechanistically opposite to what an insomnia treatment requires — this prediction should be treated as a candidate for review, not as a validated repurposing signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Narcolepsy with or without cataplexy (per literature evidence; no Danish licensing record available to confirm) |
| Predicted New Indication | Insomnia (disease) |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L4 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the structured DrugBank field for this evidence pack. Based on the supporting literature, pitolisant is known as a first-in-class, selective histamine H3-receptor inverse agonist/antagonist. By blocking presynaptic H3 autoreceptors, it increases histamine release (and downstream dopamine/acetylcholine signalling) in the brain, producing a **wake-promoting** effect. This mechanism underlies its established use for excessive daytime sleepiness in narcolepsy and, in trial settings, for residual sleepiness in OSA patients on CPAP.

This is precisely why the TxGNN prediction for **Insomnia** should be treated with caution rather than taken at face value. Insomnia treatment requires a **sedative/hypnotic** effect, whereas pitolisant's documented pharmacology drives the opposite (arousal-promoting) direction. The evidence pack itself flags this as a likely ontology-mapping artifact: the "insomnia (disease)" node in the underlying knowledge graph may be too broad and could be capturing sleep-disorder relationships in general (including narcolepsy/EDS), rather than a specific insomnia signal. None of the 8 supporting publications studied insomnia as an endpoint — they cover narcolepsy, OSA-related sleepiness, and general H3-receptor pharmacology.

Given this mechanistic contradiction, the prediction cannot currently be interpreted as clinically reasonable without manual review of how the disease node was mapped. It should not be advanced on the strength of the TxGNN score alone.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02800083](https://clinicaltrials.gov/study/NCT02800083) | Phase 2 | Withdrawn | 0 | Trial was designed to evaluate pitolisant for **alcohol use disorder**, not insomnia (title truncated in source data as "For A..."). Withdrawn with zero enrollment — no clinical data was generated. Graded "C" relevance: does not support the insomnia indication. |

*No clinical trial in this evidence pack directly evaluated pitolisant for insomnia.*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36931805](https://pubmed.ncbi.nlm.nih.gov/36931805/) | 2023 | RCT | The Lancet. Neurology | Phase 3 RCT confirming safety/efficacy of pitolisant in children ≥6 with narcolepsy with/without cataplexy — not an insomnia study. |
| [33121980](https://pubmed.ncbi.nlm.nih.gov/33121980/) | 2021 | RCT | Chest | RCT of pitolisant for residual excessive daytime sleepiness in OSA patients on CPAP — wake-promoting effect, opposite direction to insomnia treatment. |
| [31917607](https://pubmed.ncbi.nlm.nih.gov/31917607/) | 2020 | RCT | Am J Respir Crit Care Med | RCT of pitolisant for daytime sleepiness in OSA patients refusing CPAP — again a wake-promoting indication. |
| [36169322](https://pubmed.ncbi.nlm.nih.gov/36169322/) | 2022 | Cohort | Revista de neurología | Real-life cohort (WAKE study) of pitolisant in treatment-refractory type 1 narcolepsy with cataplexy. |
| [34521328](https://pubmed.ncbi.nlm.nih.gov/34521328/) | 2022 | Review | Current Neuropharmacology | Review of histaminergic system changes in neuropsychiatric disorders; notes pitolisant is used for narcolepsy sleepiness, in contrast to H1-antagonists (e.g., doxepin) used for insomnia. |
| [34225942](https://pubmed.ncbi.nlm.nih.gov/34225942/) | 2021 | Review | Handbook of Clinical Neurology | General review of histamine receptor pharmacology (H1–H4); background mechanism reference only. |
| [30214155](https://pubmed.ncbi.nlm.nih.gov/30214155/) | 2018 | Review | Drug Design, Development and Therapy | Profile of pitolisant's development and therapeutic role, confirming its approved use is narcolepsy, not insomnia. |
| [22356925](https://pubmed.ncbi.nlm.nih.gov/22356925/) | 2012 | Review | Clinical Neuropharmacology | Early review describing pitolisant as a stimulant for narcolepsy-cataplexy in teenagers with refractory sleepiness. |

*None of the above literature studied pitolisant specifically for insomnia; all directly relevant clinical studies concern narcolepsy or OSA-related excessive daytime sleepiness — the opposite clinical direction.*

---

## Denmark Market Information

Pitolisant currently holds **no marketing authorisation in Denmark** (market status: Not marketed; 0 authorisations on record). No product, dosage form, or approved-indication data is available from Danish sources in this evidence pack.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information. No structured warnings, contraindications, or drug-interaction data were available in this evidence pack (DDI query returned no results).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The predicted indication (insomnia) is mechanistically inconsistent with pitolisant's known wake-promoting pharmacology, and no clinical trial or publication in the evidence pack actually studied insomnia as an endpoint. The single associated trial (NCT02800083) targeted alcohol use disorder and was withdrawn without enrollment. This pattern is consistent with an overly broad disease-node mapping in the underlying knowledge graph rather than a genuine repurposing signal.

**To proceed, the following is needed:**
- Manual review/curation of the "insomnia (disease)" node mapping used by the TxGNN model, to confirm whether it inadvertently aggregates narcolepsy/EDS-related relationships
- Confirmed mechanism of action (MOA) documentation from DrugBank or the SmPC, rather than relying solely on literature inference
- Danish/EU licensing and SmPC data (warnings, contraindications, interactions), since pitolisant is not currently marketed in Denmark
- If the mechanistic conflict cannot be resolved, this candidate should be deprioritized in favour of the lower-confidence but mechanistically plausible ADHD signal (TxGNN score 99.36%), which is currently only supported by preclinical/mechanistic literature and warrants a Research Question stage rather than further insomnia-focused review
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

