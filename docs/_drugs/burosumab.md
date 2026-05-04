---
layout: default
title: Burosumab
parent: 僅模型預測 (L5)
nav_order: 79
evidence_level: L5
indication_count: 10
---

# Burosumab
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

# Burosumab: From X-linked Hypophosphatemia to Renal Osteodystrophy

## One-Sentence Summary

Burosumab (Crysvita®) is a fully human anti-FGF23 monoclonal antibody approved for X-linked hypophosphatemia (XLH) — a rare hereditary phosphate-wasting disorder causing rickets and osteomalacia in children and adults.
The TxGNN model predicts it may be effective for **Renal Osteodystrophy** with a prediction score of 96.93%, supported currently by **no registered clinical trials** and **1 publication** directly addressing this direction.
Notably, for the mechanistically related indication of **bone remodeling disease**, evidence is substantially stronger — with **2 completed Phase 3 RCTs** yielding an L1 evidence level.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | X-linked hypophosphatemia (XLH); no Denmark marketing authorisation on record |
| Predicted New Indication | Renal Osteodystrophy |
| TxGNN Prediction Score | 96.93% |
| Evidence Level | L4 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this Evidence Pack. Based on available clinical trial descriptions, burosumab is a fully human IgG1 monoclonal antibody that binds to and inhibits fibroblast growth factor 23 (FGF23), thereby relieving FGF23-mediated suppression of renal tubular phosphate reabsorption and restoring 1,25-dihydroxyvitamin D₃ synthesis. In XLH — driven by PHEX gene mutations that cause chronic FGF23 excess — burosumab has demonstrated efficacy in normalising serum phosphate, healing osteomalacia, and improving bone mineralisation across two Phase 3 programmes.

Renal osteodystrophy (ROD) is a broad spectrum of bone pathology arising from chronic kidney disease (CKD), characterised by concurrent mineral dysregulation: hyperphosphataemia, hypocalcaemia, secondary hyperparathyroidism, and impaired vitamin D activation. FGF23 rises markedly in CKD as a compensatory phosphatonin — the superficial resemblance to the FGF23-excess state in XLH is what drives the TxGNN prediction. However, the pathophysiology is critically different: in CKD, the FGF23 elevation is an adaptive response attempting to maintain phosphate excretion. Blocking FGF23 in this setting risks worsening hyperphosphataemia, suppressing calcitriol synthesis acutely, and accelerating vascular calcification — effects opposite to those seen in XLH.

This prediction is therefore best interpreted as a targeted hypothesis: burosumab may hold benefit in the rare FGF23-driven hypophosphatemic subtype of ROD, but carries a meaningful risk profile in the far more common hyperphosphataemic CKD patient. The single available publication — a 2024 paediatric metabolic bone disease review — does not directly study ROD treatment with burosumab, further underscoring the preliminary nature of this prediction.

---

## Clinical Trial Evidence

Currently no clinical trials investigating burosumab specifically in renal osteodystrophy are registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [37927073](https://pubmed.ncbi.nlm.nih.gov/37927073/) | 2024 | Review | Current Pediatric Reviews | Reviews diagnostic and management challenges of paediatric metabolic bone disorders including hypophosphatasia and XLH; discusses the complex pathophysiology of FGF23-mediated phosphate and calcium homeostasis — mechanistically relevant background, but does not directly study renal osteodystrophy or burosumab in CKD |

---

## Denmark Market Information

Burosumab is not currently authorised or marketed in Denmark. No marketing authorisation records are held by the Danish Medicines Agency (Lægemiddelstyrelsen). Crysvita® holds a centralised EMA marketing authorisation for XLH in other EU/EEA member states; Danish healthcare professionals should consult EMA product information and the current SmPC directly for authorised indications, dosing, and safety requirements.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for Crysvita® for complete safety information.

**Mechanistic safety note specific to this predicted indication:** In CKD-associated renal osteodystrophy, FGF23 is typically elevated as a compensatory mechanism. Blocking FGF23 with burosumab in this population may paradoxically worsen hyperphosphataemia and promote vascular calcification — the opposite of the intended therapeutic effect. This represents a clinically significant safety signal that must be formally characterised before any exploratory use is considered in this indication.

---

## Additional Predicted Indications — Evidence Landscape

The TxGNN model identified five unique repurposing candidates for burosumab. The full picture across indications is summarised below:

| Rank | Indication | TxGNN Score | Evidence Level | Recommendation |
|------|-----------|-------------|---------------|----------------|
| 1 | Renal Osteodystrophy | 96.93% | L4 | Hold |
| 3 | Impaired Renal Function Disease | 95.92% | L4 | Research Question |
| 5 | Non-renal Secondary Hyperparathyroidism | 95.78% | L5 | Hold |
| 7 | **Bone Remodeling Disease** | **95.49%** | **L1** | **Proceed with Guardrails** |
| 9 | Hyperparathyroidism, Transient Neonatal | 95.05% | L5 | Hold |

The **bone remodeling disease** indication warrants particular attention: XLH-associated osteomalacia is itself a bone remodeling disorder driven by FGF23 excess, and the Phase 3 evidence below represents the strongest available clinical support for the FGF23-inhibition mechanism across all predicted indications.

### Clinical Trial Evidence — Bone Remodeling Disease (L1)

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|-------------|
| [NCT02526160](https://clinicaltrials.gov/study/NCT02526160) | Phase 3 | Completed | 134 | Randomised, double-blind, placebo-controlled Phase 3 RCT in adults with XLH; primary endpoint: increase in serum phosphorus; demonstrates burosumab's efficacy and safety in phosphate-mediated bone remodeling pathology |
| [NCT02537431](https://clinicaltrials.gov/study/NCT02537431) | Phase 3 | Completed | 14 | Open-label Phase 3 study in adults with XLH; primary endpoint: improvement in osteomalacia assessed by osteoid volume/bone volume (OV/BV); directly evaluates burosumab's impact on bone mineralisation defects |
| [NCT03993821](https://clinicaltrials.gov/study/NCT03993821) | Early Phase 1 | Unknown | 1 | Single-patient exploratory study of burosumab in Cutaneous Skeletal Hypophosphatemia Syndrome (CSHS); limited generalisability, included as context only |

### Literature Evidence — Bone Remodeling Disease

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [37180412](https://pubmed.ncbi.nlm.nih.gov/37180412/) | 2022 | Review | Therapeutic Advances in Rare Disease | Systematic/narrative review comparing burosumab vs. conventional therapy in adult XLH; summarises burosumab's improvements in bone pain, insufficiency fracture healing, enthesopathy, and quality of life; relevant for understanding the therapeutic ceiling in FGF23-driven bone disease |
| [35235937](https://pubmed.ncbi.nlm.nih.gov/35235937/) | 2023 | Review | Hormone Research in Paediatrics | Reviews novel treatment options in paediatric bone diseases including XLH, paediatric osteoporosis, and achondroplasia; provides context for burosumab's role in the broader landscape of childhood skeletal disorders |
| [37843399](https://pubmed.ncbi.nlm.nih.gov/37843399/) | 2024 | Observational / Cohort | J Clin Endocrinol Metab | Evaluates cardiovascular risk in adults with XLH receiving conventional therapy; notes chronically elevated FGF23 in XLH and reassuring (though limited) cardiovascular data — directly relevant to long-term safety monitoring under FGF23-pathway therapies |

### Literature Evidence — Impaired Renal Function Disease (contextual, L4)

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [38195892](https://pubmed.ncbi.nlm.nih.gov/38195892/) | 2024 | Case Report | Calcified Tissue International | First published case of burosumab use in a patient with XLH and comorbid CKD stage 3b; conventional therapy was poorly tolerated; burosumab achieved biochemical and clinical improvement — represents the only direct human evidence for burosumab in a renally impaired patient |
| [32701599](https://pubmed.ncbi.nlm.nih.gov/32701599/) | 2020 | Perspective / Commentary | Curr Opin Nephrol Hypertens | Reviews burosumab in XLH and discusses its theoretical perspective for CKD-MBD; highlights the dual role of FGF23 as both a therapeutic target (XLH) and a risk marker (CKD), framing the key clinical dilemma |
| [37180412](https://pubmed.ncbi.nlm.nih.gov/37180412/) | 2022 | Review | Therapeutic Advances in Rare Disease | See above; also relevant to renal function disease through discussion of FGF23 dysregulation in XLH patients who develop renal complications |
| [36382755](https://pubmed.ncbi.nlm.nih.gov/36382755/) | 2022 | Review | Archives of Endocrinology and Metabolism | Reviews phosphorus metabolism and new therapies for hypophosphatemic rickets and osteomalacia including FGF23-targeted agents; provides mechanistic grounding for understanding burosumab's role across phosphate-wasting disorders |
| [35103802](https://pubmed.ncbi.nlm.nih.gov/35103802/) | 2022 | Review / Case Series | Zeitschrift für Rheumatologie | Reviews tumour-induced osteomalacia (TIO) — a paraneoplastic FGF23-excess syndrome causing renal phosphate wasting — and discusses therapeutic options; mechanistically parallel to XLH and relevant to FGF23 pathway interventions |
| [31905439](https://pubmed.ncbi.nlm.nih.gov/31905439/) | 2019 | Review | Annals of Pediatric Endocrinology & Metabolism | Reviews skeletal mineralisation mechanisms; explains how insufficient phosphate impairs hydroxyapatite crystal propagation, providing the mechanistic basis for why FGF23 inhibition promotes bone healing |

---

## Conclusion and Next Steps

**Decision: Hold** *(primary predicted indication: Renal Osteodystrophy)*

**Rationale:**
Evidence for burosumab in renal osteodystrophy is limited to a single indirectly relevant paediatric review with no registered clinical trials (L4), and the dual role of FGF23 in CKD introduces a clinically meaningful safety risk — namely worsening hyperphosphataemia and vascular calcification — that must be resolved before this indication can be progressed.

**To proceed, the following is needed:**
- Mechanistic phenotyping of the target ROD subtype: only FGF23-driven hypophosphatemic ROD (rare) would be a credible candidate; hyperphosphataemic CKD-ROD carries an unfavourable risk profile
- Preclinical studies in CKD animal models assessing the effect of FGF23 inhibition on serum phosphate, calcitriol, PTH, and vascular calcification markers
- Systematic analysis of the XLH+CKD case report (PMID 38195892) and any additional real-world cases to assess feasibility of a proof-of-concept study
- Formal acquisition of burosumab SmPC (EMA) and DrugBank data to document approved indications, contraindications, and pharmacokinetic parameters in renal impairment
- Development of a safety monitoring framework covering serum phosphate, calcium, FGF23, PTH, and cardiovascular calcification imaging for any exploratory use

> **Note on Bone Remodeling Disease:** If the clinical research question is broadened to FGF23-driven phosphate metabolism disorders causing impaired bone mineralisation, the evidence base is substantially stronger: 2 completed Phase 3 RCTs support an L1 rating, and a dedicated evaluation would support a **Proceed with Guardrails** recommendation. This represents the most actionable pathway for burosumab repurposing research in Denmark.

---

*This report is generated for research purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before therapeutic application. Healthcare professionals should refer to the current approved SmPC for prescribing information.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

