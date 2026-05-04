---
layout: default
title: Basiliximab
parent: 僅模型預測 (L5)
nav_order: 56
evidence_level: L5
indication_count: 10
---

# Basiliximab
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

# Basiliximab: From Renal Transplant Rejection Prophylaxis to Plasma Cell Myeloma

## One-Sentence Summary

Basiliximab (Simulect) is a chimeric monoclonal antibody targeting the IL-2 receptor (CD25), approved globally for prophylaxis of acute organ rejection in renal transplant recipients.
The TxGNN model predicts it may be effective for **Plasma Cell Myeloma** (multiple myeloma), with a prediction score of **95.61%**.
This prediction is currently supported by **3 clinical trials** and **3 publications**, primarily in the context of immune modulation during autologous stem cell transplantation (ASCT) for myeloma.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Prevention of acute organ rejection in renal transplant recipients (globally approved; Simulect/EMA) |
| Predicted New Indication | Plasma Cell Myeloma (Multiple Myeloma) |
| TxGNN Prediction Score | 95.61% |
| Evidence Level | L3 (Pilot/Phase 1–2 studies and observational data) |
| Denmark Market Status | Not marketed in Denmark |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Basiliximab is a chimeric IgG1 monoclonal antibody that specifically binds to and blocks the alpha-chain (CD25) of the interleukin-2 (IL-2) receptor on activated T-lymphocytes. By competitively inhibiting IL-2-mediated T-cell activation and proliferation, it suppresses the immune responses responsible for allograft rejection. This mechanism has established efficacy in transplant immunology.

The connection to plasma cell myeloma is mechanistically grounded in tumour immunology. Multiple myeloma progression is partly driven by immune dysfunction — in particular, the expansion of regulatory T-cells (Tregs), which suppress anti-tumour immune responses. Following autologous stem cell transplantation (ASCT), Tregs reconstitute rapidly and blunt the graft-versus-myeloma effect. Basiliximab, by blocking IL-2 receptor signalling on CD25⁺ Tregs, has been investigated as a strategy to selectively deplete Tregs in the peri-transplant window, thereby restoring effective anti-tumour immunity.

This immunological rationale is directly supported by a completed Phase 1 pilot trial (NCT01526096) and its published results (PMID 31940591), which specifically explored Treg depletion via basiliximab in myeloma patients undergoing ASCT. The shared immunosuppressive biology between transplant rejection and tumour immune evasion makes this repurposing hypothesis biologically coherent.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT01526096](https://clinicaltrials.gov/study/NCT01526096) | Phase 1 | Completed | 30 | Pilot study assessing safety and feasibility of regulatory T-cell depletion using basiliximab in myeloma patients undergoing ASCT |
| [NCT00975975](https://clinicaltrials.gov/study/NCT00975975) | Phase 2 | Completed | 17 | Basiliximab combined with cyclosporine for GVHD prevention after non-myeloablative allogeneic transplantation in blood cancers (including myeloma) |
| [NCT00594308](https://clinicaltrials.gov/study/NCT00594308) | N/A | Terminated | 10 | Early-phase comparison of basiliximab + cyclosporine vs. cyclosporine alone for GVHD prevention; terminated early due to limited accrual |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [31940591](https://pubmed.ncbi.nlm.nih.gov/31940591/) | 2020 | Pilot Study | Journal for Immunotherapy of Cancer | Basiliximab-mediated Treg depletion in myeloma ASCT was feasible; Tregs rapidly reconstitute post-ASCT and suppress anti-myeloma immunity, supporting the rationale for basiliximab intervention |
| [12476283](https://pubmed.ncbi.nlm.nih.gov/12476283/) | 2002 | Case Series | Bone Marrow Transplantation | Basiliximab demonstrated tolerability and efficacy in 17 patients with steroid-refractory acute GVHD after allogeneic SCT, including myeloma patients; supports immunomodulatory activity in haematological malignancy settings |
| [28320553](https://pubmed.ncbi.nlm.nih.gov/28320553/) | 2017 | Case Report | American Journal of Kidney Diseases | Reports on 4 myeloma patients who underwent kidney transplantation (with basiliximab induction) after achieving myeloma remission; demonstrates feasibility of immunosuppression in myeloma survivors |

---

## Denmark Market Information

Basiliximab is not registered or marketed in Denmark. There are no national or centrally authorised marketing authorisations on record in the Danish Medicines Agency (Lægemiddelstyrelsen) database for this drug.

> **Note for clinicians**: Basiliximab is marketed globally as **Simulect** (Novartis) and holds a centralised EMA marketing authorisation (EU/1/98/085) for prevention of acute rejection in adults and children receiving a first kidney transplant. Access in Denmark may require a named-patient or compassionate use application if clinical use is considered.

---

## Safety Considerations

Detailed safety data (key warnings, contraindications, and drug interactions) were not retrieved for this evaluation. Based on general knowledge:

- Basiliximab is an immunosuppressant; use increases susceptibility to infection and risk of lymphoproliferative disorders
- It should not be used in patients with hypersensitivity to basiliximab or any excipients
- Concomitant use with other immunosuppressants (e.g., tacrolimus, cyclosporine, mycophenolate mofetil) requires careful monitoring

Please refer to the approved Summary of Product Characteristics (SmPC) for Simulect for complete safety information, including warnings, contraindications, and drug interactions.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The TxGNN prediction is mechanistically plausible — basiliximab's IL-2 receptor blockade directly targets Treg-mediated immune suppression that enables myeloma progression. A completed Phase 1 pilot trial and published data specifically in myeloma ASCT confirm biological feasibility, though formal efficacy data in Phase 3 is absent and the overall evidence base remains early-stage.

**To proceed, the following is needed:**

- **Full MOA characterisation**: Obtain verified pharmacology data from DrugBank to formally document the Treg-depletion mechanism in the myeloma context
- **Safety data retrieval**: Download and parse the EMA SmPC for Simulect to complete the safety section (warnings, contraindications, DDI profile)
- **Phase 2 efficacy study**: Current evidence is limited to a Phase 1 pilot (n=30); a dedicated Phase 2 randomised trial in myeloma ASCT is needed to establish efficacy endpoints
- **Danish access pathway**: As Basiliximab is not marketed in Denmark, a named-patient access or EMA compassionate use mechanism should be clarified before any clinical application
- **Biomarker strategy**: Define Treg enumeration and IL-2 receptor expression as pharmacodynamic endpoints to confirm on-target activity in future studies

---

> ⚠️ **Disclaimer**: This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before application. All predictions and assessments should be interpreted by qualified healthcare professionals in the context of current clinical guidelines.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

