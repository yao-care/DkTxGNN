---
layout: default
title: Efmoroctocog Alfa
parent: 僅模型預測 (L5)
nav_order: 156
evidence_level: L5
indication_count: 10
---

# Efmoroctocog Alfa
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

# Efmoroctocog Alfa: From Haemophilia A to Pseudo-von Willebrand Disease

## One-Sentence Summary

Efmoroctocog alfa is a recombinant coagulation Factor VIII Fc fusion protein (rFVIIIFc), approved in multiple countries (e.g., EU as Elocta, US as Eloctate) for the prevention and treatment of bleeding episodes in patients with Haemophilia A.
The TxGNN model predicts it may be effective for **Pseudo-von Willebrand Disease**, a rare platelet-type bleeding disorder mechanistically linked to the Factor VIII–von Willebrand factor (vWF) axis.
Currently, **no clinical trials** and **no publications** specifically studying efmoroctocog alfa in this indication have been identified, meaning this prediction is supported by model inference only.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Haemophilia A (congenital Factor VIII deficiency) — prevention and treatment of bleeding episodes |
| Predicted New Indication | Pseudo-von Willebrand Disease |
| TxGNN Prediction Score | 99.997% |
| Evidence Level | L5 |
| Denmark Market Status | Not Marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Efmoroctocog alfa (rFVIIIFc) is a recombinant Factor VIII fused to the Fc region of human IgG1, which extends its circulating half-life approximately 1.5-fold compared to standard Factor VIII products. Its primary approved mechanism is to temporarily replace the deficient or absent endogenous FVIII in patients with Haemophilia A, thereby restoring normal secondary haemostasis. Critically, Factor VIII does not act in isolation: it circulates in plasma bound to von Willebrand factor (vWF), which both protects FVIII from premature proteolytic degradation and delivers it to sites of vascular injury.

Pseudo-von Willebrand disease (platelet-type vWD) is caused by a gain-of-function mutation in the platelet glycoprotein Ibα (GPIbα) receptor, which binds vWF with abnormally high affinity. This leads to spontaneous platelet clumping, consumption of high-molecular-weight vWF multimers, and secondary reduction in plasma FVIII levels — because FVIII loses its vWF chaperone. The resulting phenotype is therefore a combined platelet and secondary coagulation defect, with low FVIII activity being a clinical feature in severe cases. Providing exogenous rFVIIIFc could theoretically compensate for the FVIII component of this combined defect.

The TxGNN knowledge-graph model has likely identified this connection through the shared biological node of vWF and the co-occurrence of FVIII deficiency as a downstream consequence of pseudo-vWD. While the mechanistic rationale is biologically coherent, pseudo-vWD is currently managed primarily with platelet transfusions or desmopressin (DDAVP), and there is no established clinical precedent for using FVIII concentrate as a therapeutic strategy in this indication. The prediction therefore warrants exploratory investigation rather than immediate clinical translation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

> **Note:** No drug interaction data, contraindications, or key warnings were retrievable from the current evidence pack. Before any clinical use, the full SmPC for Elocta/Eloctate (efmoroctocog alfa) should be consulted, with particular attention to immunogenicity risk (inhibitor development against FVIII), hypersensitivity reactions, and cardiovascular monitoring in at-risk populations.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model yields an extremely high prediction score (99.997%), and the biological link between Factor VIII, vWF, and pseudo-von Willebrand disease is mechanistically coherent; however, there is currently zero supporting clinical trial or published literature evidence for efmoroctocog alfa in this indication, classifying this as a pure model prediction (L5). A Hold decision is appropriate until at least preclinical or case-series data are available to justify resource investment.

**To proceed, the following is needed:**

- **Mechanism of action confirmation:** Obtain formal MOA data from DrugBank (DB11607) to document the FVIII–vWF interaction pathway and its potential relevance to pseudo-vWD pathophysiology.
- **Expert clinical opinion:** Consult a haematologist or coagulation specialist to assess whether supplementing FVIII in pseudo-vWD is physiologically rational given the primary platelet GPIbα defect.
- **Regulatory history review:** Confirm whether any compassionate use, named-patient, or off-label use of FVIII concentrates in pseudo-vWD has been documented in EU/EMA or Laegemiddelstyrelsen records.
- **Evidence gap remediation:** Conduct a targeted literature review using broader search terms (e.g., "Factor VIII concentrate AND pseudo-von Willebrand disease", "platelet-type vWD AND factor replacement") to rule out unpublished or grey-literature evidence missed by the automated collectors.
- **Denmark market access pathway:** Since efmoroctocog alfa is not currently registered in Denmark, a market authorisation pathway via the EMA centralised procedure (Elocta is EMA-approved) or a named-patient import application would be required if clinical evaluation proceeds.
- **Safety data acquisition:** Download and parse the TFDA/EMA product information to complete the safety profile before any clinical programme is initiated.

---

> ⚠️ **Disclaimer:** This report is generated for research reference purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before application. Data cutoff: 2026-04-05.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

