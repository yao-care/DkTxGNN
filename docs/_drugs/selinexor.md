---
layout: default
title: Selinexor
parent: 僅模型預測 (L5)
nav_order: 396
evidence_level: L5
indication_count: 10
---

# Selinexor
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

# Selinexor: From an Undocumented Original Indication to Progesterone-Receptor Negative Breast Cancer

## One-Sentence Summary

Selinexor (DrugBank DB11942) is an XPO1/CRM1 nuclear export inhibitor; its documented original indication is not available in this evidence pack, and the drug is not currently marketed in Denmark. The TxGNN model surfaced several breast-cancer-related predictions, but only **Progesterone-Receptor Negative Breast Cancer** is backed by an actual completed clinical trial — a small, investigator-initiated Phase 2 study (n=10) — while the model's highest-scoring output ("drug-induced osteoporosis") is flagged in the evidence pack itself as likely model noise with no supporting mechanism, trials, or literature.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (`original_indications` empty; not marketed in Denmark) |
| Predicted New Indication | Progesterone-Receptor Negative Breast Cancer |
| TxGNN Prediction Score | 97.20% |
| Evidence Level | L2 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for Selinexor is not available in the Laegemiddelstyrelsen registration record used to build this evidence pack (flagged as a High-severity data gap). Based on the analysis accompanying this prediction, Selinexor is understood to act as a selective inhibitor of nuclear export (SINE), targeting XPO1/CRM1. This forces tumour-suppressor proteins such as p53, FOXO3a and IκB to remain in the nucleus and reduces translation of oncoproteins such as MYC and cyclin D1 — a mechanism with preclinical support across multiple solid tumours, including breast cancer.

Progesterone-receptor negative breast cancer typically carries a poorer prognosis and responds less well to hormonal therapy. An XPO1-inhibition mechanism offers a non-hormone-dependent therapeutic rationale, which is consistent with why this candidate — among the model's breast-cancer-related outputs — has actual clinical investigation behind it (see Clinical Trial Evidence below).

It is worth noting that this was not the model's top-scoring output. The highest-ranked prediction, "drug-induced osteoporosis" (score 99.22%), is explicitly annotated in the evidence pack as lacking any bone-protective mechanism — Selinexor's known adverse-effect profile (anorexia, weight loss, fatigue, thrombocytopenia) runs counter to such an indication — and has zero supporting trials or literature. Similarly, HER2-positive breast carcinoma, normal breast-like subtype, and PR-positive breast cancer show no direct mechanistic or clinical-trial support and appear to reflect generic "breast cancer" node proximity in the knowledge graph rather than subtype-specific signal. Progesterone-receptor negative breast cancer is therefore presented here as the most credible candidate, being the only one grounded in an actual completed trial.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02402764](https://clinicaltrials.gov/study/NCT02402764) | Phase 2 | Completed | 10 | Investigator-initiated, single-arm study of selinexor (KPT-330) in metastatic triple-negative breast cancer, assessing efficacy, safety and tolerability. Small sample size (n=10) limits statistical power; graded as exploratory rather than confirmatory evidence. |

---

## Literature Evidence

Currently no related literature available.

---

## Denmark Market Information

Selinexor is not currently marketed in Denmark (Laegemiddelstyrelsen market status: **Not marketed**) and holds no national or centralised (EMA) marketing authorisations on record in this evidence pack.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (XPO1/CRM1 selective inhibitor of nuclear export, SINE) |
| Myelosuppression Risk | Signal noted in evidence-pack analysis: thrombocytopenia listed among Selinexor's known safety issues; not yet confirmed against an official label |
| Emetogenicity Classification | Please refer to the Summary of Product Characteristics (SmPC) warnings and precautions |
| Monitoring Items | Complete blood count (with attention to platelets), given the noted thrombocytopenia signal; liver and renal function |
| Handling Protection | Please refer to the Summary of Product Characteristics (SmPC) and institutional cytotoxic/hazardous-drug handling policy |

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information — key warnings, contraindications and drug-drug interaction data are not yet available in this evidence pack (DDI query returned no results).

Note: the evidence pack's analytical commentary (not verified against an official label) references known Selinexor-associated adverse effects — anorexia, weight loss, fatigue, and thrombocytopenia — relevant for future monitoring-plan design.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The lead candidate (progesterone-receptor negative breast cancer) has a plausible mechanism and one completed but small, single-arm Phase 2 trial (L2, n=10) — a promising but early-stage signal. Progression is currently blocked by a Blocking-severity data gap (missing Danish/TFDA-equivalent label warnings and contraindications, which prevents even an initial safety screen) and a High-severity gap in documented mechanism of action. The model's other, higher-scoring breast-cancer and osteoporosis predictions lack any clinical or mechanistic support and are assessed as likely model artifacts rather than genuine repurposing signals.

**To proceed, the following is needed:**
- Official Danish/EU SmPC warnings, contraindications and DDI data for Selinexor (currently blocking initial safety screening)
- Confirmed original indication and mechanism-of-action documentation from DrugBank or regulatory sources
- Larger controlled (ideally randomized) trial data beyond the single-arm n=10 study before any guardrail-based progression is considered
- Re-review of the other high-score, evidence-free predictions (drug-induced osteoporosis, HER2-positive breast carcinoma, normal breast-like subtype, PR-positive breast cancer) to confirm or formally reject them as model noise
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

