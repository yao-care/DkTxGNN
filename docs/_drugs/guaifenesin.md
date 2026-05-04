---
layout: default
title: Guaifenesin
parent: 僅模型預測 (L5)
nav_order: 214
evidence_level: L5
indication_count: 10
---

# Guaifenesin
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

The txgnn-pipeline skill is focused on pipeline operations and doesn't override the report-writing task. I'll proceed directly with generating the evaluation report from the Evidence Pack.

---

# Guaifenesin: From Expectorant / Chest Congestion to Nasal Cavity Disease

## One-Sentence Summary

Guaifenesin is a widely used expectorant, traditionally indicated for relieving chest congestion by thinning and loosening mucus in the airways.
The TxGNN model predicts it may be effective for **Nasal Cavity Disease** (including chronic rhinitis and sinusitis),
with **1 clinical trial** and **2 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Expectorant – relief of chest congestion and productive cough (no formal Danish marketing authorisation on record) |
| Predicted New Indication | Nasal Cavity Disease |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L3 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on widely available pharmacological knowledge, Guaifenesin is a guaiacol glyceryl ether that acts as an expectorant by stimulating serous secretions in the respiratory tract mucosa and reducing mucus viscosity, thereby facilitating mucociliary clearance throughout the airway.

The mechanistic link to nasal cavity disease is biologically plausible. Conditions such as chronic rhinitis and sinusitis are characterised by excessive or abnormally viscous mucus accumulation and impaired mucociliary drainage in the nasal passages. Guaifenesin's ability to increase hydration of respiratory secretions and thin nasal mucus could directly improve nasal mucociliary clearance, reduce congestion, and relieve associated symptoms.

This represents a natural anatomical extension along the unified airway — the same mucosal and serous gland mechanisms that apply in the lower respiratory tract also operate throughout the nasal passages and sinuses. This biological rationale is supported by the existence of a dedicated Phase 2 pilot trial (NCT01364467), which directly tested oral guaifenesin in paediatric chronic rhinitis, confirming that the hypothesis has been considered sufficiently credible to warrant a controlled clinical study.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT01364467](https://clinicaltrials.gov/study/NCT01364467) | Phase 2 | Completed | 30 | 14-day randomised, placebo-controlled, parallel-group pilot trial of oral guaifenesin in children aged 7–18 years with chronic rhinitis (CRS). Primary measures were nasal symptom relief via the SN-5 survey, nasal airway volume, and biophysical properties of nasal secretions. Sample size is small and findings should be interpreted with caution; formal efficacy conclusions cannot be drawn from a pilot study alone. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [9065342](https://pubmed.ncbi.nlm.nih.gov/9065342/) | 1997 | Review / Case Series | American Journal of Rhinology | Management of sinusitis in 22 adult cystic fibrosis patients, including surgical cases. Guaifenesin noted as part of the mucolytic management strategy for chronic sinusitis in this high-complexity population. Low generalisability; disease-specific context limits applicability to general nasal cavity disease. |
| [12487405](https://pubmed.ncbi.nlm.nih.gov/12487405/) | 2002 | Expert Opinion / Narrative Review | Logopedics, Phoniatrics, Vocology | Decongestant combinations with guaifenesin noted as potentially useful in managing upper respiratory allergic conditions affecting the nasal cavity and larynx in professional voice users. Expert opinion only; no controlled data. |

---

## Denmark Market Information

Guaifenesin currently holds **no marketing authorisations** in Denmark (Laegemiddelstyrelsen) and is not marketed. There are no registered products to list.

> **Note:** Guaifenesin is available as an over-the-counter expectorant in numerous other countries (e.g., USA: Mucinex®; various EU combination products). Any Danish market entry would require a new regulatory submission via a national, mutual recognition, or decentralised procedure. EMA centralised authorisation is not applicable for this drug class.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information. Formal Danish regulatory safety documentation (Laegemiddelstyrelsen product labelling, contraindications, and key warnings) was not available for this assessment and constitutes a blocking data gap (DG001) that must be resolved before proceeding to a formal safety evaluation.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic rationale for guaifenesin in nasal cavity disease is biologically coherent and a completed Phase 2 pilot study exists; however, the study enrolled only 30 patients, the supporting literature is limited to tier-3 sources, guaifenesin is not currently marketed in Denmark, and formal safety documentation for the Danish context is unavailable — making this insufficient to advance without additional evidence.

**To proceed, the following is needed:**

- Obtain and review the full results publication for NCT01364467 to assess whether efficacy and safety signals are positive
- Retrieve formal mechanism of action data from DrugBank (resolves DG002)
- Obtain Danish/EMA-equivalent SmPC product information to complete safety and contraindication assessment (resolves DG001 — currently Blocking)
- Assess the regulatory pathway for introducing guaifenesin products in Denmark (national authorisation, mutual recognition, or decentralised procedure)
- If pilot data are positive: design a confirmatory Phase 2/3 randomised controlled trial in chronic rhinitis or sinusitis with adequate sample size before considering a formal indication extension
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

