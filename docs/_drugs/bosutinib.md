---
layout: default
title: Bosutinib
parent: 僅模型預測 (L5)
nav_order: 72
evidence_level: L5
indication_count: 10
---

# Bosutinib
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

# Bosutinib: From Philadelphia Chromosome-Positive CML to Myeloid Leukemia

## One-Sentence Summary

Bosutinib is a second-generation dual BCR-ABL1/Src tyrosine kinase inhibitor with well-established global approval for the treatment of Philadelphia chromosome-positive (Ph+) chronic myeloid leukaemia (CML).
The TxGNN model predicts it may be effective for **myeloid leukemia** broadly, with **50+ clinical trials** and **20 publications** currently supporting this direction — confirming its pharmacological basis in myeloid malignancies.
Although no product is currently listed in the Danish Medicines Agency (Laegemiddelstyrelsen) national database, bosutinib holds a centralised EMA marketing authorisation (Bosulif®, Pfizer) valid across all EU member states, including Denmark.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Philadelphia chromosome-positive (Ph+) chronic myeloid leukaemia (CML) |
| Predicted New Indication | Myeloid Leukemia |
| TxGNN Prediction Score | 98.75% |
| Evidence Level | L1 |
| Denmark Market Status | Not registered in national database; EMA centralised authorisation (EU/1/13/810) applies |
| Number of Marketing Authorisations | 0 (national registry); EMA centralised authorisation covers Denmark as EU member state |
| Recommended Decision | Go |

---

## Why is This Prediction Reasonable?

Bosutinib is a potent, orally administered inhibitor of two key kinase families: BCR-ABL1 and the Src family kinases (SFKs). In CML, the Philadelphia chromosome creates a constitutively active BCR-ABL1 fusion oncogene, which drives uncontrolled proliferation and survival of myeloid progenitor cells. By occupying the ATP-binding pocket of BCR-ABL1, bosutinib blocks this oncogenic signalling cascade and suppresses CML cell growth. Its additional inhibition of Src kinases — which are not targeted by first-generation imatinib — is thought to contribute to broader anti-leukaemic activity and a distinct resistance profile. This dual mechanism explains why bosutinib retains activity in a substantial proportion of patients resistant to imatinib or other BCR-ABL1 inhibitors.

The TxGNN prediction of "myeloid leukemia" is pharmacologically well-grounded, as CML is itself classified within the myeloid leukaemia spectrum. Multiple Phase 3 randomised controlled trials have confirmed bosutinib's superiority over imatinib in newly diagnosed chronic-phase CML in terms of depth and speed of molecular response (BFORE trial, NCT02130557), and its efficacy as a later-line option in patients who have failed prior TKI therapy (ASCEMBL, NCT03106779). The European LeukemiaNet (ELN) 2020 guidelines explicitly recommend bosutinib as an approved first-line treatment option alongside imatinib, dasatinib, and nilotinib. There is also preliminary evidence from exploratory trials examining bosutinib in acute myeloid leukaemia (AML) combinations, suggesting potential broader myeloid activity.

The high TxGNN score (98.75%) reflects the depth of pharmacological and network-level evidence connecting bosutinib to myeloid leukaemia biology. For Danish healthcare teams, the key clinical question is not whether evidence supports this indication — it clearly does at the highest level — but rather how to access and position bosutinib within the Danish CML treatment pathway, given that the drug does not appear in the national product register despite holding a valid EU-wide authorisation.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00574873](https://clinicaltrials.gov/study/NCT00574873) | Phase 3 | Completed | 502 | BELA trial: bosutinib vs imatinib in newly diagnosed chronic-phase Ph+ CML; evaluates complete cytogenetic response at 12 months as primary endpoint |
| [NCT02130557](https://clinicaltrials.gov/study/NCT02130557) | Phase 3 | Completed | 536 | BFORE trial: bosutinib 400 mg QD vs imatinib in newly diagnosed CP-CML; 5-year follow-up confirmed sustained molecular response benefit |
| [NCT03106779](https://clinicaltrials.gov/study/NCT03106779) | Phase 3 | Completed | 233 | ASCEMBL: asciminib vs bosutinib in CML-CP after ≥2 prior TKIs; bosutinib served as active comparator arm |
| [NCT04971226](https://clinicaltrials.gov/study/NCT04971226) | Phase 3 | Active, not recruiting | 406 | Asciminib 80 mg QD vs investigator-selected TKI (including bosutinib 400 mg QD) for newly diagnosed Ph+ CML-CP |
| [NCT03831776](https://clinicaltrials.gov/study/NCT03831776) | Phase 2 | Completed | 212 | NordCML012: ropeginterferon α-2b plus bosutinib vs bosutinib monotherapy as frontline CML therapy; aims to increase treatment-free remission rates |
| [NCT03205267](https://clinicaltrials.gov/study/NCT03205267) | Phase 2 | Unknown | 127 | Step-in dosing of bosutinib in CP-CML patients intolerant or refractory to imatinib, nilotinib, or dasatinib; tests whether gradual dose escalation reduces early toxicity |
| [NCT02810990](https://clinicaltrials.gov/study/NCT02810990) | Phase 2 | Completed | 65 | BEST study: bosutinib efficacy and tolerability in elderly CML patients failing front-line TKI therapy |
| [NCT00261846](https://clinicaltrials.gov/study/NCT00261846) | Phase 1/2 | Completed | 571 | Pivotal bosutinib phase 1/2 study in Ph+ leukaemias; established maximum tolerated dose and confirmed efficacy across multiple lines of therapy |
| [NCT03128411](https://clinicaltrials.gov/study/NCT03128411) | Phase 2 | Completed | 64 | Bosutinib monotherapy in Japanese patients with newly diagnosed CP-CML; assesses efficacy and safety in the Asian population |
| [NCT04258943](https://clinicaltrials.gov/study/NCT04258943) | Phase 1/2 | Active, not recruiting | 60 | ITCC-054/COG-AAML1921: bosutinib in paediatric patients with newly diagnosed or resistant/intolerant Ph+ CML; determines recommended paediatric dose |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29091516](https://pubmed.ncbi.nlm.nih.gov/29091516/) | 2018 | RCT | J Clin Oncol | BFORE trial: bosutinib demonstrated superior major molecular response at 12 months vs imatinib (47.2% vs 36.9%) in newly diagnosed CP-CML |
| [35643868](https://pubmed.ncbi.nlm.nih.gov/35643868/) | 2022 | RCT | Leukemia | BFORE 5-year final results: sustained molecular response benefit confirmed; 59.7% of bosutinib-treated patients remained on study at completion |
| [34407542](https://pubmed.ncbi.nlm.nih.gov/34407542/) | 2021 | RCT | Blood | ASCEMBL phase 3: asciminib showed superior MMR at 24 weeks (25.5% vs 13.2%) vs bosutinib; bosutinib established as standard-of-care comparator in later-line CML |
| [36717654](https://pubmed.ncbi.nlm.nih.gov/36717654/) | 2023 | RCT | Leukemia | ASCEMBL extended follow-up: bosutinib maintained 20.2% MMR at 96 weeks; confirmed as active and clinically relevant third-line option |
| [39164407](https://pubmed.ncbi.nlm.nih.gov/39164407/) | 2024 | Phase 4 | Leukemia | BYOND trial final results: 71.8% of Ph+ CP-CML patients achieved complete cytogenetic response with bosutinib after prior TKI failure; median follow-up 47.8 months |
| [32127639](https://pubmed.ncbi.nlm.nih.gov/32127639/) | 2020 | Guidelines | Leukemia | ELN 2020 recommendations: bosutinib endorsed as approved first-line option for CP-CML; guidance on monitoring milestones and response criteria |
| [40094679](https://pubmed.ncbi.nlm.nih.gov/40094679/) | 2025 | Review | JAMA | Comprehensive CML review: bosutinib classified as a standard second-generation TKI; approximately 5 million patients worldwide live with CML and may benefit from TKI therapy |
| [39252937](https://pubmed.ncbi.nlm.nih.gov/39252937/) | 2024 | Review | Front Oncol | Critical review of bosutinib clinical data and expert recommendations covering efficacy across lines of therapy, toxicity profile, and patient selection criteria |
| [39093014](https://pubmed.ncbi.nlm.nih.gov/39093014/) | 2024 | Review | Am J Hematol | CML 2025 update: bosutinib highlighted for favourable cardiovascular safety profile compared with nilotinib and ponatinib; suitable for patients with pre-existing cardiovascular risk |
| [30587215](https://pubmed.ncbi.nlm.nih.gov/30587215/) | 2018 | Review | J Hematol Oncol | Expert panel guidance on managing bosutinib adverse events in CP-CML; diarrhoea and hepatotoxicity are the most clinically relevant, generally manageable with dose adjustment |

---

## Denmark Market Information

Bosutinib (Bosulif®, Pfizer) does not currently appear in the Laegemiddelstyrelsen national product register. However, as a centrally authorised medicinal product, the EMA marketing authorisation is directly applicable in Denmark without requiring a separate national approval.

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EU/1/13/810 | Bosulif® (Pfizer) | Film-coated tablets (100 mg, 400 mg, 500 mg) | Ph+ CML in chronic, accelerated, and blast phase in adults previously treated with ≥1 TKI; also newly diagnosed Ph+ CP-CML |

> Prescribers in Denmark should verify the current SmPC and reimbursement status via the EMA product database (medicines.eea.europa.eu) or contact Pfizer Denmark directly regarding commercial availability.

---

## Cytotoxicity

Bosutinib is an antineoplastic targeted therapy. It is **not** a conventional cytotoxic chemotherapy agent.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy — BCR-ABL1/Src dual kinase inhibitor (2nd-generation TKI); small molecule oral targeted agent |
| Myelosuppression Risk | Moderate: thrombocytopenia and neutropenia are recognised class effects; generally less severe than with conventional chemotherapy or some other second-generation TKIs |
| Emetogenicity Classification | Low to moderate (gastrointestinal effects, primarily diarrhoea and nausea, are the dominant adverse event class; distinct from classical chemotherapy-induced emesis) |
| Monitoring Items | Full blood count (FBC) with differential; liver function tests (ALT, AST, bilirubin); renal function (eGFR/creatinine); BCR-ABL1 transcript level by IS-standardised PCR at defined milestones |
| Handling Protection | Standard oral antineoplastic handling precautions; gloves required when handling broken or crushed tablets; no special intravenous handling required |

---

## Safety Considerations

Full Danish prescribing information (SmPC) is not available within this evidence pack. Based on published clinical trial data and expert consensus:

- **Gastrointestinal toxicity**: Diarrhoea is the most frequently reported adverse event across all bosutinib trials (occurring in the majority of patients), typically appearing early in treatment and manageable through dose reduction, short-term interruption, or antidiarrhoeals — early proactive management is recommended
- **Hepatotoxicity**: Clinically significant elevations in ALT and AST occur and necessitate regular liver function monitoring, particularly during the first three months; dose interruption or reduction is usually effective
- **Haematological toxicity**: Thrombocytopenia and neutropenia occur and may require dose adjustment; haematological monitoring with FBC at regular intervals is essential
- **Drug interaction — warfarin**: A clinically relevant pharmacodynamic interaction between bosutinib and warfarin has been reported (PMID 24359239); close INR monitoring and anticoagulation management are advised if co-prescribed

Please refer to the approved EMA Summary of Product Characteristics (SmPC) for complete prescribing information: [Bosulif SmPC — EMA](https://www.ema.europa.eu/en/medicines/human/EPAR/bosulif)

---

## Conclusion and Next Steps

**Decision: Go**

**Rationale:**
The TxGNN prediction for bosutinib in myeloid leukaemia is supported by the highest available evidence level (L1: multiple completed Phase 3 RCTs, ELN guideline endorsement, and EMA centralised marketing authorisation). This is a well-characterised, globally established therapy with no regulatory barrier to use in Denmark.

**To proceed, the following is needed:**
- Confirm commercial availability and reimbursement pathway through Laegemiddelstyrelsen and the Danish Regions' joint medicine procurement system (Amgros)
- Obtain and review the current EMA SmPC to ensure prescribers are familiar with the approved indication scope, monitoring requirements, and dose modification guidelines
- Verify institutional capacity for BCR-ABL1 molecular monitoring (IS-standardised PCR), which is required for treatment response assessment and discontinuation decisions
- Position bosutinib within the local CML treatment algorithm relative to available alternatives (imatinib, dasatinib, nilotinib, asciminib), taking into account bosutinib's particularly favourable cardiovascular safety profile — relevant for Danish CML patients with pre-existing metabolic or vascular comorbidities
- Establish a structured haematological and hepatic monitoring programme aligned with ELN 2020 recommendations before initiating the first patient

---

> **Disclaimer**: This report is intended for research reference purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before therapeutic application. Data cutoff: 2026-04-04.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

