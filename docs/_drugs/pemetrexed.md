---
layout: default
title: Pemetrexed
parent: 僅模型預測 (L5)
nav_order: 342
evidence_level: L5
indication_count: 10
---

# Pemetrexed
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

# Pemetrexed: From Pleural Mesothelioma to Malignant Peritoneal Mesothelioma

## One-Sentence Summary

Pemetrexed is a multitargeted antifolate chemotherapy agent whose antitumour efficacy against malignant pleural mesothelioma is internationally well established (platinum + pemetrexed is a recognised standard first-line regimen).
The TxGNN model predicts it may also be effective for **Malignant Peritoneal Mesothelioma**, an anatomically related but distinct mesothelial malignancy,
with **11 clinical trials** and **20 publications** currently supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on the Danish registry (drug currently not marketed); internationally established for malignant pleural mesothelioma (platinum + pemetrexed first-line regimen) |
| Predicted New Indication | Malignant Peritoneal Mesothelioma |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L2 |
| Denmark Market Status | Not Marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Formal DrugBank mechanism-of-action data could not be retrieved for this candidate (data gap, see below). However, the repurposing evidence itself documents the mechanism clearly: Pemetrexed is a multitargeted antifolate that inhibits thymidylate synthase (TS), dihydrofolate reductase (DHFR), and glycinamide ribonucleotide formyltransferase (GARFT), blocking folate-dependent DNA synthesis. Mesothelioma cells, which proliferate rapidly, are highly dependent on this pathway, which is why pemetrexed plus platinum is already an internationally recognised (including FDA-approved) standard first-line treatment for malignant **pleural** mesothelioma.

Malignant peritoneal mesothelioma and malignant pleural mesothelioma are both malignancies of mesothelial-cell origin, differing essentially only in anatomical site (peritoneum vs. pleura). International treatment guidelines (e.g. NCCN) already list pemetrexed + platinum as a systemic therapy option for peritoneal mesothelioma, which supports the biological plausibility of the TxGNN prediction. That said, a dedicated Phase 3 randomised controlled trial for the peritoneal subtype is still lacking — current evidence is concentrated in Phase 1/2 trials and retrospective/case-series literature, placing this candidate at a moderate (not definitive) evidence strength.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06057935](https://clinicaltrials.gov/study/NCT06057935) | Phase 2 | Recruiting | 64 | Multicenter RCT comparing normothermic intraperitoneal vs. intravenous chemotherapy after cytoreductive surgery + HIPEC for malignant peritoneal mesothelioma. |
| [NCT06543069](https://clinicaltrials.gov/study/NCT06543069) | Phase 2 | Recruiting | 28 | Single-arm study of sintilimab + bevacizumab combined with pemetrexed/cisplatin for unresectable malignant peritoneal mesothelioma. |
| [NCT04462809](https://clinicaltrials.gov/study/NCT04462809) | Phase 2 | Unknown | 40 | Talazoparib maintenance following first-line platinum-based chemotherapy in pleural or peritoneal mesothelioma. |
| [NCT00061477](https://clinicaltrials.gov/study/NCT00061477) | Phase 2 | Completed | 48 | Pemetrexed + gemcitabine as front-line chemotherapy for pleural or peritoneal mesothelioma. |
| [NCT01353482](https://clinicaltrials.gov/study/NCT01353482) | Phase 1/2 | Withdrawn | 0 | Vorinostat + pemetrexed-cisplatin as first-line therapy in malignant pleural mesothelioma (withdrawn prior to enrollment). |
| [NCT05001880](https://clinicaltrials.gov/study/NCT05001880) | Phase 2 | Recruiting | 66 | Randomised trial of carboplatin/pemetrexed/bevacizumab with or without atezolizumab for peritoneal mesothelioma. |
| [NCT00402766](https://clinicaltrials.gov/study/NCT00402766) | Phase 1 | Completed | 19 | Cisplatin + pemetrexed + imatinib mesylate in unresectable/metastatic malignant mesothelioma. |
| [NCT03875144](https://clinicaltrials.gov/study/NCT03875144) | Phase 2 | Suspended | 66 | PIPAC combined with systemic chemotherapy (cisplatin/pemetrexed) vs. systemic chemotherapy alone as first-line treatment of malignant peritoneal mesothelioma. |
| [NCT02535312](https://clinicaltrials.gov/study/NCT02535312) | Phase 1/2 | Active, not recruiting | 30 | TRC102 combined with pemetrexed/cisplatin in advanced solid tumours, including mesothelioma refractory to pemetrexed and platinum. |
| [NCT02029690](https://clinicaltrials.gov/study/NCT02029690) | Phase 1 | Terminated | 85 | ADI-PEG 20 combined with pemetrexed and cisplatin in arginine-dependent tumours, including advanced peritoneal mesothelioma. |

*Note: one additional Phase 1 trial (NCT03564691, a broad advanced-solid-tumour study with only tangential relevance) was excluded from this table to keep the list to the 10 most relevant trials.*

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35407498](https://pubmed.ncbi.nlm.nih.gov/35407498/) | 2022 | Review | Journal of Clinical Medicine | Overview of treatment approaches for malignant peritoneal mesothelioma, including the role of systemic chemotherapy. |
| [31417959](https://pubmed.ncbi.nlm.nih.gov/31417959/) | 2019 | Cohort/Case report | Pleura and Peritoneum | Bidirectional chemotherapy enabling surgical resectability in initially unresectable peritoneal mesothelioma. |
| [28594258](https://pubmed.ncbi.nlm.nih.gov/28594258/) | 2017 | Retrospective study | Expert Review of Anticancer Therapy | Evaluates efficacy of first-line systemic pemetrexed + cisplatin chemotherapy in peritoneal mesothelioma. |
| [31287877](https://pubmed.ncbi.nlm.nih.gov/31287877/) | 2019 | Retrospective study | Japanese Journal of Clinical Oncology | Efficacy and safety of pemetrexed + cisplatin as first-line chemotherapy in advanced peritoneal mesothelioma. |
| [23291819](https://pubmed.ncbi.nlm.nih.gov/23291819/) | 2013 | Case report | BMJ Case Reports | Response to rechallenge with cisplatin and pemetrexed in peritoneal mesothelioma. |
| [41710652](https://pubmed.ncbi.nlm.nih.gov/41710652/) | 2026 | Retrospective study | Frontiers in Oncology | Single-center analysis of chemotherapy with/without bevacizumab after CRS+HIPEC in peritoneal mesothelioma. |
| [34723916](https://pubmed.ncbi.nlm.nih.gov/34723916/) | 2022 | Case report | Journal of Immunotherapy | Chemoimmunotherapy in platinum-nonresponsive metastatic peritoneal mesothelioma (2 patients). |
| [26941986](https://pubmed.ncbi.nlm.nih.gov/26941986/) | 2016 | Review | Journal of Gastrointestinal Oncology | Diagnosis and management overview of malignant peritoneal mesothelioma. |
| [30450291](https://pubmed.ncbi.nlm.nih.gov/30450291/) | 2018 | Review | Translational Lung Cancer Research | Review of peritoneal mesothelioma pathology, prognosis, and treatment options. |
| [38806763](https://pubmed.ncbi.nlm.nih.gov/38806763/) | 2024 | Retrospective multi-center study | Annals of Surgical Oncology | Treatment strategies and outcomes across a multi-center peritoneal mesothelioma cohort. |

## Denmark Market Information

Pemetrexed currently holds **no marketing authorisation on record in Denmark** (market status: Not Marketed; 0 licenses identified). No national (Laegemiddelstyrelsen) or centralised (EMA) authorisation data is available in this evidence pack to summarise in a product table.

## Cytotoxicity

Pemetrexed is a conventional cytotoxic antineoplastic agent (multitargeted antifolate/antimetabolite class), so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic chemotherapy (multitargeted antifolate/antimetabolite) |
| Myelosuppression Risk | Please refer to the Summary of Product Characteristics (SmPC) warnings and precautions |
| Emetogenicity Classification | Please refer to the Summary of Product Characteristics (SmPC) warnings and precautions |
| Monitoring Items | Please refer to the Summary of Product Characteristics (SmPC) warnings and precautions |
| Handling Protection | As a cytotoxic chemotherapy agent, standard cytotoxic drug handling and protective measures apply |

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information. No drug-drug interaction data could be retrieved (DDI query status: not found).

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The TxGNN score is very high (99.99%) and the mechanistic rationale is strong — malignant peritoneal mesothelioma shares the same mesothelial cell origin and antifolate-sensitive proliferative biology as malignant pleural mesothelioma, for which pemetrexed + platinum is already an internationally accepted standard. This is reinforced by 11 clinical trials and consistent literature, but evidence remains at Phase 1/2 and retrospective/case-series level (no peritoneal-specific completed Phase 3 RCT), placing this at evidence level L2 / decision stage S2 rather than a full Go.

**To proceed, the following is needed:**
- Danish-specific SmPC/label safety data (key warnings, contraindications) — currently a **Blocking** data gap preventing initial safety screening (S1)
- Confirmed DrugBank mechanism-of-action record (currently a data gap; mechanism was reconstructed from trial/literature rationale only)
- Clarification of the regulatory pathway, since Pemetrexed has no current Danish marketing authorisation (0 licenses)
- A peritoneal mesothelioma-specific Phase 3 RCT to raise the evidence level beyond L2
- A formal drug-drug interaction (DDI) review, as none could currently be retrieved
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

