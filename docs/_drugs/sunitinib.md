---
layout: default
title: Sunitinib
parent: 僅模型預測 (L5)
nav_order: 410
evidence_level: L5
indication_count: 10
---

# Sunitinib
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

# Sunitinib: From Unknown Original Indication to Liposarcoma

## One-Sentence Summary

> Sunitinib (DrugBank DB01268) is an orally administered multi-targeted tyrosine kinase inhibitor; the original approved indication is not recorded in this evidence pack, but the drug is well documented across the evidence base as active against multiple solid-tumor types.
> The TxGNN model predicts it may be effective for **Liposarcoma**,
> with **3 clinical trials** and **9 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no marketing authorisation or original-indication data found in this evidence pack |
| Predicted New Indication | Liposarcoma |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L2 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for sunitinib is not available in this evidence pack. However, the clinical-trial evidence itself characterizes sunitinib as an oral multi-targeted receptor tyrosine kinase inhibitor: trial NCT00474994 describes it as working "by blocking some of the enzymes needed for cell growth and by blocking blood flow to the tumor," and PMID 21154746 independently describes it as "a multitargeted receptor tyrosine kinase inhibitor active in other solid tumors."

No original indication is recorded for sunitinib in this evidence pack, so a direct comparison between an "original" and "predicted" indication cannot be made from the supplied data. That said, the literature evidence collected for the liposarcoma prediction shows sunitinib already being studied across a broad range of soft-tissue sarcoma subtypes (leiomyosarcoma, liposarcoma, malignant fibrous histiocytoma, extraskeletal myxoid chondrosarcoma), and PMID 21154746 explicitly notes its established activity in "imatinib mesylate-refractory gastrointestinal stromal tumors (GIST)" as a mechanistic precedent for use in other soft-tissue sarcomas.

Mechanistically, liposarcoma biology is described in PMID 38254762 as involving a "spectrum of molecular abnormalities" relevant to target-therapy selection, consistent with a pathway (anti-angiogenic, multi-kinase) that sunitinib is designed to inhibit. This overlap — angiogenesis- and kinase-driven tumor growth shared across sarcoma subtypes — is the basis for the TxGNN model's prediction and is corroborated by a completed Phase II trial and an individual case report of "long-lasting clinical benefit" specifically in metastatic liposarcoma (PMID 23482782).

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00400569](https://clinicaltrials.gov/study/NCT00400569) | Phase 2 | Completed | 48 | Open-label single-site study identifying a promising sunitinib dose in metastatic/unresectable soft tissue sarcoma, including liposarcoma, leiomyosarcoma, fibrosarcoma, and MFH |
| [NCT02048371](https://clinicaltrials.gov/study/NCT02048371) | Phase 2 | Completed | 131 | SARC024 protocol studying oral regorafenib in selected sarcoma subtypes; cites prior evidence of sunitinib (and sorafenib/pazopanib) activity in soft tissue sarcomas as rationale |
| [NCT00474994](https://clinicaltrials.gov/study/NCT00474994) | Phase 2 | Completed | 53 | Multicenter continuous-dosing study of sunitinib in metastatic, locally advanced, or recurrent non-GIST sarcomas |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21154746](https://pubmed.ncbi.nlm.nih.gov/21154746/) | 2011 | Phase II study | International Journal of Cancer | Phase II study of sunitinib malate in relapsed/refractory STS, focused on leiomyosarcoma, liposarcoma, and MFH |
| [23482782](https://pubmed.ncbi.nlm.nih.gov/23482782/) | 2013 | Case report | Anticancer Research | Long-lasting clinical benefit of sunitinib malate in a heavily pre-treated metastatic liposarcoma patient |
| [25884155](https://pubmed.ncbi.nlm.nih.gov/25884155/) | 2015 | Trial protocol | BMC Cancer | REGOSARC randomized placebo-controlled Phase II protocol; angiogenesis signaling as key sarcoma target, sunitinib referenced as active comparator class |
| [38254762](https://pubmed.ncbi.nlm.nih.gov/38254762/) | 2024 | Review | Cancers | Genetic, epigenetic, and transcriptome alterations in liposarcoma relevant to target-therapy selection |
| [24555529](https://pubmed.ncbi.nlm.nih.gov/24555529/) | 2014 | Review | Expert Review of Anticancer Therapy | Emerging therapies for adult soft tissue sarcoma |
| [22987955](https://pubmed.ncbi.nlm.nih.gov/22987955/) | 2012 | Review | Annals of Oncology | Histology-driven medical therapy for soft tissue sarcomas, noting trabectedin's high activity specifically in myxoid liposarcoma |
| [24712007](https://pubmed.ncbi.nlm.nih.gov/24712007/) | 2014 | Review | Magyar Onkologia | Medical treatment of soft tissue sarcomas by histological subtype |
| [28423517](https://pubmed.ncbi.nlm.nih.gov/28423517/) | 2017 | Case series | Oncotarget | Next-generation sequencing of extraskeletal myxoid chondrosarcoma, evaluating predictive factors for sunitinib benefit |
| [38717131](https://pubmed.ncbi.nlm.nih.gov/38717131/) | 2024 | Case series | American Journal of Surgical Pathology | Clinicopathologic analysis of myxoid inflammatory myofibroblastic sarcoma (background sarcoma-classification reference) |

---

## Denmark Market Information

Sunitinib currently has no registered marketing authorisations in this evidence pack (0 licenses, market status: Not marketed). No Laegemiddelstyrelsen or EMA centralised authorisation details are available to display.

---

## Cytotoxicity

Sunitinib is an oncology drug (multi-targeted receptor tyrosine kinase inhibitor, per PMID 21154746) and all evidence in this pack concerns cancer indications (liposarcoma, renal cell carcinoma subtypes), so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (multi-targeted receptor tyrosine kinase inhibitor) |
| Myelosuppression Risk | Please refer to the Summary of Product Characteristics (SmPC) warnings and precautions |
| Emetogenicity Classification | Please refer to the Summary of Product Characteristics (SmPC) warnings and precautions |
| Monitoring Items | Please refer to the Summary of Product Characteristics (SmPC) warnings and precautions |
| Handling Protection | Please refer to the Summary of Product Characteristics (SmPC) warnings and precautions |

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information. No key warnings, contraindications, or drug interaction data were available in this evidence pack (a DDI query returned no results, and the drug label/warnings query is flagged as a Blocking data gap).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Three completed Phase II trials plus a positive individual case report support antitumor activity of sunitinib in soft-tissue sarcoma/liposarcoma, but sunitinib currently has no marketing authorisation in Denmark and a **Blocking** data gap exists for TFDA/SmPC-equivalent warnings and contraindications — this prevents entry into the S1 safety pre-assessment stage regardless of the efficacy signal.

**To proceed, the following is needed:**
- Danish/EU SmPC (or equivalent label) warnings, contraindications, and drug-interaction data
- Confirmed mechanism-of-action documentation from DrugBank
- Clarification of Danish/EU marketing status (e.g., Sutent centralised EMA authorisation) and available dosage forms/routes
- If available, Phase 3 RCT data specific to liposarcoma, since current evidence is limited to Phase II single-arm/open-label studies
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

