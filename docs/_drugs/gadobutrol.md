---
layout: default
title: Gadobutrol
parent: 僅模型預測 (L5)
nav_order: 199
evidence_level: L5
indication_count: 10
---

# Gadobutrol
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

# Gadobutrol: From MRI Contrast Enhancement to Benign Prostatic Hyperplasia

## One-Sentence Summary

Gadobutrol (Gadovist®) is a macrocyclic gadolinium-based contrast agent used intravenously to enhance MRI of the central nervous system and body vasculature — it is a **diagnostic imaging agent**, not a therapeutic drug.
The TxGNN model predicts it may be effective for **Benign Prostatic Hyperplasia (BPH)**,
with **0 clinical trials** and **0 publications** currently supporting this therapeutic direction.

> **Critical clinical note:** Gadobutrol has no pharmacological effect on human tissue. The model's BPH prediction almost certainly reflects its established use as a contrast agent in prostate mpMRI — a diagnostic co-occurrence, not a therapeutic relationship.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | MRI contrast enhancement (CNS imaging, MR angiography) |
| Predicted New Indication | Benign Prostatic Hyperplasia |
| TxGNN Prediction Score | 83.24% |
| Evidence Level | L5 |
| Denmark Market Status | Not registered (data gap — Gadovist® holds EMA centralised authorisation valid in all EU/EEA member states including Denmark) |
| Number of Marketing Authorisations | 0 (data not collected — verify via Laegemiddelstyrelsen) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the Evidence Pack. Based on known pharmacology, Gadobutrol is a 1.0-molar macrocyclic gadolinium chelate that functions purely as a paramagnetic MRI contrast agent. It shortens T1 relaxation times of surrounding water protons, increasing signal intensity on T1-weighted sequences. Gadobutrol has **no pharmacological activity** at any known biological receptor, enzyme, or cellular target — its only mechanism is physical interaction with water molecules in a magnetic field.

The TxGNN model's prediction of BPH is almost certainly driven by diagnostic co-occurrence rather than therapeutic potential. Multiparametric MRI (mpMRI) — which uses gadobutrol for dynamic contrast-enhanced (DCE) sequences — is now the standard pre-biopsy imaging investigation for prostate conditions including BPH and prostate cancer. The model appears to have learned this diagnostic relationship and misclassified it as a repurposing signal.

There is no known biological mechanism by which a gadolinium chelate could therapeutically modify prostate stromal proliferation, reduce bladder outlet obstruction, or modulate the androgenic pathways underlying BPH. A meaningful repurposing hypothesis would require the identification of entirely new and currently non-existent mechanistic evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Gadobutrol in Benign Prostatic Hyperplasia.

> **Context on lower-ranked predictions:** Gadobutrol has clinical trial evidence linked to **peripheral arterial disease** (rank 3, TxGNN score 76.72%) and **peripheral vascular disease** (rank 7, TxGNN score 74.39%), with 4 trials each. However, all of these trials use gadobutrol as a **diagnostic contrast agent** for MR angiography (MRA) — not as a therapeutic intervention. They confirm its imaging utility in vascular disease but provide no basis for therapeutic repurposing.

---

## Literature Evidence

Currently no related literature available for Gadobutrol in Benign Prostatic Hyperplasia.

> **Context on lower-ranked predictions:** The 20 PubMed publications retrieved for peripheral arterial disease (ranks 3–4) are uniformly imaging studies evaluating gadobutrol-enhanced MRA techniques, image quality comparisons with other contrast agents, and diagnostic accuracy versus digital subtraction angiography (DSA). Representative examples are listed below for completeness, but these represent **diagnostic** — not therapeutic — evidence.

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [26001243](https://pubmed.ncbi.nlm.nih.gov/26001243/) | 2015 | RCT | AJR Am J Roentgenology | Large randomised study comparing gadobutrol vs. gadoterate meglumine for 3T MRA in PAOD; non-inferiority demonstrated |
| [12928960](https://pubmed.ncbi.nlm.nih.gov/12928960/) | 2003 | Prospective | European Radiology | Prospective multicentre blinded comparison of gadobutrol-enhanced moving-table MRA vs. DSA in 203 patients with PAOD |
| [22848033](https://pubmed.ncbi.nlm.nih.gov/22848033/) | 2012 | RCT | J Magn Reson Imaging | Randomised crossover study of gadoterate 0.5M vs. gadobutrol 1.0M for peripheral MRA at 3.0T |
| [20959539](https://pubmed.ncbi.nlm.nih.gov/20959539/) | 2010 | Prospective | Radiology | Evaluation of high-resolution 3T peripheral MRA protocol using low-dose gadobutrol (0.1 mmol/kg) vs. conventional angiography |
| [15149986](https://pubmed.ncbi.nlm.nih.gov/15149986/) | 2004 | Prospective | AJR Am J Roentgenology | Whole-body 3D MRA with gadobutrol in 51 PAOD patients; diagnostic performance vs. DSA |
| [19652610](https://pubmed.ncbi.nlm.nih.gov/19652610/) | 2009 | Prospective | Investigative Radiology | Single-dose (0.1 mmol/kg) gadobutrol peripheral CTM-MRA combined with time-resolved TWIST-MRA at 3.0T |
| [12928957](https://pubmed.ncbi.nlm.nih.gov/12928957/) | 2003 | Safety study | European Radiology | Safety evaluation of 1.0M gadobutrol in 435 patients undergoing CE-MRA; adverse event profile |
| [23188773](https://pubmed.ncbi.nlm.nih.gov/23188773/) | 2013 | Prospective | J Magn Reson Imaging | Diagnostic accuracy of multi-station CE-MRA of lower extremities vs. DSA in symptomatic PAOD |
| [24156379](https://pubmed.ncbi.nlm.nih.gov/24156379/) | 2013 | Prospective | J Cardiovasc Magn Reson | Steady-state vascular imaging with gadobutrol as add-on to peripheral MRA protocol |
| [12720266](https://pubmed.ncbi.nlm.nih.gov/12720266/) | 2003 | Pilot | J Magn Reson Imaging | First experience with 1M gadobutrol for total-body 3D MRA covering carotids to runoff vessels in 72 seconds |

---

## Denmark Market Information

Gadobutrol (Gadovist®) does not appear in the data collected for the Danish Medicines Agency (Laegemiddelstyrelsen) database. This is a **data collection gap**, not absence from market — Gadovist® holds a centralised marketing authorisation from the European Medicines Agency (EMA), which is automatically valid in Denmark and all EU/EEA member states. Healthcare professionals should verify the current product listing directly.

> Please confirm current Danish market status via [Laegemiddelstyrelsen produktdatabase](https://www.laegemiddelstyrelsen.dk) or the [EMA medicines search](https://www.ema.europa.eu/en/medicines/find-medicine).

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for full safety information.

> As background context on gadolinium-based contrast agents (GBCAs) as a class: macrocyclic agents such as gadobutrol carry a significantly lower risk of gadolinium deposition and nephrogenic systemic fibrosis (NSF) compared to linear GBCAs, due to their more thermodynamically and kinetically stable chelate structure. Contraindications typically include severe renal impairment for linear agents; macrocyclic agents have a more favourable renal safety profile. The full SmPC should be consulted before any clinical use.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Gadobutrol is a diagnostic MRI contrast agent with no known therapeutic mechanism relevant to benign prostatic hyperplasia or any of the other predicted indications. The TxGNN score of 83.24% for BPH almost certainly reflects diagnostic co-occurrence (routine use in prostate mpMRI) rather than therapeutic potential, and no supporting clinical or preclinical evidence exists (Evidence Level L5). Additionally, the vascular disease predictions (ranks 3–8), while supported by a substantial imaging literature, represent diagnostic — not therapeutic — evidence.

**To proceed, the following is needed:**

- **Regulatory data remediation:** Verify and populate the Denmark/EMA marketing authorisation record for Gadovist® — current data shows zero licences, which is inconsistent with its EMA centralised authorisation status
- **Model artefact review:** Investigate whether the TxGNN BPH prediction arises from diagnostic co-occurrence in training data (prostate mpMRI use); if confirmed, this candidate should be flagged as a known model limitation
- **Mechanistic hypothesis:** If any new hypothesis arises suggesting gadolinium chelates have direct cellular activity in prostate tissue, targeted preclinical studies would be required before any clinical development consideration
- **Vascular indications reinterpretation:** The peripheral arterial disease / peripheral vascular disease evidence (ranks 3–8) should be re-classified as **diagnostic use evidence**, not therapeutic repurposing evidence, and the pipeline scoring logic updated accordingly
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

