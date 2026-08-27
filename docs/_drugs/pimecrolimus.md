---
layout: default
title: Pimecrolimus
parent: 僅模型預測 (L5)
nav_order: 351
evidence_level: L5
indication_count: 8
---

# Pimecrolimus
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

# Pimecrolimus: From Atopic Dermatitis to Seborrheic Dermatitis

## One-Sentence Summary

> Pimecrolimus is a topical calcineurin inhibitor best known for treating atopic dermatitis (eczema).
> The TxGNN model predicts it may also be effective for **Seborrheic Dermatitis**,
> with **1 completed Phase 2 clinical trial** and **18 supporting publications** currently backing this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Atopic dermatitis (eczema) — based on general drug knowledge; no Danish label text is available in this evidence pack |
| Predicted New Indication | Seborrheic Dermatitis |
| TxGNN Prediction Score | 99.73% |
| Evidence Level | L2 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from DrugBank in this evidence pack. Based on general pharmacological knowledge, pimecrolimus is a topical calcineurin inhibitor (ascomycin macrolactam derivative) developed for inflammatory skin diseases, with its efficacy in atopic dermatitis well established internationally.

Seborrheic dermatitis, like atopic dermatitis, is a chronic inflammatory skin condition — its pathology is primarily driven by a localized inflammatory response triggered by *Malassezia* yeast. Pimecrolimus inhibits T-cell activation and the release of pro-inflammatory cytokines, which can relieve this inflammation without the skin-atrophy side effects associated with corticosteroids.

This mechanistic rationale is plausible and has already been directly validated in multiple clinical trials targeting facial seborrheic dermatitis, giving the TxGNN prediction reasonable biological grounding beyond a purely computational signal.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00403559](https://clinicaltrials.gov/study/NCT00403559) | Phase 2 | Completed | 113 | 4-week randomized, double-blind, parallel-group, active-comparator-controlled exploratory study of Elidel (pimecrolimus) for treatment of seborrheic dermatitis |

No EudraCT (EU Clinical Trials Register) identifiers were available in the evidence pack for this indication.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22142161](https://pubmed.ncbi.nlm.nih.gov/22142161/) | 2012 | Systematic Review of RCTs | Expert Rev Clin Pharmacol | Pimecrolimus 1% cream appears well-tolerated and effective for seborrheic dermatitis, with efficacy comparable to corticosteroids, antimycotics and placebo |
| [34910320](https://pubmed.ncbi.nlm.nih.gov/34910320/) | 2022 | RCT (comparative) | Clin Exp Dermatol | Randomized blinded trial of pimecrolimus 1% cream vs. sertaconazole 2% cream for facial seborrhoeic dermatitis |
| [23715821](https://pubmed.ncbi.nlm.nih.gov/23715821/) | 2013 | RCT (comparative) | Ir J Med Sci | Compared efficacy of sertaconazole 2% cream vs. pimecrolimus 1% cream in treatment of seborrheic dermatitis |
| [36072203](https://pubmed.ncbi.nlm.nih.gov/36072203/) | 2022 | Systematic Review | Cureus | Systematic review of RCTs on efficacy and safety of pimecrolimus in facial seborrheic dermatitis |
| [18677657](https://pubmed.ncbi.nlm.nih.gov/18677657/) | 2009 | Open, randomized, prospective, comparative study | J Dermatolog Treat | Compared topical pimecrolimus 1% cream vs. ketoconazole 2% cream in treatment of seborrheic dermatitis |
| [20000875](https://pubmed.ncbi.nlm.nih.gov/20000875/) | 2010 | Open-label Study | Am J Clin Dermatol | Pimecrolimus 1% cream effective and well tolerated for resistant facial seborrheic dermatitis |
| [23441238](https://pubmed.ncbi.nlm.nih.gov/23441238/) | 2013 | Review | J Clin Aesthet Dermatol | Topical pimecrolimus is a safe alternative to corticosteroids, suited for long-term use in seborrheic dermatitis |
| [27804089](https://pubmed.ncbi.nlm.nih.gov/27804089/) | 2017 | Systematic Review | Am J Clin Dermatol | Systematic review of topical treatments, including calcineurin inhibitors, for facial seborrheic dermatitis |
| [15700745](https://pubmed.ncbi.nlm.nih.gov/15700745/) | 2004 | Clinical study | Drugs Exp Clin Res | Pimecrolimus cream 1% effective, tolerable and safe for seborrheic dermatitis of face and trunk |
| [28589618](https://pubmed.ncbi.nlm.nih.gov/28589618/) | 2018 | Clinical study | J Cosmet Dermatol | Compared different treatment-duration regimens of pimecrolimus 1% cream for facial seborrheic dermatitis |

---

## Denmark Market Information

Currently no marketing authorisations for pimecrolimus are recorded in this evidence pack for Denmark (Lægemiddelstyrelsen or EMA centralised procedure). The drug's Danish market status is listed as **not marketed**.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information. No key warnings, contraindications, or drug-interaction data were available in this evidence pack — a drug interaction query returned no results, and label-derived warnings/contraindications were not retrievable.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple randomized controlled trials and systematic reviews directly support pimecrolimus efficacy in facial seborrheic dermatitis (Evidence Level L2), and the proposed mechanism — calcineurin-mediated anti-inflammatory action against *Malassezia*-driven inflammation — is biologically coherent with the drug's established profile in atopic dermatitis. However, critical safety and regulatory data are missing, so this should not proceed without guardrails.

**To proceed, the following is needed:**
- TFDA/SmPC label warnings and contraindications (currently a blocking data gap — required before any safety pre-assessment)
- Confirmed mechanism of action data from DrugBank
- Drug-drug interaction data (current query returned no results)
- Assessment of Danish market access pathway, since pimecrolimus is not currently marketed in Denmark
- EU-specific (EudraCT) trial data, if available, to complement the ClinicalTrials.gov record
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

