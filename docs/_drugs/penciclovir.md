---
layout: default
title: Penciclovir
parent: 僅模型預測 (L5)
nav_order: 344
evidence_level: L5
indication_count: 10
---

# Penciclovir
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

# Penciclovir: From Herpes Simplex Virus Infections to Fascioliasis

## One-Sentence Summary

> Penciclovir is a guanine nucleoside analogue antiviral, pharmacologically used against herpes simplex virus (HSV) infections by requiring viral thymidine kinase (TK) for activation.
> The TxGNN model predicts it may be effective for **Fascioliasis** (liver fluke infection), with a prediction score of **99.06%**,
> but currently **no clinical trials and no published literature** support this direction, and the model's own mechanistic rationale argues against biological plausibility.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Herpes simplex virus (HSV) infections (mechanism inferred from evidence pack rationale; structured indication registry data not available — see note below) |
| Predicted New Indication | Fascioliasis |
| TxGNN Prediction Score | 99.06% |
| Evidence Level | L5 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

**Note on Original Indication:** The evidence pack's `original_indications` and `taiwan_regulatory.licenses` fields are both empty, so no registry-sourced approved indication text is available. The indication above is inferred solely from the mechanistic description embedded in the evidence pack's own repurposing rationale (guanine nucleoside analogue activated by viral thymidine kinase — the canonical Penciclovir/HSV mechanism). This should be verified against the official Summary of Product Characteristics (SmPC) before use in any decision document.

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action (MOA) data is flagged as a data gap (`[Data Gap]`) in the structured drug record. However, the evidence pack's own repurposing rationale provides a partial mechanistic description: Penciclovir is a guanine nucleoside analogue whose antiviral activity depends on first-step phosphorylation by a **viral-specific thymidine kinase (TK)** — a mechanism specific to herpesviruses such as HSV.

Unlike a typical repurposing candidate, the mechanistic analysis included in this evidence pack **does not support** the predicted new indication. Fascioliasis is caused by the trematode *Fasciola hepatica/gigantica* (liver fluke), a helminth with no known viral-type TK-dependent activation pathway. The rationale explicitly states that there is "no known or hypothesized nucleoside-metabolism interference mechanism" supporting anti-helminthic activity for Penciclovir, and concludes that the high TxGNN similarity score is most likely driven by **knowledge-graph embedding proximity** (e.g., shared graph neighbors with other antiparasitic agents) rather than genuine pharmacological plausibility.

In other words, this is a case where the model's quantitative score (99.06%) is high, but the qualitative mechanistic evidence — drawn from the same evidence pack — actively argues against clinical relevance. This combination (high score, contradicted mechanism, zero external evidence) is the primary basis for the "Hold" recommendation below.

---

## Other Predicted Indications (Same Evidence Pack)

The evidence pack contains four additional distinct predicted indications for Penciclovir, all scored similarly high by TxGNN but likewise unsupported by clinical trials, literature, or a plausible mechanism:

| Rank | Disease | TxGNN Score | Evidence Level | Recommendation | Mechanistic Note |
|------|---------|-------------|-----------------|-----------------|-------------------|
| 3–4 | Cysticercosis | 98.99% | L5 | Hold | No overlap with standard albendazole/praziquantel mechanisms (microtubule/calcium-channel targets) |
| 5–6 | Coenurosis | 98.75% | L5 | Hold | Same helminth-class reasoning as cysticercosis; likely graph-structural artifact |
| 7–8 | Intestinal helminthiasis | 98.70% | L5 | Hold | No published in vitro/in vivo anti-helminthic activity data for Penciclovir |
| 9–10 | Malignant pleural mesothelioma | 98.51% | L5 | Hold | Penciclovir's kinase specificity is highly selective for HSV TK, with very low affinity for mammalian (including tumor) kinases; no cell-line or animal-model data support antiproliferative use |

All five predictions share the same profile: no clinical trials, no literature, L5 evidence (model prediction only), and a mechanistic rationale that explicitly cautions against interpreting the score as pharmacologically meaningful.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

*(Query log confirms ClinicalTrials.gov and WHO ICTRP searches were performed for all five predicted diseases on 2026-03-24, with zero results.)*

---

## Literature Evidence

Currently no related literature available.

*(Query log confirms PubMed searches were performed for all five predicted diseases on 2026-03-24, with zero results.)*

---

## Denmark Market Information

Penciclovir currently has **no marketing authorisations on record** in this evidence pack (`total_licenses: 0`, market status: Not marketed). No national (Laegemiddelstyrelsen) or centralised (EMA) authorisation details are available to list.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

**Important:** This evidence pack flags a **Blocking** data gap (DG001) — TFDA/label warnings and contraindications could not be retrieved, which by itself prevents progression to a formal safety (S1) evaluation. A drug interaction (DDI) query also returned no results (`not_found`), meaning absence of interactions should not be assumed — it reflects a data availability gap, not a confirmed clean interaction profile.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- All five predicted indications rest on **L5 evidence** (model prediction only) with zero supporting clinical trials or literature.
- The evidence pack's own mechanistic analysis for the top-ranked prediction (fascioliasis) explicitly concludes the high similarity score likely reflects a knowledge-graph embedding artifact rather than genuine pharmacological plausibility — the same reasoning applies to the other four candidates.
- A **Blocking** data gap (missing SmPC/label warnings and contraindications) prevents any safety pre-assessment (S1) regardless of efficacy evidence.
- Penciclovir is not currently marketed in Denmark (0 marketing authorisations), so no local dosage form or approved-indication pathway currently exists to support even guardrail-based off-label use.

**To proceed, the following is needed:**
- Retrieve the official SmPC / label warnings and contraindications (resolves DG001, Blocking)
- Obtain confirmed mechanism of action (MOA) data from DrugBank or primary literature (resolves DG002, High)
- Conduct or identify in vitro/in vivo studies testing Penciclovir against *Fasciola*, *Taenia* species, or mesothelioma cell lines before any further evidence-level upgrade is considered
- Re-run clinical trial and literature searches periodically, as current searches (2026-03-24) returned zero hits for all five candidate indications
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

