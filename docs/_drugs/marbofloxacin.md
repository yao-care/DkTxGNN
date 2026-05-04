---
layout: default
title: Marbofloxacin
parent: 僅模型預測 (L5)
nav_order: 222
evidence_level: L5
indication_count: 10
---

# Marbofloxacin
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

# Marbofloxacin: From Bacterial Infections (Veterinary) to Interventricular Septum Aneurysm

## One-Sentence Summary

Marbofloxacin is a fluoroquinolone antibiotic belonging to the same drug class as ciprofloxacin and levofloxacin; it is currently approved exclusively for **veterinary use** (treatment of bacterial infections in dogs, cats, and cattle) and holds no human marketing authorisation in Denmark or the EU.

The TxGNN model assigns its highest prediction score to **Interventricular Septum Aneurysm** (95.37%), followed by pulmonary valve disease, orofacial clefting syndrome, Laubry-Pezzi syndrome, and Pierre Robin syndrome — all structural or developmental conditions.

There is **no clinical trial evidence and no human literature** supporting any of these predicted indications; the sole retrieved publication is a veterinary reptile case report describing marbofloxacin's existing antibacterial use, not a new indication.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Bacterial infections in animals (veterinary use only; no approved human indication) |
| Predicted New Indication (Rank 1) | Interventricular Septum Aneurysm |
| TxGNN Prediction Score | 95.37% |
| Evidence Level | L5 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | **Hold** |

---

## Why Is This Prediction Reasonable?

Marbofloxacin is a third-generation fluoroquinolone antibiotic. Like all fluoroquinolones, its mechanism of action centres on the inhibition of bacterial **DNA gyrase (topoisomerase II) and topoisomerase IV**, enzymes essential for bacterial DNA replication and repair. This antibacterial mechanism has no known biological intersection with the pathogenesis of structural cardiac defects.

Currently, detailed mechanism of action data specific to marbofloxacin's pharmacology in humans is not available in this Evidence Pack. Based on known information, marbofloxacin belongs to the fluoroquinolone class, its antibacterial efficacy in animals has been well established, and there is no mechanistic rationale by which topoisomerase inhibition would treat — or interact with — cardiac structural anomalies such as interventricular septum aneurysm, which arise from embryonic developmental failures or post-infarction myocardial remodelling.

The high TxGNN scores across all top-ranked predictions are most likely attributable to **non-specific co-occurrence of "cardiac disease" nodes within the knowledge graph**, rather than true causal or mechanistic relationships. This is a recognised limitation of graph-based prediction models when drug nodes are sparsely connected: shared neighbourhood nodes inflate predicted scores without reflecting genuine pharmacological plausibility. All five predicted indications (cardiac structural defects and craniofacial developmental syndromes) are mechanistically inconsistent with an antibacterial agent; one prediction (orofacial clefting) carries the additional concern that fluoroquinolones are known to be potentially harmful to developing cartilage during pregnancy.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for any of the predicted indications.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [25831585](https://pubmed.ncbi.nlm.nih.gov/25831585/) | 2015 | Veterinary case report | *Journal of Zoo and Wildlife Medicine* | Argentine boa with bacterial endocarditis (Ochrobactrum intermedium, Pseudomonas putida) and incidental pulmonary valve changes; marbofloxacin used as an **antibacterial** agent — this is a description of the drug's original antibacterial indication in a reptile, not evidence for repurposing in humans |

> **Note:** This sole publication does not constitute evidence for any new human indication. It describes marbofloxacin's established veterinary antibacterial use. It should not be interpreted as supporting the pulmonary valve disease prediction.

---

## Denmark Market Information

Marbofloxacin holds **no marketing authorisation** in Denmark (Lægemiddelstyrelsen) and has no centralised EMA approval for human use. It is registered as a **veterinary medicinal product** in the EU under the European Medicines Agency's veterinary medicines framework.

There are therefore no human product authorisations to list.

---

## Safety Considerations

Detailed human safety data (warnings, contraindications, drug interactions) are not available in this Evidence Pack, as marbofloxacin has no approved human indication.

**Class-level considerations applicable to all fluoroquinolones** (based on established pharmacological class knowledge):

- **Tendon toxicity**: Fluoroquinolones are associated with tendinopathy and tendon rupture, particularly in elderly patients and those on corticosteroids. The EMA has issued class-level warnings for human fluoroquinolones.
- **QT prolongation**: Class-level cardiac risk; risk of torsades de pointes, especially in combination with other QT-prolonging agents.
- **Cartilage and skeletal development toxicity**: Contraindicated in pregnancy and growing children for human fluoroquinolones; animal studies confirm articular cartilage damage.
- **CNS effects**: Seizures, confusion, and peripheral neuropathy are class-level adverse events.
- **Photosensitivity**.

These class-level risks are particularly relevant here because **the top-predicted indications include developmental syndromes (orofacial clefting, Pierre Robin syndrome) in which patients may include pregnant women and neonates** — populations at the highest risk from fluoroquinolone toxicity.

For any human use consideration, a full human safety evaluation (equivalent to a Summary of Product Characteristics) would need to be conducted from first principles.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All ten top-ranked TxGNN predictions for marbofloxacin are structural cardiac defects or craniofacial developmental syndromes, none of which has any established biological connection to the drug's antibacterial mechanism of action. The evidence base is uniformly at Level L5 (model prediction only), with zero clinical trials and zero relevant human literature across all predicted indications. Additionally, marbofloxacin is not approved for human use in Denmark or anywhere in the EU, meaning the regulatory and clinical development pathway would need to begin from Phase 0.

**To proceed, the following would be needed at minimum:**

- **Mechanistic re-evaluation**: Independent biological pathway analysis to identify whether any plausible mechanism — beyond the antibacterial action — could link marbofloxacin to any cardiac or developmental condition; current evidence strongly suggests this is a knowledge-graph artefact.
- **Human safety data**: A complete human pharmacokinetic, toxicological, and safety dossier would be required before any clinical investigation; marbofloxacin has never undergone formal human clinical development.
- **Regulatory pre-consultation**: Given that this is a veterinary-only compound, a pre-submission meeting with the EMA or Lægemiddelstyrelsen would be necessary to determine the feasibility of a human development programme.
- **TxGNN model audit**: The pattern of high scores clustering around unrelated structural/developmental diseases warrants a review of the knowledge graph neighbourhood for the marbofloxacin node to rule out systematic graph artefacts before any further resources are invested.
- **Alternative indication hypothesis generation**: If repurposing of marbofloxacin is a priority, an infection-related indication in human medicine (e.g., resistant Gram-negative infections, community-acquired respiratory infections) would be mechanistically far more defensible and should be evaluated as a primary hypothesis.

---

> ⚠️ **Disclaimer**: This report is generated for research purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before any therapeutic application. All content should be reviewed by qualified healthcare professionals before informing any clinical or regulatory decision.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

