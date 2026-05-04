---
layout: default
title: Crizotinib
parent: 僅模型預測 (L5)
nav_order: 124
evidence_level: L5
indication_count: 10
---

# Crizotinib
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

# Crizotinib: From ALK-Positive Non-Small Cell Lung Cancer to Fibromatosis, Gingival

## One-Sentence Summary

Crizotinib (Xalkori®) is a first-in-class oral ATP-competitive inhibitor of the ALK, ROS1, and MET receptor tyrosine kinases, with established international approval for the treatment of ALK-positive and ROS1-rearranged non-small cell lung cancer (NSCLC).
The TxGNN model predicts it may be effective for **Fibromatosis, Gingival**, with **0 clinical trials** and **0 publications** currently supporting this specific indication.
This is a model-only prediction (Evidence Level L5) with no translational or clinical data to date, and a weak mechanistic rationale.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | ALK-positive non-small cell lung cancer (NSCLC) — based on established international approvals; no Danish authorisation on file |
| Predicted New Indication | Fibromatosis, Gingival |
| TxGNN Prediction Score | 99.81% |
| Evidence Level | L5 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on established published literature, Crizotinib is a small-molecule inhibitor that competitively blocks the ATP-binding site of three receptor tyrosine kinases: **ALK (Anaplastic Lymphoma Kinase)**, **ROS1**, and **MET (c-MET/Hepatocyte Growth Factor Receptor)**. By inhibiting constitutively active fusion proteins such as EML4-ALK, it suppresses downstream oncogenic signalling through the RAS/MAPK and PI3K/AKT pathways, leading to tumour cell apoptosis and growth arrest in ALK-positive NSCLC. This mechanism has been robustly validated across multiple Phase II and III trials.

Fibromatosis, Gingival is a rare autosomal dominant disorder characterised by excessive fibrous tissue overgrowth of the gingiva, driven primarily by mutations in **SOS1**, **REST**, and **HMGA2** — none of which have a known direct functional relationship with the ALK, ROS1, or MET signalling axes that Crizotinib targets. While MET signalling can theoretically contribute to fibroblast proliferation in some biological contexts, there is no published clinical, translational, or in vitro evidence linking Crizotinib's targets to the pathogenesis of gingival fibromatosis.

The high TxGNN prediction score most likely reflects **topological proximity** between "fibroproliferative disease" nodes in the underlying knowledge graph, rather than a genuine disease-specific mechanistic connection. This should be treated as a non-specific, algorithmically-driven prediction. The mechanistic rationale is currently insufficient to justify further investigation without additional hypothesis-generating data.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Crizotinib in Fibromatosis, Gingival.

---

## Literature Evidence

Currently no related literature available for Crizotinib in Fibromatosis, Gingival.

---

## Denmark Market Information

Crizotinib is currently **not marketed in Denmark** according to the Laegemiddelstyrelsen data on file. No national or EMA centralised marketing authorisations were retrieved in this evidence pack.

> **Important note for clinicians:** Crizotinib (Xalkori®, Pfizer) holds a centralised EMA marketing authorisation valid across EU Member States for ALK-positive advanced NSCLC and ROS1-positive advanced NSCLC. The absence of records in this dataset may reflect a data sourcing limitation rather than a genuine absence of authorisation. Current authorisation status should be verified directly via the [EMA product database](https://www.ema.europa.eu/en/medicines/human/EPAR/xalkori) or the Laegemiddelstyrelsen before any clinical or regulatory decision is made.

---

## Cytotoxicity

Crizotinib is an antineoplastic targeted therapy used in oncology. The following assessment is based on published literature, as formal toxicity data was not available in the submitted evidence pack.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — ALK/ROS1/MET tyrosine kinase inhibitor (not a conventional cytotoxic agent) |
| Myelosuppression Risk | Low to moderate; neutropenia and anaemia reported in clinical trials, though generally less severe than conventional chemotherapy |
| Emetogenicity Classification | Low to moderate |
| Monitoring Items | Liver function tests (LFTs) — hepatotoxicity risk; complete blood count (CBC); 12-lead ECG (QTc prolongation); ophthalmological assessment (visual disturbances very common); pulmonary function and chest imaging (risk of interstitial lung disease/pneumonitis) |
| Handling Protection | Follow institutional guidelines for antineoplastic drug handling; standard cytotoxic precautions apply for preparation and disposal |

> A 2026 review (PMID [41617059](https://pubmed.ncbi.nlm.nih.gov/41617059/), *Toxicology Letters*) provides a comprehensive synthesis of crizotinib-induced multisystem toxicities — including hepatotoxicity, cardiotoxicity, and interstitial lung disease — along with molecular mechanisms and clinical management strategies. This is recommended reading pending full SmPC retrieval.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for complete safety information. No specific warnings, contraindications, or drug interaction data were available in this evidence pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model returns a high prediction score for Crizotinib in Fibromatosis, Gingival, but there is zero clinical, translational, or mechanistic evidence to support this indication. The disease is driven by SOS1/REST/HMGA2 mutations with no established connection to ALK/ROS1/MET signalling, and the prediction is most plausibly explained by non-specific knowledge graph topology rather than a true pharmacological relationship.

**To proceed, the following is needed:**

- Retrieval and review of the current Xalkori® SmPC (EMA) and relevant Laegemiddelstyrelsen documentation to complete the S1 safety screening currently blocked by data gaps
- Detailed mechanism of action data from DrugBank (DB08865) to enable formal mechanistic linkage analysis
- A targeted preclinical literature search to determine whether MET or ALK inhibition has any reported effects on SOS1/REST/HMGA2-driven fibroproliferative pathways before this hypothesis can be elevated above L5
- If any preclinical signal is identified, an in vitro study in gingival fibroblast models would be the minimum required to justify further development
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

