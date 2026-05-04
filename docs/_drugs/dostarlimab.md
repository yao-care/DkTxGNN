---
layout: default
title: Dostarlimab
parent: 僅模型預測 (L5)
nav_order: 150
evidence_level: L5
indication_count: 10
---

# Dostarlimab
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

# Dostarlimab: From Cancer Immunotherapy (Anti-PD-1) to Mixed Mineral Dust Pneumoconiosis

## One-Sentence Summary

Dostarlimab is an anti-PD-1 immune checkpoint inhibitor originally developed for the treatment of cancers with mismatch repair deficiency (dMMR/MSI-H), including endometrial cancer.
The TxGNN model predicts it may be effective for **Mixed Mineral Dust Pneumoconiosis**, however there are **0 clinical trials** and **0 publications** currently supporting this direction.
The mechanistic rationale for this prediction is considered scientifically implausible and carries clinically relevant safety concerns.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in regulatory database queried; known globally as anti-PD-1 immunotherapy for dMMR/MSI-H cancers |
| Predicted New Indication | Mixed Mineral Dust Pneumoconiosis |
| TxGNN Prediction Score | 50.00% |
| Evidence Level | L5 |
| Denmark Market Status | Not found in regulatory database (0 authorisations returned) |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on the mechanistic rationale embedded in the prediction record and established pharmacological knowledge, Dostarlimab is an anti-PD-1 monoclonal antibody immune checkpoint inhibitor. It works by blocking the interaction between PD-1 (Programmed Cell Death Protein 1) on T lymphocytes and its ligands PD-L1/PD-L2 on tumour cells, thereby restoring cytotoxic T cell activity that has been suppressed within the tumour microenvironment. Its proven efficacy is in oncological settings where tumour immune evasion via the PD-1/PD-L1 axis is the central pathological mechanism.

Mixed mineral dust pneumoconiosis is a chronic fibrotic lung disease caused by sustained inhalation of mixed mineral particles (e.g., silica, coal, iron oxides). The pathophysiology involves granulomatous inflammation driven by macrophage activation, progressive fibroblast proliferation, and irreversible pulmonary fibrosis. While PD-L1 upregulation has been observed in fibrotic lung tissue and PD-1-positive T cells have been detected in bronchoalveolar lavage fluid from affected patients, this does not imply a therapeutic opportunity. On the contrary, anti-PD-1 therapy enhances T cell cytotoxic activity in an already inflamed tissue environment, which in the context of pulmonary fibrosis is more likely to **exacerbate** immune-related pneumonitis (irAE: pneumonitis) — a well-documented class effect of checkpoint inhibitors — rather than deliver therapeutic benefit.

In summary, the TxGNN model prediction for this indication lacks a coherent mechanistic rationale supporting therapeutic benefit. The known biology of the PD-1/PD-L1 pathway in fibrotic lung disease does not favour this repurposing direction, and the potential for serious respiratory irAE represents an active safety concern. No clinical or preclinical evidence has been identified to challenge this assessment.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Denmark Market Information

No marketing authorisations were found in the regulatory database for Dostarlimab. The regulatory data source returned 0 records with market status "not marketed."

> **Note for clinicians:** Dostarlimab (Jemperli®) holds a centralised EMA marketing authorisation (applicable across all EU/EEA member states including Denmark). The absence of records in this dataset likely reflects a data source limitation rather than actual non-availability. Please verify current authorisation status and approved indications directly via the [EMA product page](https://www.ema.europa.eu/) or the Danish Medicines Agency (Lægemiddelstyrelsen) at [laegemiddelstyrelsen.dk](https://www.laegemiddelstyrelsen.dk/).

---

## Cytotoxicity

Dostarlimab is an oncological agent (anti-PD-1 immune checkpoint inhibitor) and is therefore classified within the antineoplastic category.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Immunotherapy — immune checkpoint inhibitor (anti-PD-1 monoclonal antibody); not a conventional cytotoxic agent |
| Myelosuppression Risk | Low (not a cytotoxic myelosuppressant); however, immune-related haematological adverse events (e.g., immune thrombocytopenia, haemolytic anaemia) have been reported as irAEs |
| Emetogenicity Classification | Minimal (checkpoint inhibitors are not classified as emetogenic agents) |
| Monitoring Items | Full blood count (CBC), liver function tests (AST, ALT, bilirubin), renal function, thyroid function (TSH, free T4), blood glucose (HbA1c), cortisol — routine irAE monitoring panel |
| Handling Protection | Standard biological product handling precautions apply; does not require cytotoxic chemotherapy handling precautions (no dedicated closed-system transfer device requirement) |

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information. Full prescribing information including warnings, contraindications, and drug interactions was not available in this Evidence Pack.

> **Known class effect reminder:** Anti-PD-1 checkpoint inhibitors as a class carry risk of immune-related adverse events (irAEs) affecting any organ system. Pneumonitis, colitis, hepatitis, endocrinopathies, nephritis, and dermatitis are among the most clinically significant. In the context of mixed mineral dust pneumoconiosis, pre-existing compromised lung function and fibrosis may substantially increase the risk and severity of checkpoint inhibitor-induced pneumonitis.

---

## Summary of All Predicted Indications

All 10 TxGNN-predicted indications for Dostarlimab share the same evidence profile. For reference:

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Decision |
|------|----------------------|-------------|----------------|----------|
| 1 | Mixed mineral dust pneumoconiosis | 50.00% | L5 | Hold |
| 2 | Rod-cone dystrophy, sensorineural deafness, and Fanconi-type renal dysfunction | 50.00% | L5 | Hold |
| 3 | MED12-related intellectual disability syndrome | 50.00% | L5 | Hold |
| 4 | Alpha-gal syndrome | 50.00% | L5 | Hold |
| 5 | Food protein-induced allergic proctocolitis | 50.00% | L5 | Hold |
| 6 | Mast cell activation syndrome | 50.00% | L5 | Hold |
| 7 | Primary mast cell activation syndrome | 50.00% | L5 | Hold |
| 8 | Secondary mast cell activation syndrome | 50.00% | L5 | Hold |
| 9 | Food protein-induced enterocolitis syndrome | 50.00% | L5 | Hold |
| 10 | Tendinopathy | 50.00% | L5 | Hold |

**Pattern observation:** The model has assigned a uniform score of 50.00% across all 10 predictions, suggesting these results may reflect prediction uncertainty at the boundary threshold rather than genuine signal. All predicted indications are mechanistically inconsistent with the PD-1/PD-L1 checkpoint inhibitor class: five involve allergic/mast cell pathways where anti-PD-1 could theoretically **worsen** disease; three involve rare genetic/developmental syndromes with no immunological intervention rationale; one involves occupational lung fibrosis where irAE risk is heightened; and one involves tendinopathy with highly uncertain directionality. None warrant further investigation at this time.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All 10 TxGNN-predicted indications are rated L5 (model prediction only, no supporting studies), with a uniform borderline score of 50.00% that likely reflects prediction uncertainty rather than a true repurposing signal. More critically, mechanistic analysis of the top-ranked indication (mixed mineral dust pneumoconiosis) and the broader predicted indication list reveals that anti-PD-1 therapy is either irrelevant to or potentially harmful in these disease contexts. This represents one of the least clinically actionable Evidence Pack profiles encountered.

**To proceed with any further evaluation, the following would be required:**

- **Mechanism of action data (MOA):** Retrieve from DrugBank API (DB15627) to confirm target, binding mechanism, and downstream pathway effects
- **Regulatory data correction:** Reconcile the discrepancy between the 0-licence database result and the known EMA centralised authorisation status; retrieve the Jemperli® SmPC for current approved indications and complete safety information
- **Re-evaluation of prediction validity:** Investigate why TxGNN assigned uniform 50.00% scores to all 10 indications — this pattern may indicate a model confidence floor or a mapping error in the knowledge graph for this drug node
- **Alternative indication search:** If repurposing exploration for Dostarlimab is desired, focus should be directed at well-established clinical areas where PD-1 checkpoint inhibition has biological rationale (e.g., dMMR/MSI-H solid tumours beyond currently approved indications, TMB-high cancers, or specific autoimmune-associated malignancies)

> **Research use only.** This report is intended for research purposes and does not constitute medical advice. All drug repurposing candidates require clinical validation before any therapeutic application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

