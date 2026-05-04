---
layout: default
title: Metreleptin
parent: 僅模型預測 (L5)
nav_order: 231
evidence_level: L5
indication_count: 10
---

# Metreleptin
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

# Metreleptin: From Generalized Lipodystrophy to Familial Generalized Lentiginosis

## One-Sentence Summary

Metreleptin is a recombinant analogue of human leptin, approved in other jurisdictions as a leptin replacement therapy for patients with congenital or acquired generalised lipodystrophy.
The TxGNN model predicts it may be effective for **Familial Generalized Lentiginosis** with a prediction score of **99.71%**.
However, **no clinical trials and no published literature** currently support this direction, placing this prediction at the lowest evidence tier (L5).

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Generalised lipodystrophy (leptin deficiency replacement therapy) |
| Predicted New Indication | Familial Generalized Lentiginosis |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L5 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known pharmacology, Metreleptin is a recombinant methionyl-human leptin analogue that acts as a leptin receptor (LEP-R) agonist. Its primary therapeutic role is to replace deficient endogenous leptin in patients with generalised lipodystrophy, thereby restoring downstream signalling through the JAK2–STAT3 and PI3K–AKT pathways to regulate energy homeostasis, insulin sensitivity, and appetite.

Familial generalised lentiginosis is a rare genetic disorder characterised by widespread cutaneous hyperpigmentation caused by mutations in the RAS/MAPK signalling pathway (commonly *PTPN11*). The pathological mechanism is fundamentally distinct from leptin deficiency: it involves aberrant melanocyte proliferation driven by dysregulated RAS–RAF–MEK–ERK signalling, with no established direct crossover to leptin receptor signalling. While leptin signalling (via JAK-STAT3) and RAS/MAPK pathway components share some downstream convergence points in theory, no published preclinical or clinical evidence supports a therapeutic link.

The high TxGNN prediction score most likely reflects indirect graph-proximity effects within the knowledge graph, where Metreleptin's connections to rare metabolic and genetic syndrome nodes cause it to cluster near rare pigmentary disorders such as familial generalised lentiginosis, gastrocutaneous syndrome, and Moynahan syndrome (LEOPARD syndrome). This is a recognised limitation of graph-based predictions for highly connected hub nodes: the score reflects network topology rather than a validated mechanistic hypothesis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Denmark Market Information

Metreleptin is not currently authorised or marketed in Denmark. No national (Lægemiddelstyrelsen) or centralised (EMA) marketing authorisations are recorded in this dataset.

> **Note for reviewers:** Metreleptin is marketed as **Myalepta** (brand name) by Amryt Pharmaceuticals in some European countries under EMA centralised procedure for generalised lipodystrophy. Prescribers should verify current EMA/Lægemiddelstyrelsen authorisation status directly before any clinical consideration.

---

## Safety Considerations

Safety data (key warnings, contraindications, and drug interactions) are not available in this Evidence Pack.

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no clinical trial evidence, no published literature, and no established mechanistic basis linking Metreleptin to familial generalised lentiginosis. The TxGNN prediction score of 99.71% appears to reflect indirect knowledge-graph topology (proximity among rare genetic syndrome nodes) rather than a biologically plausible repurposing hypothesis. The drug is also not authorised in Denmark, adding a further regulatory barrier. Proceeding without foundational evidence would not be a responsible use of research resources.

**To proceed, the following is needed:**

- **Mechanistic validation**: Establish whether any direct or indirect crossover exists between leptin receptor (JAK-STAT3) signalling and the RAS/MAPK–melanocyte axis implicated in familial generalised lentiginosis, ideally through pathway analysis or cell-line studies.
- **Literature search expansion**: Conduct a targeted PubMed/EMBASE search using broader MeSH terms (e.g., "leptin AND pigmentation", "leptin AND RAS/MAPK") to identify any tangential evidence.
- **MOA data retrieval**: Obtain full DrugBank entry for Metreleptin (DB09046) to confirm mechanism of action, pharmacodynamic targets, and known off-target interactions.
- **Safety profile review**: Retrieve the full SmPC/product label from the EMA or an authorising authority to assess contraindications, warnings, and drug interaction profile before any further evaluation.
- **Regulatory pathway assessment**: If mechanistic plausibility is later established, consult Lægemiddelstyrelsen regarding the regulatory pathway for a non-authorised medicinal product in Denmark (e.g., named-patient / compassionate use or full MA application).
- **Re-evaluation of prediction context**: Consider whether the TxGNN high-score cluster (familial generalised lentiginosis, gastrocutaneous syndrome, Moynahan syndrome) reflects a genuine biological signal or a graph artefact — peer review of the knowledge-graph subgraph around *LEP-R* and these syndrome nodes is recommended.

---

> *This report is generated for research reference purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before any application. All content should be reviewed by qualified healthcare professionals before any clinical or regulatory decision is made.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

