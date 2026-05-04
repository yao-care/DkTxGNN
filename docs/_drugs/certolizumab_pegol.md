---
layout: default
title: Certolizumab Pegol
parent: 僅模型預測 (L5)
nav_order: 105
evidence_level: L5
indication_count: 10
---

# Certolizumab Pegol
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

# Certolizumab Pegol: From Rheumatoid Arthritis to Rheumatoid Vasculitis

---

## One-Sentence Summary

Certolizumab pegol (Cimzia®) is a PEGylated anti-TNF-α biologic agent approved internationally for rheumatoid arthritis (RA), Crohn's disease, psoriatic arthritis, and axial spondyloarthritis.
The TxGNN model predicts it may be effective for **Rheumatoid Vasculitis**, with a prediction score of **99.78%**.
However, current supporting evidence is limited to **3 indirectly relevant clinical trials** and **8 case reports or small observational studies** — and critically, the majority of the literature identifies CZP as a **cause** of drug-induced vasculitis rather than a treatment, creating a fundamental pharmacological paradox.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Rheumatoid arthritis and other inflammatory autoimmune diseases (inferred from published literature; no source regulatory data available in this dataset) |
| Predicted New Indication | Rheumatoid Vasculitis |
| TxGNN Prediction Score | 99.78% |
| Evidence Level | L4 (preclinical/mechanistic studies; no dedicated RCTs) |
| Denmark Market Status | Not marketed in Denmark (per current dataset — see note below) |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | **Hold** |

> **⚠️ Data note on Denmark market status**: Certolizumab pegol (Cimzia®) holds a centralised EMA marketing authorisation (EU/1/09/544) valid across all EU/EEA member states, including Denmark. The "not marketed" status and zero licences in this dataset likely reflect a data gap rather than actual unavailability. Please verify current authorisation status with the Danish Medicines Agency (Lægemiddelstyrelsen) or via the EMA medicines database before acting on this information.

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data was not available in the current evidence pack. Based on published literature, certolizumab pegol (CZP) is a PEGylated antigen-binding Fab' fragment of a recombinant humanised monoclonal antibody that selectively neutralises both soluble and transmembrane forms of TNF-α. Unlike conventional TNF inhibitors, CZP lacks the Fc region, which prevents complement fixation and Fc-receptor-mediated cytotoxicity. PEGylation extends the circulating half-life, and importantly, CZP does not actively cross the placenta — a clinically meaningful distinction for women of childbearing age.

The theoretical rationale for repurposing CZP in rheumatoid vasculitis rests on the central role of TNF-α in driving endothelial inflammation in RA-associated extra-articular manifestations. In rheumatoid vasculitis, TNF-α promotes vascular wall inflammation, endothelial activation, and immune complex deposition in vessel walls. Blocking TNF-α could, in theory, suppress this inflammatory cascade and prevent the ischaemic tissue damage — including leg ulcers — that characterises the condition. One published case report (PMID 34786446) documents apparent therapeutic benefit of CZP specifically for leg ulcers due to rheumatoid vasculitis, lending limited clinical face validity to the hypothesis.

However, a critical and well-documented paradox severely limits this repurposing rationale: anti-TNF therapy, including CZP, is a recognised **cause** of drug-induced vasculitis. The mechanism involves TNF-α blockade-induced immune dysregulation, immune complex deposition, and complement activation, resulting in leukocytoclastic vasculitis, hypocomplementemic urticarial vasculitis, and medium-vessel vasculitis as paradoxical adverse drug reactions. Six of the eight identified publications describe CZP-related vasculitis as an adverse event, not a treatment outcome. This paradoxical inflammation represents the dominant safety signal in the current evidence base and substantially undermines the repurposing case.

---

## Clinical Trial Evidence

No clinical trials directly evaluating certolizumab pegol as a treatment for rheumatoid vasculitis were identified. The three retrieved trials are indirectly related and all carry a Grade C relevance rating:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01579006](https://clinicaltrials.gov/study/NCT01579006) | N/A | Completed | 184 | Multinational observational study of tocilizumab (not CZP) in RA patients with inadequate response to DMARDs or one biologic; provides indirect safety background but vasculitis was not a primary endpoint |
| [NCT05696106](https://clinicaltrials.gov/study/NCT05696106) | N/A | Unknown | 750,000 | Large observational study examining risk of incident immune-mediated inflammatory diseases (IMIDs) in patients receiving biologics or immunosuppressants for a single IMID; scope is far too broad, vasculitis not a primary treatment endpoint |
| [NCT07138898](https://clinicaltrials.gov/study/NCT07138898) | Phase 2 | Not Yet Recruiting | 80 | Perioperative management of immunosuppressants in rheumatology patients undergoing elective total shoulder arthroplasty; no direct relevance to vasculitis treatment |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [34786446](https://pubmed.ncbi.nlm.nih.gov/34786446/) | 2021 | Case Report | JAAD Case Reports | CZP treatment for leg ulcers due to rheumatoid vasculitis — the **only report suggesting therapeutic benefit**; supports biological plausibility but evidence weight is limited |
| [36597972](https://pubmed.ncbi.nlm.nih.gov/36597972/) | 2022 | Retrospective Cohort | RMD Open | Long-term follow-up of CZP in uveitis due to IMIDs; multicentre study of 80 patients; demonstrates broader anti-inflammatory activity of CZP in extra-articular immune-mediated conditions |
| [36418084](https://pubmed.ncbi.nlm.nih.gov/36418084/) | 2022 | Pharmacovigilance Review | RMD Open | Infection profile of immune-modulatory drugs based on SmPC data; highlights serious infection risk relevant to vasculitis patients who are already immunocompromised |
| [29610119](https://pubmed.ncbi.nlm.nih.gov/29610119/) | 2018 | Retrospective Review / ADR | Clinical Medicine & Research | Single-centre review of biologic agent-associated cutaneous adverse events; vasculitis identified as a recurring cutaneous ADR pattern across anti-TNF agents |
| [31990069](https://pubmed.ncbi.nlm.nih.gov/31990069/) | 2020 | Case Report / ADR | J Clin Pharmacy & Therapeutics | Development of hypocomplementemic urticarial vasculitis **during** CZP treatment for RA — first reported association between CZP and HUV; underscores the paradoxical vasculitis risk |
| [28405087](https://pubmed.ncbi.nlm.nih.gov/28405087/) | 2017 | Case Report / ADR | Proc (Baylor Univ Med Center) | Leukocytoclastic vasculitis drug reaction to CZP — first reported case of this ADR specifically with CZP; highlights that this anti-TNF class effect extends to CZP |
| [41158918](https://pubmed.ncbi.nlm.nih.gov/41158918/) | 2025 | Case Report / ADR | Cureus | Anti-TNF-related medium-vessel vasculitis in a patient switched to CZP for seronegative RA; rare but serious adverse event; underscores the need for careful patient selection |
| [32687015](https://pubmed.ncbi.nlm.nih.gov/32687015/) | 2021 | Case Report / ADR | Modern Rheumatology Case Reports | Rapidly progressive glomerulonephritis after CZP initiation in a 30-year-old woman with RA; illustrates paradoxical autoimmune induction by TNF inhibition, including renal vasculitis involvement |

> **Critical signal**: 6 of 8 publications describe vasculitis as an **adverse drug reaction** to CZP or anti-TNF therapy in general, not as a therapeutic target. Only 1 publication documents potential therapeutic benefit (PMID 34786446).

---

## Denmark Market Information

No marketing authorisations for certolizumab pegol were found in the current Danish regulatory dataset (0 licences, status: not marketed).

As noted above, this almost certainly reflects a data gap. Cimzia® (certolizumab pegol) is authorised in the EU via EMA centralised procedure and should be available in Denmark. Please consult the Lægemiddelstyrelsen's product database or the EMA's medicines registry for current authorisation details, approved indications, and the Danish Summary of Product Characteristics (produktresumé).

---

## Safety Considerations

Formal safety data (key warnings, contraindications, drug-drug interactions) was not available in the current evidence pack. The following safety signals are specifically relevant to this repurposing hypothesis and are drawn from the retrieved literature:

- **Drug-induced vasculitis (Paradoxical ADR)**: Anti-TNF agents including CZP have been associated with leukocytoclastic vasculitis, hypocomplementemic urticarial vasculitis, and medium-vessel vasculitis as paradoxical adverse drug reactions. This is not merely a theoretical concern — it is documented in multiple case reports including with CZP specifically. Clinicians considering CZP in vasculitis-prone patients must weigh this risk carefully.
- **Serious infections**: As a biologic immunosuppressant, CZP carries a well-established risk of serious and opportunistic infections, including tuberculosis reactivation. Screening protocols (TB test, hepatitis B serology) apply.
- **Paradoxical autoimmune reactions**: Additional paradoxical reactions reported include psoriasiform eruptions, rapidly progressive glomerulonephritis, and drug-induced lupus. These are of particular relevance when treating patients with complex autoimmune overlap, as may be seen in rheumatoid vasculitis.

Please refer to the approved Summary of Product Characteristics (SmPC/produktresumé) for complete safety, contraindication, and interaction information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence for certolizumab pegol as a treatment for rheumatoid vasculitis is insufficient (Evidence Level L4 — mechanistic rationale and isolated case reports only), and critically, the body of evidence predominantly identifies CZP as a **cause** of drug-induced vasculitis rather than a treatment. This paradox — where the proposed therapeutic agent can also trigger the target condition — represents a fundamental barrier to clinical development without substantially more data to identify which patients might benefit versus be harmed.

**To proceed, the following would be needed:**

- **Safety data gap resolution**: Obtain and review the full EMA/Danish SmPC for Cimzia® to document key warnings and contraindications — this is currently a blocking data gap (DG001)
- **MOA documentation**: Retrieve complete mechanism of action data from DrugBank (DB08904) to formally characterise the biological plausibility pathway (DG002)
- **Dedicated vasculitis evidence**: A systematic case series or prospective observational cohort specifically examining CZP efficacy in established rheumatoid vasculitis (distinct from RA in general) is needed to move beyond anecdote
- **Paradox resolution**: Identification of biomarkers or clinical features that distinguish patients likely to benefit from those at risk of anti-TNF-induced vasculitis — this is essential before any prospective study design
- **Denmark market status verification**: Confirm current authorisation details and approved indications with Lægemiddelstyrelsen or via the EMA medicines database
- **Regulatory context review**: Assess whether rheumatoid vasculitis could be addressed within the existing RA label (as a manifestation) rather than requiring a separate repurposing pathway

---

*⚠️ Disclaimer: This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before therapeutic application. All website and report content is subject to YMYL (Your Money or Your Life) standards and must not be used as the basis for clinical decision-making without consultation of the approved product information and current clinical guidelines.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

