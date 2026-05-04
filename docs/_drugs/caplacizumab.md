---
layout: default
title: Caplacizumab
parent: 僅模型預測 (L5)
nav_order: 88
evidence_level: L5
indication_count: 10
---

# Caplacizumab
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

# Caplacizumab: From Acquired Thrombotic Thrombocytopenic Purpura to Thrombotic Thrombocytopenic Purpura

---

## One-Sentence Summary

Caplacizumab is an anti-von Willebrand factor nanobody that is internationally approved (EMA, FDA) for the treatment of acquired immune-mediated thrombotic thrombocytopenic purpura (iTTP/aTTP), yet is currently not recorded as marketed in Denmark.
The TxGNN model predicts it as highly relevant for **Thrombotic Thrombocytopenic Purpura** (TxGNN score: 99.9965%), confirming its established therapeutic target — and this prediction is supported by **14 registered clinical trials** (including three completed Phase 3 studies) and **20 publications**, among them the pivotal HERCULES and TITAN Phase 3/2 RCTs published in *The New England Journal of Medicine*.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not recorded in Danish regulatory dataset (internationally approved for acquired/immune-mediated TTP) |
| Predicted New Indication | Thrombotic Thrombocytopenic Purpura (TTP) |
| TxGNN Prediction Score | 99.9965% |
| Evidence Level | L1 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 (Danish regulatory registry) |
| Recommended Decision | Proceed with Guardrails |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on published information, caplacizumab is a humanised, bivalent variable-domain-only immunoglobulin fragment (nanobody) that specifically targets the **A1 domain of von Willebrand factor (vWF)**. Its efficacy in immune-mediated TTP has been demonstrated in two pivotal randomised controlled trials, and its direct mechanistic alignment with TTP pathology is one of the clearest target-disease matches in modern hematology.

In iTTP, a severe autoantibody-mediated deficiency of the ADAMTS13 protease leads to accumulation of ultra-large vWF multimers (UL-vWF) in the circulation. These UL-vWF multimers bind to the GPIb receptor on platelets, triggering widespread platelet aggregation and microvascular thrombosis — causing microangiopathic haemolytic anaemia, severe thrombocytopenia, and ischaemic end-organ injury (brain, kidneys, heart) with historically >90% untreated mortality. Caplacizumab directly blocks the UL-vWF A1 domain–platelet GPIb interaction, interrupting this thrombotic cycle rapidly and within days while plasma exchange and immunosuppression work to restore ADAMTS13 activity.

The TxGNN model assigns high prediction scores across several rare platelet disorders for caplacizumab (see Multi-Indication Overview below), which is consistent with the drug's mechanistic influence on the vWF–GPIb adhesion axis broadly shared among these conditions. However, only TTP has direct mechanistic alignment (★★★★★) and clinical evidence at the L1 level. Notably, pseudo-von Willebrand disease (platelet-type vWD, rank 3) shares a closely related pathological GPIb–vWF interaction and merits further research attention (★★★★☆), while the remaining high-scoring predictions reflect likely graph-proximity artefacts rather than genuine mechanistic overlap.

---

## Multi-Indication Overview

The TxGNN model identified five unique platelet-disorder indications for caplacizumab. The following table summarises each prediction (duplicate rank entries have been de-duplicated):

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Recommendation | Mechanistic Relevance |
|------|---------------------|------------|----------------|----------------|-----------------------|
| 1 | Primary release disorder of platelets | 99.9998% | L5 | Hold | ★☆☆☆☆ — Dense granule secretion defect; no overlap with vWF–GPIb adhesion pathway. Likely graph proximity artefact. |
| 3 | Pseudo-von Willebrand disease | 99.9998% | L4 | Research Question | ★★★★☆ — Gain-of-function GPIb mutation causes pathological GPIb–vWF binding; caplacizumab's vWF A1 blockade directly addresses this mechanism. |
| 5 | Glanzmann thrombasthenia | 99.9997% | L5 | Hold | ★☆☆☆☆ — GPIIb/IIIa (αIIbβ3 integrin) aggregation defect; entirely different target from vWF A1–GPIb pathway. |
| 7 | Scott syndrome | 99.9975% | L5 | Hold | ★☆☆☆☆ — TMEM16F (Anoctamin-6) mutation; phosphatidylserine externalisation defect unrelated to vWF–GPIb axis. |
| **9** | **Thrombotic thrombocytopenic purpura** | **99.9965%** | **L1** | **Proceed with Guardrails** | **★★★★★ — Direct on-target mechanism; three completed Phase 3 studies; international guidelines endorse caplacizumab as standard of care.** |

---

## Clinical Trial Evidence (Thrombotic Thrombocytopenic Purpura)

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|-----------|-------------|
| [NCT02553317](https://clinicaltrials.gov/study/NCT02553317) | Phase 3 | Completed | 145 | HERCULES pivotal trial: double-blind, placebo-controlled RCT. Caplacizumab + plasma exchange + immunosuppression significantly reduced time to platelet normalisation, composite TTP events (death, recurrence, major thromboembolism), and exacerbation rate vs placebo. Formed the regulatory basis for EMA and FDA approval. |
| [NCT02878603](https://clinicaltrials.gov/study/NCT02878603) | Phase 3 | Completed | 104 | Post-HERCULES: prospective long-term follow-up of HERCULES completers, evaluating safety and efficacy of repeated caplacizumab use over multi-year observation. Provides long-term outcome data strengthening L1 classification. |
| [NCT05468320](https://clinicaltrials.gov/study/NCT05468320) | Phase 3 | Completed | 51 | Phase 3 single-arm open-label study evaluating caplacizumab + immunosuppressive therapy **without** first-line therapeutic plasma exchange (TPE) in iTTP adults. Completed December 2024; results expand evidence base for TPE-sparing regimens. |
| [NCT01151423](https://clinicaltrials.gov/study/NCT01151423) | Phase 2 | Completed | 75 | TITAN: Phase 2 single-blind, placebo-controlled RCT. First randomised study establishing the efficacy and safety of anti-vWF nanobody as adjunct to plasma exchange in aTTP. |
| [NCT04985318](https://clinicaltrials.gov/study/NCT04985318) | N/A | Recruiting | 350 | REACT-2020: Large German national prospective multi-centre real-world study describing prescription practices, confirming real-world efficacy, and identifying predictors of persistent autoimmune activity and complications. Estimated completion 2034. |
| [NCT04720261](https://clinicaltrials.gov/study/NCT04720261) | Phase 2 | Terminated | 58 | Phase 2 non-inferiority study of personalised caplacizumab dosing guided by ADAMTS13 activity monitoring. Terminated for reasons unrelated to safety; provides exploratory data on treatment-duration optimisation strategies. |
| [NCT04074187](https://clinicaltrials.gov/study/NCT04074187) | Phase 2/3 | Completed | 21 | Open-label Phase 2/3 study in Japanese aTTP patients. Evaluated prevention of TTP recurrence, platelet count restoration, and composite aTTP-related outcomes in an Asian population. |
| [NCT06291025](https://clinicaltrials.gov/study/NCT06291025) | N/A | Recruiting | 131 | Multicentre non-inferiority study evaluating caplacizumab + immunosuppression + plasma infusion without TPE in iTTP. Recruiting; anticipated completion August 2026. Results may further redefine first-line management standards. |
| [NCT05876221](https://clinicaltrials.gov/study/NCT05876221) | N/A | Completed | 223 | Observational study of platelet count dynamics under caplacizumab. Demonstrates rapid normalisation within 3–4 days and highlights the decoupling of platelet counts from ADAMTS13 activity as a potential monitoring pitfall for over- and undertreatment decisions. |
| [NCT07205861](https://clinicaltrials.gov/study/NCT07205861) | N/A | Recruiting | 1,200 | TWI-LIGHT: Large French retrospective epidemiological study of iTTP patients in the national TMA registry. Provides disease burden and real-world treatment pattern data. Anticipated completion December 2028. |

---

## Literature Evidence (Thrombotic Thrombocytopenic Purpura)

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [30625070](https://pubmed.ncbi.nlm.nih.gov/30625070/) | 2019 | RCT (HERCULES Phase 3) | N Engl J Med | Caplacizumab added to standard therapy significantly reduced time to platelet count response, composite TTP-related event rate, and exacerbation rate; established caplacizumab as standard of care for aTTP. |
| [26863353](https://pubmed.ncbi.nlm.nih.gov/26863353/) | 2016 | RCT (TITAN Phase 2) | N Engl J Med | First Phase 2 randomised trial of caplacizumab as adjunctive therapy in aTTP; demonstrated faster platelet recovery and trend toward reduction in recurrence vs placebo. |
| [40533296](https://pubmed.ncbi.nlm.nih.gov/40533296/) | 2025 | Clinical Guidelines (Update) | J Thromb Haemost | 2025 focused update of the ISTH 2020 iTTP/cTTP management guidelines; integrates new evidence on treatment optimisation, monitoring, and management of congenital TTP. |
| [32914526](https://pubmed.ncbi.nlm.nih.gov/32914526/) | 2020 | Clinical Guidelines | J Thromb Haemost | ISTH 2020 treatment guidelines for TTP; formally includes caplacizumab as part of recommended triple therapy (plasma exchange + immunosuppression + caplacizumab) for iTTP. |
| [32914582](https://pubmed.ncbi.nlm.nih.gov/32914582/) | 2020 | Clinical Guidelines | J Thromb Haemost | ISTH 2020 diagnostic guidelines for TTP; standardises ADAMTS13 activity-based diagnosis criteria and patient stratification approach. |
| [40388146](https://pubmed.ncbi.nlm.nih.gov/40388146/) | 2025 | Systematic Review | JAMA | Comprehensive JAMA review of iTTP covering epidemiology (2–6 cases/million/year worldwide), pathophysiology, diagnostic approach, and current treatment including the role of caplacizumab. |
| [37045600](https://pubmed.ncbi.nlm.nih.gov/37045600/) | 2023 | Systematic Review & Meta-analysis | Expert Rev Hematol | Meta-analysis of caplacizumab efficacy and safety in iTTP across multiple studies; confirms reduction in recurrence, composite events, and disease-related mortality. |
| [40235949](https://pubmed.ncbi.nlm.nih.gov/40235949/) | 2025 | Multicentre Cohort Study | EClinicalMedicine | Capla 1000+ international retrospective cohort (>1,000 iTTP patients); addresses the effect of caplacizumab on mortality and identifies optimal timing of initiation. |
| [33540569](https://pubmed.ncbi.nlm.nih.gov/33540569/) | 2021 | Review | J Clin Med | Comprehensive review of TTP pathophysiology, diagnosis, and the evolving management paradigm including caplacizumab and ADAMTS13-guided treatment strategies. |
| [36890095](https://pubmed.ncbi.nlm.nih.gov/36890095/) | 2023 | Review | Transfus Apher Sci | Review of individualised TTP management in the caplacizumab era; discusses ADAMTS13-guided treatment duration, stopping criteria, and long-term disease monitoring. |

---

## Denmark Market Information

Caplacizumab is currently recorded as **not marketed in Denmark**, with **no marketing authorisations** registered in the Danish regulatory dataset.

> **Note for healthcare professionals**: Caplacizumab is marketed internationally as Cablivi® (Sanofi/Ablynx) and holds a centralised marketing authorisation from the European Medicines Agency (EMA), which in principle covers all EU/EEA member states including Denmark. The absence of records in this dataset may reflect a gap in national marketing, pricing/reimbursement, or data capture of centralised EMA authorisations. Healthcare professionals are advised to verify the current access and reimbursement status directly with the **Danish Medicines Agency (Lægemiddelstyrelsen)** and the **EMA product register** before drawing conclusions about availability.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

> No drug–drug interactions were identified in the structured interaction database search conducted on 10 March 2026.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Caplacizumab has the strongest possible mechanistic alignment with iTTP (★★★★★) and the highest clinical evidence level (L1), supported by multiple completed Phase 3 RCTs, a growing real-world evidence base across thousands of patients, and incorporation into international clinical guidelines (ISTH 2020, updated 2025). The drug already holds EMA marketing authorisation. However, Danish regulatory records show no active marketing authorisation or reimbursement pathway in Denmark, formal safety documentation is unavailable in this dataset, and there are specific monitoring considerations (bleeding risk, ADAMTS13-guided treatment duration) that require structured clinical safeguards.

**To proceed, the following is needed:**

- **Market access verification**: Confirm EMA centralised authorisation status and current commercial/reimbursement availability of Cablivi® in Denmark through Lægemiddelstyrelsen and the manufacturer (Sanofi)
- **Safety documentation**: Obtain and review the full SmPC for bleeding risk management, contraindications, special population data (pregnancy, renal/hepatic impairment, paediatric use), and administration guidance
- **Reimbursement assessment**: Engage with the Danish Medicines Council (Medicinrådet) regarding an iTTP orphan drug reimbursement application given the drug's high unit cost and ultra-rare disease context
- **MOA documentation**: Resolve data gap DG002 (mechanism of action) by querying DrugBank API for internal records completeness
- **Pseudo-vWD follow-up**: The rank 3 prediction for pseudo-von Willebrand disease (platelet-type vWD) merits academic investigation given strong mechanistic plausibility (★★★★☆) and no currently registered clinical trials — consider proposing a prospective case series or registry study

---

*This report is generated for research reference purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before therapeutic application. All website content should include a YMYL disclaimer.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

