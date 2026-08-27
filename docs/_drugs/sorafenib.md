---
layout: default
title: Sorafenib
parent: 僅模型預測 (L5)
nav_order: 405
evidence_level: L5
indication_count: 10
---

# Sorafenib
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

Using the drug-repurposing report template embedded in this task's system prompt — this is a self-contained content-generation task, no separate skill applies (not code, not a debugging/build task).

I'll flag one interpretive gap before writing: `drug.original_indications` is empty and `original_moa` is marked `[Data Gap]`, yet the required title format needs an "original indication." The evidence pack itself (rank 9/10 rationale) states sorafenib is already an approved RCC treatment — I'm using that internally-sourced reference rather than external/memorized knowledge, and flagging it explicitly rather than treating it as verified.

---

# Sorafenib: From Renal Cell Carcinoma to Liposarcoma

*Note: `original_indications` and `original_moa` are empty/Data Gap in this evidence pack (DG002). "Renal Cell Carcinoma" is used here only because it is referenced as an already-approved sorafenib indication within the pack's own repurposing rationale (rank 9–10 entries) — this has not been independently verified against a formal label/SmPC and should be confirmed before use.*

## One-Sentence Summary

Sorafenib is a multi-kinase inhibitor with an approved oncology indication in renal cell carcinoma (per internal reference in this evidence pack). The TxGNN model's top-ranked prediction is **Liposarcoma**, supported by **1 directly relevant completed Phase 2 trial** and **8 publications**, though evidence remains preliminary and largely preclinical/indirect. Nine further candidate indications for sorafenib were also assessed in this pack at lower evidence levels.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Renal Cell Carcinoma (inferred from internal rationale only — not independently confirmed; see note above) |
| Predicted New Indication | Liposarcoma |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L2 |
| Denmark Market Status | Not Marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Formal mechanism-of-action data for sorafenib is flagged as a data gap in this pack (DG002). However, the repurposing rationale attached to the prediction describes sorafenib as a multi-targeted kinase inhibitor acting on VEGFR-1/2/3, PDGFR-β, and the RAF/MEK/ERK pathway — i.e., an anti-angiogenic and anti-proliferative mechanism rather than a formally documented drug label MOA.

Liposarcoma and other soft tissue sarcomas share dependence on angiogenic and RAS-RAF-MAPK signaling. Preclinical work included in this pack shows sorafenib suppresses MAPK signaling in dedifferentiated liposarcoma and malignant peripheral nerve sheath tumor cell lines (PMID 18413802), and a related xenograft study identifies PTEN downregulation as a malignant signature in dedifferentiated liposarcoma associated with PI3K pathway sensitivity (PMID 23416162) — a pathway mechanistically adjacent to, but not identical to, sorafenib's primary targets.

The strongest direct clinical evidence is a completed Phase 2 trial of sorafenib itself (development code BAY-9006/NSC #724772, NCT00217620) in advanced soft tissue sarcoma, and a separate SWOG-directed Phase 2 single-arm trial (PMID 21751200) in the same population. Neither trial was restricted to or powered specifically for liposarcoma, so the mechanistic link to this specific histologic subtype remains indirect rather than subtype-specific.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00217620](https://clinicaltrials.gov/study/NCT00217620) | Phase 2 | Completed | 51 | Direct evidence (Relevance Grade A): tested sorafenib itself (dev. code BAY-9006) in advanced soft tissue sarcomas, including liposarcoma subtypes. |
| [NCT02048371](https://clinicaltrials.gov/study/NCT02048371) | Phase 2 | Completed | 131 | Indirect evidence (Relevance Grade C): SARC024 tested regorafenib, not sorafenib — same Bayer multi-kinase inhibitor class, mechanism analogy only, not direct sorafenib data. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21751200](https://pubmed.ncbi.nlm.nih.gov/21751200/) | 2012 | Phase 2 trial (SWOG S0505) | Cancer | Sorafenib evaluated in advanced soft tissue sarcoma, a population with limited therapeutic options. |
| [24554062](https://pubmed.ncbi.nlm.nih.gov/24554062/) | 2014 | Phase 1 trial | Annals of Surgical Oncology | Neoadjuvant conformal radiotherapy plus sorafenib in locally advanced extremity soft tissue sarcoma. |
| [36003796](https://pubmed.ncbi.nlm.nih.gov/36003796/) | 2022 | Review | Frontiers in Oncology | PDOX mouse models of sarcoma identify effective combination therapies with the CDK inhibitor palbociclib. |
| [24712007](https://pubmed.ncbi.nlm.nih.gov/24712007/) | 2014 | Review | Magyar Onkologia | Medical treatment of soft tissue sarcomas by histological subtype. |
| [22987955](https://pubmed.ncbi.nlm.nih.gov/22987955/) | 2012 | Review | Annals of Oncology | Histology- and non-histology-driven therapy for soft tissue sarcomas, including liposarcoma. |
| [18413802](https://pubmed.ncbi.nlm.nih.gov/18413802/) | 2008 | Preclinical (in vitro/in vivo) | Molecular Cancer Therapeutics | Sorafenib inhibits MAPK signaling in MPNST and dedifferentiated liposarcoma cell lines. |
| [23416162](https://pubmed.ncbi.nlm.nih.gov/23416162/) | 2013 | Preclinical (xenograft) | American Journal of Pathology | Dedifferentiated liposarcoma xenograft models show PTEN downregulation; response to PI3K pathway inhibition (not sorafenib directly). |
| [25075796](https://pubmed.ncbi.nlm.nih.gov/25075796/) | 2014 | Case report | Anti-Cancer Drugs | Response to trabectedin (a different drug) in synovial sarcoma with lung metastases — limited direct relevance to sorafenib. |

## Denmark Market Information

No marketing authorisation records are present in this evidence pack — market status is recorded as "Not Marketed" with 0 total licenses.

## Cytotoxicity

Sorafenib is an antineoplastic, and its predicted new indications are exclusively oncology diagnoses, so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (multi-kinase inhibitor: VEGFR-1/2/3, PDGFR-β, RAF/MEK/ERK — per this pack's rationale text) |
| Myelosuppression Risk | Please refer to the Summary of Product Characteristics (SmPC) warnings and precautions |
| Emetogenicity Classification | Please refer to the Summary of Product Characteristics (SmPC) warnings and precautions |
| Monitoring Items | Please refer to the Summary of Product Characteristics (SmPC) warnings and precautions |
| Handling Protection | Please refer to the Summary of Product Characteristics (SmPC) warnings and precautions |

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
One directly relevant, completed Phase 2 trial of sorafenib itself in advanced soft tissue sarcoma (including liposarcoma) plus a second independent Phase 2 single-arm trial provide L2-level clinical evidence, but no trial was specifically powered for liposarcoma histology, and most supporting literature is preclinical or of a different tumor subtype.

**To proceed, the following is needed:**
- SmPC/label safety data (warnings, contraindications) — currently a Blocking data gap (DG001)
- Confirmed mechanism-of-action and original approved indication(s) from DrugBank/regulatory source — currently a High-severity data gap (DG002)
- Liposarcoma-subtype-specific trial data or post-hoc subgroup analysis from the existing STS trials
- Drug interaction (DDI) data — current query returned no results
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

