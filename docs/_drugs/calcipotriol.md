---
layout: default
title: Calcipotriol
parent: 僅模型預測 (L5)
nav_order: 84
evidence_level: L5
indication_count: 10
---

# Calcipotriol
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

# Calcipotriol: From Psoriasis to Seborrheic Keratosis

## One-Sentence Summary

Calcipotriol is a synthetic vitamin D3 analogue with established topical use for plaque psoriasis, modulating keratinocyte proliferation and differentiation.
The TxGNN model predicts it may be effective for **Seborrheic Keratosis**, with **0 registered clinical trials** and **6 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Plaque psoriasis (topical treatment) |
| Predicted New Indication | Seborrheic Keratosis |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L3 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on established pharmacological knowledge, calcipotriol is a synthetic analogue of calcitriol (the active form of vitamin D3). It binds to the intracellular vitamin D receptor (VDR), which regulates transcription of genes governing keratinocyte proliferation, differentiation, and apoptosis. This antiproliferative and pro-differentiating effect on keratinocytes is the mechanistic basis of its efficacy in psoriasis.

Seborrheic keratosis is characterised by benign clonal hyperproliferation of epidermal keratinocytes, sharing a fundamental pathological feature with psoriasis: dysregulated keratinocyte turnover. Because calcipotriol normalises this turnover in the psoriatic context, a comparable effect on the hyperproliferative keratinocytes of seborrheic keratosis is biologically plausible. One published study has further suggested that apoptosis induction may contribute to lesion regression.

The available case series and comparative studies consistently report visible lesion regression over 3–12 months of topical calcipotriol application, with durable remission in some cohorts extending to 6–10 years. The shared dermatological substrate and mechanistic overlap make this one of the more biologically credible TxGNN predictions in the dermatology domain.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [36752725](https://pubmed.ncbi.nlm.nih.gov/36752725/) | 2023 | Case Series | Australasian Journal of Dermatology | 12 patients with flat facial seborrheic keratosis treated with 0.005% calcipotriol ointment for 3–8 months; complete lesion regression achieved; remission sustained 6–10 years at follow-up |
| [16043912](https://pubmed.ncbi.nlm.nih.gov/16043912/) | 2005 | Case Series | Journal of Dermatology | 116 cases of senile warts/seborrheic keratosis treated with topical vitamin D3 ointments (including calcipotriol) for 3–12 months; 30.2% response rate; apoptosis induction proposed as mechanism |
| [15090020](https://pubmed.ncbi.nlm.nih.gov/15090020/) | 2004 | Comparative Study | International Journal of Dermatology | Head-to-head comparison of standard cryosurgery versus topical calcipotriene, tazarotene, and imiquimod for seborrheic keratoses; sought effective non-invasive topical alternative |
| [15577148](https://pubmed.ncbi.nlm.nih.gov/15577148/) | 2004 | Review | Clinical Calcium | Narrative review of active vitamin D3 ointments (tacalcitol, calcipotriol, maxacalcitol) applied once or twice daily to senile warts/seborrheic keratosis; summarises clinical experience |
| [10721662](https://pubmed.ncbi.nlm.nih.gov/10721662/) | 2000 | Case Report | Journal of Dermatology | Keratosis lichenoides chronica with prominent seborrheic dermatitis-like facial eruption showed marked response to calcipotriol ointment; highlights broader keratotic skin disease applicability |
| [21534378](https://pubmed.ncbi.nlm.nih.gov/21534378/) | 2011 | Case Report | JAAPA | Clinical presentation and differential diagnosis of seborrheic keratosis on the shins; contextual reference for recognition and management |

---

## Denmark Market Information

According to Laegemiddelstyrelsen data in this Evidence Pack, calcipotriol currently holds **no marketing authorisations** in Denmark, with a market status of **not marketed** and zero registered licences.

> **Important note for reviewers:** Calcipotriol-containing products (e.g., Daivonex®, Daivobet®, Enstilar®) hold centralised EMA authorisations and are marketed across multiple EU member states. The absence of records in this Evidence Pack likely reflects a data gap rather than a true absence of regulatory approval. Cross-referencing with the EMA product database and the Laegemiddelstyrelsen medicines register is strongly recommended before drawing conclusions about Danish availability.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Six published studies — including a 116-case observational series and a durable 6–10-year remission case series — provide consistent clinical signal supporting calcipotriol's efficacy in seborrheic keratosis, and the antiproliferative vitamin D3 receptor mechanism offers a coherent biological rationale. However, the complete absence of registered clinical trials, the evidence resting at L3 (observational/case series only), and unresolved questions about Danish regulatory status require a cautious, structured pathway rather than immediate implementation.

**To proceed, the following is needed:**

- **Regulatory verification**: Confirm current Danish/EU marketing authorisation status for calcipotriol-containing products via Laegemiddelstyrelsen and the EMA EPAR database; clarify whether the data gap in this Evidence Pack reflects a true absence or a query limitation
- **Full safety dossier**: Retrieve SmPC warnings, contraindications, hypercalcaemia risk thresholds, and drug interaction profile (DrugBank API query recommended to resolve DG002)
- **Mechanism of action documentation**: Formalise VDR-binding MOA from DrugBank to support mechanistic link scoring (addresses DG002)
- **Prospective clinical trial**: A randomised controlled trial comparing calcipotriol to standard-of-care (cryotherapy) for seborrheic keratosis is needed to elevate evidence from L3 to L1/L2 before any broad clinical adoption
- **Formulation and dosing guidance**: Define optimal concentration (e.g., 0.005% ointment), application frequency, treatment duration, and lesion-type selection criteria (flat vs. raised; facial vs. truncal) for the Danish clinical setting
- **Monitoring plan**: Establish serum calcium monitoring protocol given systemic vitamin D activity risk with extensive topical application
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

