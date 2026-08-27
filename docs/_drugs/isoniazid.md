---
layout: default
title: Isoniazid
parent: 僅模型預測 (L5)
nav_order: 246
evidence_level: L5
indication_count: 2
---

# Isoniazid
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Isoniazid: From Tuberculosis to Conjunctivitis

## One-Sentence Summary

Isoniazid is a first-line antitubercular agent, most commonly used for treatment and prevention of tuberculosis (including latent TB infection). The TxGNN model predicts it may be effective for **Conjunctivitis**, but this prediction is supported by only **1 loosely related clinical trial** and **20 publications**, most of which describe *tuberculous* conjunctivitis (a TB disease manifestation) rather than a pharmacological effect of isoniazid on conjunctivitis generally — and at least one source suggests isoniazid can itself *cause* drug-induced conjunctivitis, an opposite-direction signal.

*Note: The evidence pack's `original_indications` field for this drug is empty (data gap); "Tuberculosis" is inferred from the clinical-trial context (isoniazid 5 mg/kg regimen for latent TB infection) included in this pack, not from a confirmed registry entry.*

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Tuberculosis (inferred from trial context; not confirmed in registry data) |
| Predicted New Indication | Conjunctivitis |
| TxGNN Prediction Score | 99.36% |
| Evidence Level | L4 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed, registry-sourced mechanism of action data is not currently available for this candidate (data gap). Based on the mechanistic review included in this evidence pack, isoniazid inhibits mycolic acid synthesis in *Mycobacterium tuberculosis* — a narrow-spectrum antimycobacterial mechanism with no established anti-inflammatory or broad antimicrobial activity relevant to common (viral, bacterial, or allergic) conjunctivitis.

The only genuine mechanistic link identified in the literature is to **tuberculous conjunctivitis** — conjunctival involvement as a manifestation of active or latent TB infection, and its resolution as a downstream consequence of treating the underlying TB, not a direct pharmacological effect on conjunctival inflammation itself. Several older publications (e.g. PMID 14253168, PMID 5103251) describe isoniazid used prophylactically or topically in TB-endemic, TB-associated eye disease, which is a materially different clinical scenario from "conjunctivitis" as a general indication.

Importantly, one review in this evidence pack (PMID 1363080) lists conjunctivitis among the **ocular side effects of systemic drugs**, raising the possibility that the TxGNN association reflects an adverse-effect signal rather than a therapeutic one. This directional ambiguity — supportive evidence limited to TB-specific ocular disease, alongside a plausible adverse-effect explanation — is the primary reason this candidate is rated at a low evidence level despite the high TxGNN score.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04094012](https://clinicaltrials.gov/study/NCT04094012) | Phase 3 | Completed | 490 | Compared systemic drug reaction rates between 3HP (rifapentine + isoniazid) and 1HP regimens for latent TB infection. This is a safety-monitoring trial, not a conjunctivitis efficacy trial — relevance graded "C" (indirect) in this evidence pack. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [14253168](https://pubmed.ncbi.nlm.nih.gov/14253168/) | 1965 | Prophylaxis study | Am Rev Respir Dis | Isoniazid prophylaxis evaluated for phlyctenular keratoconjunctivitis in a TB-endemic Alaskan population |
| [5103251](https://pubmed.ncbi.nlm.nih.gov/5103251/) | 1971 | Case series | Annales d'oculistique | Describes local (topical) use of isoniazid in treatment of ocular tuberculosis |
| [1363080](https://pubmed.ncbi.nlm.nih.gov/1363080/) | 1992 | Review | Optometry Clinics | Review of ocular side effects of systemic drugs; conjunctivitis listed as an adverse effect of several drug classes — a cautionary, not supportive, signal |
| [14089390](https://pubmed.ncbi.nlm.nih.gov/14089390/) | 1964 | Case report | Archives of Ophthalmology | Primary tuberculosis of the conjunctiva |
| [26692731](https://pubmed.ncbi.nlm.nih.gov/26692731/) | 2015 | Case report | Middle East Afr J Ophthalmol | Tuberculous conjunctivitis in an anophthalmic socket following miliary TB |
| [17133069](https://pubmed.ncbi.nlm.nih.gov/17133069/) | 2006 | Case report | Cornea | Mycobacterium tuberculosis presenting as chronic red eye (conjunctival TB) |
| [33607832](https://pubmed.ncbi.nlm.nih.gov/33607832/) | 2021 | Case report | Medicine | Pediatric sinonasal TB presenting with phlyctenular keratoconjunctivitis |
| [10641112](https://pubmed.ncbi.nlm.nih.gov/10641112/) | 1999 | Case series | Oftalmologia | 28 cases of tuberculous keratoconjunctivitis, mostly children with primary TB |
| [25433746](https://pubmed.ncbi.nlm.nih.gov/25433746/) | 2014 | Case report | Can J Ophthalmol | Conjunctival phlyctenulosis as presenting sign of impending clinical TB |
| [4233886](https://pubmed.ncbi.nlm.nih.gov/4233886/) | 1968 | Case report | Arch d'ophtalmologie | Tuberculosis of the bulbar conjunctiva |

---

## Denmark Market Information

Isoniazid is currently **not marketed** in Denmark, and no marketing authorisations are recorded in this evidence pack.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information. No drug interaction data were found in this evidence pack, and key warnings/contraindications are not currently recorded — this is flagged as a **blocking data gap** (see Conclusion).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence level is L4 — the only clinical trial is indirectly relevant (a TB-regimen safety trial, not a conjunctivitis efficacy study), and the supporting literature largely describes TB-related ocular disease rather than a pharmacological effect on conjunctivitis in general. One source raises the possibility that isoniazid causes rather than treats conjunctivitis, directly conflicting with the TxGNN prediction direction.

**To proceed, the following is needed:**
- SmPC warnings/contraindications data (currently a **blocking** gap — required before any safety pre-assessment, per this evidence pack)
- Confirmed mechanism of action documentation (currently a **high-severity** gap affecting mechanistic-relevance analysis)
- A study or trial specifically designed to test isoniazid's effect on non-tuberculous conjunctivitis, to resolve the directional ambiguity in current evidence
- Clarification of whether the TxGNN association reflects a therapeutic signal or an adverse-effect signal
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

