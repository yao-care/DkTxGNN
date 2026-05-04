---
layout: default
title: Erenumab
parent: 僅模型預測 (L5)
nav_order: 173
evidence_level: L5
indication_count: 2
---

# Erenumab
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

# Erenumab: From Migraine Prevention to Migraine with Brainstem Aura

## One-Sentence Summary

Erenumab is a fully human monoclonal antibody targeting the calcitonin gene-related peptide (CGRP) receptor, originally developed and approved for the preventive treatment of migraine.
The TxGNN model predicts it may be effective for **Migraine with Brainstem Aura**,
with **0 registered clinical trials** but **20 publications** currently supporting this direction, including post-hoc analyses of Phase 3 RCTs and a systematic review.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Migraine prevention (episodic and chronic migraine) |
| Predicted New Indication | Migraine with Brainstem Aura |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L2 |
| Denmark Market Status | Not marketed (not recorded in dataset; note: erenumab [Aimovig] holds EMA centralised authorisation EU/1/18/1293) |
| Number of Marketing Authorisations | 0 (in current dataset) |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Erenumab is a fully human monoclonal antibody that selectively binds to the calcitonin gene-related peptide (CGRP) receptor. CGRP plays a central role in migraine pathophysiology: during a migraine attack, the trigeminovascular system releases CGRP, leading to neurogenic inflammation, vasodilation, and pain signal transmission. By blocking the CGRP receptor, erenumab prevents downstream signalling and has demonstrated efficacy in reducing the frequency and severity of migraine attacks in both episodic and chronic migraine.

Migraine with brainstem aura (previously known as basilar-type migraine) is a rare migraine subtype in which the aura originates from the brainstem. Although the aura symptoms differ from typical migraine with aura, the underlying pain mechanism still involves activation of the trigeminovascular system and CGRP release. This shared CGRP-dependent pain pathway means that erenumab's mechanism of action is mechanistically applicable to this subtype.

Importantly, post-hoc analyses of pivotal Phase 3 randomised clinical trials (PMID 34928306) have demonstrated that erenumab is both safe and effective in patients with migraine with aura, without increasing cardiovascular risk. A systematic review (PMID 37012858) further confirms erenumab's prophylactic efficacy across migraine subtypes. While brainstem aura was not specifically studied as a separate subgroup in these trials, the pharmacological rationale strongly supports the prediction that CGRP receptor blockade would benefit this subtype as well.

## Clinical Trial Evidence

Currently no clinical trials specifically registered for erenumab in migraine with brainstem aura.

> Note: While no trials target brainstem aura specifically, erenumab has been studied extensively in broader migraine populations. Patients with migraine with aura were included in multiple Phase 3 trials (e.g., the LIBERTY trial, STRIVE, ARISE), and post-hoc analyses have confirmed efficacy in the aura subgroup.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30360965](https://pubmed.ncbi.nlm.nih.gov/30360965/) | 2018 | Phase 3b RCT | Lancet | LIBERTY trial: erenumab effective in episodic migraine patients who failed 2–4 prior preventives; significant reduction in monthly migraine days vs placebo |
| [34928306](https://pubmed.ncbi.nlm.nih.gov/34928306/) | 2022 | Post-hoc analysis of Phase 3 RCTs | JAMA Neurology | Erenumab safe and effective in patients with migraine with aura; no elevated vascular risk in aura subgroup |
| [37012858](https://pubmed.ncbi.nlm.nih.gov/37012858/) | 2023 | Systematic Review | Int Immunopharmacol | Confirms erenumab efficacy in preventive therapy of both episodic and chronic migraine |
| [36942409](https://pubmed.ncbi.nlm.nih.gov/36942409/) | 2023 | Prospective observational | Headache | Pooled long-term data show no increased cardiovascular risk with erenumab in patients with or without aura |
| [40275185](https://pubmed.ncbi.nlm.nih.gov/40275185/) | 2025 | Biomarker study | J Headache Pain | Plasma suPAR (inflammation biomarker) elevated in migraine with aura; investigated as predictor of erenumab response |
| [35151970](https://pubmed.ncbi.nlm.nih.gov/35151970/) | 2022 | Real-world observational | Clin Neurol Neurosurg | Croatian real-world data: erenumab effective and safe in treatment-resistant chronic migraine after 6 months |
| [32867533](https://pubmed.ncbi.nlm.nih.gov/32867533/) | 2021 | Mechanistic/Safety study | Cephalalgia | Erenumab does not alter cerebral haemodynamics or endothelial function, supporting vascular safety |
| [40596876](https://pubmed.ncbi.nlm.nih.gov/40596876/) | 2025 | Single-arm clinical study | J Headache Pain | Patients switching from erenumab to fremanezumab tolerated the switch well; characterises erenumab adverse event profile |
| [33125303](https://pubmed.ncbi.nlm.nih.gov/33125303/) | 2021 | Retrospective clinical study | J Pain Palliat Care Pharmacother | Combination of erenumab + onabotulinumtoxinA showed benefit in intractable chronic migraine |
| [35230406](https://pubmed.ncbi.nlm.nih.gov/35230406/) | 2022 | Editorial | JAMA | Summary confirming erenumab is safe and effective for patients with migraine with aura |

## Denmark Market Information

No marketing authorisations for erenumab are recorded in the current dataset.

> **Note for Danish healthcare professionals:** Erenumab is marketed in Denmark under the brand name **Aimovig** via EMA centralised marketing authorisation (EU/1/18/1293), authorised since July 2018. It is approved for prophylaxis of migraine in adults who have at least 4 migraine days per month. Please consult the Danish Medicines Agency (Lægemiddelstyrelsen) or the EMA product database for the current Summary of Product Characteristics (SmPC).

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

> **Additional context from the literature:** Post-hoc analyses of pooled Phase 3 trial data (PMID 36942409) found no increased cardiovascular risk with erenumab, even in patients with migraine with aura who carry elevated baseline vascular risk. A mechanistic study (PMID 32867533) confirmed that erenumab does not alter cerebral haemodynamics or endothelial function. Twelve-month real-world safety data (PMID 35538414) showed generally good tolerability. The most commonly reported adverse events in clinical practice include constipation, injection site reactions, and muscle spasms.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Erenumab is already EMA-approved for migraine prevention and has demonstrated efficacy and safety in patients with migraine with aura in post-hoc analyses of Phase 3 RCTs. While migraine with brainstem aura has not been studied as a separate indication, the shared CGRP-dependent pain mechanism provides a strong pharmacological basis for efficacy in this subtype. The TxGNN prediction score of 99.89% and an evidence level of L2 support further investigation.

**To proceed, the following is needed:**
- Prospective clinical data specifically enrolling patients with migraine with brainstem aura (either a dedicated trial or a pre-specified subgroup analysis)
- Confirmation of the Denmark marketing authorisation status and SmPC review for the brainstem aura population
- Detailed safety monitoring plan, particularly regarding vascular risk given the brainstem involvement in this migraine subtype
- Collection of real-world evidence from headache centres treating brainstem aura patients with erenumab off-label
- Formal assessment of whether the existing EMA indication ("migraine prophylaxis") already encompasses brainstem aura subtypes, which could simplify the regulatory pathway
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

