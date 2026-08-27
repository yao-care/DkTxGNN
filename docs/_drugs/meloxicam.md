---
layout: default
title: Meloxicam
parent: 僅模型預測 (L5)
nav_order: 282
evidence_level: L5
indication_count: 10
---

# Meloxicam
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

# Meloxicam: From Osteoarthritis to Acromesomelic Dysplasia (Hunter-Thompson Type)

## One-Sentence Summary

Meloxicam is a well-established non-steroidal anti-inflammatory drug (NSAID) widely used for osteoarthritis, rheumatoid arthritis, and musculoskeletal pain through preferential inhibition of the COX-2 enzyme.
The TxGNN model predicts it may have therapeutic potential for **Acromesomelic Dysplasia, Hunter-Thompson Type** — a rare autosomal recessive skeletal dysplasia — with a prediction confidence of **99.92%**.
However, **no clinical trials and no published literature** currently support this specific repurposing direction, placing this candidate at the lowest evidence tier (L5).

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Osteoarthritis; Rheumatoid Arthritis; Musculoskeletal pain (no Danish registration record available in dataset) |
| Predicted New Indication | Acromesomelic Dysplasia, Hunter-Thompson Type |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 |
| Denmark Market Status | Not Marketed (per current dataset — see note below) |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

> **Data Note:** Meloxicam is a globally established NSAID with EMA-authorised products available across EU member states. The "Not Marketed" status recorded here likely reflects a data collection gap rather than a true absence from the Danish market. Verification through Lægemiddelstyrelsen and the EMA product database is strongly recommended before drawing regulatory conclusions.

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on publicly known information, Meloxicam belongs to the oxicam class of NSAIDs and exerts its effects primarily through preferential inhibition of cyclooxygenase-2 (COX-2), thereby reducing prostaglandin synthesis. This leads to anti-inflammatory, analgesic, and antipyretic effects. Its COX-2 selectivity is considered to confer a lower gastrointestinal risk compared to non-selective NSAIDs.

Acromesomelic dysplasia, Hunter-Thompson type (AMDH) is a rare autosomal recessive disorder caused by loss-of-function mutations in the **GDF5** gene (growth differentiation factor 5), which encodes a signalling ligand critical for skeletal and joint morphogenesis. The condition manifests as disproportionate shortening of the middle and distal limb segments and is a fundamentally structural, developmental bone dysplasia — not driven by chronic inflammation.

The mechanistic link between COX-2 inhibition and AMDH is indirect at best. Prostaglandins do participate in bone remodelling and growth plate signalling, and there is emerging evidence that COX-2/PGE₂ pathways interact with BMP (bone morphogenetic protein) signalling networks — of which GDF5 is a member. However, no preclinical studies have investigated this connection in GDF5-deficient models, and the TxGNN high-confidence score most plausibly reflects **graph-structural clustering**: AMDH neighbours other skeletal dysplasias in the knowledge graph where NSAIDs frequently appear as candidate agents, rather than a validated pharmacological relationship. This prediction is currently at hypothesis level only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Denmark Market Information

No marketing authorisation records for Meloxicam are present in the current dataset. As noted above, this is inconsistent with Meloxicam's broad international availability and EU regulatory history, and should be treated as a data gap pending verification.

For authoritative information on Danish and EMA authorisations, consult:
- [Lægemiddelstyrelsen (DKMA) product database](https://laegemiddelstyrelsen.dk)
- [EMA European Public Assessment Reports (EPARs)](https://www.ema.europa.eu/en/medicines)

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information. Safety data — including key warnings, contraindications, and drug interaction profiles — were not available in this evidence pack and must be retrieved from the SmPC prior to any clinical evaluation.

Of note for a COX-2 preferential NSAID such as Meloxicam, standard class-level considerations typically include cardiovascular risk, renal function monitoring, gastrointestinal tolerability, and caution in the elderly — but these should be confirmed from the authorised SmPC for the specific product and the target patient population.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Meloxicam's TxGNN prediction score for acromesomelic dysplasia (Hunter-Thompson type) is high (99.92%), but the prediction reflects knowledge graph topology rather than established pharmacology: AMDH is a monogenic skeletal dysplasia with no known dependency on COX-2/prostaglandin pathways, and there is a complete absence of supporting clinical trials or peer-reviewed literature (Evidence Level L5). Proceeding without additional biological justification would not be warranted.

**To proceed, the following is needed:**

- **Market status clarification:** Verify actual Danish and EMA authorisation status via Lægemiddelstyrelsen and EMA databases
- **MOA and safety data:** Retrieve full DrugBank entry and authorised SmPC to complete drug-level characterisation
- **Mechanistic validation:** Commission or identify preclinical studies examining COX-2/PGE₂ interactions with GDF5-BMP signalling in relevant skeletal dysplasia models
- **Orphan disease context:** Assess whether anti-inflammatory or anti-remodelling effects could provide any symptomatic benefit to AMDH patients, independently of disease modification
- **Broader landscape review:** Consider whether any of the five distinct TxGNN-predicted indications (AMDH, brachyolmia-amelogenesis imperfecta syndrome, myosclerosis, brachyolmia, pseudoachondroplasia) — all rare skeletal/connective tissue disorders — share a common mechanistic thread that could justify a shared investigational strategy for Meloxicam
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

