---
layout: default
title: Bromazepam
parent: 僅模型預測 (L5)
nav_order: 78
evidence_level: L5
indication_count: 2
---

# Bromazepam
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Bromazepam: From Anxiety Disorders to Migraine Disorder

## One-Sentence Summary

Bromazepam is a benzodiazepine (BZD) belonging to the anxiolytic/sedative drug class, widely used internationally for the management of anxiety disorders and psychosomatic tension states.
The TxGNN model predicts it may be effective for **Migraine Disorder**, with a prediction score of **99.06%**; however, only **1 clinical trial** has been identified — and critically, this trial represents **negative evidence** (bromazepam as the drug being withdrawn, not the treatment) — and **no supporting publications** have been found.
Given the weak mechanistic rationale and absence of direct supportive evidence, a **Hold** decision is recommended at this stage.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Anxiety disorders / psychosomatic tension (bromazepam's established use as a BZD anxiolytic; formal indication text unavailable in this data package) |
| Predicted New Indication | Migraine Disorder |
| TxGNN Prediction Score | 99.06% |
| Evidence Level | L4 (mechanistic/preclinical only — no direct supportive studies) |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Bromazepam is a positive allosteric modulator at the GABA-A receptor (benzodiazepine binding site). Theoretically, two mechanisms could be relevant to migraine: (1) its anxiolytic effect may reduce cortical hyperexcitability that is known to lower the migraine threshold; and (2) its muscle-relaxant properties may alleviate the tension-type headache component often co-occurring with migraine.

However, these proposed links are indirect at best. The primary neurobiological pathway in migraine involves the trigeminovascular system — specifically serotonin (5-HT) receptor modulation and calcitonin gene-related peptide (CGRP) signalling — neither of which is a pharmacological target of bromazepam. The TxGNN high prediction score likely reflects graph-level co-occurrence patterns (e.g., anxiety and migraine being frequently comorbid conditions) rather than a direct mechanistic connection.

Most importantly, evidence from clinical practice points in the opposite direction: chronic benzodiazepine use leads to GABA-A receptor downregulation and central sensitisation, which are established drivers of **Medication Overuse Headache (MOH)**. Rather than treating migraine, long-term bromazepam use may actively worsen the clinical picture. The sole clinical trial identified in this evidence pack explicitly studies bromazepam withdrawal as part of MOH management, underscoring this concern.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|-------------|
| [NCT04410536](https://clinicaltrials.gov/study/NCT04410536) | Phase 4 | Completed | 25 | Home-withdrawal programme combined with behavioural therapy for Medication Overuse Headache (MOH) during COVID-19. Bromazepam appears as a **drug being withdrawn**, not a treatment intervention. This trial constitutes **negative evidence** — it highlights bromazepam as a causative agent in MOH rather than a migraine therapy. |

> ⚠️ **Important note:** The only identified trial does not support bromazepam as a migraine treatment. On the contrary, it reinforces the concern that benzodiazepine overuse causes a disabling headache disorder affecting approximately 2% of the migraine population.

---

## Literature Evidence

Currently no related literature is available supporting bromazepam as a treatment for migraine disorder.

---

## Denmark Market Information

Bromazepam currently holds **no marketing authorisations** in Denmark (neither national authorisations from the Danish Medicines Agency / Lægemiddelstyrelsen nor centralised EMA authorisations). The drug is **not marketed** in Denmark.

---

## Safety Considerations

Detailed product-specific warnings and contraindications are not available in this data package. Please refer to the approved **Summary of Product Characteristics (SmPC)** for full safety information.

Based on the drug class (benzodiazepines), the following class-level concerns are clinically relevant for this repurposing assessment:

- **Dependence and withdrawal**: Benzodiazepines carry a well-established risk of physical dependence, tolerance, and potentially severe withdrawal syndromes — particularly relevant in chronic migraine patients who may require long-term therapy.
- **Medication Overuse Headache (MOH)**: Chronic benzodiazepine use is a recognised cause of MOH, which is directly counterproductive in the proposed migraine indication.
- **CNS depression**: Risk of sedation, cognitive impairment, and psychomotor slowing — important for patient daily functioning and driving ability.
- **Pregnancy and lactation**: BZDs are generally contraindicated in pregnancy; migraine disproportionately affects women of childbearing age, making this a significant safety concern for the target population.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model assigns a high prediction score (99.06%), but the available evidence does not support repurposing bromazepam for migraine. The sole identified clinical trial constitutes negative evidence (bromazepam as the overused drug causing MOH, not a treatment), no supportive literature exists, and the mechanistic rationale is indirect. Furthermore, long-term benzodiazepine use is a recognised risk factor for worsening headache burden through MOH — the pharmacological effect is directly contrary to the therapeutic goal.

**To re-evaluate this candidate, the following would be needed:**

- **Mechanistic clarification**: Peer-reviewed evidence demonstrating a direct mechanistic link between GABA-A potentiation and migraine pathophysiology (trigeminovascular/CGRP pathway), not merely anxiety–migraine comorbidity
- **Prospective clinical data**: At minimum a controlled pilot study with bromazepam as the active intervention for acute or prophylactic migraine treatment — none currently exists
- **MOH risk mitigation strategy**: A credible clinical protocol that addresses the paradoxical risk of inducing medication overuse headache in the very population being treated
- **Safety data**: Complete SmPC-level warnings and contraindications (currently unavailable in this data package — classified as a blocking data gap)
- **Regulatory pathway assessment**: Given that bromazepam is not marketed in Denmark and carries Schedule IV-equivalent scheduling concerns, a regulatory feasibility review would be required before any clinical investigation

> *This report is intended for research purposes only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical application. All content should be reviewed in conjunction with the full approved SmPC.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

