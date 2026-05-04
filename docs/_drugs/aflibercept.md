---
layout: default
title: Aflibercept
parent: 僅模型預測 (L5)
nav_order: 18
evidence_level: L5
indication_count: 10
---

# Aflibercept
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

# Aflibercept: From Neovascular Retinal Disease to Esotropia

## One-Sentence Summary

Aflibercept is a recombinant VEGF-trap fusion protein with globally established indications in neovascular (wet) age-related macular degeneration (AMD), diabetic macular edema, retinal vein occlusion, and metastatic colorectal cancer — though it currently holds no marketing authorisation in Denmark.
The TxGNN model predicts it may be effective for **Esotropia** with a confidence score of **99.38%**,
however **no clinical trials** and **no publications** currently support this specific repurposing direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Neovascular (wet) AMD, diabetic macular edema, retinal vein occlusion (globally approved; not registered in Denmark) |
| Predicted New Indication | Esotropia |
| TxGNN Prediction Score | 99.38% |
| Evidence Level | L5 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this Evidence Pack. Based on established pharmacological knowledge, aflibercept is a recombinant fusion protein — a "VEGF trap" — constructed by combining the extracellular ligand-binding domains of VEGF receptors 1 and 2 fused to the Fc region of human IgG1. It binds VEGF-A, VEGF-B, and placental growth factor (PlGF) with high affinity, thereby blocking pathological angiogenesis and vascular hyperpermeability. This mechanism underpins its EMA-approved use in neovascular AMD, diabetic macular edema, and retinal vein occlusion (as Eylea), as well as its use in metastatic colorectal cancer in combination with FOLFIRI (as Zaltrap).

Esotropia is an inward ocular deviation (a form of strabismus) typically classified as accommodative, non-accommodative, or infantile. While the predominant forms are neuromotor or refractive in origin rather than vascular, some secondary forms of esotropia — such as those arising after retinal vascular events, retinal detachment surgery, or in the context of high myopia with posterior staphyloma — may involve VEGF-related tissue remodelling. This represents a speculative but not entirely implausible mechanistic bridge.

However, the biological rationale linking anti-VEGF therapy to primary esotropia treatment remains very weak. VEGF blockade is not a recognised therapeutic strategy for strabismus management, and the TxGNN model's high confidence score appears to reflect a learned graph-level association rather than a direct mechanistic or clinical relationship. Without any supporting literature or trial data, this prediction cannot currently be considered clinically actionable.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Denmark Market Information

Aflibercept currently holds no marketing authorisations registered with the Danish Medicines Agency (Lægemiddelstyrelsen). This drug is not marketed in Denmark at the time of this report (data cutoff: 2026-04-04).

> **Note for context:** Aflibercept is authorised in the EU via centralised EMA procedures under the brand names **Eylea** (intravitreal injection; for neovascular AMD, diabetic macular edema, macular edema following retinal vein occlusion, and diabetic retinopathy) and **Zaltrap** (intravenous infusion; for metastatic colorectal cancer in combination with FOLFIRI). These centralised authorisations apply across EU/EEA member states including Denmark, but are not reflected in the national registry data available for this Evidence Pack. Danish prescribers should verify current status via the EMA product database.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information. The SmPC for Eylea and Zaltrap are available via the EMA website. No drug interaction data or specific warnings were retrievable from this Evidence Pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN confidence score of 99.38%, no clinical trials, published literature, or mechanistic evidence linking aflibercept to esotropia treatment were identified. The prediction appears to be a graph-level model inference without direct biological or clinical substantiation, and does not meet the minimum evidence threshold for advancing to a feasibility assessment.

**To proceed, the following is needed:**
- Retrieval of mechanism of action data from DrugBank (remediation identified in Evidence Pack: DG002) to confirm whether VEGF inhibition has any documented role in ocular motility disorders
- Expanded manual literature search in PubMed and Embase using broader MeSH terms (e.g., anti-VEGF AND strabismus; VEGF AND ocular motility)
- Clinical assessment of secondary esotropia subtypes where vascular or neovascular pathology may be relevant (e.g., post-retinal surgery, myopic strabismus fixus)
- Retrieval of full safety data from the Eylea and Zaltrap SmPCs (remediation identified in Evidence Pack: DG001) to evaluate route-of-administration feasibility for any ophthalmic use in esotropia
- Consultation with a Danish ophthalmologist to assess unmet clinical need and biological plausibility before any further investment in this candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

