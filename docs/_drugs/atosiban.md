---
layout: default
title: Atosiban
parent: 僅模型預測 (L5)
nav_order: 49
evidence_level: L5
indication_count: 10
---

# Atosiban
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

# Atosiban: From Preterm Labour to Primary Hereditary Glaucoma

---

## One-Sentence Summary

Atosiban is a synthetic peptide oxytocin/vasopressin receptor (OXTR) antagonist, established in clinical practice as a tocolytic agent to inhibit uterine contractions and delay preterm birth.
The TxGNN model predicts it may be effective for **Primary Hereditary Glaucoma** with a confidence score of **99.92%**,
however, **zero clinical trials and zero published publications** currently support this direction — placing it at the lowest evidence level (L5) and raising significant mechanistic concerns about treatment directionality.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Preterm labour (tocolytic agent) |
| Predicted New Indication | Primary Hereditary Glaucoma |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 |
| Denmark Market Status | Not Marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the current evidence pack. Based on established pharmacological knowledge, Atosiban is a competitive antagonist at both oxytocin receptors (OXTR) and vasopressin V1a receptors. Its proven clinical role is inhibiting OXTR-mediated uterine smooth muscle contractions to delay premature birth.

The mechanistic link proposed by TxGNN rests on the known expression of OXTR in ocular tissues — specifically in the trabecular meshwork and ciliary body. Endogenous oxytocin has been shown in some studies to lower intraocular pressure (IOP), plausibly through prostaglandin-mediated pathways that enhance aqueous humour outflow. Because Atosiban *blocks* this receptor, its net pharmacological effect on IOP is directionally uncertain and may in fact raise IOP rather than lower it — the opposite of what is therapeutically required in glaucoma management.

Primary hereditary glaucoma arises from mutations in structural and regulatory genes (MYOC, OPTN, WDR36) that increase trabecular outflow resistance. There is no established pathogenic connection between these genetic drivers and the oxytocin–OXTR axis. The high TxGNN score most likely reflects shared gene co-expression patterns in ocular tissues captured by the graph neural network, rather than a validated therapeutic mechanism. The prediction should be interpreted with significant caution: **the pharmacological direction of Atosiban's action in glaucoma is plausibly counterproductive**.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

*(Systematic searches of ClinicalTrials.gov and the WHO ICTRP were conducted on 2026-03-10 for Atosiban across all predicted indications — primary hereditary glaucoma, open-angle glaucoma, alopecia, congenital hypotrichosis milia, and hypotrichosis simplex of the scalp — and returned zero results in all cases.)*

---

## Literature Evidence

Currently no related literature available.

*(PubMed searches conducted on 2026-03-10 for Atosiban across all five predicted indications returned zero publications.)*

---

## Denmark Market Information

Atosiban is not currently registered or marketed in Denmark according to the data available in this evidence pack. No marketing authorisations from the Danish Medicines Agency (Laegemiddelstyrelsen) or via the EMA centralised procedure are recorded.

> **Note:** This dataset may be incomplete with respect to Danish/EMA registration status. Independent verification via the Laegemiddelstyrelsen product database and the EMA medicines portal is strongly recommended before drawing final conclusions about availability in Denmark.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

*(No drug interaction data, key warnings, or contraindication data were available in this evidence pack. Retrieval from the Danish Medicines Agency product registration and DrugBank is recommended as a priority remediation step before any further evaluation.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All five predicted indications in this evidence pack rest exclusively on TxGNN model scores (L5 evidence), with zero supporting clinical trials or peer-reviewed publications identified. More critically, the leading predicted mechanism — OXTR blockade in ocular tissue — is pharmacologically counterproductive for glaucoma: Atosiban's antagonist action is likely to *oppose* the IOP-lowering effect of endogenous oxytocin, not to replicate it. This directional conflict disqualifies the primary prediction as a viable near-term repurposing candidate.

**To proceed, the following is needed:**

- **Regulatory verification:** Confirm Atosiban's current authorisation status in Denmark directly via the Laegemiddelstyrelsen product database and the EMA medicines portal, as the regulatory data in this pack appears incomplete
- **MOA data retrieval:** Obtain full mechanism of action and pharmacodynamic data from DrugBank (DB09059) and the approved SmPC to enable proper mechanistic review
- **Safety data retrieval:** Download and parse the full SmPC from the Danish/EMA labelling to identify contraindications, key warnings, and clinically relevant drug interactions
- **Preclinical mechanistic studies:** Commission or identify studies directly measuring the effect of OXTR *antagonism* (not agonism) on intraocular pressure in animal or cell-culture glaucoma models before any clinical hypothesis can be formed
- **Direction re-evaluation:** Consider whether an OXTR *agonist* (rather than Atosiban as an antagonist) would be a more pharmacologically coherent candidate for IOP reduction in glaucoma — a conceptually inverse repurposing direction
- **Cluster review:** The five predicted indications group into two biological clusters (ocular/glaucoma and hair follicle/alopecia); both clusters share the same fundamental directional concern for an OXTR antagonist, and should be reviewed together in any subsequent mechanistic analysis
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

