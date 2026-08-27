---
layout: default
title: Tipranavir
parent: 僅模型預測 (L5)
nav_order: 436
evidence_level: L5
indication_count: 10
---

# Tipranavir
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

# Tipranavir: From HIV-1 Infection to Simian Immunodeficiency Virus Infection

## One-Sentence Summary

Tipranavir is a non-peptidic HIV-1 protease inhibitor, historically used in antiretroviral therapy for treatment-experienced, multi-drug-resistant HIV-1 infection (this original-indication link is inferred from the evidence pack's internal rationale notes, since formal indication/license text is not available). The TxGNN model's top-ranked prediction is **Simian Immunodeficiency Virus (SIV) Infection**, an animal-model disease with a **99.99% prediction score** but **zero supporting clinical trials or literature**. The evidence pack's own analysis flags this as a high-score/low-clinical-value prediction driven by lentivirus-family semantic similarity, not a genuine repurposing signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in formal license data (0 Denmark authorisations); per internal rationale notes, tipranavir is a non-peptidic HIV-1 protease inhibitor used in antiretroviral therapy |
| Predicted New Indication | Simian Immunodeficiency Virus (SIV) Infection |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 (model prediction only, no clinical or literature support) |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for tipranavir is marked as a data gap at the drug level. However, the evidence pack's own repurposing-rationale text identifies tipranavir as a non-peptidic HIV-1 protease inhibitor, acting by blocking the viral protease enzyme required for maturation of infectious viral particles.

The top-ranked prediction, SIV infection, is explicitly flagged in the evidence pack as a low-clinical-value output: SIV is a primate model virus in the same *Lentivirus* genus as HIV, so the protease-inhibition mechanism is theoretically transferable — but SIV infection is an animal disease entity, not a human clinical indication, and no trial or literature evidence exists to support it. The same pattern repeats for the next few ranked predictions (feline immunodeficiency syndrome — another animal disease; a rare neurodevelopmental disorder with no known mechanistic link; and an obsolete hyperlipidemia term that actually contradicts tipranavir's known dyslipidemia side-effect profile). The evidence pack characterizes these as model noise from semantic clustering around "retroviral infection," rather than genuine repurposing candidates.

Within this pack, the only predictions reaching an advanced internal decision stage (S1, "Research Question") are **AIDS-related complex** (rank 9) and **congenital HIV infection** (rank 10) — both of which represent an extension of tipranavir's already-established antiretroviral mechanism along the HIV disease spectrum, rather than a novel repurposing hypothesis. Congenital HIV is further supported by 9 identified clinical trials, though most concern other antiretroviral regimens rather than tipranavir specifically (see below).

---

## Clinical Trial Evidence

For the top-ranked prediction (SIV infection): currently no related clinical trials registered.

*Context note: elsewhere in this evidence pack, 9 clinical trials were identified under the lower-ranked "congenital human immunodeficiency virus" prediction (L4/S1, the pack's most advanced candidate). Only one (NCT00042289, IMPAACT P1026s — antiretroviral pharmacokinetics in pregnancy/postpartum) is graded relevance B; the remaining 8 are graded C, as they evaluate other antiretroviral regimens (dolutegravir, cabotegravir/rilpivirine, etc.) rather than tipranavir directly. None specifically test tipranavir.*

---

## Literature Evidence

Currently no related literature available.

---

## Denmark Market Information

No marketing authorisations are recorded for tipranavir in this evidence pack (0 authorisations; market status: Not marketed).

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

*Note: retrieval of TFDA/local label warnings and contraindications is flagged in this evidence pack as a **Blocking** data gap (DG001) — safety data must be obtained before this candidate can enter formal safety pre-assessment (S1).*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top TxGNN-ranked prediction (SIV infection) is an animal-disease entity with L5 evidence — model prediction only, no clinical trials, no literature, and no plausible clinical development path. The drug also has no marketing authorisation in Denmark and is missing mechanism-of-action and SmPC safety data, which blocks any formal safety pre-assessment.

**To proceed, the following is needed:**
- Local SmPC / regulatory label (warnings, contraindications) — currently a Blocking data gap
- Confirmed mechanism-of-action documentation
- If pursuing repurposing further, redirect focus away from the top-ranked animal-disease predictions toward the pack's more clinically grounded candidates — AIDS-related complex and congenital HIV infection (both L4/S1) — and seek tipranavir-specific trial or literature evidence for those indications
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

