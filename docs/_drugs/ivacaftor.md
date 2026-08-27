---
layout: default
title: Ivacaftor
parent: 僅模型預測 (L5)
nav_order: 248
evidence_level: L5
indication_count: 10
---

# Ivacaftor
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

# Ivacaftor: From Cystic Fibrosis to Rheumatoid Arthritis

## One-Sentence Summary

> Ivacaftor is a CFTR potentiator whose proven use is in cystic fibrosis (CF), based on the mechanistic context described in this evidence pack.
> The TxGNN model predicts possible relevance to **Rheumatoid Arthritis**, with a prediction score of **96.97%**,
> but this is currently supported by only **1 indirect clinical trial** and **1 preclinical/basic-research publication** — neither of which studied RA directly.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Cystic Fibrosis (CFTR potentiator; not derived from a Danish marketing authorisation, as none is on file) |
| Predicted New Indication | Rheumatoid Arthritis |
| TxGNN Prediction Score | 96.97% |
| Evidence Level | L4 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on the information that is available, Ivacaftor is a CFTR (cystic fibrosis transmembrane conductance regulator) potentiator, and its efficacy in cystic fibrosis is well established in the broader literature referenced here.

The repurposing rationale in this pack describes a possible indirect link: in CF research, Ivacaftor has been observed to modulate neutrophil function and reduce inflammation (for example, decreased pancreatic ductal epithelial inflammation). Rheumatoid arthritis is an autoimmune, neutrophil-mediated joint inflammatory disease, so there is a theoretical connection via a CFTR–neutrophil–inflammation axis.

However, no direct evidence currently shows that CFTR modulators affect RA disease course. The high TxGNN score most likely reflects an indirect similarity between "neutrophil/inflammation" nodes in the knowledge graph, rather than a defined, RA-specific pharmacological mechanism. This prediction should be treated as a research hypothesis, not a validated repurposing signal.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04970225](https://clinicaltrials.gov/study/NCT04970225) | N/A | Completed | 47 | Studied blood neutrophil function and phenotype in cystic fibrosis patients, including the impact of CFTR modulator treatment. Not designed around RA patients or RA endpoints — relevance grade **C** (mechanistic association only, via neutrophil biology; no direct relevance to the RA indication). |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28634110](https://pubmed.ncbi.nlm.nih.gov/28634110/) | 2017 | Basic/Translational research (Tier 3) | Gastroenterology | Preclinical mouse models (NOD/ShiLtJ, BMP6-transduced, MRL/Mp) show that restoring CFTR activity in ducts reduces inflammation in pancreatic and salivary glands, in the context of Sjögren's syndrome and autoimmune pancreatitis — not RA. |

---

## Denmark Market Information

No marketing authorisations for Ivacaftor are currently on file for Denmark (market status: **Not marketed**; total authorisations: **0**).

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

*Note: This evidence pack flags a blocking data gap — Danish label warnings/contraindications for Ivacaftor have not yet been retrieved, which prevents a full S1 safety pre-assessment.*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication (rheumatoid arthritis) is currently supported only by an indirect, low-relevance clinical trial (grade C, in CF patients, not RA patients) and a single preclinical/basic-research publication (Tier 3, not RA-focused). Evidence level is L4 with decision stage S1 ("Research Question") — this is a mechanistic hypothesis, not clinical evidence, and does not yet justify further investment.

**To proceed, the following is needed:**
- Danish/EU SmPC warnings and contraindications for Ivacaftor (currently a Blocking data gap — required before any safety pre-assessment)
- Verified mechanism of action data via DrugBank API (currently a High-severity data gap)
- Drug-drug interaction (DDI) data (current query status: not found)
- RA-specific preclinical or clinical studies directly testing CFTR modulation in autoimmune/inflammatory arthritis models
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

