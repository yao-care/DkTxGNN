---
layout: default
title: Carbetocin
parent: 僅模型預測 (L5)
nav_order: 91
evidence_level: L5
indication_count: 4
---

# Carbetocin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Carbetocin: From Prevention of Postpartum Haemorrhage to Isotretinoin-like Syndrome

## One-Sentence Summary

Carbetocin is a synthetic long-acting oxytocin receptor agonist, used in numerous countries for the prevention of uterine atony and postpartum haemorrhage following caesarean section.
The TxGNN model predicts it may be relevant to **Isotretinoin-like Syndrome** with a prediction score of **99.15%**, however **no clinical trials** and **no supporting publications** have been identified — and the underlying mechanistic rationale is not biologically well-established.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Prevention of postpartum haemorrhage / uterine atony (not currently registered in Denmark) |
| Predicted New Indication | Isotretinoin-like Syndrome |
| TxGNN Prediction Score | 99.15% |
| Evidence Level | L5 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Carbetocin is a synthetic structural analogue of oxytocin, acting as a selective oxytocin receptor (OXTR) agonist. Upon binding to uterine OXTR, it elicits sustained myometrial contractions. Compared to natural oxytocin, carbetocin has a significantly longer half-life (approximately 40 minutes versus 3–5 minutes), which supports its single-dose clinical use. It is authorised in multiple countries outside Denmark for prevention of excessive bleeding after delivery, particularly following caesarean section. Detailed mechanism of action data from DrugBank was not available in this Evidence Pack, but its receptor pharmacology is well-characterised in the published literature.

Isotretinoin-like syndrome — also referred to as retinoic acid embryopathy — is not a disease that a patient is treated for in the conventional pharmacological sense. It is a teratogenic developmental syndrome arising from foetal exposure to high-dose vitamin A derivatives (principally isotretinoin) during early pregnancy. It is characterised by craniofacial defects, conotruncal cardiac malformations, CNS abnormalities, and thymic dysplasia, all attributable to disruption of the retinoic acid signalling axis (RAR/RXR pathway).

The predicted mechanistic connection between carbetocin and isotretinoin-like syndrome is not biologically plausible on current evidence. Carbetocin's mechanism — oxytocin receptor agonism — has no known direct involvement in the retinoic acid signalling pathway responsible for this syndrome. Although oxytocin plays modulatory roles in neurodevelopment, no published pharmacological rationale links OXTR agonism to the treatment, prevention, or modification of retinoic acid embryopathy. The high TxGNN prediction score (0.9914) most likely reflects shared knowledge graph topology in the "congenital developmental abnormalities" node cluster, rather than a genuine pharmacological relationship. This prediction should be interpreted with considerable caution.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Denmark Market Information

Carbetocin is not currently registered or marketed in Denmark. No marketing authorisations have been issued by the Danish Medicines Agency (Lægemiddelstyrelsen), and no centralised EMA authorisations are active for this market at the time of data compilation (cut-off: 2026-04-04).

> **Note for context:** Carbetocin (brand name Pabal/Duratocin) holds regulatory approvals in several other countries for prevention of postpartum haemorrhage. The absence of a Danish authorisation means that any proposed clinical use in Denmark would require a named-patient or compassionate use application.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This prediction rests solely on TxGNN model output (Evidence Level L5) with zero supporting clinical trials or published literature. Critically, the mechanistic rationale is not biologically credible — carbetocin's oxytocin receptor agonist mechanism has no established connection to the retinoic acid signalling disruption that underlies isotretinoin-like syndrome, which is a teratogenic developmental disorder rather than a tractable drug target.

**To proceed, the following is needed:**

- A credible mechanistic hypothesis linking oxytocin receptor agonism to retinoic acid signalling or to congenital craniofacial/cardiac developmental pathways
- At least one preclinical study, animal model, or observational report demonstrating a biologically relevant effect of carbetocin on this syndrome or its component defects
- Clarification of the intended therapeutic role: is carbetocin proposed as a treatment, a preventive agent, or a developmental modulator in this context?
- Full safety data for carbetocin, including complete SmPC text, contraindications, and drug-drug interaction profile (all currently unavailable in this Evidence Pack)
- Re-evaluation of the knowledge graph for potential false-positive node associations in the "congenital developmental abnormality" cluster before investing further research resources
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

