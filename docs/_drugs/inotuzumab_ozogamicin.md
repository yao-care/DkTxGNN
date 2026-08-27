---
layout: default
title: Inotuzumab Ozogamicin
parent: 僅模型預測 (L5)
nav_order: 233
evidence_level: L5
indication_count: 10
---

# Inotuzumab Ozogamicin
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

Using the drug-repurposing evaluation report template to structure this Evidence Pack into the required Markdown report.

# Inotuzumab Ozogamicin: From Acute Lymphoblastic Leukemia to Drug-Induced Osteoporosis

## One-Sentence Summary

Inotuzumab ozogamicin is an anti-CD22 antibody-drug conjugate (ADC), globally established for CD22-positive B-cell precursor acute lymphoblastic leukemia (ALL); this specific evidence pack does not itself contain the original-indication or label text (data gap). The TxGNN model predicts possible efficacy for **Drug-Induced Osteoporosis**, but this is currently supported by **0 clinical trials** and **0 publications**, and the evidence pack's own mechanistic review flags the prediction as a likely non-specific model artefact rather than a real pharmacological signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | CD22-positive B-cell precursor Acute Lymphoblastic Leukemia (ALL) — *not present in the Danish registry data (drug not marketed in Denmark); stated here from general labelling knowledge, since the evidence pack's own `original_indications` field is empty* |
| Predicted New Indication | Drug-Induced Osteoporosis |
| TxGNN Prediction Score | 98.24% |
| Evidence Level | L5 |
| Denmark Market Status | Not Marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for this candidate is not available in the evidence pack (flagged as a High-severity data gap). Based on known pharmacology, inotuzumab ozogamicin is an antibody-drug conjugate combining an anti-CD22 monoclonal antibody with the cytotoxic payload calicheamicin: binding to CD22 on malignant B-lymphocytes triggers internalisation of the conjugate, and calicheamicin then causes DNA double-strand breaks that kill the target cell. This mechanism is highly specific to CD22-expressing haematological malignancies.

There is no established pharmacological or clinical link between this mechanism and bone metabolism (osteoclast/osteoblast activity), and the evidence pack's own repurposing rationale states this explicitly: no direct mechanistic connection has been identified between CD22/calicheamicin-mediated B-cell killing and drug-induced bone loss.

The high TxGNN score most likely reflects a generic knowledge-graph association rather than a drug-specific signal — cytotoxic/chemotherapeutic drug nodes are broadly connected to bone-loss-related adverse-effect nodes in the underlying graph, which can inflate similarity scores for many cytotoxic agents regardless of their actual target biology. Notably, the other top-ranked candidates in this same evidence pack (e.g. HER2-positive and luminal-subtype breast carcinoma) show the same pattern — no CD22 target expression in the relevant tissue, and in one case the attached "supporting literature" was later found to be a keyword-matching artefact (unrelated B-cell/hepatitis-B papers matched via the letter "B" in "Luminal B"). This suggests a systematic lack of specificity in this drug's prediction set, not just an isolated weak candidate.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Denmark Market Information

Inotuzumab ozogamicin currently holds **no marketing authorisation in Denmark** (0 authorisations on file; market status: Not Marketed). No product-, dosage-form-, or indication-level licence data is therefore available from the Danish registry.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy — Antibody-Drug Conjugate (anti-CD22 antibody carrying the cytotoxic payload calicheamicin) |
| Myelosuppression Risk | Please refer to the Summary of Product Characteristics (SmPC) warnings and precautions |
| Emetogenicity Classification | Please refer to the Summary of Product Characteristics (SmPC) warnings and precautions |
| Monitoring Items | Please refer to the Summary of Product Characteristics (SmPC) warnings and precautions |
| Handling Protection | Payload is a DNA-damaging cytotoxic agent; standard cytotoxic drug handling precautions should apply pending confirmation via the SmPC |

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although the TxGNN score is high, the evidence pack's own mechanistic review assesses the top-ranked prediction (drug-induced osteoporosis) as lacking pharmacological plausibility and likely reflecting a generic graph-topology artefact rather than a drug-specific signal. There is no supporting clinical trial or literature evidence (Evidence Level L5), the drug holds no marketing authorisation in Denmark, and label/safety data required even for an initial safety screen (S1) is missing — a Blocking-severity data gap.

**To proceed, the following is needed:**
- TFDA/SmPC label warnings and contraindications (Blocking data gap: DG001)
- Confirmed mechanism-of-action detail sourced from DrugBank or the approved label (High-priority data gap: DG002)
- An independent, biologically grounded rationale linking CD22-ADC pharmacology to bone metabolism — or formal exclusion of this candidate if none can be established
- Preclinical or real-world data on bone mineral density effects, if this indication is still to be pursued
- A broader specificity review of this drug's full TxGNN prediction set, given that other top-ranked candidates (breast carcinoma subtypes) show the same absence of target-expression rationale and, in one case, contaminated literature matches
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

