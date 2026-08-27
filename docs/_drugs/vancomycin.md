---
layout: default
title: Vancomycin
parent: 僅模型預測 (L5)
nav_order: 464
evidence_level: L5
indication_count: 10
---

# Vancomycin
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

# Vancomycin: From Gram-Positive Bacterial Infections to Diffuse Scleroderma

## One-Sentence Summary

Vancomycin is a glycopeptide antibiotic used clinically for serious Gram-positive infections (e.g. MRSA, *C. difficile*). The TxGNN model predicts a possible link to **Diffuse Scleroderma**, but this direction is currently supported by **0 clinical trials** and only **1 case report**, and the case report itself describes a suspected *adverse drug reaction*, not a therapeutic effect.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Gram-positive bacterial infections (inferred from drug class; no Denmark-specific approved indication text on file) |
| Predicted New Indication | Diffuse Scleroderma |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for this candidate is not available in the evidence pack (MOA field flagged as a blocking data gap). Based on general pharmacological knowledge captured in the evidence pack's own rationale, vancomycin acts by inhibiting D-Ala-D-Ala cell-wall synthesis in Gram-positive bacteria — a mechanism with no known relevance to diffuse scleroderma, which is an autoimmune fibrotic disease driven by fibroblast activation, TGF-β signalling, and microvascular injury.

The only supporting literature (PMID 31541072) is a 2019 case report of a patient with an exfoliative rash and eosinophilia following antibiotic therapy — this describes a *suspected adverse cutaneous drug reaction*, not a therapeutic benefit in scleroderma. There is no clinical trial evidence, no preclinical mechanistic study, and no established pharmacological rationale connecting an antibacterial cell-wall inhibitor to an autoimmune fibrotic disease.

Given this, the high TxGNN score most likely reflects sparse or confounded associations in the underlying knowledge graph rather than a genuine repurposing signal. The same pattern holds across the other candidates in this batch (paratyphoid fever, salmonellosis) — both are caused by Gram-negative organisms that vancomycin cannot penetrate, making those predictions mechanistically implausible as well.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31541072](https://pubmed.ncbi.nlm.nih.gov/31541072/) | 2019 | Case Report | The American Journal of Case Reports | Describes a patient with diffuse exfoliative rash, sepsis, and eosinophilia following antibiotic treatment (including agents in the vancomycin drug class) — a suspected adverse drug reaction, not evidence of therapeutic use in scleroderma |

## Denmark Market Information

Vancomycin is not currently marketed in Denmark under this evidence pack, and no marketing authorisation records are on file (0 licenses).

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information. No drug interaction records were found in the queried database.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high, but there is no mechanistic rationale, no clinical trial evidence, and the single literature reference actually describes a drug-associated skin reaction rather than a treatment effect. Evidence level L5 (model prediction only) does not support advancing this candidate.

**To proceed, the following is needed:**
- Confirmed mechanism-of-action data for vancomycin (currently a blocking data gap, DG002)
- TFDA/SmPC warnings and contraindications (currently a blocking data gap, DG001) before any safety pre-screening (S1) can begin
- Preclinical or mechanistic studies specifically linking glycopeptide antibiotics to fibrotic/autoimmune pathways, if this candidate is to be reconsidered
- Independent re-review of the TxGNN signal, given that the top 10 ranked candidates for this drug (including paratyphoid fever and salmonellosis, both Gram-negative indications) show the same pattern of high score paired with implausible mechanism
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

