---
layout: default
title: Icatibant
parent: 僅模型預測 (L5)
nav_order: 220
evidence_level: L5
indication_count: 10
---

# Icatibant
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

Using the drug-repurposing evaluation report template to produce a structured report from the supplied Evidence Pack for Icatibant.

---

# Icatibant: From Hereditary Angioedema (Established Use) to C1 Inhibitor Deficiency (TxGNN-Confirmed Indication)

## One-Sentence Summary

Icatibant (DrugBank DB06196) is a synthetic bradykinin B2-receptor antagonist whose clinical use profile in the evidence pack is entirely built around **C1 inhibitor deficiency** (i.e., Hereditary Angioedema, HAE) — the TxGNN model assigns this indication a near-maximal prediction score, and the evidence base is unusually strong, with **23 clinical trials** (including three completed Phase 3 RCTs) and **20 publications** supporting it. Note: because this evidence pack does not record a documented "original indication" or MOA for the drug, this indication in practice appears to be Icatibant's own well-established primary use rather than a genuinely novel repurposing target — the high score reflects model confirmation, not discovery.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (no approved indication text available; see note below) |
| Predicted New Indication | C1 Inhibitor Deficiency (Hereditary Angioedema) |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L1 |
| Denmark Market Status | Not marketed (未上市) |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data is not available as a discrete field in this evidence pack (original_moa = data gap). However, the literature gathered alongside the prediction consistently describes Icatibant as a **synthetic decapeptide, selective bradykinin B2-receptor antagonist** (see PMID 21284353, PMID 24925394). Hereditary Angioedema due to C1 inhibitor deficiency (C1-INH-HAE) arises when insufficient functional C1 esterase inhibitor allows uncontrolled activation of the plasma kallikrein-kinin cascade, leading to excess bradykinin generation and the recurrent subcutaneous/submucosal swelling attacks characteristic of the disease.

Because Icatibant directly blocks the bradykinin B2 receptor — the final common effector of the pathway that C1 inhibitor deficiency dysregulates — its pharmacology maps directly onto the disease mechanism rather than requiring an indirect or speculative link. This is reflected in the evidence: unlike the model's other predicted indications for Icatibant in this pack (serpinopathy, pseudo-von Willebrand disease, platelet release disorders, immune-mediated necrotizing myopathy — all scored L5/Hold with no supporting trials or literature), C1 inhibitor deficiency is backed by decades of dedicated randomized trials, national/regional registries, and real-world outcome studies.

The practical implication is that this is likely not a "new" repurposing opportunity in the traditional sense, but rather TxGNN correctly re-identifying Icatibant's core, already-established indication (marketed elsewhere as Firazyr®). This should be read as a validation signal for the model's ranking behavior on this drug, while the true "hold" points for Denmark relate to local regulatory/market status and a blocking safety data gap (see below), not to mechanistic plausibility.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00097695](https://clinicaltrials.gov/study/NCT00097695) | Phase 3 | Completed | 84 | Pivotal RCT (FAST-1): icatibant vs. placebo for acute cutaneous/abdominal HAE attacks |
| [NCT00912093](https://clinicaltrials.gov/study/NCT00912093) | Phase 3 | Completed | 98 | Pivotal RCT (FAST-3): icatibant vs. placebo, subcutaneous injection for acute HAE attacks |
| [NCT00500656](https://clinicaltrials.gov/study/NCT00500656) | Phase 3 | Completed | 85 | Pivotal RCT (FAST-2): icatibant vs. oral tranexamic acid for acute HAE attacks |
| [NCT00997204](https://clinicaltrials.gov/study/NCT00997204) | Phase 3 | Completed | 151 | Open-label study of self-administered subcutaneous icatibant — safety, tolerability, convenience |
| [NCT01457430](https://clinicaltrials.gov/study/NCT01457430) | Phase 4 | Completed | 19 | Self-administered icatibant for acute HAE attacks (IHA study) |
| [NCT01034969](https://clinicaltrials.gov/study/NCT01034969) | N/A | Completed | 1761 | Icatibant Outcome Survey (IOS) — large international post-marketing safety registry |
| [NCT01386658](https://clinicaltrials.gov/study/NCT01386658) | Phase 3 | Completed | 32 | Pediatric/adolescent PK, tolerability, and safety of a single subcutaneous dose |
| [NCT03888755](https://clinicaltrials.gov/study/NCT03888755) | Phase 3 | Completed | 8 | Efficacy, PK, and safety of icatibant in Japanese patients with acute HAE attacks |
| [NCT04654351](https://clinicaltrials.gov/study/NCT04654351) | Phase 3 | Completed | 2 | Safety, efficacy, and PK of icatibant in Japanese children/adolescents |
| [NCT07290855](https://clinicaltrials.gov/study/NCT07290855) | Phase 4 | Completed | 5 | Real-world safety/efficacy of icatibant injection (Icanticure®) for bradykinin-induced angioedema |

*(14 additional completed/withdrawn trials were identified in the evidence pack but are omitted here per the 10-trial display limit.)*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37898409](https://pubmed.ncbi.nlm.nih.gov/37898409/) | 2024 | Review | J Allergy Clin Immunol | Reviews the burden of C1-INH deficiency HAE in the Asia-Pacific region and treatment access gaps |
| [35662289](https://pubmed.ncbi.nlm.nih.gov/35662289/) | 2022 | Registry/Observational | Clin Exp Allergy | Registry analysis of icatibant vs. C1-inhibitor use for laryngeal HAE attacks |
| [37146882](https://pubmed.ncbi.nlm.nih.gov/37146882/) | 2023 | Observational | J Allergy Clin Immunol Pract | National UK survey of HAE and acquired C1 inhibitor deficiency demographics |
| [35871284](https://pubmed.ncbi.nlm.nih.gov/35871284/) | 2023 | Retrospective/Observational | J Clin Pharmacol | Retrospective review of off-label icatibant/C1-INH prescribing patterns |
| [34965883](https://pubmed.ncbi.nlm.nih.gov/34965883/) | 2021 | Registry/Observational | Allergy Asthma Clin Immunol | Icatibant Outcome Survey (Spain) — disease characteristics and treatment outcomes |
| [29757016](https://pubmed.ncbi.nlm.nih.gov/29757016/) | 2018 | Review | Expert Rev Clin Immunol | Review of icatibant use in adolescents/children over age 2 with C1-INH-HAE |
| [30280305](https://pubmed.ncbi.nlm.nih.gov/30280305/) | 2018 | Case report | J Clin Immunol | Case series on icatibant and recombinant C1 inhibitor use during pregnancy |
| [23420425](https://pubmed.ncbi.nlm.nih.gov/23420425/) | 2013 | Systematic Review | Pneumonol Alergol Pol | Systematic review comparing conestat alfa, C1-INH, and icatibant for acute attacks |
| [22686628](https://pubmed.ncbi.nlm.nih.gov/22686628/) | 2012 | Observational | Allergy | Real-world observational study of icatibant in acquired C1-inhibitor deficiency |
| [21284353](https://pubmed.ncbi.nlm.nih.gov/21284353/) | 2010 | Review | Prescrire International | Independent drug review of icatibant's role vs. C1 esterase inhibitor for HAE attacks |

*(10 additional publications were identified in the evidence pack but are omitted here per the 10-item display limit.)*

---

## Denmark Market Information

No marketing authorisation records are currently available for Icatibant in this evidence pack — market status is recorded as **"未上市" (Not marketed)** with **0** total licenses. This is notable given that Icatibant (Firazyr®) holds an EMA centralised marketing authorisation and is used across much of the EU for HAE; this discrepancy should be verified against the Danish Medicines Agency (Lægemiddelstyrelsen) register directly, as it may reflect a data collection gap rather than true unavailability.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information. No key warnings, contraindications, or drug-drug interaction data were available in this evidence pack (DDI query status: not found).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- Clinical evidence for Icatibant in C1 inhibitor deficiency (HAE) is exceptionally strong (Evidence Level L1, three completed Phase 3 RCTs plus a 1,761-patient international outcome registry), and the mechanistic link is direct and well-established.
- However, a **Blocking**-severity data gap (DG001: missing TFDA/SmPC-equivalent warnings and contraindications) currently prevents completion of the mandatory S1 safety initial assessment, and Denmark market status shows zero marketing authorisations on record. Until basic safety labelling is available and the Danish market/registration status is confirmed, this candidate cannot advance past Hold regardless of efficacy strength.

**To proceed, the following is needed:**
- Danish/EMA product label (SmPC) to resolve DG001 (warnings, contraindications) and confirm true Denmark market/registration status (the "not marketed" flag appears inconsistent with Icatibant's known EU centralised authorisation and should be re-verified).
- Confirmed mechanism-of-action documentation from DrugBank (DG002) to formally support the mechanistic rationale summarized above.
- Drug-drug interaction data, currently unavailable (query returned "not_found").
- Clarification of whether this evaluation is intended to assess a genuinely *new* indication or to support market entry/registration in Denmark for Icatibant's already-established indication — since the "predicted" indication and the drug's real-world primary use appear to be the same condition.

*Note: TxGNN also flagged four other candidate indications for Icatibant (serpinopathy with toxic serpin polymerization, pseudo-von Willebrand disease, primary platelet release disorder, immune-mediated necrotizing myopathy), each rated L5/Hold with no supporting trials or literature and only speculative mechanistic rationale. These are not considered actionable at this time.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

