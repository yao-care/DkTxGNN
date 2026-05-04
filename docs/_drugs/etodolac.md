---
layout: default
title: Etodolac
parent: 僅模型預測 (L5)
nav_order: 179
evidence_level: L5
indication_count: 10
---

# Etodolac
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

# Etodolac: From Pain/Inflammation (NSAID) to Spondyloarthropathy

## One-Sentence Summary

Etodolac is a non-steroidal anti-inflammatory drug (NSAID) with COX-2 preferential selectivity, originally used for osteoarthritis and rheumatoid arthritis.
The TxGNN model predicts it may be effective for **Spondyloarthropathy** (among other conditions),
with **0 clinical trials** and **0 publications** currently identified for the specific predicted indications — though class-level evidence for NSAIDs in spondyloarthropathy is well-established.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Osteoarthritis, rheumatoid arthritis, pain (NSAID) |
| Predicted New Indication | Acromesomelic dysplasia, Hunter-Thompson type (rank 1); **Spondyloarthropathy** (rank 7, most clinically relevant) |
| TxGNN Prediction Score | 99.97% (rank 1); 99.96% (spondyloarthropathy) |
| Evidence Level | L5 (rank 1, model prediction only); L4 (spondyloarthropathy, class-level mechanistic evidence) |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold (overall); Proceed with Guardrails (spondyloarthropathy only) |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known pharmacology, Etodolac is a pyranocarboxylic acid derivative NSAID that preferentially inhibits cyclooxygenase-2 (COX-2), thereby reducing prostaglandin E2 (PGE2) synthesis and its downstream pro-inflammatory effects. Its COX-2 selectivity offers a more favourable gastrointestinal safety profile compared to non-selective NSAIDs, making it suitable for chronic musculoskeletal conditions.

The TxGNN model generated five unique predicted indications for Etodolac. The top-ranked predictions (acromesomelic dysplasia Hunter-Thompson type, brachyolmia-amelogenesis imperfecta syndrome, brachyolmia) are ultra-rare genetic skeletal dysplasias caused by specific gene mutations (GDF5, TRPV4, PAPSS2, etc.). The mechanistic link between COX-2 inhibition and correction of congenital bone development defects is extremely tenuous (rated 1/5 stars). These high TxGNN scores likely reflect graph-structural proximity between skeletal/connective tissue disease nodes rather than genuine therapeutic potential.

The most clinically meaningful prediction is **spondyloarthropathy** (rank 7, score 99.96%). NSAIDs are established first-line therapy for spondyloarthropathies (including ankylosing spondylitis) per ASAS/EULAR guidelines. Etodolac's COX-2 preferential inhibition directly addresses joint inflammation, pain, and morning stiffness in these patients. Historical clinical studies from the 1990s–2000s have evaluated etodolac in ankylosing spondylitis, providing class-level evidence. **Myosclerosis** (rank 5, score 99.97%) presents a weak but theoretically interesting connection via NF-kB-mediated fibrosis modulation, warranting further research.

---

## Predicted Indications Summary

Since no clinical trials or literature were found for any of the specific predicted indications, the following table summarises all unique TxGNN predictions:

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Mechanistic Link | Recommendation |
|------|---------------------|-------------|---------------|-----------------|----------------|
| 1 | Acromesomelic dysplasia, Hunter-Thompson type | 99.97% | L5 | Very weak (1/5) — rare genetic bone disorder; NSAID cannot correct GDF5 mutations | Hold |
| 3 | Brachyolmia-amelogenesis imperfecta syndrome | 99.97% | L5 | Very weak (1/5) — rare genetic disorder of bone and enamel development | Hold |
| 5 | Myosclerosis | 99.97% | L5 | Weak (2/5) — theoretical NF-kB/fibrosis link; no preclinical evidence | Research Question |
| **7** | **Spondyloarthropathy, susceptibility to** | **99.96%** | **L4** | **Strong (4/5) — NSAIDs are first-line for spondyloarthropathy (ASAS/EULAR)** | **Proceed with Guardrails** |
| 9 | Brachyolmia | 99.96% | L5 | Very weak (1/5) — overlaps with rank 3; likely redundant graph prediction | Hold |

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Etodolac in any of the specific predicted indications.

*Note: While no trials were identified for the exact disease terms queried, class-level evidence exists for NSAIDs (including etodolac) in spondyloarthropathies. A broader search using terms such as "ankylosing spondylitis" or "axial spondyloarthritis" combined with "etodolac" would likely yield relevant results.*

---

## Literature Evidence

Currently no related literature available for Etodolac in any of the specific predicted indications.

*Note: As with clinical trials, published studies on etodolac in ankylosing spondylitis and related spondyloarthropathies do exist in the broader literature but were not captured by the disease-specific query terms used.*

---

## Denmark Market Information

Etodolac is currently **not marketed** in Denmark. No marketing authorisations (neither national Laegemiddelstyrelsen nor centralised EMA) were identified.

*Note: Etodolac has been marketed in other countries (e.g., USA as Lodine; Japan; India) but does not currently hold a valid marketing authorisation in Denmark. Any repurposing consideration would first require regulatory pathway assessment for market access.*

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

*As Etodolac is not marketed in Denmark, the SmPC from a reference country (e.g., FDA label for Lodine) should be consulted. Key safety concerns common to all NSAIDs include:*
- *Cardiovascular thrombotic events*
- *Gastrointestinal bleeding, ulceration, and perforation*
- *Renal toxicity*
- *Hepatotoxicity*
- *Serious skin reactions (Stevens-Johnson syndrome, toxic epidermal necrolysis)*

---

## Conclusion and Next Steps

**Decision: Hold** (overall); **Proceed with Guardrails** (spondyloarthropathy only)

**Rationale:**
The majority of TxGNN predictions (4 out of 5 unique indications) target ultra-rare genetic skeletal disorders for which an NSAID mechanism offers no plausible therapeutic benefit — these are rated "Hold." The spondyloarthropathy prediction, while ranked 7th by TxGNN score, is the only clinically actionable candidate, supported by strong class-level mechanistic evidence and established guidelines. However, since Etodolac is not marketed in Denmark and no indication-specific trials were identified, further steps are needed before advancement.

**To proceed, the following is needed:**
- Detailed mechanism of action data for Etodolac (DrugBank API query to resolve data gap DG002)
- SmPC safety data retrieval from a reference regulatory authority (to resolve data gap DG001)
- Broader literature search for etodolac in ankylosing spondylitis/axial spondyloarthritis (using expanded search terms)
- Regulatory pathway assessment for market access in Denmark (import/compassionate use/clinical trial)
- Drug-drug interaction profiling (current DDI data returned no results)
- For the myosclerosis prediction: preclinical feasibility review of NSAID anti-fibrotic effects before any further consideration

---

*This report was generated on 2026-04-05 based on Evidence Pack v4 (data cutoff: 2026-04-05). Results are for research purposes only and do not constitute medical advice. All drug repurposing candidates require clinical validation before application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

