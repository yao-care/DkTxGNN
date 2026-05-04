---
layout: default
title: Bezlotoxumab
parent: 僅模型預測 (L5)
nav_order: 63
evidence_level: L5
indication_count: 10
---

# Bezlotoxumab
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

# Bezlotoxumab: From Clostridioides difficile Infection to Acute Female Pelvic Peritonitis

## One-Sentence Summary

Bezlotoxumab (Zinplava) is a human monoclonal antibody originally developed to prevent recurrence of *Clostridioides difficile* infection (CDI) by neutralising the bacterial TcdB toxin.
The TxGNN model predicts it may be effective for **Acute Female Pelvic Peritonitis**, however this prediction is supported by **no clinical trials** and **no published literature**.
Critically, mechanistic analysis indicates this prediction most likely reflects a structural artefact in the knowledge graph rather than a genuine therapeutic opportunity.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Reduction of recurrence of *Clostridioides difficile* infection (CDI) in adults receiving antibacterial treatment who are at high risk of recurrence |
| Predicted New Indication | Acute Female Pelvic Peritonitis |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L5 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on known pharmacological information, Bezlotoxumab is a fully human IgG1 monoclonal antibody (DrugBank: DB13140) that binds with high affinity and specificity to *Clostridioides difficile* toxin B (TcdB), neutralising its cytotoxic activity. It has no intrinsic antibacterial properties and no known broad anti-inflammatory or immunomodulatory effects. Its clinical utility is narrowly defined: reducing CDI recurrence in high-risk patients already receiving antibiotic therapy.

The mechanistic connection between Bezlotoxumab and acute female pelvic peritonitis is assessed as extremely weak. Acute pelvic peritonitis is primarily caused by polymicrobial infection (most commonly *Neisseria gonorrhoeae*, *Chlamydia trachomatis*, and enteric organisms) — none of which involve *C. difficile* TcdB as a pathogenic mechanism. Neutralising TcdB would have no expected biological effect on the inflammatory cascade, peritoneal bacterial burden, or tissue damage characteristic of pelvic peritonitis.

Reviewing all ten predicted indications in this Evidence Pack (ranks 1–10), every prediction relates to gynaecological and pelvic anatomy (pelvic peritonitis, fallopian tube cysts, tubal pregnancy, salpingitis isthmica nodosa, broad ligament disease). This striking anatomical clustering strongly suggests the predictions arise from shared "pelvic/adnexal inflammation" nodes in the TxGNN knowledge graph rather than from genuine mechanistic plausibility. This pattern is consistent with a known limitation of graph-based models: anatomical proximity bias, where nodes connected by shared anatomical region generate spuriously high scores. **These predictions should be interpreted as model noise rather than repurposing signals.**

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Denmark Market Information

Bezlotoxumab is not currently marketed in Denmark and holds no marketing authorisations granted by the Danish Medicines Agency (Lægemiddelstyrelsen) or via the EMA centralised procedure active in Denmark.

> **Note for clinicians:** In other jurisdictions (e.g., the United States and the EU), Bezlotoxumab is marketed as **Zinplava** (Merck Sharp & Dohme) for prevention of CDI recurrence. The EMA centralised marketing authorisation (EU/1/16/1136) was granted in 2017 but has since been withdrawn from the EU market. Healthcare professionals requiring access in Denmark should consult Lægemiddelstyrelsen regarding named-patient or compassionate use pathways.

---

## Safety Considerations

Please refer to the approved Summary of Product Characteristics (SmPC) for safety information.

> No drug–drug interaction data, key warnings, or contraindication data were retrieved in this Evidence Pack. The known clinical safety profile of Bezlotoxumab from regulatory approval (FDA, former EMA) should be reviewed directly from the Zinplava SmPC or the FDA prescribing information prior to any clinical consideration.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All ten TxGNN predictions for Bezlotoxumab concern gynaecological pelvic conditions for which there is no mechanistic basis — Bezlotoxumab acts exclusively by neutralising *C. difficile* TcdB toxin and has no known antibacterial, anti-inflammatory, or hormonal activity relevant to pelvic peritonitis or adnexal pathology. The uniform clustering of predictions around pelvic anatomy is a strong indicator of knowledge graph structural bias rather than a genuine repurposing signal. There is no supporting clinical trial or literature evidence for any of the predicted indications.

**To proceed, the following would be needed:**

- **Root cause analysis of the KG artefact:** Investigate which node connections in the TxGNN knowledge graph are driving the pelvic anatomy cluster for Bezlotoxumab, and apply a graph-level correction or exclusion filter for anatomical proximity bias.
- **Mechanism of action data (DrugBank):** Retrieve the full MOA record from DrugBank (DB13140) to formally document target specificity and confirm absence of off-target activity relevant to any predicted indication.
- **Safety documentation:** Obtain the Zinplava SmPC (EMA or FDA) to complete the safety profile — this is currently flagged as a Blocking data gap (DG001).
- **Alternative prediction review:** Re-run TxGNN prediction with bias-corrected graph weights or a stricter mechanistic filter to determine whether any biologically plausible repurposing candidates exist for Bezlotoxumab beyond the CDI indication space (e.g., other *C. difficile*-associated complications such as toxic megacolon or post-CDI inflammatory bowel conditions).
- **Regulatory pathway assessment:** If a genuinely plausible indication is identified in the future, a regulatory consultation with Lægemiddelstyrelsen regarding a new marketing authorisation application or line-extension would be required, given the drug's current absence from the Danish market.

---

> ⚠️ **Disclaimer:** This report is intended for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before application. All content should be reviewed in conjunction with the full approved product information.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

