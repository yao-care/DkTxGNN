---
layout: default
title: Atezolizumab
parent: 僅模型預測 (L5)
nav_order: 48
evidence_level: L5
indication_count: 10
---

# Atezolizumab
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

# Atezolizumab: From Urothelial Carcinoma to Prostatic Urethra Urothelial Carcinoma

## One-Sentence Summary

Atezolizumab (Tecentriq, Roche/Genentech) is an anti-PD-L1 monoclonal antibody and immune checkpoint inhibitor, globally approved for urothelial carcinoma (bladder cancer), non-small-cell lung cancer, triple-negative breast cancer, and hepatocellular carcinoma — though not currently authorised in Denmark.
The TxGNN model predicts it may be effective for **prostatic urethra urothelial carcinoma** (a rare urothelial malignancy at the prostatic urethral segment), with **2 clinical trials** currently supporting this direction.
Evidence is graded **L2**, based on a completed Phase 2 single-arm trial in BCG-unresponsive bladder urothelial carcinoma — the same histological tumour type.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Denmark; globally approved for urothelial carcinoma, NSCLC, TNBC, and HCC |
| Predicted New Indication | Prostatic Urethra Urothelial Carcinoma |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L2 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Atezolizumab is a humanised IgG1 monoclonal antibody that blocks the interaction between PD-L1 (Programmed Death Ligand 1) and its receptors PD-1 and B7-1. By disrupting this interaction, the drug reverses T-cell exhaustion within the tumour microenvironment, restoring anti-tumour immune activity. This mechanism is tumour-type agnostic in principle — its effectiveness depends on tumour mutational burden (TMB) and PD-L1 expression, rather than on the anatomical site of origin.

Prostatic urethra urothelial carcinoma is histologically identical to bladder urothelial carcinoma: both arise from urothelial (transitional) epithelium and share the same characteristic features of high TMB and elevated PD-L1 expression that make the broader urothelial carcinoma class immunotherapy-sensitive. The anatomical distinction (urethral vs. bladder location) does not alter the fundamental tumour biology — a completed Phase 2 trial (NCT02844816) of atezolizumab monotherapy in BCG-unresponsive non-muscle-invasive bladder cancer provides the strongest translational anchor, as the target tissue is identical.

The mechanistic link is therefore strong: PD-L1 blockade is the established mechanism of action in approved urothelial carcinoma indications globally, and the predicted extension to the prostatic urethral segment represents an anatomical extrapolation within the same histological family, rather than a mechanistic leap. This is further supported by the inclusion of urethral urothelial carcinoma patients in a large Phase 1b combination trial (NCT03170960), confirming clinical feasibility of this approach.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|-----------|--------------|
| [NCT02844816](https://clinicaltrials.gov/study/NCT02844816) | Phase 2 | Completed | 172 | Atezolizumab monotherapy in BCG-unresponsive non-muscle-invasive bladder cancer (NMIBC). Directly evaluates atezolizumab single-agent activity in urothelial carcinoma of the bladder — the closest histological match to prostatic urethral urothelial carcinoma. Completed with adequate sample size; constitutes the primary basis for L2 evidence grading. |
| [NCT03170960](https://clinicaltrials.gov/study/NCT03170960) | Phase 1b | Active, not recruiting | 914 | Dose-escalation study of cabozantinib alone or in combination with atezolizumab across multiple solid tumours, explicitly including urothelial carcinoma (bladder, renal pelvis, ureter, **urethra**), RCC, CRPC, NSCLC, TNBC, and ovarian cancer. Large multicentre trial; provides supplementary safety and exploratory efficacy signals for atezolizumab in urethral urothelial carcinoma, but cannot isolate atezolizumab's contribution as a combination design. |

---

## Literature Evidence

Currently no related literature directly addressing atezolizumab in prostatic urethra urothelial carcinoma is available.

---

## Denmark Market Information

Atezolizumab currently holds no marketing authorisation in Denmark through the Danish Medicines Agency (Lægemiddelstyrelsen), nor does it appear to hold a valid centralised EMA authorisation active in the Danish market as of the data cut-off (April 2026). Note: Tecentriq received a positive EMA opinion historically; clinicians should verify the current authorisation and market availability status directly via the [EMA product database](https://www.ema.europa.eu/en/medicines) and [Lægemiddelstyrelsen's register](https://laegemiddelstyrelsen.dk).

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|-------------------------------|-------------|-------------|---------------------|
| — | — | — | No authorisations currently registered in the Danish market |

---

## Cytotoxicity

Atezolizumab is an antineoplastic agent (immune checkpoint inhibitor) used exclusively in oncology settings.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Immunotherapy — Immune Checkpoint Inhibitor (anti-PD-L1 monoclonal antibody); not a conventional cytotoxic agent |
| Myelosuppression Risk | Low (immune-mediated cytopenias such as immune thrombocytopenia and haemolytic anaemia reported as rare immune-related adverse events, not direct myelosuppression) |
| Emetogenicity Classification | Minimal (monoclonal antibodies carry negligible direct emetogenic potential) |
| Monitoring Items | Liver function tests (immune-mediated hepatitis), thyroid function (immune-mediated thyroiditis), blood glucose (immune-mediated diabetes), renal function, CBC, chest imaging (immune-mediated pneumonitis), adrenal function |
| Handling Protection | Standard monoclonal antibody handling precautions apply; does not require cytotoxic drug handling facilities under current European guidelines, but local pharmacy protocols should be consulted |

---

## Safety Considerations

No drug-specific safety data (key warnings, contraindications, or drug interactions) is available in this Evidence Pack. Atezolizumab carries a well-characterised class-wide immune-related adverse event (irAE) profile as an immune checkpoint inhibitor.

> Please refer to the approved Summary of Product Characteristics (SmPC) for full safety information. Clinicians should specifically review guidance on immune-mediated adverse reactions (pneumonitis, colitis, hepatitis, endocrinopathies, nephritis, and skin reactions), infusion-related reactions, and embryo-foetal toxicity.

---

## Additional Predicted Indications (Overview)

The TxGNN model identified five distinct indications in this Evidence Pack. For completeness:

| Rank | Disease | TxGNN Score | Evidence Level | Recommendation |
|------|---------|------------|----------------|----------------|
| 1 | Prostatic urethra urothelial carcinoma | 99.98% | L2 | **Proceed with Guardrails** |
| 3 | Kidney pelvis sarcomatoid transitional cell carcinoma | 99.98% | L5 | Hold |
| 5 | Infiltrating bladder urothelial carcinoma, sarcomatoid variant | 99.98% | L5 | Hold |
| 7 | Renal pelvis papillary urothelial carcinoma (UTUC) | 99.98% | L3 | Research Question |
| 9 | Uterine ligament adenocarcinoma | 99.93% | L5 | Hold |

The three L5 indications lack any clinical trial or literature evidence and rely solely on model prediction; they are not recommended for near-term clinical development. Renal pelvis papillary urothelial carcinoma (UTUC, rank 7) warrants monitoring as a research question given the mechanistic plausibility and inclusion of UTUC patients in NCT03170960.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Prostatic urethra urothelial carcinoma shares the same urothelial histology as bladder cancer, for which atezolizumab's anti-PD-L1 mechanism has been directly tested in a completed Phase 2 trial (NCT02844816, n=172). The mechanistic extrapolation is well-grounded and the anatomical distinction is not a biological barrier. However, Denmark has no existing marketing authorisation for atezolizumab, and the drug has no registered patients in the Danish market, requiring a named-patient or compassionate use pathway for any clinical application.

**To proceed, the following is needed:**

- **Confirm EMA/Lægemiddelstyrelsen authorisation status**: Verify whether a valid centralised marketing authorisation exists or whether a named-patient or hospital exemption programme (§ 29 in Danish medicines law) is applicable
- **Obtain full SmPC safety data**: The current Evidence Pack has blocking data gaps for key warnings and contraindications (DG001); the SmPC must be reviewed before any patient-level safety assessment
- **Retrieve mechanism of action data from DrugBank** (DG002): Formal MOA documentation needed for the regulatory submission
- **Obtain results from NCT02844816**: Full efficacy and safety data from this completed Phase 2 trial should be retrieved and reviewed
- **PD-L1/TMB biomarker strategy**: Define patient selection criteria (PD-L1 IHC status, TMB threshold) aligned with atezolizumab's known biomarker framework
- **Multidisciplinary team consultation**: Given the rarity of prostatic urethral urothelial carcinoma and Denmark's non-marketed status, a formal oncology MDT review and ethical committee consultation are strongly recommended before clinical application

---

> ⚠️ **Disclaimer**: This report is intended for research purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before application. All content should be evaluated by qualified healthcare professionals in the context of current clinical guidelines.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

