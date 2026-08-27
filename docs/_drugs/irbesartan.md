---
layout: default
title: Irbesartan
parent: 僅模型預測 (L5)
nav_order: 244
evidence_level: L5
indication_count: 8
---

# Irbesartan
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

# Irbesartan: From Hypertension to Malignant Hypertensive Renal Disease

## One-Sentence Summary

Irbesartan is an angiotensin II receptor blocker (ARB), a drug class established for the treatment of hypertension. The TxGNN model predicts it may be effective for **Malignant Hypertensive Renal Disease**, but this specific link is currently supported by **0 clinical trials** and **0 publications** — the prediction score is high, yet purely model-derived at this stage.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (established ARB indication; no formal indication text on file for this dataset) |
| Predicted New Indication | Malignant Hypertensive Renal Disease |
| TxGNN Prediction Score | 99.31% |
| Evidence Level | L5 (model prediction only — no clinical trials or literature identified for this disease pairing) |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not currently on file for this dataset (flagged as a High-severity data gap). Based on known pharmacology, irbesartan belongs to the angiotensin II receptor blocker (ARB) class, acting via AT1-receptor blockade to lower blood pressure and provide renal protection — an effect already well established in hypertension and in diabetic nephropathy with hypertension.

Malignant hypertensive renal disease is a renal complication of severe, uncontrolled hypertension. Because ARBs directly target the blood-pressure-lowering mechanism relevant to this condition, there is a plausible mechanistic link between the original indication and the predicted one. However, malignant hypertension typically requires acute intravenous antihypertensive management; an oral ARB such as irbesartan would more plausibly play a role in subsequent maintenance therapy rather than acute-phase treatment.

The TxGNN score (99.31%) most likely reflects a broad "antihypertensive drug → hypertension-related disease" graph connection rather than evidence specific to this malignant/renal presentation. No clinical trials or publications currently support this precise indication pairing, so the mechanistic rationale should be treated as hypothesis-generating rather than confirmatory.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Denmark Market Information

No marketing authorisations are currently registered for irbesartan in this dataset (market status: **Not marketed**, 0 licences on file).

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN prediction score, there is no clinical trial or literature evidence specific to irbesartan in malignant hypertensive renal disease (Evidence Level L5), and the drug currently has no marketing authorisation on file in Denmark. The other candidate indications in this evidence pack (malignant renovascular hypertension; pulmonary hypertension, WHO Groups 3 and 5) were similarly held — the renovascular hypertension link carries a known safety concern (risk of acute renal function decline with ARBs in renal artery stenosis), and the pulmonary hypertension literature returned by the search was unrelated background material on hypoxia biology rather than substantive support.

**To proceed, the following is needed:**
- Official SmPC warnings and contraindications from Lægemiddelstyrelsen/EMA (currently a Blocking data gap — required before any S1 safety review)
- Confirmed detailed mechanism-of-action data from DrugBank (High-priority data gap)
- Disease-specific clinical evidence for ARB use in malignant hypertension / hypertensive renal crisis (e.g., as maintenance therapy following acute control)
- Renal artery imaging/status considerations if the renovascular hypertension indication is pursued, given the known risk of ARB-induced renal function decline in that population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

