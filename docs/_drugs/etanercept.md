---
layout: default
title: Etanercept
parent: 僅模型預測 (L5)
nav_order: 178
evidence_level: L5
indication_count: 10
---

# Etanercept
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

# Etanercept: From Rheumatoid Arthritis to Rheumatoid Vasculitis

## One-Sentence Summary

Etanercept is a TNF-α inhibitor (soluble TNF receptor fusion protein, marketed globally as Enbrel) widely approved for rheumatoid arthritis, ankylosing spondylitis, psoriatic arthritis, juvenile idiopathic arthritis, and plaque psoriasis. The TxGNN model predicts it may be effective for **Rheumatoid Vasculitis**, with **6 clinical trials** and **20 publications** currently supporting this direction. However, the literature presents **contradictory evidence**: while TNF-α blockade may theoretically reduce vasculitis inflammation, TNF inhibitors including etanercept have also been reported to *induce* paradoxical vasculitis, warranting careful evaluation.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Rheumatoid arthritis, ankylosing spondylitis, psoriatic arthritis, juvenile idiopathic arthritis, plaque psoriasis (globally approved) |
| Predicted New Indication | Rheumatoid Vasculitis |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L3 (Systematic review and observational studies available) |
| Denmark Market Status | Not marketed (data pending — note: etanercept/Enbrel holds EMA centralised authorisation EU/1/99/126; Danish regulatory data not yet integrated) |
| Number of Marketing Authorisations | 0 (in current database) |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Etanercept is a dimeric fusion protein consisting of two linked p75 TNF receptor extracellular domains fused to the Fc portion of human IgG1. It competitively binds TNF-α and TNF-β (lymphotoxin-α), preventing them from activating cell-surface TNF receptors and thereby suppressing downstream inflammatory signalling. This mechanism has proven effective across multiple TNF-α-driven autoimmune conditions.

Rheumatoid vasculitis (RV) is one of the most severe extra-articular manifestations of rheumatoid arthritis, characterised by immune complex deposition and TNF-α–mediated endothelial injury in small and medium-sized blood vessels. Since TNF-α plays a central role in both RA joint inflammation and the vascular endothelial damage of RV, there is a reasonable mechanistic basis for predicting that etanercept may ameliorate RV by blocking this shared pathogenic cytokine.

However, the literature presents a **critical paradox**: multiple case reports and pharmacovigilance studies have documented that TNF inhibitors — including etanercept — can themselves *induce* cutaneous and systemic vasculitis (so-called "paradoxical vasculitis"). The British Society for Rheumatology Biologics Register (BSRBR-RA) has documented vasculitis-like events in TNFi-treated RA patients. This dual nature — potential therapeutic benefit versus potential induction of vasculitis — represents a major safety concern that must be carefully weighed before any clinical application.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00001901](https://clinicaltrials.gov/study/NCT00001901) | Phase 1/2 | Completed | 60 | Etanercept in Wegener's granulomatosis (ANCA-associated vasculitis). The subsequent WGET Phase 3 trial showed etanercept provided **no additional benefit** and was associated with **increased malignancy risk**. Indirect relevance to RV. |
| [NCT02590562](https://clinicaltrials.gov/study/NCT02590562) | N/A | Completed | 808 | Cross-sectional observational study of biologic DMARD treatment patterns in RA in China. May include severe RA patients with extra-articular manifestations. |
| [NCT01579006](https://clinicaltrials.gov/study/NCT01579006) | N/A | Completed | 184 | Non-interventional study of tocilizumab in RA patients with inadequate response to prior biologics including etanercept. Indirect real-world data. |
| [NCT05696106](https://clinicaltrials.gov/study/NCT05696106) | N/A | Unknown | 750,000 | Large pharmacoepidemiology study assessing risk of incident immune-mediated inflammatory diseases in biologic-treated patients. Relevant safety data. |
| [NCT01557322](https://clinicaltrials.gov/study/NCT01557322) | N/A | Completed | 1,754 | Real-world evaluation of etanercept (Enbrel) in moderate RA, from the BSRBR. Outcomes data on etanercept-treated RA patients. |
| [NCT07138898](https://clinicaltrials.gov/study/NCT07138898) | Phase 2 | Not Yet Recruiting | 80 | Immunosuppressant management in rheumatology patients undergoing shoulder arthroplasty. Not directly related to vasculitis. |

> **Note:** No clinical trials directly studying etanercept for the treatment of rheumatoid vasculitis were identified. The available trials are indirectly related through RA or other vasculitis subtypes.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33058033](https://pubmed.ncbi.nlm.nih.gov/33058033/) | 2021 | Systematic Review | Clin Rheumatol | **PRISMA systematic review on biological therapy in RV.** Reports that biological drugs (including TNF inhibitors) have been added to the RV therapeutic armamentarium, with evidence from case series. |
| [28123776](https://pubmed.ncbi.nlm.nih.gov/28123776/) | 2017 | Pharmacovigilance/Cohort | RMD Open | **BSRBR-RA data on vasculitis-like events (VLEs) with TNFi.** Compared risk of VLEs in TNFi-treated vs nbDMARD-treated RA patients. Important safety signal. |
| [28391344](https://pubmed.ncbi.nlm.nih.gov/28391344/) | 2017 | Review | Nephrol Dial Transplant | Review of TNFα blockade in ANCA-associated vasculitis. Discusses TNFα role in vasculitis pathophysiology and the mixed clinical results of TNF inhibitors. |
| [15853915](https://pubmed.ncbi.nlm.nih.gov/15853915/) | 2005 | Case Series/Mechanistic | Scand J Immunol | Reports cutaneous vasculitis associated with both etanercept and infliximab. Discusses immunologic mechanisms of TNFi-induced autoimmunity. |
| [15468348](https://pubmed.ncbi.nlm.nih.gov/15468348/) | 2004 | Review | J Rheumatol | TNF-α blockade and the risk of vasculitis — discusses paradoxical vasculitis induction by TNF inhibitors. |
| [12209493](https://pubmed.ncbi.nlm.nih.gov/12209493/) | 2002 | Case Report | Arthritis Rheum | Accelerated nodulosis and vasculitis following etanercept therapy for RA. Documents paradoxical vasculitis. |
| [11792895](https://pubmed.ncbi.nlm.nih.gov/11792895/) | 2002 | Case Report | Rheumatology | Etanercept and infliximab associated with cutaneous vasculitis in RA patients. |
| [25544845](https://pubmed.ncbi.nlm.nih.gov/25544845/) | 2014 | Case Report | Case Rep Med | Large vessel vasculitis occurring in RA patient under anti-TNF therapy. Highlights drug-induced vasculitis risk. |
| [15801034](https://pubmed.ncbi.nlm.nih.gov/15801034/) | 2005 | Case Report | J Rheumatol | Proliferative lupus nephritis and leukocytoclastic vasculitis during etanercept treatment. |
| [19648728](https://pubmed.ncbi.nlm.nih.gov/19648728/) | 2009 | Case Report | Dermatology | Disseminated herpes zoster mimicking rheumatoid vasculitis in an RA patient on etanercept — illustrates diagnostic challenges under immunosuppression. |

> **Critical observation:** The majority of the identified literature describes etanercept as a potential *cause* of vasculitis (paradoxical vasculitis) rather than as a treatment. Only the systematic review (PMID 33058033) directly evaluates biological therapy as treatment for RV.

---

## Denmark Market Information

Etanercept is not currently captured in the DkTxGNN regulatory database. However, etanercept (Enbrel) holds a centralised European Medicines Agency (EMA) marketing authorisation (EU/1/99/126) and is available in Denmark through this authorisation. Multiple biosimilars (Benepali, Erelzi, etc.) are also authorised.

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EU/1/99/126 (EMA) | Enbrel (etanercept) | Solution for injection (prefilled syringe/pen) | RA, JIA, PsA, axial SpA, plaque psoriasis |
| EU/1/15/1074 (EMA) | Benepali (etanercept biosimilar) | Solution for injection | All reference etanercept indications |

> *Note: The above are based on known EMA authorisations. Local DkTxGNN database integration for Danish-specific regulatory data is pending.*

---

## Safety Considerations

- **Paradoxical vasculitis:** Multiple case reports and pharmacovigilance studies have documented TNF inhibitor-induced vasculitis (cutaneous leukocytoclastic vasculitis, large vessel vasculitis, lupus-like syndromes) as a known adverse effect of etanercept. This is directly relevant to the predicted indication and represents a significant safety concern.
- **Infection risk:** TNF-α inhibition increases susceptibility to serious infections including tuberculosis reactivation, opportunistic infections, and atypical presentations (e.g., disseminated herpes zoster).
- **Malignancy risk:** The WGET trial (follow-up to NCT00001901) found increased solid tumour malignancies in etanercept-treated vasculitis patients, which led to safety concerns about TNFi use in vasculitis.

> For complete prescribing information, please refer to the approved Summary of Product Characteristics (SmPC) for Enbrel or the relevant biosimilar.

---

## Additional TxGNN Predictions

The TxGNN model also predicted the following indications for etanercept. Of note, two of these are **already globally approved indications**, validating the model's predictive capability:

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Recommendation | Note |
|------|---------------------|-------------|---------------|----------------|------|
| 1 | Rheumatoid Vasculitis | 99.71% | L3 | Proceed with Guardrails | Novel prediction — contradictory evidence |
| 3 | Hypermobility of Coccyx | 99.63% | L5 | Hold | No mechanistic rationale; structural/biomechanical condition |
| 5 | **Inflammatory Spondylopathy** | 99.57% | **L1** | Proceed with Guardrails | **Already approved globally** (FDA 2003 for AS); 50+ clinical trials, multiple Phase 3 RCTs |
| 7 | Kümmell Disease | 99.55% | L5 | Hold | No mechanistic rationale; post-traumatic vertebral avascular necrosis |
| 9 | **Polyarticular Juvenile Rheumatoid Arthritis** | 99.50% | **L1** | Proceed with Guardrails | **Already approved globally** (FDA 1999 for pJIA); landmark NEJM RCT (Lovell et al., 2000) |

> The model's correct prediction of two already-approved indications (inflammatory spondylopathy and pJIA) at high confidence scores provides validation of TxGNN's methodology. However, the model also predicted two indications (hypermobility of coccyx, Kümmell disease) with no mechanistic basis, highlighting the need for expert clinical review of all predictions.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
While the TxGNN prediction score is very high (99.71%) and a systematic review of biological therapy in rheumatoid vasculitis exists, the evidence is predominantly observational and, critically, a substantial body of literature documents etanercept as a potential *cause* of vasculitis rather than a treatment. The negative results of the WGET trial (etanercept in Wegener's granulomatosis showed no benefit and increased malignancy) raise further concerns. This prediction requires very careful safety evaluation before any clinical consideration.

**To proceed, the following is needed:**
- Full analysis of the systematic review (PMID 33058033) to determine which specific biological agents showed benefit in RV and whether etanercept was among them
- Detailed review of BSRBR-RA pharmacovigilance data (PMID 28123776) to quantify the absolute risk of vasculitis-like events with etanercept versus other TNFi
- Mechanism of action data to clarify the paradox of TNF-α blockade potentially both treating and inducing vasculitis
- Integration of Danish (Laegemiddelstyrelsen/EMA) regulatory data including the full SmPC warnings and contraindications
- Expert rheumatology consensus on whether TNFi-induced vasculitis and rheumatoid vasculitis share distinct or overlapping pathogenic mechanisms
- Safety monitoring protocol addressing malignancy risk (per WGET trial findings) if clinical investigation proceeds

---

> **Disclaimer:** This report is for research purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before any therapeutic application. All treatment decisions should be made by qualified healthcare professionals based on approved product information and individual patient assessment.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

