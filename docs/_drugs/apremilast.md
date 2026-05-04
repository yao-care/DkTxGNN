---
layout: default
title: Apremilast
parent: 僅模型預測 (L5)
nav_order: 42
evidence_level: L5
indication_count: 10
---

# Apremilast
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

# Apremilast: From Psoriatic Arthritis to Rheumatoid Arthritis

## One-Sentence Summary

Apremilast (Otezla®) is an oral phosphodiesterase 4 (PDE4) inhibitor approved internationally for psoriatic arthritis and plaque psoriasis, but currently not marketed in Denmark.
The TxGNN model assigns rheumatoid arthritis a prediction score of **98.09%**, with **6 clinical trials** and **19 publications** identified — making it the highest-ranked indication with meaningful clinical evidence in this pack.
However, the largest Phase 2 randomised trial was terminated early and the commercial RA development programme appears to have been abandoned, warranting a **Hold** recommendation pending further review.

> **Note on TxGNN rankings:** Migraine disorder (98.66%) and migraine with brainstem aura (98.49%) rank higher in the TxGNN model, but no clinical trials or literature were identified for those indications (Evidence Level L5). This report therefore focuses on **rheumatoid arthritis** as the top-ranked prediction with actionable clinical evidence. A brief overview of all predictions is provided in the Conclusion.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Psoriatic arthritis; plaque psoriasis (approved in USA and EU via centralised EMA procedure; not registered in Denmark) |
| Predicted New Indication | Rheumatoid Arthritis |
| TxGNN Prediction Score | 98.09% |
| Evidence Level | L2 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Apremilast is an orally available small-molecule inhibitor of phosphodiesterase 4 (PDE4), the enzyme responsible for degrading cyclic AMP (cAMP) inside immune and inflammatory cells. By blocking PDE4, apremilast raises intracellular cAMP, which suppresses production of key pro-inflammatory mediators including TNF-α, IL-17, IL-23, interferon-γ, and nitric oxide. Although formal MOA data was not retrieved from DrugBank for this evidence pack, this mechanism is consistently described across the clinical literature (PMID 24797159, PMID 25779750) and is the established basis for apremilast's approved indications.

Rheumatoid arthritis and psoriatic arthritis share substantial immunopathological overlap — both are autoimmune, synovitis-driven arthropathies in which TNF-α, IL-17, and Th1/Th17 axis dysregulation play central roles. Apremilast has demonstrated the ability to inhibit spontaneous TNF-α production directly from human RA synovial cells in vitro and to reduce bone erosion in collagen-induced arthritis animal models through suppression of Th1/Th17 cells and enhancement of regulatory T-cell differentiation (PMID 20525198; PMID 30072998). A systematic repurposing analysis has confirmed that pathogenic inflammatory pathways are broadly shared across autoimmune diseases, supporting the plausibility of cross-indication development (PMID 33403021). The TxGNN model's prediction is therefore mechanistically well-grounded.

In practice, however, clinical translation has been limited. The largest randomised Phase 2 trial in RA (NCT01285310, n=237, MTX-inadequate responders) was terminated before completion, and the published results of a separate Phase 2 RCT (PMID 25779750) indicate that apremilast did not demonstrate sufficient efficacy relative to placebo in this population. The commercial RA development programme has been abandoned, likely reflecting insufficient benefit compared to established biologics and JAK inhibitors. Any future repurposing effort in RA would need to identify a specific patient subgroup or clinical context where PDE4 inhibition could provide a meaningful advantage.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|-----------|--------------|
| [NCT01250548](https://clinicaltrials.gov/study/NCT01250548) | Phase 2 | Completed | 34 | Placebo-controlled trial directly in active RA; assessed safety, time to onset of response, and durability of effect with apremilast — the most directly relevant completed trial (Grade A) |
| [NCT01285310](https://clinicaltrials.gov/study/NCT01285310) | Phase 2 | Terminated | 237 | Largest RA RCT: multicentre, randomised, double-blind, placebo-controlled comparison of two apremilast doses vs. placebo in MTX-inadequate responders; terminated early — reason not specified in registry (Grade B) |
| [NCT01204138](https://clinicaltrials.gov/study/NCT01204138) | Phase 2 | Withdrawn | 0 | Exploratory cross-over study of apremilast added to TNF inhibition plus methotrexate in active RA; withdrawn before any enrolment — no data generated (Grade C) |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [25779750](https://pubmed.ncbi.nlm.nih.gov/25779750/) | 2015 | Phase 2 RCT | Arthritis & Rheumatology | Multicentre, randomised, double-blind, placebo-controlled study of apremilast in active RA with inadequate response to methotrexate; primary efficacy and safety results |
| [38499181](https://pubmed.ncbi.nlm.nih.gov/38499181/) | 2024 | Clinical Guidelines | J American Academy of Dermatology | National Psoriasis Foundation guidelines on perioperative management of systemic immunomodulatory agents — including apremilast — in psoriasis and psoriatic arthritis |
| [33403021](https://pubmed.ncbi.nlm.nih.gov/33403021/) | 2020 | Systematic Review | Therapeutic Advances in Musculoskeletal Disease | Systematic repurposing analysis demonstrating that inflammatory pathways are shared across autoimmune diseases; supports rationale for cross-indication development of targeted therapies |
| [20525198](https://pubmed.ncbi.nlm.nih.gov/20525198/) | 2010 | In vitro / Mechanistic | Arthritis Research & Therapy | Apremilast inhibits spontaneous TNF-α production from human RA synovial cells and ameliorates disease in two murine arthritis models; establishes direct mechanistic rationale in RA tissue |
| [30072998](https://pubmed.ncbi.nlm.nih.gov/30072998/) | 2018 | Preclinical / Animal Study | Frontiers in Immunology | Apremilast suppresses Th1 and Th17 cells and enhances CD4+Foxp3+ regulatory T-cell differentiation in collagen-induced arthritis; reduces bone erosion on micro-CT |
| [26097790](https://pubmed.ncbi.nlm.nih.gov/26097790/) | 2014 | PK Study | Clinical Pharmacology in Drug Development | Open-label pharmacokinetic interaction study of apremilast co-administered with oral methotrexate in RA/PsA patients; no clinically significant PK interaction identified |
| [24797159](https://pubmed.ncbi.nlm.nih.gov/24797159/) | 2014 | Drug Approval Review | Drugs | First global approval review for apremilast (Otezla®); summarises development programme across psoriatic arthritis, psoriasis, and additional indications including RA |
| [40283434](https://pubmed.ncbi.nlm.nih.gov/40283434/) | 2025 | Review | Journal of Clinical Medicine | Contemporary review of rituximab, apremilast, and upadacitinib as targeted synthetic DMARDs in inflammatory arthritis, including RA; evaluates disease-modifying roles and current clinical use |
| [30917076](https://pubmed.ncbi.nlm.nih.gov/30917076/) | 2019 | Real-world Study | J Managed Care & Specialty Pharmacy | Real-world adherence, persistence, and cost data for high-cost anti-inflammatory drugs in RA; contextualises positioning of newer agents relative to established treatments |
| [32453211](https://pubmed.ncbi.nlm.nih.gov/32453211/) | 2021 | Case Report | J Clinical Rheumatology | Successful use of apremilast for rituximab-associated palmoplantar pustulosis in a seropositive RA patient; illustrates off-label use at the intersection of RA management and skin disease |

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information. Formal safety data (warnings, contraindications, and drug interactions) were not available for retrieval in this evidence pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic case for apremilast in rheumatoid arthritis is scientifically coherent — PDE4 inhibition directly targets TNF-α–driven and Th17-mediated inflammation, which are central to RA pathophysiology — and is backed by credible preclinical data. However, the clinical programme has failed to demonstrate sufficient efficacy: the largest Phase 2 RCT (n=237) was terminated early, and the published Phase 2 results indicate the drug did not meet its primary endpoint against methotrexate-inadequate responders, leading to commercial abandonment of RA development. In Denmark, no marketing authorisation exists for any indication, which adds a regulatory barrier.

**To proceed, the following is needed:**
- Full results (including primary endpoint outcomes) from NCT01250548 (Phase 2, completed, n=34) — these are not yet publicly reported in full
- Clarification of the reason for early termination of NCT01285310 (efficacy failure vs. commercial/safety decision) — critical for assessing whether the hypothesis was truly refuted
- Identification of a specific RA patient subgroup where PDE4 inhibition may offer an advantage not captured in prior trials (e.g., seronegative RA, patients with concomitant psoriasis, or biologic-naïve mild-moderate disease)
- Assessment of whether modern combination strategies (e.g., apremilast + JAK inhibitor) could overcome the efficacy ceiling seen in monotherapy trials
- Denmark-specific regulatory pathway assessment (a centralised EMA procedure would likely be required given no existing national authorisation)
- Full SmPC safety data to enable risk-benefit evaluation for Danish patient populations

---

**Overview of all TxGNN Predictions in This Pack**

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Recommendation |
|------|---------------------|-------------|----------------|----------------|
| 1–2 | Migraine disorder | 98.66% | L5 | Hold |
| 3–4 | Migraine with brainstem aura | 98.49% | L5 | Hold |
| 5–6 | **Rheumatoid arthritis** | **98.09%** | **L2** | **Hold (featured above)** |
| 7–8 | Pulmonary hypertension | 98.09% | L5 | Hold |
| 9–10 | Migraine with or without aura, susceptibility to | 97.81% | L5 | Hold |

The migraine-related predictions (ranks 1–4, 9–10) rest on a theoretical pathway — PDE4 inhibition → ↑cAMP → reduced neuroinflammatory mediators affecting the trigeminovascular system — but currently lack any clinical trials or direct literature support. The pulmonary hypertension prediction has a mechanistic analogy to approved PDE5 inhibitors (e.g., sildenafil), but cAMP-versus-cGMP selectivity differences and the absence of preclinical pulmonary data make this highly speculative. All five indications outside RA are rated L5 (model prediction only) and warrant no further action without preliminary experimental validation.

---

*This report is for research purposes only and does not constitute medical advice. All repurposing candidates require clinical validation before application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

