---
layout: default
title: Clopidogrel
parent: 僅模型預測 (L5)
nav_order: 118
evidence_level: L5
indication_count: 10
---

# Clopidogrel
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

# Clopidogrel: From Atherothrombosis Prevention to Migraine with Brainstem Aura

## One-Sentence Summary

Clopidogrel is a thienopyridine antiplatelet agent widely used for preventing atherothrombotic events in patients with acute coronary syndromes, prior stroke, or peripheral arterial disease.
The TxGNN model predicts it may be effective for **Migraine with Brainstem Aura** (TxGNN score 99.44%), with **16 publications** currently supporting this specific subtype; the closely related broader category **Migraine Disorder** is additionally supported by **8 clinical trials** (including one completed Phase 4 RCT) and **20 publications**, reaching an overall evidence level of L2.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Atherothrombotic event prevention: acute coronary syndrome, ischaemic stroke, peripheral arterial disease |
| Predicted New Indication | Migraine with Brainstem Aura |
| TxGNN Prediction Score | 99.44% |
| Evidence Level | L3 (migraine with brainstem aura); L2 for broader migraine disorder |
| Denmark Market Status | Not found in Laegemiddelstyrelsen national database (data gap — EMA centralised authorisation likely exists; see note below) |
| Number of Marketing Authorisations | 0 (national database query; centralised EMA authorisation not captured) |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on established pharmacology, clopidogrel is a P2Y12 receptor antagonist that irreversibly blocks ADP-mediated platelet activation on the platelet surface, thereby reducing thrombus formation. Its proven benefit in cerebrovascular thrombotic events laid the conceptual groundwork for investigating its role in migraine — a condition in which platelet hyperactivation and microembolic phenomena have been proposed as contributing triggers in a significant subgroup of patients.

Two mechanistic pathways directly link clopidogrel to migraine with brainstem aura. The first is a **peripheral antiplatelet route**: patent foramen ovale (PFO) and other right-to-left cardiac shunts are found in approximately 40–50% of migraineurs with aura. Platelet microemboli passing through these shunts can reach the cerebral circulation and trigger cortical spreading depolarisation (CSD). Migraine with brainstem aura — the former "basilar-type migraine" — is characterised by pronounced brainstem involvement, making the PFO-related microembolism pathway particularly relevant for this subtype.

The second pathway is **central P2Y12 receptor antagonism**: preclinical evidence (PMID 31722730) demonstrates that P2Y12 receptors expressed on microglia in the trigeminal nucleus caudalis (TNC) mediate microglial activation via the RhoA/ROCK signalling cascade, amplifying neuroinflammation and lowering the threshold for aura generation. Blockade of this receptor by clopidogrel may directly suppress central sensitisation, independently of PFO status — potentially extending benefit beyond patients with demonstrable cardiac shunts.

---

## Clinical Trial Evidence

No clinical trials have been registered specifically for clopidogrel in the *migraine with brainstem aura* subtype. The following trials address clopidogrel in PFO-associated migraine with aura and the broader migraine disorder category, and are directly relevant given that brainstem aura is a subtype of migraine with aura:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00799045](https://clinicaltrials.gov/study/NCT00799045) | Phase 4 | Completed | 220 | CANOA trial: clopidogrel + aspirin vs aspirin alone after transcatheter ASD closure — directly compared clopidogrel's effect on new-onset migraine post-cardiac procedure |
| [NCT00562289](https://clinicaltrials.gov/study/NCT00562289) | Phase 3 | Completed | 664 | PFO closure vs anticoagulation vs antiplatelet (including clopidogrel) to prevent stroke recurrence; migraine reported as secondary outcome, providing indirect evidence |
| [NCT02938182](https://clinicaltrials.gov/study/NCT02938182) | Phase 4 | Unknown | 50 | Prospective trial evaluating clopidogrel prophylaxis specifically for migraine patients with right-to-left shunt; most directly targeted design — status and final results unclear |
| [NCT05546320](https://clinicaltrials.gov/study/NCT05546320) | Phase 4 | Unknown | 1,000 | COMPETE trial: head-to-head comparison of anticoagulation vs antiplatelet (clopidogrel-based) vs migraine-specific therapy in PFO-associated migraine; results would provide definitive positioning data |
| [NCT04946734](https://clinicaltrials.gov/study/NCT04946734) | Phase 3 | Active, not recruiting | 440 | SPRING trial: PFO closure vs medical therapy (antiplatelet arm includes clopidogrel); expected completion September 2025 |
| [NCT02777359](https://clinicaltrials.gov/study/NCT02777359) | Phase 2 | Unknown | 100 | High-risk PFO closure vs antiplatelet therapy for migraine in a prospective multicentre RCT; clopidogrel is the antiplatelet protocol backbone |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39989443](https://pubmed.ncbi.nlm.nih.gov/39989443/) | 2025 | Systematic Review | Headache | Comprehensive systematic review of antithrombotic drugs as migraine preventive medications; synthesises available evidence for clopidogrel and related antiplatelet agents |
| [26551304](https://pubmed.ncbi.nlm.nih.gov/26551304/) | 2015 | RCT | JAMA | CANOA primary results (n=220): clopidogrel + aspirin significantly reduced incidence of new-onset migraine after transcatheter ASD closure vs aspirin alone — highest-quality direct evidence |
| [32965476](https://pubmed.ncbi.nlm.nih.gov/32965476/) | 2021 | Clinical Comparative Study | JAMA Cardiology | CANOA 1-year follow-up: protective effect on post-ASD migraine persisted at 6–12 months even after clopidogrel cessation at 3 months, suggesting a durable mechanistic impact |
| [24836213](https://pubmed.ncbi.nlm.nih.gov/24836213/) | 2014 | Pilot RCT | Cephalalgia | Pilot RCT of clopidogrel as prophylactic migraine treatment (not restricted to PFO patients); demonstrates feasibility and a preliminary efficacy signal in unselected migraineurs |
| [32848048](https://pubmed.ncbi.nlm.nih.gov/32848048/) | 2020 | Cohort Study | J Investigative Medicine | Clopidogrel 75 mg/day as complementary prophylaxis in drug-refractory migraineurs with PFO: significant reduction in attack frequency at 3 and 6 months |
| [16103551](https://pubmed.ncbi.nlm.nih.gov/16103551/) | 2005 | Observational Study | Heart | One of the earliest clinical observations: clopidogrel reduced migraine with aura following transcatheter PFO and ASD closure, prompting systematic investigation |
| [30478067](https://pubmed.ncbi.nlm.nih.gov/30478067/) | 2018 | Open-label Pilot | Neurology | TRACTOR study: ticagrelor (a non-thienopyridine P2Y12 inhibitor) reduced migraine in PFO patients after prior benefit was observed with clopidogrel/prasugrel — supports a P2Y12 class effect |
| [30478066](https://pubmed.ncbi.nlm.nih.gov/30478066/) | 2018 | Retrospective Review | Neurology | Retrospective review of thienopyridine (clopidogrel and prasugrel) therapy in PFO-associated migraineurs: consistent headache reduction across the cohort |
| [24770421](https://pubmed.ncbi.nlm.nih.gov/24770421/) | 2014 | Retrospective Review | Cephalalgia | Clopidogrel as primary therapy in migraineurs with right-to-left shunt: supports antiplatelet mechanism in aura migraine and establishes historical clinical rationale |
| [26908949](https://pubmed.ncbi.nlm.nih.gov/26908949/) | 2016 | RCT | European Heart Journal | PRIMA trial: PFO closure in migraine with aura (multicentre RCT); clopidogrel used post-procedurally — provides important context on the PFO-aura link and migraine outcomes |

---

## Denmark Market Information

The available Laegemiddelstyrelsen national database query returned **zero marketing authorisation records** for clopidogrel. This almost certainly reflects a **data gap** rather than actual unavailability: clopidogrel (Plavix® and multiple generic products) is the subject of EMA centralised marketing authorisation **EU/1/98/069/001**, which is valid across all EU/EEA member states including Denmark. Healthcare professionals should verify current authorisation status and product availability directly with the Danish Medicines Agency (Laegemiddelstyrelsen) or via the EMA's EPAR database.

| Marketing Authorisation | Product | Dosage Form | Approved Indication |
|---|---|---|---|
| EU/1/98/069 (EMA centralised) | Plavix® (and EMA-approved generics) | Film-coated tablet 75 mg; 300 mg loading dose | Prevention of atherothrombotic events in ACS, recent MI, recent ischaemic stroke, and established peripheral arterial disease |

> ⚠️ **Data Gap Notice**: The national database query returned 0 records. This is inconsistent with the known EU-wide authorisation status. Laegemiddelstyrelsen and the EMA EPAR database should be consulted for confirmed Danish market and reimbursement status before any prescribing decision.

---

## Safety Considerations

No safety data (key warnings, contraindications, or drug-drug interactions) was retrieved in this Evidence Pack for clopidogrel. All safety data fields returned as empty.

> Please refer to the approved Summary of Product Characteristics (SmPC) — available via the EMA EPAR entry for Plavix® (EU/1/98/069) — for complete safety information before any clinical use. Key areas to review for the migraine repurposing context include bleeding risk (particularly when combined with aspirin), CYP2C19 pharmacogenomic variability affecting antiplatelet efficacy, and management of patients undergoing surgical procedures.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The CANOA randomised controlled trial (*JAMA* 2015, n=220) provides direct Phase 4 evidence that clopidogrel + aspirin significantly reduces new-onset migraine after cardiac septal closure, supported by a mechanistically coherent dual pathway (peripheral antiplatelet + central P2Y12/RhoA/ROCK). For the specific subtype of migraine with brainstem aura, the mechanistic rationale is particularly compelling given the pronounced brainstem involvement and the known association with PFO. However, no dedicated trials exist for this subtype, and the evidence base is currently confined to PFO/cardiac-shunt-associated migraine — meaning patient selection is critical.

**To proceed, the following is needed:**
- **Safety documentation**: Retrieve and review the full EMA SmPC (EU/1/98/069) to complete contraindication and warning assessment before any off-label use protocol is designed
- **MOA formalisation**: Retrieve mechanism of action data from DrugBank (DB00758) to complete the Evidence Pack
- **Danish market verification**: Confirm clopidogrel's current authorisation, reimbursement, and availability status in Denmark via Laegemiddelstyrelsen and the EMA EPAR database
- **Patient selection criteria**: Develop a protocol requiring PFO screening (contrast-enhanced TCD or bubble echocardiogram) prior to enrolment, to enrich the target population for the peripheral antiplatelet mechanism
- **Pharmacogenomic screening**: Consider CYP2C19 genotyping, as poor metabolisers may have substantially reduced clopidogrel efficacy and could require dose adjustment or alternative P2Y12 inhibitor selection
- **Trial monitoring**: Await results of SPRING (NCT04946734, expected September 2025) and COMPETE (NCT05546320) trials, which will provide pivotal comparative data positioning clopidogrel against PFO closure and migraine-specific therapies
- **Subtype-specific study**: Design a prospective registry or feasibility study specifically targeting migraine with brainstem aura + PFO to generate subtype-level evidence currently absent from the literature
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

