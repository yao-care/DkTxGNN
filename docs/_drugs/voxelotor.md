---
layout: default
title: Voxelotor
parent: 僅模型預測 (L5)
nav_order: 475
evidence_level: L5
indication_count: 10
---

# Voxelotor
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

# Voxelotor: From Sickle Cell Disease to Hereditary Thrombocytopenia with Normal Platelets

## One-Sentence Summary

Voxelotor is a hemoglobin oxygen-affinity modulator known for its clinical use in sickle cell disease (this original indication is not confirmed by structured registry data in this pack — see note below — but is described in the accompanying mechanistic rationale). The TxGNN model predicts potential efficacy for **Hereditary Thrombocytopenia with Normal Platelets**, with a very high prediction score (**99.58%**) but currently **zero supporting clinical trials** and **zero publications**. The evidence pack's own analysis flags this prediction as a likely knowledge-graph clustering artifact rather than a genuine pharmacological signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Sickle cell disease (inferred from MOA description in the evidence rationale; not confirmed by structured regulatory data — see Data Gap DG002) |
| Predicted New Indication | Hereditary thrombocytopenia with normal platelets |
| TxGNN Prediction Score | 99.58% |
| Evidence Level | L5 (model prediction only, no clinical trials or literature) |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for voxelotor is formally flagged as a **Data Gap (DG002, High severity)** in this evidence pack — no verified DrugBank/SmPC MOA record was retrieved. However, the rationale text accompanying the TxGNN predictions consistently describes voxelotor as a **hemoglobin oxygen-affinity modulator that inhibits polymerization of sickle hemoglobin (HbS)**, which is the mechanism underlying its known clinical use in sickle cell disease. This description should be treated as background context only, not as verified structured data, until confirmed via a proper DrugBank/regulatory query.

The predicted new indication — hereditary thrombocytopenia with normal platelets — is a rare inherited platelet-function disorder. Its underlying biology involves megakaryocyte development and platelet signaling pathways, which is mechanistically distinct from voxelotor's red-blood-cell-targeted, hemoglobin-polymerization mechanism. The evidence pack's own repurposing rationale explicitly states there is **no direct biological connection** between the two conditions.

Notably, four of the five distinct diseases among the top-10 TxGNN predictions for voxelotor are platelet-related or thrombocytopenia conditions, all scoring within a narrow band (0.9951–0.9958). The evidence pack's authors interpret this as a possible **knowledge-graph embedding cluster effect** rather than a drug-specific signal. A further confound is noted: patients with sickle cell disease often present with coexisting platelet-count abnormalities (e.g., due to splenic dysfunction), which may have caused the model to learn a comorbidity association rather than a true treatment relationship. In the complete absence of clinical trial or literature support, this prediction should be treated as hypothesis-generating only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered (ClinicalTrials.gov and ICTRP searches for voxelotor against this indication both returned zero results).

---

## Literature Evidence

Currently no related literature available (PubMed search for voxelotor against this indication returned zero results).

---

## Denmark Market Information

Voxelotor's Denmark market status is recorded as **Not marketed**, with **0** registered marketing authorisations in the dataset. No product name, dosage form, or approved indication information is therefore available.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information. (Key warnings, contraindications, and drug-drug interaction data are all marked as Data Gaps in this evidence pack; the TFDA/regulatory label information required for a full safety assessment — Data Gap DG001, Blocking severity — has not yet been obtained.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This is an L5, model-prediction-only signal with no supporting clinical trials, no supporting literature, and no confirmed mechanistic link — the evidence pack's own analysis suggests the score may reflect a knowledge-graph clustering artifact among platelet-disorder nodes rather than a genuine drug-disease relationship. Voxelotor is also not marketed in Denmark, and a Blocking-level safety data gap prevents any preliminary safety assessment.

**To proceed, the following is needed:**
- Regulatory label / SmPC safety data (warnings, contraindications, DDI) — currently Blocking Data Gap (DG001)
- Verified mechanism-of-action data from DrugBank — currently High-severity Data Gap (DG002)
- Independent confirmation that the TxGNN score is not an artifact of embedding-space clustering among platelet-disorder nodes
- Preclinical or mechanistic studies specifically evaluating any link between hemoglobin-polymerization modulation and platelet-disorder pathophysiology, before any further clinical evaluation is considered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

