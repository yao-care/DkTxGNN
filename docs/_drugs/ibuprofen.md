---
layout: default
title: Ibuprofen
parent: 僅模型預測 (L5)
nav_order: 219
evidence_level: L5
indication_count: 10
---

# Ibuprofen
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

# Ibuprofen: From Pain and Inflammation to Acromesomelic Dysplasia, Hunter-Thompson Type

## One-Sentence Summary

Ibuprofen is a well-established non-steroidal anti-inflammatory drug (NSAID), widely used for the treatment of pain, fever, and inflammatory conditions. The TxGNN model predicts it may have activity in **Acromesomelic Dysplasia, Hunter-Thompson Type** — a rare congenital skeletal dysplasia caused by CDMP1/GDF5 gene mutations. This prediction is supported by **no clinical trials and no published literature**, and represents model-level speculation only (Evidence Level L5).

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Pain, fever, and inflammatory conditions (established NSAID) |
| Predicted New Indication | Acromesomelic Dysplasia, Hunter-Thompson Type |
| TxGNN Prediction Score | 99.74% |
| Evidence Level | L5 |
| Denmark Market Status | Danish regulatory data not retrieved in this Evidence Pack |
| Number of Marketing Authorisations | Danish regulatory data not retrieved in this Evidence Pack |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data was not retrieved in this Evidence Pack. Based on established pharmacology, Ibuprofen inhibits cyclooxygenase enzymes (COX-1 and COX-2), thereby reducing synthesis of prostaglandin E2 (PGE2). This underpins its well-characterised anti-inflammatory, analgesic, and antipyretic properties across a broad range of inflammatory and pain conditions.

Acromesomelic dysplasia, Hunter-Thompson type, is a rare autosomal recessive skeletal dysplasia caused by loss-of-function mutations in the *CDMP1/GDF5* gene, which encodes a member of the bone morphogenetic protein (BMP) family. The condition is characterised by shortening of the middle and distal limb segments (acromesomelia) arising during embryonic skeletal development, with no established inflammatory driver of disease progression.

The proposed mechanistic link — that COX inhibition and reduced PGE2 might indirectly modulate BMP/GDF signalling and osteoblast activity — is biologically speculative and unsupported by experimental or clinical data. PGE2 does participate in bone remodelling, but its relevance to a congenital structural defect driven by GDF5 haploinsufficiency is not established. The high TxGNN prediction score most likely reflects topological proximity between the ibuprofen node and rare skeletal disease nodes within the knowledge graph, rather than a genuine biological connection. This interpretation is consistent with the complete absence of supporting clinical trials or publications.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Denmark Market Information

Danish regulatory data (Lægemiddelstyrelsen) was not successfully retrieved in this Evidence Pack — only DrugBank data was ingested. Ibuprofen (DB01050) is a long-established NSAID with widespread use across European markets, and Danish authorisations are expected to exist under multiple brand names and dosage forms. Healthcare professionals should consult the Lægemiddelstyrelsen product registry directly for current authorisation status, approved indications, and Summary of Product Characteristics (SmPC).

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|-------------------------------|-------------|-------------|---------------------|
| — | Data not retrieved | — | Consult Lægemiddelstyrelsen registry |

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All top-ranked TxGNN predictions for Ibuprofen map exclusively to rare congenital skeletal dysplasias (acromesomelic dysplasia, brachyolmia-amelogenesis imperfecta syndrome, myosclerosis, brachyolmia, brachydactyly-syndactyly syndrome) — structural developmental defects with no inflammatory aetiology. Ibuprofen's COX-inhibition mechanism has no plausible disease-modifying rationale for these conditions, and zero clinical trials or publications support any of these predictions.

**To proceed, the following is needed:**

- **Danish regulatory data** must be retrieved from Lægemiddelstyrelsen to confirm current authorisation status, approved indications, and SmPC safety information
- **Mechanism of action data** should be retrieved from the DrugBank API (DG002) to enable formal mechanistic linkage analysis
- **TFDA SmPC safety data** (DG001) must be retrieved before any safety evaluation can proceed
- These TxGNN predictions should be flagged for **model quality review**: the clustering of rare skeletal dysplasias as top-ranked candidates for a common NSAID strongly suggests a knowledge graph topology artefact (topology clustering artifact) rather than genuine repurposing signal
- If future investigation is desired, a **rare disease or clinical pharmacology specialist** should assess biological plausibility before any further development steps are considered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

