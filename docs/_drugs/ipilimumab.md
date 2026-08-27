---
layout: default
title: Ipilimumab
parent: 僅模型預測 (L5)
nav_order: 243
evidence_level: L5
indication_count: 4
---

# Ipilimumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Ipilimumab: From Melanoma to Non-Cutaneous Melanoma

## One-Sentence Summary

Ipilimumab (Yervoy) is an anti-CTLA-4 immune checkpoint inhibitor originally developed and approved for the treatment of unresectable or metastatic cutaneous melanoma.
The TxGNN model predicts it may be effective for **non-cutaneous melanoma** (including uveal and mucosal subtypes), with **50 clinical trials** and **5 publications** currently supporting this direction.
The model also assigns its highest score to **choroideremia** (99.06%), though this finding is entirely unsupported by clinical or experimental evidence at this time.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Unresectable or metastatic melanoma (cutaneous) |
| Predicted New Indication | Non-Cutaneous Melanoma (uveal and mucosal subtypes) |
| TxGNN Prediction Score | 99.01% |
| Evidence Level | L1 |
| Denmark Market Status | Not marketed (per data pack — see note below) |
| Number of Marketing Authorisations | 0 (per data pack — see note below) |
| Recommended Decision | Proceed with Guardrails |

> **Important note on Danish market status:** The evidence pack records 0 marketing authorisations. This warrants verification: ipilimumab (Yervoy®) holds a centralised European Marketing Authorisation via the EMA, valid across all EU/EEA member states including Denmark. The discrepancy likely reflects a data gap in the current evidence pack. Clinicians should consult the EMA product page and the Danish Medicines Agency's (Lægemiddelstyrelsen) product database directly before drawing any conclusions about availability.

---

## Why is This Prediction Reasonable?

Melanoma — regardless of anatomical origin — is characterised by a tumour microenvironment in which T-cell activity is suppressed through CTLA-4-mediated immune tolerance. Ipilimumab binds and blocks CTLA-4, reversing this suppression, restoring tumour-infiltrating T-cell activity, and promoting the expansion of effector memory T cells. This mechanism is not inherently tissue-specific, which provides a biologically sound rationale for efficacy across all melanoma subtypes, including non-cutaneous variants.

Non-cutaneous melanoma subtypes — primarily uveal melanoma (arising from the choroid of the eye) and mucosal melanoma (arising from mucosal surfaces such as the oral cavity, GI tract, or genitourinary tract) — differ from cutaneous melanoma in important ways. They carry a lower tumour mutational burden (TMB), harbour distinct driver mutations (e.g., GNAQ/GNA11 in uveal melanoma), and show lower overall response rates to checkpoint inhibition compared with cutaneous disease. However, direct clinical evidence has confirmed ipilimumab activity in both uveal and mucosal subtypes (see PMID 24999899), and dual CTLA-4/PD-1 blockade with nivolumab + ipilimumab has become a recommended first-line option for these patients.

The TxGNN score of 99.01% for non-cutaneous melanoma is well grounded in this biological and clinical context. The prediction is corroborated by multiple completed Phase 3 randomised trials — including the pivotal NCT00324155 (ipilimumab + dacarbazine vs. placebo + dacarbazine, n=681) and NCT03068455 (nivolumab + ipilimumab adjuvant vs. nivolumab monotherapy, n=1,844) — providing the highest available level of clinical evidence (L1).

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|-----------|-------------|
| [NCT00324155](https://clinicaltrials.gov/study/NCT00324155) | Phase 3 | Completed | 681 | Pivotal RCT: ipilimumab 10 mg/kg + dacarbazine vs. dacarbazine + placebo in previously untreated Stage III/IV melanoma; formed a key basis for regulatory approval of ipilimumab in melanoma |
| [NCT03068455](https://clinicaltrials.gov/study/NCT03068455) | Phase 3 | Completed | 1,844 | Adjuvant nivolumab + ipilimumab vs. nivolumab monotherapy after complete resection of Stage IIIb/c/d or IV melanoma; the largest trial in this data set |
| [NCT02339571](https://clinicaltrials.gov/study/NCT02339571) | Phase 2/3 | Active, not recruiting | 600 | Nivolumab + ipilimumab ± sargramostim in unresectable Stage III/IV melanoma; long-term follow-up data ongoing until 2033 |
| [NCT02506153](https://clinicaltrials.gov/study/NCT02506153) | Phase 3 | Active, not recruiting | 1,301 | Pembrolizumab vs. physician/patient choice of high-dose interferon or ipilimumab in high-risk resected Stage III-IV melanoma; positions ipilimumab as a comparator in the adjuvant setting |
| [NCT01783938](https://clinicaltrials.gov/study/NCT01783938) | Phase 2 | Completed | 138 | Randomised: sequential nivolumab then ipilimumab in advanced/metastatic melanoma; directly supports dual checkpoint dosing strategy design |
| [NCT02905266](https://clinicaltrials.gov/study/NCT02905266) | Phase 3 | Completed | 106 | Phase IIIb: multiple administration regimens of nivolumab + ipilimumab in previously untreated unresectable/metastatic melanoma; informs dosing schedule optimisation |
| [NCT02320058](https://clinicaltrials.gov/study/NCT02320058) | Phase 2 | Completed | 119 | Nivolumab + ipilimumab in melanoma metastatic to the brain; directly relevant to advanced non-cutaneous melanoma with CNS involvement |
| [NCT01950390](https://clinicaltrials.gov/study/NCT01950390) | Phase 2 | Completed | 169 | Randomised: ipilimumab ± bevacizumab in unresectable Stage III/IV melanoma; evaluates VEGF/immune checkpoint combination benefit |
| [NCT00972933](https://clinicaltrials.gov/study/NCT00972933) | Early Phase 1 | Completed | 59 | Neoadjuvant ipilimumab in Stage IIIB-C melanoma; important immunogenicity and biomarker data in the neoadjuvant setting |
| [NCT07230613](https://clinicaltrials.gov/study/NCT07230613) | Phase 2 | Recruiting | 50 | Neoadjuvant intratumoral anti-CTLA-4 + anti-PD-1 in localised melanoma; novel delivery route exploring reduced systemic toxicity with maintained local efficacy |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [24999899](https://pubmed.ncbi.nlm.nih.gov/24999899/) | 2014 | Retrospective cohort | The Medical Journal of Australia | Efficacy and tolerability of ipilimumab across cutaneous, uveal, and mucosal melanoma subtypes in an Australian clinical setting; the most directly relevant publication for non-cutaneous melanoma activity |
| [37887546](https://pubmed.ncbi.nlm.nih.gov/37887546/) | 2023 | Real-world evidence | Current Oncology | Multi-centre retrospective cohort comparing anti-PD-1 monotherapy vs. combination with ipilimumab across age groups in advanced melanoma; real-world comparative effectiveness data |
| [29466692](https://pubmed.ncbi.nlm.nih.gov/29466692/) | 2018 | Clinical review | Discovery Medicine | Comprehensive update on anti-PD-1 mAbs as monotherapy or combined with ipilimumab; summarises mature Phase 3 survival data and current treatment landscape |
| [28183255](https://pubmed.ncbi.nlm.nih.gov/28183255/) | 2018 | Systematic review | Current Cancer Drug Targets | Systematic review of Phase I–III adjuvant melanoma trials (2000–2015) including ipilimumab; reviews evidence base at the time of ipilimumab's introduction to adjuvant setting |
| [40236344](https://pubmed.ncbi.nlm.nih.gov/40236344/) | 2025 | Case report | Cureus | Case of colonic metastasis from melanoma treated with systemic immunotherapy; highlights immune-related gastrointestinal adverse events (perforation) relevant to checkpoint inhibitor safety monitoring |

---

## Cytotoxicity

Ipilimumab is an antineoplastic agent in the immune checkpoint inhibitor class. It is used for the treatment of malignant melanoma and is classified as an immunotherapy rather than a conventional cytotoxic drug.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Immunotherapy — immune checkpoint inhibitor (anti-CTLA-4 IgG1 monoclonal antibody); not a conventional cytotoxic agent |
| Myelosuppression Risk | Low — ipilimumab is not associated with haematological toxicity in the conventional sense; immune-related adverse events (irAEs) are the primary toxicity concern |
| Emetogenicity Classification | Minimal — not classified as emetogenic; nausea may occur as part of an immune-related adverse event rather than direct chemotherapy-related emetogenicity |
| Monitoring Items | Liver function (ALT, AST, bilirubin), thyroid function (TSH, fT4), adrenal function (morning cortisol, ACTH), full blood count, renal function, blood glucose; clinical monitoring for irAEs: dermatitis, colitis, hepatitis, hypophysitis, pneumonitis, uveitis |
| Handling Protection | Standard biohazard precautions for monoclonal antibody preparations; **does not require** the full cytotoxic drug handling precautions (closed-system drug transfer devices, chemotherapy personal protective equipment) mandated for conventional cytotoxic chemotherapy |

---

## Safety Considerations

Detailed warnings and contraindications are not available in this evidence pack. Please refer to the approved Summary of Product Characteristics (SmPC) for Yervoy® for complete safety information.

> Based on the established clinical profile of ipilimumab, clinicians should be particularly aware of:
> - **Immune-related adverse events (irAEs):** colitis, hepatitis, dermatitis, hypophysitis, adrenal insufficiency, and pneumonitis — managed with high-dose corticosteroids and, in severe cases, permanent discontinuation
> - **Ocular irAEs:** uveitis and other inflammatory eye conditions have been reported — this is especially relevant given the choroideremia prediction discussed below, where pre-existing retinal pathology would represent a significant safety concern
> - **No drug-drug interaction data** is available in this evidence pack (DDI query returned no results)

---

## Secondary TxGNN Prediction: Choroideremia — Hold

The TxGNN model assigns its highest score in this evidence pack to **choroideremia** (99.06%), placing it above non-cutaneous melanoma by a small margin. Choroideremia is a rare X-linked inherited retinal dystrophy caused by mutations in the CHM gene (Xq21.2), leading to progressive degeneration of retinal pigment epithelium (RPE) and photoreceptors due to Rab Escort Protein-1 (REP-1) deficiency.

**Evidence level: L5 — model prediction only; no clinical or experimental evidence exists.**

There is no established biological link between ipilimumab's CTLA-4 blockade mechanism and the primary monogenic pathology of choroideremia. The TxGNN score likely reflects indirect connections within the knowledge graph (e.g., shared disease–protein interaction networks relating to the ocular immune microenvironment or the eye's immune-privileged status), rather than a direct mechanistic relationship. No hypothesis-generating publications, animal studies, or exploratory clinical studies support this application.

Importantly, ipilimumab can itself cause immune-related uveitis, indicating a dual — and potentially harmful — immune impact on ocular tissue. This raises significant safety concerns about its use in patients with pre-existing retinal disease.

**Recommendation: Hold** — not appropriate for clinical pursuit without substantial preclinical mechanistic investigation.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** *(for non-cutaneous melanoma)*

**Rationale:**
Multiple completed Phase 3 randomised trials provide Level 1 evidence supporting ipilimumab — particularly in combination with nivolumab — for the treatment of advanced melanoma including non-cutaneous subtypes. Direct evidence from published literature confirms activity in uveal and mucosal melanoma specifically.

**To proceed, the following is needed:**

- **Verify Danish market authorisation status:** Cross-check Yervoy® registration with the EMA and Lægemiddelstyrelsen databases; the 0 authorisations recorded in this evidence pack appears inconsistent with the known EMA centralised authorisation
- **Obtain the approved SmPC:** Review EU-approved indications to clarify whether non-cutaneous melanoma subtypes (uveal, mucosal) are explicitly included or are off-label use in Denmark
- **Document the mechanism of action formally:** MOA data is listed as a data gap in this evidence pack; obtain from DrugBank API or the SmPC pharmacodynamics section
- **Retrieve key warnings and contraindications:** Download and parse the Yervoy® SmPC for the safety section; currently blocking (Data Gap severity: Blocking)
- **Subtype-specific response rate data:** Uveal melanoma response rates to ipilimumab monotherapy are substantially lower than cutaneous melanoma; formal patient-selection criteria differentiating uveal vs. mucosal vs. other non-cutaneous subtypes should be defined before treatment initiation
- **Immune-related adverse event management protocol:** Establish a clinical pathway for irAE monitoring and management, with particular attention to ocular irAEs given the uveal melanoma patient population
- **For choroideremia prediction:** Preclinical mechanistic studies are required before any clinical consideration; this prediction should be classified as Hold pending further investigation

---

*This report is intended for research reference purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before application. This report should be read in conjunction with the approved Summary of Product Characteristics and current clinical guidelines.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

