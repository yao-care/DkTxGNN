---
layout: default
title: Rifaximin
parent: 僅模型預測 (L5)
nav_order: 378
evidence_level: L5
indication_count: 10
---

# Rifaximin
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

# Rifaximin: From Enteric Bacterial Infections to Oral Candidiasis

## One-Sentence Summary

Rifaximin is a gut-restricted rifamycin-class antibacterial (original indication and detailed MOA not on file in this Evidence Pack). TxGNN predicts a possible link to **Oral Candidiasis** with a 99.75% score, but the only supporting literature (1 cohort study, 0 clinical trials) actually reports rifaximin use being **associated with increased risk** of resistant Candida infection — i.e., an adverse-signal finding, not therapeutic evidence. Four other candidate diseases (commissural lip fistula, osteoradionecrosis of the mandible, burning mouth syndrome, oral leukoedema) were also generated, all with no clinical trial or literature support (L5).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in Evidence Pack (original_indications is empty; drug is classified as a gut-non-absorbable rifamycin-class antibacterial per rationale notes) |
| Predicted New Indication | Oral Candidiasis |
| TxGNN Prediction Score | 99.75% |
| Evidence Level | L4 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for rifaximin in this Evidence Pack. Based on the information that is available, rifaximin is a rifamycin-class antibacterial with systemic bioavailability below 0.4% — it acts locally in the gut by inhibiting bacterial RNA polymerase in gram-positive and gram-negative organisms. It has no known antifungal activity against *Candida* species, which is the causative organism in oral candidiasis.

Consequently, there is no direct pharmacological rationale connecting rifaximin to the treatment of oral candidiasis. The single relevant publication in this Evidence Pack points in the **opposite direction**: it reports that rifaximin use in allogeneic HSCT recipients was associated with a higher incidence of micafungin-resistant *Candida* infections, plausibly through disruption of gut/oropharyngeal microbial flora rather than any antifungal or protective effect.

Given this, the high TxGNN score most likely reflects a knowledge-graph proximity artifact (antibacterial drugs co-occurring with infection-related disease nodes) rather than a genuine repurposing signal. The same mechanistic disconnect applies to the four other candidate diseases identified by the model — none are infectious in nature (or, where infection is a secondary factor, rifaximin's negligible systemic exposure precludes reaching an effective concentration at the target tissue).

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34180023](https://pubmed.ncbi.nlm.nih.gov/34180023/) | 2021 | Cohort study | Annals of Hematology | In allogeneic HSCT recipients, rifaximin use was associated with a higher incidence of micafungin-resistant *Candida* spp. infections — an adverse association, not evidence of therapeutic benefit against oral candidiasis |

---

## Denmark Market Information

Rifaximin is currently **not marketed** in Denmark; no marketing authorisations (national or centralised/EMA) are on file in this Evidence Pack.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information. Note: this Evidence Pack flags the absence of label warnings/contraindications data as a **Blocking** data gap, meaning a preliminary safety assessment (S1) cannot currently be performed for this candidate.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanism of action does not support efficacy against oral candidiasis (rifaximin has no antifungal activity and negligible systemic absorption), and the only available literature reports an adverse association rather than supportive evidence. There are no clinical trials, no Denmark marketing authorisation, and a Blocking data gap on label safety information — none of the five TxGNN-predicted indications for this drug currently clear even a preliminary evidence bar.

**To proceed, the following is needed:**
- TFDA/SmPC label data (warnings, contraindications) — currently a Blocking gap
- Confirmed mechanism of action (MOA) via DrugBank
- Original indication data to properly assess mechanistic plausibility
- New supportive preclinical or clinical evidence, since the existing literature signal runs counter to the hypothesis
- If pursuing further, re-review of the other 4 candidate diseases (commissural lip fistula, osteoradionecrosis of the mandible, burning mouth syndrome, oral leukoedema), all currently L5 with no trial/literature support
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

