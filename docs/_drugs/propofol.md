---
layout: default
title: Propofol
parent: 僅模型預測 (L5)
nav_order: 361
evidence_level: L5
indication_count: 10
---

# Propofol
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

# Propofol: From General Anesthesia to Migraine

## One-Sentence Summary

Propofol is a widely used intravenous general anesthetic and sedative agent, established for induction and maintenance of anesthesia and procedural sedation. The TxGNN model predicts it may be effective for **Migraine Disorder** (as an acute/rescue abortive agent), with **5 clinical trials** and **20 publications** currently supporting this direction — though the trial base is small, and one trial was terminated early.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | General anesthesia / procedural sedation (well-established clinical use; no Danish licence text is on file in this evidence pack) |
| Predicted New Indication | Migraine Disorder |
| TxGNN Prediction Score | 99.69% |
| Evidence Level | L2 |
| Denmark Market Status | Not Marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack. Based on known pharmacology, propofol is a short-acting GABA-A receptor agonist that produces central sedative, anxiolytic-like and anti-nociceptive effects. In its approved use, it induces and maintains general anesthesia.

Two independent lines of evidence support extending propofol into acute migraine management. First, at sub-anesthetic ("low") doses, propofol has been used off-label in emergency departments as a rescue therapy for refractory acute migraine — a practice already documented in retrospective and prospective series, particularly in pediatric populations. Second, mechanistic work indicates propofol suppresses cortical spreading depression (CSD), the electrophysiological event believed to underlie migraine aura, and may modulate central pain-sensitization pathways relevant to migraine chronification.

Together, this gives a plausible pharmacological rationale (CSD suppression, central sedation/analgesia) combined with an existing off-label clinical practice base, which is consistent with the TxGNN model's high prediction score for this indication.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01604785](https://clinicaltrials.gov/study/NCT01604785) | Phase 2/3 | Completed | 74 | Low-dose propofol as abortive therapy for pediatric migraine in the ED; retrospective experience suggested safety and possible superiority over standard treatment (Grade A relevance) |
| [NCT02492295](https://clinicaltrials.gov/study/NCT02492295) | N/A | Terminated | 12 | Low-dose propofol for severe refractory migraine in the ED; stopped early, small sample limits evidence strength (Grade B relevance) |
| [NCT02485418](https://clinicaltrials.gov/study/NCT02485418) | N/A | Completed | 40 | Low-dose propofol infusion as an abortive treatment for pediatric migraine; evaluated efficacy, safe dosing limits, and duration of effect (Grade A relevance) |
| [NCT03789370](https://clinicaltrials.gov/study/NCT03789370) | N/A | Unknown | 130 | Compared sevoflurane vs. propofol anesthesia maintenance and postoperative headache incidence; only indirectly related to migraine treatment (Grade C relevance) |
| [NCT02443220](https://clinicaltrials.gov/study/NCT02443220) | N/A | Completed | 315 | Electroacupuncture study in cardiac surgery patients; not propofol-related, likely a knowledge-graph matching artifact (Grade C relevance) |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35402989](https://pubmed.ncbi.nlm.nih.gov/35402989/) | 2022 | RCT | Archives of Academic Emergency Medicine | Double-blind RCT comparing propofol+granisetron vs. propofol+metoclopramide for acute migraine symptom management |
| [29456086](https://pubmed.ncbi.nlm.nih.gov/29456086/) | 2018 | RCT | The Journal of Emergency Medicine | Prospective RCT of low-dose propofol for pediatric migraine, suggesting efficacy with a favorable side-effect profile |
| [35573713](https://pubmed.ncbi.nlm.nih.gov/35573713/) | 2022 | RCT | Archives of Academic Emergency Medicine | RCT comparing sumatriptan alone vs. sumatriptan+propofol combination for acute migraine |
| [41321235](https://pubmed.ncbi.nlm.nih.gov/41321235/) | 2026 | Review | Headache | 2025 American Headache Society guideline update on parenteral pharmacotherapies for acute migraine in the ED |
| [31621134](https://pubmed.ncbi.nlm.nih.gov/31621134/) | 2020 | Review | Academic Emergency Medicine | Systematic review of propofol safety and efficacy for acute migraine treatment in the ED |
| [27454834](https://pubmed.ncbi.nlm.nih.gov/27454834/) | 2016 | Cohort | Expert Review of Neurotherapeutics | Drug-profile review of sub-anesthetic propofol for super-refractory migraine headaches |
| [32638172](https://pubmed.ncbi.nlm.nih.gov/32638172/) | 2020 | Review | Current Pain and Headache Reports | Review of intravenous migraine treatment options in children and adolescents |
| [32410204](https://pubmed.ncbi.nlm.nih.gov/32410204/) | 2020 | Review | Current Neurology and Neuroscience Reports | Review of ED and inpatient headache management in children and adolescents |
| [32705803](https://pubmed.ncbi.nlm.nih.gov/32705803/) | 2020 | Review | Emergency Medicine Australasia | Editorial/commentary questioning whether propofol should be used for migraine despite feasibility |
| [22309235](https://pubmed.ncbi.nlm.nih.gov/22309235/) | 2012 | Review | Headache | Part 2 of a rescue-therapy series covering neuroleptics, antihistamines, and other agents including propofol |

---

## Denmark Market Information

No marketing authorisation is currently on file for propofol in Denmark within this evidence pack (0 licences; market status: Not Marketed).

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
There is an existing off-label clinical practice base plus multiple RCTs and a systematic review supporting low-dose propofol for acute migraine, but the trial base is small (largest n=74, one trial terminated early), and no Phase 3 confirmatory data exist — consistent with the L2 evidence level.

**To proceed, the following is needed:**
- TFDA/SmPC warnings and contraindications (currently blocking S1 safety pre-assessment — DG001)
- Detailed mechanism of action (MOA) data from DrugBank (DG002)
- Larger, adequately powered RCTs confirming efficacy and dosing safety beyond the pediatric ED setting
- Clarification of the causal direction behind anesthesia-induced coronary vasospasm (Prinzmetal angina) signals seen elsewhere in the TxGNN output for propofol, to rule out confounding safety concerns before any use expansion
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

