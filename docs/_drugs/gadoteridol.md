---
layout: default
title: Gadoteridol
parent: 僅模型預測 (L5)
nav_order: 200
evidence_level: L5
indication_count: 10
---

# Gadoteridol
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

# Gadoteridol: From MRI Contrast Imaging to Osteoarthritis Susceptibility

## One-Sentence Summary

Gadoteridol (ProHance®) is a non-ionic, macrocyclic gadolinium-based MRI contrast agent (GBCA), primarily used intravenously to enhance tissue visualisation during MRI examinations.
The TxGNN model predicts it may be relevant for **Osteoarthritis Susceptibility**, with a prediction score of **98.90%**; however, **no clinical trials and no supporting therapeutic literature** currently exist for this indication.
The high prediction score most likely reflects a knowledge graph artefact — gadolinium compounds are widely used in OA *diagnostic* imaging, creating network proximity to OA nodes that does not indicate therapeutic activity.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | MRI contrast enhancement (not registered in Denmark; based on established international clinical use) |
| Predicted New Indication | Osteoarthritis Susceptibility |
| TxGNN Prediction Score | 98.90% |
| Evidence Level | L5 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this Evidence Pack. Based on established clinical use, Gadoteridol is a non-ionic, macrocyclic gadolinium chelate (Gd-HP-DO3A) that enhances MRI signal by shortening local T1 relaxation times in surrounding tissue. This allows clearer delineation of lesions, inflammatory tissue, and vascular structures — it has no intended pharmacological interaction with disease pathways.

The predicted indication, *osteoarthritis susceptibility*, is a genetically-defined phenotype describing inherited predisposition to OA — not active joint disease. Gadoteridol has no known molecular targets relevant to OA pathogenesis: it does not interact with cartilage matrix degradation enzymes (MMPs, ADAMTS), chondrocyte signalling cascades, or any genetic susceptibility loci. One theoretical exception exists: free Gd³⁺ ions can block mechanosensitive calcium channels (Piezo1, TRPV4) involved in chondrocyte biology. However, chelated gadoteridol releases negligible free Gd³⁺ at clinical doses, so this mechanism does not translate to a credible therapeutic hypothesis.

The most plausible explanation for the 98.90% TxGNN score is a **knowledge graph network artefact**. Gadolinium-based contrast agents appear extensively in OA research literature — for dual/triple contrast CT cartilage assessment, synovitis MRI evaluation, and proteoglycan quantification — creating strong indirect graph connections to OA-related nodes. The model cannot distinguish between "used to study" and "used to treat." This is a recognised limitation of graph-based repurposing models when diagnostic imaging agents are included in the drug node set.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Gadoteridol in osteoarthritis susceptibility.

---

## Literature Evidence

Currently no related therapeutic literature available for the osteoarthritis susceptibility indication.

> **Contextual note — Osteoarthritis (rank 3, score 98.76%):** Twelve publications were retrieved linking Gadoteridol to osteoarthritis. All 12 papers describe **diagnostic imaging applications only** — not therapeutic interventions. Gadoteridol is used as the non-ionic reference contrast agent in dual- and triple-contrast CT protocols to quantify cartilage proteoglycan content and water distribution. Selected papers are listed below to illustrate the nature of existing evidence.

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [32525582](https://pubmed.ncbi.nlm.nih.gov/32525582/) | 2020 | Ex vivo imaging | J Orthop Res | Dual-contrast CT (iodine CA4+ + gadoteridol) allows earlier characterisation of cartilage degeneration than single-contrast; gadoteridol acts as non-ionic reference agent |
| [37593815](https://pubmed.ncbi.nlm.nih.gov/37593815/) | 2024 | Proof of concept | J Orthop Res | Triple contrast CT (BiNPs + CA4+ + gadoteridol) enables simultaneous cartilage segmentation and biomechanical assessment in cadaveric knee joints |
| [31068614](https://pubmed.ncbi.nlm.nih.gov/31068614/) | 2019 | Synchrotron imaging | Sci Reports | Synchrotron microCT simultaneously quantifies cationic and non-ionic contrast agents in articular cartilage; gadoteridol diffusion reflects water content |
| [39622931](https://pubmed.ncbi.nlm.nih.gov/39622931/) | 2024 | Proof of concept | Sci Reports | Photon-counting CT with dual-contrast approach tracks gadoteridol diffusion in bovine cartilage over 72 h; correlates with biomechanical properties |
| [33692379](https://pubmed.ncbi.nlm.nih.gov/33692379/) | 2021 | Quantitative imaging | Sci Reports | Photon-counting CT assesses articular cartilage health using gadoteridol as non-ionic contrast agent |
| [30816584](https://pubmed.ncbi.nlm.nih.gov/30816584/) | 2019 | Preclinical imaging | J Orthop Res | First application of clinical full-body CT for dual-contrast cartilage imaging using gadoteridol; validates diagnostic approach |
| [31576504](https://pubmed.ncbi.nlm.nih.gov/31576504/) | 2020 | Ex vivo | Ann Biomed Eng | Triple contrast CT method evaluates cartilage composition and enables segmentation; gadoteridol as non-ionic component |
| [31535728](https://pubmed.ncbi.nlm.nih.gov/31535728/) | 2020 | Synchrotron MicroCT | J Orthop Res | Dual-contrast technique with gadoteridol reveals full quantitative potential for cartilage composition assessment |
| [32767676](https://pubmed.ncbi.nlm.nih.gov/32767676/) | 2021 | Mechanistic / diffusion | J Orthop Res | Cartilage constituents (proteoglycans, water, collagen) affect simultaneous diffusion of cationic and non-ionic agents; helps interpret diagnostic accuracy |
| [27161058](https://pubmed.ncbi.nlm.nih.gov/27161058/) | 2016 | Observational | Eur J Radiol | Dynamic contrast-enhanced MRI (gadolinium) assesses peripatellar synovitis in knee OA and its association with pain |

---

## Denmark Market Information

Gadoteridol is **not currently registered or marketed in Denmark**. No national (Lægemiddelstyrelsen) or centralised (EMA) marketing authorisations were identified for this Evidence Pack.

Gadoteridol (ProHance®, Bracco) holds regulatory authorisations in other jurisdictions including the United States (FDA) and the European Union (EMA). Clinicians requiring this contrast agent should consult the SmPC for the applicable authorised product in the relevant jurisdiction.

---

## Safety Considerations

No drug-specific safety data (warnings, contraindications, or drug interactions) was available in this Evidence Pack.

Please refer to the approved Summary of Product Characteristics (SmPC) for full safety information.

> **General safety considerations for gadolinium-based contrast agents relevant to any repurposing context:**
> - **Nephrogenic Systemic Fibrosis (NSF):** Gadolinium chelates are contraindicated or require special caution in patients with severe renal impairment (eGFR <30 mL/min/1.73 m²) or acute kidney injury. Macrocyclic agents such as gadoteridol carry lower NSF risk than linear agents, but the risk is not zero.
> - **Gadolinium tissue deposition:** Repeated or high-dose GBCA administration leads to accumulation of gadolinium in bone, brain (particularly dentate nucleus and globus pallidus), and other tissues. Clinical long-term consequences remain under investigation. This is a critical concern for any hypothetical chronic therapeutic dosing regimen.
> - **Hypersensitivity:** Anaphylactoid reactions are possible, as with all contrast agents.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction score of 98.90% for osteoarthritis susceptibility is almost certainly a knowledge graph false positive: Gadoteridol is a *diagnostic* imaging agent with no pharmacological mechanism relevant to OA pathogenesis, and its frequent appearance in OA imaging research creates spurious network proximity to OA nodes in the knowledge graph. There are no clinical trials, no therapeutic literature, no mechanistic hypothesis, and no approved indication supporting repurposing Gadoteridol as a treatment for osteoarthritis susceptibility or any musculoskeletal disease.

**To proceed, the following would be required:**

- Identification of a biologically plausible therapeutic mechanism connecting Gadoteridol (or chelated gadolinium) to OA susceptibility pathways — currently entirely absent
- Preclinical in vitro/in vivo studies demonstrating therapeutic efficacy in OA or cartilage disease models, distinct from diagnostic imaging applications
- MOA data from DrugBank (DG002) to verify or refute any mechanistic hypotheses involving Gd³⁺-mediated ion channel modulation
- Safety data for chronic/repeated therapeutic dosing, particularly regarding gadolinium tissue deposition (DG001 — TFDA/regulatory SmPC data)
- A scientific rationale explaining why the TxGNN prediction should be taken as a therapeutic signal rather than a diagnostic imaging artefact
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

