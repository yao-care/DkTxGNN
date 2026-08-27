---
layout: default
title: Trastuzumab Deruxtecan
parent: 僅模型預測 (L5)
nav_order: 447
evidence_level: L5
indication_count: 10
---

# Trastuzumab Deruxtecan
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

# Trastuzumab Deruxtecan: From HER2-Targeted Oncology Use to Predicted Drug-Induced Osteoporosis

## One-Sentence Summary

> Trastuzumab deruxtecan (T-DXd) is a HER2-targeted antibody-drug conjugate (ADC) whose original approved indication is not specified in this evidence pack.
> The TxGNN model's top prediction is **Drug-Induced Osteoporosis** (score 99.31%), but this candidate — and the four other top-10 predictions — is supported by **zero clinical trials and zero publications**, and the evidence pack's own mechanistic analysis flags the prediction as a likely knowledge-graph artifact rather than a genuine therapeutic signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in evidence pack (drug is classified as a HER2-targeted antibody-drug conjugate per mechanistic notes) |
| Predicted New Indication | Drug-Induced Osteoporosis (duplicate entry at rank 1 and 2 — likely deduplication artifact) |
| TxGNN Prediction Score | 99.31% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Trastuzumab deruxtecan (T-DXd) is described in the evidence pack as a HER2-targeted antibody-drug conjugate (ADC), with a payload consisting of a topoisomerase I inhibitor (DXd). No original indication data was provided for this pack, so the traditional "original indication → new indication" mechanistic bridge cannot be constructed with confidence.

More importantly, the evidence pack's own rationale for every one of the top 10 predictions explicitly concludes that **there is no known mechanistic pathway** linking a HER2/topoisomerase-I-targeted ADC to any of the predicted conditions (drug-induced osteoporosis, diabetic retinopathy and its severe subtype, bronchitis, or diabetic cataract). The assessment suggests these high TxGNN scores more likely reflect semantic co-occurrence in the knowledge graph (e.g., shared nodes with bone metastasis, chemotherapy-related tissue damage, or general antibody/oncology clusters) rather than a real treatment hypothesis.

Notably, for several candidates the evidence pack raises a **directionally inverted concern**: T-DXd carries a known class of eye toxicity (corneal/keratopathy signals) and a well-established interstitial lung disease (ILD)/pneumonitis risk. If the knowledge graph associates the drug with eye- or respiratory-related disease nodes (diabetic retinopathy, diabetic cataract, bronchitis), this may reflect the drug's **known adverse-effect profile being misread as a therapeutic signal**, rather than genuine repurposing potential. This is a critical caveat for clinical interpretation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

*(Confirmed by direct queries against ClinicalTrials.gov and ICTRP for all five unique predicted indications — drug-induced osteoporosis, severe nonproliferative diabetic retinopathy, diabetic retinopathy, bronchitis, and diabetic cataract — each returning 0 results.)*

---

## Literature Evidence

Currently no related literature available.

*(Confirmed by direct PubMed queries for all five unique predicted indications, each returning 0 results.)*

---

## Denmark Market Information

No marketing authorisations are currently registered for this product in Denmark (0 licenses on file; market status: Not marketed).

---

## Cytotoxicity

Trastuzumab deruxtecan is an antineoplastic antibody-drug conjugate (HER2-targeted delivery of a cytotoxic topoisomerase I inhibitor payload), so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy — antibody-drug conjugate (ADC) delivering a conventional cytotoxic payload (topoisomerase I inhibitor) |
| Myelosuppression Risk | Please refer to the Summary of Product Characteristics (SmPC) warnings and precautions |
| Emetogenicity Classification | Please refer to the Summary of Product Characteristics (SmPC) warnings and precautions |
| Monitoring Items | Please refer to the Summary of Product Characteristics (SmPC) warnings and precautions |
| Handling Protection | Please refer to the Summary of Product Characteristics (SmPC) warnings and precautions |

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information. No drug interaction records were found in the queried database.

**Note:** Product label warnings and contraindications are flagged as a **Blocking** data gap in this evidence pack (unavailable from the regulatory source), meaning a formal safety pre-assessment cannot yet be completed for this candidate.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- All five unique predicted indications are TxGNN model output only (Evidence Level L5), with zero corroborating clinical trials or literature.
- The evidence pack's own mechanistic review concludes there is no plausible biological rationale for any top-ranked prediction, and warns that some associations may reflect the drug's known toxicity profile (ILD, keratopathy) rather than therapeutic potential.
- Product label safety data (warnings/contraindications) is a Blocking gap, preventing a formal safety pre-assessment.
- The prediction list contains duplicate entries (ranks 1–2, 3–4, 5–6, 7–8, 9–10 are identical pairs), indicating an upstream data-quality issue.

**To proceed, the following is needed:**
- TFDA/SmPC label data (warnings, contraindications) — currently Blocking
- Confirmed mechanism of action (MOA) and original approved indication(s) for this drug
- Deduplication of the predicted_indications dataset at the source
- If any candidate is pursued further, preclinical/mechanistic studies are required before advancing beyond S0, given the complete absence of clinical or literature evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

