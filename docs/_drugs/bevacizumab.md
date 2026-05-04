---
layout: default
title: Bevacizumab
parent: 僅模型預測 (L5)
nav_order: 62
evidence_level: L5
indication_count: 10
---

# Bevacizumab
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

# Bevacizumab: From Anti-VEGF Cancer Therapy to Epiglottis Neoplasm

## One-Sentence Summary

Bevacizumab is a recombinant humanised monoclonal antibody that inhibits VEGF-A, clinically established for the treatment of multiple solid tumours including colorectal cancer, non-small cell lung cancer, and glioblastoma.
The TxGNN model predicts it may be effective for **Epiglottis Neoplasm**, with a prediction score of **99.90%**.
However, **no supporting clinical trials or published literature** currently exist for this specific indication, placing this prediction at the lowest evidence tier — based solely on knowledge graph topology.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Anti-VEGF therapy for solid tumours (globally established; no local Danish authorisation data on record) |
| Predicted New Indication | Epiglottis Neoplasm |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L5 (model prediction only — no actual studies) |
| Denmark Market Status | Not marketed (no local authorisation data recorded) |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on widely established pharmacology, Bevacizumab is a humanised IgG1 monoclonal antibody that selectively binds and neutralises vascular endothelial growth factor A (VEGF-A). By blocking the interaction of VEGF-A with its receptors (VEGFR-1 and VEGFR-2) on endothelial cells, Bevacizumab inhibits tumour-driven angiogenesis — the process through which solid tumours form new blood vessels to sustain their growth. This anti-angiogenic mechanism underpins its efficacy in a range of established oncology indications.

The theoretical basis for the TxGNN prediction is that epiglottis neoplasms, like other head and neck lesions, may exhibit VEGF-dependent vascularisation. The knowledge graph identifies structural proximity between Bevacizumab's established molecular target profile and the biological environment associated with epiglottis neoplasm, generating a high prediction score. The Evidence Pack's repurposing rationale explicitly notes that anti-VEGF-A inhibition could theoretically suppress angiogenesis in epiglottic tumour tissue.

However, this connection must be treated with substantial caution. Epiglottis neoplasms are predominantly benign in nature (e.g., haemangiomas, cysts, and squamous papillomas) and are typically managed with local endoscopic resection. No preclinical or clinical research exists to support systemic anti-VEGF biologic therapy in this setting. The clinical necessity, risk-benefit balance, and safety of deploying a potent systemic biologic agent in a typically benign, surgically manageable condition have not been evaluated in any study. This prediction reflects knowledge graph topological proximity rather than an established biological or clinical rationale.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Bevacizumab in epiglottis neoplasm on ClinicalTrials.gov or the WHO ICTRP.

---

## Literature Evidence

Currently no related literature available in PubMed specifically addressing Bevacizumab for epiglottis neoplasm.

---

## Denmark Market Information

No marketing authorisation records for Bevacizumab are present in the current dataset (0 authorisations). This almost certainly reflects a **data gap** in the local data collection process rather than genuine non-availability. Bevacizumab (Avastin®) holds a centralised European Medicines Agency (EMA) authorisation and is routinely used in clinical oncology across EU member states, including Denmark. Healthcare professionals should verify the current authorisation status and approved indications via the Danish Medicines Agency (Lægemiddelstyrelsen) at [www.laegemiddelstyrelsen.dk](https://www.laegemiddelstyrelsen.dk) or the EMA product database at [www.ema.europa.eu](https://www.ema.europa.eu).

---

## Cytotoxicity

Bevacizumab is classified as an antineoplastic agent (its original indication involves solid tumour treatment); this section is therefore included.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — Anti-VEGF monoclonal antibody (not a conventional cytotoxic agent) |
| Myelosuppression Risk | Low — Bevacizumab does not act on haematopoietic precursors; clinically significant bone marrow suppression is not expected |
| Emetogenicity Classification | Minimal — biologic/monoclonal antibody agents are not associated with meaningful nausea or vomiting |
| Monitoring Items | Blood pressure (hypertension is a class effect), urinalysis for proteinuria, full blood count (CBC), renal function tests, and wound healing status prior to any elective surgical procedures |
| Handling Protection | Standard biologic/monoclonal antibody handling procedures apply; cytotoxic-grade personal protective equipment and closed-system drug-transfer devices are generally not required |

---

## Safety Considerations

No formal warnings, contraindications, or drug interaction data are available in this Evidence Pack.

Please refer to the approved Summary of Product Characteristics (SmPC) for full safety information.

> **Note for prescribers:** Based on Bevacizumab's well-characterised pharmacological class, key known safety concerns include: hypertension, proteinuria, arterial and venous thromboembolic events (including stroke and myocardial infarction), gastrointestinal perforation, impaired wound healing, haemorrhage, and posterior reversible encephalopathy syndrome (PRES). These risks must be thoroughly assessed against any theoretical benefit before considering use in any novel indication.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This prediction is based entirely on knowledge graph topological similarity with zero supporting clinical trials or published literature. Epiglottis neoplasms are predominantly benign and adequately managed with local surgical or endoscopic resection; there is no established clinical need for systemic anti-VEGF biologic therapy in this population, and the safety profile has not been evaluated in this context.

**To proceed, the following is needed:**
- Histological confirmation that the target neoplasm is malignant, highly vascularised, and not amenable to surgical management — the only scenario where systemic biologics could be clinically justified
- Retrieval of formal MOA data from DrugBank (DB00112) to complete the mechanistic plausibility assessment
- Preclinical evidence (in vitro or in vivo) demonstrating VEGF dependency in epiglottic tumour models
- Full SmPC review for Bevacizumab (Avastin®) covering contraindications, warnings, and drug interactions, obtainable from Lægemiddelstyrelsen or the EMA
- Verification of current Danish/EMA marketing authorisation status and approved indications

---

### Additional Context: Other Predicted Indications from This Pack

This Evidence Pack covers five unique predicted indications for Bevacizumab. For reference:

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Decision |
|------|---------------------|-------------|----------------|----------|
| 1 | Epiglottis Neoplasm | 99.90% | L5 | **Hold** |
| 3 | Benign Neoplasm of Tongue | 99.90% | L4 | Research Question |
| 5 | Tumour of Testis and Paratestis | 99.90% | L5 | **Hold** |
| 7 | Benign Neoplasm of Hypopharynx | 99.90% | L5 | **Hold** |
| 9 | Benign Neoplasm of Floor of Mouth | 99.90% | L3 | Research Question |

The **Benign Neoplasm of Floor of Mouth** prediction carries the strongest evidence in this pack (L3), supported by one Phase I clinical trial ([NCT01552434](https://clinicaltrials.gov/study/NCT01552434)) investigating Bevacizumab in head and neck malignancies and two relevant preclinical publications. If repurposing exploration for Bevacizumab is to continue, this indication represents the most tractable research starting point, noting that all current evidence concerns malignant rather than benign lesions.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

