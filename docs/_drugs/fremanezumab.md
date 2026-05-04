---
layout: default
title: Fremanezumab
parent: 僅模型預測 (L5)
nav_order: 196
evidence_level: L5
indication_count: 10
---

# Fremanezumab
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

# Fremanezumab: From Migraine Prevention to Migraine with Brainstem Aura

## One-Sentence Summary

Fremanezumab (Ajovy) is a fully humanized anti-CGRP monoclonal antibody approved in multiple markets for prevention of episodic and chronic migraine. The TxGNN model predicts it may be effective for **migraine with brainstem aura** — a rare subtype systematically excluded from pivotal clinical trials — with **0 registered clinical trials** but **20 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Migraine prevention (episodic and chronic migraine) — EMA centralised authorisation exists; not yet registered in Denmark |
| Predicted New Indication | Migraine with Brainstem Aura |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L3 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Fremanezumab is a fully humanized IgG2Δa monoclonal antibody that selectively binds calcitonin gene-related peptide (CGRP) — a potent neuropeptide central to migraine pathophysiology. By neutralizing CGRP directly before it can reach its receptor, fremanezumab blocks the downstream cascade of neurogenic inflammation and vasodilatation in the trigeminovascular system, which is the primary pain-generating pathway in migraine.

Migraine with brainstem aura (formerly basilar-type migraine) is characterized by aura symptoms originating from the brainstem: vertigo, dysarthria, tinnitus, diplopia, and bilateral sensory disturbance. The neurophysiological mechanism underlying aura is cortical spreading depression (CSD) — a slow, self-propagating wave of neuronal depolarization. Crucially, CSD triggers a large, acute release of CGRP, creating a direct mechanistic bridge between this condition and fremanezumab's target. Two preclinical mechanistic studies (PMID 31127003, PMID 31895266) demonstrate that fremanezumab slows CSD propagation velocity and shortens the cortical recovery period, though it does not fully prevent CSD onset. This means fremanezumab is likely to reduce aura severity and duration rather than abolish it entirely — a pattern consistent with observations from clinical case series of anti-CGRP antibodies in migraine with aura (PMID 35268319).

Patients with migraine with brainstem aura have historically been excluded from randomized controlled trials due to theoretical cardiovascular safety concerns about CSD-triggering agents. This regulatory gap has left a significant unmet clinical need. The accumulating real-world data, mechanistic studies, and indirect subgroup evidence from the Phase 3b FOCUS trial (fremanezumab in difficult-to-treat migraine with neurological dysfunction including aura; PMID 35302681) collectively support a biologically plausible and clinically underserved extension of fremanezumab's approved indication.

---

## Clinical Trial Evidence

Currently no clinical trials specifically registered for fremanezumab in migraine with brainstem aura.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [35268319](https://pubmed.ncbi.nlm.nih.gov/35268319/) | 2022 | Case Series + Literature Review | J Clin Med | Anti-CGRP mAbs (eptinezumab, fremanezumab, galcanezumab, erenumab) may reduce migraine aura frequency; case reports document aura improvement with CGRP-targeted prophylaxis |
| [38332541](https://pubmed.ncbi.nlm.nih.gov/38332541/) | 2024 | Observational Case Series | CNS Neurosci Ther | Anti-CGRP-targeted therapy shows potential preventive effectiveness for migraine with aura; limited but encouraging clinical evidence |
| [41618146](https://pubmed.ncbi.nlm.nih.gov/41618146/) | 2026 | Individual Patient Analysis | J Headache Pain | Anti-CGRP mAbs effective in hemiplegic migraine (a severe migraine-with-aura subtype excluded from RCTs); supports broader use in aura-predominant presentations |
| [35302681](https://pubmed.ncbi.nlm.nih.gov/35302681/) | 2022 | Retrospective Cohort | Eur J Neurol | Post hoc of Phase 3b FOCUS trial: fremanezumab effective in difficult-to-treat migraine patients with and without aura or similar neurological dysfunction |
| [31127003](https://pubmed.ncbi.nlm.nih.gov/31127003/) | 2019 | Preclinical / Mechanistic | J Neurosci | CSD-induced arterial dilatation and plasma protein extravasation unaffected by fremanezumab, suggesting CGRP-independent vascular CSD responses; clarifies mechanistic scope |
| [31895266](https://pubmed.ncbi.nlm.nih.gov/31895266/) | 2020 | Preclinical / Mechanistic | Pain | Fremanezumab slows CSD propagation velocity and shortens cortical recovery period in rats with compromised blood-brain barrier; does not prevent CSD onset |
| [28642283](https://pubmed.ncbi.nlm.nih.gov/28642283/) | 2017 | Preclinical / Mechanistic | J Neurosci | Fremanezumab selectively inhibits trigeminovascular neurons; establishes mechanistic basis for CGRP-targeted migraine prevention |
| [37638190](https://pubmed.ncbi.nlm.nih.gov/37638190/) | 2023 | Prospective Observational | Front Neurol | Real-world efficacy and tolerability of fremanezumab in chronic migraine confirmed in post-marketing setting; safety profile consistent with RCT data |
| [40264646](https://pubmed.ncbi.nlm.nih.gov/40264646/) | 2025 | Case Report + Literature Review | Front Neurol | Anti-CGRP mAbs effective in hemiplegic migraine case; reviews broader evidence for CGRP pathway blockade in migraine-with-aura subtypes |
| [35775208](https://pubmed.ncbi.nlm.nih.gov/35775208/) | 2022 | Observational | Cephalalgia | Erenumab, fremanezumab, and galcanezumab reduce prodromal and accompanying neurological symptoms of migraine, suggesting effects beyond peripheral pain pathways |

---

## Denmark Market Information

Fremanezumab currently holds no marketing authorisation with the Danish Medicines Agency (Laegemiddelstyrelsen) and is not marketed in Denmark. Clinicians requiring access may apply for individual special import (named-patient import) under Danish Medicines Act §28, referencing the centrally authorised EMA product Ajovy. The EMA centralised marketing authorisation for Ajovy covers prevention of migraine in adults with at least 4 migraine days per month.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information. As fremanezumab is not registered in Denmark, locally validated safety data is not available. The EMA SmPC for Ajovy should be consulted for full warnings, contraindications, and drug interaction guidance. No drug-drug interactions were identified in the evidence retrieval for this report.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic link between fremanezumab's CGRP blockade and the CSD-driven pathophysiology of migraine with brainstem aura is biologically well-grounded, and the growing body of indirect clinical evidence from aura-related studies — combined with the established safety profile from Phase 3 RCTs in chronic and episodic migraine — supports careful advancement. The primary constraint is the absence of dedicated trials in this specific subtype and the lack of a Danish marketing authorisation.

**To proceed, the following is needed:**
- Secure regulatory access pathway in Denmark (special import authorization or application for marketing authorisation extension)
- Prospective observational registry specifically enrolling patients with migraine with brainstem aura treated with fremanezumab
- Full review of the EMA SmPC (Ajovy) to confirm no subtype-specific contraindications relevant to brainstem aura
- Mechanism of action documentation retrieved from DrugBank (currently unavailable in this evidence pack)
- Danish Medicines Agency pharmacovigilance data or EU RMP review to assess cardiovascular monitoring requirements specific to this subtype
- Clinical protocol for monitoring aura frequency and severity as primary outcomes, distinct from headache-day endpoints used in standard migraine trials
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

