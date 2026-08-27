---
layout: default
title: Tocilizumab
parent: 僅模型預測 (L5)
nav_order: 440
evidence_level: L5
indication_count: 10
---

# Tocilizumab
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

# Tocilizumab: From Rheumatoid Arthritis to Ankylosing Spondylitis

## One-Sentence Summary

Tocilizumab is a humanized anti-IL-6 receptor monoclonal antibody with established use in rheumatoid arthritis. The TxGNN model predicts it may be effective for **Ankylosing Spondylitis**, but the underlying evidence base — **9 clinical trials** and **20 publications** — actually includes two terminated Phase 3 RCTs that failed to demonstrate efficacy, making this a mechanism-mismatch case rather than a supportive signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Rheumatoid Arthritis (established global indication; not confirmed via Danish licensing data — see below) |
| Predicted New Indication | Ankylosing Spondylitis |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L1 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from DrugBank for this evidence pack. Based on known information, tocilizumab is a humanized monoclonal antibody that blocks the interleukin-6 receptor (IL-6R), and its efficacy in rheumatoid arthritis (RA) — where IL-6 plays a well-established pathogenic role — has been clinically proven.

However, the mechanistic rationale does **not** transfer cleanly to ankylosing spondylitis (AS). Axial spondyloarthritis, including AS, is primarily driven by the IL-17/IL-23 axis and TNF-α rather than IL-6 signaling. This is reflected directly in the evidence: two placebo-controlled Phase 2/3 RCTs of tocilizumab in AS (NCT01209689 and NCT01209702) were both **terminated for lack of efficacy**. The TxGNN high score most likely reflects knowledge-graph co-occurrence between tocilizumab and inflammatory joint disease broadly, rather than a pathway-specific signal for AS.

In short, this is a case where a high model score is contradicted by direct clinical trial evidence — the prediction should be treated as a cautionary example rather than a promising repurposing lead.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01209689](https://clinicaltrials.gov/study/NCT01209689) | Phase 3 | Terminated | 113 | RCT of tocilizumab vs. placebo in AS patients with inadequate response to prior TNF antagonists — terminated for lack of efficacy |
| [NCT01209702](https://clinicaltrials.gov/study/NCT01209702) | Phase 2/3 | Terminated | 306 | Seamless RCT of tocilizumab vs. placebo in TNF-naïve AS patients who failed NSAIDs — terminated for lack of efficacy |
| [NCT05670301](https://clinicaltrials.gov/study/NCT05670301) | N/A | Recruiting | 2500 | Observational cytokine/biomarker profiling across systemic inflammatory diseases; not AS/tocilizumab-specific |
| [NCT02925338](https://clinicaltrials.gov/study/NCT02925338) | N/A | Completed | 1431 | Real-world observational study of Inflectra (infliximab biosimilar), not tocilizumab |
| [NCT05696106](https://clinicaltrials.gov/study/NCT05696106) | N/A | Unknown | 750000 | Registry study on risk of incident immune-mediated inflammatory diseases in biologics-treated patients |
| [NCT07477795](https://clinicaltrials.gov/study/NCT07477795) | Phase 2 | Not yet recruiting | 52 | Secukinumab (not tocilizumab) in Takayasu arteritis |
| [NCT02569736](https://clinicaltrials.gov/study/NCT02569736) | N/A | Completed | 60 | Mechanistic study of tocilizumab's effect on T follicular helper cells in RA patients |
| [NCT07138898](https://clinicaltrials.gov/study/NCT07138898) | Phase 2 | Not yet recruiting | 80 | Perioperative immunosuppressant management in rheumatology patients undergoing shoulder arthroplasty |
| [NCT01965132](https://clinicaltrials.gov/study/NCT01965132) | N/A | Recruiting | 10000 | Korean registry of biologics/targeted therapies across RA, AS and PsA — observational, not efficacy-specific |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23765873](https://pubmed.ncbi.nlm.nih.gov/23765873/) | 2014 | RCT | Annals of the Rheumatic Diseases | BUILDER-1/BUILDER-2 randomised placebo-controlled trials assessing short-term efficacy of tocilizumab in AS |
| [22452603](https://pubmed.ncbi.nlm.nih.gov/22452603/) | 2012 | Review | Inflammation & Allergy Drug Targets | Reviews IL-6 antagonism rationale and limited evidence in AS |
| [26986130](https://pubmed.ncbi.nlm.nih.gov/26986130/) | 2016 | Systematic Review | Medicine | Network meta-analysis comparing biologic regimens for AS |
| [22450391](https://pubmed.ncbi.nlm.nih.gov/22450391/) | 2012 | Review | Current Opinion in Rheumatology | Treatment alternatives for AS refractory to TNF inhibition |
| [20851032](https://pubmed.ncbi.nlm.nih.gov/20851032/) | 2010 | Case Report | Joint Bone Spine | Tocilizumab used in a patient with AS and Crohn's disease refractory to TNF antagonists |
| [33981717](https://pubmed.ncbi.nlm.nih.gov/33981717/) | 2021 | Case Report | Frontiers in Medicine | Tocilizumab for AA amyloidosis complicating AS (2 cases) |
| [19822066](https://pubmed.ncbi.nlm.nih.gov/19822066/) | 2009 | Review | Clinical and Experimental Rheumatology | Compares biologics in RA vs. AS, noting differing pathogenesis |
| [29278210](https://pubmed.ncbi.nlm.nih.gov/29278210/) | 2017 | Review | Current Pharmaceutical Biotechnology | Overview of biologics across RA, PsA and AS |
| [28413099](https://pubmed.ncbi.nlm.nih.gov/28413099/) | 2017 | Review | Seminars in Arthritis and Rheumatism | Second-line biologic therapy optimization across RA/PsA/AS |
| [29290076](https://pubmed.ncbi.nlm.nih.gov/29290076/) | 2018 | Cohort/Meta-analysis | Clinical Rheumatology | Serious infection risk with biologics in axial spondyloarthritis |

---

## Denmark Market Information

Tocilizumab currently has **no marketing authorisation on file** in this evidence pack (market status: Not marketed; 0 licenses recorded). No product-level authorisation data is available to summarize.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only direct efficacy evidence for this indication — two Phase 2/3 RCTs (NCT01209689, NCT01209702) — was terminated for lack of efficacy, and the proposed mechanism (IL-6 blockade) does not align with the IL-17/TNF-driven pathogenesis of ankylosing spondylitis. The high TxGNN score is not corroborated by, and is directly contradicted by, existing clinical trial evidence.

**To proceed, the following is needed:**
- TFDA/Danish SmPC warnings and contraindications (currently blocking safety assessment — flagged as a blocking data gap)
- Confirmed DrugBank mechanism-of-action data to formally document the IL-6R pathway rationale
- Re-review of BUILDER-1/BUILDER-2 (PMID 23765873) full trial results to confirm whether any subgroup showed partial benefit
- If pursued despite Hold status, a documented rationale for why this candidate should override two negative Phase 3 readouts
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

