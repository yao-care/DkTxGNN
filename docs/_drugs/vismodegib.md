---
layout: default
title: Vismodegib
parent: 僅模型預測 (L5)
nav_order: 472
evidence_level: L5
indication_count: 10
---

# Vismodegib
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

# Vismodegib: From Basal Cell Carcinoma to Xeroderma Pigmentosum-Associated Skin Cancer

## One-Sentence Summary

> Vismodegib is a Hedgehog-pathway (SMO) inhibitor used to treat advanced/metastatic basal cell carcinoma (BCC).
> The TxGNN model predicts it may also be effective in **Xeroderma Pigmentosum** (a rare genetic disorder causing recurrent, multiple BCCs from a young age),
> with **no registered clinical trials** but **5 supporting publications**, including two published case reports of vismodegib successfully used in xeroderma pigmentosum patients.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Basal Cell Carcinoma, advanced/metastatic (per literature evidence in this pack; formal Danish label text not yet available — see Data Gaps) |
| Predicted New Indication | Xeroderma Pigmentosum (recurrent/multiple basal cell carcinomas) |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L3 (case-report level clinical evidence; no completed clinical trials) |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Vismodegib is a small-molecule inhibitor of Smoothened (SMO), the key transducer of the Hedgehog (Hh) signalling pathway. As described in the literature captured in this evidence pack, it is "an oral inhibitor of the Hedgehog signaling pathway" that "has been used to treat basal cell carcinoma (BCC) in adults." Aberrant Hedgehog pathway activation — most commonly through *PTCH1* or *SMO* mutations — is the principal oncogenic driver of sporadic BCC, which is why vismodegib was approved for this indication.

Xeroderma pigmentosum (XP) is an autosomal recessive DNA-repair disorder (nucleotide excision repair defect) that causes extreme UV sensitivity and a dramatically increased lifetime risk of skin cancers, particularly multiple, recurrent BCCs starting in childhood. Critically, the BCCs that arise in XP patients are still driven by the same Hedgehog pathway dysregulation seen in sporadic BCC — the underlying DNA-repair defect increases the *rate* of oncogenic mutation, but the tumour biology downstream converges on the same SMO-dependent signalling that vismodegib targets. This is the mechanistic basis for the TxGNN prediction, and it is directly corroborated by the literature in this pack: two independent case reports (PMID 30178564, PMID 28297142) document vismodegib being used specifically to treat multiple BCCs in XP patients, with one reporting a 61% reduction in total lesion burden after 16.5 months of treatment and prevention of new lesions, and the other describing complete clearance of a nodular BCC in an 8-year-old XP patient after 4 months of therapy.

It is worth noting that the single highest-scoring TxGNN candidate in this pack, **medulloblastoma with extensive nodularity (MBEN)** (score 99.93%), is mechanistically even more direct — MBEN is a Hedgehog-pathway-driven medulloblastoma subtype for which SMO inhibitors are a rational targeted therapy. However, this pack currently contains **zero clinical trials or publications** for that candidate. The rationale generated alongside that prediction itself flags this as a suspected evidence-collection gap rather than a true absence of evidence, and recommends a manual PubMed/ClinicalTrials.gov search to confirm before this candidate is scored or acted upon. Several other candidates in this pack (annular epidermolytic ichthyosis, epidermolysis bullosa simplex with mottled pigmentation, prostate/brain cancer susceptibility) have no mechanistic link to the Hedgehog pathway and no supporting evidence, and are flagged in the source data itself as likely knowledge-graph false positives (semantic clustering around "skin disease" or "cancer susceptibility" nodes rather than true biological signal).

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35283513](https://pubmed.ncbi.nlm.nih.gov/35283513/) | 2021 | Review | Indian Journal of Dermatology | Reviews current therapeutic strategies for XP, including sun avoidance, surgery, laser/photodynamic therapy, retinoids, 5-FU, imiquimod, and photolyase-based approaches |
| [30178564](https://pubmed.ncbi.nlm.nih.gov/30178564/) | 2018 | Case Report | Pediatric Dermatology | Vismodegib used to treat multiple BCCs in an XP patient; 61% reduction in total lesion diameter after 16.5 months, with prevention of new lesions (one lesion later progressed) |
| [28297142](https://pubmed.ncbi.nlm.nih.gov/28297142/) | 2017 | Case Report | Pediatric Dermatology | Vismodegib 150 mg/day cleared a nodular BCC of the nasal tip in an 8-year-old XP patient after 4 months, in a site not amenable to Mohs surgery |
| [33901791](https://pubmed.ncbi.nlm.nih.gov/33901791/) | 2021 | Case Report | European Journal of Cancer | Combination of targeted therapy and immune checkpoint blockade in an XP patient with aggressive angiosarcoma and recurrent, non-resectable BCC |
| [36921168](https://pubmed.ncbi.nlm.nih.gov/36921168/) | 2023 | Case Report | Revista Paulista de Pediatria | General XP case report emphasizing early diagnosis and recognition of signs/symptoms (not vismodegib-specific) |

---

## Denmark Market Information

Vismodegib currently has **no marketing authorisations on record in Denmark** (0 licenses; market status: not marketed). No national (Lægemiddelstyrelsen) or centralised (EMA) authorisation data is available in this evidence pack for local product/dosage-form details.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (Hedgehog pathway / SMO inhibitor) — a non-cytotoxic small molecule, based on mechanism described in the literature within this evidence pack |
| Myelosuppression Risk | Please refer to the Summary of Product Characteristics (SmPC) warnings and precautions |
| Emetogenicity Classification | Please refer to the Summary of Product Characteristics (SmPC) warnings and precautions |
| Monitoring Items | Please refer to the Summary of Product Characteristics (SmPC) warnings and precautions |
| Handling Protection | Please refer to the Summary of Product Characteristics (SmPC) warnings and precautions |

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information. A drug-drug interaction search returned no results, and no formal warnings, contraindications, or interaction data are currently available in this evidence pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- Vismodegib is not currently marketed in Denmark (0 authorisations), and no clinical trials support any of the candidate indications identified by TxGNN for this drug.
- The strongest evidence available — two case reports of vismodegib used for XP-associated BCC — is real and mechanistically coherent, but remains case-report level (L3), well below the threshold needed for a Go decision.
- A **Blocking** data gap exists for the official product label (warnings/contraindications), which prevents this candidate from entering the S1 safety pre-assessment stage regardless of how promising the efficacy signal is.

**To proceed, the following is needed:**
- Official Danish/EU SmPC data (warnings, contraindications) — currently a Blocking data gap
- Confirmed mechanism-of-action documentation from DrugBank — currently a High-severity data gap
- A manual literature/trial search to verify whether the top-ranked candidate (medulloblastoma with extensive nodularity, TxGNN score 99.93%) truly lacks supporting evidence or whether this reflects a database collection gap, as flagged in the source rationale
- Clarification of the regulatory pathway (e.g., named-patient use, off-label protocol) by which XP-associated recurrent BCC could be treated with vismodegib in Denmark, given the drug is not locally marketed
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

