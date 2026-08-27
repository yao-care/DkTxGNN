---
layout: default
title: Pegaspargase
parent: 僅模型預測 (L5)
nav_order: 334
evidence_level: L5
indication_count: 10
---

# Pegaspargase
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

# Pegaspargase: From Acute Lymphoblastic Leukemia to Precursor Lymphoblastic Lymphoma/Leukemia

## One-Sentence Summary

Pegaspargase (DrugBank DB00059) is a pegylated asparaginase enzyme therapy long used as a component of multi-agent chemotherapy for acute lymphoblastic leukemia (ALL). The TxGNN model predicts it may be effective for **precursor lymphoblastic lymphoma/leukemia** — a disease spectrum that substantially overlaps with its established use — supported by **50 clinical trials** and **20 publications**, though this appears to largely reaffirm an already-known indication rather than reveal a novel repurposing opportunity.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acute lymphoblastic leukemia (component of multi-agent chemotherapy) — not documented in Danish licensing data, as the drug is not currently marketed in Denmark |
| Predicted New Indication | Precursor lymphoblastic lymphoma/leukemia |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L1 |
| Denmark Market Status | Not Marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (DrugBank MOA query pending). Based on known pharmacological information, pegaspargase is a PEGylated form of *E. coli*-derived L-asparaginase, an enzyme-based antineoplastic that depletes circulating asparagine — an amino acid that leukemic lymphoblasts cannot synthesize themselves, leading to selective protein-synthesis inhibition and cell death in asparagine-dependent malignant cells.

Precursor lymphoblastic lymphoma/leukemia (encompassing B-ALL, B-lymphoblastic lymphoma, and T-ALL/T-lymphoblastic lymphoma) is generally regarded as the same underlying disease biology as acute lymphoblastic leukemia, differing mainly by the degree of marrow versus extramedullary/nodal involvement at diagnosis. Because asparaginase's cytotoxic mechanism targets the shared metabolic vulnerability of lymphoblasts regardless of whether disease presents as leukemia or lymphoma, the mechanistic rationale for this "prediction" is strong.

It should be noted, however, that this is not a novel repurposing signal in the conventional sense: pegaspargase (marketed elsewhere as Oncaspar®) is already an established, guideline-standard component of ALL/lymphoblastic lymphoma induction and consolidation regimens internationally. The high TxGNN score most likely reflects the model correctly recovering a known, well-validated drug-disease relationship rather than surfacing a new therapeutic hypothesis. The practical value here lies in confirming Denmark's current lack of market access to a globally standard-of-care agent for this disease.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00671034](https://clinicaltrials.gov/study/NCT00671034) | Phase 3 | Completed | 166 | Randomized comparison of calaspargase pegol vs. pegaspargase combined with chemotherapy in newly diagnosed high-risk ALL |
| [NCT01117441](https://clinicaltrials.gov/study/NCT01117441) | Phase 3 | Completed | 6,136 | International collaborative protocol comparing combination chemotherapy regimens incorporating PEG-asparaginase in children/adolescents with ALL |
| [NCT00819351](https://clinicaltrials.gov/study/NCT00819351) | Phase 3 | Completed | 650 | NOPHO protocol: intermittent vs. continuous PEG-asparaginase dosing for asparagine depletion in pediatric/young adult ALL |
| [NCT00549848](https://clinicaltrials.gov/study/NCT00549848) | Phase 3 | Completed | 600 | Total Therapy XVI: high-dose vs. conventional-dose PEG-asparaginase during continuation therapy in ALL |
| [NCT02393859](https://clinicaltrials.gov/study/NCT02393859) | Phase 3 | Completed | 111 | Blinatumomab consolidation vs. conventional chemotherapy (incl. pegaspargase) in pediatric high-risk relapsed B-precursor ALL |
| [NCT01190930](https://clinicaltrials.gov/study/NCT01190930) | Phase 3 | Active, not recruiting | 9,350 | Risk-adapted chemotherapy regimens in newly diagnosed standard-risk B-ALL or localized B-lymphoblastic lymphoma |
| [NCT02003222](https://clinicaltrials.gov/study/NCT02003222) | Phase 3 | Active, not recruiting | 488 | Blinatumomab plus chemotherapy (pegaspargase-containing) vs. induction chemotherapy alone in newly diagnosed BCR-ABL-negative B-ALL |
| [NCT03914625](https://clinicaltrials.gov/study/NCT03914625) | Phase 3 | Active, not recruiting | 6,720 | Blinatumomab combined with chemotherapy including pegaspargase for standard-risk B-ALL/B-lymphoblastic lymphoma |
| [NCT02716233](https://clinicaltrials.gov/study/NCT02716233) | Phase 3 | Active, not recruiting | 2,044 | French national protocol optimizing L-asparaginase use in pediatric/adolescent ALL |
| [NCT03959085](https://clinicaltrials.gov/study/NCT03959085) | Phase 3 | Recruiting | 5,951 | Inotuzumab ozogamicin added to pegaspargase-containing post-induction therapy for high-risk B-ALL |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34228505](https://pubmed.ncbi.nlm.nih.gov/34228505/) | 2021 | Clinical Trial (DFCI 11-001) | Journal of Clinical Oncology | Efficacy and toxicity of pegaspargase vs. calaspargase pegol in childhood ALL |
| [37276451](https://pubmed.ncbi.nlm.nih.gov/37276451/) | 2023 | Clinical Trial (GIMEMA LAL1913) | Blood Advances | Pegaspargase-modified risk-oriented program improves outcomes in adult Ph-negative ALL/lymphoblastic lymphoma |
| [21454191](https://pubmed.ncbi.nlm.nih.gov/21454191/) | 2011 | Clinical Trial | Clinical Lymphoma, Myeloma & Leukemia | Augmented hyper-CVAD with intensified pegaspargase dosing improves salvage therapy outcomes in adult relapsed ALL |
| [27114587](https://pubmed.ncbi.nlm.nih.gov/27114587/) | 2016 | Clinical Trial (COG AALL0232) | Journal of Clinical Oncology | Dexamethasone and high-dose methotrexate improve outcomes in high-risk B-ALL |
| [40163215](https://pubmed.ncbi.nlm.nih.gov/40163215/) | 2025 | Clinical Trial (Phase 2) | International Journal of Hematology | Efficacy, safety, and pharmacokinetics of lyophilized pegaspargase in previously untreated ALL |
| [40109190](https://pubmed.ncbi.nlm.nih.gov/40109190/) | 2025 | Expert Consensus | Haematologica | Panel consensus on recognition, prevention, and management of asparaginase/pegaspargase-associated adverse events in adults |
| [31030380](https://pubmed.ncbi.nlm.nih.gov/31030380/) | 2019 | Review | Drugs | Comprehensive review of pegaspargase in acute lymphoblastic leukaemia |
| [31977001](https://pubmed.ncbi.nlm.nih.gov/31977001/) | 2020 | Review ("How I treat") | Blood | Practical guidance on managing pegaspargase toxicities in adult ALL |
| [17696798](https://pubmed.ncbi.nlm.nih.gov/17696798/) | 2007 | Review | Expert Opinion on Pharmacotherapy | Pharmacology and clinical role of PEG-asparaginase in acute leukemia |
| [9161659](https://pubmed.ncbi.nlm.nih.gov/9161659/) | 1997 | Review | The Annals of Pharmacotherapy | Early review of pegaspargase chemistry, pharmacology, and clinical activity |

## Denmark Market Information

Pegaspargase is **not currently marketed in Denmark** — no Marketing Authorisations (national Laegemiddelstyrelsen or centralised EMA) are recorded in the available regulatory data.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic — enzyme-depleting antineoplastic (L-asparaginase class), mechanistically distinct from DNA-damaging cytotoxics but administered within standard cytotoxic chemotherapy protocols |
| Myelosuppression Risk | Low to moderate as a standalone agent — asparaginase's primary dose-limiting toxicities are hypersensitivity, hepatotoxicity, pancreatitis, coagulopathy/thrombosis, and hyperglycemia rather than direct marrow suppression; myelosuppression risk is compounded when combined with other agents in standard multi-drug ALL regimens (per PMID 40109190, 31977001) |
| Emetogenicity Classification | Low to moderate |
| Monitoring Items | CBC with differential, liver function (ALT/AST/bilirubin/albumin), coagulation parameters (fibrinogen, antithrombin), lipase/amylase (pancreatitis risk), fasting glucose, triglycerides |
| Handling Protection | Requires standard cytotoxic/antineoplastic drug handling precautions (PPE, closed-system reconstitution, designated disposal) per institutional hazardous drug handling regulations |

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information — key warnings, contraindications, and drug interaction data were not available in the structured safety dataset for this drug.

*Supplementary note:* Literature evidence independently documents a well-characterized adverse event profile for pegaspargase, including hypersensitivity reactions, hepatotoxicity, pancreatitis, thrombosis/coagulopathy, and hyperglycemia (PMID 40109190, 31977001) — these should inform SmPC review once obtained.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The clinical trial and literature evidence base for pegaspargase in precursor lymphoblastic lymphoma/leukemia is strong (L1 — multiple completed Phase 3 RCTs), reflecting its already-established role in ALL treatment globally. However, a **Blocking** data gap (missing TFDA/SmPC warnings and contraindications) prevents completion of the mandatory S1 safety pre-assessment, and the drug currently holds zero Marketing Authorisations in Denmark.

**To proceed, the following is needed:**
- Official SmPC / product label with warnings, contraindications, and drug interaction data (currently blocking)
- Confirmed mechanism-of-action documentation from DrugBank
- Drug-drug interaction (DDI) data (current query returned no results)
- Regulatory pathway assessment for Danish market entry or named-patient/compassionate access, given the drug is not currently authorised in Denmark
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

