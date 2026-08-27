---
layout: default
title: Treprostinil
parent: 僅模型預測 (L5)
nav_order: 451
evidence_level: L5
indication_count: 10
---

# Treprostinil
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

# Treprostinil: From Pulmonary Arterial Hypertension to Connective Tissue Disease-Associated Pulmonary Arterial Hypertension

## One-Sentence Summary

> Treprostinil is a prostacyclin (PGI2/IP-receptor) analogue whose established therapeutic class is pulmonary arterial hypertension (WHO Group 1); it currently has no Danish marketing authorisation.
> The TxGNN model predicts it may be effective for **Connective Tissue Disease-Associated Pulmonary Arterial Hypertension (CTD-PAH)**,
> with **1 clinical trial** and a pool of **19 publications** — including a tier-1 RCT and a 2024 systematic review/meta-analysis — supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in Danish regulatory data (drug not currently marketed in Denmark); mechanistic rationale in the evidence pack identifies treprostinil as an established WHO Group 1 PAH therapy |
| Predicted New Indication | Connective Tissue Disease-Associated Pulmonary Arterial Hypertension |
| TxGNN Prediction Score | 99.55% |
| Evidence Level | L2 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

The evidence pack does not contain a validated `original_moa` record for treprostinil (flagged as a High-severity data gap, DG002), so the mechanistic picture below is drawn from the repurposing-rationale evidence rather than a verified DrugBank/SmPC entry and should be confirmed before final sign-off. According to that evidence, treprostinil is a prostacyclin (PGI2) analogue acting on IP receptors to produce pulmonary and systemic vasodilation, inhibit platelet aggregation, and suppress vascular smooth-muscle proliferation — the core pharmacological mechanism underlying WHO Group 1 pulmonary arterial hypertension therapy.

CTD-PAH is not a structurally distinct disease from the indications treprostinil already addresses — it is a well-recognized WHO Group 1 subgroup (most commonly arising in systemic sclerosis, followed by SLE and mixed connective tissue disease). This makes the prediction less a "repurposing into a new disease" and more a confirmation of applicability to an already-covered disease subtype. This is supported by a treprostinil-specific RCT subgroup analysis in CTD-PAH (Oudiz et al., 2004) and reinforced by a 2024 systematic review/meta-analysis of CTD-PAH treatment outcomes.

By contrast, the single highest raw TxGNN score in this evidence pack (99.7%, rank 1) points to "pulmonary arteriovenous malformation" — a structural vascular anomaly (typically HHT-related) rather than a vasoconstrictive/elevated-PVR disease. The evidence pack's own reviewer notes flag this as a likely knowledge-graph proximity artifact (similar node naming to other PAH entities) rather than a genuine mechanistic signal: it carries zero supporting trials or literature and is scored L5/Hold. It is therefore not used as the featured indication in this report, even though its raw score is nominally higher than CTD-PAH's.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02663895](https://clinicaltrials.gov/study/NCT02663895) | Phase 2 | Completed | 12 | Open-label pilot of oral treprostinil for 12 months in systemic sclerosis patients with calcinosis; primary endpoint was calcinosis reduction, not PAH — indirect supporting evidence only |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38378970](https://pubmed.ncbi.nlm.nih.gov/38378970/) | 2024 | Systematic Review / Meta-analysis | Internal and Emergency Medicine | Meta-analysis of RCT subgroup/post-hoc data on CTD-PAH treatment outcomes (functional class, survival, 6MWD, NT-proBNP) |
| [11897647](https://pubmed.ncbi.nlm.nih.gov/11897647/) | 2002 | RCT | Am J Respir Crit Care Med | Pivotal double-blind, placebo-controlled trial of continuous subcutaneous treprostinil in PAH (Simonneau et al.), foundational efficacy/safety data for the drug class |
| [15302727](https://pubmed.ncbi.nlm.nih.gov/15302727/) | 2004 | RCT subgroup analysis | Chest | Efficacy and safety of subcutaneous treprostinil specifically in CTD-associated PAH patients |
| [40566626](https://pubmed.ncbi.nlm.nih.gov/40566626/) | 2025 | RCT (selexipag, same class, not treprostinil) | Life (Basel) | Selexipag in CTD-PAH with concomitant interstitial lung disease; supportive class-effect evidence |
| [34462153](https://pubmed.ncbi.nlm.nih.gov/34462153/) | 2021 | Cohort | La Revue de Médecine Interne | Multicenter retrospective study characterizing CTD-PAH patients treated with prostanoids |
| [35412560](https://pubmed.ncbi.nlm.nih.gov/35412560/) | 2022 | Review | JAMA | General PAH diagnosis and treatment review, contextualizing prostacyclin pathway therapies |
| [41594679](https://pubmed.ncbi.nlm.nih.gov/41594679/) | 2026 | Review | Biomolecules | Current therapeutic strategies and future prospects for CTD-PAH |
| [37765060](https://pubmed.ncbi.nlm.nih.gov/37765060/) | 2023 | Review | Pharmaceuticals (Basel) | Recent advances in treatment of CTD-associated PAH |
| [16218473](https://pubmed.ncbi.nlm.nih.gov/16218473/) | 2005 | Review | Lupus | Overview of PAH associated with connective tissue diseases |
| [22621693](https://pubmed.ncbi.nlm.nih.gov/22621693/) | 2012 | Review | Drugs | Treatment approaches for PAH in connective tissue disease |

---

## Denmark Market Information

Treprostinil currently holds **no marketing authorisation in Denmark** (0 authorisations on record; market status: Not marketed). No national (Lægemiddelstyrelsen) or centralised (EMA) licence data is available in this evidence pack.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information. Key warnings, contraindications, and drug-drug interaction data are not currently available in this evidence pack (DDI query status: not found).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
CTD-PAH is a well-established WHO Group 1 PAH subgroup with a directly relevant RCT subgroup analysis, a 2024 systematic review/meta-analysis, and a shared, already-validated prostacyclin mechanism — evidence level L2. However, treprostinil has zero current Danish marketing authorisations, and drug-level safety data are blocked by a data gap (DG001), so this cannot yet advance without additional safety documentation.

**To proceed, the following is needed:**
- Danish/EU SmPC warnings and contraindications (currently blocking data gap DG001)
- Verified DrugBank/product mechanism-of-action documentation (DG002)
- Confirmation of Danish/EU marketing-authorisation or named-patient import pathway, given 0 current licences
- Drug-drug interaction screening (currently "not found")
- Route-of-administration compatibility assessment (marked "pending" across all predicted indications in this pack)
- Note: Two other PAH subtypes in this evidence pack — CHD-associated PAH (L2, Proceed with Guardrails) and HIV-associated PAH (L3, Research Question) — warrant separate evaluation; the highest raw-scoring prediction (pulmonary arteriovenous malformation, L5) is assessed by the evidence pack itself as a likely model artifact with no supporting trials or literature and should remain on Hold.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

