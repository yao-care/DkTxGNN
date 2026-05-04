---
layout: default
title: Amprenavir
parent: 僅模型預測 (L5)
nav_order: 36
evidence_level: L5
indication_count: 10
---

# Amprenavir
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

# Amprenavir: From HIV Infection to Simian Immunodeficiency Virus Infection

## One-Sentence Summary

Amprenavir is an HIV-1 protease inhibitor historically used in the treatment of HIV infection in adults and children, though it has since been largely superseded by its prodrug fosamprenavir and withdrawn from most markets.
The TxGNN model predicts it may be effective for **Simian Immunodeficiency Virus (SIV) Infection**, with **0 clinical trials** and **2 publications** currently supporting this direction — both from 2004, examining general antiretroviral susceptibility patterns across HIV-related lentiviruses.
The clinical relevance of this prediction to human patients in Denmark is very limited given both the nature of the target indication and the drug's current market status.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | HIV infection (antiretroviral therapy) |
| Predicted New Indication | Simian Immunodeficiency Virus Infection |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L4 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known pharmacological information, amprenavir belongs to the HIV-1 protease inhibitor class. It works by competitively binding to the active site of the HIV aspartyl protease enzyme, blocking the cleavage of viral Gag-Pol polyproteins into functional structural proteins and enzymes. This prevents the maturation of newly budded virions, rendering them non-infectious.

Simian Immunodeficiency Virus (SIV) is a lentivirus closely related to both HIV-1 and HIV-2, sharing significant genomic and structural homology — particularly in the protease enzyme active site. In vitro susceptibility studies have demonstrated that several HIV protease inhibitors retain measurable antiviral activity against SIV strains owing to this structural conservation. The TxGNN model's high confidence score reflects this well-established mechanistic overlap captured in the underlying knowledge graph.

However, this prediction must be understood in context: SIV infection is primarily a disease of non-human primates (macaques, chimpanzees, sooty mangabeys) and does not constitute a conventional human clinical indication. This prediction is likely capturing cross-species pharmacological overlap rather than identifying a novel therapeutic opportunity for Danish patients. Without evidence of a specific human population at risk — such as laboratory workers requiring post-exposure prophylaxis after occupational SIV exposure — the practical clinical value of this prediction is very limited.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for amprenavir in simian immunodeficiency virus infection.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [15040537](https://pubmed.ncbi.nlm.nih.gov/15040537/) | 2004 | In vitro study | Antiviral Therapy | Evaluated antiviral activity of 16 approved antiretroviral drugs against HIV-2, SIV (mac251, B670), and SHIV strains; found amprenavir among drugs with measurable activity against SIV, with implications for post-exposure prophylaxis guidance in occupational settings |
| [15040531](https://pubmed.ncbi.nlm.nih.gov/15040531/) | 2004 | Review | Antiviral Therapy | Reviews antiretroviral drug resistance and susceptibility profiles across non-subtype B HIV-1, HIV-2, and SIV; discusses treatment implications for healthcare and laboratory workers with occupational exposure risk |

---

## Denmark Market Information

Amprenavir is not currently marketed in Denmark. There are no active national marketing authorisations on record with Lægemiddelstyrelsen (the Danish Medicines Agency), and no centralised EMA authorisation is currently valid.

> **Regulatory Note:** Amprenavir (brand name Agenerase) received a centralised EMA marketing authorisation in 2000 but was subsequently withdrawn from the European market by the marketing authorisation holder. The preferred clinical alternative is fosamprenavir (Telzir), the phosphate prodrug of amprenavir, which remains authorised in some markets. Any clinical use of amprenavir in Denmark would require a special compassionate use or named-patient programme arrangement.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information. A notable safety signal identified in the literature is a possible association between amprenavir use and increased bleeding tendency in HIV-infected patients with haemophilia (PMID: [11483161](https://pubmed.ncbi.nlm.nih.gov/11483161/)), which should be considered if clinical use is contemplated.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Simian Immunodeficiency Virus infection is not a human clinical indication applicable to Danish patients under standard care, and the available evidence base consists solely of two in vitro susceptibility studies published in 2004. Additionally, amprenavir holds no active marketing authorisation in Denmark and has been withdrawn from European markets, significantly limiting any pathway to clinical use.

**To proceed, the following is needed:**

- **Clinical context clarification:** Identify whether there is a specific human population in Denmark (e.g., primate laboratory workers requiring post-exposure prophylaxis) for whom this prediction has direct clinical relevance
- **MOA data:** Retrieve complete mechanism of action and pharmacological profile from DrugBank to formally document cross-species protease inhibitor activity
- **Full safety and interaction profile:** Download and parse the original SmPC (or equivalent EMA/FDA safety documentation) to complete the safety assessment, including warnings, contraindications, and drug-drug interactions
- **Prodrug consideration:** Assess whether fosamprenavir (Telzir) — the marketed prodrug and functional equivalent — should be evaluated as the primary candidate instead of amprenavir itself
- **Regulatory pathway:** If clinical use is contemplated, a named-patient or compassionate use application to Lægemiddelstyrelsen would be required given the absence of any Danish marketing authorisation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

