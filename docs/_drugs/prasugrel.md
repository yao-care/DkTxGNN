---
layout: default
title: Prasugrel
parent: 僅模型預測 (L5)
nav_order: 356
evidence_level: L5
indication_count: 10
---

# Prasugrel
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

# Prasugrel: From Antiplatelet Therapy (ACS/PCI) to Pulmonary Hypertension

## One-Sentence Summary

Prasugrel is a thienopyridine P2Y12 inhibitor; the evidence in this pack identifies it as an antiplatelet agent used alongside aspirin after percutaneous coronary intervention (PCI) in acute coronary syndrome (ACS) patients. The TxGNN model predicts it may be effective for **Pulmonary Hypertension**, but this direction is currently supported only by **2 clinical trials** and **2 publications**, none of which directly evaluate prasugrel in pulmonary hypertension — the link is model-driven, not evidence-driven.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in Danish licensing data (drug is not marketed); literature in this pack describes established use as dual antiplatelet therapy (with aspirin) following PCI in acute coronary syndrome |
| Predicted New Indication | Pulmonary Hypertension |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L5 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for prasugrel in this evidence pack. Based on known information, prasugrel is part of the thienopyridine class of P2Y12 platelet inhibitors, and its efficacy as antiplatelet therapy following PCI in acute coronary syndrome is well established in the cited literature; mechanistically, this class could in theory extend to conditions with a thrombotic component.

For pulmonary hypertension specifically, there is no established direct mechanistic link. The theoretical rationale is that antiplatelet agents might reduce microthrombus formation implicated in chronic thromboembolic pulmonary hypertension (CTEPH), but this connection is speculative. Neither of the two associated clinical trials (an observational NOAC-management study in atrial fibrillation, and a retrospective cancer-associated thrombosis eligibility study) nor the two associated publications (a clopidogrel/prasugrel adherence study in ACS, and a COVID-19 comorbidity registry analysis) were designed to evaluate prasugrel in pulmonary hypertension. All four were surfaced by the TxGNN score alone, not by direct evidentiary support.

For context, this evidence pack also contains a lower-ranked but mechanistically better-supported candidate — migraine disorder (L3, decision stage S1) — where thienopyridine-class antiplatelet agents and the P2Y12 inhibitor ticagrelor have documented symptom benefit in patent foramen ovale (PFO)-associated migraine. That signal, while still class-level rather than prasugrel-specific, is stronger than the pulmonary hypertension signal presented here.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03993119](https://clinicaltrials.gov/study/NCT03993119) | N/A | Completed | 500 | Observational, cross-sectional study describing NOAC management in elderly Spanish patients with non-valvular atrial fibrillation; not a prasugrel or pulmonary hypertension study |
| [NCT04846556](https://clinicaltrials.gov/study/NCT04846556) | N/A | Completed | 300 | Retrospective study on the proportion of cancer-associated thrombosis patients ineligible for the CARAVAGGIO trial; not a drug intervention or pulmonary hypertension study |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21241206](https://pubmed.ncbi.nlm.nih.gov/21241206/) | 2011 | Cohort | Current Medical Research and Opinion | Evaluates factors associated with clopidogrel/prasugrel use and adherence after PCI in ACS patients; does not address pulmonary hypertension |
| [34713782](https://pubmed.ncbi.nlm.nih.gov/34713782/) | 2021 | Cohort/Observational | Kardiologiia | Analyzes background cardiovascular drug therapy and COVID-19 outcomes in the ACTIV registry; does not address prasugrel or pulmonary hypertension specifically |

---

## Denmark Market Information

Prasugrel is not currently marketed in Denmark. No national (Laegemiddelstyrelsen) or centralised (EMA) marketing authorisations are on record in this evidence pack (0 licenses).

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The TxGNN prediction score is high, but no clinical trial or publication in this pack directly evaluates prasugrel in pulmonary hypertension; the mechanistic link (antiplatelet effect on CTEPH microthrombosis) is speculative and unconfirmed. Combined with the drug's non-marketed status in Denmark, this does not meet the bar for further development at this time.

**To proceed, the following is needed:**
- TFDA/Danish SmPC label warnings and contraindications (currently a blocking data gap — required before any safety pre-assessment)
- Confirmed mechanism of action (MOA) data from DrugBank or equivalent source
- Preclinical or mechanistic studies specifically linking P2Y12 inhibition to pulmonary hypertension (particularly CTEPH subtype)
- A defined regulatory pathway, since prasugrel currently holds no marketing authorisation in Denmark
- Consideration of the migraine disorder candidate (L3 evidence) as a comparatively stronger repurposing lead for further investigation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

