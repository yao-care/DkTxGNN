---
layout: default
title: Oxazepam
parent: 僅模型預測 (L5)
nav_order: 324
evidence_level: L5
indication_count: 2
---

# Oxazepam
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

# Oxazepam: From Benzodiazepine Anxiolytic/Sedative Use to Insomnia

## One-Sentence Summary

Oxazepam is a short-acting benzodiazepine whose original approved indication is not recorded in this evidence pack (regulatory data gap). The TxGNN model predicts it may be effective for **Insomnia**, with **0 registered clinical trials** and **11 publications** currently supporting this direction, several of which directly evaluate oxazepam in insomnia populations.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in evidence pack (TFDA label unavailable — see data gap DG001) |
| Predicted New Indication | Insomnia |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L3 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Oxazepam is a short-acting benzodiazepine. Its pharmacological action works by enhancing GABA-A receptor chloride-channel conductance, producing sedative, anxiolytic, and hypnotic effects. This is the core mechanism shared by the entire benzodiazepine class, not a cross-mechanism inference — sedative-hypnotic activity is a direct, on-target effect of the drug rather than a novel or unexpected pharmacological link.

Because benzodiazepines are already established pharmacologically as sleep-promoting agents, the relationship between oxazepam and insomnia is mechanistically direct rather than speculative. The very high TxGNN score (99.86%) reflects this — it identifies a pharmacologically "obvious" association rather than a genuinely novel repurposing signal.

Currently, a formally documented mechanism-of-action record and original indication text are not available in this evidence pack (data gaps DG001/DG002). Based on known pharmacological class information, however, oxazepam's GABA-A agonism is well-established, and this mechanism plausibly supports its use in insomnia, consistent with published clinical literature on the drug.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [6691478](https://pubmed.ncbi.nlm.nih.gov/6691478/) | 1984 | RCT | The American Journal of Psychiatry | In 14 chronic insomnia patients, oxazepam improved polysomnographic sleep measures without causing the daytime sleepiness seen with flurazepam |
| [29749262](https://pubmed.ncbi.nlm.nih.gov/29749262/) | 2018 | RCT | The Annals of Pharmacotherapy | Randomized trial comparing melatonin and oxazepam for anxiety and sleep quality in STEMI patients post-PCI |
| [17317444](https://pubmed.ncbi.nlm.nih.gov/17317444/) | 2007 | Review | Archives of Gerontology and Geriatrics | Reviews effectiveness and safety of hypnotic drugs, including benzodiazepines, for insomnia in patients over 70 |
| [23330992](https://pubmed.ncbi.nlm.nih.gov/23330992/) | 2013 | Review | Expert Opinion on Drug Metabolism & Toxicology | Reviews pharmacokinetics of anxiolytic/hypnotic drugs including benzodiazepines |
| [29844949](https://pubmed.ncbi.nlm.nih.gov/29844949/) | 2018 | Review | PeerJ | Examines factors associated with long-term benzodiazepine and z-drug use, including oxazepam, in elderly populations |
| [36340306](https://pubmed.ncbi.nlm.nih.gov/36340306/) | 2022 | Review | Journal of Clinical and Experimental Hepatology | Discusses management of alcohol withdrawal syndrome, where insomnia is a key symptom managed with benzodiazepines |
| [15633073](https://pubmed.ncbi.nlm.nih.gov/15633073/) | 2005 | Review | Psychiatrische Praxis | Survey of therapeutic practice for behavioral/sleep disturbances in dementia (BPSD), including benzodiazepine use |
| [23338224](https://pubmed.ncbi.nlm.nih.gov/23338224/) | 1997 | Review | CNS Drugs | Reviews pharmacology of anxiolytic agents in panic disorder, contextualizing benzodiazepine alternatives |
| [6139491](https://pubmed.ncbi.nlm.nih.gov/6139491/) | 1983 | Cohort | JAMA | Reports withdrawal symptoms after substituting oxazepam for long-acting benzodiazepines, including sleep disturbance |
| [39544757](https://pubmed.ncbi.nlm.nih.gov/39544757/) | 2024 | Case Report | American Journal of Translational Research | Case report of a sensory adverse effect with a sedative-related agent (agomelatine), included as background CNS/sleep-drug context |

---

## Denmark Market Information

Oxazepam currently holds no marketing authorisations in Denmark (0 registered, not marketed).

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic link between oxazepam (a GABA-A-acting benzodiazepine) and insomnia is pharmacologically direct and well-supported by published literature, including two RCTs specifically evaluating oxazepam in sleep-related outcomes. However, no clinical trials have been registered for this specific indication, and key regulatory safety data (TFDA warnings/contraindications) and formal MOA documentation are currently missing, limiting formal safety review.

**To proceed, the following is needed:**
- TFDA/SmPC label data on warnings, contraindications, and precautions (DG001, blocking for safety review)
- Formal, sourced mechanism-of-action documentation (DG002)
- Drug-drug interaction (DDI) data, since the current query returned no results
- Assessment of a Danish regulatory pathway, given the drug is not currently marketed in Denmark
- Standard benzodiazepine-class risk evaluation (dependence, withdrawal, elderly fall risk) as part of any formal safety dossier
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

