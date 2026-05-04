---
layout: default
title: Grapiprant
parent: 僅模型預測 (L5)
nav_order: 213
evidence_level: L5
indication_count: 10
---

# Grapiprant
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

# Grapiprant: From Canine Osteoarthritis Pain to Amenorrhea

## One-Sentence Summary

Grapiprant (Galliprant) is an EP4 prostaglandin receptor antagonist currently approved exclusively as a veterinary medicine for pain and inflammation associated with osteoarthritis in dogs.
The TxGNN model predicts it may be relevant to **Amenorrhea**, with a prediction score of **98.91%**.
However, there are currently **no clinical trials and no published literature** supporting this direction, making this a model-only prediction requiring significant caution — particularly as the mechanistic rationale contains an inherent contradiction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Canine osteoarthritis pain and inflammation (veterinary use only) |
| Predicted New Indication | Amenorrhea |
| TxGNN Prediction Score | 98.91% |
| Evidence Level | L5 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Grapiprant acts as a selective antagonist of the EP4 prostaglandin receptor, blocking the downstream signalling of prostaglandin E2 (PGE2) at this specific receptor subtype. Unlike traditional NSAIDs that inhibit cyclooxygenase enzymes upstream, Grapiprant targets only one receptor in the prostanoid pathway, which in veterinary use translates to analgesia and anti-inflammatory effects with a potentially more targeted side-effect profile.

The mechanistic link to amenorrhea rests on the known role of PGE2–EP4 signalling in ovulation regulation. Experimental data from EP4 knockout mice shows that absence of EP4 receptor function results in ovulation failure, suggesting this receptor is required for successful follicle rupture. The TxGNN model may have identified this biological connection as a potential therapeutic target.

However, this is where the reasoning becomes contradictory: if EP4 signalling is *necessary* for ovulation, then an EP4 *antagonist* would be expected to impair ovulation and potentially induce — rather than treat — amenorrhea. The mechanistic direction is therefore reversed relative to a therapeutic intent. Furthermore, amenorrhea is a clinically heterogeneous condition with a wide range of aetiologies (hypothalamic, pituitary, ovarian, anatomical), the vast majority of which have no established connection to EP4 overactivation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Denmark Market Information

Grapiprant holds no marketing authorisations in Denmark. The drug is not registered with Laegemiddelstyrelsen (the Danish Medicines Agency) and has no EMA centralised authorisation for human use. It is approved in the EU as a veterinary medicinal product (Galliprant, for dogs), but this authorisation does not extend to human therapeutic use.

---

## Safety Considerations

Detailed human safety data for Grapiprant is not available in this Evidence Pack, as the drug has not been evaluated in human clinical registration programmes. No drug-drug interaction data was retrieved. There are no recorded contraindications or key warnings for human use in the current dataset.

Please refer to the veterinary Summary of Product Characteristics (SmPC) for Galliprant as the closest available reference, and note that extrapolation to human use carries significant unknowns.

Two mechanistically-derived safety signals warrant proactive attention:

- **Pro-thrombotic potential**: PGE2–EP4 signalling contributes to vasodilation and endothelial anti-thrombotic protection. EP4 blockade may shift haemostatic balance toward a pro-coagulant state, which is particularly relevant given two of the other top-ranked TxGNN predictions involve coagulation disorders (heparin cofactor 2 deficiency, antithrombin deficiency type 2) where EP4 antagonism is mechanistically contraindicated.
- **Reproductive effects**: As noted above, EP4 blockade may disrupt ovulation — relevant for any female patients of reproductive age.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate is a veterinary-only drug with no human clinical data, no registered trials, no supporting literature, and a mechanistic hypothesis that points in the opposite direction to the therapeutic goal for the top-predicted indication. The TxGNN score reflects a statistical association in the knowledge graph, not clinical feasibility. Proceeding to any human evaluation stage would require resolving fundamental mechanistic and regulatory barriers.

**Before this candidate can be reconsidered, the following is needed:**

- **Regulatory pathway assessment**: Clarify whether repurposing a veterinary-only EP4 antagonist for human use is viable under EMA/Laegemiddelstyrelsen frameworks, and what preclinical package would be required
- **Mechanistic resolution**: Determine whether there exists a disease subtype of amenorrhea in which EP4 *overactivation* is the pathological driver (which would align the mechanism); if no such subtype is identified, this indication should be deprioritised
- **Human safety data**: A Phase 1 first-in-human safety study would be prerequisite to any efficacy evaluation; no human pharmacokinetic, tolerability, or safety profile currently exists
- **MOA documentation**: Obtain full DrugBank pharmacology data (DG002) to complete the mechanistic analysis
- **Alternative indication review**: The other top-ranked predictions (infectious bovine rhinotracheitis, malignant catarrh) are veterinary diseases, further suggesting this TxGNN run may benefit from a human-disease-filtered prediction set before clinical prioritisation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

