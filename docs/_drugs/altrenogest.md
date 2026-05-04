---
layout: default
title: Altrenogest
parent: 僅模型預測 (L5)
nav_order: 31
evidence_level: L5
indication_count: 10
---

# Altrenogest
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

# Altrenogest: From Veterinary Progestogen to Orofacial Clefting Syndrome

## One-Sentence Summary

Altrenogest is a synthetic progestogen used exclusively in veterinary medicine (primarily to suppress oestrus and maintain pregnancy in mares and sows), with no approved human indication and no marketing authorisation in Denmark.
The TxGNN model predicts it may be effective for **Orofacial Clefting Syndrome** as its top-ranked indication, with a prediction score of **98.06%**.
However, **no clinical trials and no published literature** support this direction, and the mechanistic rationale analysis strongly suggests this prediction represents a **model false positive** rather than a genuine therapeutic opportunity.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No approved human indication — veterinary progestogen (oestrus suppression, pregnancy maintenance in animals) |
| Predicted New Indication | Orofacial Clefting Syndrome |
| TxGNN Prediction Score | 98.06% |
| Evidence Level | L5 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Altrenogest is a potent synthetic progestogen belonging to the 19-nor-testosterone class of progestins. Its primary established use is in veterinary medicine — specifically to synchronise oestrus in gilts and to maintain pregnancy in mares by supplementing endogenous progesterone levels via progesterone receptor (PR) agonism. It has no approved human indication, and human exposure is considered a significant safety concern (it is classified as a skin-absorption hazard in occupational settings).

The TxGNN model's top-ranked predictions for Altrenogest — orofacial clefting syndrome, interventricular septum aneurysm, Jeune syndrome with situs inversus, and Pierre Robin syndrome variants — are all congenital structural defects. Critically, the link between progestogens and orofacial clefting documented in the scientific literature is a **teratogenicity risk signal**, not a therapeutic one. Early observational studies raised concerns that gestational progestogen exposure may increase the risk of cleft palate; the knowledge graph appears to have mislearned this "drug–adverse effect/risk factor" edge as a "drug–treatment" relationship, generating a spurious high-confidence score.

From a biological standpoint, none of the predicted conditions — craniofacial structural malformations, cardiac septal anomalies, ciliopathy-driven thoracic dystrophy, or chromosomally-driven mandibular hypoplasia — have any recognised pharmacological mechanism by which progesterone receptor agonism could provide treatment benefit. These are fixed anatomical or genetically-driven defects for which hormone supplementation has no established corrective pathway. The consensus across all five unique predicted indications is that these predictions are very likely false positives arising from topological artefacts in the knowledge graph, rather than genuine drug–disease therapeutic relationships.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Detailed human safety data (key warnings, contraindications, and drug interactions) are not available in the current Evidence Pack. Please refer to the approved Summary of Product Characteristics (SmPC) and relevant occupational safety guidelines for safety information. Note that Altrenogest carries a well-documented **transdermal absorption hazard** in occupational settings and is considered potentially harmful to humans upon skin contact; this should be considered if any investigational human use were ever contemplated.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All ten predicted indications (five unique diseases, each appearing twice in the ranking) carry an L5 evidence level — meaning the predictions rest solely on the TxGNN model output with no corroborating clinical trials or published literature. Furthermore, the mechanistic analysis for each predicted indication identifies the high scores as likely false positives stemming from a teratogenicity signal being misclassified as a therapeutic relationship in the knowledge graph. Altrenogest has no approved human indication, is not marketed in Denmark, and is primarily a veterinary compound with known human safety risks. There is currently no scientific rationale to justify progressing this candidate.

**To proceed, the following would be needed:**
- Independent expert review to formally adjudicate whether the TxGNN predictions represent graph-topology artefacts (false positives) and, if so, flag DB11372 for exclusion from human repurposing pipelines
- Retrieval of full mechanism of action data from DrugBank (DG002) and human safety data / contraindication data (DG001) prior to any further evaluation
- If a future hypothesis were generated by an alternative method (not the current TxGNN top-10), a de novo literature review and prospective biological plausibility assessment would be required before any investigational steps
- Assessment of whether Altrenogest should be excluded from the repurposing candidate pool given its veterinary-only status and known human hazard profile

---

> **Disclaimer:** This report is generated for research reference purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before any application in human medicine.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

