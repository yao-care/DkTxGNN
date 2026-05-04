---
layout: default
title: Axitinib
parent: 僅模型預測 (L5)
nav_order: 53
evidence_level: L5
indication_count: 10
---

# Axitinib
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

# Axitinib: From Advanced Renal Cell Carcinoma to Neuroblastoma-Associated Renal Cell Carcinoma

## One-Sentence Summary

Axitinib (Inlyta®) is a selective VEGFR kinase inhibitor with established global approval for advanced renal cell carcinoma (RCC), though it is not currently marketed in Denmark.
The TxGNN model predicts activity across five rare oncological subtypes — including **renal cell carcinoma associated with neuroblastoma** (top-ranked, 99.90%), Xp11.2/TFE3 translocation RCC, unclassified RCC, childhood kidney cell carcinoma, and liposarcoma.
Across all predicted indications combined, **4 clinical trials** and **3 publications** have been identified; however, direct evidence for the top-ranked neuroblastoma-associated RCC subtype is currently absent.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Advanced renal cell carcinoma (EMA/FDA approved globally; no Danish registration) |
| Predicted New Indication | Renal cell carcinoma associated with neuroblastoma |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L4 (top-ranked indication); best available evidence across all predictions is L2 (Xp11.2/TFE3 RCC and childhood RCC) |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Research Question (top-ranked indication) |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the system database. Based on established pharmacological knowledge, Axitinib is a potent and selective second-generation tyrosine kinase inhibitor that targets VEGFR1, VEGFR2, and VEGFR3. By blocking VEGF receptor signalling, it disrupts tumour angiogenesis — the formation of new blood vessels that tumours rely on for sustained growth and metastasis. This mechanism underpins its regulatory approval for advanced RCC, where VEGF pathway overactivation is a dominant molecular driver, particularly in clear-cell histology.

Renal cell carcinomas of all subtypes share a fundamental dependency on tumour vasculature, providing a pharmacological rationale for extrapolating across RCC histologies. However, the top-ranked prediction — RCC associated with neuroblastoma — is an extremely rare entity in which the neuroblastoma component may be additionally driven by ALK amplification or MYCN pathway dysregulation, targets that fall outside the scope of VEGFR inhibition. The mechanistic link is therefore plausible but incomplete for this specific subtype, and the high TxGNN score (0.999) reflects knowledge graph structural similarity rather than direct biological evidence.

The mechanistic rationale is substantially stronger for the Xp11.2/TFE3 gene fusion subtype: TFE3 fusion proteins activate MET and downstream VEGFR signalling, creating a direct molecular target for axitinib. This subtype accounts for approximately 20–40% of paediatric RCC cases, which explains why childhood kidney cell carcinoma also appears as a closely related high-ranked prediction. For liposarcoma — specifically the myxoid subtype — published preclinical data confirm VEGFR expression and axitinib sensitivity in cell line models, though clinical trial validation is still lacking.

---

## Clinical Trial Evidence

No clinical trials were identified for the top-ranked indication (renal cell carcinoma associated with neuroblastoma). The following trials are relevant to other TxGNN-predicted indications and are presented to give a complete evidence picture.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|------|--------|-----------|-------------|
| [NCT03595124](https://clinicaltrials.gov/study/NCT03595124) | Phase 2 | Active, Not Recruiting | 15 | Randomised trial comparing axitinib + nivolumab versus nivolumab alone in TFE/translocation RCC across all age groups. Directly evaluates axitinib in both the Xp11.2/TFE3 and paediatric RCC subtypes; currently the highest-grade interventional evidence for these rare variants. Results pending (expected completion November 2026). |
| [NCT04510597](https://clinicaltrials.gov/study/NCT04510597) | Phase 3 | Recruiting | 364 | PROBE Trial: immunotherapy-based combination therapy (nivolumab, ipilimumab, pembrolizumab, or avelumab) with or without cytoreductive nephrectomy in metastatic RCC. Highest-level study design in the landscape; key evidence anchor for childhood/metastatic RCC. Results expected 2033. |
| [NCT02156895](https://clinicaltrials.gov/study/NCT02156895) | N/A | Completed | 111 | Post-marketing surveillance of Inlyta® in real-world practice. Observational design monitoring safety and effectiveness of axitinib in routine oncology care, including unclassified RCC histologies. |
| [NCT04033991](https://clinicaltrials.gov/study/NCT04033991) | N/A | Completed | 684 | UK retrospective real-world database study examining outcomes of sunitinib (1st line) → axitinib (2nd line) in metastatic/advanced RCC. Evaluates progression-free survival by MSKCC/IMDC risk category; largest observational dataset available, relevant to unclassified RCC. |

---

## Literature Evidence

No literature was identified for renal cell carcinoma associated with neuroblastoma or for unclassified RCC. The following publications are relevant to other predicted indications.

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [31012542](https://pubmed.ncbi.nlm.nih.gov/31012542/) | 2019 | Review | Pediatric Blood & Cancer | Systematic review of treatment for advanced paediatric RCC. Notes the scarcity of high-quality evidence in this population and discusses the role of VEGFR inhibitors, including axitinib, as a treatment option. |
| [26279736](https://pubmed.ncbi.nlm.nih.gov/26279736/) | 2015 | Case Report | Can Urol Assoc J | First published use of axitinib in a paediatric patient (12-year-old male) with malignant epithelioid angiomyolipoma of the kidney treated on adult protocols. Authors conclude adult axitinib regimens can be used safely in rare childhood renal malignancies. |
| [27822137](https://pubmed.ncbi.nlm.nih.gov/27822137/) | 2016 | Preclinical Study | Sarcoma | Axitinib demonstrates antiangiogenic and direct antitumour activity in myxoid liposarcoma cell lines. Screening of targeted and conventional agents confirms VEGFR-directed therapy as a promising strategy for this rare sarcoma subtype; no clinical validation available to date. |

---

## Denmark Market Information

Axitinib currently holds no marketing authorisation in Denmark. No approvals have been issued by the Danish Medicines Agency (Lægemiddelstyrelsen) and no centralised EMA authorisation is reflected in the Danish market database.

> **Access note:** Axitinib (Inlyta®) holds EMA centralised authorisation for advanced/metastatic RCC in adults and FDA approval (since 2012). Danish patients requiring axitinib would currently need access through an individual import approval or a named-patient/compassionate use pathway.

---

## Cytotoxicity

Axitinib is an antineoplastic agent (targeted kinase inhibitor approved for renal cell carcinoma; original indication involves malignancy).

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — selective VEGFR1/2/3 tyrosine kinase inhibitor (not a conventional cytotoxic agent) |
| Myelosuppression Risk | Low (VEGFR inhibitors rarely cause clinically significant myelosuppression; occasional mild anaemia or thrombocytopenia possible) |
| Emetogenicity Classification | Low (oral targeted agents have minimal emetogenic potential per MASCC/ESMO guidelines) |
| Monitoring Items | Blood pressure (hypertension is a common class effect), thyroid function (TSH), liver enzymes (ALT/AST), renal function, urine protein, hand-foot skin reaction assessment |
| Handling Protection | Standard oral antineoplastic handling precautions apply; follow local institutional cytotoxic waste disposal guidelines |

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

---

## Conclusion and Next Steps

**Decision: Research Question** (renal cell carcinoma associated with neuroblastoma — top-ranked TxGNN prediction)

**Decision: Proceed with Guardrails** (Xp11.2/TFE3 translocation RCC and childhood kidney cell carcinoma — best-evidenced indications in this evaluation)

**Rationale:**
The top-ranked TxGNN prediction lacks any direct clinical or preclinical evidence, and the neuroblastoma-associated RCC subtype is so rare that evidence generation will be inherently challenging; this indication should currently be treated as a hypothesis requiring dedicated research. In contrast, the Xp11.2/TFE3 translocation RCC and childhood kidney cell carcinoma indications are supported by a directly relevant active Phase 2 randomised trial (NCT03595124) and an ongoing Phase 3 trial (NCT04510597), providing a foundation for cautious clinical development activity.

**To proceed, the following is needed:**

- Resolution of MOA data gap (DrugBank API query for complete pharmacological profile; currently a High-severity gap)
- Full safety review from the EMA Inlyta® SmPC — currently a **Blocking** data gap required before any Danish safety assessment
- Evaluation of named-patient or compassionate use pathway for access in Denmark (drug not currently marketed)
- Await results from NCT03595124 (axitinib + nivolumab in TFE3-fusion RCC, expected November 2026)
- Paediatric-specific dosing protocols and long-term toxicity monitoring plan (growth plate, thyroid function, cardiovascular effects) for the childhood RCC indication
- Confirmation of molecular diagnostic availability in Denmark (Xp11.2/TFE3 FISH or RNA fusion panel testing) as a prerequisite for patient selection
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

