---
layout: default
title: Docetaxel
parent: 僅模型預測 (L5)
nav_order: 145
evidence_level: L5
indication_count: 10
---

# Docetaxel
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

# Docetaxel: From Advanced Solid Tumour Chemotherapy to Female Breast Carcinoma

## One-Sentence Summary

Docetaxel (Taxotere®) is a second-generation taxane cytotoxic agent with established efficacy across multiple solid tumour types, including breast cancer, non-small cell lung cancer, prostate cancer, and gastric cancer.
The TxGNN model predicts it may be effective for **Female Breast Carcinoma** with a confidence score of **99.90%**,
supported by **50 registered clinical trials** and **20 publications** in the evidence base, including multiple completed Phase 3 RCTs enrolling thousands of patients.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not captured in the Danish Medicines Agency database (data collection gap — Docetaxel holds EMA centralised authorisations for breast cancer, NSCLC, prostate cancer, gastric cancer, and head and neck cancer) |
| Predicted New Indication | Female Breast Carcinoma |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L1 |
| Denmark Market Status | Not registered in database (data collection gap — EMA centralised authorisations are valid in Denmark) |
| Number of Marketing Authorisations | 0 (data collection gap) |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Docetaxel is a semisynthetic taxane derived from the European yew tree (*Taxus baccata*). It acts by binding to and stabilising the β-tubulin subunit of assembled microtubules, preventing their depolymerisation. This disrupts normal mitotic spindle dynamics, arresting tumour cells in the G2/M phase and ultimately triggering apoptosis. Unlike vinca alkaloids — which inhibit microtubule polymerisation — docetaxel promotes microtubule hyperstabilisation, making it particularly potent against rapidly dividing cells. Docetaxel also inhibits the anti-apoptotic proteins Bcl-2 and Bcl-xL by preventing their phosphorylation, thereby lowering the apoptotic threshold in cancer cells. (Note: mechanism of action data was not retrieved from DrugBank in this evidence pack; the above reflects established pharmacological knowledge.)

Female breast carcinoma — particularly the HER2-positive and triple-negative (TNBC) subtypes — is characterised by rapid cellular proliferation and strong dependence on intact mitotic machinery. Docetaxel's dual mechanism of microtubule stabilisation and Bcl-2 inhibition is therefore directly applicable to these highly proliferative tumour cells. The drug also demonstrates synergistic activity when combined with anthracyclines (doxorubicin, epirubicin), HER2-targeted antibodies (trastuzumab, pertuzumab), and VEGF inhibitors (bevacizumab), all of which are standard combination partners in breast cancer treatment protocols.

The TxGNN prediction of 99.90% is strongly corroborated by decades of clinical evidence: docetaxel has been a cornerstone of breast cancer chemotherapy since its initial regulatory approval in the mid-1990s. It is active and guideline-recommended in adjuvant, neoadjuvant, and metastatic settings, with robust Phase 3 data supporting its use across all major breast cancer subtypes. The model's prediction is essentially a high-confidence confirmation of established clinical practice.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT00054587](https://clinicaltrials.gov/study/NCT00054587) | Phase 3 | Completed | 3,010 | Large multicenter RCT comparing Docetaxel 75 mg/m² + Epirubicin versus FEC100 in node-positive non-metastatic breast cancer; sequential Herceptin added in HER2+++ subgroup — among the largest Phase 3 trials directly evaluating docetaxel in breast cancer |
| [NCT00333775](https://clinicaltrials.gov/study/NCT00333775) | Phase 3 | Completed | 736 | AVADO trial: double-blind RCT of Bevacizumab (7.5 or 15 mg/kg) plus Docetaxel versus Docetaxel plus placebo as first-line treatment in HER2-negative metastatic breast cancer |
| [NCT00887536](https://clinicaltrials.gov/study/NCT00887536) | Phase 3 | Completed | 1,613 | Three-arm RCT: TC (Docetaxel+Cyclophosphamide) ± Bevacizumab versus TAC (Docetaxel+Doxorubicin+Cyclophosphamide) in node-positive or high-risk HER2-negative early breast cancer |
| [NCT01572038](https://clinicaltrials.gov/study/NCT01572038) | Phase 3 | Completed | 1,436 | PERUSE study: Pertuzumab + Trastuzumab + Taxane (docetaxel, paclitaxel, or nab-paclitaxel) as first-line treatment in HER2-positive advanced breast cancer — evaluated safety and tolerability in a real-world-like setting |
| [NCT00004125](https://clinicaltrials.gov/study/NCT00004125) | Phase 3 | Completed | N/A | AC chemotherapy followed by weekly versus every-3-weeks Docetaxel or Paclitaxel in axillary node-positive Stage II/IIIA breast cancer — compared taxane scheduling |
| [NCT01354522](https://clinicaltrials.gov/study/NCT01354522) | Phase 3 | Completed | 204 | TAC (Docetaxel+Doxorubicin+Cyclophosphamide) versus TCX (Docetaxel+Cyclophosphamide+Capecitabine) as adjuvant treatment in high-risk HER2-negative breast cancer |
| [NCT00047099](https://clinicaltrials.gov/study/NCT00047099) | Phase 3 | Completed | 446 | FEC versus EC-Docetaxel (sequential) as adjuvant chemotherapy in primary breast cancer — evaluated disease-free and overall survival post-surgery |
| [NCT00963729](https://clinicaltrials.gov/study/NCT00963729) | Phase 3 | Completed | 756 | Neoadjuvant combination chemotherapy (docetaxel-based) versus letrozole in postmenopausal patients with primary breast cancer — compared pathological complete response and tumour downstaging |
| [NCT00321633](https://clinicaltrials.gov/study/NCT00321633) | Phase 2 | Completed | 148 | Randomised Phase II pilot: Carboplatin versus Docetaxel in women with metastatic BRCA-mutation-positive breast cancer — directly compared docetaxel efficacy |
| [NCT00217672](https://clinicaltrials.gov/study/NCT00217672) | Phase 2 | Completed | 76 | Randomised Phase II: Docetaxel with or without Bevacizumab as first-line therapy in HER2-negative metastatic breast cancer — evaluated docetaxel as monotherapy backbone |

*EudraCT (EU Clinical Trials Register) identifiers were not available in the evidence pack for the above trials.*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [28398846](https://pubmed.ncbi.nlm.nih.gov/28398846/) | 2017 | RCT | J Clin Oncol | ABC Trials (USOR 06-090, NSABP B-46-I/USOR 07132, NSABP B-49): assessed whether TC×6 is non-inferior to anthracycline-taxane (TaxAC) combinations as adjuvant therapy in early breast cancer |
| [26874836](https://pubmed.ncbi.nlm.nih.gov/26874836/) | 2017 | Prospective Phase II | Breast Cancer (Tokyo) | Docetaxel + cyclophosphamide + trastuzumab (HER-TC) as neoadjuvant chemotherapy for HER2-positive primary breast cancer; evaluated pCR rates by hormone receptor status and tolerability |
| [16020974](https://pubmed.ncbi.nlm.nih.gov/16020974/) | 2005 | Phase II | Oncology | Multicenter Phase II study of weekly docetaxel + gemcitabine as first-line treatment for metastatic breast cancer; assessed clinical efficacy, toxicity, and dose intensity |
| [9282422](https://pubmed.ncbi.nlm.nih.gov/9282422/) | 1997 | Review | Drug Ther Bull | Early comparative review of paclitaxel and docetaxel in breast and ovarian cancer; documents the initial clinical evidence base and licensing context for both taxanes |
| [27997437](https://pubmed.ncbi.nlm.nih.gov/27997437/) | 2017 | Cohort | Anti-Cancer Drugs | Retrospective cohort study evaluating the association between adjuvant docetaxel-based chemotherapy and breast cancer-related lymphedema in Stage II/III patients |
| [12599222](https://pubmed.ncbi.nlm.nih.gov/12599222/) | 2003 | Phase I/II | Cancer | Capecitabine + docetaxel + epirubicin (TEX regimen) as first-line treatment for locally advanced or metastatic breast carcinoma; assessed activity and toxicity profile |
| [19755993](https://pubmed.ncbi.nlm.nih.gov/19755993/) | 2009 | Translational/Cohort | Br J Cancer | Microarray gene expression profiling to identify predictive markers of pathological complete response (pCR) to trastuzumab-docetaxel based treatment in HER2-positive breast carcinoma |
| [19856651](https://pubmed.ncbi.nlm.nih.gov/19856651/) | 2009 | Phase I/II | Tumori | Docetaxel + gemcitabine dose-finding study in metastatic breast cancer patients previously treated with anthracyclines; explored weekly scheduling for improved tolerability |
| [15585076](https://pubmed.ncbi.nlm.nih.gov/15585076/) | 2004 | Phase II | Clin Breast Cancer | Phase II trial of docetaxel + cisplatin as primary neoadjuvant chemotherapy for locally advanced breast cancer (tumours ≥5 cm); evaluated pCR rates and downstaging before mastectomy |
| [9364543](https://pubmed.ncbi.nlm.nih.gov/9364543/) | 1997 | Phase I/II | Oncology (NY) | Early review of combination docetaxel/vinorelbine in metastatic breast cancer and NSCLC; documents single-agent and combination activity data from Phase I/II trials |

---

## Denmark Market Information

The Danish Medicines Agency database query returned **0 marketing authorisations** for Docetaxel. This is almost certainly a **data collection gap** rather than genuine non-availability in Denmark. Docetaxel (Taxotere®, originator: Sanofi-Aventis/Accord Healthcare) and multiple generic formulations hold valid EMA centralised marketing authorisations applicable across all EU/EEA member states, including Denmark. A manual verification with Lægemiddelstyrelsen and the EMA EPAR database is strongly recommended before clinical planning.

Pending manual verification, the following authorisations are expected to be retrievable:

| Expected Product | Dosage Form | Holder | Status |
|-----------------|-------------|--------|--------|
| Taxotere® (originator) | Concentrate for solution for infusion | Sanofi-Aventis | Centralised EMA (EU-wide) |
| Docetaxel generics | Concentrate for solution for infusion | Multiple MAHs | Centralised EMA (EU-wide) |

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — Taxane class (antimicrotubule / microtubule-stabilising agent) |
| Myelosuppression Risk | **High** — neutropenia is the dose-limiting toxicity; febrile neutropenia occurs in approximately 10–15% of patients at standard doses (75–100 mg/m²) without G-CSF prophylaxis; prophylactic G-CSF (e.g., filgrastim, pegfilgrastim) is recommended in most regimens |
| Emetogenicity Classification | Low to moderate (ASCO/MASCC classification: low emetogenic potential at standard monotherapy doses; may increase with combination regimens) |
| Monitoring Items | Complete blood count with differential (before each cycle and at nadir), liver function tests (bilirubin, ALT, AST, alkaline phosphatase — dose modifications required for hepatic impairment), body weight and oedema monitoring for fluid retention syndrome, peripheral neuropathy assessment (NCI-CTCAE grading) |
| Handling Protection | Classified as a hazardous cytotoxic drug — preparation and administration must follow cytotoxic handling regulations; closed system transfer devices (CSTDs) recommended during compounding; full personal protective equipment (gloves, gown, eye protection, and mask) required |

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for complete safety information. No formal safety data was captured from the Danish/EU regulatory database in this evidence pack.

Based on established pharmacological knowledge, the following safety areas require clinical attention:

- **Hypersensitivity reactions**: Pre-medication with oral corticosteroids (typically dexamethasone 8 mg twice daily, starting the day before docetaxel administration for 3 days) is **mandatory** to reduce the risk of severe hypersensitivity reactions and cumulative fluid retention syndrome.
- **Severe neutropenia**: Neutropenia is the primary dose-limiting toxicity; prophylactic G-CSF should be considered per ESMO/ASCO guidelines. Dose reductions are required following Grade 4 or febrile neutropenia.
- **Fluid retention syndrome**: Cumulative and progressive, managed with corticosteroid premedication; severe or refractory cases may require dose reduction or treatment discontinuation.
- **Cumulative peripheral sensory neuropathy**: Grade 2 or higher neuropathy typically requires dose reduction; Grade 3–4 requires treatment discontinuation.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The evidence base for Docetaxel in female breast carcinoma represents the highest available evidence level (L1), underpinned by multiple completed Phase 3 RCTs with combined enrolment of several thousand patients across adjuvant, neoadjuvant, and metastatic settings. The TxGNN prediction of 99.90% is a high-confidence confirmation of established international clinical practice. The primary barrier to deployment in the Danish context is a data collection gap in the local regulatory database — not any clinical efficacy concern.

**To proceed, the following is needed:**
- Verify Danish/EU marketing authorisation status directly with Lægemiddelstyrelsen and the EMA centralised authorisation database (search for Taxotere® and docetaxel generic products)
- Retrieve the current EU SmPC for complete contraindications, warnings, drug interaction data, dosing guidance, and dose modification rules for hepatic impairment
- Confirm corticosteroid pre-medication protocols and G-CSF prophylaxis strategies aligned with Danish/Nordic oncology guidelines (e.g., Danish Breast Cancer Group — DBCG)
- Establish a safety monitoring plan covering: neutropenia surveillance, fluid retention management, peripheral neuropathy grading, and hepatic function monitoring
- Identify the appropriate breast cancer subgroup and partner regimen (e.g., docetaxel + trastuzumab ± pertuzumab for HER2-positive disease; docetaxel + cyclophosphamide or anthracycline-based regimens for HER2-negative disease) in alignment with current ESMO and DBCG clinical practice guidelines

> **Disclaimer**: This report is intended for research reference purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before application. All treatment decisions must be based on approved SmPC, current clinical guidelines, and individual patient assessment.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

