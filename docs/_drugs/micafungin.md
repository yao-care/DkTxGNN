---
layout: default
title: Micafungin
parent: 僅模型預測 (L5)
nav_order: 288
evidence_level: L5
indication_count: 10
---

# Micafungin
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

# Micafungin: From Invasive Candidiasis to Candida Urinary Tract Infection

## One-Sentence Summary

Micafungin is an echinocandin antifungal agent approved internationally for the treatment of invasive candidiasis, candidemia, and oesophageal candidiasis, as well as prophylaxis in haematopoietic stem cell transplant (HSCT) recipients.
The TxGNN model predicts it may be effective for **Urinary Tract Infection (Candida UTI)**, with a prediction score of **99.03%**.
Currently there are **no registered clinical trials** and **13 publications** supporting this direction, composed primarily of case reports, case series, PK/PD studies, and retrospective cohort studies.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Invasive candidiasis, candidemia, oesophageal candidiasis, prophylaxis of *Candida* infection in HSCT recipients |
| Predicted New Indication | Urinary Tract Infection (*Candida* UTI) |
| TxGNN Prediction Score | 99.03% |
| Evidence Level | L3 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Micafungin belongs to the echinocandin class of antifungals. Its mechanism of action centres on non-competitive inhibition of **β-1,3-D-glucan synthase** (encoded by *FKS1*/*FKS2* genes), a fungal-specific enzyme responsible for synthesising the structural β-glucan scaffold of the fungal cell wall. Because mammalian cells lack this enzyme entirely, the drug has a highly selective antifungal profile. Micafungin is fungicidal against most *Candida* species, including *C. albicans*, *C. glabrata* (*Nakaseomyces glabrata*), *C. krusei* (*Pichia kudriavzevii*), and the emerging multidrug-resistant *C. auris* — pathogens that frequently cause healthcare-associated urinary tract infections.

The mechanistic link to Candida UTI is biologically plausible: the same fungicidal activity that underpins micafungin's approved indications (candidaemia, invasive candidiasis) is directly relevant to *Candida* UTI, which shares the same pathogen. The key pharmacokinetic caveat, however, is that echinocandins including micafungin are excreted in the urine at **less than 1%** of the administered dose in active form — far below concentrations typically considered adequate for treating lower urinary tract infections. Nonetheless, several clinical observations suggest that (1) serum concentrations achievable with standard dosing may still suppress *Candida* in the renal parenchyma and upper urinary tract, and (2) therapeutic drug monitoring of urinary micafungin levels has identified pharmacodynamically relevant concentrations in select patients. Clinical use has been reported specifically in fluconazole-resistant *Candida* species and in patients where first-line agents (fluconazole, amphotericin B, flucytosine) are contraindicated or poorly tolerated.

It is important to note that the TxGNN model's predicted association is limited to **fungal UTI**. Micafungin has no antibacterial activity whatsoever — predictions for bacterial urethritis (gonococcal, Ureaplasma) and predominantly bacterial conditions such as xanthogranulomatous pyelonephritis represent model false positives, as the β-1,3-D-glucan synthase target is entirely absent from bacteria and mycoplasmas.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [27424599](https://pubmed.ncbi.nlm.nih.gov/27424599/) | 2016 | PK/PD Study | Int J Antimicrob Agents | Six cases of *Candida* UTI successfully treated with micafungin; therapeutic drug monitoring showed urinary levels were pharmacodynamically sufficient, particularly in fluconazole-resistant and hepatotoxicity-risk cases |
| [27587066](https://pubmed.ncbi.nlm.nih.gov/27587066/) | 2016 | Retrospective Cohort | Int Urol Nephrol | Evaluated candiduria elimination rates in micafungin-treated hospitalised patients; echinocandins remain active against azole-resistant *Candida* despite low urine concentrations |
| [29109159](https://pubmed.ncbi.nlm.nih.gov/29109159/) | 2018 | Retrospective Cohort (Multi-centre) | Antimicrob Agents Chemother | Multi-institutional study of 305 hospitalised patients characterising candiduria management; highlights antifungal overuse in asymptomatic candiduria and informs appropriate use criteria for agents like micafungin |
| [39781278](https://pubmed.ncbi.nlm.nih.gov/39781278/) | 2025 | Surveillance / Susceptibility Study | Ther Adv Infect Dis | Antifungal susceptibility profiling of *Candida* isolates from UTI and vulvovaginal candidiasis; highlights the role of non-*albicans* species and differential susceptibility patterns relevant to micafungin selection |
| [35146837](https://pubmed.ncbi.nlm.nih.gov/35146837/) | 2022 | Case Series (Paediatric) | Pediatrics International | Critically ill paediatric ICU patients treated with micafungin for nosocomial Candida UTI; reports treatment success rates by *Candida* species in a vulnerable population |
| [31111613](https://pubmed.ncbi.nlm.nih.gov/31111613/) | 2019 | Case Report | Transplant Infect Dis | Successful eradication of chronic symptomatic *Candida krusei* UTI with high-dose micafungin in a liver-kidney transplant recipient where fluconazole and amphotericin B were unsuitable |
| [26937340](https://pubmed.ncbi.nlm.nih.gov/26937340/) | 2016 | Case Series | Med Mycol Case Rep | Five cases using parenteral micafungin for candiduria; all resolved within 30 days of treatment completion after ≥6 days of therapy |
| [38827222](https://pubmed.ncbi.nlm.nih.gov/38827222/) | 2024 | Case Report | Front Pediatrics | Premature neonate with *Candida glabrata* catheter-associated UTI in the NICU successfully treated with micafungin; underscores rising non-*albicans Candida* incidence and use of echinocandins in neonates |
| [33520520](https://pubmed.ncbi.nlm.nih.gov/33520520/) | 2020 | Case Report | Cureus | *Candida auris* UTI in a nursing home patient with multidrug-resistant profile; micafungin assessed among active treatment options for this emerging pathogen |
| [38681664](https://pubmed.ncbi.nlm.nih.gov/38681664/) | 2024 | Case Report | Med Mycol Case Rep | Unilateral renal fungus ball caused by *Candida glabrata* in a diabetic patient; susceptibility-guided selection of micafungin combined with endoscopic extraction led to successful resolution |

---

## Denmark Market Information

Micafungin is not currently registered or marketed in Denmark. No marketing authorisations were identified through the Danish Medicines Agency (Lægemiddelstyrelsen) database.

> **Note for clinicians:** Although micafungin holds EMA centralised marketing authorisation (Mycamine®, EU/1/08/451/001, Astellas Pharma) valid across all EU Member States, the present data query returned zero active authorisations in the Danish national registry. Prescribers should verify current availability directly with the Lægemiddelstyrelsen or via the EMA product database before clinical use.

---

## Safety Considerations

Detailed safety data — including SmPC warnings, contraindications, and drug interaction profiles — were not available in the current evidence pack.

Please refer to the approved **Summary of Product Characteristics (SmPC)** for Mycamine® (micafungin, EMA) for comprehensive safety information, including hepatotoxicity warnings, monitoring requirements, and interaction potential with sirolimus, nifedipine, and itraconazole.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Micafungin's established fungicidal activity against the *Candida* species that most commonly cause nosocomial UTI provides a sound mechanistic basis for this prediction. Observational evidence — including retrospective cohorts, PK/PD studies, and multiple case series — demonstrates clinical use with resolution of candiduria and Candida UTI, particularly in patients with fluconazole-resistant isolates or contraindications to standard first-line agents. However, the absence of any prospective clinical trial data and the well-characterised pharmacokinetic limitation of low urinary excretion mean this remains an off-label indication requiring individualised clinical judgement.

**To proceed, the following is needed:**

- **Mechanism of action detail (SmPC / DrugBank):** Confirm full pharmacology and PK/PD parameters, including renal tissue penetration data, to support dosing decisions for upper vs. lower UTI
- **Formal safety review:** Retrieve the complete SmPC warnings and contraindications; assess hepatotoxicity risk and drug interaction potential in the target patient populations (transplant recipients, ICU patients, neonates)
- **Prospective study design:** Design a Phase 2 pilot study in a defined high-risk population (e.g., fluconazole-resistant Candida UTI, HSCT patients) with pharmacodynamic endpoints (urinary micafungin trough levels, MIC correlation) to generate controlled efficacy data
- **EMA/Lægemiddelstyrelsen authorisation status verification:** Confirm whether Mycamine® is currently accessible for clinical use in Denmark via EMA centralised procedure before initiating any use
- **Mechanistic scope clarification for clinicians:** Clearly communicate that this prediction applies **exclusively to fungal (Candida) UTI** — predictions for gonococcal urethritis, Ureaplasma urethritis, uterine inflammatory disease, and xanthogranulomatous pyelonephritis are assessed as model false positives and are not recommended for further evaluation

---

> ⚠️ **Disclaimer:** This report is intended for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before therapeutic application. All content should be interpreted in conjunction with approved product information and current clinical guidelines.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

