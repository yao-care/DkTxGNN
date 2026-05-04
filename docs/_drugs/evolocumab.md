---
layout: default
title: Evolocumab
parent: 僅模型預測 (L5)
nav_order: 184
evidence_level: L5
indication_count: 10
---

# Evolocumab
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

# Evolocumab: From Hypercholesterolaemia to Symptomatic Form of Haemophilia in Female Carriers

## One-Sentence Summary

Evolocumab is a PCSK9 inhibitor (monoclonal antibody), widely used for the treatment of hypercholesterolaemia and reduction of cardiovascular risk.
The TxGNN model predicts it may be effective for **Symptomatic Form of Haemophilia in Female Carriers**, however there are currently **no clinical trials** and **no publications** supporting this specific indication.
All five predicted indications remain at the hypothesis stage (Evidence Level L5), warranting a **Hold** recommendation.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypercholesterolaemia / Cardiovascular risk reduction (known PCSK9 inhibitor; no local licence data available) |
| Predicted New Indication | Symptomatic form of haemophilia in female carriers |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L5 — Model prediction only, no clinical or preclinical studies |
| Denmark Market Status | Not marketed (no national Laegemiddelstyrelsen or EMA centralised licence recorded in dataset) |
| Number of Marketing Authorisations | 0 (in dataset; note: Evolocumab is authorised in the EU as **Repatha** via EMA centralised procedure EU/1/15/1016 — this discrepancy reflects the data source limitation) |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Evolocumab is a fully human monoclonal antibody that inhibits proprotein convertase subtilisin/kexin type 9 (PCSK9). PCSK9 normally binds to LDL receptors on hepatocytes and promotes their degradation; by blocking PCSK9, evolocumab increases the number of LDL receptors available to clear LDL-cholesterol from the bloodstream, achieving LDL-C reductions of 50–60%. It is approved globally (including via EMA) for primary hypercholesterolaemia, mixed dyslipidaemia, and established atherosclerotic cardiovascular disease.

The TxGNN model's top prediction — symptomatic haemophilia in female carriers — is based on emerging basic science linking PCSK9 to coagulation factor clearance. Preliminary research suggests PCSK9 participates in the hepatic clearance of Factor VIII (FVIII); inhibiting PCSK9 could theoretically raise circulating FVIII levels, which might benefit patients with FVIII deficiency (haemophilia A). However, this hypothesis has **not been validated clinically**, and PCSK9's known anti-thrombotic effects (reduced platelet activation) could paradoxically worsen bleeding tendency. Furthermore, the prediction applies specifically to FVIII-related mechanisms and would not address all causes of bleeding in female carriers.

The mechanistic rationale is therefore assessed as **very weak and directionally contradictory**. The high TxGNN score (99.82%) likely reflects knowledge graph clustering of coagulation-related disorders rather than a specific, validated PCSK9–haemophilia interaction. Across all five unique predicted indications, none have any supporting clinical trial or published literature evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for any of the five predicted indications in combination with evolocumab.

*Sources searched: ClinicalTrials.gov and WHO ICTRP (query date: 2026-03-24)*

---

## Literature Evidence

Currently no related literature available for any of the five predicted indications in combination with evolocumab.

*Source searched: PubMed (query date: 2026-03-24)*

---

## All Predicted Indications Overview

Since all five unique predicted indications lack clinical evidence, a summary table is provided for comparison:

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Mechanistic Assessment | Recommendation |
|------|---------------------|-------------|---------------|----------------------|----------------|
| 1 | Symptomatic form of haemophilia in female carriers | 99.82% | L5 | Very weak; directionally contradictory. PCSK9 inhibition may reduce platelet activation (anti-thrombotic), potentially harmful in bleeding disorders. PCSK9–FVIII clearance hypothesis is unvalidated. | Hold |
| 3 | Familial apolipoprotein C-II deficiency | 99.50% | L5 | Partially related (both lipid metabolism) but mechanistically mismatched. ApoC-II deficiency causes hypertriglyceridaemia via lipoprotein lipase dysfunction; evolocumab acts on LDL receptor pathway with only modest TG reduction (12–17%). | Hold |
| 5 | Thrombocytopenic purpura | 99.42% | L5 | Indirect and unclear. PCSK9 has emerging links to platelet function and inflammation, but cannot address core TTP pathology (ADAMTS13 deficiency) or ITP pathology (autoimmune platelet destruction). | Hold |
| 7 | Factor XI deficiency | 99.29% | L5 | Very weak. No evidence that PCSK9 participates in Factor XI synthesis, secretion, or clearance. High score likely due to knowledge graph clustering of coagulation factor deficiencies. | Hold |
| 9 | Haemophilia A with vascular abnormality | 99.22% | L5 | Weak but has exploratory value. Combines two aspects: PCSK9–FVIII clearance hypothesis (unvalidated) and evolocumab's proven benefits on endothelial function and atherosclerotic plaque reduction. Relatively strongest rationale among the five candidates. | Research Question |

---

## Denmark Market Information

No marketing authorisations were found in the dataset for evolocumab.

> **Important note:** This reflects a data source limitation. Evolocumab is marketed in Denmark and the EU under the brand name **Repatha** (Amgen) via the EMA centralised marketing authorisation (EU/1/15/1016), approved for:
> - Primary hypercholesterolaemia (heterozygous familial and non-familial) or mixed dyslipidaemia
> - Homozygous familial hypercholesterolaemia
> - Established atherosclerotic cardiovascular disease (to reduce cardiovascular risk)
>
> Healthcare professionals should consult the [EMA product information](https://www.ema.europa.eu/en/medicines/human/EPAR/repatha) for the full Summary of Product Characteristics (SmPC).

---

## Safety Considerations

Detailed safety data (warnings, contraindications, drug interactions) was not available in the evidence pack. No drug-drug interactions were identified in the DDI database search.

> Please refer to the approved Summary of Product Characteristics (SmPC) for Repatha (evolocumab) available via the EMA for comprehensive safety information, including:
> - Hypersensitivity reactions
> - Injection site reactions
> - Use in patients with severe hepatic impairment
> - Effects on fertility and pregnancy

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All five predicted indications are at Evidence Level L5 (TxGNN model prediction only), with zero clinical trials and zero publications supporting any of the drug–disease combinations. The mechanistic rationale for the top prediction (haemophilia in female carriers) is assessed as very weak and potentially contradictory — PCSK9 inhibition's anti-thrombotic properties could theoretically worsen bleeding tendency. The only indication with some exploratory value is haemophilia A with vascular abnormality (Rank 9), where evolocumab's vascular benefits and the unvalidated PCSK9–FVIII hypothesis provide a minimal biological basis.

**To proceed, the following is needed:**
- **Mechanism of action data**: Detailed investigation of PCSK9's role in coagulation factor (especially FVIII) clearance, through preclinical studies
- **Safety data**: Full SmPC review for evolocumab, particularly regarding bleeding risk and coagulation parameters
- **Preclinical validation**: In vitro/in vivo studies to test whether PCSK9 inhibition affects circulating Factor VIII levels
- **Denmark regulatory alignment**: Confirm Repatha's EMA marketing authorisation details and any relevant national reimbursement status via Laegemiddelstyrelsen/Medicinrådet
- **Literature monitoring**: Set up alerts for emerging publications on PCSK9 and coagulation factor metabolism

---

*This report is for research purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before any therapeutic application. Report generated: 2026-04-05 | Data cutoff: 2026-04-05 | Evidence Pack version: v4*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

