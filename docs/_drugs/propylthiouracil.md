---
layout: default
title: Propylthiouracil
parent: 僅模型預測 (L5)
nav_order: 362
evidence_level: L5
indication_count: 6
---

# Propylthiouracil
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

# Propylthiouracil: From Hyperthyroidism (Graves' Disease) to Neonatal Thyrotoxicosis

## One-Sentence Summary

Propylthiouracil (PTU) is a thionamide antithyroid agent classically used to control hyperthyroidism, most notably Graves' disease, and is preferred in pregnancy due to lower placental transfer than methimazole. The TxGNN model predicts relevance for **Neonatal Thyrotoxicosis**, with **1 clinical trial** and **20 publications** currently supporting this direction. Evidence is indirect — no dedicated randomized trial exists in neonates for ethical reasons — but it is consistent with established clinical practice of managing maternal Graves' disease with thionamides to protect the fetus/neonate.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in the local regulatory dataset (drug not marketed in Denmark); clinically established for hyperthyroidism/Graves' disease |
| Predicted New Indication | Neonatal Thyrotoxicosis |
| TxGNN Prediction Score | 99.40% |
| Evidence Level | L3 |
| Denmark Market Status | Not Marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack. Based on known pharmacology, PTU inhibits thyroid peroxidase, blocking oxidation and organification of iodide and thereby reducing new thyroid hormone synthesis; it also partially inhibits peripheral T4-to-T3 conversion.

Neonatal thyrotoxicosis most commonly arises when maternal TSH-receptor-stimulating antibodies (Graves' disease) cross the placenta, or less commonly from activating TSHR/GNAS mutations. Because PTU's mechanism directly suppresses thyroid hormone synthesis, thionamide therapy (PTU or methimazole) is already the clinical standard for managing maternal hyperthyroidism during pregnancy to prevent fetal and neonatal thyrotoxic complications — methimazole is generally preferred postnatally due to PTU's hepatotoxicity risk, but PTU retains a defined role, particularly in the first trimester. This mechanistic and clinical continuity supports the TxGNN prediction, even though no interventional trial has been conducted directly in thyrotoxic neonates due to obvious ethical constraints.

The same evidence pack also flags two related thyroid-axis conditions — "resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta" (score 99.66%) and "hyperthyroxinemia" (score 99.08%) — but their supporting literature is largely mechanistic/genetic case material rather than treatment evidence, and in one case (PMID 10724359) PTU treatment failed to control the underlying condition. These two are therefore considered lower-confidence signals (internally flagged "Hold") and are not the focus of this report.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03066076](https://clinicaltrials.gov/study/NCT03066076) | Phase 3 | Unknown | 60 | Compares total thyroidectomy vs. thionamide antithyroid drugs in moderate-to-severe Graves' ophthalmopathy; not a direct neonatal trial, but the thionamide treatment arm provides indirect data on maternal antithyroid therapy relevant to fetal/neonatal thyroid outcomes. Trial status is "Unknown," indicating possible loss to follow-up. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33349844](https://pubmed.ncbi.nlm.nih.gov/33349844/) | 2021 | Review/Guideline | J Clin Endocrinol Metab | Guidance on testing, monitoring and treatment of thyroid dysfunction in pregnancy, including antithyroid drug risk-benefit considerations |
| [31345521](https://pubmed.ncbi.nlm.nih.gov/31345521/) | 2019 | Review | Endocrinol Metab Clin North Am | High-risk Graves' disease in pregnancy treated with PTU in the first trimester, transitioning to methimazole thereafter |
| [25747892](https://pubmed.ncbi.nlm.nih.gov/25747892/) | 2015 | Cohort | Thyroid | Gestational thyrotoxicosis and antithyroid drug use evaluated against neonatal outcomes in an integrated healthcare system |
| [24622372](https://pubmed.ncbi.nlm.nih.gov/24622372/) | 2013 | Review | Lancet Diabetes Endocrinol | Overview of hyperthyroidism in pregnancy; notes adverse outcomes can affect both mother and offspring |
| [32199749](https://pubmed.ncbi.nlm.nih.gov/32199749/) | 2020 | Review/Guideline | Best Pract Res Clin Endocrinol Metab | Management approach to thyrotoxicosis during pregnancy to prevent maternal and fetal complications |
| [6387489](https://pubmed.ncbi.nlm.nih.gov/6387489/) | 1984 | Review | N Engl J Med | Classic review of antithyroid drug pharmacology and mechanism of action |
| [18558604](https://pubmed.ncbi.nlm.nih.gov/18558604/) | 2008 | Case report | Endocr Pract | Persistent neonatal thyrotoxicosis from a rare activating TSHR mutation, illustrating non-autoimmune neonatal disease requiring antithyroid therapy |
| [12201835](https://pubmed.ncbi.nlm.nih.gov/12201835/) | 2002 | Case report | Clin Endocrinol | Neonatal thyrotoxicosis case linked to a maternal TRβ gene mutation (M313T) |
| [596245](https://pubmed.ncbi.nlm.nih.gov/596245/) | 1977 | Case series | Acta Med Scand | Early description linking postpartum hyperthyroidism exacerbation to neonatal thyrotoxicosis |
| [2090674](https://pubmed.ncbi.nlm.nih.gov/2090674/) | 1990 | Case report | J Endocrinol Invest | Neonatal hepatitis and lymphocyte sensitization following placental transfer of PTU, alongside transient neonatal thyrotoxicosis — relevant to both efficacy and safety monitoring |

---

## Denmark Market Information

Propylthiouracil is currently **not marketed** in Denmark under this evidence pack's dataset — no marketing authorisations (national Laegemiddelstyrelsen or centralised EMA) were found.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information. No key warnings, contraindications, or drug-interaction data were available in this evidence pack (DDI query: not found). Note as general pharmacological background: PTU as a drug class is associated with recognised hepatotoxicity and agranulocytosis risks, which should be confirmed against the current SmPC before clinical use.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Thionamide therapy for maternal Graves' disease during pregnancy is already established clinical practice, and the available cohort, review, and case-level evidence coherently support PTU's mechanistic relevance to neonatal thyrotoxicosis prevention/management. However, no dedicated randomized trial in neonates exists (ethically limited), and the drug currently has no marketing authorisation in Denmark.

**To proceed, the following is needed:**
- Danish SmPC warnings/contraindications (DG001, Blocking) — required before any S1 safety assessment
- Confirmed mechanism of action data from DrugBank (DG002, High)
- Drug interaction data (currently not found)
- Regulatory pathway assessment for Danish market entry given current "Not Marketed" status
- Pediatric/neonatal dosing and monitoring protocol if pursued clinically
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

