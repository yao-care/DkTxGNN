---
layout: default
title: Rozanolixizumab
parent: 僅模型預測 (L5)
nav_order: 390
evidence_level: L5
indication_count: 10
---

# Rozanolixizumab
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

# Rozanolixizumab: From IgG-Mediated Autoimmune Disease to Bronchitis (Investigational)

## One-Sentence Summary

Rozanolixizumab is an anti-FcRn monoclonal antibody; the formal approved-indication record is a **data gap** in this evidence pack, though supporting rationale text indicates it was developed for IgG-mediated autoimmune conditions (e.g. generalized myasthenia gravis, ITP, CIDP). The TxGNN model's top-ranked prediction is **Bronchitis**, but this is a knowledge-graph-only prediction with **0 clinical trials** and **0 publications**, and the model's own mechanistic rationale argues the biological link is weak — possibly even directionally opposite to benefit.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented (data gap — no approved indication text on file) |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 95.28% |
| Evidence Level | L5 |
| Denmark Market Status | Not Marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the structured record (`original_moa`: data gap). Based on the repurposing rationale supplied alongside the predictions, Rozanolixizumab is an anti-neonatal Fc receptor (FcRn) monoclonal antibody that blocks FcRn-mediated IgG recycling, thereby lowering circulating IgG concentrations. Its design target appears to be IgG-mediated autoimmune diseases such as generalized myasthenia gravis (gMG), immune thrombocytopenia (ITP), and chronic inflammatory demyelinating polyneuropathy (CIDP).

For the top-ranked predicted indication, **Bronchitis**, the evidence pack's own mechanistic analysis does **not** support plausibility: bronchitis is primarily driven by infection or airway irritants, with no known pathophysiological connection to the FcRn/IgG recycling pathway. Because anti-FcRn therapy lowers protective IgG levels, it could theoretically *increase* susceptibility to respiratory infection rather than treat it — a direction opposite to therapeutic benefit. The high TxGNN score most likely reflects proximity within the knowledge graph rather than genuine biological plausibility.

The other candidates in this batch (plasma cell myeloma, indolent plasma cell myeloma, hemoglobinopathy, gastric carcinoma) are similarly flagged in their own rationale text as indirect, unvalidated, or mechanistically unrelated associations — none are supported by any clinical or preclinical data in this pack. Overall, this is a screening-stage signal only, not a candidate ready for further evaluation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Denmark Market Information

Rozanolixizumab currently holds **no marketing authorisation** in Denmark (0 licenses on file; market status: Not Marketed).

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information. Note: TFDA/SmPC warnings and contraindications data could not be retrieved for this evaluation (blocking data gap — DG001), and no drug-drug interaction records were found.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top prediction (Bronchitis) has zero supporting clinical trials or literature, and the model's own mechanistic rationale argues against biological plausibility. Combined with the drug's unmarketed status in Denmark and a blocking gap in safety/label data, there is no basis to proceed at this time.

**To proceed, the following is needed:**
- TFDA/SmPC-equivalent warnings, contraindications, and prescribing information (currently blocking — DG001)
- Confirmed mechanism of action and original approved indication from a primary regulatory or DrugBank source (DG002)
- Independent mechanistic or preclinical validation of any candidate indication before further evidence collection
- Ongoing monitoring for new clinical trial registrations or publications on Rozanolixizumab across the candidate indications listed
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

