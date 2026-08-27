---
layout: default
title: Tepoxalin
parent: 僅模型預測 (L5)
nav_order: 426
evidence_level: L5
indication_count: 10
---

# Tepoxalin
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

Using the drug-repurposing report template directly (no dedicated skill covers this report format — it's a fully-specified prompt), here is the report.

# Tepoxalin: From Veterinary Osteoarthritis to Human Osteoarthritis

## One-Sentence Summary

Tepoxalin is a dual COX/LOX inhibitor previously marketed as a veterinary NSAID for **canine** osteoarthritis (discontinued commercially per PMID 23802664); no human indication is on record.
The TxGNN model predicts it may be effective for **Osteoarthritis** in humans,
with **no clinical trials** and **8 (veterinary/preclinical) publications** currently supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not centrally registered; known prior use was as a veterinary NSAID for canine osteoarthritis (human original indication/MOA data unavailable) |
| Predicted New Indication | Osteoarthritis |
| TxGNN Prediction Score | 96.82% |
| Evidence Level | L4 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data (human) is not available. Based on the evidence pack, tepoxalin is a dual inhibitor of cyclooxygenase (COX) and lipoxygenase (LOX), reducing both prostaglandin and leukotriene production. In canine studies it lowered eicosanoid release from synovial tissue and showed anti-proliferative/pro-apoptotic effects on synovial fibroblasts (PMID 8936587, 19624842, 22240988), consistent with a plausible anti-inflammatory, cartilage-protective mechanism.

Tepoxalin's only well-documented indication is canine osteoarthritis, where it was marketed (brand Zubrin) before being withdrawn from the market (PMID 23802664). The TxGNN prediction for "osteoarthritis" (score 96.82%) therefore represents a **veterinary-to-human** repurposing hypothesis rather than a new-disease-class hypothesis: the pathophysiology of osteoarthritis is broadly conserved between dogs and humans, and one in vitro study (PMID 8936587) did test the compound directly on human synovial tissue from both rheumatoid arthritis and osteoarthritis patients, showing reduced eicosanoid release.

However, no human pharmacokinetic, efficacy, or safety data exist in this evidence pack, and the original product was discontinued commercially for veterinary use — the reason for discontinuation is not documented here and should be investigated before further evaluation, as it may reflect a safety or commercial signal relevant to human development.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23718664](https://pubmed.ncbi.nlm.nih.gov/23718664/) | 2013 | Cohort (veterinary) | American Journal of Veterinary Research | Assessed whether tepoxalin alters kidney function in dogs with concurrent chronic kidney disease and osteoarthritis |
| [16008217](https://pubmed.ncbi.nlm.nih.gov/16008217/) | 2005 | In vivo pharmacology (animal) | American Journal of Veterinary Research | Evaluated in vivo effects on prostaglandin and leukotriene production in dogs with chronic osteoarthritis |
| [18764695](https://pubmed.ncbi.nlm.nih.gov/18764695/) | 2008 | Comparative pharmacology (animal) | American Journal of Veterinary Research | Compared firocoxib, meloxicam and tepoxalin effects on prostanoid/leukotriene production in duodenal mucosa and joint tissue of osteoarthritic dogs |
| [8936587](https://pubmed.ncbi.nlm.nih.gov/8936587/) | 1996 | In vitro (organ culture) | Prostaglandins | Reduced eicosanoid release (LTC4, 6-keto-PGF1a, PGE2) in cultured **human** synovial tissue from RA and OA patients |
| [19624842](https://pubmed.ncbi.nlm.nih.gov/19624842/) | 2009 | Animal model | BMC Veterinary Research | Explored ability of tepoxalin to reduce cytokine-induced cartilage catabolism in a canine in vitro OA model |
| [22240988](https://pubmed.ncbi.nlm.nih.gov/22240988/) | 2012 | In vitro (cell culture) | Journal of Veterinary Medical Science | Demonstrated pro-apoptotic/antiproliferative effects of tepoxalin on canine synovial fibroblasts |
| [19000257](https://pubmed.ncbi.nlm.nih.gov/19000257/) | 2008 | Review (veterinary) | Journal of Veterinary Pharmacology and Therapeutics | Review of leukotriene inhibition in small animal medicine, referencing clinical benefit of leukotriene inhibition in human osteoarthritis, allergic asthma and atopic dermatitis |
| [23802664](https://pubmed.ncbi.nlm.nih.gov/23802664/) | 2013 | Commentary (market status) | American Journal of Veterinary Research | Notes that tepoxalin is no longer commercially available |

## Denmark Market Information

Tepoxalin currently holds **no marketing authorisation in Denmark** (0 registered licences; market status: not marketed). No Laegemiddelstyrelsen or EMA centralised authorisation data is available for this product.

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information. Note: as tepoxalin has no Danish marketing authorisation, no SmPC currently exists — safety warnings, contraindications and drug interaction data (including the DDI database, which returned no results) all remain unresolved data gaps that must be closed before any human safety evaluation can proceed.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence is limited to preclinical/veterinary pharmacology (L4) with no human clinical trials and no marketing history in Denmark; a Blocking data gap on core safety/label information (DG001) prevents even an initial (S1) safety assessment.

**To proceed, the following is needed:**
- Human mechanism-of-action and pharmacokinetic data (DG002)
- TFDA/DKMA-equivalent label warnings and contraindications (DG001)
- Clarification of why the veterinary product (Zubrin) was withdrawn from commercial availability
- At minimum, translational/human in vitro or early-phase clinical data specific to osteoarthritis before advancing beyond S1
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

