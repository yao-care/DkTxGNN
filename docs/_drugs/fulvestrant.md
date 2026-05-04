---
layout: default
title: Fulvestrant
parent: 僅模型預測 (L5)
nav_order: 197
evidence_level: L5
indication_count: 10
---

# Fulvestrant
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

# Fulvestrant: From Hormone Receptor-Positive Breast Cancer to HIV Infectious Disease

## One-Sentence Summary

Fulvestrant (Faslodex) is a selective estrogen receptor degrader (SERD) with established international use in the treatment of hormone receptor-positive (HR+) advanced or metastatic breast cancer in postmenopausal women — though it is not currently authorised in Denmark.
The TxGNN model predicts it may be effective for **HIV Infectious Disease** with a score of 99.91%,
however only **1 indirect publication** has been identified (concerning HTLV-1, a distinct retrovirus, not HIV), and **no clinical trials** have been registered for this repurposing direction — placing this prediction at the lowest possible evidence level.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hormone receptor-positive (HR+) advanced breast cancer (internationally approved; not authorised in Denmark) |
| Predicted New Indication | HIV Infectious Disease |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L5 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Fulvestrant is a selective estrogen receptor degrader (SERD). Unlike tamoxifen, which partially blocks the oestrogen receptor (ER), fulvestrant binds to the ER with very high affinity and triggers its complete degradation — eliminating all ER-mediated signalling inside the cell. This mechanism has made it effective for HR+ breast cancer, particularly in cases that have progressed after aromatase inhibitor therapy. Detailed mechanism of action data was not available in this Evidence Pack; the above is based on established pharmacological knowledge.

The theoretical rationale for fulvestrant in HIV infectious disease rests on an indirect and unverified biological premise: certain in vitro studies suggest that ER-β activation may facilitate HIV-1 replication within CD4+ T cells. If ER signalling genuinely supports viral replication in this compartment, then degrading the receptor via fulvestrant could theoretically inhibit this process. However, this is a highly speculative chain of reasoning involving multiple unconfirmed mechanistic steps and has not been tested in any clinical or formal preclinical study.

Critically, the sole publication retrieved by the evidence search (PMID 40343334, 2025) concerns **HTLV-1** — the Human T-cell Leukemia Virus type 1, associated with adult T-cell leukaemia and the neuroinflammatory condition HAM/TSP — and not HIV. HTLV-1 and HIV are both retroviruses but are pathophysiologically distinct. The TxGNN model's high confidence score most likely reflects graph-level proximity between ER signalling nodes and retroviral disease nodes in the knowledge graph, rather than direct biological evidence linking fulvestrant to HIV.

---

## Clinical Trial Evidence

Currently no related clinical trials have been registered for fulvestrant in HIV infectious disease.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [40343334](https://pubmed.ncbi.nlm.nih.gov/40343334/) | 2025 | Observational (multi-cohort cross-omics) | Research Square (preprint) | Multi-cohort systems biology analysis of HTLV-1-associated myelopathy (HAM). Used genomic and epigenomic data from multiple cohorts to map disease mechanisms and candidate therapeutic targets for this neglected retroviral neuroinflammatory disorder. **This study does not investigate fulvestrant, and its subject is HTLV-1, not HIV.** It was retrieved due to overlapping retroviral immunological pathway terminology. |

> **Important caveat:** This publication has no direct relevance to the proposed repurposing of fulvestrant for HIV. It should not be interpreted as supporting evidence for this indication.

---

## Denmark Market Information

Fulvestrant currently holds **no marketing authorisations** with the Danish Medicines Agency (Laegemiddelstyrelsen).

> **Note for clinical context:** Fulvestrant (Faslodex®, AstraZeneca) holds a centralised EMA marketing authorisation valid in all EU member states for the treatment of HR-positive locally advanced or metastatic breast cancer in postmenopausal women. Healthcare professionals seeking to use fulvestrant for its established breast cancer indication should verify current EMA authorisation status and local reimbursement conditions independently.

---

## Cytotoxicity

Fulvestrant is classified as an antineoplastic agent used in cancer treatment and therefore meets the threshold for inclusion of this section.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted endocrine therapy — Selective Estrogen Receptor Degrader (SERD); **not** a conventional cytotoxic agent |
| Myelosuppression Risk | Low — fulvestrant is not a DNA-damaging agent and does not cause clinically significant bone marrow suppression |
| Emetogenicity Classification | Low |
| Monitoring Items | Liver function tests (hepatotoxicity has been reported); bone mineral density monitoring for patients on long-term therapy; injection site reactions (fulvestrant is administered as an intramuscular injection) |
| Handling Protection | Standard pharmaceutical handling applies; fulvestrant does not require the specialised cytotoxic drug handling precautions mandated for conventional chemotherapy |

---

## Safety Considerations

Detailed safety information — including specific warnings, contraindications, and drug interaction data — was not available in this Evidence Pack for fulvestrant.

Please refer to the approved Summary of Product Characteristics (SmPC) for fulvestrant (Faslodex®) for complete safety information, including contraindications in hepatic impairment and pregnancy.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a very high TxGNN prediction score of 99.91%, the evidence base for fulvestrant in HIV infectious disease is at **Level L5** — model prediction only. There are no registered clinical trials, and the single identified publication addresses HTLV-1 rather than HIV. The biological hypothesis linking oestrogen receptor degradation to HIV suppression is theoretically conceivable but entirely unverified in human studies or dedicated preclinical models. Proceeding without further mechanistic validation would not be justified.

**To proceed, the following is needed:**

- Systematic literature review specifically targeting ER-β/HIV-1 interactions in CD4+ T cells, including any dedicated preclinical (in vitro or animal model) studies
- Mechanistic confirmation that oestrogen receptor signalling plays a functionally meaningful role in HIV-1 replication in vivo and at physiologically relevant fulvestrant concentrations
- Complete safety data from the SmPC, with particular focus on use in immunocompromised patients (the HIV-positive population), hepatic safety, and interactions with antiretroviral agents
- Regulatory and ethical assessment for any first-in-indication clinical investigation

**Additional note — more promising TxGNN target:**
Among the top-ranked predictions in this Evidence Pack, **Multiple Endocrine Neoplasia (MEN)** (TxGNN score: 99.85%, evidence level L4) presents a more mechanistically coherent repurposing hypothesis. Certain MEN subtypes — including MEN1-associated breast tumours and selected neuroendocrine tumours — can express oestrogen receptors, providing a direct rationale for SERD-based therapy. Although the 50 retrieved clinical trials are all HR+ breast cancer studies (mechanistic extrapolation only, no direct MEN evidence), this direction warrants a dedicated evidence review before the HIV hypothesis is prioritised further.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

