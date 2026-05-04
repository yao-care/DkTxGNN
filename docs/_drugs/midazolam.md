---
layout: default
title: Midazolam
parent: 僅模型預測 (L5)
nav_order: 233
evidence_level: L5
indication_count: 2
---

# Midazolam
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

# Midazolam: From Sedation and Anaesthesia to Insomnia

## One-Sentence Summary

Midazolam is a short-acting benzodiazepine widely used in clinical practice for procedural sedation, anaesthesia induction, and anxiolysis. The TxGNN model predicts it may be effective for **Insomnia**, with **2 directly relevant clinical trials** and **4 RCTs in the published literature** currently supporting this direction. However, pharmacokinetic limitations and long-term safety concerns raise significant questions about its suitability for chronic insomnia management.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Sedation, anaesthesia induction, anxiolysis (established clinical use; no indication listed in Danish regulatory data) |
| Predicted New Indication | Insomnia |
| TxGNN Prediction Score | 99.74% |
| Evidence Level | L2 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Midazolam belongs to the benzodiazepine class and exerts its central nervous system effects by positively modulating GABA-A receptors at the BZ1 and BZ2 subtypes. This increases chloride ion influx, hyperpolarises neurons, and broadly suppresses CNS excitability. In sleep terms, the net result is a reduction in sleep-onset latency and an increase in the proportion of NREM sleep — both mechanistically relevant to the core pathophysiology of insomnia, which is characterised by GABAergic hypoactivity and chronic cortical hyperarousal.

The pharmacological logic connecting midazolam to insomnia is therefore sound: the same GABAergic mechanism that makes benzodiazepines effective for acute sedation also underpins their short-term hypnotic efficacy. Clinical literature from the 1980s and 1990s (see below) confirms that oral midazolam can reduce insomnia symptoms in hospitalised patients. An animal model (PMID 21396773) further corroborates the link between GABAergic dysregulation in the cingulate cortex and sleep disturbance.

Critically, however, midazolam's relatively short elimination half-life (1.5–3.5 hours) creates a significant clinical problem: as plasma levels fall in the early morning hours, rebound insomnia and anxious awakening frequently occur. Moreover, sustained receptor downregulation with repeated dosing leads to tolerance within days to weeks, and abrupt discontinuation carries a recognised withdrawal risk. These pharmacokinetic and pharmacodynamic properties mean that while midazolam may have acute hypnotic utility, it is not well-suited to the management of chronic insomnia — a condition typically requiring sustained, non-habit-forming therapy. The TxGNN model's high prediction score likely reflects the mechanistic overlap rather than a clinically actionable repurposing opportunity in its current form.

---

## Clinical Trial Evidence

Of the 32 clinical trials retrieved, the majority involved midazolam as a comparator agent for sedation or studied non-pharmacological sleep interventions. Only two trials achieved Grade B relevance for the Midazolam–insomnia repurposing question.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|------------|------|--------|-----------|-------------|
| [NCT06407518](https://clinicaltrials.gov/study/NCT06407518) | Not classified | Recruiting | 280 | Prospective RCT evaluating preoperative oral midazolam in colorectal cancer patients with sleep disturbance or anxiety; primary endpoint is postoperative pain, but the study population overlaps substantially with insomnia patients, and short-term hypnotic efficacy is assessed |
| [NCT02142595](https://clinicaltrials.gov/study/NCT02142595) | Phase 4 | Completed | 111 | Directly compares IV dexmedetomidine versus IV midazolam combined with spinal anaesthesia on postoperative sleep quality in TURP patients; addresses sleep as a secondary outcome and provides completed data, though the context is perioperative rather than primary chronic insomnia |

> **Note:** No dedicated randomised trials of midazolam specifically for primary or chronic insomnia were identified in the current search. The trials above provide indirect or partial evidence only.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|---------|-------------|
| [6120704](https://pubmed.ncbi.nlm.nih.gov/6120704/) | 1981 | Dose-Finding RCT | Arzneimittel-Forschung | Oral midazolam 10–30 mg in 75 hospitalised patients with mild-to-moderate insomnia secondary to musculoskeletal disease; established optimal dose range and confirmed hypnotic efficacy with good tolerance |
| [6138072](https://pubmed.ncbi.nlm.nih.gov/6138072/) | 1983 | RCT | Br J Clin Pharmacol | Double-blind parallel study comparing midazolam 15 mg versus Vesparax in 30 female patients with insomnia secondary to neuromuscular disease; both agents were effective hypnotics, but midazolam showed superior tolerability and caused no hangover effect |
| [2121802](https://pubmed.ncbi.nlm.nih.gov/2121802/) | 1990 | RCT | J Clin Psychopharmacol | Randomised double-blind multicenter study comparing flurazepam and midazolam over 14 days in chronic insomniacs with a history of benzodiazepine use; assessed sleep, performance, and mood — introductory paper to a larger programme |
| [2229461](https://pubmed.ncbi.nlm.nih.gov/2229461/) | 1990 | Multicenter RCT | J Clin Psychopharmacol | Executive summary of the 14-day multicenter flurazepam vs midazolam trial in chronic insomniacs; directly evaluates midazolam as a hypnotic agent over a sustained treatment period |
| [2883820](https://pubmed.ncbi.nlm.nih.gov/2883820/) | 1986 | Review | Acta Psychiatr Scand Suppl | Narrative review of the clinical use of hypnotics including benzodiazepines; discusses the relationship between pharmacokinetic profile (including midazolam's short half-life) and hypnotic suitability across insomnia subtypes |
| [36615100](https://pubmed.ncbi.nlm.nih.gov/36615100/) | 2022 | Cohort Study | J Clin Med | Pilot study of lemborexant for insomnia in high-risk pancreato-biliary endoscopy patients; highlights that traditional benzodiazepine use for insomnia increases delirium risk, supporting the growing preference for non-benzodiazepine hypnotics in vulnerable populations |

---

## Denmark Market Information

Midazolam currently holds **no marketing authorisations** with the Danish Medicines Agency (Lægemiddelstyrelsen) and is **not marketed** in Denmark in any dosage form. It is not listed among centrally authorised (EMA) products approved for the Danish market.

> Healthcare professionals requiring access to midazolam in Denmark would need to apply for a special import permit (særlig tilladelse) under applicable Danish legislation, or consider whether a licensed comparator within the benzodiazepine or hypnotic class would be appropriate.

---

## Safety Considerations

Formal SmPC-level safety data (key warnings, contraindications, and drug interaction data) were not retrievable from the current evidence sources for this evaluation.

Please refer to the approved Summary of Product Characteristics (SmPC) for full safety information.

Based on well-established class-level knowledge of benzodiazepines relevant to clinical consideration:

- **Dependence and tolerance**: Benzodiazepines, including midazolam, carry a recognised risk of physical dependence, tolerance, and withdrawal syndrome with regular or prolonged use — particularly relevant if considering a chronic insomnia indication.
- **Rebound insomnia**: Midazolam's short half-life increases the likelihood of early-morning rebound insomnia and next-day anxious awakening compared to longer-acting benzodiazepines.
- **Respiratory depression**: Risk is heightened in combination with opioids, alcohol, or other CNS depressants, and in patients with obstructive sleep apnoea — a population with high comorbid insomnia prevalence.
- **Elderly patients**: Benzodiazepines are classified as potentially inappropriate medications in older adults (Beers Criteria) due to fall risk and cognitive impairment.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
While the mechanistic basis for midazolam's hypnotic effect is pharmacologically sound and older RCT literature confirms short-term efficacy in secondary insomnia, midazolam's short half-life, tolerance liability, dependence risk, and complete absence from the Danish market make it unsuitable for a formal insomnia repurposing programme in the current regulatory and clinical context. Established alternatives (Z-drugs, orexin receptor antagonists, melatonin agonists) already carry approved insomnia indications with more favourable safety profiles for chronic use.

**To proceed, the following would be needed:**

- **Regulatory pathway clarification**: Determine whether a new indication submission to EMA or Lægemiddelstyrelsen is technically feasible given the existing benzodiazepine regulatory landscape and current Danish prescribing guidelines.
- **Pharmacokinetic reformulation strategy**: Any viable path to a chronic insomnia indication would require either a modified-release oral formulation (to address rebound insomnia) or restriction to short-term or acute use only — both require dedicated pharmaceutical development and clinical data.
- **Full SmPC safety review**: Obtain and parse the complete midazolam SmPC (injectable and oral formulations) to perform a formal S1 safety gate assessment, currently blocked by the absence of Danish regulatory label data.
- **Chronic insomnia-specific RCT data**: The available clinical trials are primarily perioperative or acute in design; a prospective trial in primary chronic insomnia patients (DSM-5 criteria) with modern polysomnographic and patient-reported outcome endpoints would be required to support any label expansion.
- **Comparative effectiveness data**: Benchmark against currently approved first-line hypnotics (e.g., eszopiclone, lemborexant, daridorexant) to establish whether a clinical niche exists for midazolam in this indication.

---

> ⚠️ **Disclaimer:** This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before application. All content relating to midazolam's potential use in insomnia is investigational.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

