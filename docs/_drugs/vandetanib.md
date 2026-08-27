---
layout: default
title: Vandetanib
parent: 僅模型預測 (L5)
nav_order: 465
evidence_level: L5
indication_count: 10
---

# Vandetanib
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

# Vandetanib: From Medullary Thyroid Cancer to Renal Cell Carcinoma

## One-Sentence Summary

Vandetanib is an oral multi-kinase inhibitor (VEGFR2/EGFR/RET) internationally approved for medullary thyroid cancer; no Danish marketing authorisation is currently on file for this drug.
The TxGNN model predicts it may be effective for **Renal Cell Carcinoma**,
with **4 clinical trials** and **6 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the Danish licensing data; literature context (PMID 24451769) indicates Vandetanib is internationally approved as a RET-kinase inhibitor for medullary thyroid cancer |
| Predicted New Indication | Renal Cell Carcinoma |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L2 (1 completed randomized Phase 2 trial) |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for Vandetanib was not returned by DrugBank in this evidence pack (data gap, High severity). Based on the literature evidence collected, Vandetanib is a multi-target tyrosine kinase inhibitor acting on VEGFR2, EGFR and RET; one review in the evidence set (PMID 26677336) explicitly groups vandetanib together with sunitinib, sorafenib and pazopanib as antiangiogenic agents targeting VEGF-driven signalling in solid tumours.

Sunitinib, sorafenib and pazopanib — drugs sharing vandetanib's core VEGFR2-inhibition mechanism — are already established first-line treatments for renal cell carcinoma, since RCC is a highly vascularised, angiogenesis-dependent tumour. This provides a direct mechanistic rationale for the TxGNN prediction: a VEGFR2-targeting agent proven effective in one angiogenesis-driven malignancy (thyroid cancer, via RET/VEGFR inhibition) is plausible in another (renal cell carcinoma), and several early-phase trials in the evidence pack (VHL-associated renal tumors, clear cell RCC, HLRCC/SDH-associated kidney cancer) have already tested this hypothesis directly.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00566995](https://clinicaltrials.gov/study/NCT00566995) | Phase 2 | Completed | 37 | Tested vandetanib (ZD6474) for antiangiogenic/antitumour effect in Von Hippel-Lindau disease-associated renal tumors |
| [NCT02495103](https://clinicaltrials.gov/study/NCT02495103) | Phase 1/2 | Terminated | 7 | Vandetanib + metformin combination in HLRCC- or SDH-associated kidney cancer and sporadic papillary RCC |
| [NCT01372813](https://clinicaltrials.gov/study/NCT01372813) | Phase 2 | Terminated | 3 | Evaluated vandetanib for tumour shrinkage/stabilisation in advanced clear cell renal carcinoma; stopped early |
| [NCT01191892](https://clinicaltrials.gov/study/NCT01191892) | Phase 2 (Randomized) | Completed | 82 | Randomized trial of carboplatin/gemcitabine ± vandetanib as first-line therapy in cisplatin-ineligible advanced urothelial/renal pelvis cancer |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36302175](https://pubmed.ncbi.nlm.nih.gov/36302175/) | 2023 | Phase II Trial | Clin Cancer Res | Guadecitabine trial in SDH-deficient tumours including HLRCC-associated renal cell carcinoma, a population resistant to conventional therapy |
| [40779213](https://pubmed.ncbi.nlm.nih.gov/40779213/) | 2025 | Review | Clin Exp Metastasis | Discusses targeted-therapy combinations for metastatic fumarate hydratase-deficient RCC, a rare, aggressive subtype with no established regimen |
| [26677336](https://pubmed.ncbi.nlm.nih.gov/26677336/) | 2015 | Review | OncoTargets Ther | Profiles antiangiogenic TKIs (sunitinib, sorafenib, pazopanib, vandetanib) approved across solid-tumour indications |
| [28477875](https://pubmed.ncbi.nlm.nih.gov/28477875/) | 2017 | Review | Bull Cancer | Reviews cabozantinib MOA/efficacy in the broader context of VEGFR/RET-targeting TKIs |
| [24451769](https://pubmed.ncbi.nlm.nih.gov/24451769/) | 2012 | Review | ASCO Educational Book | Reviews systemic therapy for advanced thyroid cancers; notes vandetanib's FDA approval as a RET-kinase inhibitor for medullary thyroid cancer |
| [31043488](https://pubmed.ncbi.nlm.nih.gov/31043488/) | 2019 | Preclinical | Mol Cancer Res | Mouse model of TFE3 Xp11.2-translocation RCC identifies novel therapeutic targets and a diagnostic marker (GPNMB) |

---

## Denmark Market Information

Vandetanib currently has no marketing authorisation on file with the Danish Medicines Agency (Laegemiddelstyrelsen) — market status is **Not marketed**, with **0** registered authorisations.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (multi-kinase inhibitor: VEGFR2, EGFR, RET) |
| Myelosuppression Risk | Please refer to the Summary of Product Characteristics (SmPC) warnings and precautions |
| Emetogenicity Classification | Please refer to the Summary of Product Characteristics (SmPC) warnings and precautions |
| Monitoring Items | Please refer to the Summary of Product Characteristics (SmPC) warnings and precautions |
| Handling Protection | As an oral antineoplastic agent, standard institutional handling precautions for cytotoxic/targeted oncology drugs should be followed pending SmPC confirmation |

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Mechanistic rationale and early-phase clinical evidence for renal cell carcinoma are present, but a Blocking data gap exists — TFDA/SmPC warnings and contraindications are unavailable, so the candidate cannot pass initial safety screening (S1), and Vandetanib holds no marketing authorisation in Denmark.

**To proceed, the following is needed:**
- SmPC warnings, contraindications and drug interaction data (currently blocking)
- Confirmed mechanism of action from DrugBank
- Danish/EMA marketing authorisation status and any centralised (EMA) licence details
- Evaluation of a pathway to Danish market entry given the current "Not marketed" status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

