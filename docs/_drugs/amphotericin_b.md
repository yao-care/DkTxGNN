---
layout: default
title: Amphotericin B
parent: 僅模型預測 (L5)
nav_order: 35
evidence_level: L5
indication_count: 0
---

# Amphotericin B
{: .fs-9 }

證據等級: **L5** | 預測適應症: **0** 個
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

# Amphotericin B: Drug Repurposing Evaluation — No TxGNN Predictions Generated

---

## One-Sentence Summary

Amphotericin B is a well-established polyene antifungal agent used for severe, invasive fungal infections. **No TxGNN repurposing predictions were generated** for this drug in the current evaluation cycle, as critical data gaps in the pipeline prevented prediction from running. This report documents the current data status and outlines the remediation steps required before a formal repurposing evaluation can proceed.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Severe invasive fungal infections *(based on established pharmaceutical knowledge; no licence data retrieved from Laegemiddelstyrelsen)* |
| Predicted New Indication | Not available — no TxGNN predictions generated |
| TxGNN Prediction Score | Not available |
| Evidence Level | Not assessable |
| Denmark Market Status | Not marketed *(per evidence pack — see important note below)* |
| Number of Marketing Authorisations | 0 *(per evidence pack)* |
| Recommended Decision | **Hold** |

> **⚠️ Important note on Denmark market status:** The evidence pack records zero Danish Marketing Authorisations. However, liposomal amphotericin B (AmBisome®) holds a valid EMA centralised Marketing Authorisation (EU/1/97/049) that is directly applicable in Denmark, and conventional amphotericin B deoxycholate products have historically been available via hospital procurement. The zero-licence result almost certainly reflects a **data processing gap** rather than the true regulatory situation, and must be verified against the Laegemiddelstyrelsen product database before any regulatory conclusions are drawn.

---

## Why is This Prediction Reasonable?

As no TxGNN prediction was generated in this evaluation cycle, this section cannot be completed in the standard comparative format. The absence of predictions is a pipeline issue, not a reflection of the drug's repurposing potential.

For context: Amphotericin B (DrugBank ID: DB00681) is a polyene macrolide antibiotic first isolated from *Streptomyces nodosus* in the 1950s. Detailed mechanism of action data was not retrieved in this evaluation cycle. Based on established pharmacological knowledge, Amphotericin B acts by binding selectively to ergosterol in the fungal cell membrane, inserting into the lipid bilayer and forming transmembrane pores. This causes irreversible leakage of intracellular ions and metabolites, leading to osmotic instability and cell death. Its selectivity for ergosterol over mammalian cholesterol underpins its clinical utility.

Recognised areas of potential repurposing discussed in the scientific literature — including antileishmanial activity (visceral leishmaniasis, already an approved indication for the liposomal form), antiviral applications, and immunomodulatory effects in oncology settings — cannot be formally ranked or evaluated without TxGNN prediction output. Re-running the prediction pipeline with corrected input data is the necessary first step.

---

## Safety Considerations

Safety data (key warnings and contraindications) was not retrieved from Laegemiddelstyrelsen in this evaluation cycle. Based on the established clinical safety profile of Amphotericin B:

- **Nephrotoxicity**: Dose-dependent renal impairment is the primary dose-limiting toxicity of the conventional deoxycholate formulation. Liposomal formulations (e.g. AmBisome®) substantially reduce nephrotoxic risk. Baseline and regular serum creatinine, urea, and electrolyte monitoring is essential.
- **Infusion-related reactions**: Fever, rigors, chills, hypotension, and bronchospasm may occur during intravenous administration; premedication protocols are standard practice.
- **Electrolyte disturbances**: Hypokalaemia and hypomagnesaemia are common and require monitoring and replacement.
- **Haematological effects**: Normochromic normocytic anaemia can develop with prolonged courses.

Please refer to the approved Summary of Product Characteristics (SmPC) — available via the European Medicines Agency (EMA) product page for AmBisome® — for complete and authoritative safety information including full contraindication and drug interaction data.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction pipeline produced no repurposing candidates for Amphotericin B, and two unresolved data gaps — one classified as Blocking, one as High severity — prevent the evaluation from advancing to safety pre-screening or clinical evidence review. No meaningful repurposing recommendation can be issued at this stage.

**To proceed, the following is needed:**

1. **[Blocking]** Resolve Laegemiddelstyrelsen licence data retrieval failure and re-populate `taiwan_regulatory` with correct Danish authorisation records, including the EMA centralised authorisation for AmBisome® (EU/1/97/049)
2. **[Blocking]** Re-run the TxGNN prediction pipeline once input data is corrected, to generate ranked repurposing candidates with confidence scores
3. **[High]** Retrieve Mechanism of Action (MOA) data via DrugBank API for DrugBank ID DB00681 to support mechanistic plausibility analysis
4. **[High]** Download and parse the current SmPC (via EMA or Laegemiddelstyrelsen) to populate key warnings, contraindications, and drug interaction data for safety pre-screening
5. Once predictions are available, re-run the full evidence collection pipeline (ClinicalTrials.gov, PubMed, EudraCT) for the top-ranked predicted indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

