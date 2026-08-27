---
layout: default
title: Peginterferon Alfa-2A
parent: 僅模型預測 (L5)
nav_order: 336
evidence_level: L5
indication_count: 10
---

# Peginterferon Alfa-2A
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

# PEGINTERFERON ALFA-2A: From Chronic Hepatitis C to Hepatitis B Virus Infection

## One-Sentence Summary

Peginterferon alfa-2a (Pegasys) is a pegylated interferon originally developed and marketed for chronic hepatitis C. The TxGNN model predicts it is effective for **Hepatitis B Virus Infection**, supported by **50 clinical trials** and **20 publications** — and the underlying evidence indicates this is largely a confirmation of an *already globally approved* indication rather than a purely novel repurposing hypothesis.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic Hepatitis C *(well-established global use; the evidence pack itself has a data gap on this field — see note below)* |
| Predicted New Indication | Hepatitis B Virus Infection |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L1 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Proceed with Guardrails |

> **Note on Original Indication:** The evidence pack's `original_indications` and Danish licence fields are both empty (Data Gap DG001/DG002). The "Chronic Hepatitis C" original indication above reflects well-established public pharmacological knowledge about peginterferon alfa-2a (Pegasys), not a value extracted from this evidence pack. This should be confirmed against the official Danish/EU SmPC before use in any regulatory context.

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data was not available from DrugBank for this evidence pack (Data Gap DG002). Based on known pharmacology, peginterferon alfa-2a is a pegylated form of recombinant interferon alfa-2a that activates the JAK-STAT signalling pathway, inducing host innate antiviral responses (interferon-stimulated gene expression) as well as immunomodulatory effects. This mechanism underlies its antiviral activity against hepatotropic viruses broadly, including both HCV and HBV.

Chronic hepatitis C and chronic hepatitis B are both hepatotropic viral infections sharing a common therapeutic rationale for interferon-based immune activation: suppression of viral replication and promotion of host immune clearance (for HBV, specifically HBeAg seroconversion and HBsAg loss).

Importantly, the repurposing rationale in the evidence pack notes that this is **not a purely speculative old-drug-new-use candidate**: peginterferon alfa-2a (Pegasys) already holds regulatory approval for chronic hepatitis B in numerous countries worldwide. The "[Data Gap]" in the `original_indications` field appears to be a data-completeness issue in this evidence pack rather than evidence that no hepatitis B indication exists. This distinction matters for how the "Proceed with Guardrails" recommendation should be interpreted — the clinical/scientific case is strong; what is missing is Denmark-specific regulatory documentation (SmPC, licence status, DDI data).

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01095835](https://clinicaltrials.gov/study/NCT01095835) | Phase 3 | Completed | 131 | RCT comparing 48 vs 96 weeks of 40kD PEG-IFN alfa-2a, alone or with lamivudine, in HBeAg-negative chronic HBV |
| [NCT01011738](https://clinicaltrials.gov/study/NCT01011738) | N/A (observational) | Completed | 1,842 | Large prospective, non-interventional cohort evaluating on-treatment predictors of response to Pegasys in HBeAg-positive/negative CHB |
| [NCT04667104](https://clinicaltrials.gov/study/NCT04667104) | Phase 2 | Completed | 48 | JNJ-73763989 + JNJ-56136379 + nucleos(t)ide analogue + PegIFN-alfa2a combination in virologically suppressed chronic HBV |
| [NCT01086085](https://clinicaltrials.gov/study/NCT01086085) | Phase 4 | Completed | 265 | Response-guided treatment (RGT) optimisation of Pegasys in HBeAg-positive CHB, quantitative HBsAg reduction |
| [NCT00940485](https://clinicaltrials.gov/study/NCT00940485) | Phase 4 | Completed | 200 | Combination/sequential Pegasys + entecavir for optimising HBeAg seroconversion |
| [NCT01373684](https://clinicaltrials.gov/study/NCT01373684) | Phase 4 | Completed | 90 | Add-on PEG-IFN alfa-2a to nucleos(t)ide analogue therapy to induce HBsAg decline in HBeAg-negative CHB |
| [NCT02570191](https://clinicaltrials.gov/study/NCT02570191) | Phase 4 | Completed | 60 | Efficacy, safety and tolerability of Pegasys in HBeAg-negative chronic HBV |
| [NCT01734018](https://clinicaltrials.gov/study/NCT01734018) | N/A (observational) | Completed | 50 | Multicentre, prospective, non-interventional study of Pegasys response parameters in HBeAg-positive/negative CHB |
| [NCT02732639](https://clinicaltrials.gov/study/NCT02732639) | Phase 3 | Completed | 31 | Pegasys monotherapy (48 weeks) in chronic hepatitis D (HBV/HDV co-infection) |
| [NCT06092333](https://clinicaltrials.gov/study/NCT06092333) | Phase 2 | Recruiting | 50 | Ongoing pilot combining VIR-2218 with peginterferon alfa-2a for chronic hepatitis B |

*(Full evidence pack contains 50 registered trials for this indication; the above 10 were selected for phase, completion status, and direct HBV relevance.)*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15987917](https://pubmed.ncbi.nlm.nih.gov/15987917/) | 2005 | RCT | New England Journal of Medicine | Landmark trial: peginterferon alfa-2a ± lamivudine vs lamivudine alone in HBeAg-positive chronic hepatitis B |
| [30865588](https://pubmed.ncbi.nlm.nih.gov/30865588/) | 2019 | Systematic Review / Meta-analysis | Antiviral Therapy | Individual participant data meta-analysis establishing PEG-IFN stopping rules in chronic hepatitis B |
| [30549279](https://pubmed.ncbi.nlm.nih.gov/30549279/) | 2019 | RCT | Hepatology | Entecavir + peginterferon alfa-2a in HBeAg-positive immune-tolerant adults with chronic HBV |
| [30318613](https://pubmed.ncbi.nlm.nih.gov/30318613/) | 2019 | RCT (paediatric) | Hepatology | Entecavir/peginterferon alfa-2a combination in HBeAg-positive immune-tolerant children with chronic HBV |
| [29689122](https://pubmed.ncbi.nlm.nih.gov/29689122/) | 2018 | Phase III RCT | Hepatology | PEG-B-ACTIVE study: peginterferon alfa-2a in children 3–<18 years with chronic hepatitis B |
| [29715359](https://pubmed.ncbi.nlm.nih.gov/29715359/) | 2018 | Review | JAMA | Overview of chronic hepatitis B infection, epidemiology and progression risk |
| [21423260](https://pubmed.ncbi.nlm.nih.gov/21423260/) | 2011 | Review | Nature Reviews Gastroenterology & Hepatology | Review of hepatitis B therapy goals and treatment response markers |
| [26700861](https://pubmed.ncbi.nlm.nih.gov/26700861/) | 2015 | Cohort | Virology Journal | Long-term effects of peginterferon alfa-2a therapy in Japanese chronic hepatitis B patients |
| [41312046](https://pubmed.ncbi.nlm.nih.gov/41312046/) | 2025 | Review | Drug Design, Development and Therapy | PEG-IFN-α-induced functional cure in special populations with chronic HBV — current trends and challenges |
| [19084016](https://pubmed.ncbi.nlm.nih.gov/19084016/) | 2009 | Study | Gastroenterology | Peginterferon alfa-2a plus ribavirin for dual chronic HBV/HCV infection |

---

## Denmark Market Information

No marketing authorisation is currently registered for peginterferon alfa-2a in this dataset — `taiwan_regulatory.total_licenses = 0` and `market_status = Not marketed`. No national (Laegemiddelstyrelsen) or centralised (EMA) authorisation records were returned for this evidence pack. This should be independently verified against the EMA/EU medicines database, since peginterferon alfa-2a (Pegasys) is known to hold centralised EU marketing authorisation historically — the absence of a record here likely reflects a data-collection gap rather than confirmed non-authorisation.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information. *(All safety fields in this evidence pack — key warnings, contraindications, and drug-drug interactions — returned as data gaps or "not found"; DG001 is flagged as a Blocking gap for safety initial assessment.)*

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
- Evidence level L1 is met (≥2 completed Phase 3 RCTs: NCT01095835 and the 2005 NEJM trial by Lau et al.), and the therapeutic rationale is exceptionally strong because peginterferon alfa-2a already holds hepatitis B indications in multiple jurisdictions globally — this is corroboration of an established use, not a speculative hypothesis.
- However, Denmark-specific regulatory data (SmPC warnings/contraindications, marketing authorisation status, DDI profile) are all missing (DG001 – Blocking), which prevents a full safety sign-off and unconditional "Go".
- For context, the model also surfaced several lower-confidence signals for this drug (hepatitis E virus infection — Research Question stage, evidence level L3; and hepatitis A virus infection, an MeSH "animal hepatitis" term, and Omsk haemorrhagic fever — all flagged **Hold** as likely knowledge-graph noise with no genuine supporting evidence). These were screened out and are not part of this recommendation.

**To proceed, the following is needed:**
- Danish/EU SmPC warnings, precautions, and contraindications (DG001, Blocking)
- Confirmed mechanism-of-action documentation via DrugBank API (DG002, High)
- Verification of actual Danish/EU marketing authorisation status (current record shows 0 licences, which should be cross-checked against EMA's centralised procedure database)
- A proper drug-drug interaction (DDI) screen, since the current query returned "not_found"
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

