---
layout: default
title: Moxidectin
parent: 僅模型預測 (L5)
nav_order: 245
evidence_level: L5
indication_count: 10
---

# Moxidectin
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

# Moxidectin: From Onchocerciasis to Polyclonal Hyperviscosity Syndrome

## One-Sentence Summary

Moxidectin is a second-generation macrocyclic lactone antiparasitic agent, approved internationally (FDA 2018, EMA) for the treatment of onchocerciasis (river blindness), but not currently authorised in Denmark.
The TxGNN model predicts it may be effective for **Polyclonal Hyperviscosity Syndrome** as the top-ranked candidate, with **0 clinical trials** and **0 publications** currently supporting this direction.
All five unique predicted indications across the full prediction list sit at Evidence Level **L5** — computational model output only — and the overall recommendation for each is **Hold**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Onchocerciasis (river blindness) — based on established FDA/EMA approvals; no Danish authorisation on record |
| Predicted New Indication | Polyclonal Hyperviscosity Syndrome |
| TxGNN Prediction Score | 98.06% |
| Evidence Level | L5 (model prediction only — no clinical trials, observational studies, or literature identified) |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on established pharmacological knowledge, Moxidectin is a macrocyclic lactone (milbemycin subclass) antiparasitic that works by selectively potentiating glutamate-gated chloride (GluCl) ion channels found exclusively in invertebrate nerve and muscle tissue. This causes sustained hyperpolarisation and paralysis of the parasite (*Onchocerca volvulus*), leading to its death. Because mammalian nervous tissue lacks GluCl channels, the drug has a favourable therapeutic index in humans.

Polyclonal hyperviscosity syndrome is driven by pathological overproduction of polyclonal immunoglobulins (IgG, IgA, or IgM) from abnormally proliferating plasma cells or B-lymphocytes, resulting in markedly elevated serum viscosity. The core pathological pathway — B-cell receptor signalling, immunoglobulin class-switching, and plasma-cell differentiation — has no established intersection with GluCl channel pharmacology. Some macrocyclic lactones, including the closely related ivermectin, have been noted to exert non-specific immunomodulatory effects in observational contexts, but no mechanistic basis connecting Moxidectin to immunoglobulin regulation or B-cell biology has been described in peer-reviewed literature.

The high TxGNN score is most likely attributable to multi-hop graph traversal noise in the knowledge graph — for example, a connection path such as Moxidectin → chloride channel → neuroinflammation → IL pathway → B-cell activation → hyperviscosity — rather than a direct pharmacological relationship. This type of distant-node artefact is a recognised limitation of graph neural network predictions, particularly when intermediate disease nodes with high connectivity act as inadvertent bridges.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Denmark Market Information

Moxidectin currently holds **no marketing authorisations in Denmark**. Neither a national authorisation through the Danish Medicines Agency (Lægemiddelstyrelsen) nor a centralised EMA authorisation with Danish coverage has been identified in this evidence pack (data cut-off: 2026-04-04). The drug is commercially available in other jurisdictions (e.g., Moxidectin 8 mg tablets under the brand name *Moxi* in the USA; *Mavenclad*-class EMA approval is a separate compound) but has not obtained market access in Denmark.

Any clinical use in Denmark would currently require either a named-patient/compassionate-use application or a full new marketing authorisation application via the EMA centralised procedure or a national procedure with Lægemiddelstyrelsen.

---

## All Unique TxGNN Predicted Indications — Overview

The following table summarises all five unique indications predicted by the TxGNN model. All carry evidence Level L5 and a **Hold** recommendation.

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Mechanistic Plausibility Assessment | Decision |
|------|---------------------|-------------|----------------|--------------------------------------|----------|
| 1 | Polyclonal Hyperviscosity Syndrome | 98.06% | L5 | Very low — GluCl channel modulation has no known intersection with immunoglobulin synthesis or B-cell signalling | Hold |
| 2 | Hyperamylasemia | 98.06% | L5 | Very low — secondary biochemical marker (not a primary disease entity); pancreatic acinar injury mechanism unrelated to GluCl pharmacology | Hold |
| 3 | Congenital Analbuminemia | 97.90% | L5 | Very low — ultra-rare genetic disorder (ALB mutation, <100 cases globally); Moxidectin has no known effect on albumin gene expression or hepatic synthesis | Hold |
| 4 | Staphylococcal Scalded Skin Syndrome (SSSS) | 97.83% | L5 | Weak — distant analogy to ivermectin's limited antimicrobial literature; no direct in vitro or in vivo data for Moxidectin against *S. aureus* or exfoliative toxins; most exploratory of the five | Hold |
| 5 | Variola Minor Infection | 97.78% | L5 | Not applicable — causative pathogen (Variola virus) eradicated globally since 1980; natural infection impossible; clinical investigation ethically and practically not feasible | Hold |

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) — FDA prescribing information or EMA product information — for full safety information, including warnings, precautions, and contraindications.

> **Note for Danish prescribers:** No Danish SmPC is available as Moxidectin is not authorised in Denmark. The FDA-approved label (2018) and any EMA assessment reports are the appropriate reference documents. Key warnings in the approved label include neurological adverse events (dizziness, somnolence, tremor) and the risk of post-treatment reactions in patients with high *Onchocerca volvulus* microfilarial burden (Mazzotti-like reactions).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All five TxGNN-predicted indications are at the lowest evidence tier (L5 — computational signal only), with zero supporting clinical trials, observational studies, or peer-reviewed publications identified across all data sources queried (ClinicalTrials.gov, ICTRP, PubMed). The mechanistic links between Moxidectin's established GluCl channel pharmacology and the predicted disease areas are either absent (polyclonal hyperviscosity, hyperamylasemia, congenital analbuminemia, variola minor) or at best weakly theoretical (staphylococcal scalded skin syndrome). Moxidectin is additionally not authorised in Denmark, adding a substantial regulatory barrier to any clinical application.

**To proceed, the following is needed:**

- **MOA confirmation:** Retrieve full mechanistic profile from DrugBank (DB11431) to enable formal mechanism-to-indication mapping
- **SmPC safety review:** Download and parse the FDA prescribing information and EMA scientific discussion documents to populate warnings, contraindications, and drug interaction data (currently all flagged as data gaps)
- **Preclinical feasibility assessment:** For Staphylococcal Scalded Skin Syndrome specifically — the only indication with a weak theoretical basis — commission targeted in vitro antimicrobial activity studies for Moxidectin against *S. aureus* and exfoliative toxin ET-A/ET-B inhibition before any further investment
- **KG audit:** Review the knowledge graph edge paths generating these predictions to identify and filter multi-hop noise artefacts; the duplicate ranking pattern (ranks 1&4, 2&3, 5&6, 7&8, 9&10 identical) suggests a systematic scoring artefact requiring technical review
- **Regulatory pathway mapping:** If any indication advances to preclinical stage, initiate a regulatory pre-submission meeting with Lægemiddelstyrelsen or EMA to define the authorisation pathway for Denmark
- **Variola minor:** Remove from active consideration — clinical investigation is not feasible for an eradicated pathogen; retain only for historical documentation

---

*This report is generated for research purposes only and does not constitute medical advice. All repurposing candidates require rigorous clinical validation before any therapeutic application. Report generated: 2026-04-04. Evidence cut-off: 2026-04-04.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

