---
layout: default
title: Alirocumab
parent: 僅模型預測 (L5)
nav_order: 24
evidence_level: L5
indication_count: 10
---

# Alirocumab
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

# Alirocumab: From Familial Hypercholesterolaemia to Cholesterol Catabolic Process Disease

## One-Sentence Summary

Alirocumab (Praluent®) is a fully human anti-PCSK9 monoclonal antibody approved by the FDA (2015) and EMA for the treatment of familial hypercholesterolaemia and cardiovascular risk reduction in adults, though it is not currently registered or marketed in Denmark.
The TxGNN model predicts it may be effective for **Cholesterol Catabolic Process Disease** — a category encompassing disorders of impaired LDL receptor function and deficient LDL-C clearance — with **1 clinical trial** and **19 publications** currently supporting this direction.
This is the highest-evidenced prediction in this Evidence Pack (Evidence Level L1), and the biological rationale is exceptionally strong.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Familial hypercholesterolaemia; cardiovascular risk reduction in high-risk adults (FDA/EMA approved globally; **not registered in Denmark**) |
| Predicted New Indication | Cholesterol Catabolic Process Disease |
| TxGNN Prediction Score | 99.36% |
| Evidence Level | L1 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Proceed with Guardrails |

> **Note on TxGNN rankings:** The highest-scored predictions by raw TxGNN score (ichthyosis X-linked, 99.43%; vitamin/cofactor metabolism disorder, 99.41%) are rated L5 (model prediction only) with no supporting clinical trials or literature, and their mechanistic link to PCSK9 inhibition is biologically implausible. The clinically actionable prediction — cholesterol catabolic process disease — ranks fifth by TxGNN score but is supported by the strongest evidence and the most direct mechanistic link. This report therefore focuses on the L1-evidenced prediction.

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available in the Evidence Pack. Based on published pharmacology, Alirocumab is a fully human IgG1 monoclonal antibody that binds the catalytic domain of PCSK9 (proprotein convertase subtilisin/kexin type 9). By blocking PCSK9's interaction with the EGF-A domain of LDL receptors (LDLR) on hepatocytes, Alirocumab prevents PCSK9-mediated lysosomal degradation of LDLR. The net result is a substantial increase in hepatic LDLR surface density, dramatically enhanced LDL-C clearance from the circulation, and a reduction in plasma LDL-C of approximately 50–60%.

The predicted indication — "cholesterol catabolic process disease" — encompasses disorders where this exact pathway is pathologically disrupted: most notably familial hypercholesterolaemia (FH, caused by loss-of-function mutations in LDLR, APOB, or gain-of-function mutations in PCSK9) and related conditions characterised by impaired cholesterol catabolism. Alirocumab targets the precise molecular mechanism underlying these diseases, making the TxGNN prediction mechanistically self-consistent. This is not a prediction by analogy; it is a direct mechanistic match.

Crucially, Alirocumab already holds regulatory approval from both the FDA and EMA for familial hypercholesterolaemia and high cardiovascular risk, backed by the ODYSSEY clinical trial programme, including the landmark ODYSSEY OUTCOMES Phase 3 RCT (approximately 18,924 participants), which demonstrated significant reductions in recurrent ischaemic cardiovascular events and all-cause mortality. The TxGNN model is, in essence, confirming an established clinical application.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03207945](https://clinicaltrials.gov/study/NCT03207945) | Phase 3 | Completed | 118 | EPIC-HIV Study: PCSK9 inhibition in HIV-positive patients on antiretroviral therapy. Assessed effects on vascular inflammation, endothelial function, and non-calcified coronary plaque — features of a distinct atherosclerotic phenotype in HIV. Directly evaluates PCSK9 inhibitor impact on cholesterol metabolism and cardiovascular risk in a challenging metabolic context. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [36739653](https://pubmed.ncbi.nlm.nih.gov/36739653/) | 2023 | Systematic Review/Meta-analysis | Kardiologia polska | Comprehensive synthesis of evidence for PCSK9 role in LDL metabolism; clinical impact of PCSK9 inhibitors on lipid parameters and cardiovascular risk reduction |
| [38658193](https://pubmed.ncbi.nlm.nih.gov/38658193/) | 2024 | Safety Analysis (ODYSSEY OUTCOMES) | Eur Heart J Cardiovasc Pharmacother | >47,296 patient-years of observation: alirocumab reduces recurrent ischaemic CV events and all-cause death; comprehensive long-term safety profile established |
| [39947256](https://pubmed.ncbi.nlm.nih.gov/39947256/) | 2025 | Mechanistic Review | Pharmacology & Therapeutics | Detailed comparison of extracellular PCSK9 inhibition (alirocumab, evolocumab) vs. hepatic PCSK9 synthesis inhibition (inclisiran); mechanism-specific clinical properties |
| [38277255](https://pubmed.ncbi.nlm.nih.gov/38277255/) | 2024 | Narrative Review | Current Opinion in Lipidology | Update on PCSK9-directed therapies; two landmark cardiovascular outcomes RCTs confirm substantial LDL-C reduction; emerging novel strategies reviewed |
| [38185721](https://pubmed.ncbi.nlm.nih.gov/38185721/) | 2024 | Translational Review | Signal Transduction and Targeted Therapy | Wide-ranging review of PCSK9 biology beyond cardiovascular disease — liver disease, infectious disease, autoimmune disorders, and cancer; highlights emerging repurposing potential |
| [34070931](https://pubmed.ncbi.nlm.nih.gov/34070931/) | 2021 | Mechanistic Review | Int J Mol Sci | PCSK9 biology and its central role in atherothrombosis; 20-year perspective on PCSK9 as a therapeutic target in dyslipidaemia and CVD management |
| [38191052](https://pubmed.ncbi.nlm.nih.gov/38191052/) | 2024 | Research Article | Metabolism: Clinical and Experimental | PCSK9 inhibition prevents and alleviates cholesterol gallstones via PPARα-mediated CYP7A1 activation; novel mechanistic link directly within the cholesterol catabolic pathway |
| [36411665](https://pubmed.ncbi.nlm.nih.gov/36411665/) | 2022 | Safety Review | Biomedicine & Pharmacotherapy | Safety profile of PCSK9 inhibitor class; 43% of statin patients fail to reach LDL-C targets; PCSK9 inhibitors as cornerstone add-on therapy for refractory hypercholesterolaemia |
| [39751968](https://pubmed.ncbi.nlm.nih.gov/39751968/) | 2025 | Review | Current Atherosclerosis Reports | Novel pharmacological approaches for homozygous familial hypercholesterolaemia (HoFH) — the most severe form of cholesterol catabolic disease; treatment challenges and emerging agents |
| [36422206](https://pubmed.ncbi.nlm.nih.gov/36422206/) | 2022 | Literature Review | Medicina (Kaunas) | Familial hypercholesterolaemia: genetics, diagnostics, and treatment including PCSK9 inhibitors; heterozygous FH prevalence 1:200–250 underscores clinical burden |

---

## Denmark Market Information

Alirocumab is **not currently registered or marketed in Denmark**. No marketing authorisations have been granted by the Danish Medicines Agency (Laegemiddelstyrelsen), and no products are listed. Alirocumab (Praluent®) holds a centralised EMA marketing authorisation valid across EU/EEA member states; however, commercial availability in Denmark would require a market launch decision by the marketing authorisation holder (Sanofi/Regeneron).

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for Praluent® (alirocumab) — available via the EMA product database — for full safety information, including warnings, contraindications, and special precautions. No safety data was available in the current Evidence Pack for local regulatory review.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Alirocumab's mechanism of action directly and specifically targets the cholesterol catabolic pathway via PCSK9-mediated LDLR regulation — the precise molecular defect underlying cholesterol catabolic process diseases such as familial hypercholesterolaemia. The drug already holds FDA and EMA approval for this therapeutic area, supported by large Phase 3 RCTs (ODYSSEY programme, up to ~18,924 participants) demonstrating both efficacy and long-term safety. Evidence Level L1 is assigned based on the completed Phase 3 trial identified plus the extensive published literature. The primary barrier to use in Denmark is the absence of a local market authorisation, not a lack of clinical evidence.

**To proceed, the following is needed:**
- Confirm EMA centralised marketing authorisation status for Praluent® and initiate market availability discussions with the marketing authorisation holder for Denmark
- Engage the Danish Medicines Agency (Laegemiddelstyrelsen) regarding reimbursement eligibility under the Danish Medicines Reimbursement Act
- Obtain and review the complete SmPC for Praluent® to document contraindications, warnings, and special populations before any clinical use
- Retrieve full MOA data from DrugBank (currently a data gap) to complete the pharmacological dossier
- Establish a safety monitoring plan covering: lipid panel (LDL-C, HDL-C, total cholesterol, TG), injection site reactions, neurocognitive monitoring per EMA label requirements, and hepatic function
- Consider patient access pathways (e.g., individual named-patient supply or compassionate use) while formal market availability is pursued

---

*This report is generated for research purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before therapeutic application. Always refer to current SmPC and local prescribing guidelines.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

