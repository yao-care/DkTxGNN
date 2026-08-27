---
layout: default
title: Nicorandil
parent: 僅模型預測 (L5)
nav_order: 309
evidence_level: L5
indication_count: 10
---

# Nicorandil
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

# Nicorandil: From Angina Pectoris to Benign Prostatic Hyperplasia

## One-Sentence Summary

Nicorandil is a hybrid ATP-sensitive potassium (K_ATP) channel opener / nitrate vasodilator, classically used as an antianginal agent (this original-indication classification is based on general pharmacological knowledge, as it is not recorded in the supplied Danish regulatory data). The TxGNN model predicts it may be effective for **Benign Prostatic Hyperplasia (BPH)**, currently supported by **3 publications** and **no registered clinical trials**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Angina pectoris (based on known pharmacology of K_ATP channel openers; not present in the Danish regulatory data supplied) |
| Predicted New Indication | Benign Prostatic Hyperplasia (BPH) |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L4 (preclinical / mechanism studies only, no clinical trials) |
| Denmark Market Status | Not Marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the evidence pack (marked as a data gap). Based on general pharmacological knowledge, Nicorandil is a K_ATP channel opener with nicotinamide-nitrate hybrid structure, producing coronary and peripheral vasodilation; its efficacy as an antianginal agent depends on this vasodilatory action.

The supporting literature suggests a plausible link between this vasodilatory mechanism and BPH: BPH/benign prostatic enlargement is increasingly recognized as associated with impaired prostatic blood flow and atherosclerotic/ischemic vascular disease, rather than being purely a hormonal proliferative process. A direct preclinical study (PMID 24448152) treated spontaneously hypertensive rats with nicorandil and observed effects on prostatic blood flow and prostatic hyperplasia development, providing a mechanistic (animal-level) rationale for the TxGNN prediction.

Because the proposed link operates through vascular physiology rather than a cancer- or hormone-specific pathway, the mechanistic story is coherent, but it currently rests entirely on one rodent model and review-level literature — there is no clinical (human) evidence yet.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24448152](https://pubmed.ncbi.nlm.nih.gov/24448152/) | 2014 | Preclinical (animal study) | Scientific Reports | In spontaneously hypertensive rats, 6 weeks of nicorandil treatment altered prostatic blood flow and tissue markers, supporting a prostatic-ischemia mechanism for BPH development and a potential protective effect of nicorandil |
| [31735753](https://pubmed.ncbi.nlm.nih.gov/31735753/) | 2019 | Review | Nihon Yakurigaku Zasshi (Folia Pharmacologica Japonica) | Reviews evidence that impaired prostatic blood flow drives BPH/BPE and associated LUTS, linking BPH to atherosclerotic disease such as hypertension |
| [26165338](https://pubmed.ncbi.nlm.nih.gov/26165338/) | 2015 | Review | Nihon Yakurigaku Zasshi (Folia Pharmacologica Japonica) | Discusses lower urinary tract symptoms as a vascular dysfunction and the potential role of nicorandil as a vasodilator (abstract not available) |

---

## Denmark Market Information

Currently not marketed in Denmark — no marketing authorisation registered (0 licenses on file).

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information. Key warnings, contraindications, and drug interaction data were not available in the evidence pack (DG001, Blocking data gap), and a DDI database query returned no results.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The BPH prediction is currently supported only by one rodent mechanistic study and two review articles (L4), with no clinical trials or human data. Combined with a Blocking data gap on Danish SmPC safety information (DG001) and the drug's unmarketed status in Denmark, there is insufficient basis to proceed to safety evaluation.

**To proceed, the following is needed:**
- Danish/EU SmPC warnings, contraindications, and precautions (DG001 — Blocking, currently prevents entry into initial safety screening)
- Confirmed mechanism-of-action documentation from DrugBank or equivalent (DG002)
- Clinical or additional preclinical evidence of nicorandil's effect on human BPH/LUTS beyond the single SHR rat model
- Clarification of Danish/EU marketing status, since the drug currently has zero registered licenses
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

