---
layout: default
title: Cabotegravir
parent: 僅模型預測 (L5)
nav_order: 82
evidence_level: L5
indication_count: 10
---

# Cabotegravir
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

# Cabotegravir: From HIV-1 Infection to Rheumatoid Arthritis

## One-Sentence Summary

Cabotegravir is an HIV-1 integrase strand transfer inhibitor (INSTI), approved in multiple countries for the treatment of HIV-1 infection (in combination with rilpivirine) and as long-acting injectable pre-exposure prophylaxis (PrEP) against HIV-1.
The TxGNN model predicts it may be effective for **Rheumatoid Arthritis**, with a prediction score of **99.45%**.
However, **no supporting clinical trials or published literature** currently exist for this indication, and the mechanistic rationale is considered extremely weak.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | HIV-1 infection treatment and pre-exposure prophylaxis (PrEP) |
| Predicted New Indication | Rheumatoid Arthritis |
| TxGNN Prediction Score | 99.45% |
| Evidence Level | L5 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on known pharmacological information, Cabotegravir belongs to the integrase strand transfer inhibitor (INSTI) class of antiretroviral drugs. It works by blocking HIV-1 integrase — a viral-specific enzyme — thereby preventing integration of viral DNA into the host cell genome. It has no known direct immunomodulatory or anti-inflammatory targets.

The mechanistic link between Cabotegravir and rheumatoid arthritis (RA) is considered extremely weak. RA pathophysiology is driven by TNF-α/IL-6 signalling, JAK-STAT pathway dysregulation, T-cell activation, and synovial hyperplasia — none of which are known targets of Cabotegravir. A very indirect hypothesis exists: some INSTIs have been observed to modulate NF-κB inflammatory signalling, but there are no systematic mechanistic data supporting this in the context of RA.

The high TxGNN score most likely reflects topological proximity in the knowledge graph between HIV-related immune dysregulation nodes and autoimmune disease nodes, rather than a genuine pharmacological relationship. This is a common source of false-positive predictions in graph-based models, particularly when a drug node is highly connected to immune-related pathways that also intersect with autoimmune disease clusters.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Denmark Market Information

Cabotegravir is currently **not registered** with the Danish Medicines Agency (Lægemiddelstyrelsen) and holds no marketing authorisations in Denmark. No centralised EMA authorisation for this product is reflected in the current dataset.

> **Note for clinicians:** Cabotegravir is approved in other jurisdictions (e.g. EMA authorisation for Vocabria/Cabenuva and Apretude in the USA and UK). Danish healthcare professionals should consult the EMA product information or the relevant Summary of Product Characteristics (SmPC) for approved indications.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no clinical trial evidence, no published literature, and no credible mechanistic basis supporting the use of Cabotegravir in rheumatoid arthritis. The TxGNN prediction score is high (99.45%), but this is assessed to reflect a knowledge graph artefact — specifically, topological overlap between HIV immune dysregulation nodes and autoimmune disease nodes — rather than a true pharmacological signal. Furthermore, Cabotegravir is not marketed in Denmark, and all safety reference data are currently unavailable.

**To proceed, the following would be needed:**

- Retrieve and review the full SmPC / prescribing information for Cabotegravir (Vocabria / Cabenuva / Apretude) to document MOA, warnings, contraindications, and drug interactions
- Conduct a systematic literature search specifically investigating any INSTI class effects on inflammatory or autoimmune pathways (NF-κB, TNF-α, IL-6), independent of HIV context
- Evaluate whether any in vitro or preclinical data exist suggesting INSTI activity in RA-relevant cell models (synoviocytes, activated T cells)
- If any preliminary mechanistic evidence is found, escalate evidence level from L5 to L4 before reconsidering the decision stage
- Consider whether the high-scoring predictions for the other four indications (sclerosing cholangitis, bronchitis, colobomatous microphthalmia-rhizomelic dysplasia syndrome, severe nonproliferative diabetic retinopathy) share similar knowledge-graph artefact characteristics — all five predictions currently carry L5 evidence and a Hold recommendation, with mechanistic rationale assessed as weak or absent

> ⚠️ **Disclaimer:** This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before application. All predictions should be interpreted in the context of established clinical evidence.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

