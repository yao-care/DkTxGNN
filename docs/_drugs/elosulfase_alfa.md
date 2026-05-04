---
layout: default
title: Elosulfase Alfa
parent: 僅模型預測 (L5)
nav_order: 159
evidence_level: L5
indication_count: 10
---

# Elosulfase Alfa
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

# Elosulfase Alfa: From Mucopolysaccharidosis IVA to Scheie Syndrome

## One-Sentence Summary

Elosulfase alfa is a recombinant human enzyme replacement therapy (ERT) that directly replaces the deficient N-acetylgalactosamine-6-sulfatase (GALNS) enzyme, approved internationally for Mucopolysaccharidosis IVA (Morquio A syndrome), but currently not registered in Denmark. The TxGNN model assigns its highest score to **Scheie Syndrome** (MPS IS) at **99.90%**; however, this prediction lacks direct mechanistic support — Scheie syndrome is caused by a completely different enzyme deficiency (IDUA) — and is backed by only **2 observational publications** with no elosulfase-specific data. This is a multi-indication evaluation: five unique predicted indications are assessed below, ranging from Hold (L5) to Proceed with Guardrails (L1).

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Mucopolysaccharidosis IVA / Morquio A Syndrome (GALNS enzyme deficiency; internationally approved, not registered in Denmark per available regulatory data) |
| Predicted New Indication (Rank 1) | Scheie Syndrome (MPS IS) |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L5 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Predicted Indications — Full Summary

This evidence pack covers five unique predicted indications (Candidate ID: TW-DB09051-multi). Duplicate ranks have been deduplicated.

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Recommendation |
|------|---------------------|-------------|----------------|----------------|
| 1 | Scheie Syndrome (MPS IS) | 99.90% | L5 | Hold |
| 2 | Lysosomal Storage Disease with Skeletal Involvement | 99.59% | L1 | Proceed with Guardrails |
| 3 | Hurler Syndrome (MPS IH) | 99.43% | L3 | Research Question |
| 4 | Sanfilippo Syndrome (MPS III) | 99.42% | L4 | Hold |
| 5 | Camptodactyly, Myopia & Medial Rectus Fibrosis | 99.09% | L5 | Hold |

> **Clinical context**: Rank 2 ("Lysosomal Storage Disease with Skeletal Involvement") is functionally equivalent to MPS IVA — elosulfase alfa's established international indication. Its L1 rating reflects the pivotal Phase 3 MORPH trial (NCT01572896, n=176). This serves as an internal validation demonstrating TxGNN's ability to correctly identify the drug's known indication within the knowledge graph.

---

## Why Is This Prediction Reasonable?

**Scheie Syndrome (Rank 1 — Highest TxGNN Score)**

Detailed mechanism of action data is not available in this Evidence Pack. Based on published literature, elosulfase alfa is a recombinant form of human N-acetylgalactosamine-6-sulfatase (GALNS). GALNS deficiency leads to lysosomal accumulation of keratan sulfate (KS) and chondroitin-6-sulfate (C6S), causing progressive skeletal dysplasia, short stature, ligamentous laxity, and cardiac valve disease — the hallmarks of Mucopolysaccharidosis IVA (Morquio A syndrome).

Scheie syndrome (MPS IS) is caused by a deficiency of an entirely different enzyme — α-L-iduronidase (IDUA) — resulting in accumulation of dermatan sulfate and heparan sulfate, with a distinct clinical profile: corneal clouding, aortic valve disease, and carpal tunnel syndrome, with normal intelligence. There is no enzymatic, substrate, or primary tissue overlap between MPS IS and MPS IVA. Elosulfase alfa cannot compensate for IDUA deficiency, and there is no established scientific rationale for this combination.

The high TxGNN score (99.90%) most likely reflects non-specific similarity between MPS-class nodes in the knowledge graph, not a genuine biological link. **A high prediction score does not override fundamental biochemical incompatibility.** This prediction is not considered biologically plausible based on current knowledge.

**Lysosomal Storage Disease with Skeletal Involvement (Rank 2 — Strongest Evidence)**

This prediction maps directly onto elosulfase alfa's approved indication. The mechanism is straightforward: weekly intravenous infusion of recombinant GALNS is taken up by cells via the mannose-6-phosphate receptor pathway, reaches the lysosome, and degrades the accumulated KS and C6S. The pivotal MORPH trial demonstrated improved endurance (6-minute walk test) and respiratory function in patients aged ≥5 years. This prediction demonstrates model validity and represents the realistic clinical opportunity for Denmark — a market registration pathway.

---

## Clinical Trial Evidence

### Scheie Syndrome (Rank 1)

Currently no related clinical trials registered for elosulfase alfa in Scheie syndrome.

### Lysosomal Storage Disease with Skeletal Involvement (Rank 2)

Currently no trials registered under this specific search query; however, the Phase 3 MORPH trial (NCT01572896) — identified through the repurposing rationale — directly supports this indication. See the Literature section below.

### Hurler Syndrome (Rank 3)

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT04532047](https://clinicaltrials.gov/study/NCT04532047) | Phase 1 | Recruiting | 10 | PEARL trial (PrEnAtal Enzyme Replacement Therapy for Lysosomal Storage Disorders): evaluates maternal and fetal safety and feasibility of in utero ERT for multiple LSD subtypes (including MPS I/Hurler). Estimated completion July 2032. Note: elosulfase alfa is not the agent used in Hurler; laronidase (Aldurazyme) is the relevant ERT for MPS IH. This trial provides class-level evidence for prenatal ERT strategy, not elosulfase-specific efficacy. |

### Sanfilippo Syndrome (Rank 4) and Camptodactyly/Myopia Syndrome (Rank 5)

Currently no related clinical trials registered for either indication.

---

## Literature Evidence

### Scheie Syndrome (Rank 1)

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [35005816](https://pubmed.ncbi.nlm.nih.gov/35005816/) | 2022 | Cohort Study | Human Mutation | Molecular characterisation of 302 Iranian MPS patients using IEM-targeted NGS; includes MPS I subtypes. No elosulfase alfa therapeutic data — cohort study on genetics and epidemiology only. |
| [18584975](https://pubmed.ncbi.nlm.nih.gov/18584975/) | 2009 | Case Series | Pathologie-Biologie | Clinical features and consanguinity of MPS I (Hurler) and MPS IVA (Morquio A) in Tunisian patients; describes IDUA and GALNS enzyme deficiencies. No elosulfase alfa data. |

> These publications relate to the broader MPS disease category and do not contain any evidence of elosulfase alfa efficacy in Scheie syndrome.

### Lysosomal Storage Disease with Skeletal Involvement (Rank 2)

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [41088244](https://pubmed.ncbi.nlm.nih.gov/41088244/) | 2025 | Review | Orphanet J Rare Dis | Comprehensive review of advances in MPS IVA treatment; confirms elosulfase alfa as the only approved ERT, reviews clinical trial data, and discusses limitations including limited efficacy on established bone disease. |
| [39541578](https://pubmed.ncbi.nlm.nih.gov/39541578/) | 2024 | Meta-Analysis Protocol | JMIR Research Protocols | Protocol for meta-analysis of phenotype-genotype correlation in Morquio A syndrome; maps the full clinical spectrum of GALNS mutations relevant to patient stratification. |
| [38831290](https://pubmed.ncbi.nlm.nih.gov/38831290/) | 2024 | Case Series | BMC Medical Genomics | Delayed diagnosis of mild MPS IVA; highlights diagnostic challenge in attenuated phenotypes and underscores the need for early ERT initiation before irreversible skeletal damage. |
| [25496828](https://pubmed.ncbi.nlm.nih.gov/25496828/) | 2015 | Clinical Guideline/Review | Mol Genet Metab | Multidisciplinary guidelines for evaluation, monitoring, and perioperative management of spinal cord compression in Morquio A — directly applicable to elosulfase alfa treatment planning. |
| [36000290](https://pubmed.ncbi.nlm.nih.gov/36000290/) | 2022 | Molecular/Case Report | Ann Hum Genet | Novel splicing variant in GALNS identified; raises need to re-evaluate primer sequences in genetic testing — relevant to pre-treatment diagnosis confirmation. |
| [25944767](https://pubmed.ncbi.nlm.nih.gov/25944767/) | 2015 | Diagnostic Study | Clin Chim Acta | Dried-leukocyte filter paper validated for Morquio A and other LSD newborn screening — important for early diagnosis enabling timely ERT. |

### Hurler Syndrome (Rank 3)

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [35005816](https://pubmed.ncbi.nlm.nih.gov/35005816/) | 2022 | Cohort Study | Human Mutation | See Scheie section above — also includes MPS IH patients in the Iranian cohort; no elosulfase alfa data. |
| [18584975](https://pubmed.ncbi.nlm.nih.gov/18584975/) | 2009 | Case Series | Pathologie-Biologie | See Scheie section above — covers MPS I clinical features. |

### Sanfilippo Syndrome (Rank 4)

> **Important retrieval note**: The 19 publications retrieved for Sanfilippo syndrome are entirely elosulfase alfa studies in MPS IVA (Morquio A), including the pivotal Phase 3 MORPH trial (PMID [24810369](https://pubmed.ncbi.nlm.nih.gov/24810369/)) and long-term extension data. None investigate elosulfase alfa in Sanfilippo syndrome. This reflects a systematic retrieval bias in which elosulfase alfa publications were associated with the broader MPS disease category node. The most clinically relevant of these publications are listed under Rank 2 above.

### Camptodactyly, Myopia & Medial Rectus Fibrosis (Rank 5)

Currently no related literature available.

---

## Denmark Market Information

Elosulfase alfa is **not registered in Denmark** according to the Laegemiddelstyrelsen data in this Evidence Pack (0 marketing authorisations, market status: not marketed).

Healthcare professionals should independently verify whether a valid EMA centralised marketing authorisation (which would apply across all EU/EEA member states including Denmark) exists through the EMA product database, as centralised authorisations may not be fully captured in the current data source.

---

## Safety Considerations

Safety data (key warnings, contraindications, and drug interactions) is not available in this Evidence Pack for this drug.

Please refer to the approved Summary of Product Characteristics (SmPC) — available through the EMA or the relevant national authority — for complete safety information, including infusion-related reaction management, immunogenicity monitoring, and contraindications.

---

## Conclusion and Next Steps

---

### Rank 1: Scheie Syndrome

**Decision: Hold**

**Rationale:**
Elosulfase alfa (GALNS replacement) has no mechanistic basis for treating Scheie syndrome (MPS IS, IDUA deficiency). These represent distinct genetic enzyme deficiencies, different lysosomal substrates, and different primary organ systems. The high TxGNN score reflects knowledge graph topology rather than biological plausibility.

**To proceed, the following would be needed:**
- A credible mechanistic hypothesis explaining how GALNS supplementation could benefit IDUA-deficient pathophysiology
- Preclinical data (cell line or animal model) demonstrating any activity in MPS IS
- This prediction should not advance beyond hypothesis generation without such foundational data

---

### Rank 2: Lysosomal Storage Disease with Skeletal Involvement (MPS IVA)

**Decision: Proceed with Guardrails**

**Rationale:**
This prediction corresponds to elosulfase alfa's internationally established indication (Morquio A syndrome), with Phase 3 RCT-level evidence (MORPH trial, n=176). The drug is not currently registered in Denmark, representing an actionable regulatory gap for this ultra-rare disease.

**To proceed, the following is needed:**
- Verify current EMA centralised authorisation status (EU/1/14/933 — Vimizim) and confirm validity for Denmark
- Initiate reimbursement assessment with the Danish Medicines Council (Medicinrådet) for ultra-rare disease pathway
- Establish specialist metabolic disease centre infrastructure for weekly IV infusion administration, infusion reaction management, and long-term monitoring (6-minute walk test, pulmonary function, urinary KS biomarker)
- Obtain complete SmPC for Danish clinical guidance

---

### Rank 3: Hurler Syndrome (MPS IH)

**Decision: Research Question**

**Rationale:**
Elosulfase alfa does not target the IDUA deficiency underlying Hurler syndrome; however, the PEARL trial (NCT04532047) explores a novel prenatal ERT strategy across multiple LSD subtypes. The research question is whether early (prenatal) intervention with the appropriate enzyme (laronidase for MPS IH) improves long-term outcomes — not whether elosulfase alfa treats Hurler syndrome. Monitoring PEARL trial results is warranted; direct elosulfase alfa development for MPS IH is not indicated.

---

### Ranks 4 & 5: Sanfilippo Syndrome and Camptodactyly/Myopia Syndrome

**Decision: Hold**

**Rationale:**
Both predictions lack mechanistic plausibility and any disease-specific supporting evidence. The Sanfilippo syndrome literature retrieved consists entirely of MPS IVA elosulfase studies (retrieval artefact). The camptodactyly/myopia syndrome has no known link to GALNS or glycosaminoglycan metabolism. Neither indication should be progressed without a fundamental mechanistic re-evaluation.

---

*Data Cutoff: 2026-04-05 | Evidence Pack Version: v4 | Candidate ID: TW-DB09051-multi*

*This report is intended for research reference only and does not constitute medical advice. All drug repurposing candidates require independent clinical validation before therapeutic application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

