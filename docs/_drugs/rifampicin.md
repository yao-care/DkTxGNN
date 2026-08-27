---
layout: default
title: Rifampicin
parent: 僅模型預測 (L5)
nav_order: 377
evidence_level: L5
indication_count: 10
---

# Rifampicin
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

Using the evidence pack as provided (no skill applies — this is a direct templated report-generation task per the system prompt's explicit format).

# Rifampicin: From Antituberculosis Therapy to Conjunctivitis

## One-Sentence Summary

Rifampicin is a rifamycin-class antibiotic classically used against tuberculosis and leprosy; the original indication and mechanism-of-action fields are not recorded in this evidence pack (data gaps DG001/DG002). The TxGNN model predicts it may be effective for **Conjunctivitis**, with a **99.95% prediction score**, but currently **0 registered clinical trials** and only **20 literature references** — mostly older case reports and one small controlled trachoma trial — support this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in evidence pack — Rifampicin is classically an antituberculosis/antileprosy rifamycin antibiotic (pending confirmation via DrugBank/TFDA, see DG002) |
| Predicted New Indication | Conjunctivitis |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L3 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data for this evidence pack is not available (DG002). Based on general pharmacological classification, rifampicin is a rifamycin that inhibits bacterial DNA-dependent RNA polymerase, giving it broad antibacterial (and some antichlamydial) activity — this is basic drug-class knowledge, not a finding from this evidence pack.

No original indication is recorded in the pack (`taiwan_regulatory.licenses` and `drug.original_indications` are both empty), so a direct comparison between "original" and "predicted" indications cannot be made from the supplied data alone.

The literature associated with the conjunctivitis prediction is largely historical: a 1975 controlled trial of topical rifampicin ointment for endemic trachoma (a chlamydial conjunctival infection) in Tunisia, a 1970 in vitro study of anti-trachoma activity, and several bacterial-etiology/susceptibility surveys of conjunctivitis pathogens. Together these suggest a plausible but dated and narrow rationale — rifampicin's known activity against *Chlamydia trachomatis* and some Gram-positive conjunctival pathogens — rather than a strong, modern, disease-specific efficacy signal.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1096630](https://pubmed.ncbi.nlm.nih.gov/1096630/) | 1975 | Controlled trial | American Journal of Ophthalmology | Compared topical 1% tetracycline, 1% rifampicin, and 5% boric acid ointments in Tunisian schoolchildren with active trachoma; treatments given twice daily for 10 weeks with follow-up to 39 weeks |
| [6635446](https://pubmed.ncbi.nlm.nih.gov/6635446/) | 1983 | Review | Reviews of Infectious Diseases | Rifampin is the most active antibiotic by weight against *Chlamydia trachomatis*; as effective as tetracyclines for topical trachoma treatment, but resistance emerges easily in vitro |
| [5411121](https://pubmed.ncbi.nlm.nih.gov/5411121/) | 1970 | Preclinical | Nature | Early study of anti-trachoma activity of rifampicin and rifamycin SV derivatives |
| [5005929](https://pubmed.ncbi.nlm.nih.gov/5005929/) | 1971 | Case report/commentary | Annals of Ophthalmology | Early ophthalmology commentary on rifampicin (abstract not available) |
| [19941479](https://pubmed.ncbi.nlm.nih.gov/19941479/) | 2010 | Review | Current Medicinal Chemistry | Reviews neglected bacterial diseases including trachoma; notes rifampin/streptomycin combinations used for related conditions |
| [33457332](https://pubmed.ncbi.nlm.nih.gov/33457332/) | 2020 | Observational | Advanced Biomedical Research | Bacterial etiology and antibiotic susceptibility of conjunctivitis isolates in Kashan, Iran |
| [21484175](https://pubmed.ncbi.nlm.nih.gov/21484175/) | 2011 | Observational | Journal of Ophthalmic Inflammation and Infection | Bacteriologic and plasmid analysis of conjunctivitis etiologic agents in Lagos, Nigeria |
| [15228931](https://pubmed.ncbi.nlm.nih.gov/15228931/) | 2004 | Observational/Review | Anales de Pediatría | Reviews prevalent bacterial conjunctivitis pathogens and antibiotic sensitivity patterns |
| [8363150](https://pubmed.ncbi.nlm.nih.gov/8363150/) | 1993 | Observational | Anales Españoles de Pediatría | Retrospective microbiologic study of 50 neonatal conjunctivitis cases; 84% positive bacterial culture |
| [14686993](https://pubmed.ncbi.nlm.nih.gov/14686993/) | 2003 | Case report | Clinical Microbiology and Infection | Primary meningococcal conjunctivitis in a 6-year-old, treated topically then with systemic rifampin after diagnosis; no complications |

## Denmark Market Information

Currently no marketing authorisation on record for Rifampicin in Denmark (market status: Not marketed; 0 authorisations).

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information. Note: TFDA/SmPC warnings and contraindications are flagged in this evidence pack as a **Blocking** data gap (DG001) — safety screening (S1) cannot currently be completed without this data.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- No clinical trials specifically evaluate rifampicin for conjunctivitis; supporting literature is limited to a 1970s controlled trachoma trial, older case reports, and general antibiotic-susceptibility surveys rather than direct efficacy evidence for conjunctivitis itself.
- A Blocking-severity data gap (DG001 — missing TFDA/SmPC warnings and contraindications) prevents even an initial safety assessment, and Rifampicin currently has no Danish marketing authorisation.

*(For context: two other TxGNN-flagged candidates in this evidence pack — "multiple endocrine neoplasia" and "HIV infectious disease" — were independently assessed as low-value signals: the former has no supporting trials/literature at all, the latter reflects TB/HIV co-treatment drug-interaction studies rather than direct anti-HIV activity. Both are recommended Hold and are not pursued further in this report.)*

**To proceed, the following is needed:**
- Confirmed original indication and mechanism-of-action data (DG002)
- TFDA/SmPC warnings, contraindications, and full DDI profile (DG001, Blocking)
- A modern, conjunctivitis-specific clinical study (rather than relying on trachoma-adjacent historical data)
- Clarification of route-of-administration compatibility (topical ophthalmic vs. systemic) for this indication
- Assessment of a Denmark/EU marketing-authorisation pathway, given current "Not marketed" status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

