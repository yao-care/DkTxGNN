---
layout: default
title: Besilesomab
parent: 僅模型預測 (L5)
nav_order: 61
evidence_level: L5
indication_count: 10
---

# Besilesomab
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

# Besilesomab: From Bone/Joint Infection Imaging to Diabetic Cataract

## One-Sentence Summary

Besilesomab (Scintimun®) is a radiolabelled murine Fab' antibody fragment targeting the NCA-90 antigen on granulocytes, approved by the EMA for diagnostic scintigraphic imaging of suspected bone and joint infections (osteomyelitis).
The TxGNN model predicts it may be effective for **Diabetic Cataract**, with a high model confidence score — however, **no clinical trials and no published literature** currently support this direction, and mechanistic analysis reveals fundamental incompatibility between the drug's target biology and cataract pathophysiology.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Scintigraphic imaging of suspected bone and joint infections (osteomyelitis) |
| Predicted New Indication | Diabetic Cataract |
| TxGNN Prediction Score | 98.52% |
| Evidence Level | L5 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on known pharmacological information, Besilesomab is a technetium-99m-labelled Fab' fragment (~48 kDa) of the murine monoclonal antibody BW 250/183. It binds specifically to NCA-90 (Non-Specific Cross-reacting Antigen 90), a carcinoembryonic antigen family member expressed on the surface of granulocytes. Following intravenous injection, it accumulates at sites of granulocyte infiltration — particularly bone and joint infections — enabling scintigraphic localisation. Its approved clinical role is entirely diagnostic, not therapeutic.

Diabetic cataract arises from a distinct and unrelated pathophysiological cascade: chronic hyperglycaemia drives the polyol pathway (aldose reductase-mediated sorbitol accumulation), advanced glycation of lens crystallin proteins, and oxidative stress within lens epithelial cells, collectively causing progressive lens opacification. The relevant therapeutic targets for cataract intervention are aldose reductase inhibition, antioxidant defence, and protein aggregation prevention — none of which intersect with granulocyte surface antigen biology.

There is furthermore a pharmacokinetic barrier: as a large antibody fragment (~48 kDa), Besilesomab is very unlikely to penetrate the aqueous humour–lens barrier in concentrations relevant to lens pathology. The TxGNN model's high confidence score here most likely reflects a graph-embedding artefact rather than a genuine biological signal. The internal mechanistic review in the Evidence Pack explicitly flags this prediction as **[Incompatible]** across all 10 top-ranked cataract subtypes.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Denmark Market Information

Besilesomab has no national marketing authorisations registered with the Danish Medicines Agency (Lægemiddelstyrelsen), and it is not currently on the Danish market.

> **Note for reviewers:** Besilesomab is marketed as **Scintimun®** under a centralised EMA marketing authorisation (EU/1/10/631/001) for adults with suspected bone/joint infections. It is a radiopharmaceutical requiring specialist nuclear medicine facilities, which may explain its limited national-level registration in smaller markets. Any potential repurposing pathway in Denmark would first require addressing this registration gap.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for Scintimun® for complete safety information. No drug interaction data was identified in the current Evidence Pack query.

> **Additional context:** As a diagnostic radiopharmaceutical, Besilesomab is administered as a single intravenous dose under controlled nuclear medicine conditions. Standard radiopharmaceutical precautions apply (radiation protection, pregnancy contraindication, handling per ALARA principles). These considerations are largely irrelevant to the proposed cataract indication, further underscoring the implausibility of this repurposing hypothesis.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model's prediction score is high (98.52%), but this is currently unsupported by any clinical trial, observational study, or published literature. More critically, the mechanistic analysis identifies a fundamental biological incompatibility: Besilesomab's granulocyte NCA-90 targeting mechanism has no known intersection with lens crystallin pathology, polyol pathway dysregulation, or oxidative stress mechanisms that drive diabetic cataract. Additionally, the drug is not marketed in Denmark, has no approved therapeutic indication anywhere, and is a diagnostic-only radiopharmaceutical. The risk-benefit calculus for pursuing this specific repurposing hypothesis is unfavourable at this stage.

**To proceed, the following would be needed:**

- **Mechanistic hypothesis generation:** Identify any plausible biological link between granulocyte/innate immune activity and lens opacification in diabetes (e.g., inflammatory infiltration in diabetic ocular tissue) before further investment
- **Preclinical feasibility data:** In vitro or animal model evidence that Besilesomab or its target (NCA-90/CEA family) modulates cataract-relevant endpoints
- **Model audit:** Investigate why TxGNN assigns top-10 predictions exclusively to cataract subtypes for this drug — this cluster pattern may indicate a graph topology artefact (e.g., shared node neighbours in the knowledge graph) rather than biological signal
- **MOA data retrieval:** Query DrugBank API and EMA SmPC to formally document mechanism of action and resolve the current data gap (DG002)
- **Safety data retrieval:** Obtain full SmPC warnings and contraindications from the EMA product page to resolve DG001 before any clinical feasibility assessment

---

*This report is generated for research reference only and does not constitute medical advice. All drug repurposing candidates require clinical validation before any application. Data cut-off: 2026-04-04.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

