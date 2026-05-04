---
layout: default
title: Allopurinol
parent: 僅模型預測 (L5)
nav_order: 26
evidence_level: L5
indication_count: 10
---

# Allopurinol
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

# Allopurinol: From Gout and Hyperuricaemia to Hepatic Porphyria

## One-Sentence Summary

Allopurinol is a well-established xanthine oxidase (XO) inhibitor, used globally for the treatment of gout and hyperuricaemia by reducing uric acid production.
The TxGNN model predicts it may be effective for **hepatic porphyria**, with **0 clinical trials** and **2 publications** currently available — both at the mechanistic hypothesis or animal-study level.
The overall evidence base is limited, placing this prediction at evidence level L4, and further targeted research is needed before clinical translation can be considered.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Gout and hyperuricaemia (xanthine oxidase inhibition; standard indication not registered in Denmark per available data) |
| Predicted New Indication | Hepatic Porphyria |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L4 (preclinical / mechanistic studies only) |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this Evidence Pack. Based on established pharmacological knowledge, allopurinol inhibits xanthine oxidase (XO), the enzyme responsible for the final steps of purine catabolism and a major source of reactive oxygen species (ROS) in the cell. By reducing XO activity, allopurinol lowers both serum urate and intracellular oxidative stress.

The proposed connection to hepatic porphyria rests on a mechanistic hypothesis: in the heme biosynthesis pathway, δ-aminolevulinate synthase (ALAS) is the rate-limiting enzyme and is under negative feedback control by the free hepatic heme pool. Acute porphyric attacks are triggered by excessive ALAS induction, which leads to accumulation of toxic heme precursors — aminolevulinic acid (ALA) and porphobilinogen (PBG). Some investigators have proposed that XO-derived ROS can disturb the free heme pool and secondarily perturb ALAS regulation. On this basis, allopurinol's antioxidant properties could theoretically dampen ALAS over-activity and reduce precursor accumulation.

However, this mechanistic chain remains entirely at the hypothesis level. No direct clinical or human data link allopurinol to improvement in hepatic porphyria. The two identified publications are a mechanistic commentary and a rat-liver pharmacology study on carbamazepine — neither tests allopurinol directly in porphyria. The TxGNN high prediction score most likely reflects shared liver-disease node proximity in the knowledge graph rather than a validated drug–disease relationship.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [31443750](https://pubmed.ncbi.nlm.nih.gov/31443750/) | 2019 | Hypothesis / Mechanistic Commentary | Medical Hypotheses | Proposes that inhibiting heme utilisation by tryptophan 2,3-dioxygenase (TDO) — thereby protecting the free hepatic heme pool — may reduce ALAS induction and prevent acute porphyric attacks; provides theoretical context for XO-inhibitor interest in porphyria |
| [1567472](https://pubmed.ncbi.nlm.nih.gov/1567472/) | 1992 | Animal Study (rat liver) | Biochemical Pharmacology | Demonstrates that acute carbamazepine administration disrupts haem metabolism in rat liver and exacerbates porphyria through loss of haem utilised by tryptophan pyrrolase; indirect mechanistic background for how oxidative haem-pool disruption contributes to acute porphyric attacks |

---

## Denmark Market Information

No marketing authorisations for allopurinol are available in the current dataset for Denmark (Laegemiddelstyrelsen). Note: this may reflect a data gap rather than true absence from the Danish market, as allopurinol is a widely available generic compound in European markets. Verification against the current Laegemiddelstyrelsen product register is recommended.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information. Key warnings, contraindications, and drug–drug interaction data were not available in this Evidence Pack and should be retrieved from the Laegemiddelstyrelsen product database or the European Medicines Agency (EMA) before any further evaluation.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only evidence supporting allopurinol in hepatic porphyria consists of a mechanistic hypothesis paper and an animal study on a different drug — neither provides direct clinical or preclinical data on allopurinol itself in porphyria. With no registered clinical trials and no human evidence, the prediction cannot progress beyond the research-question stage at this time. Additionally, no safety, contraindication, or drug–drug interaction data were available for this submission, which constitutes a blocking data gap for any formal safety evaluation.

**To proceed, the following is needed:**

- **Mechanism clarification**: Direct experimental data (cell lines or animal models) showing that allopurinol or XO inhibition modulates ALAS activity or reduces ALA/PBG accumulation in a porphyria model
- **Safety data retrieval**: Download and parse the SmPC from Laegemiddelstyrelsen (or EMA) to complete the S1 safety pre-screening, including warnings, contraindications, and drug interactions
- **Denmark market verification**: Confirm current registration status via the Laegemiddelstyrelsen product register, as 0 authorisations may reflect a data gap
- **Targeted literature search**: Conduct a focused PubMed/EMBASE search combining allopurinol + acute intermittent porphyria / AIP / ALA synthase to determine whether any direct human case reports or pilot studies exist
- **Directionality check**: Before designing any study, clarify whether XO inhibition is beneficial or potentially harmful in porphyria (via its interaction with the hepatic heme pool), as the mechanistic direction has not been confirmed

> **Disclaimer:** This report is intended for research reference only and does not constitute medical advice. Any drug repurposing candidate requires clinical validation before application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

