---
layout: default
title: Cemiplimab
parent: 僅模型預測 (L5)
nav_order: 101
evidence_level: L5
indication_count: 10
---

# Cemiplimab
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

# Cemiplimab: From Cutaneous Squamous Cell Carcinoma to Gallbladder Adenosquamous Carcinoma

## One-Sentence Summary

Cemiplimab (Libtayo®) is a fully human anti-PD-1 monoclonal antibody (immune checkpoint inhibitor) approved globally for cutaneous squamous cell carcinoma (cSCC), basal cell carcinoma (BCC), and non-small cell lung cancer (NSCLC), though it currently holds no marketing authorisation in Denmark.
The TxGNN model predicts it may be effective for **gallbladder adenosquamous carcinoma** as the highest-ranked indication, supported by **0 clinical trials** and **0 publications** for this specific subtype.
This is a multi-indication evaluation (5 unique oncological predictions), ranging from L3 evidence (external ear basal cell carcinoma, which aligns with cemiplimab's globally approved BCC indication) to L5 model-only predictions; overall recommended decisions vary from **Hold** to **Proceed with Guardrails** depending on the predicted indication.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Denmark; globally approved for cutaneous squamous cell carcinoma (cSCC), BCC, NSCLC, and cervical cancer (Libtayo® / Regeneron–Sanofi) |
| Predicted New Indication (Rank 1) | Gallbladder adenosquamous carcinoma |
| TxGNN Prediction Score | 99.99% |
| Evidence Level (Rank 1) | L5 — Model prediction only; no supporting studies |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision (Rank 1) | Hold |

---

## All Predicted Indications — Overview

This evaluation is a multi-indication candidate (ID: TW-DB14707-multi). The five unique predicted indications are summarised below (duplicate rank entries in the source data have been consolidated):

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Recommended Decision |
|------|---------------------|-------------|----------------|----------------------|
| 1 | Gallbladder adenosquamous carcinoma | 99.99% | L5 | Hold |
| 3 | Glottis squamous cell carcinoma | 99.99% | L4 | Research Question |
| 5 | Rectal cloacogenic carcinoma | 99.99% | L5 | Hold |
| **7** | **External ear basal cell carcinoma** | **99.99%** | **L3** | **Proceed with Guardrails** |
| 9 | Adenosquamous prostate carcinoma | 99.99% | L5 | Hold |

> **Key clinical finding**: The highest-evidence prediction (external ear BCC, L3) corresponds directly to cemiplimab's globally approved BCC indication (EMPOWER-BCC-1, FDA approval 2021; EMA approval). The "Not marketed" status in Denmark most likely reflects a local market access gap rather than absence of clinical evidence or regulatory approval.

---

## Why is This Prediction Reasonable?

**Mechanism of Action**

The Evidence Pack does not contain mechanistic action (MOA) data for cemiplimab. Based on published information, cemiplimab is a fully human IgG4 monoclonal antibody that binds specifically to the programmed cell death receptor 1 (PD-1) on T lymphocytes, blocking its interaction with PD-L1 and PD-L2 on tumour cells and antigen-presenting cells. This blockade relieves PD-1-mediated suppression of anti-tumour T-cell activity, restoring immune-mediated cytotoxicity within the tumour microenvironment. Cemiplimab is classified as an immune checkpoint inhibitor (ICI) and belongs to the anti-PD-1 immunotherapy category — not a conventional cytotoxic agent.

**Rank 1 — Gallbladder Adenosquamous Carcinoma (L5, Hold)**

Gallbladder adenosquamous carcinoma is a rare mixed histological subtype containing both glandular (adenocarcinoma) and squamous cell carcinoma components. The squamous cell component theoretically may express PD-L1, providing a mechanistic rationale for PD-1 blockade. Indirect support comes from the structurally related checkpoint inhibitor durvalumab, which demonstrated a statistically significant overall survival benefit in biliary tract cancer in the TOPAZ-1 Phase 3 trial. However, cemiplimab has no published clinical data in this specific rare subtype, and the TxGNN high score most likely reflects broad class-level inference from the squamous cell carcinoma category rather than indication-specific mechanistic support. This prediction requires substantially more evidence before clinical consideration.

**Most Evidence-Supported — External Ear Basal Cell Carcinoma (L3, Proceed with Guardrails)**

Basal cell carcinoma of the external ear is an anatomical subtype of BCC characterised by high surgical complexity due to proximity to the facial nerve and parotid gland, making curative resection frequently impractical. Cemiplimab received FDA approval in February 2021 for locally advanced and metastatic BCC in patients who are not candidates for curative surgery or curative radiation therapy after progression on a Hedgehog pathway inhibitor (vismodegib/sonidegib), supported by the EMPOWER-BCC-1 Phase 2 programme; EMA subsequently granted centralised authorisation. External ear BCC is precisely the clinical scenario for which this approval was designed. One published case report (PMID 34157152) documents a durable, lasting response following cemiplimab discontinuation in a patient with locally advanced BCC, mechanistically consistent with the approved indication. This is not a classic drug repurposing situation; rather, it represents a market access gap in Denmark for an already globally validated indication.

**Glottis Squamous Cell Carcinoma (L4, Research Question)**

Glottic squamous cell carcinoma falls within the head and neck squamous cell carcinoma (HNSCC) spectrum. Cemiplimab's EMPOWER-HN clinical programme has generated Phase 2/3 data across HNSCC tumour sites, including laryngeal subgroups. Glottic SCC shares key immunotherapy biomarker profiles with other HNSCC subsites — PD-L1 expression, tumour mutational burden (TMB), and HPV status — making the mechanistic analogy compelling. However, glottis-specific subgroup data are not independently available, and the evidence relies on indirect extrapolation from broader HNSCC datasets.

---

## Clinical Trial Evidence

No clinical trials were identified for any of the 5 predicted indications in this evaluation (gallbladder adenosquamous carcinoma, glottis SCC, rectal cloacogenic carcinoma, external ear BCC, or adenosquamous prostate carcinoma).

Note for clinical context: Cemiplimab has extensive Phase 2/3 trial data in related broader tumour categories (EMPOWER-BCC-1 for BCC, EMPOWER-HN for HNSCC, EMPOWER-Lung 1 and 3 for NSCLC), which underpin its global regulatory approvals. These are not listed here as they were not retrieved in the evidence collection queries for the specific predicted indications above.

---

## Literature Evidence

Literature evidence was identified only for **external ear basal cell carcinoma** (rank 7):

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [34157152](https://pubmed.ncbi.nlm.nih.gov/34157152/) | 2021 | Case Report | Clinical and Experimental Dermatology | Documents a lasting clinical response in a patient with locally advanced BCC following discontinuation of cemiplimab, supporting the durability of anti-PD-1 immune response in BCC and the potential for sustained remission after treatment cessation |

No literature was identified for gallbladder adenosquamous carcinoma, glottis SCC, rectal cloacogenic carcinoma, or adenosquamous prostate carcinoma with cemiplimab.

---

## Denmark Market Information

Cemiplimab currently holds **no marketing authorisations** in Denmark (Lægemiddelstyrelsen), with a total of 0 registered products.

However, cemiplimab (Libtayo®) holds a valid EMA centralised marketing authorisation covering the following indications — accessible in principle to Danish patients via Named Patient Programme (NPP) or comparable access pathways:

| Authorisation | Product Name | Dosage Form | Approved Indication |
|--------------|--------------|-------------|---------------------|
| EU/1/19/1376 (EMA) | Libtayo® | Concentrate for solution for infusion (350 mg/7 mL) | Cutaneous squamous cell carcinoma (cSCC) — locally advanced or metastatic; Basal cell carcinoma (BCC) — locally advanced or metastatic, after Hedgehog pathway inhibitor failure; Non-small cell lung carcinoma (NSCLC) — first-line, in combination with platinum-based chemotherapy; Cervical cancer — recurrent or ... |

> Danish prescribers seeking access for eligible patients should consult Lægemiddelstyrelsen regarding NPP/compassionate use procedures under European Regulation (EC) No 726/2004 Article 83.

---

## Cytotoxicity

Cemiplimab is an antineoplastic agent targeting solid malignancies. The following classification applies:

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Immunotherapy — Immune checkpoint inhibitor (fully human anti-PD-1 IgG4 monoclonal antibody); not a conventional cytotoxic agent |
| Myelosuppression Risk | Low compared to conventional chemotherapy; however, immune-related haematological adverse events (immune thrombocytopaenia, haemolytic anaemia, aplastic anaemia) can occur and require monitoring |
| Emetogenicity Classification | Minimal; immunotherapy agents are not associated with direct emetogenicity |
| Monitoring Items | CBC with differential, liver function tests (ALT, AST, bilirubin), thyroid function (TSH, free T4), morning cortisol/ACTH (for immune-mediated adrenal insufficiency), renal function (creatinine), blood glucose (immune-mediated type 1 diabetes mellitus), and clinical assessment for pneumonitis and colitis at each visit |
| Handling Protection | Standard biosafety precautions for monoclonal antibody preparations; conventional cytotoxic handling regulations do not apply, but institutional biological medicine safety protocols should be followed |

---

## Safety Considerations

Please refer to the EMA-approved Summary of Product Characteristics (SmPC) for Libtayo® for complete safety information, available via the European Medicines Agency (EMA) EPAR database.

Key considerations relevant to Danish prescribers:

- **Immune-related adverse events (irAEs)**: As a PD-1 checkpoint inhibitor, cemiplimab carries risk of immune-mediated pneumonitis, colitis, hepatitis, endocrinopathies (hypothyroidism, hyperthyroidism, adrenal insufficiency, type 1 diabetes mellitus), nephritis, and dermatitis. Severe irAEs (Grade 3–4) require treatment suspension and high-dose systemic corticosteroids; specialist referral (pulmonology, gastroenterology, endocrinology) is recommended.
- **Drug Interactions**: No DDI data were retrieved in this evaluation. Note that corticosteroids used to manage irAEs may potentially attenuate immunotherapy efficacy; the timing and dose of immunosuppressive therapy require careful clinical judgement and should follow published irAE management guidelines (e.g., ESMO/ASCO guidelines).

---

## Conclusion and Next Steps

---

### Primary Prediction: Gallbladder Adenosquamous Carcinoma

**Decision: Hold**

**Rationale:**
Gallbladder adenosquamous carcinoma is an ultra-rare tumour subtype with no identified clinical trial or published data for cemiplimab. The TxGNN high score reflects model-level generalisation from the squamous cell carcinoma category and does not provide sufficient clinical basis for use outside a formal investigational framework.

**To proceed, the following is needed:**
- Biomarker profiling (PD-L1 expression by IHC, TMB, MSI/MMR status) of gallbladder adenosquamous carcinoma tissue samples to confirm immunotherapy-susceptible biology
- Consideration for basket trial enrolment (tumour-agnostic PD-1 inhibitor programmes covering rare biliary/GI cancers)
- Multidisciplinary tumour board review in a specialised hepatobiliary oncology centre
- Review of emerging data from durvalumab (TOPAZ-1) in biliary tract cancer for indirect mechanistic benchmarking

---

### Most Clinically Actionable Prediction: External Ear Basal Cell Carcinoma

**Decision: Proceed with Guardrails**

**Rationale:**
External ear BCC falls squarely within cemiplimab's EMA-approved indication for locally advanced/metastatic BCC after Hedgehog pathway inhibitor failure. The "not marketed" status in Denmark appears to represent a market access gap rather than absence of validated evidence, making this the most actionable finding in this evaluation.

**To proceed, the following is needed:**
- Application for Named Patient Programme (NPP) or Expanded Access via Lægemiddelstyrelsen, citing the valid EMA marketing authorisation (Libtayo®, EU/1/19/1376)
- Confirmation of prior Hedgehog pathway inhibitor therapy (vismodegib or sonidegib) or documented contraindication, per the approved indication criteria
- Multidisciplinary assessment involving dermatology, ENT/head & neck surgery, and oncology to confirm non-resectability of the primary lesion
- Patient-specific PD-L1 testing where feasible, and baseline performance status and organ function assessment
- Full irAE safety monitoring plan per SmPC, including documented patient consent and access to specialist irAE management

---

> **Disclaimer**: This report is intended for research purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before clinical application. For patient-specific treatment decisions, please consult the approved Summary of Product Characteristics (SmPC) and applicable clinical practice guidelines.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

