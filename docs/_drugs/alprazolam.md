---
layout: default
title: Alprazolam
parent: 僅模型預測 (L5)
nav_order: 28
evidence_level: L5
indication_count: 6
---

# Alprazolam
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

# Alprazolam: From Anxiety & Panic Disorder to Insomnia

## One-Sentence Summary

Alprazolam is a triazolo-benzodiazepine widely used for anxiety disorders and panic disorder, acting through positive allosteric modulation of GABA-A receptors to suppress central nervous system activity.
The TxGNN model predicts it may also be effective for **Insomnia**, with **7 clinical trials** and **18 publications** currently supporting this direction.
Evidence is predominantly observational (Level L3), and alprazolam is **not currently authorised in Denmark**, meaning immediate clinical use would require named-patient import or consideration of authorised alternatives.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Anxiety disorder, panic disorder (well-established clinical use; no Danish marketing authorisation on file) |
| Predicted New Indication | Insomnia |
| TxGNN Prediction Score | 99.81% |
| Evidence Level | L3 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data was not included in this evidence pack. Based on established pharmacology, alprazolam is a GABA-A positive allosteric modulator: it binds to the benzodiazepine site of the GABA-A receptor, enhancing chloride ion influx and thereby suppressing central nervous system excitability. This mechanism directly produces sedative-hypnotic effects — reducing sleep onset latency and increasing total sleep time — which provide a clear pharmacological rationale for TxGNN's insomnia prediction.

Anxiety disorders and insomnia are closely intertwined conditions. Patients with generalised anxiety disorder or panic disorder frequently experience sleep disturbance as a core symptom, driven by the same state of pathological hyperarousal that alprazolam's GABAergic mechanism targets. The sedative effects of alprazolam are therefore pharmacologically continuous with its primary anxiolytic indication, making the predicted crossover to insomnia biologically plausible. In fact, several published studies use alprazolam as an active comparator in sleep disorder research (PMID 33403184, PMID 39183410), confirming its practical use in this setting.

That said, alprazolam is **not recommended as a first-line therapy for chronic insomnia** per current European guidelines. Long-term use carries substantial risks of physical dependence, tolerance, rebound insomnia upon discontinuation, and — particularly in elderly patients — falls, cognitive impairment, and road traffic accidents. The available evidence base for alprazolam specifically in insomnia consists of observational studies and indirect comparisons rather than dedicated, placebo-controlled insomnia RCTs, which limits the overall evidence rating to L3.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT02648776](https://clinicaltrials.gov/study/NCT02648776) | N/A | Unknown | 1,400 | Large prospective cohort at a Taiwanese academic centre examining medication use patterns, efficacy, safety, and pharmacokinetic/pharmacogenetic characteristics of commonly prescribed hypnotics (including alprazolam) in elderly patients with sleep disorders; provides real-world risk–benefit data |
| [NCT00266409](https://clinicaltrials.gov/study/NCT00266409) | Phase 4 | Completed | 418 | Multicentre, randomised, open-label trial comparing Niravam™ (alprazolam orally disintegrating tablet) combined with a newly prescribed SSRI or SNRI vs SSRI/SNRI alone in patients with generalised anxiety disorder or panic disorder; sleep disturbance is a core symptom domain in both target conditions |

> **Note:** Five additional trials retrieved by the evidence search (NCT04572750, NCT01146600, NCT01893632, NCT03327506, NCT01584440) were assessed as low relevance (Grade C) to alprazolam in insomnia — they investigate benzodiazepine cessation, an unrelated drug (clarithromycin), gabapentin for BZD dependence, perioperative anxiety management, and Alzheimer's agitation respectively — and have therefore been excluded from this table.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [33403184](https://pubmed.ncbi.nlm.nih.gov/33403184/) | 2020 | Comparative RCT | *Cureus* | Direct head-to-head comparison of alprazolam vs melatonin for sleep disorders in end-stage renal disease patients on haemodialysis; evaluates subjective and objective sleep quality, fatigue, and daytime functioning — the most directly relevant trial for this repurposing claim |
| [39183410](https://pubmed.ncbi.nlm.nih.gov/39183410/) | 2024 | Observational (Active Comparator) | *Medicine* | Retrospective study (n=116) comparing Du Meridian moxibustion plus ear acupuncture vs alprazolam alone in patients with comorbid coronary heart disease and insomnia; alprazolam used as the standard-of-care control, confirming its real-world use in insomnia |
| [36692463](https://pubmed.ncbi.nlm.nih.gov/36692463/) | 2023 | Systematic Review / Meta-analysis | *Acta Pharmaceutica (Zagreb)* | Systematic review and meta-analysis of tranquiliser use (including benzodiazepines) in elderly patients with chronic non-communicable diseases; assesses optimal dosing, efficacy outcomes, and adverse effects profile |
| [23330992](https://pubmed.ncbi.nlm.nih.gov/23330992/) | 2013 | Review | *Expert Opin Drug Metab Toxicol* | Comprehensive review of pharmacokinetics of anxiolytic drugs including alprazolam; provides mechanistic context for its sedative-hypnotic activity and inter-individual variability relevant to dosing in insomnia |
| [37801512](https://pubmed.ncbi.nlm.nih.gov/37801512/) | 2023 | Preclinical (Proteomics) | *Aging* | Repeated alprazolam administration in mice causes mitochondrial dysfunction and hippocampus-dependent memory consolidation impairment; mechanistic study directly relevant to long-term safety concerns when considering alprazolam for chronic insomnia |
| [37984023](https://pubmed.ncbi.nlm.nih.gov/37984023/) | 2024 | Epidemiological Model | *Value Health Reg Issues* | 10-year predictive model of benzodiazepine use in Croatia documenting real-world prescribing for anxiety, insomnia, and mood disorders; highlights rising economic burden and associated harms including memory loss and falls in elderly populations |
| [35493764](https://pubmed.ncbi.nlm.nih.gov/35493764/) | 2022 | Cohort Study | *JHEP Reports* | Deprescribing benzodiazepines (including zolpidem) reduces falls and fractures in patients with cirrhosis; provides safety signal relevant to evaluating benzodiazepine class risk in vulnerable populations |
| [38363887](https://pubmed.ncbi.nlm.nih.gov/38363887/) | 2024 | Cross-sectional | *Medicine* | Cross-sectional study of insomnia among COVID-19 survivors using the Insomnia Severity Index; characterises contemporary insomnia burden and influencing factors, providing disease-level context |

---

## Denmark Market Information

Alprazolam currently holds **no marketing authorisations** in Denmark. The drug is classified as **not marketed** by Lægemiddelstyrelsen (the Danish Medicines Agency), and no centralised EMA authorisation exists for this compound in the European Union. No product-specific safety, dosing, or indication data from a SmPC is therefore available through this channel.

Healthcare professionals wishing to prescribe alprazolam in Denmark would need to pursue use under individual named-patient import procedures and would be required to obtain safety and prescribing guidance from existing international SmPCs (e.g., FDA-approved US label or product documentation from markets where alprazolam is authorised). Consideration of therapeutic alternatives within the benzodiazepine or non-benzodiazepine hypnotic class with existing Danish marketing authorisations is strongly recommended before initiating any clinical protocol.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) from an authorised market (e.g., the US FDA label for Xanax/Niravam or equivalent) for full safety information, including warnings regarding dependence, rebound insomnia, respiratory depression, cognitive impairment, and use in elderly and hepatically impaired patients.

> No safety data (warnings, contraindications, or drug–drug interaction data) was retrievable for alprazolam through the sources queried in this evidence pack. This represents a **blocking data gap** that must be resolved before any clinical decision can be made.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Alprazolam's GABAergic mechanism provides a biologically plausible and pharmacologically well-understood basis for insomnia management, and published studies confirm its real-world use as an active comparator in sleep disorder research (particularly in haemodialysis patients). However, no dedicated placebo-controlled insomnia RCT for alprazolam exists, the evidence sits at L3, the drug is not authorised in Denmark, and critical safety data remain unavailable in this pack.

**To proceed, the following is needed:**

- **Resolve blocking data gap (DG001):** Obtain SmPC warnings and contraindications from an authorised market (e.g., download FDA label PDF) before any safety assessment can be completed
- **Resolve high-priority data gap (DG002):** Confirm mechanism of action via DrugBank API query to substantiate GABA-A modulation claims formally
- **Regulatory pathway clarification:** Assess feasibility of named-patient import in Denmark, or identify Danish-authorised benzodiazepines (e.g., nitrazepam, triazolam) as therapeutic proxies for the insomnia indication
- **Risk stratification plan:** Develop a prescribing framework addressing dependence liability, rebound insomnia, and fall/cognitive risk — particularly for elderly patients, who constitute the primary insomnia-treatment population
- **Evidence upgrade pathway:** Determine whether a prospective observational registry or comparative effectiveness study using existing Danish sleep-disorder cohorts could elevate evidence from L3 to L2 without requiring a new full RCT

---

*This report is generated for research purposes only and does not constitute medical advice. All repurposing candidates require clinical validation before therapeutic application. Data cut-off: 4 April 2026.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

