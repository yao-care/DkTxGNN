---
layout: default
title: Cannabidiol
parent: 僅模型預測 (L5)
nav_order: 87
evidence_level: L5
indication_count: 10
---

# Cannabidiol
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

# Cannabidiol: From Epilepsy to Restless Legs Syndrome

> **Disclaimer:** This report is intended for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before any therapeutic application.

---

## One-Sentence Summary

Cannabidiol (CBD) is a non-psychoactive phytocannabinoid internationally approved for treatment-resistant epilepsy (Dravet syndrome and Lennox-Gastaut syndrome), though it currently holds no marketing authorisation in Denmark.
The TxGNN model predicts it may be effective for **Restless Legs Syndrome (RLS)**, with a prediction score of **96.17%** and **4 clinical trials** registered — including one Phase 2 RCT directly targeting idiopathic RLS — providing a plausible mechanistic and emerging clinical basis for this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Epilepsy (Dravet syndrome / Lennox-Gastaut syndrome) — international approval; not currently registered in Denmark |
| Predicted New Indication | Restless Legs Syndrome |
| TxGNN Prediction Score | 96.17% |
| Evidence Level | L2 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action (MOA) data was not available in the current evidence pack. Based on established pharmacological literature, CBD acts through multiple neuromodulatory targets: it modulates the endocannabinoid system (ECS) via CB1 and CB2 receptors without acting as a direct agonist, inhibits GABA and adenosine reuptake, activates TRPV1 channels, and antagonises GPR55. It is approved as Epidiolex/Epidyolex (EMA centralised authorisation) for seizure reduction in Dravet syndrome and Lennox-Gastaut syndrome.

Restless Legs Syndrome is a sensorimotor disorder whose core pathophysiology involves striatal dopaminergic dysfunction, impaired spinal inhibitory neurotransmission, iron metabolism disturbances, and heightened central hyperarousal. CBD's potential relevance to RLS is mechanistically grounded: (1) the ECS directly modulates striatal dopamine release — the primary dysregulation in RLS; (2) GABA reuptake inhibition may reduce sensory dysaesthesia and periodic limb movements; (3) CB1 receptor-mediated spinal inhibitory signalling may attenuate the pathological urge-to-move; and (4) emerging preclinical evidence suggests ECS involvement in iron homeostasis, which intersects with the well-established iron-deficiency aetiology of RLS.

While the mechanistic pathway from epilepsy to RLS is not direct, both conditions share features of neurological hyperexcitability and disrupted inhibitory signalling. CBD's broad neuromodulatory profile — particularly its dopaminergic and GABAergic activity — provides a pharmacologically plausible basis for the TxGNN prediction, with mechanistic plausibility rated moderate-to-high.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT07224932](https://clinicaltrials.gov/study/NCT07224932) | Phase 2 | Not Yet Recruiting | 60 | Randomised, double-blind, placebo-controlled parallel RCT of high-CBD cannabis extract (BRC-002) specifically in idiopathic RLS patients; primary endpoint: tolerability and safety; start planned December 2025 — the only direct RLS trial in this dataset |
| [NCT05092191](https://clinicaltrials.gov/study/NCT05092191) | Phase 2 | Recruiting | 250 | Cannabinoids vs current standard treatments for symptom relief in Multiple Sclerosis (Canada); RLS is a recognised MS comorbidity and included as a secondary symptom endpoint; results not yet available |
| [NCT02818777](https://clinicaltrials.gov/study/NCT02818777) | Phase 2 | Completed | 13 | Double-blind, placebo-controlled crossover RCT of CBD (GWP42003) on tremor in Parkinson's Disease; completed November 2017; small sample size limits statistical power, but crossover design enhances within-subject sensitivity |
| [NCT03582137](https://clinicaltrials.gov/study/NCT03582137) | Phase 2 | Completed | 74 | Double-blind, placebo-controlled parallel RCT of CBD on motor symptoms in Parkinson's Disease; primary endpoint: MDS-UPDRS Part III motor score; completed January 2022; largest completed CBD motor-disorder RCT in this dataset |

> **Note:** NCT02818777 and NCT03582137 are Parkinson's Disease trials, not direct RLS trials. Their inclusion reflects mechanistic and phenotypic overlap between dopaminergic movement disorders; findings should not be directly extrapolated to idiopathic RLS populations.

---

## Literature Evidence

Currently no RLS-specific literature is available in this evidence pack.

---

## Denmark Market Information

Cannabidiol is currently **not marketed in Denmark** and holds no national or EMA centralised marketing authorisation registered in this dataset (0 licences). Danish healthcare professionals considering off-label use or research access should note the following:

| Consideration | Detail |
|--------------|--------|
| Epidyolex (EMA) | EMA centralised authorisation exists for Dravet syndrome/LGS; validity in Denmark subject to national reimbursement and import procedures |
| Access pathway | Named patient / hospital exemption application to Lægemiddelstyrelsen may be required |
| Regulatory contact | Lægemiddelstyrelsen — [www.laegemiddelstyrelsen.dk](https://www.laegemiddelstyrelsen.dk) |

---

## Safety Considerations

Specific safety data for this candidate is not currently available in this evidence pack — all safety fields are pending data retrieval. Please refer to the approved Summary of Product Characteristics (SmPC) for Epidiolex/Epidyolex for full safety information.

Clinically relevant safety signals from published literature and the SmPC include:
- **Hepatotoxicity**: Elevated transaminases reported, particularly when co-administered with valproate — liver function monitoring required
- **CNS effects**: Somnolence, fatigue, and sedation, especially at higher doses
- **Gastrointestinal**: Decreased appetite, diarrhoea, and vomiting
- **Drug interactions**: CBD is a CYP2C19 inhibitor and CYP3A4 substrate; DDI profiling was not returned in the current data pull and should be conducted prior to any clinical use

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The TxGNN model assigns a high prediction score (96.17%), mechanistic plausibility is moderate-to-high, and the research landscape is actively evolving — a dedicated Phase 2 RLS RCT (NCT07224932) is registered and expected to provide direct efficacy and safety data. However, no completed trials have directly evaluated CBD in idiopathic RLS, and all completed Phase 2 RCTs in this dataset are Parkinson's Disease studies. A "Proceed with Guardrails" decision is appropriate: the hypothesis is scientifically credible and worth advancing, but requires stronger direct evidence before clinical adoption.

**To proceed, the following is needed:**

- **Primary**: Await and review results from NCT07224932 (direct RLS Phase 2 RCT; originally planned for completion February 2026 — confirm recruitment status)
- **Regulatory**: Determine current EMA/Lægemiddelstyrelsen access pathway for CBD in Denmark; clarify whether Epidyolex centralised authorisation is recognised or requires separate national application
- **Safety**: Retrieve full SmPC warnings, contraindications, and DDI profile for CBD (currently data gap); assess hepatotoxicity risk in RLS patient population
- **Positioning**: Define CBD's therapeutic role relative to established first-line RLS treatments (dopamine agonists: pramipexole, ropinirole; α₂δ ligands: gabapentin enacarbil, pregabalin) — adjunct vs. alternative
- **RLS subtype**: Clarify evidence applicability to idiopathic vs. secondary (iron deficiency, renal, MS-associated) RLS subtypes, given the mechanistic intersection with iron metabolism
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

