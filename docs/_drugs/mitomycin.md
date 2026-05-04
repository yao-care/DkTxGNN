---
layout: default
title: Mitomycin
parent: 僅模型預測 (L5)
nav_order: 241
evidence_level: L5
indication_count: 10
---

# Mitomycin
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

# Mitomycin: From Solid Tumours to Osteoclastic Giant Cell Tumour of Pancreas

## One-Sentence Summary

Mitomycin (DB00305) is a cytotoxic antibiotic with established antineoplastic activity, historically used as part of combination chemotherapy regimens for gastric cancer, bladder cancer, and other solid tumours, though no approved indication data is available from Danish regulatory records.
The TxGNN model predicts it may be effective for **Osteoclastic Giant Cell Tumour of Pancreas**, an exceptionally rare pancreatic malignancy accounting for less than 1% of all pancreatic cancers.
There are currently **0 clinical trials** and **0 publications** specifically supporting this indication, placing the evidence at **Level L5** (model prediction only).

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No approved indication data available (not registered in Denmark) |
| Predicted New Indication | Osteoclastic Giant Cell Tumour of Pancreas |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L5 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this dataset. Based on known pharmacological information, Mitomycin C is a cytotoxic alkylating antibiotic derived from *Streptomyces caespitosus*. It acts as a DNA cross-linking agent — forming covalent interstrand crosslinks that inhibit DNA replication and transcription, ultimately triggering cell death preferentially in rapidly dividing tumour cells. Tumours with defects in DNA damage repair pathways (e.g., BRCA2 mutations) are theoretically more susceptible to this class of agent.

Osteoclastic giant cell tumour of the pancreas is an extremely rare biphasic neoplasm characterised by pleomorphic mononuclear neoplastic cells intermingled with non-neoplastic osteoclast-like giant cells. The theoretical basis for Mitomycin activity rests on the sensitivity of the pancreatic tumour cell component to DNA cross-linking, analogous to mechanisms exploited in other gastrointestinal malignancies. Historically, Mitomycin featured in the FAM regimen (5-FU + Adriamycin + Mitomycin) for gastric and pancreatic adenocarcinoma, providing an indirect mechanistic link to pancreatic cancer biology.

However, the biological behaviour of osteoclastic giant cell tumour differs substantially from conventional pancreatic adenocarcinoma, and no clinical or preclinical evidence currently exists for Mitomycin in this specific subtype. The high TxGNN score likely reflects generalised pancreatic tumour node connectivity within the knowledge graph rather than subtype-specific biological evidence. This prediction should be treated as a starting hypothesis only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Cytotoxicity

Mitomycin meets the criteria for the antineoplastic classification: it is a conventional cytotoxic chemotherapy agent belonging to the alkylating antibiotic class.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — Alkylating antibiotic (Mitomycin class) |
| Myelosuppression Risk | High — cumulative and characteristically delayed; nadir typically at 3–5 weeks post-dose; thrombocytopenia and leucopenia are the principal dose-limiting toxicities |
| Emetogenicity Classification | Low to moderate |
| Monitoring Items | Full blood count with differential (CBC-diff) and platelet count at frequent intervals; renal function (eGFR, serum creatinine); pulmonary function assessment with cumulative dosing (risk of Mitomycin-associated pulmonary fibrosis and bronchospasm) |
| Handling Protection | Must comply with cytotoxic drug handling regulations; preparation requires a Class II biological safety cabinet; personnel must use appropriate PPE including gloves, gown, and eye protection |

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN prediction score (99.86%), osteoclastic giant cell tumour of the pancreas is an exceptionally rare malignancy for which there is a complete absence of clinical trials, published literature, and direct mechanistic evidence supporting Mitomycin use; an L5 evidence level is insufficient to advance beyond a theoretical research question.

**To proceed, the following is needed:**

- Mechanism of action data (MOA) from DrugBank or primary pharmacological literature, with particular focus on Mitomycin activity in pancreatic tumour models
- Broader systematic literature review covering Mitomycin use across all pancreatic cancer subtypes (not restricted to the osteoclastic subtype) to establish an indirect evidence base
- Case report or case series data specifically documenting chemotherapy outcomes in osteoclastic giant cell tumour of the pancreas
- Preclinical data (in vitro cell line or in vivo xenograft) demonstrating Mitomycin activity in an osteoclastic giant cell tumour model
- Full safety and contraindication data retrieved from an approved SmPC (e.g., EMA or national authority) before any clinical application is considered
- Assessment of Danish regulatory pathway (Laegemiddelstyrelsen / EMA) if development in this indication is ultimately pursued

---

> ⚠️ **Disclaimer:** This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

