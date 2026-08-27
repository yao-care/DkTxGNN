---
layout: default
title: Rifabutin
parent: 僅模型預測 (L5)
nav_order: 376
evidence_level: L5
indication_count: 10
---

# Rifabutin
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

# Rifabutin: From Mycobacterial Infection to HIV Infectious Disease (TB/MAC Co-Infection Management)

## One-Sentence Summary

> Rifabutin is an antimycobacterial antibiotic (rifamycin class) used in the treatment and prevention of tuberculosis (TB) and *Mycobacterium avium* complex (MAC) infection. The TxGNN model predicts a link to **HIV infectious disease**, with **39 clinical trials** and **20 publications** identified — however, the underlying evidence shows this reflects rifabutin's established role in managing TB/MAC co-infection in HIV-positive patients, not a direct antiretroviral effect. Formal regulatory and safety documentation for Denmark is currently a data gap, limiting readiness for clinical decision-making.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Antimycobacterial antibiotic (tuberculosis / *M. avium* complex prophylaxis and treatment) — inferred from drug class and trial context; approved indication text not available in Danish registration data |
| Predicted New Indication | HIV infectious disease *(see caveat below — actual evidence supports TB/MAC co-infection management, not direct anti-HIV activity)* |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L2 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for rifabutin is not available in this evidence pack. Based on the evidence collected, rifabutin inhibits bacterial DNA-dependent RNA polymerase and has no direct antiretroviral activity — it does not act on HIV itself.

The link to "HIV infectious disease" arises indirectly: HIV-positive patients, especially those with low CD4 counts, are highly susceptible to concurrent tuberculosis and disseminated MAC infection, and rifabutin is a standard antimycobacterial agent for treating and preventing these co-infections. Its favorable pharmacokinetic profile (longer half-life, comparatively less enzyme induction than rifampicin) makes it preferable to rifampicin in patients on protease-inhibitor- or integrase-inhibitor-based antiretroviral therapy (ART), which explains why a large share of the trial evidence focuses on pharmacokinetics and drug-drug interaction (DDI) management rather than direct efficacy against HIV.

**Important caveat:** the TxGNN label "HIV infectious disease" should not be read as an antiviral indication. The clinically accurate framing is "treatment/prevention of TB or MAC co-infection in HIV-positive patients," which is already a well-established, decades-old use rather than a novel repurposing hypothesis.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00002122](https://clinicaltrials.gov/study/NCT00002122) | Phase 3 | Completed | 720 | Randomized study of daily/intermittent azithromycin and rifabutin (alone/combined) for prevention of disseminated MAC in HIV-infected patients |
| [NCT00001047](https://clinicaltrials.gov/study/NCT00001047) | Phase 3 | Completed | 400 | Open-label randomized trial of four regimens (clarithromycin + ethambutol + rifabutin or clofazimine) for treatment of disseminated MAC in AIDS patients |
| [NCT00002101](https://clinicaltrials.gov/study/NCT00002101) | Phase 3 | Completed | 450 | Three-arm trial comparing clarithromycin/ethambutol with rifabutin (two doses) or placebo for MAC bacteremia treatment |
| [NCT00001030](https://clinicaltrials.gov/study/NCT00001030) | Phase 3 | Completed | 1100 | Prospective randomized comparison of clarithromycin vs. rifabutin vs. combination for prevention of MAC bacteremia in advanced HIV |
| [NCT00002080](https://clinicaltrials.gov/study/NCT00002080) | N/A (Treatment IND) | Completed | N/A | Rifabutin provided to HIV-positive patients to prevent/delay MAC infection; characterizes monotherapy safety |
| [NCT00002267](https://clinicaltrials.gov/study/NCT00002267) | N/A | Completed | 750 | Double-blind, placebo-controlled trial of rifabutin monotherapy for prevention of MAC bacteremia in AIDS patients with CD4 ≤200 |
| [NCT00023361](https://clinicaltrials.gov/study/NCT00023361) | N/A (TBTC Study 23) | Completed | 215 | Rifabutin-based intermittent regimen for treatment of HIV-related, rifamycin-susceptible tuberculosis; measured treatment failure/relapse rate |
| [NCT00023348](https://clinicaltrials.gov/study/NCT00023348) | Phase 2/3 | Completed | 150 | Pharmacokinetics of intermittent isoniazid and rifabutin in HIV-related TB treatment; correlated PK abnormalities with toxicity |
| [NCT00651066](https://clinicaltrials.gov/study/NCT00651066) | Phase 2 | Completed | 47 | Evaluates rifabutin as a rifampicin substitute for combined TB/HIV treatment in Vietnam; PK with concurrent ART |
| [NCT01059422](https://clinicaltrials.gov/study/NCT01059422) | Phase 4 | Completed | 10 | Raltegravir + 3TC/ABC efficacy and safety in ART-naïve HIV/TB co-infected adults on rifabutin-based first-line anti-TB therapy |

*Note: 39 trials were identified in total; the majority not listed here are single-purpose pharmacokinetic/DDI studies (e.g., interactions with maraviroc, cabotegravir, dolutegravir, indinavir) rather than efficacy trials, and were deprioritized in this table.*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23828580](https://pubmed.ncbi.nlm.nih.gov/23828580/) | 2013 | Cochrane Systematic Review | Cochrane Database Syst Rev | Compares rifamycins (including rifabutin) to isoniazid for TB prevention in people at risk of active TB |
| [40310456](https://pubmed.ncbi.nlm.nih.gov/40310456/) | 2025 | Review | PNAS | Reviews next-generation rifamycins for mycobacterial infections; notes rifamycins induce CYP3A4, complicating co-administration |
| [28233512](https://pubmed.ncbi.nlm.nih.gov/28233512/) | 2017 | Review | Microbiology Spectrum | Describes bidirectional impact of TB and HIV co-infection, underpinning the clinical rationale for rifabutin-based co-treatment |
| [21406051](https://pubmed.ncbi.nlm.nih.gov/21406051/) | 2011 | Review | Infect Disord Drug Targets | Reviews management of adult active TB in the HIV era, including rifamycin–ART drug interactions |
| [33294914](https://pubmed.ncbi.nlm.nih.gov/33294914/) | 2021 | Cohort/PK Study | J Antimicrob Chemother | Rifabutin PK and safety in TB/HIV-coinfected children on lopinavir/ritonavir-based second-line ART |
| [31139825](https://pubmed.ncbi.nlm.nih.gov/31139825/) | 2019 | Cohort | J Antimicrob Chemother | Safety and efficacy of rifabutin in HIV/TB-coinfected children on lopinavir/ritonavir; notes prior study stopped early for neutropenia |
| [25281400](https://pubmed.ncbi.nlm.nih.gov/25281400/) | 2015 | PK Study | J Antimicrob Chemother | Short-term safety and pharmacokinetics of rifabutin with lopinavir/ritonavir in young HIV-infected children |
| [26832753](https://pubmed.ncbi.nlm.nih.gov/26832753/) | 2016 | Population PK Analysis | J Antimicrob Chemother | Pooled population PK/DDI analysis of rifabutin and HIV protease inhibitors to guide dosing in HIV-TB co-treatment |
| [21726477](https://pubmed.ncbi.nlm.nih.gov/21726477/) | 2009 | Review | BMJ Clinical Evidence | Reviews treatment approaches for tuberculosis in people with HIV |
| [7736687](https://pubmed.ncbi.nlm.nih.gov/7736687/) | 1995 | PK Review | Clinical Pharmacokinetics | Early review establishing rifabutin's clinical effectiveness for MAC prophylaxis in HIV-positive patients with low CD4 counts |

*Note: 20 publications were identified in total; several additional PK/DDI studies (with tenofovir alafenamide, dolutegravir, saquinavir, methadone, etc.) were not included above to keep the table to the 10 most clinically relevant entries.*

---

## Denmark Market Information

No marketing authorisation is currently registered for rifabutin in Denmark (0 licenses on file; market status: not marketed). No national (Laegemiddelstyrelsen) or centralised (EMA) authorisation records are available in this evidence pack.

---

## Safety Considerations

- **Regulatory Safety Data Gap:** No structured warnings, contraindications, or DDI database records are currently available for rifabutin. Please refer to the approved Summary of Product Characteristics (SmPC) for authoritative safety information once available.
- **Known Drug-Drug Interaction Burden (from evidence review):** Rifabutin is a CYP3A4 inducer/substrate with extensively documented pharmacokinetic interactions with protease inhibitors, NNRTIs, and integrase inhibitors (e.g., dolutegravir, cabotegravir, indinavir, darunavir/ritonavir), generally requiring dose adjustment when co-administered with ART. This DDI pattern is a dominant theme across the identified trial evidence, even though the formal DDI query in this evidence pack returned no records.
- **Adverse Drug Reaction Signal — Ocular Inflammation:** Literature review (PMID 17353948) identifies rifabutin as a drug associated with drug-induced ocular inflammation, including uveitis and conjunctival involvement, particularly at higher doses or when combined with clarithromycin or fluconazole. A related case report (rifabutin-associated uveitis in a pediatric HIV patient) reinforces this signal.
- **Adverse Drug Reaction Signal — Neutropenia in Pediatric Co-Treatment:** Cohort studies (PMID 33294914, PMID 31139825) report treatment-limiting neutropenia in children receiving rifabutin with protease-inhibitor-based ART, warranting hematological monitoring in this population.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple completed Phase 3 randomized trials and a Cochrane systematic review support rifabutin's established role in preventing and treating TB/MAC co-infection in HIV-positive patients, but this evidence is indirect with respect to the TxGNN label "HIV infectious disease" — rifabutin has no direct antiviral mechanism, and the label should be clinically reframed as "management of TB/MAC co-infection in HIV." Combined with the current absence of Danish regulatory and safety documentation (market status: not marketed, 0 authorisations), this supports a guarded pathway rather than an unqualified "Go."

**To proceed, the following is needed:**
- SmPC/label warnings and contraindications from a reference regulatory source (currently a Blocking data gap; required before any S1 safety pre-assessment)
- Formal mechanism-of-action documentation from DrugBank or equivalent (currently a High-severity data gap)
- A structured DDI review focused on ART co-administration (protease inhibitors, NNRTIs, integrase inhibitors), given the strong CYP3A4-mediated interaction signal already evident in the literature
- A monitoring plan addressing the identified ocular inflammation and pediatric neutropenia ADR signals
- Reframing of the target indication from "HIV infectious disease" to "TB/MAC co-infection in HIV-positive patients" to avoid clinical misinterpretation as an antiretroviral therapy
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

