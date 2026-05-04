---
layout: default
title: Guselkumab
parent: 僅模型預測 (L5)
nav_order: 215
evidence_level: L5
indication_count: 10
---

# Guselkumab
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

# Guselkumab: From Plaque Psoriasis to Drug-Induced Osteoporosis

## One-Sentence Summary

Guselkumab (Tremfya®) is a fully human monoclonal antibody that selectively blocks the IL-23 p19 subunit, globally approved for moderate-to-severe plaque psoriasis and psoriatic arthritis, but currently not marketed in Denmark.
The TxGNN model assigns its highest prediction score to **Drug-Induced Osteoporosis** (99.84%), suggesting a potential new therapeutic direction via the IL-23/RANKL bone resorption pathway.
However, there are currently **no clinical trials** and **no publications** directly supporting this specific indication, resulting in weak overall evidence for this repurposing direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Denmark; globally approved for moderate-to-severe plaque psoriasis (Tremfya®, Janssen) |
| Predicted New Indication | Drug-Induced Osteoporosis |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L5 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data from DrugBank is not available for guselkumab. Based on established scientific and clinical knowledge, guselkumab selectively binds the p19 subunit of interleukin-23 (IL-23), blocking the IL-23/Th17/IL-17 inflammatory axis. In psoriasis, IL-23 is overexpressed in lesional skin, driving Th17 cell differentiation and promoting secretion of IL-17A/F and IL-22, which in turn trigger keratinocyte hyperproliferation and epidermal inflammation. This mechanism is directly validated by multiple completed Phase 3 trials and constitutes guselkumab's FDA/EMA-approved therapeutic basis.

The theoretical link to drug-induced osteoporosis builds on IL-17's downstream role in bone metabolism: IL-17 can upregulate RANKL expression on osteoblasts and stromal cells, thereby promoting osteoclast differentiation and bone resorption. Blocking IL-23 upstream could theoretically reduce RANKL-mediated bone loss in an inflammatory context.

However, **drug-induced osteoporosis** — as a distinct clinical entity — is predominantly caused by direct bone metabolism disruption from glucocorticoids (suppressing osteoblastogenesis, enhancing osteoclastogenesis via RANKL/OPG imbalance), aromatase inhibitors (oestrogen deprivation), or other agents. These pathophysiological mechanisms operate largely independently of the IL-23/Th17 axis. The proposed mechanistic link is therefore indirect and speculative, and no preclinical or clinical evidence currently supports guselkumab's use in this indication.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for guselkumab in drug-induced osteoporosis.

---

## Literature Evidence

Currently no related literature available for guselkumab in drug-induced osteoporosis.

---

## Denmark Market Information

Guselkumab is not registered in Denmark according to the current dataset. No marketing authorisation records are held by Laegemiddelstyrelsen in this system.

> **Note for clinicians**: Tremfya® (guselkumab) holds a centralised EMA marketing authorisation for moderate-to-severe plaque psoriasis and active psoriatic arthritis in adults. Healthcare professionals should verify the current Laegemiddelstyrelsen and EMA authorisation status through the [EMA product page](https://www.ema.europa.eu) or the Danish Medicines Agency's Medicinpriser database before prescribing.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although TxGNN assigns a very high prediction score (99.84%) to drug-induced osteoporosis, the proposed mechanism relies on an indirect IL-23/IL-17/RANKL pathway that is not the primary driver of drug-induced bone loss. The complete absence of supporting preclinical data, clinical trials, and published literature prevents progression beyond model-level prediction at this time.

**To proceed, the following is needed:**
- Preclinical studies demonstrating IL-23 inhibition's effect specifically on drug-induced (glucocorticoid- or aromatase inhibitor-induced) bone loss, as distinct from inflammatory bone erosion
- Mechanism of action data retrieved from DrugBank API to formally characterise guselkumab's pharmacodynamic profile
- Safety data from the EMA SmPC, including warnings for immunosuppression, infections (tuberculosis reactivation, serious infections), and injection-site reactions
- Drug-drug interaction profiling (current DDI query returned no records)
- Clarification of the patient population: whether the target is patients on concurrent immunosuppressants where IL-23 inhibition might have a secondary bone-protective benefit

---

### Secondary Finding of High Clinical Relevance

> The TxGNN model also predicts **psoriasis** (rank 5, score 99.75%) with **Level L1 evidence** — supported by over 50 registered clinical trials and 20 publications, including multiple completed Phase 3 RCTs (VOYAGE 1, VOYAGE 2, NAVIGATE) and network meta-analyses in *JAMA Dermatology*. The recommendation for this indication is **Proceed with Guardrails**.
>
> This finding validates the TxGNN model's discriminative capability: guselkumab's established global approval for plaque psoriasis is correctly identified as a high-confidence prediction. For Danish healthcare decision-makers, this supports a pathway to evaluate formal Laegemiddelstyrelsen/EMA registration status and reimbursement consideration for psoriasis — an actionable finding requiring priority attention separate from the drug-induced osteoporosis direction.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

