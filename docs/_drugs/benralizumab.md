---
layout: default
title: Benralizumab
parent: 僅模型預測 (L5)
nav_order: 60
evidence_level: L5
indication_count: 10
---

# Benralizumab
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

# Benralizumab: From Severe Eosinophilic Asthma to Dermatitis

## One-Sentence Summary

Benralizumab (Fasenra) is an anti-IL-5 receptor alpha monoclonal antibody internationally approved for the add-on treatment of severe eosinophilic asthma; it currently holds no marketing authorisation with the Danish Medicines Agency (Laegemiddelstyrelsen).
The TxGNN model predicts it may be effective for **Dermatitis** (specifically atopic dermatitis), with **6 clinical trials** and **20 publications** currently supporting this research direction.
However, the pivotal Phase 2 HILLIER randomised controlled trial was terminated early owing to a lack of clinical efficacy in moderate-to-severe atopic dermatitis, which substantially limits the translational value of this prediction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Severe eosinophilic asthma (international approval; not marketed in Denmark) |
| Predicted New Indication | Dermatitis (atopic dermatitis) |
| TxGNN Prediction Score | 99.16% |
| Evidence Level | L2 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Benralizumab is a humanised, afucosylated monoclonal antibody that targets the alpha subunit of the IL-5 receptor (IL-5Rα). By blocking IL-5 signalling and simultaneously engaging enhanced antibody-dependent cell-mediated cytotoxicity (ADCC), the drug achieves near-complete depletion of circulating and tissue eosinophils and basophils. This eosinophil-depleting mechanism underpins its established efficacy in severe eosinophilic asthma. Formal mechanistic data from DrugBank are not yet available in this evidence pack; the description above is based on published pharmacological literature. Note: the JSON evidence pack flags mechanism of action (MOA) as a high-severity data gap (DG002) that should be resolved via a DrugBank API query before a full mechanistic analysis is conducted.

Atopic dermatitis (AD) is a chronic Type 2 inflammatory skin disease characterised by impaired skin barrier function, intense pruritus, and immune dysregulation. Eosinophils are prominently elevated in AD skin lesions and contribute to tissue damage, cytokine release, and itch amplification. This tissue eosinophilia provided an apparently reasonable mechanistic rationale — depleting eosinophils might reduce skin inflammation — and explains why the TxGNN knowledge graph assigned a high prediction score, given the proximity of eosinophil-mediated immunoregulation nodes shared between asthma and AD.

In practice, however, the clinical hypothesis was not confirmed. The Phase 2 HILLIER trial (NCT04605094, n=194) was terminated early after benralizumab failed to demonstrate meaningful improvement in established AD endpoints versus placebo. Subsequent mechanistic studies confirmed that benralizumab does successfully deplete IL-5Rα-bearing eosinophils in AD skin lesions (target engagement is achieved), yet this does not translate into clinical benefit. Current evidence suggests that IL-4 and IL-13 — rather than IL-5 — are the dominant type 2 cytokines driving keratinocyte dysfunction and itch in AD, which is why dupilumab (anti-IL-4Rα) succeeds where anti-IL-5Rα therapy does not.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT04605094](https://clinicaltrials.gov/study/NCT04605094) | Phase 2 | Terminated | 194 | HILLIER study: multinational, randomised, double-blind, placebo-controlled 16-week trial with 36-week extension comparing benralizumab vs. placebo in moderate-to-severe AD despite topical treatment. Terminated early due to lack of efficacy. |
| [NCT03563066](https://clinicaltrials.gov/study/NCT03563066) | Phase 2 | Completed | 20 | Mechanistic investigation of benralizumab in AD: assessed effects on eosinophils, basophils, and innate lymphoid type 2 (ILC2) cells in blood and skin lesions of AD patients. |
| [NCT06734884](https://clinicaltrials.gov/study/NCT06734884) | Phase 2 | Not yet recruiting | 96 | Efficacy and safety of benralizumab in Drug Reaction with Eosinophilia and Systemic Symptoms (DRESS) — a severe cutaneous drug hypersensitivity reaction with prominent eosinophil involvement. Estimated completion: September 2029. |
| [NCT06477653](https://clinicaltrials.gov/study/NCT06477653) | Phase 2 | Recruiting | 30 | Pilot study of dupilumab as add-on therapy in hypereosinophilic syndrome (HES) after partial response to eosinophil-depleting biologics including benralizumab. Provides context on the limits of single-pathway eosinophil depletion. |
| [NCT04763447](https://clinicaltrials.gov/study/NCT04763447) | Phase 4 | Recruiting | 234 | Omalizumab withdrawal trial in well-controlled severe allergic asthma with atopic comorbidities; provides context on biologic sequencing strategies in type 2 inflammatory disease. |
| [NCT04126499](https://clinicaltrials.gov/study/NCT04126499) | Observational | Completed | 28 | Retrospective observational study of benralizumab in severe eosinophilic asthma (Spanish individualised access programme); real-world demographic and safety data relevant to tolerability profiling. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [37178404](https://pubmed.ncbi.nlm.nih.gov/37178404/) | 2023 | RCT | J Eur Acad Dermatol Venereol | HILLIER Phase 2 RCT: benralizumab showed no significant improvement in signs or symptoms of moderate-to-severe AD versus placebo. Key negative evidence. |
| [38695680](https://pubmed.ncbi.nlm.nih.gov/38695680/) | 2024 | Plain language summary | Immunotherapy | Accessible summary of the HILLIER trial confirming the lack of benralizumab efficacy in moderate-to-severe AD across all assessed endpoints. |
| [40781582](https://pubmed.ncbi.nlm.nih.gov/40781582/) | 2025 | Mechanistic study | Clin Transl Allergy | Benralizumab successfully depletes IL-5Rα-bearing eosinophils in AD skin lesions, confirming biological target engagement despite absent clinical benefit. |
| [39234416](https://pubmed.ncbi.nlm.nih.gov/39234416/) | 2024 | Clinical study | J Allergy Clin Immunol: Global | Benralizumab reduces eosinophil-mediated skin inflammation after intradermal allergen challenge in AD patients; supports mechanistic role of eosinophils in allergen response. |
| [31690400](https://pubmed.ncbi.nlm.nih.gov/31690400/) | 2019 | Review | Allergy Asthma Proc | Comprehensive review of immunobiologics (anti-IgE, anti-IL-5, anti-IL-4/13) for severe asthma, AD, and chronic urticaria; contextualises benralizumab's positioning in type 2 disease. |
| [36270814](https://pubmed.ncbi.nlm.nih.gov/36270814/) | 2023 | Case report | Therapie | Benralizumab-induced interstitial granulomatous dermatitis: a rare paradoxical cutaneous adverse reaction reported in one asthma patient. Safety-relevant for dermatology use. |
| [39600395](https://pubmed.ncbi.nlm.nih.gov/39600395/) | 2024 | Review | Allergologie select | Update on biologics in allergology including anti-IL-5Rα position relative to newer approved agents for AD; notes absence of AD indication for benralizumab. |
| [34642091](https://pubmed.ncbi.nlm.nih.gov/34642091/) | 2021 | Review | Ann Allergy Asthma Immunol | Practical guidance on biologic selection for asthma, AD, urticaria, nasal polyps, and eosinophilic oesophagitis; frames the role of IL-5 vs. IL-4/13 pathway targeting. |
| [38878020](https://pubmed.ncbi.nlm.nih.gov/38878020/) | 2024 | Observational | J Allergy Clin Immunol | Patients receiving benralizumab (or dupilumab/mepolizumab) show lower post-vaccination SARS-CoV-2 antibody titres, indicating IL-5 pathway suppression modestly affects adaptive immune responses. |
| [36411004](https://pubmed.ncbi.nlm.nih.gov/36411004/) | 2023 | Review | Immunol Allergy Clin North Am | Safety review of biologics including benralizumab during pregnancy and lactation in women with asthma, allergic rhinitis, and atopic dermatitis. |

---

## Denmark Market Information

Benralizumab is not currently distributed on the Danish market and holds no registered marketing authorisations with the Danish Medicines Agency (Laegemiddelstyrelsen). Internationally, benralizumab is marketed as **Fasenra** by AstraZeneca and holds a centralised EMA authorisation (EU/1/17/1221), which is nominally valid across EU member states including Denmark. The EMA-approved indication covers add-on maintenance treatment of severe eosinophilic asthma in adults. There is no approved indication for dermatitis under any regulatory jurisdiction.

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|-------------------------------|--------------|-------------|---------------------|
| No Danish marketing authorisations currently on record | — | — | — |

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) available via the EMA for complete safety information.

Based on the published literature identified in this evidence pack, the following safety signals are particularly relevant when considering benralizumab in a dermatology context:

- **Paradoxical cutaneous reaction**: A case report (PMID 36270814) documented benralizumab-induced interstitial granulomatous dermatitis in a patient being treated for asthma. This is a rare but notable adverse effect if the drug were to be considered in dermatology patients.
- **Reduced vaccine immunogenicity**: An observational study (PMID 38878020) demonstrated lower SARS-CoV-2 antibody titres following vaccination in patients on benralizumab, indicating that IL-5Rα suppression modestly attenuates adaptive immune responses. Vaccination timing should be considered.
- **Parasitic infection risk**: Anti-type 2 immunity biologics including benralizumab carry a theoretical increased risk of helminth infections due to suppression of eosinophil-mediated anti-parasitic defence (PMID 38035014). Screening for endemic exposure is advisable before initiation.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The pivotal Phase 2 HILLIER randomised controlled trial (NCT04605094, n=194) was terminated early, and published results (PMID 37178404) confirmed that benralizumab produced no statistically or clinically meaningful improvement in atopic dermatitis endpoints compared with placebo. Although mechanistic studies confirm successful eosinophil depletion in skin lesions (target engagement), this does not translate into clinical benefit — consistent with evidence that AD is driven primarily by IL-4/IL-13 rather than IL-5. The TxGNN high prediction score most likely reflects structural proximity of immunomodulatory disease nodes in the knowledge graph rather than a clinically actionable biological connection.

**To proceed, the following would be needed:**

- Identification of a biomarker-defined AD subpopulation with a dominant eosinophilic endotype (e.g., very high tissue eosinophilia, elevated serum IL-5) that might selectively respond to IL-5Rα depletion
- A formally designed biomarker-enriched Phase 2 proof-of-concept study in this subgroup before further investment
- Resolution of the formal MOA data gap (DG002) via DrugBank API and review of the full prescribing information (SmPC) to address the safety data gap (DG001) before any clinical programme proceeds
- Regulatory pathway scoping with Laegemiddelstyrelsen, given that the product is not currently marketed in Denmark
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

