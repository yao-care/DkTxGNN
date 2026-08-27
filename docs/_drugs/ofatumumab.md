---
layout: default
title: Ofatumumab
parent: 僅模型預測 (L5)
nav_order: 318
evidence_level: L5
indication_count: 10
---

# Ofatumumab
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

# Ofatumumab: From Chronic Lymphocytic Leukemia to Follicular Lymphoma

## One-Sentence Summary

Ofatumumab is a fully human anti-CD20 monoclonal antibody originally used to treat chronic lymphocytic leukemia (CLL), targeting the CD20 antigen on malignant B-cells. The TxGNN model predicts it may also be effective for **Follicular Lymphoma**, a related CD20-positive B-cell malignancy, with **15 clinical trials** and **20 publications** currently supporting this direction. Note: TxGNN's single highest-scoring prediction was actually a molecular CLL subtype (IGHV-mutated CLL/SLL, score 99.77%), but that candidate currently has zero dedicated evidence; Follicular Lymphoma (score 99.70%) is presented here as the most actionable, evidence-backed candidate.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic Lymphocytic Leukemia (CLL) — derived from the collected literature evidence in this pack (e.g., PMID 22830942), as the formal `original_indications` field was not populated |
| Predicted New Indication | Follicular Lymphoma |
| TxGNN Prediction Score | 99.70% |
| Evidence Level | L2 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available from DrugBank for this candidate (flagged as a High-severity data gap, DG002). Based on the literature evidence collected in this pack, ofatumumab is consistently described as a fully human IgG1κ monoclonal antibody that binds a distinct membrane-proximal epitope on the CD20 antigen, triggering B-cell death predominantly through complement-dependent cytotoxicity (CDC) and antibody-dependent cell-mediated cytotoxicity (ADCC).

CLL and follicular lymphoma are both CD20-positive, indolent B-cell malignancies that share the same target antigen and cell-killing mechanism. Multiple sources in this pack (e.g., PMID 28983798, PMID 29934061) note that anti-CD20 antibodies as a class are already used across CLL, follicular lymphoma, and diffuse large B-cell lymphoma, and several trials in this pack enrolled mixed CLL/FL populations under the same protocol (e.g., NCT00742144), underscoring the mechanistic overlap.

Because the biological target and cytotoxic mechanism are identical between the original indication (CLL) and the predicted indication (follicular lymphoma), extending ofatumumab's use to FL is mechanistically well-supported — an inference reinforced by the fact that ofatumumab has already been studied directly in FL populations in numerous completed trials, described below.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01077518](https://clinicaltrials.gov/study/NCT01077518) | Phase 3 | Terminated | 346 | Randomized comparison of ofatumumab + bendamustine vs. bendamustine alone in rituximab-unresponsive indolent B-cell NHL (includes FL); largest and only Phase 3 trial identified, but terminated — reason not specified in this pack |
| [NCT01286272](https://clinicaltrials.gov/study/NCT01286272) | Phase 2 | Completed | 135 | Randomized trial of ofatumumab + bendamustine vs. ofatumumab + bortezomib + bendamustine in untreated follicular lymphoma |
| [NCT01294579](https://clinicaltrials.gov/study/NCT01294579) | Phase 2 | Completed | 49 | Ofatumumab + bendamustine induction followed by ofatumumab maintenance in indolent B-NHL relapsed after rituximab |
| [NCT02710643](https://clinicaltrials.gov/study/NCT02710643) | Phase 2 | Completed | 110 | Involved-field radiotherapy with/without ofatumumab in early-stage (I/II) follicular lymphoma, stratified by Bcl-2 status |
| [NCT00742144](https://clinicaltrials.gov/study/NCT00742144) | Phase 1 | Completed | 6 | Safety, tolerability, and PK of ofatumumab monotherapy in Japanese FL/CLL patients |
| [NCT00394836](https://clinicaltrials.gov/study/NCT00394836) | Phase 2 | Completed | 116 | Ofatumumab monotherapy in rituximab-refractory follicular lymphoma |
| [NCT01190449](https://clinicaltrials.gov/study/NCT01190449) | Phase 2 | Completed | 51 | Ofatumumab in previously untreated stage II–IV follicular NHL (CALGB) |
| [NCT00494780](https://clinicaltrials.gov/study/NCT00494780) | Phase 2 | Completed | 59 | Two-dose ofatumumab regimens combined with CHOP in untreated follicular lymphoma |
| [NCT01239394](https://clinicaltrials.gov/study/NCT01239394) | Phase 2 | Completed | 43 | Ofatumumab as initial systemic treatment for indolent B-cell lymphoma |
| [NCT00823719](https://clinicaltrials.gov/study/NCT00823719) | Phase 2 | Completed | 61 | Ofatumumab + ICE or DHAP salvage chemotherapy in relapsed/refractory aggressive lymphoma pre-transplant |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31174236](https://pubmed.ncbi.nlm.nih.gov/31174236/) | 2019 | RCT | Cancer | CALGB 50904: randomized Phase 2 trial of ofatumumab+bendamustine vs. triplet with bortezomib in untreated high-risk FL |
| [30723894](https://pubmed.ncbi.nlm.nih.gov/30723894/) | 2019 | Phase 2 multicentre study | British Journal of Haematology | CALGB 50901: single-agent ofatumumab efficacy in untreated, low/intermediate-risk advanced-stage FL |
| [38937025](https://pubmed.ncbi.nlm.nih.gov/38937025/) | 2024 | Phase 2 trial (final results) | The Lancet. Haematology | FIL MIRO: MRD-driven radiotherapy plus anti-CD20 mAb in early-stage FL |
| [22389254](https://pubmed.ncbi.nlm.nih.gov/22389254/) | 2012 | Multicenter study | Blood | Ofatumumab monotherapy in rituximab-refractory FL; ORR 13% (chemo-refractory subgroup) to 10% overall |
| [22409295](https://pubmed.ncbi.nlm.nih.gov/22409295/) | 2012 | Phase 2 chemoimmunotherapy | British Journal of Haematology | Ofatumumab + CHOP (O-CHOP) as frontline treatment for FL, two dose levels compared |
| [18390837](https://pubmed.ncbi.nlm.nih.gov/18390837/) | 2008 | Phase 1/2 trial | Blood | First clinical use of ofatumumab in relapsed/refractory FL (grade 1–2) |
| [29934061](https://pubmed.ncbi.nlm.nih.gov/29934061/) | 2018 | Evidence-based review | Clinical Lymphoma, Myeloma & Leukemia | Rapid evidence review of anti-CD20 regimens in relapsed/refractory CLL, FL, and DLBCL |
| [34607678](https://pubmed.ncbi.nlm.nih.gov/34607678/) | 2021 | Review | Bulletin du Cancer | European approval review of duvelisib in relapsed/refractory CLL and FL, contextualizing anti-CD20 comparators |
| [21083037](https://pubmed.ncbi.nlm.nih.gov/21083037/) | 2010 | Review | Expert Review of Hematology | Emerging therapeutic strategies in follicular lymphoma |
| [26043777](https://pubmed.ncbi.nlm.nih.gov/26043777/) | 2015 | Review | Expert Opinion on Biological Therapy | Review of ofatumumab activity in CD20+ B-cell lymphomas including FL |

---

## Denmark Market Information

Ofatumumab currently holds **no marketing authorisation in Denmark** (market status: Not marketed; 0 authorisations on file). No national (Laegemiddelstyrelsen) or centralised (EMA) licence records were found in this evidence pack.

---

## Cytotoxicity (Antineoplastic Drugs Only)

Ofatumumab is antineoplastic (approved for CLL, a haematologic malignancy, and studied here for follicular lymphoma).

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted immunotherapy (anti-CD20 monoclonal antibody, not a conventional cytotoxic chemotherapy agent) |
| Myelosuppression Risk | Please refer to the Summary of Product Characteristics (SmPC) warnings and precautions |
| Emetogenicity Classification | Please refer to the Summary of Product Characteristics (SmPC) warnings and precautions |
| Monitoring Items | CBC with differential; hepatitis B screening prior to initiation (standard practice for anti-CD20 agents); monitoring for infusion-related reactions |
| Handling Protection | Not a conventional cytotoxic chemotherapy agent requiring cytotoxic drug handling precautions; standard IV biologic infusion protocol with antihistamine/corticosteroid premedication applies |

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information. No warnings, contraindications, or drug interaction data were available in this evidence pack (TFDA/Laegemiddelstyrelsen label data is flagged as a Blocking data gap, DG001, pending SmPC PDF retrieval).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Follicular lymphoma shares the same CD20 target and cytotoxic mechanism as ofatumumab's original indication (CLL), and this is directly supported by an L2 evidence base — including a completed randomized Phase 2 trial (CALGB 50904) plus multiple additional completed Phase 1/2 studies spanning frontline, relapsed/refractory, and radiotherapy-combination settings. However, the only Phase 3 trial identified (NCT01077518) was terminated, and the drug is not currently marketed in Denmark.

**To proceed, the following is needed:**
- TFDA/Laegemiddelstyrelsen SmPC data (warnings, contraindications) — currently a Blocking gap (DG001)
- Formal DrugBank-sourced MOA and drug category data (DG002)
- Clarification of the termination reason for the Phase 3 trial (NCT01077518)
- A formal drug-drug interaction (DDI) review, as none was found in this pack
- Assessment of the Danish market-access pathway (e.g., named-patient/import route), given the drug currently holds no local authorisation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

