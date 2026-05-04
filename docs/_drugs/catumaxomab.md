---
layout: default
title: Catumaxomab
parent: 僅模型預測 (L5)
nav_order: 97
evidence_level: L5
indication_count: 10
---

# Catumaxomab
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

# Catumaxomab: From Malignant Ascites to Severe Nonproliferative Diabetic Retinopathy

## One-Sentence Summary

Catumaxomab (Removab) is a trifunctional bispecific antibody originally approved in the EU for the treatment of malignant ascites in patients with EpCAM-positive carcinomas, though the marketing authorisation was voluntarily withdrawn in 2017 for commercial reasons unrelated to safety or efficacy.
The TxGNN model predicts it may be effective for **Severe Nonproliferative Diabetic Retinopathy** (score: 99.64%), yet **0 clinical trials** and **0 publications** currently support this direction.
All predictions in this batch carry an **L5 evidence classification**, meaning they rest solely on model inference with no corroborating human study data; the overall recommendation is **Hold**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Malignant ascites in patients with EpCAM-positive carcinomas (EU/EMA approved, 2009; withdrawn 2017) |
| Predicted New Indication | Severe Nonproliferative Diabetic Retinopathy |
| TxGNN Prediction Score | 99.64% |
| Evidence Level | L5 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Catumaxomab is a trifunctional bispecific antibody (~150 kDa) designed to simultaneously engage three cell types: it binds **EpCAM** (Epithelial Cell Adhesion Molecule) on tumour cells, **CD3ε** on T lymphocytes, and **Fcγ receptors I/IIa/III** on accessory immune cells (macrophages, NK cells, dendritic cells) via its hybrid rat/mouse IgG2a/IgG2b Fc region. This trispecific engagement forms an immunological synapse that redirects cytotoxic T cells and accessory immune cells to kill EpCAM-expressing tumour cells — a mechanism that is tightly anchored to EpCAM-positive epithelial malignancies.

Severe nonproliferative diabetic retinopathy (severe NPDR) is a microvascular complication of diabetes characterised by pericyte dropout, capillary closure, VEGF-mediated vascular hyperpermeability, advanced glycation end-product (AGE) accumulation, and oxidative stress. These pathological mechanisms are entirely distinct from EpCAM/CD3-mediated immune cell recruitment. Although EpCAM is expressed at trace levels in retinal progenitor cells during embryogenesis, it is not meaningfully expressed in the diseased retinal microvasculature, and no therapeutic hypothesis links T-cell bridging to NPDR pathology. Furthermore, Catumaxomab's large molecular weight renders blood–retinal barrier penetration negligible following systemic administration, making pharmacokinetic delivery to the target tissue extremely unlikely.

The high TxGNN prediction score for diabetic retinopathy-spectrum conditions (ranks 1–6) most plausibly reflects indirect connectivity through shared **diabetes-related nodes** in the underlying knowledge graph rather than direct biological plausibility. Among all unique predictions in this batch, **kidney pelvis sarcomatoid transitional cell carcinoma** (ranks 9–10, score 98.29%) represents the most mechanistically credible candidate: urothelial/transitional cell carcinomas are known to express EpCAM in 40–70% of cases, aligning with Catumaxomab's original target profile. However, sarcomatoid differentiation commonly involves epithelial-to-mesenchymal transition (EMT) with significant EpCAM downregulation, which would limit expected efficacy even in this more plausible indication.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Catumaxomab in any of the predicted indications. Searches across ClinicalTrials.gov and WHO ICTRP returned zero results for all indication pairs queried (as of 2026-03-24).

---

## Literature Evidence

Currently no related literature available. PubMed searches combining "Catumaxomab" with each of the five predicted indications (severe NPDR, drug-induced osteoporosis, diabetic retinopathy, diabetic cataract, kidney pelvis sarcomatoid TCC) returned zero results.

---

## Denmark Market Information

Catumaxomab holds **no marketing authorisations** in Denmark. For contextual reference, the drug was previously centrally authorised by the EMA as **Removab** (EU/1/09/512/001–003) for intraperitoneal treatment of malignant ascites in patients with EpCAM-positive carcinomas who have no standard therapy available or for whom no further standard therapy is feasible. This authorisation was withdrawn by the marketing authorisation holder (Neovii Biotech GmbH, previously Fresenius Biotech) in **June 2017** for commercial reasons; the EMA confirmed the withdrawal was not related to safety or efficacy concerns.

No national authorisations from the Danish Medicines Agency (Lægemiddelstyrelsen) were identified.

---

## Cytotoxicity

Catumaxomab is classified as an antineoplastic agent (immunotherapy targeting EpCAM-positive cancer cells) and this section applies.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted immunotherapy — Trifunctional bispecific antibody (not conventional cytotoxic) |
| Myelosuppression Risk | Low to moderate; immune-mediated cytopenias possible via cytokine release and accessory cell activation |
| Emetogenicity Classification | Low (IV/intraperitoneal biological agent; nausea reported primarily as infusion-related systemic reaction) |
| Monitoring Items | Full blood count with differential, liver function tests (ALT, AST, bilirubin), renal function, serum cytokines/CRP (cytokine release syndrome surveillance), body temperature |
| Handling Protection | Follow institutional handling guidelines for biological/immunological agents; standard aseptic precautions apply; no alkylating/DNA-damaging risk, but protein-based biological hazard protocols recommended |

---

## Safety Considerations

Detailed SmPC-level warning and contraindication data were not available in this evidence pack (classified as a data gap at the time of analysis). Based on known clinical pharmacology from the original EU approval, the following safety considerations are recognised:

- **Cytokine Release Syndrome (CRS)**: The most clinically significant toxicity associated with Catumaxomab. Systemic inflammatory reactions — including fever, chills, nausea, vomiting, and hypotension — were frequently reported in clinical trials, particularly during and following intraperitoneal infusion. Severity can range from grade 1–2 to potentially life-threatening.
- **Hepatotoxicity**: Transient elevations in liver enzymes (ALT, AST, bilirubin) were observed in a substantial proportion of patients in pivotal trials; close hepatic monitoring is warranted.
- **Infections**: Immune activation and catheter-related procedures increase infection risk.
- **Drug–Drug Interactions**: No DDI data identified in this review (query returned zero results). Caution is advised with concomitant immunosuppressants that may blunt therapeutic T-cell activation, or with agents that potentiate cytokine release.

Please refer to the approved Summary of Product Characteristics (SmPC) and the EMA European Public Assessment Report (EPAR) for Removab for comprehensive safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Every TxGNN prediction generated for Catumaxomab in this batch is classified as **L5** (computational model prediction only), supported by neither clinical trials nor published literature. The top-ranked indications — covering the diabetic retinopathy spectrum and drug-induced osteoporosis — are **mechanistically implausible** given Catumaxomab's EpCAM/CD3 immune-bridging mechanism, its inability to penetrate the blood–retinal barrier, and the complete absence of any EpCAM-related pathology in these conditions. Advancing any of these indications without preclinical mechanistic validation would not meet a minimum scientific justification threshold.

**To proceed, the following is needed:**

- **Mechanistic feasibility review**: Formal assessment by a clinical pharmacologist of whether any predicted indication involves EpCAM-expressing target tissue accessible to a ~150 kDa biologic
- **EpCAM expression profiling**: For the most plausible candidate (kidney pelvis sarcomatoid TCC), tissue biopsy data confirming EpCAM expression in sarcomatoid-differentiated urothelial carcinoma is a prerequisite before any further investment
- **Preclinical evidence**: At minimum, in vitro cytotoxicity data in the proposed new indication's cell lines using Catumaxomab; in vivo xenograft models if in vitro signal is positive
- **Safety profile completion**: Retrieval and structured analysis of the full Removab SmPC and EPAR to address the current blocking data gap (DG001)
- **MOA documentation**: Structured extraction of Catumaxomab's mechanism of action from DrugBank (DG002) to enable proper mechanistic scoring
- **Regulatory pathway assessment**: Given the prior EMA withdrawal (commercial, not safety-driven), re-engagement would require a new Marketing Authorisation Application; early scientific advice from EMA or Lægemiddelstyrelsen is recommended before committing preclinical resources
- **Knowledge graph audit**: Investigate the indirect graph paths driving high TxGNN scores for diabetic indications to determine whether a structural bias in the knowledge graph is producing systematically inflated scores for diabetes-adjacent nodes
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

