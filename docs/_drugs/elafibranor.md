---
layout: default
title: Elafibranor
parent: 僅模型預測 (L5)
nav_order: 158
evidence_level: L5
indication_count: 10
---

# Elafibranor
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

# Elafibranor: From Metabolic Liver Disease to Amenorrhea

## One-Sentence Summary

Elafibranor is a dual PPARα/δ agonist investigated primarily for metabolic liver diseases, including Non-Alcoholic Steatohepatitis (NASH) and Primary Biliary Cholangitis (PBC), but currently holds no marketing authorisation in Denmark.
The TxGNN model predicts it may be effective for **Amenorrhea** (highest-ranked prediction, score 99.86%), yet **no clinical trials** and **no publications** were identified to support this specific repurposing direction.
All five predicted indications are at evidence level **L5 — model prediction only** — and the overall recommendation is **Hold** pending fundamental mechanistic and safety data.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No approved indication in Denmark; investigated for NASH and Primary Biliary Cholangitis |
| Predicted New Indication | Amenorrhea (rank 1) |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L5 — model prediction only; no clinical trials or publications found |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known information, Elafibranor is a dual PPARα/δ (peroxisome proliferator-activated receptor alpha/delta) agonist. Its investigational efficacy has been studied in the context of hepatic metabolic disease — specifically NASH and PBC — where it modulates fatty acid β-oxidation, lipid metabolism, and hepatic inflammation.

The proposed mechanistic link to amenorrhea rests on the hypothesis that PPARα/δ-driven enhancement of energy substrate utilisation may indirectly influence hypothalamic GnRH pulsatile secretion. This pathway is conceptually relevant to **functional hypothalamic amenorrhea** triggered by negative energy balance (e.g., exercise-induced or nutrition-deficit amenorrhea). However, this reasoning is largely extrapolated from PPARγ research; there is currently **no published evidence** that PPARα or PPARδ agonism directly modulates the hypothalamic-pituitary-ovarian (HPO) axis.

The internal mechanistic relevance rating for this pairing is extremely weak (2/10). It is therefore likely that the high TxGNN score reflects shared structural topology in the biomedical knowledge graph rather than a meaningful biological signal. This finding is consistent across all five predicted indications, none of which have confirmatory clinical or preclinical literature support.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Elafibranor in amenorrhea.

---

## Literature Evidence

Currently no related literature available for Elafibranor in amenorrhea.

---

## Denmark Market Information

Elafibranor currently holds **no marketing authorisations** in Denmark. The drug is not registered with the Danish Medicines Agency (Laegemiddelstyrelsen) and is not available on the Danish market in any dosage form or indication.

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|-------------------------------|-------------|-------------|---------------------|
| — | — | — | No authorisation on record |

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information. Drug interaction data, key warnings, and contraindications were not retrievable at the time of this assessment.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All five TxGNN-predicted indications for Elafibranor — amenorrhea, non-syndromic esophageal malformation, bone Paget disease, dentinogenesis imperfecta, and squamous cell carcinoma — are at evidence level L5, supported by model prediction alone and no confirmatory clinical trials or published literature. Mechanistic relevance ranges from extremely weak (amenorrhea, 2/10) to absent (non-syndromic esophageal malformation and dentinogenesis imperfecta, 0/10), and one prediction (squamous cell carcinoma) carries an active **safety concern**: PPARδ agonism is associated with pro-tumorigenic effects in squamous epithelia, making Elafibranor potentially contraindicated rather than therapeutic in that setting. The drug is also not currently authorised in Denmark, meaning the regulatory pathway would require initiation from scratch.

**To proceed, the following is needed:**

- **SmPC and safety data**: Retrieve the full Summary of Product Characteristics (including warnings, contraindications, and interactions) from the EMA product page or the originating company, to enable a proper safety screening (Stage S1)
- **MOA confirmation**: Obtain complete PPARα/δ agonism profile from DrugBank or primary pharmacology literature, including tissue-specific receptor activity and any known endocrine effects
- **Preclinical literature review**: Conduct a targeted search (PubMed, Embase) specifically for PPARα/δ agonists and reproductive endocrinology or hypothalamic function to assess whether any biological basis for the amenorrhea prediction exists before proceeding
- **Indication prioritisation review**: Given that the top-ranked indication has a 2/10 mechanistic score, consider whether a different therapeutic area (e.g., bone metabolism via PPARδ, rated 4/10) represents a stronger starting point for further investigation
- **Regulatory landscape mapping**: Clarify Elafibranor's current global approval status (including EMA centralised procedure for PBC) and determine whether any existing authorisation could support a label extension pathway within the EU/Denmark

---

*This report is generated for research purposes only and does not constitute medical advice. All repurposing candidates require clinical validation before any therapeutic application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

