---
layout: default
title: Busulfan
parent: 僅模型預測 (L5)
nav_order: 80
evidence_level: L5
indication_count: 10
---

# Busulfan
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

# Busulfan: From Myeloid Leukaemia to Myelodysplastic Syndrome

## One-Sentence Summary

Busulfan is a bifunctional alkylating agent historically used in the treatment of myeloid leukaemias and as a myeloablative/reduced-intensity conditioning agent prior to allogeneic haematopoietic stem cell transplantation (allo-HSCT).
The TxGNN model predicts it may be effective for **Myelodysplastic Syndrome (MDS)**, with **over 50 clinical trials** and **20 publications** — including multiple completed Phase 3 randomised controlled trials — currently supporting this direction.
The evidence base is exceptionally strong (Evidence Level L1), reflecting that Busulfan-based conditioning is already a well-established standard-of-care component for MDS patients undergoing allo-HSCT.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Myeloid leukaemias; myeloablative/reduced-intensity conditioning for allo-HSCT (no national registration in Denmark) |
| Predicted New Indication | Myelodysplastic Syndrome (MDS) |
| TxGNN Prediction Score | 99.62% |
| Evidence Level | L1 |
| Denmark Market Status | Not marketed (no national registration with Lægemiddelstyrelsen) |
| Number of Marketing Authorisations | 0 (national); EMA centralised authorisation exists — verify current status at ema.europa.eu |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack. Based on established pharmacology, Busulfan is a bifunctional alkylating agent of the alkylsulfonate class. It covalently alkylates and cross-links DNA strands at the N-7 position of guanine, causing DNA strand breaks and replication arrest that lead to apoptosis in rapidly dividing cells. This effect is particularly pronounced in haematopoietic progenitor cells, giving Busulfan its characteristic profound myeloablative and cytoreductive properties.

In MDS, the bone marrow is populated by dysplastic and clonal haematopoietic stem cells that progressively displace normal haematopoiesis. Allogeneic HSCT is the only potentially curative treatment for eligible higher-risk MDS patients. Busulfan-based conditioning regimens — most notably BuFlu (Busulfan + Fludarabine), BuCy (Busulfan + Cyclophosphamide), and BuMelFlu (Busulfan + Melphalan + Fludarabine) — achieve two critical objectives simultaneously: myeloablation of the recipient's diseased marrow including the MDS clone, and immunosuppression sufficient to prevent graft rejection, enabling donor haematopoietic stem cells to engraft and reconstitute normal haematopoiesis.

The mechanistic rationale for Busulfan in MDS is therefore directly and strongly aligned with the disease pathophysiology, particularly for high-risk subtypes such as RAEB-1 and RAEB-2. Multiple Phase 3 randomised trials have confirmed the clinical efficacy of Busulfan-containing conditioning regimens in MDS patients undergoing allo-HSCT, and the BuFlu regimen is considered a standard-of-care option in international transplant guidelines. The TxGNN prediction score of 99.62% accurately reflects the depth of existing clinical evidence.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT04713956](https://clinicaltrials.gov/study/NCT04713956) | Phase 2/3 | Unknown | 242 | Prospective comparison of G-CSF+DAC+BUCY vs G-CSF+DAC+BF (both Busulfan-containing) conditioning for RAEB-1, RAEB-2 and AML secondary to MDS undergoing allo-HSCT; directly evaluates two Busulfan regimens in the MDS target population |
| [NCT00469144](https://clinicaltrials.gov/study/NCT00469144) | Phase 3 | Completed | 233 | Randomised Phase 3 trial comparing PK-guided once-daily IV Busulfan+Fludarabine vs fixed-dose BuFlu prior to allo-HSCT for AML/MDS; assessed whether blood-level-adjusted dosing improves efficacy and reduces toxicity |
| [NCT00582933](https://clinicaltrials.gov/study/NCT00582933) | Phase 2 | Completed | 96 | IV Busulfan (Busulfex)+Melphalan+Fludarabine as chemotherapy-only myeloablative conditioning prior to T-cell depleted allo-HSCT; MDS was a primary indication; demonstrated feasibility of irradiation-free engraftment |
| [NCT00502905](https://clinicaltrials.gov/study/NCT00502905) | Phase 2 | Completed | 200 | AUC-targeted high-dose IV Busulfan (~6,500 µMol-min/day × 4 days)+Fludarabine for allo-HSCT in AML/MDS; established pharmacokinetic-directed Busulfan dosing methodology |
| [NCT00863148](https://clinicaltrials.gov/study/NCT00863148) | Phase 2 | Completed | 30 | Clofarabine+IV Busulfan+Thymoglobulin (CBT) reduced-intensity conditioning for high-risk AML, MDS or ALL; evaluated whether clofarabine can replace fludarabine in Busulfan-based regimens without additional toxicity |
| [NCT00521430](https://clinicaltrials.gov/study/NCT00521430) | NA | Completed | 30 | Non-T-cell depleted HLA-haploidentical HSCT after reduced-intensity conditioning including Busulfan; MDS was included as an indication; Phase NA design limits evidence grading |
| [NCT01707004](https://clinicaltrials.gov/study/NCT01707004) | Phase 2 | Completed | 20 | Decitabine bridging followed by bone marrow transplant and high-dose cyclophosphamide for relapsed/refractory MDS and AML; Busulfan incorporated into the conditioning backbone |
| [NCT00997386](https://clinicaltrials.gov/study/NCT00997386) | Phase 2 | Completed | 16 | Reduced-intensity allo-PBSCT with Busulfan+Melphalan+Alemtuzumab (Campath) for haematological malignancies including MDS; assessed graft acceptance and donor chimerism at reduced intensity |
| [NCT00357565](https://clinicaltrials.gov/study/NCT00357565) | Phase 2 | Completed | 34 | Busulfan+Fludarabine+Melphalan conditioning prior to umbilical cord blood transplantation in infant leukaemia and MDS; provided paediatric-specific HSCT conditioning data |
| [NCT03579875](https://clinicaltrials.gov/study/NCT03579875) | Phase 2 | Recruiting | 48 | TCRαβ/CD19-depleted PBSC transplantation for inherited bone marrow failure disorders; Busulfan as conditioning backbone; aims to eliminate routine GVHD immunosuppression and accelerate immune reconstitution |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [36702138](https://pubmed.ncbi.nlm.nih.gov/36702138/) | 2023 | Phase 3 RCT | The Lancet Haematology | Multicentre Phase 3 RCT (n=202): G-CSF+Decitabine+BuCy vs standard BuCy conditioning for MDS-RAEB or secondary AML undergoing allo-HSCT; augmented regimen significantly reduced relapse rate without increasing non-relapse mortality |
| [31606445](https://pubmed.ncbi.nlm.nih.gov/31606445/) | 2020 | Phase 3 RCT | The Lancet Haematology | MC-FludT.14/L Phase 3 trial (n=476): Treosulfan+Fludarabine vs RIC Busulfan+Fludarabine for older/comorbid AML/MDS patients before allo-HSCT; Treosulfan met non-inferiority criteria with a more favourable toxicity profile |
| [35617104](https://pubmed.ncbi.nlm.nih.gov/35617104/) | 2022 | Phase 3 RCT (Final Analysis) | American Journal of Hematology | Final analysis of MC-FludT.14/L (n=476): confirmed statistically superior event-free survival with treosulfan-based conditioning over RIC Busulfan+Fludarabine in older/comorbid AML/MDS patients |
| [28380315](https://pubmed.ncbi.nlm.nih.gov/28380315/) | 2017 | Phase 3 RCT | Journal of Clinical Oncology | BMT CTN 0901 trial: myeloablative conditioning (MAC, including Busulfan regimens) vs reduced-intensity conditioning for AML/MDS; no significant OS difference overall, but MAC associated with lower relapse rates |
| [33425740](https://pubmed.ncbi.nlm.nih.gov/33425740/) | 2020 | Systematic Review & Meta-Analysis | Frontiers in Oncology | Systematic review and meta-analysis comparing treosulfan vs Busulfan-based conditioning for AML/MDS allo-HCT; Busulfan served as the primary reference standard comparator across all included studies |
| [38648898](https://pubmed.ncbi.nlm.nih.gov/38648898/) | 2024 | Propensity Score-Matched Cohort | Transplantation and Cellular Therapy | Single-centre PSM cohort (n=138 MDS/CMML patients, Princess Margaret Hospital, Toronto) comparing treosulfan vs Busulfan-based conditioning; provided direct real-world comparative effectiveness data in a dedicated MDS population |
| [40079242](https://pubmed.ncbi.nlm.nih.gov/40079242/) | 2025 | Review | American Journal of Hematology | Contemporary review of allo-HSCT for MDS and myelofibrosis; discusses patient selection, timing, conditioning regimen choice (including Busulfan-based options), and the emerging role of genomic profiling in transplant decision-making |
| [34489555](https://pubmed.ncbi.nlm.nih.gov/34489555/) | 2021 | Retrospective Registry Cohort | Bone Marrow Transplantation | Japanese nationwide registry analysis (2006–2018) comparing Flu/Bu4 vs Bu4/Cy myeloablative conditioning for adult MDS undergoing allo-HSCT; both Busulfan-backbone regimens achieved comparable overall survival |
| [37579918](https://pubmed.ncbi.nlm.nih.gov/37579918/) | 2023 | Prospective Cohort | Transplantation and Cellular Therapy | Prospective cohort demonstrating that myeloablative Busulfan+Fludarabine with in vivo T-cell depletion is safe and effective for AML/MDS patients beyond the traditional age cut-off of 55 years, expanding the eligible conditioning population |
| [33471943](https://pubmed.ncbi.nlm.nih.gov/33471943/) | 2021 | Retrospective Cohort | Cancer | Fractionated myeloablative IV Busulfan conditioning significantly improves survival in older AML/MDS patients compared to standard non-fractionated lower-dose regimens, without increasing non-relapse mortality |

---

## Denmark Market Information

Busulfan has no national marketing authorisations registered with the Danish Medicines Agency (Lægemiddelstyrelsen); the evidence pack reports market status as not marketed with zero national licences. However, **Busulfan (Busilvex, IV formulation, Pierre Fabre Médicament) holds a centralised EMA marketing authorisation** valid across all EU/EEA member states including Denmark. Clinicians and hospital pharmacists should verify the current EMA product status, indication wording, and national reimbursement conditions prior to procurement.

| National MA (Lægemiddelstyrelsen) | Product Name | Dosage Form | Approved Indication |
|----------------------------------|-------------|-------------|---------------------|
| None registered | — | — | — |

> **Note:** Verify EMA centralised marketing authorisation status and full SmPC at [ema.europa.eu](https://www.ema.europa.eu) before clinical use. Oral busulfan (Myleran) and intravenous busulfan (Busilvex) are distinct formulations; IV Busilvex is the preferred preparation for HSCT conditioning due to superior pharmacokinetic predictability.

---

## Cytotoxicity

Busulfan meets all criteria for antineoplastic classification: it is an alkylsulfonate alkylating agent (DrugBank DB01008) used for haematological malignancies and HSCT conditioning.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — Alkylsulfonate/Alkylating agent |
| Myelosuppression Risk | Very High (intentional — profound myeloablation and pancytopaenia are the therapeutic goal in HSCT conditioning; aplasia is expected for 2–3 weeks post-infusion) |
| Emetogenicity Classification | Moderate to High (IV formulation); structured antiemetic prophylaxis per institutional HSCT protocol is required |
| Monitoring Items | CBC with differential daily during conditioning and engraftment phase; liver function tests (ALT, AST, total bilirubin, ALP) — hepatic veno-occlusive disease (VOD/SOS) surveillance; renal function; Busulfan plasma AUC therapeutic drug monitoring (target AUC ~900–1,350 µmol·min per dose for myeloablative dosing); seizure prophylaxis monitoring (anticonvulsant serum levels where applicable) |
| Handling Protection | Must comply with cytotoxic drug handling regulations; closed-system drug transfer devices (CSTDs) mandatory; full PPE (double gloves, gown, eye/face protection) required during preparation and administration; IV preparation in a certified pharmacy isolator under negative pressure; institutional spill management protocol required |

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for complete safety information. Formal contraindications and key warnings from the Danish Medicines Agency were identified as a **blocking data gap** in this evidence pack and must be obtained from the EMA SmPC for Busilvex before clinical initiation.

From published clinical literature included in this evidence pack, the following serious risks are documented in the context of Busulfan-based HSCT conditioning:

- **Hepatic veno-occlusive disease (VOD/sinusoidal obstruction syndrome)**: A potentially life-threatening complication of high-dose Busulfan conditioning; risk is amplified by prior hepatic damage, previous oxaliplatin exposure, and certain concomitant medications; defibrotide prophylaxis should be considered in high-risk patients
- **Seizure risk**: Busulfan penetrates the blood-brain barrier and has epileptogenic potential at myeloablative doses; anticonvulsant prophylaxis (e.g., levetiracetam or phenytoin) is mandatory throughout conditioning
- **Secondary malignancy**: As an alkylating agent, long-term risk of therapy-related myeloid neoplasms exists; an evidence-based risk assessment has been published (PMID [37856098](https://pubmed.ncbi.nlm.nih.gov/37856098/))

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Busulfan-based conditioning (BuFlu, BuCy, BuMelFlu) for MDS allo-HSCT is supported by Level L1 evidence, including multiple completed Phase 3 randomised controlled trials published in high-impact journals (Lancet Haematology, JCO). This represents an established standard-of-care application rather than a purely novel repurposing hypothesis, and the TxGNN prediction score of 99.62% is fully consistent with the breadth of existing clinical evidence. The "guardrails" designation reflects outstanding safety documentation gaps and the need for rigorous patient-level transplant eligibility assessment.

**To proceed, the following is needed:**
- **Resolve blocking data gap (DG001):** Obtain the full EMA SmPC for Busilvex (IV busulfan) to document contraindications and key warnings prior to any clinical initiation
- **Resolve high-severity data gap (DG002):** Confirm detailed mechanism of action and drug interaction profile via DrugBank API (DB01008)
- Verify current EMA centralised marketing authorisation status and hospital procurement pathway for Busilvex in Denmark via Lægemiddelstyrelsen and ema.europa.eu
- Conduct patient-level eligibility assessment: IPSS-R/IPSS-M risk stratification, HCT-CI comorbidity scoring, and HLA-compatible donor availability evaluation
- Establish Busulfan therapeutic drug monitoring (AUC-directed dosing) protocol and mandatory seizure prophylaxis plan within the institutional HSCT conditioning pathway
- Implement VOD/SOS risk stratification (per EBMT criteria) and document the clinical decision regarding defibrotide prophylaxis for high-risk patients
- Define long-term monitoring plan for secondary malignancy surveillance in HSCT survivors receiving alkylating agent-based conditioning
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

