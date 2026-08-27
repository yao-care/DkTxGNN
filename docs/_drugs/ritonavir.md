---
layout: default
title: Ritonavir
parent: 僅模型預測 (L5)
nav_order: 383
evidence_level: L5
indication_count: 6
---

# Ritonavir
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

# Ritonavir: From HIV-1 Infection to Simian Immunodeficiency Virus (SIV) Infection

## One-Sentence Summary

> Ritonavir is a well-known HIV-1 protease inhibitor, most commonly used today as a pharmacokinetic booster in combination antiretroviral regimens (structured original-indication data was not returned by this evidence pack).
> The TxGNN model's top-ranked prediction is **Simian Immunodeficiency Virus (SIV) Infection** — a lentiviral disease of non-human primates, not a human condition —
> with a **99.92% prediction score** but **no completed clinical trials** and only **12 preclinical/in vitro publications**, none of which establish clinical benefit in humans.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in the evidence pack (Ritonavir is a known HIV-1 protease inhibitor / pharmacokinetic booster — general pharmacological knowledge, not sourced from structured data here) |
| Predicted New Indication | Simian Immunodeficiency Virus (SIV) Infection *(a non-human primate disease)* |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L4 (preclinical/mechanistic studies only — no completed clinical trials) |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action (MOA) data was not available in this evidence pack (data gap DG002). Based on general pharmacological knowledge, ritonavir is an HIV-1 aspartyl protease inhibitor. In vitro and macaque studies in the literature confirm that ritonavir also inhibits SIV protease, since SIV and HIV are both lentiviruses with structurally homologous protease enzymes (PMID 12709355, PMID 15040537). This cross-reactivity plausibly explains why the TxGNN model links ritonavir to SIV infection with a very high score.

However, this predicted "new indication" is not clinically actionable: **SIV infection occurs only in non-human primates and is not a human disease.** All supporting literature consists of in vitro susceptibility assays or macaque animal models used as research tools for HIV pathogenesis and antiretroviral research — not evidence of a treatable human condition. The remaining predicted indications for ritonavir in this evidence pack (feline acquired immunodeficiency syndrome — a cat-only disease — and a rare human neurodevelopmental white-matter disorder with no mechanistic rationale) share the same problem: either the target species is non-human, or no plausible mechanistic link exists at all.

This suggests the current top-ranked predictions reflect a genuine mechanistic signal (protease cross-reactivity across lentiviruses) rather than a viable human drug-repurposing opportunity. A clinically meaningful human indication for ritonavir would need to be identified separately, most likely by reviewing lower-ranked candidates or re-running the query against a curated disease vocabulary restricted to human conditions.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for the top-ranked predicted indication (SIV Infection).

*(Note: one trial, [NCT02770508](https://clinicaltrials.gov/study/NCT02770508), was returned under the separate "feline acquired immunodeficiency syndrome" candidate, but it studies boosted darunavir + lamivudine in human HIV-1 patients — the evidence pack itself flags this as an apparent drug/indication mismatch in the source database, not genuine supporting evidence.)*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12709355](https://pubmed.ncbi.nlm.nih.gov/12709355/) | 2003 | In vitro susceptibility study | Antimicrobial Agents and Chemotherapy | Ritonavir inhibited SIVmac239 protease (EC50 ≈13 nM), comparable to its inhibition of HIV-1 |
| [15040537](https://pubmed.ncbi.nlm.nih.gov/15040537/) | 2004 | In vitro susceptibility study | Antiviral Therapy | Screened 16 approved anti-HIV-1 drugs, including ritonavir, against HIV-2, SIV and SHIV strains |
| [16973590](https://pubmed.ncbi.nlm.nih.gov/16973590/) | 2006 | Animal study (macaque model) | Journal of Virology | Quadruple antiretroviral therapy produced rapid viral decay in SIV-infected macaques |
| [34903055](https://pubmed.ncbi.nlm.nih.gov/34903055/) | 2021 | Animal study (neuroimmune, macaque) | mBio | Lentiviral reservoirs persisted in brain tissue despite effective antiretroviral therapy |
| [9875393](https://pubmed.ncbi.nlm.nih.gov/9875393/) | 1998 | In vitro pharmacology | Antiviral Chemistry & Chemotherapy | Fluoroquinolone derivative K-12 retained activity against ritonavir-resistant HIV-1 and SIV strains |
| [25033210](https://pubmed.ncbi.nlm.nih.gov/25033210/) | 2014 | Animal study (macaque, ART+HDAC) | PLoS ONE | Combination cART plus an HDAC inhibitor studied in SIV-infected rhesus macaques for viral reservoir impact |
| [17350308](https://pubmed.ncbi.nlm.nih.gov/17350308/) | 2007 | Animal study (SHIV construction) | Microbes and Infection | Engineered SHIV carrying HIV-1 protease gene, used as an in vivo tool for testing protease inhibitors in macaques |
| [12186895](https://pubmed.ncbi.nlm.nih.gov/12186895/) | 2002 | In vitro virology | Journal of Virology | Characterized HIV-1 protease-mediated processing of the viral Vif protein |
| [12951220](https://pubmed.ncbi.nlm.nih.gov/12951220/) | 2003 | Animal study (macaque) | Journal of Virological Methods | Oral HAART (including lopinavir/ritonavir) evaluated for effect on CD8 subset in SHIV-infected macaques |
| [11364629](https://pubmed.ncbi.nlm.nih.gov/11364629/) | 1997 | Review/Commentary | J Int Assoc Physicians AIDS Care | Brief commentary on chemokine receptor research; minimal direct relevance |

*(Two additional low-relevance records with incomplete classification, PMID 22737073 and PMID 7475727, were excluded from this table.)*

---

## Denmark Market Information

Ritonavir is currently **not marketed** in Denmark per this evidence pack, with 0 marketing authorisations on file. No Laegemiddelstyrelsen or EMA centralised authorisation records were available for listing.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

*(Key warnings, contraindications, and drug-interaction data were not available in this evidence pack — this is flagged as a blocking data gap, see Conclusion below.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication, SIV infection, is a non-human primate disease and therefore not a viable human clinical repurposing target, despite a high TxGNN score and plausible protease cross-reactivity mechanism. No completed clinical trials exist for any of the top candidates, and safety/label data required for even a preliminary safety review is missing.

**To proceed, the following is needed:**
- TFDA/SmPC warnings and contraindications (blocking data gap DG001)
- Confirmed mechanism of action (MOA) data (data gap DG002)
- Re-screening of the predicted indication list to filter out non-human disease targets (SIV infection, feline AIDS) and identify a clinically valid human candidate
- Investigation of the apparent drug/indication mismatch flagged for trial NCT02770508
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

