---
layout: default
title: Rivaroxaban
parent: 僅模型預測 (L5)
nav_order: 384
evidence_level: L5
indication_count: 10
---

# Rivaroxaban
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

Using the drug-repurposing evaluation report template (v5) supplied in the prompt to structure this directly — no additional skill applies to this content-generation task.

# Rivaroxaban: From Anticoagulation (VTE/Atrial Fibrillation) to Rheumatoid Arthritis

## One-Sentence Summary

Rivaroxaban is a direct Factor Xa inhibitor established for venous thromboembolism (VTE) treatment/prevention and stroke prevention in non-valvular atrial fibrillation. The TxGNN model predicts a possible association with **Rheumatoid Arthritis**, but currently **0 clinical trials** and only **3 publications** support this direction, and none of them test rivaroxaban's efficacy in rheumatoid arthritis directly.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Anticoagulation — VTE treatment/prevention, stroke prevention in non-valvular AF (inferred from trial/literature context; no Danish licence text available) |
| Predicted New Indication | Rheumatoid Arthritis |
| TxGNN Prediction Score | 99.57% |
| Evidence Level | L4 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action (MOA) data for rivaroxaban is currently a data gap in DrugBank. Based on established clinical knowledge referenced within the supporting evidence (e.g. the EINSTEIN CYP cohort study, non-valvular AF adherence studies), rivaroxaban is a direct, selective Factor Xa inhibitor used for VTE treatment/prevention and stroke prevention in non-valvular atrial fibrillation.

Rheumatoid arthritis (RA) is a chronic autoimmune inflammatory joint disease. The evidence pack's own mechanistic assessment concludes that rivaroxaban has **no known anti-inflammatory or immunomodulatory mechanism** that would act on RA synovitis pathology. The only plausible indirect link is that RA patients, due to chronic-inflammation-driven hypercoagulability, may have elevated VTE risk and could therefore need anticoagulation for a thrombotic complication — not as treatment for RA itself.

Consistent with this, the supporting literature (a VTE review, a thrombin-generation-assay study in autoimmune disease, and a DOAC adherence cohort) does not test rivaroxaban's efficacy in RA. This prediction should be treated as a hypothesis-generating knowledge-graph signal rather than one with independent mechanistic or clinical support, which is why the evidence level is capped at L4 and the recommendation is Hold.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33141212](https://pubmed.ncbi.nlm.nih.gov/33141212/) | 2020 | Review | JAMA | Review of lower-extremity VTE diagnosis/treatment; DVT incidence 88–112/100,000 person-years, recurrence 20–36% over 10 years — general anticoagulation context, not RA-specific |
| [29621248](https://pubmed.ncbi.nlm.nih.gov/29621248/) | 2018 | Cohort | PloS one | Adherence comparison of rivaroxaban vs. apixaban in non-valvular atrial fibrillation patients — unrelated to RA |
| [34175144](https://pubmed.ncbi.nlm.nih.gov/34175144/) | 2021 | Mechanistic/Lab | La Revue de médecine interne | Thrombin generation assay used to assess hypercoagulability/cardiovascular risk in autoimmune disease (e.g. antiphospholipid syndrome) — a lab coagulation marker study, not an RA efficacy study of rivaroxaban |

---

## Denmark Market Information

No Danish marketing authorisation is recorded in this evidence pack (0 licences on file; market status: Not marketed). This should be independently verified against the Laegemiddelstyrelsen registry before any regulatory conclusion is drawn, since the underlying data source for Danish licence records was not available at the time this pack was generated.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information. (Key warnings, contraindications, and drug-interaction data were not available in this evidence pack; the missing SmPC warning/contraindication data is flagged as a **blocking** data gap that prevents a full S1 safety assessment.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no direct mechanistic rationale linking Factor Xa inhibition to RA pathology, no clinical trials evaluating rivaroxaban in RA, and the supporting literature addresses unrelated anticoagulation contexts rather than RA efficacy. A blocking data gap in SmPC warnings/contraindications also prevents a full safety assessment.

**To proceed, the following is needed:**
- TFDA/SmPC warnings and contraindications (blocking data gap, DG001)
- Detailed mechanism-of-action data (DG002)
- Confirmation of Danish marketing authorisation status directly from Laegemiddelstyrelsen
- Dedicated preclinical or clinical studies testing rivaroxaban's effect on RA disease activity, should further investigation be warranted
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

