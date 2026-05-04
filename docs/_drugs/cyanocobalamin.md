---
layout: default
title: Cyanocobalamin
parent: 僅模型預測 (L5)
nav_order: 125
evidence_level: L5
indication_count: 2
---

# Cyanocobalamin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Cyanocobalamin: From Vitamin B12 Deficiency to Biotin Metabolic Disease

## One-Sentence Summary

Cyanocobalamin (Vitamin B12) is an essential micronutrient cofactor classically used to treat vitamin B12 deficiency states, including pernicious anaemia and megaloblastic anaemia.
The TxGNN model predicts it may have a role in **Biotin Metabolic Disease** — a group of rare inherited disorders affecting biotin-dependent enzymatic pathways — with a prediction score of **99.60%**.
Current supporting evidence comprises **15 clinical trials** and **20 publications**, though none directly investigates cyanocobalamin as a primary intervention in biotin metabolic disease; evidence is largely mechanistic and indirect (Level L4).

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Vitamin B12 deficiency / megaloblastic anaemia (universally recognised use; no Danish authorisations on record) |
| Predicted New Indication | Biotin Metabolic Disease |
| TxGNN Prediction Score | 99.60% |
| Evidence Level | L4 (preclinical/mechanistic studies; no direct interventional RCTs) |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Cyanocobalamin is the synthetic form of Vitamin B12, functioning as an obligatory cofactor for two critical enzymatic reactions: (1) the conversion of methylmalonyl-CoA to succinyl-CoA, catalysed by methylmalonyl-CoA mutase (MCM); and (2) the remethylation of homocysteine to methionine, catalysed by methionine synthase. These reactions sit at the intersection of propionate catabolism, one-carbon metabolism, and mitochondrial energy production.

The mechanistic rationale linking B12 to biotin metabolic disease rests on shared metabolic nodes in the propionate pathway. Biotin (Vitamin B7) is the obligatory cofactor for propionyl-CoA carboxylase (PCC), which converts propionyl-CoA to methylmalonyl-CoA — the direct upstream substrate for the MCM reaction that requires B12. Consequently, both vitamins are indispensable for the propionate → succinyl-CoA → TCA cycle flux. In conditions such as biotinidase deficiency or holocarboxylase synthetase (HCS) deficiency, impaired PCC function leads to propionate accumulation and secondary methylmalonic acidaemia; supplemental B12 can partly buffer the downstream metabolic bottleneck. A landmark review (PMID 23622402, Tier 1) explicitly classifies cobalamin and biotin under the unified category of "vitamin-responsive metabolic disorders," further supporting the biological proximity captured by the TxGNN knowledge graph.

It is important to note, however, that cyanocobalamin cannot repair the underlying enzymatic defects in biotinidase or HCS deficiency — that remains the domain of biotin replacement therapy. The predicted role of B12 is therefore **adjuvant/synergistic**, not curative: correcting cobalamin-dependent secondary dysfunction in patients with co-existing or overlapping organic acidaemias. This mechanistic nuance should inform the design of any future clinical investigation.

---

## Clinical Trial Evidence

No clinical trials directly testing cyanocobalamin as a primary intervention for biotin metabolic disease were identified. The trials below are the most relevant retrieved, presented with their assessed relevance grade (A = highly relevant, B = moderately relevant, C = low relevance).

| Trial Number | Phase | Status | Enrolment | Key Findings / Relevance |
|-------------|-------|--------|-----------|--------------------------|
| [NCT04312152](https://clinicaltrials.gov/study/NCT04312152) | N/A | Unknown | 200 | Double-blind, placebo-controlled, crossover RCT of metabolic support therapy (Q10 ubiquinol + Vitamins B & E) in autism spectrum disorder / Phelan-McDermid syndrome. Vitamin B complex including B12 assessed in a metabolic context. Protocol review needed to confirm biotin metabolic disease subgroup. (Grade B) |
| [NCT03444155](https://clinicaltrials.gov/study/NCT03444155) | N/A | Completed | 30 | Crossover study comparing natural vs. synthetic vitamin B complexes (including B12 and biotin) in healthy adults. Provides bioavailability comparison data for both vitamins simultaneously; sample very small. (Grade B) |
| [NCT01173315](https://clinicaltrials.gov/study/NCT01173315) | Phase 2 | Completed | 75 | Phase 2 RCT of vitamins and minerals (including B12) on neuropathy and nephropathy in type 2 diabetes. Metabolic complications studied; population not biotin metabolic disease but overlapping pathways (propionate/methylmalonyl). (Grade B) |
| [NCT05687474](https://clinicaltrials.gov/study/NCT05687474) | N/A | Completed | 6,824 | Universal genomic newborn screening programme (Wallonia-Brussels) covering 126 treatable genetic diseases including biotin metabolic disorders. Diagnostic — not a therapeutic cyanocobalamin trial. (Grade C) |
| [NCT02426775](https://clinicaltrials.gov/study/NCT02426775) | Phase 3 | Completed | 33 | Phase 3 trial of carglumic acid in propionic acidaemia (PA) and methylmalonic acidaemia (MMA) — organic acidaemias closely related to biotin-cobalamin metabolic overlap. Cyanocobalamin not the intervention; contextually relevant. (Grade C) |
| [NCT01474486](https://clinicaltrials.gov/study/NCT01474486) | N/A | Completed | 40 | Multi-micronutrient intervention in congestive heart failure veterans. Very small sample; not specific to biotin metabolic disease. (Grade C) |
| [NCT03360435](https://clinicaltrials.gov/study/NCT03360435) | N/A | Completed | 99 | Pharmacokinetic study of transdermal vs. oral vitamin absorption in post-bariatric surgery patients; not a therapeutic efficacy study for biotin metabolic disease. (Grade C) |
| [NCT00572741](https://clinicaltrials.gov/study/NCT00572741) | N/A | Completed | 39 | Nutritional intervention targeting methylation and oxidative stress in autism; B12 may be included but indication is autism, not biotin metabolic disease. (Grade C) |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [23622402](https://pubmed.ncbi.nlm.nih.gov/23622402/) | 2013 | Review (Tier 1) | Handbook of Clinical Neurology | Landmark classification of vitamin-responsive metabolic disorders; explicitly groups cobalamin and biotin disorders together, describing inborn errors of cobalamin absorption, transport, and intracellular metabolism alongside biotin-responsive multiple carboxylase deficiency |
| [38203763](https://pubmed.ncbi.nlm.nih.gov/38203763/) | 2024 | Review | Int J Mol Sciences | Comprehensive review of VitB12 deficiency mechanisms; confirms B12 as cofactor for succinyl-CoA synthesis from methylmalonyl-CoA and biotin — directly contextualising the metabolic overlap |
| [1909779](https://pubmed.ncbi.nlm.nih.gov/1909779/) | 1991 | Original Research | Pediatric Research | In vivo propionate metabolism study in PA, MMA, multiple carboxylase deficiency, and transcobalamin-II deficiency; four of eight MMA patients were B12-responsive — key mechanistic evidence for B12 role in propionate pathway disorders |
| [36476407](https://pubmed.ncbi.nlm.nih.gov/36476407/) | 2023 | Original Research | J Endocrinology | B12 deficiency in rats induces glucose intolerance and ketogenesis; demonstrates systemic metabolic consequences of B12 insufficiency beyond classical haematological effects |
| [7027768](https://pubmed.ncbi.nlm.nih.gov/7027768/) | 1981 | Review | Acta Vitaminologica et Enzymologica | Reviews vitamins in inborn metabolic errors via three mechanisms: malabsorption, metabolism errors, and vitamin-dependent syndromes; discusses pharmacological vs. nutritional dosing for apoenzyme defects |
| [25388747](https://pubmed.ncbi.nlm.nih.gov/25388747/) | 2015 | Review | Endocrine Metab Immune Disord Drug Targets | Reviews B-group vitamins including biotin and B12 in type 2 diabetes; highlights biotin involvement in glucokinase regulation and B12 in metabolic pathway cofactor roles |
| [11031989](https://pubmed.ncbi.nlm.nih.gov/11031989/) | 2000 | Review | Ryoikibetsu Shokogun Shirizu | Review of vitamin dependency syndromes — clinical classification relevant to understanding B12-responsive vs. biotin-responsive disorders |
| [958746](https://pubmed.ncbi.nlm.nih.gov/958746/) | 1976 | Case Series / Review | Pediatric Clinics of North America | Megavitamin-responsive aminoacidopathies; describes B-complex vitamins as coenzymes activating apoenzymes and advocates therapeutic vitamin trials when enzymatic diagnosis is established |
| [7015958](https://pubmed.ncbi.nlm.nih.gov/7015958/) | 1980 | Review | Ann NY Acad Sciences | B-complex vitamin interactions; establishes that thiamin, riboflavin, B12, and biotin function in interdependent metabolic and catabolic reactions — foundational for understanding pathway crosstalk |
| [6152513](https://pubmed.ncbi.nlm.nih.gov/6152513/) | 1983 | Review | Advances in Clinical Chemistry | Vitamin-responsive inborn errors of metabolism; catalogues conditions including cobalamin-responsive and biotin-responsive disorders, relevant to understanding therapeutic vitamin supplementation strategy |

---

## Denmark Market Information

Cyanocobalamin currently holds **no marketing authorisations** in Denmark (Lægemiddelstyrelsen) and is not listed as a marketed product. No Danish or EMA centralised authorisations were identified in the regulatory dataset for this active substance under this DrugBank entry.

> **Note for practitioners**: Cyanocobalamin and hydroxocobalamin (alternative B12 forms) are available in Denmark under other regulatory pathways and product names. Clinicians should verify current availability through the Danish Medicines Agency product database (produktresume.dk) for specific vitamin B12 formulations.

---

## Safety Considerations

Detailed safety data (SmPC warnings, contraindications, and drug interaction profile) for cyanocobalamin were not retrievable from the regulatory and DDI databases queried for this Evidence Pack.

> Please refer to the approved Summary of Product Characteristics (SmPC) for any cyanocobalamin-containing product authorised in the EU for comprehensive safety information, including warnings for patients with Leber's hereditary optic neuropathy (where cyanocobalamin is specifically contraindicated) and potential interactions with drugs affecting gastrointestinal absorption (e.g., proton pump inhibitors, metformin).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model assigns a high prediction score (99.60%) driven by well-characterised metabolic pathway proximity between vitamin B12 and biotin in propionate catabolism; however, no clinical trials directly testing cyanocobalamin as an intervention in biotin metabolic disease exist, and the mechanistic link is adjuvant rather than disease-modifying. Evidence level L4 — based on mechanistic reviews and indirect observational data — is insufficient to support a clinical repurposing recommendation without further targeted investigation.

**To proceed, the following is needed:**

- **Mechanism clarification**: Obtain full MOA data from DrugBank (DB00115) and published cobalamin biochemistry to formally characterise the adjuvant role of B12 in biotin-deficiency states versus direct therapeutic action
- **Targeted literature review**: Systematic review specifically on B12 supplementation in biotinidase deficiency and holocarboxylase synthetase deficiency cohorts (including case reports and registry data)
- **Regulatory safety review**: Obtain and parse the full SmPC/PIL for cyanocobalamin products authorised in the EU/EEA to complete the S1 safety screening (currently blocking — Data Gap DG001)
- **Patient population definition**: Define the specific biotin metabolic disease subtype(s) most likely to benefit from adjuvant B12 (e.g., MMA–biotinidase co-deficiency vs. isolated biotinidase deficiency) before designing any proof-of-concept study
- **Denmark market access assessment**: Confirm whether cyanocobalamin is available under any existing Danish product authorisation (e.g., hydroxocobalamin products) to determine feasibility of a clinical study without requiring a new marketing authorisation

---

> **Disclaimer**: This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before therapeutic application. This analysis is generated as part of the DkTxGNN research programme (data cut-off: 5 April 2026).
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

