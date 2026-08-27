---
layout: default
title: Necitumumab
parent: 僅模型預測 (L5)
nav_order: 306
evidence_level: L5
indication_count: 10
---

# Necitumumab
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

# Necitumumab: From Squamous Non-Small Cell Lung Cancer to Gingival Fibromatosis

## One-Sentence Summary

Necitumumab is an anti-EGFR monoclonal antibody; per the evidence pack's own annotations it is known to be approved internationally for squamous non-small cell lung cancer in combination with chemotherapy (this is not yet verified against a Danish regulatory source). The TxGNN model's top-ranked prediction is **Gingival Fibromatosis**, but there are currently **0 clinical trials** and **0 publications** supporting this direction, and the model's own rationale flags this as a likely noise signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on file in Danish registrations (drug not marketed); internationally indicated for squamous non-small cell lung cancer in combination with chemotherapy per evidence-pack annotation — not independently verified |
| Predicted New Indication | Gingival Fibromatosis |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a High-severity data gap). Based on the annotations included in this evidence pack, Necitumumab is an anti-EGFR monoclonal antibody whose known approved use is squamous non-small cell lung cancer in combination with chemotherapy.

Gingival Fibromatosis is a benign connective-tissue overgrowth condition with no known tissue or mechanistic relationship to lung oncology or EGFR signalling. The evidence pack's own model rationale explicitly describes this as the weakest mechanistic link among the ten ranked candidates, most likely a noise score arising from a distant node in the knowledge graph rather than a genuine biological signal.

For context, two lower-ranked candidates in this evidence pack — lung hilum carcinoma (rank 5, score 99.91%) and pulmonary sulcus neoplasm (rank 9, score 99.90%) — carry a more plausible tissue-level rationale, since both are malignant lung tumours that could theoretically express EGFR. Neither is currently backed by any trial or literature evidence either, but they represent a mechanistically more coherent starting point than the top-ranked Gingival Fibromatosis prediction if this candidate is pursued further.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Denmark Market Information

Necitumumab is not currently marketed in Denmark, and no marketing authorisations are on file.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (anti-EGFR monoclonal antibody, typically administered with cytotoxic chemotherapy) |
| Myelosuppression Risk | Please refer to the Summary of Product Characteristics (SmPC) warnings and precautions |
| Emetogenicity Classification | Please refer to the Summary of Product Characteristics (SmPC) warnings and precautions |
| Monitoring Items | Please refer to the Summary of Product Characteristics (SmPC) warnings and precautions |
| Handling Protection | Please refer to the Summary of Product Characteristics (SmPC) warnings and precautions |

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction has no supporting clinical trial or literature evidence, is rated L5 (model prediction only), and is flagged in the model's own rationale as a likely mechanistic false positive. The drug is also not currently marketed in Denmark, and a blocking data gap (missing SmPC warnings/contraindications) prevents even an initial safety screen.

**To proceed, the following is needed:**
- TFDA/SmPC warnings and contraindications data (blocking gap, required before any S1 safety screening)
- Confirmed mechanism of action (MOA) data from DrugBank or the manufacturer
- Re-evaluation of whether a mechanistically more plausible candidate (e.g., lung hilum carcinoma or pulmonary sulcus neoplasm) should be prioritised instead of the current top-ranked prediction
- Independent verification of the drug's original approved indication against a Danish or EMA regulatory source
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

