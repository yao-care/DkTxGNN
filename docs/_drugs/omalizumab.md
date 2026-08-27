---
layout: default
title: Omalizumab
parent: 僅模型預測 (L5)
nav_order: 321
evidence_level: L5
indication_count: 10
---

# Omalizumab
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

# Omalizumab: From Allergic Asthma/Urticaria to Bronchitis

## One-Sentence Summary

Omalizumab (Xolair) is a humanized anti-IgE monoclonal antibody whose established use, per the literature captured in this evidence pack, is moderate-to-severe allergic asthma and chronic spontaneous urticaria (CSU); a formal Danish/DrugBank-verified original indication record is not yet available. The TxGNN model predicts a new use in **Bronchitis**, but the **2 clinical trials** and **8 publications** currently attached to this candidate consist almost entirely of asthma data, and the model's own rationale flags this as a likely disease-label/ontology mismatch rather than direct bronchitis evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not registered in Denmark; internationally indicated for moderate-to-severe allergic asthma and chronic spontaneous urticaria (per literature in this pack) |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.9992% |
| Evidence Level | L3 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

A structured mechanism-of-action record from DrugBank is currently flagged as a data gap in this pack (DG002). However, the attached literature is itself informative: omalizumab is a recombinant humanized monoclonal antibody that binds free IgE and blocks its interaction with the high-affinity FcεRI receptor on mast cells and basophils, reducing downstream allergic airway inflammation (PMID 16222080, 11270941). This is the drug's well-documented mechanism in allergic asthma.

On a purely pathophysiological basis, this mechanism could plausibly extend to airway conditions with an eosinophilic/allergic component, such as eosinophilic bronchitis, since chronic bronchitis and asthma share overlapping inflammatory pathways and frequently co-occur clinically.

**However, this rationale should be read with caution.** The model's own `repurposing_rationale` explicitly notes that the trials and literature returned under the "bronchitis" label are almost entirely asthma studies (e.g., NCT02477332 is a Chronic Spontaneous Urticaria trial; the literature set includes reviews titled "Omalizumab in asthma" and "Adult asthma exacerbations"), with only one case report (PMID 31478531) tangentially referencing bronchitis via a post-procedural complication. This pattern suggests a likely knowledge-graph node overlap between "bronchitis" and "asthma" rather than a genuine, independently supported repurposing signal for bronchitis itself.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02049294](https://clinicaltrials.gov/study/NCT02049294) | Phase 2/3 | Completed | 11 | Steroid-sparing effect of omalizumab in patients with asthma and persistent eosinophilic bronchitis; very small sample (relevance grade B — actual population is asthma + eosinophilic bronchitis, not bronchitis alone) |
| [NCT02477332](https://clinicaltrials.gov/study/NCT02477332) | Phase 2 | Completed | 382 | Dose-finding study of QGE031 (ligelizumab, an anti-IgE agent related to omalizumab) as add-on therapy in Chronic Spontaneous Urticaria — disease population does not match bronchitis (relevance grade C) |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [16222080](https://pubmed.ncbi.nlm.nih.gov/16222080/) | 2005 | Review | Clinical reviews in allergy & immunology | Overview of omalizumab approval and post-approval experience; efficacy established in moderate-to-severe persistent asthma, not bronchitis |
| [21121874](https://pubmed.ncbi.nlm.nih.gov/21121874/) | 2011 | Cohort/Safety Study | Current medical research and opinion | Pooled safety analysis of omalizumab in children with allergic (IgE-mediated) asthma |
| [35369622](https://pubmed.ncbi.nlm.nih.gov/35369622/) | 2022 | Cohort | Postepy dermatologii i alergologii | Omalizumab in older patients with severe allergic asthma-COPD overlap |
| [30196731](https://pubmed.ncbi.nlm.nih.gov/30196731/) | 2018 | Review | Expert opinion on pharmacotherapy | Discusses smoking-induced airway diseases (chronic bronchitis, emphysema) as comorbid with asthma; not an omalizumab efficacy study in bronchitis |
| [17663923](https://pubmed.ncbi.nlm.nih.gov/17663923/) | 2007 | Review | Allergologia et immunopathologia | General review of monoclonal antibody use in pediatrics; mentions anti-IgE therapy only in passing |
| [21163396](https://pubmed.ncbi.nlm.nih.gov/21163396/) | 2010 | Review | Revue des maladies respiratoires | French expert review on adult asthma exacerbations; not bronchitis-specific |
| [31478531](https://pubmed.ncbi.nlm.nih.gov/31478531/) | 2019 | Case Report | Journal of investigational allergology & clinical immunology | Rare case of plastic bronchitis following bronchial thermoplasty (a device procedure); no omalizumab treatment data |
| [26466493](https://pubmed.ncbi.nlm.nih.gov/26466493/) | 2015 | Review | Masui (Japanese J. Anesthesiology) | Perioperative management review of asthma/chronic bronchitis patients; mentions omalizumab as an asthma option only |

---

## Denmark Market Information

Omalizumab currently has **no marketing authorisations on record** in this evidence pack (`total_licenses: 0`, `market_status: 未上市/Not marketed`), so no authorisation table can be populated. Note this reflects the data captured in this evidence pack — omalizumab (Xolair®) holds a centralised EU/EMA marketing authorisation for asthma, CSU, and chronic rhinosinusitis with nasal polyps in other jurisdictions; this should be independently confirmed against the Danish Medicines Agency (Laegemiddelstyrelsen) product register.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information. No structured warnings, contraindications, or drug-drug interaction data were returned for this candidate (DDI query status: not found).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- Evidence level is L3, and — more importantly — the trial and literature evidence attached to the "bronchitis" label is predominantly asthma-focused, indicating this may be a TxGNN disease-node/ontology mapping artifact rather than a validated, independent repurposing signal for bronchitis.
- Two structural data gaps block further evaluation: DG001 (Blocking) — no local product label/warnings available, so a safety pre-screen (S1) cannot be completed; DG002 (High) — no confirmed mechanism-of-action record from DrugBank.
- The drug itself has zero marketing authorisations recorded in Denmark, so there is no local regulatory foothold to build on.

**To proceed, the following is needed:**
- Confirm whether the TxGNN "bronchitis" disease node is distinct from or conflated with "asthma" in the underlying knowledge graph before treating this as a novel candidate.
- Obtain dedicated bronchitis-specific (not asthma-labeled) clinical evidence, ideally from a controlled trial in eosinophilic or chronic bronchitis populations.
- Retrieve the TFDA/Danish SmPC warnings and contraindications (DG001) and a confirmed DrugBank mechanism-of-action record (DG002).
- Given the same evidence pack contains a materially stronger, directly relevant candidate — "obstructive lung disease" (i.e., severe allergic asthma), which carries L1 evidence (multiple completed Phase 3 RCTs, e.g., NCT00314574, n=850) and a "Proceed with Guardrails" recommendation — that candidate should be evaluated separately as it appears to be the true source of the high-quality trial data currently misattributed to bronchitis.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

