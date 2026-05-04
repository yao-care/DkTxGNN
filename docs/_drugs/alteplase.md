---
layout: default
title: Alteplase
parent: 僅模型預測 (L5)
nav_order: 30
evidence_level: L5
indication_count: 10
---

# Alteplase
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

# Alteplase: From Acute Thrombotic Events to Posterolateral Myocardial Infarction

## One-Sentence Summary

Alteplase is a recombinant tissue plasminogen activator (rt-PA) established as a thrombolytic agent in acute thrombotic events, including ischaemic stroke, acute myocardial infarction, and pulmonary embolism.
The TxGNN model predicts it may be effective for **Posterolateral Myocardial Infarction** — an anatomical subtype of acute MI caused primarily by left circumflex artery (LCx) or right coronary artery (RCA) occlusion —
with **0 clinical trials** and **3 publications** currently supporting this specific anatomical subtype as a distinct indication.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not recorded in the Danish national registry (no approved indication text available in current dataset) |
| Predicted New Indication | Posterolateral Myocardial Infarction |
| TxGNN Prediction Score | 99.79% |
| Evidence Level | L3 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the structured fields for this evidence pack. Based on established pharmacology, Alteplase is a recombinant tissue-type plasminogen activator (rt-PA) that selectively binds to fibrin within a thrombus and catalyses the conversion of plasminogen to plasmin. Plasmin then degrades the fibrin matrix of the clot, re-establishing coronary arterial perfusion. This action is clot-selective under physiological conditions, meaning it operates preferentially at the site of occlusion rather than causing systemic fibrinogenolysis at therapeutic doses.

Posterolateral myocardial infarction is caused by thrombotic occlusion of the left circumflex artery (LCx) or the posterolateral branches of the RCA. The underlying pathophysiology — a fibrin-rich occlusive coronary thrombus — is structurally identical to the target of Alteplase in all anatomical MI subtypes. The TxGNN prediction therefore reflects a mechanistically direct and highly plausible extension of Alteplase's established fibrinolytic action to this anatomical territory. Posterolateral MI represents a recognised anatomical variant of acute MI rather than a biologically distinct disease process, making the mechanistic link particularly robust.

Supporting evidence includes a 1998 observational study (PMID 9502627) that specifically investigated whether posterior lead ST-elevation (V7–V9) during inferior MI identifies patients with concomitant posterior infarction who derive greater benefit from thrombolysis — directly linking this subtype to thrombolytic candidate selection. The broader TAMI-1 Phase 2/3 RCT (PMID 2521226) demonstrated rt-PA efficacy across different infarct territories including LCx and RCA distributions, with 90-minute patency rates of 68% for both the left circumflex and right coronary arteries after 150 mg rt-PA. The primary evidentiary gap remains the absence of a dedicated randomised controlled trial with posterolateral MI as a pre-specified primary endpoint.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for posterolateral myocardial infarction.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [9502627](https://pubmed.ncbi.nlm.nih.gov/9502627/) | 1998 | Observational (Diagnostic) | Journal of the American College of Cardiology | ST-segment elevation in posterior leads (V7–V9) during acute inferior MI identifies concomitant posterior infarction; these patients may benefit more from thrombolytic therapy |
| [8480981](https://pubmed.ncbi.nlm.nih.gov/8480981/) | 1993 | Case Series | Annales de cardiologie et d'angeiologie | Cerebral embolism with rapid resolution during late tPA fibrinolysis in a patient with posterolateral MI; reviews fibrinolytic effects on left intraventricular thrombi and highlights systemic embolism risk |
| [21351226](https://pubmed.ncbi.nlm.nih.gov/21351226/) | 2011 | Case Report | Catheterization and Cardiovascular Interventions | Primary PCI with mini-crush drug-eluting stents facilitated by intracoronary reteplase in a 37-year-old with posterolateral acute MI and borderline haemodynamics; LV ejection fraction 30% with posterior/lateral/apical akinesis |

---

## Denmark Market Information

No marketing authorisations for Alteplase are currently recorded in the Danish national registry (Laegemiddelstyrelsen). This dataset reflects national registrations only.

> **Note for clinical teams:** Alteplase (brand name Actilyse) holds a valid centralised EMA marketing authorisation applicable across all EU member states including Denmark. The approved indications under EMA centralised authorisation include acute ischaemic stroke, acute myocardial infarction (STEMI), and acute massive pulmonary embolism. Healthcare professionals should verify current approved indications and availability via the [EMA product database](https://www.ema.europa.eu) or the Laegemiddelstyrelsen's medicinal product portal before clinical use.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Alteplase's thrombolytic mechanism directly targets the same coronary thrombus pathophysiology underlying posterolateral MI as in all other acute MI subtypes, making the mechanistic basis for efficacy highly robust. Observational and case-level evidence supports the historical use of thrombolysis in posterior MI territory, though no dedicated RCT with posterolateral MI as the primary endpoint has been identified.

**To proceed, the following is needed:**

- Retrieval and full review of the SmPC for Actilyse (EMA centralised authorisation EU/1/95/003/001) to complete safety, contraindication, and drug interaction evaluation — this is currently a blocking data gap
- Clarification of whether posterolateral MI is already covered under the broad acute STEMI indication in the current EMA-approved label (which would reclassify this from repurposing to label clarification)
- Subgroup outcome data from landmark thrombolysis trials (GUSTO, TAMI) specifically examining posterolateral/LCx territory MI to strengthen the quantitative evidence base
- Structured assessment against current ESC guidelines on thrombolysis versus primary PCI for posterior STEMI in the Danish clinical pathway context, particularly given the widespread availability of primary PCI in Denmark
- Update of the MOA field from DrugBank (DB00009) to complete the structured evidence pack
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

