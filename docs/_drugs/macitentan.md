---
layout: default
title: Macitentan
parent: 僅模型預測 (L5)
nav_order: 275
evidence_level: L5
indication_count: 10
---

# Macitentan
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

# Macitentan: From Pulmonary Arterial Hypertension to PAH Associated with Congenital Heart Disease

## One-Sentence Summary

> Macitentan is a dual endothelin receptor antagonist (ERA), originally developed and approved for pulmonary arterial hypertension (PAH, WHO Group 1).
> The TxGNN model predicts continued benefit in **Pulmonary Arterial Hypertension Associated with Congenital Heart Disease (CHD-PAH)**, a recognized WHO Group 1 subtype,
> with **2 clinical trials** and **18 publications** currently supporting this direction — including a completed Phase III RCT (MAESTRO) in the Eisenmenger syndrome subgroup.

*Note: TxGNN generated several other candidate indications for macitentan (e.g. pulmonary arteriovenous malformation, schistosomiasis-associated PAH). Those carry no clinical trial or literature support (Evidence Level L5, decision stage S0, recommendation "Hold") and are not covered below. This report focuses on the best-evidenced candidate, CHD-PAH.*

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pulmonary arterial hypertension (WHO Group 1) — per international labeling context in the evidence pack; no Danish marketing authorisation on file |
| Predicted New Indication | Pulmonary Arterial Hypertension Associated with Congenital Heart Disease (CHD-PAH) |
| TxGNN Prediction Score | 98.75% |
| Evidence Level | L2 (1 completed Phase III RCT — MAESTRO, in Eisenmenger syndrome) |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

A formal DrugBank mechanism-of-action record has not yet been retrieved for this candidate (flagged as data gap DG002). Based on the clinical evidence assembled in this pack, macitentan is established as a **dual endothelin receptor antagonist (ERA)**, blocking ET-1-mediated pulmonary vasoconstriction and vascular remodeling — the core pathophysiology of WHO Group 1 pulmonary arterial hypertension.

CHD-PAH (including Eisenmenger syndrome) is itself classified under WHO Group 1 PAH, sharing the same vascular remodeling pathology as idiopathic/heritable PAH — macitentan's original indication. This is therefore not a mechanistic extrapolation across disease categories, but an indication-class expansion within the same approved pharmacological target.

This is directly supported by clinical data: the Phase III, double-blind, randomized, placebo-controlled **MAESTRO study** (PMID 30586694) evaluated macitentan specifically in Eisenmenger syndrome, a CHD-PAH subtype, and multiple real-world cohorts (OPUS/OrPHeUS, Asian post-marketing surveillance, pediatric multicenter series) report consistent safety and effectiveness in CHD-PAH populations already receiving macitentan off-label or under expanded indications elsewhere.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05731492](https://clinicaltrials.gov/study/NCT05731492) | Phase 1 | Withdrawn | 0 | Planned PK/safety study of macitentan and its active metabolite (aprocitentan) in children aged 1 month to <2 years with PAH; withdrawn with no participants enrolled |
| [NCT05179876](https://clinicaltrials.gov/study/NCT05179876) | Phase 3 | Recruiting | 280 | Open-label long-term follow-up platform study allowing PAH patients (multiple etiologies, including CHD) to continue study intervention after parent-trial closure; assesses long-term safety |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30586694](https://pubmed.ncbi.nlm.nih.gov/30586694/) | 2019 | RCT (Phase III, MAESTRO) | Circulation | Multicenter, double-blind, randomized, placebo-controlled 16-week trial of macitentan in Eisenmenger syndrome (CHD-PAH subtype) |
| [39585521](https://pubmed.ncbi.nlm.nih.gov/39585521/) | 2024 | Real-World/Retrospective | Cardiology and Therapy | OPUS/OrPHeUS real-world data on patients with CHD-PAH newly initiating macitentan |
| [40616677](https://pubmed.ncbi.nlm.nih.gov/40616677/) | 2026 | Cohort (multicenter) | Pediatric Cardiology | Multicenter experience of oral macitentan in pediatric PAH (Spanish Registry), safety and efficacy outcomes |
| [36329372](https://pubmed.ncbi.nlm.nih.gov/36329372/) | 2023 | Real-World/Retrospective | Drugs - Real World Outcomes | Prospective multicenter post-marketing surveillance of macitentan safety/outcomes in Asian PAH patients |
| [36196862](https://pubmed.ncbi.nlm.nih.gov/36196862/) | 2022 | Cohort | Anatolian Journal of Cardiology | Single-center comparison of macitentan efficacy/safety across idiopathic and CHD-associated PAH |
| [35514768](https://pubmed.ncbi.nlm.nih.gov/35514768/) | 2022 | Prospective Cohort | Pulmonary Circulation | POTENT study: prospective assessment of PAH patients switched from bosentan to macitentan |
| [28867027](https://pubmed.ncbi.nlm.nih.gov/28867027/) | 2017 | Cohort | Heart, Lung & Circulation | Macitentan use in PAH associated with congenital heart defects |
| [38276220](https://pubmed.ncbi.nlm.nih.gov/38276220/) | 2023 | Review | Journal of Personalized Medicine | Current management and future directions for PAH-CHD |
| [31096477](https://pubmed.ncbi.nlm.nih.gov/31096477/) | 2019 | Systematic Review/Meta-analysis | Medicine | Position of PAH-specific drug therapy in Eisenmenger syndrome |
| [30545978](https://pubmed.ncbi.nlm.nih.gov/30545978/) | 2019 | Review | European Respiratory Journal | Updated definition, classification, diagnostics and management of paediatric PAH |

---

## Denmark Market Information

Currently no marketing authorisation is on file for Denmark. Macitentan's market status in this evidence pack is recorded as **Not marketed**, with 0 registered licences (national Laegemiddelstyrelsen or centralised EMA).

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information. Key warnings, contraindications, and drug-drug interaction data are not yet available in this evidence pack (data gap DG001, flagged **Blocking** — required before this candidate can proceed past the initial safety screening stage).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
- Mechanistic fit is direct (same WHO Group 1 PAH pathology and ERA target as the original indication), and is corroborated by a completed Phase III RCT (MAESTRO, Eisenmenger syndrome) plus multiple real-world cohorts (Evidence Level L2). However, a blocking safety data gap (DG001 — TFDA/local label warnings and contraindications) prevents a full "Go" decision.

**To proceed, the following is needed:**
- Danish/EU SmPC warnings, contraindications, and drug-drug interaction data (resolves DG001, blocking)
- Confirmed DrugBank mechanism-of-action record (resolves DG002)
- Formal review of whether Denmark market entry (currently "Not marketed") is planned or required before this indication can be pursued locally
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

