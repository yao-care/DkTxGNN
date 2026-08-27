---
layout: default
title: Trastuzumab
parent: 僅模型預測 (L5)
nav_order: 446
evidence_level: L5
indication_count: 10
---

# Trastuzumab
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

# Trastuzumab: From HER2-Positive Breast Cancer to Progesterone-Receptor Positive Breast Cancer

## One-Sentence Summary

Trastuzumab is a HER2-targeted humanized monoclonal antibody, well established for HER2-positive breast cancer (the evidence pack itself does not supply a Danish-registered indication text for this drug). The TxGNN model predicts it may be effective for **progesterone-receptor positive breast cancer**, with **36 clinical trials** and **20 publications** currently associated with this hypothesis — though the strongest evidence points to the HR+/HER2+ co-expressing subgroup rather than PR status alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available from the Danish licensing data in this evidence pack (`taiwan_regulatory.licenses` is empty); trastuzumab's globally established original indication is HER2-positive breast cancer |
| Predicted New Indication | Progesterone-receptor positive breast cancer |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L1 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data is not available in this evidence pack (flagged as a High-severity data gap, DG002). Based on generally known pharmacology, trastuzumab is a humanized IgG1 monoclonal antibody that binds the extracellular domain of human epidermal growth factor receptor 2 (HER2/ERBB2), blocking HER2-driven proliferation signalling and mediating antibody-dependent cellular cytotoxicity (ADCC). Its efficacy in HER2-positive breast cancer is proven across numerous pivotal trials, and mechanistically it may extend to progesterone-receptor positive breast cancer where HER2 co-expression is present.

Importantly, the underlying repurposing rationale supplied with the evidence pack clarifies that PR status is not itself the pharmacological target — trastuzumab's indication is determined by HER2 status, not hormone-receptor status. The clinical trials and literature listed for this "new" indication predominantly enrol HR+/HER2+ (triple-positive) patients, a population where trastuzumab is already standard of care. This means the prediction should be interpreted as confirmation of an existing, guideline-recognized use in a HER2+ subgroup that happens to be PR-positive, rather than a genuinely novel repurposing hypothesis into an unrelated disease area.

The large Phase III trials in the evidence (e.g., adjuvant regimens with over 3,000 patients each) directly test trastuzumab-containing regimens in HER2-overexpressing breast cancer populations that include PR-positive tumours, which is why the evidence level reaches L1 despite the conceptual overlap with the original indication.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01275677](https://clinicaltrials.gov/study/NCT01275677) | Phase 3 | Completed | 3270 | Adjuvant chemotherapy ± trastuzumab in node-positive or high-risk node-negative HER2-low invasive breast cancer |
| [NCT00667251](https://clinicaltrials.gov/study/NCT00667251) | Phase 3 | Completed | 652 | Taxane-based chemotherapy + lapatinib vs. + trastuzumab as first-line therapy in HER2+ metastatic breast cancer |
| [NCT02152943](https://clinicaltrials.gov/study/NCT02152943) | Phase 1 | Completed | 37 | Everolimus + letrozole + trastuzumab in hormone receptor-positive and HER2-positive advanced/metastatic breast cancer and other solid tumours |
| [NCT00005970](https://clinicaltrials.gov/study/NCT00005970) | Phase 3 | Completed | 3436 | Doxorubicin/cyclophosphamide followed by paclitaxel ± trastuzumab as adjuvant treatment in HER2-overexpressing node-positive or high-risk node-negative breast cancer |
| [NCT04629846](https://clinicaltrials.gov/study/NCT04629846) | Phase 3 | Completed | 517 | QL1209 (pertuzumab biosimilar) vs. reference pertuzumab, each + trastuzumab + docetaxel, in HER2-positive/ER-PR-negative early or locally advanced breast cancer |
| [NCT03726879](https://clinicaltrials.gov/study/NCT03726879) | Phase 3 | Completed | 454 | IMpassion050: atezolizumab vs. placebo + neoadjuvant dose-dense AC then paclitaxel + trastuzumab + pertuzumab in early HER2-positive breast cancer |
| [NCT00545688](https://clinicaltrials.gov/study/NCT00545688) | Phase 2 | Completed | 417 | 4-arm neoadjuvant Herceptin ± docetaxel ± pertuzumab in locally advanced, inflammatory, or early-stage HER2-positive breast cancer |
| [NCT00134680](https://clinicaltrials.gov/study/NCT00134680) | Phase 2 | Completed | 33 | Letrozole + trastuzumab in ErbB2-positive, estrogen and/or progesterone receptor-positive metastatic breast cancer |
| [NCT04152057](https://clinicaltrials.gov/study/NCT04152057) | Phase 1/2 | Unknown | 20 | Pyrotinib + albumin-bound paclitaxel + trastuzumab in HER2-positive early or locally advanced breast cancer |
| [NCT00999804](https://clinicaltrials.gov/study/NCT00999804) | Phase 2 | Active, not recruiting | 128 | TBCRC 023: Lapatinib + trastuzumab, with or without endocrine therapy, for 12 vs. 24 weeks in HER2-overexpressing breast cancer |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27179402](https://pubmed.ncbi.nlm.nih.gov/27179402/) | 2016 | RCT | Lancet Oncol | NeoSphere 5-year follow-up: neoadjuvant pertuzumab + trastuzumab + docetaxel improves progression-free and disease-free survival in HER2-positive breast cancer |
| [32353342](https://pubmed.ncbi.nlm.nih.gov/32353342/) | 2020 | RCT | Lancet Oncol | monarcHER: abemaciclib + trastuzumab ± fulvestrant vs. chemotherapy + trastuzumab in HR+/HER2+ advanced breast cancer |
| [26874901](https://pubmed.ncbi.nlm.nih.gov/26874901/) | 2016 | RCT | Lancet Oncol | ExteNET: neratinib after trastuzumab-based adjuvant therapy in HER2-positive breast cancer |
| [29117498](https://pubmed.ncbi.nlm.nih.gov/29117498/) | 2017 | Cohort | NEJM | 20-year recurrence risk after stopping 5 years of endocrine therapy in ER-positive early breast cancer |
| [31410192](https://pubmed.ncbi.nlm.nih.gov/31410192/) | 2019 | Pending classification | Theranostics | Molecular portraits and trastuzumab responsiveness of ER-positive, PR-positive, and HER2-positive (triple-positive) breast cancer |
| [34983437](https://pubmed.ncbi.nlm.nih.gov/34983437/) | 2022 | Pending classification | BMC Cancer | Trastuzumab + fulvestrant combination therapy in HR-positive/HER2-positive advanced breast cancer (retrospective single-centre study) |
| [37166817](https://pubmed.ncbi.nlm.nih.gov/37166817/) | 2023 | Pending classification | JAMA Oncol | WSG-TP-II randomized trial: endocrine therapy + trastuzumab + pertuzumab vs. de-escalated chemotherapy in HR+/HER2+ early breast cancer |
| [35640077](https://pubmed.ncbi.nlm.nih.gov/35640077/) | 2022 | Pending classification | J Clin Oncol | ASCO guideline update: systemic therapy for advanced HER2-positive breast cancer |
| [39191270](https://pubmed.ncbi.nlm.nih.gov/39191270/) | 2024 | Pending classification | JNCCN | Clinical Treatment Score post-5 years (CTS5) and late recurrence risk in HR+/HER2+ breast cancer |
| [26253814](https://pubmed.ncbi.nlm.nih.gov/26253814/) | 2015 | Review | Breast | Clinical implications of the intrinsic molecular subtypes of breast cancer |

---

## Denmark Market Information

No marketing authorisation records are present in the evidence pack (`taiwan_regulatory.licenses` is empty, `total_licenses = 0`, `market_status = "Not marketed"`). Trastuzumab does not currently have a registered marketing authorisation in this dataset for the Danish market.

---

## Cytotoxicity

Trastuzumab is an antineoplastic agent (breast/gastric cancer indications; DrugBank monoclonal antibody classification).

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (HER2-targeted humanized monoclonal antibody; not a conventional cytotoxic chemotherapeutic) |
| Myelosuppression Risk | Please refer to the Summary of Product Characteristics (SmPC) warnings and precautions |
| Emetogenicity Classification | Please refer to the Summary of Product Characteristics (SmPC) warnings and precautions |
| Monitoring Items | Please refer to the Summary of Product Characteristics (SmPC) warnings and precautions |
| Handling Protection | Please refer to the Summary of Product Characteristics (SmPC) warnings and precautions |

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information. Note that a formal Danish/EU label warnings-and-contraindications lookup is flagged as a **Blocking** data gap (DG001) in this evidence pack — this must be resolved before a formal safety pre-assessment (S1) can proceed.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
- Evidence level L1 is supported by multiple completed Phase III RCTs and a direct Phase I combination trial in the HR+/HER2+ population, but the repurposing rationale itself notes this largely confirms an existing HER2-positive breast cancer indication in a PR-positive subgroup, rather than establishing a genuinely novel indication.
- Trastuzumab is currently not marketed in Denmark (0 authorisations on record), and formal label/safety data (warnings, contraindications, DDI) are missing, which blocks a complete safety pre-assessment.

**To proceed, the following is needed:**
- TFDA/EMA-approved product label (SmPC) with warnings, contraindications, and DDI data (Blocking gap, DG001)
- Formal mechanism-of-action documentation from DrugBank or equivalent source (DG002)
- Confirmation of Danish marketing authorisation pathway, given the drug is not currently marketed locally
- Clarification of whether the target population should be defined by HER2 status (established use) rather than PR status alone, to distinguish genuine repurposing value from label-extension confirmation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

