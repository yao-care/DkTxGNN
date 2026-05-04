---
layout: default
title: Baclofen
parent: 僅模型預測 (L5)
nav_order: 54
evidence_level: L5
indication_count: 4
---

# Baclofen
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Baclofen: From Spasticity to Attention Deficit-Hyperactivity Disorder

## One-Sentence Summary

Baclofen is a GABA-B receptor agonist established internationally for the treatment of muscle spasticity, though it currently holds no marketing authorisation in Denmark.
The TxGNN model predicts it may be effective for **Attention Deficit-Hyperactivity Disorder (ADHD)**, supported by **10 publications** but **no registered clinical trials** directly evaluating this indication.
A secondary prediction of **Nicotine Dependence** carries substantially stronger evidence, with **3 Phase 2 clinical trials** and **20 publications**, and merits parallel consideration.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Denmark; globally used for muscle spasticity (e.g., spinal cord injury, multiple sclerosis) |
| Predicted New Indication | Attention Deficit-Hyperactivity Disorder (ADHD) |
| TxGNN Prediction Score | 99.32% |
| Evidence Level | L4 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Baclofen acts as a selective agonist at GABA-B receptors, activating both presynaptic and postsynaptic receptor subtypes to reduce neuronal excitability. In its established role as a muscle relaxant, this mechanism suppresses excessive motor neuron firing in spasticity. The theoretical connection to ADHD rests on baclofen's ability to modulate GABAergic tone in the prefrontal cortex — a region critically implicated in the attention dysregulation and impulse control deficits that define ADHD — where it may indirectly dampen aberrant dopaminergic and noradrenergic signalling.

Two lines of preclinical evidence provide some mechanistic plausibility. First, studies in the spontaneously hypertensive rat (SHR), the most widely accepted ADHD animal model, have demonstrated that GABAergic agonists alter cortical and hippocampal EEG activity in ways that parallel ADHD-relevant neurophysiology (PMID 21300040). Second, there is precedent for GABAergic modulation improving impulsive decision-making — a core ADHD symptom — through shared prefrontal circuitry (PMID 24062084). Clinically, baclofen has been used in children with Tourette syndrome (which carries a high rate of ADHD comorbidity), with one clinical series of 450 patients reporting symptom reduction as assessed by the Yale Global Tic Severity Scale (PMID 10342599).

However, the mechanistic link to ADHD remains indirect. Baclofen has not been formally studied in ADHD populations in registered clinical trials, and its effects on prefrontal dopaminergic systems are substantially less characterised than those of established ADHD pharmacotherapies (methylphenidate, atomoxetine, guanfacine). The TxGNN score of 99.32% reflects knowledge graph topology rather than established clinical efficacy.

---

## Clinical Trial Evidence

**ADHD indication:** Currently no related clinical trials registered.

---

> **Secondary Prediction — Nicotine Dependence (TxGNN Score: 99.19%, Evidence Level: L2)**
>
> The TxGNN model's second-ranked unique prediction, nicotine dependence, is supported by a mechanistically coherent rationale and three registered Phase 2 trials. Baclofen inhibits mesolimbic dopamine release via GABA-B receptors in the ventral tegmental area (VTA) → nucleus accumbens pathway — the same reward circuit that nicotine hijacks to maintain dependence. This mechanism mirrors baclofen's established (and in France, approved) use in alcohol use disorder. The clinical trials below assess this indication directly.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT01821560](https://clinicaltrials.gov/study/NCT01821560) | Phase 2 | Completed | 44 | fMRI and behavioural assessment of baclofen's effects on brain and behavioural responses to smoking cues in cigarette smokers; the only completed Phase 2 trial — provides proof-of-concept clinical data for this indication |
| [NCT00257894](https://clinicaltrials.gov/study/NCT00257894) | Phase 2 | Terminated | 41 | Evaluated baclofen for reducing smoking urge, withdrawal, and reinforcement in moderate-to-heavy smokers; early termination reasons (funding vs. futility vs. safety) require confirmation before interpreting the data |
| [NCT01228994](https://clinicaltrials.gov/study/NCT01228994) | Phase 2 | Terminated | 6 | Randomised placebo-controlled trial directly testing the GABAergic hypothesis of nicotine dependence; recruitment halted after only 6 participants — negligible statistical power, though the study design has conceptual validity |

---

## Literature Evidence

The following publications relate to the **ADHD** indication (predicted_indications[0]). Studies are ordered by study design strength and direct relevance to baclofen in ADHD-related conditions.

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [35345730](https://pubmed.ncbi.nlm.nih.gov/35345730/) | 2022 | Systematic Review / Meta-analysis | Cureus | Systematic review of behavioural interventions, antipsychotics, and alpha-agonists for tic disorders in Tourette's syndrome; ADHD is a prevalent comorbidity in this population |
| [10342599](https://pubmed.ncbi.nlm.nih.gov/10342599/) | 1999 | Review | Journal of Child Neurology | Clinical series of 450 patients with tics/Tourette's treated with baclofen or botulinum toxin; tic severity rated by Yale Global Tic Severity Scale — the most direct existing clinical evidence for baclofen in a TS/ADHD-overlapping population |
| [26366961](https://pubmed.ncbi.nlm.nih.gov/26366961/) | 2015 | Review | Clinical Neuropharmacology | Mood stabilisers in children and adolescents with autism spectrum disorders; covers attention and behavioural symptom management including ADHD comorbidity |
| [24295630](https://pubmed.ncbi.nlm.nih.gov/24295630/) | 2013 | Review | International Review of Neurobiology | Emerging treatment strategies in Tourette syndrome; discusses ADHD comorbidity and the pharmacological pipeline for combined TS-ADHD management |
| [11393328](https://pubmed.ncbi.nlm.nih.gov/11393328/) | 2001 | Review | Paediatric Drugs | Clinical characteristics and pharmacotherapy strategies in Tourette syndrome, including use of clonidine and mentions of baclofen for tic suppression |
| [24062084](https://pubmed.ncbi.nlm.nih.gov/24062084/) | 2014 | Animal Study | Psychopharmacology | Noradrenergic α2A-receptor stimulation in the ventral hippocampus reduces impulsive decision-making in rats — mechanistic relevance to the impulsivity dimension of ADHD |
| [21300040](https://pubmed.ncbi.nlm.nih.gov/21300040/) | 2011 | Animal Study | Brain Research | Cortical and hippocampal EEG effects of neurotransmitter agonists in SHR (validated ADHD model) vs. kainate-treated rats; GABAergic agonists alter EEG activity patterns in the ADHD model |
| [24496320](https://pubmed.ncbi.nlm.nih.gov/24496320/) | 2014 | Animal Study | Neuropsychopharmacology | Dissociable contributions of anterior cingulate cortex and basolateral amygdala in cost-benefit effort decision-making; relevant to the motivational and cognitive-effort deficits seen in ADHD |
| [30122296](https://pubmed.ncbi.nlm.nih.gov/30122296/) | 2019 | Review / Clinical Guidance | L'Encéphale | Supervised off-label prescribing of methylphenidate in adult ADHD; contextualises the regulatory and clinical landscape for off-label treatments in adult ADHD — relevant background for any baclofen repurposing pathway |
| [24103016](https://pubmed.ncbi.nlm.nih.gov/24103016/) | 2013 | Animal Study | European Journal of Neuroscience | Habenular modulation of monoaminergic neurotransmission and social play behaviour in rats; indirect relevance to ADHD neurobiology and monoaminergic circuitry |

---

## Denmark Market Information

Baclofen currently holds **no marketing authorisations with the Danish Medicines Agency (Laegemiddelstyrelsen)** and is not marketed in Denmark.

Any clinical use in Denmark would require an individual patient exemption or a named-patient supply arrangement. For pharmacological reference, baclofen is nationally authorised in several EU member states (e.g., Germany, France, the United Kingdom pre-Brexit) for muscle spasticity, and France has additionally granted authorisation for alcohol use disorder at high doses (≥180 mg/day). No EMA centralised marketing authorisation exists for baclofen. Healthcare professionals in Denmark seeking to prescribe baclofen should consult the relevant national SmPC from an authorised country and follow Laegemiddelstyrelsen's procedures for import of non-authorised medicinal products.

---

## Safety Considerations

No Denmark-specific safety data is available in the current evidence pack.

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information — in particular, the SmPC from a country where baclofen holds national authorisation (e.g., Germany or France). Key areas to review include CNS depression and sedation, risk of abrupt withdrawal (which can cause seizures and hallucinations), renal dose adjustment requirements, and interactions with other CNS depressants.

---

## Conclusion and Next Steps

**Decision: Hold** (ADHD indication)

**Rationale:**
All available evidence for baclofen in ADHD is indirect — derived from animal models, Tourette syndrome case series with ADHD comorbidity, and mechanistic inference — with no Phase 1 or Phase 2 clinical trial data in ADHD patients. An L4 evidence base is insufficient to support clinical use, off-label prescribing, or programme investment without foundational human data.

**To proceed, the following is needed:**
- A dedicated Phase 2 proof-of-concept trial in an ADHD patient population (children or adults), evaluating standardised ADHD endpoints (e.g., ADHD Rating Scale, CAARS, CPT performance)
- Pharmacodynamic characterisation of baclofen's effects on prefrontal dopaminergic and noradrenergic activity in humans, to confirm or refute the theoretical mechanistic link
- Comprehensive safety review using the SmPC from a relevant EU national authorisation, with particular attention to CNS sedation and withdrawal risk in a paediatric or adult ADHD population
- A regulatory opinion from Laegemiddelstyrelsen on the pathway for clinical investigation or named-patient use in Denmark
- **Priority reassessment**: the nicotine dependence indication (L2, one completed Phase 2 trial, mechanistically well-grounded) may represent a more immediately actionable repurposing opportunity and warrants a separate evaluation report

---

*This report is intended for research and evaluation purposes only. Predictions from the TxGNN model require clinical validation before any therapeutic application. This document does not constitute medical advice.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

