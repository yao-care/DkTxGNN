---
layout: default
title: Dexibuprofen
parent: 僅模型預測 (L5)
nav_order: 139
evidence_level: L5
indication_count: 10
---

# Dexibuprofen
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

# Dexibuprofen: From Pain and Inflammation to Brachydactyly-Syndactyly Syndrome

## One-Sentence Summary

Dexibuprofen is the pharmacologically active S-enantiomer of ibuprofen, a well-established non-steroidal anti-inflammatory drug (NSAID) that works by inhibiting the COX enzyme to reduce pain and inflammation. The TxGNN model predicts it may be effective for **Brachydactyly-Syndactyly Syndrome**, a rare hereditary skeletal malformation disorder. However, **no clinical trials and no published literature** currently support this predicted direction, and the mechanistic rationale is considered highly speculative.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Denmark; internationally used for pain, fever, and inflammation (NSAID/COX inhibitor) |
| Predicted New Indication | Brachydactyly-Syndactyly Syndrome |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L5 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Dexibuprofen is the S(+)-enantiomer of ibuprofen and acts primarily by inhibiting cyclooxygenase (COX-1 and COX-2) enzymes, thereby reducing the synthesis of prostaglandin E2 (PGE2) and other pro-inflammatory mediators. It is generally considered to have a comparable or slightly improved tolerability profile compared to racemic ibuprofen, while retaining the same analgesic, antipyretic, and anti-inflammatory properties.

Brachydactyly-syndactyly syndrome is a rare hereditary condition characterised by abnormally short fingers and toes (brachydactyly) with soft tissue or bony fusion (syndactyly). The disorder is caused by mutations in developmental genes such as *IHH* (Indian Hedgehog) and *HOXD13*, which govern skeletal morphogenesis during embryogenesis. There is no established pharmacological connection between the COX/PGE2 pathway and these genetic developmental programmes.

While PGE2 is known to play a modulatory role in bone metabolism — including interactions with BMP/Wnt signalling pathways that influence osteoblast activity — this relationship does not translate to a plausible therapeutic rationale for a monogenic skeletal dysplasia syndrome. The TxGNN model's high prediction score (99.87%) most likely reflects a broad network connectivity effect among skeletal phenotype nodes within the knowledge graph, rather than a genuine pharmacological signal. This prediction is considered **biologically speculative** and should be interpreted with caution.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Denmark Market Information

Dexibuprofen (DrugBank ID: DB09213) currently holds **no marketing authorisations** in Denmark and is not available on the Danish market. No product licences have been issued by the Danish Medicines Agency (Lægemiddelstyrelsen), and no centralised European Medicines Agency (EMA) authorisations are on record for this active substance.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

> **Note for clinicians:** As an NSAID and COX inhibitor, dexibuprofen shares a class-based safety profile that typically includes gastrointestinal, cardiovascular, and renal considerations. Since no Danish SmPC is available, international product information (e.g., from countries where the drug is marketed) should be consulted before any clinical use.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model generates a high prediction score, but this is unsupported by any clinical trial evidence, published literature, or mechanistic biological plausibility. Brachydactyly-syndactyly syndrome is a monogenic skeletal dysplasia for which COX inhibition has no established therapeutic role; the prediction is assessed as a knowledge graph artefact rather than a genuine repurposing signal.

**To proceed, the following is needed:**

- **Mechanistic validation**: Preclinical studies examining whether COX inhibition or PGE2 modulation can influence IHH or HOXD13 signalling in relevant in vitro or in vivo models — currently absent from the literature.
- **Safety data retrieval**: Obtain the full SmPC from a country where dexibuprofen is authorised (e.g., Austria, Spain), and assess key warnings and contraindications before any further evaluation.
- **Drug interaction data**: Conduct a formal DDI assessment, as no interaction data was retrieved in the current evidence pack.
- **TxGNN model calibration review**: Evaluate whether the consistently high scores across multiple rare skeletal/connective tissue syndromes reflect a systematic over-prediction bias for musculoskeletal phenotype clusters in the knowledge graph.
- **Re-assess against lower-ranked predictions**: Consider whether indications with stronger mechanistic links (e.g., inflammatory or pain-related conditions) might represent more tractable repurposing opportunities not captured at the top of the current ranking.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

