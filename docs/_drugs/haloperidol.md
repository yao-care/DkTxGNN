---
layout: default
title: Haloperidol
parent: 僅模型預測 (L5)
nav_order: 216
evidence_level: L5
indication_count: 10
---

# Haloperidol
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

# Haloperidol: From Psychotic Disorders to Congenital Disorder of Glycosylation with Defective Fucosylation

## One-Sentence Summary

Haloperidol is a first-generation (typical) antipsychotic, primarily used in the treatment of schizophrenia and other psychotic disorders through dopamine D2 receptor antagonism.
The TxGNN model predicts it may be effective for **Congenital Disorder of Glycosylation with Defective Fucosylation (SLC35C1-CDG)**, with **no clinical trials** and **no supporting publications** identified to date.
This prediction is based entirely on model inference; the mechanistic rationale is highly speculative and no empirical evidence exists to support further investigation at this stage.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Psychotic disorders / Schizophrenia (no authorisation registered in Denmark) |
| Predicted New Indication | Congenital Disorder of Glycosylation with Defective Fucosylation |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L5 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Haloperidol is a butyrophenone-class antipsychotic whose principal mechanism is high-affinity dopamine D2 receptor antagonism in the central nervous system. It has established clinical use in schizophrenia, acute psychosis, Tourette syndrome, and agitation states. Detailed pharmacological mechanism of action data was not available in the current evidence pack; however, its D2 antagonism profile is well documented in the broader literature and is reflected throughout the repurposing rationale provided.

Congenital Disorder of Glycosylation with Defective Fucosylation — also known as SLC35C1-CDG or Leukocyte Adhesion Deficiency type II (LAD II) — is a rare autosomal recessive metabolic disorder caused by loss-of-function mutations in the SLC35C1 gene encoding the Golgi GDP-fucose transporter. The resulting failure of fucosylation of surface glycoproteins leads to recurrent infections, intellectual disability, and growth retardation. This pathological mechanism is fundamentally distinct from dopaminergic dysregulation.

There is no known direct mechanistic link between Haloperidol's D2 antagonism and the metabolic defect underlying SLC35C1-CDG. While some in vitro findings suggest antipsychotics can influence N-glycosylation of dopamine receptors, this effect is observed at the receptor level and represents the opposite of what would be therapeutically required to correct a GDP-fucose transport deficiency. No published research has examined Haloperidol in the context of this disease. The high TxGNN confidence score most likely reflects indirect pathway connections within the knowledge graph rather than a genuine disease-modifying mechanism, and this prediction should be treated as highly speculative with low credibility.

---

## Clinical Trials

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Denmark Market Information

Haloperidol has no marketing authorisations registered in Denmark. Neither a national authorisation through the Danish Medicines Agency (Laegemiddelstyrelsen) nor a centralised authorisation through the EMA is currently on record for this active substance in Denmark.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

> **Note for reviewers:** It is worth flagging that Haloperidol is known from international SmPCs to carry risks of corneal and lens pigmentation, retinal toxicity, and extrapyramidal effects. These existing safety signals are particularly relevant given that two of the top-five TxGNN predictions involve retinal and ocular conditions (retinal dystrophy with or without extraocular anomalies), where these adverse effects would represent an active contraindication to use.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no clinical, observational, or preclinical evidence supporting Haloperidol for congenital disorder of glycosylation with defective fucosylation, and no plausible mechanistic pathway connects dopamine D2 antagonism to GDP-fucose transporter deficiency. All five unique predicted indications in this evidence pack share an L5 evidence level with a unanimous Hold recommendation, indicating that none of the current TxGNN predictions for this drug are ready for clinical consideration.

**To proceed, the following is needed:**

- **Biological plausibility review:** A clinical pharmacologist or metabolic disease specialist should evaluate whether any indirect pathway connecting D2 antagonism to glycosylation biology exists before committing further resources.
- **MOA data gap resolution:** DrugBank detailed mechanism of action data must be retrieved (data gap DG002) to support any mechanistic assessment.
- **Safety data retrieval:** The SmPC/SPC for Haloperidol must be obtained and parsed from an authoritative European source (e.g., EMA product database or a national medicines agency with current approval) to address data gap DG001, particularly given the known retinal and ocular toxicity signals.
- **Preclinical feasibility study:** If the biological plausibility review yields any positive signal, targeted in vitro experiments examining Haloperidol's effect on fucosylation pathways would be required before any clinical hypothesis can be formed.
- **Market status clarification:** Confirm whether Haloperidol is available in Denmark via parallel import or compounding, as this would affect any future compassionate use or study design considerations.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

