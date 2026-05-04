---
layout: default
title: Entecavir
parent: 僅模型預測 (L5)
nav_order: 167
evidence_level: L5
indication_count: 10
---

# Entecavir
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

# Entecavir: From Chronic Hepatitis B to Chronic Hepatitis C Virus Infection

## One-Sentence Summary

Entecavir (ETV) is an oral nucleoside analogue established internationally as a first-line treatment for **chronic hepatitis B virus (HBV) infection**, where it potently suppresses viral replication by inhibiting HBV DNA polymerase.
The TxGNN model predicts it may be effective for **chronic hepatitis C virus (HCV) infection**, with a prediction score of **99.98%**; however, the available evidence — drawn from over 10 clinical trials and 20 publications — reflects its adjunctive role in HBV/HCV co-infection management rather than direct anti-HCV activity.
Entecavir is not currently marketed in Denmark.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Chronic hepatitis B virus (HBV) infection (based on international approvals and full evidence base) |
| Predicted New Indication | Chronic hepatitis C virus infection |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L3 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Entecavir is a guanosine nucleoside analogue. After intracellular phosphorylation to its active triphosphate form (ETV-TP), it competitively inhibits HBV DNA polymerase at three steps: priming of the HBV pregenomic RNA, reverse transcription (negative-strand DNA synthesis), and positive-strand HBV DNA synthesis. Its Ki is approximately 0.003 μM, conferring highly selective anti-HBV activity (IC50 < 0.01 μM) with low toxicity toward host DNA polymerases α, β, and γ.

Critically, Entecavir does **not** have meaningful inhibitory activity against the HCV NS5B RNA-dependent RNA polymerase (RdRp), which is the target of direct-acting antiviral agents (DAAs) used to treat hepatitis C. The TxGNN model's high prediction score for HCV most likely reflects the strong knowledge graph co-occurrence between Entecavir and HCV in the biomedical literature — principally because HBV and HCV share transmission routes and frequently co-infect the same patients. In this co-infection context, Entecavir is used to control HBV replication and **prevent HBV reactivation** that commonly occurs during DAA therapy for HCV, rather than to treat HCV directly.

The clinical relevance of Entecavir in the HCV setting is therefore adjunctive: when HBV/HCV co-infected patients receive DAA therapy, immunological changes can trigger HBV reactivation, and prophylactic or pre-emptive use of nucleoside analogues such as Entecavir is already established practice. This explains the observational evidence base but does not support repurposing Entecavir as a primary HCV treatment.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT02555943](https://clinicaltrials.gov/study/NCT02555943) | Phase 2/3 | Completed | 23 | Prospective study of DAA therapy in HCV/HBV co-infected patients; investigated incidence, morbidity, mortality and predisposing factors for HBV reactivation during anti-HCV treatment — most directly relevant trial for this indication |
| [NCT04405011](https://clinicaltrials.gov/study/NCT04405011) | N/A | Unknown | 60 | Three-arm randomised study evaluating prophylactic nucleos(t)ide analogue (Entecavir eligible) in HBV/HCV co-infected patients on DAA therapy; compared 12-week vs. 24-week prophylaxis vs. no prophylaxis against clinical HBV reactivation |
| [NCT04157257](https://clinicaltrials.gov/study/NCT04157257) | Phase 2 | Unknown | 60 | Open-label, multi-centre study of QL-007 (investigational HCV DAA candidate) combined with Entecavir 0.5 mg QD or Tenofovir; evaluates safety and efficacy of combination strategy directly involving Entecavir |
| [NCT06566248](https://clinicaltrials.gov/study/NCT06566248) | Phase 2 | Recruiting | 90 | Randomised, double-blind, placebo-controlled Phase IIa trial evaluating TQA3810 tablets combined with or without nucleoside analogues in chronic hepatitis B; Entecavir serves as backbone comparator |
| [NCT03272009](https://clinicaltrials.gov/study/NCT03272009) | Phase 1 | Completed | 73 | Randomised, double-blind, placebo-controlled study of EYP001a (FXR agonist) in chronically HBV-infected subjects; Entecavir used as background therapy; limited direct HCV relevance |
| [NCT01925820](https://clinicaltrials.gov/study/NCT01925820) | Phase 4 | Unknown | 540 | Pegasys plus Entecavir vs. Entecavir monotherapy vs. Pegasys alone in HBeAg-negative chronic HBV; experience base for combination antiviral strategies discussed in context of HCV treatment parallels |
| [NCT01037166](https://clinicaltrials.gov/study/NCT01037166) | Phase 2 | Completed | 84 | Entecavir antiviral activity in Japanese HBV patients with incomplete response to lamivudine; safety and pharmacokinetic data supporting chronic hepatitis management |
| [NCT01022801](https://clinicaltrials.gov/study/NCT01022801) | Phase 2 | Completed | 120 | Entecavir vs. lamivudine dose–response study in Japanese chronic HBV patients; supports characterisation of Entecavir's antiviral potency |
| [NCT03662568](https://clinicaltrials.gov/study/NCT03662568) | Phase 1 | Completed | 56 | Open-label, single-centre drug–drug interaction study of Morphothiadine Mesilate/Ritonavir (an investigational HCV agent) with Entecavir or Tenofovir in healthy subjects |
| [NCT01018381](https://clinicaltrials.gov/study/NCT01018381) | N/A | Completed | 130 | Randomised study of Arabinoxylan Rice Bran (MGN-3/Biobran) for HCC and hepatitis B and C infection; Entecavir used as background HBV therapy in HCV-co-infected participants |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [36146665](https://pubmed.ncbi.nlm.nih.gov/36146665/) | 2022 | Cohort Study | Viruses | HCV reactivation observed in anti-HCV antibody-positive CHB patients following nucleoside analogue therapy; cohort of 66 patients documented HCV RNA dynamics during Entecavir treatment — key evidence for viral interplay |
| [24773464](https://pubmed.ncbi.nlm.nih.gov/24773464/) | 2014 | Review | Expert Opinion on Pharmacotherapy | HBV/HCV co-infection patients face high risk of cirrhosis and HCC; reviews optimal treatment sequencing, including nucleoside analogues for HBV management during anti-HCV treatment |
| [24868325](https://pubmed.ncbi.nlm.nih.gov/24868325/) | 2014 | Review | World Journal of Hepatology | Management of hepatitis B and C before and after liver and kidney transplantation; Entecavir highlighted as preferred HBV agent due to high genetic barrier to resistance in transplant settings |
| [25027705](https://pubmed.ncbi.nlm.nih.gov/25027705/) | 2014 | Review | Minerva Gastroenterologica e Dietologica | Antiviral medications for HBV and HCV infection and their effects on renal function; reviews Entecavir alongside HCV DAA therapies; notes divergent mechanisms and renal profiles |
| [35327336](https://pubmed.ncbi.nlm.nih.gov/35327336/) | 2022 | Review | Biomedicines | Comprehensive review of chronic viral hepatitis therapy (HBV, HCV, HDV); clearly distinguishes mechanistic targets and treatment strategies between the three virus types |
| [22959099](https://pubmed.ncbi.nlm.nih.gov/22959099/) | 2013 | Review | Clinics and Research in Hepatology and Gastroenterology | HBV/HCV co-infection causes more severe liver injury and higher HCC incidence than mono-infection; reviews treatment approaches including nucleoside analogues for HBV control |
| [21497740](https://pubmed.ncbi.nlm.nih.gov/21497740/) | 2011 | Review | Best Practice & Research. Clinical Gastroenterology | Antiviral treatments and fibrosis progression in chronic viral hepatitis; histological improvement with nucleoside/nucleotide analogues in HBV well-established; HCV fibrosis discussed separately |
| [32173307](https://pubmed.ncbi.nlm.nih.gov/32173307/) | 2020 | Review | Clinics and Research in Hepatology and Gastroenterology | Present and future management of HBV and HCV in children; Entecavir recommended for paediatric HBV; HCV management with DAAs reviewed in parallel |
| [28487602](https://pubmed.ncbi.nlm.nih.gov/28487602/) | 2017 | Review | World Journal of Gastroenterology | HBV infection and alcohol consumption; in post-DAA era, HBV and alcoholic liver disease expected to become leading causes of HCC as HCV is eradicated; highlights ongoing importance of HBV control |
| [16937041](https://pubmed.ncbi.nlm.nih.gov/16937041/) | 2006 | Review | Wiener Medizinische Wochenschrift | Contemporary treatment and future prospects for chronic hepatitis B and C; documents Entecavir's superior antiviral potency vs. earlier HBV agents, with HCV treatment reviewed as a separate therapeutic category |

---

## Denmark Market Information

Entecavir is **not currently authorised for marketing in Denmark**. No national (Lægemiddelstyrelsen) or centralised (EMA) marketing authorisations were identified for Denmark.

For reference, Entecavir (brand name Baraclude®) holds international regulatory approvals elsewhere — including from the FDA (USA, 2005) and EMA (EU) — for chronic HBV infection in adults and paediatric patients aged ≥2 years with active viral replication and compensated or decompensated liver disease. Any clinical use in Denmark would require an import authorisation, compassionate use application, or equivalent special access pathway.

---

## Safety Considerations

Formal Danish/EU SmPC safety data (warnings, contraindications, and drug–drug interactions) are not available in this evidence pack.

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

Based on the known pharmacological class (nucleoside/nucleotide analogue), clinicians should be aware that the international SmPC for Entecavir includes the following class-relevant concerns:

- **Lactic acidosis and severe hepatomegaly with steatosis**: Rare but potentially fatal class effect of nucleoside analogues; risk increased in patients with hepatic decompensation, obesity, or prolonged nucleoside exposure (a Phase 4 study, NCT01354652, was specifically initiated to quantify lactic acidosis risk in Entecavir-treated patients with severe cirrhosis or hepatic failure)
- **Hepatitis exacerbation on treatment discontinuation**: Abrupt cessation can trigger severe HBV flares; periodic monitoring of hepatic function is required
- **Renal impairment**: Dose adjustment required when creatinine clearance is <50 mL/min

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Entecavir has no clinically meaningful direct anti-HCV activity and is not a viable candidate for HCV monotherapy or primary HCV treatment. The TxGNN prediction score of 99.98% most likely reflects co-occurrence in the biomedical knowledge graph driven by HBV/HCV co-infection literature, rather than a genuine pharmacological repurposing opportunity. All available clinical evidence is observational or adjunctive in nature (Evidence Level L3), and no trials demonstrate Entecavir efficacy against HCV replication directly.

**To proceed, the following is needed:**

- **Clarification of research question**: If the goal is evaluating Entecavir's role in **HBV reactivation prophylaxis during DAA therapy** in HBV/HCV co-infected patients, this is already an established clinical indication not requiring new regulatory approval; a clinical protocol rather than a repurposing programme would be appropriate
- **Full SmPC/safety data**: Download and parse the EU Baraclude® SmPC from the EMA product database for complete contraindications, warnings, and DDI information (resolves data gap DG001)
- **Mechanism of action data**: Retrieve the complete DrugBank record (DB00442) for formal MOA documentation, including pharmacokinetics and drug class categorisation (resolves data gap DG002)
- **Danish regulatory pathway**: If clinical use is planned in Denmark, consult Lægemiddelstyrelsen regarding import authorisation or compassionate use eligibility
- **HBV/HCV co-infection management protocol**: If the clinical application is HBV reactivation prevention during DAA therapy, define monitoring parameters (HBV DNA thresholds, prophylaxis duration, treatment end-points) aligned with current EASL and European guidelines

> ⚠️ **Disclaimer**: This report is intended for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before application in practice.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

