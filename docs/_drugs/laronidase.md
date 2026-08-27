---
layout: default
title: Laronidase
parent: 僅模型預測 (L5)
nav_order: 255
evidence_level: L5
indication_count: 10
---

# Laronidase
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

# Laronidase: From Mucopolysaccharidosis I to Lysosomal Storage Disease with Skeletal Involvement

## One-Sentence Summary

Laronidase is a recombinant human alpha-L-iduronidase enzyme replacement therapy, originally developed for **Mucopolysaccharidosis I (MPS I; Hurler / Hurler-Scheie / Scheie syndrome)** — though this evidence pack's structured `original_indications` field is empty, so that indication is inferred from the pack's own mechanistic rationale and literature, not confirmed by a regulatory source. TxGNN's top prediction, **lysosomal storage disease with skeletal involvement**, is in practice a broader ontology label for the same underlying disease the drug already treats, rather than a genuinely new indication. Evidence support is moderate: **4 publications** (no registered clinical trials) at evidence level **L2**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Mucopolysaccharidosis I (Hurler / Hurler-Scheie / Scheie syndrome) — not present in this pack's `original_indications`/license data; inferred from the evidence pack's own rationale text |
| Predicted New Indication | Lysosomal storage disease with skeletal involvement |
| TxGNN Prediction Score | 99.31% |
| Evidence Level | L2 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack (flagged as a High-severity data gap, DG002). Based on the information that is available, Laronidase is a recombinant form of human alpha-L-iduronidase, the lysosomal enzyme that is deficient in MPS I. Its efficacy in enzyme-replacement therapy for MPS I has been established through decades of clinical use, and mechanistically this activity extends directly to any condition defined by alpha-L-iduronidase deficiency and resulting glycosaminoglycan (GAG) accumulation in bone and connective tissue.

Importantly, the pack's own `repurposing_rationale` for this top-ranked prediction states that "lysosomal storage disease with skeletal involvement" is very likely the same disease as MPS I, simply captured under a broader/different ontology term — the TxGNN candidate surfaced here mainly because the drug's *original* indication was not populated in this dataset. In other words, this is best read as **evidence confirming an already-known use**, not a novel repurposing opportunity. A genuine novel-indication assessment would require re-running this analysis with `original_indications` correctly populated so that TxGNN candidates are filtered against the true label set.

For transparency: the remaining candidates in this pack (Sanfilippo syndrome, lysosomal disease with hypertrophic cardiomyopathy, syndromic neurometabolic disease with X-linked intellectual disability, eyelids malposition disorder) were all scored **L4–L5 with a Hold recommendation**. Several show evidence mismatches — e.g., the Sanfilippo syndrome literature returned by the pipeline is in fact MPS I literature, most likely due to keyword overlap on "mucopolysaccharidosis" rather than true topical relevance — and the X-linked and hypertrophic-cardiomyopathy candidates lack a plausible genetic/mechanistic basis. None of these support further action at this time.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [23127271](https://pubmed.ncbi.nlm.nih.gov/23127271/) | 2012 | Cohort/Case series | Pediatric Neurology | 6.5-year follow-up of enzyme replacement therapy in an attenuated MPS I (Scheie syndrome) case; documented skeletal, cardiac, and ophthalmologic outcomes over long-term treatment |
| [25345091](https://pubmed.ncbi.nlm.nih.gov/25345091/) | 2014 | Review | Pediatric Endocrinology Reviews | Overview of MPS I disease spectrum (Hurler / Hurler-Scheie / Scheie), diagnosis via urine GAG pattern and iduronidase enzyme assay |
| [18758061](https://pubmed.ncbi.nlm.nih.gov/18758061/) | 2008 | In vitro (basic research) | Biological & Pharmaceutical Bulletin | Demonstrated mannose-6-phosphate receptor-mediated uptake of laronidase by MPS I fibroblasts and osteoblasts, with lysosomal processing and substrate cleavage |
| [12196045](https://pubmed.ncbi.nlm.nih.gov/12196045/) | 2002 | Review | BioDrugs | Early development overview of laronidase as recombinant alpha-L-iduronidase ERT for MPS I, including orphan drug designation and Phase I trial data |

---

## Denmark Market Information

Laronidase currently has no marketing authorisation registered in Denmark (0 authorisations on file; market status: Not marketed).

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information. This evidence pack does not contain TFDA/Laegemiddelstyrelsen warning or contraindication data (flagged as a Blocking data gap, DG001), and no drug-drug interaction records were found.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The underlying evidence level (L2, supported by MPS I clinical literature) is reasonably solid, but this "new indication" appears to substantially overlap with Laronidase's already-known use rather than representing a genuinely novel repurposing candidate. Combined with the missing safety/label data, this should not be treated as a green-light case.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): obtain the approved SmPC/product warnings and contraindications before any safety evaluation (S1) can proceed
- Resolve DG002: obtain confirmed mechanism-of-action and original-indication data from DrugBank/regulatory sources to determine whether "lysosomal storage disease with skeletal involvement" is truly a new indication or a relabeling of MPS I
- If a genuinely novel indication is the goal, re-run the TxGNN candidate generation with a correctly populated `original_indications` field so existing-use overlaps are filtered out
- Given zero marketing authorisations in Denmark, confirm import/named-patient-use pathway status before any clinical consideration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

