---
layout: default
title: Erdafitinib
parent: 僅模型預測 (L5)
nav_order: 172
evidence_level: L5
indication_count: 10
---

# Erdafitinib
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

# Erdafitinib: From Urothelial Carcinoma to Pulmonary Hypertension

## One-Sentence Summary

Erdafitinib (Balversa) is a selective pan-FGFR kinase inhibitor approved by the US FDA for locally advanced or metastatic urothelial carcinoma harbouring susceptible FGFR3 or FGFR2 genetic alterations, but it currently holds no marketing authorisation in Denmark.
The TxGNN model predicts it may be effective for **Pulmonary Hypertension** (prediction score: 99.38%), offering a biologically plausible vascular remodelling rationale via the FGFR2 pathway.
However, **no clinical trials** and **no disease-specific publications** have been identified to support this indication, leaving the evidence at model-prediction level only (L5).

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Locally advanced or metastatic urothelial carcinoma with FGFR3/FGFR2 genetic alterations (FDA-approved; not registered in Denmark) |
| Predicted New Indication | Pulmonary Hypertension |
| TxGNN Prediction Score | 99.38% |
| Evidence Level | L5 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Erdafitinib is a pan-FGFR inhibitor (FGFR1–4) that competitively blocks ATP binding at the intracellular kinase domain of fibroblast growth factor receptors. By suppressing downstream MAPK/ERK and PI3K/AKT signalling, it halts the proliferation and survival of tumour cells that harbour activating FGFR alterations. Its established oncological use — urothelial carcinoma — is defined precisely by FGFR3/FGFR2 mutations or fusions.

The biological case for pulmonary arterial hypertension (PAH) rests on the well-documented role of FGFR2 in pulmonary vascular pathobiology. FGFR2 is overexpressed in the pulmonary vascular tissue of PAH patients, and FGF2 (basic FGF) actively drives pulmonary arterial smooth muscle cell proliferation and endothelial dysfunction — the two cardinal features of the vascular remodelling that characterises PAH. Blocking FGFR could, in principle, interrupt this aberrant remodelling loop.

However, the mechanistic relationship is inherently bidirectional: FGFR signalling also sustains normal vascular homeostasis and endothelial repair. Broad FGFR inhibition therefore carries a plausible risk of impairing the very repair mechanisms that counteract PAH progression. This fundamental ambiguity, combined with the complete absence of clinical or preclinical studies evaluating erdafitinib specifically in PAH, substantially limits the translational readiness of this prediction at present.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for pulmonary hypertension.

> **Note:** A single publication was retrieved for the rheumatoid arthritis prediction (rank 7–8):
>
> | PMID | Year | Type | Journal | Key Findings |
> |------|------|------|---------|-------------|
> | [31862477](https://pubmed.ncbi.nlm.nih.gov/31862477/) | 2020 | Comprehensive Review | Pharmacological Research | FDA-approved small molecule kinase inhibitors overview (2020 update); mentions erdafitinib among 2019 approvals as an FGFR inhibitor for urothelial carcinoma. Not specific to rheumatoid arthritis. |
>
> This reference does not constitute disease-specific evidence for any of the predicted indications.

---

## Denmark Market Information

Erdafitinib holds no marketing authorisation with the Danish Medicines Agency (Laegemiddelstyrelsen) and is not centrally authorised through the EMA for any indication. There are currently **0 active authorisations** in Denmark. Any clinical use would require either a named-patient import permit or a compassionate use application via the Laegemiddelstyrelsen.

---

## Cytotoxicity

Erdafitinib is an antineoplastic targeted therapy (FGFR inhibitor approved for urothelial carcinoma).

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — selective pan-FGFR kinase inhibitor (not conventional cytotoxic) |
| Myelosuppression Risk | Low to moderate (anaemia and thrombocytopenia reported; less pronounced than conventional cytotoxics) |
| Emetogenicity Classification | Low |
| Monitoring Items | Serum phosphate (hyperphosphataemia is a very common on-target class effect); retinal assessment (risk of central serous retinopathy and retinal pigment epithelium detachment); liver function tests; renal function; full blood count; electrolytes |
| Handling Protection | Standard oral anticancer drug precautions apply; follow local cytotoxic handling and disposal guidelines |

---

## Safety Considerations

Detailed Danish/EMA SmPC warnings and contraindications are not available in this Evidence Pack, as erdafitinib is not registered in Denmark.

Please refer to the FDA prescribing information (Balversa®, FDA label) for full safety data, including:

- **Reproductive toxicity warning**: The FDA label (Section 8.3) explicitly states that erdafitinib may cause **female infertility and menstrual irregularities**, including amenorrhoea as an observed adverse event in clinical trials. This is directly relevant to the TxGNN prediction of amenorrhoea (ranks 5–6) — this prediction most likely reflects the drug's established adverse effect profile rather than a genuine therapeutic opportunity, and should not be pursued.
- **Ocular toxicity**: Central serous retinopathy has been reported and requires baseline and periodic ophthalmological evaluation.
- **Hyperphosphataemia**: An on-target pharmacological effect requiring dietary phosphate restriction and, in some cases, phosphate-lowering therapy.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All five unique TxGNN-predicted indications — pulmonary hypertension, kyphoscoliotic heart disease, amenorrhoea, rheumatoid arthritis, and amyotrophic lateral sclerosis — are at Evidence Level L5 (model prediction only), with zero supporting clinical trials and no disease-specific literature. The top-ranked prediction (pulmonary hypertension) has a plausible but mechanistically ambiguous FGFR2 rationale that has not been tested in any clinical or preclinical study. Furthermore, the amenorrhoea prediction is actively contradicted by the drug's known adverse effect profile, illustrating a model artefact rather than a repurposing opportunity.

**To proceed, the following is needed:**

- Retrieval of the full FDA prescribing information (Balversa® SmPC/label) to complete the safety, contraindication, and drug interaction assessment
- Targeted literature search for FGFR inhibitors (class effect) in PAH preclinical models, to establish whether any in vitro or animal data supports the vascular remodelling hypothesis
- Mechanism of action data from DrugBank API to confirm FGFR selectivity profile and off-target kinase binding relevant to cardiovascular biology
- Regulatory pathway consultation with the Laegemiddelstyrelsen regarding requirements for repurposing trials or compassionate use in Denmark
- If preclinical data is supportive: design of a proof-of-concept study in an established PAH animal model (e.g., monocrotaline or SU5416/hypoxia rat model) before any clinical consideration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

