---
layout: default
title: Nystatin
parent: 僅模型預測 (L5)
nav_order: 314
evidence_level: L5
indication_count: 10
---

# Nystatin
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

# Nystatin: From Candidiasis to Vulvovaginitis

## One-Sentence Summary

Nystatin is a polyene antifungal antibiotic historically used against *Candida* infections, including oral, cutaneous, and vulvovaginal candidiasis. The TxGNN model predicts it may be effective for **Vulvovaginitis**, a use direction already supported by older clinical literature but with no registered clinical trials — currently **0 clinical trials** and **20 publications** support this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Candidiasis (*Candida* infections) — no official approved-indication text is available in this evidence pack; literature indicates historical use in oral, mucocutaneous, and vulvovaginal candidiasis |
| Predicted New Indication | Vulvovaginitis |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L3 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack (marked as a data gap). Based on established pharmacological knowledge, nystatin belongs to the polyene macrolide antifungal class (the same class as amphotericin B); it binds ergosterol in the fungal cell membrane, forming pores that cause leakage of cellular contents and fungal cell death.

The predicted new indication, vulvovaginitis, overlaps substantially with nystatin's traditional use. The literature included in this evidence pack explicitly documents this: "Nystatin, first introduced in the 1950s for treatment of vulvovaginal candidiasis, has been surpassed by the imidazoles and triazoles as the first choice of treatment" (PMID 1436934). In other words, TxGNN's prediction largely reconstructs a well-established, if now less commonly first-line, historical indication rather than identifying a wholly novel use.

Mechanistically this is plausible: since *Candida albicans* accounts for 85–90% of vulvovaginal candidiasis cases (PMID 25775428, PMID 19454049), and nystatin's antifungal action directly targets *Candida* species, a fungicidal effect in the vaginal mucosa is consistent with its known pharmacology. A rat-model mechanism study in this evidence pack further supports a topical/local mode of action, showing nystatin "enhances the immune response against *Candida albicans* and protects the ultrastructure of the vaginal epithelium" (PMID 30359236). Because current clinical use has shifted toward azole antifungals (largely due to resistance patterns and dosing convenience), nystatin is increasingly discussed as a second-line option for fluconazole-resistant vulvovaginal candidiasis (PMID 39771534).

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39771534](https://pubmed.ncbi.nlm.nih.gov/39771534/) | 2024 | Review | Pharmaceutics | Review of management options for fluconazole-resistant VVC, including boric acid, nystatin, oteseconazole, and ibrexafungerp |
| [25775428](https://pubmed.ncbi.nlm.nih.gov/25775428/) | 2015 | Systematic evidence review | BMJ Clinical Evidence | Vulvovaginal candidiasis is the second most common cause of vaginitis; *C. albicans* causes 85–90% of cases |
| [20406393](https://pubmed.ncbi.nlm.nih.gov/20406393/) | 2011 | Observational (n=287) | Mycoses | Correlated in vitro fluconazole/nystatin susceptibility with clinical outcome in complicated VVC |
| [21774671](https://pubmed.ncbi.nlm.nih.gov/21774671/) | 2011 | Review | J Women's Health | Reviews recurrent VVC management, including non-azole alternatives such as nystatin, amid rising non-albicans resistance |
| [37023426](https://pubmed.ncbi.nlm.nih.gov/37023426/) | 2023 | Comparative clinical study | J Infect Dev Ctries | Compared tea tree oil 5%/10% and nystatin inhibition zones against vaginal *Candida* isolates in pregnancy |
| [30359236](https://pubmed.ncbi.nlm.nih.gov/30359236/) | 2018 | Preclinical (rat model) | BMC Microbiology | Nystatin enhanced mucosal immune response and preserved vaginal epithelial ultrastructure in VVC model |
| [32104010](https://pubmed.ncbi.nlm.nih.gov/32104010/) | 2020 | In vitro | Infect Drug Resist | Nystatin and ZnO nanoparticles downregulated SAP1-3 virulence genes in fluconazole-resistant *C. albicans* |
| [16047929](https://pubmed.ncbi.nlm.nih.gov/16047929/) | 2005 | Clinical study | Ceska Gynekologie | Evaluated combined vaginal nifuratel + nystatin therapy for mixed/miscellaneous vulvovaginitis |
| [1436934](https://pubmed.ncbi.nlm.nih.gov/1436934/) | 1992 | Review | Obstet Gynecol Clin North Am | Documents nystatin's historical (1950s) role as first-line topical therapy for VVC, later surpassed by azoles |
| [12228137](https://pubmed.ncbi.nlm.nih.gov/12228137/) | 2002 | Review | BMJ | General review of vulvovaginal candidiasis diagnosis and treatment |

---

## Denmark Market Information

Nystatin currently has no marketing authorisation registered with the Laegemiddelstyrelsen (Danish Medicines Agency); market status is **not marketed**, with 0 authorisations on record in this evidence pack.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- Nystatin is not currently marketed in Denmark (0 marketing authorisations), and a Blocking-severity data gap exists on SmPC warnings/contraindications, so no safety pre-assessment (S1) can proceed. Evidence for vulvovaginitis is limited to L3 (reviews and observational/preclinical studies) with no registered clinical trials, and largely reconstructs nystatin's known — now second-line — historical use rather than confirming a novel mechanism.

**To proceed, the following is needed:**
- TFDA/SmPC-equivalent warnings, contraindications, and DDI data (currently blocking)
- Confirmed mechanism of action data from DrugBank
- Confirmation of Danish/EU marketing authorisation pathway or import status for nystatin vaginal formulations
- Prospective or comparative clinical evidence (vs. azole antifungals) specific to fluconazole-resistant VVC populations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

