---
layout: default
title: Cerliponase Alfa
parent: 僅模型預測 (L5)
nav_order: 104
evidence_level: L5
indication_count: 10
---

# Cerliponase Alfa
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

# Cerliponase Alfa: From Neuronal Ceroid Lipofuscinosis Type 2 to Scheie Syndrome

## One-Sentence Summary

Cerliponase alfa (Brineura) is a recombinant human tripeptidyl peptidase 1 (TPP1) enzyme replacement therapy, approved in the EU for Neuronal Ceroid Lipofuscinosis type 2 (CLN2 disease / late infantile Batten disease), administered intracerebroventricularly (ICV).
The TxGNN model predicts it may be effective for **Scheie Syndrome** (MPS I-S) with a score of 99.98%, yet **no supporting clinical trials or literature** have been identified for this combination.
This prediction appears to be driven by knowledge graph proximity within the lysosomal storage disease (LSD) category, rather than genuine mechanistic overlap.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Neuronal Ceroid Lipofuscinosis type 2 (CLN2 disease) — TPP1 deficiency causing progressive neurodegeneration in children |
| Predicted New Indication | Scheie Syndrome (MPS I-S) |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Cerliponase alfa is a recombinant form of human tripeptidyl peptidase 1 (TPP1), a lysosomal serine protease. In CLN2 disease, loss-of-function mutations in the *TPP1* gene cause an inability to degrade ceroid-type protein aggregates within neuronal lysosomes, resulting in progressive motor and language decline and premature death in affected children. Cerliponase alfa is delivered via an implanted intracerebroventricular (ICV) reservoir device specifically to bypass the blood-brain barrier and reach CNS neurons — reflecting the fundamentally neurological nature of its target disease.

Scheie syndrome (MPS I-S) is caused by a partial deficiency of a completely different lysosomal enzyme: **α-L-iduronidase (IDUA)**, encoded by the *IDUA* gene. The resulting accumulation of dermatan sulphate and heparan sulphate in connective tissue, heart valves, and other peripheral organs is entirely unrelated to the TPP1/ceroid pathway. An approved enzyme replacement therapy — laronidase (Aldurazyme, BioMarin/Genzyme) — already exists for this indication and targets the correct enzymatic deficit.

The high TxGNN prediction score almost certainly reflects knowledge-graph proximity: both CLN2 and Scheie syndrome are lysosomal storage disorders (LSDs), and the TxGNN model has likely learned strong associations within the LSD disease cluster. However, **enzyme replacement therapies are highly target-specific** — TPP1 has no functional redundancy with IDUA, and administering cerliponase alfa to a patient with Scheie syndrome would not address the underlying glycosaminoglycan accumulation. This is a case where graph-level category similarity does not translate into mechanistic plausibility.

---

## Clinical Trial Evidence

No clinical trials investigating cerliponase alfa in Scheie syndrome have been identified.

---

## Literature Evidence

No publications investigating cerliponase alfa in Scheie syndrome have been identified.

---

## Additional Predicted Indications — Mechanistic Assessment

The Evidence Pack includes four additional predicted indications, all within the LSD category. For completeness, a brief assessment of each is provided below. All carry the same fundamental concern: enzyme-target mismatch.

| Predicted Indication | TxGNN Score | Enzyme Deficit in Disease | Why Cerliponase Alfa Does Not Apply |
|---|---|---|---|
| Scheie Syndrome (MPS I-S) | 99.98% | IDUA (α-L-iduronidase) | Approved ERT exists (Laronidase); TPP1 ≠ IDUA |
| Hurler Syndrome (MPS I-H) | 99.97% | IDUA (same as Scheie, severe phenotype) | Laronidase approved; TPP1 ≠ IDUA |
| LSD with Skeletal Involvement | 99.95% | Multiple (umbrella term: MPS, Gaucher, etc.) | CLN2 is CNS-only; no skeletal pathology; ICV route not relevant |
| Cholesteryl Ester Storage Disease | 99.93% | LAL (lysosomal acid lipase, *LIPA* gene) | Approved ERT exists (Sebelipase alfa/Kanuma); TPP1 ≠ LAL |
| Gaucher Disease | 99.93% | β-glucocerebrosidase (*GBA* gene) | Multiple approved ERTs/SRTs; TPP1 ≠ GBA |

**Note on Gaucher Disease literature**: One PubMed article (PMID [41527340](https://pubmed.ncbi.nlm.nih.gov/41527340/)) was retrieved. This is a methodological paper on natural-history mapping of LSDs using Gaucher disease as a framework; it does not contain any evidence for cerliponase alfa in Gaucher disease.

---

## Denmark Market Information

Cerliponase alfa is not authorised for use in Denmark and holds no marketing authorisations registered with the Danish Medicines Agency (Lægemiddelstyrelsen).

> **Note for prescribers**: Cerliponase alfa (Brineura) holds a centralised EMA marketing authorisation (EU/1/17/1189, granted May 2017) for CLN2 disease throughout the EU/EEA. Access in Denmark would require application through the named-patient or compassionate use pathway. This authorisation covers the drug's approved indication (CLN2) only — not any of the LSD repurposing targets discussed in this report.

---

## Safety Considerations

Detailed Danish SmPC warnings and contraindications for cerliponase alfa were not available in the current dataset. No drug-drug interactions were identified in the DDI database.

Please refer to the approved EMA Summary of Product Characteristics (SmPC) for Brineura for complete safety information, including the known risks associated with ICV catheter implantation, device-related infections, and hypersensitivity reactions.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All five predicted indications are mechanistically implausible repurposing targets for cerliponase alfa: each condition involves a distinct lysosomal enzyme deficiency that is entirely separate from TPP1, the enzyme cerliponase alfa replaces. The high TxGNN scores (≥99.93%) across all predictions reflect category-level similarity within the LSD knowledge graph cluster, not genuine biological overlap. Furthermore, approved enzyme replacement therapies already exist for Scheie syndrome, Hurler syndrome, cholesteryl ester storage disease, and Gaucher disease, leaving no unmet therapeutic niche for cerliponase alfa in these indications.

**To proceed, the following would be needed:**

- **Mechanistic re-evaluation**: A formal mechanistic hypothesis explaining how TPP1 supplementation could benefit any MPS I, LSD-skeletal, CESD, or Gaucher phenotype would need to be established — this is currently absent
- **Preclinical evidence**: In vitro or in vivo studies demonstrating any TPP1-mediated benefit in the predicted disease models would be required as a minimum before clinical investigation could be considered
- **SmPC and safety data**: Complete cerliponase alfa prescribing information (ICV administration risks, infection rates, hypersensitivity profile) must be reviewed for any future cross-indication safety assessment
- **Danish regulatory pathway**: If future evidence were to emerge, a variation to the existing EMA authorisation or a new indication application would be required; named-patient access for non-approved indications would require ethics committee review

> **Research disclaimer**: This report is for research reference purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before any application in patient care.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

