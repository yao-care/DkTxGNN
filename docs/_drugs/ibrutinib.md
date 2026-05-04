---
layout: default
title: Ibrutinib
parent: 僅模型預測 (L5)
nav_order: 218
evidence_level: L5
indication_count: 10
---

# Ibrutinib
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

# Ibrutinib: From B-Cell Malignancies to Monoclonal Paraproteinemia Disease

## One-Sentence Summary

Ibrutinib is a first-generation irreversible BTK (Bruton's Tyrosine Kinase) inhibitor, globally approved for multiple B-cell malignancies including CLL, MCL, and Waldenström's Macroglobulinemia, but currently not registered in Denmark.
The TxGNN model predicts it may be effective for **Monoclonal Paraproteinemia Disease (Waldenström's Macroglobulinemia)** with a score of **91.16%**,
supported by **13 clinical trials** and **20 publications** — including two completed Phase 3 RCTs — placing this at **L1 evidence level**.

> **Note on highest-ranked TxGNN prediction**: The single highest TxGNN score (91.75%) was assigned to *polyclonal hypergammaglobulinemia*, but no clinical trials or literature were identified for this indication. The present report therefore focuses on **monoclonal paraproteinemia disease**, which carries L1 evidence and a direct mechanistic link to ibrutinib's established mechanism of action.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Denmark; globally approved (EMA/FDA) for CLL, MCL, Waldenström's Macroglobulinemia, and Marginal Zone Lymphoma |
| Predicted New Indication | Monoclonal Paraproteinemia Disease (Waldenström's Macroglobulinemia) |
| TxGNN Prediction Score | 91.16% |
| Evidence Level | L1 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Ibrutinib acts as an irreversible covalent inhibitor of Bruton's Tyrosine Kinase (BTK) by binding to the Cys481 residue. This blocks downstream B-cell receptor (BCR) signalling cascades — including PLCγ2, NF-κB, and PI3K/MAPK — suppressing malignant B-cell proliferation, survival, and differentiation into paraprotein-secreting plasma cells. Although detailed MOA data from DrugBank was not retrieved in this evidence pack, ibrutinib's mechanism is extensively described in the published literature cited below.

In monoclonal paraproteinemia diseases, particularly Waldenström's Macroglobulinemia (WM), the neoplastic lymphoplasmacytic cells carry the somatic MYD88 L265P mutation in approximately 90% of cases. This mutation constitutively activates the IRAK4→BTK signalling axis, creating a state of BTK dependency. Ibrutinib directly disrupts this activated pathway, inducing tumour B-cell apoptosis and reducing secretion of the pathognomonic monoclonal IgM paraprotein — the driver of WM's clinical complications including hyperviscosity, cytopenias, and neuropathy.

The TxGNN prediction is fully consistent with established clinical evidence and global regulatory approvals. The pivotal iNNOVATE Phase 3 trial (NCT02165397, n=181) established ibrutinib + rituximab as superior to rituximab alone in WM, and the ASPEN Phase 3 trial (NCT03053440, n=201) confirmed ibrutinib as an active BTK inhibitor in this disease. Ibrutinib (Imbruvica®) holds EMA centralised marketing authorisation for WM. From a Danish perspective, the challenge is not lack of efficacy evidence, but rather the absence of national registration — making this a market access question as much as a repurposing question.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT02165397](https://clinicaltrials.gov/study/NCT02165397) | Phase 3 | Completed | 181 | iNNOVATE: Double-blind RCT of ibrutinib + rituximab vs. placebo + rituximab in WM; pivotal EMA/FDA registration trial demonstrating superiority of the ibrutinib combination |
| [NCT03053440](https://clinicaltrials.gov/study/NCT03053440) | Phase 3 | Completed | 201 | ASPEN: Randomised head-to-head comparison of zanubrutinib vs. ibrutinib in MYD88-mutated WM; both arms demonstrated activity, with zanubrutinib showing a more favourable toxicity profile |
| [NCT04061512](https://clinicaltrials.gov/study/NCT04061512) | Phase 2/3 | Recruiting | 148 | RAINBOW: Ongoing randomised trial comparing ibrutinib + rituximab vs. standard DRC (dexamethasone, rituximab, cyclophosphamide) as first-line therapy in WM |
| [NCT04840602](https://clinicaltrials.gov/study/NCT04840602) | Phase 2 | Recruiting | 92 | Randomised comparison of BTK inhibitors (ibrutinib + rituximab or zanubrutinib) vs. venetoclax + rituximab in previously untreated WM/LPL |
| [NCT03620903](https://clinicaltrials.gov/study/NCT03620903) | Phase 2 | Active, not recruiting | 53 | Bortezomib + rituximab + ibrutinib (B-RI) triplet as first-line therapy in treatment-naïve WM patients |
| [NCT04062448](https://clinicaltrials.gov/study/NCT04062448) | Phase 2 | Completed | 16 | Ibrutinib + rituximab in Japanese WM patients (treatment-naïve and relapsed/refractory); evaluated overall response rate by independent review |
| [NCT01479842](https://clinicaltrials.gov/study/NCT01479842) | Phase 1 | Active, not recruiting | 48 | Dose-escalation study of BTK inhibitor + rituximab + bendamustine in R/R NHL including WM-spectrum B-cell malignancies; safety and PK data |
| [NCT07169565](https://clinicaltrials.gov/study/NCT07169565) | Phase 1 | Not yet recruiting | 21 | Time-limited ibrutinib followed by BR (bendamustine + rituximab) regimen in WM; 3+3 dose-escalation design to establish RP2D |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [32731259](https://pubmed.ncbi.nlm.nih.gov/32731259/) | 2020 | RCT Phase 3 | Blood | ASPEN trial: phase 3 randomised comparison of zanubrutinib vs. ibrutinib in symptomatic WM; confirms ibrutinib as active standard, with zanubrutinib achieving numerically higher complete/VGPR rates |
| [38315878](https://pubmed.ncbi.nlm.nih.gov/38315878/) | 2024 | Biomarker analysis | Blood Advances | ASPEN post-hoc analysis: MYD88 and CXCR4 mutation status predicts differential BTK inhibitor response; CXCR4 mutations associated with reduced ibrutinib efficacy |
| [39626287](https://pubmed.ncbi.nlm.nih.gov/39626287/) | 2025 | Sub-analysis | Blood Advances | Peripheral neuropathy resolution with zanubrutinib vs. ibrutinib in the ASPEN WM cohort; ibrutinib associated with greater neuropathy burden |
| [32603202](https://pubmed.ncbi.nlm.nih.gov/32603202/) | 2020 | Review | Expert Opinion on Pharmacotherapy | Comprehensive evaluation of ibrutinib's role in WM: genomic predictors, clinical trial landscape, resistance mechanisms, and evolving treatment paradigm |
| [33273682](https://pubmed.ncbi.nlm.nih.gov/33273682/) | 2021 | Review | Leukemia | CXCR4 mutations in WM: mechanistic role and implications for ibrutinib response, treatment sequencing, and novel targeting strategies |
| [31591468](https://pubmed.ncbi.nlm.nih.gov/31591468/) | 2019 | Review | Leukemia | Updated WM treatment landscape; ibrutinib and combination regimens as backbone of current and emerging therapy |
| [29169431](https://pubmed.ncbi.nlm.nih.gov/29169431/) | 2017 | Review | Deutsches Ärzteblatt International | Systematic differential diagnosis approach to IgM monoclonal gammopathies including WM, MGUS, and lymphoma subtypes; therapeutic implications |
| [27825468](https://pubmed.ncbi.nlm.nih.gov/27825468/) | 2016 | Review | Best Practice & Research Clin. Haematol. | Novel therapeutic targets in WM: MYD88-BTK axis, CXCR4 signalling, and emerging preclinical and clinical data on ibrutinib |
| [27825466](https://pubmed.ncbi.nlm.nih.gov/27825466/) | 2016 | Review | Best Practice & Research Clin. Haematol. | Evidence-based treatment guidelines for WM; disease burden and patient characteristics guiding treatment selection including ibrutinib |
| [25679974](https://pubmed.ncbi.nlm.nih.gov/25679974/) | 2015 | Review | Clin. Adv. Hematol. Oncol. | WM clinical overview: IPSSWM prognostic stratification, survival outcomes, and incorporation of targeted agents including ibrutinib |

---

## Denmark Market Information

Ibrutinib is currently **not registered** in Denmark. No marketing authorisations are recorded in the Danish Medicines Agency (Lægemiddelstyrelsen) database.

> **Pathway note for Danish healthcare professionals**: Ibrutinib is authorised in Europe under the EMA centralised procedure as **Imbruvica®** (Janssen-Cilag International NV), with approved indications including CLL/SLL, MCL, WM, and MZL. Danish patients may potentially access ibrutinib via a *særlig tilladelse* (special import authorisation) or named-patient programme through Lægemiddelstyrelsen pending a formal national reimbursement submission.

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — irreversible BTK inhibitor (kinase inhibitor; not conventional cytotoxic) |
| Myelosuppression Risk | Low to moderate; neutropenia and thrombocytopenia are reported adverse events, but arise primarily from disease-related bone marrow infiltration rather than direct cytotoxicity; less myelosuppressive than conventional chemotherapy regimens |
| Emetogenicity Classification | Minimal to low (oral kinase inhibitor class) |
| Monitoring Items | Full blood count with differential (CBC), liver function (ALT/AST), renal function, cardiac monitoring (12-lead ECG, blood pressure — due to atrial fibrillation and hypertension risk), bleeding history assessment |
| Handling Protection | Standard oral oncology precautions apply; does not require dedicated cytotoxic preparation facilities or CSTD (closed system transfer devices) |

---

## Safety Considerations

The SmPC-level warnings and contraindications specific to the Danish/EMA label were not retrieved in the current evidence pack.

Please refer to the approved Summary of Product Characteristics (SmPC) for Imbruvica® on the [EMA product database](https://www.ema.europa.eu/en/medicines/human/EPAR/imbruvica) for complete safety information.

**Known class-specific safety signals** (documented in the published Phase 3 literature cited above):

- **Atrial fibrillation / flutter**: Reported in 6–9% of WM patients; baseline and on-treatment cardiac monitoring is required; caution in patients with pre-existing arrhythmia
- **Major haemorrhage and bleeding**: BTK inhibition affects GPVI-mediated platelet activation; ibrutinib should be interrupted peri-operatively; co-administration with anticoagulants requires individual risk–benefit assessment
- **Hypertension**: Frequently observed; requires active monitoring and antihypertensive management
- **Serious infections**: Increased susceptibility to bacterial, viral, and fungal infections; Pneumocystis jirovecii pneumonia prophylaxis recommended in high-risk patients
- **CYP3A4 drug interactions**: Strong CYP3A4 inhibitors (e.g., azole antifungals, clarithromycin) markedly increase ibrutinib exposure; strong inducers (e.g., rifampicin, carbamazepine) substantially reduce efficacy — dose adjustment or alternative agents required

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Ibrutinib holds Level 1 evidence for Waldenström's Macroglobulinemia — the prototypical monoclonal paraproteinemia disease — based on two completed Phase 3 RCTs (iNNOVATE and ASPEN), multiple Phase 2 trials, and an established EMA centralised marketing authorisation (Imbruvica®). The TxGNN prediction is fully consistent with the known mechanistic link through the MYD88→BTK signalling axis. The primary barrier to use in Denmark is the **absence of national registration and reimbursement**, not a lack of efficacy or safety evidence.

**To proceed, the following is needed:**

- Confirm the access pathway in Denmark: evaluate eligibility for *særlig tilladelse* (special import authorisation) via Lægemiddelstyrelsen for individual patients with symptomatic WM
- Review the full EMA SmPC for Imbruvica® to complete the safety and contraindication assessment prior to any clinical use
- Confirm patient-level MYD88 mutation status (L265P) prior to initiation — MYD88 wild-type disease shows markedly reduced ibrutinib response
- Perform baseline cardiac assessment (ECG, blood pressure) and bleeding risk evaluation
- Conduct a formal drug interaction review, particularly for CYP3A4-modifying medications common in the elderly WM population
- Consider a formal national reimbursement submission to Medicinrådet if ibrutinib is intended for broader use in Danish WM patients
- Monitor the ongoing RAINBOW Phase 2/3 trial (NCT04061512, completion 2030) which will provide comparative data for ibrutinib + rituximab vs. standard DRC as first-line therapy
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

