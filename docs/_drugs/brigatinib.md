---
layout: default
title: Brigatinib
parent: 僅模型預測 (L5)
nav_order: 74
evidence_level: L5
indication_count: 10
---

# Brigatinib
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

# Brigatinib: From ALK-Positive Non-Small-Cell Lung Cancer to Fibromatosis, Gingival

## One-Sentence Summary

Brigatinib (ALUNBRIG) is a second-generation anaplastic lymphoma kinase (ALK) inhibitor with a well-established evidence base for the treatment of ALK-positive metastatic non-small-cell lung cancer (NSCLC), having received FDA accelerated approval in April 2017.
The TxGNN model assigns **Fibromatosis, Gingival** as the top predicted new indication with a score of **99.89%**; however, this prediction is currently supported by **no clinical trials and no published literature**, and the mechanistic rationale is not established.
This finding is most likely a knowledge graph proximity artefact rather than a genuine repurposing opportunity, and the overall recommendation is **Hold**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | ALK-positive metastatic NSCLC (established from published evidence; not registered in Denmark) |
| Predicted New Indication | Fibromatosis, Gingival |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L5 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on published literature identified during evidence retrieval, Brigatinib is a potent next-generation inhibitor of ALK, EGFR, ROS1, and RET fusion kinases. Its efficacy in ALK-rearranged NSCLC has been demonstrated across multiple Phase 3 clinical trials (the ALTA-1L programme), consistently showing superior progression-free survival over first-generation ALK inhibitor crizotinib (PFS HR ≈ 0.49 at final analysis).

Gingival fibromatosis (fibromatosis, gingival) is a condition characterised by progressive overgrowth of gingival connective tissue, driven by hereditary factors (SOS1/KRAS pathway mutations) or drug-induced mechanisms (calcineurin pathway dysregulation, TGF-β signalling — particularly associated with calcium channel blockers or phenytoin). There is no established molecular intersection between these fibrotic pathways and Brigatinib's primary targets. Brigatinib has no known TGF-β inhibitory, calcineurin inhibitory, or SOS1/KRAS modulatory activity.

The high TxGNN score (99.89%) most likely reflects spurious proximity within the knowledge graph via shared "fibrous tissue" node associations, rather than any genuine biological relationship. There are no clinical trials, observational studies, preclinical models, or published case reports supporting Brigatinib use in gingival fibromatosis.

> **⚠️ Evidence Pipeline Quality Alert**: During evidence retrieval, 20 publications were retrieved under the adjacent TxGNN prediction "lung benign neoplasm" (ranks 9–10). Analysis confirms that all 20 papers relate exclusively to ALK-positive *malignant* NSCLC — including the full ALTA-1L Phase 3 RCT series (PMID 34537440, 30280657, 32780660) — not to benign lung tumours. This represents a disease classification mapping error in the evidence pipeline. When correctly attributed, these papers collectively establish **L1-level direct Phase 3 RCT evidence** for Brigatinib in ALK+ NSCLC. This hidden finding does not change the gingival fibromatosis assessment, but the pipeline mapping error should be corrected before further evidence synthesis is conducted.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Denmark Market Information

Brigatinib currently holds **no marketing authorisations** in Denmark and is not marketed. Laegemiddelstyrelsen has issued no national approvals, and no centralised EMA authorisations are reflected in the current dataset for this product. Healthcare professionals in Denmark requiring access to Brigatinib should consult the EMA's current centralised procedure register and consider named-patient or compassionate use pathways if clinically justified for a patient with ALK-positive NSCLC.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy — Second-generation ALK/EGFR/ROS1/RET tyrosine kinase inhibitor (small molecule) |
| Myelosuppression Risk | Low to moderate (lymphopenia and anaemia reported in Phase 3 trials; severe haematological toxicity uncommon compared to conventional cytotoxics) |
| Emetogenicity Classification | Low (oral administration; nausea Grade 1–2 reported in approximately 33% of patients in ALTA-1L, rarely requiring dose modification) |
| Monitoring Items | Complete blood count (CBC with differential), liver function (ALT/AST/bilirubin), renal function (creatinine), pulmonary monitoring during the first 7 days of treatment (early-onset pulmonary events, EOPE, are a class-specific concern for Brigatinib), blood pressure, fasting blood glucose |
| Handling Protection | Oral tablet formulation; standard institutional handling precautions for oral antineoplastic agents apply — healthcare staff should follow local cytotoxic handling policy, including glove use when handling broken or split tablets |

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction for gingival fibromatosis represents L5-level evidence only — a computational model signal with no mechanistic support, no clinical trials, and no published literature. The high prediction score almost certainly reflects a knowledge graph structural artefact (spurious fibrous tissue node proximity), not a biologically plausible repurposing hypothesis.

**To proceed, the following would be needed:**
- Identification of a credible mechanistic link between ALK/EGFR/ROS1 inhibition and the primary pathogenic pathways of gingival fibromatosis (SOS1/KRAS, calcineurin, TGF-β signalling)
- At least one published preclinical study (in vitro or in vivo) demonstrating relevant activity in a gingival fibromatosis model
- Retrieval of complete Brigatinib MOA data from DrugBank (DB12267) to enable systematic mechanistic analysis
- Correction of the disease classification mapping error in the TxGNN evidence pipeline to prevent benign/malignant disease category conflation, which obscured genuine L1 ALK+ NSCLC evidence in this run
- Consultation with Laegemiddelstyrelsen regarding Brigatinib's current regulatory status in Denmark and available access pathways for patients with ALK-positive NSCLC who may benefit from this drug
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

