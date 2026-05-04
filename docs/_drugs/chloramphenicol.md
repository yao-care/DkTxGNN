---
layout: default
title: Chloramphenicol
parent: 僅模型預測 (L5)
nav_order: 108
evidence_level: L5
indication_count: 10
---

# Chloramphenicol
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

# Chloramphenicol: From Systemic Bacterial Infections to Conjunctivitis

## One-Sentence Summary

Chloramphenicol is a broad-spectrum bacteriostatic antibiotic introduced into clinical practice in 1948, historically used for serious systemic bacterial infections including typhoid fever, meningitis, plague, and cholera.
The TxGNN model predicts it may be effective for **Conjunctivitis** with a score of **99.66%**,
supported by **0 registered clinical trials** and **19 publications** — including multiple RCTs and two Cochrane systematic reviews. Notably, chloramphenicol is already a standard topical treatment for bacterial conjunctivitis in the United Kingdom and several other countries, but currently holds no marketing authorisation in Denmark.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available from Danish licensing records; historically used for systemic bacterial infections (typhoid fever, meningitis, cholera, rickettsial infections) |
| Predicted New Indication | Conjunctivitis |
| TxGNN Prediction Score | 99.66% |
| Evidence Level | L1 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Chloramphenicol exerts its antibacterial effect by binding to the 50S subunit of bacterial ribosomes and inhibiting peptidyl transferase activity, thereby blocking protein synthesis. This broad-spectrum bacteriostatic mechanism is directly active against the principal causative organisms of bacterial conjunctivitis — *Staphylococcus aureus*, *Haemophilus influenzae*, and *Streptococcus pneumoniae*. When applied topically as an ophthalmic solution (typically 0.5% eye drops) or ointment, the drug achieves therapeutic concentrations at the ocular surface while keeping systemic absorption to a minimum — a pharmacokinetic profile that substantially reduces the risk of the most serious known adverse effect, idiosyncratic aplastic anaemia.

The connection between chloramphenicol's original role in systemic infections and the conjunctivitis indication is mechanistically straightforward: both disease settings involve susceptible bacterial pathogens against which inhibition of 50S-mediated protein synthesis is effective. The shift to a topical ophthalmic route simply optimises the risk-benefit balance by concentrating drug exposure at the site of infection. In vitro susceptibility data (PMID 7671609) ranked chloramphenicol highest among established topical antibiotics for conjunctivitis-causing organisms.

The TxGNN model's prediction score of 99.66% is not surprising in this context: chloramphenicol ophthalmic preparations are currently authorised and widely dispensed for bacterial conjunctivitis in the United Kingdom, Ireland, and other European countries. The key clinical question for Denmark is therefore not whether the drug works for this indication — the evidence clearly shows it does — but whether a regulatory pathway and safety-monitoring framework can be established for the Danish market, where no current authorisation exists.

---

## Clinical Trial Evidence

Currently no clinical trials specifically evaluating chloramphenicol for conjunctivitis are registered on ClinicalTrials.gov or the WHO ICTRP.

The evidence base for this indication rests entirely on historical and contemporary peer-reviewed literature, including multiple RCTs and Cochrane-level systematic reviews (see Literature Evidence below).

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [38511104](https://pubmed.ncbi.nlm.nih.gov/38511104/) | 2024 | Comparative Clinical Trial | Current Therapeutic Research | Head-to-head comparison of moxifloxacin vs. chloramphenicol for bacterial eye infections; confirms chloramphenicol's continued role as an established topical ophthalmic comparator |
| [32959365](https://pubmed.ncbi.nlm.nih.gov/32959365/) | 2020 | Cochrane Systematic Review | Cochrane Database of Systematic Reviews | Evaluates prophylactic interventions for ophthalmia neonatorum (neonatal conjunctivitis); chloramphenicol assessed as one of the antibiotic options for preventing vision-threatening neonatal eye infection |
| [16378567](https://pubmed.ncbi.nlm.nih.gov/16378567/) | 2005 | Cochrane Systematic Review & Meta-analysis | British Journal of General Practice | Updated Cochrane meta-analysis of topical antibiotics vs. placebo for acute bacterial conjunctivitis in primary care; confirms benefit of topical antibiotic treatment, including chloramphenicol, over watchful waiting |
| [17947266](https://pubmed.ncbi.nlm.nih.gov/17947266/) | 2007 | RCT (equivalency) | British Journal of Ophthalmology | RCT comparing 2.5% povidone-iodine eye drops vs. ophthalmic chloramphenicol for prevention of neonatal conjunctivitis in a trachoma-endemic area; establishes chloramphenicol as an active prophylactic reference |
| [3554881](https://pubmed.ncbi.nlm.nih.gov/3554881/) | 1987 | RCT (single-blind) | Acta Ophthalmologica | Single-blind RCT (n=250) comparing fusidic acid 1% vs. chloramphenicol 0.5% for acute purulent conjunctivitis; clinical success 81% (chloramphenicol) vs. 84% (fusidic acid) — no statistically significant difference in efficacy |
| [3300139](https://pubmed.ncbi.nlm.nih.gov/3300139/) | 1987 | RCT (open-label) | Acta Ophthalmologica | Three-arm RCT in Tanzania comparing fusidic acid, chloramphenicol, and framycetin eye drops; fusidic acid superior (93% success) due to lower local resistance rates; chloramphenicol success rate 48%, limited by high resistance prevalence in that setting |
| [6188739](https://pubmed.ncbi.nlm.nih.gov/6188739/) | 1983 | RCT (double-blind multicentre) | Journal of Antimicrobial Chemotherapy | Multicentre double-blind RCT (n=230) comparing trimethoprim-polymyxin B vs. chloramphenicol ophthalmic solution in presumptive bacterial conjunctivitis; both preparations effective with minimal adverse events |
| [8800624](https://pubmed.ncbi.nlm.nih.gov/8800624/) | 1996 | Pharmacovigilance Review | Drug Safety | Critical safety review of the controversial association between topical ocular chloramphenicol and aplastic anaemia; notes widespread UK use for conjunctivitis vs. near-absence of prescribing in the USA — highlights the regulatory risk-benefit divergence |
| [8333258](https://pubmed.ncbi.nlm.nih.gov/8333258/) | 1993 | Clinical Comparison Study | Acta Ophthalmologica | Comparison of fusidic acid twice daily vs. chloramphenicol six times daily in acute conjunctivitis recruited from 38 Norwegian general practitioners; no significant difference in bacteriological or clinical response |
| [7153511](https://pubmed.ncbi.nlm.nih.gov/7153511/) | 1982 | Cohort Study | Journal of Hygiene | In neonatal chlamydial conjunctivitis (n=127 infected infants), prior chloramphenicol eye drops reduced symptom severity but failed to eradicate *Chlamydia trachomatis* (85% of eye swabs remained positive), demonstrating the drug's ineffectiveness against chlamydial aetiology |

---

## Denmark Market Information

Chloramphenicol currently holds **no marketing authorisations** in Denmark. No records exist for either national (Laegemiddelstyrelsen) or centralised (EMA) authorisations.

For contextual reference, topical chloramphenicol ophthalmic preparations (0.5% w/v eye drops; 1% w/v eye ointment) are authorised under national procedures in the United Kingdom, Ireland, and a number of other European countries for bacterial conjunctivitis. These existing national authorisations may be relevant as a regulatory reference basis for any future Danish application.

---

## Safety Considerations

**Key Safety Warning — Aplastic Anaemia Risk:**
The published literature (PMID 8800624) identifies a well-recognised pharmacovigilance concern: a controversial but potentially serious association between topical ophthalmic chloramphenicol and idiosyncratic aplastic anaemia. Although the absolute risk from topical use appears very low (systemic absorption via eye drops is minimal), this signal has historically driven divergent regulatory decisions across markets — widespread use in the UK vs. near-restriction in the USA. Any Danish authorisation pathway must explicitly address this risk with robust post-marketing pharmacovigilance requirements.

**Chlamydial Conjunctivitis Limitation:**
Evidence (PMID 7153511) confirms chloramphenicol is ineffective against *Chlamydia trachomatis*. Prescribers must ensure correct aetiological diagnosis, as chlamydial conjunctivitis requires systemic macrolide therapy and will not respond to topical chloramphenicol.

Please refer to the approved Summary of Product Characteristics (SmPC) of an applicable national or EMA authorisation for complete safety information including contraindications, drug interactions, and special population guidance.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The evidence base for topical chloramphenicol in bacterial conjunctivitis is clinically well established — supported by multiple historical RCTs, two Cochrane systematic reviews, and a TxGNN prediction score of 99.66%. The drug is already in routine clinical use for this indication across several European markets. The primary barriers in Denmark are regulatory (no current marketing authorisation) and pharmacovigilance (aplastic anaemia signal), rather than efficacy or mechanistic uncertainty.

**To proceed, the following is needed:**

- **Regulatory pathway assessment**: Evaluate options for accessing the drug in Denmark — either via a new national marketing authorisation application to Laegemiddelstyrelsen, or via import of a product already authorised in another EU Member State under Article 3(1) of Directive 2001/83/EC
- **Formal MOA documentation**: Retrieve full mechanism of action and DrugBank pharmacology data to support the regulatory submission
- **Risk management plan (RMP)**: Develop a targeted pharmacovigilance plan addressing the aplastic anaemia safety signal, including patient information materials and prescriber guidance on limiting duration of use
- **Danish resistance surveillance**: Obtain current local antibiogram data for conjunctivitis-causing pathogens in Denmark to confirm susceptibility before recommending widespread use
- **Prescriber guidance on aetiology**: Develop clear clinical criteria for bacterial vs. viral vs. chlamydial conjunctivitis to ensure appropriate use and avoid treatment failures
- **Formulation specification**: Confirm pharmaceutical quality and cold-chain requirements for the 0.5% ophthalmic solution in the Danish supply chain

---

*This report is generated for research purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before therapeutic application. Data cut-off: 2026-04-04.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

