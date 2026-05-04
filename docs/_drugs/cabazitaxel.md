---
layout: default
title: Cabazitaxel
parent: 僅模型預測 (L5)
nav_order: 81
evidence_level: L5
indication_count: 10
---

# Cabazitaxel
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

# Cabazitaxel: From Metastatic Prostate Cancer to Female Breast Carcinoma

## One-Sentence Summary

Cabazitaxel (Jevtana®) is a second-generation taxane originally approved by the FDA in 2010 for docetaxel-refractory metastatic castration-resistant prostate cancer (mCRPC). The TxGNN model predicts it may be effective for **Female Breast Carcinoma**, with a prediction confidence of **99.92%**. This prediction is supported by **0 registered clinical trials** (ClinicalTrials.gov / ICTRP) and **20 publications**, including one Phase II RCT and multiple translational studies, yielding an overall evidence level of **L2**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Metastatic castration-resistant prostate cancer (mCRPC), docetaxel-refractory |
| Predicted New Indication | Female Breast Carcinoma |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L2 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Cabazitaxel is a second-generation semisynthetic taxane that exerts its anticancer effect by binding to β-tubulin and stabilising microtubules, thereby blocking mitotic spindle disassembly and arresting tumour cells in the G2/M phase. A critical pharmacological distinction from its predecessors (paclitaxel, docetaxel) is its markedly reduced affinity for P-glycoprotein (P-gp/MDR1), the ABC transporter responsible for most clinically observed taxane resistance. This property allows cabazitaxel to retain cytotoxic activity in multidrug-resistant cell lines where docetaxel and paclitaxel fail (PMID 21076710; PMID 25416788).

Breast cancer, like prostate cancer, frequently overexpresses βIII-tubulin — an isotype associated with tumour aggressiveness and taxane resistance. Mechanistic studies have demonstrated that cabazitaxel binds more effectively to βIII-tubulin-enriched microtubules than docetaxel, translating into superior cytotoxicity in exactly those tumour subtypes most likely to relapse on standard taxane regimens (PMID 28567478). For triple-negative breast cancer (TNBC) in particular, preclinical data further show that cabazitaxel repolarises tumour-associated macrophages in a way that synergises with CD47-targeted immunotherapy, adding an immunomodulatory dimension to its direct cytotoxic effect (PMID 33753567).

Clinical translation is already underway: the GENEVIEVE Phase II RCT (PMID 28768217) directly compared cabazitaxel with weekly paclitaxel as neoadjuvant therapy in HER2-negative breast cancer, and a Phase I/II multicentre study evaluated cabazitaxel plus capecitabine in anthracycline- and taxane-pretreated metastatic breast cancer (PMID 21339064). An additional Phase II study investigated cabazitaxel combined with lapatinib in HER2+ metastatic breast cancer with CNS metastases, exploiting cabazitaxel's known ability to penetrate the blood-brain barrier (PMID 29678476). Taken together, the mechanistic rationale is strong and supported by early-phase clinical data.

---

## Clinical Trial Evidence

No clinical trials for Cabazitaxel in female breast carcinoma were retrieved from ClinicalTrials.gov or the WHO ICTRP registry at the time of data collection (2026-03-10). However, the literature references two trials with registered identifiers:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT01934894](https://clinicaltrials.gov/study/NCT01934894) | Phase II | Completed | ~35 | Cabazitaxel + lapatinib in HER2+ MBC with intracranial metastases; dose-finding results published (PMID 29678476) |

> **Note:** The GENEVIEVE trial (PMID 28768217) and the Phase I/II capecitabine combination study (PMID 21339064) were conducted prior to the current search window or under different search terms; their NCT identifiers were not captured by the automated query. Systematic manual retrieval of all registered trials is recommended.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [28768217](https://pubmed.ncbi.nlm.nih.gov/28768217/) | 2017 | Phase II RCT | Eur J Cancer | GENEVIEVE: Cabazitaxel vs weekly paclitaxel as neoadjuvant therapy in HER2-negative (TNBC and luminal B) operable breast cancer; pCR rates compared |
| [21339064](https://pubmed.ncbi.nlm.nih.gov/21339064/) | 2011 | Phase I/II | Eur J Cancer | Cabazitaxel + capecitabine in anthracycline- and taxane-pretreated metastatic breast cancer; MTD, safety, pharmacokinetics, and preliminary efficacy |
| [29678476](https://pubmed.ncbi.nlm.nih.gov/29678476/) | 2018 | Phase II | Clin Breast Cancer | Cabazitaxel + lapatinib in HER2+ MBC with intracranial metastases (NCT01934894); utilises cabazitaxel's BBB penetration |
| [33753567](https://pubmed.ncbi.nlm.nih.gov/33753567/) | 2021 | Preclinical (In Vivo + In Vitro) | J Immunother Cancer | Cabazitaxel repolarises tumour-associated macrophages, synergising with anti-CD47 immunotherapy in TNBC models |
| [28567478](https://pubmed.ncbi.nlm.nih.gov/28567478/) | 2017 | Preclinical/Translational | Cancer Chemother Pharmacol | Cabazitaxel shows superior binding and cytotoxicity vs docetaxel in βIII-tubulin-overexpressing breast cancer cells; mechanistic basis for taxane-resistant BC |
| [25416788](https://pubmed.ncbi.nlm.nih.gov/25416788/) | 2015 | Review/Mechanistic | Mol Cancer Ther | Cabazitaxel resistance mechanisms studied in MCF-7 breast cancer cells; less MDR cross-resistance than paclitaxel/docetaxel |
| [33247980](https://pubmed.ncbi.nlm.nih.gov/33247980/) | 2021 | Review/Clinical Pharmacology | Br J Clin Pharmacol | Overview of taxane PK/PD, TDM-guided dosing, and role of cabazitaxel in clinical oncology |
| [21076710](https://pubmed.ncbi.nlm.nih.gov/21076710/) | 2010 | Review | Drugs Today | Comprehensive review of cabazitaxel's pharmacokinetic profile, reduced P-gp affinity, and broad preclinical activity across cancer types |
| [30529259](https://pubmed.ncbi.nlm.nih.gov/30529259/) | 2019 | Preclinical (PDX) | J Control Release | Nanoparticle-encapsulated cabazitaxel achieved complete remission in 6/8 tumours in a basal-like patient-derived breast cancer xenograft model |
| [38562610](https://pubmed.ncbi.nlm.nih.gov/38562610/) | 2024 | Preclinical | Int J Nanomedicine | PACA nanoparticle variants of cabazitaxel in TNBC PDX model; improved efficacy and decreased M2 macrophage infiltration |

---

## Denmark Market Information

Cabazitaxel currently holds **no marketing authorisation** in Denmark (neither national authorisation via Lægemiddelstyrelsen nor centralised EMA authorisation). The drug is not listed in the Danish market.

> **Note for clinicians:** In other jurisdictions, cabazitaxel is marketed as **Jevtana®** (Sanofi) and holds EMA/FDA approval for mCRPC. Access in Denmark would require a named-patient or compassionate-use application through Lægemiddelstyrelsen.

---

## Cytotoxicity

Cabazitaxel is a conventional cytotoxic anticancer agent (taxane class) with the following profile:

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — Taxane (second-generation semisynthetic taxoid) |
| Myelosuppression Risk | **High** — Febrile neutropenia and grade 3–4 neutropenia are the primary dose-limiting toxicities; prophylactic G-CSF is strongly recommended, particularly in patients aged ≥65 or with risk factors |
| Emetogenicity Classification | Low to moderate (consistent with other intravenous taxanes) |
| Monitoring Items | Full blood count with differential (before each cycle and as clinically indicated), liver function tests (ALT, AST, bilirubin), renal function (creatinine), signs of peripheral neuropathy, hypersensitivity reactions during infusion |
| Handling Protection | Must be prepared and administered according to cytotoxic drug handling regulations; use of gloves, protective gown, and safety cabinet required; refer to institutional cytotoxic handling SOP |

---

## Safety Considerations

Detailed SmPC warnings, contraindications, and drug–drug interaction data for cabazitaxel are not available in the current Evidence Pack.

> Please refer to the approved Summary of Product Characteristics (SmPC) for Jevtana® (available via the EMA product page or national equivalents) for comprehensive safety information, including hepatic impairment dose adjustments, CYP3A4 interaction precautions, and contraindications in severe renal or hepatic insufficiency.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The TxGNN prediction of cabazitaxel for female breast carcinoma is mechanistically well-supported — the drug's ability to overcome P-gp-mediated taxane resistance and its advantage in βIII-tubulin-overexpressing tumours provide a compelling biological rationale directly applicable to taxane-resistant breast cancer subtypes (TNBC, luminal B). Early-phase clinical evidence (GENEVIEVE Phase II RCT; Phase I/II capecitabine combination; Phase II lapatinib combination) confirms human proof-of-concept, justifying advancement to a structured evidence review, though the absence of a completed Phase III trial in breast cancer and the current lack of a Denmark marketing authorisation mean guardrails are appropriate.

**To proceed, the following is needed:**

- **Comprehensive clinical trial mapping:** Manual retrieval of all registered trials (ClinicalTrials.gov, EudraCT/CTIS, ICTRP) for cabazitaxel in breast cancer subtypes, including TNBC, HER2+, and luminal B; automated search missed NCT entries present in the literature
- **Safety data completion:** Obtain and parse the Jevtana® SmPC (EMA/FDA) for full warnings, contraindications, and CYP3A4/P-gp drug–drug interaction profile to complete the S1 safety assessment
- **Mechanism of action (MOA) data:** Retrieve structured DrugBank MOA entry for DB06772 to formalise the mechanistic link score
- **Subtype-stratified evidence synthesis:** Evidence should be stratified by breast cancer subtype (TNBC vs HER2+ vs HR+/HER2−) as cabazitaxel's advantage is most pronounced in taxane-resistant and high-βIII-tubulin subtypes
- **Regulatory pathway assessment:** Evaluate requirements for a named-patient programme or EMA extension-of-indication application for Denmark, in coordination with Lægemiddelstyrelsen
- **Phase III data gap:** A prospective Phase II/III trial in taxane-pretreated metastatic breast cancer would be the critical missing piece to elevate evidence to L1

---

> **Disclaimer:** This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before any therapeutic application. All clinical decisions should be made by qualified healthcare professionals in accordance with applicable guidelines and regulations.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

