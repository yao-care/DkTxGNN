---
layout: default
title: Ribavirin
parent: 僅模型預測 (L5)
nav_order: 374
evidence_level: L5
indication_count: 10
---

# Ribavirin
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

# Ribavirin: From RNA Viral Infections (Hepatitis C, RSV) to Chronic Hepatitis B Virus Infection

## One-Sentence Summary

Ribavirin is a guanosine-analogue antiviral historically used against RNA viruses such as hepatitis C virus (HCV) and respiratory syncytial virus (RSV), typically as part of combination regimens (e.g., peginterferon + ribavirin). The TxGNN model predicts it may also be effective for **Chronic Hepatitis B Virus Infection**, but the **50 cross-referenced clinical trials** and **20 publications** identified so far are almost entirely about ribavirin's established use against HCV — direct evidence of anti-HBV activity is minimal, and the drug currently has **no marketing authorisation in Denmark**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no Denmark marketing authorisation on file (drug is not marketed); known historical use is against HCV/RSV (see mechanism section) |
| Predicted New Indication | Chronic Hepatitis B Virus Infection |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L4 |
| Denmark Market Status | Not Marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for ribavirin is not available in this evidence pack (DrugBank query pending / data gap). Based on known pharmacology, ribavirin is a guanosine analogue that primarily inhibits inosine monophosphate dehydrogenase (IMPDH) and RNA-dependent RNA polymerase, and induces lethal mutagenesis in RNA viruses — mechanisms established for HCV and RSV.

Hepatitis B virus (HBV), however, is a DNA virus that replicates via reverse transcription and is not a traditional ribavirin target. Reviewing the evidence collected, the overwhelming majority of the identified literature and trials involve **HBV/HCV co-infected patients**, where ribavirin is used to treat the HCV component of the infection rather than HBV itself. Only one publication (PMID 10832679, "Is ribavirin treatment really effective for chronic hepatitis B?") directly addresses ribavirin's efficacy against HBV, and its abstract is not available in this pack.

In short, the mechanistic link between ribavirin and chronic HBV infection is **weak and indirect**. The high TxGNN score most likely reflects network-level association (shared "hepatitis" disease-class connections and frequent co-occurrence with HBV in the co-infection literature) rather than a validated direct antiviral mechanism against HBV.

---

## Clinical Trial Evidence

Note: TxGNN-linked trials for this indication were reviewed for relevance. The great majority are graded **C (low relevance)** — they investigate ribavirin/peginterferon regimens in chronic **hepatitis C**, not hepatitis B, and appear to have been associated with this indication due to keyword overlap ("hepatitis"). No trial in the evidence pack directly tests ribavirin in HBV-infected patients.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00215865](https://clinicaltrials.gov/study/NCT00215865) | Phase 3 | Completed | 600 | PEGIntron + ribavirin dosing comparison in chronic **hepatitis C** (relapse after prior IFN therapy); not an HBV trial. |
| [NCT01447420](https://clinicaltrials.gov/study/NCT01447420) | Phase 4 | Completed | 129 | Pegasys + Copegus (ribavirin) efficacy vs. IL28B expression in genotype 1 **HCV**; not HBV-related. |
| [NCT01405027](https://clinicaltrials.gov/study/NCT01405027) | Phase 4 | Completed | 197 | Boceprevir + peginterferon + ribavirin compliance study in **hepatitis C** patients; not HBV-related. |
| [NCT01655966](https://clinicaltrials.gov/study/NCT01655966) | Phase 3 | Unknown | 80 | Vitamin D add-on to peginterferon/ribavirin in **hepatitis C** genotype 4; not HBV-related. |
| [NCT01830127](https://clinicaltrials.gov/study/NCT01830127) | Phase 2 | Completed | 35 | BI 207127 + faldaprevir + ribavirin pharmacokinetics in genotype 1b **hepatitis C**; not HBV-related. |
| [NCT02493855](https://clinicaltrials.gov/study/NCT02493855) | Phase 2 | Completed | 46 | Ombitasvir/ABT-450/ritonavir + dasabuvir with ribavirin, viral kinetics in genotype 1a **HCV**; not HBV-related. |
| [NCT01949168](https://clinicaltrials.gov/study/NCT01949168) | Phase 2 | Unknown | 30 | Boceprevir-based therapy for genotype 6 **hepatitis C**; not HBV-related. |
| [NCT03261349](https://clinicaltrials.gov/study/NCT03261349) | Phase 2 | Unknown | 21 | Ledipasvir/sofosbuvir for **HCV**-associated B-cell lymphoma; not HBV-related. |
| [NCT01220947](https://clinicaltrials.gov/study/NCT01220947) | Phase 2 | Completed | 421 | Danoprevir + ritonavir + Pegasys/Copegus in treatment-naive **hepatitis C**; not HBV-related. |
| [NCT01598090](https://clinicaltrials.gov/study/NCT01598090) | Phase 3 | Completed | 881 | Peginterferon Lambda-1a + ribavirin + telaprevir vs. alfa-2a regimen in genotype-1 **hepatitis C**; not HBV-related. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10832679](https://pubmed.ncbi.nlm.nih.gov/10832679/) | 2000 | Unclassified | Journal of Gastroenterology | Title directly asks "Is ribavirin treatment really effective for chronic hepatitis B?" — the only publication addressing ribavirin's direct anti-HBV efficacy; abstract not available in this data pack. |
| [32664198](https://pubmed.ncbi.nlm.nih.gov/32664198/) | 2020 | Review | Viruses | Reviews HCV/HBV co-infection management; peginterferon + ribavirin recommended for the HCV component in co-infected, HCV-RNA-positive patients. |
| [27433078](https://pubmed.ncbi.nlm.nih.gov/27433078/) | 2016 | Review | World Journal of Gastroenterology | Notes HBV persists even after direct-acting antiviral therapy and requires life-long treatment, unlike HCV which can be cured. |
| [24659886](https://pubmed.ncbi.nlm.nih.gov/24659886/) | 2014 | Review | World Journal of Gastroenterology | Updates on treatment outcomes in dual chronic HCV/HBV infection; higher risk of liver disease progression in dual infection. |
| [19669238](https://pubmed.ncbi.nlm.nih.gov/19669238/) | 2009 | Review | Hepatology International | Discusses viral interaction dynamics in dual HBV/HCV infection under treated vs. untreated settings. |
| [17009938](https://pubmed.ncbi.nlm.nih.gov/17009938/) | 2006 | Review | Expert Review of Anti-infective Therapy | Reviews treatment options for chronic hepatitis B and C in children, including standardized regimens. |
| [25232239](https://pubmed.ncbi.nlm.nih.gov/25232239/) | 2014 | Cohort | World Journal of Gastroenterology | IL28B polymorphism associated with SVR in HCV treated with peginterferon/ribavirin; relationship with HBV outcomes less clear (no consensus). |
| [26284971](https://pubmed.ncbi.nlm.nih.gov/26284971/) | 2015 | Cohort | Current Opinion in Virology | IL28B genotype linked to treatment-induced and spontaneous viral clearance in HCV; relevance to HBV outcome discussed. |
| [21538279](https://pubmed.ncbi.nlm.nih.gov/21538279/) | 2011 | Review | Seminars in Liver Disease | Reviews host genetic determinants of chronic HBV and HCV disease outcome. |
| [18804888](https://pubmed.ncbi.nlm.nih.gov/18804888/) | 2008 | Review | Journal of Hepatology | Discusses ongoing challenges in treating HBV/HCV co-infection. |

---

## Denmark Market Information

Ribavirin currently has no marketing authorisation on file in Denmark (market status: Not Marketed; 0 authorisations recorded). No product, dosage form, or approved-indication data are available for this evidence pack.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information. Key warnings, contraindications, and drug interaction data are not currently available in this evidence pack (a blocking data gap — SmPC warnings/contraindications retrieval — is flagged for follow-up before any S1 safety screening can proceed).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The mechanistic link is weak: ribavirin's established antiviral mechanism targets RNA viruses, while HBV is a DNA virus replicating via reverse transcription.
- Nearly all identified clinical trials concern ribavirin's established use in hepatitis C (graded low-relevance to HBV); only one older publication directly questions ribavirin's efficacy against HBV, with no abstract available.
- A blocking data gap (SmPC warnings/contraindications) prevents even an initial (S1) safety evaluation.

**To proceed, the following is needed:**
- TFDA/Danish SmPC warnings and contraindications (blocking gap, DG001)
- Confirmed mechanism of action data via DrugBank (DG002)
- Direct preclinical or clinical evidence of anti-HBV activity (the single directly relevant publication needs full-text review)
- Re-triage of the "pending" relevance-graded trials and literature to confirm none provide direct HBV evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

