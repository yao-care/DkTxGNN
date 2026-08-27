---
layout: default
title: Ribociclib
parent: 僅模型預測 (L5)
nav_order: 375
evidence_level: L5
indication_count: 10
---

# Ribociclib
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

# Ribociclib: From HR+/HER2- Metastatic Breast Cancer to Myeloid Leukemia

## One-Sentence Summary

> Ribociclib (DrugBank DB11730) is a CDK4/6 inhibitor whose established clinical use — evident throughout the literature in this evidence pack — is HR+/HER2-negative advanced/metastatic breast cancer; no formal original-indication record exists in the Danish regulatory file because the drug is currently **not marketed** in Denmark.
> The TxGNN model's top-ranked prediction is **Myeloid Leukemia**, supported by only **0 clinical trials** and **3 publications**, two of which describe a *case report of AML arising after* CDK4/6-inhibitor treatment rather than evidence of therapeutic benefit.
> Evidence is weak and directionally ambiguous — this candidate is not ready to advance.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on file in the Danish regulatory record (drug unmarketed); literature in this pack consistently identifies HR+/HER2- metastatic breast cancer as the established use |
| Predicted New Indication | Myeloid Leukemia |
| TxGNN Prediction Score | 99.35% |
| Evidence Level | L4 |
| Denmark Market Status | Not marketed (未上市) |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is flagged as a data gap in the formal record. Based on the literature retrieved in this pack, ribociclib is an orally administered, highly selective CDK4/6 inhibitor that blocks the CDK4/6–Rb pathway, arresting the cell cycle at the G1/S checkpoint. This mechanism underlies its established efficacy in HR+/HER2-negative breast cancer, where blocking proliferation of hormone-driven tumor cells is the therapeutic goal.

The mechanistic case for myeloid leukemia is genuinely mixed. One in-vitro study (PMID 32560251) explores CDK4/6 inhibitors as a way to overcome pharmacokinetic drug resistance in acute myeloid leukemia (AML) cells, offering a plausible rationale for anti-leukemic activity. However, a second report (PMID 30575100) describes a patient who developed AML with eosinophilia *after* CDK4/6-inhibitor treatment, in a setting of underlying clonal hematopoiesis — i.e., the drug class as a possible **contributor to**, rather than treatment for, myeloid malignancy. A third publication (PMID 41641105) is an unrelated vulvar adenocarcinoma case report with no clear connection to myeloid leukemia.

Because the supporting evidence points in two opposite directions — potential anti-leukemic mechanism vs. a signal of treatment-emergent AML — and no clinical trial has directly tested ribociclib in myeloid leukemia, the mechanistic plausibility cannot be considered established. This is reflected in the L4/S0 evidence classification and "Hold" recommendation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32560251](https://pubmed.ncbi.nlm.nih.gov/32560251/) | 2020 | Preclinical/mechanistic (in vitro) | Cancers | Explores CDK4/6 inhibitors to overcome pharmacokinetic drug resistance in AML cells, associated with ABCB1/ABCG2 transporter overexpression |
| [30575100](https://pubmed.ncbi.nlm.nih.gov/30575100/) | 2019 | Case report (adverse event) | American Journal of Hematology | AML with eosinophilia arising after CDK4/6-inhibitor treatment, in a patient with underlying clonal hematopoiesis of indeterminate potential — a treatment-related risk signal, not a treatment benefit |
| [41641105](https://pubmed.ncbi.nlm.nih.gov/41641105/) | 2026 | Case report (low relevance) | Frontiers in Oncology | Describes a vulvar/breast dual-primary adenocarcinoma case; no substantive link to myeloid leukemia |

---

## Denmark Market Information

Ribociclib currently has **no marketing authorisation on file** in the Danish regulatory record (market status: 未上市 / not marketed; total authorisations: 0). No product name, dosage form, or approved indication text is available to report.

---

## Cytotoxicity

Ribociclib is an antineoplastic agent (oral CDK4/6 inhibitor used in oncology), so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (CDK4/6 inhibitor) — not conventional cytotoxic chemotherapy |
| Myelosuppression Risk | High — literature in this pack consistently reports neutropenia, thrombocytopenia, anemia, lymphopenia, and febrile neutropenia as class-level hematological toxicities of CDK4/6 inhibitors |
| Emetogenicity Classification | Low to moderate (consistent with other CDK4/6 inhibitors) |
| Monitoring Items | CBC with differential, liver function tests, ECG/QTc (QT prolongation has been reported for this class) |
| Handling Protection | Please refer to the Summary of Product Characteristics (SmPC) and institutional hazardous-oral-oncolytic handling policy — formal handling classification data is not available in this evidence pack |

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information. Key warnings, contraindications, and drug-drug interaction data are not currently available in the regulatory record for this candidate (data gap DG001, Blocking severity).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- Evidence for the myeloid leukemia prediction is L4 (mechanistic/case-report only), with zero clinical trials and directionally conflicting literature — one mechanistic study suggests possible anti-leukemic activity, while a case report suggests the drug class may instead *cause* treatment-related AML. Combined with the drug's unmarketed status in Denmark and Blocking-severity gaps in safety labeling and MOA documentation, there is insufficient basis to proceed.

**To proceed, the following is needed:**
- Danish/EU SmPC with formal warnings, contraindications, and DDI data (DG001, Blocking)
- Confirmed mechanism-of-action documentation from DrugBank or equivalent (DG002, High)
- A dedicated preclinical or early-phase clinical study directly testing ribociclib activity in myeloid leukemia, rather than relying on incidental case reports
- Clarification of whether the AML signal in PMID 30575100 represents a class effect, requiring pharmacovigilance follow-up before any repurposing pathway is considered
- Formal confirmation of Denmark marketing status before any local development pathway is scoped
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

