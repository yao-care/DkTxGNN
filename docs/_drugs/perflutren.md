---
layout: default
title: Perflutren
parent: 僅模型預測 (L5)
nav_order: 346
evidence_level: L5
indication_count: 10
---

# Perflutren
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

# Perflutren: From Diagnostic Ultrasound Contrast Imaging to Myocardial Ischemia

## One-Sentence Summary

> Perflutren is a perfluoropropane-filled lipid microbubble agent, established as an ultrasound contrast agent for cardiac imaging (myocardial contrast echocardiography / left ventricular opacification).
> The TxGNN model predicts a possible role in **Myocardial Ischemia** — specifically as a therapeutic *sonothrombolysis* agent rather than merely a diagnostic tool —
> with **10 triaged clinical trials** and **10 classified publications** providing early-stage, largely mechanistic/observational support. No confirmatory Phase 3 RCT exists yet.

*Note on other TxGNN predictions*: This candidate (rank 7–8 in the evidence pack, score 96.34%) was selected over the technically higher-scoring predictions (acute intermittent porphyria, nephrogenic SIAD, MDR-tuberculosis, citrullinemia — scores 95.9–97.5%) because those four have **zero clinical trials, zero literature, and no biologically plausible mechanism** according to the evidence pack's own rationale, and are explicitly flagged there as likely knowledge-graph embedding artifacts rather than genuine repurposing signals. Myocardial ischemia is the only predicted indication that reaches decision stage S1 with real supporting evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Ultrasound contrast imaging (myocardial contrast echocardiography / left ventricular opacification) — no formal Danish licence text available (drug not marketed) |
| Predicted New Indication | Myocardial Ischemia (therapeutic sonothrombolysis) |
| TxGNN Prediction Score | 96.34% |
| Evidence Level | L3 (observational/cohort studies; no completed Phase 3 RCT) |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold (evidence pack recommendation stage: "Research Question") |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for Perflutren is not available (Data Gap). Based on known information, Perflutren is a perfluoropropane-gas-core, lipid-shell microbubble agent whose established clinical role is purely physical/acoustic: it scatters ultrasound energy to enhance left ventricular opacification and myocardial perfusion imaging. It has no known pharmacologic activity in the conventional sense (no receptor binding, enzyme inhibition, or metabolic pathway interaction).

The TxGNN prediction for "myocardial ischemia" is therefore best understood not as discovery of a hidden pharmacological mechanism, but as recognition of a **procedural/therapeutic extension of an existing diagnostic application**: when combined with high-mechanical-index diagnostic ultrasound, intravenous microbubbles can mechanically disrupt intracoronary thrombus and restore microvascular flow — a technique described in the literature as "sonothrombolysis" or "ultrasound-targeted microbubble destruction (UTMD)." Several early-phase and preclinical studies in the evidence pack (angiogenesis promotion via UTMD, acoustic activation of perfluoropropane droplets in infarct zones, sonothrombolysis feasibility trials) support this as a biologically plausible — if still investigational — mechanism distinct from Perflutren's approved diagnostic use.

Because this proposed mechanism is procedural (ultrasound-energy-dependent) rather than classically pharmacological, and because the strongest human trial in this space (NCT04217304, SONOSTEMI-LYSIS) was Phase 2 and **terminated** with only 41 patients, the evidence currently supports this as a research hypothesis worth further investigation rather than a clinically actionable repurposing candidate.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04217304](https://clinicaltrials.gov/study/NCT04217304) | Phase 2 | Terminated | 41 | SONOSTEMI-LYSIS: safety/feasibility of sonothrombolysis (microbubbles + ultrasound) in STEMI patients undergoing pharmacoinvasive reperfusion — the only trial explicitly designed to test a *therapeutic* effect; terminated early, limited sample. |
| [NCT02410330](https://clinicaltrials.gov/study/NCT02410330) | N/A | Completed | 100 | Therapeutic Use of Ultrasound in Acute Coronary Artery Disease — tested whether IV perfluorocarbon microbubbles + diagnostic ultrasound can restore microcirculatory flow and improve epicardial recanalization (sonothrombolysis). |
| [NCT04732091](https://clinicaltrials.gov/study/NCT04732091) | N/A | Unknown | 540 | High mechanical index ultrasound + microbubbles to reduce acute MI burden — multicentre attempt to demonstrate clinical effectiveness of sonothrombolysis in ACS; completion status unclear. |
| [NCT02880137](https://clinicaltrials.gov/study/NCT02880137) | Phase 4 | Completed | 36 | Real-time myocardial perfusion echocardiography (RTMPE) to detect coronary allograft vasculopathy in transplant patients — diagnostic, not therapeutic use. |
| [NCT02170103](https://clinicaltrials.gov/study/NCT02170103) | N/A | Completed | 50 | Tested whether a modified diagnostic ultrasound system plus commercial microbubbles could break up clots causing STEMI when applied emergently — diagnostic-tool-as-treatment observational design. |
| [NCT01384448](https://clinicaltrials.gov/study/NCT01384448) | N/A | Completed | 400 | Randomized comparison of coronary CT angiography vs. stress echocardiography for ED chest-pain triage — diagnostic methodology comparison, not treatment. |
| [NCT05416385](https://clinicaltrials.gov/study/NCT05416385) | N/A | Recruiting | 1500 | Combines intraplaque neovascularization imaging with carotid stress-echo risk stratification — diagnostic/risk-stratification, not treatment. |
| [NCT03173716](https://clinicaltrials.gov/study/NCT03173716) | Phase 4 | Completed | 24 | RTMPE in the ICU — evaluated impact on diagnostic confidence and downstream management of myocardial ischemia; diagnostic utility study. |
| [NCT01436773](https://clinicaltrials.gov/study/NCT01436773) | N/A | Completed | 66 | Contrast-enhanced ultrasound identification of carotid vasa vasorum and correlation with acute coronary events — observational plaque-vulnerability study. |
| [NCT00529607](https://clinicaltrials.gov/study/NCT00529607) | N/A | Completed | 200 | Evaluated new cardiac imaging modalities (incl. contrast echocardiography) against biochemical reperfusion-injury markers post-MI — diagnostic technique development. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24408670](https://pubmed.ncbi.nlm.nih.gov/24408670/) | 2015 | Cohort | Heart and Vessels | Resting myocardial contrast echocardiography predicted cardiac events after AMI and PCI, supporting a prognostic (not treatment) role for perflutren-based imaging. |
| [21564278](https://pubmed.ncbi.nlm.nih.gov/21564278/) | 2011 | Clinical/Technical | Echocardiography | Perflutren contrast improved delineation of both endocardial and epicardial borders during transthoracic echocardiography. |
| [11457757](https://pubmed.ncbi.nlm.nih.gov/11457757/) | 2001 | Cohort/Imaging | Circulation | Power-modulation contrast imaging enabled combined quantitative assessment of myocardial perfusion and regional LV function. |
| [36050231](https://pubmed.ncbi.nlm.nih.gov/36050231/) | 2022 | Mechanistic | Ultrasound in Medicine & Biology | Acoustic activation of retained perfluoropropane droplets preferentially occurs within developing infarct zones — mechanistic basis for infarct-targeted delivery. |
| [23969167](https://pubmed.ncbi.nlm.nih.gov/23969167/) | 2013 | Mechanistic/Animal | Ultrasound in Medicine & Biology | Ultrasound-targeted microbubble destruction (UTMD) promoted angiogenesis and improved heart function via myocardial microenvironment changes in a canine MI model — the clearest mechanistic support for a *therapeutic* effect. |
| [32497541](https://pubmed.ncbi.nlm.nih.gov/32497541/) | 2020 | Case Report | The American Journal of Medicine | Reported recurrent lethal allergic coronary vasospasm — a safety signal relevant to risk assessment, not efficacy. |
| [16386679](https://pubmed.ncbi.nlm.nih.gov/16386679/) | 2006 | Imaging Method Study | Journal of the American College of Cardiology | Validated real-time 3D echocardiographic perfusion imaging and volumetric contrast-inflow analysis methodology. |
| [9487468](https://pubmed.ncbi.nlm.nih.gov/9487468/) | 1998 | Pharmacology Characterization | Journal of the American Society of Echocardiography | Characterized perfusion and hemodynamic profile of an early microbubble contrast agent during acute MI in a canine model. |
| [11593652](https://pubmed.ncbi.nlm.nih.gov/11593652/) | 1999 | Animal Model | Chinese Medical Journal | Evaluated a perfluoropropene-filled contrast agent for non-invasive risk-area and infarct-area assessment in a canine ischemia-reperfusion model. |
| [7797773](https://pubmed.ncbi.nlm.nih.gov/7797773/) | 1995 | Animal Model | Journal of the American College of Cardiology | Early foundational study showing IV sonicated dextrose albumin with perfluoropropane gas could identify acute myocardial ischemia and reperfusion non-invasively. |

---

## Denmark Market Information

Perflutren currently holds **no marketing authorisation in Denmark** (national Lægemiddelstyrelsen or EMA centralised) — market status is recorded as **not marketed**, with 0 licences on file. No product/dosage-form/indication data is therefore available to tabulate.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for formal safety information — no structured warnings, contraindications, or drug-interaction data were returned by the safety data sources queried for this candidate.

For context, one publication surfaced in the literature search is worth flagging even though it falls outside the structured safety dataset: [PMID 26242615](https://pubmed.ncbi.nlm.nih.gov/26242615/) (Hauben et al., *Drug Safety*, 2015) notes that perflutren microbubble/microsphere ultrasound contrast agents carry a **black-box warning** based on case reports of serious cardiopulmonary events, and a related case report ([PMID 32497541](https://pubmed.ncbi.nlm.nih.gov/32497541/)) describes recurrent lethal allergic coronary vasospasm. These should be treated as important signals to verify against the official SmPC, not as a substitute for it.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The proposed therapeutic mechanism (ultrasound-targeted microbubble destruction / sonothrombolysis) is mechanistically plausible and supported by preclinical and early-phase human data, but the only trial designed to directly test therapeutic efficacy (NCT04217304) was Phase 2 and terminated early with a small cohort — this does not meet the bar for L1/L2 evidence.
- Perflutren is not currently marketed in Denmark, and formal safety labelling (SmPC warnings/contraindications) could not be retrieved, which blocks a proper S1 safety evaluation (per data gap DG001, severity: Blocking).
- The drug's original mechanism of action is undocumented (Data Gap), preventing a full mechanistic-plausibility assessment.

**To proceed, the following is needed:**
- Official SmPC / product labelling for Perflutren (warnings, contraindications, drug interactions) — currently a blocking data gap.
- Detailed mechanism of action data from DrugBank or primary pharmacology sources.
- A completed or ongoing adequately powered Phase 2/3 trial specifically testing sonothrombolysis as a treatment (not diagnostic adjunct) for myocardial ischemia/STEMI, ideally following up on the terminated SONOSTEMI-LYSIS trial.
- Clarification of procedural requirements (ultrasound equipment/mechanical index settings) needed to reproduce the proposed therapeutic effect, since this repurposing pathway depends on more than drug administration alone.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

