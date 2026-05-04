---
layout: default
title: Agalsidase Beta
parent: 僅模型預測 (L5)
nav_order: 19
evidence_level: L5
indication_count: 10
---

# Agalsidase Beta
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

# Agalsidase Beta: From Fabry Disease to Cervical Neuroblastoma

## One-Sentence Summary

Agalsidase beta (Fabrazyme) is a recombinant human α-galactosidase A enzyme used as enzyme replacement therapy (ERT) for Fabry disease, a rare X-linked lysosomal storage disorder causing progressive Gb3 accumulation in vital organs. The TxGNN model predicts it may be effective for **Cervical Neuroblastoma** with a prediction score of 98.37%; however, **no clinical trials or supporting publications** have been identified for this indication. Of significant concern, all top-ranked predictions share near-identical scores and cluster exclusively among head/neck and oral cavity tumours — strongly suggesting a systematic model bias rather than genuine repurposing signal.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Fabry disease (α-galactosidase A deficiency / lysosomal storage disorder) — *based on general pharmaceutical knowledge; official indication data not available in this Evidence Pack* |
| Predicted New Indication | Cervical Neuroblastoma |
| TxGNN Prediction Score | 98.37% |
| Evidence Level | L5 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Agalsidase beta is a recombinant form of human α-galactosidase A, administered intravenously as enzyme replacement therapy. In Fabry disease, inherited deficiency of this lysosomal enzyme causes progressive accumulation of globotriaosylceramide (Gb3) throughout the body — primarily damaging the kidneys, heart, and peripheral nervous system. By supplying functional enzyme, Agalsidase beta reduces Gb3 deposits and slows organ deterioration.

Cervical neuroblastoma is a malignant tumour derived from neural crest cells, typically treated with chemotherapy, immunotherapy, and radiation. While scattered research has noted Gb3 overexpression in certain tumour types, there is **no published evidence of Gb3 overexpression specifically in cervical neuroblastoma**. More fundamentally, Agalsidase beta's mechanism is to *degrade* accumulated Gb3 — it does not act as a targeted antineoplastic agent exploiting Gb3 overexpression. As a high-molecular-weight protein therapeutic, it is also unlikely to penetrate a neuroblastoma tumour microenvironment via intravenous administration. There is therefore no clearly articulable mechanistic pathway connecting Agalsidase beta to anti-tumour activity in this indication.

A critical pattern spans all 10 predictions in this Evidence Pack: every ranked candidate is a head/neck or oral cavity tumour, entries appear in duplicate (ranks 1–2 identical, 3–4 identical, etc.), and prediction scores cluster within a range of less than 0.001 (0.9831–0.9837). This is a textbook signature of **TxGNN cluster bias**, where the model generates spurious predictions based on shared ontological proximity within the knowledge graph rather than true biological plausibility. Model recalibration and validation against an independent benchmark are strongly recommended before drawing any clinical inference from these outputs.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

> **Note:** Agalsidase beta is marketed in Europe as Fabrazyme (EMA centralised authorisation). The SmPC is publicly available via the [EMA product page](https://www.ema.europa.eu/en/medicines/human/EPAR/fabrazyme) and contains full warnings, contraindications, and infusion-related reaction guidance.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN predictions for Agalsidase beta are entirely unsupported by clinical or preclinical evidence (Evidence Level L5 across all ranked indications), and the proposed mechanistic link between an intravenous ERT for a lysosomal storage disorder and head/neck malignancies is biologically implausible. The near-identical prediction scores across five distinct tumour types — each appearing in duplicate — constitute strong evidence of a systematic model artefact that should be addressed before any further evaluation of these candidates.

**To proceed, the following is needed:**

- **Model audit first:** Investigate TxGNN cluster bias for ERT-class macromolecule drugs; if confirmed, these predictions should be filtered out or down-weighted at the pipeline level
- **MOA data retrieval:** Obtain full mechanism of action and pharmacological profile from DrugBank (DB00103) to enable proper biological plausibility scoring in future runs
- **Regulatory baseline:** Retrieve the Fabrazyme EMA SmPC for full safety, contraindication, and warning data to complete the S1 safety assessment
- **Redirect repurposing scope:** If repurposing beyond Fabry disease is of genuine interest for Agalsidase beta, focus future searches on diseases with documented lysosomal dysfunction, sphingolipid dysregulation, or Gb3 accumulation (e.g., certain hypertrophic cardiomyopathies, chronic kidney disease with podocyte involvement) rather than solid tumours
- **Denmark-specific step:** Confirm whether a centralised EMA marketing authorisation for Fabrazyme could serve as the regulatory basis for an expanded indication application, should future evidence warrant it

---

> ⚠️ **Disclaimer:** This report is generated for research reference purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before any therapeutic application. Data cutoff: 2026-04-04.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

