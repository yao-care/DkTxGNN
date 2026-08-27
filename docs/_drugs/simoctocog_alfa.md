---
layout: default
title: Simoctocog Alfa
parent: 僅模型預測 (L5)
nav_order: 400
evidence_level: L5
indication_count: 10
---

# Simoctocog Alfa
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

# Simoctocog Alfa: From Haemophilia A to Pseudo-von Willebrand Disease

## One-Sentence Summary

Simoctocog alfa is a recombinant human Factor VIII (rFVIII) product used to replace FVIII deficiency in **haemophilia A**. The TxGNN model's top-ranked prediction is **pseudo-von Willebrand disease**, but this is currently supported by **0 clinical trials** and **0 publications**, and the accompanying mechanistic rationale argues the association is likely a knowledge-graph artefact rather than a genuine pharmacological signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Haemophilia A (FVIII replacement therapy) — noted in the mechanistic rationale text; not separately confirmed in structured regulatory data |
| Predicted New Indication | Pseudo-von Willebrand Disease |
| TxGNN Prediction Score | 99.997% |
| Evidence Level | L5 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for simoctocog alfa is not available in this evidence pack (flagged as a High-severity data gap). Based on the information that is available, simoctocog alfa is a recombinant FVIII concentrate whose established efficacy is in replacing deficient or absent Factor VIII in haemophilia A.

The predicted indication, pseudo-von Willebrand disease, has a fundamentally different pathophysiology: it is caused by a gain-of-function mutation in the platelet *GP1BA* gene, leading to abnormally increased affinity of the platelet GPIb receptor for von Willebrand factor. This is a platelet-receptor disorder, not a coagulation-factor deficiency. Supplementing FVIII does not correct excessive GPIb–vWF binding and, per the supplied rationale, may not address the underlying pathology at all.

The model's very high confidence score most likely reflects proximity in the knowledge graph between "coagulation/bleeding disorder" nodes rather than a true mechanistic relationship. Among the ten predictions in this pack, **acquired coagulation factor deficiency** (rank 9/10) has a comparatively more plausible link — it may encompass acquired haemophilia A, where high-dose FVIII concentrates have off-label precedent — but even this is flagged only as a "Research Question," not a supported hypothesis, given the complete absence of trial or literature evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Denmark Market Information

Simoctocog alfa currently has no registered marketing authorisations in Denmark (market status: **Not marketed**; 0 licenses on file). No product/dosage-form data is available for this evidence pack.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (pseudo-von Willebrand disease) has no clinical trial or literature support and a mechanistic rationale that argues against biological plausibility — FVIII replacement does not address the platelet-receptor defect underlying this disease. This is an L5, model-only signal with no corroborating evidence.

**To proceed, the following is needed:**
- Confirmed original indication and detailed MOA data for simoctocog alfa (currently data gaps)
- Danish/EU SmPC — including key warnings, contraindications, and drug interaction data (currently unavailable)
- Targeted literature search specifically on FVIII use in acquired coagulation factor deficiency / acquired haemophilia A (rank 9–10), the only candidate with partial mechanistic plausibility, before any further evaluation
- TFDA/Danish regulatory documentation on registration status, since 0 marketing authorisations are currently on file
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

