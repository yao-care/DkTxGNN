---
layout: default
title: Afatinib
parent: 僅模型預測 (L5)
nav_order: 17
evidence_level: L5
indication_count: 10
---

# Afatinib
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

# Afatinib: From EGFR-Mutated Non-Small Cell Lung Cancer to HER2-Positive Breast Carcinoma

## One-Sentence Summary

Afatinib is an irreversible pan-HER (ErbB) tyrosine kinase inhibitor originally approved for the treatment of EGFR mutation-positive non-small cell lung cancer (NSCLC).
The TxGNN model predicts it may be effective for **HER2 Positive Breast Carcinoma**,
with **10 clinical trials** and **19 publications** currently supporting this direction, yielding a prediction confidence of 98.65% and an evidence level of L1.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | EGFR mutation-positive non-small cell lung cancer (based on EMA/FDA global approval; no Danish national authorisation on file) |
| Predicted New Indication | HER2 Positive Breast Carcinoma |
| TxGNN Prediction Score | 98.65% |
| Evidence Level | L1 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Afatinib is an orally administered small molecule that irreversibly blocks the entire ErbB (HER) receptor family — specifically EGFR (HER1), HER2, and HER4 — by forming covalent bonds with the ATP-binding domain of these kinases. This permanently silences downstream pro-tumour signalling cascades (e.g., MAPK, PI3K/AKT). This mechanism distinguishes afatinib from first-generation reversible EGFR inhibitors such as gefitinib and erlotinib, providing more sustained and broader receptor blockade.

HER2-positive breast carcinoma is defined by HER2 gene amplification and/or protein overexpression, which occurs in approximately 15–20% of all breast cancers and historically confers a poor prognosis. Because HER2 is a primary and direct molecular target of afatinib, the mechanistic alignment between drug and disease is exceptionally strong (★★★★★). Both HER2-positive breast cancer and EGFR-mutated NSCLC share fundamental dependence on the HER/ErbB receptor signalling network, providing a compelling and well-characterised biological rationale for repurposing.

The dedicated LUX-Breast clinical programme — spanning Phase 1 through Phase 3 — was designed precisely to evaluate afatinib in HER2-positive breast cancer. The pivotal LUX-Breast 1 Phase 3 trial (NCT01125566; n=508) compared afatinib plus vinorelbine against the trastuzumab-based standard of care in trastuzumab-pre-treated patients; although the primary progression-free survival (PFS) endpoint narrowly missed statistical significance, the programme generated a comprehensive safety database and identified subgroups — particularly patients with brain metastases and those treated with dual HER2 blockade strategies — that may benefit from further targeted investigation. Afatinib's established CNS penetration adds biological plausibility for these niche but high-unmet-need populations.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT01125566](https://clinicaltrials.gov/study/NCT01125566) | Phase 3 | Completed | 508 | **LUX-Breast 1**: Afatinib + vinorelbine vs. trastuzumab + vinorelbine in HER2-overexpressing metastatic breast cancer after one prior trastuzumab treatment. Primary PFS endpoint not statistically significant; comprehensive safety and subgroup data available — highest-grade direct evidence for this indication. |
| [NCT01441596](https://clinicaltrials.gov/study/NCT01441596) | Phase 2 | Completed | 121 | **LUX-Breast 3**: Randomised, afatinib ± vinorelbine vs. investigator's choice in HER2+ breast cancer with progressive brain metastases after trastuzumab and/or lapatinib. Multi-arm efficacy and safety data in a high-unmet-need subpopulation. |
| [NCT01594177](https://clinicaltrials.gov/study/NCT01594177) | Phase 2 | Completed | 65 | Neoadjuvant dual HER2 blockade: afatinib + trastuzumab added to anthracycline/taxane chemotherapy in locally advanced or operable HER2+ breast cancer. Pathological complete response (pCR) rates evaluated; supports dual-blockade concept. |
| [NCT00431067](https://clinicaltrials.gov/study/NCT00431067) | Phase 2 | Completed | 41 | Afatinib monotherapy in HER2+ metastatic breast cancer after failure of trastuzumab-containing regimens. Established foundational single-agent activity data in trastuzumab-refractory patients. |
| [NCT02438722](https://clinicaltrials.gov/study/NCT02438722) | Phase 2/3 | Active, not recruiting | 174 | Randomised trial of afatinib + cetuximab vs. afatinib alone in treatment-naïve EGFR mutation-positive NSCLC. Explores dual ErbB blockade strategy; full results pending — design highly relevant to combination approaches. |
| [NCT00826267](https://clinicaltrials.gov/study/NCT00826267) | Phase 2 | Completed | 29 | Randomised neoadjuvant three-arm study: afatinib vs. trastuzumab vs. lapatinib in HER2-positive Stage IIIa locally advanced breast cancer (treatment-naïve). Provides direct head-to-head comparative data. |
| [NCT04158947](https://clinicaltrials.gov/study/NCT04158947) | Phase 2 | Unknown | 130 | Afatinib + T-DM1 vs. T-DM1 alone in HER2+ breast cancer with active refractory brain metastases. Phase I dose-finding followed by Phase II efficacy assessment; biologically plausible given afatinib's CNS penetration. Status unknown reduces confidence. |
| [NCT01320280](https://clinicaltrials.gov/study/NCT01320280) | Phase 2 | Terminated | 29 | Afatinib in HER2-positive hormone-refractory prostate cancer after docetaxel failure. Early termination limits efficacy interpretation; safety profile in HER2+ solid tumours remains informative. |
| [NCT01531764](https://clinicaltrials.gov/study/NCT01531764) | Phase 2 | Terminated | 2 | Afatinib + vinorelbine in intermediate HER2 expression (IHC 2+/FISH-negative) metastatic breast cancer. Terminated after enrolling only 2 patients; no meaningful efficacy conclusions possible. |
| [NCT00950742](https://clinicaltrials.gov/study/NCT00950742) | Phase 1 | Completed | 18 | Maximum tolerated dose (MTD) determination of afatinib in combination with trastuzumab in HER2-positive advanced breast cancer. Preliminary tolerability and pharmacokinetic data only. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [35138529](https://pubmed.ncbi.nlm.nih.gov/35138529/) | 2022 | Clinical Trial Report | *Breast Cancer Res Treat* | **LUX-Breast 2**: Afatinib alone and in combination with vinorelbine or paclitaxel in HER2+ metastatic breast cancer patients who failed prior trastuzumab/lapatinib. Evaluated a sequential monotherapy-then-combination strategy; real-world efficacy and safety data. |
| [35653982](https://pubmed.ncbi.nlm.nih.gov/35653982/) | 2022 | Systematic Review / Network Meta-analysis | *ESMO Open* | Systematic review and network meta-analysis of TKI-containing regimens (including afatinib) for HER2+ breast cancer brain metastases. Compared clinical outcomes against non-TKI regimens across multiple trials. |
| [24080156](https://pubmed.ncbi.nlm.nih.gov/24080156/) | 2014 | Systematic Review | *Cancer Treatment Reviews* | Systematic review of dual HER2-targeting strategies in HER2+ breast cancer, including afatinib combinations. Synthesises evidence on trastuzumab resistance mechanisms and rationale for pan-ErbB blockade. |
| [29772459](https://pubmed.ncbi.nlm.nih.gov/29772459/) | 2018 | Review | *Cancer Treatment Reviews* | Comprehensive review of TKIs for brain metastases in HER2+ breast cancer. Discusses CNS penetration properties, including afatinib's documented blood-brain barrier activity, and clinical evidence across agents. |
| [29604436](https://pubmed.ncbi.nlm.nih.gov/29604436/) | 2018 | Review | *Pharmacological Research* | Review of investigational chemotherapy and novel pharmacokinetic mechanisms for breast cancer brain metastases, including second-generation pan-HER inhibitors such as afatinib. |
| [33122343](https://pubmed.ncbi.nlm.nih.gov/33122343/) | 2021 | In vitro / Mechanistic Study | *Clin Cancer Res* | Evaluated effects of HER-family TKIs (afatinib, lapatinib, neratinib) on antibody-dependent cell-mediated cytotoxicity (ADCC) in combination with trastuzumab and pertuzumab in HER2-expressing breast cancer cells. Provides mechanistic insight into combination synergy. |
| [38367127](https://pubmed.ncbi.nlm.nih.gov/38367127/) | 2024 | Comparative Study | *Clin Exp Metastasis* | Comparison of T-DM1, T-DXd, and disitamab vedotin in a multi-resistant HER2+ breast cancer lung metastasis model. Provides context for the evolving resistance landscape and therapeutic sequencing relevant to afatinib's positioning. |
| [30350178](https://pubmed.ncbi.nlm.nih.gov/30350178/) | 2018 | Phase I Clinical Study | *Cancer Chemother Pharmacol* | Phase I trial of afatinib + 3-weekly trastuzumab with optimised anti-diarrhoeal management in HER2+ metastatic cancer. Safety, tolerability, and pharmacokinetics of the combination; supports feasibility of combination dosing. |
| [33894300](https://pubmed.ncbi.nlm.nih.gov/33894300/) | 2021 | Review | *BBA Reviews on Cancer* | Review of HER2-targeted therapies across cancer types (breast, gastric). Contextualises afatinib's mechanism within the broader HER2-targeted treatment landscape, including resistance pathways. |
| [24870559](https://pubmed.ncbi.nlm.nih.gov/24870559/) | 2014 | Review | *Expert Opin Investig Drugs* | Expert review on afatinib specifically in breast cancer treatment. Evaluates its promise as a trastuzumab-resistance strategy, summarises early LUX-Breast clinical data, and compares afatinib with neratinib. |

---

## Denmark Market Information

Afatinib is currently **not marketed in Denmark**. No marketing authorisations are registered in the Danish Medicines Agency (Lægemiddelstyrelsen) database, and no centralised EMA authorisations are reflected in the local registry for this product (data cutoff: 2026-04-04).

> **Practical note for clinical teams**: Afatinib (Giotrif®) holds a centralised EMA marketing authorisation for first-line treatment of adults with EGFR mutation-positive locally advanced or metastatic NSCLC. As an EMA-authorised product, it is legally available across all EU member states, including Denmark, but distribution and active marketing in Denmark appear limited. Access for unlicensed indications (e.g., HER2+ breast cancer) would require either a named-patient programme, compassionate use application, or participation in a clinical trial. Consult the hospital pharmacy for current availability and reimbursement status.

---

## Cytotoxicity

Afatinib is an antineoplastic agent targeting ErbB/HER receptors in cancer cells. It is classified as a targeted therapy, not conventional cytotoxic chemotherapy.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — irreversible covalent pan-ErbB (HER1/HER2/HER4) tyrosine kinase inhibitor (second-generation) |
| Myelosuppression Risk | Low — afatinib is not a classical myelosuppressive agent; significant haematological toxicity is uncommon compared to cytotoxic chemotherapy |
| Emetogenicity Classification | Low — oral targeted agents in this class carry minimal emetogenic potential |
| Monitoring Items | Liver function tests (ALT, AST, bilirubin); renal function and electrolytes (particularly magnesium, potassium); left ventricular ejection fraction (LVEF) if used in combination with trastuzumab; dermatological assessment (acneiform rash, paronychia, skin fissures); diarrhoea grading (Common Terminology Criteria); pulmonary function (interstitial lung disease surveillance) |
| Handling Protection | Standard oral anticancer agent handling precautions apply — follow institutional cytotoxic handling policy for oral antineoplastic drugs; no intravenous preparation required |

---

## Safety Considerations

Structured safety data (key warnings, contraindications, drug-drug interactions) were not available in this evidence pack. Please refer to the approved Summary of Product Characteristics (SmPC) for Giotrif® for complete safety information, including but not limited to: interstitial lung disease, hepatotoxicity, diarrhoea management, embryo-foetal toxicity, and keratitis.

> For drug-drug interaction screening, consult the current Giotrif® SmPC and institutional pharmacy resources. Of note, afatinib is a substrate and inhibitor of P-glycoprotein (P-gp); interactions with P-gp inducers (e.g., rifampicin) and inhibitors (e.g., ritonavir, ciclosporin) are clinically relevant and should be reviewed for each patient.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Afatinib has strong mechanistic alignment with HER2-positive breast carcinoma as an irreversible pan-HER inhibitor directly targeting the disease's primary driver. The completed LUX-Breast Phase 3 programme (LUX-Breast 1; n=508), multiple completed Phase 2 trials, and a substantive supporting literature base collectively provide L1-level evidence. Although the primary PFS endpoint in LUX-Breast 1 was not statistically significant versus trastuzumab, clinically meaningful activity in subpopulations — particularly patients with brain metastases and those receiving dual HER2-blockade regimens — warrants structured further evaluation.

**To proceed, the following is needed:**

- **Safety profile completion**: Retrieve the full EMA-approved SmPC for Giotrif® to document key warnings, contraindications, and drug interactions (Data Gap DG001)
- **Mechanism of action documentation**: Complete DrugBank API query for afatinib to formally document MOA (Data Gap DG002)
- **Danish access pathway**: Confirm availability via named-patient programme or compassionate use in consultation with the hospital pharmacy and Lægemiddelstyrelsen, given the absence of an active Danish marketing authorisation for breast cancer
- **Subpopulation definition**: Specify the target patient group most likely to benefit — e.g., trastuzumab-refractory HER2+ metastatic breast cancer, or HER2+ patients with active brain metastases — before any clinical protocol is drafted
- **LUX-Breast 1 subgroup analysis**: Review published subgroup data to identify responder characteristics and inform patient selection criteria for any investigator-initiated study
- **Cardiac monitoring plan**: Establish a structured LVEF monitoring protocol, particularly if afatinib is to be used in combination with trastuzumab or other cardiotoxic agents
- **Regulatory classification review**: Determine whether a repurposing application to the EMA or a Danish regulatory notification is required given the existing NSCLC authorisation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

