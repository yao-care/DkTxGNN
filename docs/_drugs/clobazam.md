---
layout: default
title: Clobazam
parent: 僅模型預測 (L5)
nav_order: 116
evidence_level: L5
indication_count: 10
---

# Clobazam
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

# Clobazam: From Epilepsy (Adjunctive Treatment) to Febrile Infection-Related Epilepsy Syndrome

## One-Sentence Summary

Clobazam is a 1,5-benzodiazepine with established antiepileptic use internationally (including as adjunctive therapy for Lennox-Gastaut syndrome), though it currently holds no marketing authorisation in Denmark.
The TxGNN model predicts it may be effective for **Febrile Infection-Related Epilepsy Syndrome (FIRES)**, with **0 clinical trials** and **2 publications** (involving related benzodiazepines, not Clobazam directly) currently available in the evidence base.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Denmark; internationally used as adjunctive antiepileptic treatment (including Lennox-Gastaut syndrome) |
| Predicted New Indication | Febrile Infection-Related Epilepsy Syndrome (FIRES) |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L5 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this evidence pack. Based on established pharmacological knowledge, Clobazam is a 1,5-benzodiazepine that acts as a positive allosteric modulator of GABA-A receptors, enhancing inhibitory neurotransmission in the central nervous system. Its proven efficacy in reducing seizure frequency — notably as adjunctive treatment for Lennox-Gastaut syndrome — reflects a broad-spectrum antiepileptic profile.

FIRES is a catastrophic, treatment-refractory form of new-onset refractory status epilepticus (NORSE) that predominantly affects previously healthy children following a febrile illness. Standard antiepileptic agents often fail, and clinicians frequently escalate to high-dose anaesthetics. Benzodiazepines — including intravenous midazolam — are a recognised part of acute FIRES management. The mechanistic rationale for Clobazam in FIRES rests on its GABA-A potentiation: enhancing cortical inhibitory tone may help suppress the intense, repetitive seizure discharges characteristic of this syndrome.

It must be emphasised, however, that the two publications retrieved do not directly evaluate Clobazam in FIRES. They describe the use of lorazepam (a related benzodiazepine) and perampanel (an AMPA receptor antagonist) — providing indirect, class-level contextual relevance but no direct efficacy or safety data for Clobazam in this specific indication.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [35770765](https://pubmed.ncbi.nlm.nih.gov/35770765/) | 2022 | Case Series | *Epileptic Disorders* | Enteral lorazepam (a benzodiazepine, not Clobazam) used as effective weaning substitute for midazolam-dependent FIRES patients; supports the broader benzodiazepine class utility in maintaining seizure control during FIRES recovery |
| [39958143](https://pubmed.ncbi.nlm.nih.gov/39958143/) | 2025 | Case Report | *Cureus* | Perampanel may reduce barbiturate dependency in a 13-year-old with FIRES; illustrates the refractory nature of FIRES and the ongoing need for alternative antiepileptic strategies beyond conventional anaesthetics |

> **Important note:** Neither publication directly studies Clobazam in FIRES. The evidence is indirect (benzodiazepine class or comparator context only) and does not support an evidence level above L5 for this specific drug–disease pair.

---

## Denmark Market Information

Clobazam currently holds **no marketing authorisation in Denmark** and is not listed in the Danish Medicines Agency (Lægemiddelstyrelsen) database.

> **Reference context:** Clobazam is authorised in other jurisdictions under brand names such as **Frisium®** (UK, Canada, and others) and **Onfi®** (USA, approved for adjunctive treatment of Lennox-Gastaut syndrome). For individual patients in Denmark, access may be possible via the named-patient or compassionate use pathways under Danish medicines regulations (§29–§30 of the Medicines Act).

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

> As no Danish SmPC exists, healthcare professionals should consult the EMA assessment reports or authorised SmPCs from the UK (MHRA), Canada (Health Canada), or the US (FDA) as the most appropriate reference documents. Key areas to review include sedation, dependence potential, respiratory depression, and drug–drug interactions (particularly with other CNS depressants).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No clinical trials and no direct Clobazam literature exist for FIRES, placing this prediction at evidence level L5 (model prediction only). Combined with the absence of any marketing authorisation in Denmark, there is currently insufficient evidence to support active clinical development or use.

**To proceed, the following is needed:**

- **Direct literature review**: Systematic search specifically for Clobazam (not generic benzodiazepine class) in FIRES, refractory status epilepticus, and NORSE
- **MOA documentation**: Retrieve full mechanism of action from DrugBank (DB00349) or published pharmacology sources
- **Safety data extraction**: Review international SmPCs (UK Frisium®, US Onfi®) to populate the key warnings, contraindications, and drug interaction sections
- **Regulatory pathway assessment**: Evaluate feasibility of named-patient access or hospital exemption in Denmark for a drug not currently marketed
- **Exploratory study design**: Given FIRES rarity and ethical constraints, consider a retrospective case series or international registry collaboration as the most pragmatic first step before any prospective trial
- **Duplicate prediction review**: The evidence pack contains duplicate entries for all predicted indications (ranks 1–2, 3–4, etc.); data pipeline deduplication is recommended before finalising further candidate prioritisation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

