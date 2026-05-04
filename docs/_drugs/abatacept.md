---
layout: default
title: Abatacept
parent: 僅模型預測 (L5)
nav_order: 11
evidence_level: L5
indication_count: 10
---

# Abatacept
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

# Drug Repurposing Evidence Report: Abatacept (DB01281)

**Candidate ID**: TW-DB01281-multi
**Report Version**: v4
**Date Generated**: 2026-04-03
**Data Cutoff**: 2026-04-03
**Prepared for**: Lægemiddelstyrelsen (Danish Medicines Agency) Context

---

## 1. Executive Summary

| Field | Detail |
|-------|--------|
| **Drug (INN)** | Abatacept |
| **DrugBank ID** | DB01281 |
| **Brand Name** | Orencia (Bristol-Myers Squibb) |
| **Number of Predicted Indications** | 5 (unique diseases) |
| **Highest Evidence Level Achieved** | **L1** — Inflammatory spondylopathy (psoriatic arthritis subtype) |
| **Top Recommendation** | **Proceed with Guardrails** (inflammatory spondylopathy / PsA) |

**Key Findings Summary:**

Abatacept, a selective T-cell co-stimulation modulator (CTLA-4-Ig fusion protein), was evaluated by the TxGNN knowledge graph model across five predicted disease indications. The analysis reveals a spectrum of evidence maturity:

1. **Inflammatory spondylopathy** (specifically the psoriatic arthritis [PsA] subtype): **L1 evidence** — supported by a completed Phase 3 RCT (NCT01860976, n=489), ACR/NPF 2018 guideline inclusion, and large-scale post-marketing safety data including a **Denmark-specific DANBIO registry study** (NCT05421442, n=38,396). Abatacept is already EMA/FDA-approved for PsA. **Recommendation: Proceed with Guardrails.**
2. **Ankylosing spondylitis (AS)**: **L2 evidence** — a Phase 2 open-label pilot (NCT00558506, n=30; PMID 21415053) demonstrated **limited efficacy**, consistent with a mechanistic mismatch (AS driven primarily by IL-17/IL-23 axis rather than T-cell co-stimulation). **Recommendation: Hold.**
3. **Rheumatoid vasculitis**: **L4 evidence** — case reports show **contradictory signals** (both therapeutic benefit and new-onset vasculitis during abatacept therapy). No clinical trials. **Recommendation: Research Question.**
4. **Hypermobility of coccyx**: **L5 evidence** — AI prediction only. No biological plausibility. **Recommendation: Hold.**
5. **Kümmell disease**: **L5 evidence** — AI prediction only. No biological plausibility. **Recommendation: Hold.**

> **Data Gaps Identified**: Lægemiddelstyrelsen product label warnings/contraindications and detailed mechanism of action data require supplementation from DrugBank API and the Danish product resume (produktresumé).

---

## 2. Drug Overview

### 2.1 Approved Indications

#### Denmark (Lægemiddelstyrelsen / EMA Centralised Authorisation)

Abatacept (Orencia) holds a centralised EMA marketing authorisation valid in Denmark for:

| Indication | Population | Route |
|------------|------------|-------|
| Rheumatoid arthritis (RA) | Adults with moderate-to-severe active RA with inadequate response to DMARDs including methotrexate or a TNF inhibitor | IV infusion / SC injection |
| Polyarticular juvenile idiopathic arthritis (pJIA) | Paediatric patients ≥2 years | IV / SC |
| Psoriatic arthritis (PsA) | Adults with active PsA with inadequate response to DMARDs | SC injection |

> **Note**: The evidence pack indicates Taiwan regulatory status as "未上市" (not marketed). In contrast, abatacept **is authorised and marketed in Denmark** under the EMA centralised procedure.

#### FDA (United States)

FDA-approved indications mirror EMA approvals: RA (adult), pJIA (≥2 years), PsA (adult), and additionally the prevention of acute graft-versus-host disease (aGVHD) in combination with a calcineurin inhibitor and methotrexate.

### 2.2 Mechanism of Action

Abatacept is a soluble fusion protein comprising the extracellular domain of human cytotoxic T-lymphocyte-associated antigen 4 (CTLA-4) linked to the modified Fc portion of human immunoglobulin G1 (IgG1). It acts as a selective co-stimulation modulator by:

1. **Binding CD80/CD86** on antigen-presenting cells (APCs), thereby blocking interaction with CD28 on T cells
2. **Inhibiting the "Signal 2" co-stimulatory pathway** required for full T-cell activation
3. **Preferentially suppressing naïve T-cell activation** while having a lesser effect on memory T cells
4. **Downstream reduction** of pro-inflammatory cytokines (TNF-α, IL-6, IL-2) and autoantibody production

> ⚠️ **Data Gap (DG002)**: Full MOA characterisation from DrugBank API was flagged as incomplete in the evidence pack. The above is reconstructed from published literature.

### 2.3 Pharmacokinetic Profile

| Parameter | IV Formulation | SC Formulation |
|-----------|---------------|----------------|
| **Bioavailability** | 100% (reference) | ~78.6% (SC vs IV) |
| **T_max** | End of infusion | ~7 days (SC) |
| **Half-life (t½)** | ~13 days (range 8–25 days) | ~14.3 days |
| **Steady-state** | By week 8 (with loading) | By week 12–13 |
| **Clearance** | ~0.22 mL/h/kg | Similar |
| **Volume of distribution (Vss)** | ~0.07 L/kg | — |
| **Dosing (IV)** | Weight-based: <60 kg: 500 mg; 60–100 kg: 750 mg; >100 kg: 1000 mg; Day 1, 15, 29, then q4w | — |
| **Dosing (SC)** | — | 125 mg weekly (with or without IV loading dose) |
| **Metabolism** | Proteolytic degradation (not CYP-mediated) | Same |
| **Immunogenicity** | Low anti-drug antibody formation (~2–3%) | Similar |

---

## 3. Evidence Analysis

### Overview: Predicted Indications Summary

| Rank | Disease | TxGNN Score | Evidence Level | Decision Stage | Recommendation |
|------|---------|-------------|---------------|----------------|----------------|
| 1 | Rheumatoid vasculitis | 0.999 | **L4** | S1 | Research Question |
| 2 | Ankylosing spondylitis | 0.999 | **L2** | S1 | Hold |
| 3 | Hypermobility of coccyx | 0.999 | **L5** | S0 | Hold |
| 4 | Inflammatory spondylopathy | 0.998 | **L1** | S3 | **Proceed with Guardrails** |
| 5 | Kümmell disease | 0.998 | **L5** | S0 | Hold |

---

### 3.1 Inflammatory Spondylopathy (Psoriatic Arthritis Subtype)

**Evidence Level: L1 | Decision Stage: S3 | Recommendation: Proceed with Guardrails**

This is the **strongest candidate** identified. Inflammatory spondylopathy encompasses psoriatic arthritis (PsA), for which abatacept is already approved globally. The evidence base is robust.

#### 3.1.1 Clinical Trials

| NCT ID | Title | Phase | Status | N | Key Finding |
|--------|-------|-------|--------|---|-------------|
| **NCT01860976** | Phase 3 RCT: Abatacept SC in Active PsA | **Phase 3** | **Completed** | 489 | Pivotal trial: abatacept SC vs placebo in PsA; primary endpoint met. Led to regulatory approval. |
| **NCT00534313** | Phase 2b RCT: Abatacept vs Placebo in PsA | Phase 2b | Terminated | 191 | Dose-finding study; established optimal dosing for PsA. |
| **NCT05421442** | Post-marketing safety: DANBIO Register (Denmark) | Post-marketing | **Completed** | **38,396** | **Denmark-specific**: nationwide post-marketing monitoring of abatacept in RA and PsA patients via DANBIO. |
| **NCT05413044** | Post-marketing safety: SRQ Register (Sweden) | Post-marketing | Completed | 140,706 | Swedish nationwide safety monitoring; malignancy incidence data. |
| **NCT03419143** | ALTEA: Real-world PsA (Germany) | Observational | Completed | 190 | Long-term real-world efficacy and safety in PsA. |
| **NCT04106804** | ABEPSA: Bone Biomarkers in PsA | Phase 4 | Unknown | 20 | Abatacept bone effects in PsA via MRI and biomarkers. |
| **NCT00558506** | Pilot: Abatacept in AS | Phase 2 | Unknown | 30 | Relevant to AS subtype only; limited efficacy reported. |
| **NCT05080218** | COVER: COVID-19 Vaccine Response | Phase 4 | Completed | 841 | Safety data on vaccine response in patients on abatacept. |

#### 3.1.2 Published Literature

**Tier 1 (Guidelines / Meta-analyses):**

- **PMID 30499246** — *ACR/NPF 2018 Guideline for the Treatment of PsA* (Arthritis & Rheumatology, 2019): Abatacept is included as a recommended biologic DMARD option for PsA patients with inadequate response to csDMARDs. This is a **clinical practice guideline** from the two leading professional bodies.
- **PMID 39992258** — *Abatacept and the risk of malignancy: a meta-analysis across disease indications* (Rheumatology, 2025): Cross-indication meta-analysis assessing malignancy risk; provides critical safety data relevant to long-term use in spondyloarthritis.

**Tier 2 (Systematic Reviews / Key Reviews):**

- **PMID 28612180** — Systematic review on immunogenicity of biologics across inflammatory diseases.
- **PMID 38331098** — Vaccination guidelines for patients on biologics including abatacept.
- **PMID 38499181** — Perioperative management guidelines for abatacept in PsA patients.
- **PMID 29737909** — Review of biological and clinical profiles of PsA responders to abatacept; notes differential efficacy across PsA domains (effective for peripheral arthritis, less so for axial disease and skin).
- **PMID 31171316** — Emerging treatment options for SpA; positions abatacept within the therapeutic landscape.
- **PMID 38639758** — Drug therapy in juvenile spondyloarthritis; reviews abatacept evidence in paediatric JSpA.

#### 3.1.3 Mechanistic Rationale

Inflammatory spondylopathy encompasses conditions driven by adaptive immune dysregulation, particularly PsA. Abatacept's inhibition of T-cell co-stimulation effectively modulates the adaptive immune response in PsA, particularly for peripheral joint manifestations. The ACR/NPF 2018 guidelines conditionally recommend abatacept for treatment-naïve PsA patients and those with inadequate response to TNF inhibitors.

**Important caveat**: Abatacept shows **limited efficacy for axial disease** within the spondyloarthritis spectrum. Its approval and guideline recommendations are restricted to peripheral PsA manifestations, not axial spondyloarthritis (including AS).

#### 3.1.4 Denmark-Specific Evidence

The **DANBIO registry study (NCT05421442)** is of particular relevance:
- **Design**: Nationwide post-marketing surveillance using the Danish DANBIO biologics register
- **Sample**: 38,396 participants with RA or PsA treated with abatacept
- **Status**: Completed (2019–2025)
- **Objective**: Expanded post-marketing monitoring of abatacept safety
- This study provides **real-world Danish population-level safety data**, directly applicable to Lægemiddelstyrelsen decision-making.

---

### 3.2 Ankylosing Spondylitis

**Evidence Level: L2 | Decision Stage: S1 | Recommendation: Hold**

#### 3.2.1 Clinical Trials

| NCT ID | Title | Phase | Status | N | Key Finding |
|--------|-------|-------|--------|---|-------------|
| **NCT00558506** | Pilot Open-Label: Abatacept in AS | Phase 2 | Unknown | 30 | **Core evidence**: 24-week open-label pilot demonstrated **limited efficacy** (PMID 21415053). |
| NCT04610476 | Phase 3 PsA Tapering RCT | Phase 3 | Unknown | 270 | PsA-focused; tangential to AS. |

#### 3.2.2 Published Literature

**Key Publication:**

- **PMID 21415053** — *Treatment of active ankylosing spondylitis with abatacept: an open-label, 24-week pilot study* (Song et al., Ann Rheum Dis, 2011): This is the **only direct clinical study** of abatacept in AS. Results showed **limited clinical efficacy**, with the majority of patients not achieving ASAS20 response. The study was not progressed to Phase 3.

**Supporting Reviews:**

- **PMID 27856659** — Sieper (Rheumatology, 2016): Explicitly states that "conventional DMARDs and also non-TNF-blocker biologics targeting IL-1, IL-6 and T cells (abatacept) **are not effective**" in axSpA.
- **PMID 22450391** — Kiltz et al. (Curr Opin Rheumatol, 2012): Reviews alternatives for TNF-refractory AS; abatacept assessed but found insufficiently effective.
- **PMID 19822066** — Braun & Kalden (Clin Exp Rheumatol, 2009): Discusses pathogenic differences between RA and AS that explain differential biologic responses.

#### 3.2.3 Mechanistic Rationale

AS is primarily driven by the HLA-B27/IL-17/IL-23 axis, with innate immunity playing a predominant role. T-cell co-stimulation blockade via abatacept does not effectively target this pathway. The clinical data (PMID 21415053) confirm this mechanistic mismatch. **This indication should not be pursued further.**

---

### 3.3 Rheumatoid Vasculitis

**Evidence Level: L4 | Decision Stage: S1 | Recommendation: Research Question**

#### 3.3.1 Clinical Trials

No clinical trials directly studying abatacept for rheumatoid vasculitis were identified. One tangentially related trial (NCT07138898, immunosuppressant management in shoulder arthroplasty) received relevance grade C.

#### 3.3.2 Published Literature

The evidence consists entirely of **case reports with contradictory signals**:

| PMID | Type | Year | Key Finding | Signal Direction |
|------|------|------|-------------|-----------------|
| **22124545** | Case Report | 2012 | 38-year-old woman with refractory RV: abatacept produced **rapid clinical improvement** after failure of steroids, plasmapheresis, and tocilizumab. | **Positive** ✅ |
| **29930884** | Case Report/Series | 2018 | Patient with RA + common variable immunodeficiency: abatacept used as alternative to rituximab for cutaneous RV. | **Positive** ✅ |
| **27052429** | Case Report | 2016 | **New onset** of rheumatoid vasculitis developed **during** abatacept therapy; subsequently improved with rituximab. | **Negative** ⚠️ |
| **30119075** | Case Report | 2018 | RA-associated orbital vasculitis presented **while on abatacept**. | **Negative** ⚠️ |
| **36418100** | Case Report | 2023 | ANCA-associated nephritis developed during abatacept + adalimumab therapy. | **Negative** ⚠️ |

#### 3.3.3 Mechanistic Rationale

Rheumatoid vasculitis (RV) is a severe extra-articular manifestation of RA involving T-cell-mediated vascular wall inflammation. Theoretically, abatacept's inhibition of T-cell co-stimulation could suppress the upstream autoimmune vascular inflammation. However, the published case reports present **contradictory evidence**:

- **In favour**: Cases of refractory RV responding to abatacept (PMID 22124545, 29930884)
- **Against**: Cases of new-onset vasculitis developing during abatacept therapy (PMID 27052429, 30119075)

This discordance suggests that the relationship between CTLA-4 pathway modulation and vasculitis is complex and possibly patient-subtype dependent.

---

### 3.4 Hypermobility of Coccyx

**Evidence Level: L5 | Decision Stage: S0 | Recommendation: Hold**

No clinical trials, no literature, no mechanistic plausibility. Coccygeal hypermobility is a mechanical/structural condition involving ligamentous laxity or joint instability. There is no immune-mediated component that would respond to T-cell co-stimulation blockade. The high TxGNN score (0.999) likely reflects **graph proximity artefact** within the musculoskeletal disease node neighbourhood. **This is considered a false positive.**

---

### 3.5 Kümmell Disease

**Evidence Level: L5 | Decision Stage: S0 | Recommendation: Hold**

No clinical trials, no literature, no mechanistic plausibility. Kümmell disease (delayed post-traumatic vertebral body collapse / avascular necrosis of the vertebral body) is a mechanical/vascular condition. There is no rational basis for immunomodulatory therapy. **This is considered a false positive.**

---

## 4. Safety Considerations

> ⚠️ **Data Gap (DG001)**: Product label warnings and contraindications from the Danish/EMA produktresumé were not available in the evidence pack. The following is based on the EMA Summary of Product Characteristics (SmPC) for Orencia and published literature.

### 4.1 Known Adverse Effects

**Common (≥1/100 to <1/10):**
- Upper respiratory tract infections (nasopharyngitis, sinusitis)
- Urinary tract infections
- Headache
- Nausea, diarrhoea
- Injection site reactions (SC formulation)
- Infusion-related reactions (IV formulation)

**Uncommon (≥1/1,000 to <1/100):**
- Herpes zoster
- Pneumonia
- Elevated transaminases

**Rare but Serious:**
- Serious infections (including sepsis, tuberculosis, opportunistic infections)
- Malignancy (meta-analysis PMID 39992258 found no significantly increased risk of malignancy excluding NMSC)
- Hypersensitivity/anaphylaxis
- Autoimmune phenomena (paradoxical vasculitis — see Section 3.3)

### 4.2 Drug Interactions

| Interaction | Severity | Detail |
|-------------|----------|--------|
| **Other biologics (TNF inhibitors, IL-6 inhibitors, rituximab)** | **Contraindicated** | Concurrent use increases serious infection risk without added efficacy |
| **Live vaccines** | **Contraindicated** | Live vaccines should not be administered concurrently or within 3 months of discontinuation |
| **Methotrexate** | Permitted | Commonly used in combination; no significant PK interaction |
| **Corticosteroids** | Permitted | No significant interaction; standard concomitant use |
| **Non-live vaccines** | Caution | Immune response may be attenuated; timing considerations apply (see PMID 38331098) |

> **Note**: DDI query returned 0 results from the evidence pack database (query status: not_found). The above is compiled from SmPC data and published guidelines.

### 4.3 Contraindications

Based on EMA SmPC:
- Hypersensitivity to abatacept or any excipient
- Severe and uncontrolled active infections (e.g., sepsis, opportunistic infections, active tuberculosis)
- Concurrent use with other biological DMARDs

### 4.4 Special Populations

| Population | Recommendation |
|------------|---------------|
| **Pregnancy** | Limited data; use only if clearly needed (PMID 40256995 — scoping review of DMARDs in pregnancy) |
| **Breastfeeding** | Abatacept detected in breast milk; risk-benefit assessment needed |
| **Tuberculosis screening** | Mandatory before initiation (PMID 39963138) |
| **Hepatitis B/C** | Screen before initiation |
| **Elderly** | No dose adjustment; increased infection vigilance |

### 4.5 Post-Marketing Safety Data (Denmark-Specific)

The **DANBIO registry study (NCT05421442)** provides large-scale Danish safety data:
- **38,396 participants** with RA or PsA in Denmark
- Monitoring period: 2019–2025 (completed)
- Focus: expanded post-marketing safety including malignancy, infections, and cardiovascular events

The complementary **Swedish SRQ registry study (NCT05413044)** enrolled 140,706 participants, providing additional Nordic real-world safety benchmarking.

---

## 5. Regulatory Status

### 5.1 Denmark (Lægemiddelstyrelsen)

| Parameter | Status |
|-----------|--------|
| **Product Name** | Orencia |
| **Marketing Authorisation** | **Authorised** (EMA centralised procedure, valid in Denmark) |
| **Approved Indications** | RA (adult), PsA (adult), pJIA (≥2 years) |
| **Formulations** | IV infusion (lyophilised powder 250 mg); SC injection (125 mg/mL prefilled syringe/pen) |
| **DANBIO Registry** | Active; abatacept included in national biologics monitoring |
| **Post-marketing study** | NCT05421442 completed (n=38,396) |

### 5.2 EMA Status

| Parameter | Detail |
|-----------|--------|
| **First Authorisation** | 2007 (RA) |
| **PsA Extension** | 2017 |
| **Current SmPC Version** | Regularly updated |
| **PASS Requirements** | Ongoing post-authorisation safety studies (including NCT05421442, NCT05413044) |

### 5.3 FDA Status

| Parameter | Detail |
|-----------|--------|
| **First Approval** | 2005 (RA) |
| **PsA Approval** | 2017 |
| **aGVHD Prevention** | 2021 (unique to FDA, not EMA-approved for this) |
| **Formulations** | IV and SC (same as EMA) |

### 5.4 Regulatory Status Summary for Predicted Indications

| Predicted Indication | Denmark/EMA | FDA | Status |
|---------------------|-------------|-----|--------|
| Inflammatory spondylopathy (PsA subtype) | **Approved** | **Approved** | Already authorised |
| Ankylosing spondylitis | Not approved | Not approved | Phase 2 failed; unlikely to progress |
| Rheumatoid vasculitis | Not approved | Not approved | Case reports only |
| Hypermobility of coccyx | Not approved | Not approved | No evidence |
| Kümmell disease | Not approved | Not approved | No evidence |

---

## 6. Conclusion and Recommendations

### 6.1 Overall Assessment

| Indication | Evidence Level | Verdict | Actionability |
|------------|---------------|---------|---------------|
| **Inflammatory spondylopathy (PsA)** | L1 | ✅ Already approved | No repurposing needed; ensure full utilisation in Danish clinical practice |
| **Ankylosing spondylitis** | L2 | ❌ Negative evidence | Do not pursue; mechanistic mismatch confirmed clinically |
| **Rheumatoid vasculitis** | L4 | ⚠️ Contradictory signals | Academic research interest only; no clinical pathway justified |
| **Hypermobility of coccyx** | L5 | ❌ False positive | Discard; no biological plausibility |
| **Kümmell disease** | L5 | ❌ False positive | Discard; no biological plausibility |

### 6.2 Evidence Gaps

| Gap ID | Item | Severity | Recommended Remediation |
|--------|------|----------|------------------------|
| DG001 | Lægemiddelstyrelsen produktresumé warnings/contraindications | Blocking | Download and parse the Danish-language SmPC from Lægemiddelstyrelsen/EMA product database |
| DG002 | Detailed MOA data from DrugBank | High | Query DrugBank API for complete target/enzyme/transporter profiles |
| — | Route compatibility assessment | Medium | Cross-reference available Danish formulations with required administration routes for each indication |
| — | Disease mapping completeness | Low | Several literature items have "pending" classification; complete relevance grading |
| — | Duplicate entries in evidence pack | Low | Ranks 1/2, 3/4, 5/6, 7/8, 9/10 appear duplicated; deduplicate in future pipeline runs |

### 6.3 Suggested Next Steps

#### For Inflammatory Spondylopathy (PsA):
1. **No repurposing action required** — abatacept is already EMA-authorised for PsA and available in Denmark
2. **Leverage DANBIO data** (NCT05421442) to inform Lægemiddelstyrelsen post-marketing surveillance reporting
3. Consider a **utilisation study** via DANBIO to assess real-world uptake and treatment sequencing of abatacept in Danish PsA patients

#### For Rheumatoid Vasculitis:
1. **Formulate as research question** for academic investigation
2. Conduct a **systematic review of all published cases** of abatacept use in RV (both therapeutic and paradoxical)
3. Consider a **national case series** via Danish rheumatology centres to identify any off-label use patterns
4. **Do not recommend clinical use** outside of a formal research protocol given contradictory safety signals

#### For Ankylosing Spondylitis:
1. **No further action** — negative Phase 2 data and mechanistic mismatch
2. Archive evidence for reference

#### For Hypermobility of Coccyx and Kümmell Disease:
1. **Flag as TxGNN false positives** for model calibration
2. These likely represent knowledge graph node proximity artefacts in the musculoskeletal disease cluster

### 6.4 Pipeline Quality Notes

The evidence pack contained **duplicate entries** (ranks 1/2, 3/4, 5/6, 7/8, 9/10 are identical disease pairs). This should be addressed in the data pipeline to prevent inflated candidate counts. After deduplication, there are **5 unique predicted indications** rather than 10.

---

## Appendix A: Data Sources Queried

| Source | Queries Run | Results Found |
|--------|-------------|---------------|
| DrugBank | 1 | 1 (drug profile) |
| ClinicalTrials.gov | 10 | 32 trials (across all indications) |
| ICTRP | 10 | 0 |
| PubMed | 10 | 97 publications (across all indications) |
| DDI Database | 1 | 0 (not found) |

## Appendix B: Key References

1. Song I-H et al. Treatment of active ankylosing spondylitis with abatacept: an open-label, 24-week pilot study. *Ann Rheum Dis*. 2011;70(6):1108-1110. PMID: 21415053
2. Singh JA et al. 2018 ACR/NPF Guideline for the Treatment of Psoriatic Arthritis. *Arthritis Rheumatol*. 2019;71(1):5-32. PMID: 30499246
3. Zuckerman BP et al. Abatacept and the risk of malignancy: a meta-analysis across disease indications. *Rheumatology*. 2025. PMID: 39992258
4. Fujii W et al. The rapid efficacy of abatacept in a patient with rheumatoid vasculitis. *Mod Rheumatol*. 2012;22(3):440-443. PMID: 22124545
5. Carvajal Alegria G et al. New onset of rheumatoid vasculitis during abatacept therapy. *Joint Bone Spine*. 2016;83(5):589-590. PMID: 27052429
6. Al Attar L, Shaver T. Abatacept as a Therapeutic Option for Rheumatoid Vasculitis. *Cureus*. 2018;10(6):e2793. PMID: 29930884
7. Zizzo G et al. Abatacept in the treatment of psoriatic arthritis: biological and clinical profiles of the responders. *Immunotherapy*. 2018;10(6):465-478. PMID: 29737909
8. Sieper J. New treatment targets for axial spondyloarthritis. *Rheumatology*. 2016;55(suppl_2):ii38-ii42. PMID: 27856659

---

> **Disclaimer**: This report is generated for **research purposes only** and does not constitute medical advice. All drug repurposing candidates require **clinical validation** before therapeutic application. Drug repurposing predictions are based on computational models (TxGNN knowledge graph) and require independent verification. Always consult healthcare professionals and the current Lægemiddelstyrelsen-approved produktresumé before making treatment decisions.
>
> *Report generated: 2026-04-03 | Data cutoff: 2026-04-03 | Pipeline version: v4*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

