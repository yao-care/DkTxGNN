---
layout: default
title: Galcanezumab
parent: 僅模型預測 (L5)
nav_order: 201
evidence_level: L5
indication_count: 10
---

# Galcanezumab
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

# Galcanezumab: From Migraine Prevention to Heparin Cofactor 2 Deficiency

## One-Sentence Summary

Galcanezumab (Emgality®) is a humanised anti-CGRP monoclonal antibody approved internationally for the prevention of episodic and chronic migraine and for episodic cluster headache, but not currently registered in Denmark.
The TxGNN model's highest-ranked prediction is **Heparin Cofactor 2 Deficiency** (score 99.50%), for which there is **no supporting clinical or literature evidence** (L5); the prediction is assessed as a likely knowledge graph artefact.
The most clinically plausible prediction in this Evidence Pack is **Migraine with Brainstem Aura** (rank 9, score 98.33%), supported by **20 publications** including Phase 3 RCT data, and rated **L2 evidence**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Migraine prevention — episodic and chronic migraine; episodic cluster headache (international approval; not registered in Denmark) |
| Predicted New Indication | Heparin Cofactor 2 Deficiency |
| TxGNN Prediction Score | 99.50% |
| Evidence Level | L5 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

**Regarding Heparin Cofactor 2 Deficiency (Rank 1):** Detailed MOA data from DrugBank are not yet available for this report. Based on the published literature, galcanezumab is a humanised IgG4 monoclonal antibody that specifically binds and neutralises the CGRP (calcitonin gene-related peptide) ligand, blocking its interaction with the CGRP receptor. This prevents trigeminovascular activation and neurogenic vasodilation — the key events underlying migraine attacks.

Heparin cofactor 2 (HCII) deficiency is a rare coagulation disorder. HCII is a serpin-family protease inhibitor that inactivates thrombin in the presence of dermatan sulphate or heparin; its deficiency predisposes patients to thrombotic events. The pathophysiology is fundamentally distinct from CGRP-mediated neuroinflammation. While CGRP has minor peripheral vascular effects that could theoretically influence the haemostatic microenvironment, no published evidence links CGRP blockade to HCII activity or the broader coagulation cascade. The TxGNN repurposing rationale embedded in this Evidence Pack explicitly notes that the high prediction score likely reflects knowledge graph topology effects — such as shared comorbidity nodes or phenotypic proximity between rare coagulation disorders and neurological drug targets — rather than direct biological relevance.

**Note on prediction clustering:** All of ranks 1–8 (4 unique diseases, each appearing twice in the output) are coagulation-related disorders: heparin cofactor 2 deficiency, antithrombin deficiency type 2, factor V excess with spontaneous thrombosis, and thrombophilia — all rated L5 with "Hold" recommendations. This clustering strongly suggests a systematic knowledge graph effect. **Migraine with Brainstem Aura** (ranks 9–10, L2, 20 supporting publications) is the most clinically credible prediction in this pack and is addressed in the sections below.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for heparin cofactor 2 deficiency.

There are also no registered clinical trials specifically evaluating galcanezumab in migraine with brainstem aura. Patients with this subtype have historically been excluded from pivotal migraine trials due to vascular safety concerns, creating a direct evidence gap despite strong mechanistic plausibility.

---

## Literature Evidence

The following 10 publications are relevant to the most clinically plausible prediction in this Evidence Pack: **Migraine with Brainstem Aura** (rank 9/10, TxGNN score 98.33%). These studies involve galcanezumab or the anti-CGRP drug class in migraine and related aura subtypes, ordered by study tier.

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [29813147](https://pubmed.ncbi.nlm.nih.gov/29813147/) | 2018 | Phase 3 RCT | JAMA Neurology | EVOLVE-1: galcanezumab significantly reduced monthly migraine headache days vs placebo in episodic migraine over 6 months |
| [33549036](https://pubmed.ncbi.nlm.nih.gov/33549036/) | 2021 | Phase 3 Pooled Analysis | J Headache Pain | Pooled EVOLVE-1, EVOLVE-2, REGAIN: galcanezumab reduced migraine severity, nausea, photophobia, phonophobia, and aura-associated symptoms |
| [36927366](https://pubmed.ncbi.nlm.nih.gov/36927366/) | 2023 | Phase 3 Secondary Analysis | J Headache Pain | Galcanezumab reduced headache occurrence after trigger exposure and aura episodes; responder/super-responder analysis |
| [36266558](https://pubmed.ncbi.nlm.nih.gov/36266558/) | 2023 | Phase 2 RCT Subgroup | Neurology and Therapy | Galcanezumab reduced migraine severity and aura-associated symptoms in Japanese patients |
| [32504377](https://pubmed.ncbi.nlm.nih.gov/32504377/) | 2020 | Systematic Review | Drugs | Comprehensive review of galcanezumab efficacy in episodic/chronic migraine and episodic cluster headache |
| [35268319](https://pubmed.ncbi.nlm.nih.gov/35268319/) | 2022 | Case Reports & Review | J Clinical Medicine | Anti-CGRP mAbs (including galcanezumab) may reduce migraine aura frequency; limited but encouraging case evidence |
| [41618146](https://pubmed.ncbi.nlm.nih.gov/41618146/) | 2026 | Quantitative Patient Analysis | J Headache Pain | Anti-CGRP mAbs effective and safe in hemiplegic migraine (migraine with motor aura) — closely related aura subtype |
| [37366160](https://pubmed.ncbi.nlm.nih.gov/37366160/) | 2023 | Case Series | Headache | Anti-CGRP mAbs including galcanezumab showed efficacy in hemiplegic migraine at a tertiary headache centre |
| [39345003](https://pubmed.ncbi.nlm.nih.gov/39345003/) | 2025 | Case Series | Headache | Galcanezumab effective in PRRT2-associated familial hemiplegic migraine — extends evidence to genetic migraine-with-aura subtypes |
| [39365416](https://pubmed.ncbi.nlm.nih.gov/39365416/) | 2024 | Case Report | Pain and Therapy | Cerebral artery vasoconstriction (RCVS-like event) following galcanezumab loading dose — key safety signal relevant to brainstem aura |

---

## Denmark Market Information

Galcanezumab is not registered in Denmark and holds no marketing authorisations from Lægemiddelstyrelsen. The drug is marketed as **Emgality®** by Eli Lilly, and holds a centralised EMA marketing authorisation for the preventive treatment of migraine in adults. Denmark does not currently have active national supply or reimbursement listing. Any clinical use in Danish patients would require an individual compassionate use or named patient import application (*enkeltindførselsordningen*).

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for full safety information.

**Key safety signal from literature:** One case report (PMID 39365416) describes cerebral artery vasoconstriction following galcanezumab loading dose, consistent with reversible cerebral vasoconstriction syndrome (RCVS). This is particularly relevant for potential use in migraine with brainstem aura, given the shared cerebrovascular involvement. Vascular monitoring — including cerebrovascular assessment — should be considered in this patient population before and during treatment.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top TxGNN prediction — heparin cofactor 2 deficiency — has no mechanistic basis, no registered clinical trials, and no published literature support. Together with antithrombin deficiency type 2, factor V excess with spontaneous thrombosis, and thrombophilia (ranks 1–8), this cluster is assessed as a knowledge graph artefact rather than a genuine repurposing opportunity. A "Hold" decision is warranted until a biologically plausible hypothesis can be established and tested.

---

**Separate consideration: Migraine with Brainstem Aura (Rank 9, Score 98.33%, L2 — "Research Question")**

This prediction is mechanistically well-grounded (galcanezumab's CGRP blockade is directly applicable to brainstem-aura pathophysiology), supported by 20 publications and multiple Phase 3 analyses in related migraine populations, and constitutes a clinically credible research question. The evidence gap arises specifically from the historical exclusion of this subtype from pivotal trials.

**To progress the migraine with brainstem aura indication, the following is needed:**

- Full SmPC review for Emgality® to identify contraindications specific to patients with brainstem aura symptoms
- Subgroup analysis or meta-analysis of existing Phase 3 RCT data (EVOLVE-1/EVOLVE-2) stratified by aura subtype
- Prospective observational cohort or registry study specifically enrolling patients diagnosed with migraine with brainstem aura (IHS classification 1.2.2)
- Cerebrovascular risk assessment and monitoring protocol, including vigilance for RCVS
- Named patient import or EMA centralised authorisation pathway for Denmark, should evidence support clinical use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

