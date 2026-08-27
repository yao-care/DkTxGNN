---
layout: default
title: Lenvatinib
parent: 僅模型預測 (L5)
nav_order: 260
evidence_level: L5
indication_count: 10
---

# Lenvatinib
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

# Lenvatinib: From Original Indication (Data Not Available) to Liposarcoma

## One-Sentence Summary

Lenvatinib's original approved indication is not documented in this evidence pack (the DrugBank/mechanism-of-action record is incomplete), though it is known to be a multi-target tyrosine kinase inhibitor (TKI) used in oncology. The TxGNN model predicts it may be effective for **Liposarcoma**, with **1 clinical trial** and **4 publications** currently supporting this direction. The drug is not currently marketed in Denmark.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in this evidence pack (DrugBank MOA and indication fields are data gaps) |
| Predicted New Indication | Liposarcoma |
| TxGNN Prediction Score | 99.51% |
| Evidence Level | L2 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in DrugBank for this record. Based on the repurposing rationale supplied with the prediction, Lenvatinib is a multi-targeted tyrosine kinase inhibitor (TKI) acting on VEGFR1-3, FGFR1-4, PDGFRα, KIT and RET — a mechanism class typically applied to angiogenesis-dependent solid tumours.

Liposarcoma is a soft-tissue sarcoma with high dependence on tumour angiogenesis for growth. When combined with eribulin (a microtubule/mitotic inhibitor), lenvatinib's anti-angiogenic activity may produce a synergistic anti-tumour effect — anti-vascular action alongside direct cytotoxic mitotic disruption.

This combination has already been tested directly in the LEADER study (NCT03526679), a completed Phase Ib/II trial in advanced adipocytic sarcoma and leiomyosarcoma (n=30), providing direct clinical evidence rather than mechanism-only extrapolation. Supporting biomarker research on CDK4 in dedifferentiated liposarcoma further strengthens the molecular rationale for combination treatment in this population.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03526679](https://clinicaltrials.gov/study/NCT03526679) | Phase 1/2 | Completed | 30 | Lenvatinib + eribulin in inoperable/metastatic adipocytic sarcoma and leiomyosarcoma; tests combined anti-angiogenic (lenvatinib) and mitotic-targeting (eribulin) activity |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36129471](https://pubmed.ncbi.nlm.nih.gov/36129471/) | 2022 | Phase Ib/II Trial | Clinical Cancer Research | LEADER study (NCT03526679): safety and efficacy of lenvatinib plus eribulin in advanced liposarcoma and leiomyosarcoma |
| [39103896](https://pubmed.ncbi.nlm.nih.gov/39103896/) | 2024 | Preclinical/Biomarker | Experimental Hematology & Oncology | CDK4 as a prognostic biomarker in soft tissue sarcoma; supports rationale for sequential/combination treatment in dedifferentiated liposarcoma |
| [29848686](https://pubmed.ncbi.nlm.nih.gov/29848686/) | 2018 | Preclinical | Anticancer Research | Eribulin combined with mechanistically distinct anticancer agents shows broad-spectrum preclinical antitumour activity |
| [34326745](https://pubmed.ncbi.nlm.nih.gov/34326745/) | 2021 | Case Report | Case Reports in Oncology | Individualized targeted therapy + surgery + chemotherapy achieved tumour size reduction in dedifferentiated liposarcoma with lung metastasis |

---

## Denmark Market Information

Lenvatinib is currently **not marketed in Denmark** — there are no national (Laegemiddelstyrelsen) or centralised (EMA) marketing authorisations on file for this record (0 licenses).

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (multi-target tyrosine kinase inhibitor: VEGFR1-3, FGFR1-4, PDGFRα, KIT, RET) |
| Myelosuppression Risk | Please refer to the Summary of Product Characteristics (SmPC) warnings and precautions |
| Emetogenicity Classification | Please refer to the Summary of Product Characteristics (SmPC) warnings and precautions |
| Monitoring Items | Please refer to the Summary of Product Characteristics (SmPC) warnings and precautions |
| Handling Protection | Please refer to the Summary of Product Characteristics (SmPC) warnings and precautions |

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The strongest evidence — a single completed, small (n=30), single-arm Phase Ib/II trial — supports a credible mechanistic rationale but falls short of registrational-quality evidence for liposarcoma specifically. The drug also currently holds zero marketing authorisations in Denmark, and core MOA/safety data are missing from this evidence pack, making a full risk-benefit assessment premature.

**To proceed, the following is needed:**
- Lenvatinib SmPC (from the relevant EU/EMA authorisation holder) for mechanism of action, warnings, contraindications, and drug interactions
- Confirmation of Danish/EU marketing authorisation status and access pathway
- Larger controlled trial data (Phase 2/3, ideally randomized) in liposarcoma specifically, beyond the single-arm LEADER study
- DDI and myelosuppression/toxicity profile confirmation from DrugBank or SmPC sources
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

