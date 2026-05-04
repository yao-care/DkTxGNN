---
layout: default
title: Belimumab
parent: 僅模型預測 (L5)
nav_order: 59
evidence_level: L5
indication_count: 10
---

# Belimumab
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

# Belimumab: From Systemic Lupus Erythematosus to Primary Release Disorder of Platelets

## One-Sentence Summary

Belimumab (Benlysta) is a fully human anti-BLyS monoclonal antibody approved for the treatment of active, autoantibody-positive Systemic Lupus Erythematosus (SLE). The TxGNN model assigns it the highest predicted score of **99.96%** for **primary release disorder of platelets** — however, only **1 clinical trial** was retrieved, and it is of marginal relevance (Grade C), with **no supporting publications** identified. The mechanistic bridge between the drug's B-cell suppression pathway and this intrinsic platelet granule disorder is extremely weak, making the current evidence base insufficient to advance this candidate.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Systemic Lupus Erythematosus (SLE) — active, autoantibody-positive |
| Predicted New Indication | Primary release disorder of platelets |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L5 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Belimumab is a fully human IgG1λ monoclonal antibody that specifically binds and neutralises soluble B-lymphocyte stimulator (BLyS, also known as BAFF). By blocking the BLyS survival signal, belimumab reduces the differentiation and survival of autoreactive B cells and thereby lowers circulating pathogenic autoantibody (e.g. anti-dsDNA, anti-Sm) titres. This mechanism is well-validated in SLE, where dysregulated BLyS overexpression drives the autoimmune cascade.

Primary release disorder of platelets (storage pool disease; δ- or α-granule deficiency) is a category of intrinsic platelet functional defects characterised by impaired release of granule contents upon activation. The pathophysiology is determined by platelet-intrinsic structural or biosynthetic deficits in granule formation — it is not driven by circulating autoantibodies or B-cell overactivity. Consequently, the mechanistic rationale provided in this evidence pack itself acknowledges that the BLyS inhibition pathway has "almost no direct mechanistic link" to this condition.

The high TxGNN score most likely reflects graph-level co-associations within the knowledge graph — for instance, overlapping node neighbourhoods shared between SLE (an autoimmune thrombocytopenic phenotype) and platelet-disorder nodes — rather than a true pharmacological hypothesis. Until a mechanistic bridge is articulated or translational data emerge, this prediction should be treated as a computational artefact rather than a clinically actionable lead.

---

## Predicted Indications Overview

The evidence pack contains five unique predicted indications (each appears twice due to a deduplication artefact). All are ranked L5 with a **Hold** recommendation, except fetal and neonatal alloimmune thrombocytopenia (FNAIT), which is classified as a **Research Question** due to a plausible, albeit unproven, immunological rationale.

| Rank | Disease | TxGNN Score | Evidence Level | Recommendation | Mechanistic Plausibility |
|------|---------|-------------|---------------|---------------|--------------------------|
| 1 | Primary release disorder of platelets | 99.96% | L5 | Hold | Very weak — intrinsic platelet granule defect, not immune-mediated |
| 3 | Pseudo-von Willebrand disease | 99.96% | L5 | Hold | Very weak — GPIbα gain-of-function mutation, not B-cell driven |
| 5 | Glanzmann thrombasthenia | 99.87% | L5 | Hold | Weak (inherited ITGA2B/ITGB3 defect); theoretical plausibility only for acquired autoimmune subtype |
| 7 | Fetal and neonatal alloimmune thrombocytopenia (FNAIT) | 99.59% | L5 | Research Question | Moderate — maternal IgG alloantibody-mediated; BLyS inhibition could theoretically reduce alloantibody production |
| 9 | Severe nonproliferative diabetic retinopathy | 99.05% | L5 | Hold | Very weak — metabolic/vascular aetiology, BLyS not a primary driver |

---

## Clinical Trial Evidence

> **Note:** Only one trial was retrieved, and its relevance grade is **C** (not applicable to primary release disorder of platelets). The trial investigated belimumab in autoimmune membranous glomerulonephropathy — a wholly different disease. This match represents a database mapping error and should not be interpreted as trial-level support for the predicted indication.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|-----------|--------------|
| [NCT01610492](https://clinicaltrials.gov/study/NCT01610492) | Phase 2 | Completed | 14 | Open-label study of belimumab (10 mg/kg IV) in PLA2R autoantibody-positive idiopathic membranous glomerulonephropathy; evaluated efficacy, safety and biomarkers over 24 weeks. **Not relevant to platelet release disorders.** |

No clinical trials were identified for pseudo-von Willebrand disease, Glanzmann thrombasthenia, FNAIT, or severe nonproliferative diabetic retinopathy.

---

## Literature Evidence

Currently no related literature available for any of the five predicted indications.

---

## Denmark Market Information

Belimumab is not registered with the Danish Medicines Agency (Lægemiddelstyrelsen) in this dataset. No national marketing authorisations are recorded.

> **Data note:** Benlysta (belimumab) holds EMA centralised authorisation (EU/1/11/700/001–002, approved 2011, extended 2017 for lupus nephritis) and is commercially available in the majority of EU member states. The absence of entries in this dataset may reflect a data-coverage gap rather than a true regulatory void in Denmark. Healthcare professionals should verify current availability via the European Medicines Agency (EMA) product register and the Danish Medicines Agency's Produktresumé database.

---

## Safety Considerations

Detailed warning and contraindication data were not retrieved in this evidence pack. Please refer to the approved Summary of Product Characteristics (SmPC) for full safety information.

Based on the known pharmacology and regulatory history of belimumab, prescribers should be aware of the following general class-level considerations:

- **Immunosuppression:** As a B-cell modulator, belimumab increases susceptibility to infections, including opportunistic and serious infections.
- **Psychiatric/neurological events:** Post-marketing data have indicated cases of depression, suicidality, and psychosis.
- **Infusion and hypersensitivity reactions:** Acute hypersensitivity reactions, including anaphylaxis, have been reported.
- **Pregnancy:** Use during pregnancy is not recommended; belimumab crosses the placenta and may affect neonatal B-cell counts. This consideration is particularly relevant for the FNAIT indication hypothesis (rank 7), where the drug would need to be administered to pregnant women — an unstudied and potentially high-risk population.
- **Live vaccines:** Should not be administered concurrently.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All five predicted indications are rated Evidence Level L5 (model prediction only, no clinical or translational studies), and for the top-ranked indication — primary release disorder of platelets — the mechanistic connection to belimumab's BLyS-inhibition pathway is biologically implausible. The single retrieved clinical trial is irrelevant (database mapping error), and no supporting literature exists for any of the five diseases.

**The single exception warranting further monitoring is FNAIT (rank 7):** the maternal alloantibody-mediated pathophysiology provides a conceptually coherent rationale for B-cell-targeted therapy. However, pregnancy safety data are absent, and no clinical or preclinical studies have been conducted.

**To advance any of these candidates, the following is required:**

- **MOA data gap (DG002):** Obtain full DrugBank mechanistic data and published BLyS biology literature to formally assess pathway overlap with each predicted indication.
- **FNAIT (rank 7) only — Preclinical proof-of-concept:** Commission or identify in vitro/animal studies examining whether anti-BLyS therapy reduces alloantibody titres in an HPA-1a sensitisation model before any human trial design.
- **FNAIT — Pregnancy safety assessment:** A dedicated benefit–risk analysis for use in pregnancy is mandatory prior to any clinical trial initiation.
- **Mapping quality control:** The retrieval pipeline returned an off-target trial (NCT01610492) for the platelet indication. A precision review of the disease-term matching algorithm is recommended to prevent false-positive evidence signals in future packs.
- **Denmark regulatory status clarification:** Confirm current Benlysta availability via EMA and the Danish Medicines Agency product register to correct the "not marketed" flag if applicable.

---

*This report is generated for research reference purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before any therapeutic application. Data cut-off: 2026-04-04.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

