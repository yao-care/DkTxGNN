---
layout: default
title: Etonogestrel
parent: 僅模型預測 (L5)
nav_order: 180
evidence_level: L5
indication_count: 10
---

# Etonogestrel
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

# Etonogestrel: From Contraception to Amenorrhea

## One-Sentence Summary

Etonogestrel is a third-generation progestogen primarily used for long-acting reversible contraception (e.g., subdermal implant marketed as Nexplanon/Implanon).
The TxGNN model predicts it may be effective for **Amenorrhea**, with a prediction score of 99.84%; however, this prediction is almost certainly a **reverse association artefact** — etonogestrel is known to *cause* amenorrhea as a side effect in 20–30% of implant users, not to treat it.
Supporting evidence is limited to **1 clinical trial** (contraception-focused, not amenorrhea treatment) and **1 relevant publication**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Contraception (long-acting reversible) |
| Predicted New Indication | Amenorrhea (disease) |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L4 — No direct therapeutic evidence; mechanistic studies only |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | **Hold** |

## Why is This Prediction Reasonable?

> Currently, detailed mechanism of action data is not available in the evidence pack. Based on known pharmacology, etonogestrel is a synthetic progestogen (the active metabolite of desogestrel) that acts as a potent agonist at the progesterone receptor. It achieves contraception primarily by suppressing ovulation via inhibition of the LH surge, thickening cervical mucus, and inducing endometrial atrophy.

**⚠️ Critical caveat — Reverse Association:** The TxGNN model has very likely misinterpreted a well-documented *side-effect relationship* as a *therapeutic relationship*. Etonogestrel-releasing implants cause amenorrhea in approximately 20–30% of users due to profound suppression of the hypothalamic-pituitary-ovarian axis and endometrial atrophy. In other words, etonogestrel **induces** amenorrhea rather than treating it. The knowledge graph likely contains numerous co-occurrence links between etonogestrel and amenorrhea in adverse event reports and clinical trial outcome data, inflating the prediction score.

From a clinical standpoint, amenorrhea itself has diverse aetiologies (hypothalamic, pituitary, ovarian, uterine), and adding a progestogen that further suppresses the HPO axis would be counterproductive in most forms of pathological amenorrhea. This prediction does not carry therapeutic significance and should not be pursued as a repurposing candidate.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04626596](https://clinicaltrials.gov/study/NCT04626596) | Phase 3 | Completed | 498 | Assessed contraceptive efficacy and safety of the etonogestrel implant during extended use (years 4–5). **Not a treatment trial for amenorrhea** — amenorrhea was recorded only as a bleeding-pattern side effect. Relevance to amenorrhea treatment: **Low (Grade C).** |

> **Note:** No clinical trials investigating etonogestrel as a *treatment* for amenorrhea were identified.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10549446](https://pubmed.ncbi.nlm.nih.gov/10549446/) | 1999 | RCT | Contraception | Compared Implanon (single-rod etonogestrel) vs. Norplant (six-capsule levonorgestrel) for contraceptive efficacy and bleeding patterns in 200 women over 2–4 years. No pregnancies occurred. **Amenorrhea was reported as a side effect**, not studied as a treatment endpoint. |

> **Note:** A second literature result (PMID 33430924) was returned by the search but concerns a COVID-19 pneumonia trial (BIO101/COVA study) with no relevance to etonogestrel or amenorrhea and has been excluded.

## Denmark Market Information

Etonogestrel currently holds no marketing authorisations in the dataset reviewed.

> **Note:** Etonogestrel-containing products (e.g., Nexplanon) may hold centralised EMA authorisations valid in Denmark. Clinicians should consult the Danish Medicines Agency (Lægemiddelstyrelsen) or the EMA Union Register for current authorisation status.

## Additional Predicted Indications (Lower-Ranked)

The TxGNN model also predicted several benign breast conditions. These are summarised below for completeness:

| Rank | Disease | TxGNN Score | Evidence Level | Recommendation | Comment |
|------|---------|-------------|----------------|----------------|---------|
| 3 | Breast fibrocystic disease | 99.61% | L5 | Research Question | Hormonal sensitivity provides theoretical rationale, but clinical evidence is contradictory. No trials or publications found. |
| 5 | Blunt duct adenosis of breast | 99.29% | L5 | Hold | Rare histopathological subtype; typically managed by imaging surveillance, not pharmacotherapy. High score likely reflects graph proximity to other breast diseases. |
| 6 | Apocrine adenosis of breast | 99.29% | L5 | Hold | Identical score to blunt duct adenosis, suggesting the model groups these via disease cluster proximity rather than independent drug-disease evidence. Not treated pharmacologically. |
| 9 | Benign mammary dysplasia | 99.21% | L5 | Research Question | Highly overlapping diagnostic concept with fibrocystic disease. Progestogen anti-oestrogenic effects are theoretically plausible but clinically unproven. |

> **Pattern observation:** The clustering of benign breast conditions with nearly identical TxGNN scores (99.2–99.6%) strongly suggests the model is propagating predictions through disease graph proximity rather than identifying independent therapeutic signals.

## Safety Considerations

> Please refer to the approved Summary of Product Characteristics (SmPC) for safety information. Key safety data (warnings, contraindications, and drug–drug interactions) were not available in this evidence pack.

> For products authorised in the EU (e.g., Nexplanon), the SmPC is available via the EMA website. Known class-level concerns for progestogens include thromboembolic events, effects on lipid metabolism, mood changes, and interactions with CYP3A4 inducers (e.g., rifampicin, carbamazepine, phenytoin).

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked TxGNN prediction (amenorrhea) represents a classic **reverse association artefact** — etonogestrel causes amenorrhea as a known pharmacological side effect and does not treat it. The remaining predictions (benign breast conditions) are all at evidence level L5 (model prediction only) with zero clinical trials and zero publications, and the identical scores across related breast conditions indicate graph-proximity-driven predictions rather than genuine therapeutic signals. This candidate should not advance to further evaluation.

**If future re-evaluation is considered, the following would be needed:**
- Detailed mechanism of action data (MOA) from DrugBank
- Safety data from the approved SmPC (warnings, contraindications, DDI)
- Clarification of Denmark market status via Lægemiddelstyrelsen / EMA registers
- For breast fibrocystic disease specifically: a targeted literature search for progestogen effects on fibrocystic breast changes (broader than etonogestrel alone)
- Expert clinical review to distinguish genuine therapeutic signals from side-effect or graph-proximity artefacts in TxGNN output

---

*This report is for research purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before any therapeutic application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

