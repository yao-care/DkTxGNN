---
layout: default
title: Apixaban
parent: 僅模型預測 (L5)
nav_order: 41
evidence_level: L5
indication_count: 10
---

# Apixaban
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

# Apixaban: From Anticoagulation (Atrial Fibrillation / VTE) to Migraine Disorder

## One-Sentence Summary

Apixaban is a direct oral Factor Xa inhibitor (DOAC) approved internationally (Eliquis®) for the prevention of stroke in non-valvular atrial fibrillation, and for the treatment and prevention of venous thromboembolism (DVT and PE). The TxGNN model predicts it may be effective for **Migraine Disorder**, with **1 indirectly relevant clinical trial** and **4 publications** (including 1 small retrospective trial and 3 case reports) currently available — though notably, two case reports suggest Apixaban may be *less* effective than warfarin in this context. The overall body of evidence is weak, with several negative clinical signals, and the current recommendation is **Hold** pending further mechanistic and clinical investigation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Prevention of stroke/systemic embolism in non-valvular atrial fibrillation; treatment and prevention of DVT/PE; VTE prophylaxis after hip/knee replacement surgery |
| Predicted New Indication | Migraine Disorder |
| TxGNN Prediction Score | 99.02% |
| Evidence Level | L4 (preclinical/mechanistic studies and case reports only) |
| Denmark Market Status | Not marketed (0 authorisations on record in this dataset) |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

> **Note on Denmark registration:** The Evidence Pack records no active marketing authorisations in Denmark. However, Apixaban (Eliquis®) holds a centralised EMA authorisation (EU/1/11/728) that is valid across all EU/EEA member states including Denmark. This likely reflects a data gap in the current dataset rather than a genuine absence from the Danish market. Verification against the Danish Medicines Agency (Lægemiddelstyrelsen) product database is recommended.

---

## Why is This Prediction Reasonable?

Apixaban is a selective, reversible inhibitor of activated Factor X (FXa), a critical convergence point in both the intrinsic and extrinsic coagulation cascades. By blocking FXa, apixaban reduces thrombin generation and fibrin clot formation without directly inhibiting thrombin itself — a key distinction from vitamin K antagonists such as warfarin.

The hypothesised link to migraine rests on two mechanistic threads. First, in patients with patent foramen ovale (PFO), paradoxical microemboli passing through the right-to-left shunt may trigger cortical spreading depression and migraine aura. Anticoagulation could theoretically reduce the microembolic burden and thereby attenuate aura frequency. Second, FXa is known to activate protease-activated receptors PAR-1 and PAR-2 on trigeminal neurons and vascular endothelium; inhibiting FXa could theoretically dampen trigeminovascular neuroinflammation, a central mechanism in migraine pathophysiology.

However, the clinical picture is complicated by a meaningful negative signal: two case reports directly compare warfarin and apixaban in the same patients, and in both cases warfarin abolished migraine with aura while apixaban did not. This suggests that the relevant target may be thrombin rather than FXa — a pathway that warfarin suppresses broadly but apixaban does not. This substantially weakens the mechanistic rationale specifically for apixaban, even if broader anticoagulation may have migraine-related benefits.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT00562289](https://clinicaltrials.gov/study/NCT00562289) | Phase 3 | Completed | 664 | CLOSE trial: Compared PFO closure vs. oral anticoagulants vs. antiplatelet therapy for secondary stroke prevention. Primary endpoint was stroke recurrence, **not migraine**. Anticoagulants included as a treatment arm but apixaban was not specifically evaluated; migraine was not a primary or secondary endpoint. This trial provides indirect, class-level background evidence only (Relevance Grade C). |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [33402037](https://pubmed.ncbi.nlm.nih.gov/33402037/) | 2021 | Small Trial / Pilot | *Lupus* | Retrospective study of 75 patients with refractory migraine and antiphospholipid antibodies (aPL): evaluated symptomatic response to antithrombotic therapy. Patients with aPL and refractory migraine may respond to anticoagulation, but apixaban was not specifically isolated; general antithrombotic class effect was assessed. |
| [37582651](https://pubmed.ncbi.nlm.nih.gov/37582651/) | 2023 | Case Report | *The Neurologist* | Migraine with aura **worsened** after initiating apixaban. Includes a literature review noting that the impact of DOACs on migraine is unclear and evidence is scarce and contradictory — a direct **negative signal** for apixaban. |
| [28960288](https://pubmed.ncbi.nlm.nih.gov/28960288/) | 2017 | Case Report | *Headache* | 55-year-old woman had complete remission of migraine with aura for 12 years on warfarin; symptoms returned within 3 weeks of switching to apixaban, and resolved again within days of resuming warfarin. Strongly suggests thrombin (not FXa) is the relevant anticoagulant target — a direct **negative signal** for apixaban specifically. |
| [29611190](https://pubmed.ncbi.nlm.nih.gov/29611190/) | 2018 | Case Report | *Headache* | Vestibular migraine resolving on warfarin and topiramate. Provides indirect class-level evidence for anticoagulation in migraine but does not evaluate apixaban. |

---

## Denmark Market Information

No marketing authorisations are recorded for apixaban in this dataset. As noted above, this is likely a data gap; the EMA centrally authorised product Eliquis® (apixaban) is marketed throughout the EU/EEA. Healthcare professionals in Denmark should consult the Lægemiddelstyrelsen product database or the EMA product page for the current SmPC and approved indications.

---

## Safety Considerations

Safety data (key warnings, contraindications, and drug-drug interactions) are not available in this Evidence Pack.

> Please refer to the approved Summary of Product Characteristics (SmPC) for Eliquis® (apixaban) for full safety information, including haemorrhagic risk, renal dose adjustments, interactions with strong CYP3A4/P-gp inhibitors and inducers, and contraindications in pregnancy.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic hypothesis linking apixaban to migraine is speculative and is actively contradicted by the best available clinical evidence: two head-to-head case comparisons demonstrate that warfarin, but not apixaban, suppresses migraine with aura in the same individual. This pattern implies that thrombin inhibition — not FXa inhibition — may underlie any anticoagulant benefit in migraine, which is mechanistically outside apixaban's pharmacological scope. No dedicated prospective trials exist, and the single relevant Phase 3 trial (NCT00562289) did not evaluate apixaban or include migraine as an endpoint.

**To proceed, the following would be needed:**
- Mechanistic clarification: Does FXa inhibition specifically (vs. thrombin suppression) reduce trigeminovascular activation in validated migraine models? Preclinical studies targeting this distinction are absent.
- Head-to-head comparison data: A prospective study comparing apixaban, warfarin, and antiplatelet therapy in PFO-associated migraine with aura is needed to disentangle drug-class effects from molecule-specific effects.
- Patient subgroup identification: If further investigation is pursued, the most plausible population is PFO-positive patients with refractory migraine with aura and documented microemboli — not the general migraine population.
- Full safety profile: Obtain the complete SmPC to enable a formal S1 safety assessment, particularly regarding bleeding risk in a population that would otherwise not require anticoagulation.
- Denmark regulatory data: Verify and update the Lægemiddelstyrelsen registration status to resolve the apparent data gap in this Evidence Pack.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

