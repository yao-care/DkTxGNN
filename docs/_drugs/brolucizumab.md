---
layout: default
title: Brolucizumab
parent: 僅模型預測 (L5)
nav_order: 77
evidence_level: L5
indication_count: 8
---

# Brolucizumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

# Brolucizumab: From Neovascular Age-Related Macular Degeneration to Mitochondrial Oxidative Phosphorylation Disorder Due to Nuclear DNA Anomalies

---

## One-Sentence Summary

Brolucizumab (Beovu) is a humanised anti-VEGF-A single-chain antibody fragment (scFv) approved for intravitreal treatment of neovascular (wet) age-related macular degeneration (nAMD) and diabetic macular edema (DME).
The TxGNN model predicts it may be effective for **Mitochondrial Oxidative Phosphorylation Disorder Due to Nuclear DNA Anomalies**,
with **0 clinical trials** and **0 publications** currently supporting this direction — making it a model-only prediction that should be interpreted with caution.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Neovascular (wet) age-related macular degeneration (nAMD); diabetic macular edema (DME) |
| Predicted New Indication | Mitochondrial oxidative phosphorylation disorder due to nuclear DNA anomalies |
| TxGNN Prediction Score | 99.67% |
| Evidence Level | L5 |
| Denmark Market Status | Not marketed in Denmark |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Brolucizumab is a humanised single-chain antibody fragment (scFv) that selectively binds and neutralises VEGF-A, thereby suppressing pathological neovascularisation and vascular permeability in the retina. It is delivered as a 6 mg intravitreal injection and has no established systemic formulation. Detailed pharmacological MOA data was not retrieved by the automated pipeline; however, the drug's anti-VEGF-A mechanism is well established in the ophthalmological literature and is reflected in the repurposing rationale data included in this Evidence Pack.

Mitochondrial oxidative phosphorylation (OXPHOS) disorders due to nuclear DNA anomalies are rare inherited metabolic diseases caused by loss-of-function mutations in nuclear-encoded genes that support the mitochondrial electron transport chain. VEGF signalling does interact with the PGC-1α transcriptional axis — which regulates mitochondrial biogenesis — and VEGF has been shown in some cell models to help maintain mitochondrial membrane potential. These connections form the graph-theoretical basis for the TxGNN prediction.

However, **the mechanistic direction is likely inverse or absent in a therapeutic context.** Inhibiting VEGF-A (brolucizumab's mechanism) could theoretically impair, rather than restore, mitochondrial function. More fundamentally, nuclear DNA-driven OXPHOS disorders are caused by irreversible genetic defects, not by aberrant angiogenesis — the primary pathological process that anti-VEGF agents address. The high TxGNN score most plausibly reflects topological proximity between mitochondrial biogenesis, vascular, and immune-related nodes in the knowledge graph, rather than a genuine therapeutic opportunity. This prediction is considered a likely false positive and should not be advanced without compelling preclinical mechanistic evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Denmark Market Information

Brolucizumab currently holds **no marketing authorisations in Denmark**. No products have been registered through the Danish Medicines Agency (Lægemiddelstyrelsen), and no centralised EMA authorisations are recorded for the Danish market as of the data cut-off date (2026-04-04).

> **Note for clinicians:** Brolucizumab (Beovu) has received EMA centralised approval for nAMD and DME in the EU. Its absence from the Danish market listing may reflect a commercial decision or post-approval safety review (Beovu was subject to an EMA safety assessment concerning intraocular inflammation and retinal vasculitis post-launch). The current authorisation status should be verified directly with Lægemiddelstyrelsen before any clinical planning.

---

## Safety Considerations

Safety data — including key warnings, contraindications, and drug–drug interactions — were not retrieved by the automated pipeline for this candidate.

Please refer to the approved Summary of Product Characteristics (SmPC) for full safety information.

> **Prescriber alert:** Brolucizumab has been associated with serious ocular adverse events including intraocular inflammation, retinal vasculitis, and retinal vascular occlusion in post-marketing experience. These risks are relevant even in the context of exploratory repurposing discussions, particularly if any systemic administration route were to be considered.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is zero clinical or published scientific evidence supporting the use of brolucizumab in mitochondrial OXPHOS disorders, and the mechanistic rationale is directionally unfavourable — VEGF-A inhibition is unlikely to correct a genetically determined defect in the electron transport chain and could theoretically worsen mitochondrial integrity. The drug is also not authorised in Denmark.

**To proceed, the following is needed:**

- **Mechanistic validation:** A formal preclinical assessment (in vitro or animal model) is required to determine whether any aspect of VEGF-A blockade could plausibly benefit OXPHOS function in nuclear DNA-variant disease models, before any human investigation is considered
- **Route-of-administration feasibility:** Brolucizumab is exclusively formulated for intravitreal injection; treating a systemic metabolic disease would require a completely new drug formulation and full pharmacokinetic/pharmacodynamic characterisation
- **Safety dossier completion:** Retrieve the full SmPC (including systemic exposure data after intravitreal injection, teratogenicity, and known contraindications) to enable a proper safety risk assessment
- **Drug–drug interaction data:** Currently no DDI data is available; this must be obtained before any clinical programme is designed
- **Regulatory pathway assessment:** As brolucizumab is not currently authorised in Denmark, any clinical programme would require either a new marketing authorisation application or a clinical trial authorisation (CTA) from Lægemiddelstyrelsen / EMA
- **Alternative candidates review:** Given the weak mechanistic basis for this specific pairing, it is recommended to evaluate whether other VEGF-pathway modulators with systemic exposure data (e.g., bevacizumab, aflibercept) have any emerging evidence in mitochondrial disease before investing further in brolucizumab for this indication

---

*This report is generated for research purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before use. Report version: v4 | Data cut-off: 2026-04-04 | Candidate ID: TW-DB14864-multi*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

