---
layout: default
title: Ustekinumab
parent: 僅模型預測 (L5)
nav_order: 462
evidence_level: L5
indication_count: 10
---

# Ustekinumab
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

# Ustekinumab: From Psoriasis/Crohn's Disease to Dermatitis (Atopic Dermatitis)

## One-Sentence Summary

Ustekinumab (Stelara) is a human monoclonal antibody originally developed for plaque psoriasis, psoriatic arthritis, Crohn's disease and ulcerative colitis. The TxGNN model predicts it may also be effective for **dermatitis**, most concretely **atopic dermatitis**, with **7 clinical trials** and **20 publications** currently identified in this evidence pack. The drug is not currently marketed in Denmark, and key safety documentation (SmPC warnings/contraindications) is still missing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in Danish licensing data (no marketing authorisations on file); internationally approved for plaque psoriasis, psoriatic arthritis, Crohn's disease and ulcerative colitis (per literature, PMID 36208443) |
| Predicted New Indication | Dermatitis (evidence concentrated on atopic dermatitis) |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L2 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available from the Danish regulatory record or DrugBank extract used to build this pack (flagged as a High-severity data gap). Based on literature evidence in this pack (PMID 27304428), ustekinumab is a fully human IgG1 monoclonal antibody that binds the shared p40 subunit of interleukin-12 (IL-12) and interleukin-23 (IL-23), blocking downstream Th1, Th17 and Th22 pathway activation. This mechanism underlies its approved efficacy in psoriasis, psoriatic arthritis, Crohn's disease and ulcerative colitis — all conditions with a strong Th17-driven inflammatory component.

Atopic dermatitis and psoriasis are both chronic inflammatory skin diseases, and there is biological plausibility for cross-over efficacy: several publications in this pack (PMID 29164954, PMID 29098604) note that Th17/Th22 activity contributes to atopic dermatitis pathology alongside the classically dominant Th2 axis, providing a rationale for IL-12/23 blockade.

However, this rationale is not as strong as for the approved indications. Real-world and systematic-review evidence in this pack (PMID 33849369, PMID 33074565) reports inconsistent results for ustekinumab in atopic dermatitis, reflecting that AD is more heterogeneous and Th2-dominant than psoriasis. The mechanistic link should therefore be regarded as plausible but not yet firmly established.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01945086](https://clinicaltrials.gov/study/NCT01945086) | Phase 2 | Completed | 79 | Randomized, double-blind, placebo-controlled trial of ustekinumab in Japanese adults with severe atopic dermatitis |
| [NCT01806662](https://clinicaltrials.gov/study/NCT01806662) | Phase 2 | Completed | 32 | Pilot RCT of ustekinumab in chronic atopic dermatitis with sub-optimal response to prior therapy |
| [NCT05535738](https://clinicaltrials.gov/study/NCT05535738) | Phase 2/3 | Recruiting | 45 | Suction-blistering model comparing biologic anti-inflammatory therapies in skin inflammation |
| [NCT02074982](https://clinicaltrials.gov/study/NCT02074982) | Phase 3 | Completed | 676 | CLEAR trial: secukinumab vs. ustekinumab in moderate-to-severe plaque psoriasis (not atopic dermatitis; included under broader "dermatitis" tag) |
| [NCT07352566](https://clinicaltrials.gov/study/NCT07352566) | Phase 4 | Not yet recruiting | 10 | Microdevice testing FDA-approved atopic dermatitis/psoriasis drugs directly in skin |
| [NCT07041112](https://clinicaltrials.gov/study/NCT07041112) | N/A | Completed | 1000 | Pharmacogenetic observational study of 10-year survival of biologic therapies in cutaneous psoriasis |
| [NCT01356758](https://clinicaltrials.gov/study/NCT01356758) | N/A | Completed | 126 | Cardiovascular risk assessment in severe psoriasis patients treated with biologic agents |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27304428](https://pubmed.ncbi.nlm.nih.gov/27304428/) | 2017 | RCT (Phase 2) | Experimental Dermatology | Ustekinumab (IL-12/IL-23p40 antagonist) assessed for efficacy/safety in moderate-to-severe atopic dermatitis, n=33 |
| [28338223](https://pubmed.ncbi.nlm.nih.gov/28338223/) | 2017 | RCT (Phase 2) | British Journal of Dermatology | Randomized, double-blind, placebo-controlled study of ustekinumab in Japanese patients with severe atopic dermatitis |
| [33074565](https://pubmed.ncbi.nlm.nih.gov/33074565/) | 2021 | Systematic Review/Meta-analysis | Allergy | EAACI evidence appraisal of systemic treatments (including ustekinumab) for moderate-to-severe atopic dermatitis |
| [29098604](https://pubmed.ncbi.nlm.nih.gov/29098604/) | 2018 | Systematic Review/Meta-analysis | American Journal of Clinical Dermatology | Evaluates whether biologics, including ustekinumab, are efficacious in atopic dermatitis |
| [29164954](https://pubmed.ncbi.nlm.nih.gov/29164954/) | 2018 | Systematic Review | Journal of Dermatological Treatment | Systematic review of ustekinumab specifically in atopic dermatitis treatment |
| [36208443](https://pubmed.ncbi.nlm.nih.gov/36208443/) | 2022 | Review | Dermatologic Therapy | Synthesizes off-label uses of ustekinumab beyond its approved indications |
| [33849369](https://pubmed.ncbi.nlm.nih.gov/33849369/) | 2022 | Observational (Real-world) | Journal of Dermatological Treatment | Real-world evidence on effectiveness of ustekinumab in atopic dermatitis; reports mixed/conflicting results |
| [39987634](https://pubmed.ncbi.nlm.nih.gov/39987634/) | 2025 | Observational (Pharmacovigilance) | International Immunopharmacology | FAERS-based real-world safety analysis of ustekinumab in psoriasis/psoriatic arthritis |
| [39201826](https://pubmed.ncbi.nlm.nih.gov/39201826/) | 2024 | Narrative Review | Children (Basel) | Reviews biologics/small molecules, including ustekinumab, for pediatric AD, psoriasis, alopecia areata and HS |
| [35130397](https://pubmed.ncbi.nlm.nih.gov/35130397/) | 2021 | Review | Dermatology Online Journal | Reviews off-label uses of TNF-α and IL-12/23 inhibitors (including ustekinumab) in dermatology |

---

## Denmark Market Information

Ustekinumab currently has no recorded marketing authorisation in the Danish regulatory dataset used for this evaluation (0 licenses, market status: Not marketed). No national (Laegemiddelstyrelsen) or centralised (EMA) authorisation details are available in this evidence pack.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information. Key warnings, contraindications, and drug-drug interaction data are not currently available in this evidence pack — this is flagged as a **Blocking** data gap (DG001), meaning a formal safety pre-assessment cannot proceed until the SmPC/label is obtained from the source regulatory agency.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- Efficacy evidence for the dermatitis/atopic dermatitis indication is limited to two completed Phase 2 RCTs with mixed real-world results (L2), not yet at the strength typically required to offset the current safety data gap.
- A Blocking-severity data gap (DG001: missing warnings/contraindications) prevents safety pre-assessment, and the drug has no existing marketing authorisation in Denmark to anchor a regulatory pathway.

**To proceed, the following is needed:**
- Danish/EU-approved SmPC (warnings, contraindications, DDI) to resolve DG001
- Confirmed mechanism-of-action documentation from DrugBank/regulatory source to resolve DG002
- Additional Phase 3 RCT data specific to atopic dermatitis (or a defined dermatitis subtype) to raise evidence level beyond L2
- Clarification of which specific "dermatitis" subtype is intended, given TxGNN's score covers a broad disease label while most direct trial evidence pertains specifically to atopic dermatitis
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

