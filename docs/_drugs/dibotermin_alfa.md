---
layout: default
title: Dibotermin Alfa
parent: 僅模型預測 (L5)
nav_order: 141
evidence_level: L5
indication_count: 10
---

# Dibotermin Alfa
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

# Dibotermin alfa: From Bone Repair to Esotropia

## One-Sentence Summary

Dibotermin alfa is a recombinant human Bone Morphogenetic Protein-2 (rhBMP-2), a biological agent used in orthopaedic surgery to stimulate bone formation in spinal fusion and fracture repair.
The TxGNN model predicts it may be effective for **Esotropia** (inward-turning convergent squint), with a prediction score of **99.97%**.
However, **no clinical trials and no supporting literature** exist for this indication, and the internal mechanistic assessment flags this prediction as a knowledge graph topology artefact with no demonstrable biological plausibility.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Bone repair and spinal fusion (EMA-authorised centrally; not registered in Denmark) |
| Predicted New Indication | Esotropia |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Detailed mechanism of action data is not available in the current evidence pack. Based on known pharmacology, Dibotermin alfa is a recombinant form of human Bone Morphogenetic Protein-2 (BMP-2). It binds cell-surface BMP receptors and activates the intracellular SMAD1/5/8 signalling cascade, which commits mesenchymal stem cells to osteogenic (bone-forming) differentiation. In clinical use, the protein is delivered locally — embedded in an absorbable collagen sponge — directly at the surgical site, where it accelerates and augments new bone growth during spinal fusion or long bone repair.

Esotropia is a form of convergent strabismus in which one or both eyes turn inward, caused by imbalance in the tension and neuromuscular coordination of the extraocular muscles. The underlying pathophysiology involves ocular motor neurone development, proprioceptive feedback loops, and accommodative-convergence reflexes — none of which are governed by the BMP-2/SMAD pathway. There is no established biological role for BMP-2 signalling in extraocular muscle tone or the neural control of eye alignment.

The mechanistic assessment embedded in the evidence pack explicitly concludes that there is a **complete absence of biological plausibility** for this prediction. The very high TxGNN score (0.9997) is attributed to a **knowledge graph topology effect**: the two entities are close neighbours in the underlying network structure, but this proximity reflects shared graph connections rather than any pharmacological relationship. This prediction should be treated as a model artefact rather than a genuine therapeutic hypothesis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Denmark Market Information

Dibotermin alfa is **not currently marketed in Denmark**. The Danish Medicines Agency (Laegemiddelstyrelsen) has issued no national marketing authorisations for this product, and it does not appear on the Danish market. For reference, the product is known internationally under the brand name **InductOS®** and holds a centralised EMA marketing authorisation for the European Union for orthopaedic indications; however, this does not translate to active market availability in Denmark.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There are no clinical trials, no relevant literature, and no plausible mechanistic link between Dibotermin alfa and esotropia. The TxGNN model's high confidence score (99.97%) is assessed as a knowledge graph topology artefact, not a pharmacological signal. No basis exists to initiate a repurposing programme for this indication.

**To proceed with any further evaluation, the following would be needed:**

- A credible biological hypothesis connecting BMP-2/SMAD1/5/8 signalling to extraocular muscle physiology, ocular motor neurone development, or strabismus pathogenesis
- Preclinical evidence (in vitro or animal model) demonstrating BMP-2 activity in ocular or neuromuscular tissue relevant to eye alignment
- Retrieval of the full SmPC and prescribing information to characterise the drug's safety, contraindications, and drug interaction profile before any further repurposing evaluation
- Clarification of the officially approved indication(s) in the relevant jurisdiction(s), as the current evidence pack contains no confirmed original indication data

> **Disclaimer:** This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before any application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

