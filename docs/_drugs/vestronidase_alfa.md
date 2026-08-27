---
layout: default
title: Vestronidase Alfa
parent: 僅模型預測 (L5)
nav_order: 469
evidence_level: L5
indication_count: 10
---

# Vestronidase Alfa
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

# Vestronidase Alfa: From Mucopolysaccharidosis VII to Scheie Syndrome

## One-Sentence Summary

> Vestronidase alfa is a recombinant human beta-glucuronidase enzyme replacement therapy, originally developed for **Mucopolysaccharidosis type VII (MPS VII, Sly syndrome)**.
> The TxGNN model's top-ranked prediction suggests possible efficacy in **Scheie syndrome**,
> but currently **no clinical trials and no published literature** support this specific indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Mucopolysaccharidosis type VII (MPS VII, Sly syndrome) — per literature evidence (approved in US/EU); not registered in Denmark in this evidence pack |
| Predicted New Indication | Scheie syndrome |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L5 |
| Denmark Market Status | Not Marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (data gap). Based on known information, vestronidase alfa is a recombinant human beta-glucuronidase (GUS) enzyme replacement therapy; its efficacy in Mucopolysaccharidosis VII — caused by GUS deficiency — is well established per the literature evidence in this pack.

However, Scheie syndrome is the attenuated form of Mucopolysaccharidosis type I (MPS I), which is caused by deficiency of a **different** enzyme, alpha-L-iduronidase, not beta-glucuronidase. This is an important mechanistic mismatch: unlike MPS VII, vestronidase alfa does not target the enzyme deficient in MPS I. Consistent with this, no supporting clinical trials or literature were found for this specific drug-disease pair. The evaluator's rationale for other ontology-adjacent predictions in this batch (e.g., "lysosomal storage disease with skeletal involvement") explicitly flags that TxGNN may be surfacing broad mucopolysaccharidosis-family ontology overlap with the drug's existing MPS VII indication, rather than a genuinely novel signal — the same caution likely applies here.

Notably, other candidates in this same evidence batch have materially stronger support: **Hurler syndrome** (also MPS I, but linked to an active prenatal enzyme-replacement trial, NCT04532047) and **Sanfilippo syndrome** (MPS III, supported by 4 literature citations, though these describe vestronidase alfa's MPS VII data rather than direct Sanfilippo studies). Given the top-ranked Scheie syndrome prediction has zero direct evidence, these alternative candidates may warrant separate, more thorough evaluation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Denmark Market Information

Vestronidase alfa is **not marketed** in Denmark — no marketing authorisations (national or centralised/EMA) are recorded in this evidence pack.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top-ranked predicted indication (Scheie syndrome) has no supporting clinical trials or literature, and its underlying enzyme deficiency (alpha-L-iduronidase) does not match vestronidase alfa's target enzyme (beta-glucuronidase), raising concern that this is an ontology-overlap artifact rather than a genuine repurposing signal.

**To proceed, the following is needed:**
- TFDA/Danish SmPC warnings and contraindications (blocking data gap, required for S1 safety screening)
- Mechanism of action (MOA) confirmation via DrugBank (high-priority data gap)
- Targeted literature/trial search specifically for vestronidase alfa in Scheie syndrome (MPS I)
- Consideration of a separate evaluation for Hurler syndrome (active trial NCT04532047) and Sanfilippo syndrome, which show more supporting evidence than the top-ranked candidate
- Confirmation of Denmark market/registration status, given current "Not Marketed" flag
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

