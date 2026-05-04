---
layout: default
title: Anakinra
parent: 僅模型預測 (L5)
nav_order: 37
evidence_level: L5
indication_count: 10
---

# Anakinra
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

# Anakinra: From Rheumatoid Arthritis to Autosomal Recessive Familial Mediterranean Fever

---

## One-Sentence Summary

Anakinra (Kineret) is a recombinant human interleukin-1 receptor antagonist (IL-1Ra), primarily known for treating rheumatoid arthritis and other autoinflammatory conditions such as Still's disease.
The TxGNN model predicts it may be effective for **autosomal recessive familial Mediterranean fever (FMF)**, with **0 clinical trials** and **20 publications** currently supporting this direction.

> **Note on prediction ranking:** The TxGNN model's highest-ranked predictions (extracutaneous mastocytoma, score 99.93%; hepatic infarction, score 99.89%) have no supporting clinical or preclinical evidence (Evidence Level L5, recommendation: Hold) and are therefore not the primary focus of this report. The FMF indication (rank 5–6, score 99.89%) carries the strongest mechanistic rationale and literature support (L3) and is selected as the primary subject for clinical evaluation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Rheumatoid arthritis; autoinflammatory conditions including Still's disease (approved in EU via EMA centralised procedure; no Danish marketing authorisation on record) |
| Predicted New Indication | Autosomal recessive familial Mediterranean fever (FMF) |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L3 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data was not available in the submitted Evidence Pack. Based on established pharmacological knowledge, Anakinra is a recombinant, non-glycosylated form of the naturally occurring human IL-1 receptor antagonist. It competitively binds to the IL-1 type I receptor (IL-1RI), blocking the biological activity of both IL-1α and IL-1β and thereby dampening downstream NF-κB-mediated inflammatory signalling. This makes Anakinra a direct, upstream suppressor of the IL-1 pathway.

Familial Mediterranean Fever is a hereditary autoinflammatory disease caused by mutations in the *MEFV* gene encoding pyrin — a central regulator of inflammasome activity. Abnormal pyrin function leads to uncontrolled caspase-1 activation and excessive IL-1β secretion, which drives the characteristic self-limiting but recurrent attacks of fever, peritonitis, pleuritis, and arthritis. Because Anakinra acts precisely at the IL-1 receptor to block this pathway, the mechanistic alignment with FMF is exceptionally high. This is not merely theoretical: the related drug canakinumab (an anti-IL-1β monoclonal antibody targeting the same cytokine axis) is already approved for FMF in the EU, directly validating IL-1 blockade as an effective treatment strategy.

The published literature consistently documents Anakinra's clinical utility in colchicine-resistant FMF — a population estimated at 5–10% of all FMF patients where there is an unmet medical need. Case reports and case series describe successful control of recurrent attacks, and notably, remarkable improvement in patients with the most severe complication of FMF: systemic AA amyloidosis with renal failure. Multiple treatment reviews and biological therapy guidelines for periodic fever syndromes cite Anakinra as a recommended option for this population, reinforcing the clinical plausibility of this TxGNN prediction.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Anakinra in autosomal recessive familial Mediterranean fever.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [21277619](https://pubmed.ncbi.nlm.nih.gov/21277619/) | 2011 | Case Series + Review | Semin Arthritis Rheum | IL-1 targeting drugs including Anakinra in FMF; functional studies link pyrin to IL-1 maturation; positions IL-1Ra as a rational therapeutic approach |
| [19033248](https://pubmed.ncbi.nlm.nih.gov/19033248/) | 2009 | Clinical Report | Nephrol Dial Transplant | Successful Anakinra treatment of colchicine-resistant FMF with AA amyloidosis; documents outcome after subsequent renal transplantation |
| [21931121](https://pubmed.ncbi.nlm.nih.gov/21931121/) | 2012 | Clinical Report | Nephrol Dial Transplant | Dramatic beneficial effect of IL-1 inhibitor (Anakinra) in FMF complicated with amyloidosis and renal failure; proteinuria reversal documented |
| [20386914](https://pubmed.ncbi.nlm.nih.gov/20386914/) | 2012 | Case Report | Rheumatol Int | Efficacy of Anakinra in a colchicine-resistant FMF patient with secondary AA amyloidosis; attack frequency markedly reduced |
| [23928237](https://pubmed.ncbi.nlm.nih.gov/23928237/) | 2013 | Case Report | Joint Bone Spine | Anakinra successfully treated FMF-associated myositis and spondyloarthritis refractory to colchicine |
| [23322405](https://pubmed.ncbi.nlm.nih.gov/23322405/) | 2013 | Treatment Review | Clin Rev Allergy Immunol | Comprehensive review of IL-1β biological treatment in FMF; Anakinra and canakinumab both reviewed with clinical data |
| [23867542](https://pubmed.ncbi.nlm.nih.gov/23867542/) | 2014 | Treatment Review | Clin Pharmacol Ther | Novel therapeutics for FMF from colchicine to biologics; Anakinra positioned as emerging alternative for colchicine non-responders |
| [28585601](https://pubmed.ncbi.nlm.nih.gov/28585601/) | 2017 | Case Series | JPMA | Anakinra and canakinumab used in four colchicine-resistant paediatric FMF patients; all successfully treated, including three siblings |
| [34550430](https://pubmed.ncbi.nlm.nih.gov/34550430/) | 2022 | Clinical Study | Rheumatol Int | Real-life canakinumab use in FMF resistant or intolerant to colchicine and/or Anakinra; confirms central role of IL-1 pathway across the drug class |
| [26572612](https://pubmed.ncbi.nlm.nih.gov/26572612/) | 2016 | Treatment Review | Curr Med Chem | Comprehensive review of biologics in FMF; Anakinra reviewed alongside other IL-1 inhibitors as effective rescue therapy |

---

## Denmark Market Information

Anakinra is not currently marketed in Denmark. No national or centralised marketing authorisations are recorded in this dataset.

> **Clarification for clinical practice:** Kineret (anakinra) holds an EMA centralised marketing authorisation (EU/1/02/203) valid across all EU member states including Denmark. The discrepancy with the "not marketed" status may reflect local distribution or active marketing arrangements rather than absence of regulatory approval. Healthcare professionals should verify current availability, approved indications, and reimbursement status directly through the Danish Medicines Agency (Lægemiddelstyrelsen) or the EMA product database prior to prescribing.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

> Anakinra belongs to the class of biological IL-1 inhibitors. As a class, these agents are associated with an increased risk of serious infections (including opportunistic infections), injection-site reactions, and potential immunosuppression-related adverse effects. Concomitant use with TNF-inhibitors or other biologics requires particular caution. Formal safety data from the SmPC should be reviewed for any FMF-specific use scenario, particularly in patients with renal impairment (relevant to FMF-associated amyloidosis).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Anakinra's mechanism as an IL-1 receptor antagonist is directly congruent with the core IL-1β-driven pathophysiology of FMF, and multiple published case reports and clinical series specifically document its efficacy in colchicine-resistant FMF — including patients with severe amyloid complications. The related IL-1 inhibitor canakinumab is already EMA-approved for FMF, providing strong class-level validation of this therapeutic approach.

**To proceed, the following is needed:**

- **Verify Danish market access:** Confirm current availability and reimbursement status of Kineret via Lægemiddelstyrelsen, as the drug holds EMA authorisation but is listed as "not marketed" in the current dataset
- **Confirm indication scope:** Determine whether Anakinra's current EMA-approved SmPC covers FMF explicitly, or whether use in FMF constitutes off-label prescribing requiring a dedicated approval pathway
- **Retrieve full SmPC safety data:** Obtain TFDA/EMA SmPC to assess contraindications, warnings, and drug interactions — this data was absent from the Evidence Pack (Data Gap DG001)
- **Obtain detailed MOA data:** Retrieve from DrugBank or EMA product documentation to support regulatory and mechanistic filings (Data Gap DG002)
- **Upgrade evidence level:** Current evidence is L3 (case reports, observational studies, treatment reviews); at least one prospective randomised controlled trial in FMF would be required to reach L1–L2 before formal guideline inclusion
- **Establish a safety monitoring plan:** Given the IL-1 inhibitor class risk of serious infections and injection-site reactions, a structured monitoring protocol should be defined, particularly for immunocompromised FMF patients with amyloidosis-related renal dysfunction

---

*This report is generated for research purposes only and does not constitute medical advice. All repurposing candidates require clinical validation before therapeutic application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

