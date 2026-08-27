---
layout: default
title: Imlifidase
parent: 僅模型預測 (L5)
nav_order: 229
evidence_level: L5
indication_count: 10
---

# Imlifidase
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

Using the drug-repurposing evaluation report template supplied in the prompt to produce the Imlifidase report below.

# Imlifidase: From Transplant Desensitisation (Unconfirmed) to Diabetic Cataract

## One-Sentence Summary

> Imlifidase (DrugBank DB15258) has no confirmed original indication in the current evidence pack — background knowledge suggests use as a pre-transplant IgG-degrading desensitisation agent, but this is **not sourced from this dataset** and requires manual verification.
> The TxGNN model predicts potential relevance to **Diabetic Cataract**, but this is supported by **0 clinical trials** and **0 publications**, and the model's own rationale flags the result as possibly a knowledge-graph clustering artefact rather than a genuine pharmacological signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not established in this evidence pack — `original_indications` is empty and `original_moa` is flagged as a data gap |
| Predicted New Indication | Diabetic Cataract |
| TxGNN Prediction Score | 98.75% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for Imlifidase in this evidence pack (`original_moa` = data gap), and no original indication is recorded. Background pharmacological knowledge — **not sourced from this dataset and requiring independent verification** — describes Imlifidase as an IgG-degrading cysteine protease used for antibody desensitisation prior to organ transplantation in highly sensitised patients. This background is included here only because the model's own repurposing rationale surfaces it; it should be confirmed against DrugBank/EMA/SmPC sources before being relied upon.

Critically, the model-generated rationale for this prediction is itself skeptical: it states that diabetic cataract pathology is driven by lens protein glycation, sorbitol-pathway accumulation, and oxidative stress — mechanisms with **no known relationship** to IgG cleavage or complement-mediated immune pathways. The rationale explicitly notes that the high TxGNN score may reflect a **clustering artefact** in the knowledge graph (disease nodes for various cataract subtypes embedding close together) rather than a true pharmacological signal.

This is reinforced by the structure of the ranked candidate list: 8 of the top 10 predictions are cataract subtypes/variants (diabetic, craniostenosis, mature, tetanic, immature, type-2-diabetes-associated) clustered at nearly identical scores (~98.7–98.75%), including exact duplicate entries. This pattern is consistent with an embedding-space artefact affecting a whole disease cluster, rather than a specific, differentiated biological hypothesis for Imlifidase. Given the absence of any mechanistic, preclinical, or clinical support, this prediction should be treated as exploratory only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Denmark Market Information

Imlifidase currently holds **no marketing authorisation in Denmark** (`market_status`: Not marketed; 0 registered licenses). No product, dosage form, or approved-indication data is available from Laegemiddelstyrelsen or EMA centralised records in this evidence pack.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

*(Note: no drug–drug interaction data was found; key warnings and contraindications are currently unavailable and are flagged as a blocking data gap — see Next Steps.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The prediction has no clinical trial or literature support (Evidence Level L5), and the model's own mechanistic rationale casts doubt on biological plausibility, suggesting a possible graph-embedding artefact affecting an entire cataract-subtype cluster rather than a specific, credible hypothesis.
- Original indication and mechanism of action data are both missing from this evidence pack, and a **Blocking**-severity data gap (missing TFDA/local label warnings and contraindications) prevents even a preliminary (S1) safety assessment.

**To proceed, the following is needed:**
- Confirmed original indication and mechanism of action for Imlifidase (DG002, High severity — query DrugBank API)
- Local regulatory label warnings, contraindications, and safety data to clear the Blocking gap (DG001 — obtain and parse SmPC/label PDF)
- Independent pharmacological assessment of whether any plausible mechanistic link exists between IgG-degrading protease activity and diabetic cataract pathology
- Resolution of the duplicate/near-identical ranked candidates before this signal is considered distinct from a broader "cataract cluster" artefact
- If pursued further, preclinical or case-level evidence before any clinical investment is considered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

