---
layout: default
title: Glucagon
parent: 僅模型預測 (L5)
nav_order: 209
evidence_level: L5
indication_count: 2
---

# Glucagon
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

# Glucagon: From Severe Hypoglycaemia to Irritable Bowel Syndrome

## One-Sentence Summary

Glucagon (DB00040) is a peptide hormone derived from the proglucagon precursor, clinically established as a rescue agent for severe hypoglycaemia and as a gastrointestinal spasmolytic agent during diagnostic procedures.
The TxGNN model predicts it may be effective for **Irritable Bowel Syndrome (IBS)**, with **11 clinical trials** and **20 publications** identified in support — however, the critical caveat is that the vast majority of this evidence relates to **GLP-1 receptor agonists** (ROSE-010, liraglutide, exendin-4) acting via a distinct receptor, not glucagon itself.
Evidence is graded **L3** (systematic reviews and observational data), and the mechanistic target requires urgent clarification before any repurposing programme is initiated.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Severe hypoglycaemia rescue (established clinical use; not currently registered in Denmark) |
| Predicted New Indication | Irritable Bowel Syndrome (IBS) |
| TxGNN Prediction Score | 99.24% |
| Evidence Level | L3 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Glucagon and glucagon-like peptide-1 (GLP-1) are both produced from the same precursor protein, proglucagon, through tissue-specific cleavage. In pancreatic alpha cells, proglucagon yields glucagon, which acts on the glucagon receptor (GCGR) to raise blood glucose. In intestinal L-cells, the same precursor is processed to produce GLP-1, which acts on GLP-1R to regulate gut motility, slow gastric emptying, reduce visceral pain sensitivity, and modulate the brain-gut axis. This shared molecular origin is most likely why TxGNN has drawn a connection between glucagon and IBS.

The underlying biological signal is real: GLP-1R activation inhibits the migrating motor complex, attenuates postprandial intestinal contractions, and reduces visceral hypersensitivity — mechanisms directly relevant to IBS pathophysiology. A 2025 systematic review and meta-analysis (PMID 40134805) confirms that GLP-1 receptor agonists improve IBS symptoms. The GLP-1 analogue ROSE-010, derived from the same proglucagon family, has completed Phase 1/2 trials in constipation-predominant IBS with encouraging results in pain reduction and gastrointestinal motor function.

However, a fundamental distinction must be stated clearly: **glucagon itself acts via GCGR, not GLP-1R**. The two receptors have different tissue distributions and signalling profiles. While glucagon has some historical use as a gastrointestinal spasmolytic (e.g., during colonoscopy), there is currently no independent clinical evidence validating glucagon *per se* as an IBS treatment. The evidence captured in this Evidence Pack represents a GLP-1 receptor agonist class effect that has been attributed — likely incorrectly — to the parent compound glucagon via knowledge graph proximity. This mechanistic gap is the primary reason for a Hold recommendation.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01056107](https://clinicaltrials.gov/study/NCT01056107) | Phase 1/2 | Completed | 52 | ROSE-010 (synthetic GLP-1 receptor agonist, proglucagon family) delays gastric emptying of solids and enhances gastric accommodation in female patients with constipation-predominant IBS; directly assesses gastrointestinal motor function as primary endpoint |
| [NCT02731664](https://clinicaltrials.gov/study/NCT02731664) | Phase 1 | Completed | 12 | Native GLP-1 inhibits prandial antro-duodeno-jejunal motility in humans; in vitro mechanistic comparison with ROSE-010 on gastrointestinal muscle strips provides mechanistic support for GLP-1 axis in gut motility — IBS is not the primary endpoint |
| [NCT04763564](https://clinicaltrials.gov/study/NCT04763564) | Phase 2 | Terminated | 8 | Liraglutide (GLP-1 receptor agonist) in patients with ileal pouch-anal anastomosis and chronic high bowel frequency; trial terminated early due to insufficient enrollment — limited conclusions possible |
| [NCT05249023](https://clinicaltrials.gov/study/NCT05249023) | N/A | Completed | 37 | Mechanistic study of butyrate in human colon health; IBS disease model is relevant context but no glucagon or GLP-1 drug intervention involved |
| [NCT06408610](https://clinicaltrials.gov/study/NCT06408610) | N/A | Completed | 66 | Moderate vs high-intensity exercise on gut dysbiosis and GLP-1 hormone levels in pre-diabetic, obese IBS patients; GLP-1 measured as observational biomarker, not as a therapeutic intervention |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [40134805](https://pubmed.ncbi.nlm.nih.gov/40134805/) | 2025 | Systematic Review & Meta-analysis | Frontiers in Endocrinology | GLP-1 receptor agonists (including ROSE-010) improve IBS symptoms by inhibiting the migrating motor complex and reducing gastrointestinal motility; highest-quality synthesis of the current evidence base |
| [35234561](https://pubmed.ncbi.nlm.nih.gov/35234561/) | 2022 | Clinical Trial Secondary Analysis | Scandinavian Journal of Gastroenterology | ROSE-010 (GLP-1 receptor agonist) reduces pain intensity during IBS attacks; cross-analysis of RCT data identifies patient subpopulations most likely to respond to GLP-1R-targeted therapy |
| [38997662](https://pubmed.ncbi.nlm.nih.gov/38997662/) | 2024 | Systematic Review | The Journal of Headache and Pain | GLP-1 receptor agonists demonstrate analgesic and anti-nociceptive potential via neuronal pathways; relevant to visceral pain component of IBS |
| [30444291](https://pubmed.ncbi.nlm.nih.gov/30444291/) | 2019 | Review | Experimental Physiology | Intestinal L-cells secrete GLP-1 in response to nutrients, bile acids, and microbial factors; GLP-1 dysregulation directly implicated in IBS pathophysiology including gut neuron sensitisation and altered motility |
| [40697433](https://pubmed.ncbi.nlm.nih.gov/40697433/) | 2025 | Cohort (real-world data) | Annals of Gastroenterology | Real-world GLP-1 receptor agonist prescription and discontinuation patterns in IBS patients; gastrointestinal adverse effects are common, raising tolerability questions for functional GI disorder populations |
| [28215540](https://pubmed.ncbi.nlm.nih.gov/28215540/) | 2017 | Clinical Study | Clinics and Research in Hepatology and Gastroenterology | Decreased circulating GLP-1 levels correlate with abdominal pain severity in constipation-predominant IBS; GLP-1 receptor expression confirmed in colonic tissue |
| [31602785](https://pubmed.ncbi.nlm.nih.gov/31602785/) | 2020 | Preclinical Study | Neurogastroenterology and Motility | GLP-1 receptor agonist exendin-4 ameliorates gastrointestinal dysfunction in Wistar Kyoto rat model of IBS; myenteric neuron activation implicated in the inhibitory effect on gut motility |
| [26765585](https://pubmed.ncbi.nlm.nih.gov/26765585/) | 2016 | Review | Expert Opinion on Investigational Drugs | Comprehensive overview of investigational agents for constipation-predominant IBS-C; GLP-1-related compounds discussed as a drug class of interest |
| [25427821](https://pubmed.ncbi.nlm.nih.gov/25427821/) | 2015 | Review/Commentary | Advances in Experimental Medicine and Biology | Aerosolised GLP-1 proposed as a potential dual-indication treatment for both diabetes mellitus and IBS; discusses delivery route challenges and gastrointestinal mechanistic rationale |
| [30023410](https://pubmed.ncbi.nlm.nih.gov/30023410/) | 2018 | Review | Cellular and Molecular Gastroenterology and Hepatology | Brain-gut-microbiome axis mechanistic overview; GLP-1 implicated as a key signalling molecule in bidirectional gut-brain communication relevant to IBS symptom generation |

---

## Denmark Market Information

Glucagon (DB00040) is currently **not registered** with the Danish Medicines Agency (Lægemiddelstyrelsen) and holds no active marketing authorisations in Denmark based on available data.

> **Note for clinicians:** Glucagon-containing products such as GlucaGen (Novo Nordisk) and Baqsimi (Eli Lilly) hold EMA centralised marketing authorisations for hypoglycaemia rescue in other EU Member States. Their availability in Denmark should be confirmed directly via Lægemiddelstyrelsen's product database (produktresume.dk) or via named patient import procedures. No product is currently authorised for use in IBS.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

> **Additional clinical note:** Glucagon's established mechanism of raising blood glucose (via GCGR-mediated hepatic glycogenolysis) presents an inherent safety concern if repurposed for a chronic functional disorder such as IBS. The hyperglycaemia risk, potential nausea/vomiting at therapeutic doses, and the parenteral-only administration route (requiring injection) would all represent significant barriers to routine IBS use and must be formally evaluated.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model has identified a plausible proglucagon-pathway connection, and the GLP-1 receptor agonist class has genuine, growing clinical evidence in IBS. However, the current evidence does not support **glucagon itself** as the active therapeutic agent — it supports GLP-1R agonism via a pharmacologically distinct receptor. Proceeding with glucagon (DB00040) as an IBS repurposing candidate without first resolving this mechanistic question would risk investing in the wrong molecular target.

**To proceed, the following is needed:**

- **Target receptor clarification:** Formally define whether the programme intends to exploit GCGR (glucagon's own receptor) or whether the true repurposing candidate is a GLP-1 receptor agonist — these are different drug development pathways
- **Glucagon-specific preclinical data:** Dedicated studies using glucagon (not GLP-1 analogues) in IBS animal models or human intestinal tissue to establish direct GI efficacy at the GCGR level
- **MOA data from DrugBank:** Retrieve complete pharmacological profile for DB00040 to confirm receptor binding profile and any documented GI effects
- **Safety risk assessment:** Evaluate whether glucagon's hyperglycaemia risk and parenteral-only route are acceptable in a chronic, non-life-threatening condition such as IBS
- **Dose-finding strategy:** Glucagon's current doses are calibrated for hypoglycaemia rescue (1 mg bolus); sub-threshold spasmolytic doses for chronic GI use would require independent pharmacokinetic/pharmacodynamic modelling
- **SmPC review:** Obtain and parse the full SmPC (available via EMA for GlucaGen) to identify contraindications, warnings, and drug interaction data before any clinical planning
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

