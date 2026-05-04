---
layout: default
title: Celecoxib
parent: 僅模型預測 (L5)
nav_order: 100
evidence_level: L5
indication_count: 10
---

# Celecoxib
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

# Celecoxib: From Arthritis and Pain Management to Acromesomelic Dysplasia, Hunter-Thompson Type

---

## One-Sentence Summary

Celecoxib is a selective COX-2 inhibitor with established international approvals for osteoarthritis, rheumatoid arthritis, and acute pain, though it currently holds no marketing authorisation in Denmark.
The TxGNN model predicts it may be effective for **Acromesomelic Dysplasia, Hunter-Thompson Type** with a prediction score of **99.88%**, however **no clinical trials or published literature** currently support this specific direction.
Across all five unique predicted indications in this multi-candidate evaluation, evidence remains at L4–L5 level; rheumatoid vasculitis (rank 5) represents the most biologically plausible target, supported by a single case report.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Osteoarthritis, rheumatoid arthritis, and acute pain (based on international approvals; no Danish marketing authorisation on record) |
| Predicted New Indication | Acromesomelic dysplasia, Hunter-Thompson type |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L5 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## All Predicted Indications — Summary

> This is a multi-indication candidate (`TW-DB00482-multi`). The table below deduplicates the top-ranked unique predictions for context before the detailed analysis of Rank 1.

| Rank | Disease | TxGNN Score | Evidence Level | Recommendation | Key Observation |
|------|---------|-------------|----------------|----------------|-----------------|
| 1 | Acromesomelic dysplasia, Hunter-Thompson type | 99.88% | L5 | Hold | GDF5 developmental defect — no trials or literature; very weak mechanistic link |
| 3 | Brachyolmia-amelogenesis imperfecta syndrome | 99.86% | L5 | Hold | Extremely rare syndrome; no actionable biological rationale |
| 5 | Rheumatoid vasculitis | 99.85% | L4 | Research Question | 1 case report available; RA complication — most plausible mechanistic link |
| 7 | Myosclerosis | 99.85% | L5 | Hold | Rare genetic fibrotic myopathy; inflammation is not the primary driver |
| 9 | Hypermobility of coccyx | 99.83% | L5 | Hold | NSAIDs already used for musculoskeletal pain — not a meaningful repurposing signal |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data from DrugBank was not available at the time of this evaluation. Based on established pharmacological knowledge, Celecoxib is a **selective inhibitor of cyclooxygenase-2 (COX-2)**, reducing the synthesis of prostaglandin E2 (PGE2) and thereby attenuating pain and inflammatory signalling. It belongs to the NSAID class but with selectivity that reduces gastrointestinal side effects compared to non-selective NSAIDs. It is approved by EMA for osteoarthritis, rheumatoid arthritis, and ankylosing spondylitis under the brand name Celebrex.

**Acromesomelic dysplasia, Hunter-Thompson type** is a rare autosomal recessive skeletal dysplasia caused by loss-of-function mutations in the *GDF5* gene (Growth Differentiation Factor 5). The condition is characterised by disproportionate shortening of the forearms and lower legs due to abnormal cartilage and bone development during embryogenesis. This is fundamentally a **developmental structural defect**, not an inflammation-driven disease process that would be amenable to COX-2 inhibition.

While COX-2/PGE2 signalling does play a modulatory role in bone remodelling, the absence or dysfunction of GDF5 cannot be corrected through anti-inflammatory mechanisms. The TxGNN high prediction score (99.88%) most likely reflects **topological proximity between skeletal disease nodes** in the biomedical knowledge graph — a known limitation of graph-based prediction when structural similarity does not imply mechanistic relevance. The biological rationale for this repurposing hypothesis is considered very weak, and no supporting clinical or preclinical data have been identified.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for the combination of Celecoxib and acromesomelic dysplasia, Hunter-Thompson type.

---

## Literature Evidence

Currently no related literature available for the combination of Celecoxib and acromesomelic dysplasia, Hunter-Thompson type.

### Supplementary: Literature for Rheumatoid Vasculitis (Rank 5)

The following publication was identified for the most clinically plausible predicted indication and is provided for completeness:

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [34847873](https://pubmed.ncbi.nlm.nih.gov/34847873/) | 2021 | Case Report | BMC Neurology | Describes spinal subarachnoid haemorrhage secondary to spinal rheumatoid vasculitis; highlights the severity and rarity of this extra-articular RA complication. The pathogenesis is described as unknown. Does not evaluate Celecoxib as a treatment. |

---

## Denmark Market Information

Celecoxib currently holds **no marketing authorisation** with the Danish Medicines Agency (Laegemiddelstyrelsen). No authorisation records are registered in the national database.

> For reference, Celecoxib is authorised in the EU under the centralised EMA procedure as **Celebrex** (Pfizer) for osteoarthritis, rheumatoid arthritis, and ankylosing spondylitis in adults. Any use in Denmark would require import authorisation or compassionate use arrangements under applicable Danish legislation.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for complete safety information.

> Based on established pharmacological knowledge of the COX-2 inhibitor class, the following considerations are clinically relevant and should be reviewed against the current EMA SmPC before any use:
> - **Cardiovascular risk**: Increased risk of serious arterial thrombotic events (myocardial infarction, stroke), particularly with long-term use or in patients with existing cardiovascular disease
> - **Hypersensitivity**: Contraindicated in patients with sulfonamide hypersensitivity; cross-reactivity risk must be assessed
> - **Renal impairment**: Prostaglandin-dependent renal function may be compromised; use with caution
> - **Gastrointestinal risk**: Lower than non-selective NSAIDs but still present, especially in combination with aspirin or anticoagulants
>
> Formal Danish/EMA SmPC data was not retrieved in this evaluation cycle (data gap DG001).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top predicted indication — acromesomelic dysplasia, Hunter-Thompson type — has no supporting clinical trials or literature, and the mechanistic link between COX-2 inhibition and a GDF5-related skeletal developmental disorder is not biologically credible. The high TxGNN score reflects knowledge graph topology, not direct pharmacological relevance. Furthermore, Celecoxib is not currently marketed in Denmark, adding a regulatory barrier to any clinical programme.

**To proceed, the following is needed:**

- **MOA documentation**: Retrieve formal mechanism of action data from DrugBank (data gap DG002) to enable mechanistic plausibility scoring
- **Safety data retrieval**: Download and parse the EMA SmPC for Celecoxib to complete the safety profile (data gap DG001)
- **Redirect repurposing focus**: Among current predictions, **rheumatoid vasculitis (rank 5)** is the most clinically credible target — Celecoxib's RA approval provides a direct mechanistic bridge, and a dedicated literature and clinical trial search (beyond the current query scope) is warranted
- **Regulatory pathway assessment**: If pursuing any Danish clinical investigation, clarify the pathway for use of a non-marketed product (compassionate use, import licence, or investigational medicinal product authorisation)
- **Biomarker and patient selection**: For a rheumatoid vasculitis investigation, a prospective observational study or mechanistic pilot trial should be designed with appropriate patient selection criteria (active RA with extra-articular manifestations) and endpoints (inflammatory markers, vascular imaging)

---

*⚠️ This report is intended for research purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before any therapeutic application. Data as of 2026-04-04.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

