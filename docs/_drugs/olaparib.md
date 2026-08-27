---
layout: default
title: Olaparib
parent: 僅模型預測 (L5)
nav_order: 319
evidence_level: L5
indication_count: 10
---

# Olaparib
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

# Olaparib: From Ovarian Cancer to Female Breast Carcinoma

## One-Sentence Summary

Olaparib is a PARP1/2 inhibitor whose first approved oncology indication was BRCA-mutated ovarian cancer. The TxGNN model predicts it may also be effective for **Female Breast Carcinoma**, and this is not a purely exploratory hypothesis — **50 clinical trials** and **20 publications** were identified for this drug–disease pair, including the pivotal OlympiA and OlympiAD randomised trials that already underpin international regulatory approvals in gBRCA-mutated breast cancer.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Ovarian cancer (BRCA1/2-mutated) — internationally established indication; no Danish licence record is available in the current dataset |
| Predicted New Indication | Female Breast Carcinoma |
| TxGNN Prediction Score | 99.09% |
| Evidence Level | L1 |
| Denmark Market Status | Not marketed (未上市) |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed structured mechanism-of-action data is not available in this evidence pack (Data Gap DG002). Based on the evidence collected alongside the prediction, olaparib is a poly(ADP-ribose) polymerase (PARP) 1/2 inhibitor. It blocks single-strand DNA repair, which is selectively lethal ("synthetic lethality") to tumour cells that already carry a homologous recombination deficiency (HRD) — most notably germline or somatic BRCA1/2 mutations.

Ovarian cancer and breast cancer share this same molecular vulnerability: approximately 5–10% of breast cancers, and a much larger share of high-grade serous ovarian cancers, carry a deleterious BRCA1/2 variant. Because olaparib's original approval was built on exploiting BRCA-driven HRD in ovarian cancer, extending it to BRCA-mutated breast cancer is a mechanistically direct, not speculative, extension.

Consistent with this, the connection TxGNN surfaced is not a novel hypothesis but a recovery of an already-validated, internationally approved indication: olaparib (Lynparza) received FDA approval for gBRCA-mutated, HER2-negative metastatic breast cancer in 2018 (OlympiAD) and was extended to the adjuvant early-breast-cancer setting in 2022 (OlympiA). This explains the very high prediction score and the L1 evidence level.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06580314](https://clinicaltrials.gov/study/NCT06580314) | Phase 3 | Recruiting | 880 | One vs. two years of maintenance olaparib ± bevacizumab in BRCA1/2-mutated or HRD+ disease; graded "A" direct support for maintenance-duration optimisation. |
| [NCT04330040](https://clinicaltrials.gov/study/NCT04330040) | Phase 4 | Completed | 202 | Post-marketing trial in Indian patients with platinum-sensitive relapsed ovarian cancer and gBRCA1/2-mutated metastatic breast cancer. |
| [NCT01445418](https://clinicaltrials.gov/study/NCT01445418) | Phase 1 | Completed | 103 | Olaparib (AZD2281) + carboplatin dose-finding/expansion in BRCA1/2 carriers with breast and ovarian cancer, including sporadic TNBC. |
| [NCT06201234](https://clinicaltrials.gov/study/NCT06201234) | Phase 2 | Recruiting | 176 | Elacestrant added to standard-of-care olaparib in HR+/HER2- locally advanced or metastatic breast cancer with gBRCA1/2 mutations. |
| [NCT05498155](https://clinicaltrials.gov/study/NCT05498155) | Phase 2 | Active, not recruiting | 50 | Neoadjuvant olaparib monotherapy vs. olaparib + durvalumab in BRCA-mutated, early-stage HER2-negative breast cancer. |
| [NCT05358639](https://clinicaltrials.gov/study/NCT05358639) | Phase 1 | Active, not recruiting | 36 | Olaparib + navitoclax (Bcl-2/Bcl-XL inhibitor) in BRCA1/2/PALB2-mutated triple-negative breast cancer and recurrent HGSC. |
| [NCT03109080](https://clinicaltrials.gov/study/NCT03109080) | Phase 1 | Completed | 24 | Olaparib combined with radiation therapy in inflammatory, locoregionally advanced/metastatic or residual TNBC. |
| [NCT04553926](https://clinicaltrials.gov/study/NCT04553926) | N/A (post-marketing) | Completed | 661 | Regulatory post-marketing surveillance of Lynparza tablets in real-world South Korean practice, per approved indications. |
| [NCT05258747](https://clinicaltrials.gov/study/NCT05258747) | Phase 1 | Completed | 70 | Bioequivalence study of generic vs. reference olaparib 150 mg tablets in BRCA-mutated ovarian/metastatic breast cancer patients. |
| [NCT02734004](https://clinicaltrials.gov/study/NCT02734004) | Phase 1/2 | Active, not recruiting | 264 | Durvalumab + olaparib (± bevacizumab) in advanced solid tumours, including breast cancer, evaluating efficacy and safety. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34081848](https://pubmed.ncbi.nlm.nih.gov/34081848/) | 2021 | RCT | The New England Journal of Medicine | OlympiA: adjuvant olaparib significantly reduced recurrence in gBRCA1/2-mutated, high-risk HER2-negative early breast cancer. |
| [28578601](https://pubmed.ncbi.nlm.nih.gov/28578601/) | 2017 | RCT | The New England Journal of Medicine | OlympiAD: olaparib improved progression-free survival vs. chemotherapy in gBRCA-mutated HER2-negative metastatic breast cancer. |
| [36228963](https://pubmed.ncbi.nlm.nih.gov/36228963/) | 2022 | RCT | Annals of Oncology | OlympiA overall-survival analysis confirming durable benefit of adjuvant olaparib in gBRCA1/2 high-risk early breast cancer. |
| [33119476](https://pubmed.ncbi.nlm.nih.gov/33119476/) | 2020 | RCT | Journal of Clinical Oncology | TBCRC 048: olaparib activity in metastatic breast cancer with somatic BRCA1/2 or non-BRCA homologous-recombination gene mutations. |
| [36893711](https://pubmed.ncbi.nlm.nih.gov/36893711/) | 2023 | RCT | European Journal of Cancer | OlympiAD extended follow-up confirming safety and OS trend for olaparib vs. chemotherapy in gBRCA-mutated metastatic breast cancer. |
| [30689707](https://pubmed.ncbi.nlm.nih.gov/30689707/) | 2019 | RCT | Annals of Oncology | OlympiAD final overall-survival and tolerability results for olaparib vs. physician's-choice chemotherapy. |
| [38588696](https://pubmed.ncbi.nlm.nih.gov/38588696/) | 2024 | RCT | Nature | PARTNER trial: neoadjuvant olaparib added to carboplatin-paclitaxel in BRCA-wild-type triple-negative breast cancer. |
| [33710534](https://pubmed.ncbi.nlm.nih.gov/33710534/) | 2021 | Review | Targeted Oncology | Overview of PARP inhibitors (olaparib, talazoparib) approved for deleterious/suspected-deleterious germline BRCA-mutated breast cancer. |
| [31650727](https://pubmed.ncbi.nlm.nih.gov/31650727/) | 2020 | Review | Annals of Laboratory Medicine | Review of BRCA1/BRCA2 pathogenic-variant breast cancer treatment and prevention strategies, including PARP-inhibitor rationale. |
| [39791278](https://pubmed.ncbi.nlm.nih.gov/39791278/) | 2025 | Review | CA: A Cancer Journal for Clinicians | Pan-tumor review of PARP inhibitors (olaparib, talazoparib, rucaparib, niraparib) and synthetic-lethality mechanism across cancer types. |

## Denmark Market Information

No marketing authorisations for Olaparib are currently on record in Denmark — Laegemiddelstyrelsen data shows **0 licences** and a market status of **Not marketed**. This is separate from the missing-label issue below (DG001): it reflects an actual absence of a registered product, not a data-collection gap.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy — PARP1/2 inhibitor exploiting synthetic lethality in BRCA1/2-mutated or HRD tumours (not a conventional cytotoxic agent) |
| Myelosuppression Risk | Please refer to the Summary of Product Characteristics (SmPC) — no structured toxicity data available in this dataset |
| Emetogenicity Classification | Please refer to the Summary of Product Characteristics (SmPC) — no structured toxicity data available in this dataset |
| Monitoring Items | Please refer to the Summary of Product Characteristics (SmPC) — no structured toxicity data available in this dataset |
| Handling Protection | Please refer to the Summary of Product Characteristics (SmPC) — no structured toxicity data available in this dataset |

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information. No structured warnings, contraindications, or drug–drug interaction data were retrievable for this candidate (DDI query status: not found).

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic and clinical evidence base is strong (L1 — multiple completed Phase 3 RCTs, including OlympiA and OlympiAD, already support olaparib in BRCA-mutated breast cancer internationally). However, Denmark-specific regulatory documentation is missing, which blocks a full safety evaluation.

**To proceed, the following is needed:**
- Danish/TFDA-equivalent product label (SmPC) — warnings and contraindications (Blocking gap, DG001; source: Laegemiddelstyrelsen label PDF)
- Confirmed DrugBank mechanism-of-action record (High-priority gap, DG002)
- Clarification of Danish marketing-authorisation pathway, given 0 current licences despite broad international approval
- Drug–drug interaction data collection (current query status: not found)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

