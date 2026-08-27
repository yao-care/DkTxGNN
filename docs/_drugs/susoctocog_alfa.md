---
layout: default
title: Susoctocog Alfa
parent: 僅模型預測 (L5)
nav_order: 411
evidence_level: L5
indication_count: 10
---

# Susoctocog Alfa
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

# Susoctocog Alfa: Toward Hemophilia (Acquired Factor VIII Deficiency) — Original Indication Not on Record

## One-Sentence Summary

> Susoctocog alfa (DrugBank DB11606) is a recombinant, B-domain-deleted porcine-sequence Factor VIII product; its originally documented indication is not recorded in the current data source.
> The TxGNN model's highest-evidenced prediction points to **Hemophilia (specifically Acquired Hemophilia A)**,
> supported by **1 clinical trial** and **20 publications**, including real-world cohort studies and reviews.
> Note: TxGNN's top-ranked predictions by raw score (platelet release disorder, pseudo-von Willebrand disease, Glanzmann thrombasthenia) have **zero supporting trials or literature** and are flagged in the model's own rationale as likely knowledge-graph proximity artifacts — they are excluded from the primary recommendation below.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in current data source (data gap) |
| Predicted New Indication | Hemophilia (Acquired Hemophilia A) |
| TxGNN Prediction Score | 99.74% |
| Evidence Level | L3 (Observational studies / reviews; no completed RCT on file) |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Formal mechanism-of-action data is currently a data gap for this record. However, the literature evidence collected alongside the prediction is unambiguous: susoctocog alfa is described as "a recombinant, B-domain deleted, porcine sequence antihaemophilic factor VIII (FVIII) product" (Burness & Scott, *Drugs* 2016, PMID 27098420) used to restore hemostatic FVIII activity in patients whose endogenous FVIII is neutralized by autoantibodies.

This maps directly onto the pathophysiology of **Acquired Hemophilia A (AHA)** — a bleeding disorder caused by autoantibody inhibition of Factor VIII — which is exactly the clinical population described across the 20 associated publications and the ongoing post-marketing surveillance trial (NCT06461533, Japan). In other words, the TxGNN signal for "hemophilia" is not a novel mechanistic leap; it is a knowledge-graph rediscovery of the drug's already-established, literature-documented use. For Denmark, the open question is therefore not mechanistic plausibility but **market entry/registration status**, since the drug currently holds zero Danish marketing authorisations.

By contrast, TxGNN's numerically higher-scoring predictions (primary platelet release disorder, pseudo-von Willebrand disease, Glanzmann thrombasthenia) involve platelet-function or platelet-membrane defects that are mechanistically unrelated to FVIII replacement. The evidence pack's own rationale explicitly attributes these to graph-embedding proximity among "bleeding tendency" nodes rather than genuine mechanistic or clinical signal, and no trials or literature support any of them. They are therefore not treated as actionable candidates in this report.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06461533](https://clinicaltrials.gov/study/NCT06461533) | N/A | Recruiting | 25 | Japanese all-case post-marketing surveillance of IV susoctocog alfa (OBIZER) in patients with bleeding events of Acquired Hemophilia A; monitors side effects and treatment outcomes. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27098420](https://pubmed.ncbi.nlm.nih.gov/27098420/) | 2016 | Review | Drugs | Comprehensive review of susoctocog alfa (Obizur); references a completed multinational Phase II/III trial (n=28 evaluable) showing effective, generally well-tolerated control of serious bleeds in AHA. |
| [32698943](https://pubmed.ncbi.nlm.nih.gov/32698943/) | 2020 | Cohort | Blood Transfusion | Italian multicentre real-world registry of 9 elderly AHA patients treated with susoctocog alfa. |
| [39158833](https://pubmed.ncbi.nlm.nih.gov/39158833/) | 2024 | Cohort (Phase II/III, NCT04580407) | Int J Hematol | Japanese open-label study of efficacy/safety of recombinant porcine FVIII in AHA; primary endpoint met for severe bleeding control. |
| [39245591](https://pubmed.ncbi.nlm.nih.gov/39245591/) | 2024 | Review | Rev Med Interne | 2024 update on acquired hemophilia diagnosis and treatment landscape. |
| [40812597](https://pubmed.ncbi.nlm.nih.gov/40812597/) | 2025 | PK study | J Thromb Haemost | Pharmacokinetic strategies for precise FVIII control with susoctocog alfa in AHA. |
| [37510704](https://pubmed.ncbi.nlm.nih.gov/37510704/) | 2023 | Case series / Review | J Clin Med | Surgery and prophylaxis with susoctocog alfa in AHA; case series and literature review. |
| [38066923](https://pubmed.ncbi.nlm.nih.gov/38066923/) | 2023 | Review | Hematology ASH Educ Program | Diagnosis and laboratory monitoring of AHA, relevant to treatment-monitoring context. |
| [41436689](https://pubmed.ncbi.nlm.nih.gov/41436689/) | 2025 | Case report | CEN Case Reports | Successful hemodialysis initiation in AHA managed with susoctocog alfa plus emicizumab. |
| [34011555](https://pubmed.ncbi.nlm.nih.gov/34011555/) | 2023 | Case report | Eur J Hosp Pharm | High-risk bleeding treated with susoctocog alfa in an AHA patient with concurrent SARS-CoV-2 infection. |
| [35501873](https://pubmed.ncbi.nlm.nih.gov/35501873/) | 2022 | Case report | J Med Case Rep | AHA with coexisting lupus anticoagulant. |

---

## Denmark Market Information

Susoctocog alfa currently holds **no marketing authorisation** in Denmark — neither a national Laegemiddelstyrelsen licence nor an EMA centralised authorisation is on record (0 of 0 licenses).

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information. Key warnings, contraindications, and drug-interaction data are not currently available in this evidence pack; obtaining the manufacturer's TFDA/EMA-approved SmPC is a **blocking** requirement before any safety pre-assessment (S1) can proceed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- Mechanistic plausibility is well supported by 20 publications and 1 ongoing surveillance trial confirming the drug's established FVIII-replacement role in Acquired Hemophilia A (Evidence Level L3), but there is no completed Phase 3 RCT on file, no Danish marketing authorisation, and no accessible SmPC safety data — a blocking gap for further evaluation.

**To proceed, the following is needed:**
- SmPC/TFDA warnings, contraindications, and drug-interaction data (Blocking gap DG001)
- Confirmed mechanism-of-action documentation from DrugBank or manufacturer labeling (High-priority gap DG002)
- Clarification of the drug's original approved indication(s), currently unrecorded in this data source
- Assessment of the Danish regulatory pathway for a product with no existing EU/EMA-linked Danish licence
- Deprioritize or formally rule out the platelet-disorder / von Willebrand / Glanzmann thrombasthenia predictions, which lack any supporting evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

