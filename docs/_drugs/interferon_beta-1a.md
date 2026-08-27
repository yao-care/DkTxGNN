---
layout: default
title: Interferon Beta-1A
parent: 僅模型預測 (L5)
nav_order: 238
evidence_level: L5
indication_count: 10
---

# Interferon Beta-1A
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

# Interferon beta-1a: From Multiple Sclerosis to Jeune Syndrome Situs Inversus

## One-Sentence Summary

Interferon beta-1a is an immunomodulatory biologic globally established for relapsing forms of multiple sclerosis. The TxGNN model predicts a possible link to **Jeune syndrome situs inversus** (a rare congenital ciliopathy/skeletal dysplasia) with a **97.47% prediction score**, but this direction currently has **zero clinical trials and zero publications** supporting it, and the model's own rationale flags the score as likely a knowledge-graph artefact rather than a genuine signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Multiple Sclerosis (well-established global indication; not present in the supplied Danish regulatory dataset — see note below) |
| Predicted New Indication | Jeune syndrome situs inversus |
| TxGNN Prediction Score | 97.47% |
| Evidence Level | L5 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

*Note: `taiwan_regulatory.licenses` is empty for this evidence pack (product not currently authorised in Denmark), so the original indication above is drawn from the drug's globally documented use — corroborated by the multiple-sclerosis literature present elsewhere in this evidence pack — rather than from Danish label text.*

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data is not available (flagged as a High-severity data gap, DG002). Based on known information, interferon beta-1a exerts antiviral and immunomodulatory effects via IFNAR signalling and modulation of Th1/Th17 responses, and its efficacy in relapsing multiple sclerosis is well established.

However, the model's own repurposing rationale for this specific prediction is explicitly negative: Jeune syndrome (asphyxiating thoracic dystrophy) with situs inversus is a congenital ciliopathy and skeletal dysplasia — a structural/developmental disorder, not an immune or inflammatory condition. There is **no known mechanistic overlap** with interferon beta-1a's antiviral/immunomodulatory pathway.

The evidence pack itself attributes the unusually high TxGNN score to a likely graph artefact: rare-disease nodes in the knowledge graph tend to have sparse connectivity, which can inflate similarity-based prediction scores without reflecting genuine biological plausibility. This prediction should therefore be treated as a hypothesis-generation output only, not as evidence of therapeutic potential.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Denmark Market Information

Interferon beta-1a does not currently hold any marketing authorisation in Denmark under this evidence pack (market status: **Not marketed**, 0 authorisations on file).

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information. (Danish label warnings, contraindications, and drug-interaction data are recorded as a Blocking data gap, DG001, and were not available for this evaluation.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This prediction has no supporting clinical trials or literature, and the model's own rationale identifies it as a probable false positive driven by sparse connectivity around a rare-disease node rather than a genuine mechanistic signal. Evidence Level L5 (model prediction only) does not support advancing this candidate.

**To proceed, the following is needed:**
- Danish SmPC warnings/contraindications (DG001, Blocking) — required before any S1 safety screening can begin
- Verified mechanism-of-action data (DG002, High) to properly assess biological plausibility
- Independent re-scoring or manual review of this drug–disease pair, given the documented risk of noise in sparsely connected rare-disease knowledge-graph nodes
- Any preclinical or mechanistic evidence connecting type-I interferon signalling to ciliopathy/skeletal dysplasia pathology, which is currently entirely absent
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

