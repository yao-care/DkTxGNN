---
layout: default
title: Atenolol
parent: 僅模型預測 (L5)
nav_order: 47
evidence_level: L5
indication_count: 10
---

# Atenolol
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

# Atenolol: From Hypertension to Posterolateral Myocardial Infarction

## One-Sentence Summary

Atenolol is a selective β1-adrenergic receptor blocker widely used for hypertension and angina pectoris.
The TxGNN model predicts it may be effective for **Posterolateral Myocardial Infarction**, with **0 registered clinical trials** and **no published literature** directly addressing this specific MI subtype.
Class-level evidence from the landmark ISIS-1 trial supports beta-blockade broadly in myocardial infarction, but subtype-specific evidence is currently absent.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No approved indication listed in Danish regulatory database |
| Predicted New Indication | Posterolateral Myocardial Infarction |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L4 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on established pharmacology, Atenolol is a cardioselective β1-adrenergic receptor blocker that reduces heart rate, myocardial contractility, and oxygen demand by competitively inhibiting sympathetic stimulation at cardiac β1 receptors. This class of agent has demonstrated clear mortality benefit in acute MI — most notably in the ISIS-1 trial, which enrolled over 16,000 patients — establishing a strong mechanistic foundation for beta-blockade across ischaemic cardiac presentations.

Posterolateral MI typically results from occlusion of the right coronary artery or the circumflex branch of the left coronary artery, compromising the lateral and posterior walls of the left ventricle. Atenolol's ability to reduce sympathetic tone, limit infarct expansion, and suppress post-infarct ventricular arrhythmias makes it a mechanistically plausible candidate for this anatomical subtype. The high TxGNN prediction score (99.87%) likely reflects this strong mechanistic alignment with established beta-blocker benefits in ischaemic heart disease as a whole.

A critical safety caveat must be acknowledged: posterolateral MI carries a higher incidence of atrioventricular (AV) nodal conduction disturbance due to right coronary or circumflex involvement. Beta-blockers, including atenolol, can exacerbate AV block in this anatomical context. Careful clinical timing — particularly avoidance in the acute phase when bradycardia or high-degree AV block is present — is therefore essential before any clinical application.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for posterolateral myocardial infarction.

---

## Literature Evidence

Currently no related literature available for posterolateral myocardial infarction.

> **Supporting context from closely related indication:** The TxGNN rank 2 prediction — **posteroinferior myocardial infarction** (score 99.87%, evidence level L3, recommendation: Proceed with Guardrails) — identified one relevant controlled study:

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [3901170](https://pubmed.ncbi.nlm.nih.gov/3901170/) | 1985 | Single-blind Crossover RCT | La Revue de medecine interne | Compared anti-ischaemic activity of atenolol (200 mg) vs diltiazem (240 mg) in 23 patients 4 weeks after limited postero-inferior or anterior MI with residual ischaemia on stress testing; exercise capacity assessed by computerised bicycle ergometer (Case-Marquette system) under placebo and randomised treatment conditions |

---

## Denmark Market Information

Atenolol currently holds no marketing authorisations with the Danish Medicines Agency (Laegemiddelstyrelsen) and is not marketed in Denmark. No authorisation-specific product or indication data is available in the current evidence pack. Clinicians should verify current EMA centralised authorisation status and any applicable national parallel import licences independently.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

> **Mechanistic safety flag from additional predicted indications:** Evidence packs for TxGNN ranks 9 and 10 — pulmonary hypertension owing to lung disease/hypoxia (L5, Hold) and pulmonary hypertension with unclear multifactorial mechanism (L5, Hold) — carry explicit safety warnings. Beta-blockers are generally contraindicated or used with extreme caution in pulmonary hypertension: they may provoke bronchoconstriction, reduce right ventricular compensatory capacity, and worsen hypoxia-driven pulmonary vascular disease. These predicted indications should not be pursued without specialist pulmonary hypertension evaluation.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
While the mechanistic basis for beta-blockade in myocardial infarction is well-established at a drug-class level, no clinical trial or literature evidence specifically addresses atenolol in posterolateral MI. An evidence level of L4 (mechanistic/preclinical support only) is insufficient to justify clinical repurposing without targeted investigation. Furthermore, critical safety information — including SmPC warnings and contraindications — is currently unavailable, representing a blocking data gap that prevents formal safety screening.

**To proceed, the following is needed:**
- Retrieve the approved SmPC or EMA product information to complete S1 safety assessment (DG001 — Blocking data gap)
- Retrieve mechanism of action data from DrugBank API to support mechanistic rationale scoring (DG002 — High severity data gap)
- Conduct a targeted systematic literature review for atenolol or class-level beta-blocker evidence specifically within posterolateral MI subpopulations
- Review ISIS-1 trial subgroup analyses to determine whether posterolateral MI patients were represented and whether they derived similar mortality benefit
- Prospectively assess AV conduction block risk in the intended patient population before initiating any clinical investigation
- Confirm whether atenolol holds or has previously held marketing authorisation in Denmark or via EMA centralised procedure, as the current absence of authorisations may reflect a data collection gap rather than true non-availability
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

