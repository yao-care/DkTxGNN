---
layout: default
title: Tacrolimus
parent: 僅模型預測 (L5)
nav_order: 412
evidence_level: L5
indication_count: 6
---

# Tacrolimus
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Tacrolimus: From Transplant Rejection Prevention to Seborrheic Dermatitis

## One-Sentence Summary

Tacrolimus is a calcineurin-inhibiting immunomodulator classically used to prevent organ transplant rejection and, in topical form (Protopic), to treat atopic dermatitis. The TxGNN model predicts it may also be effective for **Seborrheic Dermatitis**, with **2 completed clinical trials** (Phase 3 and Phase 4) and **20 supporting publications** currently identified.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in the evidence pack; tacrolimus is widely documented for prevention of organ transplant rejection (systemic) and atopic dermatitis (topical) |
| Predicted New Indication | Seborrheic Dermatitis |
| TxGNN Prediction Score | 99.26% |
| Evidence Level | L1 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack. Based on widely known information, tacrolimus is a topical calcineurin inhibitor that suppresses antigen-specific T-cell activation and downregulates the inflammatory cytokine cascade — the same mechanism underlying its established efficacy in atopic dermatitis.

Seborrheic dermatitis and atopic dermatitis are both chronic inflammatory dermatoses that share T-cell–mediated inflammatory pathways and impaired skin barrier function; seborrheic dermatitis is additionally linked to *Malassezia*-driven inflammation. Because tacrolimus reduces local T-cell–mediated inflammation regardless of the triggering antigen, its mechanism plausibly extends from atopic dermatitis to seborrheic dermatitis.

This mechanistic rationale is directly supported by clinical evidence: two dedicated trials (a completed Phase 3 RCT and a completed Phase 4 study) have specifically evaluated tacrolimus ointment for maintenance treatment of severe facial seborrheic dermatitis in adults, reinforcing the plausibility of the TxGNN prediction.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02004860](https://clinicaltrials.gov/study/NCT02004860) | Phase 3 | Completed | 120 | Evaluated tacrolimus ointment (Protopic) as maintenance therapy for severe seborrheic dermatitis on the adult face, aiming to reduce relapse frequency and steroid use |
| [NCT01591070](https://clinicaltrials.gov/study/NCT01591070) | Phase 4 | Completed | 104 | Assessed whether proactive use of 0.1% tacrolimus ointment once or twice weekly maintains remission and reduces exacerbation in adult facial seborrheic dermatitis |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33010323](https://pubmed.ncbi.nlm.nih.gov/33010323/) | 2021 | RCT | J Am Acad Dermatol | Multicenter, double-blind RCT of tacrolimus 0.1% vs ciclopiroxolamine 1% for maintenance therapy in severe facial seborrheic dermatitis |
| [24171300](https://pubmed.ncbi.nlm.nih.gov/24171300/) | 2013 | RCT | Ann Parasitol | Compared sertaconazole 2% cream vs tacrolimus 0.03% cream in 60 patients with seborrheic dermatitis |
| [39219446](https://pubmed.ncbi.nlm.nih.gov/39219446/) | 2024 | Review (Cochrane) | Clin Exp Allergy | Network meta-analysis of topical anti-inflammatory treatments for eczema, relevant to calcineurin inhibitor efficacy/safety comparisons |
| [27804089](https://pubmed.ncbi.nlm.nih.gov/27804089/) | 2017 | Systematic Review | Am J Clin Dermatol | Systematic review of topical treatments (antifungals, keratolytics, corticosteroids, TCIs) for facial seborrheic dermatitis |
| [19222250](https://pubmed.ncbi.nlm.nih.gov/19222250/) | 2009 | Review | Am J Clin Dermatol | Reviews pathophysiology, safety, and efficacy of topical calcineurin inhibitors in seborrheic dermatitis |
| [19213227](https://pubmed.ncbi.nlm.nih.gov/19213227/) | 2009 | Review | J Drugs Dermatol | Overview of facial seborrheic dermatitis status and therapeutic horizons, including TCIs |
| [15461548](https://pubmed.ncbi.nlm.nih.gov/15461548/) | 2004 | Review | Expert Opin Pharmacother | Reviews tacrolimus ointment for atopic dermatitis and other inflammatory cutaneous disease, including seborrheic dermatitis |
| [26512166](https://pubmed.ncbi.nlm.nih.gov/26512166/) | 2015 | Cohort | Ann Dermatol | Maintenance therapy of facial seborrheic dermatitis with 0.1% tacrolimus ointment |
| [37067129](https://pubmed.ncbi.nlm.nih.gov/37067129/) | 2023 | Comparative Study | Indian J Dermatol Venereol Leprol | Compared oral itraconazole + topical tacrolimus vs topical tacrolimus alone for maintenance treatment of seborrheic dermatitis (Vietnam) |
| [12833030](https://pubmed.ncbi.nlm.nih.gov/12833030/) | 2003 | Open Pilot Study | J Am Acad Dermatol | Open-label pilot study of 0.1% tacrolimus in 18 patients with seborrheic dermatitis; 61% achieved complete clearance |

---

## Denmark Market Information

Tacrolimus currently has no marketing authorisation on file in Denmark (Laegemiddelstyrelsen) in this evidence pack — market status is **Not marketed**, with 0 authorisations recorded.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Two completed clinical trials (Phase 3 and Phase 4) directly evaluate tacrolimus for facial seborrheic dermatitis maintenance treatment, supported by 20 publications including RCTs, systematic reviews, and cohort studies — meeting L1 evidence criteria. However, safety and Danish market data are entirely absent, so guardrails are required before advancing.

**To proceed, the following is needed:**
- Danish SmPC / Laegemiddelstyrelsen warnings, contraindications, and drug interaction data (currently a blocking data gap)
- Confirmed mechanism of action documentation from DrugBank
- Verification of a marketing pathway or existing authorisation in Denmark for tacrolimus (topical or systemic formulations)
- Formal route-of-administration compatibility assessment for the seborrheic dermatitis indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

