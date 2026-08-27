---
layout: default
title: Lornoxicam
parent: 僅模型預測 (L5)
nav_order: 271
evidence_level: L5
indication_count: 10
---

# Lornoxicam
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

# Lornoxicam: From NSAID Pain Management to Rheumatoid Arthritis

## One-Sentence Summary

Lornoxicam is an oxicam-class NSAID with COX-1/COX-2 inhibitory activity, already described in the literature as used for musculoskeletal and joint pain; its original approved indication(s) are not on file in this evidence pack. The TxGNN model predicts it may be effective for **Rheumatoid Arthritis**, with **0 clinical trials** and **20 publications** currently associated with this direction, though most of the literature is preclinical or formulation-focused rather than clinical-efficacy evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on file — no approved indication text available in current records |
| Predicted New Indication | Rheumatoid Arthritis |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L3 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for lornoxicam in this evidence pack. Based on the literature retrieved (PMID 8706598, PMID 22469263), lornoxicam is a short half-life oxicam-class NSAID with combined COX-1/COX-2 inhibition, analgesic, anti-inflammatory and antipyretic properties, administered orally or parenterally. This pharmacological class is a standard adjunct in the symptomatic management of inflammatory joint disease.

Notably, one of the retrieved reviews (PMID 22469263) already describes lornoxicam as used "in the muscular skeletal and joint disorders such as osteoarthritis and rheumatoid arthritis." Because this evidence pack's `original_indications` field is empty, it cannot be confirmed whether rheumatoid arthritis is a genuinely new indication or an already-established use in other markets. This distinction is material: if RA is already a labeled use elsewhere, the TxGNN signal reflects known pharmacology rather than a novel repurposing hypothesis, and this should be verified before further investment.

Mechanistically, the prediction is plausible — COX inhibition targeting prostaglandin-mediated joint inflammation is a well-established mode of action in RA — but the supporting evidence base for this candidate consists almost entirely of formulation/delivery studies (microsponge gels, transdermal patches, nanoparticles) and preclinical models rather than controlled clinical trials in RA patients.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12404032](https://pubmed.ncbi.nlm.nih.gov/12404032/) | 2002 | Crossover double-blind study | Reumatismo | Compared lornoxicam 8mg/16mg vs. diclofenac 150mg/day in RA patients for analgesic dose-finding |
| [12207202](https://pubmed.ncbi.nlm.nih.gov/12207202/) | 2002 | Long-term clinical study | Minerva medica | Assessed long-term efficacy and safety of lornoxicam in RA |
| [8706598](https://pubmed.ncbi.nlm.nih.gov/8706598/) | 1996 | Review | Drugs | Comprehensive pharmacology review; lornoxicam as effective as opioid analgesics in short trials |
| [22469263](https://pubmed.ncbi.nlm.nih.gov/22469263/) | 2011 | Review | Profiles of Drug Substances, Excipients and Related Methodology | Comprehensive substance profile; notes existing use in osteoarthritis and RA |
| [27086708](https://pubmed.ncbi.nlm.nih.gov/27086708/) | 2016 | Clinical study | Pain Management | Evaluated GI tolerability of lornoxicam (COX-1/COX-2 inhibitor) in acute and rheumatic pain |
| [12240779](https://pubmed.ncbi.nlm.nih.gov/12240779/) | 2002 | Literature review | Clinical Therapeutics | Reviewed dose-effect relationships of NSAIDs (including lornoxicam) in RA and OA |
| [18479176](https://pubmed.ncbi.nlm.nih.gov/18479176/) | 2008 | Phase I crossover study | Clinical Drug Investigation | Compared pharmacokinetics of lornoxicam quick-release tablet, standard tablet, and IM injection |
| [29056774](https://pubmed.ncbi.nlm.nih.gov/29056774/) | 2017 | Review | Reumatologia | Discussed glucocorticoid chronotherapy timing in RA management (adjacent topic, not lornoxicam-specific) |
| [27042335](https://pubmed.ncbi.nlm.nih.gov/27042335/) | 2016 | Review | RMD Open | Discussed circadian inflammation and glucocorticoid chronotherapy in RA (adjacent topic) |
| [29026298](https://pubmed.ncbi.nlm.nih.gov/29026298/) | 2017 | Preclinical (animal model) | International Journal of Nanomedicine | Compared lornoxicam-loaded nanomicellar formulation vs. free drug in experimental RA models |

## Denmark Market Information

Lornoxicam currently holds no marketing authorisations in Denmark (0 licenses on file; market status: not marketed).

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information. Key warnings, contraindications, and drug-drug interaction data for lornoxicam are not currently available in this evidence pack (including a **Blocking**-severity gap on SmPC warnings/contraindications), so no preliminary safety screening (S1) can be performed at this time.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- No completed clinical trials directly evaluate lornoxicam in rheumatoid arthritis; the literature base is dominated by formulation/delivery and preclinical studies rather than controlled clinical evidence, and at least one review suggests RA may already be a known use of this drug class rather than a novel indication.
- A Blocking-severity data gap on TFDA/label warnings and contraindications (DG001) currently prevents any preliminary safety evaluation, and the drug is not marketed in Denmark.

**To proceed, the following is needed:**
- Confirm lornoxicam's actual approved indication(s) in other jurisdictions to determine whether rheumatoid arthritis represents genuine repurposing or an already-labeled use
- Obtain SmPC warnings, contraindications, and drug interaction data (resolves Blocking gap DG001)
- Obtain mechanism of action detail from DrugBank (DG002)
- Identify or commission a completed Phase 2/3 RCT specifically evaluating lornoxicam in RA patients

**Note for reviewers:** Among the other candidates screened for lornoxicam in this evidence pack, "migraine disorder" (score 99.87%) is supported by one completed Phase 2, double-blind, placebo-controlled trial (NCT00293657, n=150) — comparatively stronger clinical evidence than the top-ranked RA candidate — and may warrant a separate, dedicated evaluation.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

