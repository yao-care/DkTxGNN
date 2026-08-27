---
layout: default
title: Imiglucerase
parent: 僅模型預測 (L5)
nav_order: 227
evidence_level: L5
indication_count: 10
---

# Imiglucerase
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

# Imiglucerase: From Gaucher Disease to Hurler Syndrome

## One-Sentence Summary

Imiglucerase (DrugBank DB00053) is a recombinant glucocerebrosidase enzyme replacement therapy, internationally established as treatment for Gaucher disease.
The TxGNN model predicts it may be effective for **Hurler syndrome (MPS I)**, with a very high similarity score but **no supporting clinical trials** and only **2 general background publications**, neither of which studies imiglucerase specifically in Hurler syndrome.
The drug's own repurposing rationale flags this prediction as a likely **false positive** driven by category-level embedding similarity ("lysosomal storage disease + enzyme replacement therapy") rather than genuine biochemical mechanism overlap.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Gaucher disease (enzyme replacement therapy)¹ |
| Predicted New Indication | Hurler syndrome (Mucopolysaccharidosis type I) |
| TxGNN Prediction Score | 99.52% |
| Evidence Level | L5 (model prediction only) |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

¹ The evidence pack's `drug.original_indications` field and `original_moa` field are both empty/data-gap (see DG002). "Gaucher disease" is stated here based on internationally recognized labeling for imiglucerase (Cerezyme), not from data contained in this evidence pack.

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack (Data Gap DG002). Based on publicly known pharmacology, imiglucerase is a recombinant form of human glucocerebrosidase, used as enzyme replacement therapy (ERT) to break down accumulated glucocerebroside in Gaucher disease.

However, the mechanistic link to Hurler syndrome is weak. Hurler syndrome (severe MPS I) is caused by deficiency of **alpha-L-iduronidase (IDUA)**, leading to accumulation of heparan sulfate and dermatan sulfate — a completely different enzyme and substrate from glucocerebrosidase. A disease-specific ERT (laronidase, Aldurazyme) is already approved for MPS I. The high TxGNN score most likely reflects a shared **class-level embedding pattern** ("lysosomal storage disease" + "enzyme replacement therapy") rather than an actual shared biochemical pathway, and should be treated as a **high-risk false-positive pattern** rather than a genuine repurposing signal.

Supporting literature identified in this evidence pack does not resolve this concern: both publications are general reviews of enzyme replacement therapy across multiple lysosomal storage diseases (mentioning Hurler syndrome only as one example among several), with no data specific to imiglucerase's efficacy in MPS I.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [20534487](https://pubmed.ncbi.nlm.nih.gov/20534487/) | 2010 | Review/Methodology | Proceedings of the National Academy of Sciences | General overview of PET imaging for monitoring enzyme replacement therapy across lysosomal storage diseases (Gaucher, Fabry, Hurler, Hunter, Maroteaux-Lamy, Pompe); not specific to imiglucerase efficacy in Hurler syndrome |
| [21211680](https://pubmed.ncbi.nlm.nih.gov/21211680/) | 2010 | Review | La Revue de médecine interne | General review of enzyme replacement therapy history and development across lysosomal storage diseases, referencing imiglucerase (Cerezyme) in the context of Gaucher disease treatment, not Hurler syndrome specifically |

---

## Denmark Market Information

Imiglucerase currently has **no marketing authorisation** on record in Denmark (`market_status: 未上市` / Not marketed, `total_licenses: 0`). No Laegemiddelstyrelsen national or EMA centralised authorisation entries were found in this evidence pack.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

*(Note: This evidence pack has a Blocking data gap — DG001 — for label warnings/contraindications, meaning safety review (S1 stage) cannot proceed until this data is obtained.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high, but the drug's own repurposing rationale identifies this as a likely embedding-level false positive: imiglucerase's target enzyme (glucocerebrosidase) is mechanistically unrelated to the alpha-L-iduronidase deficiency underlying Hurler syndrome, for which a disease-specific ERT (laronidase) is already approved. There are no clinical trials and no disease-specific literature supporting imiglucerase for this indication, and the drug is not currently marketed in Denmark. Evidence level is L5 (model prediction only) and does not support progression past initial screening.

**To proceed, the following is needed:**
- Original mechanism of action (MOA) data for imiglucerase (Data Gap DG002)
- Danish/EU label warnings and contraindications (Data Gap DG001 — Blocking; required before any S1 safety screening)
- Confirmation of original approved indication(s) from a structured regulatory source
- Any preclinical or mechanistic studies directly testing glucocerebrosidase-based ERT in MPS I models, to either substantiate or rule out the predicted signal
- Given that a specific approved therapy (laronidase) already exists for Hurler syndrome, a clear clinical rationale for why imiglucerase repurposing would offer added value
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

