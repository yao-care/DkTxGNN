---
layout: default
title: Bisoprolol
parent: 僅模型預測 (L5)
nav_order: 68
evidence_level: L5
indication_count: 10
---

# Bisoprolol
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

# Bisoprolol: From Hypertension to Malignant Renovascular Hypertension

## One-Sentence Summary

Bisoprolol is a cardioselective β1-adrenergic receptor blocker internationally established for the management of hypertension, angina pectoris, and chronic heart failure, though it currently holds no marketing authorisation in Denmark.
The TxGNN model predicts it may be effective for **Malignant Renovascular Hypertension** — a severe, end-organ-threatening form of hypertension driven by renal artery stenosis and RAAS overactivation —
with **0 clinical trials** and **0 directly relevant publications** identified; the prediction rests entirely on mechanistic plausibility.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No marketing authorisation in Denmark; internationally established for hypertension, angina pectoris, and chronic heart failure |
| Predicted New Indication | Malignant Renovascular Hypertension |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L4 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action (MOA) data is not currently available in this evidence pack. Based on Bisoprolol's well-established pharmacology, it is a highly selective β1-adrenergic receptor antagonist. Its key cardiovascular effects include suppression of renin secretion via juxtaglomerular β1 receptors, reduction in heart rate and cardiac output, and consequent lowering of systemic blood pressure.

The core pathophysiology of renovascular hypertension is renal artery stenosis causing sustained, pathological overactivation of the renin-angiotensin-aldosterone system (RAAS). Because Bisoprolol suppresses renin release at the juxtaglomerular apparatus, it directly counteracts this upstream driver, providing a mechanistically coherent rationale for the TxGNN prediction. In the **malignant (accelerated) phase**, acute target-organ damage is present, and combination antihypertensive therapy is standard; Bisoprolol would function as an adjunct to first-line agents such as RAAS inhibitors (ACE inhibitors/ARBs) or calcium channel blockers.

A clinically important nuance reinforces this prediction: patients with **bilateral renal artery stenosis** carry a heightened risk of acute kidney injury when treated with ACE inhibitors or ARBs. In this specific scenario, Bisoprolol — by controlling blood pressure through a RAAS-independent adrenergic mechanism — may represent a safer complementary or alternative agent, adding practical clinical value to the predicted indication. The TxGNN model's high score may also reflect the closely related prediction for **Malignant Hypertensive Renal Disease** (rank 2, identical score), underscoring a consistent signal across both renovascular and renal-damage phenotypes of malignant hypertension.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for Bisoprolol in malignant renovascular hypertension.

> **Note:** A query for Bisoprolol in the related indication "pulmonary hypertension owing to lung disease and/or hypoxia" (rank 7–8) returned 20 PubMed results; however, upon review these publications address general hypoxia biology and are not specific to Bisoprolol treatment. They are therefore not included here. The mechanistic rationale for that indication is weaker, and its recommendation is **Hold** (L5).

---

## Denmark Market Information

Bisoprolol currently holds no marketing authorisation in Denmark and no product-level regulatory data is available.

> **Note:** Bisoprolol is authorised across multiple European countries and has a well-established EMA-assessed safety and efficacy profile under brand names including **Emconcor**, **Bisoprolol Actavis**, and **Bisoprolol Stada**. Absence from the Danish market does not reflect an unfavourable regulatory determination. Importation under individual patient authorisation or cross-border prescribing pathways may be applicable; consultation with the Danish Medicines Agency (Lægemiddelstyrelsen) is recommended.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for full safety information. No warnings, contraindications, or drug interaction data were available in the current evidence pack.

> **Clinical reminder:** As a class effect, β-blockers should generally be used with caution in patients with significant bradycardia, advanced AV block, decompensated heart failure, or obstructive airways disease. The specific context of renal artery stenosis and malignant hypertension warrants careful haemodynamic monitoring.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model assigns a very high prediction score (99.94%) to Bisoprolol for malignant renovascular hypertension, and the β1-adrenergic blockade mechanism — particularly its suppression of juxtaglomerular renin secretion — provides a biologically coherent link to the RAAS-driven pathophysiology. However, no clinical trials or direct disease-specific publications currently support this indication, the drug is not marketed in Denmark, and full safety data for this patient population has not been retrieved.

**To proceed, the following is needed:**

- **Retrieve full MOA data** from DrugBank (data gap DG002) to formally document receptor selectivity, binding kinetics, and downstream pathway effects
- **Obtain and review the SmPC** for key warnings and contraindications (data gap DG001), with specific attention to renal impairment, bilateral renal artery stenosis, and use in malignant hypertension
- **Conduct a targeted systematic literature search** for β-blockers (with a focus on cardioselective agents) in malignant renovascular hypertension and malignant phase hypertension — clinical guidelines and hypertension society position statements should be included
- **Assess regulatory and access pathways** for use in Denmark, including whether any existing European marketing authorisation could support compassionate or off-label use
- **Develop a mechanistic evidence synthesis** (preclinical and pharmacodynamic data) to formally upgrade this from a model-generated signal to a documented research question before any clinical pathway is designed

---

*This report is generated for research purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before use in patient care. Data cut-off: 2026-04-04.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

