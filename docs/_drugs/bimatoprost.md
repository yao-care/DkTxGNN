---
layout: default
title: Bimatoprost
parent: 僅模型預測 (L5)
nav_order: 64
evidence_level: L5
indication_count: 10
---

# Bimatoprost
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

# Bimatoprost: From Glaucoma / Eyelash Hypotrichosis to Malformation Syndrome with Odontal and/or Periodontal Component

## One-Sentence Summary

Bimatoprost is a prostaglandin FP receptor agonist (PGF2α analogue) internationally established for treating elevated intraocular pressure in glaucoma (Lumigan) and eyelash hypotrichosis (Latisse), though it holds no marketing authorisation in Denmark.
The TxGNN model predicts it may be effective for **Malformation Syndrome with Odontal and/or Periodontal Component**, with a prediction score of 99.9974%.
However, **no clinical trials** and **no bimatoprost-specific publications** directly support this direction — the 20 retrieved publications are general periodontitis background literature, not studies investigating bimatoprost for this rare congenital syndrome, placing this prediction at evidence level **L5**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Denmark; internationally approved for glaucoma / ocular hypertension and eyelash hypotrichosis |
| Predicted New Indication | Malformation syndrome with odontal and/or periodontal component |
| TxGNN Prediction Score | 99.9974% |
| Evidence Level | L5 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on established pharmacology, Bimatoprost is a synthetic prostaglandin F2α (PGF2α) analogue that acts as a selective agonist at the FP prostaglandin receptor (PTGFR). In the eye, it lowers intraocular pressure by enhancing uveoscleral and trabecular aqueous outflow from the ciliary body. In hair follicles, it prolongs the anagen (active growth) phase by activating FP and EP3 receptors, a mechanism that underlies its FDA-approved use for eyelash hypotrichosis (Latisse, 2008).

The predicted indication — malformation syndrome with odontal and/or periodontal component — refers to a heterogeneous group of rare *congenital* syndromes characterised by developmental abnormalities in tooth structure and periodontal tissue formation. This is pathophysiologically distinct from the drug's known mechanism: bimatoprost acts on the prostaglandin FP receptor in adult ciliary body and hair follicle tissue, not on the embryological signalling pathways (e.g., WNT, BMP, SHH) that govern odontogenesis or periodontal ligament morphogenesis. While prostaglandin E2 (PGE2) is elevated in *acquired inflammatory* periodontitis, the PGF2α pathway has very limited documented involvement in the bone destruction or soft-tissue pathology of inflammatory periodontal disease — and still less in the congenital developmental variants predicted here.

The extremely high TxGNN knowledge graph score (99.9974%) most plausibly reflects the topological proximity of "periodontal tissue – prostaglandin – inflammation" nodes in the knowledge graph rather than a genuine therapeutic relationship. The mechanistic bridge between bimatoprost and this congenital syndrome is absent, and this prediction should be treated with significant caution.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

> **Important caveat:** The 20 retrieved publications are general periodontitis and periodontal disease literature. **None of these papers directly investigate bimatoprost for malformation syndrome with odontal/periodontal component.** They were retrieved based on the periodontal disease search term and constitute background context only — they do not constitute supportive evidence for this repurposing candidate.

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [35688447](https://pubmed.ncbi.nlm.nih.gov/35688447/) | 2022 | Clinical Guideline | J Clin Periodontol | EFP S3-level evidence-based clinical practice guideline for treatment of stage IV periodontitis, covering severity, complexity and functional sequelae |
| [35420698](https://pubmed.ncbi.nlm.nih.gov/35420698/) | 2022 | Cochrane Systematic Review | Cochrane Database Syst Rev | Periodontal treatment modestly improves HbA1c in diabetes mellitus; bidirectional relationship confirmed between glycaemic control and periodontitis |
| [29291254](https://pubmed.ncbi.nlm.nih.gov/29291254/) | 2018 | Cochrane Systematic Review | Cochrane Database Syst Rev | Supportive periodontal therapy (SPT) reduces probability of re-infection and disease progression following active periodontal treatment |
| [38362600](https://pubmed.ncbi.nlm.nih.gov/38362600/) | 2024 | Clinical Observational | J Dental Research | Stage III/IV periodontitis associated with gut microbial dysbiosis; periodontal treatment partially restores both oral and gut microbiota composition |
| [38907216](https://pubmed.ncbi.nlm.nih.gov/38907216/) | 2024 | Preclinical / Basic Research | J Nanobiotechnology | Biomaterial-mediated macrophage immunotherapy proposed as novel direction in periodontitis treatment; highlights role of immune dysregulation |
| [37435999](https://pubmed.ncbi.nlm.nih.gov/37435999/) | 2023 | Narrative Review | Periodontology 2000 | Complications and treatment errors in regenerative periodontal surgery for intrabony and furcation defects |
| [36883660](https://pubmed.ncbi.nlm.nih.gov/36883660/) | 2023 | Basic Science Review | J Dental Research | Gingival fibroblasts act as sentinel innate immune cells, modulating inflammatory response to oral pathogens in periodontitis pathogenesis |
| [29193334](https://pubmed.ncbi.nlm.nih.gov/29193334/) | 2018 | Comparative Clinical Study | Periodontology 2000 | Key structural differences between peri-implant and natural periodontal soft tissues; parallel collagen fibre orientation around implants differs from natural tooth attachment |
| [22057194](https://pubmed.ncbi.nlm.nih.gov/22057194/) | 2012 | Review | Diabetologia | Diabetes increases susceptibility to periodontitis approximately threefold; bidirectional relationship demonstrated across multiple epidemiological datasets |
| [12010523](https://pubmed.ncbi.nlm.nih.gov/12010523/) | 2002 | Evidence-based Review | J Clin Periodontol | Scaling and root planing (SRP) remains the gold standard for non-surgical treatment of chronic periodontitis, with consistent clinical outcomes across instrumentation types |

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information. Full safety data (key warnings and contraindications) were not available in this Evidence Pack and represent a blocking data gap that must be resolved before any clinical evaluation can proceed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite an extremely high TxGNN knowledge graph score (99.9974%), the predicted indication — malformation syndrome with odontal and/or periodontal component — is a rare congenital developmental disorder with no mechanistic connection to bimatoprost's prostaglandin FP receptor pharmacology. No clinical trials and no bimatoprost-specific publications exist for this indication. The evidence level is L5 (model prediction only), and the high prediction score is almost certainly a topological artefact of the knowledge graph rather than a clinically actionable signal.

> ⚠️ **Additional safety flag — Rank 7–8 (Ambras-type Hypertrichosis Universalis Congenita):** A negative mechanism alert has been identified among the top 10 predictions. Bimatoprost's well-documented side effect profile includes hypertrichosis (excess hair growth), as explicitly listed in the Latisse prescribing information. Applying bimatoprost to treat Ambras-type congenital hypertrichosis — a condition of pathological excess hair growth — would be mechanistically contradictory and carries a concrete risk of exacerbating the condition. This prediction should be considered a knowledge graph false positive with a clinical safety concern.

**To proceed with any repurposing evaluation, the following is needed:**

- **Resolve the blocking data gap**: Obtain SmPC warnings and contraindications from the official source before any safety assessment can proceed
- **Retrieve complete MOA data**: Query DrugBank API for full mechanism of action, pharmacodynamic targets, and toxicity profile
- **Redirect focus to biologically plausible candidates**: **Hypotrichosis simplex of the scalp (Rank 9–10)** is the most scientifically justified prediction in this pack — bimatoprost's FDA-approved eyelash indication and its known FP/EP3-mediated anagen prolongation provide a direct mechanistic analogy to scalp hair follicle biology. Exploratory Phase 1/2 data for androgenetic alopecia exists in the broader literature and warrants dedicated evidence collection
- **Conduct a targeted literature search**: Re-run PubMed and ClinicalTrials.gov searches specifically linking "bimatoprost" to the individual predicted indications, rather than broad periodontal disease terms, to verify whether the current zero-hit results reflect genuine evidence absence or collector coverage limitations
- **Assess route of administration feasibility**: A topical formulation strategy would be required for the scalp hypotrichosis indication; Denmark market entry requirements with the Danish Medicines Agency (Lægemiddelstyrelsen) should be evaluated separately

---

*This report is for research reference purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before any therapeutic application. Prepared: 2026-04-04.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

