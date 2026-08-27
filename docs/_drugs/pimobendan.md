---
layout: default
title: Pimobendan
parent: 僅模型預測 (L5)
nav_order: 352
evidence_level: L5
indication_count: 10
---

# Pimobendan
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

# Pimobendan: From Canine Congestive Heart Failure to Mixed Mineral Dust Pneumoconiosis

## One-Sentence Summary

Pimobendan is a PDE3 inhibitor / calcium sensitizer known for its positive inotropic and vasodilatory effects in canine congestive heart failure. The TxGNN model's top prediction is **Mixed Mineral Dust Pneumoconiosis**, but this is supported by **0 clinical trials** and **0 publications**, and the prediction score (50%) corresponds to an uninformative baseline value rather than a genuine signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available from Danish registry data (drug not marketed, no approved indication text on file). The evidence pack's mechanistic notes reference canine congestive heart failure as the drug's known use. |
| Predicted New Indication | Mixed Mineral Dust Pneumoconiosis |
| TxGNN Prediction Score | 50% |
| Evidence Level | L5 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for pimobendan is flagged as a data gap in this evidence pack (severity: High). The only mechanistic context available comes from the repurposing rationale notes, which describe pimobendan as a PDE3 inhibitor/calcium sensitizer used clinically for its positive inotropic and vasodilatory effects.

Importantly, the evidence pack's own assessment states this prediction is **not** mechanistically supported: there is no known relationship between pimobendan's cardiovascular pharmacology and the fibrotic/inflammatory processes underlying mixed mineral dust pneumoconiosis. A TxGNN score of 0.5 corresponds to an uninformative default value rather than a meaningful signal — the model is effectively expressing no preference. The same pattern holds across all ten ranked predictions for this drug (all scored 0.5, all evidence level L5, all recommended Hold), several of which are rare genetic syndromes or immune-mediated conditions with no plausible pharmacological link to pimobendan.

Given this, the prediction should be treated as a low-confidence model artifact rather than a credible repurposing hypothesis at this time.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Denmark Market Information

Pimobendan currently holds no marketing authorisation in Denmark (market status: not marketed; 0 authorisations on file), so no product/dosage-form information is available.

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information. Note: TFDA/regulatory warning and contraindication data for this drug are flagged as a **Blocking** data gap (DG001) — this must be resolved before any safety evaluation (S1 stage) can proceed.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- All ten predicted indications carry the same uninformative TxGNN score (0.5), no supporting clinical trials or literature, and evidence level L5. The pack itself notes no mechanistic plausibility for the top-ranked indication. The drug is not marketed in Denmark, and core safety data (warnings/contraindications) are a Blocking data gap.

**To proceed, the following is needed:**
- TFDA/SmPC warnings and contraindications (Blocking gap, DG001)
- Verified mechanism of action data (High-priority gap, DG002)
- Re-run TxGNN prediction with a properly discriminating score to confirm whether the current 0.5 values reflect genuine model uncertainty or a data/mapping issue
- Any preliminary preclinical or mechanistic rationale connecting pimobendan's cardiovascular pharmacology to the predicted indication before further evaluation is warranted
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

