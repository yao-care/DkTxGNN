---
layout: default
title: Aprepitant
parent: 僅模型預測 (L5)
nav_order: 43
evidence_level: L5
indication_count: 10
---

# Aprepitant
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

# Aprepitant: From Nausea and Vomiting Prevention to Nephrogenic Syndrome of Inappropriate Antidiuresis

## One-Sentence Summary

Aprepitant (Emend) is a selective neurokinin-1 (NK1) receptor antagonist, clinically established for the prevention of chemotherapy-induced nausea and vomiting (CINV) and postoperative nausea and vomiting (PONV). The TxGNN model predicts it may be effective for **nephrogenic syndrome of inappropriate antidiuresis (NSIAD)** with a confidence score of **99.97%**; however, there are currently **no clinical trials and no publications** directly supporting this repurposing direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Prevention of chemotherapy-induced nausea and vomiting (CINV) and postoperative nausea and vomiting (PONV) |
| Predicted New Indication | Nephrogenic Syndrome of Inappropriate Antidiuresis (NSIAD) |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| Denmark Market Status | Not registered in dataset |
| Number of Marketing Authorisations | 0 (in current dataset) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, the formal mechanism of action data for Aprepitant is listed as a data gap in this evidence pack. Based on its well-established clinical pharmacology, Aprepitant is a highly selective antagonist of the neurokinin-1 (NK1) receptor — the principal receptor for Substance P (SP), a neuropeptide mediating pain, inflammation, and emesis. By competitively blocking SP binding to NK1 receptors in both the nucleus tractus solitarius and peripheral tissues, Aprepitant suppresses the delayed phase of CINV. Importantly, NK1 receptors are not confined to the central nervous system: they are expressed in a range of peripheral tissues including the kidney, gastrointestinal tract, pulmonary vasculature, and skin — which forms the biological basis for the TxGNN model's broader repurposing predictions.

Nephrogenic syndrome of inappropriate antidiuresis (NSIAD) is a rare X-linked disorder caused by constitutively activating gain-of-function mutations in the *AVPR2* gene, which encodes the vasopressin V2 receptor. Unlike classical syndrome of inappropriate antidiuretic hormone secretion (SIADH), NSIAD is mutation-driven: the V2 receptor remains constitutively active regardless of circulating vasopressin levels, causing persistent aquaporin-2 trafficking to the collecting duct membrane, continuous water reabsorption, and hyponatraemia even when plasma vasopressin is undetectable. There is limited mechanistic evidence that Substance P and NK1 receptors are expressed in renal tubular cells and may modulate renal sodium and water handling; however, a direct pharmacological link between NK1 receptor blockade and correction of AVPR2 gain-of-function signalling has not been established in any published preclinical or clinical study.

This prediction most likely reflects shared biological network nodes in the TxGNN knowledge graph — such as shared signalling intermediates, co-expressed genes, or overlapping transcriptional regulators — rather than a well-characterised pharmacological mechanism. At this stage, the prediction should be regarded as a hypothesis-generating signal only, and interpreted with caution pending dedicated mechanistic investigation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Denmark Market Information

No marketing authorisations for Aprepitant were found in the current dataset.

> **Important note for Danish healthcare professionals**: Aprepitant is commercially available in Denmark through the centralised EMA marketing authorisation for **Emend** (EU/1/03/261, MSD/Merck Sharp & Dohme). The dataset used for this report does not appear to have captured this EMA-authorised product, which represents a data gap in the regulatory module. Danish prescribers should consult the current Lægemiddelstyrelsen medicinal product database and the approved Summary of Product Characteristics (SmPC) for up-to-date information on formulations, reimbursement status, and approved indications.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although the TxGNN model assigns a very high prediction score (99.97%), the evidence base for Aprepitant in NSIAD currently sits at Level 5 — model prediction only — with no clinical trials, no observational studies, and no preclinical mechanistic data to support this indication. NSIAD is a rare genetic disorder with a well-defined molecular aetiology (*AVPR2* gain-of-function mutations) that is mechanistically distant from NK1 receptor pharmacology, and the biological plausibility of this specific repurposing direction remains unestablished.

**To proceed, the following is needed:**
- Preclinical studies (in vitro or murine models) investigating NK1 receptor expression and Substance P signalling in *AVPR2*-mutant renal collecting duct cells
- Mechanistic clarification of any interaction between SP/NK1 pathways and vasopressin V2 receptor signalling or aquaporin-2 membrane trafficking
- Formal retrieval of Aprepitant MOA data from DrugBank API (currently a data gap in this evidence pack)
- Full safety review via the EMA-approved Emend SmPC, specifically targeting contraindications, key warnings, and clinically relevant drug-drug interactions
- A targeted literature search broadened beyond NSIAD to cover hyponatraemia, SIADH, and renal water handling in the context of NK1 antagonism, to identify any mechanistic bridging evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

