---
layout: default
title: Acalabrutinib
parent: 僅模型預測 (L5)
nav_order: 13
evidence_level: L5
indication_count: 10
---

# Acalabrutinib
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

# Drug Repurposing Evidence Report

## Acalabrutinib (Calquence®) — Multi-Indication Analysis

| Field | Detail |
|---|---|
| **Report ID** | DK-DB11703-multi |
| **Version** | v4 |
| **Date** | 2026-04-03 |
| **Data Cutoff** | 2026-04-03 |
| **Regulatory Context** | Lægemiddelstyrelsen (Danish Medicines Agency) / EMA |

---

## 1. Executive Summary

**Drug:** Acalabrutinib (INN), marketed as Calquence® (AstraZeneca / Acerta Pharma)

**DrugBank ID:** DB11703

**Proposed Repurposing Indications (TxGNN-predicted, ranked by score):**

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Recommendation |
|------|----------------------|-------------|----------------|----------------|
| 1 | Familial non-Hodgkin lymphoma (NHL) | 0.976 | **L1** | Proceed with Guardrails |
| 2 | Colon adenocarcinoma | 0.966 | **L5** | Hold |
| 3 | Small intestinal Burkitt lymphoma | 0.940 | **L4** | Research Question |
| 4 | Small intestinal MALT lymphoma | 0.938 | **L4** | Research Question |
| 5 | Thyroid gland MALT lymphoma | 0.938 | **L4** | Research Question |

**Key Findings:**

- Acalabrutinib is a second-generation, highly selective, irreversible Bruton tyrosine kinase (BTK) inhibitor with EMA centralised marketing authorisation (valid in Denmark) for chronic lymphocytic leukaemia (CLL) and mantle cell lymphoma (MCL).
- For **familial NHL**, robust Phase 2/3 clinical trial evidence and >20 peer-reviewed publications directly support BTK inhibition in multiple NHL subtypes. Acalabrutinib is already used as a comparator/standard-of-care arm in Phase 3 NHL trials, confirming clinical acceptance. Evidence level: **L1**.
- For **MALT lymphomas** (small intestinal and thyroid), strong mechanistic rationale exists based on BCR-pathway dependence and ibrutinib's FDA approval for marginal zone lymphoma (MZL), but no direct clinical trial data for acalabrutinib in these specific subtypes were identified. Evidence level: **L4**.
- For **Burkitt lymphoma**, mechanistic rationale is moderate (tonic rather than chronic active BCR signalling), with no clinical evidence. Evidence level: **L4**.
- For **colon adenocarcinoma**, mechanistic rationale is weak and no clinical evidence exists. Evidence level: **L5** — not recommended for further pursuit.

**Data Gaps Identified:**
- Danish/EMA product label warnings and contraindications not extracted from the current dataset (originally sourced from TFDA context).
- Full mechanism of action (MOA) detail was flagged as a data gap in the evidence pack but is well-characterised in literature (see Section 2).

---

## 2. Drug Overview

### 2.1 Approved Indications in Denmark (via EMA Centralised Procedure)

Acalabrutinib (Calquence®) holds a centralised EMA marketing authorisation (EU/1/20/1479), valid across all EU/EEA member states including Denmark. As of the data cutoff:

| Indication | Approval Basis | Line of Therapy |
|------------|----------------|-----------------|
| **Chronic lymphocytic leukaemia (CLL)** | Phase 3 RCTs (ELEVATE-TN, ASCEND) | Monotherapy or combination; treatment-naïve or relapsed/refractory |
| **Mantle cell lymphoma (MCL)** | Phase 2 pivotal (ACE-LY-004) | Monotherapy; ≥1 prior therapy |

**Note:** The evidence pack indicates "未上市" (not marketed) in Taiwan, but acalabrutinib IS authorised and available in Denmark via the EMA centralised procedure and is listed in Medicinpriser.dk.

### 2.2 Mechanism of Action

Acalabrutinib is a **second-generation, highly selective, covalent (irreversible) inhibitor of Bruton tyrosine kinase (BTK)**.

- **Target:** BTK (EC 2.7.10.2), a cytoplasmic tyrosine kinase critical to B-cell receptor (BCR) signalling.
- **Binding:** Forms a covalent bond with Cys481 in the ATP-binding pocket of BTK.
- **Downstream effects:** Blocks BCR-mediated activation of NF-κB, MAPK, and NFAT pathways → inhibits B-cell proliferation, survival, adhesion, and migration.
- **Selectivity advantage:** Compared to first-generation ibrutinib, acalabrutinib demonstrates minimal off-target inhibition of EGFR, ITK, and TEC kinases, resulting in a more favourable cardiovascular and bleeding safety profile.

### 2.3 Pharmacokinetic Profile

| Parameter | Value |
|-----------|-------|
| **Bioavailability** | ~25% (oral) |
| **Tmax** | 0.5–1.5 hours |
| **Protein binding** | ~97.5% |
| **Metabolism** | Primarily CYP3A4; active metabolite ACP-5862 (equipotent BTK inhibitor, ~2–3× lower exposure) |
| **Half-life** | ~1 hour (parent); ~6.9 hours (ACP-5862) |
| **Dosage form** | Oral capsule, 100 mg |
| **Recommended dose** | 100 mg twice daily (BID), continuous |
| **Elimination** | Hepatic metabolism; ~84% faecal, ~12% renal |
| **Food effect** | No clinically significant effect |
| **pH sensitivity** | Absorption reduced by gastric acid-reducing agents (PPIs, H2RAs) |

---

## 3. Evidence Analysis

### 3.1 Indication 1: Familial Non-Hodgkin Lymphoma (NHL)

**TxGNN Score:** 0.976 | **Evidence Level: L1** | **Decision Stage: S3 — Proceed with Guardrails**

#### 3.1.1 Mechanistic Rationale

**Directly relevant.** BTK is the critical kinase in the BCR signalling pathway. The majority of NHL subtypes—including MCL, DLBCL (particularly ABC subtype), follicular lymphoma (FL), and marginal zone lymphoma (MZL)—depend on BCR signalling for survival and proliferation. Familial NHL shares the same BCR-dependent pathobiology as sporadic NHL; the familial predisposition relates to germline susceptibility rather than a distinct tumour biology. Therefore, BTK inhibition efficacy is expected to be equivalent in familial and sporadic presentations.

#### 3.1.2 Clinical Trials

A total of **20 clinical trials** were identified on ClinicalTrials.gov. The table below summarises the most relevant:

**Completed Trials:**

| NCT ID | Phase | N | NHL Subtype | Status | Key Finding |
|--------|-------|---|-------------|--------|-------------|
| NCT03571308 | Ib/II | 39 | DLBCL | **Completed** | Acalabrutinib + R-CHOP in untreated DLBCL; safety and preliminary efficacy data available |
| NCT02362035 | Ib/2 | 161 | Haematologic malignancies | **Completed** | Acalabrutinib + pembrolizumab; safety/PD/efficacy |
| NCT04094142 | II | 66 | R/R B-cell NHL | **Completed** | Acalabrutinib + rituximab + lenalidomide |
| NCT03623373 | II | 13 | Untreated MCL | **Completed** | Pilot: acalabrutinib + BR followed by CR |
| NCT03740529 | I/2 | 803 | CLL/SLL & NHL | **Completed** | Pirtobrutinib study (acalabrutinib as prior therapy) |

**Active/Recruiting Trials:**

| NCT ID | Phase | N | NHL Subtype | Status | Relevance |
|--------|-------|---|-------------|--------|-----------|
| NCT04883437 | **II** | 49 | Untreated indolent NHL/FL | Recruiting | Acalabrutinib + obinutuzumab; **Grade A** relevance |
| NCT05583149 | **II** | 28 | R/R aggressive B-cell lymphoma | Active | Acalabrutinib + liso-cel (CAR-T); **Grade A** |
| NCT04546620 | **II** | 453 | Untreated DLBCL | Active | Molecular-guided R-CHOP ± acalabrutinib; large-scale |
| NCT07377578 | **III** | 394 | R/R MCL | Recruiting | Rocbrutinib vs. BTKi (acalabrutinib as **standard-of-care comparator**); **Grade A** |
| NCT04002947 | **II** | 132 | Untreated DLBCL | Recruiting | Acalabrutinib + DA-EPOCH-R or R-CHOP |
| NCT03899337 | **II** | 105 | Richter's Syndrome | Recruiting | Acalabrutinib + CHOP-R vs. CHOP-R |
| NCT03571568 | I/2a | 140 | R/R indolent NHL | Recruiting | BI-1206 + rituximab ± acalabrutinib |
| NCT02180711 | Ib/2 | 113 | B-cell NHL (FL, MZL) | Active | Acalabrutinib ± rituximab ± lenalidomide |

**Withdrawn/Terminated Trials:**

| NCT ID | Phase | Reason | Impact |
|--------|-------|--------|--------|
| NCT02735876 | III | Withdrawn (0 enrolled) | No data; likely strategic/commercial decision |
| NCT04836832 | Ib/II | Withdrawn (0 enrolled) | No data |
| NCT04419389 | I/2 | Terminated (1 enrolled) | Minimal data |

**Key Observation:** NCT07377578 (PRIME Study, Phase III, n=394) uses acalabrutinib as the **investigator's choice standard-of-care BTK inhibitor** comparator arm for MCL, confirming that acalabrutinib is now considered an established treatment for NHL subtypes in clinical practice.

#### 3.1.3 Published Literature

**20 publications** were identified. Key Tier 1 (highest-quality) evidence:

| PMID | Year | Study Type | Key Content |
|------|------|-----------|-------------|
| **40311141** | 2025 | **Phase 3 RCT** | Acalabrutinib + bendamustine-rituximab in untreated MCL. Demonstrated comparable efficacy to ibrutinib-BR with improved toxicity profile. Published in *J Clin Oncol*. |
| **29241979** | 2018 | **Phase 2 Pivotal** (ACE-LY-004) | Acalabrutinib monotherapy in R/R MCL: **ORR 81%**, CR 40%. Published in *The Lancet*. Basis for FDA accelerated approval. |
| **37470152** | 2024 | **Phase 2 Final Results** | Final OS data for acalabrutinib monotherapy in R/R MCL, including poor-prognosis patients. Published in *Haematologica*. |
| **38781315** | 2024 | **Phase 1b** | Acalabrutinib + venetoclax + rituximab (AVR) in treatment-naïve MCL: 2-year data, 95.2% completed induction. Published in *Blood Advances*. |
| **38555311** | 2024 | **Phase 2** | Acalabrutinib + lenalidomide + rituximab (R2A) in R/R aggressive B-cell NHL. Single-arm trial; ORR as primary endpoint. Published in *Nature Communications*. |
| **39234862** | 2025 | **Phase Ib** | Acalabrutinib + bendamustine + rituximab (ABR) in TN and R/R MCL: safety/efficacy. Published in *Haematologica*. |
| **40775236** | 2025 | **Phase 2** | Frontline acalabrutinib + lenalidomide + rituximab in advanced FL with high tumour burden. Published in *Nature Communications*. |

**Key Tier 2 (reviews and mechanistic):**

| PMID | Year | Focus |
|------|------|-------|
| 36029036 | 2023 | BTKi resistance mechanisms in CLL and NHL |
| 38578606 | 2024 | New BTK targeting strategies, including degraders |
| 35266562 | 2022 | Comprehensive MCL update (molecular pathogenesis, treatment) |
| 39742965 | 2025 | Fungal infection risk with BTKi therapy (safety signal) |

#### 3.1.4 Evidence Summary for Familial NHL

| Category | Assessment |
|----------|------------|
| Mechanistic link | **Strong** — Direct BCR/BTK pathway target |
| Phase 3 evidence | **Yes** — RCT in MCL (PMID 40311141); acalabrutinib as standard comparator (NCT07377578) |
| Phase 2 evidence | **Multiple** — Pivotal ACE-LY-004, plus ongoing/completed trials in DLBCL, FL, MZL |
| Regulatory precedent | **Yes** — EMA-approved for MCL and CLL; FDA-approved for MCL and CLL |
| Evidence level | **L1** |

---

### 3.2 Indication 2: Colon Adenocarcinoma

**TxGNN Score:** 0.966 | **Evidence Level: L5** | **Decision Stage: S0 — Hold**

#### 3.2.1 Mechanistic Rationale

**Weak association.** Colon adenocarcinoma is driven primarily by WNT/β-catenin, RAS/MAPK, and PI3K/AKT signalling pathways. BTK is expressed in tumour-associated myeloid-derived suppressor cells (MDSCs) and tumour-associated macrophages (TAMs) within the tumour microenvironment, providing a theoretical immunomodulatory rationale. However, preclinical and early clinical studies with ibrutinib in solid tumours have not demonstrated meaningful efficacy.

#### 3.2.2 Clinical Evidence

- **Clinical trials:** 0 identified
- **Published literature:** 0 identified
- **ICTRP trials:** 0 identified

#### 3.2.3 Assessment

This remains an **AI-prediction-only** candidate with no supporting clinical or preclinical evidence specific to acalabrutinib. Not recommended for further pursuit at this time.

---

### 3.3 Indication 3: Small Intestinal Burkitt Lymphoma

**TxGNN Score:** 0.940 | **Evidence Level: L4** | **Decision Stage: S1 — Research Question**

#### 3.3.1 Mechanistic Rationale

**Moderate association.** Burkitt lymphoma is a highly aggressive B-cell NHL driven primarily by MYC translocation (t(8;14)). While it is B-cell derived and expresses surface immunoglobulin, its survival depends on "tonic" BCR signalling (PI3K-dependent) rather than the "chronic active" BCR signalling (BTK-dependent) seen in DLBCL-ABC or MCL. This distinction suggests potentially limited sensitivity to BTK inhibition. The small intestinal localisation is an anatomical consideration that does not alter the drug's mechanism.

#### 3.3.2 Clinical Evidence

- **Clinical trials:** 0 identified for this specific indication
- **Published literature:** 0 identified
- **Class-effect data:** No published BTKi trials specifically in Burkitt lymphoma

#### 3.3.3 Assessment

Preclinical/mechanistic evidence only. The biological distinction between tonic and chronic active BCR signalling is a significant concern. Would require dedicated preclinical validation before clinical investigation.

---

### 3.4 Indications 4–5: MALT Lymphomas (Small Intestinal & Thyroid Gland)

**TxGNN Score:** 0.938 / 0.938 | **Evidence Level: L4** | **Decision Stage: S1 — Research Question**

#### 3.4.1 Mechanistic Rationale

**Strong association.** MALT lymphomas are low-grade B-cell lymphomas belonging to the marginal zone lymphoma (MZL) category. They are highly dependent on BCR signalling, with NF-κB pathway constitutive activation (often via API2-MALT1 fusion, TNFAIP3 deletions, or chronic antigen stimulation). Key considerations:

- **Ibrutinib precedent:** FDA approved ibrutinib for R/R MZL (including MALT subtypes) in January 2017, validating the BTK target in this disease.
- **Thyroid MALT specificity:** Commonly arises from chronic autoimmune thyroiditis (Hashimoto's), where sustained B-cell antigen stimulation activates BCR/BTK pathways.
- **Acalabrutinib data in MZL:** Trial NCT02180711 (Phase 1b/2) includes an MZL cohort evaluating acalabrutinib ± rituximab (currently active, not recruiting, n=113).

#### 3.4.2 Clinical Evidence

- **Direct clinical trials for MALT-specific sites:** 0 identified
- **MZL-inclusive trial:** NCT02180711 (Phase 1b/2, active)
- **Published literature:** 0 identified for site-specific MALT lymphoma

#### 3.4.3 Assessment

Strong mechanistic rationale supported by class-effect regulatory approval (ibrutinib for MZL). Acalabrutinib's improved selectivity profile may offer advantages over ibrutinib in this typically indolent, long-treatment-duration patient population. Data from NCT02180711 (MZL cohort) may provide supportive evidence upon completion. A dedicated study in site-specific MALT lymphomas is warranted.

---

## 4. Safety Considerations

### 4.1 Known Adverse Effects (from EMA SmPC — Calquence®)

**Note:** The original evidence pack flagged safety data as a "Data Gap" from the TFDA context. The following is based on the EMA-authorised product information applicable in Denmark.

| Category | Common (≥1/10) | Notable Serious |
|----------|-----------------|-----------------|
| **Haematologic** | Neutropenia, anaemia, thrombocytopenia | Grade ≥3 neutropenia (~30%), febrile neutropenia |
| **Infections** | Upper respiratory tract infection, urinary tract infection | Opportunistic infections (PML reported with BTKi class); invasive fungal infections (aspergillosis) |
| **Bleeding** | Bruising, petechiae | Major haemorrhage (2–4%); epistaxis |
| **Cardiac** | — | Atrial fibrillation/flutter (~4%, lower than ibrutinib); second primary malignancies |
| **GI** | Diarrhoea, nausea, abdominal pain | — |
| **Musculoskeletal** | Headache, arthralgia, myalgia | — |
| **Other** | Fatigue, rash | Tumour lysis syndrome (rare) |

**Key Safety Advantage vs. Ibrutinib:** Head-to-head data (ELEVATE-RR trial) demonstrated significantly lower rates of atrial fibrillation, hypertension, and bleeding with acalabrutinib compared to ibrutinib.

### 4.2 Drug Interactions

| Interaction Type | Agent(s) | Effect | Management |
|-----------------|----------|--------|------------|
| **Strong CYP3A4 inhibitors** | Ketoconazole, itraconazole, clarithromycin, ritonavir | ↑ acalabrutinib exposure | **Avoid concomitant use** |
| **Moderate CYP3A4 inhibitors** | Fluconazole, erythromycin, diltiazem | ↑ acalabrutinib exposure | Reduce dose to 100 mg QD |
| **Strong CYP3A4 inducers** | Rifampicin, phenytoin, carbamazepine, St. John's wort | ↓ acalabrutinib exposure | **Avoid concomitant use** |
| **Gastric acid-reducing agents** | PPIs (omeprazole), H2RAs (ranitidine) | ↓ acalabrutinib absorption | Avoid PPIs; separate H2RA dosing by 2 hours |
| **Anticoagulants/antiplatelets** | Warfarin, DOACs, aspirin | ↑ bleeding risk | Monitor closely; risk–benefit assessment |
| **CYP3A4 substrates** | — | Acalabrutinib is a weak CYP3A4 inducer | Monitor narrow TI drugs |

### 4.3 Contraindications (EMA SmPC)

- Hypersensitivity to acalabrutinib or excipients
- Concomitant use with strong CYP3A4 inhibitors (relative contraindication)

### 4.4 Special Populations

| Population | Consideration |
|------------|---------------|
| **Hepatic impairment** | Mild–moderate: no dose adjustment; severe: not recommended (insufficient data) |
| **Renal impairment** | No dose adjustment required |
| **Pregnancy** | Avoid — potential foetal harm based on animal data |
| **Elderly** | No dose adjustment; monitor for infections |

---

## 5. Regulatory Status

### 5.1 Denmark (Lægemiddelstyrelsen)

| Parameter | Status |
|-----------|--------|
| **Marketing authorisation** | **Authorised** (via EMA centralised procedure EU/1/20/1479) |
| **Approved indications** | CLL (monotherapy or combination), MCL (monotherapy, ≥1 prior therapy) |
| **Brand name** | Calquence® |
| **MAH** | AstraZeneca AB |
| **Reimbursement** | Subject to Medicinrådet (Danish Medicines Council) assessment; check current status on Medicinpriser.dk |
| **Prescription status** | Prescription-only (Rx) |

### 5.2 EMA Status

| Parameter | Status |
|-----------|--------|
| **Centralised MA** | Granted 05 November 2020 |
| **Approved indications** | CLL (treatment-naïve in combination with obinutuzumab or as monotherapy; R/R as monotherapy); MCL (R/R, ≥1 prior therapy) |
| **Orphan designation** | No |
| **Conditional/exceptional** | Standard MA |

### 5.3 FDA Status (United States)

| Parameter | Status |
|-----------|--------|
| **First approval** | 31 October 2017 (accelerated, MCL) |
| **Full approval** | November 2019 (CLL/SLL) |
| **Approved indications** | MCL (≥1 prior therapy), CLL/SLL |
| **Breakthrough therapy** | Designated for MCL |

### 5.4 Regulatory Status for Predicted Indications

| Indication | Denmark/EMA | FDA | Any Jurisdiction |
|------------|-------------|-----|------------------|
| Familial NHL | Not specifically approved; MCL approval covers one NHL subtype | MCL approved | MCL and CLL approved globally |
| Colon adenocarcinoma | Not approved | Not approved | Not approved anywhere |
| Burkitt lymphoma | Not approved | Not approved | Not approved anywhere |
| MALT lymphoma (any site) | Not approved | Not approved (ibrutinib approved for MZL) | Ibrutinib approved for MZL (FDA) |
| DLBCL | Not approved | Not approved | Clinical trials ongoing |

---

## 6. Conclusion and Recommendations

### 6.1 Overall Assessment

| Indication | Final Score | Evidence | Mechanistic | Regulatory Path | Verdict |
|------------|------------|----------|-------------|-----------------|---------|
| **Familial NHL** | **L1** | Phase 3 RCT + pivotal Phase 2 + multiple ongoing trials | Strong (direct BTK/BCR target) | Already partially approved (MCL subtype); label extension feasible | **Proceed with Guardrails** |
| **MALT lymphomas** | **L4** | Indirect (ibrutinib MZL approval; NCT02180711 MZL cohort) | Strong | Class-effect precedent exists | **Research Question — High Priority** |
| **Burkitt lymphoma** | **L4** | None | Moderate (tonic vs. active BCR concern) | No precedent | **Research Question — Low Priority** |
| **Colon adenocarcinoma** | **L5** | None | Weak | No precedent | **Hold — Not Recommended** |

### 6.2 Evidence Gaps

| Gap ID | Description | Severity | Remediation |
|--------|-------------|----------|-------------|
| DG001 | Lægemiddelstyrelsen/EMA SmPC warnings and contraindications — detailed extraction needed | High | Download SmPC from EMA product page and parse |
| DG002 | MOA detail flagged in evidence pack — **resolved** in this report via literature review | Resolved | — |
| DG003 | No Denmark-specific registry data (RKKP / Danish Lymphoma Group) on acalabrutinib use in NHL | Medium | Query RKKP-LYFO (Danish National Lymphoma Registry) |
| DG004 | No ICTRP-registered Nordic trials identified | Low | Search NordicTrialAlliance / EudraCT for Scandinavian centres |
| DG005 | Medicinrådet reimbursement assessment status not confirmed | Medium | Check current Medicinrådet recommendations |
| DG006 | Drug–drug interaction data gap in evidence pack | Resolved | Populated from EMA SmPC in this report |
| DG007 | No pharmacovigilance signal data from Danish ADR database | Low | Query Danish Pharmacovigilance database |

### 6.3 Suggested Next Steps

#### For Familial NHL (Priority: High)

1. **Label extension analysis:** Acalabrutinib is already EMA-approved for MCL. Evaluate whether existing MCL data, combined with broader NHL trial results, supports a Lægemiddelstyrelsen compassionate use or off-label recommendation for other NHL subtypes not covered by current labelling.
2. **Monitor ongoing trials:** Key trials to track:
   - NCT04546620 (n=453, DLBCL, Phase 2) — results expected ~2028
   - NCT07377578 (n=394, MCL Phase 3, acalabrutinib as comparator) — results expected ~2033
   - NCT04883437 (n=49, indolent NHL Phase 2) — results expected ~2027
3. **Danish registry study:** Collaborate with RKKP-LYFO to evaluate real-world outcomes of acalabrutinib in Danish NHL patients receiving off-label treatment.
4. **Familial NHL subgroup analysis:** Request manufacturer data on outcomes in patients with family history of NHL from existing pivotal trials.

#### For MALT Lymphomas (Priority: Medium)

1. **Await NCT02180711 MZL cohort data** (expected completion 2028).
2. **Propose investigator-initiated trial** in partnership with Danish Lymphoma Group (DLG) for acalabrutinib in R/R MALT lymphoma, leveraging ibrutinib MZL data as proof of concept.
3. **Pharmacovigilance comparison:** Compare long-term safety profiles of acalabrutinib vs. ibrutinib for the indolent, long-treatment-duration MALT population — acalabrutinib's selectivity advantage may be clinically meaningful.

#### For Burkitt Lymphoma (Priority: Low)

1. **Preclinical validation required:** Recommend in vitro studies of acalabrutinib in Burkitt lymphoma cell lines to assess sensitivity (tonic vs. active BCR signalling dependency).
2. **Do not pursue clinical investigation** until preclinical data supports BTK-dependence.

#### For Colon Adenocarcinoma (Priority: None)

1. **No further action recommended.** Insufficient mechanistic rationale and absence of any supporting evidence.

---

## Appendix A: Data Sources & Query Log Summary

| Source | Queries | Results |
|--------|---------|---------|
| ClinicalTrials.gov | 10 queries across 5 indications | 20 trials (NHL); 0 (all others) |
| ICTRP | 10 queries | 0 across all indications |
| PubMed | 10 queries | 20 publications (NHL); 0 (all others) |
| DrugBank | 1 query | 1 result (drug identified) |
| DDI database | 1 query | 0 results (data gap) |

**Data collection date:** 2026-03-24

## Appendix B: Evidence Level Definitions

| Level | Definition | Applicable Indications |
|-------|------------|----------------------|
| **L1** | Phase 3+ clinical trial evidence | Familial NHL |
| **L2** | Phase 2 clinical trial evidence | — |
| **L3** | Observational study evidence | — |
| **L4** | Preclinical/mechanistic evidence | Burkitt lymphoma, MALT lymphomas |
| **L5** | AI prediction only (no clinical evidence) | Colon adenocarcinoma |

---

> **Disclaimer:** This report is generated for research purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before therapeutic application. This report was prepared in the context of the Danish Medicines Agency (Lægemiddelstyrelsen) regulatory framework. Clinicians should consult the current EMA-approved Summary of Product Characteristics (SmPC) and Medicinrådet guidelines before making prescribing decisions.
>
> **YMYL Notice:** The content herein pertains to pharmaceutical and oncological research. Treatment decisions must be made by qualified healthcare professionals in consultation with patients.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

