---
layout: default
title: Teicoplanin
parent: 僅模型預測 (L5)
nav_order: 420
evidence_level: L5
indication_count: 10
---

# Teicoplanin
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

# Teicoplanin: From Gram-Positive Bacterial Infections to Bacterial Arthritis

## One-Sentence Summary

Teicoplanin is a glycopeptide antibiotic long used to treat serious gram-positive bacterial infections (bacteremia, endocarditis, skin/soft-tissue and bone-joint infections). The TxGNN model predicts it may also be effective for **Bacterial Arthritis**, a prediction already substantially supported by **20 publications** describing real-world use in septic/bone-joint infections, though **no registered clinical trials** exist for this specific indication and the drug is currently **not marketed in Denmark**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in the available Danish regulatory data (drug not marketed); literature describes established use in serious gram-positive bacterial infections |
| Predicted New Indication | Bacterial Arthritis |
| TxGNN Prediction Score | 94.25% |
| Evidence Level | L3 (systematic review/meta-analysis and observational studies; no registered clinical trials) |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack. Based on known information, Teicoplanin is a glycopeptide-class antibiotic active against gram-positive bacteria (including MRSA); its efficacy in serious gram-positive infections such as bacteremia, endocarditis, and skin/soft-tissue infections is well established in the literature.

Bacterial (septic) arthritis is most commonly caused by *Staphylococcus aureus* and other gram-positive organisms — the same pathogen spectrum teicoplanin already targets. Several of the publications retrieved for this candidate go beyond a purely computational hypothesis: they describe teicoplanin dosing regimens specifically for septic arthritis (e.g., 12 mg/kg/day, higher than the standard maintenance dose), and multiple studies report clinical outcomes in patients with pyogenic/septic arthritis treated with teicoplanin. This suggests the "new indication" reflects an already-recognized, if not formally registered, clinical use rather than a purely novel mechanistic extrapolation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8351549](https://pubmed.ncbi.nlm.nih.gov/8351549/) | 1993 | Clinical trial | Southern Medical Journal | Community-based trial of once-daily teicoplanin (avg. 10.1 mg/kg) in 66 patients with gram-positive bone/joint infections including septic arthritis |
| [1381644](https://pubmed.ncbi.nlm.nih.gov/1381644/) | 1992 | Clinical trial (cooperative study) | Eur J Surg Suppl | Teicoplanin Bone and Joint Cooperative Study Group (USA): 90/98 patients evaluated, including acute/chronic osteomyelitis |
| [2952062](https://pubmed.ncbi.nlm.nih.gov/2952062/) | 1987 | Clinical trial | Antimicrob Agents Chemother | 19 patients with serious gram-positive infections incl. pyogenic arthritis; 8/13 evaluable cases clinically cured |
| [12481488](https://pubmed.ncbi.nlm.nih.gov/12481488/) | 2002 | Retrospective study | Medicina | 89 episodes of MRSA bone/joint infections, including 10 septic arthritis cases; efficacy assessed by dosing schedule |
| [27809799](https://pubmed.ncbi.nlm.nih.gov/27809799/) | 2016 | Retrospective cohort | BMC Infectious Diseases | Teicoplanin-based therapy (incl. subcutaneous route) in *S. aureus* bone and joint infection |
| [17825421](https://pubmed.ncbi.nlm.nih.gov/17825421/) | 2007 | Cohort study | The Journal of Infection | Trough teicoplanin levels in musculoskeletal infection; standard doses may be subtherapeutic |
| [2140111](https://pubmed.ncbi.nlm.nih.gov/2140111/) | 1990 | Clinical trial | J Antimicrob Chemother | 33 patients with bone/soft-tissue infections incl. 3 septic arthritis cases treated with teicoplanin |
| [9474479](https://pubmed.ncbi.nlm.nih.gov/9474479/) | 1997 | Review | Drugs | Reviews anti-gram-positive agents; specifies higher teicoplanin dose (12 mg/kg/day) for septic arthritis |
| [11131961](https://pubmed.ncbi.nlm.nih.gov/11131961/) | 2000 | Review | Journal of Chemotherapy | Reviews teicoplanin dosing across serious infections including bone and joint infections |
| [30876673](https://pubmed.ncbi.nlm.nih.gov/30876673/) | 2019 | Retrospective cohort | Enferm Infecc Microbiol Clin | Dual teicoplanin + cefazolin prophylaxis to prevent prosthetic joint infection |

---

## Denmark Market Information

Teicoplanin currently has no marketing authorisation on record in Denmark (0 licenses; market status: not marketed).

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The literature base (L3: retrospective/cohort studies and reviews, no registered RCTs) offers reasonable mechanistic and real-world support, but the drug is not currently marketed in Denmark and a **Blocking** data gap exists — Danish/EU product-label warnings and contraindications are unavailable, which prevents the mandatory initial safety (S1) evaluation.

**To proceed, the following is needed:**
- Official SmPC/label warnings and contraindications (Blocking gap)
- Detailed mechanism of action data from DrugBank or equivalent source
- Confirmation of any EU/EMA marketing authorisation pathway applicable to Denmark
- Drug-drug interaction data (currently not found)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

