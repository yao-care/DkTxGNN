---
layout: default
title: Amitraz
parent: 僅模型預測 (L5)
nav_order: 33
evidence_level: L5
indication_count: 10
---

# Amitraz
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

# Amitraz: From Veterinary Acaricide to Alopecia

## One-Sentence Summary

Amitraz is a broad-spectrum veterinary ectoparasiticide (acaricide) with no approved human medical indication, used exclusively in animals to treat mite infestations such as demodicosis and sarcoptic mange.
The TxGNN model predicts it may be effective for **Alopecia** in humans,
with **0 clinical trials** and **15 publications** (all veterinary animal studies) currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No approved human indication; veterinary acaricide for *Demodex* and *Sarcoptes* mite infestations in animals |
| Predicted New Indication | Alopecia |
| TxGNN Prediction Score | 98.42% |
| Evidence Level | L4 |
| Denmark Market Status | Not marketed |
| Number of Marketing Authorisations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from DrugBank. Based on known pharmacological information, Amitraz is a broad-spectrum acaricide that acts as an **alpha-2 adrenergic agonist** and inhibits monoamine oxidase (MAO) in ectoparasites, causing paralysis and death of mites. It is approved exclusively for veterinary use in several countries for the treatment of *Demodex* spp. (demodectic mites) and *Sarcoptes* spp. (sarcoptic mange mites) infestations in dogs, cats, cattle, and other animals.

The theoretical mechanistic link to human alopecia rests on a single indirect chain of reasoning: in animals, mite infestation of hair follicles causes follicular inflammation and secondary hair loss (alopecia); successful mite eradication with amitraz reliably leads to hair regrowth. By analogy, if *Demodex folliculorum* or *Demodex brevis* overpopulation in human hair follicles were a causally relevant driver of follicular inflammation and hair loss in a specific human alopecia subtype, an effective acaricide might theoretically restore hair growth. This is the pathway that the TxGNN knowledge graph has captured with a high score.

However, the strength of this biological hypothesis is currently very limited. All 15 retrieved publications are exclusively veterinary case reports and reviews in dogs, cats, ferrets, alpacas, and other animals — there is no direct human clinical evidence. Critically, amitraz carries significant systemic safety concerns in humans (hypotension, bradycardia, sedation, respiratory depression) arising from alpha-2 adrenergic agonism, which constitutes a major barrier to any human clinical development. The TxGNN score of 98.42% most likely reflects indirect semantic linkage in the knowledge graph ("acaricide → eliminates *Demodex* → resolves alopecia"), rather than a genuine human efficacy signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered (ClinicalTrials.gov and ICTRP both returned 0 results for Amitraz + alopecia).

---

## Literature Evidence

> **Note:** All 15 retrieved publications are veterinary studies. No human clinical evidence is available for this drug–disease pair.

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [22488596](https://pubmed.ncbi.nlm.nih.gov/22488596/) | 2012 | Veterinary Narrative Review | Compendium (Yardley, PA) | Overview of canine demodicosis therapy; amitraz rinse (0.025%) approved every 2 weeks; higher concentrations improve success rate but increase adverse effects |
| [22167167](https://pubmed.ncbi.nlm.nih.gov/22167167/) | 2011 | Veterinary Evidence-Based Review | Tierarztliche Praxis | Evidence-based summary of canine demodicosis treatment options; disease characterised by alopecia, papules and crusts; amitraz among standard therapies |
| [32814497](https://pubmed.ncbi.nlm.nih.gov/32814497/) | 2021 | Veterinary Case Report | New Zealand Veterinary Journal | Combination topical amitraz + subcutaneous ivermectin successfully treated sarcoptic and chorioptic mange with extensive alopecia, erythema and crusting in an alpaca herd |
| [34022785](https://pubmed.ncbi.nlm.nih.gov/34022785/) | 2021 | Veterinary Case Report | Annals of Parasitology | *Psoroptes ovis* parasitism reported in a dog; irregular alopecia, scabs, dry desquamation and erythema; treated with acaricide |
| [19265536](https://pubmed.ncbi.nlm.nih.gov/19265536/) | 2009 | Veterinary Case Report | Parasites & Vectors | Amitraz + metaflumizone spot-on formulation effective against generalised canine demodectic mange with diffuse alopecia; *Demodex* and *Malassezia pachydermatis* co-infection resolved |
| [19843334](https://pubmed.ncbi.nlm.nih.gov/19843334/) | 2009 | Veterinary Case Series | Acta Veterinaria Scandinavica | *Demodex gatoi*-associated contagious pruritic dermatosis in cats from 6 Finnish households; skin disease with alopecia and pruritus |
| [17610494](https://pubmed.ncbi.nlm.nih.gov/17610494/) | 2007 | Veterinary Case Report | Veterinary Dermatology | Three alpacas with sarcoptic mange unresponsive to eprinomectin/doramectin successfully treated with amitraz; extensive alopecia, erythema and scaling resolved |
| [15624702](https://pubmed.ncbi.nlm.nih.gov/15624702/) | 2004 | Veterinary Comparative Study | Immunological Investigations | Comparison of amitraz (conventional) vs. T11TS immunotherapy in canine generalised demodicosis; immunotherapy showed superior immune restoration alongside alopecia resolution |
| [8833611](https://pubmed.ncbi.nlm.nih.gov/8833611/) | 1996 | Veterinary Case Report | The Veterinary Quarterly | Demodicosis with local alopecia in two ferrets; amitraz treatment was effective and did not cause noticeable adverse effects |
| [7492657](https://pubmed.ncbi.nlm.nih.gov/7492657/) | 1995 | Veterinary Case Report | J Veterinary Medical Science | Golden hamster with dorsal alopecia from *Demodex* spp.; topical amitraz 0.013% partially effective; complete cure achieved with coumaphos |

---

## Denmark Market Information

Amitraz is **not marketed in Denmark** and holds **no marketing authorisations** from the Danish Medicines Agency (Lægemiddelstyrelsen) or the European Medicines Agency (EMA) for any human indication.

> There are no registered human-use products containing amitraz in Denmark. In the EU/EEA, amitraz is approved exclusively as a veterinary medicinal product (e.g., for tick and mite control in dogs under the trade name Ectodex/Taktic in certain member states), with no centralised or national human marketing authorisation.

---

## Safety Considerations

**Key Warnings:**

Amitraz is not approved for human use in any jurisdiction. Based on accidental human poisoning case reports and toxicological data, the following systemic risks are documented:

- **Alpha-2 adrenergic toxidrome:** Central nervous system depression (sedation, coma), hypotension, bradycardia, hypothermia, miosis, and respiratory depression. Yohimbine (alpha-2 antagonist) has been used as an antidote in animal poisoning cases.
- **No human SmPC available:** As no human marketing authorisation exists, there is no approved Summary of Product Characteristics for human safety reference.
- **No drug interaction data available** from DrugBank for human use context.

> As Amitraz holds no approved human indication or marketing authorisation in Denmark or any other country, please refer to toxicological reference databases (e.g., TOXBASE, Micromedex) and veterinary product SmPCs for available safety and exposure information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The entire available evidence base consists exclusively of veterinary case reports and reviews in animals (L4), with no human clinical trials, no human observational data, and no human mechanistic studies. Combined with the absence of any human marketing authorisation globally, significant systemic safety risks from alpha-2 adrenergic agonism, and critical data gaps in MOA and human safety profiling, there is currently no basis to advance amitraz as a human drug repurposing candidate for alopecia.

**To proceed, the following would be needed:**

- **Proof-of-concept in humans:** Evidence that *Demodex* overpopulation is causally linked to the specific alopecia subtype in question (e.g., biopsy-confirmed demodicosis-associated alopecia)
- **Human safety pharmacology data:** Dermal absorption, systemic bioavailability, and tolerability of a topical amitraz formulation in humans
- **Preclinical studies in human skin models:** In vitro or ex vivo studies confirming efficacy against human *Demodex* with acceptable safety margins
- **Mechanism of action clarification:** Full pharmacological profile from DrugBank/primary literature to assess alpha-2 agonist systemic exposure risk with topical application
- **Regulatory pathway assessment:** Consultation with Lægemiddelstyrelsen on feasibility of a first-in-human programme given the current regulatory status (no approved human product)
- **Drug interaction data:** Formal DDI assessment before any human study can be designed

---

*This report is generated for research purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before any therapeutic application. Data cut-off: 2026-04-04.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

