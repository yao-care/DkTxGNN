---
layout: default
title: Risankizumab
parent: 僅模型預測 (L5)
nav_order: 381
evidence_level: L5
indication_count: 10
---

# Risankizumab
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

# Risankizumab: From Psoriasis to Dermatitis

## One-Sentence Summary

Risankizumab is a humanised IL-23 (p19 subunit) inhibitor monoclonal antibody, originally developed and approved for psoriasis and psoriatic arthritis. The TxGNN model predicts it may also be effective for **Dermatitis** (most of the supporting evidence points specifically to atopic dermatitis), with **7 clinical trials** and **17 publications** currently associated with this direction — though only one of those trials was a controlled study conducted directly for this indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on file in the Danish registry dataset; per literature, first approved (Japan, 2019) for psoriasis vulgaris, psoriatic arthritis, generalized pustular psoriasis and erythrodermic psoriasis, later also in the US/Canada/EU |
| Predicted New Indication | Dermatitis (evidence base is predominantly atopic dermatitis) |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L2 |
| Denmark Market Status | Not Marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed DrugBank-sourced mechanism-of-action data is currently unavailable for this candidate. Based on the literature evidence collected (PMID 31098898), risankizumab is a humanised IgG monoclonal antibody that selectively targets the p19 subunit of interleukin-23 (IL-23), blocking IL-23-driven Th17 inflammatory signalling. Its efficacy in psoriasis — a classic IL-23/Th17-mediated inflammatory skin disease — is well established and is the basis of its existing approvals.

Atopic dermatitis, the specific form of dermatitis for which most of the collected evidence exists, is pathophysiologically more heterogeneous than psoriasis. As summarized in the retrieved literature (PMID 36588137), atopic dermatitis involves Th2 and Th22 pathways alongside a "potentially" contributory Th17 component, which is cited as the rationale for testing IL-23/IL-22 blockade in this disease. This provides a plausible but less direct mechanistic bridge than a straightforward psoriasis-to-psoriasis extension would offer.

Notably, the evidence pack contains only one completed controlled trial specifically in atopic dermatitis (a Phase 2 study), and no Phase 3 trial for this indication appears in the collected data — most of the remaining trials concern psoriasis subtypes (genital/scalp psoriasis, plaque psoriasis vs. apremilast) rather than dermatitis itself. This suggests the mechanistic hypothesis was tested but does not yet show confirmed late-stage clinical progression for dermatitis specifically.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03706040](https://clinicaltrials.gov/study/NCT03706040) | Phase 2 | Completed | 172 | Safety and efficacy of risankizumab in moderate-to-severe atopic dermatitis (adults and adolescents) |
| [NCT07041112](https://clinicaltrials.gov/study/NCT07041112) | N/A | Completed | 1000 | Retrospective observational study of genetic/cardiometabolic factors on 10-year biologic drug survival in cutaneous psoriasis |
| [NCT04818385](https://clinicaltrials.gov/study/NCT04818385) | N/A | Completed | 240 | Prospective observational cohort in Taiwan; PASI90 response durability of risankizumab vs. other biologics in moderate-to-severe plaque psoriasis |
| [NCT07352566](https://clinicaltrials.gov/study/NCT07352566) | Phase 4 | Not yet recruiting | 10 | Microdevice testing multiple FDA-approved atopic dermatitis/psoriasis drugs directly on skin |
| [NCT04908475](https://clinicaltrials.gov/study/NCT04908475) | Phase 4 | Completed | 352 | Risankizumab vs. apremilast in adults with moderate plaque psoriasis |
| [NCT07021495](https://clinicaltrials.gov/study/NCT07021495) | N/A | Recruiting | 840 | Observational biomarker profiling across six immune-mediated inflammatory skin diseases, including atopic dermatitis |
| [NCT05969223](https://clinicaltrials.gov/study/NCT05969223) | Phase 4 | Completed | 214 | Risankizumab in moderate-to-severe genital psoriasis or moderate-to-severe scalp psoriasis |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36588137](https://pubmed.ncbi.nlm.nih.gov/36588137/) | 2023 | RCT | Dermatology and Therapy | Phase 2 randomized, double-blind, placebo-controlled study of risankizumab in moderate-to-severe atopic dermatitis; rationale based on Th2/Th22/Th17 pathway involvement |
| [31098898](https://pubmed.ncbi.nlm.nih.gov/31098898/) | 2019 | Review | Drugs | "First Global Approval" profile; confirms IL-23 p19 targeting mechanism and initial approvals for psoriasis-spectrum indications |
| [39201826](https://pubmed.ncbi.nlm.nih.gov/39201826/) | 2024 | Review | Children (Basel) | Narrative review of biologics/small molecules for pediatric alopecia areata, psoriasis, atopic dermatitis and hidradenitis suppurativa |
| [33078990](https://pubmed.ncbi.nlm.nih.gov/33078990/) | 2020 | Review | Expert Opinion on Biological Therapy | Review of current and emerging biologics for pediatric atopic dermatitis |
| [40856907](https://pubmed.ncbi.nlm.nih.gov/40856907/) | 2025 | Systematic Review | American Journal of Clinical Dermatology | Systematic review of systemic therapies, including risankizumab, for erythrodermic psoriasis |
| [40794374](https://pubmed.ncbi.nlm.nih.gov/40794374/) | 2025 | Systematic Review | Inflammopharmacology | Systematic review of IL inhibitors (including IL-23 agents) in lichen planus, therapeutic and paradoxical effects |
| [38607726](https://pubmed.ncbi.nlm.nih.gov/38607726/) | 2024 | Review | Military Medicine | Review of systemic immunomodulators for psoriasis and eczema in military populations |
| [40071317](https://pubmed.ncbi.nlm.nih.gov/40071317/) | 2025 | Retrospective Study | Experimental Dermatology | Retrospective longitudinal study of risankizumab treatment response in patients with prior erythrodermic psoriasis |
| [39668419](https://pubmed.ncbi.nlm.nih.gov/39668419/) | 2025 | Case Series | International Journal of Dermatology | Effectiveness and safety of combined dupilumab and risankizumab in concomitant atopic dermatitis and psoriasis |
| [37381703](https://pubmed.ncbi.nlm.nih.gov/37381703/) | 2023 | Case Report | The Journal of Dermatological Treatment | Rapid successful treatment of acrodermatitis continua of Hallopeau with risankizumab in an elderly patient |

---

## Denmark Market Information

Risankizumab currently has **no marketing authorisation on file in the Danish dataset** (market status: Not Marketed; 0 authorisations recorded). Note: risankizumab (Skyrizi®) does hold centralised EMA marketing authorisation for psoriasis, psoriatic arthritis, Crohn's disease and ulcerative colitis in the EU — this evidence pack simply has no corresponding record captured, so the current authorisation and SmPC status should be verified directly with Lægemiddelstyrelsen/EMA before use.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information. No drug-drug interaction, contraindication, or warning data were retrievable for this evaluation.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The safety data gap (SmPC warnings/contraindications) is flagged as **Blocking**, meaning this candidate cannot yet complete even a preliminary safety screen.
- Evidence for the specific predicted indication (dermatitis/atopic dermatitis) is limited to a single completed Phase 2 RCT, with no Phase 3 trial identified in this evidence pack — most other trials concern psoriasis, a related but distinct indication.
- No confirmed Danish marketing authorisation is on record for this product.

**To proceed, the following is needed:**
- SmPC warnings, contraindications, and drug interaction data (from TFDA/EMA/Lægemiddelstyrelsen source documents)
- Confirmation of risankizumab's current Danish/EU regulatory and licensing status
- Verification of whether atopic dermatitis clinical development progressed beyond the Phase 2 stage (NCT03706040), or was discontinued
- Detailed mechanism-of-action documentation from DrugBank to strengthen the mechanistic rationale section
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

