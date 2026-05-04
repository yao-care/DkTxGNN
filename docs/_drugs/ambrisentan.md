---
layout: default
title: Ambrisentan
parent: 僅模型預測 (L5)
nav_order: 32
evidence_level: L5
indication_count: 10
---

# Ambrisentan
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

# Ambrisentan: From Pulmonary Arterial Hypertension to Pulmonary Arteriovenous Malformation

> **Multi-Indication Evaluation** (Candidate ID: TW-DB06403-multi). This evidence pack covers ten predicted indications. The highest TxGNN score belongs to pulmonary arteriovenous malformation (PAVM); however, the most clinically actionable predictions are PAH associated with HIV infection (L1 evidence), connective tissue disease (L2), and congenital heart disease (L2).

---

## One-Sentence Summary

Ambrisentan is an oral selective endothelin receptor type A (ETA) antagonist, approved internationally (EMA/FDA) for pulmonary arterial hypertension (PAH), but not currently registered in Denmark.
The TxGNN model assigns its highest prediction score to **pulmonary arteriovenous malformation** (PAVM, 99.41%); however, the most clinically actionable findings in this evaluation are PAH associated with **HIV infection** (evidence level L1: 1 completed Phase 3 RCT), **connective tissue disease** (L2), and **congenital heart disease** (L2).
Across all evaluated indications, this evidence pack encompasses **10 clinical trials** and **37 publications**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Pulmonary arterial hypertension (WHO Group 1; EMA/FDA approved internationally — no Danish marketing authorisation on record) |
| Top-Ranked Predicted Indication | Pulmonary arteriovenous malformation (PAVM) |
| TxGNN Prediction Score | 99.41% (PAVM); 99.37% (PAH-CHD); 99.30% (PAH-CTD, PAH-HIV) |
| Evidence Level | L4 — PAVM (Hold); L1 — PAH-HIV (Proceed with Guardrails); L2 — PAH-CTD and PAH-CHD (Proceed with Guardrails) |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold (PAVM); Proceed with Guardrails (PAH-HIV, PAH-CTD, PAH-CHD) |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on published information, Ambrisentan is an oral selective ETA receptor antagonist. Its efficacy in pulmonary arterial hypertension has been established through pivotal randomised trials, and mechanistically its ETA-blockade pathway may be applicable to other conditions driven by endothelin-1-mediated pulmonary vascular overactivation.

**Regarding the highest-scored prediction — pulmonary arteriovenous malformation (PAVM):** PAVM is a structural vascular anomaly characterised by direct arteriovenous connections in the lungs that bypass the capillary bed. It is managed primarily by catheter-based embolisation, not pharmacological vasotone modulation, and elevated ET-1 does not play an established pathogenic role in its formation or progression. The only identified publication (PMID 33969094) describes a patient with hereditary haemorrhagic telangiectasia (HHT) who concurrently developed PAH — this reflects coincident co-morbidity rather than evidence for ETA antagonism in PAVM itself. Mechanistic relevance for this prediction is low.

**Regarding the three actionable PAH-associated subtypes:** All share the same core ETA-overexpression pathway targeted by Ambrisentan. In congenital heart disease, sustained high pulmonary blood flow and shear stress trigger endothelial ET-1 overproduction, driving progressive pulmonary vascular remodelling — the same process Ambrisentan attenuates in idiopathic PAH. HIV infection stimulates ET-1 release from endothelial cells via gp120 protein, while HIV Nef protein suppresses nitric oxide synthase, creating the ET-1/NO imbalance that underpins HIV-PAH. In connective tissue diseases — particularly systemic sclerosis — chronic endothelial injury and immune dysregulation sustain ET-1 overexpression, making selective ETA blockade mechanistically well-justified. All three are formal WHO Group 1 PAH subclasses, sharing the same biologic target as Ambrisentan's established indication.

---

## Clinical Trial Evidence

*No clinical trials were identified for pulmonary arteriovenous malformation (PAVM). The following presents the most relevant trials from all other evaluated indications in this evidence pack.*

| Trial Number | Indication | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|------|---------|
| [NCT00709956](https://clinicaltrials.gov/study/NCT00709956) | PAH-HIV | Phase 3 | Completed | 64 | Multicentre, double-blind, randomised, placebo-controlled crossover RCT; directly evaluates Ambrisentan in patients with IPAH, FPAH, and HIV-associated PAH on stable background PAH therapy; exercise capacity primary endpoint — the strongest direct evidence in this pack |
| [NCT02290613](https://clinicaltrials.gov/study/NCT02290613) | PAH-CTD (SSc) | Phase 2 | Completed | 38 | EDITA trial: early Ambrisentan in borderline SSc-PAH (mPAP values just above threshold); randomised double-blind proof-of-concept; assessed pulmonary vascular remodelling markers and haemodynamics as primary endpoints |
| [NCT01042158](https://clinicaltrials.gov/study/NCT01042158) | PAH-CTD (SSc) | Phase 4 | Completed | 25 | Ambrisentan + Tadalafil combination in PAH-scleroderma spectrum disease; 36-week open-label study; 6MWD, NYHA functional class, and echocardiographic RV-PV function assessed |
| [NCT01808313](https://clinicaltrials.gov/study/NCT01808313) | PAH (broad, incl. CHD subgroup) | Phase 3 | Completed | 134 | Open-label Phase 3b in Chinese PAH patients; Ambrisentan 5 mg over 12 weeks primary evaluation period; exercise capacity (6MWT) as primary endpoint; CHD subgroup included |
| [NCT01342952](https://clinicaltrials.gov/study/NCT01342952) | Paediatric PAH (incl. CHD) | Phase 2 | Completed | 38 | Long-term extension of paediatric PAH study (ages 8–18 years); includes PAH-CHD subgroup; completed June 2022; high reference value for paediatric CHD-PAH management |
| [NCT01332331](https://clinicaltrials.gov/study/NCT01332331) | Paediatric PAH | Phase 2 | Terminated | 41 | High vs. low weight-adjusted Ambrisentan dose comparison in paediatric PAH; terminated early — provides partial dose-response relationships and PK data relevant to CHD-PAH children |
| [NCT02885012](https://clinicaltrials.gov/study/NCT02885012) | CTD-PAH (ERA switch) | Phase 4 | Terminated | 3 | Switch from bosentan or macitentan to Ambrisentan in CTD-PAH; terminated after 3 patients enrolled — no clinically meaningful efficacy or safety conclusions available |
| [NCT04095286](https://clinicaltrials.gov/study/NCT04095286) | Healthy volunteers (PK) | Phase 1 | Completed | 29 | Relative bioavailability of lower-dose paediatric Ambrisentan tablet dispersed in water vs. marketed tablet; pharmacokinetic reference for paediatric dosing — no efficacy endpoint |
| [NCT02688387](https://clinicaltrials.gov/study/NCT02688387) | Healthy volunteers (PK) | Phase 1 | Completed | 112 | Relative bioavailability of Ambrisentan + Tadalafil fixed-dose combination formulations; pharmacokinetic data supporting FDC development — no efficacy endpoint |
| [NCT01884675](https://clinicaltrials.gov/study/NCT01884675) | Inoperable CTEPH | Phase 3 | Terminated | 33 | Randomised, double-blind, placebo-controlled study of Ambrisentan 5 mg vs. placebo in inoperable chronic thromboembolic pulmonary hypertension; terminated early — insufficient data for conclusions |

---

## Literature Evidence

*Selected from across all evaluated indications, prioritised by study type and direct relevance to Ambrisentan. No literature was identified for PAVM beyond one indirect case report.*

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38378970](https://pubmed.ncbi.nlm.nih.gov/38378970/) | 2024 | Systematic Review & Meta-analysis | Internal and Emergency Medicine | Comprehensive meta-analysis of RCTs in CTD-PAH; demonstrates ERA-class benefit on 6MWD, functional class, and delay of clinical worsening; strongest aggregate evidence for CTD-PAH treatment |
| [23906950](https://pubmed.ncbi.nlm.nih.gov/23906950/) | 2013 | Meta-analysis | BMJ Open | CTD-PAH pharmacotherapy meta-analysis; quantifies ERA efficacy including Ambrisentan; useful for comparing relative treatment effect sizes across ERA-class agents |
| [32161055](https://pubmed.ncbi.nlm.nih.gov/32161055/) | 2020 | Post-hoc Analysis (RCT-based) | Annals of the Rheumatic Diseases | AMBITION trial post-hoc: initial Ambrisentan + Tadalafil combination superior to monotherapy in CTD-PAH; SSc-PAH subgroup shows attenuated response compared to iPAH — monitoring implications highlighted |
| [28039187](https://pubmed.ncbi.nlm.nih.gov/28039187/) | 2017 | Observational (RCT subgroup) | Annals of the Rheumatic Diseases | AMBITION CTD-PAH/SSc-PAH subgroup: combination Ambrisentan + Tadalafil benefit demonstrated; baseline risk stratification predictors identified for response optimisation |
| [27492539](https://pubmed.ncbi.nlm.nih.gov/27492539/) | 2016 | Retrospective Cohort | Respiratory Medicine | ARIES-E 3-year CTD-PAH subgroup analysis: sustained Ambrisentan efficacy and tolerability over long-term follow-up; relevant to durability of response in Danish CTD-PAH patients |
| [21371683](https://pubmed.ncbi.nlm.nih.gov/21371683/) | 2011 | Observational / Case Series | American Journal of Cardiology | Ambrisentan specifically in Eisenmenger syndrome (PAH-CHD): improvement in resting and exercise haemodynamics in a cohort of consecutive ES patients at Columbia University; first direct CHD-PAH case series for Ambrisentan |
| [34921523](https://pubmed.ncbi.nlm.nih.gov/34921523/) | 2022 | Prospective Observational | Pediatric Pulmonology | Real-world safety and tolerability of Ambrisentan + Tadalafil combination in paediatric pulmonary hypertension; supports use in paediatric CHD-PAH populations |
| [31096477](https://pubmed.ncbi.nlm.nih.gov/31096477/) | 2019 | Systematic Review | Medicine | PAH-specific drug therapy in Eisenmenger syndrome: systematic review and meta-analysis supporting ERA-class benefit on exercise capacity, quality of life, and functional class in CHD-PAH |
| [28425346](https://pubmed.ncbi.nlm.nih.gov/28425346/) | 2017 | Narrative Review | Therapeutic Advances in Respiratory Disease | Comprehensive Ambrisentan review: pharmacology, pivotal trial evidence across PAH subtypes including CTD-PAH, safety profile (incl. liver safety advantages over non-selective ERAs), and combination therapy evidence |
| [35412560](https://pubmed.ncbi.nlm.nih.gov/35412560/) | 2022 | Narrative Review | JAMA | PAH diagnosis and treatment overview; contextualises current standard-of-care and positions ETA antagonist class within modern PAH management algorithms |

---

## Denmark Market Information

Ambrisentan is not registered with the Danish Medicines Agency (Lægemiddelstyrelsen) and has no Danish marketing authorisations on record. The evidence pack identifies zero national authorisations.

> **Note for clinical access:** Ambrisentan (Volibris®) holds EMA centralised marketing authorisation, which is in principle valid across all EU member states including Denmark. If this authorisation is currently active, the product may be accessible to Danish patients through hospital pharmacy import procedures or via the EU centralised authorisation route. Danish prescribers should verify current availability and reimbursement status through Lægemiddelstyrelsen's Medicinpriser database and the hospital pharmacy import pathway (§29 procedure) before initiating treatment.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for complete safety information. No detailed key warnings, contraindications, or drug interaction data are available in this evidence pack.

Based on the drug class (selective ETA receptor antagonists), the following areas require SmPC verification before clinical use:

- **Hepatotoxicity**: All ERA-class agents require baseline and periodic liver enzyme monitoring (ALT/AST); Ambrisentan has a more favourable liver safety profile than non-selective ERAs, but monitoring remains mandatory
- **Teratogenicity**: ETA antagonists are teratogenic and embryotoxic; strict contraception and confirmed pregnancy exclusion are required for all women of childbearing potential
- **Peripheral oedema and fluid retention**: Common class-level adverse effect; relevant in patients with right heart failure
- **Drug interactions in PAH-HIV patients**: Ambrisentan is a CYP3A4 substrate and a P-glycoprotein substrate; interactions with ritonavir-boosted antiretroviral regimens and other HIV drugs require individual pharmacokinetic assessment before co-administration

---

## Conclusion and Next Steps

This evidence pack reveals markedly different levels of support across ten predicted indications. The following provides a decision per indication:

---

### Indication: Pulmonary Arteriovenous Malformation (PAVM) — *Highest TxGNN Score*

**Decision: Hold**

**Rationale:**
Despite the highest TxGNN prediction score (99.41%), PAVM is a structural vascular malformation managed by embolisation rather than pharmacological vasotone modulation. The ET-1 pathway has no established role in PAVM pathogenesis, and the only retrieved publication (PMID 33969094) is an indirect HHT-PAH co-morbidity case report, not evidence for Ambrisentan in PAVM.

**To proceed, the following is needed:**
- Mechanistic evidence demonstrating ET-1 pathway involvement in PAVM formation or progression
- Prospective case series or observational data reporting ETA antagonist outcomes in PAVM patients

---

### Indication: PAH Associated with HIV Infection — *Highest Evidence Level (L1)*

**Decision: Proceed with Guardrails**

**Rationale:**
NCT00709956 (Phase 3 RCT, double-blind, placebo-controlled crossover, n=64, completed) provides direct L1 evidence for Ambrisentan in HIV-PAH. This is a rare and underserved condition where evidence-based access to targeted therapy is clinically critical.

**To proceed, the following is needed:**
- Antiretroviral drug interaction assessment: detailed CYP3A4 and P-gp profile with the patient's specific HIV regimen
- Verification that EMA-authorised Ambrisentan (Volibris®) is accessible in Denmark
- Multidisciplinary management protocol involving pulmonology and infectious disease

---

### Indication: PAH Associated with Connective Tissue Disease (CTD-PAH)

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple completed trials (EDITA Phase 2, AMBITION Phase 4 subgroup), two meta-analyses (PMID 38378970, PMID 23906950), and 3-year ARIES-E follow-up collectively provide robust L2 support. The SSc-PAH subgroup consistently shows an attenuated response relative to idiopathic PAH and demands a structured monitoring programme.

**To proceed, the following is needed:**
- Baseline right heart catheterisation and echocardiographic monitoring plan (SSc-PAH can progress despite therapy)
- Baseline and follow-up liver function testing
- Danish access pathway confirmation for Ambrisentan (Volibris®)

---

### Indication: PAH Associated with Congenital Heart Disease (PAH-CHD)

**Decision: Proceed with Guardrails**

**Rationale:**
NCT01808313 (Phase 3, completed, n=134), PMID 21371683 (Eisenmenger syndrome case series), paediatric extension data (NCT01342952), and a systematic review (PMID 31096477) provide supporting L2 evidence. CHD is a formal WHO Group 1 PAH subcategory sharing the ETA pathway targeted by Ambrisentan.

**To proceed, the following is needed:**
- Formal assessment of operability status and shunt type prior to treatment initiation
- Haematological monitoring plan for Eisenmenger syndrome patients (polycythaemia, iron deficiency, coagulation)
- Paediatric formulation availability confirmation for younger CHD-PAH patients

---

*This report is for research reference only and does not constitute medical advice. All drug repurposing candidates require clinical validation before therapeutic application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

