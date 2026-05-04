---
layout: default
title: Carfilzomib
parent: 僅模型預測 (L5)
nav_order: 93
evidence_level: L5
indication_count: 10
---

# Carfilzomib
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

# Carfilzomib: From Multiple Myeloma to CMM7 (Malignant Melanoma Subtype)

## One-Sentence Summary

Carfilzomib (Kyprolis®) is an irreversible proteasome inhibitor approved globally for relapsed or refractory multiple myeloma, though it is not currently registered with the Danish Medicines Agency. The TxGNN model assigns its highest prediction score (**99.37%**) to **CMM7** — a non-standard identifier likely representing a malignant melanoma subtype per disease ontology classification — drawing on the drug's broad anti-tumour mechanism involving proteasomal pathway disruption. However, **no clinical trials or direct publications** support this specific indication, and the ambiguity of the CMM7 disease label itself prevents a rigorous mechanistic evaluation at this stage.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Multiple myeloma (relapsed/refractory) — established from global regulatory approvals; no Danish authorisation on record |
| Predicted New Indication | CMM7 (non-standard disease code; likely a malignant melanoma subtype) |
| TxGNN Prediction Score | 99.37% |
| Evidence Level | L5 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | **Hold** |

---

## Why Is This Prediction Reasonable?

Detailed mechanism of action data was not provided in this Evidence Pack. Based on established pharmacological knowledge, Carfilzomib is an epoxyketone-class proteasome inhibitor that **irreversibly and selectively binds the chymotrypsin-like (CT-L) active site of the 20S proteasome β5 subunit**. By blocking ubiquitin-dependent protein degradation, it causes accumulation of pro-apoptotic proteins (Bax, p27Kip1), stabilises IκBα to suppress NF-κB signalling, and triggers endoplasmic reticulum stress via the unfolded protein response (UPR) — collectively driving tumour cell death.

Both multiple myeloma and melanoma are malignancies with high dependency on protein homeostasis for survival. Melanoma cells, like myeloma plasma cells, generate large quantities of misfolded or damaged proteins that require continuous proteasomal clearance; disrupting this pathway theoretically renders them vulnerable. The in vitro study by Lee et al. (PMID 33671902) provides the most direct preclinical support, demonstrating that Carfilzomib combined with bortezomib synergistically induced apoptosis in B16-F1 murine melanoma cells through activation of caspases 3, 8, 9, and 12 — suggesting dual proteasome blockade may overcome partial resistance.

However, "CMM7" is a non-standard disease designation that cannot be unambiguously mapped to a specific clinical or histological entity without further ontology resolution. Even assuming CMM7 refers to a malignant melanoma subtype, important challenges remain: melanoma cells frequently maintain high intracellular glutathione levels that serve as an antioxidant barrier against ER stress inducers; if CMM7 involves CNS localisation, Carfilzomib's high molecular weight (~719 Da) and P-glycoprotein substrate status create a severe blood-brain barrier penetration barrier. Until the disease label is resolved and dedicated preclinical models are evaluated, the mechanistic rationale remains broad and indirect.

---

## Clinical Trial Evidence

Currently no clinical trials related to CMM7 are registered in ClinicalTrials.gov or the ICTRP registry.

---

## Literature Evidence

No literature specifically addressing Carfilzomib and CMM7 was identified. The following publications relate to Carfilzomib and **melanoma** (the broader disease category CMM7 most likely belongs to), retrieved from the evidence pack under the "melanoma" predicted indication:

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [33671902](https://pubmed.ncbi.nlm.nih.gov/33671902/) | 2021 | In vitro preclinical | *Biology* | Carfilzomib + bortezomib combination enhanced apoptotic cell death in B16-F1 murine melanoma cells; apoptosis confirmed via Annexin V staining and activation of caspases 3, 8, 9, and 12 — strongest direct preclinical evidence available |
| [36134605](https://pubmed.ncbi.nlm.nih.gov/36134605/) | 2023 | Computational / In silico | *J Biomol Struct Dyn* | Molecular docking and dynamics simulations of clinical drugs (including Carfilzomib) against 18 validated kinase targets across 10 cancer types including melanoma; suggests binding potential at relevant cancer kinase sites |
| [31540997](https://pubmed.ncbi.nlm.nih.gov/31540997/) | 2019 | Mechanistic / molecular biology | *Mol Cancer Res* | ZANF2A/AIRAP gene regulates cell survival in human melanoma via E3-ligase cIAP2, implicating the ubiquitin-proteasome pathway as a functional node in melanoma biology |
| [27016342](https://pubmed.ncbi.nlm.nih.gov/27016342/) | 2016 | Preclinical | *Matrix Biol* | Carfilzomib and bortezomib activate NF-κB, triggering heparanase upregulation in tumour cells and potentially promoting an aggressive phenotype; NF-κB blockade restores cytotoxic efficacy — mechanistically important cautionary finding |
| [29581547](https://pubmed.ncbi.nlm.nih.gov/29581547/) | 2018 | Preclinical / PROTAC | *Leukemia* | BET-domain-targeting PROTACs exploiting proteasomal degradation demonstrated activity in myeloma preclinical models; supports broader concept of therapeutic proteasome pathway exploitation in haematological and solid tumours |

---

## Denmark Market Information

Carfilzomib is **not currently registered** with the Danish Medicines Agency (Laegemiddelstyrelsen). No national marketing authorisations were identified in this dataset.

> **Reviewer note:** Carfilzomib (Kyprolis®, Amgen) holds a centralised EMA Marketing Authorisation (EU/1/13/848) for relapsed/refractory multiple myeloma, which is legally valid across all EU/EEA member states including Denmark. The absence of a record in this dataset may reflect a limitation of the national licence search scope. Current availability and reimbursement status should be verified via the EMA medicines database and the Danish Medicines Council (Medicinrådet).

---

## Cytotoxicity

Carfilzomib is a targeted antineoplastic agent (proteasome inhibitor) used in haematological malignancy treatment. The cytotoxicity section is therefore applicable.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — Irreversible proteasome inhibitor (epoxyketone class; selective 20S β5 subunit inhibitor; NOT conventional cytotoxic) |
| Myelosuppression Risk | Moderate to high — thrombocytopenia and anaemia are commonly reported in multiple myeloma trials; neutropenia less frequent than with conventional cytotoxics |
| Emetogenicity Classification | Low to moderate |
| Monitoring Items | Full blood count (FBC) with differential; renal function (creatinine, eGFR — acute kidney injury risk); liver function tests; cardiac assessment (echocardiography recommended — cardiomyopathy and cardiac failure reported); pulmonary function (dyspnoea, pulmonary arterial hypertension); blood pressure monitoring |
| Handling Protection | Follow institutional cytotoxic drug handling regulations; standard PPE for intravenous antineoplastic preparation and administration required |

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for complete safety information, including warnings, contraindications, and drug interactions. Formal safety data were not available in this Evidence Pack.

> For the EMA-authorised product, the full Kyprolis® SmPC is accessible at the EMA product page: [https://www.ema.europa.eu/en/medicines/human/EPAR/kyprolis](https://www.ema.europa.eu/en/medicines/human/EPAR/kyprolis)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
CMM7 is an unresolved disease identifier with no available clinical trials, translational studies, or directly relevant preclinical evidence linking Carfilzomib to this entity; the evidence level is L5 (model prediction only), and the disease label itself must be clarified before any scientific or regulatory evaluation can proceed.

**To proceed, the following is needed:**

- **Resolve CMM7 disease identity**: Map the CMM7 code to a standard clinical nomenclature (e.g., MONDO, ICD-10, SNOMED CT, or OMIM) to determine the precise histological and clinical context
- **Obtain MOA and safety data**: Retrieve full mechanism of action profile and SmPC warnings/contraindications from DrugBank API and EMA product label (Data Gaps DG001 and DG002)
- **Commission targeted preclinical work**: Design in vitro and in vivo studies of Carfilzomib in the specific CMM7 melanoma subtype, with particular attention to glutathione-mediated resistance mechanisms
- **Blood-brain barrier assessment**: If CMM7 involves CNS or leptomeningeal disease, evaluate strategies to address Carfilzomib's poor CNS penetration (~719 Da, P-gp substrate)
- **Paediatric considerations**: If CMM7 encompasses paediatric populations, a dedicated paediatric safety and pharmacokinetic programme is required given the significant data gap
- **Upgrade to L4 minimum**: A systematic review of proteasome inhibition across melanoma subtypes, and at least one targeted in vitro study in the resolved CMM7 cell type, is required before clinical translation can be contemplated
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

