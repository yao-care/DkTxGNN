---
layout: default
title: Letermovir
parent: 僅模型預測 (L5)
nav_order: 261
evidence_level: L5
indication_count: 10
---

# Letermovir
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

# Letermovir: From CMV Infection Prevention to Vulvovaginal Candidiasis

## One-Sentence Summary

Letermovir is a CMV (cytomegalovirus) terminase inhibitor used to prevent CMV reactivation in allogeneic haematopoietic stem cell transplant (HSCT) recipients. The TxGNN model predicts it may be effective for **Vulvovaginal Candidiasis**, but this prediction is currently supported by **0 clinical trials** and **0 publications**, and the drug's own mechanism of action has no known antifungal activity.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | CMV infection prophylaxis in transplant recipients (inferred from source evidence in this pack; not formally registered — see Data Gaps below) |
| Predicted New Indication | Vulvovaginal Candidiasis |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for Letermovir is not available in the formal drug record (`original_moa: [Data Gap]`). However, source evidence within this pack (clinical trial descriptions) indicates Letermovir works by inhibiting the CMV DNA terminase complex (pUL56/pUL89/pUL51), a mechanism specific to human betaherpesvirus (CMV) replication. It is used clinically to prevent CMV reactivation after allogeneic stem cell transplantation.

There is no known pharmacological pathway connecting CMV terminase inhibition to antifungal activity — Letermovir does not act on ergosterol synthesis, fungal cell wall β-glucan, or fungal nucleic acid metabolism, which are the standard targets of antifungal drugs. The predicted link to Vulvovaginal Candidiasis (caused by *Candida* species) therefore has no plausible mechanistic basis.

TxGNN's high prediction score most likely reflects a **knowledge-graph co-occurrence artifact**: Letermovir is closely linked in the graph to "post-transplant infection prevention" concepts, which also connect to fungal infection nodes in immunocompromised patients, without representing a true pharmacological relationship. This pattern also appears across several other top TxGNN predictions for this drug in the same evidence pack (e.g., *fungal infectious disease*, *tinea nigra*), and two lower-ranked predictions (*malignant catarrhal fever*, *infectious bovine rhinotracheitis*) are veterinary diseases entirely outside human indication scope — reinforcing that this cluster of predictions likely reflects graph proximity bias rather than genuine repurposing signal.

## Clinical Trial Evidence

Currently no related clinical trials registered.

*(Note: 3 clinical trials were found under the broader, related TxGNN prediction "fungal infectious disease," but all were graded "C" — none study Letermovir for treating a fungal infection; they concern CMV prophylaxis in lung/heart transplant recipients and CMV reactivation in CAR-T patients.)*

## Literature Evidence

Currently no related literature available.

## Denmark Market Information

Letermovir is not currently marketed in Denmark. No marketing authorisations (national or centralised/EMA) are on record in this evidence pack.

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

**Data Gap:** Detailed product label warnings, contraindications, and drug interaction data were not available at the time of this evaluation (severity: Blocking) — this must be resolved before any safety assessment can proceed.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication has no clinical trial or literature support, no plausible mechanistic link to the drug's known antiviral activity, and the drug is not currently marketed in Denmark. This corresponds to the lowest evidence tier (L5 — model prediction only).

**To proceed, the following is needed:**
- Confirmed mechanism-of-action data for Letermovir (currently a data gap)
- Official product label warnings/contraindications (currently a data gap; blocking)
- Any preclinical or in-vitro evidence of antifungal activity, if it exists, to establish biological plausibility before further evaluation
- Re-screening once new clinical trial or literature evidence becomes available for this specific indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

