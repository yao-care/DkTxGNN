---
layout: default
title: Adalimumab
parent: 僅模型預測 (L5)
nav_order: 16
evidence_level: L5
indication_count: 10
---

# Adalimumab
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

# Adalimumab: From Rheumatoid Arthritis to Rheumatoid Vasculitis

## One-Sentence Summary

Adalimumab (Humira®) is a fully human anti-TNF-α monoclonal antibody globally approved for the treatment of rheumatoid arthritis and other chronic inflammatory diseases, with no current marketing authorisation recorded in the Danish regulatory database.
The TxGNN model predicts it may be effective for **Rheumatoid Vasculitis**,
with **5 clinical trials** and **20 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Rheumatoid arthritis (globally approved; no marketing authorisation currently recorded in Danish regulatory data) |
| Predicted New Indication | Rheumatoid Vasculitis |
| TxGNN Prediction Score | 99.80% |
| Evidence Level | L3 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known information, adalimumab is a fully human IgG1 monoclonal antibody that targets tumour necrosis factor-alpha (TNF-α). It works by blocking both soluble and membrane-bound TNF-α from binding to its receptors (p55 and p75), thereby suppressing the NF-κB signalling pathway and reducing the downstream cascade of pro-inflammatory cytokines including IL-1β, IL-6, and IL-8. This core mechanism underlies its established use in conditions such as rheumatoid arthritis, psoriatic arthritis, ankylosing spondylitis, and inflammatory bowel disease.

Rheumatoid vasculitis (RV) is one of the most severe extra-articular manifestations of long-standing, seropositive rheumatoid arthritis, typically affecting small and medium-sized blood vessels. Its pathogenesis shares the same central inflammatory driver as RA: immune complex deposition in vessel walls combined with TNF-α overexpression jointly drives vascular wall damage, endothelial cell activation, and complement cascade activation. Because adalimumab directly neutralises this key cytokine, the mechanistic basis for its application in RV is biologically coherent and follows directly from its established mode of action in RA.

A 2021 systematic review specifically addressing the role of biological agents in RV (PMID 33058033) documented the use of TNF inhibitors including adalimumab in this condition. A case report (PMID 25133007) described a patient with long-standing RA and digital vasculitis with necrotising fingertip ulcers who responded well to adalimumab after conventional therapy failed. Conversely, a case of acute pulmonary hypertension crisis following adalimumab dose reduction in established RV (PMID 30773522) simultaneously confirms the drug's activity in this condition and highlights the serious clinical consequences of treatment interruption — reinforcing the need for careful dose management if adalimumab is used for RV.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02590562](https://clinicaltrials.gov/study/NCT02590562) | N/A | Completed | 808 | Multi-centre cross-sectional study of biological DMARD treatment patterns (including adalimumab) in Chinese RA patients; provides real-world context on biologic use across the RA disease spectrum, indirectly relevant to RV management |
| [NCT01579006](https://clinicaltrials.gov/study/NCT01579006) | N/A | Completed | 184 | Non-interventional observational study of tocilizumab in RA patients with inadequate response to prior biologics including adalimumab; 6-month follow-up provides safety and effectiveness data in a population that may include patients with extra-articular manifestations such as RV |
| [NCT05696106](https://clinicaltrials.gov/study/NCT05696106) | N/A | Unknown | 750,000 | Large retrospective epidemiological study assessing the risk of incident immune-mediated inflammatory diseases (IMID) in patients treated with biologics; provides population-level context on inflammatory disease progression under biologic therapy |
| [NCT07138898](https://clinicaltrials.gov/study/NCT07138898) | Phase 2 | Not yet recruiting | 80 | Evaluates perioperative immunosuppressant management in rheumatology patients undergoing elective shoulder arthroplasty; includes anti-TNF agents and provides safety data on treatment interruption in rheumatologic disease |
| [NCT05111743](https://clinicaltrials.gov/study/NCT05111743) | N/A | Completed | 9,261 | Retrospective real-world cohort of brolucizumab for neovascular AMD; low direct relevance to adalimumab in RV — likely matched by inflammatory or neovascular keyword overlap |

> **Note**: No direct randomised controlled trials specifically evaluating adalimumab for rheumatoid vasculitis were identified in the current search. All trials above are indirectly relevant. Evidence for this indication rests primarily on observational studies and case-level literature.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33058033](https://pubmed.ncbi.nlm.nih.gov/33058033/) | 2021 | Systematic Review | Clinical Rheumatology | PRISMA-compliant systematic review on biological agents (TNF inhibitors, rituximab, tocilizumab) in RV; confirms that biologics including adalimumab are being incorporated into the therapeutic armamentarium for this severe RA complication, with significant associated morbidity and mortality |
| [34068884](https://pubmed.ncbi.nlm.nih.gov/34068884/) | 2021 | Narrative Review | Journal of Clinical Medicine | Comprehensive review of RA-associated episcleritis and scleritis, including the role of TNF-α inhibitors; relevant because ocular vasculitis overlaps with systemic RV pathogenesis |
| [28123776](https://pubmed.ncbi.nlm.nih.gov/28123776/) | 2017 | Cohort | RMD Open | BSRBR-RA registry analysis characterising the drug-specific risk of vasculitis-like events (VLEs) in TNFi-treated RA patients compared with non-biological DMARD controls; provides risk quantification data essential for benefit-risk assessment |
| [37699653](https://pubmed.ncbi.nlm.nih.gov/37699653/) | 2024 | Cohort | Annals of the Rheumatic Diseases | HLA-DRB1 and HLA-DQA1 alleles associated with immunogenicity to adalimumab in RA; pharmacogenomic data relevant to predicting adalimumab treatment durability in RV patients |
| [36418100](https://pubmed.ncbi.nlm.nih.gov/36418100/) | 2023 | Case Series | Internal Medicine (Tokyo) | ANCA-associated nephritis developing during combined abatacept and adalimumab therapy in an RA patient; attenuated by tocilizumab; illustrates the complexity of autoimmune renal vasculitis during biologic therapy and the need for renal monitoring |
| [25133007](https://pubmed.ncbi.nlm.nih.gov/25133007/) | 2014 | Case Report | Case Reports in Rheumatology | 42-year-old female with 15-year RA history and digital vasculitis (necrotising fingertip ulcers); responded well to adalimumab — direct clinical evidence supporting adalimumab efficacy in RV |
| [30773522](https://pubmed.ncbi.nlm.nih.gov/30773522/) | 2019 | Case Report | Internal Medicine (Tokyo) | Acute pulmonary hypertension crisis 8 months after adalimumab dose reduction in established RV; patient died despite steroid pulse therapy — critical safety signal emphasising the risks of treatment interruption |
| [19482531](https://pubmed.ncbi.nlm.nih.gov/19482531/) | 2009 | Case Report | Nephrologie & Therapeutique | MPO-ANCA-positive extracapillary glomerulonephritis (necrotising vasculitis) developing during adalimumab therapy for RA; important safety signal for renal surveillance in RV patients receiving adalimumab |
| [28719435](https://pubmed.ncbi.nlm.nih.gov/28719435/) | 2018 | Case Report | Am J Dermatopathology | Leukocytoclastic vasculitis with cutaneous perivascular hemophagocytosis in a patient receiving adalimumab for RA; highlights the paradoxical vasculitis phenomenon known to occur with TNF-α inhibitors |
| [21385558](https://pubmed.ncbi.nlm.nih.gov/21385558/) | 2011 | Case Report | Clinical and Experimental Rheumatology | Successful treatment with anti-IL-6R antibody (tocilizumab) in multidrug-refractory, anti-TNF-resistant systemic RV; provides essential treatment sequencing context for patients who fail or cannot receive adalimumab |

---

## Denmark Market Information

According to available regulatory data, adalimumab currently has no recorded marketing authorisations with the Danish Medicines Agency (Lægemiddelstyrelsen). This is most likely a **data collection gap** rather than a genuine absence from the Danish market: adalimumab (Humira®) and multiple biosimilars (Imraldi®, Hyrimoz®, Amgevita®, Hadlima®, and others) hold EMA centralised marketing authorisations valid across all EU member states including Denmark, covering indications such as rheumatoid arthritis, psoriatic arthritis, axial spondyloarthritis, Crohn's disease, and others.

For prescribing information applicable in Denmark, consult:
- **EMA Humira® EPAR**: [https://www.ema.europa.eu/en/medicines/human/EPAR/humira](https://www.ema.europa.eu/en/medicines/human/EPAR/humira)
- **Lægemiddelstyrelsen product database**: [https://produktresume.dk](https://produktresume.dk)

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A 2021 systematic review provides direct evidence that biological agents including adalimumab are used in rheumatoid vasculitis, and the TNF-α inhibition mechanism is mechanistically well-aligned with RV pathogenesis; however, the complete absence of prospective RCTs specifically in RV, combined with the dual observation that adalimumab can both treat and paradoxically trigger vasculitic events, requires rigorous patient selection criteria, pre-treatment screening, and structured monitoring before wider clinical adoption.

**To proceed, the following is needed:**
- Formal retrieval and review of the SmPC warnings and contraindications, including blackbox warnings (currently a blocking data gap)
- Confirmation of current Danish/EU marketing authorisation status and approved indications via Lægemiddelstyrelsen and the EMA database
- Completion of a detailed mechanism of action review from DrugBank (DB00051) or equivalent authoritative source
- Design of a prospective registry or observational cohort study specifically evaluating adalimumab in rheumatoid vasculitis, given the current absence of RCT-level evidence for this specific indication
- Pre-treatment screening protocol: latent tuberculosis testing (Mantoux/IGRA), hepatitis B serology, ANCA titres, urinalysis, and baseline renal function
- Ongoing safety monitoring plan: renal function, ANCA titres, vasculitis disease activity index (e.g., Birmingham Vasculitis Activity Score), and injection site reactions
- Review of drug-drug interaction profile, particularly for immunosuppressants commonly co-prescribed in RV (e.g., cyclophosphamide, azathioprine)

---

> ⚠️ **Disclaimer**: This report is generated for research reference purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before therapeutic application. All prescribing decisions must be made by qualified healthcare professionals in accordance with approved product labelling and applicable clinical guidelines.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

