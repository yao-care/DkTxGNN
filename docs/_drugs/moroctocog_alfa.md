---
layout: default
title: Moroctocog Alfa
parent: 僅模型預測 (L5)
nav_order: 300
evidence_level: L5
indication_count: 10
---

# Moroctocog Alfa
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

# Moroctocog Alfa: From Haemophilia A to Primary Release Disorder of Platelets

## One-Sentence Summary

Moroctocog alfa (DB13999) is a recombinant, B-domain deleted coagulation Factor VIII (rFVIII), established internationally as replacement therapy for Haemophilia A in patients with congenital Factor VIII deficiency.
The TxGNN model predicts it may have utility in **Primary Release Disorder of Platelets** with a prediction score of **99.97%**, yet currently **no directly relevant clinical trials or published literature** support this specific repurposing hypothesis.
The proposed rationale is based on an indirect mechanistic inference, and clinical plausibility has not been independently verified.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Haemophilia A (congenital Factor VIII deficiency — replacement therapy)¹ |
| Predicted New Indication | Primary Release Disorder of Platelets |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L4 (mechanistic/preclinical inference only) |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | **Hold** |

¹ Not registered in Denmark; original indication inferred from drug class (recombinant FVIII) and international regulatory status.

---

## Why is This Prediction Reasonable?

Moroctocog alfa is a recombinant B-domain deleted Factor VIII that functions as a critical cofactor in the intrinsic coagulation pathway. It forms the **tenase complex (FVIIIa–FIXa)** on activated platelet phospholipid surfaces, massively amplifying the generation of thrombin — the central effector of fibrin clot formation. Its established therapeutic role is in Haemophilia A, where endogenous FVIII is absent or severely reduced.

Primary release disorder of platelets refers to a group of inherited or acquired conditions in which platelet dense granules (δ-granules) and/or alpha granules (α-granules) fail to release their stored contents — including ADP, ATP, serotonin, fibrinogen, and von Willebrand factor — upon platelet activation. This secretion defect disrupts the positive feedback amplification loop of platelet recruitment, resulting in impaired primary haemostasis and a clinically significant bleeding tendency. The TxGNN prediction is built on the premise that supplementary FVIII could theoretically compensate by enhancing thrombin generation at residual platelet phospholipid surfaces, partially offsetting the weakened platelet activation signal downstream.

However, this mechanistic link is **highly indirect and clinically unproven**. Moroctocog alfa acts downstream of the granule secretion step — it does not interact with the molecular machinery (SNARE complexes, RAB GTPases, or signalling kinases) responsible for granule exocytosis. Boosting tenase complex activity cannot restore the primary secretion defect. This situation is analogous to providing more fuel to an engine whose spark plugs have failed: the fuel tank is full, but ignition remains impaired. No clinical experience with FVIII administration in platelet release disorders is documented, and the risk-benefit profile in this context is entirely unknown.

---

## Clinical Trial Evidence

> **Important note:** No clinical trials were identified that directly investigate moroctocog alfa or any recombinant FVIII product as a treatment specifically for primary release disorder of platelets. The seven trials retrieved through broad keyword searching all received a relevance grade of **C** (not directly applicable to this repurposing hypothesis) and are listed below for transparency only.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|-----------|--------------|
| [NCT07400848](https://clinicaltrials.gov/study/NCT07400848) | N/A | Recruiting | 200 | Observational study of Post-COVID-19 Vaccination Syndrome (PACVS); assesses multi-system symptoms including fatigue, cardiac and neurological dysfunction. No FVIII intervention — retrieved due to coagulation keyword overlap. |
| [NCT07343687](https://clinicaltrials.gov/study/NCT07343687) | N/A | Not yet recruiting | 80 | Observational study of clinico-haematological and coagulation profiles in newly diagnosed AML patients receiving induction chemotherapy. No FVIII intervention. |
| [NCT01913405](https://clinicaltrials.gov/study/NCT01913405) | Phase 3 | Completed | 30 | Safety and efficacy of PEGylated rFVIII (BAX 855, a distinct product) in previously treated males with severe Haemophilia A undergoing elective surgery. Different product; indication is Haemophilia A, not platelet release disorder. |
| [NCT07329036](https://clinicaltrials.gov/study/NCT07329036) | N/A | Recruiting | 25 | Effect of combined DPMAS and therapeutic plasma exchange (ALSS) on primary coagulation and organ function in acute-on-chronic liver failure. No FVIII supplementation component. |
| [NCT04161495](https://clinicaltrials.gov/study/NCT04161495) | Phase 3 | Completed | 159 | Prophylaxis and on-demand treatment with rFVIIIFc-VWF-XTEN (BIVV001) in previously treated patients ≥12 years with severe Haemophilia A. Different product and indication; shares drug class only. |
| [NCT04759131](https://clinicaltrials.gov/study/NCT04759131) | Phase 3 | Completed | 74 | Safety and efficacy of BIVV001 in previously treated paediatric patients <12 years with severe Haemophilia A. Different product and indication; shares drug class only. |
| [NCT07439939](https://clinicaltrials.gov/study/NCT07439939) | N/A | Recruiting | 45 | Exploratory study of systemic and portal haemostasis during TIPS placement in patients with portal vein thrombosis/cirrhosis. No FVIII intervention. |

---

## Literature Evidence

Currently no related literature is available for moroctocog alfa in primary release disorder of platelets.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although TxGNN assigns a very high algorithmic prediction score (99.97%), the proposed mechanism linking moroctocog alfa to primary release disorder of platelets is highly indirect — FVIII supplementation does not address the underlying granule secretion defect — and no supporting clinical trials or peer-reviewed literature exist for this repurposing hypothesis. The drug is not currently marketed in Denmark, and no authorisations are on record with the Danish Medicines Agency (Lægemiddelstyrelsen) or via centralised EMA procedure in this dataset.

**To proceed, the following is needed:**

- **Regulatory data**: Retrieve the full SmPC/product information including warnings, contraindications, and drug interactions (Data Gap DG001 — currently blocking safety assessment)
- **Mechanism of action data**: Obtain full MOA details from DrugBank API to enable a proper mechanistic rationale analysis (Data Gap DG002)
- **Literature search expansion**: Perform a targeted search for any published case reports, ex vivo studies, or preclinical evidence using FVIII preparations in models of platelet release defects (dense granule or α-granule secretion disorders)
- **Expert consultation**: Engage a specialist in haemostasis and thrombosis to assess the clinical plausibility of FVIII supplementation in this indication before committing research resources
- **Additional predicted indications review**: Among the lower-ranked predictions, **acquired coagulation factor deficiency** (rank 7–8; score 99.88%) carries the strongest mechanistic link in this dataset — particularly the acquired Haemophilia A subtype — and may represent a more scientifically defensible research question if evidence generation is being considered

---

*This report is generated for research purposes only and does not constitute medical advice. All drug repurposing candidates require prospective clinical validation before any therapeutic application. Refer to current SmPC and national guidelines for authorised indications.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

