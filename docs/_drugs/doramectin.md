---
layout: default
title: Doramectin
parent: 僅模型預測 (L5)
nav_order: 147
evidence_level: L5
indication_count: 10
---

# Doramectin
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

# Doramectin: From Antiparasitic Agent to Insomnia

## One-Sentence Summary

Doramectin is a macrocyclic lactone antiparasitic agent belonging to the avermectin family, currently approved exclusively for veterinary use with no human marketing authorisations anywhere in the world, including Denmark.
The TxGNN model predicts it may be effective for **Insomnia** with a score of **99.22%** — however, **no clinical trials** and **no publications** currently support this specific direction, placing it at the lowest evidence tier (L5).
A related CNS indication, **Anxiety**, carries the strongest available evidence (L4, 2 preclinical animal studies) and may represent a more credible first step for further investigation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Veterinary antiparasitic (not approved for human use) |
| Predicted New Indication | Insomnia |
| TxGNN Prediction Score | 99.22% |
| Evidence Level | L5 (model prediction only) |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for Doramectin in humans is not available. Doramectin belongs to the avermectin family of macrocyclic lactones and is structurally related to ivermectin. Its established pharmacological basis in veterinary medicine involves disruption of invertebrate neuromuscular signalling through glutamate-gated chloride channels, which are absent in mammals — this is the basis for its selective antiparasitic safety profile in animal hosts.

The proposed link to insomnia rests on a secondary, extrapolated mechanism: Doramectin is hypothesised to act as a positive allosteric modulator of mammalian GABA-A receptors at a binding site distinct from the classical benzodiazepine site. Enhanced GABAergic inhibitory tone could theoretically increase sleep pressure and promote non-REM (NREM) sleep. This reasoning is derived entirely from structural analogy with ivermectin and the TxGNN graph-based computational prediction — no direct preclinical or clinical data in human sleep disorders exists to date.

The closest indication with actual supporting data is **Anxiety** (TxGNN rank 5, score 91.85%). A 2000 rat study (PMID 11246508) directly tested Doramectin using validated anxiety behavioural models (elevated plus-maze, light-dark box) and provided neurochemical evidence of GABAergic modulation. A 2002 parallel study using structurally related ivermectin (PMID 12184502) further supports a potential class effect across avermectins. While this evidence is preclinical only, it provides a more mechanistically grounded foundation than the insomnia prediction.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

> **Note:** No literature is available for the top-ranked indication (Insomnia, L5). The publications below pertain to **Anxiety** (TxGNN rank 5, L4 evidence), which currently represents the strongest available scientific evidence for any CNS repurposing of Doramectin.

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [11246508](https://pubmed.ncbi.nlm.nih.gov/11246508/) | 2000 | Animal Study | Comp Biochem Physiol Toxicol Pharmacol | Doramectin (100–1000 µg/kg SC) produced anxiolytic and anticonvulsant effects in rats using elevated plus-maze and light-dark box paradigms; neurochemical analyses confirmed changes in GABAergic metabolites, providing direct mechanistic support |
| [12184502](https://pubmed.ncbi.nlm.nih.gov/12184502/) | 2002 | Animal Study | Veterinary Research Communications | Structurally related ivermectin demonstrated possible anxiolytic effects in a rat behavioural model; authors explicitly reference prior Doramectin findings, supporting an avermectin class-effect hypothesis for GABAergic modulation |

---

## Denmark Market Information

Doramectin holds no marketing authorisations in Denmark. Neither national (Laegemiddelstyrelsen) nor centralised (EMA) authorisations exist for any human-use formulation. The drug is not registered or marketed for human therapeutic use.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information. No drug–drug interaction data, specific clinical warnings, or human-use contraindications for Doramectin were identified in the current evidence review. Given that the drug has no approved human indication, formal human safety data should be regarded as absent until dedicated first-in-human studies are conducted.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN prediction score for insomnia (99.22%), the evidence base is entirely model-derived (L5) with no clinical trials, no human studies, and no relevant literature — and Doramectin has no approved human indication anywhere globally. Proceeding without foundational safety and pharmacokinetic data in humans would not be scientifically or regulatorily defensible.

**To proceed, the following is needed:**

- **Establish human safety profile:** Commission a formal toxicological review of available veterinary safety data and assess its relevance to human risk; consider a Phase 0/I first-in-human study design
- **Obtain full MOA data:** Query DrugBank API and primary literature to confirm and characterise the GABA-A positive modulation hypothesis in mammalian systems
- **Run dedicated preclinical sleep studies:** Conduct rodent polysomnography (EEG-based sleep staging) with Doramectin specifically to evaluate effects on NREM/REM architecture before advancing to human sleep indications
- **Prioritise Anxiety as lead indication:** Given existing L4 preclinical evidence (PMID 11246508), Anxiety represents a more scientifically tractable entry point than Insomnia; a structured preclinical-to-IND development plan for anxiety should be evaluated first
- **Regulatory consultation:** Engage the Danish Medicines Agency (Laegemiddelstyrelsen) and EMA regarding the regulatory pathway for repurposing a veterinary-only compound into human CNS indications, including requirements for first-in-human approval
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

