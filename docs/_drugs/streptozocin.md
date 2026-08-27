---
layout: default
title: Streptozocin
parent: 僅模型預測 (L5)
nav_order: 408
evidence_level: L5
indication_count: 10
---

# Streptozocin
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

# Streptozocin: From Unspecified Original Indication to Relapsing-Remitting Multiple Sclerosis

## One-Sentence Summary

Streptozocin is a nitrosourea-class DNA-alkylating cytotoxic agent; its original approved indication is not recorded in this evidence pack. The TxGNN model predicts potential efficacy for **Relapsing-Remitting Multiple Sclerosis**, with a prediction score of **99.97%**, but this direction is currently supported by **0 clinical trials** and only **1 publication** — and that publication does not actually study streptozocin as a treatment for multiple sclerosis, indicating this top-ranked prediction is very likely a false positive.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (data gap) |
| Predicted New Indication | Relapsing-Remitting Multiple Sclerosis |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| Denmark Market Status | Not Marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for streptozocin is not available in this evidence pack (data gap DG002). Based on the information that is available, streptozocin is a nitrosourea-class DNA-alkylating cytotoxic compound, historically used to selectively damage pancreatic islet beta cells (a property exploited both experimentally, to induce diabetes in animal models, and clinically in oncology).

For the top-ranked prediction — Relapsing-Remitting Multiple Sclerosis — there is no plausible mechanistic link. MS pathophysiology centers on immune-mediated demyelination and remyelination, processes unrelated to islet-cell alkylating cytotoxicity. The single supporting publication (PMID 28162947) does not study streptozocin in MS at all: it investigates **FTY720 (fingolimod)** — the actual approved MS drug — improving erectile dysfunction in **streptozotocin-induced diabetic rats**. Streptozocin appears only as the diabetes-induction tool in the animal model, not as a candidate MS therapy. This pattern is consistent with a text-mining false match rather than a genuine repurposing signal.

For context, other candidates surfaced by the model carry more directly relevant (though not supportive) evidence: streptozocin itself was tested in several historical Phase II trials for small cell lung carcinoma, but was explicitly reported as an "inactive agent" (PMID 229984) and an "ineffective nonmyelosuppressive agent" (PMID 148321). This underscores that the MS prediction lacks even the negative-trial-level evidence available for other candidates, and should not be advanced without independent mechanistic or preclinical validation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28162947](https://pubmed.ncbi.nlm.nih.gov/28162947/) | 2017 | Animal Study | The Journal of Sexual Medicine | Studies FTY720 (fingolimod, the actual approved MS drug) reversing erectile dysfunction in streptozotocin-induced diabetic rats. Streptozocin is used only as the diabetes-induction agent in this model and is not evaluated as a treatment for multiple sclerosis — this citation does not support the predicted indication. |

---

## Denmark Market Information

Streptozocin currently holds no marketing authorisation (national Laegemiddelstyrelsen or centralised EMA) in Denmark; market status is "Not Marketed" with 0 registered licenses.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (nitrosourea alkylating agent) |
| Myelosuppression Risk | Reported in the literature as comparatively low for single-agent use — one historical trial title describes streptozocin as an "ineffective, nonmyelosuppressive agent" (PMID 148321); please confirm against SmPC as formal toxicity data is not in this evidence pack |
| Emetogenicity Classification | Please refer to the Summary of Product Characteristics (SmPC) warnings and precautions |
| Monitoring Items | CBC, renal function, and blood glucose/pancreatic islet function are standard considerations for nitrosourea agents; confirm specific monitoring against SmPC |
| Handling Protection | Cytotoxic drug handling precautions apply, per standard regulations for antineoplastic alkylating agents |

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information. (TFDA/national label warnings, contraindications, and drug-interaction data are all recorded as data gaps in this evidence pack — notably DG001, a **Blocking**-severity gap that prevents this candidate from entering S1 safety pre-screening.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top-ranked prediction (Relapsing-Remitting Multiple Sclerosis) has no plausible mechanistic basis, zero clinical trials, and its single literature citation is unrelated to the predicted indication — consistent with a text-mining false positive rather than a genuine signal.
- Mechanism of action (DG002) and TFDA/SmPC safety data (DG001, blocking) are both missing, so this candidate cannot proceed even if the indication signal were stronger.

**To proceed, the following is needed:**
- SmPC/label safety data (warnings, contraindications, interactions) to resolve blocking gap DG001
- Confirmed mechanism-of-action data (DG002) to properly evaluate mechanistic plausibility
- If pursuing further repurposing evaluation, prioritize candidates with actual streptozocin-specific trial history (e.g., small cell lung carcinoma) over the current top-ranked MS prediction, despite its higher TxGNN score
- Original indication documentation for this drug, currently absent from the evidence pack
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

