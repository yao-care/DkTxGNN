---
layout: default
title: Simvastatin
parent: 僅模型預測 (L5)
nav_order: 401
evidence_level: L5
indication_count: 10
---

# Simvastatin
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

# Simvastatin: From Hypercholesterolemia to Familial Hypercholesterolemia

## One-Sentence Summary

Simvastatin is a well-established HMG-CoA reductase inhibitor ("statin") originally used to treat hypercholesterolemia and mixed dyslipidemia. The TxGNN model predicts it may be effective for **Familial Hypercholesterolemia (FH)** — a genetic subtype of its original target condition — with a prediction score of **99.63%**, currently supported by **19 clinical trials** and **18 publications**, including multiple completed Phase 3 RCTs.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypercholesterolemia / mixed dyslipidemia (established statin indication; Danish-specific label text not available in this evidence pack — see Data Gaps) |
| Predicted New Indication | Familial Hypercholesterolemia |
| TxGNN Prediction Score | 99.63% |
| Evidence Level | L1 |
| Denmark Market Status | Not Marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Drug-specific mechanism-of-action documentation was not available in this evidence pack (Data Gap DG002). Based on established pharmacology, simvastatin is a well-characterized HMG-CoA reductase inhibitor: it blocks the rate-limiting step of hepatic cholesterol biosynthesis, which upregulates hepatocyte LDL-receptor expression and increases clearance of circulating LDL cholesterol (LDL-C).

Familial hypercholesterolemia is a genetic disorder of LDL-C metabolism — most commonly caused by mutations affecting the LDL receptor, ApoB, or PCSK9 pathway — that produces markedly elevated LDL-C from birth and premature cardiovascular disease. It is, in effect, a more severe and genetically defined subset of the general hypercholesterolemia/dyslipidemia population that statins were originally developed to treat, so this prediction sits very close to simvastatin's established therapeutic territory rather than representing a mechanistically novel repurposing candidate.

This fit is corroborated by the model's own rationale: simvastatin's LDL-receptor-upregulating action maps directly onto the LDL-receptor/ApoB/PCSK9 clearance defects that define FH, and statin therapy is already a guideline-recommended cornerstone of FH management (reflected in the 2026 ACC/AHA dyslipidemia guideline and multiple completed Phase 3 trials below). This is consistent with L1-level evidence — the strongest tier in this framework — and stands in clear contrast to lower-confidence candidates elsewhere in this evidence pack (e.g., brain stem infarction, CETP deficiency), which rest on mechanistic speculation with L5/no direct evidence.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00552097](https://clinicaltrials.gov/study/NCT00552097) | Phase 3 | Completed | 720 | ENHANCE trial: ezetimibe + high-dose simvastatin vs. simvastatin alone; assessed carotid intima-media thickness progression in heterozygous FH |
| [NCT00129402](https://clinicaltrials.gov/study/NCT00129402) | Phase 3 | Completed | 248 | Ezetimibe co-administered with simvastatin vs. simvastatin alone in adolescents (10–17y) with heterozygous FH |
| [NCT00654446](https://clinicaltrials.gov/study/NCT00654446) | Phase 3 | Completed | 442 | Compared renal effects of rosuvastatin vs. simvastatin in Fredrickson type IIa/IIb dyslipidaemia, including heFH |
| [NCT00465088](https://clinicaltrials.gov/study/NCT00465088) | Phase 3 | Completed | 199 | SUPREME: niacin ER + simvastatin vs. atorvastatin; compared HDL-C-raising effect in hyperlipidemia/mixed dyslipidemia |
| [NCT01070966](https://clinicaltrials.gov/study/NCT01070966) | N/A | Completed | 2089 | Post-marketing re-examination of VYTORIN (ezetimibe/simvastatin) safety and efficacy in routine practice |
| [NCT03884452](https://clinicaltrials.gov/study/NCT03884452) | Phase 3 | Completed | 50 | Ezetimibe 10mg added to atorvastatin or simvastatin in homozygous FH; efficacy and safety |
| [NCT03885921](https://clinicaltrials.gov/study/NCT03885921) | Phase 3 | Completed | 44 | 24-month open-label extension evaluating long-term safety of ezetimibe + atorvastatin/simvastatin in homozygous FH |
| [NCT00145574](https://clinicaltrials.gov/study/NCT00145574) | Phase 4 | Completed | 194 | Colesevelam add-on to stable pediatric statin therapy (incl. simvastatin) in heterozygous FH |
| [NCT03510715](https://clinicaltrials.gov/study/NCT03510715) | Phase 3 | Completed | 18 | Alirocumab in pediatric/adolescent homozygous FH; simvastatin present only as background statin therapy, not the study drug |
| [NCT00475826](https://clinicaltrials.gov/study/NCT00475826) | N/A | Unknown | N/A | Chylomicron metabolism sub-study in heFH patients on statin + ezetimibe; observational, recruitment status unknown |

No EudraCT identifiers were present in the evidence pack for these trials.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18376000](https://pubmed.ncbi.nlm.nih.gov/18376000/) | 2008 | RCT | New England Journal of Medicine | ENHANCE trial: simvastatin ± ezetimibe in FH; ezetimibe added no incremental benefit on carotid IMT despite greater LDL-C lowering |
| [15794711](https://pubmed.ncbi.nlm.nih.gov/15794711/) | 2005 | Review | Expert Opinion on Drug Safety | Long-term efficacy/safety benefits and risks of simvastatin specifically in FH patients |
| [12908847](https://pubmed.ncbi.nlm.nih.gov/12908847/) | 2003 | Review | Drug Safety | Earlier review of benefits and risks of simvastatin in FH, supporting long-term statin therapy |
| [35629051](https://pubmed.ncbi.nlm.nih.gov/35629051/) | 2022 | Cohort | Journal of Clinical Medicine | Simvastatin 10mg in pediatric FH showed no adverse impact on cellular immune parameters vs. diet-only controls |
| [41824552](https://pubmed.ncbi.nlm.nih.gov/41824552/) | 2026 | Guideline | Circulation | 2026 ACC/AHA dyslipidemia guideline; statin therapy remains foundational, including for FH |
| [27417002](https://pubmed.ncbi.nlm.nih.gov/27417002/) | 2016 | Cohort/Outcomes | Journal of the American College of Cardiology | Quantifies statin-associated reduction in CAD events and mortality in heterozygous FH |
| [31696945](https://pubmed.ncbi.nlm.nih.gov/31696945/) | 2019 | Systematic Review (Cochrane) | Cochrane Database of Systematic Reviews | Systematic review of statins, including simvastatin, for children with FH |
| [28437620](https://pubmed.ncbi.nlm.nih.gov/28437620/) | 2017 | Guideline | Endocrine Practice | AACE/ACE dyslipidemia management guideline; statins as first-line therapy |
| [11383320](https://pubmed.ncbi.nlm.nih.gov/11383320/) | 2001 | Comparative Study | Nutrition, Metabolism & Cardiovascular Diseases | Head-to-head comparison of atorvastatin vs. simvastatin efficacy/safety in heterozygous FH |
| [1346327](https://pubmed.ncbi.nlm.nih.gov/1346327/) | 1992 | Study | Lancet | Early study of simvastatin's effect on lipoprotein(a) levels |

---

## Denmark Market Information

No marketing-authorisation records are present in this evidence pack: 0 authorisations on file, and market status is reported as **Not Marketed**. This should be verified against the Laegemiddelstyrelsen register directly, as simvastatin is a long-genericized molecule and this evidence pack's regulatory data may be incomplete rather than reflecting a true absence from the Danish market.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information. Key warnings, contraindications, and drug–drug interaction data were not available in this evidence pack (Data Gap DG001, Blocking severity) — this must be resolved before any formal safety sign-off (S1 stage).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
- The mechanistic fit between simvastatin (HMG-CoA reductase inhibition → LDL-receptor upregulation) and FH pathophysiology (LDL-receptor/ApoB/PCSK9 clearance defects) is direct and guideline-supported, and evidence strength meets L1 (multiple completed Phase 3 RCTs, including the pivotal ENHANCE trial).
- However, Denmark-specific regulatory and safety data are entirely unconfirmed (0 marketing authorisations on file; no SmPC warnings, contraindications, or DDI data retrieved), which blocks a full safety sign-off despite strong clinical evidence.

**To proceed, the following is needed:**
- Danish SmPC / Laegemiddelstyrelsen label data (warnings, contraindications) — currently a Blocking gap (DG001)
- Drug-specific mechanism-of-action documentation from DrugBank (High-priority gap, DG002)
- Verification of actual Danish marketing-authorisation status, since 0 authorisations for a long-genericized statin is unusual and may reflect an incomplete data pull rather than true non-availability
- A complete DDI screen, since the current query returned "not found" (0 interactions), which is implausible for simvastatin and likely reflects a data gap rather than a clean safety profile
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

