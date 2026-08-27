---
layout: default
title: Natalizumab
parent: 僅模型預測 (L5)
nav_order: 305
evidence_level: L5
indication_count: 10
---

# Natalizumab
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

# Natalizumab: From Multiple Sclerosis to Bronchitis

## One-Sentence Summary

Natalizumab is a monoclonal antibody; the evidence pack does not contain confirmed Danish regulatory indication data, but the supporting literature consistently identifies its established use as relapsing-remitting multiple sclerosis. The TxGNN model predicts a possible new indication for **Bronchitis**, but this prediction is currently backed by **0 clinical trials** and **0 publications** — it is a pure model output with no corroborating clinical or mechanistic evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in regulatory data (`taiwan_regulatory.licenses` is empty); literature context (see evidence citations below) indicates use for relapsing-remitting multiple sclerosis |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.46% |
| Evidence Level | L5 (model prediction only, no clinical trials or literature) |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for natalizumab in this evidence pack (flagged as a High-severity data gap). Based on known pharmacology referenced across the supporting literature, natalizumab is a monoclonal antibody against α4-integrin (VLA-4) that blocks leukocyte migration across the blood–brain barrier and gut endothelium, used in the management of relapsing-remitting multiple sclerosis.

For the top-ranked candidate, **Bronchitis**, no mechanistic or clinical rationale is provided in the evidence pack. Bronchitis is predominantly an infectious/irritant airway condition, and there is no established pathophysiological link to α4-integrin blockade. If anything, natalizumab's systemic immunosuppressive effect would be expected to *increase* susceptibility to respiratory infection rather than treat it — the evidence direction runs counter to the repurposing hypothesis.

It is also worth noting that several lower-ranked candidates in this evidence pack (parapsoriasis, psoriasis, acute lichenoid pityriasis) did return literature hits, but nearly all of these describe natalizumab **inducing or aggravating** these skin conditions as adverse drug reactions (e.g., PMID 30323758, PMID 35646438, PMID 23096069), not treating them. Only one report (PMID 33589543) describes comorbid psoriasis improving during natalizumab treatment. This pattern — high TxGNN similarity scores paired with literature that points toward harm rather than benefit — further weakens confidence in the model's dermatological and respiratory predictions for this drug and supports a cautious, evidence-first approach before any repurposing consideration.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for the Bronchitis indication specifically.

## Denmark Market Information

No marketing authorisations are currently on file for natalizumab in Denmark in this evidence pack (`total_licenses: 0`, market status: not marketed).

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information — structured warnings, contraindications, and DDI data are not available in this evidence pack (`[Data Gap]` for all three fields; DDI query returned no results).

**Literature signal (supplementary, not from structured safety data):** a substantial share of the literature surfaced across this drug's candidate indications concerns Progressive Multifocal Leukoencephalopathy (PML), a serious JC-virus-related CNS complication associated with natalizumab (e.g., PMID 20298966, 19647202, 24136456, 30324046, 36283150, 22082208). While this data was retrieved in the context of unrelated disease-prediction searches rather than a formal safety query, it is a clinically material signal that any reviewer should be aware of before further evaluation.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication (Bronchitis) has zero supporting clinical trials or literature (Evidence Level L5), no plausible mechanistic link, and the drug is not currently marketed in Denmark. Related dermatological candidates in the same evidence pack show literature evidence pointing toward adverse drug reactions rather than therapeutic benefit, reinforcing that this evidence pack does not currently support progression.

**To proceed, the following is needed:**
- Confirmed original indication and approved SmPC text (currently unavailable — regulatory license data is empty)
- Mechanism of action detail from DrugBank or SmPC (DG002)
- TFDA/Danish Medicines Agency label warnings and contraindications (DG001, Blocking)
- Any preclinical or mechanistic rationale specifically connecting α4-integrin blockade to bronchitis pathophysiology
- Reassessment if future clinical trials or literature specific to Bronchitis emerge
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

