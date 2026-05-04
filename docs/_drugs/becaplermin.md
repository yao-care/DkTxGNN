---
layout: default
title: Becaplermin
parent: 僅模型預測 (L5)
nav_order: 57
evidence_level: L5
indication_count: 10
---

# Becaplermin
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

# Becaplermin: From Diabetic Foot Ulcers to Amenorrhea

---

## One-Sentence Summary

Becaplermin (Regranex) is a recombinant human platelet-derived growth factor BB (PDGF-BB) originally approved for the topical treatment of lower extremity diabetic neuropathic ulcers.
The TxGNN model predicts it may be effective for **Amenorrhea** as the top-ranked new indication (score 99.86%); however, **no clinical trials** and **no publications** currently support this specific direction.
Across all five uniquely predicted indications, mechanistic analysis consistently reveals that PDGF-BB *agonism* is either biologically implausible or directionally contraindicated — a **Hold** decision is recommended for all candidates pending fundamental safety and mechanistic review.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Lower extremity diabetic neuropathic ulcers |
| Predicted New Indication (Rank 1) | Amenorrhea |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L5 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Becaplermin is a recombinant human PDGF-BB that acts as a PDGF receptor agonist, primarily stimulating cell proliferation, chemotaxis, and extracellular matrix synthesis in tissues expressing PDGF receptors (PDGFRα and PDGFRβ). Its established clinical role is topical promotion of granulation tissue formation in chronic diabetic wounds.

Detailed mechanism of action data was not available in the Evidence Pack. Based on known pharmacology, becaplermin is a PDGF-BB receptor agonist; its efficacy in diabetic foot ulcers has been clinically proven, and it acts through growth factor signalling pathways involved in tissue repair and cell proliferation. PDGF signalling has been reported to play an auxiliary role in folliculogenesis and ovarian stromal cell proliferation, which may have led the TxGNN knowledge graph to generate an indirect association with the female reproductive axis.

However, the mechanistic link to amenorrhea is very weak. Amenorrhea is predominantly caused by hypothalamic-pituitary-gonadal (HPG) axis dysregulation, hyperprolactinaemia, or structural uterine pathology — none of which involve PDGF-BB as a primary mediator. This prediction most likely reflects an indirect node-level association in the TxGNN graph rather than a clinically plausible biological pathway.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Denmark Market Information

Becaplermin is **not currently marketed in Denmark**. The Danish Medicines Agency (Lægemiddelstyrelsen) holds no active national marketing authorisations for this product.

> **Regulatory note**: Becaplermin (Regranex 0.01% gel) holds a centralised European Marketing Authorisation (EU/1/99/095) granted by the EMA for the treatment of lower limb neuropathic diabetic ulcers in adults. Although the EU authorisation is technically valid across all EU/EEA member states, the product appears to have no active distribution or supply in Denmark. Healthcare professionals wishing to prescribe it may need to arrange individual import through the Lægemiddelstyrelsen's compassionate use or named-patient import pathway.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for complete safety information.

> ⚠️ **Critical safety signal — Black Box Warning**: Becaplermin carries an FDA Black Box Warning for increased risk of cancer mortality, based on post-marketing pharmacovigilance data showing a higher incidence of malignant neoplasms in diabetic foot ulcer patients who received three or more tubes. This warning has direct and serious implications for any proposed oncology-adjacent repurposing (see Additional Predicted Indications below).

---

## Additional Predicted Indications — Overview and Safety Assessment

The TxGNN model returned five unique predicted indications (each appearing twice in the ranked list). All five received a **Hold** recommendation. The table below summarises each, followed by the key mechanistic concern.

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Literature | Recommendation |
|------|----------------------|-------------|----------------|------------|----------------|
| 1 | Amenorrhea | 99.86% | L5 | 0 | Hold |
| 3 | Erectile Dysfunction | 99.72% | L4 | 1 | Hold |
| 5 | HER2+ Breast Carcinoma | 99.70% | L4 | 1 | Hold |
| 7 | PR– Breast Cancer | 99.50% | L4 | 2 | Hold |
| 9 | Pulmonary Hypertension | 99.49% | L4 | 20 | Hold |

---

### Erectile Dysfunction — Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [28245285](https://pubmed.ncbi.nlm.nih.gov/28245285/) | 2017 | Basic science (cell/molecular) | PLoS One | PDGFR/STAT3 signalling regulates phenotypic transition of corpus cavernosum smooth muscle cells (CCSMCs) in rats; hypoxia-driven phenotypic switch implicated in ED pathogenesis |

**Mechanistic concern**: PDGFR/STAT3 signalling is involved in CCSMC phenotypic transition (contractile → synthetic), which is pathologically relevant to erectile dysfunction. However, becaplermin as a PDGF-BB *agonist* may *promote* smooth muscle cell proliferation and synthetic phenotype transition, theoretically worsening fibrotic remodelling rather than reversing it. The mechanistic direction requires very careful evaluation before any further investigation.

---

### HER2+ Breast Carcinoma — Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [19298655](https://pubmed.ncbi.nlm.nih.gov/19298655/) | 2009 | Basic science (cell model) | Breast Cancer Research | PPARγ protects ERBB2-positive breast cancer cells from palmitate toxicity via lipid metabolism regulation; de novo fatty acid synthesis is critical for ERBB2+ cell survival |

**Mechanistic concern — direction reversed**: PDGF signalling in the tumour microenvironment generally acts as a pro-tumorigenic driver (activating cancer-associated fibroblasts, promoting angiogenesis and tumour invasion). Combined with the existing Black Box Warning for increased cancer incidence, using a PDGF-BB agonist in HER2+ breast carcinoma carries a significant theoretical risk of accelerating tumour growth. The mechanistic rationale directly conflicts with the treatment objective.

---

### PR– Breast Cancer — Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [24577164](https://pubmed.ncbi.nlm.nih.gov/24577164/) | 2016 | Biomarker study (clinical) | American Journal of Clinical Oncology | High circulating Tie2 associated with pathological complete response to chemotherapy and anti-angiogenic therapy (bevacizumab) in breast cancer; angiogenic pathway profiling |
| [21733044](https://pubmed.ncbi.nlm.nih.gov/21733044/) | 2011 | Basic science (animal model) | Cancer Science | Soluble PDGFRβ (decoy receptor) *inhibits* intraosseous growth of breast cancer cells in nude mice; blocking PDGF-BB/PDGFRβ signalling reduces bone metastasis |

**Mechanistic concern — direction directly reversed**: PMID 21733044 explicitly demonstrates that *reducing* PDGF-BB/PDGFRβ signalling inhibits breast cancer bone metastasis. Becaplermin, as a PDGF-BB agonist, acts in the exact opposite direction. PR– breast cancer carries higher aggressiveness, and PDGF pathway activation is associated with promoting epithelial-mesenchymal transition (EMT) and metastatic spread. This prediction should not be pursued.

---

### Pulmonary Hypertension — Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [33591958](https://pubmed.ncbi.nlm.nih.gov/33591958/) | 2021 | Animal model + human tissue | JCI Insight | Macrophage-derived PDGF-B **directly induces** pulmonary arteriole muscularisation in murine and human PAH; clodronate-mediated macrophage depletion attenuates disease |
| [18420966](https://pubmed.ncbi.nlm.nih.gov/18420966/) | 2008 | Mechanistic study | Am J Respir Crit Care Med | PDGF promotes PASMC proliferation and migration; overexpression demonstrated in idiopathic PAH lesions |
| [18382765](https://pubmed.ncbi.nlm.nih.gov/18382765/) | 2008 | Animal model + human SMCs | J Clin Invest | BMP-2/PPARγ/apoE axis prevents PDGF-BB–induced PASMC proliferation; BMP-RII mutations linked to PAH |
| [17339547](https://pubmed.ncbi.nlm.nih.gov/17339547/) | 2007 | Animal model | Circulation | Enhanced PDGF signalling in apoE-deficient mice linked to PAH; PPARγ activation reverses disease |
| [19324949](https://pubmed.ncbi.nlm.nih.gov/19324949/) | 2009 | Clinical study | European Respiratory Journal | Elevated circulating PDGF-BB levels across pulmonary circulation in PAH patients; correlates with haemodynamic severity |
| [39360410](https://pubmed.ncbi.nlm.nih.gov/39360410/) | 2024 | Basic science (non-coding RNA) | Arteriosclerosis, Thrombosis, Vascular Biology | PDGF signalling activation promotes PASMC hyperproliferation and pulmonary vascular remodelling in PAH |
| [39901736](https://pubmed.ncbi.nlm.nih.gov/39901736/) | 2025 | Multi-omics, animal model | American Journal of Hypertension | PDGF-BB–induced PASMC model used to map transcriptomic and metabolomic changes in PAH pathogenesis |
| [41213438](https://pubmed.ncbi.nlm.nih.gov/41213438/) | 2026 | Basic science (animal model) | Free Radical Biology & Medicine | TRIB2 promotes PASMC proliferation via SERCA2 ubiquitination; PDGF-BB stimulation used as disease model |
| [39551320](https://pubmed.ncbi.nlm.nih.gov/39551320/) | 2024 | Basic science (non-coding RNA) | Int J Biological Macromolecules | miR-34a-3p/DUSP1 axis inhibits PDGF-BB–induced hPASMC proliferation; MEG3 lncRNA aggravates APE-induced PAH |
| [38614383](https://pubmed.ncbi.nlm.nih.gov/38614383/) | 2024 | Pharmacological study | European Journal of Pharmacology | Corosolic acid attenuates PDGF signalling in macrophages and SMCs; anti-PAH effect via PDGF pathway *inhibition* |

**Mechanistic concern — critically reversed, high patient safety risk**: This is the most clinically significant safety flag in the entire analysis. The overwhelming consensus across 20 publications is that PDGF-B/PDGFRβ signalling *drives* pulmonary arterial smooth muscle cell (PASMC) hyperproliferation and vascular remodelling — the defining pathological process of pulmonary arterial hypertension (PAH). Importantly, the PDGF receptor inhibitor imatinib (Gleevec) has been studied in Phase 3 clinical trials for PAH precisely by *blocking* this pathway. Administering becaplermin (a PDGF-BB *agonist*) to a patient with pulmonary hypertension would theoretically directly accelerate vascular remodelling. **This indication must not be pursued.**

---

## Conclusion and Next Steps

**Decision: Hold (All Predicted Indications)**

**Rationale:**
For the highest-ranked prediction (amenorrhea), the evidence level is L5 — model prediction only, with zero supporting clinical trials or published literature, and no biologically plausible mechanistic link between PDGF-BB agonism and the condition. More broadly, across all five predicted indications, mechanistic analysis consistently shows that becaplermin's mode of action (PDGF-BB agonism) is either directionally inconsistent with therapeutic benefit or poses active safety risk — most critically in pulmonary hypertension, where the existing literature establishes PDGF-BB as a key disease driver, and in oncology-related indications where the existing Black Box Warning must be treated as a blocking signal.

**To proceed with any further investigation, the following is required:**

- **MOA data gap resolution**: Obtain full DrugBank mechanism-of-action profile to characterise receptor binding specificity, downstream signalling cascades, and tissue distribution
- **Danish regulatory and safety data**: Obtain the approved EMA SmPC for Regranex (EU/1/99/095), paying particular attention to the oncology Black Box Warning and its implications for any proposed new indication
- **Route compatibility assessment**: The current approved formulation is a topical gel (0.01%). For all predicted indications (amenorrhea, erectile dysfunction, breast cancer, pulmonary hypertension), systemic or alternative delivery would be required — a separate formulation development programme would be necessary
- **Preclinical biological plausibility work for amenorrhea**: Before any clinical consideration, in vitro and in vivo studies demonstrating PDGF-BB–mediated effects on HPG axis regulation or endometrial function would be required
- **Formal safety risk assessment for oncology-adjacent indications**: Before any investigation in breast cancer subtypes, a structured benefit-risk analysis addressing the Black Box Warning and the pro-tumorigenic role of PDGF signalling must be completed and reviewed by a multidisciplinary team
- **Definitive exclusion of pulmonary hypertension**: Given the weight of evidence demonstrating PDGF-BB as a direct contributor to PAH pathogenesis, this indication should be formally excluded from further repurposing consideration without extraordinary new mechanistic evidence

---

*This report is generated for research reference purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before any therapeutic application. Please refer to the full approved Summary of Product Characteristics (SmPC) for all prescribing decisions.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

