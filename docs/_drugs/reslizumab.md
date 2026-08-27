---
layout: default
title: Reslizumab
parent: 僅模型預測 (L5)
nav_order: 372
evidence_level: L5
indication_count: 10
---

# Reslizumab
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

# Reslizumab: From Eosinophilic Asthma to Thrombocytopenia Due to Immune Destruction

## One-Sentence Summary

> Reslizumab is an anti-IL-5 monoclonal antibody; its confirmed approved indication is **not present in this Evidence Pack** (flagged as a blocking data gap — see below), though it is publicly known as a biologic for severe eosinophilic asthma.
> The TxGNN model predicts it may be effective for **Thrombocytopenia Due to Immune Destruction**, but this is currently supported by **0 clinical trials** and **0 publications**, and the model's own mechanistic rationale states there is **no known biological pathway** linking IL-5/eosinophil suppression to immune-mediated platelet destruction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not confirmed in Evidence Pack (data gap). Publicly known drug class: anti-IL-5 monoclonal antibody, historically used for severe eosinophilic asthma — **not verified against a regulatory source** |
| Predicted New Indication | Thrombocytopenia Due to Immune Destruction |
| TxGNN Prediction Score | 99.53% |
| Evidence Level | L5 (model prediction only, no clinical trials or literature) |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for Reslizumab is not available in this Evidence Pack (data gap DG002, High severity). Based on general pharmacological knowledge, Reslizumab is an anti-IL-5 monoclonal antibody that reduces circulating and tissue eosinophils; its efficacy has been established for eosinophil-driven respiratory disease, but this specific indication is not confirmed by the data provided here.

Critically, the Evidence Pack's own repurposing rationale for the top-ranked prediction explicitly argues **against** a plausible mechanistic link: immune thrombocytopenia is driven by anti-platelet autoantibodies (e.g., anti-GPIIb/IIIa) and Fc-receptor-mediated clearance by splenic macrophages — a pathway with no known intersection with IL-5 or eosinophil biology. The rationale states that IL-5 suppression does not affect B-cell autoantibody production or Fc-receptor-mediated platelet clearance, and characterizes this prediction as based **only on TxGNN embedding similarity, without biological support**.

Across all ten ranked predictions (five unique diseases, each duplicated), the pattern is consistent: all are platelet/hemostasis disorders (immune thrombocytopenia, primary platelet release disorder, pseudo-von Willebrand disease, autoimmune thrombocytopenia, Glanzmann thrombasthenia), all are scored L4–L5, and all carry a "Hold" recommendation. The one indirect literature signal (PMID 20565230) concerns **mepolizumab** — a different anti-IL-5 agent — in hypereosinophilic syndrome (HES), not Reslizumab, and not thrombocytopenia due to immune destruction directly. It offers, at best, a weak class-effect hypothesis (HES-associated bone marrow infiltration could secondarily affect platelets), not a validated mechanism.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for this indication (Thrombocytopenia Due to Immune Destruction).

**Note:** A related but lower-ranked TxGNN prediction for this drug — "primary release disorder of platelets" (score 99.25%) — is associated with one indirect publication:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [20565230](https://pubmed.ncbi.nlm.nih.gov/20565230/) | 2010 | Review | Current Medical Research and Opinion | Reviews management of hypereosinophilic syndrome (HES) including mepolizumab (a related but different anti-IL-5 agent); does not study Reslizumab or platelet disorders directly |

This publication is not direct evidence for Reslizumab or for the primary predicted indication.

---

## Denmark Market Information

Reslizumab is currently **not marketed** in Denmark. No Marketing Authorisations (national Laegemiddelstyrelsen or centralised EMA) are on record in this Evidence Pack.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information. Label warnings, contraindications, and drug-interaction data were not available at the time of this report (data gap DG001, **Blocking severity** — this gap prevents the candidate from entering the S1 safety pre-assessment stage).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This prediction rests solely on TxGNN embedding similarity (L5), with zero supporting clinical trials, zero direct literature, and no Danish market presence. The Evidence Pack's own mechanistic analysis states there is no known biological pathway connecting IL-5/eosinophil suppression to immune-mediated platelet destruction, and a Blocking-severity safety data gap (product label warnings/contraindications) prevents any safety pre-assessment.

**To proceed, the following is needed:**
- Confirmed original indication and approved SmPC from a Danish/EU regulatory source (currently unverified)
- Mechanism-of-action data via DrugBank API (data gap DG002)
- Product label warnings and contraindications (data gap DG001, blocking — required before S1 safety pre-assessment)
- Independent preclinical or mechanistic evidence connecting IL-5/eosinophil pathways to platelet destruction, beyond embedding-similarity prediction
- If further pursued, treat the mepolizumab/HES literature as a hypothesis-generating signal only, not clinical evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

