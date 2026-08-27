---
layout: default
title: Toripalimab
parent: 僅模型預測 (L5)
nav_order: 442
evidence_level: L5
indication_count: 10
---

# Toripalimab
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

# Toripalimab: From Oncology (PD-1 Immunotherapy) to Mixed-Type Autoimmune Hemolytic Anemia

## One-Sentence Summary

Toripalimab is a PD-1 immune checkpoint inhibitor; formal Danish licensing records list no confirmed original indication, but the drug's known mechanism is used in oncology to enhance anti-tumour T-cell activity. The TxGNN model predicts a possible effect on **mixed-type autoimmune hemolytic anemia (AIHA)**, but this prediction is supported by **zero clinical trials and zero publications**, and the accompanying mechanistic analysis explicitly flags a **biological contradiction** rather than a plausible repurposing rationale.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on file (no Danish licenses recorded; general mechanism data indicate oncology use as a PD-1 checkpoint inhibitor) |
| Predicted New Indication | Mixed-type autoimmune hemolytic anemia |
| TxGNN Prediction Score | 93.76% |
| Evidence Level | L5 (model prediction only — no clinical trials, no literature) |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for Toripalimab is not available in the formal drug record (MOA field is unpopulated). Based on information present elsewhere in the evidence pack, Toripalimab is a PD-1 immune checkpoint inhibitor whose pharmacological action is to **release the immune brake and enhance T-cell cytotoxic activity**, an approach used in oncology to help the immune system attack tumour cells.

Mixed-type autoimmune hemolytic anemia, by contrast, is a condition in which the immune system already over-attacks the body's own red blood cells; standard treatment relies on **immunosuppression**, not immune activation. The evidence pack's own mechanistic assessment flags this directly: anti-PD-1 agents are clinically known to *cause* AIHA and related cytopenias as an immune-related adverse event (irAE), rather than treat them. The same pattern repeats across the other high-scoring candidates in this pack — idiopathic aplastic anemia, dermatitis, paroxysmal nocturnal hemoglobinuria, and drug-induced AIHA all carry the same annotation: the predicted indication is a *known adverse effect* of PD-1 inhibition, not a therapeutic target.

The most likely explanation is that TxGNN's high score reflects **semantic proximity in the embedding space** (autoimmune/hematologic disease cluster) rather than a genuine, biologically supported treatment relationship. This is a case where the prediction should be treated as a modeling artifact until independent mechanistic or clinical evidence emerges.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Denmark Market Information

Toripalimab currently has no marketing authorisation on record in Denmark (0 licenses; market status: not marketed). No product, dosage form, or approved-indication data is available to report.

---

## Cytotoxicity

Toripalimab is a PD-1 immune checkpoint inhibitor, a class of antineoplastic immunotherapy.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Immunotherapy (PD-1 checkpoint inhibitor) — not a conventional cytotoxic agent |
| Myelosuppression Risk | Please refer to the Summary of Product Characteristics (SmPC) warnings and precautions |
| Emetogenicity Classification | Please refer to the Summary of Product Characteristics (SmPC) warnings and precautions |
| Monitoring Items | Please refer to the Summary of Product Characteristics (SmPC) warnings and precautions |
| Handling Protection | Please refer to the Summary of Product Characteristics (SmPC) warnings and precautions |

Note: unlike conventional chemotherapy, checkpoint inhibitors as a class carry a risk of immune-related adverse events (irAEs) — including immune hemolytic anemia, dermatitis, and other autoimmune-pattern toxicities — which is directly relevant to this candidate, since the predicted new "indication" overlaps with known irAEs of this drug class.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate rests on an L5 model-score-only signal with no supporting clinical trials or literature, and the evidence pack's own mechanistic analysis identifies a direct biological contradiction — PD-1 inhibition is more plausibly a cause of the predicted condition than a treatment for it. A blocking data gap (missing TFDA/SmPC safety data) also prevents this candidate from formally entering the S1 safety evaluation stage.

**To proceed, the following is needed:**
- Official SmPC/label safety data (warnings, contraindications, DDI) — currently a Blocking data gap
- Confirmed mechanism of action documentation from DrugBank — currently a High-severity data gap
- Independent preclinical or case-level evidence specifically supporting PD-1 inhibition in autoimmune cytopenias, since none currently exists
- Given the mechanistic contradiction, consider deprioritizing this signal in favor of other TxGNN candidates with stronger biological plausibility
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

