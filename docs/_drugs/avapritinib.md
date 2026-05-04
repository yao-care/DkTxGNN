---
layout: default
title: Avapritinib
parent: 僅模型預測 (L5)
nav_order: 51
evidence_level: L5
indication_count: 10
---

# Avapritinib
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

# Avapritinib: From GIST / Systemic Mastocytosis to Axial Spondylometaphyseal Dysplasia

## One-Sentence Summary

Avapritinib (Ayvakit) is a selective KIT and PDGFRA kinase inhibitor approved internationally for unresectable or metastatic gastrointestinal stromal tumours (GIST) harbouring PDGFRA exon 18 mutations, and for advanced systemic mastocytosis — it is, however, not registered in Denmark.
The TxGNN model predicts it may be effective for **Axial Spondylometaphyseal Dysplasia** with a score of 99.92%, yet **no supporting clinical trials or published literature** exist for this direction.
Across all five unique predicted indications in this Evidence Pack, the evidence level is uniformly **L5 (model prediction only)** and the recommendation is **Hold** for every candidate.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Denmark; globally approved for PDGFRA exon 18-mutant GIST and advanced systemic mastocytosis |
| Predicted New Indication | Axial Spondylometaphyseal Dysplasia |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this Evidence Pack. Based on published scientific literature, Avapritinib is a highly selective inhibitor of KIT (exon 17/18 mutations) and PDGFRA (D842V mutation) — two constitutively activated receptor tyrosine kinases that drive tumour growth in GIST and mast cell proliferation in systemic mastocytosis. Its antineoplastic activity is thus tightly coupled to inhibiting aberrant KIT/PDGFRA signalling in oncological contexts.

Axial spondylometaphyseal dysplasia, however, is a rare skeletal dysplasia caused by loss-of-function mutations in the *PAPSS2* gene, which encodes an enzyme essential for sulphation of cartilage proteoglycans. The underlying disease mechanism — defective sulphate metabolism leading to skeletal malformation — has no known intersection with KIT or PDGFRA signalling pathways. There is no established biological rationale connecting Avapritinib's pharmacological targets to bone morphogenesis or sulphate metabolism.

The high TxGNN prediction score (99.92%) most likely reflects structural patterns or indirect node adjacencies within the knowledge graph rather than a genuine biological relationship. This concern applies equally to all five unique predicted indications in this Evidence Pack: none presents a plausible mechanistic connection to Avapritinib's known pharmacology. Of all candidates, amyotrophic lateral sclerosis (ALS, rank 3) carries the weakest-but-least-implausible rationale — KIT is expressed on mast cells implicated in ALS neuroinflammation, and PDGFRA is expressed on oligodendrocyte precursor cells with potential neuroprotective roles — but even this link is indirect, speculative, and entirely unvalidated at the drug level.

---

## All Predicted Indications — Top 5 Unique Diseases

| Rank | Disease | TxGNN Score | Evidence Level | Decision | Mechanistic Assessment |
|------|---------|-------------|----------------|----------|------------------------|
| 1 | Axial Spondylometaphyseal Dysplasia | 99.92% | L5 | Hold | *PAPSS2* mutation (sulphation defect) — no known KIT/PDGFRA link |
| 2 | Bilateral Parasagittal Parieto-Occipital Polymicrogyria | 99.92% | L5 | Hold | Cortical structural malformation (*ADGRG1*/GPR56) — no drug-amenable window |
| 3 | Amyotrophic Lateral Sclerosis (ALS) | 99.92% | L5 | Hold | Indirect mast cell / PDGFRA-OPC link — speculative, no clinical validation |
| 4 | Trichomegaly–Retinal Pigmentary Degeneration–Dwarfism Syndrome | 99.92% | L5 | Hold | *PNPLA6* mutation (phospholipid metabolism) — no KIT/PDGFRA link; extremely rare |
| 5 | ALS, Susceptibility To | 99.91% | L5 | Hold | Shares ALS rationale; preventive use in presymptomatic carriers adds ethical complexity |

---

## Clinical Trial Evidence

Currently no related clinical trials are registered for any of the predicted indications.

---

## Literature Evidence

Currently no related literature is available for any of the predicted indications.

---

## Denmark Market Information

Avapritinib is currently not marketed in Denmark. No national (Lægemiddelstyrelsen) or centralised marketing authorisations are recorded in this dataset.

> **Note for clinicians:** Avapritinib (Ayvakit) holds a European Medicines Agency (EMA) centralised marketing authorisation (EU/1/20/1515) for PDGFRA exon 18-mutant unresectable or metastatic GIST and for advanced systemic mastocytosis. Commercial availability in Denmark should be confirmed with the relevant pharmaceutical supplier. Any use outside a registered indication would require application through named-patient supply, compassionate use, or an approved clinical trial framework.

---

## Cytotoxicity

Avapritinib qualifies as an antineoplastic agent (KIT/PDGFRA-targeted oral kinase inhibitor). The following classification applies:

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — selective KIT/PDGFRA tyrosine kinase inhibitor (not conventional cytotoxic) |
| Myelosuppression Risk | Moderate — anaemia, thrombocytopenia, and neutropenia have been reported in clinical trials for the approved indications |
| Emetogenicity Classification | Low to moderate (oral targeted agent) |
| Monitoring Items | Full blood count (FBC) with differential, liver function, renal function, coagulation; particular vigilance for intracranial haemorrhage, cognitive changes, and neuropsychiatric symptoms (class-specific risk) |
| Handling Protection | Classified as a hazardous antineoplastic agent; standard precautions for oral hazardous drug handling apply per institutional cytotoxic handling protocols (NIOSH/ESOP guidelines) |

---

## Safety Considerations

Detailed safety data (key warnings, contraindications, and drug-drug interactions) is not available in this Evidence Pack.

> Please refer to the approved Summary of Product Characteristics (SmPC) for Ayvakit for complete safety information, including warnings regarding intracranial haemorrhage, cognitive impairment, photosensitivity, and embryo-foetal toxicity.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All predicted indications are rated at evidence level L5 — the TxGNN model generated these predictions solely from knowledge graph structure, with zero supporting clinical trials or peer-reviewed literature. The mechanistic links between Avapritinib's pharmacology (KIT/PDGFRA inhibition) and every predicted disease are either absent or highly indirect; the uniformly high prediction scores across structurally unrelated rare diseases strongly suggest knowledge-graph topology artefacts rather than genuine biological signal.

**To proceed, the following is needed:**

- **Retrieve MOA and safety data**: Query DrugBank API and download the Ayvakit SmPC to fill the two blocking data gaps (DG001, DG002) before any further evaluation is meaningful
- **For ALS (the most mechanistically explorable candidate)**: Conduct a systematic literature review of KIT inhibition in neuroinflammatory ALS models and PDGFRA inhibition in oligodendrocyte precursor cell biology before assessing feasibility — this is a prerequisite, not a clinical readiness criterion
- **Deprioritise structural malformation indications**: Axial spondylometaphyseal dysplasia (rank 1) and bilateral polymicrogyria (rank 2) represent fixed structural anomalies with no pharmacologically accessible intervention window; these should be removed from further consideration
- **Deprioritise Oliver-McFarlane syndrome** (rank 4): Mechanistically unrelated, extremely rare globally (fewer than 50 reported cases), making clinical trial design infeasible
- **Confirm Denmark availability**: Verify current commercial availability of Ayvakit via the EMA-authorised centralised route, as the authorisation exists but local market entry status requires clarification
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

