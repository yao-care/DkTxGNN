---
layout: default
title: Minoxidil
parent: 僅模型預測 (L5)
nav_order: 238
evidence_level: L5
indication_count: 10
---

# Minoxidil
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

# Minoxidil: From Androgenetic Alopecia to Hypotrichosis Simplex of the Scalp

## One-Sentence Summary

Minoxidil is a potassium channel opener approved in many countries for androgenetic alopecia (pattern hair loss) and, at higher doses, for severe refractory hypertension.
The TxGNN model predicts it may be effective for **Hypotrichosis Simplex of the Scalp**, a rare hereditary hair loss disorder for which no established treatment currently exists,
with **0 clinical trials** and **3 publications** (case series and case reports) currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Androgenetic alopecia; severe hypertension (FDA/EMA approved in other markets; not registered in Denmark) |
| Predicted New Indication | Hypotrichosis Simplex of the Scalp |
| TxGNN Prediction Score | ~99.9999% |
| Evidence Level | L3 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Formal mechanism of action data could not be retrieved from DrugBank for this evidence pack; however, published literature within the pack provides a detailed picture. Minoxidil is a prodrug metabolised in the hair follicle by sulfotransferase (SULT1A1) into minoxidil sulfate, its active form. This active metabolite opens ATP-sensitive potassium (K_ATP) channels in vascular smooth muscle and dermal papilla cells, causing vasodilation and prolongation of the anagen (active growth) phase of the hair cycle. Additionally, minoxidil activates the Wnt/β-catenin signalling pathway, exerts anti-inflammatory effects, and has mild antiandrogenic properties — collectively creating a multi-pathway stimulus for hair follicle survival and growth (PMID 34159872).

Hypotrichosis simplex of the scalp (HSS) is a rare autosomal dominant monogenic disorder caused by mutations in *CDSN*, encoding the desmosomal protein corneodesmosin, which is essential for hair follicle structural integrity. The disease presents in childhood as progressive diffuse thinning, primarily reflecting impaired follicular cycling rather than complete follicular destruction. Because residual functional follicles remain present, minoxidil's anagen-prolonging and dermal papilla-stimulating properties are mechanistically well positioned to address the underlying follicular dysfunction — a direct correspondence that the repurposing rationale from the evidence pack explicitly highlights.

This mechanistic alignment is further validated by direct clinical reports: PMID 35761391 explicitly employs oral minoxidil combined with growth factors to treat hereditary hypotrichosis simplex, and PMID 36651821 reports successful improvement with topical minoxidil 2% combined with platelet-rich plasma in a confirmed HSS patient. Both androgenetic alopecia (minoxidil's established indication) and HSS involve impaired follicular cycling and reduced hair density, making the mechanistic bridge between them strong and biologically coherent.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [35761391](https://pubmed.ncbi.nlm.nih.gov/35761391/) | 2022 | Case Series | Dermatologic Therapy | Oral minoxidil combined with growth factors used to treat hereditary hypotrichosis simplex of the scalp; reports clinical hair density improvement |
| [36651821](https://pubmed.ncbi.nlm.nih.gov/36651821/) | 2023 | Case Report | J Dermatological Treatment | 14-year-old with hereditary HSS treated with combined platelet-rich plasma injections and topical minoxidil 2%; reports successful outcome in a condition otherwise lacking satisfactory treatment |
| [39902296](https://pubmed.ncbi.nlm.nih.gov/39902296/) | 2024 | Case Report | Frontiers in Genetics | Familial HSS (*CDSN* mutation confirmed) in an 8-year-old male treated with botanical extract and minoxidil combination; highlights that definitive effective treatments remain lacking for this condition |

---

## Denmark Market Information

Minoxidil does not hold a marketing authorisation in Denmark. There are no active licenses in the Laegemiddelstyrelsen national registry, and no centralised EMA authorisation covers the Danish market for this drug. Minoxidil is, however, widely authorised across other EU member states and in the United States (FDA OTC approval for 2% and 5% topical solution, 5% foam) for androgenetic alopecia.

Any clinical use in Denmark would require either a named-patient/compassionate use application or a formal marketing authorisation application.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information. No drug-drug interaction data were retrieved in this evidence pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic basis is compelling and the unmet medical need is high — HSS has no approved pharmacological treatment — but the current evidence rests entirely on three case-level reports (evidence level L3) with no registered clinical trials, which is insufficient to support a formal repurposing programme or a regulatory application at this stage.

**To proceed, the following is needed:**
- Retrieval of formal mechanism of action and safety data from DrugBank (currently a data gap)
- Full review of the Laegemiddelstyrelsen / EMA SmPC equivalents for approved minoxidil products in other EU markets, including warnings, contraindications, and paediatric safety data
- Establishment of a prospective registry or pilot study systematically documenting outcomes in HSS patients treated with oral or topical minoxidil, with genetic confirmation of *CDSN* mutation status
- Consultation with Laegemiddelstyrelsen on orphan drug designation potential — HSS qualifies as a rare disease, and this designation could accelerate and incentivise the development pathway
- Assessment of the optimal route of administration (topical vs. low-dose oral) and dosing for a paediatric-onset rare disease population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

