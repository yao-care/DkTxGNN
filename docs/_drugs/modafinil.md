---
layout: default
title: Modafinil
parent: 僅模型預測 (L5)
nav_order: 242
evidence_level: L5
indication_count: 2
---

# Modafinil
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

# Modafinil: From Narcolepsy/Excessive Daytime Sleepiness to Insomnia

> ⚠️ **Analyst Note — High-Risk False Positive Flag:** This TxGNN prediction has been flagged as a likely mechanistic false positive. Modafinil is a wake-promoting agent; its pharmacological mechanism is the *opposite* of what is required to treat insomnia. This report documents the evidence in full and supports a **Hold** decision.

---

## One-Sentence Summary

Modafinil is a wake-promoting agent approved in many countries for narcolepsy, shift work sleep disorder, and obstructive sleep apnoea-related excessive daytime sleepiness.
The TxGNN model predicts it may be effective for **Insomnia**, achieving a prediction score of **99.85%**; however, this prediction is considered a probable false positive, as insomnia is listed as a *known adverse event* of modafinil (incidence 5–15%), not a therapeutic target.
No clinical trials or dedicated publications specifically testing modafinil as an insomnia treatment were identified; the **19 publications** retrieved address modafinil's established uses in wakefulness and overlapping sleep-disorder contexts.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Narcolepsy; shift work sleep disorder; excessive daytime sleepiness associated with obstructive sleep apnoea |
| Predicted New Indication | Insomnia (disease) |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L5 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why This Prediction Is Likely Incorrect

Modafinil promotes wakefulness through at least three known mechanisms: (1) inhibition of the dopamine transporter (DAT), increasing synaptic dopamine; (2) up-regulation of hypothalamic histamine release; and (3) activation of orexin/hypocretin neurons in the lateral hypothalamus. The net effect is sustained alertness and reduced sleep propensity.

The therapeutic goal in insomnia is precisely the opposite — facilitating sleep onset and maintaining sleep continuity. Because insomnia and the disorders modafinil actually treats (narcolepsy, excessive daytime sleepiness) both fall under the broad ICD category of "sleep disorders," the TxGNN model very likely confused the two directions within the same disease cluster. Insomnia appears as a **common adverse event** in modafinil prescribing information (reported in 5–15% of patients in clinical trials), confirming that the drug exacerbates, rather than alleviates, insomnia.

The 19 PubMed publications identified by the search query were retrieved under a broad modafinil + sleep-disorder search strategy. On closer inspection they address: modafinil for excessive daytime sleepiness in Parkinson's disease, narcolepsy management, fatigue in neurological conditions, and shift work sleep disorder — none of which constitutes evidence for modafinil as an insomnia treatment. No dedicated randomised or observational study testing modafinil for primary insomnia was found.

---

## Clinical Trial Evidence

No clinical trials investigating modafinil for the treatment of insomnia were identified in ClinicalTrials.gov or the ICTRP registry.

---

## Literature Evidence

The publications below were retrieved via a modafinil + insomnia search. They primarily document modafinil's **established wake-promoting uses** and related sleep-disorder contexts. None constitutes evidence supporting modafinil as a treatment for insomnia; several are directly relevant to understanding why this TxGNN prediction should be rejected.

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|------------|
| [22021174](https://pubmed.ncbi.nlm.nih.gov/22021174/) | 2011 | Systematic Review / EBM Guideline | *Movement Disorders* | MDS evidence-based review of non-motor symptom treatments in Parkinson's disease, including sleep and daytime sleepiness; modafinil reviewed for EDS, not insomnia |
| [27010071](https://pubmed.ncbi.nlm.nih.gov/27010071/) | 2016 | Systematic Review | *Parkinsonism & Related Disorders* | Meta-analysis of pharmacological interventions for daytime sleepiness and sleep disorders in PD; modafinil assessed for EDS |
| [24312590](https://pubmed.ncbi.nlm.nih.gov/24312590/) | 2013 | Systematic Review | *PLoS ONE* | Modafinil for fatigue and excessive daytime sleepiness in neurological disorders; confirms wake-promoting (not sleep-inducing) efficacy |
| [18729534](https://pubmed.ncbi.nlm.nih.gov/18729534/) | 2008 | Narrative Review | *Drugs* | Comprehensive review of approved and investigational uses of modafinil; covers narcolepsy, SWSD, OSA-EDS, and off-label uses — insomnia treatment not among them |
| [39535843](https://pubmed.ncbi.nlm.nih.gov/39535843/) | 2024 | Review | *Expert Opinion on Pharmacotherapy* | Pharmacological and non-pharmacological management of sleep disturbances in Parkinson's disease |
| [18219235](https://pubmed.ncbi.nlm.nih.gov/18219235/) | 2008 | Randomised Trial | *J Head Trauma Rehabilitation* | RCT of modafinil for fatigue and excessive daytime sleepiness in chronic traumatic brain injury; outcome is wakefulness improvement, not insomnia relief |
| [17181377](https://pubmed.ncbi.nlm.nih.gov/17181377/) | 2006 | Review | *Drugs* | Shift work sleep disorder: burden of illness and management approaches; modafinil discussed as approved treatment for shift-work EDS |
| [18805301](https://pubmed.ncbi.nlm.nih.gov/18805301/) | 2008 | Review | *Revue Neurologique* | Narcolepsy with cataplexy — clinical features and treatment; modafinil as first-line for EDS in narcolepsy; sleep-maintenance insomnia listed as a narcolepsy symptom, not a modafinil target |
| [26483900](https://pubmed.ncbi.nlm.nih.gov/26483900/) | 2014 | Case Report | *Sleep Science* | Cataplexy as a side effect of modafinil in a patient without narcolepsy — highlights potential adverse CNS effects |
| [17060310](https://pubmed.ncbi.nlm.nih.gov/17060310/) | 2006 | Case Series | *Am J Hospice & Palliative Care* | Modafinil reduces fatigue in Charcot-Marie-Tooth disease type 1A; off-label use for fatigue, not insomnia |

---

## Denmark Market Information

Modafinil is **not marketed in Denmark**. The Danish Medicines Agency (Lægemiddelstyrelsen) holds no active marketing authorisations for modafinil as of the data cut-off date (2026-04-04). The drug is also not registered under a centralised EMA authorisation for the Danish market.

Modafinil holds marketing authorisations in several other countries (e.g., United States: Provigil®; United Kingdom: Provigil®; France: Modiodal®) for narcolepsy, obstructive sleep apnoea-related EDS, and shift work sleep disorder, but these do not confer Danish marketing rights.

---

## Safety Considerations

Detailed prescribing information (SmPC) for modafinil is not available within this Evidence Pack. Please refer to the Summary of Product Characteristics of an authorised product (e.g., EMA or MHRA SmPC for Provigil®) for full safety information, including:

- Known adverse events (notably **insomnia, headache, nausea, anxiety, palpitations**)
- Psychiatric and cardiovascular contraindications
- CYP3A4-mediated drug–drug interactions
- Pregnancy and lactation restrictions

Importantly, insomnia is listed as a **common adverse effect** of modafinil in approved prescribing information, which further contradicts the TxGNN prediction.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction of modafinil for insomnia is assessed as a **high-probability false positive** arising from model confusion within the "sleep disorder" disease cluster. Modafinil's mechanism of action (DAT inhibition, histamine up-regulation, orexin activation) is diametrically opposed to the pharmacological goal of insomnia treatment, and insomnia is a documented adverse effect of the drug. No clinical trial or dedicated publication supporting this repurposing hypothesis was identified. Modafinil is also not authorised in Denmark, meaning any clinical development pathway would require a full de novo regulatory application.

**To proceed, the following would be needed (purely hypothetical threshold):**
- A credible biological hypothesis explaining how a wake-promoting agent could benefit insomnia (e.g., via a specific insomnia subtype such as hypersomnia-insomnia overlap) — currently absent
- At minimum one exploratory clinical study or case series specifically demonstrating sleep-onset or sleep-maintenance improvement with modafinil in an insomnia population
- Clarification of the TxGNN model's disease-node disambiguation between "sleep disorder — hypersomnolence" and "sleep disorder — insomnia" to resolve the likely false-positive classification
- Full MOA data from DrugBank to formally complete the mechanistic plausibility assessment

> *This report is intended for research purposes only and does not constitute medical advice. All drug repurposing candidates require prospective clinical validation before any therapeutic application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

