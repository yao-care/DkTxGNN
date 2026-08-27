---
layout: default
title: Sebelipase Alfa
parent: 僅模型預測 (L5)
nav_order: 393
evidence_level: L5
indication_count: 10
---

# Sebelipase Alfa
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

Using the report-drafting instructions in the prompt directly (no codebase skill applies to this documentation task).

Note on the data before the report: `predicted_indications[0]` (Scheie syndrome) is required by the template for the headline, but its own `repurposing_rationale` states there is no mechanistic overlap and zero supporting evidence — it reads as KG noise. Separately, entries ranked 7–10 (cholesteryl ester storage disease, Wolman disease) are **not** new indications — they are Sebelipase alfa's existing approved uses (LAL-D) surfacing in the "predicted" list. I've kept the report honest about this rather than dressing up rank 1 as a strong signal.

---

# Sebelipase alfa: From Lysosomal Acid Lipase Deficiency to Scheie Syndrome

## One-Sentence Summary

Sebelipase alfa is a recombinant human lysosomal acid lipase (LAL) enzyme-replacement therapy; its established use is lysosomal acid lipase deficiency (LAL-D, including Wolman disease and cholesteryl ester storage disease), based on literature within this evidence pack, though the drug's official original-indication and MOA fields are not yet populated. The TxGNN model's top-ranked new-indication candidate is **Scheie syndrome**, but this candidate is supported by **0 clinical trials** and **0 publications**, and the model's own mechanistic rationale states there is **no known mechanism overlap** between sebelipase alfa's target enzyme (LAL) and Scheie syndrome's underlying deficiency (IDUA). This should be treated as a low-confidence signal, not a validated repurposing lead.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Lysosomal Acid Lipase Deficiency (LAL-D) — inferred from supporting literature in this pack; official label text unavailable (see Data Gaps) |
| Predicted New Indication | Scheie syndrome |
| TxGNN Prediction Score | 99.80% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (Data Gap, severity: High). Based on known information from the evidence pack's supporting literature, sebelipase alfa is a recombinant human lysosomal acid lipase (LAL) used as long-term enzyme replacement therapy; its efficacy in LAL-D (including the infantile-onset Wolman disease phenotype and the later-onset cholesteryl ester storage disease phenotype) is well documented in this pack's own trial and literature evidence.

Scheie syndrome, however, is a mild phenotype of mucopolysaccharidosis type I (MPS I), caused by deficiency of α-L-iduronidase (IDUA) — a different enzyme, acting on a different substrate (glycosaminoglycans) via a different metabolic pathway than LAL (which hydrolyzes cholesteryl esters and triglycerides). The evidence pack's own repurposing rationale explicitly states there is **no mechanistic overlap** between the two targets, and that the high TxGNN score most likely reflects clustering of "lysosomal storage disease" nodes within the knowledge graph rather than a genuine pharmacological signal.

No clinical trials or literature specific to sebelipase alfa in Scheie syndrome were found in any of the queried sources (ClinicalTrials.gov, ICTRP, PubMed — all returned 0 results). On the current evidence, this prediction should be treated as an unvalidated model artifact rather than a plausible repurposing hypothesis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Denmark Market Information

Sebelipase alfa is not currently marketed in Denmark; no Laegemiddelstyrelsen or EMA centralised marketing authorisation is recorded in this evidence pack (0 licenses on file).

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top-ranked candidate (Scheie syndrome) has no clinical trial or literature support, and the mechanistic rationale itself concludes there is no known biological link between sebelipase alfa's enzymatic target (LAL) and Scheie syndrome's underlying deficiency (IDUA) — this is an L5, model-only signal with a "Hold" recommendation.
- Separately, this evidence pack's ranked list also surfaces cholesteryl ester storage disease and Wolman disease (ranks 7–10, evidence level L1) — these are **not** new indications but sebelipase alfa's existing approved uses (LAL-D) re-emerging from the knowledge graph; they should not be counted as repurposing evidence for this report's target indication.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): Danish/EU SmPC warnings and contraindications, required before any safety pre-assessment
- Resolve DG002 (High): confirmed mechanism-of-action data from DrugBank or the approved label
- A biologically grounded rationale (or independent literature) connecting LAL enzyme replacement to MPS I / Scheie syndrome pathology before any further evaluation stage is warranted
- If interest continues in LAL-D-adjacent indications already covered by sebelipase alfa's approved use, re-scope this evaluation around Denmark market-entry status for LAL-D rather than "new indication" repurposing
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

