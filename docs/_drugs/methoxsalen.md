---
layout: default
title: Methoxsalen
parent: 僅模型預測 (L5)
nav_order: 230
evidence_level: L5
indication_count: 10
---

# Methoxsalen
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

# Methoxsalen: From Psoriasis/Vitiligo (PUVA Therapy) to Localized Pagetoid Reticulosis

## One-Sentence Summary

Methoxsalen is a psoralen photosensitiser used globally in PUVA (Psoralen + UVA) photochemotherapy, with established indications including psoriasis, vitiligo, and cutaneous T-cell lymphoma (CTCL)/mycosis fungoides — though it holds no current marketing authorisation in Denmark.
The TxGNN model predicts it may be effective for **Localized Pagetoid Reticulosis**, a rare indolent CTCL subtype, with a prediction score of **99.97%**, but **no clinical trials** and **no direct publications** are currently available for this specific indication.
The mechanistic rationale is nonetheless biologically coherent: pagetoid reticulosis belongs to the same CTCL disease spectrum for which PUVA therapy is already a guideline-endorsed treatment option.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Psoriasis, vitiligo, mycosis fungoides/CTCL (PUVA therapy) — established globally; not registered in Denmark |
| Predicted New Indication | Localized Pagetoid Reticulosis |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L4 (mechanistic inference; no direct clinical trials or literature for this subtype) |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on established pharmacological knowledge, Methoxsalen is a naturally occurring furocoumarin (psoralen) that acts as a photoactivatable DNA-crosslinking agent. When administered orally or topically and combined with UVA irradiation, methoxsalen intercalates between DNA base pairs and — upon UVA activation — forms covalent monofunctional and bifunctional adducts that cross-link complementary DNA strands. This blocks DNA replication and triggers apoptosis preferentially in rapidly proliferating cells. In the extracorporeal photopheresis (ECP) setting, methoxsalen-treated leucocytes reinfused after UVA irradiation additionally stimulate tolerogenic dendritic cell differentiation, modulating the tumour immune microenvironment.

Localized pagetoid reticulosis (Woringer-Kolopp disease) is a rare, indolent variant of CTCL characterised by a solitary, slowly expanding plaque with striking intraepidermal infiltration by neoplastic CD4+ or CD8+ T-cells. Taxonomically, it resides on the same CTCL spectrum as mycosis fungoides (MF), for which PUVA therapy is a recognised first-line or standard option in early-stage disease per EORTC consensus guidelines. The localised, superficial nature of pagetoid reticulosis lesions makes them especially well-suited to targeted PUVA or bath-PUVA delivery, and the mechanistic extrapolation from MF to this subtype is biologically sound.

It is important to note that the TxGNN prediction for this specific subtype is driven by mechanistic and knowledge-graph proximity reasoning rather than direct clinical evidence. No clinical trials or publications specifically studying methoxsalen in localised pagetoid reticulosis were identified in this Evidence Pack. The L4 designation reflects mechanistic plausibility without empirical validation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered specifically for Methoxsalen in localised pagetoid reticulosis.

---

## Literature Evidence

Currently no related literature available specifically for Methoxsalen in localised pagetoid reticulosis.

> **Note — Supporting Evidence for Related Indication:** For the closely related indication of **indolent primary cutaneous T-cell lymphoma** (TxGNN rank 3, score 99.91%, Evidence Level L3), 2 relevant publications were identified. These provide indirect mechanistic and clinical support for the use of methoxsalen-based photopheresis across the CTCL spectrum:

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [12118838](https://pubmed.ncbi.nlm.nih.gov/12118838/) | 2000 | Retrospective cohort / Case series | Int J Artif Organs | Five-year experience with extracorporeal photopheresis (ECP) in CTCL, including mycosis fungoides; supports ECP efficacy in indolent CTCL with acceptable safety profile |
| [23074497](https://pubmed.ncbi.nlm.nih.gov/23074497/) | 2006 | Evidence-based review / Systematic analysis | Ontario Health Technol Assess Ser | Systematic evidence analysis of ECP effectiveness, safety, and cost-effectiveness for refractory erythrodermic CTCL and chronic graft-versus-host disease; supports clinical utility in refractory CTCL |

---

## Denmark Market Information

Methoxsalen currently holds **no marketing authorisation** with the Danish Medicines Agency (Lægemiddelstyrelsen) and is not available as a marketed product in Denmark. There are no national or centralised (EMA) authorisations on record. Healthcare professionals wishing to access this medicine for clinical use would need to pursue a named-patient authorisation (særlig tilladelse) or a compassionate-use/hospital exemption pathway via Lægemiddelstyrelsen.

---

## Cytotoxicity

Methoxsalen is used in oncological and dermatological settings as a photochemotherapy agent (PUVA) and as a photosensitiser in extracorporeal photopheresis (ECP) for CTCL. Although not classified as a conventional cytotoxic chemotherapy agent, its antineoplastic mechanism (DNA cross-linking in malignant T-cells) and application in malignant conditions warrant specific safety guidance.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Photochemotherapy agent / Photosensitiser (Psoralen class); not a conventional cytotoxic; antineoplastic action is light-dependent |
| Myelosuppression Risk | Low for PUVA therapy; ECP may cause mild, transient leucocyte fluctuations due to the apheresis procedure itself |
| Emetogenicity Classification | Low (oral methoxsalen may cause nausea/GI upset; generally manageable) |
| Monitoring Items | Ophthalmological monitoring (UV-protective eyewear required for at least 24 hours post-oral dose to prevent cataract risk); skin surveillance for photodamage and secondary squamous cell carcinoma with long-term PUVA; liver function tests (hepatotoxicity reported with chronic use) |
| Handling Protection | Standard precautions for handling; UVA source safety protocols required for clinical staff during phototherapy; for ECP procedures, standard apheresis laboratory precautions apply |

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) — available via EMA or the originator's country of registration — for complete safety information. No drug interaction, key warning, or contraindication data was available in this Evidence Pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN prediction score (99.97%) and a biologically coherent mechanistic link — pagetoid reticulosis is a CTCL subtype and methoxsalen/PUVA therapy is already guideline-endorsed for the CTCL spectrum — there is currently no direct clinical trial or publication evidence for this specific rare subtype, and methoxsalen is not registered in Denmark. An L4 evidence level (mechanistic inference only) is insufficient to support clinical application without further validation.

**To proceed, the following is needed:**

- Targeted systematic literature review for pagetoid reticulosis treatment outcomes with PUVA, bath-PUVA, or methoxsalen-based ECP (given the rarity of the condition, high-quality case series and expert consensus may be the most realistic evidence level available)
- Retrieval and review of methoxsalen's full SmPC/prescribing information from an authorised country (e.g., United States — Oxsoralen-Ultra; or EMA if a centralised authorisation exists) to assess safety, contraindications, and drug interactions
- Clarification of complete MOA data via DrugBank API (listed as a known data gap)
- Regulatory pathway consultation with Lægemiddelstyrelsen for named-patient access if clinical use is being considered
- Dermatology and clinical oncology expert input on whether localised PUVA is a feasible and accepted management strategy for pagetoid reticulosis within Danish clinical practice
- Review of the broader predicted indication landscape: the related indication of **indolent primary cutaneous T-cell lymphoma** (rank 3, L3 evidence, "Proceed with Guardrails") has supporting literature and may represent a more actionable near-term repurposing target
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

