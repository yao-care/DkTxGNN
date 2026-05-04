---
layout: default
title: Chlorambucil
parent: 僅模型預測 (L5)
nav_order: 107
evidence_level: L5
indication_count: 10
---

# Chlorambucil
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

# Chlorambucil: From Chronic Lymphocytic Leukemia to CLL/SLL with IgHV Somatic Hypermutation

## One-Sentence Summary

Chlorambucil is a nitrogen mustard alkylating agent with a decades-long history as first-line treatment for chronic lymphocytic leukemia (CLL) and low-grade non-Hodgkin lymphomas.
The TxGNN model predicts it may be effective for **CLL/SLL with immunoglobulin heavy chain variable-region gene (IgHV) somatic hypermutation** — a molecularly distinct, more favourable-prognosis subtype of CLL — with a prediction score of **99.72%**.
However, the evidence pack contains **no clinical trials** and **no literature** specific to this molecular subtype, yielding an Evidence Level of **L5**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Chronic lymphocytic leukemia (CLL) and non-Hodgkin lymphomas (based on known clinical use; no regulatory record available in Denmark) |
| Predicted New Indication | CLL/SLL with IgHV somatic hypermutation (mutated IGHV subtype) |
| TxGNN Prediction Score | 99.72% |
| Evidence Level | L5 |
| Denmark Market Status | Not marketed (no marketing authorisation on file) |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the evidence pack. Based on established clinical knowledge, chlorambucil is a bifunctional alkylating agent belonging to the nitrogen mustard class. It forms interstrand and intrastrand DNA cross-links, blocking DNA replication and transcription, and ultimately inducing apoptosis in proliferating lymphocytes. This mechanism has made it effective against indolent lymphoid malignancies for over 50 years.

The predicted new indication — CLL/SLL with mutated IgHV (somatic hypermutation of the immunoglobulin heavy chain variable-region gene) — is not a separate disease but a molecularly defined subgroup within CLL. Patients with mutated IGHV have a significantly more indolent disease course, lower genomic complexity, and historically demonstrated better depth and duration of response to chlorambucil-based regimens compared with their unmutated IGHV counterparts. The TxGNN model's top prediction therefore reflects a biologically plausible subtype-refinement of chlorambucil's established indication rather than a wholly novel therapeutic use.

The landmark Phase 3 RESONATE-2 trial (PMID 36672456) explicitly used chlorambucil as the comparator arm for previously untreated CLL/SLL in patients aged ≥65 years, confirming its continued relevance as a benchmark therapy in this population. The model's prediction that the mutated IGHV subgroup may be a preferential target aligns with published prognostic data showing mutated IGHV as a predictor of superior outcomes with conventional chemotherapy.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for CLL/SLL with IgHV somatic hypermutation specifically.

---

## Literature Evidence

No publications identified specifically combining chlorambucil with CLL/SLL with IgHV somatic hypermutation.

> **Context note:** The evidence pack identifies supporting literature under secondary predicted indications (pregerminal center CLL/SLL and primary pulmonary lymphoma), detailed below.

---

## Supporting Evidence: Secondary Predicted Indications

The evidence pack lists several closely related predicted indications. Below is a consolidated summary of the available literature, which provides broader context for chlorambucil's activity in B-cell lymphoid malignancies.

### Pregerminal Center CLL/SLL (Rank 2, Score 99.72%)

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [12577769](https://pubmed.ncbi.nlm.nih.gov/12577769/) | 2003 | Review | Ned Tijdschr Geneeskd | Describes two molecular subtypes of CLL — pregerminal centre (unmutated IGHV) and post-germinal centre (mutated IGHV); argues for risk-adapted treatment; highlights that ~50% of stage A patients require treatment |

### Primary Pulmonary Lymphoma (Rank 7, Score 99.42%)

This indication has the strongest supporting literature in the evidence pack, with 16 publications including direct case reports and observational studies documenting chlorambucil use.

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [36672456](https://pubmed.ncbi.nlm.nih.gov/36672456/) | 2023 | RCT (Phase 3) | Cancers | RESONATE-2 ≥5-year follow-up: ibrutinib superior to chlorambucil in previously untreated CLL/SLL (≥65 years, no del(17p)); chlorambucil used as active comparator |
| [19541720](https://pubmed.ncbi.nlm.nih.gov/19541720/) | 2009 | Observational cohort | Eur Respir J | Pulmonary MALT lymphoma: 63-case multicentre series; evaluates clinical characteristics, staging, and long-term outcomes |
| [18603558](https://pubmed.ncbi.nlm.nih.gov/18603558/) | 2008 | Practice guidelines | Haematologica | Italian Society of Hematology guidelines for primary lung lymphomas; alkylating agents including chlorambucil listed as treatment options for low-grade subtypes |
| [25452791](https://pubmed.ncbi.nlm.nih.gov/25452791/) | 2015 | Case report / Review | Exp Ther Med | Pulmonary MALT lymphoma in a 19-year-old; reviews diagnostic approach and treatment strategies including chemotherapy |
| [3307632](https://pubmed.ncbi.nlm.nih.gov/3307632/) | 1987 | Phase II trial | Cancer Chemother | Chlorambucil 4–6 mg/day in 8 haematological malignancies including CLL and pseudolymphoma of the lung; partial remission achieved in CLL and pulmonary pseudolymphoma |
| [3699123](https://pubmed.ncbi.nlm.nih.gov/3699123/) | 1986 | Case report | Eur J Respir Dis | Primary NHL of the lung with bilateral infiltrates; chlorambucil given for 5 months; patient achieved subsequent remission |
| [6248988](https://pubmed.ncbi.nlm.nih.gov/6248988/) | 1980 | Case report | Sem Hop Paris | Primary lymphosarcoma of the lung secreting IgM; 3-year clinical remission maintained with continuous chlorambucil monotherapy |
| [11289295](https://pubmed.ncbi.nlm.nih.gov/11289295/) | 2001 | Case report | Dis Colon Rectum | Simultaneous MALT lymphoma of colon and lung; treated with mitoxantrone and chlorambucil combination |
| [11223743](https://pubmed.ncbi.nlm.nih.gov/11223743/) | 2001 | Case report | Respiration | Pulmonary MALT lymphoma in a common variable immunodeficiency patient; discusses treatment approach including alkylating agents |
| [11483337](https://pubmed.ncbi.nlm.nih.gov/11483337/) | 2001 | Retrospective | Int J Radiat Oncol | Stage I/II MALT lymphoma across multiple organs treated with involved-field radiotherapy; establishes treatment benchmarks |

---

## Denmark Market Information

No marketing authorisations for chlorambucil are registered in the Laegemiddelstyrelsen database as of the data cutoff (2026-04-04).

> **Important note for Danish clinicians:** Chlorambucil (brand name Leukeran, Aspen Pharma) holds marketing authorisations in several EU member states and has historically been available via centralised or national procedures. The absence of a record in this evidence pack may reflect a data gap rather than true non-availability. Direct verification with the Laegemiddelstyrelsen is required before any clinical consideration.

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — Alkylating agent (nitrogen mustard class, bifunctional) |
| Myelosuppression Risk | High — dose-limiting toxicities include neutropenia, thrombocytopenia, and anaemia; myelosuppression is cumulative and may be prolonged |
| Emetogenicity Classification | Low to moderate (oral tablet; generally well tolerated in this regard) |
| Monitoring Items | Full blood count with differential (CBC) before each course; liver function tests; renal function (eGFR); uric acid and LDH (tumour lysis risk at initiation) |
| Handling Protection | Oral solid dosage form; must be handled according to cytotoxic drug handling regulations (PPE required; tablets must not be crushed; disposal per hazardous waste protocols) |

---

## Safety Considerations

Detailed warnings and contraindication data are not available in this evidence pack. Please refer to the approved Summary of Product Characteristics (SmPC) for full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top predicted indication — CLL/SLL with mutated IgHV — represents a molecular subtype of chlorambucil's established historical indication rather than a genuinely novel use. The evidence pack returns zero clinical trials and zero dedicated literature for this specific subtype (L5), no marketing authorisation data for Denmark is on file, and critical safety data (SmPC warnings, contraindications, DDI profile) are absent. Furthermore, modern CLL treatment guidelines have largely displaced chlorambucil with BTK inhibitors and BCL-2 inhibitors for most patients, limiting the clinical relevance of further investigation unless specifically targeting a cost-sensitive, elderly, or comorbid population where chlorambucil retains a role.

**To proceed, the following is needed:**

- Verify current Laegemiddelstyrelsen / EMA marketing authorisation status for chlorambucil (Leukeran) and obtain the approved Danish SmPC
- Retrieve full safety data: TFDA/EMA label warnings and contraindications (Data Gap DG001) and DrugBank MOA entry (Data Gap DG002)
- Conduct a targeted literature review of landmark CLL trials (RESONATE-2, CLL8, CLL10, COMPLEMENT-1) with IgHV mutation-stratified subgroup analyses to assess whether mutated IGHV patients derive quantifiably superior benefit from chlorambucil
- Define the specific clinical niche (e.g., elderly patients with comorbidities unsuitable for intensive regimens) in which chlorambucil in the mutated IGHV subgroup would add value over current standard-of-care options
- If proceeding to primary pulmonary lymphoma (rank 7), formalise evidence level for the existing case series and evaluate whether an investigator-initiated study is warranted given the absence of any registered trials
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

