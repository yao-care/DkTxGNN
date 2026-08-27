---
layout: default
title: Remdesivir
parent: 僅模型預測 (L5)
nav_order: 371
evidence_level: L5
indication_count: 10
---

# Remdesivir
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

# Remdesivir: From COVID-19 to Multiple Endocrine Neoplasia

## One-Sentence Summary

Remdesivir is an intravenous antiviral (RNA-dependent RNA polymerase inhibitor) established for COVID-19 treatment, and it is not currently marketed in Denmark. The TxGNN model's top-ranked prediction is **Multiple Endocrine Neoplasia** (score **99.50%**), but this candidate has **zero supporting clinical trials or publications**, and the evidence pack's own mechanistic review flags it as a likely false-positive with no biological plausibility.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | COVID-19 (per clinical trial records in this evidence pack, e.g. NCT04669990: "Remdesivir has recently received full approval for COVID-19 by US FDA"); not independently confirmed via Danish regulatory filings, as the drug is not marketed in Denmark |
| Predicted New Indication | Multiple Endocrine Neoplasia |
| TxGNN Prediction Score | 99.50% |
| Evidence Level | L5 |
| Denmark Market Status | Not Marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the structured `drug.original_moa` field (flagged as a Blocking/High-severity data gap in this pack). However, the evidence pack's own rationale text describes Remdesivir as a nucleotide analog prodrug that targets RNA-dependent RNA polymerase (RdRp), giving it activity against (+)ssRNA viruses such as SARS-CoV-2 and Ebola.

Multiple Endocrine Neoplasia (MEN) is a hereditary endocrine tumour syndrome driven by *RET* or *MEN1* gene mutations — a genetic oncogenic pathway with no known connection to viral RdRp inhibition. The evidence pack explicitly characterizes this pairing as a "typical TxGNN false-positive high-score candidate": the model score is high, but there is no supporting biological rationale, and querying ClinicalTrials.gov, ICTRP, and PubMed for this drug-disease pair returned zero results across all three sources.

It is also worth noting that the next-ranked candidate in this pack, "HIV infectious disease" (score 99.32%), superficially appears better supported — 23 registered trials and 20 publications. On review, however, every cited trial and abstract concerns COVID-19/SARS-CoV-2 (e.g. the WHO Solidarity Trial, ACTT-3, ACTIV-3/TICO), not HIV. Remdesivir's RdRp-targeting mechanism does not apply to HIV, a retrovirus that depends on reverse transcriptase. This strongly suggests a disease-ontology mapping error in the pipeline rather than genuine anti-HIV evidence, and should not be read as supporting this repurposing direction either.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Denmark Market Information

Not marketed in Denmark — no marketing authorisations are on file (`total_licenses = 0`).

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information. Key warnings, contraindications, and drug-drug interaction data were not available in this evidence pack (DG001, Blocking severity — data must be retrieved from the official product label before this candidate can enter any safety screening stage).

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication (Multiple Endocrine Neoplasia) has no supporting clinical trials or literature and no plausible mechanistic link to Remdesivir's antiviral mode of action. The apparently better-evidenced alternative (HIV infectious disease) is undermined by a likely disease-label mismatch — all associated trials and papers are COVID-19 studies, not HIV studies.

**To proceed, the following is needed:**
- Correct the disease-ontology mapping for the "HIV infectious disease" candidate (evidence appears to be COVID-19 data mislabeled)
- Resolve DG001 (Blocking): obtain TFDA/Danish SmPC warnings, contraindications, and DDI data before any S1 safety screening
- Resolve DG002 (High): obtain confirmed original MOA from the DrugBank API
- Verify Denmark/EU marketing status directly (EMA centralised authorisation for Veklury exists globally; this pack shows 0 licenses, which should be reconciled)
- De-duplicate the ranked candidate list — ranks 1–2, 3–4, 5–6, 7–8, and 9–10 are each identical repeated entries — before any re-scoring or prioritization
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

