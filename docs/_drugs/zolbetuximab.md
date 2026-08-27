---
layout: default
title: Zolbetuximab
parent: 僅模型預測 (L5)
nav_order: 478
evidence_level: L5
indication_count: 10
---

# Zolbetuximab
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

# Zolbetuximab: From Gastric/GEJ Adenocarcinoma (Mechanism-Inferred) to Diabetic Cataract

## One-Sentence Summary

> Zolbetuximab is a cytotoxic monoclonal antibody directed against CLDN18.2, a mechanism associated with its established use in CLDN18.2-positive gastric/gastroesophageal junction cancer — however, this specific original indication is **not recorded** in the current evidence pack (data gap).
> The TxGNN model predicts it may be effective for **Diabetic Cataract**, but this prediction is currently supported by **0 clinical trials** and **0 publications**, and the model's own mechanistic rationale explicitly argues **against** biological plausibility.
> Given the absence of any supporting evidence and a mechanistically implausible drug–disease link, this candidate should be placed on **Hold**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in evidence pack (data gap — see below); mechanism data implies anti-CLDN18.2 oncology use |
| Predicted New Indication | Diabetic Cataract |
| TxGNN Prediction Score | 98.49% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is marked as a data gap (`original_moa: [Data Gap]`) in the drug record itself. However, the model's own repurposing rationale describes Zolbetuximab as a cytotoxic monoclonal antibody targeting Claudin 18.2 (CLDN18.2), acting through antibody-dependent cellular cytotoxicity (ADCC) and complement-dependent cytotoxicity (CDC) to eliminate CLDN18.2-expressing cells — a mechanism consistent with its known oncology use.

**This mechanism does not translate to diabetic cataract.** Diabetic cataract results from chronic hyperglycemia driving polyol-pathway activation, sorbitol accumulation, lens protein oxidation, and osmotic changes in the lens — a metabolic/structural process with no known relationship to CLDN18.2 expression or antibody-mediated cytotoxicity. There is no evidence that lens epithelial cells meaningfully express CLDN18.2, and no evidence that depleting CLDN18.2-positive cells would prevent or reverse lens opacification.

Notably, all ten of the top predicted indications in this evidence pack are cataract-related (diabetic cataract, tetanic cataract, craniostenosis-associated cataract, mature/immature cataract, type 2 diabetes-associated cataract), several appearing as duplicate entries with near-identical scores. This pattern is consistent with a knowledge-graph statistical artifact rather than an independently supported, disease-specific signal, and using a cytotoxic immune-effector antibody in a non-oncologic, non-inflammatory ophthalmic condition also raises an independent safety-plausibility concern (potential immune-mediated ocular tissue injury). The prediction should be treated as low-confidence and not biologically actionable at this time.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Denmark Market Information

No marketing authorisations are currently registered in Denmark for Zolbetuximab (0 licenses on file; market status: Not marketed).

---

## Cytotoxicity

Zolbetuximab is classified here based on its described mechanism (cytotoxic anti-CLDN18.2 monoclonal antibody used in oncology).

| Item | Content |
|------|------|
| Cytotoxicity Classification | Immunotherapy (monoclonal antibody; ADCC/CDC-mediated cytotoxicity against CLDN18.2-expressing cells) |
| Myelosuppression Risk | Please refer to the Summary of Product Characteristics (SmPC) warnings and precautions |
| Emetogenicity Classification | Please refer to the Summary of Product Characteristics (SmPC) warnings and precautions |
| Monitoring Items | Please refer to the Summary of Product Characteristics (SmPC) warnings and precautions |
| Handling Protection | Please refer to the Summary of Product Characteristics (SmPC) warnings and precautions |

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information. Note: TFDA/Danish label warnings and contraindications for this product are currently a **blocking data gap** (DG001) — a formal safety review (S1) cannot proceed until this is resolved.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The predicted indication is supported by zero clinical trials and zero literature (Evidence Level L5, decision stage S0), and the model's own mechanistic rationale argues the drug–disease link is biologically implausible rather than merely under-studied.
- Zolbetuximab is not marketed in Denmark (0 authorisations), and critical safety inputs (label warnings/contraindications, MOA) are marked as blocking/high-severity data gaps in this evidence pack.

**To proceed, the following is needed:**
- TFDA/Danish SmPC warnings and contraindications (currently blocking — DG001)
- Confirmed mechanism of action data from DrugBank or product labeling (DG002)
- Confirmed original approved indication(s) for Zolbetuximab, which are absent from this evidence pack
- Independent biological/preclinical rationale connecting CLDN18.2 biology to lens pathology, if this candidate is to be reconsidered
- Given the current evidence, re-evaluation of whether this candidate should remain in the pipeline at all is recommended before further data collection is invested
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

