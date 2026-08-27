---
layout: default
title: Lanadelumab
parent: 僅模型預測 (L5)
nav_order: 254
evidence_level: L5
indication_count: 10
---

# Lanadelumab
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

# Lanadelumab: From Hereditary Angioedema to C1 Inhibitor Deficiency

## One-Sentence Summary

Lanadelumab (Takhzyro®) is a monoclonal antibody that inhibits plasma kallikrein; the clinical trial records in this evidence pack show it is an already-approved prophylactic treatment for hereditary angioedema (HAE) in multiple countries (e.g. Japan, China, South Korea), though no formal indication/MOA record for this drug exists in the current evidence pack and it currently holds no marketing authorisation in Denmark.
The TxGNN model's top prediction, **C1 Inhibitor Deficiency**, is the pathophysiological name for Type I/II HAE — i.e., essentially the same disease Lanadelumab is already used for elsewhere.
This is supported by **22 clinical trials** and **20 publications**, but should be read as a *confirmation* of an existing global indication rather than a novel repurposing signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hereditary Angioedema (HAE) — inferred from clinical trial evidence in this pack; no formal indication/MOA record is on file for this drug |
| Predicted New Indication | C1 Inhibitor Deficiency (clinically synonymous with HAE Type I/II) |
| TxGNN Prediction Score | 99.996% |
| Evidence Level | L2 (1 completed Phase 3 RCT: HELP Study, NCT02586805) |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not formally on file for this drug in the evidence pack (original_moa: Data Gap). However, the literature evidence collected alongside the prediction (PMID 30267321) describes Lanadelumab as "a fully human monoclonal antibody that inhibits plasma kallikrein," developed to prevent hereditary angioedema (HAE) attacks caused by mutations in *SERPING1* leading to C1 inhibitor deficiency or dysfunction, which results in uncontrolled plasma kallikrein activity and excessive bradykinin production.

Importantly, "C1 Inhibitor Deficiency" — the TxGNN top prediction — is not a distinct new disease relative to HAE; it is the underlying biochemical classification of HAE Type I/II, the condition Lanadelumab was originally developed and is already approved for in multiple jurisdictions (trial records in this pack reference approval status in Japan, China, and South Korea). This means the model has essentially re-identified the drug's known indication rather than surfaced a genuine repurposing candidate. The predictive score is very high (99.996%) precisely because the drug–disease association is already well established in the underlying knowledge graph.

Three other TxGNN predictions in this evidence pack (serpinopathy with toxic serpin polymerization, pancreatitis, pseudo-von Willebrand disease, primary release disorder of platelets) scored highly but have no supporting clinical trials or literature and were scored L5/Hold — these are not discussed further here as they lack any evidentiary basis.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02586805](https://clinicaltrials.gov/study/NCT02586805) | Phase 3 | Completed | 125 | HELP Study — randomized, double-blind, placebo-controlled trial confirming efficacy/safety of Lanadelumab (DX-2930) for long-term HAE prophylaxis |
| [NCT02741596](https://clinicaltrials.gov/study/NCT02741596) | Phase 3 | Completed | 212 | HELP Study Extension — open-label long-term safety and efficacy follow-up |
| [NCT04070326](https://clinicaltrials.gov/study/NCT04070326) | Phase 3 | Completed | 21 | SPRING Study — safety, PK/PD in pediatric HAE patients 2 to <12 years |
| [NCT04180163](https://clinicaltrials.gov/study/NCT04180163) | Phase 3 | Completed | 12 | Efficacy and safety in Japanese HAE Type I/II patients |
| [NCT05460325](https://clinicaltrials.gov/study/NCT05460325) | Phase 3 | Completed | 20 | Safety, PK and efficacy in Chinese HAE patients over 26 weeks |
| [NCT04444895](https://clinicaltrials.gov/study/NCT04444895) | Phase 3 | Completed | 73 | Long-term safety/efficacy in non-histaminergic angioedema with normal C1-INH |
| [NCT04130191](https://clinicaltrials.gov/study/NCT04130191) | N/A | Completed | 140 | ENABLE — 3-year real-world effectiveness study |
| [NCT03845400](https://clinicaltrials.gov/study/NCT03845400) | N/A | Completed | 168 | EMPOWER — observational HAE attack-rate study, US/Canada |
| [NCT02093923](https://clinicaltrials.gov/study/NCT02093923) | Phase 1 | Completed | 38 | Multiple ascending dose safety/tolerability/PK study in HAE subjects |
| [NCT01923207](https://clinicaltrials.gov/study/NCT01923207) | Phase 1 | Completed | 32 | First-in-human single ascending dose safety/tolerability study in healthy subjects |

No EudraCT identifiers were present in the evidence pack.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30480729](https://pubmed.ncbi.nlm.nih.gov/30480729/) | 2018 | RCT | JAMA | Lanadelumab vs. placebo significantly reduces HAE attack rate (HELP Study primary publication) |
| [40434599](https://pubmed.ncbi.nlm.nih.gov/40434599/) | 2025 | Network Meta-Analysis | Drugs in R&D | Comparative efficacy/safety of Lanadelumab vs. garadacimab, C1-INH, berotralstat for HAE prophylaxis |
| [39508959](https://pubmed.ncbi.nlm.nih.gov/39508959/) | 2024 | Systematic Review | Clinical Reviews in Allergy & Immunology | Characterizes breakthrough attacks in HAE patients on long-term prophylaxis |
| [39836016](https://pubmed.ncbi.nlm.nih.gov/39836016/) | 2025 | Indirect Treatment Comparison | J Comp Eff Res | Compares Lanadelumab vs. C1-INH in pediatric HAE (<12 years) |
| [34287942](https://pubmed.ncbi.nlm.nih.gov/34287942/) | 2022 | Open-label Extension | Allergy | HELP OLE Study — long-term effectiveness and safety confirmed |
| [30267321](https://pubmed.ncbi.nlm.nih.gov/30267321/) | 2018 | Review | Drugs | "Lanadelumab: First Global Approval" — MOA and development summary |
| [32187470](https://pubmed.ncbi.nlm.nih.gov/32187470/) | 2020 | Review | NEJM | General review of hereditary angioedema pathophysiology and treatment |
| [30539362](https://pubmed.ncbi.nlm.nih.gov/30539362/) | 2019 | Review | BioDrugs | Preclinical and Phase I data review for Lanadelumab in C1-INH deficiency |
| [37898409](https://pubmed.ncbi.nlm.nih.gov/37898409/) | 2024 | Review | J Allergy Clin Immunol | Disease burden of HAE due to C1-inhibitor deficiency in Asia-Pacific |
| [39701274](https://pubmed.ncbi.nlm.nih.gov/39701274/) | 2025 | Observational | J Allergy Clin Immunol Pract | INTEGRATED multicountry real-world effectiveness study |

---

## Denmark Market Information

Lanadelumab currently holds **no marketing authorisation** in Denmark (0 licences on file; market status: not marketed). No national (Laegemiddelstyrelsen) or centralised (EMA) authorisation records are available in this evidence pack.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- A blocking data gap exists (DG001: no TFDA/SmPC warnings or contraindications on file), which prevents completion of the initial safety screening (S1) required before any recommendation to proceed. This holds even though the underlying indication is not novel — Lanadelumab is already an approved HAE therapy elsewhere, supported by one completed placebo-controlled Phase 3 RCT (L2) and substantial real-world evidence.

**To proceed, the following is needed:**
- Official SmPC / product label with warnings, precautions, and contraindications (source: TFDA or equivalent regulator)
- Formal mechanism-of-action (MOA) record from DrugBank or manufacturer labeling
- Drug-drug interaction (DDI) data (current query returned no results)
- If Danish market entry is being considered: a formal marketing authorisation application, since no licence currently exists in Denmark
- Clarification that "C1 Inhibitor Deficiency" reflects the drug's existing approved indication rather than a new repurposing target, to avoid mischaracterizing this as a novel finding
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

