---
layout: default
title: Granisetron
parent: 僅模型預測 (L5)
nav_order: 212
evidence_level: L5
indication_count: 10
---

# Granisetron
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

# Granisetron: From Chemotherapy-Induced Nausea and Vomiting to Manic Bipolar Affective Disorder

## One-Sentence Summary

Granisetron is a selective 5-HT₃ receptor antagonist primarily used for the prevention and treatment of chemotherapy-induced nausea and vomiting (CINV) and postoperative nausea and vomiting (PONV).
The TxGNN model predicts it may be effective for **Manic Bipolar Affective Disorder**, with **0 clinical trials** and **0 publications** currently supporting this specific direction.
The high prediction score (99.62%) is a hypothesis-generating signal only; the overall evidence base remains at L5.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Chemotherapy-induced nausea and vomiting (CINV); postoperative nausea and vomiting (PONV) |
| Predicted New Indication | Manic Bipolar Affective Disorder |
| TxGNN Prediction Score | 99.62% |
| Evidence Level | L5 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on well-established pharmacology, Granisetron is a highly selective 5-HT₃ receptor antagonist: it competitively blocks serotonin type 3 receptors located on vagal afferent neurons and in the chemoreceptor trigger zone, which is the basis for its antiemetic effect.

The proposed mechanistic link to manic bipolar affective disorder rests on the observation that 5-HT₃ receptors are expressed in the limbic system, where their activation modulates dopamine release. Because serotonin-dopamine imbalance is a recognised feature of bipolar mood episodes, 5-HT₃ blockade could theoretically dampen dysregulated limbic dopaminergic activity during manic phases.

However, this connection is highly indirect. The path from peripheral antiemetic action to central mood regulation involves multiple unvalidated steps, and no direct preclinical or clinical data exist for Granisetron — or any 5-HT₃ antagonist — specifically in manic episodes. The TxGNN prediction should be treated as a hypothesis to investigate, not as actionable clinical evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Granisetron in manic bipolar affective disorder.

---

## Literature Evidence

Currently no related literature available for Granisetron in manic bipolar affective disorder.

---

## Denmark Market Information

Granisetron currently holds no marketing authorisations registered in Denmark. No approved product labelling or Summary of Product Characteristics (SmPC) is available through the Danish Medicines Agency (Lægemiddelstyrelsen) in the current dataset.

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|-------------------------------|--------------|-------------|---------------------|
| — | — | — | No authorisations on record |

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

---

## Additional Predicted Indications (Overview)

The model returned five unique indications in the top 10. All are currently at L4–L5 with no direct clinical evidence for Granisetron specifically.

| Rank | Indication | TxGNN Score | Evidence Level | Recommendation |
|------|-----------|-------------|---------------|----------------|
| 1 | Manic Bipolar Affective Disorder | 99.62% | L5 | Hold |
| 3 | Tourette Syndrome | 99.52% | L4 | Research Question |
| 5 | Acute Contagious Conjunctivitis | 99.49% | L5 | Hold |
| 7 | Angioedema | 99.36% | L5 | Hold |
| 9 | Allergic Urticaria | 99.32% | L5 | Hold |

**Tourette Syndrome** carries the strongest mechanistic rationale of the five: 5-HT₃ antagonism can indirectly modulate basal ganglia dopamine activity, and the related drug ondansetron has been explored in small trials for tic disorders (indirect class-effect evidence). This indication warrants a dedicated literature review before a final recommendation.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although the TxGNN prediction score is high across all five indications, there are zero registered clinical trials and zero publications directly supporting Granisetron for any of the predicted conditions. The mechanistic rationale is indirect and speculative, MOA data is missing, and the drug has no registered marketing authorisation in Denmark.

**To proceed, the following is needed:**

- **MOA data**: Retrieve full DrugBank mechanism-of-action and pharmacology entry for Granisetron
- **Safety data**: Obtain approved SmPC (available via EMA/Kytril EPAR) to populate warnings, contraindications, and drug interaction profile
- **Class-effect literature review**: Assess whether ondansetron or other 5-HT₃ antagonists have preclinical or clinical data in bipolar disorder or Tourette syndrome — positive class-effect evidence would upgrade Granisetron's rating
- **Preclinical proof-of-concept**: Commission or identify animal model studies for 5-HT₃ antagonism in manic-phase behaviour before any human trial consideration
- **Regulatory pathway clarification**: Verify whether Granisetron has an existing EMA centralised authorisation (e.g., Kytril) that could support a label extension discussion with Lægemiddelstyrelsen
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

