---
layout: default
title: Enfortumab Vedotin
parent: 僅模型預測 (L5)
nav_order: 164
evidence_level: L5
indication_count: 10
---

# Enfortumab Vedotin
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

# Enfortumab Vedotin: From Urothelial Carcinoma to Leprosy

## One-Sentence Summary

Enfortumab vedotin (brand name Padcev) is a Nectin-4-directed antibody-drug conjugate (ADC) approved internationally for the treatment of locally advanced or metastatic urothelial carcinoma.
The TxGNN model predicts it may be effective for **Leprosy** with a score of 99.53%, however **no clinical trials** and **no published literature** currently support this direction.
The mechanistic rationale for this prediction is considered extremely weak; the high prediction score most likely reflects non-specific topological associations within the knowledge graph rather than genuine pharmacological relevance.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Locally advanced or metastatic urothelial carcinoma |
| Predicted New Indication | Leprosy |
| TxGNN Prediction Score | 99.53% |
| Evidence Level | L5 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on established pharmacological knowledge, Enfortumab vedotin (EV) is a Nectin-4-directed antibody-drug conjugate. Its antibody component selectively binds Nectin-4 — a cell adhesion molecule overexpressed on urothelial carcinoma cells — triggering receptor-mediated internalisation and intracellular release of its cytotoxic payload, monomethyl auristatin E (MMAE). MMAE disrupts microtubule polymerisation, leading to cell cycle arrest and apoptosis in tumour cells.

Leprosy is a chronic infectious disease caused by *Mycobacterium leprae*, an obligate intracellular bacterium predominantly affecting the skin, peripheral nerves, and mucous membranes. The underlying pathology is fundamentally different from urothelial carcinoma: there is no malignant cellular proliferation, and no known biological connection exists between Nectin-4 expression and *M. leprae* pathogenesis. MMAE has no established antibacterial mechanism, and fungal or bacterial cells do not express human Nectin-4, making targeted ADC delivery to the site of infection impossible.

The high TxGNN prediction score is most likely attributable to non-specific topological overlap in the knowledge graph — particularly shared neural and skin tissue nodes between urothelial cancer biology and leprosy neuropathology — rather than any pharmacologically relevant relationship. This prediction should be interpreted with significant caution and is not considered actionable without substantial preclinical justification.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Enfortumab vedotin in leprosy.

---

## Literature Evidence

Currently no related literature available for Enfortumab vedotin in leprosy.

---

## Denmark Market Information

Enfortumab vedotin is not registered with the Danish Medicines Agency (Laegemiddelstyrelsen), and no national or centralised marketing authorisations are recorded in this Evidence Pack.

> **⚠ Data Gap Notice**: Padcev (enfortumab vedotin) received EMA centralised approval in 2023 for urothelial carcinoma. The absence of records in this Evidence Pack may reflect a gap in the Laegemiddelstyrelsen-specific query rather than a true absence of European authorisation. Clinicians should independently verify current EMA authorisation status via the [EMA Product Database](https://www.ema.europa.eu/en/medicines) and the [Laegemiddelstyrelsen medicin.dk database](https://www.medicin.dk).

---

## Cytotoxicity

Enfortumab vedotin is an antineoplastic antibody-drug conjugate; the following cytotoxicity information applies.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — Antibody-Drug Conjugate (ADC); Nectin-4-directed monoclonal antibody linked to MMAE (microtubule-disrupting cytotoxin) |
| Myelosuppression Risk | High — neutropenia, including febrile neutropenia, is a well-documented class effect of MMAE-containing ADCs; anaemia and thrombocytopenia also reported |
| Emetogenicity Classification | Low to moderate |
| Monitoring Items | Full blood count with differential (CBC/diff), liver function tests (ALT/AST/bilirubin), renal function (creatinine/eGFR), fasting blood glucose (hyperglycaemia risk with EV), peripheral neuropathy assessment (MMAE-associated neuropathy is dose-limiting) |
| Handling Protection | Must be handled in accordance with cytotoxic drug handling regulations; additional biosafety precautions for antibody-based biologics apply (cold chain, spill management per institutional SOPs) |

---

## Safety Considerations

Safety data (warnings, contraindications, and drug interactions) are not available in this Evidence Pack for Enfortumab vedotin.

Please refer to the approved Summary of Product Characteristics (SmPC) for complete safety information, including known risks of peripheral neuropathy, severe skin reactions (including Stevens-Johnson syndrome), hyperglycaemia, pneumonitis, and ocular toxicity associated with EV.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction of Enfortumab vedotin for leprosy reaches Evidence Level L5 — model prediction only, with no supporting clinical trials or literature. The mechanistic link is biologically implausible: EV is a Nectin-4-directed ADC with no known antibacterial activity, and *Mycobacterium leprae* does not express human Nectin-4. Proceeding with any clinical exploration of this indication cannot be justified on current evidence.

**To proceed, the following would be needed:**

- **Preclinical biomarker data**: Evidence that Nectin-4 is aberrantly expressed in *M. leprae*-infected neural or skin tissues
- **Mechanistic justification**: A plausible hypothesis linking Nectin-4 or MMAE to mycobacterial pathogenesis or host immune dysregulation in leprosy
- **In vitro / in vivo activity data**: Minimum requirement before any clinical translation is considered
- **Complete SmPC data**: Full safety profile for Enfortumab vedotin (currently a blocking data gap per DG001)
- **EMA authorisation verification**: Confirm current European marketing authorisation status and Danish availability via Laegemiddelstyrelsen / medicin.dk
- **Alternative indication review**: Given the L5 Hold across all top-10 predictions, a broader review of EV's known Nectin-4-expressing tumour types (e.g., breast, cervical, head and neck cancers) may yield more clinically plausible repurposing candidates than those surfaced in this Evidence Pack

---

*This report is generated for research reference purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before therapeutic application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

