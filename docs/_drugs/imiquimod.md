---
layout: default
title: Imiquimod
parent: 僅模型預測 (L5)
nav_order: 228
evidence_level: L5
indication_count: 10
---

# Imiquimod
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

Using the Evidence Pack for Imiquimod (DB00724), here is the evaluation report.

# Imiquimod: From Actinic Keratosis to Pre-Malignant Neoplasm

## One-Sentence Summary

Imiquimod is a topical Toll-like receptor 7 (TLR7) agonist already established for actinic keratosis, superficial basal cell carcinoma, and genital warts — all of which fall within the broad "pre-malignant/HPV-related lesion" category. The TxGNN model predicts continued and expanded effectiveness across **pre-malignant neoplasm** as a class, and this direction is currently supported by **19 clinical trials** and **9 publications**, most concentrated on cervical, vulvar, and actinic pre-malignant lesions.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not registered in Denmark (drug not marketed); internationally, imiquimod is approved for actinic keratosis, superficial basal cell carcinoma, and external genital/perianal warts (context drawn from trial descriptions in the evidence pack) |
| Predicted New Indication | Pre-malignant neoplasm |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L2 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Currently, a formal, structured mechanism-of-action record for imiquimod is not available in this evidence pack (flagged as data gap DG002, High severity). Based on the information captured in the trial and rationale data, however, imiquimod acts as a **TLR7 agonist**: local activation of Toll-like receptor 7 triggers release of IFN-α, TNF-α, and IL-12, driving apoptosis and immune-mediated clearance of dysplastic/abnormal keratinocytes. This mechanism already underlies imiquimod's established use in actinic keratosis (AK) — which is itself formally classified as a pre-malignant skin lesion — as well as its use in superficial basal cell carcinoma and HPV-related genital warts.

Because AK is already a recognised pre-malignant neoplasm treated by imiquimod, the TxGNN model's high score for the broader "pre-malignant neoplasm" category is, in part, a re-confirmation of known biology. The genuinely novel repurposing signal lies in extending this same TLR7-driven mechanism to **other anatomic sites with HPV-associated pre-malignant epithelium** — vulvar intraepithelial neoplasia (VIN), cervical intraepithelial neoplasia (CIN), and anal intraepithelial neoplasia (AIN) — all of which share the same immune-evasion and dysplastic-epithelium biology as AK.

This mechanistic continuity is why multiple independent research groups have tested topical imiquimod in CIN and VIN despite these not being on-label indications: the local immune activation needed to clear dysplastic epithelium is not anatomically restricted to skin. The strongest direct evidence is a completed Phase 2 RCT in high-grade CIN (Brazil, n=90) and case-series/mechanistic work in VIN 2/3, while a dedicated Phase 3 RCT in CIN (NCT02329171) confirms proof-of-concept but was terminated early due to poor enrollment (n=9), limiting definitive confirmation.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02329171](https://clinicaltrials.gov/study/NCT02329171) | Phase 3 | Terminated | 9 | RCT of topical imiquimod for high-grade cervical intraepithelial neoplasia (CIN) as a non-invasive alternative to LLETZ excision; terminated early due to poor recruitment |
| [NCT01720407](https://clinicaltrials.gov/study/NCT01720407) | Phase 3 | Completed | 259 | Imiquimod as neoadjuvant treatment for lentigo maligna of the face to reduce excision size and risk of intralesional excision |
| [NCT02242929](https://clinicaltrials.gov/study/NCT02242929) | Phase 3 | Unknown | 145 | Non-inferiority RCT: surgical excision vs. curettage + imiquimod for nodular basal cell carcinoma |
| [NCT00175643](https://clinicaltrials.gov/study/NCT00175643) | Phase 3 | Completed | 20 | Open-label study of imiquimod 5% cream (3 days/week) for actinic keratoses on the head |
| [NCT03233412](https://clinicaltrials.gov/study/NCT03233412) | Phase 2 | Completed | 90 | Randomized trial of topical imiquimod for high-grade cervical intraepithelial lesions (Brazil) |
| [NCT00941811](https://clinicaltrials.gov/study/NCT00941811) | Phase 2 | Completed | 5 | Explorative controlled study of immune escape mechanisms and imiquimod efficacy in VIN 2/3 and anogenital warts |
| [NCT01229319](https://clinicaltrials.gov/study/NCT01229319) | Phase 4 | Unknown | 20 | Post-marketing study of imiquimod 3.75% cream (Zyclara) after cryotherapy for hypertrophic actinic keratoses |
| [NCT04219358](https://clinicaltrials.gov/study/NCT04219358) | Phase 1 | Terminated | 49 | RCT comparing 5%, 0.05%, and nanoencapsulated 0.05% imiquimod gel for actinic cheilitis (pre-malignant lip lesion) |
| [NCT04883645](https://clinicaltrials.gov/study/NCT04883645) | Early Phase 1 | Completed | 16 | Pilot trial of neoadjuvant TLR7 agonist (imiquimod) immunotherapy in early-stage oral squamous cell carcinoma |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23235673](https://pubmed.ncbi.nlm.nih.gov/23235673/) | 2012 | Review (Cochrane) | Cochrane Database of Systematic Reviews | Systematic review of interventions for anal canal intraepithelial neoplasia (AIN), a pre-malignant HPV-associated condition |
| [21491403](https://pubmed.ncbi.nlm.nih.gov/21491403/) | 2011 | Review (Cochrane) | Cochrane Database of Systematic Reviews | Systematic review of medical interventions for high-grade vulval intraepithelial neoplasia (VIN), including imiquimod |
| [20505896](https://pubmed.ncbi.nlm.nih.gov/20505896/) | 2010 | Review | Skin Therapy Letter | Overview of current management of actinic keratoses, including topical field therapies such as imiquimod |
| [26516853](https://pubmed.ncbi.nlm.nih.gov/26516853/) | 2015 | Review | International Journal of Molecular Sciences | Review of combined photodynamic therapy approaches for non-melanoma skin cancer and its precursor lesions |
| [15584683](https://pubmed.ncbi.nlm.nih.gov/15584683/) | 2004 | Review | Seminars in Cutaneous Medicine and Surgery | Review of topical treatment strategies (including imiquimod) for non-melanoma skin cancer and precursor lesions |
| [29500135](https://pubmed.ncbi.nlm.nih.gov/29500135/) | 2018 | Preclinical PK/PD | Urologic Oncology | Rat model PK/PD study of TLR7 agonists used topically for pre-malignant skin lesions, exploring intravesical use for bladder cancer |
| [30284955](https://pubmed.ncbi.nlm.nih.gov/30284955/) | 2019 | Case Report | International Journal of STD & AIDS | Successful treatment of high-grade VIN with imiquimod 5% in an immunosuppressed renal transplant recipient |
| [18931984](https://pubmed.ncbi.nlm.nih.gov/18931984/) | 2008 | Case Report | Der Hautarzt | Case of disseminated superficial actinic porokeratosis with coexisting actinic keratoses resistant to topical treatment |
| [15601490](https://pubmed.ncbi.nlm.nih.gov/15601490/) | 2004 | Case Report | International Journal of STD & AIDS | Successful clearance of Bowenoid papulosis of the penis (a pre-malignant ano-genital condition) using topical imiquimod 5% |

## Denmark Market Information

Imiquimod does not currently hold any marketing authorisation in Denmark (market status: **Not marketed**, 0 registered products with Laegemiddelstyrelsen). A new marketing authorisation application — national or via EMA centralised procedure — would be required before this repurposing candidate could be evaluated for clinical use in Denmark.

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information. Key warnings, contraindications, and drug-interaction data for imiquimod were not available in this evidence pack (data gap DG001, Blocking severity — required before the safety pre-screen (S1) can proceed).

One safety signal worth flagging for future off-label extension work: literature evidence for a related, lower-scoring predicted indication (benign neoplasm of buccal mucosa, not the primary indication in this report) includes a case report of **malignant conversion of oral papillomatosis during topical imiquimod therapy** (PMID 12719972). While not directly applicable to the pre-malignant neoplasm indication assessed here, it underscores the need for site-specific safety review before any mucosal (non-skin) application is pursued.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Evidence level L2 is supported by one completed Phase 2 RCT in high-grade CIN and consistent mechanistic/case-series data in VIN and AK, and the underlying TLR7 mechanism is already clinically validated in imiquimod's approved use for actinic keratosis. However, imiquimod is not currently marketed in Denmark, and two data gaps — missing official MOA documentation (DG002) and missing TFDA/SmPC warnings and contraindications (DG001, Blocking) — must be resolved before this candidate can advance past the safety pre-screen.

**To proceed, the following is needed:**
- Official Summary of Product Characteristics (warnings, contraindications, DDI) — currently blocking safety pre-screen (S1)
- Formal DrugBank/regulatory-sourced mechanism-of-action documentation
- Confirmation of route/formulation compatibility for non-cutaneous pre-malignant sites (cervix, vulva, anus) versus imiquimod's existing topical skin formulation
- A larger, adequately powered controlled trial in CIN, given that the only dedicated Phase 3 RCT (NCT02329171) was terminated early due to enrollment failure (n=9)
- A Danish marketing authorisation pathway assessment, since imiquimod currently holds no registration in Denmark
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

