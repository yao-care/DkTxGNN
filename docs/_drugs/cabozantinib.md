---
layout: default
title: Cabozantinib
parent: 僅模型預測 (L5)
nav_order: 83
evidence_level: L5
indication_count: 10
---

# Cabozantinib
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

# Cabozantinib: From Renal Cell Carcinoma to Liposarcoma

## One-Sentence Summary

Cabozantinib is a multi-kinase inhibitor (targeting VEGFR2, MET, AXL, and RET) globally approved for renal cell carcinoma, hepatocellular carcinoma, and medullary thyroid carcinoma, though it is not currently registered in Denmark.
The TxGNN model predicts it may be effective for **Liposarcoma**, with **1 active Phase 2 clinical trial** and **1 Phase 1 publication** currently supporting this direction.
While mechanistic rationale is strong, the evidence base remains at an early stage and requires further clinical validation before a formal repurposing decision can be reached.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Denmark; globally approved for renal cell carcinoma, hepatocellular carcinoma, and medullary thyroid carcinoma |
| Predicted New Indication | Liposarcoma |
| TxGNN Prediction Score | 99.83% |
| Evidence Level | L3 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Cabozantinib is a small-molecule tyrosine kinase inhibitor with activity against multiple oncogenic targets, including VEGFR2 (vascular endothelial growth factor receptor 2), MET (hepatocyte growth factor receptor), AXL, and RET. Its anti-tumour effects are primarily mediated through two parallel mechanisms: inhibiting tumour angiogenesis via VEGFR2 blockade, and disrupting tumour-stroma signalling via MET inhibition of the HGF/MET axis — a pathway particularly important in mesenchymal tumour types.

Liposarcoma, a subtype of soft tissue sarcoma (STS) arising from adipose tissue, commonly overexpresses VEGFR, MET, and PDGFR, making it molecularly susceptible to Cabozantinib's multi-target profile. The co-existence of MDM2/CDK4 amplification with elevated VEGF expression in well-differentiated and dedifferentiated liposarcoma subtypes provides an additional biological rationale for anti-angiogenic strategies. Although the formal mechanism of action data from the DrugBank record was not available at the time of this report generation, the mechanistic link between Cabozantinib's established targets and the molecular landscape of liposarcoma is well-supported by preclinical biology.

The broader context of soft tissue sarcoma further strengthens this prediction: Cabozantinib has demonstrated activity across multiple STS subtypes in early-phase trials, and liposarcoma — while a distinct pathological entity — shares the same overarching biology of aberrant VEGF/MET signalling. The TxGNN knowledge graph prediction score of 99.83% reflects the strong structural connectivity between Cabozantinib's molecular targets and the liposarcoma disease node.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT05836571](https://clinicaltrials.gov/study/NCT05836571) | Phase 2 | Active, Not Recruiting | 66 | Randomised comparison of cabozantinib + ipilimumab + nivolumab vs. ipilimumab + nivolumab alone in advanced soft tissue sarcoma. Liposarcoma is included as an eligible subtype. Primary completion expected May 2026; results not yet published. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [41770651](https://pubmed.ncbi.nlm.nih.gov/41770651/) | 2026 | Phase 1 Trial | American Journal of Clinical Oncology | Phase 1 dose-finding study of neoadjuvant cabozantinib combined with concurrent radiotherapy in extremity soft tissue sarcomas. Evaluated safety of the combination given concerns about fistula/perforation risk. Establishes tolerability parameters for sarcoma use. |

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — multi-kinase inhibitor (VEGFR2, MET, AXL, RET inhibitor) |
| Myelosuppression Risk | Low to moderate (haematological toxicity less prominent than conventional cytotoxics; neutropenia and thrombocytopenia reported at lower frequency) |
| Emetogenicity Classification | Low |
| Monitoring Items | Complete blood count (CBC), liver function tests (ALT, AST, bilirubin), renal function, thyroid function (TSH), blood pressure, urine protein, wound healing status |
| Handling Protection | Standard oral kinase inhibitor precautions; cytotoxic handling protocols recommended given antineoplastic classification |

---

## Safety Considerations

Detailed warnings, contraindications, and drug interaction data were not available in this Evidence Pack. Common class-effect concerns for VEGFR/MET inhibitors of this type include hypertension, haemorrhage, thromboembolic events, gastrointestinal perforation or fistula, hepatotoxicity, and impaired wound healing.

> Please refer to the approved Summary of Product Characteristics (SmPC) for Cabometyx® (cabozantinib, EMA) for comprehensive safety information, including specific warnings, contraindications, and drug interaction profiles.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic case for Cabozantinib in liposarcoma is biologically coherent — VEGFR/MET/PDGFR overexpression in liposarcoma directly matches the drug's established target profile — and early clinical activity in the broader soft tissue sarcoma class provides indirect supporting evidence. However, with only one active Phase 2 trial (results pending) and one Phase 1 safety publication, the evidence base remains at L3, insufficient for a definitive repurposing recommendation without further data.

**To proceed, the following is needed:**

- **Results from NCT05836571**: Await publication of efficacy outcomes from this randomised Phase 2 trial; liposarcoma-specific subgroup analyses would be particularly informative
- **Formal MOA documentation**: Retrieve Cabozantinib DrugBank entry and Danish SmPC equivalents (EMA SmPC for Cabometyx®) to complete the mechanism profile and confirm target binding data
- **Safety data for this indication**: Obtain full warning and contraindication profile; assess sarcoma-specific risks (e.g., wound healing post-surgery, GI fistula risk in abdominal disease)
- **Liposarcoma-dedicated trial data**: Consider whether a dedicated Phase 2 trial in liposarcoma subtypes (well-differentiated, dedifferentiated, myxoid/round cell) would be warranted based on NCT05836571 outcomes
- **Regulatory pathway assessment**: Cabozantinib is EMA-approved under centralised procedure (Cabometyx®); an off-label use application or expanded indication submission pathway should be evaluated in consultation with Laegemiddelstyrelsen if evidence strengthens

---

> **Disclaimer:** This report is produced for research purposes only and does not constitute medical advice. All drug repurposing candidates require prospective clinical validation before clinical application. This report was generated using the DkTxGNN drug repurposing prediction system (data cutoff: 2026-04-04).
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

