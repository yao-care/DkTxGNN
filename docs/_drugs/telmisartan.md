---
layout: default
title: Telmisartan
parent: Kun modelforudsigelse (L5)
nav_order: 421
evidence_level: L5
indication_count: 10
---

# Telmisartan
{: .fs-9 }

Evidensniveau: **L5** | Forudsagte indikationer: **10** stk.
{: .fs-6 .fw-300 }

---

## Indholdsfortegnelse
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Farmaceutens vurderingsrapport

</div>

# Telmisartan: From Hypertension to Prinzmetal Angina

## One-Sentence Summary

Telmisartan is an angiotensin II receptor blocker (ARB) established for the treatment of hypertension. The TxGNN model's top-ranked prediction in this Evidence Pack is **Prinzmetal angina**, with a prediction score of **99.98%** — but currently **zero clinical trials and zero publications** support this specific indication.

> Note: `original_indications` and Danish market data were empty in this Evidence Pack. "Hypertension" is stated based on established pharmacological knowledge of telmisartan (ARB class), not extracted from the pack.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (general drug-class knowledge; not present in Evidence Pack) |
| Predicted New Indication | Prinzmetal angina |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| Denmark Market Status | Not marketed (Not marketed) |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action (MOA) data is not available in this Evidence Pack (flagged as a High-severity data gap, DG002). Based on known pharmacology, telmisartan is an angiotensin II type 1 (AT1) receptor blocker that lowers blood pressure by inhibiting the renin-angiotensin-aldosterone system (RAAS); it also has partial PPAR-γ agonist activity.

Prinzmetal (variant) angina is caused primarily by focal coronary artery vasospasm, and standard treatment relies on calcium channel blockers and nitrates — agents that directly relax vascular smooth muscle. Telmisartan's RAAS-inhibition/antihypertensive mechanism has no established direct link to the pathophysiology of coronary vasospasm, so the mechanistic rationale for this specific prediction is weak.

This appears to be a high-confidence TxGNN knowledge-graph association rather than a mechanistically or clinically substantiated signal: no clinical trials, no ICTRP-registered trials, and no PubMed literature were found for telmisartan in Prinzmetal angina across any of the queries in this pack.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Denmark Market Information

Telmisartan currently has **no marketing authorisations on record** in this Evidence Pack (market status: not marketed; total authorisations: 0). No national (Lægemiddelstyrelsen) or centralised (EMA) licence entries were available to tabulate.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information. (Key warnings, contraindications, and drug-drug interaction data were not available in this Evidence Pack — DG001, flagged Blocking severity, notes that TFDA/label warning data still needs to be retrieved before a safety pre-assessment can proceed.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (Prinzmetal angina) has no clinical trial or literature evidence and only a weak mechanistic rationale, meeting criteria for evidence level L5 (model prediction only). Combined with the absence of Danish marketing authorisation and unresolved safety data gaps, this candidate does not currently support further evaluation.

**To proceed, the following is needed:**
- Telmisartan MOA and product labeling data (DG002)
- TFDA/SmPC warnings, contraindications, and DDI data (DG001 — Blocking)
- Any preclinical or mechanistic studies specifically linking ARBs to coronary vasospasm
- Confirmation of Danish market/authorisation status

**Additional note:** This Evidence Pack contains 10 ranked candidate indications for telmisartan. Several lower-ranked candidates have materially stronger evidence than the top-ranked one above — notably **cerebral artery occlusion** (rank 7–8, TxGNN score 99.95%, Evidence Level **L2**, recommendation **Proceed with Guardrails**), supported by a completed Phase 4 RCT (NCT01075698, n=1228) and 17 preclinical publications on neuroprotective mechanisms. If a repurposing candidate is needed for further action, that indication is a substantially better-evidenced starting point than Prinzmetal angina and may warrant its own dedicated evaluation report.
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

