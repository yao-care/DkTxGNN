---
layout: default
title: Emicizumab
parent: 僅模型預測 (L5)
nav_order: 161
evidence_level: L5
indication_count: 10
---

# Emicizumab
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

# Emicizumab: From Congenital Haemophilia A to Acquired Coagulation Factor Deficiency

## One-Sentence Summary

Emicizumab is a humanised bispecific monoclonal antibody that substitutes for activated Factor VIII (FVIIIa) by bridging FIXa and FX in the intrinsic coagulation pathway, globally approved for prophylaxis in congenital Haemophilia A with and without inhibitors.
The TxGNN model's highest-scoring predictions cover platelet-type bleeding disorders (pseudo-von Willebrand disease, 99.99%), but the most clinically actionable and mechanistically grounded predicted indication is **Acquired Coagulation Factor Deficiency** (Acquired Haemophilia A, AHA), supported by **2 prospective Phase 2/3 studies** and **19 publications**.
Note: Emicizumab is not registered in the Danish national medicines database, although the EMA centralised authorisation (Hemlibra, EU/1/18/1271) is valid across all EU/EEA member states including Denmark.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Congenital Haemophilia A prophylaxis (globally approved; absent from Danish national database) |
| Highest TxGNN-Scored Prediction | Pseudo-von Willebrand disease (99.99%) — no supporting evidence (L5, Hold) |
| Most Evidence-Supported Prediction | Acquired Coagulation Factor Deficiency / Acquired Haemophilia A (TxGNN score 99.90%) |
| Evidence Level | L2 — Phase 2 and Phase 3 prospective studies (acquired coagulation factor deficiency) |
| Denmark Market Status | Not marketed (national database) |
| Number of Marketing Authorisations | 0 (national) |
| Recommended Decision | **Proceed with Guardrails** (acquired coagulation factor deficiency) / **Hold** (platelet-type bleeding disorders) |

---

## Why is This Prediction Reasonable?

Emicizumab acts by simultaneously binding FIXa and FX, physically replacing the cofactor role of FVIIIa within the intrinsic tenase complex. This mechanism is entirely independent of whether FVIII protein is absent due to a genetic mutation or neutralised by circulating autoantibodies. Consequently, the transition from congenital to acquired FVIII deficiency represents a direct mechanistic extension rather than a speculative repurposing leap.

Acquired Haemophilia A arises when the immune system generates inhibitory autoantibodies against FVIII, producing the same downstream coagulation failure as severe congenital Haemophilia A — loss of effective FVIIIa cofactor activity. The approved bypass rationale used for recombinant activated Factor VIIa (rFVIIa, NovoSeven) in AHA applies equally to emicizumab, with the additional advantage of subcutaneous dosing and a longer half-life enabling prophylactic rather than purely on-demand use. Multiple prospective studies have now tested this logic: the Phase 2 GTH-AHA-EMI trial (*Lancet Haematology*, 2023) and the Phase 3 AGEHA study (Japan, *J Thromb Haemost* 2023/2025) both demonstrate that emicizumab prevents bleeds in AHA and enables deferral of immunosuppressive therapy, which is the major source of treatment-related mortality in this predominantly elderly, frail population.

**Why the TxGNN top predictions (platelet disorders) are deprioritised here**: The model assigns its highest scores to pseudo-von Willebrand disease, primary release disorder of platelets, Glanzmann thrombasthenia, and Scott syndrome — all bleeding disorders with phenotypic overlap in the knowledge graph. However, emicizumab targets the coagulation cascade, not platelet function, and lacks direct biological rationale for pure platelet disorders. Glanzmann thrombasthenia (GT) is a partial exception: in refractory GT patients with anti-GPIIb/IIIa antibodies, a bypass haemostasis strategy analogous to rFVIIa may theoretically apply. However, no dedicated emicizumab clinical data for GT exist, placing this at L4. All other platelet-type predictions remain Hold (L5).

---

## Clinical Trial Evidence

The Phase 2 (GTH-AHA-EMI) and Phase 3 (AGEHA) prospective interventional trials of emicizumab in Acquired Haemophilia A have been completed; their results appear in the Literature Evidence section below. The trial registered in this evidence pack is an ongoing observational registry.

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT04398628](https://clinicaltrials.gov/study/NCT04398628) | N/A (Observational) | Recruiting | 3,000 | ATHN Transcends: US natural history registry collecting long-term safety and real-world effectiveness data on emicizumab and novel therapies across non-neoplastic haematologic disorders (haemophilia, platelet disorders). Does not provide comparative efficacy data for AHA specifically; serves as a source of real-world utilisation patterns. |

---

## Literature Evidence

The following publications concern Emicizumab in **Acquired Haemophilia A (AHA)**, the principal clinical entity within the predicted indication of acquired coagulation factor deficiency.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39134043](https://pubmed.ncbi.nlm.nih.gov/39134043/) | 2025 | Phase 3 study (AGEHA final) | Thrombosis and Haemostasis | AGEHA Phase 3 final analysis: emicizumab (6 mg/kg SC loading, then maintenance) showed favourable benefit-risk in all AHA patients including those ineligible for immunosuppressive therapy (Cohort 2); long-term prophylaxis sustained. |
| [37858328](https://pubmed.ncbi.nlm.nih.gov/37858328/) | 2023 | Phase 2 study (GTH-AHA-EMI) | The Lancet Haematology | Open-label, single-arm, multicentre Phase 2 study: emicizumab protected AHA patients from bleeding and allowed deferral of immunosuppression during the first 12 weeks — potentially reducing IST-associated infections and mortality. |
| [40795229](https://pubmed.ncbi.nlm.nih.gov/40795229/) | 2025 | 2-year follow-up | Blood Advances | GTH-AHA-EMI 2-year follow-up: sustained survival benefit demonstrated; postponing IST alongside emicizumab reduced deaths from severe infection compared with historical IST-first approaches. |
| [36696195](https://pubmed.ncbi.nlm.nih.gov/36696195/) | 2023 | Phase 3 study (AGEHA primary) | J Thrombosis and Haemostasis | AGEHA primary analysis: prospective, multicentre, open-label Phase 3 study in Japanese AHA patients; emicizumab prophylaxis feasible regardless of inhibitor titre. |
| [38049124](https://pubmed.ncbi.nlm.nih.gov/38049124/) | 2024 | Consensus recommendations | Hamostaseologie | GTH-AHA Working Group consensus on emicizumab in AHA: practical guidance on prophylaxis initiation, immunosuppression timing strategy, dose, and laboratory monitoring. |
| [39361769](https://pubmed.ncbi.nlm.nih.gov/39361769/) | 2024 | Real-world cohort | Blood Advances | Retrospective multicenter US cohort (62 AHA patients, 12 haemophilia treatment centres): off-label emicizumab for median 10 weeks; confirms real-world effectiveness aligned with trial data. |
| [38936699](https://pubmed.ncbi.nlm.nih.gov/38936699/) | 2024 | Comparative analysis | J Thrombosis and Haemostasis | Emicizumab versus early immunosuppressive therapy in AHA: emicizumab reduces need for aggressive early IST, with implications for management protocols in frail patients. |
| [39536818](https://pubmed.ncbi.nlm.nih.gov/39536818/) | 2025 | Narrative review | J Thrombosis and Haemostasis | Comprehensive review of AHA management in the emicizumab era: covers epidemiology, pathophysiology, diagnosis, hemostatic management, and integration of emicizumab into current practice. |
| [40683780](https://pubmed.ncbi.nlm.nih.gov/40683780/) | 2025 | Review | Blood Reviews | Current trends in AHA management; highlights underestimation of AHA in patients on antithrombotic therapy and the diagnostic and therapeutic role of emicizumab. |
| [37391649](https://pubmed.ncbi.nlm.nih.gov/37391649/) | 2024 | Review | Annals of Hematology | rFVIIa (NovoSeven) in haemophilia and rare bleeding disorders including GT: contextualises the bypass haemostasis rationale relevant to both rFVIIa and emicizumab across multiple coagulation and platelet disorders. |

---

## Denmark Market Information

Emicizumab has **0 national marketing authorisations** listed in the Danish medicines database, and its market status is recorded as not marketed in the national registry included in this evidence pack.

However, Hemlibra (emicizumab) received EMA centralised marketing authorisation (EU/1/18/1271) in November 2018 for congenital Haemophilia A with inhibitors, subsequently extended to patients without inhibitors. This authorisation is valid in Denmark. Clinicians should verify current reimbursement status and access pathways through:
- **Lægemiddelstyrelsen** (Danish Medicines Agency): [www.laegemiddelstyrelsen.dk](https://www.laegemiddelstyrelsen.dk)
- **EMA product page**: EU/1/18/1271

Use in Acquired Haemophilia A remains off-label in most jurisdictions, including Denmark, and requires specialist haematology oversight and appropriate compassionate use or named-patient authorisation as applicable.

---

## Safety Considerations

Formal safety data (warnings, contraindications, drug-drug interactions) were not available in this evidence pack. Please refer to the approved Hemlibra Summary of Product Characteristics (SmPC) available from the EMA for complete safety information.

Based on published clinical literature, the following safety signals are clinically important:

- **Thrombotic microangiopathy (TMA) and thromboembolism**: Reported in congenital Haemophilia A patients receiving emicizumab concurrently with activated prothrombin complex concentrate (aPCC/FEIBA). Concurrent use of bypassing agents — particularly aPCC — must be avoided or undertaken with extreme caution under specialist guidance.
- **Coagulation assay interference**: Emicizumab prolongs APTT-based clotting assays even in the presence of residual or recovering FVIII activity, complicating standard monitoring of FVIII inhibitor titres in AHA. Chromogenic assays with bovine reagents are recommended for FVIII monitoring.
- **Immunosuppression interaction**: When combined with IST in AHA, careful monitoring for infectious complications is required, particularly in elderly patients.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Emicizumab's FIXa-FX bridging mechanism is a direct functional substitute for FVIII cofactor activity, making it mechanistically applicable to Acquired Haemophilia A regardless of FVIII inhibitor titre. This is supported by a completed Phase 2 study (GTH-AHA-EMI, *Lancet Haematology* 2023) and a Phase 3 study (AGEHA, 2023–2025) showing bleed prevention and a survival benefit from deferred immunosuppression — a clinically meaningful outcome in a high-mortality rare disease. For platelet-type bleeding disorders (pseudo-vWD, primary release disorder, Glanzmann thrombasthenia, Scott syndrome), the biological rationale is weak or absent and a Hold recommendation applies.

**To proceed, the following is needed:**

- **Regulatory and access confirmation**: Verify Hemlibra (EU/1/18/1271) reimbursement status and named-patient access pathway in Denmark for the off-label AHA indication via Lægemiddelstyrelsen
- **Safety documentation**: Obtain the current approved Hemlibra SmPC for full contraindications, drug interactions, dose guidance, and monitoring requirements in AHA (note: dosing in AHA may differ from approved congenital HA dosing)
- **Specialist pathway**: Establish a haematology-led multidisciplinary team approach; immunosuppressive therapy remains necessary in AHA for inhibitor eradication and must be co-managed alongside emicizumab prophylaxis
- **Laboratory setup**: Confirm availability of chromogenic bovine Factor X assays for emicizumab monitoring and FVIII inhibitor quantification in the treating institution
- **Clinical protocol**: Review the GTH-AHA Working Group consensus recommendations (PMID 38049124) for practical clinical implementation, particularly regarding timing of IST initiation and duration of emicizumab prophylaxis
- **Glanzmann thrombasthenia (conditional)**: If emicizumab is considered for refractory GT with inhibitors to platelet transfusion, a formal case-by-case ethical and clinical review is required; no controlled data exist and this would constitute highly experimental off-label use

> **Disclaimer**: This report is intended for research and clinical decision support purposes only. It does not constitute medical advice. Predicted repurposing candidates require clinical validation before therapeutic application. All treatment decisions must be made by qualified healthcare professionals in compliance with applicable regulations.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

