---
layout: default
title: Dasatinib
parent: 僅模型預測 (L5)
nav_order: 132
evidence_level: L5
indication_count: 10
---

# Dasatinib
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

# Dasatinib: From Chronic Myeloid Leukemia to Ewing Sarcoma

## One-Sentence Summary

Dasatinib (Sprycel) is a potent second-generation BCR-ABL and Src family kinase inhibitor, internationally approved for Chronic Myeloid Leukemia (CML) and Philadelphia chromosome-positive Acute Lymphoblastic Leukemia (Ph+ ALL), but not currently registered in Denmark.
The TxGNN model predicts it may also be effective for **Ewing sarcoma**, supported by **3 registered clinical trials** and **9 publications** — however, the only dedicated paediatric trial was terminated after enrolling just 7 patients, representing an important negative signal that must be weighed carefully.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | CML and Ph+ ALL (internationally approved; not registered in Denmark) |
| Predicted New Indication | Ewing sarcoma |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L3 |
| Denmark Market Status | Not on market |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Dasatinib is an orally administered small-molecule inhibitor of multiple tyrosine kinases. Its primary targets are BCR-ABL (which drives CML) and Src family kinases (LCK, HCK, FYN). It is approximately 325-fold more potent than imatinib against wild-type BCR-ABL in vitro. Beyond haematological malignancies, dasatinib also inhibits c-KIT and PDGFR-β, giving it a broader kinase coverage that may be relevant to solid tumours.

Ewing sarcoma is a highly aggressive bone and soft tissue cancer primarily affecting children, adolescents, and young adults. Its hallmark molecular feature is the EWS-FLI1 (or related EWSR1-ETS) fusion gene. Multiple preclinical studies published between 2007 and 2022 have demonstrated that Src kinase is abnormally activated in Ewing sarcoma cells, particularly through the FAK-Src axis. This signalling axis drives the formation of invadopodia — specialised cellular structures associated with tumour invasion and metastatic spread. The EWS-FLI1 fusion protein has been shown to indirectly modulate Src pathway activity, providing a mechanistic basis for targeting Src in this disease.

In theory, dasatinib's Src family kinase inhibition could disrupt the molecular machinery that drives Ewing sarcoma invasion and migration. Early in vitro work (2007–2008) confirmed antiproliferative and antimigratory activity in Ewing sarcoma cell lines, and more recent studies (2016–2022) have refined our understanding of the FAK-Src-tenascin-C network in this tumour. However, dasatinib as a single agent failed to demonstrate meaningful activity in the completed Phase II sarcoma basket trial (NCT00464620), and the only dedicated paediatric trial (NCT00788125) was terminated after 7 enrolments. Combination strategies targeting FAK and Src simultaneously have been proposed as a more promising direction.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|-------------|
| [NCT00788125](https://clinicaltrials.gov/study/NCT00788125) | Phase 1/2 | Terminated | 7 | Paediatric trial of dasatinib combined with ifosfamide, carboplatin, and etoposide in solid tumours including Ewing sarcoma. Early termination after only 7 patients is a significant negative signal. The reason for termination (inadequate efficacy, unacceptable toxicity, or recruitment failure) has not been confirmed in the public record — this distinction is critical for any repurposing decision. |
| [NCT00464620](https://clinicaltrials.gov/study/NCT00464620) | Phase 2 | Completed | 366 | Broad basket trial of dasatinib monotherapy in advanced sarcomas. Ewing sarcoma was included as a subgroup, but was not the primary endpoint. The overall results indicated limited single-agent activity of dasatinib across sarcoma subtypes. Ewing-specific subgroup data require review of the full publication to determine response rates in this population. |
| [NCT06500819](https://clinicaltrials.gov/study/NCT06500819) | Phase 1 | Recruiting | 41 | B7-H3 CAR-T cell immunotherapy (autologous) in children and young adults with relapsed/refractory solid tumours expressing B7-H3, including Ewing sarcoma. This is not a dasatinib trial and the mechanism is entirely different; included here as context for the current treatment landscape. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [17363602](https://pubmed.ncbi.nlm.nih.gov/17363602/) | 2007 | In vitro | Cancer Research | Dasatinib inhibits migration and invasion in diverse human sarcoma cell lines and induces apoptosis in bone sarcoma cells dependent on Src kinase for survival. Foundational preclinical evidence establishing biological plausibility in sarcoma. |
| [18202781](https://pubmed.ncbi.nlm.nih.gov/18202781/) | 2008 | In vitro | Oncology Reports | Dasatinib shows antiproliferative and antimigratory activity in Ewing sarcoma and neuroblastoma cell lines, mediated through inhibition of c-KIT and PDGFR — both expressed in these tumour types. |
| [26170970](https://pubmed.ncbi.nlm.nih.gov/26170970/) | 2015 | Review | Oncology Letters | Comprehensive review of Src signalling in sarcoma biology. Discusses Src's roles in proliferation, apoptosis resistance, invasion, and metastasis, and evaluates the feasibility of dasatinib as a targeted therapeutic. |
| [27566104](https://pubmed.ncbi.nlm.nih.gov/27566104/) | 2016 | Preclinical | Neoplasia | Micro-environmental stress (hypoxia, nutrient deprivation) drives Src-dependent invadopodia formation and cell migration in Ewing sarcoma. Dasatinib inhibited this stress-induced invasive phenotype, suggesting that combination with stress-targeting agents may be more effective. |
| [31521948](https://pubmed.ncbi.nlm.nih.gov/31521948/) | 2019 | Preclinical | Neoplasia | Tenascin-C and Src cooperate in the tumour microenvironment to promote invadopodia formation and metastasis in Ewing sarcoma. Reinforces the FAK-Src axis as a mechanistically relevant target. |
| [35655525](https://pubmed.ncbi.nlm.nih.gov/35655525/) | 2022 | Preclinical | Sarcoma | Investigation of FAK-Src complex inhibition in Ewing sarcoma, DSRCT, and rhabdomyosarcoma. Confirms that dasatinib single-agent treatment failed in the Phase II sarcoma study; proposes dual FAK+Src inhibition as the preferred combination approach. |
| [29776413](https://pubmed.ncbi.nlm.nih.gov/29776413/) | 2018 | Preclinical | Cell Commun. Signal. | CXCR4 antagonism (plerixafor) unexpectedly activates receptor tyrosine kinase signalling in Ewing sarcoma cell lines. Contextually relevant for understanding kinase crosstalk in the tumour microenvironment. |

---

## Cytotoxicity

Dasatinib is classified as an antineoplastic targeted therapy. The following parameters apply:

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — BCR-ABL / Src family kinase inhibitor (not conventional cytotoxic) |
| Myelosuppression Risk | Moderate — neutropenia, thrombocytopenia, and anaemia are commonly reported; risk is higher in advanced-phase disease and with higher doses |
| Emetogenicity Classification | Low |
| Monitoring Items | Full blood count (CBC) with differential (weekly for first 2 months, then monthly); liver function tests; renal function; QTc interval (ECG); pulmonary assessment (chest X-ray or CT if dyspnoea or cough develops) due to known pleural effusion risk |
| Handling Protection | Standard cytotoxic drug precautions apply (gloves, avoid crushing or splitting tablets); does not require the same level of containment as conventional IV chemotherapy |

---

## Safety Considerations

Formal warnings and contraindications were not available in the current evidence pack. Based on the clinical literature retrieved, the following safety signals are consistently reported with dasatinib and warrant attention:

- **Pleural effusion**: Occurs in approximately one-third of patients on long-term dasatinib therapy. A prospective multicentre study (NCT02546791, n=101 CML patients) specifically characterised its frequency and severity. Chylothorax — chyle leakage into the pleural space — has been described as a rare variant, including after years of low-dose therapy.
- **Pulmonary complications**: Case series describe dasatinib-associated interstitial pneumonitis. Patients presenting with new respiratory symptoms require prompt investigation.
- **Cardiovascular effects**: Pericardial effusion and pulmonary arterial hypertension have been reported with long-term use and should be monitored in patients with pre-existing cardiac or pulmonary conditions.

Please refer to the approved Summary of Product Characteristics (SmPC) for complete, formally validated safety information before use.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a compelling preclinical mechanistic basis (Src/FAK axis is well-documented in Ewing sarcoma biology), the available clinical evidence is insufficient and directionally negative: the dedicated paediatric Phase 1/2 trial was terminated after only 7 enrolments, and dasatinib failed as a single agent in the broader sarcoma Phase II basket trial. The clinical benefit-risk balance for Ewing sarcoma cannot currently be established with confidence.

**To proceed, the following is needed:**
- Clarification of the precise reason for early termination of NCT00788125 (efficacy failure vs. toxicity vs. operational factors) — this is the single most important missing piece of information
- Ewing sarcoma-specific subgroup efficacy and safety data from the completed Phase II trial (NCT00464620)
- Preclinical proof-of-concept for a combination strategy (e.g., dasatinib + FAK inhibitor, or dasatinib + standard VIDE/VAC chemotherapy) before any new clinical trial is designed
- Access to the official SmPC (currently not available for the Danish market context) to complete the safety assessment
- Paediatric pharmacokinetics and dosing data, given that Ewing sarcoma primarily affects children and adolescents — a population with distinct drug metabolism profiles

---

> **Disclaimer**: The results in this report are provided for research reference only and do not constitute medical advice. Drug repurposing candidates require clinical validation before application. All website pages must include a YMYL disclaimer.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

