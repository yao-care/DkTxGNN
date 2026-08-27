---
layout: default
title: Lebrikizumab
parent: 僅模型預測 (L5)
nav_order: 257
evidence_level: L5
indication_count: 10
---

# Lebrikizumab
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

# Lebrikizumab: From Atopic Dermatitis to Severe Nonproliferative Diabetic Retinopathy

## One-Sentence Summary

Lebrikizumab is a high-affinity IL-13-targeting monoclonal antibody with an extensive, well-established clinical trial and literature base in atopic dermatitis (29 trials, 20 publications on file for the "dermatitis" candidate). The TxGNN model's top-ranked prediction, however, is **Severe Nonproliferative Diabetic Retinopathy** (score **97.94%**), a candidate for which **zero clinical trials and zero publications** are currently on file — this is a pure algorithmic signal, not a literature- or trial-supported hypothesis.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Atopic Dermatitis *(inferred from extensive Phase 2/3 trial and literature titles in this evidence pack; not formally recorded in the drug-level or Danish regulatory fields — see note below)* |
| Predicted New Indication | Severe Nonproliferative Diabetic Retinopathy |
| TxGNN Prediction Score | 97.94% |
| Evidence Level | L5 (model prediction only — no clinical trials or literature identified) |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

**Note on Original Indication:** The evidence pack's `drug.original_indications` field is empty and no Danish marketing authorisation exists (`taiwan_regulatory.licenses` is empty), so this is not a formally documented fact — it is inferred from the disease context of 29 registered trials and 20 publications associated with the "dermatitis" candidate elsewhere in this pack (see Clinical Trial and Literature Evidence for that candidate under "Related Established-Use Evidence" below).

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (`drug.original_moa` = data gap). Based on literature associated with this drug elsewhere in the evidence pack (PMID 36920778, PMID 37310643), lebrikizumab is a high-affinity IgG4 monoclonal antibody that binds interleukin-13 (IL-13) and prevents formation of the IL-4Rα–IL-13Rα1 heterodimer receptor signaling complex, blocking downstream Th2-driven inflammatory signaling. This mechanism underlies its extensively documented use in atopic dermatitis.

For the top-ranked candidate, **severe nonproliferative diabetic retinopathy**, the `repurposing_rationale.mechanistic_link` field in this evidence pack is marked "pending" — no mechanistic hypothesis linking IL-13 signaling to diabetic retinal microvascular pathology has been documented or retrieved from the literature/trial searches performed (query IDs 3–5, 6–8: all zero results). A second, non-severe form of diabetic retinopathy (rank 5/6, score 96.84%) shows the same pattern, suggesting the model is picking up a directional signal around retinal disease broadly, but this has no external validation in the sources queried.

Because no mechanistic rationale, trial, or publication currently supports this specific drug–disease pairing, this prediction should be treated as an unvalidated hypothesis generated purely by the TxGNN algorithm.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

---

### Related Established-Use Evidence (for context)

Not part of the predicted new-indication evidence, but present in this pack under the "dermatitis" candidate (rank 9/10, score 95.97%) and directly relevant to the drug's real-world profile: **29 clinical trials** (multiple completed Phase 3 RCTs, e.g. NCT04146363, NCT04178967, NCT04250337, NCT05559359) and **20 publications** (e.g. PMID 36920778 — *NEJM*, "Two Phase 3 Trials of Lebrikizumab for Moderate-to-Severe Atopic Dermatitis"; PMID 38186219 — *Allergy*, noting EU approval of lebrikizumab for atopic dermatitis in 2023) document lebrikizumab's efficacy and safety in moderate-to-severe atopic dermatitis. This is included for context only, since it does not evidence the retinopathy prediction under evaluation.

---

## Denmark Market Information

Lebrikizumab is not currently marketed in Denmark, and no marketing authorisations (national Laegemiddelstyrelsen or centralised EMA) are on file in this evidence pack (`total_licenses: 0`).

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information. A structured drug-interaction database search (2026-03-24) returned no interactions on file for lebrikizumab; this does not rule out interactions that have not yet been catalogued.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (severe nonproliferative diabetic retinopathy, 97.94%) has no supporting clinical trials, literature, or documented mechanistic rationale — it meets only L5 (model prediction only). Combined with the drug's unmarketed status in Denmark and missing MOA/safety data, there is currently no basis to advance this candidate beyond hypothesis stage.

**To proceed, the following is needed:**
- Mechanism-of-action data (DrugBank API query) to assess biological plausibility of IL-13 signaling in diabetic retinal microvascular disease (data gap DG002, High severity)
- TFDA/SmPC warnings and contraindications, currently a blocking gap for any S1 safety screening (data gap DG001, Blocking)
- Targeted literature/preclinical search specifically on IL-13 and retinal vasculopathy, beyond the disease-matched queries already run (which returned zero results)
- A Danish regulatory pathway assessment, since the product is not currently marketed locally
- Ongoing monitoring of the "diabetic retinopathy" and "severe nonproliferative diabetic retinopathy" TxGNN signal (both flagged independently) for any emerging trial registrations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

