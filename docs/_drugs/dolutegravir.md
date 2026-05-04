---
layout: default
title: Dolutegravir
parent: 僅模型預測 (L5)
nav_order: 146
evidence_level: L5
indication_count: 6
---

# Dolutegravir
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

# Dolutegravir: From HIV-1 Infection to Simian Immunodeficiency Virus Infection

---

## One-Sentence Summary

Dolutegravir (DTG) is a second-generation integrase strand transfer inhibitor (INSTI) approved since 2013 for the treatment of human HIV-1 infection; the Danish national registry data shows no registered authorisations, which is a known data gap rather than a true absence from the market.
The TxGNN model predicts it may be effective against **Simian Immunodeficiency Virus (SIV) Infection**, with **1 clinical trial** and **15 publications** currently supporting this direction — primarily through non-human primate (NHP) pre-clinical research.
The evidence reflects dolutegravir's established cross-species antiviral activity rather than a novel clinical repurposing opportunity for human patients.

> ⚠️ **Important data note**: The `original_indications` field is empty and `market_status` reads "not marketed" in this dataset. This is a data extraction gap, not the actual clinical reality. Dolutegravir (Tivicay®, ViiV Healthcare) holds EMA centralised marketing authorisation valid across all EU/EEA countries including Denmark, and is a WHO-recommended first-line antiretroviral agent for HIV-1 infection.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | HIV-1 infection (data gap in national registry — EMA/FDA approved since 2013) |
| Predicted New Indication | Simian Immunodeficiency Virus (SIV) Infection |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L3 |
| Denmark Market Status | Not found in national registry (data gap — Tivicay® holds EMA centralised authorisation) |
| Number of Marketing Authorisations | 0 (national registry only; EMA centralised authorisation applies) |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Dolutegravir is a second-generation integrase strand transfer inhibitor (INSTI). It works by blocking the viral integrase enzyme, which is essential for inserting the virus's genetic material into host cell DNA. By binding tightly to the integrase–DNA complex at the active site (DDE motif), DTG halts replication at a critical step and maintains a higher genetic barrier to resistance than first-generation INSTIs such as raltegravir or elvitegravir.

Simian Immunodeficiency Virus (SIV) belongs to the same lentivirus family as HIV-1 and HIV-2. SIV integrase shares more than 80% amino acid sequence similarity with HIV-1 integrase, including conservation of the active site residues that DTG targets. This structural homology means that DTG's mechanism of action transfers directly across species. Multiple independent NHP studies have confirmed that DTG-containing antiretroviral regimens effectively suppress SIV replication to clinically relevant levels in rhesus macaques (*Macaca mulatta*) and have characterised resistance patterns, CNS penetration, and long-term pharmacokinetics in this model.

It is important to set expectations correctly: SIV infection in non-human primates is a pre-clinical research model used to understand HIV pathogenesis, study cure strategies, and validate antiretroviral drug regimens — it is not an independent human clinical indication. The TxGNN prediction therefore validates DTG's biological plausibility in this cross-species context and confirms its utility as a pre-clinical tool. For Danish healthcare professionals, this is best understood as a mechanistic research confirmation rather than a repurposing opportunity requiring regulatory or clinical action.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT03577782](https://clinicaltrials.gov/study/NCT03577782) | Phase 1/2 | Unknown | 12 | Vedolizumab (an integrin antagonist) combined with antiretroviral therapy (ART) to achieve virological remission in HIV/SIV-infected subjects without prior ART. DTG formed part of the background ART regimen but was not the primary investigational agent. The small sample size and unknown status limit data reliability; DTG-specific contributions cannot be isolated from this trial. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [30381490](https://pubmed.ncbi.nlm.nih.gov/30381490/) | 2019 | Animal Model – NHP | Journal of Virology | DTG monotherapy in SIV-infected macaques selects for resistance mutations (analogous to HIV patterns) with variable virological outcomes; confirms high but not absolute resistance barrier in NHP models |
| [26378179](https://pubmed.ncbi.nlm.nih.gov/26378179/) | 2015 | In vitro / Animal | Journal of Virology | Characterised INSTI resistance profiles in SIVmac239; showed that the same resistance mutations produce equivalent phenotypes in both SIV and HIV, validating SIV as a DTG resistance model |
| [26150024](https://pubmed.ncbi.nlm.nih.gov/26150024/) | 2016 | Animal Model | AIDS Research and Human Retroviruses | Two novel injectable cART regimens (including DTG-based) effectively suppressed SIVmac239 replication to clinically relevant levels in rhesus macaques, supporting DTG's use as an NHP model backbone |
| [32506843](https://pubmed.ncbi.nlm.nih.gov/32506843/) | 2021 | Structural/Mechanistic Review | The FEBS Journal | HIV/SIV intasome crystal structures reveal how second-generation INSTIs (DTG, bictegravir) achieve tight integrase binding; explains cross-species activity and resistance escape mechanisms at atomic level |
| [36365101](https://pubmed.ncbi.nlm.nih.gov/36365101/) | 2022 | Animal Model – Longitudinal | Pharmaceutics | Pharmacokinetic validation of long-term TDF+FTC+DTG in SIVmac251-infected NHPs; DTG plasma concentrations and viral suppression confirmed, establishing the NHP as a reliable pharmacological model |
| [34903055](https://pubmed.ncbi.nlm.nih.gov/34903055/) | 2021 | Animal Model – CNS | mBio | CNS lentiviral reservoir persists despite effective DTG-based ART in both human and SIV macaque models; highlights brain as a pharmacological sanctuary site |
| [40093003](https://pubmed.ncbi.nlm.nih.gov/40093003/) | 2025 | Animal Model – Neuroimaging | Frontiers in Immunology | White matter tract deficits in SIV-infected rhesus macaques before and after FTC+TDF+DTG initiation; assesses ART timing, CNS repair, and viral control in an NHP model |
| [28923862](https://pubmed.ncbi.nlm.nih.gov/28923862/) | 2017 | In vitro / Animal | Antimicrobial Agents and Chemotherapy | Compared bictegravir and cabotegravir against INSTI-resistant SIVmac239 and HIV-1; contextualises DTG's resistance barrier relative to next-generation INSTIs |
| [25583721](https://pubmed.ncbi.nlm.nih.gov/25583721/) | 2015 | In vitro / Animal | Antimicrobial Agents and Chemotherapy | Simian-tropic HIV-1 chimeric virus validated as NHP model for studying INSTI resistance; supports use of SIV/HIV recombinants to characterise DTG resistance pathways |
| [24920794](https://pubmed.ncbi.nlm.nih.gov/24920794/) | 2014 | In vitro / Animal | Journal of Virology | HIV-1 INSTI resistance mutations (including DTG-selected) introduced into SIVmac239 integrase; established cross-species susceptibility mapping and confirmed conserved DDE active site |

---

## Denmark Market Information

No marketing authorisations were identified in the Danish Medicines Agency (Lægemiddelstyrelsen) national registry for dolutegravir at the time of data extraction (cutoff: 2026-04-05).

> ⚠️ **Data Gap — Action Required**: This almost certainly reflects an incomplete pull from national records rather than genuine absence. Dolutegravir is available in Denmark under the following EMA centralised authorisations (valid in all EU/EEA member states):
>
> | Product Name | Manufacturer | Formulation | Indication |
> |-------------|-------------|-------------|------------|
> | **Tivicay®** | ViiV Healthcare | 50 mg film-coated tablet | HIV-1 infection in adults and children (≥4 weeks, ≥3 kg) |
> | **Triumeq®** | ViiV Healthcare | Dolutegravir/abacavir/lamivudine fixed-dose tablet | HIV-1 infection in adults and adolescents |
>
> Healthcare professionals should verify current authorisation status directly via the [EMA product register](https://www.ema.europa.eu) or the Lægemiddelstyrelsen's own product database before prescribing.

---

## Additional Predicted Indications — Summary

The evidence pack contains two further indication clusters, each with important caveats:

### Feline Acquired Immunodeficiency Syndrome (FIV-AIDS) — Rank 2, L4

FIV (Feline Immunodeficiency Virus) and HIV-1 share approximately 40–50% integrase sequence homology — substantially lower than SIV's >80%. The DDE active site motif that DTG targets shows divergence in FIV, meaning in vitro IC₅₀ data for DTG against FIV are insufficient.

Direct veterinary evidence consists of a single study: PMID [37112803](https://pubmed.ncbi.nlm.nih.gov/37112803/) (Kim et al., *Viruses*, 2023) — a case series evaluating cART (DTG 2.5 mg/kg + tenofovir + emtricitabine) in FIV-infected domestic cats. Pharmacokinetics were characterised, but clinical outcome data were limited.

> ⚠️ **Knowledge graph mapping artefact**: The 5 clinical trials listed for this indication (SAILING, SPRING-2, SINGLE, ING116070, SPRING-1) are all pivotal human HIV-1 trials — they have no relevance to feline immunodeficiency and should not be interpreted as FIV evidence. This is a TxGNN disease-linkage error.

**Recommendation: Hold** — Insufficient direct evidence; veterinary research question only.

---

### Neurodevelopmental Disorder with Ataxic Gait, Absent Speech, and Decreased Cortical White Matter — Rank 5, L5

No clinical trials or literature support this as a treatment target. Zero evidence exists.

> ⚠️ **Reverse safety signal — do not pursue**: The TxGNN prediction likely reflects a knowledge graph artefact driven by the well-documented adverse association between periconceptional DTG exposure and neural tube defects (Zash et al., *NEJM* 2018/2019, Botswana cohort data). The model may be misinterpreting this *harmful* association as a *therapeutic* link. This disorder (OMIM: 617133) is a monogenic condition caused by mutations unrelated to integrase function. DTG has no known mechanism to modify or treat it.

**Recommendation: Hold — do not pursue. Flag the neural tube defect signal prominently in any safety review.**

---

## Safety Considerations

No structured safety data (warnings, contraindications, or drug interactions) was available in this evidence package.

> Please refer to the approved Summary of Product Characteristics (SmPC) for **Tivicay®** and **Triumeq®** (available via the [EMA product page](https://www.ema.europa.eu)) for complete safety information. Key areas to review include: neural tube defect risk with periconceptional exposure, hypersensitivity reactions (particularly in patients with HLA-B\*57:01 for abacavir-containing combinations), hepatotoxicity in patients with underlying liver disease, and drug–drug interactions via UGT1A1/CYP3A4 induction (e.g. rifampicin, carbamazepine, St John's Wort).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction of SIV infection as a "new indication" is mechanistically sound — SIV integrase is highly homologous to HIV-1 integrase, and DTG's activity in NHP models is well established across multiple independent publications. However, SIV infection is a pre-clinical *research model*, not a human clinical indication. There is no new repurposing opportunity here that requires action from Danish healthcare professionals; this prediction confirms existing, well-validated cross-species pharmacology.

---

**Priority actions — before any further evaluation:**

- **Resolve the Denmark market data gap**: Confirm EMA centralised authorisation status for Tivicay® and Triumeq® with Lægemiddelstyrelsen and update the national registry accordingly. This is a critical correction as the current dataset incorrectly implies DTG is unavailable in Denmark.
- **Restore the original indication**: Add HIV-1 infection as the documented original indication (FDA-approved August 2013; EMA-approved January 2014) so that downstream TxGNN analyses are not distorted by the empty field.
- **Periconceptional safety documentation**: Ensure the neural tube defect risk signal (Zash et al., *NEJM*) is explicitly flagged in all patient-facing prescribing materials for women of reproductive age.

**To proceed with the secondary FIV indication (veterinary research only):**

- Commission feline-specific pharmacokinetic studies (dose optimisation for domestic cats)
- Obtain DTG in vitro IC₅₀ data against FIV integrase directly
- Standard veterinary research ethics approval — no human regulatory pathway required

---

*This report is intended for research reference only and does not constitute medical advice. All drug repurposing candidates require clinical validation before application. This report was generated by the DkTxGNN drug repurposing research system (data cutoff: 2026-04-05).*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

