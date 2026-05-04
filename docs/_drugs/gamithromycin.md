---
layout: default
title: Gamithromycin
parent: 僅模型預測 (L5)
nav_order: 204
evidence_level: L5
indication_count: 10
---

# Gamithromycin
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

# Gamithromycin: From Bovine Respiratory Disease to Interventricular Septum Aneurysm

## One-Sentence Summary

Gamithromycin is a long-acting macrolide antibiotic developed exclusively for veterinary use, approved in several markets for treatment of bovine respiratory disease (BRD) in cattle. The TxGNN model predicts it may have activity against **Interventricular Septum Aneurysm**, with a prediction score of **95.67%**. However, **no clinical trials and no published literature** currently support this direction, and the predicted indication is a structural cardiac defect with no plausible mechanistic link to macrolide antibiotic pharmacology.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Bovine respiratory disease (veterinary use only; no human approvals) |
| Predicted New Indication | Interventricular Septum Aneurysm |
| TxGNN Prediction Score | 95.67% |
| Evidence Level | L5 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for Gamithromycin is not currently available in the Evidence Pack. Based on its drug class, Gamithromycin belongs to the azalide subclass of macrolide antibiotics and, like other macrolides (e.g., azithromycin, tulathromycin), likely exerts its antimicrobial effect by binding to the 50S ribosomal subunit, thereby inhibiting bacterial protein synthesis. Macrolides as a class are also known to have secondary immunomodulatory properties, including suppression of pro-inflammatory cytokines such as IL-6 and TNF-α. However, Gamithromycin has been developed and authorised solely for veterinary use, and no human pharmacokinetic or clinical data are available.

Interventricular septum aneurysm (ISA) is a structural cardiac abnormality — either congenital or acquired as a sequela of myocardial infarction or inflammation — characterised by abnormal outpouching of the interventricular septum. The pathophysiology is primarily mechanical and structural, with no known infectious or sustained inflammatory driver that macrolide antibiotics could meaningfully address. The immunomodulatory properties of macrolides (cytokine suppression) do not translate to any established mechanism for remodelling or repairing cardiac wall architecture.

The high TxGNN score most likely reflects indirect graph-level connectivity between the macrolide drug node and cardiac structural disease nodes in the knowledge graph, rather than a direct biological relationship. All five of the top-ranked predicted indications in this pack are structural cardiac or craniofacial developmental anomalies — a pattern consistent with a systematic knowledge graph artefact rather than true pharmacological plausibility. This prediction is assessed as a **model false positive**.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Denmark Market Information

Gamithromycin holds no marketing authorisations in Denmark. The drug is not registered by the Danish Medicines Agency (Lægemiddelstyrelsen) for human use, nor does it hold a centralised EMA authorisation for human indications. It is authorised in the EU exclusively as a veterinary medicinal product (e.g., Zactran® / Tulaven® class veterinary authorisations for cattle).

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information. No human safety data, DDI data, contraindications, or key warnings are available in the current Evidence Pack.

> **Important note for Danish healthcare professionals:** As a veterinary-only macrolide, Gamithromycin has undergone no human clinical safety evaluation. Macrolides as a class carry known risks in humans including QT interval prolongation, hepatotoxicity, and drug interactions via CYP3A4 inhibition. These class-level risks are particularly relevant given the cardiac nature of the predicted indication. Any extrapolation from veterinary pharmacology to human use would require a full first-in-human safety programme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Gamithromycin is a veterinary macrolide antibiotic with no human approvals, no human clinical data, and no biological plausibility for the top-predicted indication of interventricular septum aneurysm — a structural cardiac defect incompatible with antibiotic or immunomodulatory mechanisms. The L5 evidence level (model prediction only) combined with the absence of a credible mechanistic rationale and the veterinary-only regulatory status makes further development towards this indication unjustifiable at this stage.

**To proceed, the following would be needed:**

- Formal mechanistic hypothesis connecting macrolide immunomodulation to cardiac structural pathology (currently absent)
- Human pharmacokinetic and safety data for Gamithromycin (requires dedicated first-in-human studies)
- At least preclinical (in vitro or animal model) evidence demonstrating relevant activity in cardiac structural disease, to upgrade from L5 to L4
- Regulatory pathway assessment from the Danish Medicines Agency (Lægemiddelstyrelsen) and EMA for reclassification from veterinary to human use
- MOA data retrieval from DrugBank (Data Gap DG002) to enable proper mechanistic analysis
- Re-evaluation of whether the TxGNN predictions across all five indications represent a shared graph artefact, warranting a flag in the model's output for this drug node

> **This report is for research purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before any application in patient care.**
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

