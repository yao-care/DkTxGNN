---
layout: default
title: Enoxaparin
parent: 僅模型預測 (L5)
nav_order: 165
evidence_level: L5
indication_count: 2
---

# Enoxaparin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Enoxaparin: From VTE Prevention and Treatment to Autosomal Recessive Protein C Deficiency Thrombophilia

## One-Sentence Summary

Enoxaparin is a low molecular weight heparin (LMWH) anticoagulant widely used for prevention and treatment of venous thromboembolism (VTE), deep vein thrombosis, and acute coronary syndromes.
The TxGNN model predicts it may be effective for **thrombophilia due to protein C deficiency, autosomal recessive**, with a prediction confidence of **99.58%** — however, **no clinical trials** and **no published literature** currently exist specifically investigating this application.
This prediction is mechanistically plausible but remains at the hypothesis-generation stage and requires formal clinical investigation before further development.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | VTE prophylaxis and treatment, deep vein thrombosis, pulmonary embolism, acute coronary syndromes |
| Predicted New Indication | Thrombophilia due to Protein C deficiency, autosomal recessive |
| TxGNN Prediction Score | 99.58% |
| Evidence Level | L4 (model prediction; no clinical studies in this specific indication) |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Enoxaparin is a low molecular weight heparin that exerts its anticoagulant effect primarily by binding antithrombin III (ATIII), thereby potentiating the inhibition of Factor Xa and, to a lesser degree, Factor IIa (thrombin). Crucially, this mechanism is entirely independent of the Protein C anticoagulant pathway. Enoxaparin therefore has the theoretical capacity to provide compensatory anticoagulation in conditions where the Protein C pathway is dysfunctional.

Autosomal recessive Protein C deficiency results from biallelic loss-of-function mutations in the *PROC* gene, rendering Protein C unable to inactivate clotting Factors Va and VIIIa. The resulting severe hypercoagulable state markedly elevates thrombosis risk. In the most severe homozygous form, this manifests at birth as neonatal purpura fulminans — a life-threatening emergency characterised by widespread microvascular thrombosis and skin necrosis. The TxGNN model recognises that enoxaparin's ATIII-mediated mechanism directly targets the hypercoagulable downstream consequences of Protein C deficiency, effectively circumventing the deficient pathway.

It is important, however, to frame enoxaparin's potential role accurately: this represents an indirect compensatory mechanism — not correction of the underlying defect. The established first-line treatment for acute severe disease remains Protein C concentrate or fresh frozen plasma (FFP). Enoxaparin's clinical role, if any, would most likely be adjunctive — for example, in longer-term thromboprophylaxis in milder heterozygous carriers, or as bridging anticoagulation in settings where Protein C concentrate is unavailable. This contextual nuance is critical for clinical decision-making.

---

## Clinical Trial Evidence

Currently no related clinical trials are registered specifically investigating enoxaparin for thrombophilia due to protein C deficiency, autosomal recessive.

---

## Literature Evidence

Currently no related literature is available specifically investigating enoxaparin for thrombophilia due to protein C deficiency, autosomal recessive.

---

## Denmark Market Information

Enoxaparin is not currently registered with the Danish Medicines Agency (Lægemiddelstyrelsen) and holds no marketing authorisations in Denmark. There are no national or centrally authorised (EMA) products on record.

> **Note:** Enoxaparin is authorised in numerous other EU/EEA countries under the brand name Clexane (Sanofi) and various generics. Any use in Denmark would currently require either a named-patient import or a regulatory submission.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information. Key areas to review for this drug class include bleeding risk, heparin-induced thrombocytopenia (HIT), monitoring of anti-Factor Xa levels, and renal dose adjustment requirements.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
While the mechanistic basis for enoxaparin use in autosomal recessive Protein C deficiency thrombophilia is scientifically coherent — enoxaparin's ATIII-dependent pathway directly bypasses the Protein C defect — the current evidence level is L4 (model prediction only). There are no registered clinical trials, no published studies, and enoxaparin is not marketed in Denmark. This combination of factors warrants a Hold until foundational clinical evidence is established.

**To proceed, the following is needed:**

- **Systematic literature review:** Search for case reports, case series, and observational cohort data on LMWH use specifically in hereditary Protein C deficiency (both homozygous and heterozygous presentations)
- **Clinical expert consultation:** Engage Danish haematology and thrombosis specialists to evaluate clinical feasibility and unmet need versus existing standard of care (Protein C concentrate, warfarin, DOACs)
- **Regulatory pathway assessment:** Determine the pathway for enoxaparin authorisation in Denmark (named-patient import, centralised EMA procedure, or national application)
- **Safety profile review:** Obtain the full SmPC to characterise contraindications, key warnings, and drug interactions — currently a blocking data gap
- **Mechanism of action documentation:** Retrieve formal DrugBank MOA data to complete the mechanistic analysis
- **Positioning clarification:** Define whether the intended use is acute/emergency (where Protein C concentrate remains first-line) or long-term prophylaxis (where enoxaparin may have a more viable role)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

