---
layout: default
title: Empagliflozin
parent: 僅模型預測 (L5)
nav_order: 162
evidence_level: L5
indication_count: 6
---

# Empagliflozin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Empagliflozin: From Type 2 Diabetes Mellitus to Classic Stiff Person Syndrome

## One-Sentence Summary

Empagliflozin is a sodium-glucose co-transporter 2 (SGLT2) inhibitor primarily established for the treatment of type 2 diabetes mellitus, heart failure, and chronic kidney disease.
The TxGNN model predicts it may be effective for **Classic Stiff Person Syndrome**, a rare autoimmune neurological disorder characterised by progressive muscle rigidity.
However, **no clinical trials or published literature** currently support this repurposing direction, and the mechanistic link is considered highly speculative.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Type 2 Diabetes Mellitus (SGLT2 inhibitor class; known from pharmacological class — not derived from regulatory database) |
| Predicted New Indication | Classic Stiff Person Syndrome |
| TxGNN Prediction Score | 99.06% |
| Evidence Level | L5 |
| Denmark Market Status | Not found in regulatory database *(see note below)* |
| Number of Marketing Authorisations | 0 *(data source limitation — see note below)* |
| Recommended Decision | Hold |

> **⚠️ Data Source Note:** The regulatory database consulted returned no records for empagliflozin. This likely reflects a limitation of the data source rather than actual market absence. Empagliflozin (Jardiance®) holds a centralised EMA marketing authorisation valid across all EU/EEA member states, including Denmark. Clinicians should verify the current approved indications and SmPC directly via the [EMA product page](https://www.ema.europa.eu/en/medicines/human/EPAR/jardiance) or the Danish Medicines Agency ([Lægemiddelstyrelsen](https://www.laegemiddelstyrelsen.dk/)).

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the current Evidence Pack. Based on its pharmacological class, empagliflozin is an SGLT2 inhibitor that reduces glucose reabsorption in the renal proximal tubule, lowering blood glucose independently of insulin. Beyond glycaemic control, SGLT2 inhibitors have demonstrated pleiotropic anti-inflammatory effects — including downregulation of NF-κB signalling and reduction of circulating IL-6 and TNF-α — as well as potential neuroprotective properties through AMPK activation and promotion of ketone body production.

Classic Stiff Person Syndrome (SPS) is a rare, severe autoimmune neurological condition. It is primarily driven by anti-GAD65 antibodies (directed against glutamic acid decarboxylase 65), which disrupt GABAergic inhibitory interneurons in the spinal cord and brainstem, leading to relentless axial muscle stiffness, episodic spasms, and progressive disability. The TxGNN model likely identifies a distant connection via shared inflammatory or metabolic network nodes in the biomedical knowledge graph.

However, the mechanistic link between SGLT2 inhibition and SPS pathophysiology is **highly indirect and speculative**. There is currently no experimental evidence that empagliflozin can modulate anti-GAD65 autoimmunity, penetrate the central nervous system at clinically relevant concentrations, or directly restore GABAergic inhibitory tone. The peripheral anti-inflammatory effects of SGLT2 inhibition, while real, are unlikely to address the core central autoimmune mechanism of SPS. Biological plausibility for clinical benefit is therefore considered very low at this stage.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for empagliflozin in classic stiff person syndrome.

---

## Literature Evidence

Currently no related literature available for empagliflozin in classic stiff person syndrome.

---

## Denmark Market Information

No marketing authorisation records were returned from the regulatory database for empagliflozin. As noted above, this reflects a data gap rather than actual non-approval. For confirmed authorisation details and the current approved SmPC, please consult:

- **EMA:** [Jardiance® EPAR](https://www.ema.europa.eu/en/medicines/human/EPAR/jardiance)
- **Lægemiddelstyrelsen:** [produktresumé (SmPC)](https://www.laegemiddelstyrelsen.dk/)

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

Full safety data — including key warnings, contraindications, and drug interactions — were not available in the Evidence Pack for this candidate. The SmPC for Jardiance® (empagliflozin) is accessible via the EMA EPAR link above and contains information on, among others: risk of diabetic ketoacidosis, urogenital infections, volume depletion, Fournier's gangrene, and renal function monitoring requirements.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN prediction score (99.06%), there is currently no supporting clinical or preclinical evidence for empagliflozin in classic stiff person syndrome, and the mechanistic connection to the core anti-GAD65 / GABAergic pathophysiology of SPS is highly speculative with extremely low biological plausibility. Progression at this stage is not warranted.

**To proceed, the following is needed:**

- **Preclinical evidence:** In vitro or animal model data demonstrating that SGLT2 inhibition affects GABAergic circuits, neuroinflammation, or anti-GAD65 autoimmune activity in the central nervous system
- **Mechanistic hypothesis refinement:** A credible biological pathway connecting empagliflozin's known molecular effects to SPS pathophysiology (e.g., via CNS ketone body utilisation in GABAergic neurons, or modulation of peripheral Treg/Th17 balance relevant to anti-GAD65 autoimmunity)
- **Clinical signal:** At least one published case report or pharmacovigilance signal suggesting unexpected benefit in SPS patients already receiving empagliflozin for diabetes or heart failure
- **Full safety profile:** Retrieval of the complete SmPC (warnings, contraindications, and drug interactions) from EMA/Lægemiddelstyrelsen to enable a proper S1 safety screen
- **Regulatory confirmation:** Verification of the current approved indications and any off-label use frameworks applicable in Denmark

---

*This report is generated for research reference only. Drug repurposing candidates require clinical validation before therapeutic application. All content should be interpreted in accordance with applicable YMYL (Your Money or Your Life) standards for medical information.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

