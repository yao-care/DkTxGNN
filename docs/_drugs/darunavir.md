---
layout: default
title: Darunavir
parent: 僅模型預測 (L5)
nav_order: 131
evidence_level: L5
indication_count: 8
---

# Darunavir
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

# Darunavir: From HIV-1 Infection to Simian Immunodeficiency Virus Infection

## One-Sentence Summary

Darunavir is a second-generation HIV-1 protease inhibitor, approved as part of combination antiretroviral therapy (cART) for HIV-1-infected adults and children. The TxGNN model predicts it may be effective for **Simian Immunodeficiency Virus (SIV) Infection**, with **0 registered clinical trials** and **4 non-human primate (NHP) publications** currently supporting this direction. It should be noted, however, that this prediction reflects a mechanistic extension into an established preclinical animal model rather than a genuinely novel clinical indication.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | HIV-1 infection (combination antiretroviral therapy) |
| Predicted New Indication | Simian Immunodeficiency Virus (SIV) Infection |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L3 |
| Denmark Market Status | Not found in current data extract — EMA centralised authorisation should be independently verified |
| Number of Marketing Authorisations | 0 (per current data extract) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on well-established pharmacological knowledge, Darunavir is a second-generation HIV-1 protease inhibitor that binds non-covalently and with high affinity to the active site of HIV-1 protease. It prevents cleavage of the viral Gag-Pol polyprotein precursor, thereby blocking the maturation of infectious virions. Darunavir is routinely co-administered with the pharmacokinetic boosters ritonavir or cobicistat to achieve therapeutic plasma concentrations.

The mechanistic basis for the TxGNN prediction is structurally sound: SIV protease shares approximately 50–60% amino acid sequence similarity with HIV-1 protease, and the key catalytic and binding-site residues are sufficiently conserved for Darunavir's binding geometry to transfer across species. For this reason, Darunavir is routinely incorporated into suppressive cART regimens used in SIVmac239- and SIVmac251-infected rhesus macaques — the internationally accepted preclinical model for HIV/AIDS research and viral reservoir studies.

However, this prediction requires important contextualisation. SIV infection in non-human primates is not an independent therapeutic target; it is the standard translational bridge used to evaluate HIV pharmacology before human trials. All four supporting publications use Darunavir as a cART backbone to achieve stable virological suppression in macaques, enabling downstream investigation of viral reservoirs and eradication strategies. This constitutes a direct mechanistic extension of Darunavir's known activity, not a new clinical application. The true clinical translation endpoint is human HIV-1 infection — for which Darunavir already holds regulatory approval.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [26150024](https://pubmed.ncbi.nlm.nih.gov/26150024/) | 2016 | Animal Model (NHP) | AIDS Research and Human Retroviruses | Evaluated two novel coformulated injectable cART regimens (including darunavir) in SIVmac239-infected rhesus macaques; demonstrated effective viral suppression to clinically relevant levels suitable for viral reservoir studies |
| [25033210](https://pubmed.ncbi.nlm.nih.gov/25033210/) | 2014 | Animal Model (NHP) + Intervention | PLoS ONE | Intensive cART combined with the HDAC inhibitor SAHA in SIV-infected Chinese-origin rhesus macaques; characterised viral reservoir dynamics in an NHP model designed to mimic HIV-infected humans on cART |
| [22737073](https://pubmed.ncbi.nlm.nih.gov/22737073/) | 2012 | Animal Model (NHP) | PLoS Pathogens | Highly intensified ART (including darunavir) achieved stable long-term virological suppression across a wide baseline viraemia range (10³–10⁷ RNA copies/mL) in SIVmac251-infected macaques and significantly restricted the size of the viral reservoir |
| [21505294](https://pubmed.ncbi.nlm.nih.gov/21505294/) | 2011 | Animal Model (NHP) | AIDS (London) | Gold compound auranofin combined with darunavir-containing cART reduced the lentiviral reservoir in a monkey AIDS model; partial viral load containment was observed following ART suspension |

---

## Denmark Market Information

The current data extract contains no marketing authorisation records for darunavir held by Lægemiddelstyrelsen (the Danish Medicines Agency). This is likely a data gap: darunavir (Prezista®, Janssen) received centralised EMA marketing authorisation in 2007, which is valid across all EU/EEA member states including Denmark. Healthcare professionals should verify current availability, authorised indications, and approved product information via the EMA product database or the Danish medicines information portal (pro.medicin.dk / medicinpriser.dk).

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|-------------------------------|-------------|-------------|---------------------|
| Not found in current extract | — | — | Please verify via EMA EPAR or Lægemiddelstyrelsen |

---

## Safety Considerations

No safety warnings, contraindications, or drug interaction data are available in the current Evidence Pack for darunavir.

Please refer to the approved Summary of Product Characteristics (SmPC) for complete safety information. As a boosted protease inhibitor, darunavir co-administered with ritonavir or cobicistat is a potent CYP3A4 inhibitor with an extensive drug-drug interaction profile. Clinicians should consult the current SmPC or a validated drug interaction tool (e.g., the University of Liverpool HIV Drug Interaction Checker) prior to prescribing alongside other medications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction for SIV infection does not represent a novel repurposing opportunity in the conventional sense: SIV infection in non-human primates is the established preclinical surrogate model for human HIV-1, and all supporting literature uses darunavir as a cART component within this modelling context, not as a treatment for SIV as an independent disease. The underlying pharmacological activity is already well-characterised for HIV-1, and this prediction carries no additional translational value beyond the drug's approved use.

**To proceed, the following is needed:**
- **Reframe the repurposing question**: Consider whether the evidence pipeline should be redirected to assess darunavir for genuinely novel indications (e.g., non-HIV indications such as SARS-CoV-2 protease inhibition, which has been explored in the literature) rather than SIV infection
- **Resolve MOA data gap**: Obtain full mechanism of action documentation via DrugBank API (DrugBank ID: DB01264)
- **Verify Danish market status**: Confirm current EMA centralised authorisation details, authorised indications, and availability of approved product information through the EMA EPAR database and Lægemiddelstyrelsen
- **Complete safety profiling**: Retrieve full SmPC warnings, contraindications, and drug-drug interaction data from the EMA product page or Lægemiddelstyrelsen before any clinical evaluation proceeds

---

> **Disclaimer:** This report is intended for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before any therapeutic application. All information should be verified against current approved product labelling.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

