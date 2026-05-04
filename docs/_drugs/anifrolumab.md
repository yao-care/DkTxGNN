---
layout: default
title: Anifrolumab
parent: 僅模型預測 (L5)
nav_order: 40
evidence_level: L5
indication_count: 10
---

# Anifrolumab
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

# Anifrolumab: From Systemic Lupus Erythematosus to Diabetic Cataract

## One-Sentence Summary

Anifrolumab (Saphnelo) is a human monoclonal antibody targeting the type I interferon receptor subunit 1 (IFNAR1), approved internationally for moderate-to-severe systemic lupus erythematosus (SLE) in adult patients receiving standard therapy.
The TxGNN model predicts it may be effective for **Diabetic Cataract** with a prediction score of 98.50%; however, there are **0 clinical trials** and **0 publications** currently supporting this direction, and the mechanistic analysis embedded in the evidence pack raises serious concerns about the validity of this prediction.

> ⚠️ **Research Use Only.** This report is for research reference purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before any application.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Moderate-to-severe active systemic lupus erythematosus (SLE) in adults [international approval; not registered in Denmark] |
| Predicted New Indication | Diabetic Cataract |
| TxGNN Prediction Score | 98.50% |
| Evidence Level | L5 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data was not available in this evidence pack. Based on publicly known information, Anifrolumab is a fully human IgG1κ monoclonal antibody that binds to subunit 1 of the type I interferon receptor (IFNAR1), blocking the signalling of all type I interferons (IFN-α, IFN-β, IFN-ω). An elevated "interferon signature" — upregulated expression of IFN-stimulated genes — is observed in the majority of SLE patients and drives systemic inflammation, end-organ damage, and disease flares. By blocking IFNAR1, Anifrolumab suppresses downstream JAK/STAT-mediated IFN-stimulated gene expression and attenuates this pathological immune activation.

Diabetic cataract, the top-ranked predicted indication, is driven primarily by hyperglycaemia-induced activation of the aldose reductase (polyol) pathway, osmotic stress from sorbitol accumulation, advanced glycation end-product (AGE) formation, and oxidative damage to lens crystallins. These mechanisms are fundamentally distinct from type I IFN signalling. While there is emerging research exploring a role for IFN-α in promoting islet inflammation in type 2 diabetes, the causal chain from IFNAR1 blockade to prevention or treatment of lens opacification lacks any direct pathophysiological, preclinical, or clinical support.

A critical finding in this evidence pack is that **all 10 top-ranked predictions are variants of cataract** (diabetic, tetanic, mature, immature, craniostenosis-associated, and T2DM-associated). This tight cluster pattern strongly suggests a **knowledge graph topology artefact** — the TxGNN model appears to have assigned high scores based on graph neighbourhood proximity among ophthalmological disease nodes rather than genuine biological plausibility. Several of the predicted conditions (tetanic cataract caused by hypocalcaemia, craniostenosis-associated cataract driven by FGFR mutations) have no conceivable immunological mechanism and are explicitly flagged as model misclassifications in the evidence pack rationale. Healthcare professionals should interpret these high TxGNN scores with considerable caution.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Denmark Market Information

Anifrolumab is not currently registered or marketed in Denmark. There are no active marketing authorisations granted by the Danish Medicines Agency (Laegemiddelstyrelsen) or via the centralised EMA procedure for this drug in the Danish market at the time of this report (data cut-off: 2026-04-04).

For contextual reference: Anifrolumab (Saphnelo, AstraZeneca) received EMA centralised marketing authorisation within the European Union in February 2023 for the treatment of moderate-to-severe active systemic lupus erythematosus in adult patients who are receiving standard therapy. Danish clinicians seeking access may explore named-patient or compassionate use pathways through Laegemiddelstyrelsen. Current EMA authorisation status should be verified at the time of use via the EMA product page.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information. Full warning, contraindication, and drug interaction data were not available in this evidence pack and should be retrieved from the EMA-approved Saphnelo SmPC prior to any clinical consideration.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All 10 TxGNN-predicted indications for Anifrolumab are cataract subtypes, none have supporting clinical trials or peer-reviewed literature, and the mechanistic analysis in this evidence pack explicitly identifies these predictions as likely knowledge graph false positives with no plausible IFNAR1-to-lens biology linkage. This repurposing hypothesis does not warrant further development at this stage.

**To proceed, the following would be needed:**

- Identification of a biologically plausible mechanistic link between IFNAR1 blockade and cataractogenesis (e.g., a peer-reviewed preclinical study demonstrating type I IFN pathway involvement in lens opacification)
- Re-evaluation of TxGNN model output for Anifrolumab using de-biased or re-weighted knowledge graph edges to rule out topology artefacts
- Retrieval of full safety profile from the approved EMA SmPC, including key warnings, contraindications, and drug interaction data
- If a credible mechanistic hypothesis emerges: a prospective feasibility assessment including route-of-administration compatibility (current approved route: intravenous infusion) and target patient population definition

---

*Report generated: 2026-04-04 | Evidence Pack: TW-DB11976-multi v4 | Data cut-off: 2026-04-04*
*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

