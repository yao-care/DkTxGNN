---
layout: default
title: Olodaterol
parent: 僅模型預測 (L5)
nav_order: 320
evidence_level: L5
indication_count: 4
---

# Olodaterol
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

# Olodaterol: From COPD to Bronchitis

## One-Sentence Summary

Olodaterol is a long-acting β2-adrenergic agonist (LABA) already established, per the supporting literature in this evidence pack, as a once-daily maintenance bronchodilator for Chronic Obstructive Pulmonary Disease (COPD). The TxGNN model additionally predicts efficacy for **Bronchitis**, currently supported by **3 clinical trials** and **2 publications** — with a closely related "Obstructive Lung Disease" prediction (same drug, overlapping mechanism) backed by substantially stronger evidence (50+ trials, including multiple completed Phase 3 RCTs).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic Obstructive Pulmonary Disease (COPD) — established via literature evidence in this pack; no Danish label data available |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L3 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for olodaterol is not available in this evidence pack (a High-severity data gap). Based on the supporting literature retrieved, olodaterol is a once-daily inhaled long-acting β2-adrenoceptor agonist (LABA) that relaxes bronchial smooth muscle via β2-receptor stimulation, and its efficacy as a maintenance bronchodilator in COPD has been established (e.g., PMID 25773742, 31119643, 27354040).

Bronchitis — particularly chronic bronchitis — is clinically a component phenotype of COPD rather than a distinct disease category, so the mechanistic rationale for extending olodaterol's use is strong: the same airway smooth-muscle relaxation and bronchodilation that benefits COPD patients directly addresses the airflow obstruction and bronchial inflammation seen in bronchitis. This is corroborated by the supporting trials themselves, several of which explicitly enrolled patients with "COPD (Chronic Bronchitis, Emphysema)" (e.g., NCT02850978).

Notably, the evidence pack also contains a second, closely related predicted indication — "Obstructive Lung Disease" — for the same drug, supported by over 50 clinical trials including multiple completed Phase 3 RCTs (e.g., TONADO 1/2, DYNAGITO). This much larger evidence base reinforces the mechanistic plausibility of the bronchitis prediction, though the bronchitis-specific evidence itself remains limited to observational/post-marketing studies.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05127304](https://clinicaltrials.gov/study/NCT05127304) | N/A (observational) | Completed | 11,316 | Compared healthcare resource utilization and clinical outcomes of Tiotropium/Olodaterol vs. Fluticasone Furoate/Umeclidinium/Vilanterol in COPD patients |
| [NCT03333018](https://clinicaltrials.gov/study/NCT03333018) | N/A (observational) | Completed | 22,155 | Post-authorisation drug utilisation study describing patterns of use of aclidinium (mono/combination) vs. other COPD medications, including off-label use assessment |
| [NCT02850978](https://clinicaltrials.gov/study/NCT02850978) | N/A (observational) | Completed | 1,335 | Long-term post-marketing surveillance of Tiotropium+Olodaterol FDC (Spiolto) in Japanese patients with COPD, including chronic bronchitis and emphysema |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27354040](https://pubmed.ncbi.nlm.nih.gov/27354040/) | 2016 | Review | American Journal of Health-System Pharmacy | Reviews pharmacology, pharmacokinetics, efficacy, and safety of once-daily LABA olodaterol |
| [25515181](https://pubmed.ncbi.nlm.nih.gov/25515181/) | 2015 | Guideline/Review | Basic & Clinical Pharmacology & Toxicology | Finnish national COPD guideline covering diagnosis, assessment, and pharmacotherapy of stable COPD |

---

## Denmark Market Information

Olodaterol is currently **not marketed** in Denmark, and no marketing authorisations (national Laegemiddelstyrelsen or centralised EMA) are on record in this evidence pack.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information. (Note: this evidence pack flags TFDA label warnings/contraindications as a **Blocking** data gap, meaning safety data is currently insufficient for an S1 safety pre-assessment.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The bronchitis-specific evidence (predicted_indications[0]) is limited to 3 observational/post-marketing studies and 2 non-RCT publications (Evidence Level L3), and olodaterol is not currently marketed in Denmark.
- A Blocking data gap exists for TFDA/SmPC warnings and contraindications, which prevents any safety pre-assessment (S1) from proceeding.

**To proceed, the following is needed:**
- Approved SmPC / product label with warnings, contraindications, and drug interaction data
- Confirmed mechanism of action documentation (currently a data gap)
- Consideration of whether "Obstructive Lung Disease" (the closely related prediction with 50+ trials and multiple completed Phase 3 RCTs) should be evaluated as the primary repurposing target instead of bronchitis specifically
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

