---
layout: default
title: Dornase Alfa
parent: 僅模型預測 (L5)
nav_order: 149
evidence_level: L5
indication_count: 10
---

# Dornase Alfa
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

# Dornase alfa: From Cystic Fibrosis to Mixed Mineral Dust Pneumoconiosis

## One-Sentence Summary

Dornase alfa (brand name: Pulmozyme) is a recombinant human deoxyribonuclease I (DNase I) enzyme originally approved for the management of cystic fibrosis (CF), where it reduces airway mucus viscosity by degrading extracellular DNA released from degenerating neutrophils.
The TxGNN model predicts it may be effective for **mixed mineral dust pneumoconiosis** — an occupational lung disease driven by chronic mineral dust-induced inflammation.
However, no clinical trials or published literature currently support this direction, and all 10 predicted indications in this pack are rated **L5 (model prediction only)**, with an overall recommendation of **Hold**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Cystic fibrosis (inhaled mucolytic / DNase therapy) |
| Predicted New Indication | Mixed mineral dust pneumoconiosis |
| TxGNN Prediction Score | 50.00% |
| Evidence Level | L5 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack. Based on established pharmacology, Dornase alfa is a recombinant human DNase I that selectively cleaves the phosphodiester backbone of extracellular DNA (eDNA). In cystic fibrosis, massive eDNA accumulation from lysed neutrophils in the airways creates pathologically viscous mucus, and inhaled Dornase alfa reduces this viscosity, improves mucociliary clearance, and thereby lowers the risk of pulmonary exacerbations.

The mechanistic rationale proposed by TxGNN for mixed mineral dust pneumoconiosis rests on the observation that mineral dusts (silica, coal, asbestos) trigger sustained neutrophil infiltration into the lung parenchyma. Activated neutrophils release neutrophil extracellular traps (NETs) — web-like structures of eDNA, histones, and antimicrobial proteins — that can perpetuate chronic inflammation. In theory, Dornase alfa could degrade these NETs, thereby interrupting the inflammatory signalling cascade and reducing the inflammatory burden.

However, the core pathological driver of pneumoconiosis is irreversible silicate- or coal dust-induced fibrosis — a process in which eDNA accumulation is a secondary, downstream phenomenon rather than the primary cause. The mechanistic link between Dornase alfa's DNase activity and clinically meaningful fibrosis attenuation is therefore weak, indirect, and speculative. No clinical or preclinical studies have directly investigated Dornase alfa in pneumoconiosis, and the TxGNN prediction most plausibly reflects disease-node topological proximity in the knowledge graph rather than strong biological rationale.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Denmark Market Information

According to the current dataset, Dornase alfa holds no marketing authorisations recorded in the Danish regulatory database (Laegemiddelstyrelsen).

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|-------------------------------|--------------|-------------|---------------------|
| — | — | — | No records found |

> **Note for clinicians:** Pulmozyme (dornase alfa) holds a centralised EMA marketing authorisation (EU/1/94/011) that is valid across all EU/EEA member states, including Denmark. Healthcare professionals should verify the current supply and reimbursement status directly via the EMA product database or Laegemiddelstyrelsen's national medicines registry, as the absence of a local licence entry may reflect a data coverage gap rather than regulatory unavailability.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All 10 TxGNN-predicted indications for Dornase alfa are rated L5 with a uniform prediction score of 50%, and the top-ranked indication (mixed mineral dust pneumoconiosis) is supported by only a weak, inferential mechanistic hypothesis with no clinical or preclinical evidence. Initiating any repurposing programme at this stage would be premature.

**Landscape note across all 10 predictions:**
Among the 10 predicted indications, **tendinopathy (rank 10)** carries the most scientifically grounded hypothesis: NETs have been detected in damaged tendon tissue and shown, in early preclinical work, to promote chronic inflammation and tenocyte apoptosis via the HMGB1/TLR4 pathway. DNase treatment has been reported to degrade tendon-resident NETs and improve the tissue repair microenvironment. While still L5, tendinopathy is the sole candidate that the evidence pack explicitly flags as a **Research Question** worth further exploration. The remaining 8 indications (allergy syndromes, rare genetic disorders, mast cell disorders) have mechanistic links ranging from highly speculative to absent.

**To proceed, the following is needed:**
- Retrieval of the full Mechanism of Action (MOA) for Dornase alfa from the DrugBank API (currently a high-severity data gap per this pack)
- Retrieval and review of the approved SmPC/PIL (Danish or EMA) for Dornase alfa to complete safety profiling (key warnings, contraindications) — currently a blocking data gap
- Verification of current EMA/Laegemiddelstyrelsen marketing authorisation status and local supply availability for Pulmozyme
- For **mixed mineral dust pneumoconiosis** specifically: a targeted literature review in occupational medicine databases (e.g., NIOSHTIC, CISDOC) to confirm absence of any preclinical NET-in-pneumoconiosis evidence before closing this hypothesis
- For **tendinopathy** (if prioritised for further evaluation): commissioning or identifying a preclinical proof-of-concept study (NET degradation in tendon tissue models) as a prerequisite before any consideration of a clinical-stage repurposing programme
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

