---
layout: default
title: Lorazepam
parent: 僅模型預測 (L5)
nav_order: 269
evidence_level: L5
indication_count: 10
---

# Lorazepam
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

Using none of the loaded skills here — this is a direct, fully-specified report-writing task with an explicit template already given in the prompt, so I'll follow it directly rather than force-fit a skill.

One judgment call worth flagging up front: `predicted_indications[0]` ("trigeminal nerve neoplasm") is explicitly annotated in its own `repurposing_rationale` as TxGNN graph noise with zero supporting evidence ("屬 TxGNN 知識圖譜連結雜訊，應排除" — recommendation: Hold, evidence L5). Reporting that as the headline indication would be actively misleading to a prescriber. I used the next candidate with real, gradable evidence instead — **insomnia (disease)**, L2, "Proceed with Guardrails" — and note the excluded noise candidates below the report.

---

# Lorazepam: From Anxiety Disorders to Insomnia

## One-Sentence Summary

Lorazepam is a benzodiazepine (GABA-A receptor positive allosteric modulator) established for anxiety and, at the class level, for short-term sedative-hypnotic use. The TxGNN model predicts continued effectiveness for **Insomnia**, with **23 clinical trials** and **18 publications** currently identified, including one completed Phase 3 RCT of a lorazepam-containing combination product.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | No Danish marketing authorisation on file (product not marketed); pharmacologically established as an anxiolytic/sedative-hypnotic, benzodiazepine class |
| Predicted New Indication | Insomnia (disease) |
| TxGNN Prediction Score | 99.80% |
| Evidence Level | L2 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (DrugBank MOA field: Data Gap). Based on known information, lorazepam belongs to the benzodiazepine class, acting as a positive allosteric modulator at the GABA-A receptor to enhance inhibitory neurotransmission — the same mechanism responsible for its established anxiolytic and sedative effects.

The link between anxiolytic/sedative use and insomnia is direct rather than speculative: GABA-A potentiation produces sedation and reduced sleep latency as a core pharmacological effect, not a secondary or off-target one. Multiple identified trials studied lorazepam specifically as a hypnotic agent (e.g., in combination with diphenhydramine and zolpidem for transient insomnia), and one publication (PMID 30764) explicitly characterizes lorazepam's behavioral pharmacology profile as consistent with both anxiolytic and anti-convulsant/sedative activity.

Because benzodiazepines as a class are already used clinically for short-term insomnia in multiple jurisdictions, the mechanistic rationale here is strong; the main open question is not "does it work" but "how does it compare on safety/dependence risk to current standard-of-care hypnotics," which the guardrails below are meant to address.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03331042](https://clinicaltrials.gov/study/NCT03331042) | Phase 3 | Completed | 85 | 4-way crossover RCT of SM-1 (diphenhydramine + zolpidem + delayed-release lorazepam) vs. diphenhydramine+zolpidem, diphenhydramine+lorazepam, and placebo in a phase-advance model of transient insomnia |
| [NCT02671760](https://clinicaltrials.gov/study/NCT02671760) | Phase 2 | Completed | 39 | Pharmacodynamic study of a lorazepam-containing combination (with diphenhydramine, zolpidem) on total sleep time in transient insomnia |
| [NCT04396327](https://clinicaltrials.gov/study/NCT04396327) | Phase 2 | Not yet recruiting | 14 | 2-way crossover PD study of SM-1 vs. a diphenhydramine+lorazepam active comparator in a 3-hour phase-advance model of transient insomnia |
| [NCT03338764](https://clinicaltrials.gov/study/NCT03338764) | Phase 3 | Withdrawn (enrollment 0) | 0 | Planned double-blind, placebo-controlled study of SM-1 efficacy/safety/pattern-of-use in transient insomnia; withdrawn before enrollment |
| [NCT02648776](https://clinicaltrials.gov/study/NCT02648776) | N/A | Unknown | 1400 | Prospective Taiwanese cohort on risk/benefit of hypnotic agents (including benzodiazepine class) in elderly patients; large sample but not lorazepam-specific and status unknown |
| [NCT04572750](https://clinicaltrials.gov/study/NCT04572750) | N/A | Completed | 170 | Self-management intervention to promote benzodiazepine cessation (incl. lorazepam); informs dependence/discontinuation risk rather than efficacy |
| [NCT06584513](https://clinicaltrials.gov/study/NCT06584513) | N/A | Recruiting | 470 | Intervention to reduce benzodiazepine/sedative-hypnotic use in older adults with sleep problems; directionally supports safety caution rather than efficacy |
| [NCT00826553](https://clinicaltrials.gov/study/NCT00826553) | Phase 1 | Terminated | 6 | Polysomnographic comparison of α2-agonist vs. GABA-agonist sedation in mechanically ventilated patients |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3280615](https://pubmed.ncbi.nlm.nih.gov/3280615/) | 1988 | RCT | Journal of Clinical Pharmacology | Double-blind crossover trial: lorazepam 2mg outperformed flurazepam 30mg on most sleep parameters in chronic insomniacs over 3 weeks |
| [10220122](https://pubmed.ncbi.nlm.nih.gov/10220122/) | 1999 | Cohort/Clinical study | International Clinical Psychopharmacology | Tested lorazepam 0.5mg TID (24-hour dosing) vs. 1.5mg HS (evening) in primary insomnia, targeting daytime fatigue symptoms |
| [35087274](https://pubmed.ncbi.nlm.nih.gov/35087274/) | 2022 | Review | Journal of Multidisciplinary Healthcare | Reviews efficacy, safety and drug-drug interactions of insomnia therapies in COVID-19 patients ("coronasomnia") |
| [30625122](https://pubmed.ncbi.nlm.nih.gov/30625122/) | 2018 | Review | The Medical Letter on Drugs and Therapeutics | General review of drug options for chronic insomnia |
| [36692463](https://pubmed.ncbi.nlm.nih.gov/36692463/) | 2023 | Meta-analysis | Acta Pharmaceutica | Meta-analysis of tranquilizer use (dose, outcomes, adverse effects) in elderly patients |
| [39315391](https://pubmed.ncbi.nlm.nih.gov/39315391/) | 2024 | Cohort (prescription pattern) | BMJ Neurology Open | Characterizes benzodiazepine prescribing in patients with psychogenic non-epileptic seizures |
| [15341891](https://pubmed.ncbi.nlm.nih.gov/15341891/) | 2004 | Cohort (prescription pattern) | Sleep Medicine | Assesses hypnotic prescription patterns and patient characteristics in a large managed-care population |
| [25453732](https://pubmed.ncbi.nlm.nih.gov/25453732/) | 2014 | Cohort (prescription pattern) | Clinical Therapeutics | Examines potentially inappropriate benzodiazepine/sedative-hypnotic use in seriously ill older veterans |
| [19514972](https://pubmed.ncbi.nlm.nih.gov/19514972/) | 2009 | Preclinical (animal) | Drug Delivery | Rat model comparing intranasal microemulsion delivery of diazepam, lorazepam and alprazolam for sleep induction |

## Denmark Market Information

Lorazepam currently has **no marketing authorisation on file with the Danish Medicines Agency (Lægemiddelstyrelsen)** — market status is "Not marketed," with 0 registered licenses (national or EMA-centralised) in this dataset.

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information. No Danish label warnings, contraindications, or drug-drug interaction data were retrievable in this evidence pack (DDI query: not found).

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
- The insomnia signal has genuine mechanistic and clinical-trial support (L2: one completed Phase 3 RCT, plus a directly-on-target 1988 RCT), unlike the top TxGNN-ranked candidates (trigeminal nerve neoplasm, reading/audiogenic/eating/thinking/orgasm-induced seizures), which have no clinical trial evidence and in several cases are explicitly flagged in the source data as knowledge-graph noise.
- However, this drug has **no current Danish marketing authorisation** and **no retrievable SmPC/label safety data** — a Blocking-severity data gap that prevents a full safety pre-assessment (S1) despite the indication itself reaching an S2 evidence stage.

**To proceed, the following is needed:**
- Danish/EU SmPC (warnings, contraindications, DDI) — currently a Blocking data gap
- Mechanism of action confirmation from DrugBank (currently Data Gap)
- Formal relevance grading of the "pending" clinical trials and literature listed above
- Given the benzodiazepine dependence/withdrawal safety signal present across several trials (e.g. NCT04572750, NCT06584513), a specific risk-benefit assessment for long-term vs. short-term insomnia use before any guardrails are finalized
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

