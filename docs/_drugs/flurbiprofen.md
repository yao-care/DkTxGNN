---
layout: default
title: Flurbiprofen
parent: 僅模型預測 (L5)
nav_order: 194
evidence_level: L5
indication_count: 10
---

# Flurbiprofen
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

# Flurbiprofen: From Pain and Inflammation to Acromesomelic Dysplasia, Hunter-Thompson Type

## One-Sentence Summary

Flurbiprofen is a non-steroidal anti-inflammatory drug (NSAID) of the propionic acid class, widely used for relief of pain, inflammation, and fever in musculoskeletal and arthritic conditions.
The TxGNN model predicts it may be effective for **acromesomelic dysplasia, Hunter-Thompson type**, with **0 clinical trials** and **0 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Pain and inflammation; musculoskeletal and arthritic conditions (no Denmark marketing authorisation on record) |
| Predicted New Indication | Acromesomelic dysplasia, Hunter-Thompson type |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known information, Flurbiprofen is a non-selective NSAID that inhibits cyclooxygenase enzymes (COX-1 and COX-2), reducing the synthesis of prostaglandins — particularly prostaglandin E2 (PGE2). This mechanism underlies its established clinical use in pain and inflammatory conditions, including rheumatoid arthritis, osteoarthritis, and in ophthalmic formulations for inhibition of intraoperative miosis during cataract surgery.

Acromesomelic dysplasia, Hunter-Thompson type is a rare skeletal dysplasia caused by mutations in the *CDMP1/GDF5* gene, which impairs the BMP (bone morphogenetic protein) signalling pathway and results in shortening of the distal and middle limb segments. COX inhibition by Flurbiprofen could theoretically reduce PGE2 levels, which may indirectly modulate BMP/TGF-β downstream inflammatory responses. However, the BMP signalling pathway is not a primary or established target of NSAIDs, and this connection is highly indirect and speculative.

Overall, the link between Flurbiprofen's anti-inflammatory mechanism and the genetic aetiology of acromesomelic dysplasia is extremely weak. The TxGNN prediction most likely reflects network-level topological proximity in the knowledge graph rather than a direct pharmacological relationship. No preclinical animal studies or clinical investigations have been conducted to support this hypothesis. The same assessment applies to all other predicted indications in this report (brachydactyly-syndactyly syndrome, colobomatous microphthalmia-rhizomelic dysplasia syndrome, brachyolmia-amelogenesis imperfecta syndrome, and myosclerosis), all of which are rare genetic disorders where the mechanistic link to COX inhibition is either indirect or absent.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for any of the predicted indications.

---

## Literature Evidence

Currently no related literature available for any of the predicted indications.

---

## Denmark Market Information

Flurbiprofen currently holds no marketing authorisations in Denmark. The drug is not marketed through the Danish Medicines Agency (Lægemiddelstyrelsen) or via the EMA centralised procedure applicable to Denmark. Any clinical use would require a compassionate use or named-patient basis application.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All five predicted indications are rare genetic skeletal dysplasia or connective tissue syndromes at the L5 evidence level — meaning the TxGNN prediction is unsupported by any registered clinical trial, preclinical study, or peer-reviewed publication. The mechanistic links between COX inhibition and these genetic disorders are highly speculative and do not meet the threshold for further development investment at this stage.

**To proceed, the following is needed:**
- Detailed mechanism of action data (MOA) retrieved from DrugBank API (DB00712)
- Safety profile and contraindications from the approved SmPC or Lægemiddelstyrelsen records (currently unavailable — classified as Blocking data gap)
- Preclinical (in vitro or animal model) evidence specifically investigating Flurbiprofen in BMP/TGF-β signalling or any of the predicted skeletal dysplasia pathways
- Clarification of whether Flurbiprofen is available for import or compassionate use in Denmark before any investigator-initiated study can be considered
- Re-evaluation of the TxGNN prediction model to understand why rare monogenic structural dysplasias cluster at the top of the ranking for an established NSAID — this may indicate a model calibration issue rather than a genuine repurposing signal
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

