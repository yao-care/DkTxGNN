---
layout: default
title: Doravirine
parent: 僅模型預測 (L5)
nav_order: 148
evidence_level: L5
indication_count: 6
---

# Doravirine
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

# Doravirine: From HIV-1 Infection to Simian Immunodeficiency Virus Infection

## One-Sentence Summary

Doravirine is a third-generation non-nucleoside reverse transcriptase inhibitor (NNRTI) approved internationally for the treatment of HIV-1 infection in adults, though it currently holds no marketing authorisation in Denmark.
The TxGNN model predicts it may have activity against **Simian Immunodeficiency Virus (SIV) infection**, with a prediction score of **99.93%**.
Supporting evidence at this stage is limited to **1 background publication** and **no registered clinical trials**, placing this prediction in the early mechanistic hypothesis category only.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | HIV-1 infection in adults (not authorised in Denmark; no Danish regulatory data available) |
| Predicted New Indication | Simian Immunodeficiency Virus (SIV) Infection |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L4 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Doravirine is a diarylpyrimidine NNRTI that exerts its antiviral effect by binding to the non-nucleoside binding pocket (NNBP) of HIV-1 reverse transcriptase (RT), thereby blocking the RNA-dependent DNA polymerisation step essential for viral replication. A key advantage of doravirine over earlier NNRTIs (e.g., efavirenz, nevirapine) is its flexible molecular scaffold, which retains activity against common resistance mutations such as K103N and Y181C. It is authorised by the EMA as Pifeltro (doravirine monotherapy) and Delstrigo (doravirine/lamivudine/tenofovir disoproxil fumarate fixed-dose combination).

Simian Immunodeficiency Virus (SIV) is a lentivirus phylogenetically related to HIV, and it likewise depends on a reverse transcriptase enzyme for viral replication. This shared mechanistic dependency provides a theoretical basis for the TxGNN prediction — the knowledge graph connects HIV-1, lentiviruses, and reverse transcriptase inhibitors in structural proximity to SIV. However, the NNBP of SIV RT differs from that of HIV-1 RT at critical amino acid positions (e.g., the V181 locus), and established NNRTIs designed for HIV-1 have been shown to exhibit substantially reduced or absent binding affinity for SIV RT. Although doravirine's flexible diarylpyrimidine structure provides some theoretical tolerance for variant binding pockets, no direct experimental data exist to confirm this for SIV.

An important translational caveat is that the vast majority of non-human primate antiviral studies use SHIV (a chimeric SIV/HIV construct engineered to carry the HIV-1 envelope gene), rather than wild-type SIV. Results from SHIV models do not map directly onto pure SIV biology, further limiting the inferential value of graph-based predictions. This prediction is best understood as a knowledge graph neighbourhood association — mechanistically plausible at a high level of abstraction, but lacking the structural or experimental evidence needed to progress.

---

## Clinical Trial Evidence

No clinical trials investigating doravirine for simian immunodeficiency virus infection are currently registered on ClinicalTrials.gov or the WHO ICTRP.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [31658118](https://pubmed.ncbi.nlm.nih.gov/31658118/) | 2020 | Review / Drug Profile | *Current Opinion in HIV and AIDS* | Reviews islatravir (ISL), a novel RT translocation inhibitor, for HIV-1 treatment and prevention — retrieved as contextual background on RT inhibitors and lentiviral biology; does not assess doravirine or SIV directly |

> **Important note:** The single retrieved publication concerns **islatravir**, a mechanistically distinct antiretroviral from a different drug class (nucleoside RT translocation inhibitor, NRTTI). No literature directly assessing doravirine activity against SIV was identified in this evidence search.

---

## Denmark Market Information

Doravirine currently holds **no marketing authorisation** in Denmark and is not registered in the Danish Medicines Registry (Lægemiddelstyrelsen).

For reference, doravirine is centrally authorised in the EU/EEA by the EMA:

| Authorisation | Product Name | Dosage Form | Authorised Indication |
|--------------|-------------|-------------|----------------------|
| EMA (centralised) | Pifeltro | Film-coated tablet (100 mg) | Treatment of HIV-1 infection in adults with no past or present viral resistance to the NNRTI class |
| EMA (centralised) | Delstrigo | Film-coated tablet (doravirine 100 mg / lamivudine 300 mg / tenofovir DF 245 mg) | Treatment of HIV-1 infection in adults with no past or present viral resistance to the NNRTI class |

Danish patients may potentially access doravirine through an individual import authorisation (§29 import) if clinically indicated.

---

## Safety Considerations

Comprehensive safety data from Danish regulatory sources are unavailable, as doravirine is not marketed in Denmark.

Please refer to the approved Summary of Product Characteristics (SmPC) for **Pifeltro** and **Delstrigo** for full safety information, available via the European Medicines Agency (EMA) website at [www.ema.europa.eu](https://www.ema.europa.eu).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN prediction score (99.93%), the prediction that doravirine is active against SIV infection reflects a knowledge graph structural association between lentiviruses and NNRTI-class drugs, rather than empirical antiviral evidence. Structurally meaningful differences between HIV-1 RT and SIV RT at the NNBP render direct activity highly uncertain, and the single retrieved publication concerns a different drug entirely. There is currently no preclinical, clinical, or veterinary evidence to support progressing this candidate.

**To proceed, the following is needed:**

- **In vitro RT inhibition assays**: Determine doravirine IC₅₀ against recombinant SIV RT, with direct comparison to HIV-1 RT under identical conditions
- **Structural modelling**: Computational docking of doravirine into the SIV RT NNBP to assess binding feasibility at the residue level (particularly V181 and surrounding positions)
- **Clarification of clinical target**: Define whether the indication is human occupational/zoonotic SIV exposure or veterinary / primate research use — these have very different regulatory and ethical pathways
- **MOA documentation**: Retrieve full doravirine mechanism of action, resistance profile, and pharmacokinetic data from DrugBank (currently absent from this evidence pack)
- **Safety review**: Obtain and review the EMA SmPC for Pifeltro/Delstrigo to complete the safety assessment before any further evaluation steps
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

