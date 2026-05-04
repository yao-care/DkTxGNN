---
layout: default
title: Ceftaroline Fosamil
parent: 僅模型預測 (L5)
nav_order: 98
evidence_level: L5
indication_count: 10
---

# Ceftaroline Fosamil
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

# Ceftaroline fosamil: From Bacterial Infections to Rheumatoid Arthritis

## One-Sentence Summary

Ceftaroline fosamil (brand name Zinforo) is a fifth-generation cephalosporin antibiotic, approved in the EU for acute bacterial skin and skin structure infections (ABSSSI) and community-acquired bacterial pneumonia (CABP).
The TxGNN model predicts it may be effective for **Rheumatoid Arthritis**, with a high model confidence score of **98.20%**.
However, this prediction is currently supported by **0 clinical trials** and **0 relevant publications** — and the mechanistic analysis strongly suggests this is a knowledge graph topology false positive rather than a genuine repurposing opportunity.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Acute bacterial skin and skin structure infections (ABSSSI); community-acquired bacterial pneumonia (CABP) |
| Predicted New Indication | Rheumatoid Arthritis |
| TxGNN Prediction Score | 98.20% |
| Evidence Level | L5 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known pharmacology, ceftaroline fosamil is a β-lactam antibiotic whose mechanism centres on inhibition of bacterial cell wall synthesis via binding to penicillin-binding proteins (PBPs) — notably PBP2a of MRSA — thereby achieving broad-spectrum bactericidal activity against Gram-positive and selected Gram-negative pathogens.

Rheumatoid arthritis (RA) is an autoimmune condition driven by dysregulated T- and B-cell activation, synovial hyperplasia, and a pro-inflammatory cytokine cascade dominated by TNF-α and IL-6. There is no known pharmacological pathway by which PBP binding or cell wall synthesis inhibition would modulate autoimmune inflammation. Unlike tetracyclines or macrolides — which possess pleiotropic anti-inflammatory properties independent of their antimicrobial effects — β-lactam antibiotics have no established immunomodulatory mechanism relevant to RA pathophysiology.

The most plausible explanation for this high TxGNN score is an indirect knowledge graph (KG) connection: ceftaroline nodes linked to "septic arthritis treatment" or "joint infection" are topologically proximate to RA nodes within the graph, producing an artifactual high-confidence prediction. This is a known limitation of graph-based models when infectious disease nodes share structural proximity with inflammatory joint disease nodes. The prediction should be treated as a **graph topology false positive** pending any contrary experimental evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Ceftaroline fosamil in Rheumatoid Arthritis.

---

## Literature Evidence

Currently no related literature available for Ceftaroline fosamil in Rheumatoid Arthritis.

---

## Denmark Market Information

Ceftaroline fosamil currently holds no marketing authorisation active in the Danish market. The drug does hold a centralised EMA authorisation (Zinforo, EU/1/12/787/001-004) valid across the EU/EEA; however, it is not commercially distributed in Denmark at the time of this report.

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|-------------------------------|-------------|-------------|---------------------|
| EU/1/12/787 (EMA — not actively marketed in DK) | Zinforo | Powder for concentrate for solution for infusion (600 mg) | Acute bacterial skin and skin structure infections; community-acquired bacterial pneumonia in adults |

---

## Safety Considerations

Detailed Danish/TFDA SmPC warnings and contraindications were not available in this Evidence Pack. Please refer to the approved Summary of Product Characteristics (SmPC) for Zinforo — available via the [EMA product page](https://www.ema.europa.eu/en/medicines/human/EPAR/zinforo) — for full safety information including hypersensitivity reactions, *Clostridioides difficile*-associated diarrhoea, haematological effects (haemolytic anaemia, neutropenia), and renal dose adjustment requirements.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model assigns a high numerical score (98.20%), but this is almost certainly a knowledge graph topology artefact driven by proximity between infectious arthritis and inflammatory arthritis nodes — not a genuine pharmacological signal. Ceftaroline fosamil has no known mechanism relevant to autoimmune or degenerative joint disease, and the complete absence of supporting clinical trials or peer-reviewed literature confirms this assessment. Proceeding would not meet any scientific or regulatory standard for a repurposing programme.

**To advance beyond Hold, the following would be required:**

- **Mechanistic evidence**: Identification of a plausible biological mechanism linking PBP binding (or any ceftaroline off-target effect) to RA pathophysiology — currently none exists in the published literature.
- **Experimental in vitro / in vivo data**: Demonstration of anti-inflammatory activity in validated RA models (e.g., CIA mouse model, synoviocyte assays).
- **KG audit**: Review of the knowledge graph edge path generating this prediction to confirm or refute the suspected false-positive topology.
- **Safety data**: Retrieval and review of the full Zinforo SmPC, including immunological effects and any post-marketing signals relevant to inflammatory conditions.
- **Clinical context clarification**: The 2 PubMed publications retrieved (PMIDs [27530754](https://pubmed.ncbi.nlm.nih.gov/27530754/) and [23312602](https://pubmed.ncbi.nlm.nih.gov/23312602/)) concern *osteoarticular infection* management — not RA or degenerative joint disease — and do not constitute evidence for any of the predicted non-infectious indications in this pack.

> **Research disclaimer**: This report is for research reference only and does not constitute medical advice. All drug repurposing candidates require clinical validation before application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

