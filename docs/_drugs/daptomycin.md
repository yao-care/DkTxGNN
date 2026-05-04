---
layout: default
title: Daptomycin
parent: 僅模型預測 (L5)
nav_order: 128
evidence_level: L5
indication_count: 10
---

# Daptomycin
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

# Daptomycin: From Gram-Positive Bacterial Infections to Rheumatoid Arthritis

## One-Sentence Summary

Daptomycin (Cubicin) is a cyclic lipopeptide antibiotic approved for serious Gram-positive bacterial infections including complicated skin and soft tissue infections, *Staphylococcus aureus* bacteraemia, and right-sided infective endocarditis.
The TxGNN model assigns high prediction scores across several musculoskeletal indications; the most scientifically credible new candidate is **Rheumatoid Arthritis** (TxGNN score: 99.84%), supported by **2 preclinical studies** demonstrating anti-inflammatory activity via NF-κB pathway suppression in a collagen-induced arthritis (CIA) mouse model.
No clinical trials currently exist for any of the predicted new indications, and the highest-ranked prediction (osteoarthritis) is assessed as a likely knowledge graph artefact rather than a genuine repurposing signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Complicated skin and skin structure infections; *Staphylococcus aureus* bacteraemia; right-sided infective endocarditis caused by Gram-positive bacteria |
| Predicted New Indication (Best Candidate) | Rheumatoid Arthritis |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L4 (Preclinical studies only) |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Daptomycin is a cyclic lipopeptide antibiotic that acts by inserting into bacterial cell membranes in a calcium-dependent manner, causing rapid membrane depolarisation and irreversible disruption of bacterial physiology. This mechanism is highly effective against Gram-positive bacteria — including methicillin-resistant *Staphylococcus aureus* (MRSA) — and underpins its approved indications. Detailed mechanism of action (MOA) data was not available in the DrugBank submission within this evidence pack (Data Gap DG002), but the antibacterial mechanism is well established in the published literature.

Beyond its antibacterial action, two preclinical studies published in 2025 have revealed a previously unrecognised anti-inflammatory property. Daptomycin was found to inhibit the NF-κB signalling pathway in joint tissue, reducing the secretion of pro-inflammatory cytokines — specifically TNF-α, IL-1β, and IL-6 — and producing measurable joint-protective effects in a collagen-induced arthritis (CIA) mouse model (PMID 39571268). A follow-up study synthesised and tested five novel daptomycin-derived cyclic lipopeptide analogues, demonstrating that anti-arthritic activity appears to be a class effect of the cyclic lipopeptide scaffold rather than unique to daptomycin itself (PMID 40923559).

Rheumatoid arthritis is driven by chronic synovial inflammation, osteoclast activation, and NF-κB-mediated inflammatory cascades — precisely the pathways these studies suggest daptomycin can modulate. The mechanistic link is therefore conceptually plausible. However, it is critical to note that (1) no human clinical trials have been conducted, (2) the transition from CIA mouse models to clinical RA has historically proven difficult, and (3) current IV-only administration makes chronic use in RA practically challenging. The other top-ranked TxGNN predictions should be interpreted with significant caution: the osteoarthritis signal (rank 1, score 99.86%) appears to be a knowledge graph artefact — all supporting literature describes daptomycin treating *bacterial infections complicating joint surgery*, not osteoarthritis itself. The gout prediction (score 99.79%) actually reflects a **safety signal**: daptomycin can *induce* acute gout via rhabdomyolysis-related hyperuricaemia, and should not be interpreted as a treatment opportunity.

---

## Clinical Trial Evidence

Currently no related clinical trials are registered for any of the predicted indications (osteoarthritis, rheumatoid arthritis, osteoarthritis susceptibility, gout, or pseudoachondroplasia). Searches were conducted on ClinicalTrials.gov and WHO ICTRP as of 10 March 2026.

---

## Literature Evidence

The following publications are relevant to the predicted repurposing indications. Publications are listed with priority given to mechanistic relevance over source type.

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [39571268](https://pubmed.ncbi.nlm.nih.gov/39571268/) | 2025 | Pre-clinical Animal Study (CIA Model) | International Immunopharmacology | **Most relevant.** Daptomycin alleviates collagen-induced arthritis in mice by suppressing TNF-α, IL-1β, IL-6 and blocking NF-κB activation — first study to evaluate daptomycin's anti-inflammatory activity in an RA model |
| [40923559](https://pubmed.ncbi.nlm.nih.gov/40923559/) | 2025 | Pre-clinical Drug Discovery | Journal of Medicinal Chemistry | **Most relevant.** Five novel daptomycin-derived cyclic lipopeptides synthesised and tested; CLP-d2 outperforms daptomycin in CIA model — confirms anti-arthritis activity as a class effect of the cyclic lipopeptide scaffold |
| [23519823](https://pubmed.ncbi.nlm.nih.gov/23519823/) | 2013 | Retrospective Cohort | International Orthopaedics | High-dose daptomycin + rifampicin for Gram-positive osteoarticular infections post-surgery — context: antibiotic treatment of infection, not OA/RA treatment |
| [22511636](https://pubmed.ncbi.nlm.nih.gov/22511636/) | 2012 | Observational/Case Series | Journal of Antimicrobial Chemotherapy | Daptomycin in knee/hip periprosthetic joint infections (PJI) — context: post-arthroplasty infection management |
| [17999973](https://pubmed.ncbi.nlm.nih.gov/17999973/) | 2008 | Retrospective Cohort | Journal of Antimicrobial Chemotherapy | Daptomycin vs standard therapy for osteoarticular infections associated with *S. aureus* bacteraemia — context: infectious complication, not joint disease treatment |
| [26235888](https://pubmed.ncbi.nlm.nih.gov/26235888/) | 2015 | Retrospective Cohort | International Journal of Antimicrobial Agents | High-dose daptomycin (>6 mg/kg) for bone/joint and implant-associated infections caused by Gram-positive bacteria |
| [25650692](https://pubmed.ncbi.nlm.nih.gov/25650692/) | 2015 | Retrospective Microbiology Study | Surgical Infections | Antibiotic susceptibility profile of staphylococci in osteoarticular infections over 10 years — context: microbiology/infection management |
| [23312602](https://pubmed.ncbi.nlm.nih.gov/23312602/) | 2013 | Survey/Network Study | International Journal of Antimicrobial Agents | Survey of infectious disease physicians on PJI management; daptomycin frequently used as second-line for MRSA PJI |
| [36693494](https://pubmed.ncbi.nlm.nih.gov/36693494/) | 2023 | Case Report (Adverse Event) | The American Journal of the Medical Sciences | **Safety signal, not repurposing evidence.** Daptomycin-induced rhabdomyolysis complicated by acute gouty arthritis — daptomycin as a *trigger* for gout, not a treatment |

> **Note on osteoarthritis literature (PMIDs 23519823, 22511636, 26235888, 22854340, 17999973, 32206362, 23312602, 21477701, 25650692):** All publications describe daptomycin used to treat *bacterial infections occurring in osteoarthritis patients following joint replacement surgery*. None describe daptomycin treating osteoarthritis pathology (cartilage degeneration). The high TxGNN score for osteoarthritis is assessed as a knowledge graph concept conflation between "osteoarticular infection" and "osteoarthritis."

---

## Denmark Market Information

Daptomycin is currently **not marketed in Denmark**. There are no active Danish Medicines Agency (Laegemiddelstyrelsen) marketing authorisations.

| Marketing Authorisation | Product Name | Dosage Form | Approved Indication |
|------------------------|-------------|-------------|---------------------|
| No active Danish licences | — | — | — |

> **EMA centralised authorisation note:** Daptomycin (Cubicin®) holds a centralised EMA marketing authorisation (EU/1/05/308/001-010) for complicated skin and skin structure infections and *S. aureus* bacteraemia/right-sided infective endocarditis in adults and paediatric patients (≥1 year). Although not currently marketed in Denmark, prescribers may be able to access it via special import or individual patient access pathways when clinically indicated for its approved indications. For any repurposing purpose, separate regulatory approval would be required.

---

## Safety Considerations

**Key Warnings:**
- **Myopathy and Rhabdomyolysis**: Daptomycin can cause skeletal muscle toxicity. Creatine phosphokinase (CPK) levels must be monitored at least weekly during treatment. Unexplained muscle pain, tenderness, or weakness warrants immediate evaluation and possible discontinuation.
- **Rhabdomyolysis-induced Gout**: At least one documented case shows daptomycin-induced rhabdomyolysis leading to hyperuricaemia and acute gouty arthritis (PMID 36693494). This is particularly relevant: the TxGNN gout prediction reflects an adverse effect signal, not a therapeutic opportunity — use in gout patients should be approached with heightened vigilance.
- **Pulmonary Inefficacy**: Daptomycin is inactivated by pulmonary surfactant and must not be used for pneumonia — this limits repurposing for any pulmonary indication.

**Drug Interactions:**
No DDI data was retrieved in this evidence pack query. Based on the known SmPC, co-administration with statins or other drugs causing myopathy (e.g., cyclosporin) may increase the risk of rhabdomyolysis; temporary statin discontinuation is recommended during daptomycin therapy.

> Full prescribing safety information, including contraindications and warnings specific to the Summary of Product Characteristics (SmPC), could not be retrieved in this evidence pack (Data Gap DG001 — Laegemiddelstyrelsen SmPC not yet parsed). The EMA SmPC for Cubicin® should be consulted before any clinical use.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The sole scientifically credible repurposing signal — daptomycin as an anti-inflammatory agent in rheumatoid arthritis — is supported only by two preclinical animal studies published in 2025, with no clinical trials, no human pharmacokinetic/pharmacodynamic data for anti-inflammatory dosing, and no validated biomarker endpoint. Additionally, daptomycin's current IV-only formulation and known myotoxicity profile present serious practical barriers to use in a chronic disease such as RA. The majority of high-scoring TxGNN predictions are assessed as false positives (OA, OA susceptibility, pseudoachondroplasia) or adverse effect signals (gout), not genuine repurposing opportunities.

**To proceed to the next evaluation stage, the following is needed:**

- **Resolve Data Gap DG001**: Retrieve and parse the Cubicin SmPC (via EMA) for full safety, contraindication, and warning profile
- **Resolve Data Gap DG002**: Confirm daptomycin's anti-inflammatory MOA (NF-κB pathway) using DrugBank API and primary pharmacology databases
- **In vitro human cell studies**: Validate NF-κB suppression and cytokine inhibition in human RA synoviocytes before further investment
- **Dose-toxicity window assessment**: Determine whether anti-inflammatory-effective doses are achievable in humans without triggering myopathy (CPK elevation threshold vs. therapeutic NF-κB inhibition)
- **Route of administration feasibility**: Assess whether subcutaneous or alternative formulations of daptomycin could support chronic autoimmune disease management
- **Independent replication**: The two key preclinical studies (PMIDs 39571268 and 40923559) originate from overlapping author groups — independent replication is needed before escalating evidence evaluation
- **Systematic literature update**: Conduct a formal scoping review on daptomycin anti-inflammatory mechanisms, including potential immunomodulatory effects beyond the CIA model
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

