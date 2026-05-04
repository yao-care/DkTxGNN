---
layout: default
title: Dienogest
parent: 僅模型預測 (L5)
nav_order: 142
evidence_level: L5
indication_count: 10
---

# Dienogest
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

# Dienogest: From Endometriosis to Amenorrhea

## One-Sentence Summary

Dienogest (Visanne®) is a fourth-generation synthetic progestin with established clinical use for **endometriosis** in numerous countries outside Denmark.
The TxGNN model predicts it may be effective for **Amenorrhea**, with **4 clinical trials** and **6 publications** retrieved in relation to this direction.
⚠️ However, a critical mechanistic contradiction is identified: dienogest's core pharmacological action actively *induces* amenorrhoea as a therapeutic endpoint — strongly suggesting this high-scoring prediction is an algorithmic false positive rather than a genuine repurposing opportunity.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Endometriosis (inferred from clinical context and trial data; no Danish marketing authorisation on record) |
| Predicted New Indication | Amenorrhea (disease) |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L3 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

> ⚠️ **Mechanistic Contradiction Warning — Likely Algorithmic False Positive**

Detailed mechanism of action data is not available from DrugBank for this assessment. However, based on established pharmacology, dienogest is a fourth-generation progestin with highly selective progesterone receptor agonist activity and no oestrogenic activity. Its core mechanism for treating endometriosis involves suppressing LH pulsatile secretion, reducing ovarian oestradiol production, and inducing endometrial atrophy via the hypothalamic-pituitary-ovarian (HPO) axis. Clinically, the **amenorrhoea rate serves as a primary efficacy endpoint** in endometriosis trials — amenorrhoea is the intended pharmacological consequence of treatment, not a disease state that dienogest is designed to reverse.

Positioning dienogest as a treatment for amenorrhoea (disease) therefore creates a fundamental mechanistic contradiction: **the drug causes amenorrhoea; it does not treat it**. The TxGNN high prediction score (0.9971) most plausibly arises from dense knowledge graph connectivity between dienogest, the HPO axis, and menstrual cycle nodes — a well-recognised source of non-specific, false-positive scoring in graph-based models.

The only theoretically indirect link would involve evaluation of menstrual recovery *after* cessation of dienogest in women with endometriosis-related secondary menstrual dysfunction. However, this represents a post-treatment pharmacokinetic observation, not a direct therapeutic mechanism targeting amenorrhoea as a primary condition. No clinical programme has been designed around this hypothesis.

---

## Clinical Trial Evidence

> All retrieved trials enrolled endometriosis patients. Amenorrhoea appears in these studies exclusively as a reported side effect, tolerability endpoint, or as a *baseline pharmacological condition* intentionally induced by dienogest — not as the target disease.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT07164183](https://clinicaltrials.gov/study/NCT07164183) | Phase 3 | Recruiting | 290 | Multicenter open-label RCT comparing Indinol Forto® 200 mg vs Visanne® 2 mg (dienogest) for endometriosis; non-inferiority design; amenorrhoea likely captured as a tolerability measure |
| [NCT02425462](https://clinicaltrials.gov/study/NCT02425462) | N/A (Observational) | Completed | 895 | Prospective observational cohort of Visanne® in Asian women with endometriosis across routine clinical settings; quality of life as primary endpoint; amenorrhoea rate documented as secondary safety/tolerability item |
| [NCT04495855](https://clinicaltrials.gov/study/NCT04495855) | N/A (Observational) | Completed | 968 | Real-world observational study of dienogest in endometriosis clinical practice; evaluated symptom control and long-term treatment outcomes; amenorrhoea recorded as a common adverse event |
| [NCT07204093](https://clinicaltrials.gov/study/NCT07204093) | N/A | Active, not recruiting | 138 | Compares transdermal oestradiol add-back (with dienogest vs drospirenone) in endometriosis; study design explicitly *presupposes* dienogest-induced amenorrhoea as the pharmacological baseline state, then adds oestradiol to mitigate hypoestrogenic side effects — this further confirms dienogest as an amenorrhoea *inducer*, not a treatment |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [39090694](https://pubmed.ncbi.nlm.nih.gov/39090694/) | 2024 | Systematic Review + Bayesian Analysis | BMC Pharmacology & Toxicology | Comprehensive analysis of adverse effects of dienogest in endometriosis and adenomyosis; amenorrhoea confirmed as the predominant reported pharmacological effect, consistent with its mechanism of action |
| [34405378](https://pubmed.ncbi.nlm.nih.gov/34405378/) | 2022 | Narrative Review | Reviews in Endocrine & Metabolic Disorders | Reviews hormonal management of endometriosis; confirms oestrogen dependency and progesterone resistance as key pathogenic factors; describes HPO axis suppression by dienogest as the central therapeutic mechanism |
| [41329046](https://pubmed.ncbi.nlm.nih.gov/41329046/) | 2026 | Pharmacological / Mechanistic Study | European Journal of Contraception & Reproductive Health Care | Demonstrates high inhibition ratio and transformation index of dienogest 2 mg; supports induction of amenorrhoea and a hypoestrogenic milieu as the intended pharmacological goal in endometriosis management |
| [29161960](https://pubmed.ncbi.nlm.nih.gov/29161960/) | 2018 | Retrospective Cohort | Reproductive Sciences | Long-term efficacy and safety of dienogest in ovarian endometrioma (N=514, 7 university hospitals); amenorrhoea rate and endometrioma recurrence evaluated as key outcomes at >12 months of treatment |
| [34918698](https://pubmed.ncbi.nlm.nih.gov/34918698/) | 2021 | Case Report | Medicine | Case report of ovarian granulosa cell tumour in a PCOS patient; tangentially related to ovarian hormone physiology but provides no evidence for dienogest use in amenorrhoea |
| [40543564](https://pubmed.ncbi.nlm.nih.gov/40543564/) | 2025 | Review / Imaging Study | Journal of Pediatric and Adolescent Gynecology | Advanced 3D and VR visualisation techniques for Müllerian anomalies; addresses structural causes of amenorrhoea but contains no data relevant to dienogest as a pharmacological intervention |

---

## Denmark Market Information

Dienogest is currently **not authorised for sale in Denmark**. No marketing authorisations have been registered with the Danish Medicines Agency (Lægemiddelstyrelsen), and the product has no market presence.

For reference, dienogest (as Visanne® 2 mg tablets, Bayer AG) holds marketing authorisation in Germany and multiple other EU member states, and has been approved for endometriosis in Japan, South Korea, and Australia, among others. Any use in Denmark would currently require a named-patient or compassionate use application to Lægemiddelstyrelsen.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) — for example, the German or EMA-registered Visanne® SmPC — for full safety information.

Warnings, contraindications, and drug interaction data specific to the Danish regulatory context were not available for this assessment. Clinicians should note that progestins as a class carry class-specific considerations including thromboembolic risk in relevant patient populations, effects on bone mineral density with prolonged use, and potential mood-related adverse effects.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction of amenorrhoea as a new indication for dienogest is assessed as a **high-confidence algorithmic false positive**. Dienogest's established pharmacological mechanism *causes* amenorrhoea as a therapeutic outcome in endometriosis management; there is no biological or clinical basis for its use as a treatment for amenorrhoea as a primary disease. All four retrieved clinical trials and the most directly relevant literature confirm this reverse relationship. The prediction score likely reflects non-specific HPO-axis network connectivity in the TxGNN knowledge graph rather than a genuine drug–disease therapeutic relationship.

**To proceed, the following is needed:**

- **Mechanistic clarification**: Define whether any specific amenorrhoea subtype exists (e.g., anovulatory amenorrhoea secondary to chronic oestrogen excess) where progestogenic activity could theoretically restore cycling — and confirm this is distinct from dienogest's suppressive mechanism
- **MOA data retrieval**: Obtain complete DrugBank MOA entry for dienogest, including progesterone receptor subtype (PRA/PRB) selectivity and downstream endometrial signalling data
- **Safety data retrieval**: Download and parse the Visanne® SmPC (Bayer AG) or the TFDA package insert to complete the safety profiling, including contraindications and key warnings
- **Targeted literature search**: Conduct a focused PubMed search for progestin therapy specifically indicated for amenorrhoea treatment (not endometriosis management) to identify any precedent
- **False positive flagging**: Consider categorising this prediction as a graph-artifact false positive in the TxGNN output pipeline to prevent recurrence in future runs; the amenorrhoea–progestin node connection should be annotated with directionality (drug *induces* condition, not *treats* it)

---

*This report is generated for research purposes only and does not constitute medical advice. All drug repurposing candidates require prospective clinical validation before any therapeutic application. Data cutoff: 2026-04-05.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

