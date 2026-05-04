---
layout: default
title: Eculizumab
parent: 僅模型預測 (L5)
nav_order: 154
evidence_level: L5
indication_count: 10
---

# Eculizumab
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

# Eculizumab: From Complement-Mediated Diseases to Cyclic Hematopoiesis

## One-Sentence Summary

Eculizumab (Soliris) is a humanised monoclonal antibody that blocks terminal complement activation, approved internationally for paroxysmal nocturnal haemoglobinuria (PNH), atypical haemolytic uraemic syndrome (aHUS), generalised myasthenia gravis (gMG), and neuromyelitis optica spectrum disorder (NMOSD).
The TxGNN model predicts it may be effective for **Cyclic Hematopoiesis** (cyclic neutropenia),
with **no clinical trials** and **no publications** currently supporting this specific indication — this prediction is based on model inference alone.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Denmark; internationally approved for PNH, aHUS, gMG, and NMOSD |
| Predicted New Indication | Cyclic Hematopoiesis (cyclic neutropenia) |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the current evidence pack. Based on published pharmacology, eculizumab is a humanised IgG2/4κ monoclonal antibody that binds with high affinity to complement protein C5, blocking its cleavage into C5a (a pro-inflammatory anaphylatoxin) and C5b (the nucleating subunit of the membrane attack complex, MAC). This prevents terminal complement pathway activation, downstream cell lysis, and complement-driven inflammation. Its established efficacy in PNH and aHUS is directly attributable to this mechanism, as both conditions are characterised by uncontrolled alternative complement activation causing haemolysis and thrombotic microangiopathy.

Cyclic hematopoiesis (cyclic neutropenia) is a genetically distinct disorder caused primarily by autosomal dominant mutations in the *ELANE* gene encoding neutrophil elastase. These mutations trigger endoplasmic reticulum (ER) stress and accelerated apoptosis of neutrophil precursor cells, producing characteristic 21-day oscillations in circulating neutrophil counts. The disease mechanism is fundamentally intracellular — ER-mediated unfolded protein response and mitochondrial apoptotic signalling — rather than extracellular complement-driven destruction.

The mechanistic overlap between eculizumab's C5-blocking activity and the ELANE-mediated pathology of cyclic hematopoiesis is therefore indirect at best. While complement activation can theoretically contribute to neutrophil clearance in some haematological contexts, this is not a primary driver of cyclic neutropenia. The TxGNN model's high prediction score most likely reflects indirect linkages within the knowledge graph between complement system nodes and haematopoietic network nodes, rather than a direct pharmacological relationship supported by experimental evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for eculizumab in cyclic hematopoiesis.

---

## Literature Evidence

Currently no related literature available for eculizumab in cyclic hematopoiesis.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

> **Note:** Eculizumab carries a well-established risk of life-threatening *Neisseria meningitidis* infections. All patients treated with eculizumab internationally must be vaccinated against meningococcal disease prior to treatment initiation and may require prophylactic antibiotics. This safety consideration is critical for any future use evaluation, regardless of indication.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no clinical trial evidence or disease-specific literature supporting the use of eculizumab in cyclic hematopoiesis, and the mechanistic basis for the TxGNN prediction is weak — cyclic neutropenia is driven by intracellular ELANE-mediated ER stress, a pathway that lies outside eculizumab's C5-complement blocking mechanism of action. Additionally, eculizumab is not registered in Denmark, making near-term clinical application impossible without a formal regulatory pathway.

**To proceed, the following is needed:**

- **Preclinical mechanistic evidence:** At least one in vitro or animal-model study demonstrating a complement-dependent component in ELANE-mediated neutrophil precursor apoptosis
- **Regulatory data:** Retrieval of the approved SmPC (Soliris EU/EMA product information, EU/1/07/393) to complete safety profiling including warnings, contraindications, and meningococcal prophylaxis requirements
- **Formal MOA data:** DrugBank or EMA EPAR data confirming the molecular pharmacology to refine the mechanistic plausibility analysis
- **Indication context review:** Clarification of whether the TxGNN model conflates cyclic hematopoiesis with other complement-related neutrophil disorders (e.g., aHUS-associated neutropenia) within its knowledge graph
- **Regulatory pathway assessment:** Evaluation of the EMA centralised procedure applicability for any future compassionate use or clinical trial application in Denmark

---

> ⚠️ **Disclaimer:** This report is intended for research reference purposes only and does not constitute medical advice. All drug repurposing candidates require rigorous clinical validation before any application in patient care.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

