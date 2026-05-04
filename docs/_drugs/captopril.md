---
layout: default
title: Captopril
parent: 僅模型預測 (L5)
nav_order: 90
evidence_level: L5
indication_count: 8
---

# Captopril
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

# Captopril: From Hypertension to Malignant Renovascular Hypertension

## One-Sentence Summary

Captopril is a first-generation angiotensin-converting enzyme (ACE) inhibitor, long established in global clinical practice for hypertension, chronic heart failure, and diabetic nephropathy.
The TxGNN model predicts it may be effective for **malignant renovascular hypertension** — and the closely related **malignant hypertensive renal disease** — with an identical TxGNN score of **99.28%** for both indications.
No registered clinical trials have evaluated this repurposing direction, but **20 publications** across case series, clinical studies, and mechanistic literature currently support the renovascular indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension / heart failure (no Danish Marketing Authorisation on record; original indication data not available in this pack) |
| Predicted New Indication | Malignant Renovascular Hypertension |
| TxGNN Prediction Score | 99.28% |
| Evidence Level | L3 (malignant renovascular hypertension) / L4 (malignant hypertensive renal disease) |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Formal mechanism of action data was not retrievable for this Evidence Pack. Based on established pharmacology, captopril blocks angiotensin-converting enzyme (ACE), preventing the conversion of angiotensin I to angiotensin II (Ang II). By reducing circulating Ang II, captopril lowers systemic vascular resistance, suppresses aldosterone-driven sodium retention, and — critically for renal involvement — reduces intraglomerular pressure by relaxing the efferent arteriole. This nephroprotective mechanism underpins its long-established role in hypertensive renal damage and diabetic nephropathy.

Malignant renovascular hypertension and malignant hypertensive renal disease share a common pathophysiology: pathological overactivation of the renin-angiotensin-aldosterone system (RAAS). In renovascular disease, renal artery stenosis or renin-secreting tumours drive excess renin release → Ang II accumulation → explosive blood pressure rise → end-organ damage (kidneys, retina, brain). Captopril targets this cascade at its core enzymatic step, making it one of the most mechanistically direct pharmacological interventions available. The TxGNN knowledge graph assigns identical scores of 99.28% to both RAAS-driven renal indications, strongly supporting this link.

One critical safety caveat defines the guardrails: in patients with bilateral renal artery stenosis or a solitary functioning kidney, blocking Ang II removes the compensatory efferent arteriolar tone that sustains glomerular filtration pressure. This can precipitate acute, potentially irreversible renal failure. Patient selection and mandatory pre-treatment imaging are the central conditions for safe use in this setting.

---

## Clinical Trial Evidence

Currently no related clinical trials registered (search conducted 2026-03-26 across ClinicalTrials.gov and WHO ICTRP for both malignant hypertensive renal disease and malignant renovascular hypertension).

---

## Literature Evidence

Ten publications selected from 20 retrieved papers on malignant renovascular hypertension, ranked by direct therapeutic relevance to captopril:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [6145432](https://pubmed.ncbi.nlm.nih.gov/6145432/) | 1984 | Clinical Study (Non-RCT) | Biulleten' Vsesoiuznogo kardiologicheskogo | Direct clinical evaluation of captopril in arterial hypertension with both stable and malignant course |
| [232024](https://pubmed.ncbi.nlm.nih.gov/232024/) | 1979 | Clinical Study | Clinical Science | Captopril induced reactive hyper-reninaemia in 43 of 44 patients with renovascular hypertension; diastolic BP reductions confirmed pharmacological response |
| [3928961](https://pubmed.ncbi.nlm.nih.gov/3928961/) | 1985 | Case Report | Klinische Wochenschrift | Captopril used as antihypertensive in neurofibromatosis with bilateral renal artery stenosis and aortic coarctation; patient refused surgery, BP controlled with captopril |
| [2887673](https://pubmed.ncbi.nlm.nih.gov/2887673/) | 1987 | Mechanistic Study | Japanese Heart Journal | Neurohormonal characterisation of benign vs malignant Goldblatt hypertension; elevated Ang II central to malignant phase, supporting RAAS as the primary therapeutic target |
| [8070421](https://pubmed.ncbi.nlm.nih.gov/8070421/) | 1994 | Review | Endocrinology and Metabolism Clinics | Renin-secreting (JGC) tumours: blood pressure consistently drops during ACE inhibitor (captopril) treatment; converts enzyme blockade as diagnostic and therapeutic tool |
| [17008836](https://pubmed.ncbi.nlm.nih.gov/17008836/) | 2006 | Review | Minerva Medica | Clinical concepts of renovascular hypertension; distinguishes renal artery stenosis from renovascular hypertension; RAAS-targeted treatment strategies reviewed |
| [11334320](https://pubmed.ncbi.nlm.nih.gov/11334320/) | 2001 | Case Report + Review | Clinical Nephrology | Two NF1 cases with renovascular hypertension; captopril test used to quantify plasma renin activity and guide antihypertensive management |
| [10955932](https://pubmed.ncbi.nlm.nih.gov/10955932/) | 2000 | Case Series | Pediatric Nephrology | 27 paediatric NF1 patients studied with captopril test, Doppler, and angiography; renovascular hypertension prevalence and management described |
| [2040938](https://pubmed.ncbi.nlm.nih.gov/2040938/) | 1991 | Review | The Journal of Pediatrics | Malignant hypertension overview in paediatric population including pathophysiology and pharmacological management approaches |
| [1572120](https://pubmed.ncbi.nlm.nih.gov/1572120/) | 1992 | Case Report | Clinical Nuclear Medicine | Case of malignant hypertension evaluated by captopril renal scintigraphy; illustrates captopril's mechanistic role in RAAS-dependent hypertensive states |

---

## Denmark Market Information

Captopril currently holds **no marketing authorisation** registered with the Danish Medicines Agency (Lægemiddelstyrelsen) as of the data cut-off (2026-04-04). There are no approved products on record.

> Captopril is approved in multiple European countries and has an established EMA-level safety and efficacy profile. Its absence from the Danish regulatory database may reflect historic market withdrawal or non-registration of generic products. Any clinical use in Denmark would require verification of a valid authorisation pathway (e.g., compassionate use, named-patient import, or parallel import licence) through the Lægemiddelstyrelsen.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for complete safety information, as the formal product insert data for this submission was not available in the Evidence Pack.

**Critical safety signals identified from the repurposing rationale:**

- **Bilateral renal artery stenosis / solitary kidney — contraindication**: Captopril removes the compensatory Ang II-mediated efferent arteriolar tone essential for maintaining glomerular filtration pressure. Use in this setting can precipitate acute renal failure. Mandatory renal imaging before initiation is non-negotiable in the renovascular hypertension context.
- **Renal function and electrolyte monitoring**: ACE inhibitors are associated with hyperkalaemia and worsening renal function. Serum creatinine, eGFR, and potassium must be checked at baseline and within 1–2 weeks of initiation.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Captopril's direct pharmacological action on ACE and the RAAS pathway is mechanistically precise for malignant renovascular hypertension — a condition defined by pathological Ang II overproduction. The L3 evidence base (clinical studies, case series, and mechanistic literature) provides sufficient biological plausibility and clinical signal to move forward, provided the bilateral stenosis contraindication is rigorously screened. The related indication of malignant hypertensive renal disease (L4, same TxGNN score) remains a research question until dedicated therapeutic — rather than purely diagnostic — studies are available.

**To proceed, the following is needed:**
- **Renal imaging** (Doppler ultrasonography or CT angiography) to exclude bilateral renal artery stenosis or solitary functioning kidney before any treatment initiation
- **Baseline and follow-up labs**: serum creatinine, eGFR, and potassium at initiation and at 1–2 weeks post-start
- **Safety data gap resolution (DG001)**: obtain and review full SmPC / product insert to confirm the complete contraindication and warning profile (TFDA/EMA source)
- **MOA data gap resolution (DG002)**: formal DrugBank API query to support mechanistic analysis documentation
- **Prospective data collection**: establish a registry or observational study protocol to generate higher-quality clinical evidence (target: L2 or above) specifically for the malignant renovascular hypertension indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

