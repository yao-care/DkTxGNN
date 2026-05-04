---
layout: default
title: Denosumab
parent: 僅模型預測 (L5)
nav_order: 136
evidence_level: L5
indication_count: 4
---

# Denosumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Denosumab: From Osteoporosis to Severe Nonproliferative Diabetic Retinopathy

## One-Sentence Summary

Denosumab is a fully human monoclonal antibody targeting RANKL (Receptor Activator of Nuclear Factor Kappa-B Ligand), approved internationally for osteoporosis and cancer-related bone disease.
The TxGNN model predicts it may be effective for **Severe Nonproliferative Diabetic Retinopathy**, and more broadly for **Diabetic Retinopathy**, with a prediction score of **99.63%**.
At present, there are no clinical trials directly investigating this new indication; however, **1 indirectly relevant completed Phase 3 trial** and **2 publications** provide preliminary biological context for the broader diabetic retinopathy hypothesis.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Osteoporosis; bone loss associated with hormone-deprivation therapy (internationally approved) |
| Predicted New Indication | Severe Nonproliferative Diabetic Retinopathy |
| TxGNN Prediction Score | 99.63% |
| Evidence Level | L5 (severe NPDR, no direct studies) / L4 (broader diabetic retinopathy, indirect studies) |
| Denmark Market Status | Not marketed (no licences registered in the current Danish dataset) |
| Number of Marketing Authorisations | 0 (dataset) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known information, denosumab is a fully human IgG2 monoclonal antibody that binds and neutralises RANKL — a key cytokine driving osteoclast formation, function, and survival. Its established efficacy in osteoporosis and cancer-related bone disease is well-documented globally. Critically, the RANKL/RANK/OPG axis is not confined to bone: functional expression has been described in retinal pigment epithelium (RPE) cells and retinal vascular pericytes, which forms the biological starting point for this repurposing hypothesis.

The proposed mechanistic bridge to diabetic retinopathy operates on multiple levels. RANKL blockade may suppress NF-κB signalling in retinal vascular endothelial cells, reducing the expression of adhesion molecules (ICAM-1, VCAM-1) and pro-inflammatory mediators (TNF-α, IL-6) — thereby limiting leucocyte adhesion and vascular leakage, which are hallmarks of early diabetic retinopathy. In addition, real-world cohort data (PMID 38899553) suggest that denosumab is associated with a lower incidence of type 2 diabetes and improved microvascular outcomes compared with bisphosphonates, hinting at a systemic metabolic benefit through improved insulin sensitivity. Reducing vascular calcification — another downstream effect of RANKL inhibition — may further improve retinal microcirculatory perfusion.

It must be emphasised clearly that all of the above mechanistic links remain theoretical or indirect. No cell-based study, animal model, or dedicated clinical trial has directly tested denosumab in diabetic retinopathy. The TxGNN prediction is a knowledge-graph neural-network inference and should be treated strictly as a hypothesis-generating signal.

---

## Clinical Trial Evidence

No clinical trials directly investigating denosumab for severe nonproliferative diabetic retinopathy were identified. The following trial was retrieved for the broader indication of **Diabetic Retinopathy** and is considered indirectly relevant.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT00925600](https://clinicaltrials.gov/study/NCT00925600) | Phase 3 | Completed | 769 | Randomised, double-blind, placebo-controlled study evaluating new or worsening lens opacifications (cataracts) in men with non-metastatic prostate cancer receiving denosumab for androgen-deprivation therapy-related bone loss. Primary endpoint was ocular safety — not diabetic retinopathy efficacy. Value for this indication: (a) confirms acceptable ocular safety profile of denosumab; (b) any diabetic subgroup within the dataset may permit exploratory analysis of retinopathy outcomes. Direct relevance is low. |

---

## Literature Evidence

No publications directly investigating denosumab for severe nonproliferative diabetic retinopathy were identified. The following were retrieved for the broader indication of **Diabetic Retinopathy**.

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [38899553](https://pubmed.ncbi.nlm.nih.gov/38899553/) | 2024 | Observational Cohort / Meta-analysis | Diabetes, Obesity & Metabolism | Real-world cohort analysis with meta-analysis showing denosumab (vs. bisphosphonates) reduced incidence of type 2 diabetes, risk of foot ulceration, and all-cause mortality. Microvascular outcomes — including retinopathy, neuropathy, and nephropathy — were explicitly assessed, providing indirect support for a protective effect of RANKL inhibition on diabetic microvascular complications. |
| [36960265](https://pubmed.ncbi.nlm.nih.gov/36960265/) | 2023 | Cross-sectional / Review | Cureus | Evaluated the FRAX fracture-risk tool in patients with type 2 diabetes, documenting rates of anti-osteoporotic therapy (including denosumab) in high-fracture-risk diabetic patients. Provides epidemiological context linking T2DM, bone fragility, and anti-resorptive treatment — relevant background for understanding the target patient population. |

---

## Denmark Market Information

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|-------------------------------|--------------|-------------|---------------------|
| — | — | — | No marketing authorisations registered in the current Danish dataset. |

> **Important note for Danish healthcare professionals:** Denosumab holds centralised European Medicines Agency (EMA) authorisations under the brand names **Prolia®** (osteoporosis) and **Xgeva®** (bone metastases / giant cell tumour). The absence of records in this dataset likely reflects a data gap rather than true non-availability in Denmark. Current authorisation status should be verified directly via the **Lægemiddelstyrelsen** product database or the [EMA medicines portal](https://www.ema.europa.eu/en/medicines).

---

## Safety Considerations

Detailed SmPC warnings, contraindications, and drug interaction data are not available in this evidence pack.

Please refer to the approved Summary of Product Characteristics (SmPC) for Prolia® and Xgeva® — available via Lægemiddelstyrelsen or the EMA — for complete safety information. Key areas to review include: hypocalcaemia risk, osteonecrosis of the jaw, atypical femoral fractures, and immunogenicity.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although the TxGNN model assigns a high prediction score (99.63%) and a biologically plausible — if entirely theoretical — mechanistic rationale exists, there are no dedicated preclinical or clinical studies directly supporting denosumab use in severe nonproliferative diabetic retinopathy. Available indirect evidence is insufficient to justify progressing to a clinical programme at this stage.

**To proceed, the following is needed:**

- **Preclinical validation:** In vitro studies in retinal vascular endothelial cells and pericytes; streptozotocin-induced diabetic retinopathy animal models to test RANKL blockade effects on retinal vasculature
- **Retrospective data mining:** Extract diabetic retinopathy endpoints from existing large denosumab osteoporosis trials (e.g., the FREEDOM study and its extension) to obtain hypothesis-confirming signals
- **MOA confirmation:** Formal RANKL/RANK/OPG expression profiling in diabetic human retinal tissue
- **Pharmacokinetic assessment:** Evaluate blood-retinal barrier penetration following subcutaneous denosumab administration
- **Full safety review:** Obtain complete SmPC from Lægemiddelstyrelsen / EMA and assess risk-benefit for a diabetic patient population, particularly hypocalcaemia and immunosuppression risks
- **If preclinical data are positive:** Design a Phase 1/2 exploratory trial in patients with moderate-to-severe nonproliferative diabetic retinopathy

---

*This report is generated for research purposes only and does not constitute medical advice. All repurposing candidates require clinical validation before any therapeutic application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

