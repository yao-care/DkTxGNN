---
layout: default
title: Pazopanib
parent: 僅模型預測 (L5)
nav_order: 333
evidence_level: L5
indication_count: 10
---

# Pazopanib
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

Using the drug-repurposing evidence pack directly (no additional skill applies — this is a structured content-generation task per the prompt's own template). Note: the array's rank‑1/2 entries (ultra-rare RCC subtypes, pediatric RCC) carry zero clinical/literature evidence (L5/L4, Hold), while the **liposarcoma** candidate (score 0.9959, appearing at ranks 7–8) has 9 trials and 20 publications. As a repurposing analyst, that is the indication with an actual decision to report on, so it anchors this report; the near-empty candidates are summarized briefly rather than given empty tables.

# Pazopanib: From Renal Cell Carcinoma / Soft Tissue Sarcoma to Liposarcoma

## One-Sentence Summary

Pazopanib is a multi-target tyrosine kinase inhibitor internationally approved for advanced renal cell carcinoma and for non-adipocytic soft tissue sarcoma (liposarcoma subtypes were historically excluded from that approval).
The TxGNN model predicts it may also be effective specifically for **Liposarcoma**,
with **9 clinical trials** and **20 publications** currently supporting this direction — including two trials dedicated to pazopanib monotherapy in liposarcoma.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | No Danish label data on file (drug not marketed here). Based on known international labeling, pazopanib (Votrient) is approved for advanced renal cell carcinoma and for select soft tissue sarcoma subtypes |
| Predicted New Indication | Liposarcoma |
| TxGNN Prediction Score | 99.59% |
| Evidence Level | L2 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not present in the local database for this candidate. Based on known pharmacology (supplementary, not from local sources), pazopanib is an oral multi-target receptor tyrosine kinase inhibitor of VEGFR-1/2/3, PDGFR-α/β, and c-KIT, acting primarily through anti-angiogenic and anti-proliferative mechanisms.

Renal cell carcinoma and soft tissue sarcomas — including liposarcoma — share a strong dependence on tumour angiogenesis and, in several liposarcoma subtypes, PDGFR pathway activation. Pazopanib's established efficacy against VEGFR/PDGFR-driven tumours in RCC provides a mechanistic rationale for activity in liposarcoma.

Notably, liposarcoma was originally *excluded* from pazopanib's soft-tissue-sarcoma approval (based on a subgroup signal in the PALETTE trial), which is precisely why this TxGNN-flagged indication is clinically interesting: several dedicated post-hoc and prospective Phase 2 studies (e.g., NCT01692496, NCT01506596) subsequently examined pazopanib specifically in liposarcoma and reported disease control, suggesting the original exclusion may not fully reflect drug activity across all liposarcoma subtypes.

*Other candidates in this evidence pack* — ultra-rare RCC subtypes (neuroblastoma-associated RCC, Xp11.2/TFE3-fusion RCC), unclassified RCC, and childhood RCC — carry the same high TxGNN score band but have no supporting literature/trials specific to those populations (L4–L5, Hold) and are not detailed further here.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01692496](https://clinicaltrials.gov/study/NCT01692496) | Phase 2 | Completed | 52 | Pazopanib monotherapy in advanced/metastatic liposarcoma relapsed after standard therapy — direct pazopanib-liposarcoma evidence |
| [NCT01506596](https://clinicaltrials.gov/study/NCT01506596) | Phase 2 | Completed | 42 | Single-agent pazopanib in unresectable/metastatic liposarcoma |
| [NCT02357810](https://clinicaltrials.gov/study/NCT02357810) | Phase 2 | Completed | 178 | Pazopanib + oral topotecan in metastatic/non-resectable soft tissue and bone sarcomas |
| [NCT01532687](https://clinicaltrials.gov/study/NCT01532687) | Phase 2 | Completed | 54 | Randomized double-blind gemcitabine ± pazopanib in refractory soft tissue sarcoma |
| [NCT02180867](https://clinicaltrials.gov/study/NCT02180867) | Phase 2/3 | Active, not recruiting | 140 | Pazopanib neoadjuvant trial (chemoradiation ± pazopanib) in non-rhabdomyosarcoma soft tissue sarcoma |
| [NCT06239272](https://clinicaltrials.gov/study/NCT06239272) | Phase 1/2 | Recruiting | 139 | Maintenance pazopanib + dose-escalated radiotherapy ± selinexor in non-rhabdomyosarcoma soft tissue sarcoma (pediatric/AYA population) |
| [NCT01900743](https://clinicaltrials.gov/study/NCT01900743) | Phase 2 | Completed | 219 | Regorafenib (not pazopanib) in metastatic soft tissue sarcoma post-anthracycline — same drug class, indirect evidence only |
| [NCT02048371](https://clinicaltrials.gov/study/NCT02048371) | Phase 2 | Completed | 131 | SARC024: oral regorafenib across sarcoma subtypes — indirect, different drug |
| [NCT06263231](https://clinicaltrials.gov/study/NCT06263231) | Phase 3 | Active, not recruiting | 333 | Intratumoral INT230-6 vs. US standard of care in soft tissue sarcomas — different drug class, low relevance |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28844815](https://pubmed.ncbi.nlm.nih.gov/28844815/) | 2017 | RCT (PALETTE subgroup analysis) | The Lancet. Oncology | Commentary on pazopanib activity specifically in the liposarcoma subgroup of the pivotal PALETTE trial |
| [33355646](https://pubmed.ncbi.nlm.nih.gov/33355646/) | 2021 | Phase 2 RCT (PAPAGEMO, final results) | JAMA Oncology | Efficacy of pazopanib with/without gemcitabine in anthracycline/ifosfamide-refractory soft tissue sarcoma |
| [36890471](https://pubmed.ncbi.nlm.nih.gov/36890471/) | 2023 | RCT protocol (Phase 2, JCOG1802) | BMC Cancer | Randomized comparison of trabectedin, eribulin, and pazopanib as second-line therapy for advanced soft tissue sarcoma |
| [35609512](https://pubmed.ncbi.nlm.nih.gov/35609512/) | 2022 | Review | Oncology Research and Treatment | Overview of established and experimental systemic treatments for advanced liposarcoma, including pazopanib |
| [32026050](https://pubmed.ncbi.nlm.nih.gov/32026050/) | 2020 | Review | Current Treatment Options in Oncology | Systemic therapy options for dedifferentiated liposarcoma |
| [34050255](https://pubmed.ncbi.nlm.nih.gov/34050255/) | 2021 | Phase 2, single-arm | British Journal of Cancer | Pazopanib with oral topotecan active in refractory soft tissue sarcoma, prolongs PFS |
| [28832986](https://pubmed.ncbi.nlm.nih.gov/28832986/) | 2017 | Phase 2, prospective single-arm | Cancer | Single-agent pazopanib shows treatment activity and manageable safety in unresectable/metastatic liposarcoma |
| [31010343](https://pubmed.ncbi.nlm.nih.gov/31010343/) | 2019 | Cohort / subgroup analysis | Expert Opinion on Investigational Drugs | Review of pazopanib's anti-angiogenic activity in advanced intermediate/high-grade liposarcoma |
| [34356494](https://pubmed.ncbi.nlm.nih.gov/34356494/) | 2021 | Translational / pathology study | Biology | Molecular profiling of soft tissue sarcoma samples before/after neoadjuvant pazopanib (GISG-04/NOPASS) |
| [25500074](https://pubmed.ncbi.nlm.nih.gov/25500074/) | 2014 | Preclinical (xenograft) | Translational Oncology | Pazopanib suppresses tumour growth via anti-angiogenesis in dedifferentiated liposarcoma xenograft models |

## Denmark Market Information

Pazopanib currently has **no marketing authorisation on file in Denmark** (market status: Not marketed; 0 authorisations recorded). No Laegemiddelstyrelsen or EMA centralised licence data is available in this evidence pack to summarize.

## Cytotoxicity

Pazopanib's oncology use (renal cell carcinoma, soft tissue sarcoma) qualifies it for this section, though local toxicity/category data was not returned by DrugBank for this pack.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (multi-target receptor tyrosine kinase inhibitor — VEGFR/PDGFR/c-KIT; based on known pharmacology, not local database) |
| Myelosuppression Risk | Please refer to the Summary of Product Characteristics (SmPC) — TKIs as a class typically carry lower myelosuppression risk than conventional cytotoxic chemotherapy, but drug-specific hematologic data is not in this evidence pack |
| Emetogenicity Classification | Please refer to the SmPC |
| Monitoring Items | Please refer to the SmPC — general TKI monitoring commonly includes blood pressure, liver function tests, CBC, and QT interval |
| Handling Protection | Please refer to the SmPC and institutional oral-oncolytic handling policy |

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information — key warnings, contraindications, and drug-interaction data for pazopanib were not available in this evidence pack (data gap DG001, Blocking).

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple pazopanib-specific Phase 2 trials — including two dedicated to liposarcoma monotherapy (NCT01692496, NCT01506596) — plus PALETTE-trial subgroup literature support biological activity in liposarcoma. However, pazopanib is not currently marketed in Denmark and local safety/label data is entirely missing, so this cannot proceed without further work.

**To proceed, the following is needed:**
- Danish/EU SmPC warnings, contraindications, and DDI data (DG001, Blocking)
- Confirmed mechanism-of-action documentation from DrugBank (DG002, High)
- A Danish or EU marketing-authorisation pathway assessment, since pazopanib currently has zero licences on file here
- Direct citation and full data extraction from the PALETTE Phase 3 RCT (referenced only indirectly via PMID 28844815)
- Clarification of applicability across liposarcoma histologic subtypes (well-differentiated/dedifferentiated/myxoid/pleomorphic), since trial populations were heterogeneous
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

