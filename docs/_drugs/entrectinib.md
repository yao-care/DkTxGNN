---
layout: default
title: Entrectinib
parent: 僅模型預測 (L5)
nav_order: 168
evidence_level: L5
indication_count: 10
---

# Entrectinib
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

# Entrectinib: From NTRK Fusion-Positive Solid Tumours to Multiple Endocrine Neoplasia

## One-Sentence Summary

Entrectinib (Rozlytrek) is a CNS-active multikinase inhibitor approved for NTRK fusion-positive solid tumours and ROS1-positive non-small cell lung cancer, working by blocking aberrant receptor tyrosine kinase signalling that drives tumour growth and survival.
The TxGNN model predicts it may be effective for **Multiple Endocrine Neoplasia (MEN)**, with **2 clinical trials** and **1 publication** currently providing indirect supporting evidence for this direction.
The mechanistic link is plausible but remains unvalidated, and further biomarker-driven research is needed before clinical translation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | NTRK fusion-positive solid tumours (tissue-agnostic); ROS1-positive non-small cell lung cancer (based on known regulatory approvals; field empty in data source) |
| Predicted New Indication | Multiple Endocrine Neoplasia (MEN) |
| TxGNN Prediction Score | 98.58% |
| Evidence Level | L4 |
| Denmark Market Status | Not marketed (no national marketing authorisation registered) |
| Number of Marketing Authorisations | 0 national authorisations on record — note: EMA centralised authorisation (Rozlytrek, EU/1/20/1467) is valid across the EEA including Denmark |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Entrectinib is a potent, CNS-penetrant inhibitor of three receptor tyrosine kinase families: TRKA, TRKB, and TRKC (encoded by *NTRK1*, *NTRK2*, and *NTRK3*), ROS1, and ALK. When these kinases carry oncogenic gene fusions, they become constitutively active and drive tumour proliferation via downstream RAS/MAPK, PI3K/AKT, and PLCγ signalling cascades. Entrectinib competitively binds the ATP-binding pocket of these kinases, switching off the oncogenic signal regardless of the tumour's tissue of origin — a tissue-agnostic mechanism.

Multiple Endocrine Neoplasia (MEN) is a group of hereditary syndromes characterised by tumours in multiple endocrine glands. MEN2A and MEN2B are driven by activating mutations in the *RET* proto-oncogene, manifesting primarily as medullary thyroid carcinoma (MTC), phaeochromocytoma, and, in MEN2A, primary hyperparathyroidism. MEN1 arises from loss-of-function mutations in the *MEN1* tumour suppressor, producing parathyroid adenomas, pituitary tumours, and pancreatic neuroendocrine tumours (pNETs). The indirect link to entrectinib rests on two observations: (1) NTRK gene fusions have been identified in a subset of thyroid cancers and neuroendocrine tumours — precisely the tumour types that characterise MEN syndromes; (2) the supporting literature (PMID 38438731) documents a patient with MTC (the hallmark MEN2 cancer) developing off-target resistance to the selective RET inhibitor selpercatinib via alternative oncogenic drivers, raising the hypothesis that NTRK/ROS1 inhibition could potentially address bypass mechanisms in RET-driven endocrine tumours.

It is essential to note that mutant RET — the primary oncogenic driver in MEN2 — is **not** a direct target of entrectinib. The high TxGNN score (98.58%) most likely reflects knowledge-graph co-occurrence patterns linking NTRK/ROS1 inhibitors to endocrine tumour biology rather than a directly validated mechanism. The prediction should therefore be treated as hypothesis-generating and interpreted with caution, pending dedicated mechanistic and clinical validation.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04551495](https://clinicaltrials.gov/study/NCT04551495) | Phase 2 | Active, not recruiting | 65 | Neoadjuvant ROS1 inhibition (entrectinib) combined with endocrine therapy in invasive lobular breast carcinoma (ILBC) harbouring CDH1 loss. Based on a preclinical finding that ROS1 is a synthetic lethal partner of CDH1 inactivation. Not MEN-specific, but validates the principle of entrectinib activity in an endocrine-sensitive, hormone receptor-positive tumour context. |
| [NCT03878524](https://clinicaltrials.gov/study/NCT03878524) | Phase 1 | Terminated | 2 | Basket trial (SMMART PRIME) testing personalised drug combinations guided by individual tumour molecular profiling to overcome drug resistance. Terminated early due to poor accrual. No MEN-specific data available and no efficacy conclusions can be drawn. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [38438731](https://pubmed.ncbi.nlm.nih.gov/38438731/) | 2024 | Case Report / Molecular Analysis | NPJ Precision Oncology | Describes adaptive off-target resistance to the selective RET inhibitor selpercatinib in a patient with metastatic medullary thyroid carcinoma (MTC) harbouring a RET D898_E901del activation-loop mutation. Resistance emerged through alternative oncogenic mechanisms rather than secondary RET mutations. Highlights the clinical challenge of alternative pathway bypass in RET-driven MEN2 tumours, and indirectly supports exploring multi-kinase strategies — including NTRK/ROS1 inhibitors such as entrectinib — for treatment-refractory MEN2-associated MTC. |

---

## Cytotoxicity

Entrectinib is an antineoplastic targeted therapy approved for oncological indications (NTRK fusion-positive solid tumours; ROS1-positive NSCLC).

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — Multikinase inhibitor (NTRK1/2/3, ROS1, ALK); not a conventional cytotoxic agent |
| Myelosuppression Risk | Low to moderate — anaemia is the most frequently reported haematological adverse event; neutropenia and thrombocytopenia occur but are less common than with conventional cytotoxic chemotherapy |
| Emetogenicity Classification | Low — nausea is reported but is typically mild to moderate in severity for oral targeted agents of this class |
| Monitoring Items | Full blood count (CBC with differential), liver function (ALT, AST, total bilirubin), renal function, cardiac monitoring (ECG for QTc prolongation, assessment for congestive heart failure), and neurological assessment (cognitive effects, dizziness, mood changes, and sleep disturbances are class-related CNS effects) |
| Handling Protection | Standard cytotoxic oral drug handling precautions apply; follow institutional guidelines for preparation, dispensing, and disposal of oral antineoplastic agents |

---

## Safety Considerations

Detailed warning statements, contraindications, and drug interaction data are not available in the current evidence pack.

> Please refer to the approved Summary of Product Characteristics (SmPC) for Rozlytrek (entrectinib) — available via the EMA product page — for complete safety information. Key areas to review include cardiac toxicity (congestive heart failure, QTc prolongation), CNS effects (cognitive impairment, mood disorders, sleep disturbance), hepatotoxicity, embryo-foetal toxicity, and pharmacokinetic interactions with strong CYP3A4 inducers and inhibitors.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN prediction score (98.58%), the available evidence for entrectinib specifically in Multiple Endocrine Neoplasia is indirect and insufficient to support clinical use or a formal repurposing programme at this stage. Neither identified clinical trial is designed for or enrolling MEN patients, the sole literature evidence concerns resistance mechanisms in RET-driven MTC rather than direct NTRK/ROS1-targeted anti-tumour efficacy in MEN, and entrectinib has no registered national marketing authorisation in Denmark for any indication.

**To proceed, the following is needed:**

- **Biomarker screening**: Systematic molecular profiling of MEN-associated tumour cohorts (MTC, pNETs, phaeochromocytoma) to determine the prevalence of NTRK gene fusions, ROS1 rearrangements, or ALK alterations that would indicate on-target activity of entrectinib
- **Preclinical validation**: Cell line and patient-derived xenograft studies in MEN tumour models to demonstrate meaningful anti-tumour activity of entrectinib
- **Dedicated clinical evidence**: Prospective basket trial data or registry-based observational evidence specifically including MEN patients with NTRK/ROS1/ALK-positive tumours
- **Full safety assessment**: Formal review of the Rozlytrek SmPC, including evaluation of drug interactions relevant to the MEN management context (e.g. concurrent use of somatostatin analogues, proton pump inhibitors, antihypertensives)
- **Regulatory clarification**: Confirmation of the EMA centralised authorisation status for Rozlytrek in Denmark and assessment of the feasibility of an off-label use programme or expanded indication application via the EMA's Type II variation pathway
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

