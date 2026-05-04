---
layout: default
title: Fidaxomicin
parent: 僅模型預測 (L5)
nav_order: 189
evidence_level: L5
indication_count: 10
---

# Fidaxomicin
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

# Fidaxomicin: From Clostridioides difficile Infection to Staphylococcal Scalded Skin Syndrome

## One-Sentence Summary

Fidaxomicin is a narrow-spectrum macrolide antibiotic approved in the EU (marketed as Dificlir) for the treatment of *Clostridioides difficile*-associated diarrhoea (CDAD), acting primarily within the gastrointestinal tract due to minimal systemic absorption.
The TxGNN model predicts it may be effective for **Staphylococcal Scalded Skin Syndrome (SSSS)**, along with several other Gram-positive bacterial and toxin-mediated infections, as the highest-ranked novel indication.
However, **no clinical trials and no published literature** currently support any of these predicted indications, and the mechanistic evidence for translation to clinical use is considered weak.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | *Clostridioides difficile*-associated diarrhoea (CDAD) |
| Predicted New Indication | Staphylococcal Scalded Skin Syndrome |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L5 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Fidaxomicin exerts its antibacterial effect by selectively inhibiting bacterial RNA polymerase — the same mechanism as rifamycins, but binding to a distinct site. This confers potent activity against Gram-positive anaerobes, most notably *Clostridioides difficile*, with virtually no systemic absorption after oral administration (bioavailability <1%). Its clinical value lies precisely in achieving very high intestinal concentrations while sparing the systemic microbiome.

Staphylococcal Scalded Skin Syndrome (SSSS) is caused by exfoliative toxins (ETA/ETB) produced by *Staphylococcus aureus* — a Gram-positive organism. The TxGNN model has likely captured this taxonomic overlap through knowledge graph node similarity: both *C. difficile* and *S. aureus* are Gram-positive pathogens against which fidaxomicin has demonstrable *in vitro* activity. The same logic applies to the other top-ranked indications (bullous impetigo, impetigo, and botulism), all of which involve Gram-positive or anaerobic pathogens within the Clostridiales or Staphylococcaceae families.

However, the mechanistic link breaks down at the pharmacokinetic level. SSSS and the other predicted skin and toxin-mediated infections require meaningful systemic drug concentrations to reach the site of infection (skin, neuromuscular junction, lung), which fidaxomicin cannot provide. Furthermore, in toxin-mediated diseases such as SSSS and botulism, the pathology is driven by already-released toxins; antibiotic killing of the bacterium plays only a supporting role, and the primary treatment remains antitoxin therapy or systemic anti-staphylococcal agents. The TxGNN model's high scores here reflect structural similarity in the knowledge graph — not clinical translatability.

---

## Clinical Trial Evidence

No clinical trials have been registered for fidaxomicin in any of the predicted indications.

*Currently no related clinical trials registered.*

---

## Literature Evidence

No published literature has been identified linking fidaxomicin to any of the predicted indications.

*Currently no related literature available.*

---

## Denmark Market Information

Fidaxomicin is **not registered in Denmark** and holds no marketing authorisations with the Danish Medicines Agency (Lægemiddelstyrelsen).

> **Note:** Fidaxomicin is approved in the European Union under the centralised procedure as **Dificlir** (fidaxomicin 200 mg film-coated tablets; EU/1/11/736) for the treatment of *C. difficile* infections in adults and children ≥6 months. This product is not currently marketed in Denmark. Danish clinicians requiring access would need to pursue a named-patient or compassionate use pathway.

---

## Safety Considerations

Safety data specific to the Danish/EU regulatory context was not retrieved as part of this Evidence Pack. For complete safety information — including warnings, contraindications, and special populations — please consult:

> Please refer to the approved Summary of Product Characteristics (SmPC) for Dificlir available via the [EMA product page](https://www.ema.europa.eu/en/medicines/human/EPAR/dificlir) for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All five predicted indications are supported exclusively by TxGNN model prediction (Evidence Level L5), with zero clinical trials and zero publications identified. Critically, the pharmacokinetic profile of fidaxomicin — near-zero systemic bioavailability — creates a fundamental mechanistic barrier to treating any infection outside the gastrointestinal lumen, which covers all of the predicted indications.

**The following would be required before this candidate could progress:**

- **Pharmacokinetic reassessment:** Demonstrate whether any alternative route of administration (e.g., topical, inhaled) could achieve therapeutically relevant tissue concentrations at the target site
- **In vitro susceptibility data:** Confirm fidaxomicin MIC values for the specific pathogens involved (*S. aureus* ETA/ETB-producing strains, *C. botulinum*) under conditions relevant to the predicted indication
- **Mechanistic feasibility study:** Address whether the toxin-mediated pathology of SSSS and botulism can be meaningfully altered by bacterial RNA polymerase inhibition after toxin release
- **MOA documentation:** Retrieve full DrugBank mechanistic profile (currently listed as data gap) to support or refute knowledge graph predictions
- **SmPC / Regulatory data:** Obtain full warning and contraindication data from the approved EU SmPC before any clinical hypothesis can enter safety screening (S1)

Given the magnitude of the pharmacokinetic mismatch, repurposing fidaxomicin for systemic or skin infections is **not recommended as a near-term priority** without a novel delivery innovation (e.g., nanoparticle-encapsulated topical formulation). The TxGNN predictions here appear to reflect taxonomic graph proximity rather than true clinical opportunity.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

