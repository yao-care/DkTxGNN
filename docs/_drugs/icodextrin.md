---
layout: default
title: Icodextrin
parent: 僅模型預測 (L5)
nav_order: 221
evidence_level: L5
indication_count: 10
---

# Icodextrin
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

# Icodextrin: From Peritoneal Dialysis to Irritable Bowel Syndrome

## One-Sentence Summary

Icodextrin is a large-molecule glucose polymer used as an osmotic agent in peritoneal dialysis solutions (intraperitoneal fluid/ultrafiltration management for patients with renal failure). The TxGNN model predicts a possible link to **Irritable Bowel Syndrome (IBS)**, but this prediction is currently supported by **0 clinical trials** and **0 publications**, and the model's own mechanistic assessment flags it as biologically implausible and possibly a knowledge-graph artefact rather than a genuine repurposing signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Peritoneal dialysis (osmotic ultrafiltration agent) — no formal indication text is available in the evidence pack, and the drug currently holds no Danish marketing authorisation |
| Predicted New Indication | Irritable Bowel Syndrome |
| TxGNN Prediction Score | 98.53% |
| Evidence Level | L5 (model prediction only, no supporting trials or literature) |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for icodextrin is not available in this evidence pack. Based on the information that is available, icodextrin is a large-molecule (starch-derived) osmotic agent administered intraperitoneally as a peritoneal dialysis solution. It is essentially not absorbed into the systemic circulation and has no established pharmacology relevant to gut motility, visceral sensitivity, or the gut-brain axis — the core pathophysiological pathways implicated in IBS.

There is no known mechanistic bridge between peritoneal dialysis (a fluid-removal/renal-replacement therapy) and IBS (a functional gastrointestinal motility/sensitivity disorder). The model's own repurposing rationale explicitly acknowledges this gap, noting that the connection "cannot rule out being a high-score false signal caused by comorbidity or node-proximity effects in the knowledge graph," rather than a true, biologically grounded treatment hypothesis.

Given the absence of original MOA documentation, zero corroborating clinical trials, and zero supporting literature, this prediction should be treated as a hypothesis-generation signal only, not as a candidate ready for further pharmacological or clinical evaluation at this time.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Denmark Market Information

No Danish marketing authorisations are currently on file for Icodextrin. Market status is recorded as **Not marketed**, with **0** registered authorisations, so no approved indication text is available for comparison.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information. No structured warnings, contraindications, or drug-interaction data are currently available for this candidate.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- Evidence level is L5 — this is a model prediction with no supporting clinical trials or literature, and the drug's own mechanistic rationale argues against biological plausibility (a non-absorbed, intraperitoneal osmotic agent has no known pathway relevant to IBS).
- A **Blocking**-severity data gap exists (TFDA/SmPC label warnings and contraindications are missing), which by itself prevents this candidate from entering even an initial (S1) safety evaluation.
- Four other TxGNN-predicted indications for icodextrin (non-syndromic esophageal malformation, C1 inhibitor deficiency, potassium deficiency disease, and serpinopathy with toxic serpin polymerization) were also returned at similarly high scores but were assessed by the same rationale process as mechanistically implausible or, in the case of the structural esophageal malformation, not a drug-treatable condition at all — reinforcing that these signals likely reflect knowledge-graph node proximity rather than genuine pharmacological relationships.

**To proceed, the following is needed:**
- Sourced SmPC/label warnings and contraindications (currently a Blocking data gap)
- Documented mechanism of action (currently a High-severity data gap)
- Independent verification of whether the IBS signal reflects a true pharmacological hypothesis or a knowledge-graph artefact, before any preclinical or literature follow-up is commissioned
- Confirmation of Danish marketing authorisation status before any further regulatory or clinical planning, since the product is not currently marketed in Denmark
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

