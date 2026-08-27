---
layout: default
title: Idursulfase
parent: 僅模型預測 (L5)
nav_order: 224
evidence_level: L5
indication_count: 10
---

# Idursulfase
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

Using no additional tools — this is a direct content-generation task governed entirely by the prompt's own instructions (extract fields from the given Evidence Pack JSON and render the fixed report sections). I'll produce the report now, being careful to only state what the JSON actually supports and to flag where fields are genuinely empty rather than inventing values.

A few notes on how I handled gaps in this particular pack, before the report:
- `drug.original_indications` is empty and `original_moa` is `"[Data Gap]"`, so there's no formally-sourced "original indication" field. However, the `repurposing_rationale` text for several candidates explicitly describes Idursulfase as an iduronate‑2‑sulfatase enzyme-replacement therapy for lysosomal storage disease, and twice names Hunter syndrome (MPS II) by name — I used that text (it's part of the Evidence Pack, not outside knowledge) rather than leaving the title/overview blank.
- All 10 `predicted_indications` entries collapse to 5 unique diseases (each duplicated once), all L5/Hold, all with rationale text arguing *against* a real mechanistic link. I reported the top-ranked candidate per the template and flagged this pattern rather than presenting it as if it were strong evidence.
- Cytotoxicity section omitted — Idursulfase is an enzyme-replacement biologic, not antineoplastic.

---

# Idursulfase: From Lysosomal Storage Disease (Enzyme Replacement Therapy) to Ptosis-Strabismus-Ectopic Pupils Syndrome

## One-Sentence Summary

Idursulfase is a recombinant iduronate-2-sulfatase enzyme replacement therapy used in lysosomal storage disorders such as Hunter syndrome (Mucopolysaccharidosis II). The TxGNN model predicts a possible link to **Ptosis-Strabismus-Ectopic Pupils Syndrome**, a rare congenital cranial dysinnervation disorder, but this is currently supported by **0 clinical trials** and **0 publications** — and the evidence pack's own mechanistic analysis argues against a genuine biological connection.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not formally on file (no Danish licence text available); described in supporting rationale as lysosomal storage disease / enzyme replacement therapy (Hunter syndrome, MPS II) |
| Predicted New Indication | Ptosis-Strabismus-Ectopic Pupils Syndrome |
| TxGNN Prediction Score | 97.89% |
| Evidence Level | L5 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available as a structured field for this drug (marked as a data gap). Based on the supporting rationale text in this evidence pack, Idursulfase acts as an enzyme replacement therapy that breaks down accumulated glycosaminoglycans (GAGs — heparan sulfate and dermatan sulfate) that build up in lysosomal storage disorders such as Hunter syndrome.

The predicted indication, Ptosis-Strabismus-Ectopic Pupils Syndrome, belongs to a different disease family entirely: congenital cranial dysinnervation disorders (CCDDs), which arise from abnormal embryonic development of the ocular motor nerve nuclei — a neurodevelopmental, not metabolic, mechanism. There is no known GAG accumulation or lysosomal enzyme deficiency involved in its pathogenesis.

Critically, the evidence pack's own mechanistic assessment concludes that this is **not** a mechanism-level connection. It attributes the high TxGNN score to phenotypic node proximity within the knowledge graph — shared surface-level features such as "ptosis" and "strabismus" that also appear as secondary ocular manifestations of other MPS-related conditions (e.g., corneal clouding) — rather than any causal pathway. This pattern repeats across all five unique candidates in this pack (ranks 1–10, each disease duplicated once): every one carries a similarly high score (97.6%–97.9%) paired with a rationale explicitly stating the mechanistic link is weak, indirect, or absent (e.g., congenital Horner syndrome from sympathetic nerve pathway injury; CCDD-spectrum muscle fibrosis; developmental lacrimal punctum absence). This consistent self-flagging suggests a knowledge-graph topology artifact (dense clustering of ocular/ophthalmologic phenotype nodes) rather than a set of independently plausible repurposing hypotheses.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Denmark Market Information

Idursulfase currently has **no marketing authorisation registered** in Denmark (market status: not marketed; 0 authorisations on file). No Laegemiddelstyrelsen national licence or EMA centralised authorisation data is present in this evidence pack.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information. No key warnings, contraindications, or drug–drug interaction data are currently on file for this drug (DDI query returned no results).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence level is L5 — a model prediction with zero supporting clinical trials or publications — and the pack's own mechanistic review finds no credible biological pathway linking iduronate-2-sulfatase enzyme replacement to congenital cranial dysinnervation/ptosis-strabismus syndromes. Combined with a Blocking data gap on Danish labeling safety data, this candidate cannot advance past initial screening.

**To proceed, the following is needed:**
- Danish SmPC / product label data (warnings, contraindications) — currently a **Blocking** data gap (DG001) that prevents any S1 safety review
- Verified mechanism of action documentation sourced directly from DrugBank or a regulatory filing (DG002, High severity) rather than inferred from rationale text
- Independent (non-KG-topology) evidence of biological plausibility for a CCDD-family/ophthalmologic phenotype link, e.g. genetic or pathway-level analysis
- At least preliminary clinical or case-report evidence before this candidate can move beyond L5
- Reconciliation of the duplicate candidate entries (5 unique diseases listed twice each) to confirm this isn't a data-pipeline artifact before further triage
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

