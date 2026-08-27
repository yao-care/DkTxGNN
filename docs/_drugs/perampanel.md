---
layout: default
title: Perampanel
parent: 僅模型預測 (L5)
nav_order: 345
evidence_level: L5
indication_count: 10
---

# Perampanel
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

Using the drug-repurposing evaluation report format, here is the report generated strictly from the supplied Evidence Pack.

---

# Perampanel: From Epilepsy (Focal & Generalized Seizures) to Visual Epilepsy

## One-Sentence Summary

> Perampanel (DrugBank DB08883) is a well-established antiseizure medication, already used internationally to treat focal-onset and primary generalized tonic-clonic seizures in epilepsy.
> The TxGNN model predicts it may also be effective for **Visual Epilepsy**, a reflex-epilepsy subtype triggered by visual stimuli,
> with **3 clinical trials** and **20 publications** currently linked to this candidate — though none of them study visual epilepsy specifically.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in Danish regulatory data (no licenses on file). Per the literature in this evidence pack, perampanel is internationally approved as adjunctive/monotherapy for focal-onset seizures (with or without secondary generalization) and as adjunctive therapy for primary generalized tonic-clonic seizures (PMID 24559052) |
| Predicted New Indication | Visual Epilepsy |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L2 |
| Denmark Market Status | Not marketed (未上市) |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from DrugBank (flagged as data gap DG002, severity High). However, the clinical literature included in this evidence pack consistently describes perampanel as a **selective, non-competitive antagonist of AMPA (α-amino-3-hydroxy-5-methyl-4-isoxazolepropionic acid) glutamate receptors** (PMID 36150304, 24559052, 21635236). By blocking AMPA-receptor-mediated postsynaptic excitation, perampanel dampens the cortical hyperexcitability that underlies seizure generation — the basis for its approval in over 35 countries as an antiseizure medication (ASM) for focal-onset seizures and primary generalized tonic-clonic seizures (PMID 24559052).

Visual epilepsy is a subtype of **reflex epilepsy**, in which seizures are triggered by specific visual stimuli (e.g., flickering light, contrast patterns). Because the seizure-generating mechanism in reflex epilepsies — excessive glutamatergic (AMPA-mediated) cortical excitation — overlaps mechanistically with focal and generalized epilepsy, it is biologically plausible that an AMPA-receptor antagonist already proven effective in epilepsy would also suppress seizures triggered by visual stimuli. This is reinforced by the fact that TxGNN generated closely related predictions for several other reflex/situational epilepsy subtypes in the same run (audiogenic seizures, startle epilepsy, eating seizures, micturition-induced seizures, thinking seizures, orgasm-induced seizures), consistent with a class-level mechanistic effect rather than a disease-specific signal.

It should be noted that none of the clinical trials or publications currently linked to this candidate specifically studied "visual epilepsy" as a defined clinical entity — the underlying evidence concerns perampanel's use in epilepsy broadly (partial-onset and generalized seizures, EEG/neurophysiology effects, pediatric and adult populations). The mechanistic rationale is therefore considerably stronger than the direct clinical evidence for this specific reflex-epilepsy subtype.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03780907](https://clinicaltrials.gov/study/NCT03780907) | Phase 2 | Completed | 18 | Randomised, double-blind, placebo-controlled study of tolerability, safety and pharmacokinetics of perampanel (E2007) in patients with refractory partial or generalised seizures on concomitant AED therapy |
| [NCT02900755](https://clinicaltrials.gov/study/NCT02900755) | Phase 4 | Completed | 30 | Evaluated cognition and EEG effects of perampanel as adjunctive treatment for refractory partial-onset seizures |
| [NCT03653741](https://clinicaltrials.gov/study/NCT03653741) | Phase 4 | Completed | 12 | Assessed perampanel's effects on EEG, somatosensory/brainstem auditory/visual evoked potentials in healthy volunteers, to determine whether it confounds standard neurophysiology testing |

*None of the above trials specifically enrolled patients with visual/photosensitive reflex epilepsy; all concern epilepsy in general.*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36206645](https://pubmed.ncbi.nlm.nih.gov/36206645/) | 2022 | Systematic Review & Meta-analysis (RCTs) | Seizure | Pooled efficacy and safety of perampanel in epilepsy across randomised controlled trials |
| [36878742](https://pubmed.ncbi.nlm.nih.gov/36878742/) | 2023 | Systematic Review & Meta-analysis | Brain & Development | Efficacy, tolerability and safety of perampanel in children and adolescents with epilepsy |
| [25878177](https://pubmed.ncbi.nlm.nih.gov/25878177/) | 2015 | Pooled Phase 3 RCT analysis | Neurology | Impact of concomitant enzyme-inducing AEDs on perampanel efficacy/safety across the three pivotal Phase 3 trials |
| [24559052](https://pubmed.ncbi.nlm.nih.gov/24559052/) | 2014 | Review | Expert Opinion on Drug Discovery | Discovery and development of perampanel; describes AMPA-receptor antagonist mechanism and approval history |
| [36150304](https://pubmed.ncbi.nlm.nih.gov/36150304/) | 2022 | Review (Clinical Trial & Real-World Evidence) | Epilepsy & Behavior | Summarizes perampanel monotherapy efficacy across trial and real-world data |
| [29898971](https://pubmed.ncbi.nlm.nih.gov/29898971/) | 2018 | Practice Guideline | Neurology | AAN/AES guideline update on efficacy/tolerability of newer AEDs (including perampanel) for new-onset epilepsy |
| [26111428](https://pubmed.ncbi.nlm.nih.gov/26111428/) | 2015 | Review | Expert Opinion on Drug Metabolism & Toxicology | Pharmacokinetic and pharmacodynamic evaluation of perampanel for partial-onset seizures |
| [37378757](https://pubmed.ncbi.nlm.nih.gov/37378757/) | 2023 | Systematic Review & Network Meta-analysis | Journal of Neurology | Compares antiseizure medications, including perampanel, for idiopathic generalized epilepsies |
| [37684052](https://pubmed.ncbi.nlm.nih.gov/37684052/) | 2023 | Review | BMJ | Management of epilepsy (including AED safety profiles) during pregnancy and lactation |
| [41043235](https://pubmed.ncbi.nlm.nih.gov/41043235/) | 2025 | Prospective Multicenter Study | Epilepsy & Behavior | Evaluated perampanel's effect on seizure control and sleep quality in people with epilepsy |

*10 of 20 available publications shown, prioritized by evidence quality (systematic reviews/meta-analyses and pooled Phase 3 data first). None specifically address visual/photosensitive epilepsy.*

---

## Denmark Market Information

No marketing authorisation records are present in the Evidence Pack for Denmark — `taiwan_regulatory.total_licenses = 0` and the license list is empty, with market status recorded as **Not marketed (未上市)**.

This warrants verification: the literature in this evidence pack states perampanel is "approved in over 35 countries... including the members of the European Union" (PMID 24559052), which would ordinarily include Denmark via EMA centralised authorisation. The absence of any Danish license record should therefore be treated as a possible **data collection gap** rather than confirmed non-availability, and should be re-verified directly against the Laegemiddelstyrelsen and EMA registers before final decision-making.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

No key warnings, contraindications, or drug-drug interaction data are available in this evidence pack:
- `safety.key_warnings` and `safety.contraindications` contain only "[Data Gap]" placeholders.
- The DDI query for PERAMPANEL returned `not_found` (0 interactions retrieved).
- This is registered as **DG001 (Blocking severity)** in the evidence pack: the missing SmPC warnings/contraindications data explicitly blocks entry into S1 safety pre-assessment.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- DG001 is a **Blocking**-severity data gap — TFDA/Danish SmPC warnings and contraindications are unavailable, which by definition prevents safety pre-assessment (S1) from proceeding.
- No marketing authorisation is currently on file for Denmark (0 licenses), and this status itself needs reconciliation against the drug's known broad international approval.
- While the AMPA-receptor-antagonist mechanism gives strong mechanistic plausibility for reflex epilepsy subtypes, **no trial or publication in the evidence pack specifically studies visual epilepsy** — all available evidence concerns epilepsy in general, so the clinical evidence base for this specific indication remains indirect.

**To proceed, the following is needed:**
- Resolve DG001: obtain and parse the approved SmPC (warnings, precautions, contraindications) from TFDA/Laegemiddelstyrelsen or EMA
- Resolve DG002: confirm mechanism of action via DrugBank API query
- Reconcile the "not marketed / 0 licenses" status in Denmark against perampanel's known EU-wide (EMA) approval as Fycompa
- Re-run the DDI query (current status: not_found) to obtain a usable interaction profile
- Seek or commission case series/trials specifically addressing perampanel in visual or other reflex-epilepsy subtypes, since current evidence supports epilepsy broadly but not this indication specifically
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

