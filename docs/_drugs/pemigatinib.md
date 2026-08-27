---
layout: default
title: Pemigatinib
parent: 僅模型預測 (L5)
nav_order: 343
evidence_level: L5
indication_count: 10
---

# Pemigatinib
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

Using the given Evidence Pack, I'll flag upfront that this pack is unusual: `original_indications` is empty and `original_moa` is a data gap, and every one of the 10 predicted-indication entries is either L5 (model-only) or, at best, L4 with a single review citation — several rationale fields explicitly self-flag as likely knowledge-graph noise or safety-signal-in-wrong-direction. I'm reporting this honestly rather than dressing it up as a strong candidate.

# Pemigatinib: From Unrecorded Original Indication to Multiple Endocrine Neoplasia

## One-Sentence Summary

> Pemigatinib's originally approved indication is not recorded in this evidence pack (data gap DG002), though the model's own rationale text identifies it as an FGFR1/2/3 kinase inhibitor.
> The TxGNN model's top-ranked signal is **Multiple Endocrine Neoplasia**, but this prediction is unsupported by any clinical trial or literature evidence, and the accompanying mechanistic rationale itself flags it as a likely knowledge-graph artefact rather than a genuine biological signal.
> Across all 10 predictions in this pack, none reach an actionable evidence level — the best-supported signal (HER2-positive breast carcinoma) is only L4/"Research Question," and Pemigatinib is not currently marketed in Denmark.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in this evidence pack (data gap — confirm via DrugBank/SmPC) |
| Predicted New Indication | Multiple Endocrine Neoplasia |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L5 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available as a structured field in this evidence pack (data gap DG002). However, the model's own repurposing rationale consistently describes Pemigatinib as an FGFR1/2/3 (fibroblast growth factor receptor) tyrosine kinase inhibitor, so this classification can be treated as reliable context rather than a fabricated addition.

For the top-ranked signal, **Multiple Endocrine Neoplasia (MEN)**, the rationale text is explicitly negative: MEN is driven by germline mutations in *RET*, *MEN1*, and *CDKN1B*, none of which have a known direct relationship to FGFR signalling. The rationale states there is no literature or preclinical support for an FGFR inhibitor having any role in MEN, and it explicitly labels this prediction score as "lacking an explainable biological basis," suspected to arise from indirect co-occurrence noise in the knowledge graph rather than a true drug–disease relationship. The same disease appears twice in the ranked list (ranks 1 and 2) with identical scores, which is consistent with a duplication artefact in the underlying prediction table rather than independent corroborating evidence.

The third-ranked signal, **amenorrhea**, is even more concerning from a safety standpoint: FGFR1 loss-of-function is a known cause of Kallmann syndrome / hypogonadotropic hypogonadism, which can present with amenorrhea. Since Pemigatinib pharmacologically *inhibits* FGFR (the same direction as the loss-of-function mutation), the rationale explicitly states this should be read as a potential **adverse-effect signal** (i.e., Pemigatinib could plausibly cause or worsen amenorrhea), not as evidence of therapeutic benefit. This candidate should not be interpreted as a repurposing opportunity.

The only signal with any literature support is **HER2-positive breast carcinoma** (ranks 5–6, score 99.49%, evidence level L4, decision stage S1 "Research Question"). The rationale describes a plausible indirect mechanism: FGFR1/2 amplification/activation has been reported in the literature as a bypass-resistance pathway to anti-HER2 therapies (e.g., trastuzumab, lapatinib), suggesting a theoretical role for an FGFR inhibitor like Pemigatinib as an *add-on* to overcome HER2-targeted-therapy resistance — not as monotherapy for HER2-positive breast cancer itself. The single supporting citation, however, is a general 2021 review of FDA-approved kinase inhibitors, not a study specific to Pemigatinib or this combination hypothesis, so this remains a research question rather than a supported indication.

Two further entries — **infectious bovine rhinotracheitis** and **malignant catarrh** — are veterinary/ruminant herpesvirus diseases with no relevance to human drug repurposing; the rationale flags these as likely cross-species ontology contamination in the knowledge graph and recommends they be excluded during data cleaning rather than evaluated further. **Cytomegalovirus infection** likewise has no rationale-supported mechanistic link to FGFR signalling and no literature or trial evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

*(This applies to the top-ranked indication, Multiple Endocrine Neoplasia. No candidate disease in this evidence pack — across all 10 ranked entries — has any registered ClinicalTrials.gov or ICTRP trial.)*

---

## Literature Evidence

Currently no related literature available for the top-ranked indication (Multiple Endocrine Neoplasia).

### Other Predicted Signals in This Evidence Pack

For transparency, since this pack contains 10 ranked entries (5 unique diseases, each duplicated), the one literature citation that does exist belongs to a lower-ranked, higher-evidence-level candidate:

| PMID | Year | Type | Journal | Associated Disease | Key Findings |
|------|-----|------|------|------|---------|
| [33513356](https://pubmed.ncbi.nlm.nih.gov/33513356/) | 2021 | Review | Pharmacological Research | HER2-positive breast carcinoma | General review of FDA-approved kinase inhibitors; not specific to Pemigatinib or to a FGFR/HER2 combination strategy |

| Disease (unique) | Best TxGNN Score | Evidence Level | Decision Stage | Recommendation | Caveat |
|---|---|---|---|---|---|
| Multiple endocrine neoplasia | 99.71% | L5 | S0 | Hold | No mechanistic link to FGFR; suspected KG noise |
| Amenorrhea | 99.54% | L5 | S0 | Hold | Mechanism points to Pemigatinib *causing* amenorrhea, not treating it — safety signal, not therapeutic |
| HER2-positive breast carcinoma | 99.49% | L4 | S1 | Research Question | Only candidate with any literature; hypothesis is combination-with-anti-HER2-therapy, not monotherapy |
| Cytomegalovirus infection | 99.46% | L5 | S0 | Hold | No known mechanistic link |
| Infectious bovine rhinotracheitis / Malignant catarrh | 99.43% | L5 | S0 | Hold | Veterinary/animal diseases — likely cross-species ontology noise; recommend exclusion from ranking |

No candidate in this pack currently supports a Go decision.

---

## Denmark Market Information

Pemigatinib is **not currently marketed in Denmark**. The evidence pack records 0 Marketing Authorisations (neither national Laegemiddelstyrelsen nor centralised EMA authorisations), so no product/dosage-form table can be produced at this time.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information. This evidence pack does not currently contain key warnings, contraindications, or drug–drug interaction data for Pemigatinib (data gap DG001, marked as Blocking severity — this must be resolved before any S1 safety pre-assessment can proceed).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top-ranked prediction (Multiple Endocrine Neoplasia) is explicitly flagged by its own mechanistic rationale as lacking biological plausibility and likely representing knowledge-graph noise, with zero supporting trials or literature.
- The second candidate (amenorrhea) points to a probable **adverse-effect** signal rather than a therapeutic opportunity given Pemigatinib's FGFR-inhibitory mechanism.
- The only candidate reaching a "Research Question" stage (HER2-positive breast carcinoma, combination hypothesis) is supported by a single non-specific review article, not primary evidence.
- Blocking safety data (Danish SmPC warnings/contraindications, DG001) and mechanism-of-action confirmation (DG002) are both missing, so this candidate cannot proceed to an S1 safety pre-assessment regardless of the disease target chosen.
- Pemigatinib is not marketed in Denmark, so there is no existing local regulatory/safety dossier to draw on.

**To proceed, the following is needed:**
- Resolve DG001: obtain Pemigatinib's approved warnings/contraindications (e.g., from the EMA SmPC, since it is not registered in Denmark) — currently a Blocking gap
- Resolve DG002: confirm mechanism of action via the DrugBank API
- Confirm and document Pemigatinib's original approved indication(s), which are entirely absent from this evidence pack
- Flag the veterinary-disease entries (infectious bovine rhinotracheitis, malignant catarrh) to the knowledge-graph data-cleaning pipeline for likely exclusion
- If the amenorrhea signal is pursued at all, redirect it to pharmacovigilance/adverse-event review rather than repurposing evaluation
- If the HER2-positive breast carcinoma combination hypothesis is pursued, commission a targeted literature search specifically on FGFR-inhibitor + anti-HER2-therapy resistance reversal, rather than relying on the current general kinase-inhibitor review citation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

