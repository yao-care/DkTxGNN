---
layout: default
title: Catridecacog
parent: 僅模型預測 (L5)
nav_order: 96
evidence_level: L5
indication_count: 10
---

# Catridecacog
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

# Catridecacog: From Congenital Factor XIII Deficiency to Primary Release Disorder of Platelets

## One-Sentence Summary

Catridecacog (NovoThirteen®) is a recombinant human Factor XIII A-subunit approved by the EMA and FDA for prophylaxis of bleeding in congenital Factor XIII A-subunit deficiency, but currently not registered in Denmark.
The TxGNN model's highest-ranked prediction is efficacy for **Primary Release Disorder of Platelets** (score 99.29%), supported by mechanistic reasoning alone with **no clinical trials or publications** currently available for this indication.
Importantly, the model also independently identifies **Congenital Factor XIII Deficiency** as a high-confidence prediction (score 98.79%, rank 7), backed by **9 clinical trials** and **3 publications** — both validating the model and highlighting a significant regulatory access gap for Danish patients with this rare bleeding disorder.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Congenital Factor XIII A-subunit deficiency (EMA/FDA approved; not registered in Denmark) |
| Predicted New Indication | Primary Release Disorder of Platelets |
| TxGNN Prediction Score | 99.29% |
| Evidence Level | L5 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known pharmacological information, catridecacog is a recombinant human coagulation Factor XIII A-subunit (rFXIII-A). When administered intravenously, it reconstitutes functional Factor XIII by combining with the endogenous circulating B-subunit. Upon activation by thrombin in the presence of calcium ions, active FXIIIa catalyses the formation of covalent ε-(γ-glutamyl)lysine cross-links between fibrin γ-γ and α-α chains, producing a mechanically stable and fibrinolysis-resistant clot — the final stabilisation step of the secondary haemostasis cascade.

The biological rationale for the prediction in **primary release disorder of platelets** rests on the fact that platelets store Factor XIII within their α-granules and release it upon activation. In patients with α-granule release defects or dense granule deficiency, platelet activation fails to properly secrete ADP, ATP, serotonin, and α-granule-stored contents, including platelet-bound Factor XIII. Exogenous rFXIII could theoretically compensate for this release-dependent functional FXIII deficit by strengthening downstream fibrin clot stability. However, patients with primary platelet release disorders typically retain substantial circulating plasma FXIII (the plasma pool accounts for the dominant proportion of systemic FXIII activity), so the functional deficit is far less severe than in congenital FXIII deficiency, and the clinical benefit threshold for supplementation is uncertain.

The TxGNN prediction score of 0.9929 most likely derives from the biological association between platelet α-granules and Factor XIII embedded in the knowledge graph — a mechanistically valid connection — rather than from any direct clinical evidence. This prediction should be treated as a hypothesis-generating signal only, requiring prospective investigation before clinical application.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for catridecacog in primary release disorder of platelets.

---

> **Contextual Note — Congenital Factor XIII Deficiency (TxGNN Rank 7, Score 98.79%, Evidence Level L1)**
>
> Although congenital Factor XIII deficiency is catridecacog's globally approved indication rather than a novel repurposing target, it carries no marketing authorisation in Denmark. The trials below are directly relevant to Danish clinicians seeking access for eligible patients and serve as internal model validation demonstrating that TxGNN correctly recovers the drug's established indication.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT00713648](https://clinicaltrials.gov/study/NCT00713648) | Phase 3 | Completed | 41 | MENTOR1: Pivotal multi-centre open-label single-arm trial of monthly prophylactic rFXIII replacement in adults with congenital FXIII deficiency; primary basis for EMA/FDA approval |
| [NCT00978380](https://clinicaltrials.gov/study/NCT00978380) | Phase 3 | Completed | 63 | MENTOR2: Long-term safety extension study with up to 36 months of monthly prophylaxis; largest Phase 3 dataset for this indication |
| [NCT01862367](https://clinicaltrials.gov/study/NCT01862367) | Observational | Completed | 30 | Prospective multi-centre real-world study of NovoThirteen® in EU patients; monitored FXIII antibody formation, allergic reactions, and thromboembolic events |
| [NCT01253811](https://clinicaltrials.gov/study/NCT01253811) | Phase 3 | Completed | 6 | Paediatric safety extension (ages 1–6 years); long-term monthly prophylaxis data in young children with congenital FXIII A-subunit deficiency |
| [NCT01230021](https://clinicaltrials.gov/study/NCT01230021) | Phase 3b | Completed | 6 | MENTOR4: PK and safety profile of single IV dose rFXIII in paediatric patients (ages 1–6); basis for paediatric dosing extrapolation |
| [NCT00056589](https://clinicaltrials.gov/study/NCT00056589) | Phase 1 | Completed | 11 | First-in-patient dose-escalation study in congenital FXIII deficiency; established safety and PK profile in the target population |
| [NCT01082406](https://clinicaltrials.gov/study/NCT01082406) | Phase 1 | Completed | 51 | Bioequivalence cross-over study comparing rFXIII from two manufacturers (Novo Nordisk vs. Avecia) in healthy volunteers |
| [NCT01848002](https://clinicaltrials.gov/study/NCT01848002) | Phase 1 | Completed | 24 | Multi-dose safety and PK randomised double-blind placebo-controlled study in healthy volunteers; characterised dose accumulation and repeat-dose safety |
| [NCT01847989](https://clinicaltrials.gov/study/NCT01847989) | Phase 1 | Completed | 50 | Single-dose escalating safety and PK randomised double-blind placebo-controlled study in healthy volunteers; established dose-exposure relationship |

---

## Literature Evidence

Currently no related literature available for catridecacog in primary release disorder of platelets.

---

> **Contextual Literature — Congenital Factor XIII Deficiency**

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [36580025](https://pubmed.ncbi.nlm.nih.gov/36580025/) | 2023 | Cohort | Blood Transfusion | Italian FXIII Study: Multi-centre real-world assessment of catridecacog efficacy and safety in FXIII-deficient patients; covers PK from MENTOR2 trial to clinical practice |
| [30915205](https://pubmed.ncbi.nlm.nih.gov/30915205/) | 2019 | Case Report | Hematology Reports | Successful perioperative management using catridecacog prophylaxis (35 IU/kg every 28 days) in a patient with severe FXIII deficiency undergoing inguinal hernia repair |
| [25031548](https://pubmed.ncbi.nlm.nih.gov/25031548/) | 2014 | Review | Journal of Blood Medicine | Comprehensive review of catridecacog as a breakthrough therapy for congenital FXIII A-subunit deficiency; covers clinical presentation, diagnosis, and the pivotal clinical evidence base |

---

## Denmark Market Information

Catridecacog is not registered with the Danish Medicines Agency (Lægemiddelstyrelsen) and holds no current marketing authorisations in Denmark.

The product is marketed as **NovoThirteen®** (Novo Nordisk A/S) under a centralised EMA marketing authorisation for congenital Factor XIII A-subunit deficiency. Danish patients with confirmed congenital FXIII deficiency may be eligible for access through an individual patient import (*særlig tilladelse*) or named-patient programme via the Danish Medicines Agency.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

---

## Conclusion and Next Steps

### Decision A: Hold — Primary Release Disorder of Platelets (TxGNN Rank 1, L5)

**Rationale:**
The top-ranked TxGNN prediction for primary release disorder of platelets rests solely on the biological association between platelet α-granules and Factor XIII content. There are no clinical trials, observational studies, or case reports supporting this indication. While the mechanistic hypothesis is coherent, plasma FXIII pools remain largely intact in patients with platelet release disorders, making the clinical benefit of supplementation uncertain.

**To proceed, the following is needed:**
- Measurement of functional FXIII activity levels in patients with primary platelet release disorders to characterise the actual degree of deficiency
- Exploratory pilot study or prospective case series in patients with a documented bleeding phenotype and confirmed release disorder
- Retrieval of full MOA data from DrugBank (DrugBank ID: DB09310) to strengthen the mechanistic rationale
- Full SmPC review (TFDA/EMA) for contraindications, warnings, and dose guidance relevant to this non-approved population

---

### Decision B: Proceed with Guardrails — Congenital Factor XIII Deficiency (TxGNN Rank 7, L1)

**Rationale:**
Catridecacog has completed two pivotal Phase 3 trials (MENTOR1 and MENTOR2) and holds a centralised EMA marketing authorisation for congenital Factor XIII A-subunit deficiency — one of the rarest coagulation disorders globally (estimated incidence 1 in 2 million). The drug is not registered in Denmark, creating a direct access barrier for Danish patients with this potentially life-threatening rare bleeding disorder. The evidence base is robust given the rarity of the condition.

**To proceed, the following is needed:**
- Engagement with the Danish Medicines Agency regarding *særlig tilladelse* (special import permission) for individual patients with confirmed congenital FXIII A-subunit deficiency
- Haematology centre mapping to identify Danish patients with this diagnosis who may benefit from access
- Coordination with Novo Nordisk Denmark regarding named-patient or managed access programme availability
- Full SmPC review and local pharmacovigilance plan before clinical use

---

> ⚠️ **Disclaimer:** This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before application. All findings should be interpreted by qualified healthcare professionals in conjunction with approved product information.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

