---
layout: default
title: Levetiracetam
parent: 僅模型預測 (L5)
nav_order: 262
evidence_level: L5
indication_count: 10
---

# Levetiracetam
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

# Levetiracetam: From Epilepsy to Visual Epilepsy

## One-Sentence Summary

Levetiracetam is a second-generation antiseizure medication, historically established for epilepsy and seizure disorders (marketed internationally as Keppra®).
The TxGNN model predicts it may also be effective for **Visual Epilepsy**, a photosensitive reflex-epilepsy subtype,
with **9 clinical trials** and **20 publications** currently associated with this candidate — though most of this evidence addresses levetiracetam in epilepsy/seizures broadly rather than visual epilepsy specifically.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Epilepsy / seizure disorders (general knowledge — not present as a structured field in the evidence pack; see note below) |
| Predicted New Indication | Visual Epilepsy |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L2 |
| Denmark Market Status | Not Marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed structured mechanism-of-action data is not available in DrugBank for this candidate (flagged as a data gap, DG002). However, the collected literature itself describes the mechanism: levetiracetam is a "new generation antiseizure medication which binds to synaptic vesicle protein SV2A and inhibits the release of neurotransmitters" (PMID 35848684), and earlier work similarly describes it as binding synaptic vesicle protein 2A (SV2A) to modulate neurotransmitter release (PMID 34903423). This SV2A-binding mechanism underlies its broad anticonvulsant activity across seizure types.

Visual epilepsy (photosensitive/reflex epilepsy triggered by visual stimuli) is mechanistically a subtype of the broader epilepsy spectrum that levetiracetam already treats. The evidence pack for this candidate is dominated by trials and publications on levetiracetam across other seizure contexts — traumatic brain injury, intracerebral haemorrhage, neonatal seizures, status epilepticus, and idiopathic generalized epilepsy — rather than visual/photosensitive epilepsy specifically. This supports a plausible mechanistic rationale (an established anticonvulsant extending to a related seizure phenotype) but **direct evidence for visual epilepsy itself is currently limited**; it is not yet backed by trials or publications diagnosing or targeting this specific reflex-epilepsy subtype.

Because the original indication is not populated as a structured field in this evidence pack, the "original indication" above is stated from general drug knowledge (consistent with how mechanism-of-action gaps are handled) rather than sourced data — this should be confirmed against the formal record before use.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04573803](https://clinicaltrials.gov/study/NCT04573803) | Phase 3 | Not yet recruiting | 1649 | MAST trial — optimal duration/choice (phenytoin vs levetiracetam) of anti-epileptic drugs after traumatic brain injury |
| [NCT00855738](https://clinicaltrials.gov/study/NCT00855738) | Phase 4 | Completed | 111 | Liceo study — observational assessment of newer AEDs (incl. levetiracetam) as first bitherapy in focal epilepsy |
| [NCT07336992](https://clinicaltrials.gov/study/NCT07336992) | Phase 3 | Not yet recruiting | 580 | Prophylactic levetiracetam for functional outcome in acute intracerebral haemorrhage (RCT, placebo-controlled) |
| [NCT03107507](https://clinicaltrials.gov/study/NCT03107507) | Phase 4 | Unknown | 40 | Efficacy of levetiracetam in control of neonatal seizures |
| [NCT04833907](https://clinicaltrials.gov/study/NCT04833907) | Phase 1/2 | Enrolling by invitation | 24 | AVASPA gene therapy trial in Canavan disease (levetiracetam relevance unclear from summary) |
| [NCT00105040](https://clinicaltrials.gov/study/NCT00105040) | Phase 2 | Completed | 87 | Randomized, double-blind, placebo-controlled safety study of cognitive/neuropsychological effects of adjunctive levetiracetam in children with refractory partial seizures |
| [NCT04559529](https://clinicaltrials.gov/study/NCT04559529) | Phase 2 | Completed | 62 | Levetiracetam's effect on hippocampal hyperactivity in psychosis (fMRI study) |
| [NCT04277936](https://clinicaltrials.gov/study/NCT04277936) | Phase 2 | Terminated | 1 | Levetiracetam's effect on hippocampal hyperactivity in psychosis (terminated early) |
| [NCT00203216](https://clinicaltrials.gov/study/NCT00203216) | N/A | Completed | 31 | Open-label trial of levetiracetam (Keppra®) for prophylactic treatment of migraine, with/without visual aura |

No trial in this set is registered specifically for "visual epilepsy"; relevance grading for all listed trials is still marked "pending" in the source data.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35963261](https://pubmed.ncbi.nlm.nih.gov/35963261/) | 2022 | RCT (Phase 3) | The Lancet Neurology | PEACH trial — prophylactic levetiracetam did not show clear benefit preventing acute seizures after intracerebral haemorrhage |
| [32385134](https://pubmed.ncbi.nlm.nih.gov/32385134/) | 2020 | RCT | Pediatrics | Levetiracetam vs phenobarbital for neonatal seizures |
| [38678766](https://pubmed.ncbi.nlm.nih.gov/38678766/) | 2024 | RCT | Seizure | Open-label RCT of phenytoin vs levetiracetam for acute symptomatic seizures in children with acute encephalitis syndrome |
| [30487494](https://pubmed.ncbi.nlm.nih.gov/30487494/) | 2018 | RCT | Mymensingh Medical Journal | RCT of phenobarbital vs levetiracetam in childhood epilepsy |
| [34286461](https://pubmed.ncbi.nlm.nih.gov/34286461/) | 2022 | Systematic Review/Meta-analysis | Neurocritical Care | Levetiracetam for seizure prophylaxis in neurocritical care (ICH, TBI, SAH, post-neurosurgery) |
| [38316735](https://pubmed.ncbi.nlm.nih.gov/38316735/) | 2024 | Clinical Practice Guideline | Neurocritical Care | Guideline on seizure prophylaxis in adults hospitalized with moderate-severe TBI |
| [36209676](https://pubmed.ncbi.nlm.nih.gov/36209676/) | 2022 | Systematic Review/Network Meta-analysis | Seizure | Comparative effectiveness of treatments for benzodiazepine-resistant status epilepticus |
| [37378757](https://pubmed.ncbi.nlm.nih.gov/37378757/) | 2023 | Systematic Review/Network Meta-analysis | Journal of Neurology | Efficacy/safety of antiseizure medications for idiopathic generalized epilepsies |
| [40450767](https://pubmed.ncbi.nlm.nih.gov/40450767/) | 2025 | Systematic Review/Meta-analysis | Epilepsy & Behavior | Levetiracetam for myoclonic seizures in idiopathic generalized epilepsy (incl. JME) |
| [21936590](https://pubmed.ncbi.nlm.nih.gov/21936590/) | 2011 | Review | CNS Drugs | "Spotlight on levetiracetam in epilepsy" — overview of approved indications and pharmacology |

None of the top publications are specific to "visual epilepsy"; the closest directly relevant evidence for reflex/photosensitive epilepsy subtypes appears under other TxGNN-predicted candidates in this same pack (e.g., startle epilepsy, audiogenic seizures), not under this indication's own evidence set.

---

## Denmark Market Information

Levetiracetam currently has **no registered marketing authorisation** in this evidence pack (`market_status: 未上市 / Not Marketed`, `total_licenses: 0`). This appears inconsistent with levetiracetam's well-established international marketing status (e.g., as Keppra®), so this record should be verified directly against the Laegemiddelstyrelsen (Danish Medicines Agency) product register before relying on it.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information. No structured warnings, contraindications, or drug-interaction data were returned for this candidate (DDI query status: not found), and this data gap is flagged as **Blocking** for safety pre-assessment (DG001).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
A Blocking data gap exists — no TFDA/SmPC-equivalent warnings or contraindications are available, which prevents any safety pre-assessment (S1). In addition, Denmark shows zero marketing authorisations on file (a status that itself warrants verification), and the evidence collected for "visual epilepsy" specifically is thin — most trials/publications address levetiracetam in epilepsy or seizure contexts broadly, not this reflex-epilepsy subtype.

**To proceed, the following is needed:**
- Danish/EU SmPC or labeling data (warnings, contraindications, DDI) to clear the Blocking data gap (DG001)
- Structured DrugBank MOA confirmation (DG002) — current MOA description is derived from literature abstracts, not a structured source
- Verification of Denmark market/licensing status against the Laegemiddelstyrelsen registry (data pack shows 0 licenses, which is unexpected for a long-established antiepileptic)
- Trial/literature evidence specifically targeting visual epilepsy or photosensitive reflex epilepsy, rather than epilepsy/seizures generally
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

