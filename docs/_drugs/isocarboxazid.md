---
layout: default
title: Isocarboxazid
parent: 僅模型預測 (L5)
nav_order: 245
evidence_level: L5
indication_count: 10
---

# Isocarboxazid
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

# Isocarboxazid: From Depression to Benign Paroxysmal Torticollis of Infancy

## One-Sentence Summary

Isocarboxazid is an irreversible non-selective monoamine oxidase inhibitor (MAOI) historically used to treat depression (per cited literature; it is currently not marketed in Denmark).
The TxGNN model's top-ranked prediction is **Benign Paroxysmal Torticollis of Infancy**, but this evidence pack contains **no clinical trials and no literature** supporting that specific link, and the pack's own mechanistic assessment flags it as a likely **false positive** driven by graph-embedding similarity rather than pharmacology.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in Danish regulatory data (drug not marketed in Denmark); literature in this pack indicates historical use for depression, incl. treatment-resistant/atypical depression (PMID 3372704) |
| Predicted New Indication | Benign Paroxysmal Torticollis of Infancy |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, no structured mechanism-of-action field is available for isocarboxazid (`original_moa` is a data gap). However, this evidence pack's own repurposing rationale texts describe isocarboxazid as an irreversible, non-selective MAO-A/B inhibitor that raises synaptic concentrations of serotonin (5-HT), norepinephrine (NE), and dopamine (DA) — the classical MAOI mechanism.

For the top-ranked prediction, **Benign Paroxysmal Torticollis of Infancy**, the pack's own assessment states there is no identifiable mechanistic link: this condition is thought to relate to vestibular/migraine-associated pathophysiology, which has no known connection to monoamine oxidase inhibition. The evidence pack explicitly characterizes this high TxGNN score as a likely graph-embedding artifact (false positive), and it is supported by zero clinical trials and zero publications.

By contrast, the same evidence pack contains four other distinct candidate indications for isocarboxazid — agoraphobia, obsessive-compulsive disorder, neurotic disorder, and phobic disorder — all psychiatric conditions mechanistically consistent with MAOI pharmacology. Of these, **neurotic disorder** and **phobic disorder** reach the highest evidence level in this pack (L3), supported by historical controlled/cohort studies specifically involving isocarboxazid (e.g., PMID 2404536, PMID 3372704), reflecting MAOIs' documented historical role in atypical depression with phobic anxiety (Klein/Fink classification). These are not the subject of this report's headline prediction but represent more pharmacologically plausible leads within the same dataset.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Denmark Market Information

Isocarboxazid currently holds no marketing authorisation in Denmark (market status: **Not marketed**; 0 authorisations recorded in the Laegemiddelstyrelsen dataset used for this pack).

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information. Key warnings, contraindications, and drug-interaction data are not available in this evidence pack (DDI query returned no results), and this is flagged as a **blocking data gap** for safety evaluation (see Conclusion).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top-ranked TxGNN prediction (Benign Paroxysmal Torticollis of Infancy) has no supporting clinical trials, no literature, and is explicitly flagged within this evidence pack as a probable false positive with no plausible mechanistic link (Evidence Level L5, decision stage S0).
- A blocking data gap exists for Danish SmPC warnings/contraindications, which prevents any safety pre-assessment regardless of indication.

**To proceed, the following is needed:**
- Danish SmPC / Laegemiddelstyrelsen warning and contraindication data (currently blocking)
- Confirmed mechanism-of-action documentation for isocarboxazid
- If pursuing repurposing further, consider re-scoping the evaluation toward the pack's higher-evidence candidates (**phobic disorder** and **neurotic disorder**, both L3 / "Research Question" stage) rather than the top raw TxGNN score
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

