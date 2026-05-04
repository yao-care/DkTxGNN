---
layout: default
title: Capsaicin
parent: 僅模型預測 (L5)
nav_order: 89
evidence_level: L5
indication_count: 10
---

# Capsaicin
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

# Capsaicin: From Peripheral Neuropathic Pain to Otitis Externa

## One-Sentence Summary

Capsaicin is a naturally occurring alkaloid from chili peppers, used clinically in high-concentration topical formulations for peripheral neuropathic pain via TRPV1 receptor desensitisation.
The TxGNN model predicts it may be effective for **Otitis Externa** (inflammation of the outer ear canal),
with a prediction score of **98.76%** and **1 publication** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Peripheral neuropathic pain |
| Predicted New Indication | Otitis Externa |
| TxGNN Prediction Score | 98.76% |
| Evidence Level | L4 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known pharmacological information, capsaicin is a potent agonist of the TRPV1 (Transient Receptor Potential Vanilloid 1) receptor, a non-selective cation channel widely expressed on sensory neurons. Initial activation of TRPV1 triggers pain signalling, but repeated or sustained stimulation leads to receptor desensitisation and depletion of neuropeptides such as substance P — which is the basis for its established analgesic effect in peripheral neuropathic pain.

Otitis externa is an inflammatory condition of the external ear canal, typically accompanied by local pain, oedema, and sensory nerve sensitisation. TRPV1 receptors are expressed in the sensory innervation of the external ear canal, and neurogenic inflammation driven by neuropeptide release is thought to contribute to symptom severity. The mechanistic overlap between TRPV1-mediated pain pathways in neuropathic conditions and the nociceptive component of external ear inflammation provides a plausible biological basis for this TxGNN prediction. A preclinical publication (PMID 12769482) has specifically described experimental models of acute inflammation in the ear, suggesting that inflammatory nociceptive pathways in this anatomical region are recognised research targets.

It should be noted, however, that translating TRPV1 desensitisation from neuropathic pain to an acutely inflamed ear canal involves significant unknowns — including appropriate formulation, local tolerability, and interaction with the inflammatory microenvironment. The prediction remains at the preclinical hypothesis stage.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for otitis externa.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [12769482](https://pubmed.ncbi.nlm.nih.gov/12769482/) | 2003 | Preclinical / Methods | Methods in Molecular Biology | Describes experimental animal models of acute inflammation in the ear, establishing a preclinical framework relevant to inflammatory ear conditions and related nociceptive pathways |

---

## Denmark Market Information

Capsaicin currently holds **no marketing authorisations** registered with the Danish Medicines Agency (Lægemiddelstyrelsen). It is not available as an approved medicinal product in Denmark.

> **Note:** Capsaicin 8% patch (Qutenza) holds a centralised EMA authorisation for peripheral neuropathic pain in other EU/EEA markets. Its absence from the Danish market may reflect a commercial or reimbursement decision rather than a safety concern. This should be verified with the Lægemiddelstyrelsen and the marketing authorisation holder before any repurposing strategy is developed.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence supporting capsaicin's use in otitis externa is currently limited to a single preclinical methodology paper from 2003, with no registered clinical trials in this indication. Although the TRPV1-mediated mechanism provides a biologically plausible rationale, the evidence base is insufficient to support clinical development or regulatory progression at this stage.

**To proceed, the following is needed:**

- **MOA data:** Retrieve full mechanism of action profile from DrugBank (DB06774) to strengthen the mechanistic rationale
- **Safety data:** Download and parse the SmPC for capsaicin (Qutenza or equivalent) to identify contraindications, warnings, and ear-canal-specific tolerability data
- **Preclinical evidence:** Conduct a systematic search for in vitro or in vivo studies specifically evaluating capsaicin in external ear inflammation models
- **Formulation assessment:** Evaluate whether existing topical formulations (patch, cream, solution) are compatible with the ear canal route of administration
- **Regulatory consultation:** Assess the pathway for a new indication in Denmark via the Lægemiddelstyrelsen, including whether an off-label use framework or a new marketing authorisation application would apply
- **Clinical feasibility study:** Design a Phase 1/2 pilot study to assess local tolerability and preliminary efficacy of a capsaicin-based formulation in otitis externa patients

---

> ⚠️ **Disclaimer:** This report is intended for research purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before any therapeutic application. This prediction has been generated by the TxGNN model and has not been reviewed by a regulatory authority.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

