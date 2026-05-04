---
layout: default
title: Naproxen
parent: 僅模型預測 (L5)
nav_order: 248
evidence_level: L5
indication_count: 8
---

# Naproxen
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

# Naproxen: From Pain and Inflammation Management to Brachydactyly-Syndactyly Syndrome

## One-Sentence Summary

Naproxen is a well-established non-steroidal anti-inflammatory drug (NSAID), widely used for pain relief, fever, and inflammatory conditions such as arthritis and dysmenorrhoea.
The TxGNN model predicts it may be effective for **Brachydactyly-Syndactyly Syndrome**, a rare congenital skeletal malformation disorder.
However, **no clinical trials and no published literature** currently support this indication, and the mechanistic link is considered biologically weak — this prediction is most likely a knowledge graph artefact.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Pain, fever, and inflammation (well-established NSAID; no Danish regulatory data available in this data package) |
| Predicted New Indication | Brachydactyly-Syndactyly Syndrome |
| TxGNN Prediction Score | 99.35% |
| Evidence Level | L5 |
| Denmark Market Status | Not marketed (per current data; no marketing authorisations on record) |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Naproxen is a propionic acid-class NSAID whose primary mechanism is inhibition of cyclooxygenase enzymes (COX-1 and COX-2), reducing prostaglandin synthesis. This forms the pharmacological basis for its anti-inflammatory, analgesic, and antipyretic effects. Detailed mechanism of action data was not available in the current data package; the above is based on well-established pharmacological knowledge.

Brachydactyly-syndactyly syndrome is a rare, genetically determined congenital malformation characterised by abnormally short digits (brachydactyly) and fused digits (syndactyly). These are fixed structural defects established during foetal development — fundamentally distinct from the acquired inflammatory processes that Naproxen targets. There is no recognised clinical rationale for COX inhibition to correct or ameliorate pre-existing skeletal structural anomalies.

The speculative mechanistic path proposed by the model — COX-2 inhibition → reduced PGE2 → disrupted bone remodelling signalling → indirect crosstalk with BMP/GDF developmental pathways — is not supported by clinical or preclinical evidence for this specific syndrome. The high TxGNN prediction score almost certainly reflects a **knowledge graph false positive**: both Naproxen and skeletal dysplasias share "skeletal" category nodes in the underlying graph, creating a spurious structural association. This prediction should be interpreted with considerable scepticism.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a superficially high TxGNN prediction score (99.35%), this candidate has no supporting clinical trial or literature evidence (Evidence Level L5), and the proposed mechanistic link between COX inhibition and a congenital structural skeletal defect is biologically implausible. The prediction most likely represents a structural bias in the knowledge graph rather than a genuine therapeutic opportunity.

**To proceed, the following is needed:**
- **Biological plausibility review:** Independent expert assessment of whether COX/prostaglandin inhibition could have any meaningful therapeutic effect on a genetically determined congenital skeletal malformation
- **Knowledge graph audit:** Investigate whether shared "skeletal" category nodes in the TxGNN graph are generating systematic false positives for Naproxen across rare skeletal dysplasias (note: ranks 3–8 in this pack are all rare skeletal/developmental syndromes, suggesting a pattern)
- **MOA data retrieval:** Obtain full pharmacological profile from DrugBank (DB00788) to support or refute any mechanistic hypothesis
- **Safety data retrieval:** Download and parse the SmPC from Lægemiddelstyrelsen to complete the safety profile, including warnings, contraindications, and drug interactions
- **Danish regulatory data verification:** Confirm current marketing authorisation status of Naproxen-containing products with Lægemiddelstyrelsen; the absence of authorisation records in this data package likely reflects a data gap, as Naproxen is a long-established NSAID
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

