---
layout: default
title: Pretomanid
parent: 僅模型預測 (L5)
nav_order: 359
evidence_level: L5
indication_count: 10
---

# Pretomanid
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

# Pretomanid: From Multidrug-Resistant Tuberculosis to Candidiasis

## One-Sentence Summary

> Pretomanid is a nitroimidazooxazine antimycobacterial, used as part of the BPaL/BPaLM regimen (bedaquiline, pretomanid, linezolid ± moxifloxacin) for extensively drug-resistant and treatment-intolerant/non-responsive multidrug-resistant pulmonary tuberculosis.
> The TxGNN model predicts it may be effective for **Candidiasis**, but this is a **pure model prediction with no supporting clinical trials or literature**, and the evidence pack's own mechanistic review flags it as biologically implausible.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Multidrug-/extensively drug-resistant pulmonary tuberculosis (as part of the BPaL/BPaLM regimen) — not captured in structured `taiwan_regulatory` data |
| Predicted New Indication | Candidiasis |
| TxGNN Prediction Score | 99.69% |
| Evidence Level | L5 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for Pretomanid is not available in this evidence pack (flagged as a High-severity data gap). Based on known information, Pretomanid is a nitroimidazooxazine prodrug that requires activation by the mycobacteria-specific deazaflavin-dependent nitroreductase (Ddn)/F420 cofactor system to exert its bactericidal effect — a pathway specific to the *Mycobacterium* genus.

Candida species do not possess this Ddn/F420 activation pathway, and there is no known antifungal mechanism for Pretomanid. The evidence pack's own mechanistic assessment explicitly notes that this prediction reflects **knowledge-graph similarity rather than biological plausibility**, and that it lacks a credible pharmacological rationale.

For context, other top-ranked TxGNN candidates in this evidence pack (leprosy, coronary artery disease, myocardial ischemia, ALCAPA) were reviewed under the same lens: leprosy has some genus-level mechanistic logic (both *M. leprae* and *M. tuberculosis* are mycobacteria) but is directly contradicted by *in vitro* evidence showing *M. leprae* is naturally resistant to PA-824/Pretomanid; the cardiovascular predictions have no plausible mechanism and instead run counter to Pretomanid's known QT-prolongation risk. None of the candidates in this pack currently clear a basic mechanistic plausibility bar.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Denmark Market Information

Pretomanid currently holds no marketing authorisation in Denmark (0 licenses; market status: not marketed).

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

*Note: structured `key_warnings`, `contraindications`, and DDI data were not available for this evidence pack (query status: not_found). Separately, the evidence pack's mechanistic notes for other predicted indications reference a known QT-prolongation signal for Pretomanid — this should be confirmed against the SmPC before any further evaluation.*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The candidiasis prediction is supported only by a TxGNN similarity score (L5, no clinical trials, no literature), and the pack's own mechanistic review finds no plausible antifungal pathway for a mycobacteria-specific prodrug. Combined with a Blocking-severity data gap on SmPC warnings/contraindications, this candidate does not meet the threshold to advance past S0.

**To proceed, the following is needed:**
- TFDA/Danish SmPC label data (warnings, contraindications) — currently a Blocking data gap (DG001)
- Confirmed mechanism of action (DG001/DG002) to properly assess relevance to any non-mycobacterial indication
- Any *in vitro* or preclinical evidence of Pretomanid activity against *Candida* species before further investment
- If the leprosy signal is of interest instead, note it is directly contradicted by existing *in vitro* resistance data (PMID 17005816) and would also require dedicated re-evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

