---
layout: default
title: Eprinomectin
parent: 僅模型預測 (L5)
nav_order: 170
evidence_level: L5
indication_count: 10
---

# Eprinomectin
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

# Eprinomectin: From Veterinary Antiparasitic to Candidiasis

## One-Sentence Summary

Eprinomectin is a semi-synthetic avermectin (macrocyclic lactone) of the avermectin class, currently used exclusively as a veterinary antiparasitic agent in livestock, with no approved human indication in Denmark or elsewhere.
The TxGNN model predicts it may be effective for **Candidiasis**, based on indirect mechanistic hypotheses involving ergosterol biosynthesis interference and immunomodulation.
There are currently **0 clinical trials** and **0 publications** directly supporting this repurposing direction, meaning the prediction rests entirely on computational modelling.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Veterinary antiparasitic (no human indication registered) |
| Predicted New Indication | Candidiasis |
| TxGNN Prediction Score | 98.89% |
| Evidence Level | L5 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the Evidence Pack. Based on known pharmacological class information, Eprinomectin belongs to the avermectin family (macrocyclic lactones), which exerts its primary antiparasitic action by activating glutamate-gated chloride (GluCl) channels in invertebrate neural and muscle tissue — a target that does not exist in fungi. The drug has proven efficacy against ectoparasites and endoparasites in cattle, and its close structural analogue ivermectin has been more extensively studied in human medicine.

The mechanistic link to Candidiasis proposed by the TxGNN model relies on several indirect hypotheses: (1) avermectin-class compounds may interfere with fungal ergosterol biosynthesis pathways (ivermectin has been reported in vitro to inhibit ergosterol synthesis in *Candida*); (2) host IL-4/IL-13 immunomodulation could theoretically alter the mucosal Th2/Th17 immune environment, indirectly affecting *Candida* colonisation; and (3) inhibition of ABC transporters (P-glycoprotein) might theoretically impair fungal fluconazole efflux pumps, potentially acting as an adjunct to azole therapy.

However, these pathways remain entirely hypothetical for Eprinomectin specifically. No direct antifungal activity of Eprinomectin against *Candida* has ever been tested, and its safety profile in human subjects has not been evaluated. The biological plausibility is weak, and any mechanistic connection would require extensive basic research before clinical investigation could be considered.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Denmark Market Information

Eprinomectin (DrugBank ID: DB11405) holds no marketing authorisations with the Danish Medicines Agency (Lægemiddelstyrelsen) and no centralised EMA authorisation for human use. It is not registered as a medicinal product for human use in Denmark.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information. No human safety data (warnings, contraindications, or drug–drug interactions) were available in the Evidence Pack for Eprinomectin.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model assigns a high prediction score (98.89%) to the Candidiasis indication, but this reflects knowledge-graph connectivity rather than biological or clinical validation. With zero supporting clinical trials, zero supporting publications, no human pharmacokinetic data, no human safety profile, no Danish or EMA marketing authorisation, and a mechanistic link that is entirely indirect and unverified, there is insufficient basis to advance this candidate at this time.

**To proceed, the following is needed:**

- **Mechanism of action clarification**: Confirm whether Eprinomectin has any direct or indirect antifungal activity in validated *in vitro* assays against *Candida* spp.
- **Human safety data**: Obtain or generate Phase 1 pharmacokinetic and safety data in humans, as none currently exist
- **Formulation feasibility**: Evaluate whether a clinically viable route of administration (oral, topical mucosal) exists for human antifungal use
- **Comparative benchmark**: Assess whether the predicted antifungal effect, if confirmed, would offer meaningful clinical advantage over well-established azoles, echinocandins, or polyenes
- **DrugBank MOA data**: Retrieve full mechanism, target, and toxicity data from DrugBank (DB11405) to enable proper mechanistic and safety analysis
- **Regulatory pathway assessment**: Determine whether a repurposing application to the EMA or Lægemiddelstyrelsen would be feasible given the exclusively veterinary status of the compound

> ⚠️ **Research Use Only**: The predictions and analysis in this report are intended for research purposes only and do not constitute medical advice. Drug repurposing candidates require clinical validation before any therapeutic application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

