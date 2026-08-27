---
layout: default
title: Velaglucerase Alfa
parent: 僅模型預測 (L5)
nav_order: 466
evidence_level: L5
indication_count: 10
---

# Velaglucerase Alfa
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

# Velaglucerase alfa: From Gaucher Disease to Steel Syndrome

## One-Sentence Summary

Velaglucerase alfa is an enzyme replacement therapy (recombinant glucocerebrosidase) established for Gaucher disease. The TxGNN model predicts a possible link to **Steel syndrome**, a rare skeletal dysplasia, but this prediction is currently supported by **0 clinical trials** and **0 publications**, and the underlying mechanistic rationale is assessed as weak.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Gaucher disease (per DrugBank enzyme-replacement classification; no Danish regulatory record exists since the drug is not marketed) |
| Predicted New Indication | Steel syndrome |
| TxGNN Prediction Score | 96.99% |
| Evidence Level | L5 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for Velaglucerase alfa is not available in this evidence pack. Based on available information, Velaglucerase alfa is an enzyme replacement therapy supplying recombinant glucocerebrosidase, with proven efficacy in Gaucher disease, a lysosomal storage disorder.

Steel syndrome is caused by *COL27A1* mutations and results in skeletal dysplasia. It has no known direct enzymatic or metabolic pathway relationship with glucocerebrosidase replacement. The high TxGNN score most likely reflects similarity between skeletal/joint phenotype nodes in the knowledge graph — Gaucher disease also commonly involves skeletal manifestations (bone infarcts, osteopenia) — rather than a genuine shared pharmacological mechanism.

Given this, the prediction should be treated as a hypothesis-generating signal arising from phenotype-level graph similarity, not as evidence of direct pharmacological applicability to Steel syndrome.

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
The prediction rests solely on TxGNN model output (L5, no clinical trials or literature), and the proposed mechanistic link to Steel syndrome is indirect (shared skeletal-phenotype graph nodes rather than a shared pharmacological pathway). Velaglucerase alfa is also not currently marketed in Denmark, so no regulatory or real-world usage data exist to support further evaluation.

**To proceed, the following is needed:**
- Confirmed mechanism-of-action data for Velaglucerase alfa (currently a Blocking/High-severity data gap)
- Danish/EU SmPC warnings, contraindications, and interaction data (currently a Blocking data gap — required before any S1 safety assessment)
- Preclinical or case-level evidence establishing a plausible biological link between glucocerebrosidase replacement and Steel syndrome pathology
- Note: other candidate indications in this batch (esophageal varices, hypophosphatasia, Wolman disease) show similarly weak, indirect mechanistic rationale and the same L5/Hold status — none currently warrant prioritization over Steel syndrome.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

