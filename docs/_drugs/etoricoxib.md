---
layout: default
title: Etoricoxib
parent: 僅模型預測 (L5)
nav_order: 181
evidence_level: L5
indication_count: 10
---

# Etoricoxib
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

# Etoricoxib: From Pain and Inflammation to Migraine Disorder

## One-Sentence Summary

Etoricoxib is a selective COX-2 inhibitor widely used internationally for the treatment of osteoarthritis, rheumatoid arthritis, ankylosing spondylitis, and acute gouty arthritis. The TxGNN model predicts it may be effective for **Migraine Disorder**, with **0 clinical trials** and **0 publications** directly captured in this dataset — although published RCTs of etoricoxib 120 mg for acute migraine are known to exist outside the current evidence collection. Currently, no marketing authorisations for etoricoxib are registered in the dataset for Denmark.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Osteoarthritis, rheumatoid arthritis, ankylosing spondylitis, acute gouty arthritis, chronic musculoskeletal pain (based on known international approvals; no local licence data in dataset) |
| Predicted New Indication | Migraine Disorder |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L4 (published RCT evidence exists outside dataset) |
| Denmark Market Status | Not marketed (per dataset) |
| Number of Marketing Authorisations | 0 (per dataset) |
| Recommended Decision | Hold |

> **Note on market status:** Etoricoxib (Arcoxia®) holds a centralised EMA marketing authorisation (EU/1/08/470) and is available in multiple EU member states. The "not marketed" status in this report reflects the current dataset scope and should be verified against the Laegemiddelstyrelsen and EMA registers.

---

## Why is This Prediction Reasonable?

Etoricoxib is a highly selective cyclooxygenase-2 (COX-2) inhibitor. COX-2-mediated prostaglandin synthesis — particularly PGE2 and PGI2 — plays a key role in the activation of the trigeminovascular system and neurogenic inflammation, both of which are central to migraine pathophysiology. By selectively inhibiting COX-2, etoricoxib can reduce prostaglandin-driven dural vasodilation and trigeminal sensitisation, the two principal drivers of migraine pain.

Non-selective NSAIDs (ibuprofen, naproxen, aspirin) are already established as Level A evidence-based options for acute migraine treatment according to the American Headache Society (AHS) and European Headache Federation (EHF) guidelines. Etoricoxib's COX-2 selectivity offers a theoretical advantage over non-selective NSAIDs: equivalent or superior anti-inflammatory and analgesic effects in the trigeminovascular system with a reduced risk of gastrointestinal adverse effects from COX-1 inhibition.

Importantly, the repurposing rationale notes that at least one published RCT evaluating etoricoxib 120 mg for acute migraine exists in the literature but was not captured by the current evidence collection pipeline. This suggests the evidence gap is partly a data-collection artefact rather than a true absence of clinical data, and the mechanistic rationale is well-supported by the established role of the NSAID class in migraine management.

---

## Clinical Trial Evidence

Currently no related clinical trials registered in this dataset for the combination of etoricoxib and migraine disorder.

> **Data completeness note:** The repurposing rationale identifies that published RCT data for etoricoxib 120 mg in acute migraine exists but was not retrieved. A supplementary search of ClinicalTrials.gov and the EU Clinical Trials Register (EudraCT) is recommended.

---

## Literature Evidence

Currently no directly relevant literature captured in this dataset for etoricoxib in migraine disorder.

The literature retrieved for the related indication "migraine with or without aura, susceptibility to" consists primarily of epilepsy genetics and epileptogenesis studies. Only one publication has partial relevance:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33856647](https://pubmed.ncbi.nlm.nih.gov/33856647/) | 2021 | Narrative Review | Molecular Neurobiology | Reviews shared genetic and molecular mechanisms between epilepsy and migraine, including ion channel variants and neuroinflammatory pathways; discusses potential for shared therapeutic strategies |

> **Data quality note:** The remaining 19 retrieved publications relate to epilepsy susceptibility genetics and are not relevant to etoricoxib's potential use in migraine. The PubMed search likely matched on the term "susceptibility" rather than migraine-specific content. A targeted re-search using terms such as "etoricoxib AND migraine" or "COX-2 inhibitor AND migraine" is strongly recommended.

---

## Denmark Market Information

No marketing authorisations recorded in the current dataset.

> **Important:** Etoricoxib is marketed in the EU under the centralised procedure. The EMA-authorised product **Arcoxia®** (MSD) is available in film-coated tablet formulations (30 mg, 60 mg, 90 mg, 120 mg) for osteoarthritis, rheumatoid arthritis, ankylosing spondylitis, acute gouty arthritis, and short-term dental surgery pain. Availability in Denmark should be confirmed with Laegemiddelstyrelsen or the EMA Community Register of medicinal products.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

> **Known class-level concerns for COX-2 selective inhibitors (for reference):**
> - Cardiovascular risk: COX-2 inhibitors as a class carry warnings regarding increased risk of thrombotic cardiovascular events (myocardial infarction, stroke), particularly with prolonged use and in patients with pre-existing cardiovascular disease.
> - Gastrointestinal: Although lower GI risk than non-selective NSAIDs, GI perforation, ulceration, and bleeding remain possible.
> - Renal: Potential for fluid retention, oedema, and renal impairment.
> - Hepatic: Liver function monitoring may be warranted.
> - Hypertension: Dose-dependent increases in blood pressure have been reported.
>
> *These points are based on general COX-2 inhibitor class information. Prescribers must consult the current Arcoxia® SmPC for complete, product-specific safety data.*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction score is very high (99.90%), and the mechanistic rationale for etoricoxib in migraine is well-founded — NSAIDs as a class are already guideline-recommended for acute migraine, and COX-2 selectivity offers a plausible advantage. However, the current evidence pack contains no clinical trials or directly relevant literature, and critical data gaps exist for MOA details, SmPC safety information, and local market registration. The repurposing rationale itself notes that published RCT data for etoricoxib 120 mg in acute migraine was not captured, indicating a significant evidence-collection gap that must be resolved before a decision to proceed.

**To proceed, the following is needed:**
- **Supplementary evidence search**: Targeted PubMed and ClinicalTrials.gov/EudraCT search for "etoricoxib AND migraine" to capture the known published RCT(s)
- **SmPC safety review**: Obtain and review the current Arcoxia® SmPC for contraindications, warnings, and drug interactions relevant to migraine patients
- **Denmark market verification**: Confirm current availability and reimbursement status of etoricoxib in Denmark via Laegemiddelstyrelsen/EMA registers
- **Cardiovascular risk assessment**: Given that migraine (particularly migraine with aura) is itself associated with increased cardiovascular risk, a specific risk–benefit analysis for COX-2 inhibitor use in this population is essential
- **Dose–indication alignment**: The existing RCT used 120 mg (the highest approved dose, typically reserved for acute gout); evaluate whether this dose is appropriate or if lower doses could be effective for migraine
- **Mechanism of action data**: Retrieve detailed MOA data from DrugBank to support mechanistic linkage analysis

---

*Disclaimer: This report is for research purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before application. Data cutoff: 2026-04-05.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

