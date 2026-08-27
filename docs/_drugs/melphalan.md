---
layout: default
title: Melphalan
parent: 僅模型預測 (L5)
nav_order: 283
evidence_level: L5
indication_count: 10
---

# Melphalan
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

# Melphalan: From Multiple Myeloma to Gonadal Germ Cell Tumor

---

## One-Sentence Summary

Melphalan is a bifunctional alkylating agent with established use in multiple myeloma and haematopoietic stem cell transplantation conditioning. The TxGNN model predicts it may be effective for **Gonadal Germ Cell Tumor**, with **8 clinical trials** and **4 publications** currently supporting this direction. Evidence is anchored by a completed Phase 2 trial directly targeting melphalan-containing high-dose chemotherapy in relapsed germ cell tumours, placing overall support at Level L2.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Multiple myeloma and haematologic malignancies (established international use; not currently authorised in Denmark) |
| Predicted New Indication | Gonadal Germ Cell Tumor |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L2 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Melphalan (L-phenylalanine mustard) belongs to the nitrogen mustard class of alkylating agents. It exerts its cytotoxic effect by forming DNA interstrand crosslinks (ISC), which physically block the replication fork and prevent transcription, ultimately triggering apoptosis in rapidly dividing cells. This mechanism is precisely why melphalan has long been the backbone of high-dose conditioning regimens before autologous stem cell transplantation (ASCT) — the DNA damage inflicted is severe enough to ablate the bone marrow, necessitating stem cell rescue.

Gonadal germ cell tumours (GCTs) are among the most chemotherapy-sensitive solid tumours in clinical oncology. First-line BEP (bleomycin, etoposide, cisplatin) cures the majority of patients, but platinum-refractory or relapsed disease represents a significant unmet need. In this salvage setting, high-dose chemotherapy (HDC) combined with ASCT is an established strategy to overcome platinum resistance. Because melphalan's mechanism of action — DNA crosslinking via the alkylating pathway — is mechanistically distinct from platinum-based crosslinks, it offers a non-cross-resistant route to cytotoxicity, making it a rational partner in salvage HDC regimens for cisplatin-refractory GCT.

This rationale has been tested clinically. The GD-HDCT regimen (gemcitabine + docetaxel + melphalan + carboplatin), studied in a completed Phase 2 trial (NCT00936936, n=64) specifically in poor-prognosis relapsed GCT, represents the strongest direct evidence for this repurposing prediction and demonstrates that the TxGNN model is capturing a biologically and clinically plausible signal.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00936936](https://clinicaltrials.gov/study/NCT00936936) | Phase 2 | Completed | 64 | Two-cycle HDC regimen for poor-prognosis relapsed GCT: Cycle 1 = gemcitabine + docetaxel + **melphalan** + carboplatin; Cycle 2 = ifosfamide + carboplatin + etoposide. Only completed Phase 2 trial directly targeting relapsed GCT with a melphalan-containing regimen — the core evidence for this indication. |
| [NCT00060255](https://clinicaltrials.gov/study/NCT00060255) | Phase 2 | Completed | 451 | Eight HDC regimens ± TBI prior to ASCT in haematologic malignancies and selected solid tumours; GCT was a common enrolled tumour type. Large Phase 2 dataset provides safety and feasibility data for ASCT-based approaches relevant to GCT. |
| [NCT00536601](https://clinicaltrials.gov/study/NCT00536601) | NA | Completed | 174 | Pilot trial comparing HDC regimens ± total-body irradiation before ASCT in haematologic cancers and solid tumours; provides safety data applicable to the GCT transplant setting. |
| [NCT00638898](https://clinicaltrials.gov/study/NCT00638898) | Phase 1 | Completed | 25 | HDC with busulfan + **melphalan** + topotecan followed by ASCT in advanced and recurrent solid tumours including GCT; evaluates dose-safety of this melphalan-containing combination. |
| [NCT00003425](https://clinicaltrials.gov/study/NCT00003425) | Phase 1/2 | Completed | 25 | Dose-escalation trial of high-dose **melphalan** with ASCT and amifostine cytoprotection; directly evaluates melphalan pharmacology, maximum tolerated dose, and tolerability across cancer types. |
| [NCT01272817](https://clinicaltrials.gov/study/NCT01272817) | NA | Completed | 36 | Nonmyeloablative allogeneic HSCT using antithymocyte globulin with **melphalan** and cladribine or total lymphoid irradiation for haematologic malignancies; provides reference safety data for melphalan in conditioning. |
| [NCT00003926](https://clinicaltrials.gov/study/NCT00003926) | Phase 1 | Terminated | 13 | Amifostine chemoprotection with ASCT in paediatric solid tumours; terminated early (n=13), melphalan as carrier agent rather than primary study drug — limited evidentiary value. |
| [NCT00002750](https://clinicaltrials.gov/study/NCT00002750) | Phase 1 | Completed | 6 | Intrathecal melphalan for recurrent neoplastic meningitis; route-specific study, not relevant to systemic GCT treatment; included for completeness only. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [4270380](https://pubmed.ncbi.nlm.nih.gov/4270380/) | 1973 | Clinical Study | Oncology | Early systematic clinical experience with chemotherapy — including alkylating agents — in testicular germinal tumours; provides historical basis for melphalan in GCT. |
| [24913](https://pubmed.ncbi.nlm.nih.gov/24913/) | 1977 | Clinical Review | Urologic Clinics of North America | Review of seminoma management including cytotoxic chemotherapy options; contextualises the use of alkylating agents in gonadal GCT before platinum-based regimens became standard. |
| [13392619](https://pubmed.ncbi.nlm.nih.gov/13392619/) | 1956 | Case Series | Voprosy Onkologii | Among the earliest documented use of sarcolysin (melphalan) for seminoma of the testes and its metastases; historical proof-of-concept for melphalan activity in GCT. |
| [14151951](https://pubmed.ncbi.nlm.nih.gov/14151951/) | 1964 | Mechanistic Study | Acta — Unio Internationalis Contra Cancrum | Mechanistic investigation of alkylating drug effects on pituitary follicle-stimulating function; provides indirect mechanistic context for melphalan's endocrine effects in gonadal tumour treatment. |

---

## Denmark Market Information

Melphalan currently holds **no marketing authorisations** in Denmark — neither via the Danish Medicines Agency (Lægemiddelstyrelsen) national procedure nor via the EMA centralised procedure. The drug is not commercially available on the Danish market.

Healthcare professionals seeking access for individual patients would need to apply through the named-patient (enkeltpatient) or compassionate-use pathway administered by Lægemiddelstyrelsen. Internationally, melphalan is authorised under the brand name **Alkeran** in numerous countries for multiple myeloma and as a conditioning agent prior to ASCT.

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — Nitrogen mustard / Alkylating agent (bifunctional) |
| Myelosuppression Risk | **High** — severe, dose-limiting myelosuppression (neutropenia, thrombocytopenia, anaemia) is the primary and expected toxicity; high-dose regimens require mandatory ASCT support for haematopoietic rescue |
| Emetogenicity Classification | Low to moderate (oral standard-dose); moderate to high (intravenous high-dose regimens) |
| Monitoring Items | Full blood count (CBC) with differential and platelets — frequent monitoring required; serum creatinine and eGFR (melphalan clearance is renally influenced); liver function tests (ALT, AST, bilirubin); electrolytes; mucositis assessment; long-term surveillance for secondary malignancy (AML/MDS) |
| Handling Protection | Must comply with cytotoxic drug handling regulations; appropriate PPE (gloves, gown, eye protection) required during preparation and administration; dedicated cytotoxic preparation area required |

---

## Safety Considerations

Detailed warnings, contraindications, and drug–drug interaction data were not available in the current evidence pack. Please refer to the approved Summary of Product Characteristics (SmPC) for complete safety information.

> **Clinical note for Danish practitioners**: Melphalan is known to carry significant long-term risks, including secondary acute myeloid leukaemia (AML) and myelodysplastic syndrome (MDS) with cumulative use, pulmonary toxicity, reproductive toxicity (gonadotoxicity), and teratogenicity. These risks are particularly relevant when considering use in younger GCT patients. A formal risk–benefit assessment and specialist MDT review are strongly recommended before initiating treatment.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The TxGNN model's prediction of melphalan utility in gonadal germ cell tumour (score 99.77%) is biologically well-founded and supported by a completed Phase 2 clinical trial (NCT00936936, n=64) that directly evaluated a melphalan-containing HDC regimen in poor-prognosis relapsed GCT — meeting L2 evidence criteria. The drug's DNA alkylating mechanism is non-cross-resistant with platinum, providing a sound scientific rationale for salvage use in platinum-refractory disease, a setting with limited alternatives in Denmark.

**To proceed, the following is needed:**

- **Regulatory access**: Submit a named-patient or compassionate-use application to Lægemiddelstyrelsen, as melphalan is not marketed in Denmark
- **Safety documentation**: Retrieve the full SmPC (warnings, contraindications, DDI profile) — this is a Blocking data gap in the current evidence pack
- **MOA confirmation**: Obtain complete mechanism of action data from DrugBank to finalise the mechanistic analysis and support the clinical rationale document
- **Patient population definition**: Restrict this indication to the evidence-supported population — platinum-refractory or relapsed GCT patients being considered for salvage HDC + ASCT in a specialist transplant centre
- **MDT review**: Establish a haematology/oncology multidisciplinary team (MDT) review process; involve a transplant centre with ASCT capability before any clinical application
- **Prospective safety monitoring plan**: Define specific monitoring parameters for myelosuppression, secondary malignancy surveillance, and organ function given the high-dose setting
- **Feasibility of trial enrolment**: Assess whether Danish patients could be enrolled in an existing or planned international Phase 2/3 trial for relapsed GCT rather than off-label use

---

*This report is generated for research reference purposes only and does not constitute medical advice. Repurposing candidates require clinical validation before therapeutic application. All pages referencing drug repurposing predictions should be understood in the context of investigational research.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

