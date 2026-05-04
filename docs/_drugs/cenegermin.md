---
layout: default
title: Cenegermin
parent: 僅模型預測 (L5)
nav_order: 102
evidence_level: L5
indication_count: 10
---

# Cenegermin
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

# Cenegermin: From Neurotrophic Keratitis to HER2 Positive Breast Carcinoma

## One-Sentence Summary

Cenegermin (Oxervate) is a recombinant human nerve growth factor (rhNGF), approved by the EMA for the treatment of neurotrophic keratitis — a rare, sight-threatening corneal disease caused by impaired trigeminal innervation. The TxGNN model predicts it may be effective for **HER2 Positive Breast Carcinoma**, with a prediction score of **96.83%**; however, **no clinical trials or relevant literature** currently support this direction, and the available mechanistic analysis raises active safety concerns regarding pro-tumour risk.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Neurotrophic keratitis (EMA-approved as Oxervate; not registered in Denmark) |
| Predicted New Indication | HER2 Positive Breast Carcinoma |
| TxGNN Prediction Score | 96.83% |
| Evidence Level | L5 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Cenegermin is a recombinant form of human nerve growth factor (rhNGF), produced via an *E. coli* expression system. Its sole approved clinical application is neurotrophic keratitis — a corneal condition in which loss of trigeminal innervation leads to epithelial breakdown. In that context, topical cenegermin restores corneal epithelial integrity by activating TrkA (NTRK1) receptors on corneal cells, thereby supporting cell survival, differentiation, and wound healing.

The proposed mechanistic link to HER2-positive breast carcinoma rests on the observation that NGF-TrkA signalling and HER2 (ErbB2) downstream pathways share the PI3K/Akt axis. In principle, this convergence could be interpreted as a point of therapeutic relevance. However, this intersection cuts both ways: in the setting of HER2-amplified tumours, activation of the PI3K/Akt pathway — which is precisely what an NGF agonist would promote — is a known driver of tumour cell survival and resistance to therapy, not a therapeutic target.

Critically, the existing preclinical literature does not support the use of NGF agonism in any breast cancer subtype. Studies in ER-positive cell lines (e.g. MCF-7) indicate that NGF promotes tumour cell proliferation. In triple-negative breast cancer, *inhibition* of TrkA (not activation) has been associated with anti-tumour effects. The TxGNN high score for this indication most likely reflects the NGF-breast tissue relationship encoded in the knowledge graph as a broad biological association, rather than a disease-specific therapeutic signal. Based on the current mechanistic evidence, proceeding with this repurposing hypothesis carries a plausible risk of harm.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

No trials combining cenegermin (or rhNGF) with HER2-positive breast carcinoma, or any breast cancer subtype, were identified in ClinicalTrials.gov or the WHO ICTRP as of the data cut-off (2026-04-04).

---

## Literature Evidence

Currently no relevant literature available.

The PubMed search retrieved results for the "breast tumor luminal A or B" query pairing, but upon review all retrieved publications were entirely unrelated to cenegermin or breast cancer treatment (papers concerned B-cell biology, hepatitis B vaccination, HLA typing, and unrelated chemistry). No publications examining cenegermin, rhNGF, or NGF agonism in any breast cancer indication were identified.

---

## Denmark Market Information

Cenegermin is **not registered or marketed in Denmark**. No national (Laegemiddelstyrelsen) or centralised (EMA) marketing authorisations are currently active in the Danish market.

> **Note for completeness:** Cenegermin is centrally authorised in the EU under the trade name **Oxervate** (EU/1/17/1187/001, Dompé farmaceutici S.p.A.) for the treatment of moderate-to-severe neurotrophic keratitis in adults. Danish prescribers wishing to access this product for the approved indication would need to do so via special import or named-patient procedures. This centralised authorisation covers the EU including Denmark, but the product is not actively distributed in the Danish market as of the data cut-off.

---

## Safety Considerations

No drug-specific safety data (warnings, contraindications, or drug interactions for cenegermin) were retrievable in this Evidence Pack. The following concern arises specifically from the repurposing context:

- **Mechanistic pro-tumour risk**: As an NGF agonist, cenegermin activates TrkA/PI3K/Akt signalling. In HER2-amplified or ER-positive tumour settings, this pathway activation is associated with tumour cell survival promotion rather than inhibition. This theoretical risk has not been formally evaluated in clinical or robust preclinical oncology studies.

Please refer to the approved Summary of Product Characteristics (SmPC) for Oxervate for the full safety profile in its licensed indication.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction score is high (96.83%), but the evidence base is entirely absent (L5 — model prediction only), and the mechanistic analysis actively contradicts the therapeutic hypothesis: cenegermin is an NGF agonist, and NGF-TrkA pathway activation is associated with pro-tumour effects in breast cancer cell lines. There is no clinical, translational, or preclinical study directly supporting cenegermin's use in any breast cancer subtype. Proceeding to the next evaluation stage is not justified at this time.

**To revisit this indication, the following would be needed:**

- Dedicated preclinical studies (in vitro and in vivo) examining the effect of rhNGF/TrkA agonism specifically in HER2-amplified breast cancer models, with particular attention to tumour proliferation, survival signalling, and anti-HER2 therapy interactions
- Clarification of whether the TxGNN high score reflects a true disease-specific repurposing signal or a non-specific NGF–breast tissue graph relationship
- Full MOA documentation from DrugBank (data gap DG002) to complete the mechanistic assessment
- Review of the full Oxervate SmPC for safety data applicable to potential systemic or novel-route administration contexts (current approval is topical ophthalmic only)
- An assessment of route-of-administration feasibility: cenegermin is currently formulated exclusively as ophthalmic eye drops (0.02% solution), and any oncology application would require a fundamentally different delivery strategy

> **Research disclaimer:** This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any therapeutic application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

