---
layout: default
title: Alpelisib
parent: 僅模型預測 (L5)
nav_order: 27
evidence_level: L5
indication_count: 10
---

# Alpelisib
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

# Alpelisib: From Breast Cancer to Pulmonary Hypertension

## One-Sentence Summary

Alpelisib (Piqray) is a selective PI3Kα inhibitor approved internationally for PIK3CA-mutated, hormone receptor-positive/HER2-negative advanced or metastatic breast cancer, though it holds no marketing authorisation in Denmark.
The TxGNN model predicts it may be effective for **pulmonary hypertension** with a prediction score of 99.03%; however, existing clinical and preclinical evidence primarily documents **adverse pulmonary and cardiac effects** rather than therapeutic benefit, and no supportive trials for this indication have been identified.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Denmark; known internationally for PIK3CA-mutated HR+/HER2− advanced/metastatic breast cancer |
| Predicted New Indication | Pulmonary Hypertension |
| TxGNN Prediction Score | 99.03% |
| Evidence Level | L4 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known information, Alpelisib is a selective PI3Kα (phosphoinositide 3-kinase alpha) inhibitor that targets the PI3K/Akt/mTOR signalling cascade. Its efficacy in PIK3CA-mutated HR+/HER2− breast cancer has been established clinically, and it acts by blocking aberrant PI3Kα-driven cellular proliferation and survival.

The theoretical basis for the pulmonary hypertension (PAH) prediction rests on the established role of the PI3K/Akt/mTOR pathway in vascular smooth muscle cell (VSMC) proliferation and endothelial dysfunction — two key drivers of pulmonary arterial remodelling in PAH. In principle, selective PI3Kα inhibition could attenuate the pathological narrowing of pulmonary vasculature.

However, the available evidence presents a critical concern that directly undermines this hypothesis: rather than therapeutic benefit, existing data document **adverse effects in the cardiopulmonary system**. A clinical case report records Alpelisib-induced interstitial lung disease (PMID 35730191), and a preclinical mechanistic study shows that PI3Kα pathway inhibition in combination with doxorubicin produces biventricular atrophy and right ventricular dysfunction (PMID 31039672). These findings strongly suggest that PI3Kα inhibition may be **harmful** in patients with pre-existing pulmonary vascular disease, and the repurposing hypothesis has not been validated in any clinical setting.

---

## Clinical Trial Evidence

> **Note:** The one clinical trial retrieved for this indication — [NCT06705504](https://clinicaltrials.gov/study/NCT06705504) — was assessed as **not relevant** (Relevance Grade C). It is a real-world retrospective cohort study of **ribociclib** (not alpelisib) in HR+/HER2− breast cancer patients and has no connection to pulmonary hypertension. Its inclusion represents a search result mismatch and it should not be counted as supporting evidence for this indication.

**Currently no relevant clinical trials for alpelisib in pulmonary hypertension have been identified.**

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [35730191](https://pubmed.ncbi.nlm.nih.gov/35730191/) | 2023 | Case Report | J Oncol Pharm Pract | Alpelisib-induced interstitial lung disease in an advanced breast cancer patient — documents pulmonary **toxicity**, not therapeutic benefit in PAH |
| [31039672](https://pubmed.ncbi.nlm.nih.gov/31039672/) | 2019 | Pre-clinical / Mechanistic Study | J Am Heart Assoc | PI3Kα pathway inhibition combined with doxorubicin causes biventricular atrophy and right ventricular dysfunction — suggests PI3Kα inhibition may be **cardiotoxic**, particularly relevant to right heart function in PAH |

> **Critical interpretation:** Both publications document adverse or potentially harmful signals for the cardiopulmonary system. Neither supports alpelisib as a treatment for pulmonary hypertension. The retrieved evidence argues **against** rather than in favour of this repurposing hypothesis.

---

## Denmark Market Information

Alpelisib is currently **not marketed in Denmark**. The Laegemiddelstyrelsen records no active national or centralised marketing authorisations for this product.

For contextual reference, Alpelisib (Piqray, Novartis) holds regulatory approval from the EMA and FDA for PIK3CA-mutated HR+/HER2− advanced or metastatic breast cancer in combination with fulvestrant. Any future repurposing use in Denmark would require either a new marketing authorisation, compassionate use, or named-patient access via the Laegemiddelstyrelsen.

---

## Cytotoxicity

Alpelisib meets the criteria for inclusion of this section: it is a targeted antineoplastic agent (PI3Kα inhibitor) approved for oncological use in breast cancer.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — selective PI3Kα (PIK3CA) inhibitor |
| Myelosuppression Risk | Low for conventional myelosuppression; haematological monitoring still recommended |
| Emetogenicity Classification | Low to moderate (oral targeted agent) |
| Monitoring Items | **Blood glucose** (hyperglycaemia is a prominent class effect of PI3K inhibitors; fasting plasma glucose should be monitored before initiation and throughout treatment), liver function tests, renal function, CBC with differential, pulmonary symptoms |
| Handling Protection | Standard oral cytotoxic handling precautions apply; follow institutional and national cytotoxic drug handling guidelines |

---

## Safety Considerations

Full Danish SmPC warnings and contraindications data are not available in this Evidence Pack. Please refer to the approved EMA Summary of Product Characteristics (SmPC) for Piqray for comprehensive safety information.

**Clinically relevant signals identified in this evidence review:**

- **Pulmonary toxicity:** A case report documents Alpelisib-induced interstitial lung disease (PMID 35730191). This is directly relevant to the predicted indication and represents a significant safety concern for use in patients with pulmonary disease.
- **Cardiac toxicity:** Preclinical data (PMID 31039672) indicate that PI3Kα inhibition may cause biventricular atrophy and right ventricular dysfunction — this is particularly concerning in patients with pulmonary hypertension, who already carry right ventricular strain.
- **Hyperglycaemia:** PI3Kα inhibition disrupts insulin signalling; hyperglycaemia and diabetes mellitus are well-recognised class effects requiring proactive glucose management.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No direct clinical evidence supports alpelisib as a therapeutic option for pulmonary hypertension. Critically, the only retrieved evidence documents cardiopulmonary **harm** — including Alpelisib-induced interstitial lung disease and preclinical right ventricular dysfunction following PI3Kα inhibition — which directly contradicts the repurposing hypothesis and raises a patient safety concern in a population with pre-existing cardiopulmonary compromise.

**To proceed, the following is needed:**

- Retrieval and review of the complete EMA SmPC (Piqray) for full safety, contraindication, and warning data, including updated pulmonary and cardiac safety data from post-marketing surveillance
- Detailed mechanism of action profile from DrugBank (DB12015) to complete the mechanistic assessment
- Dedicated preclinical studies evaluating alpelisib in validated animal models of pulmonary arterial hypertension (e.g., monocrotaline or SU5416/hypoxia rat models)
- Resolution of the adverse signal: systematic review of alpelisib-associated pneumonitis and cardiotoxicity incidence to determine whether a therapeutic window exists
- Drug-drug interaction assessment with established PAH therapies (endothelin receptor antagonists, PDE5 inhibitors, prostacyclin analogues, soluble guanylate cyclase stimulators)
- Clarification of whether Alpelisib's oral availability and systemic PI3Kα inhibition at clinically achievable concentrations could even reach the pulmonary vasculature at levels relevant to PAH pathophysiology

> *This report is for research purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before any therapeutic application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

