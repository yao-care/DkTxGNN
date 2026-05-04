---
layout: default
title: Ertapenem
parent: 僅模型預測 (L5)
nav_order: 174
evidence_level: L5
indication_count: 10
---

# Ertapenem
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

# Ertapenem: From Broad-Spectrum Bacterial Infections to Staphylococcus aureus Infection

## One-Sentence Summary

Ertapenem is a broad-spectrum carbapenem antibiotic approved internationally for complicated intra-abdominal, skin, urinary tract, and pelvic infections, as well as community-acquired pneumonia and diabetic foot infections. The TxGNN model predicts it may be effective for **Staphylococcus aureus infection** (particularly persistent MSSA bacteremia in combination therapy), with **8 clinical trials** and **20 publications** currently supporting this direction. A secondary prediction for **bacterial arthritis** (TxGNN score 99.72%) is also mechanistically plausible but has weaker clinical evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Complicated bacterial infections (intra-abdominal, skin/skin structure, urinary tract, pneumonia, diabetic foot) |
| Predicted New Indication | Staphylococcus aureus infection (persistent MSSA bacteremia, combination therapy) |
| TxGNN Prediction Score | 99.28% |
| Evidence Level | L2 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Proceed with Guardrails |

> **Note on additional predictions:** Bacterial arthritis was the highest-scored TxGNN prediction (99.72%) but with L4 evidence only. Predictions for hyperamylasemia, polyclonal hyperviscosity syndrome, and congenital analbuminemia were flagged as knowledge graph artefacts (adverse reaction or pharmacokinetic property misclassified as therapeutic relationships) and are placed on **Hold**.

---

## Why is This Prediction Reasonable?

Ertapenem is a 1-β-methyl carbapenem antibiotic that exerts its bactericidal effect by binding to penicillin-binding proteins (PBPs), particularly PBP2 and PBP3, thereby inhibiting bacterial cell wall synthesis. It is stable against most β-lactamases including extended-spectrum β-lactamases (ESBLs) and has a uniquely long half-life (~4 hours) that permits once-daily dosing — a characteristic that distinguishes it from other carbapenems and makes it well-suited for outpatient parenteral antibiotic therapy (OPAT).

While ertapenem alone has only moderate intrinsic activity against methicillin-susceptible *Staphylococcus aureus* (MSSA), a compelling body of evidence has emerged since 2016 demonstrating that the combination of **cefazolin plus ertapenem** produces synergistic bactericidal activity against persistent MSSA bacteremia. The mechanistic basis is complementary PBP targeting: ertapenem preferentially binds PBP1a/1b while cefazolin binds PBP2/3, resulting in dual blockade of cell wall synthesis at different enzymatic steps. Additionally, ertapenem has been shown to stimulate interleukin-1β release from monocytes, potentially enhancing the innate immune response against *S. aureus*.

This is not a classic "drug repurposing" scenario but rather an indication extension through combination therapy. The strong mechanistic rationale, supported by in vitro synergy studies, animal models of endocarditis, clinical case series showing rapid bacteremia clearance, and now multiple prospective clinical trials, makes this one of the most well-supported predictions in this evaluation.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04886284](https://clinicaltrials.gov/study/NCT04886284) | Phase 2 | Recruiting | 60 | **CERT trial**: Directly evaluates cefazolin + ertapenem combination for MSSA bacteremia. Sub-study of the SNAP adaptive platform trial (NCT05137119). First RCT for this combination. |
| [NCT07376889](https://clinicaltrials.gov/study/NCT07376889) | Phase 4 | Not yet recruiting | 2,096 | **COMBAT-SAB**: Large multicentre trial evaluating combination antibiotic therapy vs monotherapy for S. aureus bacteremia. Planned completion 2029. |
| [NCT07148960](https://clinicaltrials.gov/study/NCT07148960) | Phase 4 | Enrolling by invitation | 300 | **SABEDTIO**: Pragmatic RCT comparing early dual IV antibiotic therapy vs single-agent therapy for S. aureus bacteremia. Aims to decrease bacteremia duration to <6 days. |
| [NCT00366249](https://clinicaltrials.gov/study/NCT00366249) | Phase 3 | Completed | 1,061 | Tigecycline vs ertapenem for diabetic foot infections. Co-primary efficacy endpoints were not met (for tigecycline). Provides large-scale safety data for ertapenem. |

> **Note:** 4 additional registered trials (NCT06634940, NCT06174649, NCT03218397, NCT06044272) address antimicrobial resistance surveillance or diagnostic methodology and provide epidemiological context but are not directly therapeutic.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15164963](https://pubmed.ncbi.nlm.nih.gov/15164963/) | 2004 | RCT (subgroup) | Int J Antimicrob Agents | Ertapenem vs piperacillin-tazobactam for MSSA complicated skin infections: comparable cure rates in 185 patients with MSSA |
| [38946294](https://pubmed.ncbi.nlm.nih.gov/38946294/) | 2024 | Retrospective cohort | J Antimicrob Chemother | Carbapenem combination therapy vs standard of care for persistent MSSA bacteremia — first comparative effectiveness data |
| [40448546](https://pubmed.ncbi.nlm.nih.gov/40448546/) | 2025 | Retrospective cohort | J Antimicrob Chemother | Impact of hypoalbuminemia on ertapenem combination therapy for MSSA — faster blood culture sterilisation observed; caution in albumin <2.5 g/dL |
| [39230345](https://pubmed.ncbi.nlm.nih.gov/39230345/) | 2025 | Review | Am J Health-Syst Pharm | Comprehensive review of combination treatment options for persistent MSSA bacteremia including cefazolin + ertapenem |
| [31773134](https://pubmed.ncbi.nlm.nih.gov/31773134/) | 2020 | Case series | Clin Infect Dis | Cefazolin + ertapenem salvage therapy cleared 11 cases of persistent MSSA bacteremia (6 endocarditis); clearance ≤24h in 8 cases. Synergy confirmed in rat endocarditis model |
| [27572414](https://pubmed.ncbi.nlm.nih.gov/27572414/) | 2016 | Case series / in vitro | Antimicrob Agents Chemother | First report of cefazolin + ertapenem synergy clearing refractory MSSA bacteremia; confirmed in murine skin infection model |
| [34978891](https://pubmed.ncbi.nlm.nih.gov/34978891/) | 2022 | Mechanistic study | Antimicrob Agents Chemother | Cefazolin + ertapenem stimulates IL-1β release from monocytes — potential immunomodulatory mechanism explaining clinical efficacy |
| [35493130](https://pubmed.ncbi.nlm.nih.gov/35493130/) | 2022 | In vitro study | Open Forum Infect Dis | Ertapenem + cefazolin demonstrates potent activity within staphylococcal biofilms — relevant to endocarditis treatment |
| [39777519](https://pubmed.ncbi.nlm.nih.gov/39777519/) | 2025 | In vitro study | J Infect Dis | Adjunctive carbapenems (ertapenem or meropenem) enhance efficacy of ceftaroline or vancomycin against MRSA — extends the combination concept |
| [16801442](https://pubmed.ncbi.nlm.nih.gov/16801442/) | 2006 | In vitro / in vivo | Antimicrob Agents Chemother | Linezolid + ertapenem shows high synergy against MRSA in rabbit endocarditis model |

---

## Denmark Market Information

Ertapenem currently holds **no marketing authorisations** in Denmark (neither national via Laegemiddelstyrelsen nor centralised via EMA for this specific product).

> **International context:** Ertapenem is marketed globally under the brand name **Invanz** (MSD/Merck) and holds marketing authorisations in many countries including the USA (FDA-approved 2001), EU member states, and others. It is available as a 1 g powder for solution for injection/infusion. Danish healthcare professionals may access ertapenem through special import procedures (*udleveringstilladelse*) if clinically indicated.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

> **Key pharmacological considerations from literature:**
> - **Protein binding:** Ertapenem is approximately 95% protein-bound (primarily to albumin). Patients with serum albumin <2.5 g/dL may experience altered pharmacokinetics and suboptimal drug exposures (PMID [40448546](https://pubmed.ncbi.nlm.nih.gov/40448546/)).
> - **Seizure risk:** As with all carbapenems, CNS adverse effects including seizures have been reported, particularly in patients with renal impairment or pre-existing CNS disorders.
> - **Once-daily dosing:** 1 g IV/IM once daily; no dose adjustment needed for hepatic impairment; renal dose adjustment required for CrCl ≤30 mL/min.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The use of ertapenem in combination with cefazolin (or oxacillin) for persistent MSSA bacteremia is supported by a coherent mechanistic rationale (complementary PBP binding and IL-1β immunomodulation), multiple clinical case series demonstrating rapid bacteremia clearance, retrospective comparative data, and now at least three prospective clinical trials including the CERT Phase 2 RCT (NCT04886284) and the large COMBAT-SAB trial (NCT07376889, n=2,096). This represents an indication extension with substantial and growing clinical evidence, not a speculative repurposing.

**To proceed, the following is needed:**
- **Regulatory pathway assessment:** Determine feasibility of obtaining ertapenem access in Denmark (special import, compassionate use, or EMA centralised authorisation)
- **Awaiting RCT results:** The CERT trial (NCT04886284, expected completion July 2026) will provide the first randomised evidence for cefazolin + ertapenem in MSSA bacteremia
- **Safety monitoring protocol:** Establish monitoring plan for protein binding–related issues (albumin levels), CNS adverse effects, and potential impact on carbapenem resistance patterns
- **Antimicrobial stewardship considerations:** Develop guidance to ensure ertapenem combination use is restricted to persistent MSSA bacteremia (≥72h despite appropriate therapy) to minimise resistance selection pressure
- **Danish clinical microbiology consultation:** Engage with local infectious disease specialists to assess local MSSA epidemiology and resistance patterns

---

*This report is for research purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before clinical application. Report generated 2026-04-05.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

