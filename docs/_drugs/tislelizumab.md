---
layout: default
title: Tislelizumab
parent: 僅模型預測 (L5)
nav_order: 438
evidence_level: L5
indication_count: 10
---

# Tislelizumab
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

# Tislelizumab: From Advanced Solid Tumours to Mixed-Type Autoimmune Hemolytic Anemia

## One-Sentence Summary

Tislelizumab is an anti-PD-1 (programmed cell death protein 1) monoclonal antibody used in advanced solid tumours (e.g., NSCLC, esophageal cancer). TxGNN predicts it may be effective for **Mixed-Type Autoimmune Hemolytic Anemia**, but this prediction is supported by **zero clinical trials** and **zero publications** — and the drug's known pharmacology points in the opposite direction: anti-PD-1 agents are documented to *cause*, not treat, autoimmune hemolytic anemia as an immune-related adverse event.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on file in Danish regulatory data (drug not marketed). Per literature evidence in this pack, tislelizumab is an anti-PD-1 therapy used for advanced solid tumours (e.g., NSCLC, esophageal cancer, cholangiocarcinoma) |
| Predicted New Indication | Mixed-Type Autoimmune Hemolytic Anemia |
| TxGNN Prediction Score | 93.76% |
| Evidence Level | L5 (model prediction only — no clinical trials or literature for this pairing) |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Formal mechanism-of-action documentation is flagged as a data gap in this evidence pack. However, literature collected under a related candidate (PMID 41268547) describes tislelizumab as a humanized IgG4 anti-PD-1 monoclonal antibody that blocks the PD-1/PD-L1 pathway to **reactivate** anti-tumour immunity — i.e., it removes a brake on immune activation.

Mixed-type autoimmune hemolytic anemia (AIHA) is a condition driven by *excessive* immune activity against red blood cells. A drug that removes immune checkpoints would be expected to worsen, not resolve, this kind of autoimmune process. This is not a theoretical concern: literature gathered elsewhere in this same evidence pack for a related candidate ("dermatitis," rank 5–6) documents that tislelizumab and other anti-PD-1 agents commonly **induce** immune-related adverse events — including Stevens-Johnson syndrome/toxic epidermal necrolysis, DRESS syndrome, and cytopenias/agranulocytosis (e.g., PMID 41346629, 40447060, 38910480). The same pattern applies to two other top-ranked candidates in this pack, "idiopathic aplastic anemia" and "drug-induced autoimmune hemolytic anemia" — both are conditions anti-PD-1 therapy is known to precipitate, not treat.

TxGNN's high score here most likely reflects graph proximity between the drug and these disease nodes learned from adverse-event/safety literature, rather than a genuine treatment relationship. The predicted direction of effect should be treated as inverted (a safety signal) until proven otherwise.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Denmark Market Information

Currently no marketing authorisation on file for Denmark. Tislelizumab has market status "Not marketed" with 0 registered authorisations.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information. No key warnings, contraindications, or drug-drug interaction data are on file in this evidence pack.

Note: although not part of the formal safety dataset, literature gathered elsewhere in this pack for a related candidate documents serious immune-related adverse events associated with tislelizumab, including SJS/TEN, DRESS syndrome, and agranulocytosis. This should be considered when assessing this drug's risk profile.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication has no clinical trial or literature support (L5), and the drug's known immune-activating mechanism runs directly counter to the pathophysiology of autoimmune hemolytic anemia. Corroborating literature elsewhere in this evidence pack shows the drug class induces this exact condition as an adverse event, indicating the TxGNN association most likely reflects a safety signal rather than a therapeutic effect.

**To proceed, the following is needed:**
- Confirmed mechanism-of-action and original-indication data (currently marked as data gaps)
- TFDA/SmPC-level warnings and contraindications (currently marked as blocking data gap)
- Independent pharmacological review to confirm or refute the directionality of the drug-disease relationship before any further evaluation
- If pursued at all, re-scope toward pharmacovigilance/adverse-event monitoring rather than efficacy testing
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

