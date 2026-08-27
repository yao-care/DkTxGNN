---
layout: default
title: Ticagrelor
parent: 僅模型預測 (L5)
nav_order: 432
evidence_level: L5
indication_count: 10
---

# Ticagrelor
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

# Ticagrelor: From Acute Coronary Syndrome to Intracranial Arteriosclerosis

## One-Sentence Summary

Ticagrelor is an oral, reversible P2Y12 platelet inhibitor used as antiplatelet therapy in acute coronary syndrome and related atherothrombotic conditions. The TxGNN model predicts it may also be effective for **Intracranial Arteriosclerosis** (intracranial atherosclerotic disease, ICAD), with **11 clinical trials** and **3 publications** currently identified in support of this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acute Coronary Syndrome (ACS) — inferred from trial/mechanistic context; no structured indication text is present in this Evidence Pack |
| Predicted New Indication | Intracranial Arteriosclerosis (Intracranial Atherosclerotic Disease) |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L2 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, a structured mechanism-of-action record is not available in this Evidence Pack (`original_moa` is a data gap, pending DrugBank API lookup — see DG002). Based on the mechanistic reasoning captured alongside this prediction, ticagrelor is a reversibly-binding P2Y12 receptor antagonist that inhibits ADP-induced platelet activation and aggregation — the standard antiplatelet mechanism used in atherothrombotic disease (ACS, post-PCI, and ischemic stroke prevention).

Intracranial arteriosclerosis (ICAD) causes ischemic stroke through the same underlying pathology as ticagrelor's established use: atherosclerotic plaque formation and platelet-driven thrombus formation, here occurring in intracranial vessels rather than coronary arteries. Because ticagrelor's core mechanism directly targets this thrombotic pathway, its extension into ICAD represents an application of an already-validated antiplatelet principle to a different, but mechanistically related, vascular bed — rather than a novel or speculative mechanism.

This mechanistic plausibility is reinforced by an active evidence base: the ongoing Phase 3 CAPTIVA trial (NCT05047172) directly compares ticagrelor- and rivaroxaban-based regimens against clopidogrel in symptomatic intracranial arterial stenosis, and several additional trials evaluate antiplatelet strategies (including ticagrelor) in intracranial stenting and stroke prevention settings.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06714526](https://clinicaltrials.gov/study/NCT06714526) | NA | Recruiting | 100 | Pilot RCT of genotype-guided P2Y12 inhibitor selection vs. conventional clopidogrel in symptomatic intracranial atherosclerotic disease. |
| [NCT04948749](https://clinicaltrials.gov/study/NCT04948749) | NA | Recruiting | 792 | DREAM-PRIDE: drug-eluting stent plus aggressive medical therapy vs. medical therapy alone to prevent recurrent stroke in symptomatic ICAD. |
| [NCT02605447](https://clinicaltrials.gov/study/NCT02605447) | Phase 4 | Completed | 2009 | EVOLVE Short DAPT: safety of 3-month dual antiplatelet therapy in high bleeding-risk patients after PCI with the SYNERGY stent system. |
| [NCT05047172](https://clinicaltrials.gov/study/NCT05047172) | Phase 3 | Active, not recruiting | 1683 | CAPTIVA: rivaroxaban and/or ticagrelor vs. clopidogrel for reducing 1-year ischemic stroke, intracerebral hemorrhage, or vascular death in intracranial arterial stenosis. |
| [NCT01732822](https://clinicaltrials.gov/study/NCT01732822) | Phase 3 | Completed | 13885 | EUCLID: ticagrelor vs. clopidogrel for cardiovascular death, MI, and ischemic stroke in peripheral artery disease. |
| [NCT06058130](https://clinicaltrials.gov/study/NCT06058130) | NA | Unknown | 2171 | Anticoagulation alone vs. anticoagulation plus antiplatelet therapy in acute ischemic stroke with atrial fibrillation and extracranial/intracranial artery stenosis. |
| [NCT06857045](https://clinicaltrials.gov/study/NCT06857045) | NA | Withdrawn | 0 | 3 vs. 6 months DAPT after NOVA intracranial sirolimus-eluting stent implantation (trial withdrawn before enrollment). |
| [NCT03620760](https://clinicaltrials.gov/study/NCT03620760) | Phase 4 | Unknown | 2036 | Low-dose vs. standard-dose ticagrelor after drug-eluting stent implantation for unstable angina. |
| [NCT01813435](https://clinicaltrials.gov/study/NCT01813435) | Phase 3 | Completed | 15991 | GLOBAL LEADERS: ticagrelor+aspirin (1 month) then ticagrelor monotherapy vs. standard DAPT after stent implantation. |
| [NCT07354828](https://clinicaltrials.gov/study/NCT07354828) | N/A | Not yet recruiting | 3500 | Quality control indicator optimization for DAPT-based coronary revascularization in coronary heart disease. |

No EudraCT (EU Clinical Trials Register) identifiers were available in this Evidence Pack.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39862061](https://pubmed.ncbi.nlm.nih.gov/39862061/) | 2025 | RCT (trial design) | International Journal of Stroke | Design and early progress of the CAPTIVA trial comparing anticoagulation vs. antiplatelet combinations for intracranial vascular atherostenosis. |
| [38252758](https://pubmed.ncbi.nlm.nih.gov/38252758/) | 2024 | Review | Stroke | Focused update on intracranial atherosclerosis, including current knowledge gaps relevant to antithrombotic strategy selection. |
| [39658130](https://pubmed.ncbi.nlm.nih.gov/39658130/) | 2025 | Cohort/Observational | Journal of NeuroInterventional Surgery | Lower-dose ticagrelor (60 mg twice daily) plus aspirin compared with standard aspirin/clopidogrel DAPT for intracranial stenting. |

---

## Denmark Market Information

Ticagrelor is not currently marketed in Denmark (0 marketing authorisations on record in this Evidence Pack), so no product-level licence data is available.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information. Danish label warnings/contraindications and drug-drug interaction data were not available in this Evidence Pack (see data gap DG001, flagged as Blocking for safety pre-assessment).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Ticagrelor's antiplatelet mechanism is directly relevant to the thrombotic pathology of intracranial arteriosclerosis, and this direction is actively being tested in a dedicated ongoing Phase 3 trial (CAPTIVA) alongside a completed Phase 3 trial (EUCLID) and multiple supporting studies — corresponding to Evidence Level L2. However, no completed trial has yet reported a primary efficacy result specific to the ICAD population, so guardrails are warranted pending mature outcome data.

**To proceed, the following is needed:**
- Danish/EU-approved product label (SmPC) warnings, contraindications, and drug-drug interaction data (Blocking gap, DG001)
- Confirmed mechanism-of-action detail from DrugBank (High-priority gap, DG002)
- Primary results from the ongoing CAPTIVA trial (NCT05047172, expected completion 2028-05-31)
- Confirmation of Denmark/EU marketing authorisation status, since ticagrelor currently has no recorded Danish licence in this Evidence Pack
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

