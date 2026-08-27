---
layout: default
title: Pregabalin
parent: 僅模型預測 (L5)
nav_order: 358
evidence_level: L5
indication_count: 10
---

# Pregabalin
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

# Pregabalin: From Neuropathic Pain to Tendinitis

## One-Sentence Summary

Pregabalin is a globally established anticonvulsant/neuropathic-pain agent, with known indications including neuropathic pain, epilepsy (adjunctive therapy), and generalized anxiety disorder. The TxGNN model predicts potential efficacy for **Tendinitis**, but this direction is currently supported only by **6 publications and no dedicated clinical trials**, none of which directly studied pregabalin for tendinitis pathology itself.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Neuropathic pain / epilepsy (adjunct) / generalized anxiety disorder (established global indications; Danish licence text not available in current dataset) |
| Predicted New Indication | Tendinitis |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L4 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Pregabalin binds the α2δ subunit of voltage-gated calcium channels, reducing calcium influx at nerve terminals and decreasing release of excitatory neurotransmitters such as glutamate and substance P. This mechanism underlies its established efficacy in neuropathic pain and its central antinociceptive effect when used as a perioperative analgesic adjunct.

Tendinitis, however, is primarily a localized inflammatory/collagen-degenerative condition of the tendon, not a neuropathic disorder. The literature retrieved for this pairing does not demonstrate a tendinitis-specific mechanism. Instead, it clusters around two unrelated themes: pregabalin used as a perioperative analgesic after arthroscopic rotator cuff (tendon) surgery, and an unrelated case report of fluoroquinolone-induced tendinopathy. Neither line of evidence addresses pregabalin's effect on tendon inflammation or repair.

This pattern suggests the high TxGNN similarity score likely reflects a shared "pain / orthopedic surgery" node in the knowledge graph rather than a genuine tendinitis-specific pharmacological link. Given the indirect mechanistic overlap, this prediction should currently be treated as a hypothesis-generating signal only (Evidence Level L4), not a basis for clinical application.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32839073](https://pubmed.ncbi.nlm.nih.gov/32839073/) | 2021 | RCT (retrospective cohort) | J Orthop Sci | Evaluated opioid-sparing analgesic effect of pregabalin after arthroscopic rotator cuff repair; not a tendinitis treatment study |
| [34052386](https://pubmed.ncbi.nlm.nih.gov/34052386/) | 2022 | RCT | Arthroscopy | Compared perioperative oral pregabalin vs. interscalene brachial plexus block for post-rotator-cuff-repair pain control |
| [41017607](https://pubmed.ncbi.nlm.nih.gov/41017607/) | 2025 | Case report | Praxis | Describes fluoroquinolone (ciprofloxacin)-associated tendinopathy; unrelated to pregabalin |
| [40818536](https://pubmed.ncbi.nlm.nih.gov/40818536/) | 2025 | Editorial commentary | Arthroscopy | Discusses piriformis syndrome and sciatic nerve/tendon release; not a tendinitis pharmacotherapy study |
| [37051935](https://pubmed.ncbi.nlm.nih.gov/37051935/) | 2023 | Case report | Pain Practice | Posterior femoral cutaneous nerve impingement from running-related tendonitis; no pregabalin intervention described |
| [39703364](https://pubmed.ncbi.nlm.nih.gov/39703364/) | 2024 | Animal study | Adv Pharmacol Pharm Sci | Herbal extract (Cissus quadrangularis) effect on vincristine-induced neuropathy; unrelated to pregabalin |

## Denmark Market Information

Pregabalin currently has no marketing authorisation registered in the Danish Medicines Agency (Lægemiddelstyrelsen) dataset used for this evaluation (0 licences on file, market status "Not marketed").

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic link between pregabalin and tendinitis is indirect (perioperative analgesia after tendon surgery, not tendon pathology treatment), no dedicated clinical trials exist, and a Blocking-severity data gap on Danish SmPC warnings/contraindications (DG001) prevents any safety evaluation.

**To proceed, the following is needed:**
- Danish SmPC warnings and contraindications for pregabalin (DG001, Blocking — currently prevents Stage S1 safety review)
- Confirmed mechanism-of-action data via DrugBank API (DG002)
- Mechanistic or preclinical studies directly testing pregabalin's effect on tendon inflammation/repair, rather than general perioperative pain control
- Note: among the other TxGNN-predicted candidates in this pack, **migraine disorder** (score 99.47%) currently shows stronger supporting evidence (Evidence Level L2, multiple RCTs and a Cochrane review on antiepileptics including pregabalin for migraine prophylaxis) and may warrant separate evaluation as a more promising repurposing direction than tendinitis.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

