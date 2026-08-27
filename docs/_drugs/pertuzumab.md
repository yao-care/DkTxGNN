---
layout: default
title: Pertuzumab
parent: 僅模型預測 (L5)
nav_order: 348
evidence_level: L5
indication_count: 10
---

# Pertuzumab
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

Using the provided Evidence Pack, here is the completed evaluation report.

# Pertuzumab: From HER2-Positive Breast Cancer to Normal Breast-Like Subtype of Breast Carcinoma

## One-Sentence Summary

Pertuzumab (DrugBank DB06366) is a HER2-targeted monoclonal antibody with an established role in HER2-positive breast cancer treatment (in combination with trastuzumab and chemotherapy); this general indication is well known but is **not** present in this Evidence Pack's structured registry data, since Pertuzumab is currently **not marketed in Denmark**.
The TxGNN model predicts a possible extension to the **normal breast-like molecular subtype of breast carcinoma**, but this specific hypothesis is currently supported only by **6 clinical trials** (none of them subtype-specific) and **no dedicated literature**.
Within the same prediction set, closely related hypotheses — **PR-positive** and **PR-negative breast cancer** — carry substantially stronger evidence (L1, multiple completed Phase 3 RCTs) and should be considered alongside this candidate (see Conclusion).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HER2-positive breast cancer (established drug-class use; not present in Danish registry data — see Data Gap) |
| Predicted New Indication | Normal breast-like subtype of breast carcinoma |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L2 |
| Denmark Market Status | Not Marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Research Question |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack (Data Gap DG002, severity: High). Based on known pharmacological information, Pertuzumab is a recombinant humanized monoclonal antibody that binds the extracellular dimerization domain (subdomain II) of HER2, blocking HER2-HER3 heterodimerization and downstream PI3K/AKT signalling. It is used in combination with trastuzumab (and typically a taxane) for HER2-positive breast cancer, where its efficacy is well established.

"Normal breast-like" is one of the PAM50 intrinsic molecular subtypes of breast cancer, defined primarily by gene-expression profiling rather than by HER2 receptor status. None of the clinical trials retrieved for this candidate specifically enrolled patients by PAM50 subtype — they were designed around conventional HER2-positive breast cancer populations (e.g., biology-driven neoadjuvant selection studies), and the association with "normal breast-like" subtype is inferred only indirectly, through the overlap between "HER2-positive" and this molecular subtype. No dedicated literature was retrieved to support this specific link.

By contrast, within the same TxGNN prediction set for this drug, **progesterone-receptor (PR) positive and PR-negative breast cancer** carry much stronger, more direct supporting evidence, including completed Phase 3 randomized trials and a real-world cohort study (PMID 37723497) showing PR status modifies the magnitude of pertuzumab's neoadjuvant benefit. This suggests the receptor-status subtypes are mechanistically better substantiated hypotheses than the PAM50 "normal breast-like" subtype evaluated here (see Conclusion for details).

**Important caveat:** All rationale above assumes the tumor is HER2-positive. Confirmation of HER2-positive status is a prerequisite for any of these repurposing hypotheses, and this field is not available in the current Evidence Pack.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05900206](https://clinicaltrials.gov/study/NCT05900206) | Phase 2 | Recruiting | 370 | ARIADNE: compares trastuzumab deruxtecan to standard preoperative treatment in non-metastatic HER2-positive breast cancer, using biology-driven treatment selection; no results yet. |
| [NCT04329065](https://clinicaltrials.gov/study/NCT04329065) | Phase 2 | Recruiting | 25 | WOKVAC vaccine combined with neoadjuvant chemotherapy and HER2-targeted monoclonal antibody therapy; small exploratory immunotherapy study. |
| [NCT01796197](https://clinicaltrials.gov/study/NCT01796197) | Phase 2 | Completed | 23 | Paclitaxel + trastuzumab + pertuzumab as preoperative therapy for inflammatory breast cancer; regimen-relevant but not subtype-specific. |
| [NCT05582499](https://clinicaltrials.gov/study/NCT05582499) | Phase 2 | Recruiting | 716 | FASCINATE-N: precision neoadjuvant therapy platform based on clinical/molecular subtyping of operable breast cancer. |
| [NCT06348134](https://clinicaltrials.gov/study/NCT06348134) | Phase 2 | Recruiting | 74 | Efficacy/safety of optimal neoadjuvant-to-adjuvant anti-HER2 therapy in Nigerian women with HER2-positive breast cancer. |
| [NCT04750122](https://clinicaltrials.gov/study/NCT04750122) | Phase 1/2 | Recruiting | 46 | Neoadjuvant therapy guided by drug-screening in patient-derived tumor-cell clusters for HER2-positive early breast cancer. |

## Literature Evidence

Currently no related literature available for this specific predicted indication (normal breast-like subtype of breast carcinoma).

## Denmark Market Information

Pertuzumab currently has **no marketing authorisations on file in Denmark** (market status: Not Marketed; total licenses: 0). No product-level dosage form or approved-indication data is available from the Danish registry for this Evidence Pack.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (anti-HER2 monoclonal antibody; not a conventional cytotoxic agent) |
| Myelosuppression Risk | Please refer to the Summary of Product Characteristics (SmPC) warnings and precautions |
| Emetogenicity Classification | Please refer to the Summary of Product Characteristics (SmPC) warnings and precautions |
| Monitoring Items | Please refer to the Summary of Product Characteristics (SmPC) warnings and precautions |
| Handling Protection | Please refer to the Summary of Product Characteristics (SmPC) warnings and precautions |

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information. No key warnings, contraindications, or drug-drug interaction data are currently available in this Evidence Pack (DDI query status: not found).

**Note:** A Blocking-severity data gap has been identified — the Danish/EU product label (warnings and contraindications) has not yet been obtained (DG001), which prevents this candidate from entering the S1 safety pre-screening stage. This should be resolved before any further evaluation proceeds.

## Conclusion and Next Steps

**Decision: Research Question**

**Rationale:**
The "normal breast-like subtype" hypothesis is supported only by L2-level evidence — a single completed Phase 2 trial in a related but non-subtype-specific population, no dedicated literature, and no confirmed HER2-positive status for the target population. Combined with a Blocking-severity gap in safety labelling data, this candidate is not yet ready to advance beyond a research question.

Notably, within this same prediction batch, **PR-positive and PR-negative breast cancer** subtypes are supported by L1 evidence (≥2 completed Phase 3 RCTs, including IMpassion050 [NCT03726879] and the QL1209 biosimilar equivalence trial [NCT04629846]) and are already rated "Proceed with Guardrails." These related hypotheses represent a more evidence-mature repurposing opportunity for the same drug and disease area, and may warrant prioritized follow-up evaluation ahead of, or alongside, the normal breast-like subtype candidate.

**To proceed, the following is needed:**
- Danish/EU product label (SmPC) — warnings, contraindications, and DDI data (Blocking gap, DG001)
- Detailed mechanism of action confirmation from DrugBank (High-priority gap, DG002)
- Confirmation of HER2-positive status as an inclusion criterion for the target population
- Subtype-specific (PAM50 "normal breast-like") clinical trial or literature evidence, since current evidence is only indirectly applicable
- A parallel evaluation of the PR-positive/PR-negative breast cancer candidates from this same prediction set, given their stronger (L1) evidence base
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

