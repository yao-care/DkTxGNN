---
layout: default
title: Regorafenib
parent: 僅模型預測 (L5)
nav_order: 369
evidence_level: L5
indication_count: 10
---

# Regorafenib
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

# Regorafenib: From Metastatic Colorectal Cancer to Liposarcoma

## One-Sentence Summary

Regorafenib is an oral multikinase inhibitor originally developed for metastatic colorectal cancer, GIST and hepatocellular carcinoma. The TxGNN model predicts it may be effective for **Liposarcoma**, with **2 clinical trials** and **9 publications** available — however, the two completed Phase II randomised trials that specifically tested this indication both found **no clinical benefit** in liposarcoma patients, directly contradicting the model's prediction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Metastatic colorectal cancer, GIST, hepatocellular carcinoma (per international product labeling; no Danish marketing authorisation on file to confirm locally) |
| Predicted New Indication | Liposarcoma |
| TxGNN Prediction Score | 99.76% |
| Evidence Level | L2 (2 completed Phase II RCTs directly addressing this indication — but with negative results) |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Regorafenib is an oral multikinase inhibitor targeting angiogenic (VEGFR1-3, TIE2), stromal (PDGFR-β, FGFR) and oncogenic receptor tyrosine kinases (KIT, RET, RAF) (per literature evidence, PMID 30069758). Its original approval was built on this broad antiangiogenic/antiproliferative profile in metastatic colorectal cancer, GIST and hepatocellular carcinoma.

Soft tissue sarcomas, including liposarcoma, are highly vascularised tumours in which angiogenesis signalling plays a key role in tumour biology (per REGOSARC trial protocol, PMID 25884155). This provided the mechanistic rationale for testing regorafenib across multiple sarcoma subtypes, and it is this class-level plausibility that the TxGNN model appears to be capturing.

**However, mechanistic plausibility did not translate into clinical benefit for this specific subtype.** The REGOSARC trial (PMID 27751846) showed regorafenib improved outcomes in leiomyosarcoma and synovial sarcoma but explicitly **did not** show benefit in the liposarcoma cohort. The independent SARC024 trial (PMID 32701199) confirmed this finding in a treatment-refractory liposarcoma population and concluded that "routine use of regorafenib in this patient population" is not supported. This is a case where a strong knowledge-graph-based mechanistic signal is directly contradicted by dedicated randomised clinical trial data.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01900743](https://clinicaltrials.gov/study/NCT01900743) | Phase 2 | Completed | 219 | REGOSARC: international, randomised, double-blind, placebo-controlled trial of regorafenib in metastatic/unresectable soft tissue sarcoma after anthracycline failure; liposarcoma was one of five predefined cohorts |
| [NCT02048371](https://clinicaltrials.gov/study/NCT02048371) | Phase 2 | Completed | 131 | SARC024: blanket protocol studying oral regorafenib across selected sarcoma subtypes, including a dedicated liposarcoma cohort |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27751846](https://pubmed.ncbi.nlm.nih.gov/27751846/) | 2016 | RCT | The Lancet. Oncology | REGOSARC: regorafenib improved progression-free survival vs placebo in non-adipocytic soft tissue sarcoma, but **not** in liposarcoma |
| [32701199](https://pubmed.ncbi.nlm.nih.gov/32701199/) | 2020 | RCT | The Oncologist | SARC024 liposarcoma cohort: results **do not support routine use** of regorafenib in treatment-refractory liposarcoma |
| [29902612](https://pubmed.ncbi.nlm.nih.gov/29902612/) | 2018 | RCT (post-cross-over analysis) | European Journal of Cancer | Updated REGOSARC analysis confirms lack of efficacy in liposarcoma even after placebo-to-regorafenib cross-over |
| [28295221](https://pubmed.ncbi.nlm.nih.gov/28295221/) | 2017 | RCT post-hoc analysis | Cancer | Q-TWiST analysis of REGOSARC; quality-adjusted clinical benefit concentrated in non-adipocytic cohorts |
| [25884155](https://pubmed.ncbi.nlm.nih.gov/25884155/) | 2015 | Study protocol | BMC Cancer | REGOSARC trial design; rationale based on angiogenesis's role in sarcoma biology |
| [29931504](https://pubmed.ncbi.nlm.nih.gov/29931504/) | 2018 | Review | Targeted Oncology | Reviews regorafenib's evolving role across soft tissue sarcoma subtypes, including liposarcoma |
| [33290314](https://pubmed.ncbi.nlm.nih.gov/33290314/) | 2021 | Retrospective study | Anti-Cancer Drugs | Anlotinib in WDLS/DDLS; cites regorafenib as an approved TKI for non-adipocytic STS, not liposarcoma specifically |
| [40975452](https://pubmed.ncbi.nlm.nih.gov/40975452/) | 2025 | Review | Critical Reviews in Oncology/Hematology | Reviews maintenance therapy strategies after first-line treatment of advanced STS |
| [26266019](https://pubmed.ncbi.nlm.nih.gov/26266019/) | 2015 | Case report | Rare Tumors | Pazopanib case in Ewing sarcoma; cited as part of the rationale for including a liposarcoma arm in SARC024 |

---

## Denmark Market Information

Regorafenib currently has no marketing authorisation on file in Denmark (0 authorisations recorded; market status: not marketed).

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (oral multikinase inhibitor: VEGFR1-3, TIE2, PDGFR-β, FGFR, KIT, RET, RAF) |
| Myelosuppression Risk | Low–Moderate — literature evidence for this drug class emphasises hand-foot skin reaction, hypertension and diarrhoea over myelosuppression (PMID 30069758); no direct haematologic toxicity data in this evidence pack |
| Emetogenicity Classification | Low (typical for oral multikinase TKIs) |
| Monitoring Items | Blood pressure (VEGFR-inhibition-related hypertension, PMID 36583425), liver function (hepatotoxicity risk across anti-angiogenic TKIs, PMID 23981115), skin examination for hand-foot skin reaction (PMID 23700287), CBC |
| Handling Protection | Oral targeted anticancer agent — follow institutional oral antineoplastic handling protocols; local TFDA/SmPC-specific handling requirements are a data gap pending label review |

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information. TFDA-equivalent label warnings/contraindications and DDI data were not available in this evidence pack (flagged as a **Blocking** data gap — DG001 — preventing initial safety screening).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- Regorafenib has no existing marketing authorisation in Denmark, and local SmPC safety data is a Blocking gap that prevents even an initial safety screen.
- More importantly, the two completed Phase II RCTs that specifically tested regorafenib in liposarcoma (REGOSARC, SARC024) both found **no clinical benefit** in this subtype, directly contradicting the TxGNN model's high prediction score. This is a case where the model's knowledge-graph-level signal does not hold up against dedicated clinical trial evidence.

**To proceed, the following is needed:**
- TFDA/SmPC warnings, contraindications and drug interaction data (currently Blocking gap, DG001)
- Formal mechanism-of-action documentation (DrugBank MOA field, DG002)
- If pursued further, reframe as a research question around *why* TxGNN scores this indication highly despite negative trial data (e.g., biomarker-selected subpopulations, combination regimens) rather than pursuing liposarcoma monotherapy directly
- Confirm whether any EU/EMA centralised authorisation exists for regorafenib under its approved indications, which would affect off-label pathway feasibility in Denmark
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

