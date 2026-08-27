---
layout: default
title: Tasimelteon
parent: 僅模型預測 (L5)
nav_order: 418
evidence_level: L5
indication_count: 10
---

# Tasimelteon
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

# Tasimelteon: From No Danish Registration to Insomnia (Circadian Rhythm Sleep Disorder)

## One-Sentence Summary

Tasimelteon is a melatonin MT1/MT2 receptor agonist with no current marketing authorisation in Denmark and no local approved-indication data on file.
The TxGNN model's most clinically credible signal points to **Insomnia (disease)**, a mechanistically on-target use supported by **4 clinical trials** (including a completed pivotal Phase 3 RCT) and **6 publications**.
Several other TxGNN-ranked candidates (e.g. polymicrogyria, ALS, axial spondylometaphyseal dysplasia) carry similarly high raw scores but have **zero** supporting trials or literature and are explicitly flagged in the source data as likely graph noise — they are not covered further in this report.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on file — Tasimelteon has no marketing authorisation in Denmark, so no approved-indication text exists in the regulatory data |
| Predicted New Indication | Insomnia (disease) |
| TxGNN Prediction Score | 99.47% |
| Evidence Level | L1 |
| Denmark Market Status | Not Marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Tasimelteon is a melatonin MT1/MT2 receptor agonist that acts directly on the suprachiasmatic nucleus (the body's central circadian pacemaker) to shift circadian phase and promote sleep onset. This is described consistently across the supporting literature and in the model's own rationale text.

Because this mechanism directly governs the sleep-wake cycle, the "predicted" indication of insomnia is not a distant cross-mechanism hypothesis — it is the drug's core, on-target pharmacology. The evidence pack itself notes this is "屬藥理機轉核心適應症範疇，非跨機轉推論" (a core mechanism-consistent indication, not a repurposing inference), which is consistent with the drug class already being used clinically for insomnia and other circadian rhythm sleep-wake disorders.

This is reinforced by a completed Phase 3, double-blind, placebo-controlled trial (n=322) and an actively recruiting Phase 3 pediatric trial (n=420), showing sustained clinical development interest in this indication area — evidence considerably stronger than the model score alone would suggest.

**Note on other TxGNN candidates:** Bilateral parasagittal parieto-occipital polymicrogyria, amyotrophic lateral sclerosis, and axial spondylometaphyseal dysplasia scored similarly high but returned zero clinical trials and zero literature hits. The evidence pack explicitly characterises these as having no known pathophysiological link to melatonin receptor agonism and recommends "Hold" for all of them — they are not analysed further here.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00548340](https://clinicaltrials.gov/study/NCT00548340) | Phase 3 | Completed | 322 | Multicenter, randomized, double-blind, placebo-controlled trial of VEC-162 (tasimelteon) 20mg/50mg daily vs. placebo over 5 weeks in primary insomnia — pivotal-grade efficacy/safety evidence |
| [NCT06953869](https://clinicaltrials.gov/study/NCT06953869) | Phase 3 | Recruiting | 420 | Ongoing multicenter, double-blind, randomized study of tasimelteon vs. placebo for pediatric insomnia disorder |
| [NCT03291041](https://clinicaltrials.gov/study/NCT03291041) | Phase 2 | Completed | 25 | Proof-of-concept study of tasimelteon vs. placebo in travelers with jet lag disorder (adjacent circadian indication) |
| [NCT05922995](https://clinicaltrials.gov/study/NCT05922995) | Early Phase 1 | Terminated | 20 | Single-center, open-label pilot study of tasimelteon 20mg for REM Behavior Disorder; trial terminated early, low evidentiary weight |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35585820](https://pubmed.ncbi.nlm.nih.gov/35585820/) | 2023 | Review | Current Drug Safety | Discusses melatonin/tasimelteon relevance to Alzheimer's-related sleep and behavioral disturbance |
| [25207602](https://pubmed.ncbi.nlm.nih.gov/25207602/) | 2014 | Review | International Journal of Molecular Sciences | Reviews efficacy/safety of melatonin receptor agonists (incl. tasimelteon) across insomnia, depression, and circadian rhythm disorders |
| [24228714](https://pubmed.ncbi.nlm.nih.gov/24228714/) | 2014 | Review | Journal of Medicinal Chemistry | Reviews MT1/MT2 receptor pharmacology; identifies tasimelteon as a high-affinity nonselective MT1/MT2 agonist |
| [22010042](https://pubmed.ncbi.nlm.nih.gov/22010042/) | 2011 | Review | Therapeutic Advances in Neurological Disorders | Reviews melatonin/analogs for sleep disturbance and neuroprotection in Parkinson's disease |
| [22167135](https://pubmed.ncbi.nlm.nih.gov/22167135/) | 2011 | Review | Neuro Endocrinology Letters | Reviews circadian sleep disruption and potential therapeutic value of melatonin in obesity |
| [19557144](https://pubmed.ncbi.nlm.nih.gov/19557144/) | 2009 | Review | Neuropsychiatric Disease and Treatment | Reviews prolonged-release melatonin and synthetic melatoninergic agonists for insomnia management |

---

## Denmark Market Information

Tasimelteon is not currently marketed in Denmark — no marketing authorisation (national or centralised/EMA) is on file, and no approved indication text is available.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A completed Phase 3 RCT (n=322) plus an actively recruiting Phase 3 trial (n=420) provide mechanism-consistent, L1-grade evidence for tasimelteon in insomnia/circadian rhythm sleep disorders. However, the drug has no Danish marketing authorisation and no local safety/label data, so a full risk-benefit assessment cannot yet be completed.

**To proceed, the following is needed:**
- Local safety/label data (key warnings, contraindications) — currently a Blocking data gap preventing safety pre-assessment (S1)
- Formal mechanism-of-action documentation (structured MOA field is currently unpopulated, though rationale text confirms MT1/MT2 agonism)
- Drug-drug interaction (DDI) data — current query returned no results
- A regulatory pathway assessment for Denmark, given zero existing marketing authorisations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

