---
layout: default
title: Ioversol
parent: 僅模型預測 (L5)
nav_order: 220
evidence_level: L5
indication_count: 10
---

# Ioversol
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

# Ioversol: From Diagnostic Contrast Imaging to Osteoarthritis

## One-Sentence Summary

Ioversol is a non-ionic, low-osmolar iodinated contrast agent routinely used for diagnostic imaging procedures such as coronary angiography, CT enhancement, and urography.
The TxGNN model predicts it may be relevant for **Osteoarthritis** — specifically through the genicular artery embolisation (GAE) procedure — with **4 clinical trials** and **1 publication** providing contextual support.
However, a critical caveat applies: all identified evidence uses **Lipiodol** (ethiodized oil), a structurally distinct oil-based iodinated agent, and cannot be directly extrapolated to Ioversol.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Diagnostic contrast imaging (no formal regulatory approval data available in this dataset) |
| Predicted New Indication | Osteoarthritis |
| TxGNN Prediction Score | 99.63% |
| Evidence Level | L4 |
| Denmark Market Status | Not Marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for Ioversol in this dataset. Based on established pharmacological knowledge, Ioversol is a non-ionic, low-osmolar iodinated contrast medium of the triiodobenzoic acid family (brand name: Optiray®). It provides X-ray attenuation through its iodine content, distributes rapidly in the extracellular space following intravenous administration, and is excreted renally without significant metabolism. Its primary role is diagnostic, not therapeutic.

The TxGNN model links Ioversol to osteoarthritis through the emerging interventional technique of **Genicular Artery Embolisation (GAE)**. In GAE, an embolic agent is delivered into the genicular arteries to reduce synovial hypervascularity — a recognised driver of pain and inflammation in knee osteoarthritis. Iodinated contrast agents are routinely used to guide these endovascular procedures via arteriography, which may explain the topological proximity between Ioversol and osteoarthritis disease nodes in the TxGNN knowledge graph.

A critical mechanistic distinction must, however, be made. Clinical trials in this space uniformly employ **Lipiodol** (ethiodized oil), an oil-based iodinated agent whose viscous, non-water-soluble properties allow *durable* vascular occlusion. Ioversol is water-soluble and clears from the vasculature within minutes of administration, rendering it unsuitable as an embolic agent. Although both agents contain iodine, their physicochemical profiles and clinical roles are fundamentally different. The mechanistic analogy is therefore indirect at best, and the TxGNN prediction most likely reflects knowledge graph neighbour-diffusion rather than a true therapeutic relationship.

> **Note on secondary predictions:** The top-ranked TxGNN prediction is "osteoarthritis susceptibility" (score 99.67%), which represents a *genetic risk phenotype*, not a treatment target. No contrast agent has a known mechanism for modifying genetic susceptibility to osteoarthritis. This prediction is assessed as L5 (model prediction only) and is not actionable clinically.

---

## Clinical Trial Evidence

> ⚠️ **All trials below use Lipiodol® (ethiodized oil) as the embolic agent — not Ioversol.** These are included as indirect contextual evidence for the GAE approach in osteoarthritis; they do not constitute direct evidence for Ioversol repurposing.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06497140](https://clinicaltrials.gov/study/NCT06497140) | Phase 3 | Recruiting | 130 | Randomised, sham-controlled, multicentre trial evaluating GAE with ethiodized oil emulsion for symptomatic knee OA; the highest-quality ongoing trial in this area (estimated completion 2028) |
| [NCT04733092](https://clinicaltrials.gov/study/NCT04733092) | Phase 1 | Completed | 22 | Prospective study of Lipiodol emulsion embolisation of inflammatory hypervascularisation in knee OA; established initial safety data for the GAE approach |
| [NCT06611007](https://clinicaltrials.gov/study/NCT06611007) | Phase 1/2 | Recruiting | 15 | Pilot study evaluating safety and efficacy of Lipiodol® arterial embolisation in symptomatic hand (digital) OA refractory to conventional treatment |
| [NCT06859164](https://clinicaltrials.gov/study/NCT06859164) | Phase 2 | Recruiting | 50 | NIH-NIAMS funded pilot randomised sham-controlled study (SHAM-PAIN) assessing GAE for knee OA pain reduction at 3 months using KOOS pain subscore |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38102013](https://pubmed.ncbi.nlm.nih.gov/38102013/) | 2024 | RCT (Phase 1/2) | Diagnostic and Interventional Imaging | LipioJoint-1 trial: evaluated safety and efficacy of transient GAE using an ethiodized oil-based emulsion for knee OA; foundational publication for the Lipiodol-based GAE approach |

---

## Denmark Market Information

Ioversol is **not currently marketed in Denmark**. No authorisations from the Danish Medicines Agency (Laegemiddelstyrelsen) or EMA centralised procedures were identified in this dataset. Ioversol is commercially available internationally under the brand name Optiray® (Guerbet), but a marketing authorisation pathway in Denmark would need to be assessed from scratch.

---

## Safety Considerations

No formal safety data (key warnings, contraindications, or drug interactions) was available in the current dataset.

Please refer to the approved Summary of Product Characteristics (SmPC) for full safety information.

Based on the general pharmacology of non-ionic iodinated contrast agents, clinicians should be aware of the following considerations:

- **Contrast-induced acute kidney injury (CI-AKI):** Risk is elevated in patients with pre-existing renal impairment, diabetes mellitus, dehydration, or concomitant nephrotoxic agents. Standard pre-hydration protocols apply.
- **Hypersensitivity reactions:** Range from mild urticaria and nausea to severe anaphylactoid reactions. Pre-medication protocols and resuscitation preparedness are recommended.
- **Haemoglobinopathies (special caution):** Available literature (PMID: [22195536](https://pubmed.ncbi.nlm.nih.gov/22195536/)) investigated the safety of iodinated intravenous contrast in sickle cell disease, noting that in vitro erythrocyte sickling is less pronounced with second-generation low-osmolar agents such as Ioversol compared with older formulations. Clinical significance remains to be confirmed. These publications highlight a safety *concern* in this population rather than a therapeutic application.
- **Metformin interaction:** Standard guidance to withhold metformin peri-procedure in patients at risk of CI-AKI applies.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All identified clinical evidence relates exclusively to Lipiodol (an oil-based iodinated agent) and cannot be applied to Ioversol, which is water-soluble and incapable of achieving the durable vascular occlusion required for therapeutic embolisation; furthermore, Ioversol holds no current marketing authorisation in Denmark, and no direct evidence supports its therapeutic use in osteoarthritis or any other non-imaging indication.

**To proceed, the following is needed:**

- **Mechanistic feasibility assessment:** Determine whether Ioversol could function as a therapeutic embolic or anti-inflammatory agent in osteoarthritis — this requires preclinical physicochemical and in vivo data distinct from Lipiodol studies.
- **MOA data retrieval:** Query DrugBank API and published literature for full mechanism of action data to support or refute the TxGNN prediction.
- **Safety and regulatory data:** Obtain the full SmPC (or equivalent), including key warnings, contraindications, and interaction profile, prior to any clinical evaluation.
- **Danish regulatory pathway:** Assess whether a marketing authorisation application (national or EMA centralised) is feasible and what clinical data package would be required by Laegemiddelstyrelsen.
- **Direct Ioversol clinical evidence:** Any further investigation should require studies specifically investigating Ioversol — not Lipiodol — in a musculoskeletal therapeutic context.

---

> *This report is generated for research purposes only and does not constitute medical advice. All drug repurposing candidates require rigorous clinical validation before therapeutic application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

