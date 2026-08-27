---
layout: default
title: Tylosin
parent: 僅模型預測 (L5)
nav_order: 459
evidence_level: L5
indication_count: 10
---

# Tylosin
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

# Tylosin: From Veterinary Antibacterial Use to Jeune Syndrome with Situs Inversus

## One-Sentence Summary

Tylosin is a macrolide antibiotic used exclusively in veterinary medicine (not approved for human use) to treat bacterial respiratory and other infections in livestock. The TxGNN model predicts a possible association with **Jeune syndrome with situs inversus**, a rare ciliopathy-related genetic disorder, but this prediction is currently supported by **zero clinical trials and zero publications**, and the evidence pack itself states there is no known mechanistic link between the two. This candidate should be treated as an unvalidated model output only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Veterinary use only — bacterial infections (e.g., respiratory disease) in animals; not approved for human use |
| Predicted New Indication | Jeune syndrome with situs inversus |
| TxGNN Prediction Score | 97.67% |
| Evidence Level | L5 |
| Denmark Market Status | Not Marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data for Tylosin is not available (flagged as a High-severity data gap). What is known is that Tylosin is a macrolide antibiotic that inhibits bacterial 50S ribosomal protein synthesis and is used solely in veterinary practice — it has never been developed or approved for human therapeutic use.

Jeune syndrome with situs inversus is a rare inherited ciliopathy involving thoracic dysplasia and organ laterality defects. There is no known biological, pharmacological, or mechanistic pathway connecting an antibacterial ribosomal inhibitor to a structural/genetic ciliopathy. The evidence pack explicitly states this candidate has no supporting clinical trials, no supporting literature, and no established mechanistic rationale — the high TxGNN score (97.67%) reflects graph-topological proximity in the knowledge graph rather than any therapeutic signal.

For context, among the other candidates surfaced for this drug, "heart disease" (L4, S1) had associated literature — but that literature describes **cardiotoxicity of Tylosin-class macrolides (tilmicosin, tildipirosin) in animal models**, i.e., a safety signal, not efficacy evidence. This reinforces that none of the current predictions for Tylosin have credible mechanistic or clinical support.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Denmark Market Information

Tylosin holds no marketing authorisation in Denmark (0 registered products; market status: Not Marketed). As a veterinary-only antibacterial, it has no human-use product license on file.

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information. Note: no key warnings, contraindications, or drug-interaction data are currently on file for Tylosin, and no Danish SmPC exists since the product is not marketed in Denmark or approved for human use.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate has no clinical trials, no supporting literature, and no established mechanistic rationale connecting Tylosin to Jeune syndrome with situs inversus (evidence level L5, decision stage S0). Tylosin is also not marketed in Denmark and is not approved for human use, which independently precludes further development at this time.

**To proceed, the following is needed:**
- TFDA/SmPC warnings and contraindications for Tylosin (currently a Blocking data gap — required before any safety pre-assessment)
- Confirmed mechanism of action data (currently a High-severity data gap)
- Any preclinical or mechanistic rationale linking macrolide antibiotics to ciliopathy/laterality disorders
- Re-evaluation against alternative predicted indications with stronger evidence bases, while noting that the "heart disease" signal reflects cardiotoxicity risk rather than efficacy
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

