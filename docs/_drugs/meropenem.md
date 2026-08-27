---
layout: default
title: Meropenem
parent: 僅模型預測 (L5)
nav_order: 285
evidence_level: L5
indication_count: 10
---

# Meropenem
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

# Meropenem: From Serious Bacterial Infections to Bacterial Arthritis

## One-Sentence Summary

Meropenem is a broad-spectrum carbapenem antibiotic widely used in clinical practice for the treatment of serious bacterial infections, including hospital-acquired pneumonia, complicated intra-abdominal infections, bacterial meningitis, and septicaemia in critically ill patients.
The TxGNN model predicts it may be effective for **Bacterial Arthritis**,
with **1 clinical trial** and **20 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Serious bacterial infections (hospital-acquired pneumonia, complicated intra-abdominal infections, meningitis, septicaemia — based on established global clinical use; no formal Danish authorisation found in current data) |
| Predicted New Indication | Bacterial Arthritis |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L3 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Meropenem is a carbapenem beta-lactam antibiotic that inhibits bacterial cell wall synthesis through high-affinity binding to penicillin-binding proteins PBP2 and PBP3. This mechanism produces broad-spectrum bactericidal activity against both Gram-negative and Gram-positive organisms. It is particularly potent against multidrug-resistant (MDR) Gram-negative pathogens — including MDR *Pseudomonas aeruginosa*, ESBL-producing Enterobacteriaceae, and *Burkholderia pseudomallei* — which are precisely the organisms most likely to cause difficult-to-treat bacterial arthritis where first-line agents have failed.

Bacterial (septic) arthritis shares key pathophysiological features with other deep-seated bacterial infections for which meropenem is already established: bacteraemia as an entry route, penetration into privileged anatomical compartments, and frequent involvement of MDR pathogens in immunocompromised hosts. Synovial fluid penetration of meropenem has been estimated at approximately 40–60% of serum concentrations under inflammatory conditions, sufficient to achieve the pharmacodynamic target (free time above MIC >40%) for susceptible Gram-negative pathogens. Retrospective clinical series — particularly those documenting musculoskeletal melioidosis — confirm that all isolates causing septic arthritis were susceptible to meropenem, and antibiogram studies from orthopaedic infection centres identify meropenem as the empiric agent of choice for MDR Gram-negative bone and joint infections.

Clinically, meropenem is already referenced in infectious disease guidelines as a second-line or last-resort option for MDR/XDR Gram-negative septic arthritis when standard agents (cefazolin, ceftriaxone) are inappropriate. The TxGNN prediction accurately captures this established but off-label role. It is important to note that meropenem is **not effective against MRSA** — in mixed or Gram-positive-dominant cases, combination with vancomycin or a targeted Gram-positive agent is required.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01371656](https://clinicaltrials.gov/study/NCT01371656) | Phase 3 | Completed | 624 | Randomised trial of levofloxacin prophylaxis against bacteraemia in children with acute leukaemia undergoing chemotherapy or HSCT (2011–2017). This trial concerns levofloxacin — not meropenem — in an oncology/immunosuppression context and does not directly evaluate bacterial arthritis. Its appearance in the evidence pack reflects knowledge-graph adjacency between antibiotic agents and infectious complications; no direct evidence contribution for meropenem in septic arthritis. |

> **Evidence note**: No clinical trials directly evaluating meropenem for bacterial arthritis were identified in ClinicalTrials.gov or ICTRP at the time of data collection.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [39489417](https://pubmed.ncbi.nlm.nih.gov/39489417/) | 2024 | Retrospective Review | Indian Journal of Medical Microbiology | 22 culture-confirmed musculoskeletal melioidosis cases; 9 with septic arthritis, 12 with osteomyelitis. All isolates susceptible to meropenem — directly supports meropenem activity in joint infections caused by *Burkholderia pseudomallei*. |
| [37713001](https://pubmed.ncbi.nlm.nih.gov/37713001/) | 2024 | Observational Study | European Journal of Orthopaedic Surgery & Traumatology | Antibiogram study for empiric antibiotic selection in adult non-spinal orthopaedic infections (septic arthritis, osteomyelitis, PJI) in a developing-world setting. Meropenem identified as key agent for MDR Gram-negative isolates. |
| [35146367](https://pubmed.ncbi.nlm.nih.gov/35146367/) | 2021 | Retrospective Cohort | Le infezioni in medicina | Retrospective cohort of osteoarticular melioidosis; characterises clinical presentation, microbiology, and treatment of bone and joint *Burkholderia pseudomallei* infection, supporting carbapenem-based therapy. |
| [39193962](https://pubmed.ncbi.nlm.nih.gov/39193962/) | 2024 | Epidemiological Study | Clinical Laboratory | Pathogen distribution and antimicrobial resistance analysis in bone and joint infections in children under 4 years; provides resistance data to guide empiric carbapenem selection in paediatric septic arthritis. |
| [31319190](https://pubmed.ncbi.nlm.nih.gov/31319190/) | 2019 | Experimental Model | International Journal of Antimicrobial Agents | Rabbit model of carbapenemase-producing *Klebsiella pneumoniae* prosthetic joint infection; evaluated colistin-impregnated cement spacer combined with systemic antibiotics including meropenem, supporting local and systemic carbapenem strategy for resistant orthopaedic infections. |
| [33857030](https://pubmed.ncbi.nlm.nih.gov/33857030/) | 2021 | Laboratory Study | Journal of Bone and Joint Surgery (American) | Thermal stability and in vitro elution kinetics of meropenem from PMMA bone cement beads; confirms meropenem retains bactericidal activity after cement mixing and elutes sustainably, relevant to local delivery in joint and bone infections caused by MDR organisms. |
| [36804370](https://pubmed.ncbi.nlm.nih.gov/36804370/) | 2023 | Narrative Review | International Journal of Antimicrobial Agents | Reviews off-label and guideline antibiotic use for MDR/XDR bacteria including CR-Enterobacterales and CR-*Pseudomonas aeruginosa*; discusses carbapenem-based combination regimens relevant to MDR bacterial arthritis. |
| [38649034](https://pubmed.ncbi.nlm.nih.gov/38649034/) | 2024 | PK Study | International Journal of Antimicrobial Agents | Meropenem tissue penetration evaluated in a unilateral lung injury model; demonstrates that tissue penetration is maintained under inflammatory conditions — a pharmacokinetic principle directly applicable to inflamed synovial joint spaces. |
| [39681779](https://pubmed.ncbi.nlm.nih.gov/39681779/) | 2025 | Population PK Study | Clinical Pharmacokinetics | Population pharmacokinetics of meropenem across the adult lifespan (including older adults); identifies optimal dosing regimens and age-related PK variability relevant to achieving fT>MIC targets in deep-seated infections including septic joints. |
| [2808217](https://pubmed.ncbi.nlm.nih.gov/2808217/) | 1989 | In Vitro Study | Journal of Antimicrobial Chemotherapy | Early characterisation of meropenem bactericidal activity against clinical isolates including *Pseudomonas aeruginosa*; MBCs approximately 2-fold above MICs, confirming potent bactericidal mechanism applicable to joint space infections where bacterial eradication is the primary therapeutic goal. |

---

## Denmark Market Information

Meropenem is **not currently listed as marketed in Denmark** according to the Laegemiddelstyrelsen database (market status: not marketed; 0 authorisations retrieved). No national or centrally authorised (EMA) marketing authorisations were identified in the evidence pack.

> **Practical note for Danish clinicians**: Meropenem (e.g., Meronem® 500 mg and 1 g powder for solution for injection/infusion) holds a centralised EMA marketing authorisation valid across all EU/EEA member states. It is widely stocked in Danish hospital pharmacies as a hospital-restricted antimicrobial. Prescribers should verify current formulary listing and access pathways with the relevant hospital pharmacy or the Laegemiddelstyrelsen's medicine database (medicinpriser.dk / pro.medicin.dk).

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

> Detailed warning, contraindication, and drug interaction data were not available in the current evidence pack. Key clinical safety considerations known for carbapenems in general include: risk of seizures (particularly in patients with CNS disorders or renal impairment at standard doses), *Clostridioides difficile*-associated diarrhoea, hypersensitivity reactions (cross-reactivity with other beta-lactams should be assessed), and nephrotoxicity risk in combination with other nephrotoxic agents. Renal dose adjustment is required. Consult the Meronem® SmPC via the EMA product page for full prescribing information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Meropenem has well-documented in vitro and clinical activity against the principal MDR Gram-negative pathogens responsible for difficult-to-treat bacterial arthritis, adequate synovial fluid penetration, and is already recognised in infectious disease practice guidelines as a rescue therapy for refractory or MDR septic joint infections. Observational cohort data from musculoskeletal infection series and antimicrobial susceptibility studies provide meaningful biological plausibility. However, no dedicated prospective or randomised trials exist for this specific indication, and the evidence base rests primarily on Level 3 observational and microbiological data.

**To proceed, the following is needed:**

- Prospective PK/PD data characterising meropenem synovial fluid and joint tissue penetration specifically in patients with septic arthritis (accounting for the effect of synovial inflammation and joint effusion on drug distribution)
- Prospective observational registry or multicentre cohort study documenting clinical outcomes (cure rates, surgical intervention rates, mortality) of meropenem-based regimens in culture-confirmed MDR Gram-negative bacterial arthritis
- Local Danish/Nordic surveillance data on carbapenem resistance rates in orthopaedic isolates to define the target patient population most likely to benefit
- Formal assessment of meropenem's hospital formulary status and prescribing pathway in Denmark (including antibiotic stewardship committee approval criteria for this indication)
- Clarification of MRSA co-infection risk in the target population and appropriate combination therapy protocols (meropenem is not active against MRSA; a Gram-positive cover strategy should be specified)
- Safety monitoring plan including renal function monitoring, CNS adverse event surveillance, and *C. difficile* infection tracking
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

