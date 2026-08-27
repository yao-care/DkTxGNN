---
layout: default
title: Phenprocoumon
parent: 僅模型預測 (L5)
nav_order: 350
evidence_level: L5
indication_count: 10
---

# Phenprocoumon
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

# Phenprocoumon: From Thromboembolic Disorders to Posteroinferior Myocardial Infarction

## One-Sentence Summary

> Phenprocoumon is a vitamin K antagonist (VKA) oral anticoagulant; no structured data on its original approved indication is available in this evidence pack. The TxGNN model predicts a **99.86% score** association with **Posteroinferior Myocardial Infarction** — however, this is an anatomical subtype node of myocardial infarction rather than a distinct clinical entity, and **0 clinical trials** and **0 publications** specific to phenprocoumon in this indication are currently registered.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in structured data (`original_indications` is empty). Evidence-pack rationale notes phenprocoumon is clinically used as a vitamin K antagonist (VKA) oral anticoagulant, analogous to warfarin |
| Predicted New Indication | Posteroinferior Myocardial Infarction (anatomical MI subtype — not an independent clinical entity) |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L4 |
| Denmark Market Status | Not Marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (`original_moa: [Data Gap]`). Based on the contextual information supplied in this evidence pack's own rationale notes, phenprocoumon is a vitamin K antagonist (VKA), pharmacologically comparable to warfarin, and its established clinical role is long-term oral anticoagulation.

The top-ranked predicted indication, "Posteroinferior Myocardial Infarction," is explicitly flagged in the evidence pack as an **anatomical location subtype of myocardial infarction**, not a separate disease entity. The rationale explains that VKA-class drugs have class-level (not phenprocoumon-specific) historical Phase 3 RCT support for secondary prevention of post-MI thromboembolic events (e.g. WARIS-II, ASPECT-2 are referenced as background literature, but neither trial is included as structured evidence in this pack). The very high TxGNN score most likely reflects a generalized "anticoagulant–MI" association learned by the knowledge graph, rather than evidence specific to this anatomical subtype or to phenprocoumon itself.

This evidence pack additionally lists four other candidate diseases at similarly high scores: posterolateral myocardial infarction (99.86%), heparin cofactor 2 deficiency (99.86%, supported by 1 review-level publication from 1989), septal myocardial infarction (99.85%), and factor 5 excess with spontaneous thrombosis (99.80%, no supporting records at all). Note that several ranks in the underlying data (e.g. rank 1 and rank 3, rank 2 and rank 4) are exact duplicates of the same disease/score pairing — this should be treated as a data quality artifact for triage purposes rather than independent corroboration.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

*(Note: the related candidate "heparin cofactor 2 deficiency" — an inherited thrombophilia — is supported by one 1989 review-level publication, [2483712](https://pubmed.ncbi.nlm.nih.gov/2483712/), which is not a direct trial of phenprocoumon in this MI subtype and is presented here for transparency only, not as evidence for the primary predicted indication above.)*

---

## Denmark Market Information

Phenprocoumon currently holds **no marketing authorisation in Denmark** (market status: Not Marketed; 0 registered licenses). No Laegemiddelstyrelsen or EMA centralised product record is available for this evidence pack.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information. Note: since phenprocoumon is not marketed in Denmark, no Danish SmPC currently exists — key warnings, contraindications, and drug interaction data are all recorded as data gaps (`DG001`, marked **Blocking** severity in this evidence pack, as it prevents entry into the S1 safety pre-screen). Consult an EU/other-jurisdiction SmPC or DrugBank/DDI database directly before any clinical use is considered.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication is an anatomical MI subtype rather than a distinct clinical entity, with zero direct clinical trials or publications supporting phenprocoumon specifically in this context — the high TxGNN score appears to reflect a generalized anticoagulant–MI graph association rather than targeted evidence. Combined with the drug's non-marketed status in Denmark and a Blocking-severity safety data gap, this candidate does not currently meet the bar to proceed.

**To proceed, the following is needed:**
- TFDA/Danish SmPC warnings and contraindications (`DG001`, Blocking — required before any S1 safety pre-screen)
- Confirmed mechanism of action data from DrugBank (`DG002`)
- Disambiguation of the duplicated ranking entries in the candidate list (data quality check)
- Direct clinical trial or literature evidence for phenprocoumon specifically in post-MI thromboembolic prevention, rather than class-level VKA background literature
- Clarification of whether Denmark has any historical or off-label use pathway for phenprocoumon, given its current non-marketed status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

