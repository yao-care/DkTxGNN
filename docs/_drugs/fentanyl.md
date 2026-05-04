---
layout: default
title: Fentanyl
parent: 僅模型預測 (L5)
nav_order: 188
evidence_level: L5
indication_count: 4
---

# Fentanyl
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Fentanyl: From Pain Management to Nephrogenic Syndrome of Inappropriate Antidiuresis

## One-Sentence Summary

Fentanyl is a synthetic opioid analgesic widely used for the management of acute and chronic pain, as well as anaesthetic induction. The TxGNN model predicts it may be effective for **Nephrogenic Syndrome of Inappropriate Antidiuresis (NSIAD)**, with a prediction confidence score of **99.46%**. However, there are currently **no clinical trials** and **no publications** supporting this direction, placing this candidate at the lowest evidence tier.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available from current regulatory data (fentanyl is classically indicated for pain management and anaesthesia) |
| Predicted New Indication | Nephrogenic Syndrome of Inappropriate Antidiuresis (NSIAD) |
| TxGNN Prediction Score | 99.46% |
| Evidence Level | L5 — Model prediction only, no supporting studies identified |
| Denmark Market Status | Not authorised in Denmark |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on known pharmacological knowledge, fentanyl is a highly potent synthetic opioid that acts primarily as a full agonist at the μ-opioid receptor (MOR). Its analgesic and anaesthetic properties are mediated through central and peripheral opioid pathways involving inhibition of neuronal excitability and modulation of neurotransmitter release.

NSIAD is a rare X-linked condition caused by gain-of-function mutations in the V2 vasopressin receptor gene (*AVPR2*), resulting in constitutive receptor activation, inappropriate water reabsorption, and dilutional hyponatraemia. The theoretical mechanistic bridge between fentanyl and NSIAD may lie in opioid modulation of the arginine vasopressin (AVP) axis: preclinical data suggest μ-opioid receptor activation can influence hypothalamic AVP secretion and renal aquaporin-2 trafficking, potentially intersecting with the V2 receptor signalling cascade dysregulated in NSIAD.

However, this mechanistic link remains speculative. No published clinical studies or trials have examined fentanyl's role in NSIAD management. The TxGNN model's high prediction score likely reflects graph-level connectivity between opioid receptor nodes and vasopressin pathway nodes in the knowledge graph, rather than direct experimental evidence. This prediction should be treated as a hypothesis-generating signal only, requiring rigorous mechanistic validation before any clinical consideration.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Denmark Market Information

Fentanyl holds no marketing authorisations registered in the current dataset for Denmark. No product listings, approved indications, or dosage forms are available from the regulatory data provided.

> **Note:** This absence may reflect a data completeness limitation in the current Evidence Pack (candidate ID TW-DB00813-multi), as fentanyl-containing products are authorised by the EMA and commonly available in many European markets. Verification against the Lægemiddelstyrelsen product database and the EMA centralised authorisation register is strongly recommended before drawing regulatory conclusions.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

> **Important:** Fentanyl is a Schedule II controlled opioid with a well-established risk profile including respiratory depression, opioid dependence, tolerance, and misuse potential. Even without formal SmPC data in the current Evidence Pack, any repurposing study must account for these class-level risks, particularly in a non-pain, non-anaesthesia patient population such as NSIAD patients who may have concurrent electrolyte and renal vulnerabilities.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction score is very high (99.46%), indicating strong graph-based signal, but there is a complete absence of corroborating clinical or preclinical evidence — no trials, no published studies, and no safety data are available. The proposed mechanistic pathway (opioid–vasopressin axis interaction) is biologically plausible but entirely unvalidated for this indication. Fentanyl's significant safety and regulatory burden as a controlled opioid further elevates the threshold for evidence required before proceeding.

**To proceed, the following is needed:**

- **Mechanistic validation:** Preclinical studies examining fentanyl or μ-opioid receptor agonists on V2 receptor signalling, aquaporin-2 expression, and urine osmolality in NSIAD animal models or V2 receptor gain-of-function cell lines
- **Safety data retrieval:** Full SmPC and Lægemiddelstyrelsen/EMA label data for fentanyl, with particular attention to renal, electrolyte, and CNS adverse effect profiles relevant to the NSIAD population
- **Regulatory status confirmation:** Cross-reference the Danish Lægemiddelstyrelsen and EMA product databases to confirm current authorisation status and available formulations
- **Drug interaction assessment:** NSIAD patients may receive tolvaptan or urea; opioid DDI profile with these agents must be established
- **MOA documentation:** Retrieve full mechanism of action data from DrugBank (DB00813) to complete the repurposing rationale analysis
- **Expert consultation:** Nephrology and clinical pharmacology review of the biological plausibility before any IND or protocol development is initiated
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

