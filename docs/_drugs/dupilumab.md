---
layout: default
title: Dupilumab
parent: 僅模型預測 (L5)
nav_order: 152
evidence_level: L5
indication_count: 10
---

# Dupilumab
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

# Dupilumab: From Atopic Dermatitis / Type 2 Inflammation to Bronchitis

> ⚠️ **Disclaimer**: This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before application.

---

## One-Sentence Summary

Dupilumab (Dupixent®) is a fully human monoclonal antibody that blocks the IL-4 receptor alpha subunit (IL-4Rα), with established efficacy in Type 2 inflammatory diseases including atopic dermatitis, moderate-to-severe asthma, and chronic rhinosinusitis with nasal polyps. The TxGNN model predicts it may be effective for **Bronchitis**, with **1 clinical trial** and **6 publications** currently supporting this direction. Evidence is primarily mechanistic extrapolation from closely related airway conditions, as no bronchitis-specific Phase 2/3 RCT has been completed to date.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No indication registered in the Danish Medicines Agency (Laegemiddelstyrelsen) dataset; globally established for atopic dermatitis and asthma (EMA-authorised) |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L3 |
| Denmark Market Status | Not marketed (no local authorisations on record) |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Dupilumab is a fully human IgG4 monoclonal antibody that binds the shared alpha subunit of the IL-4 and IL-13 receptors (IL-4Rα), simultaneously blocking downstream JAK-STAT signalling of both cytokines. IL-4 and IL-13 are the principal drivers of Type 2 (Th2) inflammation: they promote IgE class-switching, goblet cell hyperplasia, mucus hypersecretion, and subepithelial fibrosis. This mechanism has been clinically validated in atopic dermatitis, moderate-to-severe eosinophilic asthma, chronic rhinosinusitis with nasal polyps (CRSwNP), prurigo nodularis, and eosinophilic oesophagitis.

Chronic bronchitis — particularly phenotypes with eosinophilic airway inflammation or confirmed Type 2 immune activation — shares precisely this pathophysiological axis. IL-13, in particular, drives mucin overproduction and goblet cell metaplasia in the bronchial mucosa, while IL-4 amplifies Th2 polarisation and eosinophil recruitment. The "united airway" hypothesis positions upper airway sinusitis, nasal polyposis, asthma, and lower airway bronchitis along the same biological continuum, making IL-4Rα blockade mechanistically plausible across all sites. This continuum is supported by the inclusion of CRSsNP (NCT04362501) in the current evidence pack, where Th2 airway inflammation responds to dupilumab despite differing anatomical targets.

However, it is essential to note that mechanistic plausibility does not equate to confirmed clinical benefit. The critical gap is the absence of a Phase 2 or Phase 3 RCT directly enrolling bronchitis patients. Smoker-predominant neutrophilic bronchitis — the most common phenotype — is unlikely to respond to Th2 blockade and was actively excluded from most asthma and CRSsNP dupilumab trials. Patient phenotyping using blood eosinophil count and fractional exhaled nitric oxide (FeNO) will be essential to identify a biologically responsive subpopulation.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT04362501](https://clinicaltrials.gov/study/NCT04362501) | Phase 2 | Completed | 33 | Dupilumab in chronic rhinosinusitis without nasal polyps (CRSsNP). Evaluates clinical effectiveness across Type 2 and non-Type 2 disease endotypes. CRSsNP shares IL-4/IL-13-driven inflammation with bronchitis but involves the upper airway; results provide indirect mechanistic support but cannot be directly extrapolated to bronchitis outcomes. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [30273510](https://pubmed.ncbi.nlm.nih.gov/30273510/) | 2019 | Systematic Review / Meta-Analysis | J Asthma | Pooled analysis of RCTs confirms dupilumab efficacy and safety in uncontrolled asthma; reduced exacerbation rates and improved FEV1. Provides the strongest mechanistic bridge to Type 2 bronchitis. |
| [34597534](https://pubmed.ncbi.nlm.nih.gov/34597534/) | 2022 | RCT Extension | Lancet Respir Med | TRAVERSE study: long-term (>1 year) dupilumab safety and efficacy in moderate-to-severe asthma. Demonstrates sustained reduction in exacerbations and acceptable long-term safety profile. |
| [38488768](https://pubmed.ncbi.nlm.nih.gov/38488768/) | 2024 | Review | Pediatr Pulmonol | Discusses novel therapies for eosinophilic paediatric plastic bronchitis; identifies IL-4/IL-13 blockade as a mechanistically relevant approach, offering the most direct literature link to bronchitis specifically. |
| [32428511](https://pubmed.ncbi.nlm.nih.gov/32428511/) | 2020 | Mechanistic / Imaging Study | Chest | Anti-T2 biologic treatment (dupilumab) improves ventilation defect patterns visualised by inhaled gas MRI in eosinophilic asthma. Demonstrates objective functional improvement in small airway obstruction driven by eosinophilic inflammation. |
| [39904363](https://pubmed.ncbi.nlm.nih.gov/39904363/) | 2025 | Comprehensive Review | Tuberc Respir Dis | Reviews pharmacologic strategies for preventing COPD exacerbations, including novel biologic agents targeting Type 2 pathways; contextualises dupilumab within the broader chronic airway disease treatment landscape. |
| [30196731](https://pubmed.ncbi.nlm.nih.gov/30196731/) | 2018 | Review | Expert Opin Pharmacother | Addresses challenges in treating asthma overlapping with smoking-induced chronic bronchitis and emphysema (asthma-COPD overlap). Highlights that smokers are routinely excluded from biologic trials — a key gap affecting evidence translation to typical bronchitis populations. |

---

## Denmark Market Information

Dupilumab has **no marketing authorisation** recorded in the Danish Medicines Agency (Laegemiddelstyrelsen) registry in this dataset.

> **Important context for clinicians**: Dupilumab (Dupixent®) holds a **centralised EU marketing authorisation** issued by the European Medicines Agency (EMA), valid in all EU/EEA member states including Denmark. Approved indications include moderate-to-severe atopic dermatitis (adults, adolescents, and children ≥6 months), moderate-to-severe asthma with Type 2 inflammation, chronic rhinosinusitis with nasal polyps, prurigo nodularis, and eosinophilic oesophagitis. Healthcare professionals should consult the current **EMA SmPC for Dupixent®** for up-to-date prescribing information and reimbursement status with Sundhedsstyrelsen/Medicinrådet.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

> Specific safety data (key warnings, contraindications, and drug-drug interaction data) were not retrievable from this evidence pack. Based on the drug class (IL-4Rα monoclonal antibody), clinicians should be aware of class-associated considerations including conjunctivitis, injection site reactions, and potential for paradoxical inflammatory responses (e.g., psoriasiform eruptions). Formal SmPC review is required prior to any clinical application.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic rationale for dupilumab in Type 2-phenotype bronchitis is biologically sound and supported by robust data from directly adjacent indications (asthma, CRSsNP). However, no bronchitis-specific Phase 2 or Phase 3 RCT has been completed, and current evidence is rated L3 (mechanistic extrapolation and observational studies only). Clinical translation in a general bronchitis population cannot be recommended without dedicated prospective evidence, particularly given the heterogeneity of bronchitis phenotypes and the limited likelihood of benefit in the neutrophilic/smoking-related majority.

**To proceed, the following is needed:**

- **Phase 2 RCT** targeting bronchitis patients enriched for Type 2 biomarkers (blood eosinophils ≥300 cells/μL or FeNO ≥25 ppb) using validated endpoints (e.g., exacerbation rate, symptom score, sputum eosinophil count)
- **Phenotype stratification strategy**: clearly distinguish eosinophilic bronchitis from neutrophilic/smoking-related bronchitis before enrolment — the current evidence supports only the former
- **SmPC and pharmacovigilance review** for dupilumab in the target bronchitis population, including assessment of any contraindications relevant to comorbid COPD or smoker populations
- **Regulatory and reimbursement pathway assessment** in Denmark via Medicinrådet/Sundhedsstyrelsen, given the off-label nature of this proposed indication
- **Data gap remediation**: obtain the full Dupixent® Danish prescribing information from the EMA/Laegemiddelstyrelsen to enable a complete safety assessment before advancing to clinical studies
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

