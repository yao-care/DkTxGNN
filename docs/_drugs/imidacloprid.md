---
layout: default
title: Imidacloprid
parent: 僅模型預測 (L5)
nav_order: 226
evidence_level: L5
indication_count: 10
---

# Imidacloprid
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

# Imidacloprid: From Insecticide (No Approved Human Indication) to Cauda Equina Syndrome

## One-Sentence Summary

Imidacloprid (DrugBank ID: DB11421) is a neonicotinoid insecticide with no approved human therapeutic indication and no marketing authorisation in Denmark. The TxGNN model predicts potential efficacy for **Cauda Equina Syndrome**, but this prediction is currently supported by **zero clinical trials** and **zero publications** — it rests entirely on knowledge-graph topology rather than any pharmacological or clinical evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | None — Imidacloprid is an agricultural/veterinary insecticide; it has no approved human therapeutic indication |
| Predicted New Indication | Cauda Equina Syndrome |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Denmark Market Status | Not Marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for Imidacloprid in humans is not available (**[Data Gap]**). What is known is that Imidacloprid acts as a neonicotinoid insecticide by selectively binding insect nicotinic acetylcholine receptors (nAChR). Its affinity for mammalian nAChR is very low — this is precisely the pharmacological basis for its comparatively low toxicity to humans and other mammals, and the reason it is used as a pesticide rather than a drug.

Cauda equina syndrome is an acute neurosurgical emergency caused by compression of the lumbosacral nerve roots, typically requiring urgent surgical decompression. There is no established or plausible pathophysiological link between an insect-selective nAChR-acting insecticide and this condition. The very high TxGNN score (0.9999) most likely reflects topological similarity between graph nodes in the knowledge graph rather than genuine biological plausibility.

**In summary: the mechanistic case for this prediction is weak to absent.** This should be treated as a hypothesis-generating signal only, not as evidence of therapeutic potential, and it does not currently meet the threshold for further pharmacological or clinical investigation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

*(Query log confirms 0 results from ClinicalTrials.gov and ICTRP for "Imidacloprid" + "cauda equina syndrome", searched on two separate occasions.)*

---

## Literature Evidence

Currently no related literature available.

*(Query log confirms 0 results from PubMed for "Imidacloprid" + "cauda equina syndrome".)*

---

## Denmark Market Information

Imidacloprid holds **no marketing authorisation** in Denmark (Laegemiddelstyrelsen) as a human medicinal product. Market status is recorded as **Not Marketed**, with 0 total licenses on file. No product, dosage form, or approved indication data exists for this compound in the Danish register.

---

## Safety Considerations

No human safety data are currently available for this compound:

- **Key Warnings**: Not available (data gap)
- **Contraindications**: Not available (data gap)
- **Drug Interactions**: No interaction data found in DDI database query (query status: not found)

Because Imidacloprid has no approved Summary of Product Characteristics (SmPC) as a human medicinal product in Denmark, no authoritative human safety reference exists. This is flagged as a **Blocking** data gap (DG001) — it prevents this candidate from proceeding to even a preliminary (S1) safety evaluation.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The predicted indication (cauda equina syndrome) has **no clinical trial or literature support whatsoever** (Evidence Level L5 — model prediction only).
- The proposed mechanistic link is not biologically plausible: Imidacloprid's therapeutic rationale as an insecticide depends on selectivity for insect nAChR over mammalian nAChR, which argues *against* relevant human pharmacological activity rather than for it.
- Imidacloprid has no approved human indication anywhere and no marketing authorisation in Denmark (0 licenses), so there is no existing clinical use pattern to build a repurposing case on.
- Human safety data are entirely absent, which is a **Blocking** gap — this candidate cannot proceed to even a preliminary safety review (S1) without it.

**To proceed, the following is needed:**
- Confirmed mechanism of action (MOA) data in human/mammalian systems (currently a High-severity data gap, DG002)
- Human toxicology/safety data sufficient to support an initial safety evaluation (currently a Blocking gap, DG001)
- Independent verification of the disease-node mapping quality (e.g., confirm this is not a knowledge-graph artifact or false-positive signal) before any further investment
- At minimum, preclinical or mechanistic studies establishing biological plausibility before considering any clinical evidence-generation activity

**Note:** Given the complete absence of supporting evidence, the implausible mechanistic rationale, and the drug's status as a non-therapeutic insecticide with no regulatory presence in Denmark, this candidate is not recommended for further development at this time. This assessment is for research reference only and does not constitute medical advice.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

