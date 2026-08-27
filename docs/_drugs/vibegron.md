---
layout: default
title: Vibegron
parent: 僅模型預測 (L5)
nav_order: 470
evidence_level: L5
indication_count: 10
---

# Vibegron
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

# Vibegron: From Overactive Bladder to Polycystic Kidney Disease 3

## One-Sentence Summary

Vibegron is a highly selective β3-adrenergic receptor agonist developed for overactive bladder (OAB), acting on detrusor muscle β3 receptors to promote bladder relaxation during the storage phase. The TxGNN model predicts a possible link to **Polycystic Kidney Disease 3 (with or without Polycystic Liver Disease)**, with a prediction score of **94.50%**, but this is currently supported by **zero clinical trials** and only general disease-background literature — no evidence directly connects Vibegron to this indication.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Overactive bladder (OAB) — derived from externally verified mechanism-of-action data; not available from Danish licensing records, as the drug is not marketed in Denmark |
| Predicted New Indication | Polycystic kidney disease 3 with or without polycystic liver disease |
| TxGNN Prediction Score | 94.50% |
| Evidence Level | L5 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

The Evidence Pack's structured data marks Vibegron's mechanism of action as a data gap. Externally verified information indicates Vibegron is a highly selective β3-adrenergic receptor agonist: it relaxes detrusor smooth muscle during bladder filling and suppresses parasympathetic acetylcholine release, which is the basis for its approved use in overactive bladder.

Polycystic Kidney Disease 3 (PKD3) and associated polycystic liver disease belong to a genetically distinct disease class — a ciliopathy driven by mutations affecting polycystin and related fibrocystin/PKHD1 pathways, leading to progressive cyst formation in kidney and liver. There is no established biological pathway connecting β3-adrenergic receptor agonism to polycystin-mediated ciliary signaling or cystogenesis.

Given this, the high TxGNN score (94.50%) most likely reflects knowledge-graph embedding similarity (e.g., shared graph neighbors or indirect associations) rather than a genuine pharmacological rationale. This assessment is consistent with the reviewed literature, which addresses PKD/PLD disease biology in general but contains no study of Vibegron or any β3-agonist in this disease context.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

*Note: the following literature discusses PKD3/polycystic liver disease pathophysiology and management in general — none of it studies Vibegron directly. It is included as disease-background context only.*

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35728731](https://pubmed.ncbi.nlm.nih.gov/35728731/) | 2022 | Guideline | Journal of Hepatology | EASL clinical practice guidelines on diagnosis and management of cystic liver diseases, including polycystic liver disease |
| [30819518](https://pubmed.ncbi.nlm.nih.gov/30819518/) | 2019 | Review | Lancet | Overview of autosomal dominant polycystic kidney disease (ADPKD) as a systemic disorder with renal and extrarenal (hepatic) manifestations |
| [35487607](https://pubmed.ncbi.nlm.nih.gov/35487607/) | 2022 | Review | Clinics in Liver Disease | ADPKD and polycystic liver disease (PCLD) follow a similar clinical course of hepatomegaly with preserved liver function; tolvaptan can slow renal deterioration |
| [29038287](https://pubmed.ncbi.nlm.nih.gov/29038287/) | 2018 | Review | JASN | Genetic overlap between ADPKD and autosomal dominant polycystic liver disease (ADPLD); eight causative genes identified |
| [38097330](https://pubmed.ncbi.nlm.nih.gov/38097330/) | 2023 | Pending classification | Advances in Kidney Disease and Health | PKD1/PKD2 mutations account for most ADPKD cases; ciliary dysfunction is central to pathogenesis |
| [34724412](https://pubmed.ncbi.nlm.nih.gov/34724412/) | 2022 | Pending classification | Annual Review of Pathology | PLD mechanisms involve primary (causative gene mutation), secondary (cyst initiation), and tertiary (cystogenesis progression) processes |
| [36200122](https://pubmed.ncbi.nlm.nih.gov/36200122/) | 2022 | Pending classification | Hepatic Medicine: Evidence and Research | Overview of PLD pathophysiology, diagnosis and treatment; most patients asymptomatic |
| [35777701](https://pubmed.ncbi.nlm.nih.gov/35777701/) | 2023 | Pending classification | Human Pathology | Update on ductal plate malformations and fibropolycystic liver diseases |
| [38689396](https://pubmed.ncbi.nlm.nih.gov/38689396/) | 2024 | Pending classification | Kidney360 | Genetic analysis of severe PLD in Japan; PKD2 variants found in 34% of severe cases |
| [40296340](https://pubmed.ncbi.nlm.nih.gov/40296340/) | 2025 | Pending classification | Annals of Transplantation | Outcomes of combined liver-kidney transplantation in 9 PLD/PKD patients |

## Denmark Market Information

Vibegron currently holds no marketing authorisation in Denmark (Danish Medicines Agency / EMA); it is not marketed in the Danish market.

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information. As Vibegron is not currently marketed in Denmark, a Danish/EU SmPC is not yet available.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a TxGNN model score (L5 — no disease-specific clinical trials or literature), and the underlying mechanistic analysis found no known biological pathway linking Vibegron's β3-adrenergic agonism to the polycystin/ciliopathy pathway responsible for PKD3/PLD. The drug is also not currently marketed in Denmark. Nine additional TxGNN-predicted indications for Vibegron in this Evidence Pack (mitochondrial oxidative phosphorylation disorder, renal-hepatic-pancreatic dysplasia, Joubert syndrome with renal defect, thoracic malformation) show the same pattern — high graph-similarity scores with no supporting trials or literature — and are similarly rated Hold/L5.

**To proceed, the following is needed:**
- Danish/EU SmPC or equivalent regulatory safety documentation (warnings, contraindications, drug interactions) — currently a blocking data gap
- Confirmed original indication and MOA sourced from an official regulatory or DrugBank record (current data marked as gap)
- Preclinical or mechanistic studies directly testing β3-adrenergic modulation in polycystin-pathway models
- Any future disease-specific clinical trial or case-report data connecting Vibegron to PKD/PLD
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

