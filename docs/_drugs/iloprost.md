---
layout: default
title: Iloprost
parent: 僅模型預測 (L5)
nav_order: 225
evidence_level: L5
indication_count: 10
---

# Iloprost
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

# Iloprost: From Pulmonary Arterial Hypertension to HIV-Associated Pulmonary Arterial Hypertension

## One-Sentence Summary

Iloprost is a synthetic prostacyclin (prostanoid) analogue originally used to treat pulmonary arterial hypertension (PAH). Across the candidate indications evaluated in this evidence pack, the TxGNN model's highest-confidence prediction with actual supporting evidence points to **HIV-associated pulmonary arterial hypertension**, backed by **1 completed Phase 3 randomised controlled trial (n=64)** and **4 supporting publications**. Note that the model's single *highest-scoring* prediction overall (hypotrichosis simplex of the scalp) has **zero clinical trials and zero literature support** and is flagged in the underlying analysis as likely knowledge-graph noise rather than a genuine signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pulmonary Arterial Hypertension (WHO Group 1, primary/idiopathic) — inferred from repurposing rationale text; not confirmed via Danish licensing data (see Denmark Market Information) |
| Predicted New Indication | HIV-Associated Pulmonary Arterial Hypertension |
| TxGNN Prediction Score | 99.21% |
| Evidence Level | L1 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Candidate Indications Considered

This evidence pack evaluated multiple predicted indications for iloprost. For transparency, all distinct candidates are summarised below (duplicate KG/DL entries collapsed):

| Disease | TxGNN Score | Evidence Level | Decision Stage | Recommendation |
|---------|------------|-----------------|-----------------|-----------------|
| HIV-associated PAH | 99.21% | L1 | S3 | Proceed with Guardrails |
| PAH associated with connective tissue disease | 99.21% | L3 | S2 | Research Question |
| PAH associated with congenital heart disease | 99.32% | L3 | S2 | Research Question |
| Pulmonary arteriovenous malformation | 99.31% | L4 | S0 | Hold |
| Congenital hypotrichosis milia | 99.33% | L5 | S0 | Hold |
| Hypotrichosis simplex of the scalp | 99.45% | L5 | S0 | Hold |

The two hypotrichosis-related predictions carry the *highest* raw TxGNN scores but have no mechanistic plausibility, no trials, and no literature — the underlying analysis explicitly attributes this to embedding noise on rare-disease nodes. This report therefore focuses on **HIV-associated PAH**, the candidate with the strongest actual clinical evidence.

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for iloprost is not available in this evidence pack (data gap, DrugBank query pending resolution). Based on the information available, iloprost is a prostacyclin (IP receptor agonist) analogue whose pharmacology produces pulmonary vasodilation and inhibition of platelet aggregation/vascular smooth-muscle proliferation. It is an established treatment for primary (idiopathic) PAH.

HIV-associated PAH is classified, together with idiopathic PAH, under WHO Group 1 pulmonary arterial hypertension. Both share the same underlying pathophysiology — pulmonary vascular endothelial dysfunction, smooth-muscle proliferation, and progressive vascular remodelling — which is the pharmacological target of prostacyclin analogues. Because iloprost is already approved for the mechanistically identical parent condition (idiopathic PAH), its extension to HIV-associated PAH represents use within the same drug class for a closely related disease mechanism, rather than a speculative cross-disease jump.

By contrast, the two related candidates — PAH associated with congenital heart disease and PAH associated with connective tissue disease — are also WHO Group 1 subtypes with plausible mechanistic overlap, but their supporting evidence is weaker (observational/review-level, L3), and in the case of congenital heart disease the disease process is driven by a structural shunt rather than primary vascular pathology, so response may differ from idiopathic PAH.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00709956](https://clinicaltrials.gov/study/NCT00709956) | Phase 3 | Completed | 64 | Multicentre, double-blind, randomised, placebo-controlled crossover study of a single dose of inhaled iloprost on exercise capacity in patients with symptomatic PAH, enrolling idiopathic, familial, HIV-associated, and drug/toxin-induced PAH (NYHA class II–IV), on top of stable background therapy (bosentan, ambrisentan, or sildenafil). |

*Supporting trial for a related candidate (PAH associated with congenital heart disease):* [NCT01383083](https://clinicaltrials.gov/study/NCT01383083) — Phase N/A, status Unknown, n=42, assessing safety, tolerability, and haemodynamic effects of iloprost in adults with Eisenmenger-physiology PAH. Trial completion/reporting status is unconfirmed, which limits its evidentiary weight.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31090367](https://pubmed.ncbi.nlm.nih.gov/31090367/) | 2019 | Cohort/Registry | Terapevticheskii arkhiv | Six-year national PAH registry analysis of prevalence, clinical course, and current therapy across PAH subgroups, including associated forms. |
| [18260882](https://pubmed.ncbi.nlm.nih.gov/18260882/) | 2007 | Review | Kardiologiia | Review series on controlled trials of prostacyclin and its synthetic analogues (including iloprost) in idiopathic PAH and PAH associated with connective tissue disease, congenital heart disease, and HIV infection. |
| [17195895](https://pubmed.ncbi.nlm.nih.gov/17195895/) | 2006 | Review | The Mount Sinai Journal of Medicine | Overview of HIV-related pulmonary hypertension: estimated incidence ~0.5% of HIV-infected individuals, unclear pathogenesis, variable presentation from dyspnoea to syncope. |
| [14720012](https://pubmed.ncbi.nlm.nih.gov/14720012/) | 2003 | Review | American Journal of Respiratory Medicine | Review of prostanoid therapy for PAH, explicitly grouping HIV-associated PAH with idiopathic PAH and other associated forms as sharing near-identical obstructive pulmonary microvascular pathology. |

---

## Denmark Market Information

Iloprost currently has **no marketing authorisation on file in Denmark** in this evidence pack (0 licenses recorded, market status "Not marketed"). No Laegemiddelstyrelsen national authorisation or EMA centralised authorisation record is available in the dataset to summarise dosage forms or approved indication text.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information. No structured warnings, contraindications, or drug–drug interaction data were returned by the available queries in this evidence pack.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** *(applies specifically to the HIV-associated PAH indication)*

**Rationale:**
A completed Phase 3 randomised controlled trial (n=64) evaluating iloprost in a PAH population that included HIV-associated patients, together with consistent mechanistic and review-level literature support, gives this indication the strongest evidence base (L1) among all candidates in this pack. The other WHO Group 1 candidates (congenital heart disease-, connective tissue disease-associated PAH) remain at "Research Question" status (L3) pending stronger trial-level data, and the two hypotrichosis-related predictions should be held as likely model artifacts with no supporting evidence.

**To proceed, the following is needed:**
- Danish/EU label safety warnings and contraindications for iloprost — this is currently a **blocking** data gap that prevents entry into the S1 safety pre-assessment stage.
- Detailed mechanism-of-action data (DrugBank MOA) to formally support the mechanistic rationale.
- Subgroup-level results from NCT00709956 specific to the HIV-associated PAH cohort, since the trial population was mixed (idiopathic, familial, HIV-associated, and drug/toxin-induced PAH).
- Drug–drug interaction data with antiretroviral therapy (ART), given the target population — the DDI query for iloprost returned no results.
- Confirmation of Danish/EU marketing authorisation pathway, since iloprost is not currently recorded as marketed in Denmark.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

