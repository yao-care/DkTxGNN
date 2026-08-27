---
layout: default
title: Insulin Aspart
parent: 僅模型預測 (L5)
nav_order: 234
evidence_level: L5
indication_count: 10
---

# Insulin Aspart
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

# Insulin Aspart: Established Use in Type 1 Diabetes Mellitus (Data Gap Flagged, Not a Novel Repurposing Candidate)

## One-Sentence Summary

> Insulin Aspart (DrugBank DB01306) is a rapid-acting human insulin analogue. Because the drug record's *original indication* field is empty in this Evidence Pack, the model has surfaced **Type 1 Diabetes Mellitus** — insulin aspart's own well-established core indication — as the top "predicted" indication, supported by **>50 clinical trials** and **20 publications**. This is **not a genuine drug-repurposing signal**; it reflects a data-gap artefact and should be read as a mechanism/evidence confirmation exercise rather than a novel indication proposal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in this Evidence Pack (data gap — `original_indications` is empty and no Danish licence text exists to extract from) |
| Predicted New Indication | Type 1 Diabetes Mellitus *(see caveat below — this is the drug's known established indication, not a novel candidate)* |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L1 (≥2 completed Phase 3 RCTs identified) |
| Denmark Market Status | Not Marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Proceed with Guardrails *(for confirmatory/market-entry purposes — see Conclusion)* |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action text is not available in this Evidence Pack (`original_moa: [Data Gap]`). Based on the information that is available, however, insulin aspart is a rapid-acting human insulin analogue in which proline at position B28 is substituted with aspartic acid, accelerating subcutaneous absorption relative to regular human insulin. Like all insulin products, it acts by binding the insulin receptor and activating the PI3K/Akt and MAPK signalling cascades, promoting cellular glucose uptake, hepatic glycogen synthesis, and suppression of hepatic gluconeogenesis.

Type 1 diabetes mellitus is caused by autoimmune destruction of pancreatic β-cells, resulting in absolute insulin deficiency. Insulin aspart directly replaces this missing hormone — the mechanistic link is direct and well established, not inferential.

**Important caveat:** The evidence pack's own repurposing rationale explicitly flags that this is *not* a repurposing candidate: "此項並非'老藥新用'候選，而是藥物已確立之核心適應症，資料庫因 `original_indications` 欄位缺失而將其列為預測項目" (this item is not a drug-repurposing candidate but the drug's already-established core indication; it was listed as a "prediction" only because the `original_indications` field is empty). The large body of Phase 3 evidence below therefore confirms an already-known use rather than validating a new one. Given that insulin aspart is **not currently marketed in Denmark**, the practical value of this evidence is to support a potential **market authorisation submission**, not a repurposing pathway.

For completeness, the model also returned several lower-ranked candidates (autoimmune oophoritis, opsismodysplasia, thiamine-responsive dysfunction syndrome, permanent neonatal diabetes mellitus) with high raw scores but little-to-no direct clinical or mechanistic support in this pack; these are not elaborated further here per the reporting scope, but should not be mistaken for validated repurposing leads.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01486940](https://clinicaltrials.gov/study/NCT01486940) | Phase 3 | Completed | 598 | Multinational RCT comparing insulin detemir + insulin aspart vs. NPH + human soluble insulin in basal-bolus regimen for T1DM |
| [NCT01513473](https://clinicaltrials.gov/study/NCT01513473) | Phase 3 | Completed | 350 | 26-week + 26-week extension RCT of degludec vs. detemir with insulin aspart as bolus in children/adolescents with T1DM (BEGIN Young 1) |
| [NCT02670915](https://clinicaltrials.gov/study/NCT02670915) | Phase 3 | Completed | 834 | Global RCT of faster-acting insulin aspart vs. NovoRapid, both combined with degludec, in children/adolescents with T1DM |
| [NCT01134107](https://clinicaltrials.gov/study/NCT01134107) | Phase 3 | Completed | 133 | Double-blind crossover RCT of insulin lispro vs. insulin aspart in CSII pump reservoirs for T1DM |
| [NCT00046150](https://clinicaltrials.gov/study/NCT00046150) | Phase 3 | Completed | 59 | RCT comparing safety of HMR1964 vs. insulin aspart in continuous subcutaneous insulin infusion (CSII) for T1DM |
| [NCT01513590](https://clinicaltrials.gov/study/NCT01513590) | Phase 3 | Completed | 394 | 26-week RCT of insulin degludec/aspart (IDegAsp) vs. BIAsp 30, both with metformin, in insulin-naïve T2DM |
| [NCT04196231](https://clinicaltrials.gov/study/NCT04196231) | Phase 4 | Completed | 258 | RCT (BEYOND) evaluating durability of glycaemic control with basal insulin/GLP-1RA or SGLT-2i vs. basal-bolus regimen in T2DM |
| [NCT06199505](https://clinicaltrials.gov/study/NCT06199505) | Phase 2 | Completed | 153 | RCT comparing GZR101 vs. insulin degludec/aspart in T2DM inadequately controlled on oral agents |
| [NCT00675493](https://clinicaltrials.gov/study/NCT00675493) | N/A (observational) | Completed | 942 | 24-week observational study of NovoMix 30 (biphasic insulin aspart 30) for T1DM/T2DM glycaemic control (Romania) |
| [NCT00700648](https://clinicaltrials.gov/study/NCT00700648) | N/A (observational) | Completed | 3024 | Multicentre observational study of IV insulin aspart (NovoRapid) safety/efficacy in hospitalised patients (Asia) |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37863084](https://pubmed.ncbi.nlm.nih.gov/37863084/) | 2023 | RCT | Lancet | ONWARDS 6: once-weekly insulin icodec vs. once-daily degludec as part of basal-bolus regimen (with aspart as bolus) in T1DM |
| [36623517](https://pubmed.ncbi.nlm.nih.gov/36623517/) | 2023 | RCT | Lancet Diabetes & Endocrinology | EXPECT trial: degludec vs. detemir, both combined with insulin aspart, in pregnant women with T1DM |
| [21333580](https://pubmed.ncbi.nlm.nih.gov/21333580/) | 2011 | RCT/Systematic Review | Diabetes & Metabolism | Systematic review confirming efficacy/safety of rapid-acting insulin aspart vs. regular human insulin in T1DM and T2DM |
| [41697686](https://pubmed.ncbi.nlm.nih.gov/41697686/) | 2026 | Review | JAMA | Overview of T1DM pathophysiology (autoimmune β-cell destruction) and epidemiology, underpinning insulin replacement rationale |
| [37290466](https://pubmed.ncbi.nlm.nih.gov/37290466/) | 2023 | Review | Lancet Diabetes & Endocrinology | Management of T1DM in pregnancy, including insulin analogue use and glycaemic targets |
| [15871555](https://pubmed.ncbi.nlm.nih.gov/15871555/) | 2003 | Review | Treatments in Endocrinology | Insulin aspart lowers HbA1c vs. regular human insulin in T1DM/T2DM RCTs |
| [12215068](https://pubmed.ncbi.nlm.nih.gov/12215068/) | 2002 | Review | Drugs | Review of insulin aspart efficacy/safety in T1DM and T2DM management |
| [25143741](https://pubmed.ncbi.nlm.nih.gov/25143741/) | 2014 | Review | Vascular Health and Risk Management | Insulin degludec/aspart combination for T1DM and T2DM treatment |
| [30789066](https://pubmed.ncbi.nlm.nih.gov/30789066/) | 2019 | Review | Expert Opinion on Drug Metabolism & Toxicology | Review of degludec/aspart premix insulin use in T1DM |
| [18710361](https://pubmed.ncbi.nlm.nih.gov/18710361/) | 2008 | Cohort | Expert Opinion on Pharmacotherapy | Evidence-based review of biphasic insulin aspart 30 for T1DM treatment |

---

## Denmark Market Information

Insulin Aspart currently has **no Marketing Authorisations recorded in Denmark** (market status: Not Marketed; 0 licences). No Laegemiddelstyrelsen or centralised EMA authorisation data is available in this Evidence Pack.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information. No key warnings, contraindications, or drug-drug interaction data were available for extraction from this Evidence Pack (DDI query status: not found).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
- The clinical trial and literature base for insulin aspart in Type 1 Diabetes Mellitus is extensive and mature (multiple completed Phase 3 RCTs, decades of published evidence), but this evidence confirms an **already-established indication**, not a novel repurposing opportunity — the "prediction" arose from a data gap in the `original_indications` field, not a genuine model-driven hypothesis.
- Because the product is **not currently marketed in Denmark**, the practical decision this evidence pack supports is whether to pursue Danish market authorisation for an insulin product with a well-known international safety and efficacy record — not a repurposing evaluation.

**To proceed, the following is needed:**
- TFDA/SmPC-equivalent Danish or EU labelling data (warnings, contraindications, precautions) — currently a **Blocking** data gap preventing any S1 safety pre-assessment
- Confirmed mechanism-of-action documentation from DrugBank (currently a **High**-severity data gap)
- Correction of the `original_indications` field so future TxGNN runs do not re-surface the drug's own core indication as a "predicted new indication"
- If Danish market entry is the actual goal, a formal review of EMA/centralised authorisation status for insulin aspart products (e.g., NovoRapid, Fiasp) and applicability to the Danish market
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

