---
layout: default
title: Sirolimus
parent: 僅模型預測 (L5)
nav_order: 402
evidence_level: L5
indication_count: 10
---

# Sirolimus
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

# Sirolimus: From Renal Transplant Rejection Prophylaxis to Liposarcoma

## One-Sentence Summary

> Sirolimus (rapamycin) is an mTOR inhibitor originally developed as an immunosuppressant to prevent organ rejection in renal transplantation.
> The TxGNN model predicts it may be effective for **Liposarcoma**,
> with **5 clinical trials** and **12 publications** currently supporting this direction — though most of the trial evidence comes from related mTOR inhibitors (temsirolimus, everolimus, ridaforolimus) rather than Sirolimus itself.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Immunosuppression / prophylaxis of renal transplant rejection (well-established use; specific Danish regulatory indication text is not confirmed in the available data) |
| Predicted New Indication | Liposarcoma |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L2 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack. Based on known pharmacology, Sirolimus is a **mammalian target of rapamycin (mTOR) inhibitor** ("rapalog"), a drug class whose efficacy in preventing renal transplant rejection is well established, and which mechanistically may be applicable to certain soft-tissue sarcomas.

Dedifferentiated liposarcoma frequently shows activation of the PI3K–Akt–mTOR signalling pathway (PMID 26518767), and mTOR inhibition can block this downstream proliferative signal — giving the prediction a clear molecular biology rationale. However, of the 5 clinical trials identified for this indication, only **one** (NCT02821507) uses Sirolimus itself directly; the remaining four involve related agents in the same drug class (temsirolimus, everolimus, ridaforolimus). This means the supporting evidence is largely a **class-effect inference** rather than direct, drug-specific proof for Sirolimus in liposarcoma.

It is also worth noting that among the other candidate indications generated for Sirolimus in this evidence pack (not detailed in this report), **lymphangioleiomyomatosis (LAM)** and **PEComa/angiomyolipoma** show substantially more direct, disease-specific Sirolimus evidence — including a completed Phase 3 RCT (NCT00414648, MILES trial) for LAM — and may warrant separate, higher-priority evaluation.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02821507](https://clinicaltrials.gov/study/NCT02821507) | Phase 2 | Completed | 70 | Single-arm trial of **Sirolimus** + cyclophosphamide in metastatic/unresectable myxoid liposarcoma and chondrosarcoma — direct use of Sirolimus itself, indication-matched |
| [NCT00093080](https://clinicaltrials.gov/study/NCT00093080) | Phase 2 | Completed | 216 | Large trial of ridaforolimus (same-class mTOR inhibitor, not Sirolimus) in advanced sarcoma |
| [NCT01614795](https://clinicaltrials.gov/study/NCT01614795) | Phase 2 | Completed | 46 | Cixutumumab + temsirolimus (same-class, not Sirolimus) in pediatric recurrent/refractory sarcoma |
| [NCT00949325](https://clinicaltrials.gov/study/NCT00949325) | Phase 1/2 | Completed | 24 | Torisel (temsirolimus) + liposomal doxorubicin in advanced soft tissue and bone sarcoma |
| [NCT03114527](https://clinicaltrials.gov/study/NCT03114527) | Phase 2 | Active, not recruiting | 48 | Ribociclib + everolimus (same-class) in advanced dedifferentiated liposarcoma and leiomyosarcoma |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37967116](https://pubmed.ncbi.nlm.nih.gov/37967116/) | 2024 | Single-arm clinical trial report | Clin Cancer Res | Ribociclib + everolimus in dedifferentiated liposarcoma/leiomyosarcoma; synergistic mTOR/CDK4-pathway inhibition |
| [26093731](https://pubmed.ncbi.nlm.nih.gov/26093731/) | 2015 | Cohort | Transplantation Proceedings | Cancer screening in renal transplant patients on long-term immunosuppression, including mTOR inhibitors |
| [16434506](https://pubmed.ncbi.nlm.nih.gov/16434506/) | 2006 | Cohort | J Am Soc Nephrol | Sirolimus after early cyclosporine withdrawal reduced cancer risk vs. cyclosporine in renal transplant recipients |
| [39796641](https://pubmed.ncbi.nlm.nih.gov/39796641/) | 2024 | Review | Cancers | Review of novel therapeutics in soft tissue sarcoma, including mTOR-pathway approaches |
| [37222206](https://pubmed.ncbi.nlm.nih.gov/37222206/) | 2023 | Review | Curr Opin Oncol | Review of new targeted treatments for advanced sarcomas |
| [20497911](https://pubmed.ncbi.nlm.nih.gov/20497911/) | 2010 | Review | Bulletin du Cancer | Review of targeted treatment strategies for rare connective tissue tumours and sarcomas by molecular subgroup |
| [26518767](https://pubmed.ncbi.nlm.nih.gov/26518767/) | 2016 | Mechanism study | Tumour Biology | Analysis of 99 dedifferentiated liposarcoma specimens showing Akt/mTOR and MAPK pathway activation |
| [37400145](https://pubmed.ncbi.nlm.nih.gov/37400145/) | 2023 | Preclinical | Cancer Genomics Proteomics | Chloroquine + rapamycin synergistically inhibits autophagy, effective in well-differentiated liposarcoma models |
| [36309387](https://pubmed.ncbi.nlm.nih.gov/36309387/) | 2022 | Preclinical (PDX model) | In Vivo | Chloroquine + rapamycin arrests tumour growth in a patient-derived xenograft model of dedifferentiated liposarcoma |
| [25519700](https://pubmed.ncbi.nlm.nih.gov/25519700/) | 2015 | Preclinical | Mol Cancer Ther | ATP-competitive mTOR kinase inhibitor MLN0128 shows antitumor activity in bone/soft-tissue sarcoma models |

---

## Denmark Market Information

Sirolimus is **not currently marketed in Denmark** — no national (Lægemiddelstyrelsen) or centralised (EMA) marketing authorisations are recorded in the evidence pack (0 licenses on file).

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information. No drug interaction, warning, or contraindication data were available for review in this evidence pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- Sirolimus is not currently marketed in Denmark, and a **blocking data gap** exists for SmPC warnings/contraindications, meaning an initial safety assessment cannot yet be performed.
- Evidence for the liposarcoma indication specifically is class-effect based: only 1 of 5 trials uses Sirolimus itself directly, and the drug's own original indication/MOA data could not be confirmed from available sources.

**To proceed, the following is needed:**
- Obtain SmPC / product safety data (warnings, contraindications, drug interactions) from Lægemiddelstyrelsen or EMA
- Confirm the drug's approved original indication and mechanism of action via DrugBank or regulatory sources
- Clarify access pathway given the drug is not marketed in Denmark (e.g., named-patient/off-label import)
- Consider prioritizing evaluation of related predicted indications (lymphangioleiomyomatosis, PEComa/angiomyolipoma), where Sirolimus has more direct and mature supporting evidence than for liposarcoma
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

