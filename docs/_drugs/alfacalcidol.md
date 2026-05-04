---
layout: default
title: Alfacalcidol
parent: 僅模型預測 (L5)
nav_order: 22
evidence_level: L5
indication_count: 10
---

# Alfacalcidol
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

# Alfacalcidol: From Renal Osteodystrophy to Familial Isolated Hypoparathyroidism due to Impaired PTH Secretion

## One-Sentence Summary

Alfacalcidol is a synthetic 1α-hydroxylated analogue of vitamin D₃, established in clinical practice for the management of calcium and phosphorus metabolism disorders associated with chronic kidney disease, secondary hyperparathyroidism, and osteoporosis. The TxGNN model predicts it may be effective for **familial isolated hypoparathyroidism due to impaired PTH secretion**, with a prediction score of **99.61%** and an extremely strong mechanistic rationale (★★★★★). However, no clinical trials or published literature specific to this precise indication have yet been identified, and the drug is not currently registered in Denmark.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No marketing authorisation in Denmark; known use includes renal osteodystrophy, secondary hyperparathyroidism, and osteoporosis |
| Predicted New Indication | Familial isolated hypoparathyroidism due to impaired PTH secretion |
| TxGNN Prediction Score | 99.61% |
| Evidence Level | L5★ |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data from DrugBank is not currently available for this report. Based on established pharmacology, alfacalcidol (1α-hydroxycholecalciferol) is a vitamin D analogue that bypasses the renal 1α-hydroxylation step ordinarily required to convert 25-hydroxyvitamin D into the fully active hormone calcitriol (1,25(OH)₂D₃). Unlike native vitamin D₃, alfacalcidol requires only hepatic 25-hydroxylation to become biologically active. This pharmacological property makes it particularly valuable when renal function or PTH-mediated signalling is impaired — precisely the mechanism disrupted in the predicted indication.

In familial isolated hypoparathyroidism due to impaired PTH secretion, inadequate PTH production leads to failure of renal 1α-hydroxylase stimulation. The downstream consequence is reduced calcitriol synthesis, resulting in chronic hypocalcaemia and hyperphosphataemia. Alfacalcidol directly provides the 1α-pre-hydroxylated substrate, bypassing this enzymatic bottleneck and restoring active vitamin D signalling independently of PTH. The mechanistic connection is therefore rated ★★★★★ (extremely strong) in the evidence assessment.

It is important to note that alfacalcidol already has established clinical use in broader hypoparathyroidism — including post-surgical and idiopathic forms — in several EU countries. Familial isolated hypoparathyroidism due to impaired PTH secretion shares the same downstream metabolic defect as these better-studied subtypes. The TxGNN prediction is therefore highly biologically plausible; the primary limitation is the absence of published evidence specific to this rare genetic subentity rather than any mechanistic uncertainty.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for this indication.

---

## Literature Evidence

Currently no related literature available for this specific indication.

---

## Denmark Market Information

Alfacalcidol is not currently registered in Denmark. The Danish Medicines Agency (Laegemiddelstyrelsen) has issued no marketing authorisations for this drug, and no products are currently on the Danish market.

Alfacalcidol products (e.g., **One-Alpha**, Leo Pharma) hold marketing authorisations in other EU Member States and the United Kingdom for indications including renal osteodystrophy, secondary hyperparathyroidism, hypoparathyroidism, and osteoporosis. Use in Denmark would require a named-patient (individuelt tilskud) or compassionate use authorisation, or cross-border supply under the EU pharmaceutical framework.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a TxGNN prediction score of 99.61% and an extremely strong mechanistic basis — alfacalcidol directly restores calcitriol activity that is lost due to absent PTH signalling — no clinical trials or published literature specific to this rare genetic subtype have been identified (Evidence Level L5★). The drug is also not registered in Denmark, which introduces an additional regulatory barrier. A Hold decision reflects the need for targeted evidence generation and regulatory pathway assessment before clinical application can be considered.

**To proceed, the following is needed:**

- **Regulatory scope review**: Confirm whether existing EU SmPC hypoparathyroidism indications already encompass this genetic subtype, which would shift the classification from off-label to on-label use
- **Safety documentation**: Obtain complete warnings, contraindications, and drug interaction data from the SmPC (currently a data gap); Danish clinicians should consult the Leo Pharma SmPC for One-Alpha as a reference
- **MOA documentation**: Complete DrugBank mechanism of action entry (currently flagged as a data gap, severity: High)
- **Systematic literature review**: Conduct a dedicated search for case reports or observational studies in patients with genetically confirmed familial isolated hypoparathyroidism to verify that evidence truly remains at L5
- **Rare disease network engagement**: Contact relevant ERN networks (e.g., ERN BOND or ERN ENDO) to identify patient populations suitable for prospective observational studies or registry inclusion
- **Regulatory pathway**: Initiate dialogue with Laegemiddelstyrelsen regarding named-patient authorisation or evaluate whether a centralised EMA indication extension could be sought

> **Research note:** This prediction shares mechanistic overlap with two additional TxGNN top predictions not detailed in this report: **Dahlberg-Borer-Newcomer syndrome** (which includes a hypoparathyroid component; 20 supporting publications identified; Evidence Level L4) and **renal tubular acidosis** (8 supporting publications identified, including a clinical series showing 200–250× greater efficacy than vitamin D₂; Evidence Level L3; Recommendation: **Proceed with Guardrails**). Clinicians seeking a higher-evidence repurposing opportunity with alfacalcidol in Denmark may wish to prioritise the renal tubular acidosis indication for further evaluation.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

