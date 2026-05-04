---
layout: default
title: Naldemedine
parent: 僅模型預測 (L5)
nav_order: 247
evidence_level: L5
indication_count: 0
---

# Naldemedine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **0** 個
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

# Naldemedine: Opioid-Induced Constipation — No TxGNN Predictions Available

## One-Sentence Summary

Naldemedine (DB11691) is a peripherally acting µ-opioid receptor antagonist (PAMORA) approved internationally for the treatment of opioid-induced constipation (OIC) in adults with chronic non-cancer pain.
The current Evidence Pack contains **no TxGNN-predicted new indications**, as the prediction pipeline did not return candidate diseases for this drug.
With zero marketing authorisations in Denmark and critical data gaps in safety, mechanism of action, and prediction output, no repurposing evaluation can be completed at this stage.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Opioid-induced constipation (OIC) — chronic non-cancer pain (based on international approvals; not recorded in Evidence Pack) |
| Predicted New Indication | — (No predictions returned) |
| TxGNN Prediction Score | — |
| Evidence Level | L5 (Model prediction only — no output generated) |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

No TxGNN predictions were returned for Naldemedine in this Evidence Pack (`predicted_indications: []`). A repurposing rationale therefore cannot be constructed from model output.

For reference: Naldemedine is a derivative of naltrexone engineered to act peripherally by restricting CNS penetration. It antagonises µ-, δ-, and κ-opioid receptors in the gastrointestinal tract, reversing opioid-induced reduction of GI motility without diminishing central analgesic effect. This highly targeted peripheral mechanism is narrow in scope, which may partly explain why the TxGNN graph traversal did not identify strong cross-disease candidates.

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on known pharmacology, Naldemedine belongs to the PAMORA class; its efficacy in opioid-induced constipation has been established in pivotal Phase 3 trials, and mechanistically it may be applicable to broader disorders of gut motility — but this hypothesis is not supported by the current prediction run and would require a new pipeline execution with complete input data.

---

## Clinical Trial Evidence

No predicted indication is available; condition-specific trial evidence cannot be scoped.

For completeness, Naldemedine's pivotal OIC trials (the drug's established indication) include:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT01965158](https://clinicaltrials.gov/study/NCT01965158) | Phase 3 | Completed | 547 | COMPOSE-1: Naldemedine 0.2 mg vs placebo in OIC; met primary endpoint of responder rate |
| [NCT01993940](https://clinicaltrials.gov/study/NCT01993940) | Phase 3 | Completed | 553 | COMPOSE-2: Confirmatory trial; significant improvement in spontaneous bowel movement frequency |
| [NCT02117388](https://clinicaltrials.gov/study/NCT02117388) | Phase 3 | Completed | 1,246 | COMPOSE-3: 52-week safety and efficacy; sustained response maintained over long-term use |

> These trials relate to the **approved** indication only, not to any repurposing target.

---

## Literature Evidence

No repurposing target indication is available; disease-specific literature cannot be scoped.

---

## Denmark Market Information

Naldemedine is **not authorised for marketing in Denmark** according to this Evidence Pack. No national (Lægemiddelstyrelsen) or centralised (EMA) marketing authorisations are on record.

> **Note for investigators:** Naldemedine (Symproic®) holds EMA centralised marketing authorisation (granted 2019) and FDA approval (2017) for OIC. The absence from the Danish market may reflect commercial, not regulatory, reasons. Verification against the current Lægemiddelstyrelsen product database is recommended before drawing conclusions.

---

## Safety Considerations

No safety data is available in this Evidence Pack (key warnings, contraindications, and drug interaction records are all absent). The two critical data gaps flagged by the pipeline are:

- **DG001 (Blocking):** TFDA SmPC warnings and contraindications not retrieved — prevents S1 safety screening.
- **DG002 (High):** Mechanism of action data not retrieved from DrugBank — prevents mechanistic relevance analysis.

> Please refer to the approved Summary of Product Characteristics (SmPC) — available via the EMA product page for Symproic® — for all safety information, including QT-interval effects, opioid withdrawal symptoms, and drug interactions (particularly with strong CYP3A4 inducers/inhibitors, which may alter naldemedine plasma levels).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Evidence Pack is critically incomplete — no TxGNN predictions were generated, no safety data was retrieved, and no MOA information is available. A meaningful repurposing evaluation cannot be produced from the current dataset.

**To proceed, the following is needed:**

- [ ] **Re-run the TxGNN prediction pipeline** with a complete input set to generate repurposing candidates (`predicted_indications`)
- [ ] **Retrieve MOA data from DrugBank** (DB11691) to enable mechanistic plausibility analysis (remediation for DG002)
- [ ] **Download and parse the SmPC / prescribing information** (EMA Symproic® EPAR or TFDA product monograph) to populate safety warnings, contraindications, and drug interactions (remediation for DG001)
- [ ] **Confirm Denmark/EMA marketing status** directly from the Lægemiddelstyrelsen product register, as the EMA-authorised Symproic® may already be accessible via the centralised procedure
- [ ] Once predictions are available, re-issue this report under the standard v5 format with full evidence tables

---

> ⚠️ *This report is generated for research purposes only and does not constitute medical advice. Any drug repurposing candidate requires clinical validation before therapeutic application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

