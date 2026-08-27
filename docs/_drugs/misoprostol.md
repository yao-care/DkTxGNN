---
layout: default
title: Misoprostol
parent: 僅模型預測 (L5)
nav_order: 296
evidence_level: L5
indication_count: 4
---

# Misoprostol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Misoprostol: From Gastric Ulcer Protection to Amenorrhea

## One-Sentence Summary

Misoprostol is a synthetic prostaglandin E1 (PGE1) analogue established in clinical practice for the prevention of NSAID-induced gastric ulcers and for obstetric indications including cervical ripening and medical abortion.
The TxGNN model predicts it may be effective for **Amenorrhea**, with **0 registered clinical trials** and **7 publications** currently supporting this direction — however, all available evidence pertains to pregnancy-related amenorrhoea in the context of medical abortion, not to primary or secondary amenorrhoea as an independent gynaecological condition.
This conceptual overlap substantially limits the interpretability of the prediction and warrants careful scoping before any repurposing programme is initiated.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Denmark; known internationally for NSAID-associated gastric ulcer prevention and obstetric use (cervical ripening, medical abortion) |
| Predicted New Indication | Amenorrhea |
| TxGNN Prediction Score | 99.64% |
| Evidence Level | L4 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Misoprostol is a synthetic prostaglandin E1 (PGE1) analogue that binds to EP1 and EP3 receptors on uterine smooth muscle and the cervix. Through this mechanism, it induces uterine contractions and cervical softening and dilation. In the specific context of **pregnancy-related amenorrhoea** — such as missed abortion, anembryonic pregnancy, or unwanted early pregnancy — activating these receptors can trigger endometrial shedding and restore menstrual flow. When co-administered with mifepristone (a progesterone receptor antagonist), the synergistic effect on endometrial shedding is well established and forms the basis of licensed medical abortion regimens worldwide.

The biological rationale for the TxGNN prediction is therefore mechanistically coherent within a narrow clinical context: misoprostol restores menstruation by expelling uterine contents in women whose amenorrhoea is caused by an ongoing pregnancy. This is also the mechanistic pathway captured in the knowledge graph, which likely drove the high prediction score of 99.64%.

However, there is a critical conceptual limitation that must be highlighted for clinical decision-making. **All seven publications identified in this evidence pack address termination of pregnancy — not the treatment of amenorrhoea as a primary gynaecological diagnosis.** Primary amenorrhoea (e.g., due to hypothalamic-pituitary-ovarian axis dysfunction or chromosomal abnormality) and secondary amenorrhoea (e.g., due to Asherman's syndrome, hyperprolactinaemia, or premature ovarian insufficiency) involve fundamentally different aetiologies for which misoprostol's prostaglandin-mediated uterine contractility has no established therapeutic role. The high TxGNN score reflects pharmacological overlap in a knowledge graph pathway rather than evidence of benefit in the broader amenorrhoea disease category.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for misoprostol in amenorrhoea (ClinicalTrials.gov and ICTRP searches returned 0 results as of 2026-03-26).

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [27678099](https://pubmed.ncbi.nlm.nih.gov/27678099/) | 2017 | RCT | *Reproductive Sciences* | Low-dose mifepristone (75 mg) + self-administered misoprostol for ultra-early medical abortion in women with amenorrhoea ≤35 days; n=744; confirms safety, efficacy, and acceptability in hospital vs. self-administration settings |
| [25394644](https://pubmed.ncbi.nlm.nih.gov/25394644/) | 2015 | RCT | *Reproductive Sciences* | Dose-ranging RCT of mifepristone (50–150 mg) + misoprostol (200 µg) for termination of ultra-early pregnancy (amenorrhoea ≤35 days); n=2,500; complete abortion without surgical intervention as primary endpoint |
| [29974571](https://pubmed.ncbi.nlm.nih.gov/29974571/) | 2018 | RCT | *J Obstet Gynaecol Res* | Self-administered low-dose mifepristone + misoprostol for early pregnancy termination; safety and efficacy confirmed across self- and clinic-administration arms |
| [26405260](https://pubmed.ncbi.nlm.nih.gov/26405260/) | 2015 | Cohort Study | *Human Reproduction* | Feasibility study of mifepristone + misoprostol administered before expected menstruation for unintended pregnancy prevention; evaluates restoration of non-pregnant menstrual status |
| [1486304](https://pubmed.ncbi.nlm.nih.gov/1486304/) | 1992 | Prospective Case Series | *BMJ* | Early evidence for misoprostol in medical management of missed abortion and anembryonic pregnancy; demonstrates uterine evacuation without surgical intervention |
| [26001691](https://pubmed.ncbi.nlm.nih.gov/26001691/) | 2015 | Systematic Review | *J Obstet Gynaecol Canada* | Systematic review of endometrial ablation for abnormal uterine bleeding; provides broader context for uterine interventions affecting menstrual patterns, though misoprostol is not the primary focus |
| [37113350](https://pubmed.ncbi.nlm.nih.gov/37113350/) | 2023 | Case Series | *Cureus* | Case report of acute fatty liver of pregnancy (AFLP) presenting with amenorrhoea as a symptom; misoprostol used in peripartum management; peripheral relevance only |

---

## Denmark Market Information

Misoprostol currently holds **no marketing authorisations** recorded in the Danish Medicines Agency (Laegemiddelstyrelsen) dataset used for this analysis.

> **Note for clinicians:** Misoprostol-containing products (e.g., Cytotec®, or the fixed-dose combination Arthrotec® with diclofenac) and mifepristone-misoprostol combination products for medical abortion may be available in Denmark via centralised EMA authorisation, parallel import, or named-patient supply arrangements. Current availability and authorisation status should be verified directly with Laegemiddelstyrelsen or the EMA product database before any prescribing decision.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for full safety information.

> **Important clinical notice:** Although formal safety data were not available in the current evidence pack, misoprostol carries well-recognised and serious risks that are essential for any clinical evaluation. These include uterine hyperstimulation, uterine rupture (risk markedly elevated in women with prior uterine surgery or caesarean section), severe foetal harm and teratogenicity, and significant gastrointestinal adverse effects. Misoprostol is **absolutely contraindicated** in pregnancy when used outside of a supervised obstetric or termination-of-pregnancy protocol. These considerations must be formally documented before any repurposing assessment can proceed past Stage 0.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN prediction score (99.64%), the evidence base reveals a fundamental scope mismatch: all seven identified publications address medical abortion in the setting of pregnancy-related amenorrhoea, rather than amenorrhoea as an independent gynaecological condition. With zero registered clinical trials, no Danish marketing authorisation, and missing safety and MOA data in the formal evidence pack, this candidate cannot advance beyond the research hypothesis stage.

**To proceed, the following is needed:**

- **Clarify the target phenotype:** Define whether the repurposing hypothesis concerns (a) pregnancy-related amenorrhoea (where misoprostol is already in clinical use, making formal repurposing redundant) or (b) primary/secondary non-pregnancy amenorrhoea (where a new mechanistic rationale and dedicated clinical evidence would need to be developed from scratch)
- **Retrieve full MOA data** from DrugBank (DB00929) to complete the mechanistic analysis
- **Obtain the SmPC / prescribing information** including all warnings, contraindications, and special precautions from Laegemiddelstyrelsen or EMA to enable a Stage 1 safety screen
- **Conduct DDI analysis** — current dataset returned no interactions, likely due to a query failure rather than an absence of interactions
- **Commission a targeted literature review** specifically on misoprostol in non-pregnancy secondary amenorrhoea (e.g., Asherman's syndrome, HPO axis disorders) to determine whether any relevant preclinical or early-phase evidence exists beyond the current retrieval
- **Regulatory pathway assessment:** If the hypothesis is refined and evidence supports progression, determine whether a new indication application to Laegemiddelstyrelsen or EMA is feasible given the current marketing authorisation landscape in Denmark

---

*This report is generated for research purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before any therapeutic application. All website pages and reports must include YMYL disclaimer: results are for research reference only and do not constitute medical advice.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

