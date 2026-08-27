---
layout: default
title: Mupirocin
parent: 僅模型預測 (L5)
nav_order: 302
evidence_level: L5
indication_count: 10
---

# Mupirocin
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

# Mupirocin: From Topical Bacterial Skin Infections to Pleural Empyema

## One-Sentence Summary

Mupirocin is a topical antibiotic with established use against Gram-positive bacterial skin infections (including impetigo and MRSA nasal decolonisation), but it currently holds no marketing authorisation in Denmark. The TxGNN model predicts it may be effective against **Pleural Empyema** with a score of **99.49%**; however, **no supporting clinical trials or publications** exist for this repurposing direction, and a fundamental route-of-administration barrier means the current formulation cannot physically reach the pleural cavity. All five unique predicted indications carry a **Hold** recommendation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Denmark; internationally used topically for bacterial skin infections and MRSA nasal decolonisation |
| Predicted New Indication | Pleural Empyema |
| TxGNN Prediction Score | 99.49% |
| Evidence Level | L5 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Mupirocin is a naturally derived pseudomonic acid antibiotic (originally isolated from *Pseudomonas fluorescens*). Its mechanism centres on selective, reversible inhibition of bacterial isoleucyl-tRNA synthetase (IleRS), which blocks incorporation of isoleucine into nascent bacterial proteins and halts protein synthesis. This target is structurally distinct from human IleRS, which largely explains its selective antibacterial activity and topical tolerability. Its spectrum is narrow, covering primarily Gram-positive organisms — notably *Staphylococcus aureus* (including MRSA), coagulase-negative staphylococci, and Streptococcal species.

Pleural empyema is a suppurative infection of the pleural space, and *Staphylococcus aureus* and Streptococcal species are among the most common causative pathogens — precisely the organisms Mupirocin targets. This pathogen-disease overlap in the TxGNN knowledge graph almost certainly drives the high prediction score of 99.49%, as the model recognises a valid biological link between the drug's antibacterial target and the common aetiology of empyema.

However, a critical and currently insurmountable barrier exists: **route incompatibility**. Mupirocin is formulated exclusively as a topical ointment (skin and nasal). No systemic, intravenous, or intrapleural formulation is commercially available or clinically validated. Effective treatment of pleural empyema requires either systemic antibiotics with adequate pleural penetration, or direct intrapleural drainage and instillation — neither of which is achievable with existing Mupirocin preparations. The TxGNN score reflects mechanistic plausibility at the molecular level, not clinical deliverability, and must be interpreted accordingly.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Mupirocin in Pleural Empyema.

---

## Literature Evidence

Currently no related literature available for Mupirocin in Pleural Empyema.

---

## Denmark Market Information

Mupirocin currently holds no marketing authorisations in Denmark — neither via national procedure through the Danish Medicines Agency (Lægemiddelstyrelsen) nor via centralised procedure through the European Medicines Agency (EMA). The product is not commercially available on the Danish market.

---

## Other Predicted Indications — Overview

The evidence pack contains predictions for four additional unique indications. All carry a **Hold** recommendation and are summarised below for completeness:

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Key Concern |
|------|---------------------|-------------|---------------|-------------|
| 1 | Pleural Empyema | 99.49% | L5 | Route incompatibility; topical formulation cannot reach pleural cavity |
| 3 | Punctate Epithelial Keratoconjunctivitis | 99.10% | L5 | Predominantly viral/non-bacterial aetiology; no antiviral activity; ocular safety not established |
| 5 | Neurotrophic Keratopathy | 98.48% | L5 | Non-infectious, neurodegenerative disease; Mupirocin has no neuroprotective or epithelial repair mechanism |
| 7 | Cutaneous Candidiasis | 98.27% | L4 | Fungal target (cell wall/membrane synthase) differs entirely from bacterial IleRS; one 1991 early-phase paper (PMID 1678836) provides weak indirect signal only |
| 9 | Vaginal Discharge | 96.01% | L5 | Only associated trial (NCT07142408) concerns pre-operative MRSA decolonisation, not vaginal infection; likely TxGNN mapping artefact |

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information. No drug-drug interaction data, key warnings, or contraindication data were retrievable for this evidence pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction for Mupirocin in pleural empyema rests on a biologically coherent but clinically non-actionable mechanistic link: the causative pathogens of empyema overlap with Mupirocin's antibacterial spectrum, yet no systemic or intrapleural formulation exists and no clinical or preclinical evidence supports this indication. The same fundamental barrier — route incompatibility or mechanistic mismatch — applies to all five predicted indications. Additionally, the drug is entirely absent from the Danish market, meaning even its established topical indications would require a full regulatory submission before any repurposing programme could proceed.

**To proceed, the following would be needed:**

- **Formulation development**: Demonstration that a systemic, intravenous, or intrapleural formulation of Mupirocin can be developed with acceptable pharmacokinetics, safety, and adequate pleural tissue penetration (currently no such formulation exists)
- **Preclinical evidence**: In vitro MIC data for empyema-relevant Gram-positive pathogens at achievable tissue concentrations, followed by animal model studies for intrapleural efficacy
- **MOA data retrieval**: Resolve data gap DG002 via DrugBank API to formally document the IleRS inhibition mechanism and confirm spectrum of activity
- **Safety data retrieval**: Obtain full SmPC/SPC from the European product label or EMA public assessment report to resolve the blocking data gap DG001 before any safety evaluation can begin
- **Regulatory pathway**: As the drug is not authorised in Denmark, a marketing authorisation application or compassionate use framework would be required before any clinical development programme could be initiated locally

> ⚠️ *This report is for research purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before therapeutic application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

