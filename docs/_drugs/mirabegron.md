---
layout: default
title: Mirabegron
parent: 僅模型預測 (L5)
nav_order: 239
evidence_level: L5
indication_count: 10
---

# Mirabegron
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

# Mirabegron: From Overactive Bladder to Thoracic Malformation

## One-Sentence Summary

Mirabegron is a selective β3-adrenergic receptor agonist internationally approved for overactive bladder (OAB) treatment, though no Danish national marketing authorisations were identified in this dataset.
The TxGNN model predicts its highest-ranked new potential indication is **Thoracic Malformation** (score: 83.06%), supported by **0 clinical trials** and **0 publications**.
Across all five predicted indications in this multi-candidate report, the mechanistic rationale is weak and evidence does not exceed L4 (disease background literature only); all carry a **Hold** recommendation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Overactive bladder (OAB) — based on known pharmacology; not available in Danish regulatory dataset |
| Predicted New Indication | Thoracic Malformation |
| TxGNN Prediction Score | 83.06% |
| Evidence Level | L5 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 (national); see note on EMA centralised authorisation below |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data was not available in this dataset. Based on known pharmacology, Mirabegron is a selective β3-adrenergic receptor (β3-AR) agonist. β3-AR (ADRB3) is primarily expressed in the bladder detrusor muscle, adipose tissue, and renal tubules. Its activation stimulates the Gsα → adenylyl cyclase → intracellular cAMP pathway, causing relaxation of the detrusor muscle and increased bladder storage capacity — the pharmacological basis for its approved OAB indication.

Thoracic malformation is a structural congenital defect. Its pathogenesis involves embryonic skeletal and soft tissue developmental regulation governed by HOX gene networks, FGF signalling, and related developmental pathways. There is no established direct mechanistic connection between the β3-AR/cAMP signalling axis and the embryonic processes underlying thoracic skeletal morphogenesis.

The high TxGNN prediction score (0.83) for this indication is therefore likely an artefact arising from indirect knowledge graph connections via kidney or mesenchymal tissue nodes, rather than a biologically grounded prediction. This is explicitly flagged in the mechanistic rationale as probable model noise rather than a genuine drug–disease relationship.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Denmark Market Information

No marketing authorisations were identified for Mirabegron in the Danish national regulatory database (0 licences, not marketed).

> **Note:** Mirabegron (brand name Betmiga) holds a centralised EMA marketing authorisation (EU/1/12/809) for overactive bladder in adults. Availability in Denmark via the EMA centralised procedure should be confirmed directly with Laegemiddelstyrelsen, as centralised EMA authorisations may not be reflected in the national dataset used here.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

---

## Additional Predicted Indications

This is a multi-candidate report (TW-DB08893-multi). The TxGNN model identified five unique diseases across the top 10 predictions. All carry a **Hold** recommendation. The table below summarises key differences in evidence level and mechanistic concerns.

| Rank | Disease | TxGNN Score | Evidence Level | Key Mechanistic Concern | Recommendation |
|------|---------|-------------|----------------|------------------------|----------------|
| 1 | Thoracic Malformation | 83.06% | L5 | No known β3-AR connection to thoracic development; likely model noise | Hold |
| 3 | Renal-Hepatic-Pancreatic Dysplasia | 82.93% | L5 | Ciliopathy (NPHP3 mutation); β3-AR/cAMP not linked to ciliary assembly or planar cell polarity pathways | Hold |
| 5 | PKD3 ± Polycystic Liver Disease | 82.20% | L4 | β3-AR → cAMP axis **shares the same direction** as the PKD disease pathway; may worsen cyst proliferation | Hold |
| 7 | Joubert Syndrome with Renal Defect | 80.89% | L5 | Ciliopathy (AHI1/CEP290/TMEM67); β3-AR/cAMP not linked to IFT system or Hedgehog signalling | Hold |
| 9 | Adult Familial Nephronophthisis–Spastic Quadriparesia | 80.32% | L5 | Ultra-rare ciliopathy; no mechanistic link; patient numbers too small for clinical feasibility | Hold |

### PKD3 Background Literature

The PKD3 indication (rank 5) is the only prediction with associated literature (20 publications). **None of these publications study Mirabegron in PKD3; they are disease background context only.** Furthermore, the mechanistic analysis raises a potential safety concern: Mirabegron's cAMP-elevating mechanism aligns with — rather than counters — the PKD3 disease pathway, potentially accelerating cyst proliferation. This must be clarified before the indication can be advanced.

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [30819518](https://pubmed.ncbi.nlm.nih.gov/30819518/) | 2019 | Review | *Lancet* | Comprehensive ADPKD review: systemic disorder with renal cysts, hypertension, liver cysts, intracranial aneurysms, and cardiac valvular disease |
| [38958301](https://pubmed.ncbi.nlm.nih.gov/38958301/) | 2024 | Clinical Guideline | *Am J Gastroenterol* | ACG guideline on focal liver lesions; covers management of hepatic cystic lesions including polycystic liver disease |
| [35728731](https://pubmed.ncbi.nlm.nih.gov/35728731/) | 2022 | Clinical Guideline | *J Hepatol* | EASL guidelines on cystic liver diseases: hepatic cysts, polycystic liver disease, Caroli disease — diagnosis and management |
| [35487607](https://pubmed.ncbi.nlm.nih.gov/35487607/) | 2022 | Review | *Clin Liver Dis* | ADPKD and polycystic liver disease overview; tolvaptan's role in slowing renal function decline and cyst growth |
| [29038287](https://pubmed.ncbi.nlm.nih.gov/29038287/) | 2018 | Review | *JASN* | Eight genes associated with ADPKD/ADPLD identified, including GANAB — the gene implicated in PKD3 |
| [38097330](https://pubmed.ncbi.nlm.nih.gov/38097330/) | 2023 | Review | *Adv Kidney Dis Health* | Genetic spectrum of PKD/PLD: PKD1 accounts for ~80% of ADPKD; primary cilia dysfunction central to pathogenesis |
| [34724412](https://pubmed.ncbi.nlm.nih.gov/34724412/) | 2022 | Review | *Annu Rev Pathol* | PLD pathogenesis: sequence of primary gene mutations → cyst initiation → hepatic cystogenesis progression; potential therapeutic targets |
| [28375157](https://pubmed.ncbi.nlm.nih.gov/28375157/) | 2017 | Basic Research | *J Clin Invest* | Whole exome sequencing in 102 PCLD patients identifies novel causative genes; isolated PCLD genes act as effectors of polycystin-1 |
| [36200122](https://pubmed.ncbi.nlm.nih.gov/36200122/) | 2022 | Review | *Hepatic Med* | PLD pathophysiology: ductal plate malformation, ciliary dysfunction, and aberrant cell signalling drive cystogenesis |
| [37943238](https://pubmed.ncbi.nlm.nih.gov/37943238/) | 2023 | Review | *Adv Kidney Dis Health* | Symptomatic PLD complications arising from massive cyst enlargement; liver is the most common extrarenal site in ADPKD |

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
None of the five predicted indications presents a credible mechanistic basis linking Mirabegron's β3-AR agonism to the predicted disease pathways, all of which involve congenital structural defects or ciliopathies with fundamentally different molecular drivers. The PKD3 prediction (rank 5) is the most developed mechanistically, but Mirabegron's cAMP-promoting effect theoretically aligns with — rather than opposes — the disease mechanism, raising a potential harm signal that must be resolved before any further study is justified.

**To proceed, the following is needed:**

- **MOA data**: Retrieve complete mechanism of action data from DrugBank (DB08893) to underpin all mechanistic plausibility assessments
- **Safety data**: Obtain the approved SmPC (EMA Betmiga EU/1/12/809) to establish the full safety profile, including warnings, contraindications, and known drug interactions
- **Danish regulatory confirmation**: Verify Betmiga's current availability in Denmark under the EMA centralised authorisation pathway with Laegemiddelstyrelsen
- **PKD3 cAMP directionality study**: Before PKD3 can be considered further, dedicated mechanistic studies are required to determine whether β3-AR agonism exacerbates or protects against cyst progression in GANAB-mutant and ADPKD models
- **De-prioritise remaining indications**: Thoracic malformation, renal-hepatic-pancreatic dysplasia, Joubert syndrome, and adult familial nephronophthisis–spastic quadriparesia all lack supporting evidence and biologically plausible mechanistic links — further investigation is not recommended at this stage
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

