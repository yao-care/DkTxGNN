---
layout: default
title: Abemaciclib
parent: 僅模型預測 (L5)
nav_order: 12
evidence_level: L5
indication_count: 10
---

# Abemaciclib
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

# Drug Repurposing Evidence Report

## Abemaciclib (DB12001) — Multi-Indication Analysis

**Report ID**: TW-DB12001-multi | **Version**: v4
**Date**: 2026-04-03 | **Data Cutoff**: 2026-04-03
**Prepared for**: Lægemiddelstyrelsen (Danish Medicines Agency) Context

---

## 1. Executive Summary

| Field | Detail |
|-------|--------|
| **Drug** | Abemaciclib (INN); DrugBank ID: DB12001 |
| **Brand Name** | Verzenio™ (Eli Lilly) |
| **Proposed Indications** | 5 unique repurposing candidates identified by TxGNN prediction model |
| **Highest Evidence Level** | **L4** (Preclinical/mechanistic) — Multiple Endocrine Neoplasia |
| **Overall Recommendation** | **Hold / Research Question** — No candidates have direct clinical trial evidence for the proposed indications |

### Top Predicted Indications Summary

| Rank | Disease | TxGNN Score | Evidence Level | Recommendation |
|------|---------|-------------|----------------|----------------|
| 1 | Rheumatoid Arthritis | 0.973 | L5 | Hold |
| 2 | Hyperthyroidism | 0.972 | L5 | Hold |
| 3 | **Multiple Endocrine Neoplasia** | 0.971 | **L4** | **Research Question** |
| 4 | Resistance to Thyroid Hormone (RTHβ) | 0.969 | L5 | Hold |
| 5 | Homozygous Familial Hypercholesterolemia | 0.966 | L5 | Hold |

**Key Findings**: Of the five predicted disease targets, only **multiple endocrine neoplasia (MEN)** reaches L4 evidence level based on a plausible mechanistic rationale connecting CDK4/6 pathway dysregulation to endocrine tumor proliferation. However, no clinical trials directly investigate abemaciclib for any of the five proposed indications. The remaining four candidates lack both clinical evidence and a credible mechanistic link, and are classified as L5 (AI prediction only). Significant data gaps exist for safety labelling and mechanism of action documentation within the Danish regulatory framework.

---

## 2. Drug Overview

### 2.1 Approved Indications

#### International Approvals (EMA/FDA)

Abemaciclib is approved as a selective inhibitor of cyclin-dependent kinases 4 and 6 (CDK4/6) for the treatment of:

- **HR+/HER2− advanced or metastatic breast cancer** in combination with an aromatase inhibitor or fulvestrant as initial or subsequent endocrine-based therapy
- **HR+/HER2− early-stage breast cancer** at high risk of recurrence, in combination with endocrine therapy (adjuvant setting; FDA: monarchE indication)

#### Denmark (Lægemiddelstyrelsen) / EMA Status

Abemaciclib (Verzenio) received **EMA marketing authorisation** and is available in Denmark for the approved breast cancer indications. It is listed in the Danish national formulary under oncology therapeutics. The Medicinrådet (Danish Medicines Council) has issued recommendations regarding its use in specific breast cancer subpopulations.

> **Note**: The evidence pack originates from a Taiwanese (TFDA) regulatory context where abemaciclib is recorded as "未上市" (not marketed). In Denmark, the drug **is** available through EMA centralised authorisation.

### 2.2 Mechanism of Action

| Parameter | Detail |
|-----------|--------|
| **Drug Class** | Selective CDK4/6 inhibitor |
| **Primary Targets** | Cyclin-dependent kinase 4 (CDK4) and cyclin-dependent kinase 6 (CDK6) |
| **Molecular Mechanism** | Inhibits CDK4/6-mediated phosphorylation of the retinoblastoma protein (Rb), preventing the G1→S cell cycle transition and arresting tumour cell proliferation |
| **Selectivity** | Among CDK4/6 inhibitors, abemaciclib demonstrates the highest CDK4 selectivity (CDK4 IC₅₀ ~2 nM vs CDK6 IC₅₀ ~10 nM), with additional activity against CDK9 |
| **Distinguishing Feature** | Ability to cross the blood-brain barrier (demonstrated in NCT02308020) |

> ⚠️ **Data Gap (DG002)**: Detailed MOA documentation from the DrugBank source was flagged as incomplete in the evidence pack. The above is supplemented from EMA Assessment Report (EPAR) and published pharmacology literature.

### 2.3 Pharmacokinetic Profile

| Parameter | Value |
|-----------|-------|
| **Route** | Oral (film-coated tablets: 50 mg, 100 mg, 150 mg, 200 mg) |
| **Bioavailability** | ~45% (absolute) |
| **T_max** | 8 hours (median) |
| **Protein Binding** | ~96.3% (albumin) |
| **Metabolism** | Hepatic via CYP3A4 (primary); active metabolites M2 (N-desethylabemaciclib), M20, M18 |
| **Half-life** | 18.3 hours (abemaciclib); 56.4 hours (M2 active metabolite) |
| **Elimination** | Faecal (81%); renal (3.4%) |
| **CNS Penetration** | Yes — CSF:plasma ratio demonstrated in clinical studies |
| **Dosing** | 150 mg BID (combination); 200 mg BID (monotherapy) — continuous schedule |

---

## 3. Evidence Analysis

### 3.1 Indication 1: Rheumatoid Arthritis (TxGNN Score: 0.973)

**Evidence Level: L5 — AI Prediction Only**

#### Clinical Trials
- **Direct trials**: None identified (0 results on ClinicalTrials.gov; 0 on ICTRP)
- No registered clinical trials investigate abemaciclib for rheumatoid arthritis or any inflammatory arthropathy

#### Published Literature
One indirectly relevant publication was identified:

| PMID | Citation | Relevance |
|------|----------|-----------|
| 40504547 | Jacobs F, et al. *The Oncologist* (2025). "Pre-existing and emerging immune-mediated diseases in patients with breast cancer undergoing CDK4/6 inhibitors and endocrine therapy." | **Indirect** — This observational study examines autoimmune disease emergence (including RA) as an *adverse event* in breast cancer patients receiving CDK4/6 inhibitors, rather than as a therapeutic benefit. |

#### Mechanistic Assessment
**Weak and potentially contradictory**. While CDK4/6 regulates T-cell proliferation (theoretically, inhibition could suppress autoreactive T-cell expansion), clinical evidence indicates CDK4/6 inhibitors more commonly *trigger* immune-related adverse events (interstitial pneumonitis, hepatitis, autoimmune phenomena) rather than exerting immunosuppressive therapeutic effects. No preclinical data support anti-rheumatic efficacy.

#### Verdict
❌ **Not recommended for further pursuit.** The mechanistic link is indirect and contradicted by clinical safety signals suggesting immune activation rather than suppression.

---

### 3.2 Indication 2: Hyperthyroidism (TxGNN Score: 0.972)

**Evidence Level: L5 — AI Prediction Only**

#### Clinical Trials
- **Direct trials**: None identified (0 results across all registries)

#### Published Literature
- No relevant publications identified (0 PubMed results)

#### Mechanistic Assessment
**No credible link.** Hyperthyroidism is primarily driven by TSH receptor autoantibodies (Graves' disease) or autonomous thyroid nodule secretion. The CDK4/6-Rb pathway governs cell cycle progression and has no direct connection to thyroid hormone synthesis, secretion, or autoantibody production. While CDK4/6 inhibition could theoretically reduce thyrocyte proliferation, this does not address the fundamental pathophysiology of hormone overproduction.

#### Verdict
❌ **Not recommended for further pursuit.** No mechanistic, preclinical, or clinical basis exists.

---

### 3.3 Indication 3: Multiple Endocrine Neoplasia (TxGNN Score: 0.971)

**Evidence Level: L4 — Preclinical/Mechanistic Evidence**

> ⭐ **Highest-ranked candidate by evidence quality**

#### Clinical Trials

22 clinical trials were retrieved from ClinicalTrials.gov. However, upon expert review, **none directly investigate abemaciclib for MEN syndrome**. All retrieved trials relate to abemaciclib use in breast cancer or other solid tumours. Key trials reviewed:

| NCT ID | Phase | Status | N | Disease | Relevance to MEN |
|--------|-------|--------|---|---------|-------------------|
| NCT02107703 (MONARCH 2) | Phase 3 | Active | 669 | HR+/HER2− breast cancer | **C** — Safety/efficacy profile reference only |
| NCT02308020 | Phase 2 | Completed | 162 | Brain metastases (breast, NSCLC, melanoma) | **C** — Demonstrates CNS penetration; potentially relevant to MEN1-associated pituitary tumours |
| NCT02981342 | Phase 2 | Completed | 106 | Metastatic pancreatic cancer | **C** — Pancreatic tumours share features with MEN1-associated pNETs |
| NCT03675893 (RESOLVE) | Phase 2 | Recruiting | 180 | Endometrial/ovarian cancer | **C** — Hormone-sensitive tumour context |
| NCT04931342 | Phase 2 | Active | 176 | Rare epithelial ovarian tumours | **C** — Biomarker-driven platform; proof-of-concept for rare tumour types |

#### Published Literature
- No MEN-specific publications identified (0 PubMed results)

#### Mechanistic Assessment
**Moderately plausible.** Several molecular connections support investigation:

1. **MEN1/Menin–Cyclin D axis**: Loss of menin protein (MEN1 gene mutations) leads to upregulation of Cyclin D1, a direct activator of CDK4/6. CDK4/6 inhibition could therefore address downstream consequences of menin loss.
2. **Pancreatic NETs (pNETs)**: MEN1-associated pNETs show dependency on cell cycle progression pathways. Early-phase studies of CDK4/6 inhibitors in pNETs exist in the broader literature.
3. **CDK4 amplification**: Some endocrine tumours (particularly well-differentiated NETs) harbour CDK4 gene amplification or Rb pathway alterations.
4. **CNS penetration**: Abemaciclib's ability to cross the blood-brain barrier is relevant for MEN1-associated pituitary adenomas.

**Limitations**: MEN is a hereditary syndrome with multi-organ tumour manifestations; single-target therapy is unlikely to provide comprehensive disease control. No direct clinical trial data exist.

#### Verdict
🔬 **Research Question** — Warrants further preclinical investigation, particularly in MEN1-associated pNET cell lines and menin-deficient tumour models. A basket trial or case series in MEN1 patients with progressive tumours could be considered.

---

### 3.4 Indication 4: Resistance to Thyroid Hormone (RTHβ) (TxGNN Score: 0.969)

**Evidence Level: L5 — AI Prediction Only**

#### Clinical Trials
- **Direct trials**: None identified (0 results across all registries)

#### Published Literature
- No relevant publications identified (0 PubMed results)

#### Mechanistic Assessment
**No credible link.** RTHβ results from mutations in the THRB gene encoding thyroid hormone receptor beta, causing impaired receptor signalling. This is a nuclear receptor/transcription factor defect with no intersection with CDK4/6-mediated cell cycle control. CDK4/6 inhibition cannot correct a mutant hormone receptor.

#### Verdict
❌ **Not recommended for further pursuit.** Fundamental pathway mismatch.

---

### 3.5 Indication 5: Homozygous Familial Hypercholesterolemia (TxGNN Score: 0.966)

**Evidence Level: L5 — AI Prediction Only**

#### Clinical Trials
- **Direct trials**: None identified (0 results across all registries)

#### Published Literature
- No relevant publications identified (0 PubMed results)

#### Mechanistic Assessment
**No credible link.** HoFH is caused by homozygous mutations in LDLR, APOB, or PCSK9 genes, leading to severely impaired LDL clearance. Cholesterol metabolism and LDL receptor biology operate through pathways entirely distinct from CDK4/6 cell cycle regulation. Although tangential research exists linking cell proliferation with lipid metabolism, this does not constitute a viable therapeutic hypothesis for CDK4/6 inhibition in hypercholesterolemia.

#### Verdict
❌ **Not recommended for further pursuit.** No biological plausibility.

---

## 4. Safety Considerations

> ⚠️ **Data Gap (DG001)**: Local regulatory labelling (TFDA 仿單) was not available. The following safety information is derived from the EMA Summary of Product Characteristics (SmPC) for Verzenio and published clinical trial data.

### 4.1 Known Adverse Effects

| Category | Common (≥10%) | Serious / Notable |
|----------|---------------|-------------------|
| **Gastrointestinal** | Diarrhoea (81–86%), nausea (45%), vomiting (26%), abdominal pain (20%) | Grade 3-4 diarrhoea (13%); requires dose modification |
| **Haematological** | Neutropenia (41–46%), anaemia (29%), thrombocytopenia (16%), leukopenia (21%) | Grade 3-4 neutropenia (24%); febrile neutropenia rare (~1%) |
| **Hepatic** | ALT elevation (13%), AST elevation (11%) | Grade 3-4 hepatotoxicity (~4%); hepatic failure (rare) |
| **Infections** | Infections (31%) | Sepsis, pneumonia |
| **Thromboembolic** | Venous thromboembolism (2–5%) | Pulmonary embolism, DVT |
| **Pulmonary** | — | Interstitial lung disease/pneumonitis (~3%; some fatal) |
| **Renal** | Serum creatinine increase (98%) | Inhibition of tubular secretion transporters (OCT2, MATE); not reflective of GFR change |
| **General** | Fatigue (40%), decreased appetite (24%) | — |

### 4.2 Drug Interactions

| Interaction Type | Agent | Effect | Clinical Significance |
|------------------|-------|--------|----------------------|
| **CYP3A4 inhibitors** (strong) | Ketoconazole, clarithromycin, itraconazole | ↑ Abemaciclib exposure (AUC +16-fold with ketoconazole) | **Contraindicated or dose reduction required** |
| **CYP3A4 inducers** (strong) | Rifampicin, phenytoin, carbamazepine | ↓ Abemaciclib exposure (AUC −90% with rifampicin) | **Avoid co-administration** |
| **CYP3A4 substrates** (sensitive) | Midazolam, simvastatin | ↑ Substrate exposure | Monitor; consider dose adjustment |
| **Transporter substrates** | Metformin (OCT2/MATE) | ↑ Metformin exposure | Monitor renal function |

> ⚠️ **DDI Query Status**: The evidence pack DDI search returned 0 results, indicating a data gap. The above is supplemented from the EMA SmPC.

### 4.3 Contraindications

- Hypersensitivity to abemaciclib or any excipient
- Co-administration with strong CYP3A4 inhibitors should be avoided or managed with dose reduction
- Severe hepatic impairment (Child-Pugh C) — not recommended due to increased exposure

### 4.4 Special Considerations for Repurposing

For the proposed non-oncology indications, the following safety concerns are particularly relevant:

| Concern | Impact on Repurposing |
|---------|----------------------|
| **Myelosuppression** | Unacceptable risk–benefit for non-malignant conditions (RA, hyperthyroidism, HoFH) |
| **Diarrhoea severity** | Quality-of-life impact likely unacceptable for chronic non-oncology use |
| **Immunomodulation** | Paradoxically may *worsen* autoimmune conditions |
| **Teratogenicity** | Embryo-foetal toxicity demonstrated in animal studies; contraindicated in pregnancy |
| **Cost** | Approximately DKK 25,000–30,000/month; not justifiable for unproven indications |

---

## 5. Regulatory Status

### 5.1 Denmark (Lægemiddelstyrelsen)

| Parameter | Status |
|-----------|--------|
| **Marketing Authorisation** | ✅ Authorised via EMA centralised procedure |
| **Brand Name** | Verzenio (Eli Lilly) |
| **Approved Indication** | HR+/HER2− breast cancer (advanced/metastatic and adjuvant) |
| **Reimbursement** | Subject to Medicinrådet recommendation; available through hospital-based oncology |
| **Repurposing Status** | No applications or compassionate use programmes for any predicted indication |

### 5.2 European Medicines Agency (EMA)

| Parameter | Status |
|-----------|--------|
| **Initial Authorisation** | 27 September 2018 (EU/1/18/1307) |
| **Indication Extensions** | Adjuvant breast cancer (2022) |
| **Orphan Designation** | None for any predicted indication |
| **PRIME Designation** | Not applicable for predicted indications |
| **Paediatric Investigation Plan** | Completed for approved indication |

### 5.3 US FDA

| Parameter | Status |
|-----------|--------|
| **Approval Date** | 28 September 2017 (accelerated); 12 October 2021 (adjuvant) |
| **Approved Indications** | HR+/HER2− advanced/metastatic breast cancer; high-risk early breast cancer (adjuvant) |
| **Breakthrough Therapy** | Not for predicted indications |

### 5.4 Taiwan (TFDA) — Source Context

| Parameter | Status |
|-----------|--------|
| **Market Status** | Not marketed (未上市) |
| **Total Licences** | 0 |

---

## 6. Conclusion and Recommendations

### 6.1 Overall Assessment

| Indication | Evidence | Mechanistic Link | Safety Feasibility | Overall |
|------------|----------|------------------|--------------------|---------|
| **Multiple Endocrine Neoplasia** | L4 | Moderate | Acceptable (oncology context) | 🔬 Research Question |
| Rheumatoid Arthritis | L5 | Weak/Contradictory | Poor (toxicity profile) | ❌ Hold |
| Hyperthyroidism | L5 | None | Poor | ❌ Hold |
| RTHβ | L5 | None | Poor | ❌ Hold |
| HoFH | L5 | None | Poor | ❌ Hold |

**Only one candidate — Multiple Endocrine Neoplasia — demonstrates sufficient scientific rationale to warrant further investigation.** The remaining four indications lack both biological plausibility and clinical evidence, and the toxicity profile of abemaciclib (myelosuppression, severe diarrhoea, hepatotoxicity) renders it unsuitable for non-oncological, chronic-disease applications.

### 6.2 Evidence Gaps

| Gap ID | Description | Severity | Recommended Action |
|--------|-------------|----------|-------------------|
| DG001 | Local regulatory labelling (safety warnings/contraindications) | Blocking | Obtain EMA SmPC and Danish national labelling |
| DG002 | Mechanism of action documentation in evidence pack | High | Query DrugBank API; supplement from EMA EPAR |
| — | No direct clinical trials for any predicted indication | High | Literature surveillance; monitor ClinicalTrials.gov |
| — | No MEN-specific preclinical data in pack | Medium | Systematic PubMed search for "CDK4/6 inhibitor" AND "MEN1" or "neuroendocrine tumour" |
| — | Duplicate entries in prediction output (ranks 1/2, 3/4, 5/6, 7/8, 9/10) | Low | Deduplicate TxGNN output pipeline |

### 6.3 Suggested Next Steps

#### For Multiple Endocrine Neoplasia (Priority Candidate)

1. **Targeted Literature Review**: Conduct a systematic search for CDK4/6 inhibitors (abemaciclib, palbociclib, ribociclib) in neuroendocrine tumours, MEN1-associated pNETs, and pituitary adenomas
2. **Preclinical Validation**: Evaluate abemaciclib efficacy in menin-deficient cell line models (e.g., BON-1, QGP-1 pancreatic NET lines)
3. **Clinical Signal Mining**: Query EMA EudraVigilance and FAERS databases for MEN patients who received CDK4/6 inhibitors for concurrent breast cancer — assess any incidental tumour responses
4. **Collaboration**: Engage Danish ENETS (European Neuroendocrine Tumor Society) centres for potential case series or basket trial design
5. **Regulatory Pathway**: Consider EMA orphan medicinal product designation for MEN1-associated progressive NETs if preclinical data are supportive

#### For All Other Candidates

6. **No further action recommended** at this time for rheumatoid arthritis, hyperthyroidism, RTHβ, or HoFH
7. **Pipeline Improvement**: Address duplicate entries in TxGNN output; recalibrate prediction model to incorporate mechanism-of-action pathway compatibility as a filtering criterion

#### Data Gap Remediation

8. Resolve **DG001** (Blocking): Obtain complete EMA SmPC for Danish regulatory context
9. Resolve **DG002** (High): Complete DrugBank API query for comprehensive MOA data

---

## Appendix A: Data Sources Queried

| Source | Queries | Results Found |
|--------|---------|---------------|
| ClinicalTrials.gov | 10 disease-specific queries | 22 (MEN-related keyword match; none directly relevant) |
| WHO ICTRP | 10 disease-specific queries | 0 |
| PubMed | 10 disease-specific queries | 1 (indirect; RA-related) |
| DrugBank | 1 drug query | 1 |
| DDI Database | 1 drug query | 0 (data gap) |

## Appendix B: TxGNN Model Note

The TxGNN knowledge graph prediction model generated high confidence scores (0.966–0.973) for all five candidate indications. However, these scores reflect topological proximity within the biomedical knowledge graph and **do not incorporate mechanism-of-action compatibility, safety feasibility, or clinical translatability assessments**. The high false-positive rate observed (4 of 5 candidates lack biological plausibility) suggests that post-prediction mechanistic filtering is essential for this drug class.

---

> **Disclaimer**: This report is generated for research purposes only and does not constitute medical advice. All drug repurposing candidates require rigorous clinical validation before any therapeutic application. This analysis has not been reviewed or endorsed by the Lægemiddelstyrelsen, EMA, or any regulatory authority. Healthcare professionals should be consulted before making any treatment decisions.
>
> *Report generated: 2026-04-03 | Evidence pack version: v4 | Candidate ID: TW-DB12001-multi*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

