---
layout: default
title: Carprofen
parent: 僅模型預測 (L5)
nav_order: 94
evidence_level: L5
indication_count: 10
---

# Carprofen
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

# Carprofen: From Withdrawn NSAID to Rheumatoid Arthritis

## One-Sentence Summary

Carprofen is a propionic acid-class NSAID that was historically approved in several European markets for rheumatoid arthritis and musculoskeletal inflammation before being voluntarily withdrawn from all human markets in the late 1980s, primarily due to idiosyncratic hepatotoxicity; it is currently used exclusively in veterinary medicine (e.g., Rimadyl® for dogs).
The TxGNN model predicts it may be effective for **Rheumatoid Arthritis**, with **0 registered clinical trials** and **20 publications** — including at least one double-blind crossover RCT — currently supporting this direction.
This evaluation represents a **historical indication re-assessment** rather than a conventional drug repurposing scenario: the efficacy signal is established, but the hepatotoxicity that caused market withdrawal remains the central unresolved barrier.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Rheumatoid arthritis and musculoskeletal inflammatory conditions (historical European approval; withdrawn from all human markets ~late 1980s) |
| Predicted New Indication | Rheumatoid Arthritis |
| TxGNN Prediction Score | 99.80% |
| Evidence Level | L2 (1 completed double-blind crossover RCT in RA patients, from historical literature) |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Carprofen belongs to the arylpropionic acid (profen) subclass of NSAIDs, related to ibuprofen, naproxen, and ketoprofen. It acts as a non-selective cyclooxygenase inhibitor (COX-1 and COX-2), reducing prostaglandin E₂ (PGE₂) synthesis in inflamed synovial tissue. Lower synovial PGE₂ levels translate directly into reduced joint inflammation, swelling, and pain — the defining features of rheumatoid arthritis. Multiple laboratory studies have confirmed that carprofen reduces synovial fluid PGE₂ and thromboxane B₂ concentrations in RA patients (PMID 3864577, 2155476) and, notably, also inhibits IgM rheumatoid factor production by approximately 50% in vitro (PMID 6120390) — an immunomodulatory effect that goes beyond simple prostaglandin suppression.

The clinical evidence base is concentrated in the 1980s and is directly relevant: a four-month double-blind crossover RCT (PMID 6340183, n = 28) demonstrated that carprofen 300 mg/day produced efficacy comparable to indomethacin 75 mg/day in definite or classic RA using standard disease activity measures. A parallel-group, dose-ranging double-blind trial (PMID 7009441, n = 36) confirmed dose-dependent effects at 150–450 mg/day. A multiple-crossover dose-response study (PMID 3293874, n = 38) established a linear plasma concentration–therapeutic response relationship. Pharmacokinetic data confirm that carprofen reaches therapeutically relevant concentrations in synovial fluid after oral dosing (mean 6.2 µg/mL; PMID 6573017). In aggregate, the mechanistic rationale and historical clinical data are strong.

However, this is not a typical drug repurposing case. TxGNN is effectively re-identifying carprofen's own historical human indication. The reason it is being evaluated here is that it was *withdrawn* from the market before completing a full regulatory approval cycle in most jurisdictions — not because efficacy was in doubt, but because post-marketing hepatotoxicity reports emerged. Any pathway forward must therefore start with the hepatotoxicity signal, not efficacy. The question for Danish healthcare professionals is not "does carprofen work in RA?" but "can the liver risk be characterised and managed well enough to justify re-entering development against a backdrop of far more modern RA therapies?"

---

## Clinical Trial Evidence

Currently no related clinical trials registered on ClinicalTrials.gov or the WHO ICTRP for carprofen in rheumatoid arthritis.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [6340183](https://pubmed.ncbi.nlm.nih.gov/6340183/) | 1983 | RCT (Double-blind Crossover) | Scand J Rheumatol Suppl | 4-month crossover trial, n = 28 definite/classic RA; carprofen 300 mg/day vs. indomethacin 75 mg/day showed comparable efficacy across standard RA activity measures with acceptable tolerability |
| [7009441](https://pubmed.ncbi.nlm.nih.gov/7009441/) | 1980 | Comparative Clinical Study (Double-blind Parallel) | Int J Clin Pharmacol Ther Toxicol | 6-week trial, n = 36 RA patients; dose escalation 150–450 mg/day carprofen vs. indomethacin 100 mg/day; classical RA parameters and toxicity panel assessed |
| [3293874](https://pubmed.ncbi.nlm.nih.gov/3293874/) | 1988 | Dose-Response RCT (Multiple Crossover) | Clin Pharmacol Ther | n = 38 active RA; 100–800 mg/day carprofen; linear dose-response confirmed for 6/9 efficacy measures; plasma concentration linked to therapeutic response |
| [6573017](https://pubmed.ncbi.nlm.nih.gov/6573017/) | 1983 | Pharmacokinetic Study | Scand J Rheumatol Suppl | n = 13 RA patients; carprofen achieves mean 6.2 µg/mL in synovial fluid 4 hours after 100 mg oral dose — confirms adequate joint penetration |
| [2155476](https://pubmed.ncbi.nlm.nih.gov/2155476/) | 1990 | Clinical Study (Synovial Fluid Analysis) | Scand J Rheumatol | n = 53 RA patients across 9 NSAIDs + prednisolone; carprofen reduced synovial PGE₂, leukotriene B4, and white cell count in joint fluid |
| [3864577](https://pubmed.ncbi.nlm.nih.gov/3864577/) | 1985 | Clinical Study (Prostanoid Analysis) | Clin Rheumatol | One-day treatment with 9 NSAIDs; carprofen clearly reduced synovial PGE₂ and TxB₂, confirming COX inhibition in the joint compartment |
| [6120390](https://pubmed.ncbi.nlm.nih.gov/6120390/) | 1982 | In vitro Mechanistic Study | Lancet | Carprofen inhibited IgM rheumatoid factor production ~50% in peripheral blood mononuclear cells; suggests immunomodulatory activity beyond prostaglandin suppression |
| [6592146](https://pubmed.ncbi.nlm.nih.gov/6592146/) | 1984 | Mechanistic Study (in vitro + in vivo) | Inflammation | Carprofen reduced IgM rheumatoid factor both in vitro and in serum of treated RA patients in vivo |
| [7037867](https://pubmed.ncbi.nlm.nih.gov/7037867/) | 1981 | Safety / Organ Function Study | J Clin Pharmacol | Renal effects (salt/water homeostasis, creatinine clearance, blood pressure) of carprofen vs. indomethacin in 6 RA patients and 6 healthy volunteers; carprofen showed broadly similar but slightly milder renal impact |
| [3554157](https://pubmed.ncbi.nlm.nih.gov/3554157/) | 1987 | Narrative Review | Pharmacotherapy | Comprehensive review of carprofen's pharmacology, clinical efficacy in RA/OA, and adverse effects; discusses hepatotoxicity signal and the positioning of carprofen within the NSAID class |

---

## Denmark Market Information

Carprofen currently holds no marketing authorisations in Denmark issued by the Danish Medicines Agency (Laegemiddelstyrelsen) and is not approved through the centralised EMA procedure for human use. The drug is not marketed for human use anywhere in the European Union or the United Kingdom. It remains approved for veterinary use under the brand name Rimadyl® (carprofen for dogs).

---

## Safety Considerations

**Hepatotoxicity — Primary Safety Barrier:**
Carprofen was withdrawn from human markets in the late 1980s following post-marketing reports of severe, idiosyncratic (non-dose-dependent) hepatotoxicity, including cases of fulminant hepatic failure. This is the single most critical safety concern and the direct cause of market withdrawal. Any clinical development programme would require a thorough characterisation of the hepatotoxicity mechanism, incidence estimation from historical pharmacovigilance data, and a mandatory liver function monitoring protocol.

**Photosensitivity — Clinically Significant:**
Carprofen has a documented and notably high rate of photosensitising reactions. A systematic photopatch test study (PMID 2951351, n = 86) found photoallergic or phototoxic reactions in 24.4% of patients tested — one of the highest rates among NSAIDs evaluated. Individual case reports of both phototoxic and photoallergic reactions have been published (PMID 6525967). Patients would require sun-avoidance counselling and appropriate skin protection measures.

**General NSAID Class Effects:**
As a COX-1/COX-2 inhibitor, carprofen carries all standard NSAID class risks, including gastrointestinal mucosal injury (ulceration, bleeding), renal effects (confirmed in human studies: PMID 7037867), cardiovascular risks associated with long-term COX inhibition, and potential hypersensitivity reactions including cross-reactivity in aspirin-sensitive patients.

**Drug Interactions:**
No interaction data were available in the current Evidence Pack. Given the NSAID class profile, clinically relevant interactions with anticoagulants (e.g., warfarin), antihypertensives, diuretics, lithium, and methotrexate should be anticipated and evaluated before clinical use.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The efficacy evidence for carprofen in rheumatoid arthritis is historically established, with direct human clinical data including a double-blind crossover RCT. However, the drug was withdrawn from all human markets specifically due to idiosyncratic hepatotoxicity — a blocking safety signal that has not been resolved. Furthermore, modern RA treatment has transformed dramatically since the 1980s (DMARDs, biologics, JAK inhibitors), fundamentally shifting the benefit-risk context. Proceeding with development requires resolving the hepatotoxicity question and demonstrating a compelling advantage over currently available therapies.

**To proceed, the following is needed:**
- **Hepatotoxicity risk assessment**: Full review and synthesis of all post-marketing liver adverse event reports from the 1980s withdrawal period; estimation of incidence and severity distribution; comparison with current NSAID hepatotoxicity profiles
- **Mechanistic hepatotoxicity investigation**: Clarification of whether the liver injury is metabolite-mediated, immune-idiosyncratic, or related to a specific patient subgroup — critical for determining whether it is preventable or manageable
- **Benefit-risk analysis vs. current standard of care**: Formal comparison of carprofen's efficacy and safety profile against modern RA therapies (methotrexate, biologics, JAK inhibitors, celecoxib); the bar for re-entering a saturated therapeutic area is high
- **Complete MOA documentation**: Formal MOA data from DrugBank or scientific literature to support regulatory submissions
- **Regulatory feasibility consultation**: Pre-submission dialogue with the Danish Medicines Agency (Laegemiddelstyrelsen) on the regulatory pathway for re-developing a compound previously withdrawn for safety reasons
- **If hepatotoxicity can be de-risked**: Design of a safety-first Phase 1/2 study with mandatory, frequent liver function monitoring (ALT, AST, bilirubin) and pre-defined stopping rules

> **Research note**: This evaluation covers the top-ranked TxGNN prediction (rheumatoid arthritis). Lower-ranked predictions (colobomatous microphthalmia-rhizomelic dysplasia syndrome, brachydactyly-syndactyly syndrome) are assessed as biologically implausible artefacts of graph topology and are not recommended for further investigation. The osteoarthritis susceptibility prediction warrants re-evaluation once the indication definition is clarified (genetic susceptibility vs. symptomatic OA treatment). The tendinitis prediction has limited but mechanistically plausible clinical support (PMID 6983966) and could be revisited alongside any RA development programme.

---
*This report is for research purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before therapeutic application. Data as of 2026-04-04.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

