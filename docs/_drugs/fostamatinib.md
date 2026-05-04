---
layout: default
title: Fostamatinib
parent: 僅模型預測 (L5)
nav_order: 195
evidence_level: L5
indication_count: 10
---

# Fostamatinib
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

# Fostamatinib: From Immune Thrombocytopenia (ITP) to Autosomal Thrombocytopenia with Normal Platelets

## One-Sentence Summary

Fostamatinib (brand name: Tavalisse/Tavlesse) is an oral spleen tyrosine kinase (SYK) inhibitor approved for the treatment of chronic immune thrombocytopenia (ITP) in adults who have had an insufficient response to a previous therapy.
The TxGNN model predicts it may be effective for **Autosomal Thrombocytopenia with Normal Platelets** — a rare inherited platelet disorder — with a prediction confidence of **99.45%**.
However, **no clinical trials and no disease-specific publications** currently support this repurposing direction; the prediction reflects knowledge graph clustering of thrombocytopenia-related disease nodes rather than direct mechanistic evidence.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Chronic immune thrombocytopenia (ITP) in adults |
| Predicted New Indication | Autosomal Thrombocytopenia with Normal Platelets |
| TxGNN Prediction Score | 99.45% |
| Evidence Level | L4 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the current evidence pack. Based on known pharmacology, Fostamatinib is a selective inhibitor of spleen tyrosine kinase (SYK). In chronic immune thrombocytopenia (ITP), activated SYK mediates Fcγ receptor (FcγR)-driven macrophage destruction of antibody-coated platelets. By inhibiting SYK, Fostamatinib reduces this immune-mediated clearance and thereby raises circulating platelet counts. This mechanism has been clinically validated across multiple Phase 3 trials leading to FDA (2018) and EMA approval.

Autosomal Thrombocytopenia with Normal Platelets (OMIM reference) is a genetically inherited condition caused by germline mutations affecting platelet production or survival — not by autoantibody-mediated platelet destruction. Because the underlying aetiology is fundamentally different from ITP, the SYK-FcγR inhibition mechanism has **limited direct applicability** to this inherited disorder.

That said, SYK signalling is known to participate in megakaryocyte differentiation and platelet biogenesis pathways. This opens a theoretical — but currently unproven — hypothesis that SYK modulation could influence platelet production in genetic thrombocytopenias. The TxGNN high score (99.45%) most plausibly reflects the model's knowledge graph clustering effect among thrombocytopenia-related disease nodes, and should be interpreted as a hypothesis-generating signal requiring preclinical validation before any clinical consideration.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Fostamatinib in Autosomal Thrombocytopenia with Normal Platelets.

---

## Literature Evidence

Currently no related literature available for Fostamatinib in Autosomal Thrombocytopenia with Normal Platelets.

---

## Denmark Market Information

Fostamatinib is currently **not marketed in Denmark** and holds no marketing authorisations from the Danish Medicines Agency (Laegemiddelstyrelsen). No centralised European Marketing Authorisation (EMA) procedure listing is present in the evidence pack.

> **Note for prescribers:** Fostamatinib is approved in the EU as **Tavlesse** (R-Pharm) for chronic ITP in adult patients. The EMA-approved Summary of Product Characteristics (SmPC) is available via the EMA product database and constitutes the authoritative reference for dosing, contraindications, and safety in any potential named-patient or compassionate use context in Denmark.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for Tavlesse (EMA) for complete safety information, including warnings, contraindications, and drug interactions.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Autosomal Thrombocytopenia with Normal Platelets is a genetically inherited platelet disorder with a pathophysiology distinct from the immune-mediated ITP for which Fostamatinib is approved; there is no clinical trial evidence, no disease-specific literature, and no confirmed mechanistic link to support advancing this repurposing candidate at this stage.

**To proceed, the following is needed:**

- **Preclinical evidence:** Establish whether SYK pathway dysregulation is present in the specific genetic variant(s) underlying this condition (e.g., in vitro megakaryocyte differentiation assays or patient-derived iPSC models)
- **Mechanistic data (MOA):** Retrieve full Fostamatinib pharmacology from DrugBank API (currently flagged as Data Gap DG002) to refine mechanistic plausibility assessment
- **Safety profile review:** Obtain and review the Tavlesse SmPC from EMA (Data Gap DG001 equivalent) — particularly hepatotoxicity, hypertension, and neutropenia signals relevant to any investigational use
- **Genetic subtype mapping:** Define the specific OMIM mutation(s) and determine whether any involve SYK-related signalling cascades before framing a research hypothesis
- **Orphan disease pathway assessment:** If preclinical data are supportive, evaluate eligibility for EU orphan designation prior to any clinical development planning
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

