---
layout: default
title: Gefitinib
parent: 僅模型預測 (L5)
nav_order: 206
evidence_level: L5
indication_count: 10
---

# Gefitinib
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

# Gefitinib: From Non-Small Cell Lung Cancer to Fibromatosis, Gingival

## One-Sentence Summary

Gefitinib (Iressa) is a selective EGFR tyrosine kinase inhibitor, approved internationally for the treatment of non-small cell lung cancer (NSCLC) with activating EGFR mutations.
The TxGNN model assigns its highest prediction score to **Fibromatosis, Gingival** (99.89%), however this indication carries **no supporting clinical trials or literature** — and the mechanistic rationale raises a critical concern: gingival hyperplasia (gingival overgrowth) is itself a known adverse effect of EGFR TKIs, suggesting this is very likely a pharmacovigilance false-positive signal rather than a true therapeutic opportunity.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Non-Small Cell Lung Cancer (NSCLC) with activating EGFR mutations |
| Predicted New Indication | Fibromatosis, Gingival |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L5 |
| Denmark Market Status | Not Marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Gefitinib is a selective, reversible inhibitor of the epidermal growth factor receptor tyrosine kinase (EGFR/HER1/ErbB1). It blocks autophosphorylation of the intracellular EGFR kinase domain, thereby suppressing downstream proliferation and survival signalling cascades (RAS/MAPK and PI3K/AKT pathways). In NSCLC harbouring activating EGFR mutations — most commonly exon 19 deletions and the L858R point mutation — this blockade produces clinically meaningful tumour regression, as demonstrated in the landmark IPASS trial (NEJM, 2009). Detailed mechanism of action data was not retrieved from DrugBank in this evidence pack; the above is based on established pharmacological classification.

Gingival fibromatosis is a rare, benign condition characterised by progressive fibrous hyperplasia of the gingival connective tissue. There is currently no published evidence that EGFR overexpression or constitutive EGFR activation plays a pathological role in this disease. The biological rationale for treating gingival fibromatosis with an EGFR TKI is therefore absent.

**This prediction is most likely a false positive.** Gingival hyperplasia (gingival overgrowth) is a well-documented adverse drug reaction of EGFR TKIs, including gefitinib. The TxGNN knowledge graph likely captured a drug–disease co-occurrence originating from pharmacovigilance databases and misinterpreted this adverse effect association as a therapeutic signal. This is a recognised artefact pattern in graph neural network-based repurposing models, where adverse effect edges and therapeutic edges share structural similarity in the knowledge graph.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Gefitinib in Fibromatosis, Gingival.

---

## Literature Evidence

Currently no related literature available for Gefitinib in Fibromatosis, Gingival.

---

## Denmark Market Information

Gefitinib holds no national or centralised marketing authorisations currently registered with the Danish Medicines Agency (Laegemiddelstyrelsen). Healthcare professionals requiring access for individual patients would need to apply for a special authorisation (*særlig tilladelse* / named patient programme).

> **Note for context:** Gefitinib (Iressa, AstraZeneca) holds EMA centralised marketing authorisation for EGFR-mutated NSCLC in other EU/EEA member states. Its absence from the Danish market does not reflect a safety withdrawal but a commercial decision. Access via special authorisation is feasible if clinical need arises.

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — first-generation selective EGFR tyrosine kinase inhibitor (not a conventional cytotoxic agent) |
| Myelosuppression Risk | Low (myelosuppression is uncommon; not a hallmark toxicity of EGFR TKIs) |
| Emetogenicity Classification | Low |
| Monitoring Items | Liver function (ALT, AST, bilirubin — hepatotoxicity risk); pulmonary function (interstitial lung disease / pneumonitis — rare but potentially fatal); skin and nail toxicity (acneiform rash, paronychia); renal function and electrolytes |
| Handling Protection | Standard oral antineoplastic precautions apply; follow local institutional cytotoxic handling policy |

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for complete safety information. Full Danish/EMA warnings, contraindications, and drug interaction data were not available in this evidence pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top TxGNN prediction — Fibromatosis, Gingival (score 99.89%) — is assessed as a **pharmacovigilance-driven false positive**. Gingival hyperplasia is a known adverse reaction of EGFR TKIs; the model has likely interpreted this adverse effect co-occurrence as a therapeutic signal. No mechanistic rationale, no clinical trials, and no supporting literature exist for this indication. Gefitinib is also not marketed in Denmark (0 authorisations), presenting an additional regulatory barrier to any clinical use.

**To proceed with further evaluation, the following is needed:**

- **Disqualify or confirm this signal:** A targeted literature review of EGFR pathway biology in gingival fibromatosis should be conducted before any further development steps are taken; current expectation is formal disqualification.
- **MOA data gap closure:** Retrieve complete mechanism of action and adverse effect data from DrugBank (DB00317) to support future evaluations.
- **Safety data gap closure:** Download and parse the SmPC from the EMA product page to complete contraindication, warning, and drug interaction profiles.
- **Consider the higher-quality signal at rank 9:** **Lung Hilum Carcinoma** (score 99.86%, L4 evidence, 1 case report of a gefitinib super-responder) represents a mechanistically coherent repurposing candidate — EGFR mutations are prevalent in central-type lung adenocarcinoma, and gefitinib's efficacy in NSCLC is supported by Phase 3 RCT evidence (IPASS). This should be elevated to a formal **Research Question** stage assessment.
- **Regulatory pathway:** If clinical investigation of gefitinib for any Danish-relevant indication is considered, initiate a named patient / compassionate use dialogue with Laegemiddelstyrelsen, or assess eligibility under EMA's existing centralised authorisation.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

