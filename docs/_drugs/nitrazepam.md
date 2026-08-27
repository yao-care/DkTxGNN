---
layout: default
title: Nitrazepam
parent: 僅模型預測 (L5)
nav_order: 310
evidence_level: L5
indication_count: 6
---

# Nitrazepam
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Nitrazepam: From Unregistered Original Indication to Sleep Disorder, Initiating and Maintaining Sleep (Insomnia)

## One-Sentence Summary

Nitrazepam's own approved indication is not on record in this Evidence Pack (`original_indications` is a data gap), but it is a long-marketed benzodiazepine hypnotic (Mogadon). The TxGNN model predicts it is effective for **Sleep Disorder, Initiating and Maintaining Sleep** (insomnia) with a **99.89%** prediction score, supported by **20 publications** (including 1 RCT) and **no registered clinical trials**. Note: this predicted indication overlaps with nitrazepam's well-known historical use, so the finding should be read as a confirmation of known pharmacology rather than a novel repurposing signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on record (data gap — no `original_indications` entries; drug is not currently marketed in Denmark) |
| Predicted New Indication | Sleep Disorder, Initiating and Maintaining Sleep (Insomnia) |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L2 |
| Denmark Market Status | Not Marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

The `original_moa` field is a data gap, but the model's own repurposing rationale supplies the mechanism: nitrazepam is a classic benzodiazepine that binds the benzodiazepine site on the GABA-A receptor's α subunit, positively modulating GABA-gated chloride influx and enhancing central inhibitory neurotransmission. This produces sedative, hypnotic, anxiolytic, anticonvulsant and muscle-relaxant effects.

Importantly, the "predicted new indication" here — sleep-onset and sleep-maintenance insomnia — is not actually a new therapeutic hypothesis. Nitrazepam has been marketed for decades under the brand name Mogadon specifically as a hypnotic for insomnia. The literature evidence below (pharmacokinetics reviews, a head-to-head RCT against triazolam, safety reviews) reflects this established use rather than an unproven extrapolation. The apparent "prediction" arises because the `original_indications` field in this Evidence Pack is empty (data gap), so the model/report pipeline is unable to recognize that this is already the drug's core indication.

Mechanistically the link is therefore direct and well-established, not inferred: GABA-A receptor potentiation reduces sleep latency and increases total sleep time, consistent with nitrazepam's known clinical pharmacology.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [6135296](https://pubmed.ncbi.nlm.nih.gov/6135296/) | 1983 | RCT | Acta Psychiatrica Scandinavica | Double-blind cross-over in 26 geriatric inpatients: nitrazepam 5mg vs triazolam 0.25mg — comparable sleep quantity/quality and psychomotor performance |
| [7037262](https://pubmed.ncbi.nlm.nih.gov/7037262/) | 1981 | Review | Clinical Pharmacokinetics | Review of nitrazepam's clinical pharmacokinetics |
| [4892037](https://pubmed.ncbi.nlm.nih.gov/4892037/) | 1969 | Review | British Medical Journal | 27 patients with acute nitrazepam overdose (up to 80 tablets) showed only drowsiness; double-blind trial found nitrazepam as effective as butobarbitone as a hypnotic |
| [1125532](https://pubmed.ncbi.nlm.nih.gov/1125532/) | 1975 | Case Report | British Journal of Psychiatry | Case report of nitrazepam (Mogadon) dependence |
| [4712500](https://pubmed.ncbi.nlm.nih.gov/4712500/) | 1973 | Case Report | British Medical Journal | Case report on nitrazepam's effects on dreaming/subconscious content |
| [238826](https://pubmed.ncbi.nlm.nih.gov/238826/) | 1975 | Review | Drugs | Review of sleep physiology and hypnotic drug efficacy assessment |
| [19450355](https://pubmed.ncbi.nlm.nih.gov/19450355/) | 2007 | Review | BMJ Clinical Evidence | Up to 40% of adults have insomnia; prevalence rises with age; risk factors include psychological stress and hyperarousal |
| [7725291](https://pubmed.ncbi.nlm.nih.gov/7725291/) | 1995 | Review | Tidsskrift for den Norske Laegeforening | Review of insomnia classification, diagnosis and treatment developments |
| [15089115](https://pubmed.ncbi.nlm.nih.gov/15089115/) | 2004 | Review | CNS Drugs | Review of residual "hangover" effects of hypnotics (daytime sleepiness, psychomotor/cognitive impairment) and accident risk |
| [39231170](https://pubmed.ncbi.nlm.nih.gov/39231170/) | 2024 | — | PLoS ONE | Study of inappropriate benzodiazepine prescribing patterns in primary care, including dependence and cognitive-decline risk in older adults |

---

## Denmark Market Information

Nitrazepam has **0 marketing authorisations** on file and is currently **not marketed** in Denmark. No Laegemiddelstyrelsen or EMA centralised authorisation records are available in this Evidence Pack.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information. No key warnings, contraindications, or drug-drug interaction data are currently on file (DDI query status: not found).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Literature evidence (including a direct RCT of nitrazepam as a hypnotic) supports plausibility for insomnia, but this largely reconfirms nitrazepam's known, decades-old clinical use rather than establishing a genuinely new indication. Critical data gaps — no Danish SmPC/warnings/contraindications (Blocking, DG001), no formal MOA record (High, DG002), and no confirmed original indication — block any registration-level decision, and the drug is not currently marketed in Denmark.

**To proceed, the following is needed:**
- Danish/EU SmPC warnings, contraindications and DDI data (resolve DG001, blocking)
- Formal MOA documentation via DrugBank (resolve DG002)
- Confirmation of nitrazepam's actual approved indication(s) in source markets, to clarify whether this is a genuine new-use signal or a data-registration gap
- Marketing-authorisation pathway assessment given current "Not Marketed" status in Denmark

*Note: The model also flagged two lower-confidence candidates — acute encephalopathy with biphasic seizures and late reduced diffusion (AESD) and Wernicke-Korsakoff syndrome — both at Evidence Level L5 with no supporting literature or trials; both are recommended **Hold**.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

