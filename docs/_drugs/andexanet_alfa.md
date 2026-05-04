---
layout: default
title: Andexanet Alfa
parent: 僅模型預測 (L5)
nav_order: 38
evidence_level: L5
indication_count: 8
---

# Andexanet Alfa
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

# Andexanet Alfa: From Factor Xa Inhibitor Reversal to Glanzmann Thrombasthenia

## One-Sentence Summary

Andexanet Alfa (Ondexxya®) is a recombinant modified human Factor Xa decoy protein approved internationally as a reversal agent for life-threatening or uncontrolled bleeding in patients anticoagulated with direct Factor Xa inhibitors (apixaban, rivaroxaban).
The TxGNN model predicts it may have potential in **Glanzmann Thrombasthenia** (TxGNN score: 99.77%), a rare inherited platelet aggregation disorder — however, the mechanistic analysis in this evidence pack flags this as a **likely false-positive prediction** arising from shared "bleeding disorder" phenotype nodes in the knowledge graph, with **no supporting clinical trials and no supporting literature** identified for this specific indication.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Reversal of anticoagulation by apixaban or rivaroxaban in adults with life-threatening or uncontrolled bleeding |
| Predicted New Indication | Glanzmann Thrombasthenia |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L5 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data was not available in this evidence pack. Based on established pharmacological knowledge, Andexanet Alfa is a catalytically inactive recombinant modified human Factor Xa (FXa) protein. It acts as a competitive decoy by binding and sequestering Factor Xa inhibitors (apixaban, rivaroxaban) circulating in plasma, thereby restoring endogenous thrombin generation. This mechanism operates exclusively within **secondary haemostasis** — specifically the final common coagulation pathway — and has no interaction with platelet biology.

Glanzmann Thrombasthenia, by contrast, is a **primary haemostasis** disorder caused by deficiency or dysfunction of the platelet surface glycoprotein complex GPIIb/IIIa (integrin αIIbβ3). The pathology lies entirely in platelet aggregation failure, and standard treatments are platelet transfusion or recombinant activated Factor VIIa (rFVIIa). These two pathways — FXa inhibitor reversal and GPIIb/IIIa-mediated platelet aggregation — are biochemically independent with no known crossover points.

The mechanistic rationale provided in this evidence pack explicitly identifies this TxGNN prediction as a **probable false positive**, most likely resulting from co-localised "bleeding disorder" phenotype nodes in the knowledge graph creating a spurious connection, rather than any true biological or mechanistic similarity. This prediction should not be pursued without an independent credible biological hypothesis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for Glanzmann Thrombasthenia.

> **Contextual note — Hemophilia (TxGNN Rank 7, score 99.10%):** This is the highest-ranked prediction with any literature support (11 publications, evidence level L4). However, none of these publications study andexanet alfa as a treatment *for* haemophilia. They primarily describe andexanet alfa in its approved role as a DOAC reversal agent, or address laboratory interference in haemophilia diagnostics. The table below is provided for context only and does not constitute evidence supporting a repurposing hypothesis.

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [33742436](https://pubmed.ncbi.nlm.nih.gov/33742436/) | 2021 | Clinical Guideline | Thrombosis and Haemostasis | ICSH updated recommendations for DOAC laboratory measurement; references andexanet alfa as specific reversal agent for apixaban/rivaroxaban |
| [38620086](https://pubmed.ncbi.nlm.nih.gov/38620086/) | 2024 | Observational Registry | Circulation | ANNEXA-4 subanalysis: andexanet alfa efficacy and safety in acute gastrointestinal bleeding in patients on FXa inhibitors |
| [30309890](https://pubmed.ncbi.nlm.nih.gov/30309890/) | 2018 | Narrative Review | Blood | Review of andexanet alfa US licensure and the unmet clinical need for reversing FXa inhibitors in bleeding trauma patients |
| [31962376](https://pubmed.ncbi.nlm.nih.gov/31962376/) | 2020 | Laboratory Study | Haemophilia | Andexanet alfa used to neutralise rivaroxaban interference in FVIII/FIX clotting assays; relevant to haemophilia A/B laboratory diagnosis |
| [36819179](https://pubmed.ncbi.nlm.nih.gov/36819179/) | 2023 | Protocol Review | EJHaem | Review of UK hospital protocols for andexanet alfa use; practical implementation guidance |
| [31446606](https://pubmed.ncbi.nlm.nih.gov/31446606/) | 2019 | Narrative Review | Internal and Emergency Medicine | Overview of reversal agents for DOAC-associated major or life-threatening bleeding including andexanet alfa |
| [31298165](https://pubmed.ncbi.nlm.nih.gov/31298165/) | 2019 | Narrative Review | Current Pharmaceutical Design | New haemostatic agents in perioperative settings; includes andexanet alfa among procoagulant antidotes |
| [28277769](https://pubmed.ncbi.nlm.nih.gov/28277769/) | 2017 | Narrative Review | Br J Hospital Medicine | Strategies for reversal of direct oral anticoagulants; early review including novel reversal agents |
| [26519420](https://pubmed.ncbi.nlm.nih.gov/26519420/) | 2016 | Narrative Review | Drug Safety | NOAC reversal strategies — state of development and future perspectives |
| [39715914](https://pubmed.ncbi.nlm.nih.gov/39715914/) | 2025 | Drug Approval Review | Drugs | Marstacimab (anti-TFPI antibody) first approval for haemophilia A/B; contextualises novel haemostatic mechanisms in haemophilia — distinct from andexanet alfa's mechanism |

---

## Denmark Market Information

Andexanet Alfa is **not currently authorised or marketed in Denmark**. No marketing authorisations from Laegemiddelstyrelsen (national procedure) or via the EMA centralised procedure have been registered for use in Denmark at the time of this report.

| Marketing Authorisation | Product Name | Status | Note |
|------------------------|-------------|--------|------|
| EU/1/19/1376 (EMA) | Ondexxya® (AstraZeneca) | Centrally authorised in EU — **not registered in Denmark** | Approved for reversal of apixaban/rivaroxaban in life-threatening bleeding in adults |

> If access is required in Denmark, a Named Patient Programme or hospital exemption import application to Laegemiddelstyrelsen would be the applicable pathway, referencing the EMA-approved Ondexxya® SmPC.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for Ondexxya® (EU/1/19/1376) for complete safety information.

> Safety data (key warnings, contraindications, drug-drug interactions) were not available in this evidence pack. Clinicians should be aware that andexanet alfa carries a known risk of **thromboembolic events** (including stroke, myocardial infarction, and deep vein thrombosis) associated with its pro-coagulant reversal mechanism. Full risk-benefit assessment is required for each individual patient.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top TxGNN prediction of Glanzmann Thrombasthenia carries an evidence level of L5 (model prediction only, no clinical or preclinical studies) and the embedded mechanistic rationale explicitly identifies this as a biological implausibility — Andexanet Alfa's FXa-decoy mechanism targets secondary haemostasis (the coagulation cascade), while Glanzmann Thrombasthenia is a primary haemostasis disorder (platelet aggregation failure via GPIIb/IIIa deficiency) with no mechanistic overlap. All other predicted indications in this pack (platelet release disorders, pseudo-von Willebrand disease, hemophilia) similarly lack supporting clinical trial evidence and do not have a credible mechanistic basis for repurposing.

**To proceed, the following would be needed:**
- An independent credible biological hypothesis linking andexanet alfa's FXa-decoy mechanism to platelet biology or any of the predicted bleeding disorders
- Preclinical evidence (in vitro models or animal studies) demonstrating pharmacological activity relevant to the proposed new indication
- Expert haematology consultation to evaluate biological plausibility before any clinical exploration
- Complete SmPC and safety profile review, including thromboembolic risk assessment, before any clinical consideration
- Resolution of the data gap regarding the full mechanism of action (DrugBank API query recommended per DG002)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

