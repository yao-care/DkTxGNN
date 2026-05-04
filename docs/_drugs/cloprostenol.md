---
layout: default
title: Cloprostenol
parent: 僅模型預測 (L5)
nav_order: 119
evidence_level: L5
indication_count: 10
---

# Cloprostenol
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

# Cloprostenol: From Veterinary Prostaglandin Analogue to Rheumatoid Arthritis

---

## One-Sentence Summary

Cloprostenol is a synthetic prostaglandin F2α (PGF2α) analogue currently used exclusively in veterinary medicine — primarily for reproductive management (luteolysis and oestrus synchronisation) in livestock and horses — with no approved human indication in Denmark or elsewhere.
The TxGNN model predicts it may be effective for **Rheumatoid Arthritis (RA)**, based on prostaglandin signalling pathways that intersect with immune regulation in synovial inflammation.
However, this prediction is supported by **0 clinical trials** and **0 publications** specifically linking Cloprostenol to RA in humans, placing it at the lowest evidence tier.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No approved human indication; veterinary use only (reproductive synchronisation in livestock) |
| Predicted New Indication | Rheumatoid Arthritis |
| TxGNN Prediction Score | 97.64% |
| Evidence Level | L5 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Cloprostenol is a selective FP receptor (prostaglandin F2α receptor) agonist. In its established veterinary context, it acts on uterine smooth muscle to cause luteolysis — breakdown of the corpus luteum — enabling controlled reproductive cycling. Its potency and selectivity for FP receptors over other prostanoid receptors is well characterised in animal physiology.

The mechanistic rationale for RA is highly speculative. Prostaglandins play a dual role in inflammatory arthritis: PGE2 (acting via EP receptors) is the dominant pro-inflammatory mediator in RA synovium, driving vasodilation, pain sensitisation, and joint destruction. PGF2α signalling via FP receptors is less studied in human immunology, but there is theoretical evidence that FP receptor activation on certain immune cell populations may modulate Th17 differentiation — a pathway central to RA pathogenesis. This creates a plausible but extremely tenuous pharmacological hypothesis.

Critically, PGF2α analogues also increase smooth muscle contractility and vascular permeability, effects that could worsen the inflammatory microenvironment in RA joints rather than improve it. No preclinical models of RA using FP receptor agonists have been published, and no human data exist. The remaining predicted indications (rare congenital skeletal syndromes, interventricular septum aneurysm, gout) carry even weaker mechanistic justification and likely represent computational noise from knowledge graph pathway co-occurrence rather than biologically meaningful signals.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Cloprostenol in any of the five predicted indications (rheumatoid arthritis, colobomatous microphthalmia-rhizomelic dysplasia syndrome, brachydactyly-syndactyly syndrome, interventricular septum aneurysm, or gout).

---

## Literature Evidence

Currently no related literature available linking Cloprostenol to any of the predicted human indications.

---

## Denmark Market Information

Cloprostenol holds no marketing authorisations in Denmark — neither national authorisations via Lægemiddelstyrelsen nor centralised authorisations via EMA for human use. Veterinary authorisations (e.g., Estrumate® for cattle/horses) exist in several EU member states but fall outside the scope of human drug repurposing evaluation.

---

## Safety Considerations

No approved human SmPC exists for Cloprostenol in Denmark. The following general considerations apply based on the drug class:

- **Drug Interactions**: No human drug-drug interaction data identified in the evidence pack query.
- **General Class Warning**: As a prostaglandin F2α analogue, Cloprostenol carries well-established risks in veterinary use including bronchospasm, hypotension, uterine hyperstimulation, and vascular effects. Extrapolation to human safety profiles requires dedicated clinical assessment.

Please refer to the veterinary Summary of Product Characteristics (SmPC) for pharmacological safety data, and note that formal human safety assessment (TFDA/EMA SmPC equivalent) is entirely absent and must be generated before any clinical investigation.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate is at evidence level L5 — the TxGNN model prediction is the sole basis for the RA indication, with zero supporting clinical trials, zero supporting literature, no approved human use anywhere globally, no human safety data, and no mechanism of action documentation in the evidence pack. The theoretical FP receptor → immune modulation link in RA is highly speculative and is pharmacologically counterbalanced by known pro-inflammatory effects of PGF2α analogues (increased vascular permeability, smooth muscle contraction). The four other predicted indications (two rare congenital syndromes, interventricular septum aneurysm, gout) all carry even weaker mechanistic rationale and are most likely knowledge graph artefacts.

**To proceed, the following is needed:**

- **Mechanism of action documentation**: Retrieve full DrugBank entry for DB11507 including receptor binding profile, pharmacodynamics, and any human pharmacology data
- **Preclinical literature search**: Systematic PubMed/EMBASE search for Cloprostenol OR "prostaglandin F2α analogue" AND (rheumatoid arthritis OR synovitis OR Th17) to confirm evidence gap
- **Human safety baseline**: Identify any human exposure data (case reports, occupational exposure studies) to characterise basic human tolerability
- **FP receptor biology review**: Assess whether FP receptor agonism in human immune cells has any supporting preclinical evidence for anti-inflammatory activity in arthritis models
- **Regulatory pathway clarification**: Determine whether a veterinary-to-human development pathway is feasible, given the drug has no existing human regulatory history in the EU
- **Decision gate**: Only reassess for "Proceed with Guardrails" if at least one peer-reviewed preclinical study in a relevant arthritis model emerges from the above review

> ⚠️ **Research Disclaimer**: This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before any therapeutic application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

