---
layout: default
title: Febuxostat
parent: 僅模型預測 (L5)
nav_order: 187
evidence_level: L5
indication_count: 6
---

# Febuxostat
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Febuxostat: From Hyperuricaemia to Renal Hypouricaemia

## One-Sentence Summary

Febuxostat is a selective xanthine oxidoreductase (XOR) inhibitor widely used to reduce serum uric acid in adults with gout and chronic hyperuricaemia.
The TxGNN model predicts it may also be effective for **Renal Hypouricaemia (Hypouricemia, Renal)**,
with **1 clinical trial** and **2 publications** currently providing supporting evidence for this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hyperuricaemia / Gout (based on established pharmacology; no Danish MA on file) |
| Predicted New Indication | Hypouricemia, Renal |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L4 |
| Denmark Market Status | Not Marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on established pharmacological knowledge, febuxostat is a non-purine selective inhibitor of xanthine oxidoreductase (XOR) — the enzyme that catalyses the conversion of hypoxanthine → xanthine → uric acid. By blocking this final step in purine catabolism, febuxostat substantially lowers serum urate concentrations.

Renal hypouricaemia (RHUC) is a rare inherited disorder in which defects in renal tubular urate transporters (most commonly URAT1, encoded by *SLC22A12*) lead to abnormally low serum uric acid. At first glance, repurposing a urate-lowering agent for a condition characterised by *low* urate seems paradoxical. However, the clinical rationale lies in a specific and dangerous complication: **exercise-induced acute kidney injury (EIAKI)**. During intense anaerobic exercise, the rapid catabolism of purines generates a surge in xanthine and uric acid. In patients with RHUC, the kidneys cannot reabsorb urate normally, resulting in extremely high urinary xanthine/urate concentrations, oxidative stress, and acute tubular injury.

The proposed repurposing hypothesis — supported by a published case report (PMID 36754409) — is therefore to use febuxostat **prophylactically** to blunt the peri-exercise surge in xanthine/urate production, thereby preventing EIAKI, rather than to treat the low baseline serum urate itself. This mechanistic link is pharmacologically coherent and explains the high TxGNN prediction score.

> **Additional predictions of note:** TxGNN also ranked **HPRT partial deficiency** (99.98%) and **Lesch-Nyhan syndrome** (99.68%) as plausible indications. Both conditions are characterised by XOR pathway dysregulation leading to severe hyperuricaemia, where febuxostat's urate-lowering effect would be directly applicable. These indications are pharmacologically less surprising and are discussed further in the Conclusion.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT04398251](https://clinicaltrials.gov/study/NCT04398251) | Phase 4 | Unknown | 100 | Prospective controlled study exploring the effect of uric acid control on kidney stone recurrence and renal function in patients with hyperuricaemia-related calculi. Indirectly relevant — addresses urate management in renal disease but does not specifically enrol RHUC patients or evaluate EIAKI prevention. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [36754409](https://pubmed.ncbi.nlm.nih.gov/36754409/) | 2023 | Case Report | Internal Medicine (Tokyo) | 16-year-old football player with familial RHUC (compound heterozygous *URAT1* mutations) and recurrent EIAKI refractory to hydration. Febuxostat was trialled as prophylaxis to reduce exercise-triggered xanthine/urate flux; supports XOR inhibition as a mechanistically plausible preventive strategy for EIAKI in RHUC. |
| [31650389](https://pubmed.ncbi.nlm.nih.gov/31650389/) | 2020 | Review | Clinical Rheumatology | Narrative review of hypouricaemia for practising rheumatologists, covering definition (serum urate < 2 mg/dL), aetiology (renal vs. non-renal subtypes), complications including EIAKI, and management principles. Provides clinical context for the RHUC population. |

---

## Denmark Market Information

Febuxostat has no active marketing authorisations registered with the Danish Medicines Agency (Lægemiddelstyrelsen) and is recorded as **not marketed** in Denmark.

> **Prescriber note:** Febuxostat is authorised across the European Union as **Adenuric®** (EMA centralised authorisation EU/1/08/447, Menarini) for the management of hyperuricaemia in adults with gout, including those with renal impairment. Danish prescribers should verify current national availability, reimbursement status, and any risk-management conditions via [Lægemiddelstyrelsen](https://www.laegemiddelstyrelsen.dk) and [medicinpriser.dk](https://medicinpriser.dk) before clinical use.

---

## Safety Considerations

No safety data (key warnings, contraindications, or drug interactions) is available in this Evidence Pack.

Please refer to the approved Summary of Product Characteristics (SmPC) for Adenuric® (available via the [EMA product page](https://www.ema.europa.eu/en/medicines/human/EPAR/adenuric)) for full safety information, including the cardiovascular risk signal identified in post-marketing studies.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence base for febuxostat in renal hypouricaemia currently consists of a single case report and one Phase 4 trial with unknown completion status that does not directly address the RHUC/EIAKI indication. The drug carries no Danish marketing authorisation, and safety data is absent from this Evidence Pack. The mechanistic rationale is plausible but requires prospective validation before clinical adoption can be recommended.

**To proceed, the following is needed:**

- **Safety data retrieval:** Obtain the Adenuric® SmPC (EMA) for mechanism of action, contraindications, key warnings (notably the cardiovascular risk signal), and drug interactions
- **Danish availability check:** Confirm import/named-patient access pathways via Lægemiddelstyrelsen, given the absence of a local MA
- **Dedicated RHUC/EIAKI study:** Commission or identify a prospective case series or controlled study in RHUC patients using febuxostat as EIAKI prophylaxis — the current single case report is insufficient for clinical guidance
- **Paediatric data:** RHUC with EIAKI frequently presents in young athletes; paediatric safety and dosing data for febuxostat should be reviewed separately
- **Evaluate HPRT/Lesch-Nyhan indications independently:** Given the higher evidence base for febuxostat in XOR-overactive conditions (HPRT partial deficiency, Lesch-Nyhan syndrome), separate Evidence Packs targeting these indications may yield a more actionable near-term recommendation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

