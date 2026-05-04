---
layout: default
title: Digoxin
parent: 僅模型預測 (L5)
nav_order: 143
evidence_level: L5
indication_count: 10
---

# Digoxin
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

# Digoxin: From Heart Failure / Atrial Fibrillation to Prinzmetal Angina

## One-Sentence Summary

Digoxin is a cardiac glycoside with a long clinical history, primarily used for the management of heart failure and rate control in atrial fibrillation/flutter.
The TxGNN model predicts it may be effective for **Prinzmetal Angina** (vasospastic angina),
with **0 clinical trials** and **2 publications** currently available — both of which are only indirectly relevant to this indication.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Heart failure; rate control in atrial fibrillation/flutter |
| Predicted New Indication | Prinzmetal Angina (vasospastic angina) |
| TxGNN Prediction Score | 99.81% |
| Evidence Level | L5 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on well-established pharmacological knowledge, digoxin is a cardiac glycoside that inhibits the Na⁺/K⁺-ATPase pump in cardiac myocytes, leading to increased intracellular calcium and a positive inotropic effect. It also exerts vagomimetic (parasympathomimetic) effects on the sinoatrial and atrioventricular nodes, which underpins its use in heart failure and atrial fibrillation rate control.

Prinzmetal angina (also called variant or vasospastic angina) is characterised by transient coronary artery vasospasm, often occurring at rest and in the absence of obstructive coronary artery disease. The TxGNN model may be leveraging graph-level associations between digoxin and vasomotor or autonomic cardiovascular pathways. Digoxin's parasympathomimetic properties could theoretically modulate coronary vasomotor tone, which is the hallmark of Prinzmetal angina.

However, it is important to note that digoxin may actually worsen myocardial oxygen demand in certain ischaemic settings, and it is generally not recommended — and in some guidelines explicitly cautioned — in anginal syndromes. The absence of any dedicated clinical trial evidence for this indication, and the indirect nature of the available literature, means the mechanistic rationale remains speculative at this stage.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [9206110](https://pubmed.ncbi.nlm.nih.gov/9206110/) | 1996 | Observational | Chinese Medical Sciences Journal | Study of 30 patients with angina decubitus (a related anginal syndrome); found severe coronary obstructive lesions and increased myocardial oxygen consumption before onset — suggests angina decubitus is effort-related rather than vasospastic. Digoxin is not directly evaluated. |
| [10736610](https://pubmed.ncbi.nlm.nih.gov/10736610/) | 1999 | Review | Acta Physiologica et Pharmacologica Bulgarica | Reviews circadian rhythms in antihypertensive pharmacotherapy; discusses timing of cardiovascular drug effects. Relevant to cardiovascular pharmacology broadly, but does not specifically address digoxin in Prinzmetal angina. |

> ⚠️ **Note:** Neither publication directly investigates the use of digoxin in Prinzmetal angina. The evidence base is insufficient to support this repurposing hypothesis at this time.

---

## Denmark Market Information

Digoxin is currently recorded as **not marketed** in Denmark, with no active marketing authorisations identified in this dataset.

> ⚠️ **Note:** This data gap is clinically significant. Digoxin (e.g., as Lanoxin) is a long-established cardiovascular medicine in Europe and may hold historical or current authorisations not captured in the present dataset. It is strongly recommended to verify directly with the Danish Medicines Agency (Lægemiddelstyrelsen) and the EMA's medicines database before drawing conclusions about market availability.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for full safety information.

> ⚠️ **Important clinical note:** Although structured safety data is unavailable in this evidence pack, digoxin is widely known to have a **narrow therapeutic index**, with toxicity risk (digitalis toxicity: nausea, arrhythmias, visual disturbances, xanthopsia) even at doses within the therapeutic range. Renal function significantly affects digoxin clearance and dosing. Healthcare professionals should consult the authorised SmPC and current clinical guidelines before considering any off-label use.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence base for digoxin in Prinzmetal angina is essentially absent — there are no registered clinical trials and only 2 indirectly relevant publications. Furthermore, the known pharmacological profile of digoxin (increased myocardial oxygen demand, narrow therapeutic index) raises mechanistic concerns about its suitability in a vasospastic angina context, where calcium channel blockers and nitrates are the established standard of care.

**To proceed, the following is needed:**

- Obtain and review the full SmPC / product monograph for digoxin to assess contraindications and warnings specific to ischaemic heart disease
- Clarify Danish market authorisation status directly with Lægemiddelstyrelsen and the EMA
- Retrieve and populate the mechanism of action (MOA) data from DrugBank (DB00390) to enable a structured mechanistic analysis
- Conduct a targeted literature review specifically examining digoxin and coronary vasomotor regulation or vasospasm
- Determine whether any preclinical or mechanistic studies exist linking cardiac glycosides to coronary artery spasm pathways before progressing to a Phase 2/3 evidence assessment

---

*This report is generated for research reference purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before any therapeutic application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

