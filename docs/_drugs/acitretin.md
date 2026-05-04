---
layout: default
title: Acitretin
parent: 僅模型預測 (L5)
nav_order: 15
evidence_level: L5
indication_count: 8
---

# Acitretin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

# Acitretin: From Psoriasis to Acne

## One-Sentence Summary

Acitretin is a second-generation oral aromatic retinoid internationally established for the treatment of severe psoriasis and other keratinization disorders, though it currently holds no marketing authorisation in Denmark.
The TxGNN model predicts it may be effective for **acne (disease)** — including hidradenitis suppurativa (acne inversa) — with a prediction score of **99.94%**.
Evidence supporting this direction includes **1 clinical trial** (indirect, retinoid class context only) and **18 publications**, several of which directly report acitretin use in hidradenitis suppurativa and acne-spectrum conditions.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Severe psoriasis and keratinization disorders (established international use; not registered in Denmark) |
| Predicted New Indication | Acne (disease), including hidradenitis suppurativa / acne inversa |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L3 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Acitretin is the active metabolite of etretinate and acts as a full agonist at nuclear retinoic acid receptors (RAR-α, RAR-β, and RAR-γ). Through these receptors, it regulates gene transcription controlling keratinocyte proliferation, differentiation, and sebaceous gland activity. Critically for acne, RAR activation downregulates lipogenesis genes in sebaceous glands, reducing sebum production — a central pathogenic driver of both acne vulgaris and hidradenitis suppurativa (HS). In parallel, acitretin exerts anti-inflammatory and immunomodulatory effects by suppressing pro-inflammatory cytokines (IL-1β, TNF-α) and inhibiting leukotriene C4 release from eosinophils, addressing the inflammatory component of acne-spectrum disease.

The mechanistic overlap between acitretin's established indication (psoriasis) and acne is substantial. Both conditions involve abnormal keratinocyte differentiation, follicular hyperkeratinisation, and dysregulated inflammatory cascades centred on the pilosebaceous unit — the primary target of retinoid therapy. Hidradenitis suppurativa, now frequently termed "acne inversa," is understood as a follicular occlusion disease with a chronic inflammatory component, making RAR agonism a mechanistically rational approach. Importantly, published literature notes that acitretin shows superior efficacy to isotretinoin in HS, precisely because its mechanism better addresses follicular hyperkeratosis rather than sebum suppression alone.

The mechanistic rationale is corroborated by real-world clinical reports: Boer & Nazary (BJD, 2011) describe over 25 years of long-term acitretin therapy for HS with promising outcomes, and Scheman (Cutis, 2002) documents successful treatment of severe nodulocystic acne and HS with acitretin after failed isotretinoin courses. The European S1 Guideline for HS/acne inversa (Zouboulis et al., JEADV 2015) incorporates retinoid therapy within its therapeutic framework, reinforcing the scientific credibility of this repurposing direction.

---

## Clinical Trial Evidence

The evidence search identified only one clinical trial, which is of low direct relevance to acitretin for acne:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT04663906](https://clinicaltrials.gov/study/NCT04663906) | N/A | Unknown | 300 | Observational study assessing whether oral **isotretinoin** (not acitretin) increases COVID-19 infection risk in acne patients via retinoid-induced mucosal dryness. Study drug is a different retinoid; primary endpoint is infectious risk, not treatment efficacy. Provides retinoid class background only — no direct evidence for acitretin in acne. |

> No clinical trials specifically evaluating acitretin for acne vulgaris or hidradenitis suppurativa are currently registered on ClinicalTrials.gov or the WHO ICTRP.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [20874789](https://pubmed.ncbi.nlm.nih.gov/20874789/) | 2011 | Retrospective case series | Br J Dermatol | **Direct acitretin evidence**: Long-term acitretin therapy for HS over 25 years; acitretin shows promising outcomes where isotretinoin has limited effect; challenges the label "acne inversa" given distinct mechanisms |
| [12080949](https://pubmed.ncbi.nlm.nih.gov/12080949/) | 2002 | Case Report | Cutis | **Direct acitretin evidence**: Severe nodulocystic facial acne and HS successfully treated with acitretin after two full courses of isotretinoin failed to achieve remission |
| [25640693](https://pubmed.ncbi.nlm.nih.gov/25640693/) | 2015 | Clinical Guideline (S1) | JEADV | European S1 guideline for HS/acne inversa; retinoid therapy included as treatment option; covers epidemiology (1% prevalence in Europe), disease burden, and management framework |
| [29234829](https://pubmed.ncbi.nlm.nih.gov/29234829/) | 2018 | Review | Der Hautarzt | Drug therapy of acne inversa; describes retinoids (including acitretin) alongside antibiotics (clindamycin/rifampicin) and TNF-α inhibitors (adalimumab) as therapeutic options |
| [41692081](https://pubmed.ncbi.nlm.nih.gov/41692081/) | 2026 | Review | Clin Dermatol | Comprehensive review of vitamin A and retinoids in dermatology; explicitly names acitretin among therapeutic oral retinoids; discusses indication spectrum including inflammatory skin diseases |
| [9074840](https://pubmed.ncbi.nlm.nih.gov/9074840/) | 1997 | Review | Drugs | Overview of retinoid use in dermatology; acitretin (second-generation) used for psoriasis, hyperkeratotic disorders, severe acne-related dermatoses, and chemoprevention of skin cancer |
| [8573927](https://pubmed.ncbi.nlm.nih.gov/8573927/) | 1995 | Mechanistic Review | Dermatology | Retinoid inhibition of sebaceous gland activity; evaluates whether anti-acne effects of newer oral retinoids (including acitretin) can be predicted from experimental models |
| [2112772](https://pubmed.ncbi.nlm.nih.gov/2112772/) | 1990 | Mechanistic Study | Prostaglandins | Acitretin demonstrated inhibition of leukotriene C4 release from eosinophils — supporting the anti-inflammatory mechanism relevant to acne pathogenesis |
| [1617858](https://pubmed.ncbi.nlm.nih.gov/1617858/) | 1992 | PK/Efficacy Review | Clin Pharmacokinet | Pharmacokinetics and clinical efficacy of retinoids including acitretin; describes second-generation retinoids' primary success in psoriasis with relevant discussion of acne-spectrum applications |
| [11586072](https://pubmed.ncbi.nlm.nih.gov/11586072/) | 2001 | Review | Skin Pharmacol Appl Skin Physiol | Retinoids as pleiotropic compounds acting via nuclear receptors on specific skin structures; discusses future dermatological indications and mechanistic basis for acne-spectrum conditions |

---

## Denmark Market Information

Acitretin currently holds no national or centralised marketing authorisation in Denmark. No product is listed in Lægemiddelstyrelsens register.

| Marketing Authorisation Number | Product Name | Dosage Form | Approved Indication |
|-------------------------------|--------------|-------------|---------------------|
| *No authorisations held in Denmark* | — | — | — |

> **Practical note for Danish prescribers:** Acitretin is commercially available in several EU member states as **Neotigason** (Stiefel/GSK, 10 mg and 25 mg capsules), authorised under the EMA mutual recognition procedure for severe psoriasis and keratinization disorders. Access in Denmark would require an application for special authorisation (*særlig tilladelse*) from Lægemiddelstyrelsen. The Neotigason SmPC is accessible via the EMA medicines database.

---

## Safety Considerations

Detailed safety data from a Danish or EMA package insert could not be retrieved in the current evidence pack. However, acitretin carries well-known class-level safety concerns that are critical for clinical decision-making:

- **Teratogenicity (severe):** Acitretin is a potent teratogen. A strict pregnancy prevention programme is mandatory. Uniquely, acitretin can be re-esterified to etretinate (a long-lasting teratogen) in the presence of alcohol, extending the teratogenic risk window to **at least 3 years** after cessation — substantially longer than for isotretinoin.
- **Hepatotoxicity:** Liver function tests required at baseline and during treatment.
- **Hyperlipidaemia:** Triglyceride and cholesterol monitoring required; dose adjustment may be needed.
- **Mucocutaneous toxicity:** Dry skin, cheilitis, and mucous membrane dryness are very common and dose-dependent.

> Please refer to the approved Summary of Product Characteristics (SmPC) for Neotigason — available via the EMA medicines database — for the complete and authoritative safety profile, contraindications, and drug interaction information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic basis for acitretin in acne-spectrum disease is well-established and pharmacologically coherent (RAR agonism → sebaceous gland suppression, follicular normalisation, anti-inflammatory effects), and real-world clinical use in hidradenitis suppurativa/acne inversa is documented in peer-reviewed literature and endorsed within European clinical guidelines (L3 evidence). However, no randomised controlled trials of acitretin specifically for acne vulgaris or HS have been conducted, no marketing authorisation exists in Denmark, and critical safety documentation has not yet been formally reviewed.

**To proceed, the following is needed:**
- **[Blocking]** Obtain and review the full Neotigason SmPC (EMA) for complete contraindications, warnings, and drug interactions before any clinical use
- **Clarify clinical scope:** Distinguish between acne vulgaris and hidradenitis suppurativa/acne inversa as the target indication — evidence base and treatment context differ substantially
- **Regulatory pathway:** Determine whether a *særlig tilladelse* application to Lægemiddelstyrelsen is required and feasible for the intended patient population
- **Pregnancy prevention protocol:** Establish a mandatory pregnancy prevention programme (analogous to iPLEDGE or EU-RETINOID programme) given acitretin's long teratogenic risk window
- **Evidence upgrading:** Consider initiating or supporting a prospective observational study or systematic review on acitretin in HS to move the evidence level from L3 toward L2

---

*This report is generated for research purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before therapeutic application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

