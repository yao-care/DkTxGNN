---
layout: default
title: Ramipril
parent: 僅模型預測 (L5)
nav_order: 364
evidence_level: L5
indication_count: 10
---

# Ramipril
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

# Ramipril: From Hypertension to Pulmonary Hypertension due to Lung Disease and/or Hypoxia

## One-Sentence Summary

Ramipril is an ACE inhibitor publicly known for treating hypertension and related cardiovascular/renal conditions, though this specific Evidence Pack contains no confirmed original-indication or MOA data. The TxGNN model predicts a possible role in **Pulmonary Hypertension due to Lung Disease and/or Hypoxia (WHO Group 3)**, but this is currently supported by **0 clinical trials** and **20 publications that are all unrelated to ramipril or pulmonary hypertension treatment** — the evidence base is essentially absent.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the Danish regulatory record (drug not currently marketed in Denmark); publicly known as an ACE inhibitor for hypertension |
| Predicted New Indication | Pulmonary Hypertension due to Lung Disease and/or Hypoxia (WHO Group 3) |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L5 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for this record is a data gap (`original_moa: [Data Gap]`), and no original indication is registered for Denmark. Based on the drug's known pharmacological class — referenced within this Evidence Pack's own analysis — ramipril is an ACE inhibitor that suppresses the renin-angiotensin-aldosterone system (RAAS), a mechanism with established benefit in hypertension and, per the REIN study literature, in renal protection for chronic kidney/diabetic nephropathy.

For the top-ranked predicted indication, however, the mechanistic rationale supplied with this evidence pack is **cautionary rather than supportive**: WHO Group 3 pulmonary hypertension arises from chronic hypoxia/lung disease, where hypoxic pulmonary vasoconstriction (HPV) is a protective compensatory mechanism. Systemic vasodilators — including ACE inhibitors — may worsen ventilation-perfusion mismatch and aggravate hypoxemia, which is why current clinical guidelines do not recommend this drug class for Group 3 PH.

The 20 attached publications are all general hypoxia-biology papers (neurodegeneration, tumour metabolism, multiple sclerosis, altitude physiology) and **do not address ramipril or pulmonary hypertension treatment**. Combined with the mechanistic concern above, this prediction should be treated as a knowledge-graph association rather than a therapeutically actionable signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40347693](https://pubmed.ncbi.nlm.nih.gov/40347693/) | 2025 | Basic research | Redox Biology | Hypoxia's role in multiple sclerosis pathology; not related to ramipril or PH |
| [40815459](https://pubmed.ncbi.nlm.nih.gov/40815459/) | 2025 | Basic research | Rev Med Inst Mex Seguro Soc | Hypobaric hypoxia and high-altitude acclimatisation; not drug-related |
| [37915135](https://pubmed.ncbi.nlm.nih.gov/37915135/) | 2023 | Basic research | BMB Reports | CMGC kinase regulation by hypoxia in tumours; not related to ramipril or PH |
| [37572528](https://pubmed.ncbi.nlm.nih.gov/37572528/) | 2023 | Basic research | Neurobiology of Aging | Hypoxia link between Alzheimer's disease and cancer; unrelated to ramipril/PH |
| [37328448](https://pubmed.ncbi.nlm.nih.gov/37328448/) | 2023 | Basic research | Advanced Science | Hypoxia tolerance mechanism in gastric cancer glycolysis; unrelated to ramipril/PH |
| [36100192](https://pubmed.ncbi.nlm.nih.gov/36100192/) | 2022 | Basic research | J Control Release | Hypoxia-targeted nanomedicine for tumours; unrelated to ramipril/PH |
| [34618295](https://pubmed.ncbi.nlm.nih.gov/34618295/) | 2022 | Review | Metabolic Brain Disease | Cognitive impairment from hypoxia; unrelated to ramipril/PH |
| [33862277](https://pubmed.ncbi.nlm.nih.gov/33862277/) | 2021 | Review | Ageing Research Reviews | Hypoxia's role in brain aging/neurodegeneration; unrelated to ramipril/PH |
| [34535359](https://pubmed.ncbi.nlm.nih.gov/34535359/) | 2021 | Review | Clinical Oncology | Therapeutic modification of tumour hypoxia (radiotherapy context); unrelated to ramipril/PH |
| [33278780](https://pubmed.ncbi.nlm.nih.gov/33278780/) | 2021 | Basic research | Redox Biology | Glucose metabolism in keloid fibroblasts under hypoxia; unrelated to ramipril/PH |

**Note:** None of the above literature discusses ramipril or its use in pulmonary hypertension. These are general hypoxia-biology papers that surfaced through keyword overlap ("hypoxia") rather than direct evidence for this repurposing hypothesis.

---

## Denmark Market Information

Ramipril has no marketing authorisations recorded for Denmark in this Evidence Pack (0 licenses; market status: Not marketed).

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information. No key warnings, contraindications, or drug-interaction data were found in this Evidence Pack (DDI query status: not found).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication (Group 3 pulmonary hypertension) conflicts with established clinical concern that ACE inhibitors may worsen hypoxemia by blunting protective hypoxic pulmonary vasoconstriction. No clinical trials exist, and all 20 attached publications are unrelated to ramipril or pulmonary hypertension. Evidence level is L5 (model prediction only), and the drug is not currently marketed in Denmark.

**To proceed, the following is needed:**
- SmPC warnings/contraindications from the manufacturer (currently blocking safety assessment — DG001)
- Confirmed mechanism of action and original indication data (DG002)
- A clinical or preclinical rationale specifically evaluating ACE inhibition in Group 3 PH, rather than general hypoxia biology
- Drug interaction (DDI) data, currently unavailable
- If pursued despite the above: a pharmacology review addressing the HPV-blunting concern before any further evaluation stage
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

