---
layout: default
title: Brentuximab Vedotin
parent: 僅模型預測 (L5)
nav_order: 73
evidence_level: L5
indication_count: 10
---

# Brentuximab Vedotin
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

# Brentuximab Vedotin: From CD30+ Lymphoma (Classical Hodgkin Lymphoma / Systemic ALCL) to Follicular Lymphoma

## One-Sentence Summary

Brentuximab vedotin (BV; Adcetris) is an anti-CD30 antibody-drug conjugate approved globally for the treatment of classical Hodgkin lymphoma (cHL) and systemic anaplastic large cell lymphoma (sALCL).
The TxGNN model predicts it may be effective for **Follicular Lymphoma**, with **6 clinical trials** and **20 publications** currently supporting this direction.
However, the majority of trials have been terminated or withdrawn, and the central clinical challenge remains the highly variable — and generally low — CD30 expression rate (~10–20%) across the follicular lymphoma patient population, making rigorous biomarker-driven patient selection essential.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Classical Hodgkin lymphoma (cHL); systemic anaplastic large cell lymphoma (sALCL) |
| Predicted New Indication | Follicular Lymphoma |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L2 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Brentuximab vedotin is an antibody-drug conjugate (ADC) consisting of the anti-CD30 monoclonal antibody brentuximab linked via a protease-cleavable linker to MMAE (monomethyl auristatin E), a potent microtubule-disrupting cytotoxic agent. Upon binding to CD30-expressing tumour cells, the conjugate is internalised, MMAE is released intracellularly, and cell division is halted — ultimately inducing apoptosis. Detailed MOA data from DrugBank was not retrieved in this evidence pack and remains a data gap; however, the mechanism described above is well-established in the clinical literature and regulatory dossiers for BV's approved indications.

CD30 is expressed at near-universal levels in cHL (~100%) and sALCL (~100%), underpinning BV's globally approved efficacy in those settings. Follicular lymphoma (FL) shares its B-lymphocyte origin with cHL, but critically, CD30 expression in FL is highly heterogeneous: approximately 10–20% of unselected FL cases are CD30-positive, with notably higher rates in Grade 3B FL and in cases undergoing histological transformation. Several Phase 2 trials investigating BV in FL have specifically mandated CD30 positivity as an inclusion criterion, validating the biomarker-driven rationale and confirming that patient selection is the key determinant of whether this mechanistic link translates to clinical benefit.

The main concern tempering enthusiasm is the accumulated evidence of trial feasibility challenges. Multiple clinical programmes targeting CD30+ B-cell lymphomas — including FL — have been withdrawn or terminated primarily due to enrolment difficulties, which directly reflects how few FL patients screen positive for CD30. The one currently active and recruiting trial (NCT04587687) demonstrates sustained investigator interest, but results are not yet available. Until Phase 2 efficacy data mature from adequately CD30-selected FL cohorts, this indication warrants a cautious "Proceed with Guardrails" classification.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04587687](https://clinicaltrials.gov/study/NCT04587687) | Phase 2 | Recruiting | 23 | BV + bendamustine in relapsed/refractory follicular lymphoma; the most directly relevant and currently active trial; expected completion December 2026; results pending |
| [NCT01805037](https://clinicaltrials.gov/study/NCT01805037) | Phase 1/2 | Terminated | 20 | BV + rituximab as frontline therapy for CD30+ and/or EBV+ lymphomas, including FL; validated biomarker-driven patient selection; provided dose and tolerability data |
| [NCT02594163](https://clinicaltrials.gov/study/NCT02594163) | Phase 2 | Terminated | 25 | Randomised: rituximab + bendamustine ± BV for R/R CD30+ DLBCL; terminated early due to slow accrual, illustrating real-world screening difficulties with CD30+ selection in B-cell lymphomas |
| [NCT04138875](https://clinicaltrials.gov/study/NCT04138875) | Phase 2 | Withdrawn | 0 | Multicenter risk-stratified sequential rituximab + BV ± bendamustine in newly diagnosed CD20+/CD30+ PTLD; withdrawn prior to enrolment; no data generated |
| [NCT02623920](https://clinicaltrials.gov/study/NCT02623920) | Phase 2 | Withdrawn | 0 | BV + bendamustine + rituximab in CD30+ R/R B-cell NHL; withdrawn before enrolment, echoing recurring recruitment barriers |
| [NCT04795869](https://clinicaltrials.gov/study/NCT04795869) | Phase 2 | Withdrawn | 0 | BV + pembrolizumab in recurrent systemic PTCL; withdrawn before enrolment; limited direct FL relevance |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40758949](https://pubmed.ncbi.nlm.nih.gov/40758949/) | 2025 | Phase 2 Trial | Blood Advances | BV + gemcitabine in R/R PTCL (≥5% CD30+) followed by BV maintenance; reports ORR after 4 induction cycles; directly informs CD30 threshold methodology applicable to FL biomarker selection |
| [34797505](https://pubmed.ncbi.nlm.nih.gov/34797505/) | 2022 | Prospective Cohort | Advances in Therapy | Real-world BV + cyclophosphamide/epirubicin/prednisone in untreated CD30+ NHL (including PTCL-TFH, ALCL, AITL); supports frontline BV utility across CD30+ lymphoid malignancies |
| [35663281](https://pubmed.ncbi.nlm.nih.gov/35663281/) | 2022 | Review | Leukemia Research Reports | Immunotherapy in indolent NHL including FL, MZL, and CLL/SLL; contextualises the role of novel targeted agents including ADCs within the current FL treatment landscape |
| [32476657](https://pubmed.ncbi.nlm.nih.gov/32476657/) | 2020 | Case Report | Gulf Journal of Oncology | Grade I FL transformed to CD30+ ALK1– ALCL achieved complete response with BV + high-dose methotrexate; directly demonstrates BV efficacy when FL acquires CD30 expression upon transformation |
| [33320379](https://pubmed.ncbi.nlm.nih.gov/33320379/) | 2021 | Retrospective Cohort | European Journal of Haematology | BV + ifosfamide/carboplatin/etoposide (ICE) in R/R PTCL; confirms BV combinability with salvage chemotherapy backbones of relevance to FL salvage strategies |
| [38306597](https://pubmed.ncbi.nlm.nih.gov/38306597/) | 2024 | Review | Blood | Evolving treatment paradigms for nodal PTCLs (PTCL-NOS, ALCL, T-follicular helper lymphomas); BV + CHP now incorporated frontline for CD30+ disease; key background on CD30-targeted therapy |
| [39644004](https://pubmed.ncbi.nlm.nih.gov/39644004/) | 2024 | Review | Hematology (ASH Education Program) | BV and novel agents in PTCL management; discusses biomarker-driven selection strategies directly applicable to the CD30-positive FL subpopulation approach |
| [28967896](https://pubmed.ncbi.nlm.nih.gov/28967896/) | 2018 | Review | Bone Marrow Transplantation | Post-ASCT maintenance in lymphoma; rituximab maintenance established in FL; BV consolidation post-ASCT discussed in high-risk HL — relevant to maintenance strategy considerations in FL |
| [40517441](https://pubmed.ncbi.nlm.nih.gov/40517441/) | 2025 | Review | Hematological Oncology | Comprehensive review of PTCL biology and emerging therapies; provides broad context for CD30-directed ADC use across lymphoid malignancies |
| [28340875](https://pubmed.ncbi.nlm.nih.gov/28340875/) | 2017 | Review | Hematology/Oncology Clinics of North America | Angioimmunoblastic T-cell lymphoma (a follicular T-helper-derived neoplasm); discusses BV among newer approaches; relevant to understanding CD30 expression in follicular-lineage lymphomas |

---

## Denmark Market Information

Brentuximab vedotin (Adcetris) currently holds **no marketing authorisations in Denmark** and is listed as not marketed. The total number of licences on record with Lægemiddelstyrelsen is zero.

For reference, brentuximab vedotin holds a centralised EMA marketing authorisation (EU/1/12/794, Adcetris, Takeda) valid across the EU/EEA for the following approved indications: previously untreated stage III–IV cHL, relapsed/refractory cHL after ASCT, relapsed/refractory sALCL, CD30+ cutaneous T-cell lymphoma (mycosis fungoides), and CD30+ peripheral T-cell lymphoma. Access for Danish patients under currently approved indications would require application through a compassionate use or named patient programme (§ 29a, Lægemiddelloven) via Lægemiddelstyrelsen.

There are no Danish national marketing authorisation numbers, product names, dosage forms, or approved indications to tabulate at this time.

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — Antibody-Drug Conjugate (ADC); anti-CD30 monoclonal antibody (brentuximab) conjugated to MMAE (monomethyl auristatin E), a microtubule polymerisation inhibitor |
| Myelosuppression Risk | Moderate-to-High — neutropenia is the most commonly reported Grade ≥3 adverse event in pivotal trials (occurring in ~55% of patients in cHL studies); thrombocytopenia and anaemia also observed; myelosuppression risk is compounded when BV is used in combination with chemotherapy |
| Emetogenicity Classification | Low (BV monotherapy is classified as low emetogenic potential per MASCC/ESMO/ASCO guidelines; combination regimens may elevate this classification) |
| Monitoring Items | Complete blood count with differential (prior to each cycle), liver function tests (ALT, AST, bilirubin — particularly with CYP3A4-metabolised combinations), renal function, neurological assessment at each visit (peripheral sensory and motor neuropathy is the most clinically significant cumulative toxicity), pulmonary function monitoring (risk of non-infectious pulmonary toxicity / pneumonitis) |
| Handling Protection | Must be handled in accordance with cytotoxic drug handling regulations; the MMAE payload is a potent auristatin; preparation requires trained oncology pharmacy personnel, biological safety cabinet, closed-system drug transfer devices, and full cytotoxic PPE per institutional and national guidelines |

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for Adcetris (EU/1/12/794) available via the EMA product database for full safety information, including boxed warnings, peripheral neuropathy management guidelines, PML risk, and infusion reaction management.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
There is a biologically coherent CD30-targeting mechanism in CD30-positive FL subpopulations and one actively recruiting Phase 2 trial (NCT04587687), but the overall FL population has low CD30 expression (~10–20%), no completed Phase 2/3 trial has reported positive efficacy data in FL to date, and repeated enrolment failures across multiple trials signal real-world implementation barriers that must be addressed before broader clinical deployment.

**To proceed, the following is needed:**

- **Awaited efficacy results** from NCT04587687 (Phase 2, BV + bendamustine in R/R FL; estimated completion December 2026) — this is the pivotal missing dataset
- **CD30 expression prevalence mapping** in the Danish FL patient population (incidence and distribution of CD30+ FL cases across Danish haematology centres), to assess local feasibility
- **Definition of CD30 positivity threshold** for patient selection — current trials use heterogeneous cut-offs (e.g., ≥1%, ≥5%, ≥10% by IHC); a harmonised threshold is needed before a Danish study or compassionate use programme can be designed
- **Full safety profile review**: retrieve and review the EMA SmPC for Adcetris (EU/1/12/794), with particular attention to peripheral neuropathy (dose-limiting, cumulative), progressive multifocal leukoencephalopathy (PML) risk, hepatotoxicity, and infusion reaction profiles
- **Mechanism of action data gap resolution**: DrugBank MOA data should be retrieved (currently marked as a blocking gap — DG002) to support mechanistic rationale documentation
- **Access pathway assessment**: coordinate with Lægemiddelstyrelsen to explore named patient programme (§ 29a) or compassionate use options for eligible CD30+ FL patients in Denmark, given current non-marketed status
- **Health technology assessment consideration**: given the EMA approval status (cHL/ALCL/CTCL/PTCL), evaluate whether an indication extension or off-label use framework would be required under Danish reimbursement regulations (Medicinrådet) for a FL indication

> **Disclaimer:** This report is for research reference only and does not constitute medical advice. All drug repurposing candidates require clinical validation before therapeutic application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

