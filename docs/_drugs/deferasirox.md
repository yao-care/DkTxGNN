---
layout: default
title: Deferasirox
parent: 僅模型預測 (L5)
nav_order: 133
evidence_level: L5
indication_count: 10
---

# Deferasirox
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

# Deferasirox: From Chronic Iron Overload to HIV Infectious Disease

## One-Sentence Summary

Deferasirox is an oral iron chelator used internationally for chronic iron overload due to frequent blood transfusions (e.g., in β-thalassaemia and myelodysplastic syndrome).
The TxGNN model predicts it may be effective for **HIV Infectious Disease**, with a prediction score of 99.40%.
Currently, **0 clinical trials** and **2 publications** support this direction — both at the preclinical, mechanistic level only.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Chronic iron overload due to frequent blood transfusions (transfusional haemosiderosis) |
| Predicted New Indication | HIV Infectious Disease |
| TxGNN Prediction Score | 99.40% |
| Evidence Level | L4 (preclinical/mechanistic studies only) |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data from DrugBank was not available for this report. Based on established pharmacology, Deferasirox is a once-daily oral iron chelator that selectively binds trivalent iron (Fe³⁺) with high affinity, promoting iron excretion via urine and faeces. Its proven efficacy in reducing systemic iron burden in transfusion-dependent patients (β-thalassaemia, MDS) is the foundation from which this repurposing hypothesis is derived.

Iron metabolism plays a fundamental role in the HIV-1 replication cycle. Endolysosomal free iron facilitates correct folding of the HIV-1 Tat protein, enabling it to transactivate the LTR promoter — a critical step that drives viral gene expression. By chelating intracellular free iron within endolysosomes, Deferasirox may induce abnormal oligomerization of HIV-1 Tat, thereby disrupting LTR transactivation and suppressing viral replication. This constitutes a potential **host-directed antiviral therapy (HDT)** mechanism that does not overlap with any existing antiretroviral (ARV) drug target, suggesting theoretical potential for combination use.

It must be emphasised that this mechanistic hypothesis rests solely on in vitro evidence. No animal model studies or human clinical data have been generated to date. At this stage, the prediction is best classified as an early research question rather than a clinical development candidate.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [34550543](https://pubmed.ncbi.nlm.nih.gov/34550543/) | 2021 | In vitro mechanistic study | Journal of Neurovirology | Endolysosomal iron promotes HIV-1 Tat-mediated LTR transactivation; chelation of endolysosomal iron increases HIV-1 Tat oligomerization and β-catenin expression, restricting viral transcriptional activation — provides the primary mechanistic rationale for this repurposing prediction |
| [16529348](https://pubmed.ncbi.nlm.nih.gov/16529348/) | 2006 | Drug overview / new drug summary | Journal of the American Pharmacists Association | Narrative overview of Deferasirox at initial approval; no direct evidence for HIV indication, but contextualises the drug's pharmacological profile |

---

## Denmark Market Information

No marketing authorisations for Deferasirox were identified in the Danish Medicines Agency (Laegemiddelstyrelsen) dataset (0 registered authorisations).

> **Clinical Note:** Deferasirox (Exjade®, Jadenu®) holds a centralised EMA marketing authorisation (EU/1/05/313) that is valid across all EU/EEA member states, including Denmark. Healthcare professionals should verify current availability, reimbursement status, and approved indications directly with the Danish Medicines Agency or via the EMA product information portal.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

> Safety data (key warnings, contraindications, and drug interactions) were not available in this Evidence Pack. This is classified as a **Blocking Data Gap** (DG001) that must be resolved before any clinical safety assessment can proceed. The SmPC for Exjade®/Jadenu® is available via the EMA website.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence is limited exclusively to in vitro mechanistic studies (Evidence Level L4) with no clinical trials and no observational human data. The iron-chelation / HIV-Tat oligomerization hypothesis is biologically coherent but entirely unvalidated beyond the cell culture setting, making clinical translation premature at this stage.

**To proceed, the following is needed:**

- **Resolve Blocking Data Gap (DG001):** Obtain and review the full SmPC (warnings, contraindications, drug-drug interactions) before any safety pre-screening can be completed
- **Resolve High-Priority Data Gap (DG002):** Confirm Deferasirox MOA via DrugBank API to support mechanistic linkage analysis
- **In vivo validation:** Animal model studies (e.g., HIV-infected humanised mouse models) demonstrating antiviral activity of Deferasirox
- **DDI assessment with ARV regimens:** Evaluate pharmacokinetic interactions between Deferasirox and standard antiretroviral drugs (e.g., integrase inhibitors, protease inhibitors, NRTIs), particularly given Deferasirox's known interactions with CYP3A4 and UGT substrates
- **CNS penetration data:** Given the relevance to HIV-associated neurocognitive disorder (HAND) highlighted in the mechanistic paper, CNS pharmacokinetic profiling would be required for this indication
- **Proof-of-concept clinical study design:** If preclinical validation is successful, a Phase 1b/2a adjunctive study in virologically suppressed PLHIV or a treatment-intensification model should be defined before advancing further

---

*This report is generated for research purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before any therapeutic application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

