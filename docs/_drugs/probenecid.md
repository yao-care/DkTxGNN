---
layout: default
title: Probenecid
parent: 僅模型預測 (L5)
nav_order: 360
evidence_level: L5
indication_count: 6
---

# Probenecid
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

# Probenecid: From an Undocumented Original Indication to Renal Hypouricemia

## One-Sentence Summary

> Probenecid (DrugBank DB01032) is a well-established uricosuric agent, but this evidence pack does not record a confirmed original indication or mechanism of action for it.
> The TxGNN model predicts a possible link to **Renal Hypouricemia** ("hypouricemia, renal") with a **99.73%** prediction score, but this is currently supported only by **0 clinical trials** and **20 publications that describe the disease itself rather than probenecid as a treatment for it**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (drug.original_indications is empty) |
| Predicted New Indication | Renal Hypouricemia (hypouricemia, renal) |
| TxGNN Prediction Score | 99.73% |
| Evidence Level | L5 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for probenecid is not available in this evidence pack (flagged as data gap DG002, High severity), and no original indication is on record (drug.original_indications is empty). Because of this, the mechanistic rationale below is necessarily limited and should be treated as provisional pending confirmed MOA data.

There is a specific concern worth flagging: renal hypouricemia is a condition of *abnormally low* serum uric acid caused by defective renal tubular urate reabsorption, and pharmacologically it is the opposite problem from hyperuricemia/gout (which uricosuric drugs are typically used to treat by *increasing* urate excretion). Reviewing the 20 supporting publications, probenecid does not appear as a proposed treatment for this disease — it appears repeatedly as a **diagnostic challenge agent** ("the probenecid test"), used by researchers to characterize the defective urate transporter (URAT1/SLC22A12) in these patients (e.g. PMID 8341392, PMID 7099326, PMID 854144). In several of these reports, urate excretion in affected patients is described as minimally responsive, or even paradoxically decreased, when probenecid is administered.

This pattern is consistent with the caution already recorded elsewhere in this evidence pack: the same underlying logic (a uricosuric drug being mismatched to a low-urate condition) is explicitly why rank 3/4 candidate "Lesch-Nyhan syndrome" was already scored **Evidence Level L4, Hold** in this pack, with the rationale noting that uricosuric agents are relatively contraindicated in conditions of urate overload or defective urate handling. Given the same class of mechanistic mismatch applies to renal hypouricemia, the top-ranked prediction should be treated with equivalent caution rather than as a straightforward repurposing opportunity.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [16678460](https://pubmed.ncbi.nlm.nih.gov/16678460/) | 2006 | Pending classification | Molecular Genetics and Metabolism | Hereditary renal hypouricemia is caused by loss-of-function mutations in SLC22A12 (URAT1), the transporter responsible for proximal tubular urate reabsorption |
| [7771493](https://pubmed.ncbi.nlm.nih.gov/7771493/) | 1995 | Pending classification | American Journal of Kidney Diseases | Review of renal hypouricemia and its association with exercise-induced acute renal failure; discusses prevention strategies |
| [14694169](https://pubmed.ncbi.nlm.nih.gov/14694169/) | 2004 | Pending classification | Journal of the American Society of Nephrology | Clinical/molecular analysis of 32 Japanese renal hypouricemia patients; correlates SLC22A12 genotype with urate clearance |
| [3813739](https://pubmed.ncbi.nlm.nih.gov/3813739/) | 1987 | Pending classification | Archives of Internal Medicine | Diabetic patients show increased pyrazinamide-suppressible urate clearance underlying diabetic renal hypouricemia |
| [14655203](https://pubmed.ncbi.nlm.nih.gov/14655203/) | 2003 | Pending classification | American Journal of Kidney Diseases | Case report of two siblings with hereditary renal hypouricemia and exercise-induced acute renal failure |
| [1944743](https://pubmed.ncbi.nlm.nih.gov/1944743/) | 1991 | Pending classification | Nephron | Study of uricosuric mechanisms in type I diabetics with elevated urate clearance and fractional excretion |
| [1656732](https://pubmed.ncbi.nlm.nih.gov/1656732/) | 1991 | Pending classification | American Journal of Kidney Diseases | Case report: cholangiocarcinoma associated with severe renal hypouricemia; renal mechanism studied |
| [31650389](https://pubmed.ncbi.nlm.nih.gov/31650389/) | 2020 | Pending classification | Clinical Rheumatology | Narrative review of hypouricemia etiology for practicing rheumatologists |
| [8341392](https://pubmed.ncbi.nlm.nih.gov/8341392/) | 1993 | Pending classification | Nephron | Novel subtype of renal hypouricemia with no urate response to either pyrazinamide or **probenecid** challenge |
| [7099326](https://pubmed.ncbi.nlm.nih.gov/7099326/) | 1982 | Pending classification | Nephron | Familial case where urate excretion was **paradoxically decreased** by probenecid administration |

*Study-type classification for this candidate is marked "pending" in the source data; types above are shown as provided rather than inferred.*

---

## Denmark Market Information

No marketing authorisations are recorded for probenecid in this evidence pack. Market status is listed as **Not marketed**, with 0 total licenses on file.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information. Note: this evidence pack marks the drug-label warnings/contraindications review (DG001) as a **Blocking** data gap — a formal safety assessment cannot proceed until this is resolved.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- Foundational data is missing at the Blocking/High severity level (DG001: label warnings/contraindications; DG002: mechanism of action), so no formal safety assessment is currently possible.
- The predicted indication itself is mechanistically questionable: probenecid is a uricosuric agent, and the supporting literature uses it as a diagnostic probe for defective urate reabsorption rather than as a proposed therapy for renal hypouricemia — a pattern of mismatch consistent with the "Hold" already assigned to the related Lesch-Nyhan candidate in this same pack.
- There are zero clinical trials and no Denmark marketing authorisation to anchor a Go decision.

**To proceed, the following is needed:**
- Confirmed original indication and mechanism of action for probenecid (resolve DG002)
- TFDA/Danish product label warnings and contraindications (resolve DG001, Blocking)
- Clarification from the TxGNN/evidence pipeline on directionality — i.e., whether "hypouricemia, renal" was intended as a target disease for treatment or reflects a network association driven by probenecid's role as a urate-transport probe
- If pursued further, pharmacological justification for why increasing urate excretion would benefit a condition already characterized by excessive urate loss
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

