---
layout: default
title: Golimumab
parent: 僅模型預測 (L5)
nav_order: 211
evidence_level: L5
indication_count: 10
---

# Golimumab
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

# Golimumab: From Rheumatoid Arthritis to Rheumatoid Vasculitis

## One-Sentence Summary

Golimumab (Simponi, DrugBank: DB06674) is a fully human anti-TNF-α monoclonal antibody approved in the EU and the US for the treatment of rheumatoid arthritis, psoriatic arthritis, and ankylosing spondylitis.
The TxGNN model predicts it may be effective for **Rheumatoid Vasculitis** with a prediction confidence of **99.73%**; however, current evidence consists of only **6 background publications** — no randomised controlled trials directly targeting this specific indication have been identified.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Rheumatoid arthritis, psoriatic arthritis, ankylosing spondylitis (EMA-approved; no marketing authorisation found in Denmark) |
| Predicted New Indication | Rheumatoid Vasculitis |
| TxGNN Prediction Score | 99.73% |
| Evidence Level | L4 (mechanistic/indirect evidence only) |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Although detailed mechanism of action data could not be retrieved from the local database, Golimumab is a well-characterised fully human IgG1κ monoclonal antibody that binds to both soluble and transmembrane forms of tumour necrosis factor-alpha (TNF-α). By blocking TNF-α from engaging its receptors (TNFR1 and TNFR2), Golimumab suppresses NF-κB activation and the downstream inflammatory cascade responsible for tissue destruction in chronic immune-mediated diseases. This mechanism is the basis for its approval in rheumatoid arthritis, psoriatic arthritis, and ankylosing spondylitis.

Rheumatoid vasculitis is a severe extra-articular complication of long-standing, seropositive RA. The pathology is characterised by systemic inflammation of the vessel wall — driven by excessive TNF-α activity, immune complex deposition, and neutrophil infiltration. The mechanistic rationale for extending Golimumab to this indication is therefore biologically coherent: suppressing TNF-α could theoretically attenuate the same inflammatory cascade that causes vasculitic lesions, in the same patient population already treated for their underlying RA.

Importantly, indirect evidence in the literature (PMID 29075910) documents that the introduction of anti-TNF biological agents into RA practice has been associated with a reduction in the incidence of rheumatoid vasculitis. Individual case reports also describe Golimumab being used off-label in other immune-mediated vasculitic conditions (Behçet-associated uveitis, PMID 23252659), providing further biological plausibility. However, no dedicated randomised controlled trial of Golimumab specifically for rheumatoid vasculitis exists. The TxGNN model's high prediction score most likely reflects the tight pathological proximity between RA and rheumatoid vasculitis within the knowledge graph rather than direct clinical efficacy data.

---

## Clinical Trial Evidence

No clinical trials directly evaluating Golimumab for rheumatoid vasculitis were identified. The three trials retrieved provide only indirect background context on biological therapy use in RA-related conditions.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT01579006](https://clinicaltrials.gov/study/NCT01579006) | N/A | Completed | 184 | Multinational observational study of Tocilizumab (not Golimumab) in RA patients with inadequate response to non-biological DMARDs or one biological agent; provides real-world context on biological use in RA but does not address rheumatoid vasculitis as an endpoint |
| [NCT05696106](https://clinicaltrials.gov/study/NCT05696106) | N/A | Unknown | 750,000 | Large retrospective observational study examining the risk of developing additional immune-mediated inflammatory diseases (IMIDs) in patients already treated with biologics or immunosuppressants for a single IMID; broad safety background, not specific to vasculitis efficacy |
| [NCT07138898](https://clinicaltrials.gov/study/NCT07138898) | Phase 2 | Not yet recruiting | 80 | Evaluates perioperative immunosuppressant management strategies in rheumatology patients undergoing elective shoulder arthroplasty; not relevant to vasculitis efficacy |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [29075910](https://pubmed.ncbi.nlm.nih.gov/29075910/) | 2018 | Case Report | Rheumatology International | Reports pyoderma gangrenosum and septic arthritis as severe sepsis in a Golimumab-treated RA patient; importantly notes that introduction of anti-TNF agents has historically reduced the incidence of rheumatoid vasculitis in seropositive RA — indirect support for TNF-α blockade in vasculitis prevention |
| [23252659](https://pubmed.ncbi.nlm.nih.gov/23252659/) | 2013 | Case Report | Ocular Immunol Inflamm | Behçet disease-associated uveitis (an immune-mediated vasculitic condition) successfully treated with Golimumab after failure of other anti-TNF agents; supports off-label use of Golimumab in vasculitic manifestations beyond approved indications |
| [22999907](https://pubmed.ncbi.nlm.nih.gov/22999907/) | 2013 | Case Report | Joint Bone Spine | Two cases of Takayasu's arteritis (large vessel vasculitis) emerging paradoxically during anti-TNF therapy; while encouraging results support anti-TNF in relapsing Takayasu's arteritis, this report raises awareness of paradoxical inflammatory reactions — a relevant safety signal |
| [31491879](https://pubmed.ncbi.nlm.nih.gov/31491879/) | 2019 | Network Meta-analysis | Int J Mol Sci | Network meta-analysis of 36 RCTs comparing five TNF inhibitors (including Golimumab) versus methotrexate on radiographic joint destruction in RA; confirms class-level anti-TNF efficacy but does not address vasculitis as an endpoint |
| [23557513](https://pubmed.ncbi.nlm.nih.gov/23557513/) | 2013 | Narrative Review | BMC Medicine | Overview of biologic therapies for autoimmune diseases; discusses the broader anti-TNF class, including mechanism and clinical use in rheumatologic diseases, providing contextual background for repurposing considerations |
| [27591827](https://pubmed.ncbi.nlm.nih.gov/27591827/) | 2017 | Observational Cohort | Semin Arthritis Rheum | Describes frequency and causes of end-stage renal disease in RA, with reference to systemic RA complications including vasculitis; contextualises the disease burden of RA extra-articular manifestations |

---

## Denmark Market Information

No marketing authorisations for Golimumab were identified in the Danish Medicines Agency (Laegemiddelstyrelsen) database at the time of this evaluation (0 licences, status: not marketed).

It should be noted that Golimumab (Simponi®) holds a valid centralised EMA marketing authorisation for rheumatoid arthritis, psoriatic arthritis, and axial spondyloarthritis in adults, as well as for polyarticular-course juvenile idiopathic arthritis in children. Prescribers should verify current market availability and reimbursement status in Denmark directly via the EMA product register or Medicinrådet.

---

## Safety Considerations

No safety data (key warnings, contraindications, or drug interactions) are available in the current data extract for Golimumab.

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model assigns a high mechanistic plausibility score (99.73%) based on the shared TNF-α-driven pathology between RA and rheumatoid vasculitis, but the current evidence base is rated L4 — no clinical trials have directly tested Golimumab in rheumatoid vasculitis, and published support is limited to indirect case reports and observational background data. This is insufficient to advance without additional evidence.

**To proceed, the following is needed:**
- Targeted systematic literature review on anti-TNF treatment of established rheumatoid vasculitis, including case series and retrospective cohort data from the broader TNF inhibitor class
- Retrieval of Golimumab SmPC safety data (key warnings, contraindications, drug interactions) to enable full benefit-risk assessment — currently a blocking data gap (DG001)
- DrugBank MOA data retrieval to formally document the mechanism of action (DG002)
- Assessment of whether an investigator-initiated observational study or registry could capture Golimumab use in RA patients with vasculitic complications in Scandinavia
- Verification of Golimumab market availability and national reimbursement conditions in Denmark via Medicinrådet before any clinical programme is proposed

> **Note:** Two other predicted indications in this evidence pack have substantially stronger evidence and should be prioritised for near-term clinical evaluation: **Inflammatory Spondylopathy** (rank 5/6, L1 evidence, multiple completed Phase 3 RCTs, recommendation: Proceed with Guardrails) and **Polyarticular Juvenile Rheumatoid Arthritis** (rank 9/10, L2 evidence, one completed Phase 3 trial, recommendation: Proceed with Guardrails).

---

*This report is generated for research purposes only and does not constitute medical advice. All drug repurposing candidates require prospective clinical validation before clinical application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

