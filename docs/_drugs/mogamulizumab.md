---
layout: default
title: Mogamulizumab
parent: 僅模型預測 (L5)
nav_order: 243
evidence_level: L5
indication_count: 10
---

# Mogamulizumab
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

# Mogamulizumab: From Cutaneous T-Cell Lymphoma to Prostatic Urethra Urothelial Carcinoma

## One-Sentence Summary

Mogamulizumab (brand name: Poteligeo) is a defucosylated humanised anti-CCR4 monoclonal antibody approved internationally for relapsed or refractory mycosis fungoides and Sézary syndrome — subtypes of cutaneous T-cell lymphoma (CTCL) — but currently not marketed in Denmark.
The TxGNN model predicts it may be effective for **Prostatic Urethra Urothelial Carcinoma**, a rare urological malignancy, with a prediction score of **99.44%**.
However, **no clinical trials or published literature** currently support this specific repurposing direction, making this a purely model-driven hypothesis at this stage.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Mycosis fungoides (MF) and Sézary syndrome (SS) — relapsed/refractory cutaneous T-cell lymphoma (EMA/FDA approved globally; not registered in Denmark) |
| Predicted New Indication | Prostatic Urethra Urothelial Carcinoma |
| TxGNN Prediction Score | 99.44% |
| Evidence Level | L5 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the Evidence Pack. Based on known pharmacological information, Mogamulizumab is a defucosylated IgG1 monoclonal antibody that specifically targets CC chemokine receptor 4 (CCR4). Its primary mechanism is antibody-dependent cellular cytotoxicity (ADCC), which selectively depletes CCR4-expressing cells — most notably CCR4⁺ regulatory T cells (Tregs) found in the tumour microenvironment. In its approved CTCL indication, CCR4 is highly expressed on the malignant T-cell population itself, making it both a direct therapeutic target and an immune modulator.

The mechanistic rationale for repurposing to prostatic urethra urothelial carcinoma centres on immune suppression reversal: by depleting CCR4⁺ Tregs that infiltrate the tumour microenvironment, mogamulizumab could theoretically restore CD8⁺ cytotoxic T lymphocyte (CTL) activity and break immune tolerance. Elevated Treg infiltration has been associated with poor prognosis across a range of solid tumours, providing a broad biological rationale for this class of agents beyond haematological malignancies.

However, three critical uncertainties undermine confidence in this specific prediction: (1) prostatic urethra urothelial carcinoma is an extremely rare histological subtype, and published data on Treg infiltration patterns in this localisation are virtually absent; (2) CCR4 expression within this particular tumour subtype has not been confirmed in the literature; (3) the high TxGNN score likely reflects indirect knowledge graph connections — "urothelial carcinoma → immunotherapy → tumour → CCR4 pathway" — rather than direct biological evidence. The prediction should be treated as a hypothesis-generating signal only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Mogamulizumab in prostatic urethra urothelial carcinoma.

---

## Literature Evidence

Currently no related literature available for Mogamulizumab in prostatic urethra urothelial carcinoma.

---

## Denmark Market Information

Mogamulizumab currently holds no marketing authorisations in Denmark — neither a national authorisation via Lægemiddelstyrelsen nor a centralised EMA authorisation applicable to the Danish market.

> **Note for prescribers**: Mogamulizumab is approved by the EMA under the brand name **Poteligeo** for adult patients with mycosis fungoides or Sézary syndrome who have received at least one prior systemic therapy. Named-patient or compassionate use access may be available for licensed indications — contact Lægemiddelstyrelsen for current access pathways. No approved pathway exists for the predicted indication (prostatic urethra urothelial carcinoma).

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted immunotherapy — Anti-CCR4 defucosylated monoclonal antibody (not a conventional cytotoxic agent) |
| Myelosuppression Risk | Low to moderate (lymphopenia is the primary haematological risk; classical neutropenia/thrombocytopenia not a dominant feature) |
| Emetogenicity Classification | Minimal (consistent with the emetogenic profile of monoclonal antibodies as a class) |
| Monitoring Items | Full blood count with differential (lymphocyte count), liver and renal function tests, infusion reaction monitoring, skin toxicity assessment (serious dermatological reactions including Stevens-Johnson syndrome and toxic epidermal necrolysis have been reported) |
| Handling Protection | Follow institutional cytotoxic drug handling guidelines for preparation and disposal; standard biologic/monoclonal antibody precautions apply for administration |

---

## Safety Considerations

Formal safety data (approved warnings, contraindications, and drug interaction profile) were not available in this Evidence Pack for the Danish/EMA registration context.

Please refer to the approved Summary of Product Characteristics (SmPC) for Poteligeo, available via the EMA's European Public Assessment Report (EPAR), for comprehensive safety information including serious immune-mediated adverse reactions (e.g., severe dermatitis, infusion-related reactions, and infections).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is currently no clinical or preclinical evidence supporting the use of mogamulizumab in prostatic urethra urothelial carcinoma, and the target is an extremely rare histological subtype with no confirmatory biological data confirming CCR4 expression or Treg involvement at this specific anatomical site. Proceeding without foundational biomarker and safety data would not meet the minimum threshold for a responsible repurposing programme.

**To proceed, the following is needed:**

- **Biomarker validation**: Confirm CCR4 expression and quantify CCR4⁺ Treg infiltration in prostatic urethra urothelial carcinoma tissue (immunohistochemistry and/or flow cytometry in archival or prospective samples)
- **Preclinical evidence**: Establish in vitro or in vivo antitumour activity of mogamulizumab in urothelial carcinoma cell line or animal models
- **Safety data retrieval**: Obtain and review the full EMA SmPC (Poteligeo), including all warnings, contraindications, and special population data relevant to a urothelial carcinoma patient population
- **Broader literature scan**: Search for mogamulizumab evidence in the wider urothelial carcinoma category (not restricted to this rare subtype) to determine whether any indirect supportive data exist
- **Regulatory pathway clarification**: Determine whether a clinical trial or named-patient access programme in Denmark is feasible, and what Lægemiddelstyrelsen requirements would apply for an off-label or investigational use in a solid tumour indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

