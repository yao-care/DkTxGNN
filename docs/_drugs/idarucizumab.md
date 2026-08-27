---
layout: default
title: Idarucizumab
parent: 僅模型預測 (L5)
nav_order: 222
evidence_level: L5
indication_count: 10
---

# Idarucizumab
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

# Idarucizumab: From Dabigatran Anticoagulation Reversal to Hemoglobinopathy

## One-Sentence Summary

Idarucizumab is a monoclonal antibody fragment whose only established use is the emergency reversal of dabigatran's anticoagulant effect. The TxGNN model predicts a possible effect on **Hemoglobinopathy**, but this prediction is currently supported by **0 clinical trials** and **0 publications**, and the model's own rationale flags the mechanistic link as implausible.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Reversal of dabigatran (anticoagulant) activity in emergency/life-threatening bleeding — not present as structured license data in this dataset (Data Gap DG001); stated here from general drug knowledge only |
| Predicted New Indication | Hemoglobinopathy |
| TxGNN Prediction Score | 95.66% |
| Evidence Level | L5 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action documentation for Idarucizumab is not available in this dataset (Data Gap DG002). However, the model's own repurposing rationale describes its only known pharmacological action: Idarucizumab binds free and thrombin-bound dabigatran molecules and neutralizes their anticoagulant activity. This is a highly specific, target-restricted mechanism with no known relationship to hemoglobin structure, globin gene function, or red-cell pathology.

Hemoglobinopathies (e.g., sickle cell disease, other hemoglobin structural variants) arise from globin gene mutations and abnormal hemoglobin polymerization — a disease process that has no described biochemical or pharmacological overlap with dabigatran neutralization. The evidence pack's own analysis characterizes this prediction as a likely **false-positive signal driven by knowledge-graph embedding similarity** rather than a biologically grounded hypothesis.

This assessment is reinforced by a broader pattern in the prediction set: the next four highest-ranked candidates for this drug (rheumatoid arthritis, 16p13.3 deletion syndrome, beta-thalassemia, and pyruvate kinase deficiency) all score similarly high yet share the same absence of any supporting clinical trial or literature evidence, and each is flagged in the rationale as lacking a plausible mechanistic basis. Taken together, this suggests the model's embedding neighborhood for Idarucizumab is poorly informed by real-world evidence at this time, rather than pointing to a genuine repurposing opportunity.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Denmark Market Information

No marketing authorisations are currently recorded for Idarucizumab in this dataset (market status: **Not marketed**, 0 licenses on file). Formal Summary of Product Characteristics (SmPC) data has not been retrieved for this candidate (Data Gap DG001).

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication (hemoglobinopathy) has no supporting clinical trials or literature, and the model's own mechanistic rationale finds no plausible biological pathway connecting dabigatran-reversal activity to hemoglobinopathy pathology — this is most likely a knowledge-graph artifact rather than a genuine repurposing signal. In addition, safety documentation (warnings, contraindications, drug interactions) is a blocking data gap (DG001), which independently precludes any safety pre-assessment.

**To proceed, the following is needed:**
- Retrieval of the approved SmPC / product label (warnings, contraindications, DDI) to close the blocking data gap (DG001)
- Confirmed mechanism-of-action documentation from DrugBank or equivalent source (DG002)
- Independent biological or preclinical evidence linking Idarucizumab (or its Fab-fragment antibody class) to red-cell/hemoglobin pathology before any further evaluation is warranted
- Re-review of the TxGNN prediction set for this drug, given that all top-ranked candidates share the zero-evidence, low-plausibility pattern noted above
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

