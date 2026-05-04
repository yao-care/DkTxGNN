---
layout: default
title: Desmopressin
parent: 僅模型預測 (L5)
nav_order: 137
evidence_level: L5
indication_count: 10
---

# Desmopressin
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

# Desmopressin: From Diabetes Insipidus / Nocturnal Enuresis to Congenital Prothrombin Deficiency

## One-Sentence Summary

Desmopressin (DDAVP) is a synthetic analogue of arginine vasopressin, with established approved indications including central diabetes insipidus and nocturnal enuresis, and well-documented haemostatic use in mild haemophilia A and von Willebrand disease.
The TxGNN model predicts it may also be effective for **Congenital Prothrombin Deficiency** (prediction score 99.70%), with **1 clinical trial** (indirect) and **4 publications** currently identified in support of this direction.
However, direct clinical trial evidence for desmopressin in congenital prothrombin deficiency specifically is absent, and the overall evidence base remains limited to case reports and contextual reviews.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Central diabetes insipidus; nocturnal enuresis (no Denmark marketing authorisation data available in this Evidence Pack) |
| Predicted New Indication | Congenital Prothrombin Deficiency |
| TxGNN Prediction Score | 99.70% |
| Evidence Level | L4 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Detailed mechanism of action data was not returned in this Evidence Pack. Based on well-established pharmacological knowledge, however, desmopressin acts as a selective agonist at the V2 (vasopressin-2) receptor expressed on renal collecting duct cells and vascular endothelial cells. Stimulation of endothelial V2 receptors triggers the rapid exocytosis of Weibel-Palade bodies, releasing stored von Willebrand factor (vWF) and coagulation factor VIII (FVIII) into the systemic circulation. The resulting elevation in vWF and FVIII promotes platelet adhesion to damaged vessel walls and accelerates fibrin clot formation, effectively shortening the bleeding time. This mechanism forms the basis for desmopressin's established haemostatic utility in mild haemophilia A and type 1 von Willebrand disease.

Congenital prothrombin deficiency (hypoprothrombinæmia or dysprothrombinæmia) is a rare autosomal recessive coagulopathy resulting from deficient or dysfunctional Factor II (prothrombin), a central component of the common coagulation pathway. Although desmopressin does not directly replace or upregulate prothrombin, its ability to boost vWF-mediated primary haemostasis and FVIII-dependent secondary haemostasis can provide clinically meaningful adjunctive support in the context of complex or mild-to-moderate coagulation factor deficiencies. Case reports document successful DDAVP use in combined congenital Factor V and Factor VIII deficiency (PMID 2607619) — a phenotype mechanistically adjacent to isolated prothrombin deficiency — lending credibility to the TxGNN prediction.

The knowledge-graph basis for this prediction likely reflects the dense clustering of rare inherited bleeding disorders within the TxGNN network and desmopressin's broad haemostatic connectivity across multiple coagulopathy nodes. The biological plausibility is moderate: desmopressin would function as a haemostatic adjunct rather than a specific replacement therapy, and its benefit would be most expected in mild phenotypes or perioperative settings. Prospective clinical evaluation is required before any clinical translation.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT04567511](https://clinicaltrials.gov/study/NCT04567511) | Phase 4 | Recruiting | 20 | Evaluates emicizumab (Hemlibra) — **not desmopressin** — in mild haemophilia A (FVIII 5–30%); assesses coagulation parameters, joint health, and haemostatic efficacy. Provides indirect context for novel haemostatic agents in rare coagulopathies, but is not directly relevant to desmopressin in congenital prothrombin deficiency. |

> **Important caveat:** No clinical trial investigating desmopressin specifically in congenital prothrombin deficiency was identified. The trial listed above is retrieved as contextual evidence for the broader rare coagulopathy space.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [2607619](https://pubmed.ncbi.nlm.nih.gov/2607619/) | 1989 | Case Report | Rinsho ketsueki (Japanese Journal of Clinical Hematology) | **Most directly relevant.** DDAVP administered to a patient with congenital combined Factor V and Factor VIII deficiency; documents haemostatic response and mechanistic discussion. |
| [1942544](https://pubmed.ncbi.nlm.nih.gov/1942544/) | 1991 | Case Report | Rinsho ketsueki (Japanese Journal of Clinical Hematology) | Perioperative management (caesarean section) in a woman with combined congenital FV/FVIII deficiency using factor VIII concentrates; discusses adjunctive haemostatic strategies in complex congenital coagulopathies. |
| [7684674](https://pubmed.ncbi.nlm.nih.gov/7684674/) | 1993 | Review | Drugs | Systematic review of treatment options for common inherited bleeding disorders; recommends desmopressin for mild haemophilia A and most von Willebrand disease subtypes, and assesses safety, efficacy, and cost. |
| [21115138](https://pubmed.ncbi.nlm.nih.gov/21115138/) | 2011 | Review | Autoimmunity Reviews | Comprehensive overview of acquired haemophilia A (autoantibodies against FVIII); covers diagnosis, clinical spectrum, and treatment options. Provides broader context for FVIII-related coagulopathies and haemostatic management challenges. |

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for full safety information, as warning and contraindication data were not available in this Evidence Pack.

> Based on published literature (PMID 36656570), clinicians should be aware of the following known safety signals for desmopressin:
> - **Hyponatraemia and fluid retention**: Risk increases with high fluid intake, in elderly patients, and with repeated dosing — requires monitoring of serum sodium.
> - **Arterial thrombotic events**: Rare but reported, particularly in patients with pre-existing cardiovascular risk factors.
> - **Drug–drug interactions**: No DDI data was returned in this Evidence Pack; a formal interaction review is required prior to clinical use.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN prediction score (99.70%), no clinical trial directly investigating desmopressin in congenital prothrombin deficiency has been identified, and the available literature is limited to case reports in related (but mechanistically distinct) coagulopathies. Desmopressin has no registered marketing authorisation in Denmark according to available data, and critical safety information (SmPC warnings, contraindications, DDI profile) is currently absent from this Evidence Pack.

**To proceed, the following is needed:**

- **Regulatory verification**: Confirm desmopressin's actual authorisation status in Denmark via the Laegemiddelstyrelsen register and EMA database (Minirin®, Nocdurna®, Octostim® are known trade names in other EU countries)
- **SmPC review**: Retrieve and analyse the full Summary of Product Characteristics for approved indications, warnings, contraindications, and special populations
- **DDI assessment**: Complete a formal drug–drug interaction review (DDI data returned as "not found" in this Evidence Pack)
- **Mechanistic feasibility study**: Evaluate whether desmopressin's vWF/FVIII-releasing mechanism can provide clinically meaningful haemostatic benefit in prothrombin (Factor II) deficiency, which lies downstream in the coagulation cascade
- **Clinical pilot**: Design a prospective case series or n-of-1 studies measuring haemostatic response (e.g., thrombin generation assay, bleeding time, perioperative blood loss) in congenital prothrombin deficiency patients treated with desmopressin
- **Rare disease pathway**: Given the very low prevalence of congenital prothrombin deficiency, assess eligibility for EMA orphan designation to support future development

---

> *This report is generated for research purposes only and does not constitute medical advice. All drug repurposing candidates require prospective clinical validation before therapeutic application. Healthcare professionals should consult the current approved SmPC and applicable clinical guidelines.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

