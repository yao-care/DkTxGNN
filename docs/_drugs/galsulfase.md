---
layout: default
title: Galsulfase
parent: 僅模型預測 (L5)
nav_order: 203
evidence_level: L5
indication_count: 10
---

# Galsulfase
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

# Galsulfase: From Mucopolysaccharidosis Type VI to Ptosis-Strabismus-Ectopic Pupils Syndrome

## One-Sentence Summary

Galsulfase (Naglazyme) is a recombinant enzyme replacement therapy (ERT) approved for Mucopolysaccharidosis Type VI (MPS VI / Maroteaux-Lamy syndrome), where it restores the deficient N-acetylgalactosamine 4-sulfatase enzyme and reduces pathological glycosaminoglycan (GAG) accumulation throughout the body. The TxGNN model predicts it may be effective for **ptosis-strabismus-ectopic pupils syndrome**, with a prediction score of **97.89%**; however, **no supporting clinical trials or publications** exist for this indication. Importantly, the mechanistic analysis included in this Evidence Pack identifies the high score as a knowledge graph topology artefact rather than a genuine biological signal.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Mucopolysaccharidosis Type VI (MPS VI / Maroteaux-Lamy syndrome) |
| Predicted New Indication | Ptosis-Strabismus-Ectopic Pupils Syndrome |
| TxGNN Prediction Score | 97.89% |
| Evidence Level | L5 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Galsulfase is a recombinant form of N-acetylgalactosamine 4-sulfatase (arylsulfatase B), the lysosomal enzyme deficient in MPS VI. When administered intravenously, it is taken up by cells via mannose-6-phosphate receptors and traffics to lysosomes, where it degrades accumulated dermatan sulfate. Patients with MPS VI do develop secondary ocular manifestations — most notably corneal clouding — as a consequence of GAG deposition in corneal stroma. This establishes a documented, albeit indirect, association between Galsulfase and ocular pathology, which likely explains the drug's connectivity to eye-related phenotype nodes in the TxGNN knowledge graph.

However, **ptosis-strabismus-ectopic pupils syndrome** is a congenital neurodevelopmental disorder characterised by structural anatomical abnormalities of the eye and pupil arising during embryogenesis. It is not caused by lysosomal enzyme deficiency or GAG over-accumulation. Enzyme replacement therapy has no established mechanism by which it could reverse or modify congenital structural defects of the anterior segment, extraocular muscles, or autonomic neural pathways.

The mechanistic rationale included in this Evidence Pack explicitly characterises this as a **knowledge graph topology false positive**: the high TxGNN score (97.89%) most plausibly results from "ptosis" being a high-connectivity shared phenotype node in the knowledge graph, generating systematically elevated scores for all ptosis-associated conditions regardless of their biological relationship to GAG metabolism. Notably, all five unique predictions in the top-10 list share the same pattern — rare congenital ptosis-related syndromes — which strongly supports a systematic model bias rather than any genuine repurposing opportunity.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Denmark Market Information

Galsulfase is not currently registered or actively marketed in Denmark, and no national or centralised marketing authorisations are on record for this jurisdiction in the Evidence Pack.

> **Note for prescribers:** Naglazyme (galsulfase) holds a centralised EMA marketing authorisation (EU/1/05/302) valid across all EU/EEA member states. Danish patients with confirmed MPS VI may be eligible for access through named-patient programmes or hospital exemption pathways. Please consult the Danish Medicines Agency (Laegemiddelstyrelsen) for current availability and reimbursement status.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Every top-ranked TxGNN prediction for Galsulfase involves a rare congenital ptosis-related syndrome with no mechanistic connection to GAG metabolism, no supporting clinical trials, and no published literature. The Evidence Pack's own mechanistic analysis identifies these high scores as a systematic knowledge graph topology artefact driven by the high node-connectivity of "ptosis" phenotypes — not a biological signal. Proceeding with any of these indications is not scientifically justified at this stage.

**To proceed, the following is needed:**

- **MOA data retrieval**: Obtain full mechanistic and pharmacological profile from DrugBank (DB01279) and current EMA/FDA product labelling to populate the data gaps flagged in this report
- **Knowledge graph audit**: Commission a formal review of phenotype-driven prediction bias in the TxGNN model for lysosomal storage disease ERT agents, to identify and correct topology artefacts before re-ranking candidates
- **Biologically plausible re-query**: Investigate whether MPS VI–related ocular manifestations (corneal clouding, glaucoma, papilloedema) or systemic GAG-deposition conditions could yield more mechanistically credible repurposing candidates through targeted evidence searches
- **Named-patient access clarification**: Confirm current availability of Naglazyme in Denmark via Laegemiddelstyrelsen for MPS VI patients, independent of the repurposing evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

