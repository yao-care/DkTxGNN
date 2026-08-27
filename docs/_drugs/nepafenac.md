---
layout: default
title: Nepafenac
parent: 僅模型預測 (L5)
nav_order: 308
evidence_level: L5
indication_count: 10
---

# Nepafenac
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

# Nepafenac: From Post-Cataract Surgery Ocular Inflammation to Eye Disease

## One-Sentence Summary

Nepafenac is a topical ophthalmic NSAID prodrug (converted in the eye to amfenac), whose extensive trial record shows it is already established for preventing and treating ocular inflammation and pain associated with cataract surgery.
The TxGNN model predicts continued/broader effectiveness for **Eye Disease**,
with **41 clinical trials** and **20 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Ocular inflammation and pain associated with cataract surgery (inferred from the trial evidence in this pack; no formal local label text was available) |
| Predicted New Indication | Eye Disease |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L1 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data from a formal drug label are not available (data gap). Based on general pharmacological information reflected throughout the evidence pack, Nepafenac is a topical ophthalmic NSAID that is converted to its active metabolite, amfenac, after ocular penetration; amfenac inhibits cyclooxygenase (COX-1/COX-2) to suppress prostaglandin-mediated inflammation. This mechanism explains its established role in preventing and treating inflammation and pain after cataract surgery, and its investigated use in diabetic macular edema, cystoid macular edema, laser iridotomy, and vitreoretinal procedures.

The predicted new indication, "Eye Disease," is broad and largely coincides with the domain in which Nepafenac already operates as an approved ophthalmic anti-inflammatory. Rather than pointing to a genuinely novel organ system or disease mechanism, the TxGNN signal here appears to reflect and reinforce Nepafenac's known pharmacology — its anti-inflammatory action is mechanistically plausible across a range of ocular inflammatory conditions beyond the primary cataract-surgery label, such as diabetic macular edema and post-vitrectomy inflammation, both of which are well represented in the clinical trial evidence below.

Because the predicted indication label is generic, this should be treated as confirmatory of Nepafenac's existing therapeutic class rather than a distinct repurposing opportunity; further disambiguation of the specific eye disease subtype is needed before this can support a concrete indication-expansion decision.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01109173](https://clinicaltrials.gov/study/NCT01109173) | Phase 3 | Completed | 2120 | Safety and efficacy of nepafenac ophthalmic suspension 0.3% for prevention/treatment of inflammation and pain after cataract extraction |
| [NCT01853072](https://clinicaltrials.gov/study/NCT01853072) | Phase 3 | Completed | 881 | Nepafenac 0.3% once daily superior to vehicle for clinical outcomes in diabetic subjects after cataract surgery |
| [NCT01872611](https://clinicaltrials.gov/study/NCT01872611) | Phase 3 | Completed | 819 | Companion Phase 3 trial confirming superiority of nepafenac 0.3% vs vehicle in diabetic subjects post-cataract surgery |
| [NCT03025945](https://clinicaltrials.gov/study/NCT03025945) | NA | Completed | 662 | Adjunctive once-daily nepafenac 0.3% vs placebo for prevention of pseudophakic cystoid macular edema |
| [NCT03499873](https://clinicaltrials.gov/study/NCT03499873) | Phase 3 | Completed | 448 | Bioequivalence of generic nepafenac 0.3% suspension vs Ilevro for pain/inflammation after cataract surgery |
| [NCT01318499](https://clinicaltrials.gov/study/NCT01318499) | Phase 2 | Completed | 1342 | Comparison of nepafenac 0.3% vs 0.1% vs vehicle for prevention/treatment of post-cataract inflammation and pain |
| [NCT01426854](https://clinicaltrials.gov/study/NCT01426854) | Phase 3 | Completed | 260 | Nepafenac 0.1% superior to vehicle for ocular inflammation and pain in Chinese cataract-surgery subjects |
| [NCT00333255](https://clinicaltrials.gov/study/NCT00333255) | Phase 3 | Completed | 267 | Nepafenac 0.1% compared to Acular LS for treating post-cataract ocular inflammation |
| [NCT00405730](https://clinicaltrials.gov/study/NCT00405730) | Phase 3 | Completed | 227 | European study: nepafenac 0.1% vs ketorolac vs placebo for post-cataract inflammation and pain |
| [NCT00332774](https://clinicaltrials.gov/study/NCT00332774) | Phase 3 | Completed | 149 | 3-month safety comparison of nepafenac 0.1% vs Acular LS 0.4% and vehicle after cataract surgery |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39936354](https://pubmed.ncbi.nlm.nih.gov/39936354/) | 2025 | Systematic Review & Meta-analysis | European Journal of Ophthalmology | Nepafenac reduces foveal thickening and improves visual outcomes after cataract surgery when added to topical steroids |
| [35196591](https://pubmed.ncbi.nlm.nih.gov/35196591/) | 2022 | RCT | Ophthalmology Glaucoma | Nepafenac 0.1% vs bromfenac 0.09% for inflammation control after laser peripheral iridotomy |
| [32672612](https://pubmed.ncbi.nlm.nih.gov/32672612/) | 2020 | RCT | Ophthalmology Glaucoma | Nepafenac 0.1% vs prednisolone acetate 1% for inflammation control after laser peripheral iridotomy |
| [22795976](https://pubmed.ncbi.nlm.nih.gov/22795976/) | 2012 | RCT | J Cataract Refract Surg | Prophylactic nepafenac 0.1% vs ketorolac vs placebo evaluated for prevention of macular edema post-phacoemulsification |
| [24345529](https://pubmed.ncbi.nlm.nih.gov/24345529/) | 2014 | Phase 3 Clinical Study | J Cataract Refract Surg | Once-daily nepafenac 0.3% effective in preventing/treating ocular pain and inflammation after cataract surgery |
| [35025078](https://pubmed.ncbi.nlm.nih.gov/35025078/) | 2022 | Review | Drugs | Reviews diagnostic and therapeutic agents, including topical NSAIDs, for non-infectious corneal injury |
| [34210237](https://pubmed.ncbi.nlm.nih.gov/34210237/) | 2022 | Review | Clinical & Experimental Optometry | Reviews the established role of topical NSAIDs, including nepafenac, in routine cataract surgery |
| [26474497](https://pubmed.ncbi.nlm.nih.gov/26474497/) | 2016 | Pharmacokinetic Study | Experimental Eye Research | Characterizes distribution of nepafenac/amfenac to the posterior segment of the eye |
| [17259381](https://pubmed.ncbi.nlm.nih.gov/17259381/) | 2007 | Preclinical (Animal) | Diabetes | Topical nepafenac inhibits diabetes-induced retinal microvascular disease in a rat model |
| [19897019](https://pubmed.ncbi.nlm.nih.gov/19897019/) | 2010 | Preclinical | Brain Research Bulletin | Nepafenac/amfenac inhibit retinal angiogenesis in vitro and in the rat OIR model |

---

## Denmark Market Information

Nepafenac currently has **no marketing authorisation on file in Denmark** (Laegemiddelstyrelsen market status: not marketed; 0 licenses recorded). No national or centralised (EMA) authorisation details are available in this evidence pack.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information. No key warnings, contraindications, or drug-interaction data were available in this evidence pack (all flagged as data gaps), including a **Blocking**-severity gap on local label warnings/contraindications that must be resolved before any safety pre-assessment (S1) can proceed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- A Blocking-severity data gap (missing TFDA/local label warnings and contraindications) prevents entry into the S1 safety pre-assessment stage, and Nepafenac is not currently marketed in Denmark (0 marketing authorisations).
- Although evidence level is L1 (multiple completed Phase 3 RCTs), the predicted indication "Eye Disease" is generic and largely overlaps with Nepafenac's already-established ophthalmic anti-inflammatory use rather than representing a clearly novel repurposing signal.

**To proceed, the following is needed:**
- Local/SmPC label data: warnings, contraindications, and drug interactions (source: TFDA/EMA SmPC)
- Formal mechanism-of-action documentation (source: DrugBank)
- Disambiguation of the specific "eye disease" subtype intended by the TxGNN prediction, to distinguish genuine repurposing value from confirmation of existing use
- Status/timeline of any marketing authorisation application for Denmark
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

