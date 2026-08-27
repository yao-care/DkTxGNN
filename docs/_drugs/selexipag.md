---
layout: default
title: Selexipag
parent: 僅模型預測 (L5)
nav_order: 395
evidence_level: L5
indication_count: 10
---

# Selexipag
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

# Selexipag: From Pulmonary Arterial Hypertension to Pulmonary Arterial Hypertension Associated with Congenital Heart Disease

## One-Sentence Summary

Selexipag is an oral, selective prostacyclin (IP) receptor agonist established in the treatment of pulmonary arterial hypertension (PAH, WHO Group 1). The TxGNN model predicts continued efficacy in **Pulmonary Arterial Hypertension Associated with Congenital Heart Disease (PAH-CHD)** — a disease subtype that falls within the drug's existing pharmacological scope rather than an unrelated new indication — supported by **2 clinical trials** and **15 publications** currently in evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pulmonary Arterial Hypertension (WHO Group 1) — established via literature in this evidence pack; not confirmed through Danish regulatory records, as the drug is not currently marketed in Denmark |
| Predicted New Indication | Pulmonary Arterial Hypertension Associated with Congenital Heart Disease |
| TxGNN Prediction Score | 98.03% |
| Evidence Level | L2 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed DrugBank-sourced mechanism-of-action data is not available in this evidence pack (data gap). However, the included literature independently confirms Selexipag's pharmacology: it is described as "an oral selective prostacyclin receptor agonist approved for treating pulmonary arterial hypertension (PAH) in adults" (PMID 41429287), and its labelled use already extends to PAH associated with connective tissue disease (PMID 39076250). As a selective IP-receptor agonist, Selexipag raises intracellular cAMP, producing pulmonary vasodilation and anti-proliferative/anti-remodeling effects.

Critically, this mechanism is not specific to disease etiology — it targets the shared vascular pathology across all WHO Group 1 PAH subtypes. PAH associated with congenital heart disease (including Eisenmenger syndrome) is itself one of the recognized aetiological subgroups within Group 1 PAH, and was represented in Selexipag's pivotal Phase 3 GRIPHON trial population.

Because of this, the predicted "new" indication functions less as a novel repurposing target and more as a label-adjacent sub-population already mechanistically covered by the drug's known therapeutic class. This is reflected directly in the evidence pack's own rationale: "CHD-PAH 本屬於原適應症之涵蓋族群，機轉關聯性強、近乎藥品既有標籤延伸而非全新適應症" (CHD-PAH belongs to the population already covered by the original indication; the mechanistic link is strong and closely resembles a label extension rather than an entirely new indication).

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04435782](https://clinicaltrials.gov/study/NCT04435782) | Phase 4 | Terminated | 9 | Assessed Selexipag's effect on right ventricular remodeling in PAH via cardiac MRI; study was terminated early, limiting the strength of the evidence |
| [NCT05179876](https://clinicaltrials.gov/study/NCT05179876) | Phase 3 | Recruiting | 280 | Long-term, open-label follow-up platform study allowing PAH participants (including PAH-CHD) from several parent trials to continue treatment and assess long-term safety; still recruiting, no results yet |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30632656](https://pubmed.ncbi.nlm.nih.gov/30632656/) | 2019 | Cohort (RCT-derived) | European Journal of Heart Failure | Insights from the randomised controlled GRIPHON study on Selexipag in corrected CHD-PAH; corrected CHD-PAH patients have poorer prognosis and limited RCT evidence base |
| [33442633](https://pubmed.ncbi.nlm.nih.gov/33442633/) | 2020 | Cohort | European Heart Journal - Case Reports | Case series showing Selexipag as an oral alternative to parenteral prostacyclins in PAH-CHD, potentially reducing treatment-related risk while improving outcomes |
| [29521655](https://pubmed.ncbi.nlm.nih.gov/29521655/) | 2018 | Cohort | American Journal of Therapeutics | First report of Selexipag use in CHD-associated PAH and Eisenmenger syndrome |
| [41429287](https://pubmed.ncbi.nlm.nih.gov/41429287/) | 2025 | Phase 2 PK study | Chest | Prospective multicenter Phase 2 study of Selexipag pharmacokinetics, safety, tolerability, and exploratory efficacy in children with PAH |
| [33781364](https://pubmed.ncbi.nlm.nih.gov/33781364/) | 2021 | Cohort | Cardiology in the Young | Single-centre report of Selexipag use in four paediatric PAH-CHD patients |
| [36204579](https://pubmed.ncbi.nlm.nih.gov/36204579/) | 2022 | Cohort | Frontiers in Cardiovascular Medicine | Selexipag-based triple combination therapy improves prognosis in Chinese PAH patients |
| [41513133](https://pubmed.ncbi.nlm.nih.gov/41513133/) | 2026 | Real-world registry | Journal of Cardiology | Retrospective Japan PH Registry study characterizing real-world use of Selexipag and parenteral prostacyclin analogs across PAH aetiologies |
| [31738929](https://pubmed.ncbi.nlm.nih.gov/31738929/) | 2020 | Expert consensus | Chest | Expert panel consensus statements on initiating oral prostacyclin pathway agents (including Selexipag) in adults with PAH |
| [30545978](https://pubmed.ncbi.nlm.nih.gov/30545978/) | 2019 | Review | European Respiratory Journal | Updates on definition, classification, diagnostics and management of paediatric PAH, including CHD-associated disease |
| [38276220](https://pubmed.ncbi.nlm.nih.gov/38276220/) | 2023 | Review | Journal of Personalized Medicine | Review of current management and future directions for PAH associated with congenital heart disease |

---

## Denmark Market Information

Selexipag currently holds **no marketing authorisation in Denmark** (market status: Not marketed; 0 registered authorisations). No Laegemiddelstyrelsen or EMA centralised licence data is available in this evidence pack to confirm approved dosage forms or indication wording for the Danish market.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information. No key warnings, contraindications, or drug-drug interaction data were retrievable in this evidence pack (DDI query status: not found).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic case is strong — PAH-CHD is a recognized sub-population within Selexipag's own WHO Group 1 PAH indication class rather than a distinct disease target — and it is backed by RCT-derived subgroup data (GRIPHON) plus an actively recruiting Phase 3 long-term safety study. However, no completed trial designed specifically for this sub-population exists yet, and Denmark-specific regulatory/safety data are entirely absent.

**To proceed, the following is needed:**
- Danish SmPC / product warnings and contraindications (currently a **Blocking** data gap — required before any S1 safety assessment)
- Formal mechanism-of-action documentation via DrugBank or equivalent source (**High**-severity data gap)
- Confirmation of marketing authorisation pathway or import route, given the drug is not currently marketed in Denmark
- Mature results from the ongoing NCT05179876 long-term follow-up study once available
- A dedicated drug-drug interaction review, as none is currently on record
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

