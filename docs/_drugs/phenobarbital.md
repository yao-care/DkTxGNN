---
layout: default
title: Phenobarbital
parent: 僅模型預測 (L5)
nav_order: 349
evidence_level: L5
indication_count: 10
---

# Phenobarbital
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

Using no specific slash-skill here — this is a direct report-authoring task governed entirely by the prompt's own template/rules, so I'll follow those instructions directly rather than invoke an unrelated skill.

One important note before the report: the Evidence Pack's own `repurposing_rationale` for the #1-ranked prediction explicitly flags itself as a likely **knowledge-graph mapping artifact** (the cited literature is about Sturge-Weber syndrome, not a trigeminal nerve tumour). Per the "no guessing / must state uncertainty" discipline, I've kept "Trigeminal Nerve Neoplasm" as the headline prediction (as the template's field-extraction rule requires: `predicted_indications[0]`), but made this caveat explicit throughout rather than presenting the 99.96% score at face value. I also added one supplementary section (not in the mandated list, but not prohibited either) summarizing the other unique candidate diseases in the pack, since 9 of the 10 entries are duplicates or near-duplicates of just 6 distinct diseases — omitting them would understate what evidence actually exists.

---

# Phenobarbital: From Epilepsy to Trigeminal Nerve Neoplasm

## One-Sentence Summary

Phenobarbital is a barbiturate historically used to treat epilepsy, seizure disorders, and as a sedative-hypnotic.
The TxGNN model's top-ranked prediction is **Trigeminal Nerve Neoplasm** (score **99.96%**), but the single supporting publication actually describes an unrelated condition (Sturge-Weber syndrome), which strongly suggests this specific prediction is a **knowledge-graph mapping artifact rather than a genuine drug-disease signal**.
Other lower-score candidates in the same batch (e.g., audiogenic seizures, startle epilepsy) are mechanistically more plausible but supported only by preclinical/animal studies or isolated case reports.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Epilepsy / seizure disorders (incl. neonatal seizures), sedation — based on established pharmacological classification; no structured registry record was returned for this field |
| Predicted New Indication | Trigeminal Nerve Neoplasm |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L5 (model prediction only; supporting literature does not match the disease) |
| Denmark Market Status | Not Marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

A structured mechanism-of-action (MOA) record was not available for this drug in the current data pull (data gap, High severity). Based on established pharmacology captured elsewhere in this evidence pack, phenobarbital is a positive allosteric modulator of the GABA‑A receptor, producing central nervous system depression and anticonvulsant activity, and it is also a known hepatic CYP450 enzyme inducer. There is no established antineoplastic or anti-neural-tumour mechanism associated with this drug class.

The relationship between the original indication (epilepsy/seizure control) and the predicted new indication (trigeminal nerve neoplasm) is not pharmacologically coherent. The only literature citation returned for this prediction (PMID 9157801) is a case series of **Sturge-Weber syndrome** — a neurocutaneous vascular malformation syndrome presenting with a facial port-wine stain in the trigeminal nerve distribution combined with seizures — which is a fundamentally different clinical entity from a "trigeminal nerve neoplasm." This mismatch is most consistent with a disease-ontology mapping error inside the knowledge graph (the trigeminal-distribution feature of Sturge-Weber syndrome appears to have been mapped onto a neoplasm-related disease node).

Given this, the 99.96% TxGNN score for this specific prediction should be treated with caution: it most likely reflects a mapping defect rather than a genuine pharmacological association, and should not be advanced without first correcting or re-verifying the underlying disease-node mapping.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9157801](https://pubmed.ncbi.nlm.nih.gov/9157801/) | 1997 | Case Series | Anales españoles de pediatría | Reviews 14 cases of **Sturge-Weber syndrome** — a vascular malformation/seizure syndrome, not a trigeminal nerve tumour. The disease mismatch is the basis for suspecting a knowledge-graph mapping error underlying this prediction. |

---

## Additional Predicted Indications in This Batch (Lower Priority, Not Yet Formally Scored)

The evidence pack contained ten ranked predictions collapsing to six distinct candidate diseases (several ranks are duplicate entries for the same disease). These are not analyzed in detail here but are noted for completeness, since some carry more plausible mechanistic rationale than the headline prediction above:

| Predicted Indication | TxGNN Score | Evidence Level | Recommendation | Note |
|---|---|---|---|---|
| Trigeminal Nerve Neoplasm | 99.96% | L5 | Hold | Likely KG mapping artifact (see above) |
| Audiogenic Seizures | 99.96% | L3 | Research Question | GABAergic mechanism plausible; evidence is almost entirely preclinical/animal (DBA/2 mouse models); only 1 human case report |
| Thinking Seizures | 99.96% | L3 | Research Question | A reflex-epilepsy subtype; evidence is indirect (general neonatal seizure guidelines/RCTs), no study targets this subtype specifically |
| Micturition-Induced Seizures | 99.96% | L4 | Hold | Purely indirect extrapolation from general antiepileptic evidence; no direct study identified |
| Startle Epilepsy / Hyperekplexia | 99.96% | L4 | Research Question | Most mechanistically coherent candidate — linked to GABA/glycine receptor pathophysiology — but supported only by case reports/genetic studies, no phenobarbital-specific study |
| Eating Seizures | 99.96% | L4 | Hold | Supported only by a single 50-year case follow-up report |

All six candidates share the same TxGNN score band (~99.96%), which suggests the model is scoring these as a cluster of "seizure-type" disease nodes rather than discriminating meaningfully between them — a further reason for caution before treating any single score as strong evidence.

---

## Denmark Market Information

Phenobarbital currently holds **no marketing authorisation in Denmark** (0 licenses on file; market status: Not Marketed). No national (Laegemiddelstyrelsen) or centralised (EMA) authorisation records were returned in this data pull.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information. No structured warnings, contraindications, or drug-drug interaction data were available in the current evidence pack (DDI query returned no results).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The headline prediction (trigeminal nerve neoplasm) has no plausible mechanistic basis, and its only supporting citation describes an unrelated syndrome — indicating a likely knowledge-graph mapping error rather than a genuine drug-disease signal.
- Phenobarbital is not marketed in Denmark (0 authorisations), and a **Blocking**-severity data gap exists for SmPC-level warnings/contraindications, which by itself prevents any safety pre-screening (Stage S1) regardless of the indication being considered.
- The mechanistically more credible alternative candidates in this batch (audiogenic seizures, startle epilepsy) are supported only by preclinical or case-report-level evidence (L3–L4) and are not yet ready to progress past a research question.

**To proceed, the following is needed:**
- Verify and, if necessary, correct the TxGNN disease-node mapping responsible for the "trigeminal nerve neoplasm" prediction (likely conflated with Sturge-Weber syndrome)
- Obtain the approved SmPC (warnings, contraindications) from the Danish Medicines Agency or an equivalent EMA reference product, to close the Blocking-severity data gap
- Obtain a confirmed mechanism-of-action record from DrugBank
- If pursuing the reflex-epilepsy candidates (audiogenic seizures, startle epilepsy), commission a targeted literature review to check for any human clinical evidence beyond case reports
- Given the drug's non-marketed status in Denmark, assess feasibility of a named-patient/import pathway before further evaluation investment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

