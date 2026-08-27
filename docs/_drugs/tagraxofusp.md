---
layout: default
title: Tagraxofusp
parent: 僅模型預測 (L5)
nav_order: 416
evidence_level: L5
indication_count: 10
---

# Tagraxofusp
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

Using the report as a direct content-generation task (fixed template, no code/debug/design work — no skill fits this format-following writeup task, so producing it directly).

One judgment call up front: `predicted_indications[0]` (esotropia, score 99.73%) is explicitly flagged by the evidence pack's own rationale as a knowledge-graph embedding false positive with zero supporting evidence (same for ranks 5–8, and rank 10's "ductular proliferation" literature is confirmed keyword-coincidence, not drug-relevant). The only prediction with real trial evidence is rank 3, **pre-malignant neoplasm** (L2, S2, "Research Question"). I used that as the report's subject rather than the literal top-ranked-by-score entry, and noted the discarded predictions below.

# Tagraxofusp: From Blastic Plasmacytoid Dendritic Cell Neoplasm (BPDCN) to Pre-Malignant Neoplasm

## One-Sentence Summary

Tagraxofusp (SL-401, Elzonris) is a CD123-targeted diphtheria toxin fusion protein approved for blastic plasmacytoid dendritic cell neoplasm (BPDCN). The TxGNN model predicts potential relevance to **Pre-Malignant Neoplasm**, but the only supporting clinical evidence actually comes from trials in confirmed CD123+ myeloid malignancies (relapsed/refractory AML, BPDCN, myelofibrosis) — **5 clinical trials** support the mechanistic rationale, though **0 publications** and no trial directly targets a strictly defined pre-malignant disease stage.

> **Note:** TxGNN's top-ranked predictions for this drug (esotropia, inner ear neoplasm, benign tongue neoplasm, childhood bronchial adenoma/carcinoid) were assessed by the evidence pipeline itself as biologically implausible embedding artifacts with no supporting trials or literature, and are excluded from this report as false positives. A tenth candidate ("ductal or ductular proliferation") returned 20 PubMed hits, but all concern hepatic bile-duct pathology with no mention of tagraxofusp or CD123 — a keyword coincidence, not drug evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Blastic Plasmacytoid Dendritic Cell Neoplasm (BPDCN) *(sourced from clinical trial evidence in this pack; drug not yet authorised in Denmark, so no local SmPC indication text exists)* |
| Predicted New Indication | Pre-Malignant Neoplasm |
| TxGNN Prediction Score | 99.73% |
| Evidence Level | L2 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Tagraxofusp (SL-401) is a recombinant fusion protein combining human IL-3 with a truncated diphtheria toxin, designed to target CD123 (IL3RA)-expressing cells. It is approved for BPDCN, where malignant plasmacytoid dendritic cells characteristically overexpress CD123. Its cell-killing mechanism is distinct from conventional cytotoxic chemotherapy — it works via receptor-mediated internalization and toxin-driven cell death rather than DNA damage.

CD123 is also highly expressed on leukemic stem/progenitor cells across a broader range of myeloid disorders, including acute myeloid leukemia (AML), myelodysplastic syndrome (MDS), and myeloproliferative neoplasms (MPN) such as myelofibrosis. This shared target biology is the basis for TxGNN's mechanistic link between tagraxofusp and "pre-malignant neoplasm" — early or precursor-stage myeloid disease sharing the same CD123+ cell population as BPDCN.

However, the actual clinical trial evidence does not target a precisely defined "pre-malignant" clinical entity. All five identified trials enroll patients with **already-diagnosed** disease (relapsed/refractory AML, high-risk MDS, BPDCN, or myelofibrosis), with one trial (NCT07148180) targeting measurable residual disease (MRD) after treatment — conceptually closest to a "residual/precursor" state but not a formal pre-malignant diagnosis. This is a real label-to-population gap that should be flagged for any downstream use of this prediction.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03113643](https://clinicaltrials.gov/study/NCT03113643) | Phase 1 | Recruiting | 72 | SL-401 (tagraxofusp) combined with azacitidine ± venetoclax in relapsed/refractory AML, BPDCN, and high-risk MDS — direct drug/mechanism match (relevance grade A) |
| [NCT07148180](https://clinicaltrials.gov/study/NCT07148180) | Phase 1/2 | Recruiting | 31 | Tagraxofusp + azacitidine + venetoclax targeting measurable residual disease (MRD) in AML to prevent recurrence — closest conceptual match to a "pre-malignant/residual" state (grade B) |
| [NCT05476770](https://clinicaltrials.gov/study/NCT05476770) | Phase 1 | Recruiting | 54 | Tagraxofusp ± chemotherapy in pediatric relapsed/refractory CD123+ hematologic malignancies (grade B) |
| [NCT06414681](https://clinicaltrials.gov/study/NCT06414681) | Early Phase 1 | Not yet recruiting | 20 | Tagraxofusp + pacritinib in intermediate-2+ myelofibrosis after prior JAK inhibitor therapy (grade B) |
| [NCT03386513](https://clinicaltrials.gov/study/NCT03386513) | Phase 1/2 | Active, not recruiting | 179 | IMGN632 (pivekimab tazoxatane), a different CD123-targeted agent, in CD123+ AML — same target class, not tagraxofusp itself (grade C, indirect reference) |

## Literature Evidence

Currently no related literature available for the pre-malignant neoplasm indication.

## Denmark Market Information

Tagraxofusp currently has no marketing authorisation in Denmark — neither a national Laegemiddelstyrelsen authorisation nor an EMA centralised authorisation is on record (`market_status: Not marketed`, 0 licenses).

## Cytotoxicity

Tagraxofusp is an antineoplastic agent (approved for the hematologic malignancy BPDCN; CD123-directed cytotoxic fusion protein).

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (CD123-directed protein-toxin conjugate; diphtheria-toxin fusion protein, mechanistically distinct from conventional cytotoxic chemotherapy) |
| Myelosuppression Risk | Please refer to the Summary of Product Characteristics (SmPC) warnings and precautions |
| Emetogenicity Classification | Please refer to the Summary of Product Characteristics (SmPC) warnings and precautions |
| Monitoring Items | Please refer to the Summary of Product Characteristics (SmPC) warnings and precautions |
| Handling Protection | Please refer to the Summary of Product Characteristics (SmPC) warnings and precautions |

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
A blocking data gap exists on approved-label warnings and contraindications (no TFDA/Danish SmPC safety data available), which prevents even an initial (S1) safety assessment. The drug is not marketed in Denmark, and while the CD123 mechanistic rationale is plausible and supported by L2-level evidence (one directly matching Phase 1 trial plus several adjacent trials), no trial precisely targets the "pre-malignant neoplasm" label — all enroll patients with confirmed AML, BPDCN, MDS, or MPN.

**To proceed, the following is needed:**
- TFDA/Danish SmPC safety data — warnings, contraindications (currently a blocking gap, DG001)
- Detailed mechanism-of-action documentation from DrugBank (currently a data gap, DG002)
- Drug-drug interaction data (current query returned no results)
- Clarification of what "pre-malignant neoplasm" specifically denotes clinically, and whether the MRD/residual-disease trial (NCT07148180) or an equivalent population is an acceptable evidentiary substitute
- Monitoring of Danish/EMA marketing authorisation status, since the drug is currently unavailable in Denmark
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

