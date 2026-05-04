---
layout: default
title: Miglustat
parent: 僅模型預測 (L5)
nav_order: 237
evidence_level: L5
indication_count: 10
---

# Miglustat
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

# Miglustat: From Gaucher Disease to Autosomal Ichthyosis Syndrome with Fatal Disease Course

## One-Sentence Summary

Miglustat (Zavesca®) is a glucosylceramide synthase (GCS) inhibitor approved in the EU for Gaucher disease type 1 and Niemann-Pick disease type C (NPC), acting via substrate reduction therapy (SRT) to curb toxic glycosphingolipid accumulation.
The TxGNN model predicts it may be effective for **autosomal ichthyosis syndrome with fatal disease course** with a prediction score of **99.83%**; however, **no clinical trials or supporting publications** have been identified for this indication, and the mechanistic rationale is considered weak.
This is a multi-indication evidence pack (TW-DB00419-multi) also covering cholesteryl ester storage disease, Krabbe disease, metachromatic leukodystrophy, and Wolman disease — of which **metachromatic leukodystrophy carries the strongest mechanistic rationale** and is recommended for active follow-up.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Gaucher disease type 1; Niemann-Pick disease type C (NPC) |
| Predicted New Indication (Top Rank) | Autosomal ichthyosis syndrome with fatal disease course |
| TxGNN Prediction Score | 99.83% |
| Evidence Level | L5 — model prediction only; no clinical trials or literature identified |
| Denmark Market Status | Not found in database — see note below |
| Number of Marketing Authorisations | 0 (database record) |
| Recommended Decision | **Hold** (top prediction); **Proceed with Guardrails** (metachromatic leukodystrophy, rank 4) |

> **⚠️ Registration note:** Miglustat (Zavesca®) holds a centralised EU marketing authorisation (EU/1/02/237) granted by the European Medicines Agency (EMA), which is valid in all EU member states including Denmark. The absence of records in the current database likely reflects a data collection gap rather than a genuine lack of authorisation. Healthcare professionals should consult the EMA product page and the current Danish Summary of Product Characteristics (SmPC) for authoritative registration status before drawing any regulatory conclusions.

---

## Multi-Indication Prediction Summary

This evidence pack contains five unique predicted indications (duplicated entries in ranks 1–10 have been deduplicated). All are in the lysosomal storage disorder / sphingolipid metabolism disease space — consistent with Miglustat's known mechanism of action.

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Recommendation |
|------|---------------------|-------------|----------------|----------------|
| 1 | Autosomal ichthyosis syndrome with fatal disease course | 99.83% | L5 | Hold |
| 2 | Cholesteryl ester storage disease (CESD) | 99.82% | L5 | Research Question |
| 3 | Krabbe disease | 99.78% | L4 | Research Question |
| **4** | **Metachromatic leukodystrophy (MLD)** | **99.77%** | **L4** | **Proceed with Guardrails** |
| 5 | Wolman disease with hypolipoproteinemia and acanthocytosis | 99.76% | L5 | Hold |

> **Editorial note:** Although TxGNN scores are nearly identical across all five indications (difference < 0.1%), the quality of mechanistic rationale varies substantially. Metachromatic leukodystrophy (rank 4) has the clearest pathway-level connection to Miglustat and the highest actionable recommendation in this set.

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data was not retrieved from DrugBank in this evidence pack (data gap DG002). Based on established pharmacological knowledge, Miglustat is an **iminosugar and competitive inhibitor of glucosylceramide synthase (GCS)** — the enzyme responsible for the first committed step in glycosphingolipid (GSL) biosynthesis. By reducing substrate flux into the GSL synthesis pathway, Miglustat lowers the accumulation of glucocerebrosides and downstream sphingolipids that would otherwise overload deficient lysosomal enzymes. Critically, Miglustat has demonstrated **blood-brain barrier (BBB) penetration**, making it uniquely relevant to CNS manifestations of lysosomal storage disorders.

**Why the top prediction (autosomal ichthyosis syndrome) is mechanistically weak:** Some congenital ichthyoses — notably Sjögren-Larsson syndrome — involve lipid metabolism abnormalities (ALDH3A2 mutations affecting fatty aldehyde catabolism). However, this pathway intersects with Miglustat's GCS inhibition route only distantly, with no shared enzymatic step. The designation "fatal disease course" further indicates an extreme phenotype where substrate reduction therapy offers no established rationale.

**Why other indications in this pack show stronger rationale:** Metachromatic leukodystrophy (MLD, ARSA deficiency) causes sulfatide accumulation via the same glycosphingolipid synthesis route that Miglustat directly suppresses — GCS inhibition reduces upstream galactocerebroside substrate availability, thereby limiting sulfatide production. Miglustat's BBB penetration is an additional advantage for this CNS demyelinating disease, and the concept has been explored in ARSA-knockout mouse models. Krabbe disease (GALC deficiency, psychosine accumulation) shares glycosphingolipid pathway adjacency with supporting data from the Twitcher mouse model. Cholesteryl ester storage disease and Wolman disease involve lysosomal dysfunction that overlaps pathologically with NPC — Miglustat's approved indication — though the enzymatic connection through the LAL/LIPA pathway is indirect.

---

## Clinical Trial Evidence

No clinical trials have been identified for any of the five predicted indications (autosomal ichthyosis syndrome, cholesteryl ester storage disease, Krabbe disease, metachromatic leukodystrophy, or Wolman disease with hypolipoproteinemia and acanthocytosis) in the ClinicalTrials.gov, ICTRP, or related registries search conducted on 2026-03-10.

> **Recommendation:** A broader literature and trial search using disease synonyms (e.g., "sulfatide lipidosis" and "ARSA deficiency" for MLD; "globoid cell leukodystrophy" for Krabbe disease; "LAL deficiency" for CESD/Wolman) and expanded search windows is advised before concluding that no evidence exists.

---

## Literature Evidence

No relevant publications have been identified linking Miglustat to any of the five predicted indications in the PubMed search conducted on 2026-03-10.

> **Recommendation:** As above, expanded searches using MeSH terms, disease synonyms, and broader glycosphingolipid/SRT-related queries may yield relevant preclinical literature, particularly for MLD and Krabbe disease.

---

## Denmark Market Information

No marketing authorisation records for Miglustat were returned from the Danish Medicines Agency (Laegemiddelstyrelsen) database query.

> As noted above, this is likely a data collection gap. Zavesca® (miglustat, 100 mg capsules) holds centralised EU authorisation EU/1/02/237 (Actelion/Janssen) for Gaucher disease type 1 and NPC neurological manifestation stabilisation; this authorisation is directly valid in Denmark. Prescribers should verify current Danish product information via the EMA product page or Laegemiddelstyrelsen's Medicinprodukter database.

---

## Safety Considerations

No safety data (key warnings, contraindications, or drug interactions) was retrieved for Miglustat during evidence collection for this evidence pack.

Please refer to the approved **Summary of Product Characteristics (SmPC) for Zavesca®** for full safety information before any clinical or research use.

---

## Conclusion and Next Steps

### Primary Prediction (Rank 1 — Autosomal Ichthyosis Syndrome with Fatal Disease Course)

**Decision: Hold**

**Rationale:**
The mechanistic link between Miglustat's GCS inhibition and autosomal ichthyosis is distant and unsupported by any clinical trial or published literature (L5 evidence only). The "fatal disease course" designation and absence of a plausible SRT intervention rationale make this an unfavourable candidate for development at this time.

---

### Priority Follow-Up Recommendation — Metachromatic Leukodystrophy (MLD, Rank 4)

**Decision: Proceed with Guardrails**

**Rationale:**
MLD is mechanistically the most compelling indication in this pack. Miglustat's direct suppression of upstream glycosphingolipid substrate and its established BBB penetration provide a biologically coherent rationale for the CNS demyelinating phenotype of MLD, supported by preclinical animal model data (L4 evidence).

**To proceed, the following is needed:**

- **Close the data gaps:** Retrieve Miglustat's DrugBank MOA entry (DG002) and the Danish/EMA SmPC safety profile (DG001)
- **Expanded literature search:** Use broader MeSH terms ("arylsulfatase A deficiency", "sulfatide lipidosis", "SRT leukodystrophy") to identify any published preclinical or early-phase data
- **Trial registry re-query:** Search ClinicalTrials.gov with NCT query terms for "miglustat AND leukodystrophy" and "substrate reduction AND MLD"
- **Regulatory pathway review:** Assess whether MLD's orphan disease designation in the EU (Regulation EC 141/2000) opens accelerated regulatory routes for a repurposing dossier
- **Specialist consultation:** Engage Danish or Nordic lysosomal storage disease specialists (e.g., at Copenhagen University Hospital – Rigshospitalet) to assess clinical feasibility and patient population size
- **Comparative context:** Review arylsulfatase A gene therapy approvals (Libmeldy/atidarsagene autotemcel, EMA approved 2020) to understand the current standard of care and where oral SRT might complement or serve patients ineligible for gene therapy

---

*This report is generated for research reference purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before any therapeutic application.*
*Data cutoff: 2026-04-04 | Candidate ID: TW-DB00419-multi | Evidence Pack version: v4*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

