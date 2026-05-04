---
layout: default
title: Droperidol
parent: 僅模型預測 (L5)
nav_order: 151
evidence_level: L5
indication_count: 10
---

# Droperidol
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

# Droperidol: From Acute Psychosis / Procedural Sedation to Tourette Syndrome

## One-Sentence Summary

Droperidol is a butyrophenone-class antipsychotic/neuroleptic traditionally used internationally for rapid tranquilisation of acutely agitated patients and as an adjunct in procedural sedation and anaesthesia, though it is not currently marketed in Denmark.
The TxGNN model predicts it may be effective for **Tourette Syndrome**, with **0 clinical trials** and **1 publication** currently supporting this specific direction — the evidence is based primarily on mechanistic analogy with the related butyrophenone drug haloperidol, which holds FDA approval for Tourette syndrome.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Denmark; internationally recognised for acute agitation/sedation and adjunct anaesthesia |
| Predicted New Indication | Tourette Syndrome |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L4 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data for droperidol is not available in the Evidence Pack. Based on known pharmacological information, droperidol is a butyrophenone-class dopamine D2 receptor antagonist — the same drug class as haloperidol, which has received FDA approval for the treatment of Tourette syndrome. Both agents block striatal dopamine D2 receptors, and this shared mechanism forms the basis of the TxGNN model's prediction: reduced dopaminergic overactivity in the mesolimbic and nigrostriatal pathways is thought to suppress the involuntary motor and vocal tics that define Tourette syndrome.

The class-effect hypothesis is therefore mechanistically coherent. However, it is important to note that droperidol and haloperidol, while sharing the same pharmacological class, differ significantly in their pharmacokinetic profiles, receptor binding affinity, duration of action, and clinical use context. Haloperidol is administered orally for chronic management of Tourette syndrome, whereas droperidol is primarily used as a short-acting parenteral agent for acute settings — which raises questions about route compatibility and dosing feasibility for a chronic neurological indication.

Critically, there are currently no clinical trials and no published studies examining droperidol directly in patients with Tourette syndrome. The single literature item retrieved is a 1976 study on haloperidol — not droperidol — and serves only to illustrate the class-level mechanistic rationale. QTc interval prolongation is a well-documented and serious safety concern with droperidol (resulting in a US FDA Black Box Warning), which adds a further barrier to any repurposing investigation in a paediatric-predominant population such as Tourette syndrome patients.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [791589](https://pubmed.ncbi.nlm.nih.gov/791589/) | 1976 | Clinical Study | Current Psychiatric Therapies | Haloperidol (a butyrophenone class-mate of droperidol) evaluated in severe behavioural disorders — provides indirect mechanistic analogy for D2 antagonism in tic-related conditions; **does not directly study droperidol** |

---

## Denmark Market Information

Droperidol is **not currently marketed in Denmark**. No marketing authorisations have been granted by the Danish Medicines Agency (Lægemiddelstyrelsen), and no centralised EMA authorisations are active for this drug in Denmark. Any future repurposing use would require either a new marketing authorisation application or a named-patient / compassionate use pathway.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

> **Important contextual note:** The repurposing rationale analysis flags **QTc interval prolongation** as a clinically significant safety concern with droperidol. This has previously led to a US FDA Black Box Warning and withdrawal or restriction of the product in several markets. Any safety screening for new indications — particularly in populations that include children and adolescents (as with Tourette syndrome) — must prioritise cardiac safety evaluation, including baseline and on-treatment ECG monitoring.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction for Tourette syndrome is mechanistically coherent as a class-effect hypothesis (butyrophenone D2 antagonism shared with haloperidol), but there is no direct clinical evidence supporting the use of droperidol specifically in Tourette syndrome. With an evidence level of L4 (mechanistic analogy only), a paediatric-predominant patient population, and a known cardiac safety risk (QTc prolongation), the threshold for proceeding is not yet met.

**To proceed, the following is needed:**

- **MOA confirmation:** Retrieve full DrugBank pharmacology data to formally document D2 receptor binding profile and compare with haloperidol's Tourette syndrome activity
- **Safety screening (S1):** Obtain full SmPC / TFDA package insert to complete the blocking safety gap (DG001) — in particular, QTc-related contraindications and warnings
- **Literature gap assessment:** Conduct a systematic PubMed search specifically for droperidol AND Tourette syndrome (or Gilles de la Tourette) to confirm absence of any unpublished or foreign-language evidence
- **Route compatibility analysis:** Evaluate whether an oral or alternative formulation of droperidol exists or could be developed for chronic administration, given the indication's need for long-term management
- **Paediatric safety review:** Assess cardiac risk in the Tourette syndrome patient demographic (predominantly children and adolescents) before any prospective feasibility work is initiated

---

> **Additional signal of interest:** Among the five unique predicted indications in this Evidence Pack, **manic bipolar affective disorder** (TxGNN score: 99.82%, Evidence Level: L3) carries substantially stronger evidence, including two Cochrane systematic reviews (PMID [11406047](https://pubmed.ncbi.nlm.nih.gov/11406047/), [27976370](https://pubmed.ncbi.nlm.nih.gov/27976370/)) and direct case series describing oral droperidol use in treatment-refractory mania (PMID [9789713](https://pubmed.ncbi.nlm.nih.gov/9789713/)). A dedicated repurposing report for the manic bipolar affective disorder indication is recommended and may warrant a **Proceed with Guardrails** designation pending full safety review.

---

*This report is for research reference purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before any therapeutic application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

