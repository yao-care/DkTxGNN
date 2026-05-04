---
layout: default
title: Mepolizumab
parent: 僅模型預測 (L5)
nav_order: 228
evidence_level: L5
indication_count: 10
---

# Mepolizumab
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

# Mepolizumab: From Severe Eosinophilic Asthma to Thrombocytopenia Due to Immune Destruction

## One-Sentence Summary

Mepolizumab (Nucala) is a humanized anti-interleukin-5 (IL-5) monoclonal antibody best known for its approved use in severe eosinophilic asthma and hypereosinophilic syndrome (HES). The TxGNN model predicts it may have utility in **thrombocytopenia due to immune destruction**, with a prediction score of **99.66%**; however, supporting evidence at this time consists solely of **1 case report** and **no registered clinical trials**, placing this firmly at an early exploratory stage.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Severe eosinophilic asthma / Hypereosinophilic syndrome (HES) *(from EMA authorisation; no national Danish records captured in this dataset)* |
| Predicted New Indication | Thrombocytopenia Due to Immune Destruction |
| TxGNN Prediction Score | 99.66% |
| Evidence Level | L4 |
| Denmark Market Status | Not marketed *(national database only — see note below)* |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available in this Evidence Pack. Based on well-established published information, Mepolizumab is a humanized IgG1κ monoclonal antibody that binds interleukin-5 (IL-5) with high affinity and specificity, blocking its interaction with the IL-5 receptor on eosinophil surfaces. This prevents eosinophil proliferation, differentiation, and survival, leading to a sustained reduction in circulating and tissue eosinophil counts. Its proven clinical benefit in severe eosinophilic asthma, HES, eosinophilic granulomatosis with polyangiitis (EGPA), and chronic rhinosinusitis with nasal polyps (CRSwNP) all stem from this shared eosinophil-suppression mechanism.

The proposed link to immune-mediated thrombocytopenia is **indirect**. In hypereosinophilic syndrome, persistently elevated eosinophil counts drive systemic inflammation through multiple pathways: immune complex deposition, complement cascade activation (generating C3a and C5a anaphylatoxins), and direct release of toxic granule products such as major basic protein (MBP) and eosinophil cationic protein (ECP). These mediators can injure platelets and megakaryocytes, and can activate the complement membrane attack complex — collectively producing a secondary, eosinophil-driven form of immune platelet destruction. By substantially reducing the eosinophil burden, mepolizumab may indirectly mitigate this downstream thrombocytopenic process.

The sole published case (PMID 28648630) describes a patient with steroid-resistant hypereosinophilic immune diathesis and atypical haemolytic uremic syndrome (aHUS) in whom mepolizumab resolved the hypereosinophilic syndrome and concurrently ameliorated mixed thrombotic microangiopathy — a condition with shared complement-mediated platelet-destructive pathophysiology. This is biologically coherent within the specific framing of HES-associated secondary thrombocytopenia, but the mechanistic chain is indirect and extrapolation to primary immune thrombocytopenia (ITP) unrelated to eosinophilia is not currently supported.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [28648630](https://pubmed.ncbi.nlm.nih.gov/28648630/) | 2018 | Case Report | Blood Cells, Molecules & Diseases | A steroid-resistant hypereosinophilic immune diathesis complicated by aHUS resolved following mepolizumab treatment, with concomitant amelioration of mixed thrombotic microangiopathy. Suggests that eosinophil-driven complement activation may be upstream of platelet injury in this setting, and that anti-IL-5 therapy can interrupt this cascade. |

---

## Denmark Market Information

No national (Laegemiddelstyrelsen) marketing authorisations are currently recorded for Mepolizumab in this dataset.

> **Important note for clinicians**: Mepolizumab is centrally authorised by the European Medicines Agency (EMA) as **Nucala** (EU/1/15/1043), and this centralised authorisation is directly valid in Denmark. Approved indications include severe refractory eosinophilic asthma (adults and children ≥6 years), hypereosinophilic syndrome (HES), eosinophilic granulomatosis with polyangiitis (EGPA), and chronic rhinosinusitis with nasal polyps (CRSwNP). The absence of entries in this dataset most likely reflects a gap in national-level data capture rather than a true lack of authorisation. The current predicted indication (thrombocytopenia due to immune destruction) falls **outside** all currently approved indications.

---

## Safety Considerations

Formal safety data — including key warnings, contraindications, and drug-drug interactions — was not available in this Evidence Pack.

> Please refer to the approved Summary of Product Characteristics (SmPC) for Nucala (mepolizumab) available via the [EMA product page](https://www.ema.europa.eu/en/medicines/human/EPAR/nucala) and the Danish Medicines Agency (Laegemiddelstyrelsen) for complete prescribing information, including immunogenicity, injection-site reactions, hypersensitivity, and monitoring requirements.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The sole supporting publication is a single case report describing HES-associated thrombotic microangiopathy — an indirect and highly context-specific presentation that does not constitute adequate evidence for a broader repurposing claim in primary immune thrombocytopenia. No clinical trials are registered for this indication-drug pair, and mechanistic plausibility is limited to secondary thrombocytopenia occurring in the context of eosinophil-driven immune activation.

**To proceed, the following is needed:**

- **Clarify clinical scope**: Determine whether the target population is (a) HES patients with secondary thrombocytopenia (where the indirect mechanistic rationale is biologically coherent) or (b) primary immune thrombocytopenia (ITP) patients without eosinophilia (where the rationale is currently unsupported).
- **Structured literature review**: Conduct a systematic search for all cases and case series of eosinophilia-associated thrombocytopenia treated with anti-IL-5 biologics (mepolizumab, benralizumab, reslizumab).
- **Clinical trial landscape audit**: Search whether ongoing or completed HES trials include platelet count or thrombocytopenia as a secondary or safety endpoint.
- **Retrieve full SmPC safety data**: Download and parse the EMA SmPC and Risk Management Plan (RMP) for Nucala to complete the safety profile before any clinical evaluation proceeds.
- **Mechanism of action documentation**: Obtain formal MOA data from DrugBank (DB06612) or regulatory filings to support mechanistic plausibility analysis.
- **If HES-associated framing is confirmed**: Consider designing a prospective observational cohort study or a retrospective registry analysis in HES patients receiving mepolizumab, with platelet dynamics as a pre-specified endpoint.

---

*This report is generated for research purposes only and does not constitute medical advice. All repurposing candidates require clinical validation before any therapeutic application. Data cut-off: 4 April 2026.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

