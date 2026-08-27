---
layout: default
title: Robenacoxib
parent: 僅模型預測 (L5)
nav_order: 385
evidence_level: L5
indication_count: 10
---

# Robenacoxib
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

# Robenacoxib: From Veterinary Osteoarthritis to Human Osteoarthritis

## One-Sentence Summary

Robenacoxib is a highly COX-2-selective NSAID currently approved **only for veterinary use** (dogs and cats, marketed as Onsior) for pain and inflammation, including osteoarthritis; it holds no human marketing authorisation in Denmark. The TxGNN model predicts activity against human **Osteoarthritis** (score 98.79%), but the underlying evidence base consists entirely of veterinary randomized trials and pharmacokinetic studies — **no human clinical trial or human safety data currently exists** for this compound.

> ⚠️ **Critical caveat**: The predicted "new indication" (osteoarthritis) is the *same disease* the drug already treats — but only in dogs and cats. This is a cross-species extrapolation signal, not a genuine new-indication repurposing candidate, until human data is generated.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in Danish/human regulatory data. Per veterinary literature, Robenacoxib (Onsior®) is EU-approved for pain and inflammation associated with musculoskeletal disorders (incl. osteoarthritis) and peri-operative pain in **dogs and cats only** |
| Predicted New Indication | Osteoarthritis (human) |
| TxGNN Prediction Score | 98.79% |
| Evidence Level | **L4** (veterinary RCT/mechanistic evidence only — no completed human trials; see note below) |
| Denmark Market Status | Not marketed (未上市) |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | **Hold** |

**On Evidence Level**: the evidence pack's internal scoring labels this "L2," which reflects the strength of the *veterinary* trial base (multiple completed randomized veterinary trials). Applying the evidence-level rubric to the **human** indication under evaluation, there are zero completed human trials (confirmed 0 hits in ClinicalTrials.gov and ICTRP), so the correct classification for human decision-making is **L4 (preclinical/mechanistic analog evidence)**, not L1/L2.

---

## Why is This Prediction Reasonable?

Detailed DrugBank mechanism-of-action data is flagged as a gap (DG002) in this evidence pack. However, the retrieved literature (PMID 30148083) describes Robenacoxib as a coxib-class NSAID with high selectivity for cyclooxygenase-2 (COX-2) and weak, rapidly reversible COX-1 binding — the same mechanistic class as human NSAIDs used in osteoarthritis (e.g., celecoxib, etoricoxib). This selectivity profile is the pharmacological basis for its anti-inflammatory and analgesic effect in veterinary osteoarthritis.

The original and predicted indications are, in fact, the identical disease (osteoarthritis) — the "prediction" reflects that Robenacoxib already has strong, repeated evidence of efficacy against osteoarthritic pain, just in a different species. Mechanistically, COX-2-mediated prostaglandin synthesis and joint inflammation pathways are highly conserved between dogs, cats, and humans, which is why the TxGNN knowledge graph scores this pairing so highly.

That conservation does **not**, however, establish human efficacy or safety. Robenacoxib has never been evaluated in a human clinical trial; species differences in pharmacokinetics, protein binding, and GI/renal/hepatic tolerability for coxib-class NSAIDs are well documented and cannot be assumed to translate directly from cats and dogs to humans.

---

## Clinical Trial Evidence

Currently no related human clinical trials registered (ClinicalTrials.gov and WHO ICTRP both returned 0 results for Robenacoxib + osteoarthritis).

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22673598](https://pubmed.ncbi.nlm.nih.gov/22673598/) | 2012 | RCT (veterinary, non-inferiority) | J Vet Med Sci | Oral robenacoxib non-inferior to carprofen for canine osteoarthritis over 28 days (n=32) |
| [26058587](https://pubmed.ncbi.nlm.nih.gov/26058587/) | 2016 | RCT (veterinary, placebo-controlled) | J Feline Med Surg | Confirmed clinical safety of robenacoxib in feline osteoarthritis vs. placebo |
| [21480932](https://pubmed.ncbi.nlm.nih.gov/21480932/) | 2012 | RCT (veterinary, non-inferiority) | J Vet Pharmacol Ther | Robenacoxib non-inferior to carprofen in canine osteoarthritis, multicentre trial (n=125+) |
| [33833276](https://pubmed.ncbi.nlm.nih.gov/33833276/) | 2021 | RCT (veterinary) | Scientific Reports | Robenacoxib effective for degenerative joint disease pain in cats (n=109), blinded pilot trial |
| [23782347](https://pubmed.ncbi.nlm.nih.gov/23782347/) | 2013 | Systematic Review | J Vet Intern Med | Systematic review of NSAID-induced adverse effects in dogs, including robenacoxib class |
| [38587872](https://pubmed.ncbi.nlm.nih.gov/38587872/) | 2024 | Review/Consensus Guideline | J Feline Med Surg | 2024 ISFM/AAFP consensus guidelines on long-term NSAID use in cats |
| [30148083](https://pubmed.ncbi.nlm.nih.gov/30148083/) | 2018 | Review | Vet Med (Auckland) | Overview of robenacoxib pharmacology, safety, and place in veterinary therapy |
| [23452411](https://pubmed.ncbi.nlm.nih.gov/23452411/) | 2013 | Cohort/experimental (biomarker) | BMC Vet Res | Robenacoxib reduced synovial fluid C-reactive protein in dogs with osteoarthritis (n=34) |
| [31487772](https://pubmed.ncbi.nlm.nih.gov/31487772/) | 2019 | Comparative clinical study (veterinary) | Veterinary Sciences | Compared UC-II collagen vs. robenacoxib for mobility impairment in canine osteoarthritis |
| [20922466](https://pubmed.ncbi.nlm.nih.gov/20922466/) | 2010 | PK/population study | Pharm Res | Population PK of robenacoxib in blood and synovial fluid of healthy and osteoarthritic dogs |

*Note: all 11 retrieved publications are veterinary studies; one additional PK study (PMID 23726662) was omitted from this table as duplicative of the PK entry above.*

---

## Denmark Market Information

Robenacoxib currently has **no marketing authorisation in Denmark** (0 licenses on record) and is not registered as a human medicinal product. It is marketed in the EU exclusively as a veterinary product (Onsior®) for use in dogs and cats.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information — no human key-warning, contraindication, or drug-interaction data is currently available for Robenacoxib (DG001, Blocking gap).

Additional context from veterinary literature: coxib-class NSAIDs as a group carry known risks of gastrointestinal, renal, and hepatic adverse effects (PMID 23782347, PMID 38587872), which would need to be re-established through human pharmacovigilance and trial data before any human use is considered.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Robenacoxib is a veterinary-only NSAID with no Danish or human marketing authorisation, no human clinical trial data, and a blocking data gap on SmPC warnings/contraindications (DG001). The TxGNN signal is mechanistically plausible (COX-2 inhibition is a validated osteoarthritis pathway) but is built entirely on animal trial evidence, so it does not meet the bar for progressing toward human development at this time.

**To proceed, the following is needed:**
- Formal DrugBank/literature-sourced mechanism of action data (DG002)
- Danish/EU regulatory review of human SmPC warnings, contraindications, and drug interactions (DG001)
- At minimum, preclinical human-relevant toxicology and pharmacokinetic bridging data before any human trial is designed
- Confirmation of whether any human-formulation development program for Robenacoxib exists
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

