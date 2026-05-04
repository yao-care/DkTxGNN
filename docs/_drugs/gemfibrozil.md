---
layout: default
title: Gemfibrozil
parent: 僅模型預測 (L5)
nav_order: 207
evidence_level: L5
indication_count: 10
---

# Gemfibrozil
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

# Gemfibrozil: From Dyslipidaemia to Rheumatoid Arthritis

## One-Sentence Summary

Gemfibrozil is a fibric acid derivative (fibrate) classically used for the management of hypertriglyceridaemia and mixed dyslipidaemia.
The TxGNN model predicts it may be effective for **Rheumatoid Arthritis**, with **0 clinical trials** and **4 publications** — primarily animal model and mechanistic studies — currently supporting this direction.
Notably, two additional predicted indications (HIV-associated dyslipidaemia and hypoalphalipoproteinemia) carry substantially stronger clinical evidence (Evidence Level L2) and are summarised in the Conclusion section.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypertriglyceridaemia and mixed dyslipidaemia |
| Predicted New Indication | Rheumatoid Arthritis |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L4 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Gemfibrozil is a PPARα (peroxisome proliferator-activated receptor alpha) agonist of the fibric acid class. Its primary pharmacological action involves activating PPARα in the liver, which promotes fatty acid β-oxidation, reduces VLDL-triglyceride synthesis, and upregulates ApoA-I/ApoA-II to raise HDL-cholesterol — the mechanism underlying its established use in dyslipidaemia. Detailed DrugBank mechanism of action data was not available for this evidence pack and should be retrieved to complete the mechanistic analysis.

The biological rationale for Gemfibrozil in rheumatoid arthritis rests on the well-characterised anti-inflammatory properties of PPARα activation. PPARα agonism suppresses the NF-κB signalling pathway, thereby downregulating key pro-inflammatory cytokines including IL-6, TNF-α, and IL-1β — the same targets addressed by current RA biologic therapies. The PPARα/γ axis also influences T-cell differentiation, including Foxp3⁺ regulatory T cell (Treg) activity, and has been implicated in the modulation of synovial inflammation, providing a mechanistically plausible immune-metabolic link to RA pathophysiology.

Current preclinical evidence is promising but limited: a 2019 rat adjuvant-induced arthritis study demonstrated that Gemfibrozil combined with reduced-dose prednisolone achieved disease control comparable to full-dose steroids (PMID 30074417), and a 2026 experimental study confirmed that the structurally related pan-PPAR agonist bezafibrate attenuates experimental RA via PPARγ-dependent inflammatory modulation (PMID 41207105). Critically, this evidence reflects a fibrate class effect rather than Gemfibrozil-specific data, and no human clinical trials in RA have been conducted to date.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [30074417](https://pubmed.ncbi.nlm.nih.gov/30074417/) | 2019 | Animal Study | Modern Rheumatology | Gemfibrozil (30 mg/kg) combined with low-dose prednisolone achieved comparable arthritis control to full-dose steroids in a rat adjuvant-induced arthritis (AIA) model; direct preclinical evidence for Gemfibrozil in inflammatory arthritis |
| [41207105](https://pubmed.ncbi.nlm.nih.gov/41207105/) | 2026 | Animal Study | International Immunopharmacology | Pan-PPAR agonist bezafibrate (fibrate class) attenuates experimental RA via PPARγ-dependent downregulation of inflammatory pathways; supports fibrate class effect as anti-arthritic mechanism |
| [20083653](https://pubmed.ncbi.nlm.nih.gov/20083653/) | 2010 | Basic Research | Journal of Immunology | MBP priming reduces Foxp3 expression in T cells via nitric oxide; provides mechanistic context for PPAR/Treg axis relevance in autoimmune disease |
| [18039017](https://pubmed.ncbi.nlm.nih.gov/18039017/) | 2007 | Review/Case Series | Am J Clin Dermatology | Review of palmar erythema as secondary manifestation of systemic conditions including RA; peripheral relevance to RA as a systemic inflammatory disease |

---

## Denmark Market Information

Gemfibrozil currently holds **no marketing authorisations in Denmark**. Neither national authorisation via the Danish Medicines Agency (Lægemiddelstyrelsen) nor centralised authorisation via the EMA has been issued.

Gemfibrozil (brand name Lopid®) is authorised and actively marketed in several countries including the United States (FDA-approved) and the United Kingdom. Should clinical use in Denmark be considered, a special access pathway — such as named-patient use or hospital exemption — would be required.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for complete safety information.

> **Clinically relevant safety signals identified from the evidence literature (not from formal safety data fields):**
>
> - **Statin–Gemfibrozil combination risk**: A case of fatal rhabdomyolysis following cerivastatin–gemfibrozil co-administration in an HIV patient has been reported (PMID 11371708). The statin–fibrate combination is a well-established contraindication concern.
> - **Protease inhibitor DDI**: NCT00474201 was specifically designed to evaluate whether lopinavir/ritonavir reduces Gemfibrozil plasma levels via CYP2C8/OATP interaction. Clinicians managing HIV patients on protease inhibitors should be aware of this pharmacokinetic interaction.

---

## Conclusion and Next Steps

**Decision: Hold** (for Rheumatoid Arthritis as the primary TxGNN-predicted indication)

**Rationale:**
Evidence for Gemfibrozil in RA is confined to animal models and fibrate class-effect preclinical data; no human clinical trials have been initiated, and the drug is not marketed in Denmark, creating both an efficacy evidence gap and a regulatory access challenge that must be resolved before clinical application.

**To proceed with the RA indication, the following is needed:**
- Complete MOA data from DrugBank (PPARα binding affinity, selectivity versus PPARγ, downstream transcriptional targets)
- Full safety profiling: retrieve the US FDA label or UK SmPC and extract key warnings, contraindications, and drug interaction data
- Drug interaction assessment with common RA co-medications (methotrexate, NSAIDs, JAK inhibitors, and biologics)
- Proof-of-concept in a validated human RA cell or ex vivo synovial tissue model before any clinical study design
- Regulatory pathway assessment for special access in Denmark

---

### Summary of All TxGNN Predicted Indications

| Indication | TxGNN Score | Evidence Level | Decision | Key Note |
|-----------|-------------|---------------|---------|----------|
| Rheumatoid arthritis | 99.90% | L4 | **Hold** | Animal model evidence only; no clinical trials |
| Multiple endocrine neoplasia | 99.83% | L5 | **Hold** | Model prediction only; no biological plausibility supported |
| HIV infectious disease | 99.80% | L2 | **Research Question** | 3 trials (PK/DDI focus) + 1 RCT (PMID 12409741); use case is PI-associated hypertriglyceridaemia, not antiviral; critical DDI risk with PIs |
| Hypoalphalipoproteinemia | 99.77% | L2 | **Proceed with Guardrails** | 2 RCTs + multiple clinical studies; closely aligned with established Gemfibrozil pharmacology; strongest near-term candidate |
| Brachydactyly-syndactyly syndrome | 99.77% | L5 | **Hold** | Model prediction only; no mechanistic or clinical basis |

> **Clinical prioritisation note:** Of the five predicted indications, **hypoalphalipoproteinemia** (low HDL-cholesterol) has the most robust clinical evidence and the closest mechanistic alignment with Gemfibrozil's known PPARα-mediated upregulation of ApoA-I/ApoA-II and HDL-raising effect. If a repurposing or expanded-use case is to be pursued, this indication represents the lowest-risk, highest-evidence entry point. The **HIV-associated dyslipidaemia** indication also has an RCT-level evidence base (PMID 12409741) but requires a thorough DDI safety assessment before any recommendation can be issued.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

