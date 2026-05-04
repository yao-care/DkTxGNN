---
layout: default
title: Ceritinib
parent: 僅模型預測 (L5)
nav_order: 103
evidence_level: L5
indication_count: 10
---

# Ceritinib
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

# Ceritinib: From ALK-Positive Non-Small Cell Lung Cancer to Gingival Fibromatosis

## One-Sentence Summary

Ceritinib is a second-generation oral ALK (anaplastic lymphoma kinase) tyrosine kinase inhibitor, internationally approved for the treatment of ALK-rearranged non-small cell lung cancer (NSCLC), but not currently registered in Denmark.
The TxGNN model predicts it may have activity in **Gingival Fibromatosis (fibromatosis, gingival)** with a prediction score of **99.86%**; however, **no clinical trials or published literature** currently support this specific indication.
The biological rationale connecting ceritinib's mechanism of action to gingival fibromatosis is limited, and the high model score most likely reflects structural patterns within the knowledge graph rather than genuine pharmacological relevance.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | ALK-positive non-small cell lung cancer (NSCLC) — not registered in Denmark; inferred from published literature |
| Predicted New Indication | Fibromatosis, Gingival |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L5 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Ceritinib (Zykadia®, Novartis) is a potent second-generation ALK inhibitor first approved by the US FDA in 2014 under Breakthrough Therapy designation for ALK-rearranged NSCLC after progression on crizotinib, and subsequently approved by the EMA in 2015. Although full mechanism of action data was not retrievable in this evidence pack, published literature consistently documents ceritinib's primary mechanism as competitive inhibition of the ALK kinase domain with approximately 20-fold greater potency than crizotinib, along with inhibitory activity against IGF1R, InsR, and ROS1 kinases. Multiple Phase 3 trials (including ASCEND-4) have confirmed its efficacy in first-line ALK-rearranged NSCLC, and it is well-established within that therapeutic context globally — though it has not obtained marketing authorisation in Denmark.

Gingival Fibromatosis is a rare, typically hereditary disorder characterised by progressive benign overgrowth of gingival connective tissue. Its known pathogenic genes — **SOS1, REST, and KCNJ13** — have no established relationship with ALK signalling or any of ceritinib's primary target kinases. While ceritinib's activity at IGF1R could theoretically influence fibroblast proliferation pathways, this remains a purely speculative inference without any experimental, preclinical, or clinical support.

The extremely high TxGNN score (99.86%) for this indication most likely reflects **topological proximity** between the gingival fibromatosis node and other fibrous tissue-related disease nodes within the knowledge graph, rather than a genuine pharmacological connection. This is a recognised limitation of graph-based machine learning models, where structural similarity in the graph can yield high scores for disease pairs with no meaningful biological relationship, and highlights the critical importance of expert mechanistic review prior to any clinical evaluation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — second-generation ALK tyrosine kinase inhibitor (not a conventional cytotoxic agent) |
| Myelosuppression Risk | Low (haematological toxicity is uncommon; anaemia and neutropenia have been reported at low frequencies, substantially lower than conventional chemotherapy) |
| Emetogenicity Classification | Moderate (nausea, vomiting, and diarrhoea are the most frequent adverse effects across clinical trials; antiemetic prophylaxis and dose modification may be required) |
| Monitoring Items | Liver function tests (ALT/AST — hepatotoxicity risk), pancreatic enzymes (lipase/amylase — pancreatitis risk), ECG (QTc prolongation), fasting blood glucose (hyperglycaemia), pulmonary function / HRCT if respiratory symptoms emerge (interstitial lung disease/pneumonitis) |
| Handling Protection | Standard oncology drug handling precautions apply; institutional cytotoxic handling procedures should be followed per local policy |

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) — available via the EMA (EU/1/15/1017) — for full safety information including contraindications, warnings, and drug interactions.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no clinical, preclinical, or mechanistic evidence linking ceritinib to gingival fibromatosis. The disease is caused by hereditary connective tissue gene abnormalities (SOS1/REST/KCNJ13) unrelated to ALK signalling, and the TxGNN model's very high prediction score reflects knowledge graph topology rather than biological plausibility. Advancing this candidate further cannot be justified on current evidence.

**To proceed, the following is needed:**

- Retrieval of full mechanism of action data from DrugBank (DB09063) to confirm the complete kinase inhibition profile and any secondary targets relevant to connective tissue biology
- Preclinical investigation into whether ALK or IGF1R pathway activity plays any role in gingival fibroblast proliferation or fibromatosis pathogenesis
- TxGNN disease ontology review to determine whether the "fibromatosis, gingival" node shares structural features with any disease for which ceritinib has established activity
- Formal safety data retrieval from the Danish Medicines Agency (Laegemiddelstyrelsen) or full EMA SmPC for contraindications, key warnings, and drug interaction profile

---

> ⚠️ **Data Quality Note — Rank 9–10 Indication (Lung Benign Neoplasm):**
> The "lung benign neoplasm" entries at ranks 9–10 are associated with **20 PubMed publications**; however, all 20 papers address ALK-rearranged **NSCLC** — a malignancy — and not benign lung tumours. This constitutes a **critical disease label mismatch** in the TxGNN disease ontology. If the node label was intended to capture ALK+ NSCLC, the evidence level would upgrade to **L1** (Phase 3 RCT ASCEND-4, PMID 28126333, *Lancet* 2017), and a dedicated evaluation with a **"Proceed with Guardrails"** recommendation would be warranted. This mismatch should be resolved in the ontology before further evaluation of the full candidate list.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

