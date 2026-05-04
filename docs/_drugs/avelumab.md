---
layout: default
title: Avelumab
parent: 僅模型預測 (L5)
nav_order: 52
evidence_level: L5
indication_count: 10
---

# Avelumab
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

# Avelumab: From Merkel Cell Carcinoma to HHV-8-Related Tumour

## One-Sentence Summary

Avelumab (Bavencio) is a fully human anti-PD-L1 monoclonal antibody approved internationally for Merkel cell carcinoma and urothelial carcinoma maintenance therapy, though it is not currently registered in Denmark.
The TxGNN model predicts it may be effective for **HHV-8-related tumours** (including Kaposi's sarcoma, primary effusion lymphoma, and multicentric Castleman disease), with a prediction confidence of **99.97%**.
At present, **no dedicated clinical trials** or **publications** directly investigate this drug–disease combination, though the mechanistic rationale is substantiated by class-level evidence from the related checkpoint inhibitor pembrolizumab.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Merkel cell carcinoma; urothelial carcinoma maintenance — globally approved (EMA/FDA); not registered in Denmark |
| Predicted New Indication | HHV-8-Related Tumour (Kaposi's sarcoma, Primary Effusion Lymphoma, Castleman Disease) |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L4 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known information, Avelumab is a fully human IgG1 monoclonal antibody that blocks the interaction between PD-L1 and its receptors PD-1 and CD80, thereby restoring cytotoxic CD8+ T cell and NK cell activity against tumour cells. Critically, unlike other checkpoint inhibitors, Avelumab's IgG1 Fc region retains **antibody-dependent cell-mediated cytotoxicity (ADCC)** activity — enabling direct tumour cell killing through NK cell engagement, a second mechanism of action beyond checkpoint blockade alone.

Human herpesvirus 8 (HHV-8) is the causative agent of Kaposi's sarcoma, primary effusion lymphoma (PEL), and multicentric Castleman disease. HHV-8-infected malignant cells are known to upregulate PD-L1 expression as an immune evasion strategy, suppressing both anti-viral and anti-tumour immune surveillance by CD8+ T cells and NK cells. Blocking PD-L1 with Avelumab could therefore restore immune-mediated killing of HHV-8-harbouring cells through two complementary pathways — checkpoint disinhibition and direct ADCC — potentially offering a dual advantage over anti-PD-1 agents in this setting.

Class-level biological plausibility is supported by the fact that pembrolizumab (an anti-PD-1 antibody) has entered Phase 2 clinical evaluation in Kaposi's sarcoma (NCT02494960). This precedent indicates that the broader immune checkpoint inhibitor class is considered mechanistically sound for HHV-8-associated malignancies by the clinical research community. TxGNN's high prediction score of 99.97% reflects this mechanistic alignment as captured in the knowledge graph, even in the absence of Avelumab-specific trial data.

---

## Clinical Trial Evidence

Currently no related clinical trials registered specifically for Avelumab in HHV-8-related tumours.

> **Class-level note:** The related anti-PD-1 agent pembrolizumab has an ongoing Phase 2 trial in Kaposi's sarcoma — [NCT02494960](https://clinicaltrials.gov/study/NCT02494960) — providing indirect evidence that immune checkpoint inhibition is biologically feasible in this disease context.

---

## Literature Evidence

Currently no related literature available for Avelumab specifically in HHV-8-related tumours.

---

## Cytotoxicity

Avelumab is an oncology immunotherapy agent (anti-PD-L1 monoclonal antibody). This section applies.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Immunotherapy — immune checkpoint inhibitor (anti-PD-L1 IgG1 monoclonal antibody with ADCC activity); not a conventional cytotoxic agent |
| Myelosuppression Risk | Low for direct myelosuppression; immune-mediated haematological events (e.g. immune thrombocytopenia, haemolytic anaemia) are possible irAEs |
| Emetogenicity Classification | Minimal |
| Monitoring Items | Full blood count (CBC with differential), liver function tests (ALT, AST, bilirubin), renal function (creatinine), thyroid function (TSH, free T4), fasting blood glucose, cortisol (adrenal function); infusion reaction monitoring during and after administration |
| Handling Protection | Standard monoclonal antibody handling precautions apply; dedicated cytotoxic drug handling regulations are not required |

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

> **Important clinical note:** As a checkpoint inhibitor, Avelumab carries class-specific immune-related adverse events (irAEs) that require active monitoring and management. These include, but are not limited to: immune-mediated pneumonitis, colitis, hepatitis, nephritis, endocrinopathies (hypothyroidism, hyperthyroidism, adrenal insufficiency, type 1 diabetes mellitus), and infusion-related reactions. Practitioners should follow current immunotherapy toxicity management guidelines (e.g. ESMO/ASCO irAE guidelines). The Bavencio SmPC approved by EMA provides the authoritative full safety profile.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence for Avelumab specifically in HHV-8-related tumours is currently at the preclinical/mechanistic level only (L4), with no registered clinical trials and no published literature directly investigating this drug–disease combination. The mechanistic basis is scientifically sound — HHV-8-driven PD-L1 upregulation is well described, and class-level evidence from pembrolizumab in Kaposi's sarcoma supports the plausibility of checkpoint inhibition in this setting — but drug-specific clinical validation is entirely absent.

**To proceed, the following is needed:**
- Systematic review of the existing pembrolizumab Kaposi's sarcoma trial (NCT02494960) results to assess class-level transferability to Avelumab
- Translational or preclinical data specifically addressing whether Avelumab's ADCC mechanism confers additional benefit over anti-PD-1 agents in HHV-8-associated malignancies
- PD-L1 expression prevalence data across the spectrum of HHV-8-related tumour subtypes (Kaposi's sarcoma, PEL, Castleman disease), including assessment in immunocompromised subpopulations (HIV-positive patients)
- Full SmPC review and safety gap remediation: the current Evidence Pack is missing key safety data (TFDA/EMA warnings, contraindications, drug–drug interactions) which are classified as blocking for formal safety pre-screening (DG001)
- Danish epidemiological feasibility assessment: HHV-8-related malignancies are uncommon in Denmark; patient population sizing is needed to evaluate clinical and health-economic viability
- Registration pathway analysis: Avelumab is not currently marketed in Denmark; any clinical use would require a named patient programme, compassionate use authorisation, or a prospective clinical trial
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

