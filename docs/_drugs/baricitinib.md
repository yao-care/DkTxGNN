---
layout: default
title: Baricitinib
parent: 僅模型預測 (L5)
nav_order: 55
evidence_level: L5
indication_count: 4
---

# Baricitinib
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Baricitinib: From Rheumatoid Arthritis to Colobomatous Microphthalmia-Rhizomelic Dysplasia Syndrome

---

## One-Sentence Summary

Baricitinib is a selective JAK1/JAK2 inhibitor primarily used to treat inflammatory and autoimmune conditions, including rheumatoid arthritis, atopic dermatitis, and alopecia areata.
The TxGNN model predicts it may be effective for **Colobomatous Microphthalmia-Rhizomelic Dysplasia Syndrome**, a rare congenital disorder affecting eye and limb development.
However, there are currently **0 clinical trials** and **0 publications** supporting this direction — the prediction rests entirely on computational modelling, and the mechanistic link is considered highly indirect.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not found in Danish Medicines Agency registration data (Baricitinib is internationally recognised as a JAK1/JAK2 inhibitor for rheumatoid arthritis and other inflammatory conditions) |
| Predicted New Indication | Colobomatous Microphthalmia-Rhizomelic Dysplasia Syndrome |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L5 |
| Denmark Market Status | Not marketed (per available registration data) |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

> **Data quality note:** The absence of Danish marketing authorisation data is likely a data gap rather than a true absence. Baricitinib (Olumiant®) holds a centralised EMA authorisation and is distributed across EU Member States including Denmark. This record should be verified against the Laegemiddelstyrelsen product database before drawing regulatory conclusions.

---

## Why is This Prediction Reasonable?

Baricitinib acts by selectively and reversibly inhibiting Janus kinases JAK1 and JAK2, thereby blocking phosphorylation of the downstream signal transducers STAT1, STAT3, and STAT5. This suppresses cytokine-driven inflammatory and immune signalling cascades — the mechanism underlying its approved use in conditions such as rheumatoid arthritis, atopic dermatitis, and alopecia areata.

Colobomatous microphthalmia-rhizomelic dysplasia syndrome is a rare congenital disorder caused by mutations affecting ocular development genes (PAX2, PAX6, STRA6) and peroxisome metabolic pathways associated with the rhizomelic chondrodysplasia punctata (RCDP) phenotype. The JAK-STAT pathway has no established role in the pathogenesis of this condition. The only theoretical point of contact is that STAT3 participates in retinal progenitor cell differentiation — an indirect and speculative connection that falls far short of a mechanistic rationale for therapeutic intervention.

Critically, this is a structural congenital malformation, not an inflammatory or immune-mediated disease. Baricitinib's anti-inflammatory mechanism offers no conceptual basis for reversing or ameliorating a fixed developmental defect. The high TxGNN score most likely reflects knowledge-graph topology (shared node connections) rather than true biological plausibility. This prediction should be treated as a hypothesis-generating signal only, not as clinical evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Denmark Market Information

No marketing authorisations were found in the current dataset for Denmark.

> As noted above, this is likely a data gap. Olumiant® (baricitinib 2 mg and 4 mg tablets, Eli Lilly) holds centralised EMA authorisation (EU/1/17/1201) for rheumatoid arthritis, atopic dermatitis, alopecia areata, and COVID-19. Danish healthcare professionals should consult the Laegemiddelstyrelsen medicinal product database (pro.medicin.dk / laegemiddelstyrelsen.dk) for current national availability and reimbursement status.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

> Safety data (key warnings, contraindications, and drug–drug interactions) were not available in the current Evidence Pack. For Baricitinib, clinicians should be aware that JAK inhibitors as a class carry important regulatory warnings, including risks of serious infections, venous thromboembolism, major adverse cardiovascular events (MACE), and malignancy. Full prescribing information is available via the EMA product page for Olumiant®.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model assigns a high score (99.94%) to baricitinib for colobomatous microphthalmia-rhizomelic dysplasia syndrome, but this indication is classified at Evidence Level L5 — computational prediction only, with zero supporting clinical trials or publications. More importantly, the proposed mechanistic link is speculative and conceptually weak: baricitinib targets inflammatory JAK-STAT signalling, whereas the predicted indication is a fixed structural congenital anomaly with no established immune or cytokine-driven pathology. Proceeding further is not justified at this stage.

**To proceed, the following is needed:**

- **Mechanistic validation:** Identify and document any peer-reviewed evidence linking JAK-STAT signalling to ocular or peroxisomal developmental pathways relevant to this syndrome
- **Literature re-query:** Perform a broader search using MeSH terms, OMIM, and rare disease databases (Orphanet) to confirm the complete absence of baricitinib or JAK-inhibitor research in this disease area
- **Denmark regulatory verification:** Confirm Olumiant® (baricitinib) status in the Laegemiddelstyrelsen database and EMA product register to correct the current data gap
- **Safety data retrieval:** Download and parse the EMA/Laegemiddelstyrelsen SmPC for baricitinib to complete the S1 safety screening
- **Expert consultation:** If future mechanistic evidence emerges, engage an ophthalmologist and rare disease specialist before advancing to S1 evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

