---
layout: default
title: Binimetinib
parent: 僅模型預測 (L5)
nav_order: 66
evidence_level: L5
indication_count: 0
---

# Binimetinib
{: .fs-9 }

證據等級: **L5** | 預測適應症: **0** 個
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

# Binimetinib: MEK1/2 Inhibitor — Evaluation on Hold (Incomplete Evidence Pack)

## One-Sentence Summary

Binimetinib (Mektovi) is a selective MEK1/2 inhibitor in the targeted oncology class, approved by EMA for BRAF V600-mutant unresectable or metastatic melanoma in combination with encorafenib.
The current Evidence Pack contains **no TxGNN repurposing predictions** for this compound, and two data gaps — including safety data (Blocking) and mechanism of action documentation (High) — prevent a complete evaluation.
A meaningful repurposing assessment cannot be finalised until these gaps are resolved and the TxGNN prediction pipeline is re-run.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | BRAF V600-mutant unresectable or metastatic melanoma (EMA-approved; not reflected in current registry data) |
| Predicted New Indication | No predictions generated |
| TxGNN Prediction Score | N/A |
| Evidence Level | N/A — pipeline did not produce candidates |
| Denmark Market Status | Not registered in local registry (centralised EMA authorisation likely applies — see below) |
| Number of Marketing Authorisations | 0 (per registry data) |
| Recommended Decision | **Hold** |

---

## Why Is This Prediction Reasonable?

No TxGNN predictions were generated for binimetinib in the current Evidence Pack, so no prediction-specific mechanistic rationale can be provided. The prediction pipeline must be re-executed before any repurposing direction can be formally evaluated.

From established pharmacological knowledge, binimetinib is a selective, ATP non-competitive inhibitor of MEK1 and MEK2 — serine/threonine kinases that are central nodes in the MAPK/ERK signalling cascade. Dysregulation of this pathway drives proliferation across a broad spectrum of human malignancies: colorectal cancer (KRAS/BRAF-mutant), non-small cell lung cancer, pancreatic cancer, and several haematological cancers. This biological breadth makes binimetinib a plausible candidate for TxGNN repurposing predictions, particularly within the oncology space, once the data infrastructure is complete.

Mechanism of action documentation (data gap DG002) is currently absent from the Evidence Pack, which prevents formal pathway-level analysis. Once DrugBank MOA data is retrieved, a more rigorous mechanistic rationale connecting the original melanoma indication to candidate repurposing targets can be constructed.

---

## Denmark Market Information

The Evidence Pack records **0 marketing authorisations** in the Danish national registry. However, binimetinib holds a **centralised EMA marketing authorisation** (EU/1/18/1314, Pierre Fabre), which is directly valid in all EU/EEA member states including Denmark. This strongly suggests a data collection gap in the current pipeline rather than a genuine absence of authorisation.

The table below is populated from EMA public records; it is **not** sourced from the Evidence Pack:

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|------|------|------|------|
| EU/1/18/1314 | Mektovi | Film-coated tablet (15 mg) | Unresectable or metastatic melanoma with BRAF V600 mutation, in combination with encorafenib (Braftovi) |

> ⚠️ **Action required:** The local registry query should be reviewed to confirm that EMA centralised authorisations are correctly captured. Clinicians should consult the Lægemiddelstyrelsen product database and the EMA Product Information page directly.

---

## Cytotoxicity

Binimetinib is a targeted antineoplastic agent (small-molecule kinase inhibitor). The following information is derived from general pharmacological knowledge of the MEK inhibitor class, as DrugBank toxicity data was not retrieved in the current Evidence Pack.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — selective MEK1/2 inhibitor (non-conventional cytotoxic) |
| Myelosuppression Risk | Low to moderate — anaemia is the most commonly reported haematological effect; not primarily myelosuppressive compared to conventional cytotoxics |
| Emetogenicity Classification | Low |
| Monitoring Items | Liver function tests (hepatotoxicity), ophthalmological examinations (retinal vein occlusion, retinal pigment epithelial detachment, uveitis), ECG (QTc prolongation), creatine phosphokinase (rhabdomyolysis), blood pressure, left ventricular ejection fraction (cardiomyopathy) |
| Handling Protection | Standard oral oncology precautions apply; not classified as a traditional cytotoxic — follow local pharmacy handling guidelines for oral targeted therapies |

---

## Safety Considerations

Safety warnings and contraindications are flagged as a **Blocking data gap** (DG001) in the current Evidence Pack. No drug-drug interaction data was returned in the query log.

Please refer to the approved Summary of Product Characteristics (SmPC) for Mektovi for full prescribing safety information. Key areas of clinical concern known from the MEK inhibitor class include:

- Serious ocular events (retinal vein occlusion, uveitis, retinal pigment epithelial detachment)
- Hepatotoxicity (monitor LFTs)
- Cardiomyopathy / decreased LVEF
- Venous thromboembolism and pulmonary embolism
- Severe skin reactions
- Rhabdomyolysis (elevated CPK)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Evidence Pack for binimetinib is critically incomplete — no TxGNN repurposing candidates were generated, and a Blocking data gap (DG001: regulatory safety data) prevents the mandatory S1 safety screening step from being executed. No repurposing evaluation can be responsibly issued under these conditions.

**To proceed, the following is needed:**

- **[Blocking — DG001]** Retrieve and parse TFDA/EMA SmPC PDF to populate warnings, contraindications, and special precautions
- **[High — DG002]** Query DrugBank API to populate mechanism of action data and enable pathway-level mechanistic analysis
- **Re-run TxGNN prediction pipeline** once drug-level data is complete, to generate repurposing candidates for this drug
- **Fix regulatory data collection** to correctly capture the EMA centralised authorisation (EU/1/18/1314 — Mektovi) for Denmark
- **Re-query DDI database** after MOA data is available, to assess interaction risk for the predicted indication population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

