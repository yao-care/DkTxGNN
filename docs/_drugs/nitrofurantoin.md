---
layout: default
title: Nitrofurantoin
parent: 僅模型預測 (L5)
nav_order: 311
evidence_level: L5
indication_count: 10
---

# Nitrofurantoin
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

# Nitrofurantoin: From Urinary Tract Infection to Rheumatoid Arthritis

## One-Sentence Summary

Nitrofurantoin is a nitrofuran-class antibacterial, established as a first-line oral treatment for uncomplicated urinary tract infection (UTI); this specific indication text is not present in the current Evidence Pack, so it is stated here from established pharmacological knowledge rather than sourced data. The TxGNN model predicts it may be effective for **Rheumatoid Arthritis**, but the current evidence base consists of **0 clinical trials** and **11 literature items**, nearly all of which describe drug-induced toxicity (pulmonary fibrosis, hepatitis) in RA patients rather than therapeutic efficacy — this is a model-score-only prediction with a possible safety signal, not an efficacy finding.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Urinary tract infection (UTI) — not recorded in Evidence Pack; based on established pharmacology |
| Predicted New Indication | Rheumatoid Arthritis |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L5 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available (Data Gap DG002). Based on established pharmacology, nitrofurantoin is reduced by bacterial flavoproteins into reactive intermediates that damage bacterial DNA, ribosomal proteins, and other macromolecules — a nonspecific antibacterial mechanism with no established immunomodulatory or anti-rheumatic activity.

Urinary tract infection and rheumatoid arthritis belong to unrelated disease categories (infectious vs. autoimmune/rheumatologic), unlike typical repurposing pairs that share organ system or pathway overlap. No mechanistic or pharmacological rationale connecting the two indications is present in this Evidence Pack.

The 11 literature items returned for this pairing do **not** support a therapeutic rationale. They are almost entirely case reports and reviews describing nitrofurantoin-induced pulmonary and hepatic toxicity occurring *in* RA patients (e.g., a fatal interaction with methotrexate), plus one observational study on antibiotics and RA flares that is not specific to nitrofurantoin. In other words, the literature clusters around nitrofurantoin as a **risk factor** in RA patients, not as a **treatment** for RA. This should be read as a high TxGNN similarity score without corroborating biological or clinical support — comparable to the model's other low-confidence, no-evidence predictions in this same output (e.g., the L5/Hold calls for the two syndromic diagnoses at ranks 3–4 and 9–10).

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31222078](https://pubmed.ncbi.nlm.nih.gov/31222078/) | 2019 | Observational (self-controlled case series) | Scientific Reports | Analysis of 31,992 newly diagnosed RA patients (UK CPRD GOLD) examining antibiotic exposure timing vs. RA flares; not nitrofurantoin-specific efficacy data |
| [15195196](https://pubmed.ncbi.nlm.nih.gov/15195196/) | 2004 | Review | Saudi Medical Journal | Review of drug-induced pulmonary fibrosis; lists nitrofurantoin among causative drugs and notes RA as a predisposing condition for fibrosis |
| [35145797](https://pubmed.ncbi.nlm.nih.gov/35145797/) | 2022 | Case report | Cureus | Irreversible pulmonary fibrosis in a 94-year-old RA patient from combined methotrexate + nitrofurantoin therapy — a toxicity/interaction signal, not efficacy evidence |
| [25362778](https://pubmed.ncbi.nlm.nih.gov/25362778/) | 2014 | Review | La Revue du praticien | Review of drug-induced interstitial lung disease; nitrofurantoin listed among causative antibiotics |
| [3335140](https://pubmed.ncbi.nlm.nih.gov/3335140/) | 1988 | Case series | Chest | Cohort of 57 hospitalised RA patients with interstitial lung fibrosis; describes RA-associated lung disease, does not evaluate nitrofurantoin as treatment |
| [11937933](https://pubmed.ncbi.nlm.nih.gov/11937933/) | 2002 | Case report | Annales de dermatologie et de venereologie | Phenylbutazone-induced sialadenitis case; nitrofurantoin mentioned only as another drug associated with sialadenitis, unrelated to RA treatment |
| [899886](https://pubmed.ncbi.nlm.nih.gov/899886/) | 1977 | Observational | Acta Medica Scandinavica | Short-term nitrofurantoin therapy for bacteriuria in middle-aged women; unrelated to RA |
| [41635325](https://pubmed.ncbi.nlm.nih.gov/41635325/) | 2026 | Case report | Cureus | Autoimmune hepatitis case; nitrofurantoin is one of several drugs ruled out as cause of drug-induced liver injury, RA mentioned only as a differential diagnosis |
| [8104358](https://pubmed.ncbi.nlm.nih.gov/8104358/) | 1993 | Case report | Revue de pneumologie clinique | Gold-salt-induced pneumonitis/alveolitis case in a patient on anti-rheumatic therapy; nitrofurantoin not directly implicated |
| [4608019](https://pubmed.ncbi.nlm.nih.gov/4608019/) | 1974 | Review | Der Internist | General synopsis of alveolitis and pulmonary fibrosis mechanisms |

**Note:** This literature set is dominated by nitrofurantoin **toxicity in RA patients**, not evidence of therapeutic benefit for RA.

---

## Denmark Market Information

No marketing authorisations found. Nitrofurantoin is currently **not marketed** in Denmark according to the available data (0 licenses on record).

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information (key warnings, contraindications, and DDI data are not available in this Evidence Pack — flagged as Blocking Data Gap DG001).

**Note from literature review:** A case report ([PMID 35145797](https://pubmed.ncbi.nlm.nih.gov/35145797/)) describes irreversible pulmonary fibrosis in an RA patient from combined methotrexate and nitrofurantoin use — this interaction signal should be considered before any further evaluation of nitrofurantoin in RA patients.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No clinical trials exist for this pairing, no MOA data is available, and the associated literature describes toxicity risk in RA patients rather than therapeutic efficacy. The 99.89% TxGNN score reflects model similarity only (Evidence Level L5) and is not corroborated by any biological or clinical rationale — this is not sufficient to justify further investment at this time.

**To proceed, the following is needed:**
- Danish SmPC / warnings and contraindications data (Blocking gap, DG001)
- DrugBank mechanism of action data (DG002)
- A targeted literature or preclinical search specifically for immunomodulatory/anti-inflammatory activity of nitrofurantoin, since none currently exists
- Clarification of the drug-drug interaction risk with methotrexate (common RA therapy) before any clinical consideration
- Confirmation of Danish market/registration status, as the drug is currently unmarketed with 0 authorisations on record
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

