---
layout: default
title: Lonoctocog Alfa
parent: 僅模型預測 (L5)
nav_order: 268
evidence_level: L5
indication_count: 10
---

# Lonoctocog Alfa
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

# Lonoctocog alfa: From Recombinant Factor VIII Replacement to Pseudo-von Willebrand Disease

## One-Sentence Summary

Lonoctocog alfa (DrugBank DB13998) is a recombinant Factor VIII (FVIII) replacement product; its original approved indication is not recorded in this evidence pack. The TxGNN model predicts it may be effective for **Pseudo-von Willebrand disease**, but currently **no clinical trials** and **no publications** support this direction — it is a model-only prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in this evidence pack (no licence data on file); drug class is recombinant Factor VIII replacement |
| Predicted New Indication | Pseudo-von Willebrand disease |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L5 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a High-severity data gap). Based on the information present in this evidence pack, Lonoctocog alfa is a recombinant Factor VIII (FVIII) replacement product, i.e. it raises circulating FVIII activity — the pharmacological principle underlying its use in FVIII-deficiency coagulopathies.

However, the mechanistic link to the top-ranked predicted indication, pseudo-von Willebrand disease, is explicitly flagged as weak in the evidence pack itself. Pseudo-von Willebrand disease is caused by a gain-of-function mutation in the platelet GPIbα receptor, leading to abnormally high affinity for von Willebrand factor and secondary platelet/VWF clearance — the pathology sits at the platelet receptor level, not at circulating coagulation factor concentration. Supplementing exogenous FVIII does not correct this receptor defect. The evidence pack's own rationale notes the high TxGNN score may simply reflect shared "bleeding disorder" graph co-occurrence rather than a direct pharmacological pathway.

Notably, among the ten predictions returned, rank 9/10 ("acquired coagulation factor deficiency") carries the strongest mechanistic plausibility — Lonoctocog alfa could in principle supplement FVIII lost to inhibitors or consumptive coagulopathy — but this candidate has a lower TxGNN score, an unspecified (non-FVIII-specific) disease grouping, and, like all others, zero supporting trials or literature.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Denmark Market Information

No marketing authorisation is currently on file for Lonoctocog alfa in Denmark (market status: not marketed; 0 authorisations recorded).

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information. (Danish Medicines Agency warning/contraindication text and drug-interaction data are not yet available in this evidence pack — flagged as a Blocking data gap.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- Evidence level is L5 (model prediction only — zero clinical trials, zero publications), and the evidence pack's own mechanistic analysis rates the drug–disease link as weak; the product also has no marketing authorisation in Denmark.

**To proceed, the following is needed:**
- TFDA/SmPC warnings, contraindications and drug interaction data (Blocking gap, DG001)
- Mechanism of action detail from DrugBank (High-priority gap, DG002)
- Preclinical or mechanistic studies addressing whether FVIII replacement has any plausible effect on platelet-receptor disorders (pseudo-von Willebrand disease, Glanzmann thrombasthenia, Scott syndrome, primary platelet release disorder)
- Clarification of the "acquired coagulation factor deficiency" candidate (rank 9/10) — confirm whether it is FVIII-specific, as this candidate has the strongest mechanistic rationale in this set despite its lower score
- Danish marketing authorisation status confirmation, given the product is currently not marketed
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

