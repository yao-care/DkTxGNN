---
layout: default
title: Paclitaxel
parent: 僅模型預測 (L5)
nav_order: 327
evidence_level: L5
indication_count: 10
---

# Paclitaxel
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

# Paclitaxel: From Ovarian/Lung Cancer to Female Breast Carcinoma

## One-Sentence Summary

Paclitaxel is a taxane-class cytotoxic chemotherapy agent with broad international approval across solid tumors (e.g., ovarian and non-small cell lung cancer); Danish-specific original-indication text was not available in this evidence pack. The TxGNN model predicts continued/renewed relevance for **Female Breast Carcinoma**, supported by an unusually large body of existing evidence — **50 clinical trials** (including multiple completed Phase 3 RCTs) and **20 publications** were retrieved, though this largely reflects paclitaxel's already-established role in breast cancer rather than a novel repurposing signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available from Danish licence records (0 licences on file); internationally approved for ovarian cancer, non-small cell lung cancer, and other solid tumors |
| Predicted New Indication | Female Breast Carcinoma |
| TxGNN Prediction Score | 99.995% |
| Evidence Level | L1 (≥2 completed Phase 3 RCTs identified) |
| Denmark Market Status | Not marketed (未上市) |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from DrugBank for this evidence pack (flagged as a High-severity data gap, DG002). Based on generally known pharmacology, Paclitaxel is a taxane-class agent that stabilizes microtubules and blocks mitotic spindle disassembly, driving apoptosis in rapidly dividing cells — a mechanism broadly applicable across proliferative solid tumors.

Paclitaxel's efficacy in ovarian and lung cancer, both high-proliferation solid tumors, is mechanistically consistent with activity against breast carcinoma, which shares similar dependence on cell-cycle progression and microtubule dynamics for tumor growth.

Importantly, the volume and maturity of the retrieved evidence (multiple completed Phase 3 randomized trials spanning three decades, including adjuvant, neoadjuvant, and metastatic settings) indicate that paclitaxel is **already an established standard-of-care agent in breast cancer treatment internationally**. This TxGNN prediction therefore largely reconfirms known clinical practice rather than surfacing a genuinely novel repurposing opportunity — a point that should inform how "new indication" is interpreted in this specific case.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00005970](https://clinicaltrials.gov/study/NCT00005970) | Phase 3 | Completed | 3,436 | AC followed by weekly paclitaxel ± trastuzumab as adjuvant therapy in HER2-overexpressing or high-risk node-positive/negative breast cancer |
| [NCT00561119](https://clinicaltrials.gov/study/NCT00561119) | Phase 3 | Completed | 326 | Maintenance vs. observation after 6 cycles of gemcitabine + paclitaxel as 1st-line therapy in metastatic/recurrent breast cancer |
| [NCT00004125](https://clinicaltrials.gov/study/NCT00004125) | Phase 3 | Completed | N/A | AC followed by paclitaxel or docetaxel, weekly vs. every 3 weeks, in axillary node-positive breast cancer |
| [NCT00002953](https://clinicaltrials.gov/study/NCT00002953) | Phase 3 | Completed | 704 | Epirubicin + cyclophosphamide vs. epirubicin + paclitaxel in metastatic breast cancer |
| [NCT01426880](https://clinicaltrials.gov/study/NCT01426880) | Phase 2/3 | Completed | 595 | Addition of carboplatin to neoadjuvant anthracycline-taxane-trastuzumab therapy in triple-negative and HER2+ early breast cancer |
| [NCT03289819](https://clinicaltrials.gov/study/NCT03289819) | Phase 2 | Completed | 53 | Neoadjuvant pembrolizumab + nab-paclitaxel followed by pembrolizumab + EC in triple-negative breast cancer |
| [NCT05296798](https://clinicaltrials.gov/study/NCT05296798) | Phase 3 | Active, not recruiting | 922 | Giredestrant + Phesgo vs. Phesgo after induction with Phesgo + taxane in HER2+/ER+ advanced breast cancer |
| [NCT02280252](https://clinicaltrials.gov/study/NCT02280252) | Phase 2 | Completed | 69 | Concurrent paclitaxel and radiation in locally advanced breast cancer, multiethnic cohort |
| [NCT01366144](https://clinicaltrials.gov/study/NCT01366144) | Phase 1 | Active, not recruiting | 94 | Veliparib + carboplatin + paclitaxel in solid tumor patients with hepatic/renal dysfunction |
| [NCT05189535](https://clinicaltrials.gov/study/NCT05189535) | Phase 2/3 | Completed | 66 | Pentoxifylline for prevention of paclitaxel-induced peripheral neuropathy in breast cancer patients |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31783552](https://pubmed.ncbi.nlm.nih.gov/31783552/) | 2019 | Review | Biomolecules | Comprehensive review of paclitaxel's mechanistic and clinical effects in breast cancer, including resistance mechanisms |
| [9282422](https://pubmed.ncbi.nlm.nih.gov/9282422/) | 1997 | Review | Drug and Therapeutics Bulletin | Early regulatory review of paclitaxel and docetaxel use in breast and ovarian cancer |
| [9164198](https://pubmed.ncbi.nlm.nih.gov/9164198/) | 1997 | Phase II trial | J Clin Oncol | ECOG study of biweekly paclitaxel + cisplatin in advanced breast carcinoma |
| [11147586](https://pubmed.ncbi.nlm.nih.gov/11147586/) | 2000 | Phase II trial | Cancer | Doxorubicin + paclitaxel combination in advanced metastatic breast carcinoma |
| [32461977](https://pubmed.ncbi.nlm.nih.gov/32461977/) | 2020 | Real-world study | BioMed Research International | Neoadjuvant EC + weekly paclitaxel + trastuzumab in HER2-positive breast carcinoma |
| [24068539](https://pubmed.ncbi.nlm.nih.gov/24068539/) | 2013 | Phase I-II trial | Breast Cancer Res Treat | Tipifarnib + sequential weekly paclitaxel and AC in inflammatory and ER-positive breast carcinoma |
| [11745249](https://pubmed.ncbi.nlm.nih.gov/11745249/) | 2001 | Case series | Cancer | Paclitaxel in multimodality treatment of inflammatory breast carcinoma |
| [39317691](https://pubmed.ncbi.nlm.nih.gov/39317691/) | 2024 | Preclinical | Chemical Biology & Drug Design | Paclitaxel combination therapeutic potential against breast carcinoma with in vivo biomarker identification |
| [17272681](https://pubmed.ncbi.nlm.nih.gov/17272681/) | 2007 | Preclinical | Molecular Pharmacology | Mechanistic study of stathmin-mediated resistance reversal to paclitaxel in breast carcinoma cells |
| [9821299](https://pubmed.ncbi.nlm.nih.gov/9821299/) | 1998 | Preclinical | Folia Microbiologica | Antitumor activity of paclitaxel + epirubicin combination in ER-positive human breast carcinoma model |

---

## Denmark Market Information

No marketing authorisation records were returned for Paclitaxel in this evidence pack (`total_licenses: 0`, `market_status: 未上市/Not marketed`). This is notable given paclitaxel's broad international generic availability, and should be treated as a data-collection gap requiring verification rather than confirmed absence from the Danish market.

---

## Cytotoxicity

Paclitaxel is a well-established cytotoxic antineoplastic (taxane class), so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (taxane / microtubule-stabilizing agent) |
| Myelosuppression Risk | Please refer to the Summary of Product Characteristics (SmPC) — no toxicity data was returned in this evidence pack |
| Emetogenicity Classification | Please refer to the Summary of Product Characteristics (SmPC) — no toxicity data was returned in this evidence pack |
| Monitoring Items | Please refer to the Summary of Product Characteristics (SmPC) warnings and precautions |
| Handling Protection | Cytotoxic drug handling precautions are expected to apply as a class-standard requirement for antineoplastic infusion agents; specific protocol should follow SmPC/local guidance |

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- Existing clinical evidence for paclitaxel in breast carcinoma is strong (Evidence Level L1, multiple completed Phase 3 RCTs), but this reflects already-established international standard-of-care use rather than a novel repurposing signal.
- A Blocking-severity data gap (DG001: TFDA/SmPC warnings and contraindications unavailable) prevents any safety initial assessment (S1) from proceeding, regardless of efficacy evidence strength.

**To proceed, the following is needed:**
- Obtain TFDA/Danish SmPC label text (warnings, contraindications) — resolves Blocking gap DG001
- Retrieve confirmed mechanism of action data from DrugBank — resolves High-severity gap DG002
- Verify actual Danish/EU marketing authorisation status, since the current record of 0 licences is inconsistent with paclitaxel's known wide generic availability and likely reflects incomplete data collection
- Clarify whether "female breast carcinoma" should be treated as a genuine repurposing candidate or reclassified as confirmatory evidence of existing standard-of-care use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

