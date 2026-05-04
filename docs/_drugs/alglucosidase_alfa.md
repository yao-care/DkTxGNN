---
layout: default
title: Alglucosidase Alfa
parent: 僅模型預測 (L5)
nav_order: 23
evidence_level: L5
indication_count: 10
---

# Alglucosidase Alfa
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

# Alglucosidase alfa: From Pompe Disease to Adult Polyglucosan Body Disease

## One-Sentence Summary

Alglucosidase alfa (Myozyme/Lumizyme) is a recombinant human acid alpha-glucosidase enzyme replacement therapy, originally approved for treating Pompe disease (Glycogen Storage Disease Type II) — a rare lysosomal glycogen storage disorder causing progressive muscle and respiratory failure.
The TxGNN model predicts it may be effective for **Adult Polyglucosan Body Disease (APBD)**, a related but mechanistically distinct glycogen metabolism disorder.
Currently, **no clinical trials** and **no publications** specifically supporting this repurposing direction have been identified; this prediction is supported by model inference only.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Pompe disease (Glycogen Storage Disease Type II / acid alpha-glucosidase deficiency) |
| Predicted New Indication | Adult Polyglucosan Body Disease (APBD) |
| TxGNN Prediction Score | 99.47% |
| Evidence Level | L5 |
| Denmark Market Status | Not marketed in Denmark |
| Number of Marketing Authorisations | 0 (national Danish registry) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the current Evidence Pack. Based on published pharmacological literature, alglucosidase alfa is a recombinant form of human acid alpha-glucosidase (GAA) — the lysosomal enzyme responsible for breaking down glycogen within lysosomes. In Pompe disease, absent or severely reduced GAA activity causes glycogen to accumulate pathologically in muscle cells, leading to progressive myopathy, cardiomyopathy, and respiratory failure. Alglucosidase alfa corrects this by supplying the missing enzyme via intravenous infusion, reducing the lysosomal glycogen burden in affected tissues.

Adult Polyglucosan Body Disease is also a disorder of glycogen metabolism, arising from partial deficiency of glycogen branching enzyme (GBE1, encoded by the *GBE1* gene). When branching enzyme is impaired, structurally abnormal, poorly soluble glycogen chains — called "polyglucosan bodies" — accumulate in neurons, astrocytes, and muscle. Clinically, APBD presents in adulthood with progressive upper and lower motor neuron dysfunction, sensory neuropathy, neurogenic bladder, and in some cases cognitive decline. The biochemical overlap — both diseases involving pathological glycogen accumulation in tissues — is the most plausible reason TxGNN assigns a high-confidence score to this pairing.

However, the mechanistic rationale requires careful scrutiny: alglucosidase alfa addresses a deficiency in lysosomal glycogen *degradation* (GAA), whereas APBD is caused by defective glycogen *branching* (GBE1). Whether augmenting lysosomal glycogenolysis can compensate for the upstream structural defect in glycogen synthesis remains entirely unproven. This distinction means the biological plausibility, while present at a high level (shared glycogen metabolism pathway), does not translate directly to a clear therapeutic mechanism. Preclinical exploration in GBE1-deficient animal models would be the necessary next step before any clinical hypothesis can be formed.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Denmark Market Information

Alglucosidase alfa does not hold a national marketing authorisation registered with the Danish Medicines Agency (Lægemiddelstyrelsen). No Danish national licences were identified.

> **Important note for Danish prescribers**: Alglucosidase alfa is centrally authorised across the European Union by the European Medicines Agency (EMA) under the brand name **Myozyme** (authorisation number EU/1/06/333) for the long-term enzyme replacement therapy of patients with confirmed Pompe disease. As a centrally authorised product, it is legally available in Denmark without requiring a separate national marketing authorisation. A second formulation, **Nexviazyme** (avalglucosidase alfa), received EMA approval in 2022 as a higher-efficacy successor product. Healthcare professionals should consult the current EMA-approved Summary of Product Characteristics (SmPC) for the most up-to-date prescribing information.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No clinical trials or published literature supporting the use of alglucosidase alfa in adult polyglucosan body disease have been identified; the prediction rests solely on TxGNN model inference (Evidence Level L5), and the mechanistic link — while biologically plausible at the level of glycogen metabolism — does not translate directly to a clear therapeutic rationale given the distinct enzymatic deficiencies involved in Pompe disease versus APBD.

**To proceed, the following is needed:**
- **Mechanistic clarification**: Retrieve full MOA data from DrugBank (DB01272) and published literature to determine whether acid alpha-glucosidase supplementation could plausibly benefit a GBE1-deficient substrate
- **Preclinical evidence**: Conduct or identify studies in GBE1-deficient animal models evaluating alglucosidase alfa, or any acid alpha-glucosidase, for APBD-relevant endpoints
- **Safety data gap remediation**: The full SmPC warning/contraindication profile and drug–drug interaction data must be obtained before clinical feasibility can be assessed (currently Blocking data gap per Evidence Pack)
- **Expanded literature search**: Broaden the PubMed and ICTRP search strategy to include related glycogen storage disease terms (e.g., GBE1, polyglucosan, Type IV glycogen storage disease) — the current query returned zero results, which may reflect overly narrow search parameters rather than a true absence of relevant literature
- **Regulatory pathway consultation**: Engage the Danish Medicines Agency (Lægemiddelstyrelsen) and EMA regarding the feasibility of an orphan drug label extension for APBD, noting that APBD is an ultra-rare disease with very limited treatment options
- **Unmet need assessment**: Estimate the Danish patient population with APBD through rare disease registries (e.g., ORPHANET, Danish National Patient Registry) to inform whether a development programme would be viable

---

*⚠️ This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any therapeutic application. Data cutoff: 2026-04-04.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

