---
layout: default
title: Linaclotide
parent: 僅模型預測 (L5)
nav_order: 265
evidence_level: L5
indication_count: 6
---

# Linaclotide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Linaclotide: From IBS-C/Chronic Constipation to Cauda Equina Syndrome

## One-Sentence Summary

Linaclotide is a locally acting gut GC-C agonist used for irritable bowel syndrome with constipation (IBS-C) and chronic idiopathic constipation. The TxGNN model predicts a possible link to **Cauda Equina Syndrome**, but this prediction is currently supported by **0 clinical trials** and **0 publications**, and the evidence pack itself flags it as likely a knowledge-graph artifact rather than a genuine pharmacological signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not formally recorded in this dataset (drug class notes reference IBS-C / chronic idiopathic constipation) |
| Predicted New Indication | Cauda Equina Syndrome |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Linaclotide is a guanylate cyclase-C (GC-C) agonist that acts locally on intestinal epithelial cells to stimulate fluid secretion and bowel motility. Systemic bioavailability is under 0.1%, and the drug does not cross the blood-brain barrier — its pharmacological effect is essentially confined to the gut lumen.

Cauda equina syndrome is a neurosurgical emergency caused by compression of the lumbosacral nerve roots, which can present with bowel and bladder dysfunction, including neurogenic constipation. The superficial overlap is a shared "constipation" symptom node, not a shared disease mechanism.

Based on the mechanistic assessment already included in this evidence pack, the high TxGNN score most likely reflects a knowledge-graph co-occurrence edge between "constipation" and cauda equina syndrome, rather than evidence that linaclotide treats the underlying nerve compression. Even under an optimistic reading, the drug could at most offer symptomatic relief of a secondary bowel symptom — it would not address the causative pathology — and no clinical or mechanistic data currently confirm this in humans.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Denmark Market Information

No marketing authorisations are currently registered for linaclotide in Denmark (market status: not marketed; total licenses on file: 0).

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

> Note: Danish label warnings/contraindications data (TFDA-equivalent source) is flagged as a **Blocking** data gap in this evidence pack (DG001) — this must be resolved before any safety pre-assessment (S1) can proceed.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high, but evidence level is L5 — no clinical trials, no literature, and the pack's own mechanistic review concludes the drug's local, non-systemic mode of action has no plausible pathway to cauda equina syndrome. This looks like a knowledge-graph artifact rather than a real repurposing signal.

**To proceed, the following is needed:**
- Danish/EU-approved SmPC with warnings and contraindications (currently a Blocking gap)
- Confirmed original indication and mechanism of action data for linaclotide
- Any mechanistic, preclinical, or case-level evidence specifically linking GC-C agonism to neurogenic bowel dysfunction in cauda equina syndrome before this candidate is reconsidered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

