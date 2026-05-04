---
layout: default
title: Everolimus
parent: 僅模型預測 (L5)
nav_order: 182
evidence_level: L5
indication_count: 10
---

# Everolimus
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

# Everolimus: From Targeted Anticancer Therapy to Liposarcoma

## One-Sentence Summary

Everolimus is an mTOR inhibitor (mTORC1) used as targeted anticancer therapy in indications such as renal cell carcinoma, breast cancer, and neuroendocrine tumours. The TxGNN model predicts it may be effective for **Liposarcoma**, with **1 clinical trial** and **4 publications** currently supporting this direction. Additional predicted indications include dermatofibrosarcoma protuberans and several rare sarcoma subtypes, though with substantially less evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not registered in Denmark in the evidence pack (Everolimus is known internationally for renal cell carcinoma, HER2− breast cancer, neuroendocrine tumours, TSC-associated conditions) |
| Predicted New Indication | Liposarcoma |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L2 |
| Denmark Market Status | Not marketed (per evidence pack) |
| Number of Marketing Authorisations | 0 (per evidence pack) |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Everolimus is a selective inhibitor of mTORC1 (mammalian target of rapamycin complex 1), a key node in the PI3K/AKT/mTOR signalling cascade that controls cell growth, proliferation, and survival. It is well established as a targeted anticancer agent, approved globally for multiple solid tumour types where mTOR pathway dysregulation plays a central role.

Dedifferentiated liposarcoma (DDLPS) has been demonstrated to harbour overactivation of both the Akt-mTOR and MAPK pathways (PMID: 26518767). An immunohistochemical and in vitro study of 99 DDLPS specimens confirmed that mTOR inhibition exerts antitumour effects in this sarcoma subtype. This provides a direct pharmacological rationale for everolimus in liposarcoma. Furthermore, CDK4 amplification is a hallmark of DDLPS, and the combination of CDK4/6 inhibitors (such as ribociclib) with mTOR inhibitors has shown synergistic growth inhibition in multiple tumour models — blocking parallel proliferative pathways simultaneously.

A Phase II clinical trial (NCT03114527) is actively evaluating the combination of ribociclib and everolimus specifically in advanced dedifferentiated liposarcoma, with 48 patients enrolled. While this is combination therapy rather than everolimus monotherapy, it directly validates the clinical relevance of mTOR inhibition in this disease. The convergence of mechanistic rationale and ongoing clinical investigation makes this a well-supported repurposing prediction.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03114527](https://clinicaltrials.gov/study/NCT03114527) | Phase 2 | Active, not recruiting | 48 | Two-arm study evaluating ribociclib (300 mg/day, 3 weeks on/1 week off) + everolimus (2.5 mg) in advanced dedifferentiated liposarcoma (Arm A) and leiomyosarcoma (Arm B) after ≥1 prior systemic therapy. Completed enrolment; in follow-up/analysis phase. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37967116](https://pubmed.ncbi.nlm.nih.gov/37967116/) | 2024 | Phase II Clinical Trial Report | Clin Cancer Res | Reports results of ribociclib + everolimus combination in advanced DDL and LMS. CDK4/6 + mTOR dual inhibition showed synergistic growth inhibition across multiple tumour models. |
| [26518767](https://pubmed.ncbi.nlm.nih.gov/26518767/) | 2016 | Translational/Mechanistic Study | Tumour Biol | Immunohistochemical analysis of 99 DDLPS specimens confirmed Akt-mTOR and MAPK pathway activation. In vitro study demonstrated antitumour effects of mTOR inhibition in dedifferentiated liposarcoma. |
| [36003796](https://pubmed.ncbi.nlm.nih.gov/36003796/) | 2022 | Review (Preclinical Models) | Front Oncol | Review of patient-derived orthotopic xenograft (PDOX) models identifying effective CDK inhibitor combinations in sarcomas, supporting CDK + mTOR inhibition strategies. |
| [29848686](https://pubmed.ncbi.nlm.nih.gov/29848686/) | 2018 | Preclinical Combination Study | Anticancer Res | Evaluated eribulin combinations with mechanistically different anticancer agents in liposarcoma and other tumour xenograft models, providing context for multi-agent approaches. |

---

## Denmark Market Information

Everolimus currently has no marketing authorisations recorded in the evidence pack for Denmark. However, it should be noted that everolimus is authorised in the EU via centralised EMA procedures (Afinitor®, Certican®/Votubia®) for multiple indications including advanced renal cell carcinoma, HER2-negative breast cancer, pancreatic neuroendocrine tumours, and tuberous sclerosis complex-associated conditions. Clinicians should consult the Danish Medicines Agency (Lægemiddelstyrelsen) for current local availability and reimbursement status.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (mTOR inhibitor, rapamycin analogue) |
| Myelosuppression Risk | Moderate (thrombocytopenia, anaemia, and neutropenia are common; Grade 3/4 events reported in clinical studies) |
| Emetogenicity Classification | Low |
| Monitoring Items | CBC with differential, liver function (ALT, AST, bilirubin), renal function (creatinine, eGFR), fasting glucose, lipid profile, pulmonary function (risk of non-infectious pneumonitis) |
| Handling Protection | Standard precautions for oral anticancer agents; no special cytotoxic handling requirements beyond standard practice for oral targeted therapies |

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information. The evidence pack did not contain specific warnings, contraindications, or drug-drug interaction data for everolimus. Key safety concerns known from the SmPC include:

- **Non-infectious pneumonitis**: Clinically significant; requires monitoring and may necessitate dose adjustment or discontinuation
- **Immunosuppression**: Increased susceptibility to infections (bacterial, fungal, viral including hepatitis B reactivation)
- **Metabolic effects**: Hyperglycaemia, hyperlipidaemia
- **Stomatitis/mucositis**: Very common adverse effect

---

## Additional Predicted Indications

The TxGNN model also predicted the following indications for everolimus, listed by evidence strength:

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Recommendation |
|------|---------------------|-------------|----------------|----------------|
| 1 | Liposarcoma | 99.88% | L2 | Proceed with Guardrails |
| 3 | Ovarian myxoid liposarcoma | 99.84% | L5 | Hold |
| 5 | Dermatofibrosarcoma protuberans | 99.82% | L4 | Research Question |
| 7 | Parameningeal embryonal rhabdomyosarcoma | 99.77% | L5 | Hold |
| 9 | Botryoid-type embryonal rhabdomyosarcoma of the vagina | 99.76% | L5 | Hold |

**Notes:**
- **Dermatofibrosarcoma protuberans (DFSP)**: The core driver is COL1A1-PDGFB fusion gene leading to PDGFR overactivation. mTOR is a downstream effector of PDGFR (PDGFR → PI3K → AKT → mTOR), suggesting potential activity in imatinib-resistant cases. Two translational publications exist (PMID: 37610680, 15921309) but no clinical evidence for everolimus in DFSP.
- **Rhabdomyosarcoma subtypes**: PI3K/AKT/mTOR is known to participate in RMS progression, but no clinical or preclinical evidence specific to everolimus in these rare subtypes was identified. The high TxGNN scores likely reflect shared molecular features across sarcoma types.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The TxGNN prediction of everolimus for liposarcoma is mechanistically well-founded: dedifferentiated liposarcoma demonstrates clear Akt-mTOR pathway activation, and a Phase II clinical trial (NCT03114527) is actively evaluating everolimus in combination with ribociclib in this setting. Published translational evidence directly supports mTOR as a therapeutic target in DDLPS. While the clinical trial uses combination therapy rather than everolimus monotherapy, the evidence collectively supports further investigation.

**To proceed, the following is needed:**
- **Full SmPC safety review**: Obtain the EMA-approved SmPC for Afinitor® to complete the safety assessment (warnings, contraindications, drug interactions)
- **Detailed MOA documentation**: Retrieve comprehensive mechanism of action data from DrugBank to strengthen the pharmacological rationale
- **Denmark market access evaluation**: Confirm current availability, reimbursement status, and any compassionate use pathways via Lægemiddelstyrelsen
- **NCT03114527 results**: Monitor for final results of the Phase II ribociclib + everolimus trial in DDLPS (expected completion December 2025)
- **Monotherapy evidence search**: Conduct a broader literature search for everolimus monotherapy data in soft tissue sarcomas to assess single-agent activity independent of CDK4/6 inhibition

---

*This report is for research purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before application. Report generated: 2026-04-05.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

