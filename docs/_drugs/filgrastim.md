---
layout: default
title: Filgrastim
parent: 僅模型預測 (L5)
nav_order: 190
evidence_level: L5
indication_count: 10
---

# Filgrastim
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

# Filgrastim: From Neutropenia / Stem Cell Mobilisation to Primary Release Disorder of Platelets

## One-Sentence Summary

Filgrastim is a recombinant human granulocyte colony-stimulating factor (G-CSF), established in clinical practice for treating chemotherapy-induced neutropenia and mobilising haematopoietic stem cells prior to transplantation.
The TxGNN model predicts it may be effective for **Primary Release Disorder of Platelets**, with **14 clinical trials** and **1 publication** retrieved — however, none directly address this indication.
Evidence is assessed at **Level L4**, reflecting mechanistic plausibility only; no direct clinical support currently exists.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available from Danish licensing data (no authorisations on file) |
| Predicted New Indication | Primary Release Disorder of Platelets |
| TxGNN Prediction Score | 99.998% |
| Evidence Level | L4 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on established pharmacology, Filgrastim is a recombinant G-CSF that stimulates the proliferation, differentiation, and activation of neutrophil precursors, and is widely used clinically to mobilise CD34+ haematopoietic stem cells from bone marrow into peripheral blood for collection and transplantation.

The mechanistic rationale proposed by TxGNN follows an indirect pathway: G-CSF administration → mobilisation of CD34+ haematopoietic stem cells → haematopoietic stem cell transplantation (HSCT) → potential curative correction of an inherited platelet release disorder. For severe, refractory cases of primary release disorder of platelets, HSCT is theoretically a curative option, and Filgrastim would function as the mobilisation agent enabling stem cell harvest. Some literature also suggests G-CSF may exert indirect effects on megakaryopoiesis pathways — the cellular lineage responsible for platelet production — though this has not been studied specifically in platelet release disorder populations.

The very high TxGNN score (99.998%) most likely reflects shared knowledge graph nodes connecting G-CSF → haematopoietic stem cell biology → HSCT → platelet disorder correction, rather than a direct pharmacological mechanism targeting the platelet release defect itself. No clinical trial has directly enrolled patients with primary release disorder of platelets to evaluate Filgrastim as a treatment.

---

## Clinical Trial Evidence

All 14 retrieved trials were independently assessed as **Grade C** — not directly relevant to the target indication. They involve HSCT procedures for unrelated conditions (autoimmune diseases, haematological malignancies, GVHD prophylaxis) where Filgrastim appears incidentally as a mobilisation agent. None enrolled patients specifically diagnosed with primary release disorder of platelets.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT00076752](https://clinicaltrials.gov/study/NCT00076752) | Phase 2 | Completed | 9 | Intensified lymphodepletion + autologous HSCT for severe SLE; Filgrastim used for stem cell mobilisation, not for platelet disorder |
| [NCT00923364](https://clinicaltrials.gov/study/NCT00923364) | Phase 2 | Completed | 19 | Reduced-intensity HSCT feasibility study for patients with GATA2 mutations; stem cell collection protocols included |
| [NCT00043979](https://clinicaltrials.gov/study/NCT00043979) | Phase 2 | Completed | 60 | Allogeneic/syngeneic blood stem cell transplantation for high-risk paediatric sarcomas; no platelet disorder endpoints |
| [NCT00281879](https://clinicaltrials.gov/study/NCT00281879) | Phase 2 | Terminated | 200 | Unrelated donor HSCT for haematological malignancies; terminated early, no platelet function endpoints |
| [NCT05436418](https://clinicaltrials.gov/study/NCT05436418) | Phase 1/2 | Recruiting | 260 | Optimising lowest effective dose of post-transplant cyclophosphamide for GVHD prophylaxis after peripheral blood SCT |
| [NCT06859424](https://clinicaltrials.gov/study/NCT06859424) | Phase 2 | Recruiting | 358 | Platform trial comparing GVHD prophylaxis regimens in mismatched unrelated donor PBSCT; primary endpoints are transplant outcomes |
| [NCT02646098](https://clinicaltrials.gov/study/NCT02646098) | Phase 2 | Completed | 64 | CD34+ selected vs unselected autologous SCT in advanced mantle cell and diffuse large B-cell lymphoma; oncology indication |
| [NCT04047628](https://clinicaltrials.gov/study/NCT04047628) | Phase 3 | Recruiting | 156 | Randomised controlled trial of AHSCT vs best available therapy for treatment-resistant relapsing multiple sclerosis |
| [NCT00245037](https://clinicaltrials.gov/study/NCT00245037) | Phase 1/2 | Completed | 147 | Non-myeloablative allogeneic HSCT for haematological malignancies using busulfan, fludarabine, and TBI |
| [NCT00354172](https://clinicaltrials.gov/study/NCT00354172) | Phase 2 | Terminated | 16 | Umbilical cord blood transplantation for myeloid leukaemia; terminated, not platelet disorder |

> **Assessment**: None of the above trials enrolled patients with primary release disorder of platelets. The retrieved trial set does not provide direct evidentiary support for this repurposing hypothesis.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [29770133](https://pubmed.ncbi.nlm.nih.gov/29770133/) | 2018 | Cohort Study | Frontiers in Immunology | G-CSF mobilisation in healthy allogeneic stem cell donors causes preferential mobilisation of specific lymphocyte subsets; relevant to understanding post-transplant immune complications but not to platelet release disorder treatment |

> **Assessment**: This single identified publication concerns immune cell mobilisation kinetics in stem cell donors, not the treatment of platelet release disorders. It provides no direct evidence for the repurposing hypothesis.

---

## Denmark Market Information

Filgrastim is **not currently marketed in Denmark** according to this Evidence Pack. No marketing authorisations from Lægemiddelstyrelsen (the Danish Medicines Agency) are recorded, and the total licence count is zero.

> **Important caveat**: Filgrastim products (originator Neupogen and biosimilars including Zarzio, Nivestim, Tevagrastim, and others) hold centralised EMA marketing authorisations valid across all EU/EEA member states, including Denmark. The "not marketed" status recorded here likely reflects that no product is actively distributed or listed on the Danish market at the time of this data cut (19 April 2026), rather than an absence of any EU-level regulatory approval. Healthcare professionals should verify current Danish market availability directly with Lægemiddelstyrelsen or the relevant marketing authorisation holders.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information. Key warnings, contraindications, and drug interactions were not available in this Evidence Pack (data gaps DG001 and DG002 were flagged as Blocking/High severity).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All 14 retrieved clinical trials are Grade C (none directly relevant to primary release disorder of platelets), only 1 peripherally related publication was identified, and no mechanistic action data (MOA) is available. The TxGNN high prediction score appears to reflect an indirect knowledge graph pathway (G-CSF → HSCT support → platelet disorder) rather than a validated direct pharmacological mechanism, making the repurposing hypothesis scientifically plausible in theory but unsupported by clinical evidence at this stage.

**To proceed, the following is needed:**

- **MOA data gap (DG002)**: Retrieve complete mechanism of action from DrugBank API to enable mechanistic link analysis
- **Safety data gap (DG001)**: Download and parse SmPC/PIL from Lægemiddelstyrelsen or EMA product information to complete contraindication and warning review before any S1 safety assessment
- **Targeted evidence search**: Conduct a focused literature search for G-CSF use specifically in inherited platelet function disorders and for HSCT mobilisation protocols in this rare disease population
- **Disease characterisation**: Confirm whether HSCT is an accepted standard-of-care option for severe refractory primary release disorder of platelets, which would validate the indirect mechanistic pathway
- **Denmark market clarification**: Verify current EMA centralised authorisation status and Danish distribution/reimbursement status for Filgrastim biosimilars through Lægemiddelstyrelsen

---

> **Note on additional TxGNN predictions**: Four further unique indications were predicted with high scores — pseudo-von Willebrand disease (99.997%, L5), Glanzmann thrombasthenia (99.996%, L5), Scott syndrome (99.956%, L5), and hemorrhagic disorder due to constitutional thrombocytopenia (99.911%, L5). All four are currently assessed as **Hold** due to absence of any direct clinical trial or literature evidence, and mechanistic plausibility is weak or absent for each. These predictions are likely artefacts of shared haematology/platelet nodes in the TxGNN knowledge graph.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

