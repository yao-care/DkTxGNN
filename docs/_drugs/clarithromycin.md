---
layout: default
title: Clarithromycin
parent: 僅模型預測 (L5)
nav_order: 114
evidence_level: L5
indication_count: 10
---

# Clarithromycin
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

# Clarithromycin: From Bacterial Infections to Hyperamylasemia

## One-Sentence Summary

Clarithromycin is a macrolide antibiotic used to treat a broad spectrum of bacterial infections, including respiratory tract infections, skin and soft tissue infections, and *Helicobacter pylori*-associated peptic ulcer disease.
The TxGNN model predicts it may be effective for **Hyperamylasemia**, with **0 clinical trials** and **1 publication** currently supporting this direction.
The overall evidence base is minimal (L5), and no direct mechanistic link between clarithromycin and hyperamylasemia has been established.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Denmark; clarithromycin is globally recognised for bacterial infections (respiratory tract, skin, *H. pylori* eradication) |
| Predicted New Indication | Hyperamylasemia |
| TxGNN Prediction Score | 99.35% |
| Evidence Level | L5 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known information, clarithromycin is a macrolide antibiotic belonging to the same class as azithromycin and erythromycin. Its antibacterial effect is achieved by binding to the 50S ribosomal subunit, thereby inhibiting bacterial protein synthesis. In addition, macrolides are recognised for immunomodulatory properties — particularly suppression of NF-κB signalling, reduction of pro-inflammatory cytokines (IL-6, IL-8, TNF-α), and inhibition of matrix metalloproteinases — which underlie their use in chronic airway inflammatory conditions such as diffuse panbronchiolitis.

Hyperamylasemia is defined as an elevated serum amylase level and arises from a range of causes including acute pancreatitis, salivary gland disorders, and secondary involvement of these organs during systemic illness. Clarithromycin has no established pharmacological pathway to reduce or modulate serum amylase.

The sole supporting publication (PMID 15228140) is a 2004 Japanese case report describing a 76-year-old man with *Mycobacterium abscessus* lung infection who incidentally had primary macroamylasemia as a comorbidity. Hyperamylasemia in this case was not a treatment target — it was an accompanying finding, likely from pancreatic or salivary gland involvement during systemic infection. The TxGNN prediction most likely reflects a distant knowledge-graph connection between infection, systemic inflammation, and amylase elevation, rather than a direct therapeutic relationship. The biological plausibility of this repurposing hypothesis is very low.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [15228140](https://pubmed.ncbi.nlm.nih.gov/15228140/) | 2004 | Case Report | Nihon Kokyuki Gakkai zasshi (J. Japanese Respiratory Society) | A 76-year-old man with *M. abscessus* lung infection complicated by primary macroamylasemia. Hyperamylasemia was an incidental comorbidity — not the indication for clarithromycin treatment, and not a clinically targeted outcome. |

---

## Denmark Market Information

Clarithromycin is not currently registered or marketed in Denmark. No marketing authorisations are on record with the Danish Medicines Agency (Lægemiddelstyrelsen), and no centralised EMA authorisations are listed for this drug in this dataset.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN model score (99.35%), the evidence supporting clarithromycin for hyperamylasemia consists of a single 2004 case report where elevated amylase was an incidental comorbidity — not the treatment target. There is no established mechanistic link, no clinical trials, no regulatory approval in Denmark, and the biological plausibility is assessed as very low.

**To proceed, the following is needed:**
- Mechanism of action data (MOA) from DrugBank to assess any indirect pathway linking clarithromycin to amylase regulation
- Full safety profile including key warnings, contraindications, and drug-drug interactions (from the SmPC)
- At least one hypothesis-generating preclinical study demonstrating an effect of clarithromycin on amylase production or secretion
- A plausible biological rationale distinguishing this prediction from a knowledge-graph artefact before any clinical investigation is warranted
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

