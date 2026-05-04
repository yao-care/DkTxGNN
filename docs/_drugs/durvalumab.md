---
layout: default
title: Durvalumab
parent: 僅模型預測 (L5)
nav_order: 153
evidence_level: L5
indication_count: 10
---

# Durvalumab
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

# Durvalumab: From Urothelial Carcinoma to Prostatic Urethra Urothelial Carcinoma

## One-Sentence Summary

Durvalumab (Imfinzi, AstraZeneca) is an anti-PD-L1 immune checkpoint inhibitor with centralised EMA approval for urothelial carcinoma, non-small cell lung cancer (NSCLC), small cell lung cancer (SCLC), and biliary tract cancer — but it is not currently registered in Denmark.
The TxGNN model predicts it may be effective for **Prostatic Urethra Urothelial Carcinoma**, an extremely rare anatomical variant of urothelial carcinoma (< 1% of all urothelial carcinomas), with a prediction score of **99.98%**.
This prediction is currently supported by **no clinical trials** and **no publications** specific to this subtype, placing the evidence firmly at **L5 (computational prediction only)**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Denmark; EMA-approved internationally for urothelial carcinoma, NSCLC, SCLC, and biliary tract cancer |
| Predicted New Indication | Prostatic Urethra Urothelial Carcinoma |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 — model prediction only; no disease-specific clinical trials or publications identified |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Durvalumab is a fully human IgG1κ monoclonal antibody that selectively blocks PD-L1 (programmed death-ligand 1), preventing its binding to PD-1 and CD80 receptors on T cells. By disabling this immune checkpoint, Durvalumab restores anti-tumour T cell cytotoxicity — a mechanism applicable to any tumour that exploits the PD-L1/PD-1 axis for immune evasion. The broader urothelial carcinoma family is one of the best-characterised tumour types in terms of PD-L1 expression, making checkpoint inhibition a biologically rational strategy across its anatomical variants.

Prostatic urethra urothelial carcinoma shares the same urothelial histological origin as bladder urothelial carcinoma and upper urinary tract urothelial carcinoma (UTUC) — both of which have documented PD-L1 expression and established clinical responses to PD-L1/PD-1 inhibitors. The TxGNN model's high score (0.9998) reflects the strong knowledge graph connectivity between this rare anatomical subtype and the broader urothelial carcinoma node cluster, where PD-L1 pathway associations are well established. This is a case of biologically plausible signal propagation rather than direct disease-specific evidence.

However, the prediction must be interpreted with caution: prostatic urethra urothelial carcinoma is so uncommon that dedicated clinical trials are practically very difficult to conduct, and no published studies of any kind — preclinical, observational, or interventional — were identified for this exact subtype. The mechanistic link is theoretically sound, but entirely unvalidated for this anatomical location. The appropriate next step is to characterise PD-L1 expression rates and tumour microenvironment features in this rare entity before committing to prospective clinical research.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for this specific indication (prostatic urethra urothelial carcinoma).

---

## Literature Evidence

Currently no related literature available for this specific indication.

---

## Denmark Market Information

Durvalumab is not currently registered or marketed in Denmark. No marketing authorisations have been identified through the Danish Medicines Agency (Lægemiddelstyrelsen). Clinicians should refer to the centralised EMA authorisation for Imfinzi (AstraZeneca) for current approved indications, SmPC, and risk management information.

> No marketing authorisation records to display for Denmark.

---

## Supplementary: All Predicted Indications — Overview

The TxGNN model returned five unique disease predictions for Durvalumab, all within the urothelial/genitourinary oncology space. The table below summarises the full landscape to support prioritisation decisions:

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Clinical Trials | Recommended Action |
|------|---------------------|-------------|----------------|-----------------|-------------------|
| 1 | Prostatic urethra urothelial carcinoma | 99.98% | L5 | 0 | Hold |
| 2 | Kidney pelvis sarcomatoid transitional cell carcinoma | 99.98% | L3 | 1 (indirect) | Research Question |
| 3 | Infiltrating bladder urothelial carcinoma — sarcomatoid variant | 99.98% | L3 | 2 (1 terminated) | Research Question |
| 4 | Renal pelvis papillary urothelial carcinoma (UTUC) | 99.98% | L5 | 0 | Hold |
| 5 | Uterine ligament adenocarcinoma | 99.92% | L5 | 0 | Hold |

The two indications with existing clinical trial data — kidney pelvis sarcomatoid transitional cell carcinoma and infiltrating bladder urothelial carcinoma sarcomatoid variant — represent the stronger near-term candidates and are detailed below.

---

### Clinical Trial Evidence — Kidney Pelvis Sarcomatoid Transitional Cell Carcinoma (Rank 2)

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT02812420](https://clinicaltrials.gov/study/NCT02812420) | Early Phase 1 | Active, Not Recruiting | 54 | Pilot pre-surgical study of Durvalumab + Tremelimumab (PD-L1 + CTLA-4 dual blockade) in cisplatin-ineligible muscle-invasive urothelial carcinoma. Enrolment complete; results pending. Relevant as an indirect signal for sarcomatoid urothelial subtypes with highly immunosuppressive tumour microenvironments. |

**Mechanistic note:** Sarcomatoid transformation is associated with epithelial-to-mesenchymal transition (EMT) and PD-L1 upregulation — features that may confer heightened sensitivity to PD-L1 blockade. The dual PD-L1 + CTLA-4 design in NCT02812420 is particularly rational for this high-grade, immune-suppressed subtype.

---

### Clinical Trial Evidence — Infiltrating Bladder Urothelial Carcinoma, Sarcomatoid Variant (Rank 3)

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT03912818](https://clinicaltrials.gov/study/NCT03912818) | Phase 2 | Terminated | 7 | Open-label study of Durvalumab combined with neoadjuvant chemotherapy (MVAC or GC/carboplatin) in **variant histology bladder cancer** — directly including sarcomatoid subtype. Terminated early due to severe under-enrolment (planned vs. actual n=7). Termination reflects recruitment feasibility challenges in rare subtypes, not a negative efficacy signal. Results, if published, should be actively sought. |
| [NCT02812420](https://clinicaltrials.gov/study/NCT02812420) | Early Phase 1 | Active, Not Recruiting | 54 | Broad urothelial carcinoma cohort; indirect support for Durvalumab safety and immunological activity in muscle-invasive disease. |

**Important note on NCT03912818:** Early termination with only 7 patients enrolled means this trial cannot provide meaningful efficacy conclusions. However, it confirms that investigator interest exists and identifies recruiting ultra-rare subtypes as the key operational barrier. This should not be interpreted as evidence against pursuing this indication.

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Immunotherapy — immune checkpoint inhibitor (anti-PD-L1 monoclonal antibody); **not a conventional cytotoxic agent** |
| Myelosuppression Risk | Low (no direct myelosuppressive mechanism; immune-mediated haematological adverse events such as autoimmune haemolytic anaemia are rare but possible) |
| Emetogenicity Classification | Minimal (intravenous monoclonal antibody; infusion-related reactions are possible but not classified as emetogenic) |
| Monitoring Items | Liver function (ALT, AST, bilirubin), thyroid function (TSH, free T4), adrenal function (cortisol), CBC, renal function (creatinine/eGFR), blood glucose — all for immune-related adverse event (irAE) surveillance |
| Handling Protection | Standard aseptic preparation for intravenous infusion; conventional cytotoxic handling precautions (closed system, PPE for cytotoxics) are not required for monoclonal antibody immunotherapies under standard pharmacy guidelines |

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for Imfinzi (EMA centralised authorisation) for full safety information. The current dataset does not contain Danish-specific warnings or contraindications (data gap DG001).

> **Class-level clinical reminder:** As a checkpoint inhibitor, Durvalumab carries a well-characterised spectrum of **immune-related adverse events (irAEs)**, including immune-mediated pneumonitis, hepatitis, colitis, endocrinopathies (hypothyroidism, hyperthyroidism, adrenal insufficiency), nephritis, and dermatitis. These are not documented in the Evidence Pack but are thoroughly described in the Imfinzi EMA SmPC and should be reviewed before any clinical use.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction score for prostatic urethra urothelial carcinoma is exceptionally high (99.98%), reflecting genuine mechanistic plausibility via shared PD-L1 pathway biology across the urothelial carcinoma histological family. However, this anatomical subtype is so rare that no clinical trials or published literature have addressed it specifically — Evidence Level L5 does not support moving beyond hypothesis generation at this stage. Promising signal exists for the related sarcomatoid urothelial variants (Ranks 2–3), where at least indirect trial-level evidence exists.

**To proceed, the following is needed:**

- **Immediate:** Retrieve Durvalumab mechanism of action (MOA) data from DrugBank API (data gap DG002) to complete mechanistic documentation
- **Immediate:** Download and parse the Imfinzi EMA SmPC to address the safety data gap (DG001) — warnings, contraindications, special populations
- **Short-term:** Characterise PD-L1 expression rate and tumour microenvironment features specifically in prostatic urethra urothelial carcinoma (tissue profiling or published case series review)
- **Short-term:** Assess MSI status / TMB profile for this rare subtype — relevant for identifying patients most likely to respond
- **Medium-term:** Evaluate feasibility of enrolling this subtype within existing basket trials targeting PD-L1-positive or variant histology urothelial carcinoma
- **Medium-term:** Pursue results from NCT02812420 (recruitment complete; results pending) and investigate the termination record of NCT03912818 for any extractable data
- **Consider prioritising:** Infiltrating bladder urothelial carcinoma sarcomatoid variant (Rank 3) as the near-term clinical research focus, given it has directly relevant Phase 2 trial precedent (NCT03912818) and represents a more tractable research question within Danish investigator-initiated trial frameworks

> *This report is for research reference purposes only and does not constitute medical advice. All drug repurposing candidates require prospective clinical validation before clinical application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

