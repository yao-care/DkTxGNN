---
layout: default
title: Parecoxib
parent: 僅模型預測 (L5)
nav_order: 332
evidence_level: L5
indication_count: 10
---

# Parecoxib
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

# Parecoxib: From Postoperative Pain to Migraine Disorder

*(Note: the Evidence Pack does not record an original indication for Parecoxib — `original_indications` is empty. "Postoperative pain" reflects Parecoxib's publicly known approved use as an injectable COX-2 inhibitor prodrug of valdecoxib; it is not sourced from this Evidence Pack and should be verified against the official SmPC.)*

## One-Sentence Summary

Parecoxib is a parenteral, selective COX-2 inhibitor (prodrug of valdecoxib); its original approved indication is not captured in this Evidence Pack, and it currently holds **0 marketing authorisations** in Denmark ("Not Marketed"). The TxGNN model predicts it may be effective for **Migraine Disorder** with a prediction score of **99.55%**, but this top-ranked candidate has **no directly linked clinical trials or literature** of its own — supporting evidence is indirect, drawn from a closely related "Headache Disorder" cluster (same TxGNN score family, one pilot RCT).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in Evidence Pack (general knowledge: short-term treatment of postoperative pain) |
| Predicted New Indication | Migraine Disorder |
| TxGNN Prediction Score | 99.55% |
| Evidence Level | L3 (per pack scoring; based on indirect evidence, not direct trials/literature for this entity) |
| Denmark Market Status | Not Marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for Parecoxib is not available in this Evidence Pack (blocking/high-severity data gap: DG002). Based on general pharmacological knowledge, Parecoxib is a selective COX-2 inhibitor administered parenterally and rapidly hydrolysed in vivo to its active metabolite, valdecoxib. COX-2 inhibition reduces prostaglandin E2 (PGE2) production, which is the mechanism underlying its established analgesic use.

Migraine pathophysiology involves neurogenic inflammation and meningeal vasodilation, processes partly mediated by the COX-2/PGE2 pathway. Theoretically, COX-2 inhibition could reduce PGE2-induced vasodilation and pain sensitization, complementing triptans (which act on 5-HT1B/1D receptors to cause vasoconstriction). This rationale is documented in the repurposing evidence for the closely related "Headache Disorder" candidate (same disease-entity family, TxGNN score 0.9955), where a pilot RCT (PMID 21996647) directly compared parecoxib to sumatriptan and rizatriptan in acute migraine attacks.

Importantly, this specific "Migraine Disorder" entry has **zero directly linked clinical trials or literature** — the mechanistic case rests on indirect linkage to the neighboring "Headache Disorder" cluster, not on evidence generated for migraine itself.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

*Indirect note: the related "Headache Disorder" candidate lists 3 trials (NCT01930318, NCT03823846, NCT06623513), all graded "C" relevance — none target migraine/headache directly; they involve postoperative or periprocedural pain settings.*

---

## Literature Evidence

Currently no related literature available.

*Indirect note: PMID [21996647](https://pubmed.ncbi.nlm.nih.gov/21996647/) (2011, RCT, Clinical Neuropharmacology, Tier 1) — a pilot study comparing IV parecoxib 40mg, SC sumatriptan, and oral rizatriptan for acute migraine attacks — is linked to the "Headache Disorder" candidate, not directly to this "Migraine Disorder" entry.*

---

## Denmark Market Information

Not marketed in Denmark; 0 marketing authorisations currently registered in this Evidence Pack.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

*(Key warnings, contraindications, and drug interaction data are all flagged as data gaps in this Evidence Pack — DG001 is a Blocking-severity gap: TFDA/label warnings and contraindications are unresolved, which prevents a S1 safety pre-assessment.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top-ranked candidate (Migraine Disorder) has no direct clinical trial or literature support of its own; the mechanistic case relies on indirect linkage to a neighboring disease cluster and a single small pilot RCT.
- Parecoxib is not currently marketed in Denmark (0 authorisations), and a Blocking data gap (label warnings/contraindications, DG001) prevents even an initial safety screen.

**To proceed, the following is needed:**
- Danish/EU SmPC or approved label — warnings and contraindications (resolves DG001, Blocking)
- Confirmed mechanism-of-action documentation and original approved indication (resolves DG002)
- Direct clinical trials or literature evaluating Parecoxib specifically in migraine (not only the adjacent headache-disorder cluster)
- Assessment of route/dosage-form compatibility for acute migraine treatment (Parecoxib's known formulation is parenteral; suitability for outpatient/self-administered migraine care needs review)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

