---
layout: default
title: Canakinumab
parent: 僅模型預測 (L5)
nav_order: 86
evidence_level: L5
indication_count: 10
---

# Canakinumab
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

# Canakinumab: From Autoinflammatory Periodic Fever Syndromes to Periodic Fever-Infantile Enterocolitis-Autoinflammatory Syndrome

## One-Sentence Summary

Canakinumab (Ilaris) is a fully human anti-IL-1β monoclonal antibody approved by FDA and EMA for cryopyrin-associated periodic syndromes (CAPS), familial Mediterranean fever (FMF), HIDS/MKD, and TRAPS — but currently not registered in Denmark.
The TxGNN model identifies **Periodic Fever-Infantile Enterocolitis-Autoinflammatory Syndrome** as the highest-evidence predicted new indication, supported by a strong mechanistic alignment with the drug's established IL-1β inhibition pathway.
This prediction is supported by **0 registered clinical trials** specific to this exact syndrome but **19 publications** across the broader IL-1β-driven periodic fever disease spectrum, yielding an overall evidence level of **L2**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Autoinflammatory periodic fever syndromes (CAPS, FMF, HIDS/MKD, TRAPS, SJIA) — globally approved via EMA/FDA, not registered in Denmark |
| Predicted New Indication | Periodic Fever-Infantile Enterocolitis-Autoinflammatory Syndrome |
| TxGNN Prediction Score | 99.57% |
| Evidence Level | L2 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Canakinumab is a fully human IgG1/κ monoclonal antibody that selectively and potently neutralises interleukin-1β (IL-1β). By binding free IL-1β with picomolar affinity, it prevents engagement with the IL-1 receptor complex, thereby blocking downstream NF-κB activation, prostaglandin release, and acute-phase protein induction. All of Canakinumab's currently approved indications share a single common pathological driver: constitutive or stimulus-triggered overactivation of the NLRP3 (or related) inflammasome, leading to excessive IL-1β cleavage and systemic autoinflammation manifesting as recurrent fever, serositis, or mucosal inflammation.

Periodic fever-infantile enterocolitis-autoinflammatory syndrome — which encompasses NLRC4 inflammasomopathy, certain PFAPA-related enterocolitis variants, and closely related periodic fever disorders — operates through the same fundamental inflammasome-IL-1β axis. The core disease mechanism is aberrant NLRP3/NLRC4 inflammasome activation → IL-1β overproduction → cyclical systemic fever and mucosal/intestinal inflammation. Canakinumab directly intercepts this cascade at the most proximal druggable point. The 2018 NEJM pivotal trial (PMID 29768139) demonstrated that Canakinumab significantly reduced flare frequency across three mechanistically related periodic fever syndromes (FMF, HIDS/MKD, TRAPS) in a single randomised study, providing direct proof-of-concept for the IL-1β inhibition strategy across the entire disease spectrum. This indication therefore represents a scientifically well-supported extension of an already-validated therapeutic approach.

> **Note on TxGNN Ranking:** The TxGNN model's top-ranked prediction is hepatic infarction (score 99.86%), followed by hepatic veno-occlusive disease, peliosis hepatis, and syndrome with combined immunodeficiency — all rated L5 (model prediction only) with no supporting clinical literature. These scores likely reflect indirect knowledge-graph connectivity via hepatic vascular and inflammatory pathology nodes rather than direct mechanistic evidence. For hepatic infarction, the single retrieved publication concerns bempedoic acid — a structurally and mechanistically unrelated drug — confirming negligible evidence relevance. This report focuses on the periodic fever-infantile enterocolitis-autoinflammatory syndrome prediction (rank 9–10), which is the sole prediction with meaningful clinical literature and an actionable recommendation.

---

## TxGNN Prediction Overview

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Recommendation |
|------|---------------------|-------------|---------------|----------------|
| 1–2 | Hepatic infarction | 99.86% | L5 | Hold |
| 3–4 | Hepatic veno-occlusive disease | 99.82% | L5 | Hold |
| 5–6 | Peliosis hepatis | 99.78% | L5 | Hold |
| 7–8 | Syndrome with combined immunodeficiency | 99.71% | L5 | **⚠ Hold — safety concern: IL-1β inhibition may worsen existing immune deficiency** |
| 9–10 | **Periodic fever-infantile enterocolitis-autoinflammatory syndrome** | **99.57%** | **L2** | **Proceed with Guardrails** |

---

## Clinical Trial Evidence

No clinical trials specifically investigating Canakinumab in **periodic fever-infantile enterocolitis-autoinflammatory syndrome** are currently registered on ClinicalTrials.gov or the WHO ICTRP. Trials for mechanistically overlapping conditions (CAPS, FMF, HIDS/MKD, TRAPS) have been conducted and serve as the primary supporting evidence base.

---

## Literature Evidence

The following publications are drawn from the 19 items retrieved for the periodic fever-infantile enterocolitis-autoinflammatory syndrome prediction, ranked by study type and clinical relevance:

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [29768139](https://pubmed.ncbi.nlm.nih.gov/29768139/) | 2018 | Clinical Trial / Pivotal Study | N Engl J Med | Phase 3 pivotal trial: Canakinumab significantly reduced flare rates vs. placebo in FMF, HIDS/MKD, and TRAPS — the closest mechanistic analogues to the predicted indication |
| [38268504](https://pubmed.ncbi.nlm.nih.gov/38268504/) | 2024 | Real-World Cohort Study | Arthritis Rheumatol | Japanese nationwide survey confirming long-term efficacy and tolerability of canakinumab in CAPS patients in a real-world setting |
| [39334417](https://pubmed.ncbi.nlm.nih.gov/39334417/) | 2024 | Retrospective Cohort Study | Pediatr Rheumatol Online J | Retrospective Chinese paediatric study: canakinumab effective and safe across all CAPS phenotypes including severe NOMID |
| [35874710](https://pubmed.ncbi.nlm.nih.gov/35874710/) | 2022 | Systematic Review | Front Immunol | Systematic review of IL-1 biologics (anakinra, canakinumab, rilonacept) confirming consistent safety/efficacy across multiple IL-1-mediated autoinflammatory disorders |
| [20065636](https://pubmed.ncbi.nlm.nih.gov/20065636/) | 2010 | Drug Review | mAbs | Comprehensive overview of canakinumab's MOA, IL-1β neutralisation mechanism, early clinical data, and initial FDA approvals for FCAS and MWS |
| [30447083](https://pubmed.ncbi.nlm.nih.gov/30447083/) | 2019 | Pharmacology/Regulatory Study | Clin Pharmacol Ther | Paediatric dosage considerations for canakinumab in periodic fever syndromes, including weight-based dosing guidance without age restriction (post-2016 FDA approval) |
| [28454496](https://pubmed.ncbi.nlm.nih.gov/28454496/) | 2017 | Review | Expert Rev Clin Immunol | Evidence for canakinumab in TRAPS — supports IL-1β as a therapeutic target in TNF-receptor-associated periodic fever, mechanistically linked to the target indication |
| [30175395](https://pubmed.ncbi.nlm.nih.gov/30175395/) | 2018 | Review | Curr Treat Options Neurol | CAPS clinical spectrum, NLRP3 mutation consequences, IL-1β excess pathophysiology, and canakinumab treatment outcomes including neurological manifestations |
| [25438464](https://pubmed.ncbi.nlm.nih.gov/25438464/) | 2014 | Review | Isr Med Assoc J | CAPS disease biology: NLRP3 overactivation → IL-1β/IL-18 excess → clinical spectrum from FCAS to NOMID; provides mechanistic framework applicable to the predicted indication |
| [27343963](https://pubmed.ncbi.nlm.nih.gov/27343963/) | 2016 | Review | Clin Dermatol | PFAPA syndrome — innate immune dysregulation and periodic fever pathogenesis; relevant as a phenotypically overlapping periodic fever disorder |

---

## Denmark Market Information

Canakinumab is **not registered** with the Danish Medicines Agency (Lægemiddelstyrelsen) and has no national marketing authorisations in Denmark. However, it holds an EMA centralised marketing authorisation (Ilaris, EU/1/09/564) covering the following indications, which would provide a regulatory pathway for access in Denmark:

| Authorisation | Product Name | Dosage Form | Approved Indication |
|--------------|-------------|-------------|---------------------|
| EMA EU/1/09/564 | Ilaris (Novartis) | Solution for injection (150 mg/mL) | CAPS (FCAS, MWS, NOMID/CINCA), FMF, HIDS/MKD, TRAPS, SJIA, Adult-onset Still's disease (AOSD) |

Access in Denmark would require either a national reimbursement application based on the existing EMA authorisation, or use via named-patient/compassionate use procedures through Novartis.

---

## Safety Considerations

No drug interaction data for Canakinumab was identified in the evidence pack, and Danish-specific SmPC safety data is unavailable due to the absence of a national marketing authorisation.

Please refer to the approved **EMA Summary of Product Characteristics (SmPC) for Ilaris** for complete safety information. Based on the drug's known pharmacology as an IL-1β inhibitor / immunosuppressant biologic, the following areas are of particular relevance:

- **Infection risk**: Increased susceptibility to serious bacterial, viral, and fungal infections, including tuberculosis and opportunistic infections. TB screening is mandatory before initiation.
- **Immunodeficiency context**: Use in patients with combined immunodeficiency (TxGNN rank 7–8 prediction) carries an explicit safety warning — IL-1β inhibition may further suppress innate immune defences. This indication should **not** be pursued without case-by-case expert evaluation.
- **Neutropenia**: Haematological monitoring (full blood count) recommended during treatment.
- **Vaccination**: Live vaccines should be avoided during treatment; vaccination status should be updated prior to initiation.
- **Paediatric dosing**: Weight-based dosing applies for paediatric patients; consult current SmPC for age- and weight-appropriate regimens.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Periodic fever-infantile enterocolitis-autoinflammatory syndrome sits directly within the IL-1β-driven autoinflammatory disease spectrum for which Canakinumab is already globally approved. A pivotal Phase 3 trial (NEJM 2018) and multiple real-world cohort studies provide solid L2-level evidence supporting IL-1β inhibition in mechanistically identical conditions. The absence of trials in this specific syndrome most likely reflects its rarity and recent characterisation rather than a lack of therapeutic rationale.

**To proceed, the following is needed:**

- **SmPC review**: Obtain and review the full current EMA SmPC for Ilaris to complete safety profiling before any clinical use
- **Genetic confirmation**: Confirm the precise syndrome subtype via genetic testing (NLRC4, NLRP3, MEFV, MVK, TNFRSF1A, or other relevant variants) — mechanistic fit and dosing strategy depend on the underlying genetic diagnosis
- **Regulatory pathway**: Explore named-patient access or compassionate use via the EMA-authorised Ilaris product; no Danish marketing authorisation currently exists
- **Specialist referral**: Engage a paediatric rheumatology centre with autoinflammatory disease expertise (e.g., via the European Reference Network for Rare Immunodeficiency, Autoinflammatory and Autoimmune Diseases — ERN RITA)
- **Registry enrolment**: If treatment is initiated, prospectively document outcomes via Eurofever/PRINTO or Eurotraps registries to contribute to the evidence base for this rare indication
- **Pharmacovigilance plan**: Establish a monitoring plan per the EMA SmPC, including infection surveillance, CBC monitoring, and TB screening

> **⚠ Disclaimer:** This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before therapeutic application. All website content should include a YMYL disclaimer.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

