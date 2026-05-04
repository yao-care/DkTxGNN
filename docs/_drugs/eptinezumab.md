---
layout: default
title: Eptinezumab
parent: 僅模型預測 (L5)
nav_order: 171
evidence_level: L5
indication_count: 10
---

# Eptinezumab
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

# Eptinezumab: From Migraine Prevention to Migraine with Brainstem Aura

## One-Sentence Summary

Eptinezumab (Vyepti) is an intravenous anti-CGRP monoclonal antibody approved globally for the preventive treatment of episodic and chronic migraine in adults, although it is not currently registered in Denmark. The TxGNN model predicts it may be effective for **Migraine with Brainstem Aura** — a rare and clinically distinct migraine subtype — with **0 clinical trials** targeting this specific subtype and **8 publications** providing indirect mechanistic and subgroup support. Evidence is currently at Level L3, and the prediction is mechanistically plausible but requires dedicated prospective validation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Preventive treatment of migraine in adults (episodic and chronic; FDA-approved 2020, EMA-approved; not registered in Denmark) |
| Predicted New Indication | Migraine with Brainstem Aura |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L3 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, formal mechanism of action data from DrugBank is not available for this assessment. Based on known published information, eptinezumab is a humanised IgG1 monoclonal antibody that targets calcitonin gene-related peptide (CGRP) directly; its efficacy in preventing episodic and chronic migraine has been demonstrated in two pivotal Phase 3 trials (PROMISE-1 and PROMISE-2), and this mechanism may plausibly extend to the brainstem aura subtype.

CGRP is widely expressed throughout the trigeminovascular system, including brainstem nuclei directly implicated in aura generation — notably the periaqueductal grey matter (PAG) and the locus coeruleus. Migraine with brainstem aura involves cortical spreading depression-like phenomena (CSD-like events) originating in the brainstem, in which CGRP plays both pro-inflammatory and vasodilatory roles. By blocking free CGRP from reaching its receptor, eptinezumab could theoretically lower the brainstem aura trigger threshold. Mechanistic plausibility is therefore rated moderate-to-high (★★★☆). A 2022 post hoc subgroup analysis of PROMISE-1 and PROMISE-2 further demonstrated that eptinezumab was efficacious and well-tolerated in migraine patients with self-reported aura broadly, lending indirect clinical support to the prediction.

An important caveat is that a 2025 RCT (PMID 40229719) showed that PACAP38-induced migraine attacks are largely independent of CGRP signalling, suggesting that parallel pathways — beyond CGRP — are involved in aura generation. This means that CGRP blockade alone may not fully prevent brainstem aura events in all patients, and the magnitude of benefit may be smaller in this subtype than in non-aura phenotypes. PACAP38 pathway involvement should be considered when designing future studies.

---

## Clinical Trial Evidence

Currently no clinical trials registered in ClinicalTrials.gov or the WHO ICTRP specifically address **migraine with brainstem aura** as an indication for eptinezumab.

> **Note:** The pivotal PROMISE-1 (episodic migraine) and PROMISE-2 (chronic migraine) Phase 3 trials enrolled general migraine populations; patients with aura were included, but brainstem aura was not a dedicated enrolment criterion or primary endpoint. No EudraCT-registered EU trials specifically for this subtype were identified.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [35302389](https://pubmed.ncbi.nlm.nih.gov/35302389/) | 2022 | Post-hoc analysis of Phase 3 RCTs (PROMISE-1/2) | *Cephalalgia* | Post hoc subgroup analysis: eptinezumab demonstrated efficacy and acceptable safety in migraine patients with self-reported aura, providing the strongest available indirect evidence for aura subtypes including brainstem aura |
| [40341526](https://pubmed.ncbi.nlm.nih.gov/40341526/) | 2025 | Genetic/Clinical Study | *Headache* | Case series reporting patients with genetic migraine disorders (including chronic migraine with visual aura) who responded to CGRP antagonist therapy, supporting CGRP involvement across heterogeneous aura phenotypes |
| [35268319](https://pubmed.ncbi.nlm.nih.gov/35268319/) | 2022 | Case Reports + Literature Review | *Journal of Clinical Medicine* | Anti-CGRP monoclonal antibodies (including eptinezumab) may reduce migraine aura frequency; limited but encouraging data suggest partial suppression of cortical spreading depression |
| [40191903](https://pubmed.ncbi.nlm.nih.gov/40191903/) | 2025 | Case Report | *Revista de Neurología* | Eptinezumab IV successfully managed a wearing-off effect in a chronic migraine-with-aura patient refractory to two subcutaneous CGRP antibodies, highlighting the clinical advantage of its intravenous administration route |
| [40229719](https://pubmed.ncbi.nlm.nih.gov/40229719/) | 2025 | RCT | *The Journal of Headache and Pain* | PACAP38-induced migraine attacks are largely independent of CGRP signalling; this finding suggests CGRP blockade may not address all brainstem aura triggers and points to a complementary, CGRP-independent pathway |
| [33550872](https://pubmed.ncbi.nlm.nih.gov/33550872/) | 2021 | Review | *Pain Management* | Overview of new migraine preventive therapies; eptinezumab listed among four CGRP-targeting preventive agents, with mechanistic rationale for broader migraine subtype application |
| [32699706](https://pubmed.ncbi.nlm.nih.gov/32699706/) | 2020 | Review | *Cureus* | CGRP antagonists reviewed for episodic and chronic migraine prevention; mechanistic basis for CGRP-targeting in aura-associated migraine phenotypes discussed |
| [30725283](https://pubmed.ncbi.nlm.nih.gov/30725283/) | 2019 | Review | *Handbook of Experimental Pharmacology* | Comprehensive review of CGRP's role in migraine pathophysiology, including trigeminal system and brainstem involvement, establishing the mechanistic foundation for CGRP-targeted therapies |

---

## Denmark Market Information

Eptinezumab is **not currently authorised** by the Danish Medicines Agency (Lægemiddelstyrelsen) and holds no national or centralised marketing authorisations applicable to Denmark. There are therefore no approved product entries to list.

For clinical reference, eptinezumab is internationally available as **Vyepti** (100 mg/mL concentrate for solution for infusion, 100 mg dose administered IV every 12 weeks):

- **US FDA**: Approved February 2020 — preventive treatment of migraine in adults
- **EMA (centralised)**: Marketing authorisation held by H. Lundbeck A/S — preventive treatment of migraine in adults

Danish healthcare professionals wishing to use eptinezumab outside a clinical trial must apply for a named-patient or compassionate use authorisation through Lægemiddelstyrelsen under the provisions of the Danish Medicines Act (§29-30), or await a potential future application for national/centralised authorisation.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for full safety information. Specific local warnings and contraindications from the Danish Medicines Agency are not available, as the product is not registered in Denmark.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Eptinezumab's mechanism of action — CGRP blockade in the trigeminovascular system, including brainstem nuclei involved in aura generation — provides moderate-to-high mechanistic plausibility for efficacy in migraine with brainstem aura. Post hoc evidence from the PROMISE-1 and PROMISE-2 Phase 3 trials supports efficacy in the broader migraine-with-aura population, and the TxGNN score of 99.94% reflects a model confidence consistent with this overlap. However, no dedicated trials for the brainstem aura subtype exist, the evidence level is L3, and the PACAP38-independent pathway introduces uncertainty about the completeness of CGRP blockade as a therapeutic strategy for this specific phenotype.

**To proceed, the following is needed:**

- A dedicated prospective clinical trial or observational registry study specifically enrolling patients with confirmed migraine with brainstem aura according to ICHD-3 criteria (code 1.2.2), with eptinezumab as the intervention
- Formal mechanism of action documentation (from DrugBank or EMA SmPC) for inclusion in any Danish regulatory or HTA submission
- Full safety profile review from the EMA SmPC, with specific attention to hypersensitivity reactions relevant to IV monoclonal antibody infusion
- Named-patient or compassionate use authorisation from Lægemiddelstyrelsen if off-label use in Denmark is considered prior to formal registration
- A pharmacovigilance plan accounting for non-responders in whom PACAP38-independent brainstem aura pathways may be dominant, and for potential wearing-off effects between quarterly infusions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

