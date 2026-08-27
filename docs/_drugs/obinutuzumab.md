---
layout: default
title: Obinutuzumab
parent: 僅模型預測 (L5)
nav_order: 316
evidence_level: L5
indication_count: 6
---

# Obinutuzumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Obinutuzumab: From CD20+ B-Cell Malignancy to Follicular Lymphoma

## One-Sentence Summary

Obinutuzumab (DrugBank DB08935) is a type II anti-CD20 monoclonal antibody; Denmark-specific original indication and label data are not available in this dataset (data gap). The TxGNN model's evidence-backed lead candidate in this pack is **Follicular Lymphoma**, supported by **>40 matched clinical trials (10 highest-relevance shown)** — including two completed Phase 3 RCTs — and **19 publications**, giving it the strongest evidence level (L1) among all candidates evaluated.

> **Note on ranking**: TxGNN's top-scored predictions (rank 1–4) are narrowly-named CLL/SLL molecular subtypes (e.g. "pregerminal center CLL/SLL") that returned **zero** matching trials or literature — the pack's own analysis attributes this to disease-naming granularity, not a true absence of evidence, and recommends re-querying with broader CLL/SLL terms. Because Follicular Lymphoma (rank 5, score 99.18%, essentially tied with rank 1's 99.21%) is the only candidate in this dataset with actual retrievable evidence, it is used as the lead candidate for this report.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — drug is unregistered in Denmark; no local label/indication text on file (data gap DG001/DG002) |
| Predicted New Indication | Follicular Lymphoma |
| TxGNN Prediction Score | 99.18% |
| Evidence Level | L1 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Obinutuzumab is a glycoengineered, humanized type II anti-CD20 monoclonal antibody. It binds CD20 on the surface of B cells and induces cell death through a combination of antibody-dependent cellular cytotoxicity (ADCC), antibody-dependent cellular phagocytosis (ADCP), and direct (non-apoptotic) cell death — a mechanism distinct from and generally more potent than type I anti-CD20 antibodies such as rituximab.

Follicular lymphoma tumor cells are characteristically CD20-positive, making them a direct pharmacological match for obinutuzumab's target. This is not a speculative mechanistic leap: obinutuzumab (Gazyva/Gazyvaro) is already an approved therapy for follicular lymphoma in multiple other jurisdictions (both first-line and rituximab-refractory/relapsed settings), and the dataset's own clinical trial and literature record for FL is extensive and mature — including the pivotal Phase 3 GALLIUM trial (NCT01332968, n=1,401) comparing obinutuzumab-chemotherapy to rituximab-chemotherapy.

The other high-scoring predictions in this pack (pregerminal-center and IGHV-mutation-defined CLL/SLL subtypes) are mechanistically just as plausible — CD20 expression is independent of these molecular subtyping schemes — but this dataset could not retrieve trial or literature evidence for those exact subtype names. This is most likely a search-granularity artifact rather than a genuine absence of supporting data, and warrants a follow-up query using the broader term "chronic lymphocytic leukemia/small lymphocytic lymphoma" before those candidates are scored or dismissed.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01332968](https://clinicaltrials.gov/study/NCT01332968) | Phase 3 | Completed | 1401 | GALLIUM trial: obinutuzumab + chemotherapy vs rituximab + chemotherapy in previously untreated advanced indolent NHL (mostly FL) |
| [NCT01059630](https://clinicaltrials.gov/study/NCT01059630) | Phase 3 | Completed | 413 | Bendamustine alone vs bendamustine + obinutuzumab in rituximab-refractory indolent NHL |
| [NCT03332017](https://clinicaltrials.gov/study/NCT03332017) | Phase 2 | Completed | 217 | ROSEWOOD: zanubrutinib + obinutuzumab vs obinutuzumab monotherapy in relapsed/refractory FL (Grade A — key comparator trial) |
| [NCT01691898](https://clinicaltrials.gov/study/NCT01691898) | Phase 1/2 | Completed | 231 | Randomized evaluation of obinutuzumab-based combination regimens in relapsed/refractory FL (Grade A) |
| [NCT02611323](https://clinicaltrials.gov/study/NCT02611323) | Phase 1b/2 | Completed | 133 | Obinutuzumab + polatuzumab vedotin + venetoclax in relapsed/refractory FL (Grade A) |
| [NCT06191744](https://clinicaltrials.gov/study/NCT06191744) | Phase 3 | Recruiting | 1095 | EPCORE™FL-2: epcoritamab + R² vs chemoimmunotherapy in previously untreated FL |
| [NCT05100862](https://clinicaltrials.gov/study/NCT05100862) | Phase 3 | Recruiting | 780 | Zanubrutinib + anti-CD20 antibodies vs lenalidomide + rituximab in relapsed/refractory FL/MZL |
| [NCT05929222](https://clinicaltrials.gov/study/NCT05929222) | Phase 3 | Recruiting | 190 | GAZEBO: radiotherapy alone vs radiotherapy + obinutuzumab in early-stage FL |
| [NCT03980171](https://clinicaltrials.gov/study/NCT03980171) | Phase 1b/2 | Active, not recruiting | 50 | Lenalidomide + venetoclax + obinutuzumab in treatment-naïve FL (Grade B) |
| [NCT01680991](https://clinicaltrials.gov/study/NCT01680991) | Phase 1 | Completed | 48 | Pharmacokinetics/safety of obinutuzumab in Chinese patients with CD20+ malignancy (Grade B — dosing basis) |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28976863](https://pubmed.ncbi.nlm.nih.gov/28976863/) | 2017 | RCT | New England Journal of Medicine | GALLIUM: obinutuzumab-based vs rituximab-based chemotherapy for first-line FL |
| [29856692](https://pubmed.ncbi.nlm.nih.gov/29856692/) | 2018 | RCT | Journal of Clinical Oncology | GALLIUM sub-analysis: influence of chemotherapy backbone on efficacy/safety |
| [37404773](https://pubmed.ncbi.nlm.nih.gov/37404773/) | 2023 | RCT | HemaSphere | GALLIUM final analysis: obinutuzumab vs rituximab immunochemotherapy in untreated iNHL |
| [37506346](https://pubmed.ncbi.nlm.nih.gov/37506346/) | 2023 | RCT | Journal of Clinical Oncology | ROSEWOOD: zanubrutinib + obinutuzumab vs obinutuzumab monotherapy in relapsed/refractory FL |
| [31296423](https://pubmed.ncbi.nlm.nih.gov/31296423/) | 2019 | RCT | The Lancet Haematology | GALEN: obinutuzumab + lenalidomide in relapsed/refractory FL |
| [31360086](https://pubmed.ncbi.nlm.nih.gov/31360086/) | 2017 | Review | Blood and Lymphatic Cancer: Targets and Therapy | Impact of obinutuzumab alone and in combination for FL |
| [38660754](https://pubmed.ncbi.nlm.nih.gov/38660754/) | 2024 | Review | Turkish Journal of Haematology | Comprehensive review of FL management, including obinutuzumab-based regimens |
| [39830356](https://pubmed.ncbi.nlm.nih.gov/39830356/) | 2024 | Review/HTA | Frontiers in Pharmacology | Efficacy, safety and cost-effectiveness of obinutuzumab in FL |
| [35180337](https://pubmed.ncbi.nlm.nih.gov/35180337/) | 2022 | Review | Oncology (Williston Park) | Current and emerging therapies for FL |
| [28324270](https://pubmed.ncbi.nlm.nih.gov/28324270/) | 2017 | Review | Targeted Oncology | Obinutuzumab in rituximab-refractory/relapsed FL |

## Denmark Market Information

Obinutuzumab is currently not marketed in Denmark, and no marketing authorisations (national Laegemiddelstyrelsen or centralised EMA) are on file in this dataset.

## Cytotoxicity

Obinutuzumab is an antineoplastic agent (targeted immunotherapy class, used across CD20+ B-cell malignancies including the predicted FL indication).

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy / immunotherapy (anti-CD20 monoclonal antibody) — not a conventional cytotoxic chemotherapeutic |
| Myelosuppression Risk | Low–Moderate; anti-CD20 antibodies as a class are associated with neutropenia (including delayed-onset) and B-cell depletion; no drug-specific toxicity data available in this dataset |
| Emetogenicity Classification | Low; monoclonal antibodies are generally minimally emetogenic, though infusion-related reactions are common with first infusions |
| Monitoring Items | CBC with differential (neutropenia), hepatitis B screening/monitoring (anti-CD20 reactivation risk), infusion-related reaction monitoring during administration |
| Handling Protection | Standard biologic infusion precautions apply; does not require cytotoxic-drug handling protocols, but premedication and infusion monitoring per class labeling are advised — please refer to the SmPC for definitive guidance |

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information. No drug interaction, contraindication, or warning data specific to obinutuzumab were retrievable in this dataset (DDI query: not found).

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
- The Follicular Lymphoma indication is backed by L1-level evidence, including two completed Phase 3 RCTs (GALLIUM, and the bendamustine ± obinutuzumab trial) and a mature literature base of 19 publications, and mirrors approvals already granted in other jurisdictions.
- However, the drug is currently unregistered in Denmark, and both label-level safety data (DG001, Blocking) and formal MOA documentation (DG002, High) are data gaps that must be closed before an S1 safety review can proceed.

**To proceed, the following is needed:**
- TFDA/Danish SmPC warnings, contraindications, and DDI data (DG001)
- Verified mechanism-of-action documentation (DG002)
- Confirmation of EU/EMA centralised marketing authorisation status for obinutuzumab in Denmark
- A follow-up evidence search using the broader term "chronic lymphocytic leukemia/small lymphocytic lymphoma" to properly evaluate the rank 1–4 molecular-subtype predictions, which currently show zero evidence likely due to overly specific disease naming
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

