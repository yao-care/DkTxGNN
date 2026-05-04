---
layout: default
title: Brodalumab
parent: 僅模型預測 (L5)
nav_order: 76
evidence_level: L5
indication_count: 10
---

# Brodalumab
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

# Brodalumab: From Plaque Psoriasis to Strongyloidiasis

## One-Sentence Summary

Brodalumab is a fully human monoclonal antibody targeting the interleukin-17 receptor A (IL-17RA), primarily approved for the treatment of moderate-to-severe plaque psoriasis in adults. The TxGNN model assigns its highest prediction score to **Strongyloidiasis** (99.84%), yet **no clinical trials or published literature** currently support this indication. Critically, mechanistic analysis suggests this prediction likely represents a **potential safety hazard rather than a therapeutic opportunity**, as IL-17 signalling plays a protective — not pathological — role in host defence against *Strongyloides stercoralis*.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Moderate-to-severe plaque psoriasis (approved in US and Japan; not registered in Denmark) |
| Predicted New Indication | Strongyloidiasis |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L5 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on published pharmacological literature, Brodalumab is a fully human IgG2 monoclonal antibody that binds with high affinity to IL-17 receptor A (IL-17RA), blocking the signalling of multiple IL-17 family cytokines — including IL-17A, IL-17F, IL-17A/F, IL-17C, and IL-25 (IL-17E). By interrupting this pro-inflammatory cascade, Brodalumab suppresses keratinocyte activation and the downstream inflammatory response characteristic of psoriatic skin disease. The drug is approved for moderate-to-severe plaque psoriasis in the United States (Siliq®) and Japan (Lumicef®), though it is not currently registered in Denmark.

Strongyloidiasis is an intestinal nematode infection caused by *Strongyloides stercoralis*, capable of causing life-threatening hyperinfection syndrome in immunocompromised hosts. **The mechanistic relationship between Brodalumab and Strongyloidiasis runs directly counter to the repurposing hypothesis.** IL-17 cytokines actively promote mucosal anti-parasitic immunity: they drive neutrophil recruitment, enhance IgA secretion, and orchestrate Th17-mediated defence against extracellular pathogens including helminths. Blocking IL-17RA with Brodalumab would be expected to weaken this protective immune response, potentially predisposing patients to primary infection or — more dangerously — to disseminated hyperinfection in those with latent *Strongyloides* carriage.

This counter-mechanistic prediction most likely reflects the TxGNN model capturing indirect network relationships within the knowledge graph — for example, shared inflammatory pathway nodes or comorbidity co-occurrence patterns — rather than a genuine therapeutic signal. In clinical practice, anti-IL-17 therapies (as a class) carry a recognised risk of exacerbating certain infections, and Strongyloides screening prior to initiating immunosuppressive biologics is already recommended in guidelines for patients from endemic regions. **This prediction should be interpreted and documented as a mechanistic safety signal, not a repurposing candidate.**

---

## Clinical Trial Evidence

Currently no clinical trials investigating Brodalumab for Strongyloidiasis have been registered.

---

## Literature Evidence

Currently no related literature on Brodalumab for Strongyloidiasis is available.

---

## Denmark Market Information

Brodalumab currently holds no marketing authorisations in Denmark and has not been assigned a national authorisation number by the Danish Medicines Agency (Laegemiddelstyrelsen). The drug was previously granted a centralised marketing authorisation in the European Union (Kyntheum®, LEO Pharma A/S), but this authorisation was subsequently withdrawn from the European market. For the current regulatory status, consult the Laegemiddelstyrelsen product database or the EMA's European Public Assessment Reports (EPAR) directly.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for detailed safety information.

> **Clinically relevant note for this evaluation:** Detailed warnings and contraindications were not available in this Evidence Pack. However, given that this report concerns the potential repurposing of an IL-17RA-blocking biologic for a parasitic infection, the following drug-class safety considerations are directly relevant: (1) immunosuppressive biologics of this class increase susceptibility to serious infections, including fungal and parasitic infections; (2) prior to initiating IL-17RA–blocking therapy in patients from *Strongyloides*-endemic regions, screening and pre-emptive treatment for strongyloidiasis are advisable per international guidelines; (3) Brodalumab carries a specific black-box warning for suicidal ideation and behaviour, identified in pivotal psoriasis trials. A complete SmPC review is required before any clinical decision.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model's top prediction for Brodalumab is Strongyloidiasis, but mechanistic analysis clearly indicates that IL-17RA blockade is biologically expected to *worsen* rather than treat this parasitic infection. With an evidence level of L5 (model prediction only, zero supporting trials or literature), there is no basis to advance this indication — and the prediction itself warrants documentation as a counter-mechanistic safety concern.

**To proceed productively, the following steps are recommended:**

- **Obtain the Brodalumab SmPC** (from EMA EPAR or the US prescribing information) to complete the S1 safety assessment and populate the key warnings and contraindications fields
- **Confirm MOA data** via DrugBank API (DB11776) to formalise the mechanism-of-action section
- **Reassess the TxGNN model architecture** to understand why a counter-mechanistic prediction receives the highest confidence score — this may indicate a knowledge graph edge that captures comorbidity risk (e.g., patients on biologics have *Strongyloides* risk) rather than a therapeutic edge
- **Prioritise evaluation of the rank-3 prediction — Eye Disease (TxGNN score: 99.82%, Evidence Level: L4)** — which carries a mechanistically plausible IL-17 rationale (IL-17RA expression in corneal epithelium and uveal tissue; existing exploratory data for secukinumab in uveitis) and has at least one indirect observational study and one supporting review article; this represents a more credible repurposing hypothesis that warrants a dedicated evaluation report
- **Consider optic perineuritis and recurrent idiopathic neuroretinitis** (ranks 9–10) as lower-priority exploratory hypotheses, given the theoretical IL-17/Th17 involvement in autoimmune neuro-ophthalmic inflammation, pending literature search confirmation

---

*This report is generated for research reference purposes only. Drug repurposing candidates require clinical validation before any therapeutic application. All content should be reviewed in conjunction with the full SmPC and current clinical guidelines.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

