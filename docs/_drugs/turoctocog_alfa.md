---
layout: default
title: Turoctocog Alfa
parent: 僅模型預測 (L5)
nav_order: 457
evidence_level: L5
indication_count: 10
---

# Turoctocog Alfa
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

# TUROCTOCOG ALFA: From Haemophilia A to Primary Release Disorder of Platelets

## One-Sentence Summary

Turoctocog alfa is a recombinant Factor VIII (FVIII) replacement therapy; the evidence pack's own rationale text confirms its established use is Haemophilia A (congenital FVIII deficiency), though no structured original-indication or Danish licence data is on file.
The TxGNN model predicts possible relevance to **Primary Release Disorder of Platelets** (score **99.99%**), but this is a pure knowledge-graph similarity signal — **zero clinical trials and zero publications** support it, and the pack's own mechanistic assessment states there is **no known pharmacological basis** for the link.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Haemophilia A (congenital Factor VIII deficiency) — per drug-class/rationale text; not present in structured licence data |
| Predicted New Indication | Primary Release Disorder of Platelets |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 (model prediction only — no clinical trials or literature identified) |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, turoctocog alfa is a recombinant human Factor VIII replacement therapy; per the evidence pack's own repurposing rationale, its established role is in Haemophilia A, where FVIII acts as a cofactor in the intrinsic coagulation cascade (the tenase complex, together with Factor IXa) to support thrombin generation.

Primary Release Disorder of Platelets, by contrast, is a defect in platelet granule (dense/alpha granule) content release that impairs secondary platelet aggregation — a distinct haemostatic mechanism from the coagulation-cascade role of FVIII. The evidence pack's own mechanistic assessment states explicitly that there is no known pharmacological basis supporting FVIII supplementation to improve platelet granule release function.

This prediction should therefore be read as a pure knowledge-graph similarity signal — likely driven by shared proximity to a general "bleeding disorder"/"haemostasis" node — rather than a mechanistically grounded hypothesis. The same caveat applies to three of the other four predicted indications in this pack (pseudo-von Willebrand disease, Glanzmann thrombasthenia, Scott syndrome), each of which the pack's rationale text also flags as mechanistically weak or indirect. The exception is *acquired coagulation factor deficiency* (rank 9/10), where a direct mechanistic link is plausible **if** the diagnosis specifically covers acquired FVIII deficiency (e.g., acquired haemophilia A) — this remains unconfirmed in the current data.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Denmark Market Information

This product is not currently marketed in Denmark (Laegemiddelstyrelsen). No marketing authorisations are recorded in the evidence pack (total_licenses = 0).

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All predicted indications carry Evidence Level L5 (model prediction only), with no clinical trials or literature identified for any of them, and the pack's own analysis flags weak-to-absent mechanistic plausibility for most candidates. Combined with the drug not being marketed in Denmark and missing SmPC/MOA data, there is currently no basis to advance beyond hypothesis generation.

**To proceed, the following is needed:**
- Danish/EU SmPC warnings and contraindications (blocking data gap — DG001)
- Confirmed mechanism of action documentation (DG002)
- Pharmacological/preclinical validation of any FVIII–platelet-disorder mechanistic link before clinical hypothesis testing
- Clarification of whether "acquired coagulation factor deficiency" specifically includes acquired FVIII deficiency/inhibitors, which would strengthen that candidate's rationale
- A repeat drug interaction (DDI) query, as the initial query returned no results
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

