---
layout: default
title: Zolmitriptan
parent: 僅模型預測 (L5)
nav_order: 479
evidence_level: L5
indication_count: 6
---

# Zolmitriptan
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Zolmitriptan: From Migraine to Migraine with Brainstem Aura

## One-Sentence Summary

Zolmitriptan is a selective 5-HT1B/1D receptor agonist (triptan) originally developed for the acute treatment of migraine. The TxGNN model assigns an extremely high prediction score (**99.99%**) to the rare subtype **migraine with brainstem aura**, but this signal is currently supported only by general migraine literature (**19 publications**, **0 subtype-specific clinical trials**) — and, importantly, existing headache-society guidance treats triptans as *relatively contraindicated* in this subtype due to a theoretical risk of posterior-circulation vasoconstriction. This is therefore a signal that requires caution rather than a straightforward repurposing opportunity.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Migraine (acute treatment, general/typical migraine) — not formally captured in Danish regulatory data below, as the product is not currently marketed in Denmark |
| Predicted New Indication | Migraine with Brainstem Aura |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L4 (mechanism/preclinical-level evidence only; no subtype-specific clinical trials) |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed structured mechanism-of-action data is not available from DrugBank for this record. Based on well-established pharmacology, zolmitriptan is a selective serotonin 5-HT1B/1D receptor agonist ("triptan"). It relieves acute migraine attacks through intracranial vasoconstriction and inhibition of trigeminovascular inflammatory mediator release (e.g., CGRP), and it is widely used for typical migraine, including migraine with typical (non-brainstem) aura.

Migraine with brainstem aura (formerly known as basilar-type migraine) is a rare subtype of migraine whose pathophysiology involves dysfunction of the vertebrobasilar (posterior cerebral) circulation. On a purely mechanistic level, the same 5-HT1B/1D receptor pathway that underlies zolmitriptan's efficacy in typical migraine is present throughout the trigeminovascular system, which is why the knowledge graph links zolmitriptan closely to this disease node.

However, this mechanistic proximity cuts both ways. Because triptans act via vasoconstriction, their use in migraine with brainstem aura is treated with caution in most clinical guidelines — including the American Headache Society's evidence assessment — which group this subtype together with hemiplegic migraine as conditions where triptans are relatively contraindicated, rather than indicated, out of concern for exacerbating posterior-circulation ischemia. The TxGNN score of 99.99% most likely reflects the model's general "migraine" cluster association rather than a subtype-level distinction, and should **not** be read as positive efficacy evidence for this specific indication.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for zolmitriptan in migraine with brainstem aura.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11903526](https://pubmed.ncbi.nlm.nih.gov/11903526/) | 2001 | Clinical review | Headache | Discusses triptan use in basilar migraine and migraine with prolonged aura — the most directly relevant reference to this subtype; addresses safety concerns with prominent neurologic symptoms |
| [25916333](https://pubmed.ncbi.nlm.nih.gov/25916333/) | 2015 | RCT/Meta-comparison | The Journal of Headache and Pain | Compares frovatriptan vs. rizatriptan, zolmitriptan, and almotriptan in migraine with aura; notes triptans are likely ineffective if taken during the aura phase itself |
| [22644173](https://pubmed.ncbi.nlm.nih.gov/22644173/) | 2012 | RCT subgroup analysis | Neurological Sciences | Double-blind, randomized subgroup analysis comparing frovatriptan 2.5mg vs. zolmitriptan 2.5mg specifically in migraine with aura (n=18) |
| [25600718](https://pubmed.ncbi.nlm.nih.gov/25600718/) | 2015 | Review/Guideline | Headache | American Headache Society evidence assessment of acute migraine pharmacotherapies, including triptan-class efficacy and cautions |
| [12083998](https://pubmed.ncbi.nlm.nih.gov/12083998/) | 2002 | Review | Expert Opinion on Pharmacotherapy | Reviews zolmitriptan's 5-HT1B/1D receptor agonism and clinical efficacy across migraine presentations |
| [10473025](https://pubmed.ncbi.nlm.nih.gov/10473025/) | 1999 | Review | Drugs | Comprehensive review of zolmitriptan's efficacy and tolerability in randomized, placebo-controlled migraine trials |
| [9399012](https://pubmed.ncbi.nlm.nih.gov/9399012/) | 1997 | Preclinical pharmacology | Cephalalgia | Describes zolmitriptan's central and peripheral 5HT1B/1D agonist activity and trigeminovascular inhibition — mechanistic basis for the prediction |
| [25538676](https://pubmed.ncbi.nlm.nih.gov/25538676/) | 2014 | Review | Frontiers in Neurology | Reviews treatment options for vestibular migraine, a related brainstem-associated migraine subtype |
| [17177580](https://pubmed.ncbi.nlm.nih.gov/17177580/) | 2007 | Cohort/Real-world | Clinical Drug Investigation | Postmarketing surveillance study of zolmitriptan 5mg nasal spray in real-world acute migraine treatment |
| [27910087](https://pubmed.ncbi.nlm.nih.gov/27910087/) | 2017 | Review | Headache | Review of menstrual migraine treatment options, including triptan therapy |

---

## Denmark Market Information

No marketing authorisations are currently recorded for zolmitriptan in Denmark. Market status is **Not marketed** (total licenses: 0). No national (Lægemiddelstyrelsen) or centralised (EMA) authorisation data is available in this evidence pack.

---

## Safety Considerations

- **Contextual safety caveat (not from formal SmPC data):** Triptans as a class, including zolmitriptan, are conventionally treated as relatively contraindicated in migraine with brainstem aura and hemiplegic migraine, due to a theoretical risk of exacerbating posterior-circulation vasoconstriction. This is a well-recognised class-level caution reflected in the clinical literature reviewed above, and should be weighed heavily against the TxGNN prediction score.

No structured drug-specific warnings, contraindications, or drug-drug interaction data were retrievable for this evidence pack. Please refer to the approved Summary of Product Characteristics (SmPC) for full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This is a safety-driven Hold, not merely an evidence-insufficiency Hold. There are no subtype-specific clinical trials, and although the TxGNN score is very high, the literature base is general-migraine evidence rather than brainstem-aura-specific evidence. More importantly, the mechanistic rationale itself flags that triptan vasoconstrictor activity is conventionally viewed as a relative contraindication — not a therapeutic rationale — for this specific migraine subtype. (Two additional low-ranked TxGNN predictions for this drug, atrophoderma vermiculata and ulerythema ophryogenesis, were evaluated as L5/S0 — model-prediction-only with no plausible mechanistic link or literature support — and are not recommended for further pursuit.)

**To proceed, the following is needed:**
- Official SmPC warnings/contraindications from the relevant regulatory source (currently a Blocking data gap)
- Formal, structured mechanism-of-action documentation from DrugBank or equivalent
- Neurology/headache-specialist review specifically addressing vasoconstrictive risk in posterior-circulation migraine subtypes before any further development
- Any subtype-specific case series, registry data, or controlled studies in migraine with brainstem aura (currently absent)
- Confirmation of registration/market status in Denmark should a regulatory pathway ever be considered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

