---
layout: default
title: Belatacept
parent: 僅模型預測 (L5)
nav_order: 58
evidence_level: L5
indication_count: 0
---

# Belatacept
{: .fs-9 }

證據等級: **L5** | 預測適應症: **0** 個
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

# Belatacept: Kidney Transplant Rejection Prevention — No Repurposing Predictions Available

## Summary

Belatacept (DrugBank ID: DB06681) is a selective T-cell costimulation blocker approved internationally under the brand name **Nulojix** for prevention of acute rejection in adult kidney transplant recipients.
**The TxGNN model did not generate any repurposing predictions** for this candidate in the current run, and the drug has no recorded marketing authorisations in Denmark.
Critical data gaps — including mechanism of action detail and formal safety data — must be resolved before a full evaluation can proceed.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Prevention of acute rejection in adult kidney transplant recipients (international approval; no Danish MA on file) |
| Predicted New Indication | No predictions generated |
| TxGNN Prediction Score | N/A |
| Evidence Level | N/A — No predictions available |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why No Predictions Were Generated

The TxGNN pipeline successfully identified Belatacept in DrugBank (query log entry 2, status: `success`), but returned zero repurposing candidate indications. This is likely caused by one or more of the following:

1. **Score threshold filtering**: All candidate disease–drug association scores may have fallen below the minimum threshold applied in this prediction run.
2. **Knowledge graph coverage for biologics**: Belatacept is a large fusion protein (CTLA-4-Ig), not a small-molecule drug. The TxGNN knowledge graph has historically fewer mechanistic edges for biologics, which can impair embedding quality and reduce predicted scores.
3. **Missing MOA data (DG002)**: Without mechanism of action annotations in the graph, the drug node is under-connected, reducing the reach of graph-based inference.

A re-run after resolving data gaps DG001 and DG002 — or with a relaxed score threshold — may yield candidate predictions in a future cycle.

---

## Drug Background

Although mechanism of action data is absent from the Evidence Pack, Belatacept is a well-characterised biological agent in international literature:

- **Class**: Fusion protein (CTLA-4-Ig); selective T-cell costimulation blocker
- **Mechanism**: Binds CD80 and CD86 on antigen-presenting cells, blocking the CD28 co-stimulatory signal required for full T-cell activation — thereby suppressing the alloimmune response without calcineurin inhibition
- **International approval**: EMA-centralised authorisation as **Nulojix** (EU/1/11/694) for prophylaxis of acute rejection in adult renal transplant recipients; FDA-approved since 2011
- **Route**: Intravenous infusion (hospital/specialist setting)

The costimulation blockade mechanism is biologically plausible for indications beyond renal transplantation — for example other solid-organ transplants, graft-versus-host disease, and certain autoimmune diseases. However, no formal TxGNN predictions are available at this time, and no repurposing recommendation can therefore be made.

---

## Denmark Market Information

No marketing authorisations for Belatacept are recorded in the current dataset for Denmark. Although the EMA centralised authorisation for Nulojix is valid across all EU member states, the Evidence Pack reflects that the product is not actively marketed in Denmark.

| Item | Status |
|------|--------|
| National MA (Laegemiddelstyrelsen) | None on file |
| EMA Centralised MA (Nulojix, EU/1/11/694) | Not reflected in current dataset — verify directly with EMA |
| Market Status | Not marketed |

Healthcare professionals requiring access in Denmark should check with the Danish Medicines Agency (Laegemiddelstyrelsen) regarding named-patient or hospital import programmes.

---

## Safety Considerations

No safety data is available in the current Evidence Pack. Please refer to the approved Summary of Product Characteristics (SmPC) for Nulojix for complete safety information.

> **Note for prescribers**: Published international SmPCs for Nulojix carry a prominent warning regarding **post-transplant lymphoproliferative disorder (PTLD)** — with elevated risk in EBV-seronegative patients — and increased susceptibility to serious infections including progressive multifocal leukoencephalopathy (PML). These are provided here for contextual awareness only; the Danish SmPC should be consulted for locally approved prescribing information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No TxGNN repurposing predictions were generated for Belatacept in this run, and the two blocking/high-severity data gaps (DG001, DG002) prevent even a preliminary safety and mechanistic assessment. Proceeding to clinical evaluation without predictions or safety data is not justified at this stage.

**To proceed, the following is needed:**

- **Resolve DG002 (High)**: Retrieve full MOA and target data from the DrugBank API to improve knowledge graph coverage and enable a prediction re-run
- **Resolve DG001 (Blocking)**: Retrieve the EMA SmPC for Nulojix (or local Danish equivalent) to populate warnings, contraindications, and DDI data
- **Re-run TxGNN prediction**: After data gap remediation, re-run with standard threshold; consider a sensitivity run at a relaxed threshold to assess whether any borderline candidates exist
- **Confirm Danish market status**: Contact Laegemiddelstyrelsen or check the EMA product page to confirm whether Nulojix is available via any access programme in Denmark
- **Assess biologic-specific KG coverage**: If re-run still yields no predictions, escalate to the TxGNN modelling team to review graph edge density for biologics
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

