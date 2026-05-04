---
layout: default
title: Clonazepam
parent: 僅模型預測 (L5)
nav_order: 117
evidence_level: L5
indication_count: 6
---

# Clonazepam
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

# Clonazepam: From Epilepsy and Anxiety Disorders to Restless Legs Syndrome

## One-Sentence Summary

Clonazepam is a long-acting benzodiazepine internationally established as a first- or second-line treatment for epilepsy and panic disorder, currently holding **no marketing authorisation in Denmark**.
The TxGNN model predicts it may be effective for **Restless Legs Syndrome (RLS)** with a prediction score of **99.65%**,
supported by **0 registered clinical trials** but **20 publications** — including a 2025 AASM clinical practice guideline, a 2017 Cochrane systematic review, and a 2024 historical systematic review confirming that approximately 25% of treated RLS patients currently receive benzodiazepines.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Denmark; internationally used for epilepsy and panic disorder |
| Predicted New Indication | Restless Legs Syndrome (RLS) |
| TxGNN Prediction Score | 99.65% |
| Evidence Level | L3 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the Danish regulatory record. Based on established pharmacological knowledge, clonazepam belongs to the benzodiazepine drug class and acts as a positive allosteric modulator of GABA-A receptors, potentiating inhibitory neurotransmission throughout the central and peripheral nervous system. Its efficacy in epilepsy and anxiety is well-documented internationally.

The mechanistic rationale for restless legs syndrome is grounded in clonazepam's GABAergic activity at the spinal cord level. By enhancing GABA-A receptor function in spinal motor neurons and suppressing polysynaptic spinal reflex arcs, clonazepam can reduce the frequency and intensity of periodic limb movements during sleep (PLMS) — a hallmark co-occurring feature in the majority of RLS patients. Its long plasma half-life (18–50 hours) further supports uninterrupted nocturnal sleep maintenance, breaking the vicious cycle of sleep deprivation and worsened sensory discomfort that characterises severe RLS. Indirect modulation of dopaminergic circuits in subcortical motor pathways may provide an additional contributory mechanism, given that the dopamine system is the primary pathophysiological target in RLS.

From a clinical practice perspective, the evidence base is well-established historically. The 2024 historical systematic review by Walters et al. identified 17 published articles on clonazepam use specifically in RLS and PLMS, and the 2025 AASM clinical practice guideline formally includes benzodiazepines among recommended treatment options. The original condition (epilepsy/seizure suppression) and the new indication (RLS/PLMS suppression) share a common GABAergic substrate, lending strong biological plausibility to this repurposing prediction.

---

## Clinical Trial Evidence

No registered clinical trials evaluating clonazepam specifically for restless legs syndrome were identified at the time of data extraction (ClinicalTrials.gov and ICTRP search date: 2026-03-26).

> Currently no related clinical trials registered.

*Note: For the closely related second-ranked prediction (insomnia), 12 clinical trials were identified, including one multicenter Phase 4 RCT (NCT03977441, n=240) and one completed Phase 4 trial with direct clonazepam use (NCT00025740, n=78). This additional evidence strengthens the overall evidence package for clonazepam in sleep-related disorders.*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [39324694](https://pubmed.ncbi.nlm.nih.gov/39324694/) | 2025 | Clinical Guideline | J Clin Sleep Med | AASM clinical practice guideline for treatment of RLS and PLMD in adults and children; formally addresses benzodiazepine use |
| [38708125](https://pubmed.ncbi.nlm.nih.gov/38708125/) | 2024 | Historical Systematic Review | Tremor Other Hyperkinetic Mov | ~25% of 16,694 surveyed RLS patients receive benzodiazepines; 17 articles on clonazepam in RLS/PLMS comprehensively reviewed |
| [28319266](https://pubmed.ncbi.nlm.nih.gov/28319266/) | 2017 | Cochrane Systematic Review | Cochrane Database Syst Rev | Cochrane review of benzodiazepines for RLS; evaluates strength and limitations of evidence base for clonazepam |
| [36692194](https://pubmed.ncbi.nlm.nih.gov/36692194/) | 2023 | Systematic Review / Meta-Analysis | J Clin Sleep Med | Meta-analysis of pharmacological responsiveness of PLMS; quantifies drug category efficacy including benzodiazepines |
| [31942156](https://pubmed.ncbi.nlm.nih.gov/31942156/) | 2019 | Prospective Open-Label RCT | J Mid-Life Health | Direct comparison of clonazepam vs nortriptyline in women >40 years with RLS; provides comparative efficacy data |
| [11313161](https://pubmed.ncbi.nlm.nih.gov/11313161/) | 2001 | Placebo-Controlled Sleep Lab Study | Eur Neuropsychopharmacol | 1 mg clonazepam significantly improved objective polysomnographic and subjective sleep parameters in RLS/PLMD versus placebo |
| [6380197](https://pubmed.ncbi.nlm.nih.gov/6380197/) | 1984 | Randomised Double-Blind Crossover RCT | Acta Neurol Scand | Earliest RCT of clonazepam in RLS (n=6); significantly improved subjective sleep quality and leg dysaesthesia versus placebo; concluded clonazepam is safe and effective for RLS |
| [18925578](https://pubmed.ncbi.nlm.nih.gov/18925578/) | 2008 | Evidence-Based Review | Mov Disord | Movement Disorder Society task force evidence-based review of all RLS treatments; classifies therapeutic efficacy level of clonazepam |
| [24363103](https://pubmed.ncbi.nlm.nih.gov/24363103/) | 2014 | Narrative Review | Neurotherapeutics | Overview of evolving RLS treatment landscape across drug classes including benzodiazepines; summarises clinical positioning |
| [17876423](https://pubmed.ncbi.nlm.nih.gov/17876423/) | 2007 | Expert Consensus | Arq Neuropsiquiatr | Brazilian RLS Study Group consensus on diagnosis and management; addresses benzodiazepine use alongside Class I evidence-based agents |

---

## Denmark Market Information

Clonazepam currently holds **no marketing authorisation in Denmark**. No licences are registered with the Danish Medicines Agency (Lægemiddelstyrelsen), and the product is not commercially available through normal distribution channels.

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|-------------------------------|-------------|-------------|-------------------|
| — | — | — | No authorisations registered in Denmark |

*Clonazepam (e.g., Rivotril®) is authorised in numerous other European countries. Use in Denmark would require a named-patient or special-import application via Lægemiddelstyrelsen.*

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

> Safety data (key warnings, contraindications, and drug interactions) were not available in this evidence pack. Full safety review against the internationally approved SmPC is a prerequisite before any clinical application.

*Key areas of known clinical concern for benzodiazepines that should be reviewed in the SmPC include: physical dependence and withdrawal risk with prolonged use, respiratory depression (particularly in patients with sleep-disordered breathing), daytime sedation, cognitive impairment, and fall risk in elderly patients — all of which are especially relevant in the context of RLS, a chronic condition often requiring long-term pharmacotherapy.*

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple convergent sources — including a 2017 Cochrane systematic review, the 2025 AASM clinical practice guideline, and decades of controlled and observational studies — confirm that clonazepam has a well-established, biologically plausible, and clinically documented role in restless legs syndrome and periodic limb movement disorder; however, the absence of dedicated Phase 2/3 RCTs registered for this indication, the lack of a Danish marketing authorisation, and the unresolved safety data package require guardrails before clinical implementation.

**To proceed, the following is needed:**
- Obtain and review the full SmPC (Summary of Product Characteristics) from an authorised jurisdiction (e.g., EMA or a national European authority) — specifically sections on warnings, contraindications, and drug-drug interactions
- Complete mechanism of action (MOA) data retrieval from DrugBank (DB01068)
- Apply for named-patient or special import authorisation via the Danish Medicines Agency (Lægemiddelstyrelsen) if clinical use is planned
- Establish a structured monitoring plan covering: dependence assessment, daytime sedation, cognitive function (executive function impairment is documented in chronic insomnia patients on clonazepam), and fall risk — especially in elderly patients
- Define the clinical positioning of clonazepam relative to first-line RLS treatments registered in Denmark (dopamine agonists: pramipexole, ropinirole; alpha-2-delta ligands: pregabalin, gabapentin), to reserve clonazepam for adjunct or second-line use
- Plan for restricted treatment duration with scheduled re-evaluation to minimise chronic dependence risk in this long-term condition
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

