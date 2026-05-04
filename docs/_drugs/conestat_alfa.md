---
layout: default
title: Conestat Alfa
parent: 僅模型預測 (L5)
nav_order: 122
evidence_level: L5
indication_count: 10
---

# Conestat Alfa
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

# Conestat Alfa: From No Active Danish Registration to C1 Inhibitor Deficiency (Hereditary Angioedema)

## One-Sentence Summary

Conestat alfa (Ruconest®) is a recombinant human C1-esterase inhibitor (rhC1-INH) produced in transgenic rabbits, approved by the EMA and FDA for treating acute hereditary angioedema (HAE) attacks in adults and adolescents with C1 inhibitor deficiency — but not currently active in the Danish Laegemiddelstyrelsen database.
The TxGNN model assigns it a prediction score of **99.999%** for **C1 Inhibitor Deficiency**, a finding supported by **multiple completed Phase 3 RCTs** and **20 publications** directly evaluating this drug-disease pair.
Importantly, this is not a conventional repurposing scenario: the TxGNN prediction reflects perfect mechanistic alignment with the drug's established global indication, and the primary clinical question for Denmark is one of **market access and implementation** rather than scientific uncertainty.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No approved indication registered in the Danish Medicines Agency (Laegemiddelstyrelsen) database |
| Predicted New Indication | C1 Inhibitor Deficiency (Hereditary Angioedema, HAE Type I/II) |
| TxGNN Prediction Score | 99.999% |
| Evidence Level | L1 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Conestat alfa is a recombinant form of human C1-esterase inhibitor (C1-INH), the protein encoded by the *SERPING1* gene. C1-INH belongs to the serpin superfamily and serves as a critical physiological brake on three interconnected plasma cascades: the complement system (inhibiting C1r and C1s), the contact activation/kallikrein-kinin pathway (inhibiting FXIIa, plasma kallikrein, and FXIa), and the coagulation system. Because detailed formal MOA documentation was not available in the current evidence pack, the mechanistic reasoning below is based on established published knowledge about the drug's protein class and the pathophysiology of HAE.

In patients with C1 inhibitor deficiency — both HAE Type I (reduced C1-INH protein quantity, ~85% of patients) and Type II (dysfunctional C1-INH protein, ~15%) — the loss of inhibitory control over the contact activation pathway leads to unregulated FXII → kallikrein → bradykinin generation. Excess bradykinin binds to endothelial B2 receptors, increasing vascular permeability and causing the characteristic subcutaneous and submucosal swelling affecting the extremities, face, gastrointestinal tract, and larynx. Laryngeal attacks carry a risk of fatal asphyxiation, making this a potentially life-threatening rare disease.

Conestat alfa acts as a **direct replacement therapy**: intravenous administration immediately restores functional C1-INH protein levels in the patient's circulation, halting the dysregulated protease cascade and resolving the acute attack. This mechanism directly targets the disease's root molecular defect — it is not an indirect or repurposed mechanism but a biologically precise intervention. The TxGNN model's near-perfect prediction score therefore reflects the complete mechanistic alignment between this drug and this disease rather than a novel discovery, and should be interpreted as strong confirmatory evidence for a drug that has already been approved by the EMA (as Ruconest®) and FDA but has yet to be actively established in Danish clinical practice.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00262301](https://clinicaltrials.gov/study/NCT00262301) | Phase 3 | Completed | 75 | Randomised, double-blind, placebo-controlled pivotal study confirming safety, tolerability, efficacy, and PK/PD of recombinant human C1-INH (rhC1INH) for acute HAE attacks |
| [NCT01188564](https://clinicaltrials.gov/study/NCT01188564) | Phase 3 | Completed | 75 | Phase 3 RCT with open-label extension confirming efficacy, safety, and immunogenicity of rhC1INH 50 U/kg for treatment of acute HAE angioedema attacks |
| [NCT00289211](https://clinicaltrials.gov/study/NCT00289211) | Phase 3 | Completed | 83 | LEVP2005-1/Part A — core pivotal RCT (double-blind, placebo-controlled) evaluating C1INH-nf for acute HAE attacks; directly supports EMA regulatory approval |
| [NCT00225147](https://clinicaltrials.gov/study/NCT00225147) | Phase 2/3 | Completed | 77 | Randomised, double-blind, placebo-controlled Phase 2/3 study evaluating safety, tolerability, efficacy, and PK/PD of recombinant human C1-INH for acute HAE attacks |
| [NCT01005888](https://clinicaltrials.gov/study/NCT01005888) | Phase 3 | Completed | 26 | LEVP2005-1/Part B — double-blind, placebo-controlled confirmatory study of C1INH-nf for prophylactic prevention of HAE attacks |
| [NCT01359969](https://clinicaltrials.gov/study/NCT01359969) | Phase 2 | Completed | 57 | Open-label study evaluating safety, immunogenicity, PK, and efficacy of Ruconest 50 U/kg for acute HAE attacks in paediatric patients aged 2–13 years |
| [NCT00168103](https://clinicaltrials.gov/study/NCT00168103) | Phase 2/3 | Completed | 126 | Plasma-derived C1-INH concentrate (CE1145) in 126 patients with congenital C1-INH deficiency and acute abdominal or facial HAE attacks; supports class effect |
| [NCT02663687](https://clinicaltrials.gov/study/NCT02663687) | Phase 1 | Completed | 48 | Randomised, double-blind, placebo-controlled ascending-dose study assessing safety, tolerability, and PK of recombinant human C1-INH (SHP623) administered IV and SC in healthy adults |
| [NCT02870972](https://clinicaltrials.gov/study/NCT02870972) | Phase 2 | Completed | 75 | Randomised, double-blind, placebo-controlled, dose-ranging parallel-group study of oral BCX7353 (kallikrein inhibitor) for preventing HAE attacks; supports mechanistic importance of the bradykinin pathway |
| [NCT06679426](https://clinicaltrials.gov/study/NCT06679426) | Phase 3 | Not yet recruiting | 24 | Phase 3 RCT evaluating Conestat alfa specifically for ACE-inhibitor-induced angioedema — represents an active indication-expansion programme |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30021471](https://pubmed.ncbi.nlm.nih.gov/30021471/) | 2018 | Prospective Clinical Study | Expert Rev Clin Immunol | Conestat alfa (rhC1-INH) reviewed for prophylactic use in HAE; confirmed registration for acute attacks in adults and adolescents across Europe, Americas, and Israel |
| [31982824](https://pubmed.ncbi.nlm.nih.gov/31982824/) | 2020 | Clinical Cohort Study | Int Immunopharmacol | Real-world evaluation of home treatment efficacy and safety with rhC1-INH in HAE-C1-INH deficiency, including short-term prophylaxis outcomes |
| [22946752](https://pubmed.ncbi.nlm.nih.gov/22946752/) | 2012 | Drug Review | BioDrugs | Comprehensive review of Conestat alfa's efficacy from two pivotal randomised, double-blind, placebo-controlled trials; confirms clinical significance |
| [24801469](https://pubmed.ncbi.nlm.nih.gov/24801469/) | 2014 | Clinical Study | Allergy Asthma Proc | Real-life home treatment with Conestat alfa across 65 oedematous episodes in HAE-C1-INH patients; demonstrates practical safety and rapid symptom resolution |
| [22171564](https://pubmed.ncbi.nlm.nih.gov/22171564/) | 2012 | Clinical Study (PD) | BioDrugs | Pharmacodynamic assessment of recombinant C1-INH (Ruconest®) effects on coagulation and fibrinolysis in HAE patients; demonstrates favourable thromboembolic safety profile vs. plasma-derived products |
| [23420425](https://pubmed.ncbi.nlm.nih.gov/23420425/) | 2013 | Systematic Review | Pneumonol Alergol Pol | Comparative systematic review of clinical effectiveness of Conestat alfa, human C1-INH, and icatibant for treatment of acute angioedema attacks in adults with HAE |
| [26250409](https://pubmed.ncbi.nlm.nih.gov/26250409/) | 2015 | Review | Immunotherapy | Review of recombinant replacement therapy for HAE due to C1 inhibitor deficiency, covering regulatory approvals, mechanisms, and clinical evidence base |
| [28687108](https://pubmed.ncbi.nlm.nih.gov/28687108/) | 2017 | Review | Immunol Allergy Clin North Am | Acute management of HAE attacks: four approved treatments including rhC1-INH reviewed with practical guidance; notes limited availability in developing countries |
| [26106828](https://pubmed.ncbi.nlm.nih.gov/26106828/) | 2015 | Clinical Practice Guidelines | Curr Opin Allergy Clin Immunol | Italian national diagnostic and therapeutic management guidelines for C1-INH deficiency HAE, including Conestat alfa as a standard treatment option |
| [27940765](https://pubmed.ncbi.nlm.nih.gov/27940765/) | 2016 | Review | Pediatrics | Management of children with HAE due to C1 inhibitor deficiency; reviews newly approved adult therapies for paediatric application — directly relevant to NCT01359969 paediatric data |

---

## Denmark Market Information

According to the evidence pack, Conestat alfa currently has **no active marketing authorisation** recorded in the Laegemiddelstyrelsen database (market status: not marketed, 0 authorisations).

However, it is important to note that Ruconest® holds a **centralised EMA marketing authorisation** (EU/1/10/631/001, granted 2010), which in principle covers all EU member states including Denmark. The absence from the local database may reflect a commercial availability or reimbursement (tilskud) gap rather than a regulatory barrier. Clinicians are strongly advised to verify current supply and reimbursement status directly with the Laegemiddelstyrelsen or the regional hospital pharmacy before attempting to prescribe.

| Marketing Authorisation | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMA EU/1/10/631/001 (centralised — verify local availability) | Ruconest® | Powder for solution for injection (2100 IU vial, IV) | Treatment of acute angioedema attacks in adults and adolescents (≥13 years) with HAE due to C1-INH deficiency |
| No Danish national authorisation found in database | — | — | — |

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for Ruconest® (conestat alfa) for complete safety information, as no specific safety data (key warnings, contraindications, or drug interactions) were available in this evidence pack.

Based on established pharmacological class knowledge, the following points are clinically relevant for Danish prescribers:

- **Rabbit allergy**: Conestat alfa is produced in the milk of transgenic rabbits. Patients with known or suspected rabbit allergy should **not** receive this product, as hypersensitivity reactions — including anaphylaxis — have been reported. Pre-treatment allergy screening is required.
- **Drug interactions**: No DDI data were retrieved. C1-INH replacement therapy is generally considered to have low interaction potential with small-molecule drugs, but the SmPC should be consulted for any updates.
- **No myelosuppression or cytotoxicity risk** applicable to this drug class.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The evidence base for Conestat alfa in C1 inhibitor deficiency is among the strongest available for any orphan biologic — multiple completed Phase 3 randomised controlled trials, regulatory approvals from both EMA and FDA, and a rich real-world literature base confirm both efficacy and safety. The TxGNN prediction score of >99.999% is analytically consistent with this established evidence. The primary barrier to use in Denmark is not clinical uncertainty but rather the absence of an active commercial pathway and confirmed reimbursement arrangement.

**To proceed, the following is needed:**

- **Confirm regulatory availability**: Verify with Laegemiddelstyrelsen whether the EMA centralised authorisation for Ruconest® (EU/1/10/631/001) is actively available for prescribing and supply in Denmark, or whether a named-patient/compassionate-use pathway is required in the interim
- **Obtain the full SmPC**: Download the current Ruconest® SmPC from the EMA product page for Danish-language safety communication and prescriber information
- **Confirm reimbursement (tilskud) status**: Engage with Medicinrådet or the relevant regional formulary committee to assess whether reimbursement has been established or needs to be applied for
- **Identify and map the Danish HAE patient population**: HAE due to C1-INH deficiency affects approximately 1:50,000 individuals; coordinate with specialist immunology/allergology centres (e.g., Odense University Hospital, Aarhus, Rigshospitalet) who manage the national HAE cohort
- **Obtain complete SmPC safety data**: Retrieve the Laegemiddelstyrelsen product leaflet or EMA SmPC to complete the safety gap items (DG001 — warnings/contraindications; DG002 — formal MOA documentation) before initiating any new patient programme
- **Establish administration protocol**: Ruconest® is administered intravenously; confirm whether hospital-based or home-based self-administration protocols are appropriate for the Danish HAE cohort, drawing on the published home treatment experience (PMID 24801469, PMID 31982824)

> **Disclaimer**: This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before therapeutic application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

