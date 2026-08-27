---
layout: default
title: Tolvaptan
parent: 僅模型預測 (L5)
nav_order: 441
evidence_level: L5
indication_count: 10
---

# Tolvaptan
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

# Tolvaptan: From Hyponatremia to Polycystic Kidney Disease

## One-Sentence Summary

> Tolvaptan is a selective vasopressin V2-receptor antagonist, internationally developed and marketed for hyponatremia (e.g. SIADH); it is **not currently marketed in Denmark**.
> The TxGNN model predicts it may be effective for **Polycystic Kidney Disease 3 (autosomal dominant polycystic kidney disease, ADPKD, with or without polycystic liver disease)**,
> with **20 supporting publications**, including two landmark completed Phase 3 RCTs, though no clinical-trial registry records were captured in this evidence pack.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hyponatremia (SIADH / euvolemic-hypervolemic hyponatremia) — general international knowledge; not present in this evidence pack (drug-level fields are data gaps) |
| Predicted New Indication | Polycystic kidney disease 3 with or without polycystic liver disease (ADPKD spectrum) |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L1 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack (data gap). Based on general pharmacological knowledge, Tolvaptan is a selective vasopressin V2-receptor (V2R) antagonist. Its efficacy in hyponatremia has been established internationally, and mechanistically the same V2R blockade is applicable to autosomal dominant polycystic kidney disease (ADPKD): V2R activation drives intracellular cAMP accumulation in renal tubular epithelium, which is a key driver of cyst growth and fluid secretion. Blocking V2R therefore slows cyst expansion and the decline in kidney function.

Both conditions — hyponatremia and ADPKD — center on the same renal vasopressin/cAMP signalling axis, which supports the mechanistic plausibility of this prediction. Notably, this is not a purely speculative prediction: Tolvaptan already has regulatory approval for ADPKD in several jurisdictions worldwide (based on the pivotal trials below), which independently corroborates the TxGNN model's output for this candidate.

---

## Clinical Trial Evidence

Currently no related clinical trials registered (the ClinicalTrials.gov / ICTRP query for this exact disease term returned zero results in this evidence pack). Note: the literature evidence below includes reports of pivotal completed Phase 3 trials (see PMID 23121377 and PMID 29105594) that were not captured by the registry search, likely due to disease-term string mismatch.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23121377](https://pubmed.ncbi.nlm.nih.gov/23121377/) | 2012 | RCT (Phase 3, TEMPO 3:4) | The New England Journal of Medicine | V2-receptor antagonism inhibits cyst growth and slows kidney function decline in ADPKD |
| [29105594](https://pubmed.ncbi.nlm.nih.gov/29105594/) | 2017 | RCT (Phase 3, REPRISE) | The New England Journal of Medicine | Confirms efficacy and safety of tolvaptan in later-stage ADPKD |
| [38091246](https://pubmed.ncbi.nlm.nih.gov/38091246/) | 2024 | RCT (pediatric) | Pediatric Nephrology | Tolvaptan safety/pharmacodynamics in children (5–17y) with ADPKD, risk-stratified analysis |
| [37150675](https://pubmed.ncbi.nlm.nih.gov/37150675/) | 2023 | Systematic Review / Meta-analysis | Nefrologia | Confirms safety and efficacy of tolvaptan across pooled ADPKD trials |
| [39356039](https://pubmed.ncbi.nlm.nih.gov/39356039/) | 2024 | Systematic Review (Cochrane) | Cochrane Database of Systematic Reviews | Evaluates disease-modifying agents, including tolvaptan, for ADPKD progression |
| [35134221](https://pubmed.ncbi.nlm.nih.gov/35134221/) | 2022 | Consensus Statement | Nephrology Dialysis Transplantation | ERA Working Group consensus on tolvaptan use in ADPKD, incl. initiation criteria |
| [40126492](https://pubmed.ncbi.nlm.nih.gov/40126492/) | 2025 | Review | JAMA | Comprehensive review of ADPKD, including tolvaptan as the approved disease-modifying therapy |
| [40726372](https://pubmed.ncbi.nlm.nih.gov/40726372/) | 2025 | Review | Current Opinion in Nephrology and Hypertension | Reviews emerging ADPKD therapies beyond tolvaptan, confirming tolvaptan as current standard |
| [35487607](https://pubmed.ncbi.nlm.nih.gov/35487607/) | 2022 | Review | Clinics in Liver Disease | Tolvaptan slows deterioration of renal function and cyst growth in ADPKD/polycystic liver disease |
| [35328738](https://pubmed.ncbi.nlm.nih.gov/35328738/) | 2022 | Review | International Journal of Molecular Sciences | ADPKD pathophysiology of cystogenesis and treatment advances |

---

## Denmark Market Information

Tolvaptan currently has no marketing authorisation on file in this evidence pack (0 licenses; market status: not marketed). No national (Laegemiddelstyrelsen) or centralised (EMA) authorisation record was available for extraction.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information. Key warnings, contraindications, and drug-drug interaction data are marked as data gaps in this evidence pack (DG001, Blocking severity — TFDA/label warnings and contraindications must be sourced before safety evaluation can proceed).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Two completed Phase 3 RCTs (TEMPO 3:4, REPRISE) plus a Cochrane systematic review and an ERA consensus statement provide strong (L1) efficacy evidence for tolvaptan in ADPKD. However, the drug has no current Danish marketing authorisation and this evidence pack has a Blocking safety data gap (label warnings/contraindications), so safety review cannot yet be completed.

**To proceed, the following is needed:**
- Danish/EU labeling data (SmPC warnings, contraindications) — currently Blocking (DG001)
- Mechanism of action confirmation via DrugBank (currently High-severity gap, DG002)
- Confirmation of original approved indication(s) and any prior Danish/EU regulatory history
- Drug-drug interaction data (DDI query returned no results)
- Clinical-trial registry cross-check to link the pivotal trials (TEMPO 3:4, REPRISE) to their registry records
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

