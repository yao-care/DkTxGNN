---
layout: default
title: Alemtuzumab
parent: 僅模型預測 (L5)
nav_order: 21
evidence_level: L5
indication_count: 10
---

# Alemtuzumab
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

# Alemtuzumab: From B-Cell Chronic Lymphocytic Leukaemia to Syndrome with Combined Immunodeficiency

## One-Sentence Summary

Alemtuzumab is a humanised anti-CD52 monoclonal antibody internationally approved for B-cell chronic lymphocytic leukaemia (B-CLL) and relapsing-remitting multiple sclerosis, but not currently registered in Denmark. The TxGNN model predicts it may be effective as a conditioning agent in allogeneic haematopoietic stem cell transplantation (allo-HSCT) for **Syndrome with Combined Immunodeficiency**, supported by **13 clinical trials** and **12 publications**. Note: the numerically highest TxGNN score belongs to hepatic infarction (94.44%), but this indication carries no supporting clinical evidence (L5, Hold); syndrome with combined immunodeficiency (93.73%) represents the most clinically actionable and evidence-supported prediction in this evidence pack.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | B-Cell Chronic Lymphocytic Leukaemia / Relapsing-Remitting Multiple Sclerosis (international approvals; no registered indication in Denmark) |
| Predicted New Indication | Syndrome with Combined Immunodeficiency |
| TxGNN Prediction Score | 93.73% |
| Evidence Level | L3 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available in the current evidence pack. Based on established pharmacological knowledge, Alemtuzumab is a humanised IgG1 kappa monoclonal antibody targeting CD52 — a glycoprotein highly expressed on mature T lymphocytes, B lymphocytes, NK cells, and monocytes. Upon binding CD52, it triggers rapid and sustained lymphocyte depletion via complement-dependent cytotoxicity (CDC), antibody-dependent cellular cytotoxicity (ADCC), and direct apoptotic signalling, with minimal toxicity to non-haematopoietic tissues.

This lymphodepletion mechanism maps directly onto the requirements of allo-HSCT conditioning for combined immunodeficiency. Patients with primary combined immunodeficiency disorders — including SCID, XIAP deficiency, Hyper-IgM syndrome (CD40L deficiency), IPEX syndrome, Wiskott-Aldrich syndrome, and chronic granulomatous disease (CGD) — are characterised by absent or severely impaired lymphocyte function. Curative allo-HSCT in this setting requires immune space creation prior to transplant to permit donor cell engraftment while minimising graft-versus-host disease (GvHD) risk and transplant-related mortality. Alemtuzumab's selective lymphocyte targeting, low organ toxicity, and suitability for reduced-intensity conditioning (RIC) make it particularly appropriate for fragile paediatric patients who cannot safely tolerate conventional myeloablative conditioning regimens.

The repurposing rationale is therefore a direct extension of the drug's established pharmacology: the same CD52-targeting lymphodepletion used in treating lymphocytic malignancy is applied to immune-space creation for curative transplantation. Multiple specialist transplant centres internationally have incorporated alemtuzumab-based RIC as a standard conditioning backbone for paediatric primary immunodeficiency, and the available evidence base reflects established clinical practice rather than a speculative hypothesis. The primary evidence gap is the absence of Phase 3 RCTs, which reflects the rarity of these conditions rather than a fundamental pharmacological uncertainty.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT00579137](https://clinicaltrials.gov/study/NCT00579137) | Phase 1/2 | Terminated | 3 | Only trial directly naming alemtuzumab as sole conditioning agent for allo-HSCT in SCID and primary immunodeficiency disorders; terminated early (3 patients enrolled), primary value is safety signal generation |
| [NCT01182675](https://clinicaltrials.gov/study/NCT01182675) | Phase 2 | Terminated | 7 | Novel chemo-free conditioning using alemtuzumab + plerixafor/filgrastim for HSCT in children with SCID; aims to eliminate toxic chemotherapy conditioning while maximising T/B cell immune reconstitution |
| [NCT05463133](https://clinicaltrials.gov/study/NCT05463133) | Phase 1/2 | Recruiting | 50 | Allo-HSCT for chronic granulomatous disease using alemtuzumab/busulfan/TBI combined with cytokine antagonists (IL-6 ± IFN-γ); largest ongoing trial directly incorporating alemtuzumab in a primary immunodeficiency |
| [NCT07284641](https://clinicaltrials.gov/study/NCT07284641) | Phase 2 | Recruiting | 25 | RIC-HSCT with TBI for CVID and other autoimmune manifestations of primary immune regulatory disorders; most recently initiated prospective trial in this indication (2026 start) |
| [NCT01652092](https://clinicaltrials.gov/study/NCT01652092) | N/A | Active, not recruiting | 57 | Standard-of-care allo-HSCT guideline registry for primary immune deficiencies; largest real-world dataset in this indication, reflecting current clinical practice |
| [NCT01962415](https://clinicaltrials.gov/study/NCT01962415) | Phase 2 | Recruiting | 100 | RIC with cord blood/bone marrow/PBSC transplant in paediatric and young adult non-malignant disorders including immunodeficiencies; largest active enrolment among ongoing trials |
| [NCT01019876](https://clinicaltrials.gov/study/NCT01019876) | Phase 2/3 | Completed | 38 | Risk-adapted allo-SCT for non-malignant diseases including immunodeficiencies across four strata (bone marrow failure, immunodeficiencies, metabolic errors, histiocytoses); completed 2021 — long-term outcome data available |
| [NCT01821781](https://clinicaltrials.gov/study/NCT01821781) | Phase 2 | Active, not recruiting | 20 | RIC-HSCT for immune function disorders using maximised host immunosuppression to reduce graft rejection; alemtuzumab likely included as conditioning component |
| [NCT00744692](https://clinicaltrials.gov/study/NCT00744692) | Phase 1 | Completed | 22 | Feasibility of RIC in paediatric non-malignant disorder cord blood transplantation; earliest safety feasibility data in this population, engraftment endpoint >25% donor chimerism at 180 days |
| [NCT04528355](https://clinicaltrials.gov/study/NCT04528355) | N/A | Recruiting | 50 | Prospective outcomes registry for non-malignant disorders undergoing RIC-HSCT; specifically examines alemtuzumab dosing strata to prevent graft failure and support immune reconstitution |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [27543157](https://pubmed.ncbi.nlm.nih.gov/27543157/) | 2016 | Retrospective Cohort | Biol Blood Marrow Transplant | Single-centre comparison: alemtuzumab/fludarabine/melphalan RIC (n=4) vs myeloablative busulfan/cyclophosphamide/ATG (n=14) in CGD; RIC showed lower transplant-related toxicity |
| [23131490](https://pubmed.ncbi.nlm.nih.gov/23131490/) | 2013 | Multicenter Retrospective | Blood | International survey of allo-HCT for XIAP deficiency (19 patients); alemtuzumab-based RIC predominated among 11 patients receiving reduced-intensity regimens; overall outcomes poor, highlighting unmet need |
| [29155317](https://pubmed.ncbi.nlm.nih.gov/29155317/) | 2018 | Retrospective Cohort | Biol Blood Marrow Transplant | 160 children with primary immunodeficiency receiving treosulfan/fludarabine/alemtuzumab conditioning; improved toxicity and T-cell chimerism compared to earlier cyclophosphamide-based cohort (n=70) |
| [21325599](https://pubmed.ncbi.nlm.nih.gov/21325599/) | 2011 | Retrospective Cohort | Blood | 70 children with primary immunodeficiency receiving treosulfan conditioning with alemtuzumab; lower veno-occlusive disease rates compared to busulfan; does not require pharmacokinetic monitoring |
| [18940685](https://pubmed.ncbi.nlm.nih.gov/18940685/) | 2008 | Case Series | Biol Blood Marrow Transplant | Campath-1H (alemtuzumab) + fludarabine for rescue of stem cell graft failure in 12 paediatric patients including 4 with SCID; effective lymphodepletion achieved without myeloablation |
| [26073206](https://pubmed.ncbi.nlm.nih.gov/26073206/) | 2015 | Single-Centre Retrospective | Pediatric Transplantation | HSCT outcomes for Hyper-IgM syndrome due to CD40L deficiency (5 patients, median age 41 months); HSCT demonstrated as curative in this combined immunodeficiency variant |
| [19471859](https://pubmed.ncbi.nlm.nih.gov/19471859/) | 2009 | Case Series | Immunologic Research | FOXP3+ T-regulatory cell reconstitution after RIC-HSCT for IPEX syndrome; immune reconstitution of regulatory T cells correlated with clinical remission of multi-organ autoimmunity |
| [11841458](https://pubmed.ncbi.nlm.nih.gov/11841458/) | 2002 | Case Report | Br J Haematol | Non-myeloablative BMT in a 26-year-old with Wiskott-Aldrich syndrome; alemtuzumab-based conditioning achieved partial engraftment and immune restoration despite active infections and vasculitis |
| [15590388](https://pubmed.ncbi.nlm.nih.gov/15590388/) | 2004 | Safety Review | Haematologica | Infectious toxicity profile of alemtuzumab; key safety reference for its use in profoundly immunocompromised patients undergoing conditioning |
| [18502831](https://pubmed.ncbi.nlm.nih.gov/18502831/) | 2008 | Case Report | Blood | EBV-positive lymphoproliferative disease following alemtuzumab-CHOP therapy; documents EBV reactivation risk with profound immunodepletion — critical safety signal for transplant setting |

---

## Denmark Market Information

Alemtuzumab currently has **no national marketing authorisations registered with Lægemiddelstyrelsen** (0 Danish registrations). Two alemtuzumab products hold or have held centralised EU marketing authorisations via the EMA, which apply in Denmark:

| Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------------------|-------------|-------------|---------------------|
| EU/1/01/193 (marketing suspended) | MabCampath 30 mg/3 mL | Concentrate for solution for infusion | B-cell chronic lymphocytic leukaemia (first-line and relapsed/refractory); available via exceptional circumstances/compassionate use in EU |
| EU/1/13/878 | Lemtrada 12 mg/1.2 mL | Concentrate for solution for infusion | Active relapsing-remitting multiple sclerosis in adults with ≥2 relapses in the preceding 2 years or rapidly evolving severe RRMS |

> Clinical use in Denmark for non-approved indications (e.g., conditioning for combined immunodeficiency) requires individual patient authorisation from Lægemiddelstyrelsen under named-patient or compassionate use provisions, or enrolment within an approved clinical trial protocol.

---

## Cytotoxicity

Alemtuzumab carries antineoplastic approval (B-cell CLL). In the context of this repurposing evaluation, it functions as a targeted lymphodepleting conditioning agent rather than a direct tumour cytotoxic.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted biological therapy — humanised anti-CD52 monoclonal antibody; lymphocyte-depleting; not a conventional cytotoxic agent |
| Myelosuppression Risk | Moderate — profound and prolonged lymphopenia (T, B, NK cell depletion); thrombocytopenia and neutropenia possible, particularly in combination with fludarabine/melphalan conditioning regimens |
| Emetogenicity Classification | Minimal to low (monoclonal antibody; primary acute toxicity is infusion-related reactions, not chemotherapy-type nausea/vomiting) |
| Monitoring Items | Full blood count with differential (CBC), lymphocyte subsets (CD3, CD4, CD8, CD19, CD56), CMV/EBV PCR (quantitative), renal function, liver function, thyroid function (long-term, for secondary autoimmunity), donor chimerism post-transplant |
| Handling Protection | Standard biological/monoclonal antibody handling procedures; not classified as a hazardous cytotoxic agent — standard aseptic precautions apply |

---

## Safety Considerations

Detailed SmPC warnings and contraindications are not available in the current evidence pack (blocking data gap — EMA SmPC for Lemtrada/MabCampath should be retrieved prior to prescribing). Based on published literature and known pharmacology:

- **Infectious toxicity**: Profound and prolonged lymphopenia creates substantial risk for opportunistic infections including CMV reactivation, EBV-driven post-transplant lymphoproliferative disease, *Pneumocystis jirovecii* pneumonia, and invasive fungal infections; antimicrobial, antiviral, and antifungal prophylaxis is mandatory (PMID 15590388)
- **EBV-driven lymphoproliferation**: Documented following alemtuzumab-induced immunodepletion; requires vigilant EBV PCR monitoring post-infusion (PMID 18502831)
- **Secondary autoimmunity**: Well-documented after alemtuzumab in MS (immune thrombocytopenic purpura, autoimmune thyroid disease, anti-GBM nephropathy); relevance in the HSCT conditioning context requires monitoring for a minimum of 48 months post-infusion

Please refer to the approved Summary of Product Characteristics (SmPC) for Lemtrada and MabCampath for complete, current safety information before initiating treatment.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Alemtuzumab has a mechanistically sound and clinically documented role as a reduced-intensity conditioning agent in allo-HSCT for combined immunodeficiency, with a consistent evidence base across multiple Phase 1/2 trials and multicenter retrospective cohorts in paediatric populations where standard myeloablative conditioning carries unacceptable toxicity. The absence of Phase 3 RCT data reflects disease rarity rather than a fundamental evidence deficiency.

**To proceed, the following is needed:**

- **Mandatory — blocking**: Retrieve complete SmPC safety data (warnings, contraindications, drug interactions) for Lemtrada/MabCampath from the EMA or Lægemiddelstyrelsen before formal safety evaluation can be completed
- **High priority**: Obtain mechanism of action documentation from DrugBank (currently missing; affects mechanistic link analysis)
- **Regulatory**: Apply for individual patient authorisation from Lægemiddelstyrelsen (named-patient basis), as alemtuzumab has no registered indication for immunodeficiency in Denmark
- **Clinical**: Referral to a specialist paediatric haematology/immunology transplant centre for case-by-case assessment
- **Precision**: Define the specific combined immunodeficiency subtype (SCID, CGD, XIAP, Hyper-IgM, IPEX, WAS, etc.) as conditioning intensity, donor selection, and risk-benefit profiles differ substantially across subtypes
- **Safety protocol**: Establish pre-transplant infectious disease risk assessment and full prophylaxis protocol (CMV, EBV, PCP, invasive fungal) prior to conditioning initiation
- **Monitoring plan**: Post-transplant immune reconstitution monitoring (lymphocyte subsets, donor chimerism) and long-term surveillance for secondary autoimmunity (minimum 48-month follow-up)

> **Note on hepatic infarction (TxGNN rank 1, score 94.44%)**: Although this indication received the numerically highest prediction score, it carries no clinical trial or literature support (Evidence Level L5). The high score likely reflects indirect topological connectivity in the knowledge graph (shared transplant complication nodes) rather than a direct causal pharmacological pathway. There is no known biological bridge between CD52-targeted lymphocyte depletion and vascular occlusive hepatic disease. **Recommendation: Hold** — no further evaluation warranted without new mechanistic evidence.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

