---
layout: default
title: Iodixanol
parent: 僅模型預測 (L5)
nav_order: 240
evidence_level: L5
indication_count: 10
---

# Iodixanol
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

# Iodixanol: From Radiographic Contrast Imaging to Osteoarthritis Susceptibility

## One-Sentence Summary

Iodixanol is a nonionic iodinated contrast agent used diagnostically in radiographic and CT imaging, not a disease-treating drug in the conventional sense. The TxGNN model's top-ranked prediction links it to **Osteoarthritis Susceptibility** with a very high score (99.16%), but this specific prediction is currently backed by **zero clinical trials and zero publications** — it is a model-only signal with no mechanistic or clinical corroboration.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Radiographic/CT contrast imaging (diagnostic agent; not a disease-treating indication) |
| Predicted New Indication | Osteoarthritis susceptibility |
| TxGNN Prediction Score | 99.16% |
| Evidence Level | L5 |
| Denmark Market Status | Not Marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for Iodixanol is not available in this evidence pack (data gap, high severity). Based on the information that is available, Iodixanol is a diagnostic iodinated contrast medium — its evidence base consists entirely of imaging and tracer studies, not pharmacological treatment data. There is no known anti-inflammatory, chondroprotective, or disease-modifying mechanism that would explain a therapeutic effect in osteoarthritis.

The top-ranked prediction, "osteoarthritis susceptibility," has no supporting clinical trials or literature at all — it reflects the TxGNN graph-embedding score alone, with no mechanistic or clinical clue behind it. A closely related candidate in the same screen, plain "osteoarthritis," does have seven associated publications, but per the evidence pack's own assessment these describe using iodixanol as a molecular tracer/contrast agent to study cartilage-bone interface solute transport and nanoparticle-based CT arthrography — diagnostic imaging research tools, not treatment studies. The same pattern holds for the other candidates surfaced for this drug (rheumatoid arthritis, hemoglobinopathy, brachyolmia): available literature either concerns contrast-agent desensitization/safety, imaging quality, or a potential safety concern (contrast media affecting red-cell deformability in sickle cell disease), none of it supporting therapeutic repurposing.

Taken together, the mechanistic case for repurposing Iodixanol into osteoarthritis (or any of the other predicted indications) is currently unsubstantiated.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

*(Note: the closely related candidate "osteoarthritis" — distinct from the top-ranked "osteoarthritis susceptibility" — has 7 associated publications, but these are cartilage-imaging/tracer studies rather than therapeutic evidence; see rationale above.)*

## Denmark Market Information

No marketing authorisations are currently registered for Iodixanol in Denmark; the drug's status in this evidence pack is "Not Marketed" with 0 recorded licenses.

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

*(Note: a blocking data gap exists — Danish label warnings/contraindications and DDI data have not yet been retrieved, which prevents even a preliminary safety screen for this candidate.)*

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score for this prediction is high, but it is entirely unsupported — zero clinical trials, zero literature, and no plausible mechanistic link, placing it at the lowest evidence tier (L5, model prediction only). A blocking data gap on label safety information also prevents any safety pre-screen.

**To proceed, the following is needed:**
- Confirmed mechanism of action data for Iodixanol (currently a data gap)
- Approved product label / SmPC warnings and contraindications (blocking data gap)
- Any preclinical or translational study testing a genuine therapeutic (not diagnostic/tracer) effect in osteoarthritis
- Re-evaluation against other TxGNN candidates for this drug, none of which currently show stronger evidence either
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

