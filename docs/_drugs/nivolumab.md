---
layout: default
title: Nivolumab
parent: 僅模型預測 (L5)
nav_order: 312
evidence_level: L5
indication_count: 10
---

# Nivolumab
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

# Nivolumab: From Melanoma to Non-Cutaneous Melanoma

## One-Sentence Summary

> Nivolumab is an anti-PD-1 immune checkpoint inhibitor whose first approved use was in melanoma treatment.
> The TxGNN model predicts it may also be effective for **Non-Cutaneous Melanoma** (rare melanoma subtypes such as mucosal, ocular, and metastatic-site presentations),
> with **50 clinical trials** and **8 publications** currently supporting this direction — though this represents an extension of an already-validated mechanism rather than a true cross-disease repurposing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (no Danish marketing authorisation on file); Nivolumab's known first approved oncology indication is (cutaneous) melanoma |
| Predicted New Indication | Non-Cutaneous Melanoma |
| TxGNN Prediction Score | 98.41% |
| Evidence Level | L1 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is flagged as a data gap in this evidence pack (DG002). However, Nivolumab's pharmacological class is well established in the broader literature and is reflected in the underlying prediction rationale: it is an anti-programmed cell death protein 1 (anti-PD-1) monoclonal antibody, an immune checkpoint inhibitor that blocks PD-1/PD-L1 signalling to restore T-cell-mediated anti-tumour immunity.

Melanoma — including cutaneous forms — was among Nivolumab's earliest approved oncology indications. "Non-cutaneous melanoma" is not a distinct disease but a grouping of rarer melanoma presentations (e.g. mucosal, ocular/uveal, metastatic-site melanoma) that share the same underlying tumour biology and PD-L1 expression pathways as cutaneous melanoma. Because the checkpoint-blockade mechanism does not depend on the anatomical site of the primary lesion, extending Nivolumab to non-cutaneous subtypes is mechanistically a natural and low-risk extension of an already-validated therapeutic principle, rather than a repurposing into an unrelated disease area.

This is corroborated by the supporting evidence: several trials and cohort studies directly enrol non-cutaneous/rare melanoma subtypes (e.g. mucosal, acral, ocular, mediastinal, anorectal presentations) alongside standard cutaneous melanoma populations, generally showing continued — though sometimes attenuated — clinical activity.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03635983](https://clinicaltrials.gov/study/NCT03635983) | Phase 3 | Completed | 783 | NKTR-214 + nivolumab vs. nivolumab alone in previously untreated unresectable/metastatic melanoma; largest completed head-to-head trial in this pack |
| [NCT04114136](https://clinicaltrials.gov/study/NCT04114136) | Phase 2 | Recruiting | 72 | Anti-PD-1 mAb (pembrolizumab/nivolumab) as standard-of-care arm across melanoma and other solid tumours, testing metabolic modulators to reverse tumour hypoxia |
| [NCT02990611](https://clinicaltrials.gov/study/NCT02990611) | N/A (non-interventional) | Completed | 1087 | National prospective real-world study of nivolumab monotherapy or with ipilimumab in advanced and adjuvant melanoma settings |
| [NCT04157985](https://clinicaltrials.gov/study/NCT04157985) | Phase 3 | Completed | 161 | Randomised trial evaluating optimal duration of PD-1/PD-L1 inhibitor therapy in advanced solid tumours including melanoma |
| [NCT05116202](https://clinicaltrials.gov/study/NCT05116202) | Phase 1b/2 | Completed | 110 | Morpheus-Melanoma umbrella study evaluating multiple nivolumab-based treatment combinations in resectable/metastatic melanoma |
| [NCT03325257](https://clinicaltrials.gov/study/NCT03325257) | N/A (follow-up cohort) | Completed | 350 | Two-year follow-up of melanoma patients treated with nivolumab during the French early-access (ATU) programme |
| [NCT03033576](https://clinicaltrials.gov/study/NCT03033576) | Phase 2 | Completed | 94 | Nivolumab ± ipilimumab in advanced melanoma refractory to prior anti-PD-1/PD-L1 therapy |
| [NCT02910700](https://clinicaltrials.gov/study/NCT02910700) | Phase 2 | Active, not recruiting | 52 | Triplet combinations of nivolumab with BRAF/MEK inhibitors in BRAF-mutated metastatic melanoma |
| [NCT04146324](https://clinicaltrials.gov/study/NCT04146324) | N/A (observational) | Completed | 150 | Prospective real-world study of adjuvant nivolumab in resected melanoma (Australia), 5-year follow-up |
| [NCT04165967](https://clinicaltrials.gov/study/NCT04165967) | Phase 1 | Completed | 9 | TIL adoptive transfer combined with nivolumab in advanced melanoma failing prior immunotherapy |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26841210](https://pubmed.ncbi.nlm.nih.gov/26841210/) | 2016 | Cohort | J Eur Acad Dermatol Venereol | Single-institution comparison of cutaneous vs. non-cutaneous melanoma treated with nivolumab |
| [30510916](https://pubmed.ncbi.nlm.nih.gov/30510916/) | 2018 | Cohort | Frontiers in Oncology | Serum soluble CD163 as a predictive biomarker of nivolumab effectiveness in advanced melanoma |
| [37887546](https://pubmed.ncbi.nlm.nih.gov/37887546/) | 2023 | Cohort | Current Oncology | Retrospective comparison of anti-PD-1 ± ipilimumab outcomes by age group in advanced melanoma |
| [34176837](https://pubmed.ncbi.nlm.nih.gov/34176837/) | 2022 | Case Report | Internal Medicine (Tokyo) | Mediastinal (non-cutaneous) malignant melanoma with marked shrinkage on nivolumab monotherapy |
| [40236344](https://pubmed.ncbi.nlm.nih.gov/40236344/) | 2025 | Case Report | Cureus | Colonic metastasis from melanoma managed with immunotherapy including nivolumab |
| [41774417](https://pubmed.ncbi.nlm.nih.gov/41774417/) | 2025 | Case Report | Pigment Cell & Melanoma Research | Epidermotropic metastatic melanoma continuing to form new lesions despite adjuvant nivolumab |
| [30549256](https://pubmed.ncbi.nlm.nih.gov/30549256/) | 2019 | Case Report | Int J Rheum Dis | Association between rheumatic immune-related adverse events and treatment response to PD-1 inhibitors |
| [28171845](https://pubmed.ncbi.nlm.nih.gov/28171845/) | 2017 | Case Report | Int J Surg Case Rep | First reported case of metastatic anorectal amelanotic (non-cutaneous) melanoma responding to nivolumab |

---

## Denmark Market Information

Nivolumab currently has no marketing authorisation on file in Denmark (0 authorisations recorded; market status: not marketed). No product name, dosage form, or approved indication text is available from Danish regulatory sources for this evidence pack.

---

## Cytotoxicity

Nivolumab is an immune checkpoint inhibitor (anti-PD-1 monoclonal antibody) and is classified as antineoplastic based on its established oncology indication and drug class, though it is **not** a conventional cytotoxic agent.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Immunotherapy (anti-PD-1 immune checkpoint inhibitor) |
| Myelosuppression Risk | Low — mechanism does not directly target bone marrow; classic cytotoxic myelosuppression is not the primary concern |
| Emetogenicity Classification | Low |
| Monitoring Items | Immune-related adverse events (irAEs): thyroid function, liver function (LFTs), renal function, pulmonary status (pneumonitis), colitis symptoms, skin reactions, and cardiac monitoring — literature in this pack documents nivolumab-associated myocarditis and rhabdomyolysis cases |
| Handling Protection | Standard biologic/monoclonal antibody handling precautions apply; conventional cytotoxic drug handling protocols are not required |

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information. This evidence pack has no key warnings, contraindications, or drug-drug interaction data on file for Nivolumab (a blocking data gap, DG001, has been logged for missing Danish label information).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The underlying anti-PD-1 mechanism is already clinically validated in melanoma, including a completed Phase 3 head-to-head trial (NCT03635983, n=783) and a large real-world cohort (n=1087), supporting L1-level evidence overall. However, this is an extension within an already-approved disease area rather than a novel repurposing, and formal safety/label data for the Danish market is entirely missing (blocking gap).

**To proceed, the following is needed:**
- Danish/EU Summary of Product Characteristics (SmPC) — resolves blocking data gap DG001
- Confirmed mechanism-of-action documentation from DrugBank — resolves DG002
- Subtype-specific efficacy data isolating non-cutaneous melanoma outcomes from mixed-population trials
- A structured immune-related adverse event monitoring plan given the myocarditis and rhabdomyolysis signals noted in the literature review
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

