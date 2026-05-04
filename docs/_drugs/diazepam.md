---
layout: default
title: Diazepam
parent: 僅模型預測 (L5)
nav_order: 140
evidence_level: L5
indication_count: 10
---

# Diazepam
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

# Diazepam: From Anxiety and Seizure Disorders to Insomnia

## One-Sentence Summary

Diazepam (Valium) is a long-established benzodiazepine widely used clinically for anxiety disorders, epileptic seizures, and muscle spasms via positive allosteric modulation of GABA-A receptors. The TxGNN model predicts it may be effective for **Insomnia**, with a prediction score of **99.99%**, supported by **24 clinical trials** and **18 publications** in the evidence database — including at least one direct head-to-head randomised controlled trial comparing diazepam specifically for sleep disorders (PMID 6113175). However, given diazepam's well-known dependency risk and the availability of newer, safer hypnotics, clinical deployment requires careful patient selection and a structured safety monitoring plan.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Anxiety disorders, epilepsy, muscle spasms (established clinical use; not specified in current dataset) |
| Predicted New Indication | Insomnia (disease) |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L1 |
| Denmark Market Status | Not marketed (dataset shows 0 licences — verification with Lægemiddelstyrelsen recommended) |
| Number of Marketing Authorisations | 0 (per current dataset) |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Diazepam is a classic positive allosteric modulator (PAM) of the GABA-A receptor, binding at the benzodiazepine recognition site located between the α and γ subunits and amplifying chloride ion conductance in response to endogenous GABA. Of particular relevance to insomnia, the α1 subunit of the GABA-A receptor is the primary mediator of the sedative-hypnotic effects of benzodiazepines: α1-selective modulation reduces sleep-onset latency, increases stage N2 sleep duration, and stabilises sleep continuity. A 2024 systematic review in *Bioorganic Chemistry* (PMID 39581171) explicitly identifies diazepam as a prototypical GABA-A PAM with established therapeutic roles in epilepsy, anxiety, and insomnia.

The mechanistic connection between diazepam and insomnia is direct. Insomnia is characterised by insufficient GABAergic inhibition and hyperactivation of cortical-limbic and hypothalamic-brainstem arousal circuits. Diazepam counteracts this hyperarousal state by enhancing inhibitory tone, thereby lowering the cortical arousal threshold that prevents sleep initiation and maintenance. A 1981 double-blind, active-controlled RCT (PMID 6113175) directly validated this mechanism in 100 insomnia outpatients, comparing diazepam 5 mg to lormetazepam 1 mg over seven days; lormetazepam showed numerically superior sleep latency reduction, but both arms demonstrated clinically meaningful hypnotic effects. A 2025 meta-analysis in *Sleep* (PMID 40570297) further characterises how chronic benzodiazepine use remodels sleep architecture — increasing N2 sleep while reducing N3 slow-wave sleep and REM — confirming the pharmacodynamic basis for this indication.

A critical consideration is diazepam's long half-life (parent compound: 20–100 hours; active metabolite desmethyldiazepam: 36–200 hours), which predisposes patients to daytime residual sedation, psychomotor impairment, and accumulation with repeated dosing. Long-term use carries documented risks of tolerance, physical dependence, and cognitive decline. A 2022 translational study in *Nature Neuroscience* (PMID 35228700) demonstrated that prolonged diazepam treatment impairs dendritic spine structural plasticity and cognitive performance in mice through TSPO-mediated microglial engulfment of synaptic spines. Current European and Danish clinical guidelines accordingly recommend benzodiazepine use for insomnia only as short-term treatment (2–4 weeks maximum), and position newer agents — Z-drugs and dual orexin receptor antagonists such as lemborexant — as preferred options for longer-term management.

---

## Clinical Trial Evidence

The retrieved clinical trials focus predominantly on benzodiazepine-class management in insomnia (tapering, discontinuation, substitution) rather than direct efficacy trials for diazepam in insomnia. This reflects the current research landscape in which diazepam's acute hypnotic effect is taken as established, while research attention has shifted to safer long-term strategies.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02530580](https://clinicaltrials.gov/study/NCT02530580) | Phase 1 | Completed | 12 | Randomised, double-blind, placebo-controlled crossover biomarker study of selective GABA modulator AZD7325; benzodiazepines including diazepam/Valium cited as reference treatment for epilepsy, insomnia, and anxiety, with the new agent designed to avoid benzodiazepine side effects |
| [NCT04751851](https://clinicaltrials.gov/study/NCT04751851) | N/A | Completed | 128 | RCT comparing psychological support vs Acceptance and Commitment Therapy (ACT) within a structured benzodiazepine withdrawal programme for adults with hypnotic-dependent insomnia |
| [NCT04050176](https://clinicaltrials.gov/study/NCT04050176) | Phase 3 | Active, not recruiting | 260 | Randomised longitudinal trial evaluating blinded hypnotic tapering combined with therapist-delivered CBT-I to enhance benzodiazepine/Z-drug discontinuation rates in insomnia patients |
| [NCT03687086](https://clinicaltrials.gov/study/NCT03687086) | N/A | Completed | 188 | Novel multi-mechanism intervention to help older adults achieve and sustain discontinuation of benzodiazepine-class sleeping medications; targets both tapering and insomnia symptom management |
| [NCT02831894](https://clinicaltrials.gov/study/NCT02831894) | Phase 2 | Completed | 74 | Examines effect of tapering pace and individual patient traits on successful hypnotic discontinuation in treatment-seeking insomnia patients using benzodiazepines or benzodiazepine receptor agonists |
| [NCT02648776](https://clinicaltrials.gov/study/NCT02648776) | N/A | Unknown | 1,400 | Prospective cohort assessing medication use patterns, efficacy, safety, pharmacokinetics, and pharmacogenomics of hypnotics including benzodiazepines for sleep disorders in elderly patients; Taiwanese academic medical centre |
| [NCT03461042](https://clinicaltrials.gov/study/NCT03461042) | Phase 4 | Completed | 17 | Placebo-controlled multicentre RCT of ramelteon (melatonin receptor agonist) co-administered during dose reduction of BZD and non-BZD hypnotics in chronic insomnia patients |
| [NCT02281175](https://clinicaltrials.gov/study/NCT02281175) | N/A | Completed | 114 | RCT of a structured psychosocial intervention (PASSE-65+) designed to help older benzodiazepine users gradually taper; addresses anxiety, insomnia, and depression co-indications |
| [NCT05935553](https://clinicaltrials.gov/study/NCT05935553) | Phase 2/3 | Recruiting | 93 | Baclofen (GABA-B agonist) to facilitate benzodiazepine titration in benzodiazepine-dependent patients; diazepam serves as the background benzodiazepine against which baclofen augmentation is tested |
| [NCT07417813](https://clinicaltrials.gov/study/NCT07417813) | N/A | Recruiting | 121 | Prospective observational study of lemborexant (dual orexin receptor antagonist) for insomnia in patients with comorbid psychiatric disorders; provides contemporary comparative context for benzodiazepine alternatives |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [6113175](https://pubmed.ncbi.nlm.nih.gov/6113175/) | 1981 | RCT (active-controlled) | J Int Med Res | Direct 7-day double-blind RCT: diazepam 5 mg vs lormetazepam 1 mg in 100 insomnia outpatients; both demonstrated hypnotic efficacy; lormetazepam showed statistically superior reduction in sleep latency and prolongation of uninterrupted sleep duration |
| [39581171](https://pubmed.ncbi.nlm.nih.gov/39581171/) | 2024 | Systematic Review | Bioorganic Chemistry | Comprehensive review of small-molecule GABA-A receptor modulators for neurological disorders; diazepam explicitly reviewed as the prototypical benzodiazepine PAM used clinically for epilepsy, anxiety, insomnia, and depression; side effects of sedation and addiction noted |
| [35228700](https://pubmed.ncbi.nlm.nih.gov/35228700/) | 2022 | Translational Research | Nature Neuroscience | Long-term diazepam treatment causes microglial-mediated dendritic spine engulfment via TSPO, impairing structural synaptic plasticity and producing persistent cognitive impairment in mice; key mechanistic safety signal for chronic use |
| [6135990](https://pubmed.ncbi.nlm.nih.gov/6135990/) | 1983 | Authoritative Review | N Engl J Med | Landmark review of benzodiazepine pharmacology, clinical use, and risks; foundational reference establishing diazepam's role in anxiety and sleep disorders as well as concerns regarding tolerance and withdrawal |
| [40570297](https://pubmed.ncbi.nlm.nih.gov/40570297/) | 2025 | Meta-analysis / Systematic Review | Sleep | Chronic BZD/BZRA use disrupts NREM slow oscillations, sleep spindles, and spindle-SO coupling in older adults with chronic insomnia; confirms that benzodiazepines alter sleep architecture (increase N2, reduce N3 and REM) even while promoting sleep onset |
| [7595266](https://pubmed.ncbi.nlm.nih.gov/7595266/) | 1995 | Systematic Review | J Fam Pract | Systematic review of 10 clinical trials of benzodiazepines for insomnia in community-dwelling elderly; short-term sleep benefit demonstrated; no long-term efficacy data available; injury risk highlighted |
| [7525193](https://pubmed.ncbi.nlm.nih.gov/7525193/) | 1994 | Clinical Guidelines | Drugs | Evidence-based guidelines for rational benzodiazepine prescribing; benzodiazepines (including diazepam) indicated for transient and short-term insomnia; prescriptions should be limited to days to a few weeks; pharmacokinetic differences between agents discussed |
| [39374004](https://pubmed.ncbi.nlm.nih.gov/39374004/) | 2024 | RCT | JAMA Intern Med | Masked taper combined with augmented CBT-I enhances benzodiazepine receptor agonist discontinuation in insomnia patients; underscores that discontinuation — not initiation — is now the focus of clinical research |
| [6114852](https://pubmed.ncbi.nlm.nih.gov/6114852/) | 1981 | Review | Drugs | Comprehensive review of triazolam (short-acting benzodiazepine) for insomnia; explicitly contrasts it with longer-acting benzodiazepines including diazepam, flurazepam, and nitrazepam in terms of hypnotic suitability and residual effects |
| [40583063](https://pubmed.ncbi.nlm.nih.gov/40583063/) | 2025 | Clinical Study | Cell Mol Biol Lett | Long-term use of benzodiazepines (diazepam) and Z-drugs (zolpidem) associated with exacerbated breast cancer risk via GABA-A receptor modulation in clinical data; important long-term oncological safety signal requiring further investigation |

---

## Denmark Market Information

According to the current dataset, no marketing authorisations for Diazepam were identified in the Danish regulatory database, and market status is recorded as not marketed with zero registered licences.

> **Data quality note**: This result is inconsistent with established clinical practice. Diazepam-containing products (e.g., Stesolid® rectal tubes, Diazepam Desitin®) are known to be available in Denmark and have been in use for decades. The absence of registered licences in this dataset most likely reflects a gap in the data collection process for this evidence pack rather than true non-availability. Healthcare professionals should verify the current and complete marketing authorisation status directly with:
> - **Danish Medicines Agency (Lægemiddelstyrelsen):** [lmst.dk](https://laegemiddelstyrelsen.dk)
> - **EMA Product Authorisation Database:** [ema.europa.eu](https://www.ema.europa.eu)
> - **Product Resumé (Danish SmPC) database:** [produktresume.dk](https://produktresume.dk)

---

## Safety Considerations

Please refer to the approved Danish Summary of Product Characteristics (SmPC) for comprehensive safety information, as detailed warning and contraindication data were not available in this evidence pack.

Based on mechanistic evidence and retrieved literature, the following safety considerations are clinically relevant for the insomnia indication:

- **Dependence and withdrawal**: Diazepam carries a well-documented risk of physical and psychological dependence with use exceeding 2–4 weeks. Abrupt discontinuation after prolonged use may provoke a withdrawal syndrome including rebound insomnia, anxiety, tremor, and seizures. Gradual tapering is mandatory (PMID 6114793).
- **Cognitive impairment**: Both short-term (psychomotor) and long-term (structural synaptic) cognitive effects are established, including working memory impairment and increased dementia risk with prolonged use (PMID 35228700).
- **Residual sedation and falls**: Diazepam's exceptionally long half-life (parent compound plus active metabolite desmethyldiazepam) causes significant next-day sedation, particularly hazardous in elderly patients due to increased fall and fracture risk.
- **Long-term oncological signal**: A 2025 clinical study (PMID 40583063) reported an association between prolonged benzodiazepine/Z-drug use and exacerbated breast cancer risk; clinical significance is not yet established but warrants monitoring.
- **Drug interactions**: No DDI data were retrieved in this evidence pack. Clinically critical interactions are known with other CNS depressants (alcohol, opioids, antipsychotics), CYP3A4 inhibitors (e.g., azole antifungals, macrolides), and CYP3A4 inducers (e.g., rifampicin, carbamazepine). A dedicated DDI review is strongly recommended before clinical use.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Diazepam's GABA-A α1 modulation provides a well-characterised and direct pharmacological basis for hypnotic efficacy in insomnia, supported by a direct clinical RCT (PMID 6113175), multiple authoritative reviews, and decades of real-world clinical use. However, the risk-benefit profile in insomnia is unfavourable for long-term use compared with modern alternatives, and the dataset reveals important gaps in regulatory data and safety documentation that must be addressed before formal evaluation in the Danish context.

**To proceed, the following is needed:**

- **Regulatory verification**: Confirm current Danish marketing authorisation status and approved indications directly with Lægemiddelstyrelsen; determine whether insomnia is already an approved or established off-label indication in Denmark
- **SmPC retrieval**: Download and review the Danish-approved product information document to extract full warnings, contraindications, and dosing guidance
- **DDI assessment**: Repeat the drug interaction search using a structured clinical database (e.g., Drugs.com, Lexicomp, SFINX-PHARAO for Danish prescribers); diazepam has multiple clinically significant interactions
- **Patient selection criteria**: Define eligibility criteria restricting use to short-term treatment (≤4 weeks) in adults without prior history of substance dependence, respiratory compromise, or significant cognitive impairment
- **Monitoring protocol**: Establish a structured monitoring plan covering: sleep diary outcomes, Epworth Sleepiness Scale (daytime sedation), cognitive screening (e.g., MMSE or MoCA in elderly), and tapering plan from treatment initiation
- **Comparative positioning**: Evaluate whether a formal head-to-head comparison with first-line agents (CBT-I, lemborexant, or other orexin receptor antagonists) is needed to support clinical adoption, given current guidelines preferring these over benzodiazepines for chronic insomnia management

---

*This report is generated for research reference purposes only and does not constitute medical advice. Repurposing candidates require clinical validation before application. All content must be interpreted by qualified healthcare professionals in conjunction with full SmPC data and current clinical guidelines.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

