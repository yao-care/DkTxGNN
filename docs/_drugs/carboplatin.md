---
layout: default
title: Carboplatin
parent: 僅模型預測 (L5)
nav_order: 92
evidence_level: L5
indication_count: 10
---

# Carboplatin
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

# Carboplatin: From Ovarian Cancer to Female Breast Carcinoma

## One-Sentence Summary

Carboplatin is a platinum-based cytotoxic chemotherapy agent, globally established as a backbone treatment for ovarian cancer and other solid tumours, though it currently holds no marketing authorisation in Denmark.
The TxGNN model predicts it may be effective for **Female Breast Carcinoma** — with a prediction score of **99.86%** — and this direction is supported by **more than 30 clinical trials** and **20 peer-reviewed publications**, including multiple completed Phase 2/3 randomised trials demonstrating improved pathological complete response (pCR) rates in triple-negative and BRCA-mutated breast cancer.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Ovarian cancer (global standard of care; not registered in Denmark — see Denmark Market Information) |
| Predicted New Indication | Female Breast Carcinoma |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L1 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Carboplatin is a second-generation platinum compound that kills cancer cells by forming covalent cross-links both within a single DNA strand (intra-strand adducts) and between opposing strands (inter-strand cross-links). This structural damage stalls the DNA replication machinery and triggers programmed cell death (apoptosis). Although detailed DrugBank mechanism data were unavailable for this report, carboplatin's mechanism is well established in the literature and confirmed by the evidence pack's repurposing rationale.

The mechanistic link to breast cancer is particularly compelling in two subtypes. First, triple-negative breast cancer (TNBC) and BRCA1/2-mutated breast cancers carry defects in homologous recombination DNA repair (HRD). Because these tumours cannot efficiently repair platinum-induced DNA damage, they are disproportionately sensitive to carboplatin — a concept validated by the landmark GeparSixto trial (Lancet Oncology, 2014), which showed a significant improvement in pCR when carboplatin was added to neoadjuvant chemotherapy in TNBC. Second, HER2-positive breast cancer is routinely treated with the TCHP regimen (docetaxel, carboplatin, trastuzumab, pertuzumab), supported by multiple Phase 2/3 trials; carboplatin in this context is not truly experimental but rather a guideline-concordant backbone agent.

An additional biological rationale involves the concept of synthetic lethality: carboplatin-induced DNA damage combined with PARP inhibition creates a lethal repair burden in HRD-deficient cells that cannot survive either type of insult. Multiple clinical trials (BROCADE3, ZAP-IT) are actively exploiting this synergy, further reinforcing the TxGNN model's prediction.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01426880](https://clinicaltrials.gov/study/NCT01426880) | Phase 2/3 | Completed | 595 | GeparSixto-adjacent design: randomised addition of carboplatin to standard anthracycline/taxane (± trastuzumab) neoadjuvant chemotherapy in TNBC and HER2+ early breast cancer; directly evaluated carboplatin contribution to pCR improvement |
| [NCT03168880](https://clinicaltrials.gov/study/NCT03168880) | Phase 3 | Active, not recruiting | 720 | RCT of neoadjuvant weekly paclitaxel vs weekly paclitaxel + weekly carboplatin in large operable or locally advanced TNBC; high-powered study in Sub-Saharan African population |
| [NCT00321633](https://clinicaltrials.gov/study/NCT00321633) | Phase 2 | Completed | 148 | Randomised head-to-head comparison of carboplatin vs docetaxel in metastatic BRCA-mutated (genetic) breast cancer; one of few direct carboplatin monotherapy efficacy trials in breast cancer |
| [NCT04159142](https://clinicaltrials.gov/study/NCT04159142) | Phase 2 | Recruiting | 414 | Multi-centre open-label RCT comparing nab-paclitaxel + carboplatin vs nab-paclitaxel + capecitabine in advanced TNBC; large ongoing trial evaluating first-line combination strategies |
| [NCT02413320](https://clinicaltrials.gov/study/NCT02413320) | Phase 2 | Completed | 101 | Randomised neoadjuvant trial: carboplatin + docetaxel or carboplatin + paclitaxel, followed by doxorubicin/cyclophosphamide, in Stage I-III TNBC; directly assessed optimal carboplatin pairing |
| [NCT01366144](https://clinicaltrials.gov/study/NCT01366144) | Phase 1 | Active, not recruiting | 94 | Veliparib (PARP inhibitor) + carboplatin + paclitaxel in solid tumours with hepatic/renal dysfunction; includes breast cancer cohort, exploring PARP-platinum synthetic lethality |
| [NCT06351332](https://clinicaltrials.gov/study/NCT06351332) | Phase 1/2 | Active, not recruiting | 78 | ZAP-IT trial: azenosertib (WEE1 inhibitor) + carboplatin + pembrolizumab in metastatic TNBC; novel triple combination targeting DNA damage response in immunotherapy setting |
| [NCT00616967](https://clinicaltrials.gov/study/NCT00616967) | Phase 2 | Active, not recruiting | 68 | Double-blind RCT of carboplatin + nab-paclitaxel ± vorinostat (HDAC inhibitor) as preoperative chemotherapy in HER2-negative operable breast cancer; evaluates epigenetic sensitisation |
| [NCT05843292](https://clinicaltrials.gov/study/NCT05843292) | Phase 4 | Not yet recruiting | 48 | Short-term sintilimab (anti-PD-1) + taxane + carboplatin neoadjuvant therapy in early-stage TNBC; assesses optimal immunotherapy integration duration |
| [NCT05861830](https://clinicaltrials.gov/study/NCT05861830) | Phase 3 | Recruiting | 80 | Exploratory Phase 3: dalpiciclib (CDK4/6 inhibitor) + endocrine therapy ± carboplatin in HR+/HER2- recurrent/metastatic breast cancer after CDK4/6 inhibitor failure; uses 18F-FES PET/CT to predict response |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24794243](https://pubmed.ncbi.nlm.nih.gov/24794243/) | 2014 | RCT (Phase 2/3) | The Lancet Oncology | GeparSixto trial: carboplatin added to neoadjuvant paclitaxel/non-pegylated liposomal doxorubicin significantly increased pCR in TNBC (53.2% vs 36.9%); synergy also explored in HER2+ breast cancer |
| [33208340](https://pubmed.ncbi.nlm.nih.gov/33208340/) | 2021 | RCT (Phase 2) | Clinical Cancer Research | NeoSTOP trial: multisite randomised Phase II comparing anthracycline-free (carboplatin + paclitaxel) vs anthracycline-containing carboplatin regimens in Stage I-III TNBC; both arms yielded encouraging pCR rates, supporting anthracycline-free options |
| [39671272](https://pubmed.ncbi.nlm.nih.gov/39671272/) | 2025 | RCT | JAMA | CamRelief trial: camrelizumab (PD-1 inhibitor) + standard neoadjuvant chemotherapy (including platinum) vs placebo + chemotherapy in early/locally advanced TNBC; demonstrated improved pCR with immunotherapy addition |
| [40593759](https://pubmed.ncbi.nlm.nih.gov/40593759/) | 2025 | RCT (Phase 2b) | Nature Communications | MUKDEN 06: ARX788 (anti-HER2 ADC) + pyrotinib vs standard TCbHP (docetaxel, carboplatin, trastuzumab, pertuzumab) neoadjuvant in HER2+ breast cancer; carboplatin-containing arm serves as reference standard |
| [38309017](https://pubmed.ncbi.nlm.nih.gov/38309017/) | 2024 | Phase 3 RCT (final OS) | European Journal of Cancer | BROCADE3 final OS analysis: veliparib + carboplatin + paclitaxel vs placebo + carboplatin + paclitaxel in germline BRCA1/2-mutated HER2-negative advanced breast cancer; confirmed PFS benefit with veliparib addition |
| [16720915](https://pubmed.ncbi.nlm.nih.gov/16720915/) | 2006 | Systematic Review | Medical Oncology | Comprehensive synthesis of paclitaxel-carboplatin combination in advanced breast cancer; established evidence for synergy, single-agent activity of carboplatin, and non-cross-resistance with anthracyclines |
| [25247558](https://pubmed.ncbi.nlm.nih.gov/25247558/) | 2014 | Meta-analysis | PLoS One | Meta-analysis confirming both carboplatin and bevacizumab independently improve pCR rates in neoadjuvant treatment of TNBC; supports carboplatin's role as an efficacy-enhancing backbone agent |
| [40779028](https://pubmed.ncbi.nlm.nih.gov/40779028/) | 2025 | Phase 1 Trial | Breast Cancer Research & Treatment | Phase I trial of mifepristone (glucocorticoid receptor antagonist) + carboplatin + gemcitabine in advanced breast and recurrent ovarian cancer; explores GR-mediated carboplatin resistance |
| [33256829](https://pubmed.ncbi.nlm.nih.gov/33256829/) | 2020 | Phase 2 Trial | Breast Cancer Research | Phase II trial of carboplatin + bevacizumab in breast cancer brain metastases; demonstrated feasibility and preliminary efficacy in this difficult-to-treat population |
| [40817986](https://pubmed.ncbi.nlm.nih.gov/40817986/) | 2025 | Phase 2 RCT | Breast Cancer Research & Treatment | Randomised Phase II: single-agent carboplatin vs carboplatin + everolimus (mTOR inhibitor) in advanced TNBC; investigates whether mTOR pathway inhibition enhances platinum sensitivity in PTEN-loss tumours |

---

## Denmark Market Information

Carboplatin is currently **not marketed in Denmark** and holds no active marketing authorisations with Laegemiddelstyrelsen (the Danish Medicines Agency). No licences were identified in the regulatory dataset.

> **Note for clinicians:** Carboplatin is a well-established generic chemotherapy agent available under EMA-centralised marketing authorisations and numerous national authorisations across EU member states (e.g., under brand names including Paraplatin and multiple generics). Its absence from the Danish register may reflect data completeness at the time of this report rather than absence from clinical use. Danish oncology centres may access carboplatin through hospital procurement channels or named-patient import provisions. Verification with Laegemiddelstyrelsen's current online register is recommended before clinical decision-making.

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — Platinum compound (alkylating-like mechanism via DNA cross-linking) |
| Myelosuppression Risk | **High** — thrombocytopenia is the primary dose-limiting toxicity; Grade 3/4 anaemia reported in 30–40% of patients receiving neoadjuvant TCHP regimen (PMID 35837812); neutropenia common but typically less severe than with cisplatin |
| Emetogenicity Classification | **Moderate to high** — emetogenicity is dose-dependent; AUC-based dosing (Calvert formula) affects emetic potential; 5-HT3 antagonist + NK1 antagonist + dexamethasone prophylaxis recommended |
| Monitoring Items | Full blood count with differential (before each cycle and as clinically indicated); serum creatinine and eGFR (required for Calvert formula dose calculation); liver function tests; audiometry for patients receiving high-dose or cumulative carboplatin regimens |
| Handling Protection | Must be prepared and handled in accordance with cytotoxic drug handling regulations; preparation in a certified pharmacy under a biological safety cabinet; personnel to use appropriate personal protective equipment (PPE) including gloves, gown, and eye protection |

---

## Safety Considerations

Detailed warnings, contraindications, and drug interaction data were not available in this Evidence Pack (classified as data gaps). Please refer to the approved Summary of Product Characteristics (SmPC) for complete safety information.

> **Key safety considerations from established oncology practice** (for reference only — clinicians must consult the current SmPC):
> - **Dose calculation**: Carboplatin dose must be calculated using the Calvert formula (dose [mg] = AUC × [GFR + 25]); renal function must be assessed before each cycle
> - **Hypersensitivity reactions**: Risk increases with cumulative exposure (typically after ≥6 cycles); desensitisation protocols may be required
> - **Ototoxicity**: Clinically significant at high doses (e.g., TI-CE salvage regimen in germ cell tumours); relevant when combining with aminoglycosides or loop diuretics
> - **Peripheral neuropathy**: Less pronounced than with cisplatin or paclitaxel, but additive when combined with taxanes
> - **Nephrotoxicity**: Less nephrotoxic than cisplatin but GFR monitoring is essential

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The evidence base for carboplatin in female breast carcinoma is among the strongest available for any drug repurposing candidate in this dataset, with Level 1 evidence derived from multiple completed Phase 2/3 randomised controlled trials (including GeparSixto, NeoSTOP, BROCADE3) demonstrating clinically meaningful improvements in pCR and progression-free survival. The biological rationale — HRD-driven platinum sensitivity in TNBC and BRCA-mutated subtypes, and established guideline use in HER2+ neoadjuvant TCHP regimens — is robust and well mechanistically grounded.

**To proceed, the following is needed:**

- **Regulatory clarification**: Confirm whether carboplatin can be sourced through EMA centralised marketing authorisation, national import, or hospital exemption under Danish law; contact Laegemiddelstyrelsen for current status
- **Safety documentation**: Retrieve the full SmPC to complete contraindication and drug interaction assessment (currently blocking data gaps DG001 and DG002)
- **Patient population definition**: Specify target subtype precisely — TNBC (highest evidence), BRCA1/2-mutated HER2-negative (BROCADE3 data), or HER2+ neoadjuvant (TCHP guideline-concordant use) — as benefit-risk profiles differ substantially
- **Dosing and monitoring protocol**: Establish institutional protocol for Calvert-formula dosing, renal function monitoring schedule, and haematological toxicity management (especially thrombocytopenia and anaemia thresholds for dose reduction or delay)
- **Biomarker testing strategy**: Define pre-treatment testing for BRCA mutation status, HRD score, and PD-L1 expression to guide patient selection and combination regimen choice
- **Combination partner decision**: Determine whether carboplatin will be used as monotherapy, with taxane, or with PARP inhibitor/immunotherapy based on available data and patient eligibility

---

*This report is generated for research purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before application. Danish healthcare professionals should refer to current clinical guidelines and the approved SmPC before prescribing.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

