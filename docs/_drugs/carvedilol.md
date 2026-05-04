---
layout: default
title: Carvedilol
parent: 僅模型預測 (L5)
nav_order: 95
evidence_level: L5
indication_count: 10
---

# Carvedilol
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

# Carvedilol: From Heart Failure to Malignant Renovascular Hypertension

## One-Sentence Summary

Carvedilol is a non-selective beta-adrenergic blocker with additional alpha-1 blocking activity, established globally for treating heart failure, hypertension, and left ventricular dysfunction following myocardial infarction.
The TxGNN model predicts it may be effective for **Malignant Renovascular Hypertension** with a prediction score of **99.55%**,
however **no clinical trials or directly relevant publications** currently support this specific repurposing direction, placing this candidate at the lowest evidence tier.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Heart failure, hypertension, left ventricular dysfunction post-myocardial infarction (not registered in Denmark) |
| Predicted New Indication | Malignant Renovascular Hypertension |
| TxGNN Prediction Score | 99.55% |
| Evidence Level | L5 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Carvedilol is a third-generation beta-blocker with dual adrenergic blockade: it blocks β1 receptors (reducing heart rate and cardiac output) and α1 receptors (causing peripheral vasodilation and reducing systemic vascular resistance). This combined mechanism makes it more effective at lowering blood pressure than selective beta-blockers alone, and it is also known to possess antioxidant properties capable of scavenging reactive oxygen species.

Malignant renovascular hypertension is typically caused by renal artery stenosis triggering excessive activation of the renin-angiotensin-aldosterone system (RAAS), leading to severely elevated blood pressure with end-organ damage. Carvedilol's blood pressure-lowering mechanism does offer a theoretical rationale for intervention. Additionally, its antioxidant properties may theoretically help mitigate oxidative stress-mediated vascular and renal injury.

However, the mechanistic fit carries meaningful safety concerns. Non-selective beta-blockade can interfere with β1-mediated renin suppression in the ischaemic kidney, potentially worsening renal hypoperfusion in the context of renal artery stenosis. In this specific pathophysiology, RAAS-targeted agents (ACE inhibitors, ARBs) or calcium channel blockers are typically preferred. The TxGNN signal likely reflects the general blood pressure–lowering profile of the drug rather than a disease-specific mechanistic match.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for any of the predicted new indications (malignant renovascular hypertension, malignant hypertensive renal disease, pulmonary hypertension, or Braddock syndrome).

---

## Literature Evidence

No directly relevant publications were identified for the top predicted indication (malignant renovascular hypertension).

> **Note on retrieved literature (pulmonary hypertension with hypoxia, ranks 7–8):** A PubMed search returned 20 publications under the query for "carvedilol + pulmonary hypertension owing to lung disease and/or hypoxia." Upon review, all retrieved articles address hypoxia biology in general contexts (e.g., neurodegeneration, cancer metabolism, tissue repair) and do not specifically investigate carvedilol for pulmonary hypertension. These are considered non-relevant background literature and are excluded from evidence scoring. Representative titles include reviews on hypoxia and brain aging, HIF-1α signalling in tumours, and cognitive impairment under hypoxia — none evaluate carvedilol as a therapeutic agent for this indication. The evidence level for this indication therefore remains L5.

---

## Denmark Market Information

Carvedilol currently holds no marketing authorisations granted by the Danish Medicines Agency (Lægemiddelstyrelsen) and is not an authorised medicinal product on the Danish market.

> Carvedilol is, however, a widely authorised medicine in the EU through centralised EMA procedures and national authorisations in other member states (e.g., Coreg®, Dilatrend®). Access in Denmark for individual patients may be possible via the special import (særlig import) pathway subject to Lægemiddelstyrelsen approval.

---

## Safety Considerations

Detailed warnings, contraindications, and drug interaction data were not available in the current Evidence Pack for the Danish market context.

Please refer to the approved Summary of Product Characteristics (SmPC) — for example, the EMA-authorised product SmPC or equivalent national labelling — for full safety information.

> **Key safety signals known from general pharmacological knowledge (for context only):**
> - Non-selective beta-blockade may exacerbate bronchospasm in patients with asthma or reactive airway disease
> - Use in renal artery stenosis (the underlying cause in renovascular hypertension) carries risk of acute renal deterioration
> - Caution required in patients with decompensated heart failure, severe bradycardia, or heart block
> - Abrupt discontinuation should be avoided due to risk of rebound hypertension or angina

*These notes are based on general pharmacological knowledge and do not substitute for the approved SmPC.*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All predicted indications are rated at evidence Level 5 (TxGNN model prediction only), with no supporting clinical trials and no directly relevant literature. The mechanistic rationale for malignant renovascular hypertension is theoretically present but carries specific safety concerns that have not been evaluated in this context, and the drug is not currently marketed in Denmark.

**To proceed, the following is needed:**

- Retrieve and review the full SmPC (e.g., EMA Dilatrend/Coreg SmPC) to assess contraindications and warnings relevant to malignant renovascular hypertension
- Obtain mechanism-of-action data from DrugBank (DB01136) to strengthen or challenge the mechanistic link
- Conduct a targeted literature search specifically for carvedilol in renovascular or malignant hypertension (not relying on general hypoxia literature)
- Consult a clinical nephrologist or cardiologist to evaluate whether non-selective beta-blockade is appropriate in the setting of renal artery stenosis–driven hypertension
- Consider whether alternative cardiovascular drugs with higher evidence levels for these specific indications should be prioritised ahead of carvedilol in the repurposing pipeline

---

*This report is for research purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before any therapeutic application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

