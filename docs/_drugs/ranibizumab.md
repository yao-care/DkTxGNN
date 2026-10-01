---
layout: default
title: Ranibizumab
parent: Kun modelforudsigelse (L5)
nav_order: 367
evidence_level: L5
indication_count: 10
---

# Ranibizumab
{: .fs-9 }

Evidensniveau: **L5** | Forudsagte indikationer: **10** stk.
{: .fs-6 .fw-300 }

---

## Indholdsfortegnelse
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Farmaceutens vurderingsrapport

</div>

# Ranibizumab: Fra oprindelig indikation (ikke angivet i data) til svær non-proliferativ diabetisk retinopati

## Resumé i få sætninger

Ranibizumab er en anti-VEGF-antistoffragment (Fab), der gives som injektion i øjet. Datasættet angiver ingen oprindelig indikation. TxGNN-modellen forudsiger, at lægemidlet kan have effekt ved **svær non-proliferativ diabetisk retinopati (NPDR)**. Retningen understøttes af **6 kliniske forsøg** og **20 publikationer**, heriblandt et nyligt fase 3-forsøg med ranibizumab i NPDR.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Ikke angivet i data (indikationsteksten i den danske registrering er tom) |
| Forudsagt ny indikation | Svær non-proliferativ diabetisk retinopati |
| TxGNN-forudsigelsesscore | 99,99 % |
| Evidensniveau | L1 (se forbehold nedenfor) |
| Markedsstatus i Danmark | Markedsført |
| Antal markedsføringstilladelser | 1 |
| Anbefalet beslutning | Proceed with Guardrails (fortsæt med sikkerhedsforanstaltninger) |

---

## Hvorfor er forudsigelsen rimelig?

Der foreligger ingen detaljerede data om virkningsmekanismen i evidenspakken. Ranibizumab er dog et anti-VEGF-Fab-fragment. VEGF fremmer karlækage, retinal non-perfusion og neovaskularisering ved diabetisk retinopati, og VEGF-niveauerne i glaslegemet er forhøjede ved sygdommen (PMID 36580154). Hæmning af VEGF er derfor en biologisk plausibel behandlingsstrategi.

De pivotale RIDE/RISE-forsøg viste regression af sværhedsgraden af diabetisk retinopati under ranibizumab, og fase 3-forsøget PAVILION undersøger direkte ranibizumab via Port Delivery System ved NPDR uden makulaødem.

Datasættet har tomme felter for oprindelig indikation og virkningsmekanisme. Der er derfor sandsynligvis tale om en datamangel og ikke et ægte repurposing-tilfælde. Den gældende godkendte indikation for diabetisk retinopati bør verificeres i officielle kilder, før kandidaten klassificeres som repurposing.

---

## Evidens fra kliniske forsøg

| Forsøgsnummer | Fase | Status | Antal deltagere | Hovedresultater |
|---------|------|------|------|---------|
| [NCT04503551](https://clinicaltrials.gov/study/NCT04503551) | Fase 3 | Aktivt, rekrutterer ikke | 174 | Randomiseret forsøg med ranibizumab via Port Delivery System ved diabetisk retinopati uden central makulaødem. Samme lægemiddel og sygdom (relevans A). |
| [NCT02634333](https://clinicaltrials.gov/study/NCT02634333) | Fase 3 | Afsluttet | 399 | DRCR Protocol W. Intravitreal anti-VEGF til forebyggelse af synstruende komplikationer ved NPDR. Det undersøgte middel er aflibercept, så evidensen gælder stofklassen. |
| [NCT00444600](https://clinicaltrials.gov/study/NCT00444600) | Fase 3 | Afsluttet | 691 | DRCR Protocol I. Ranibizumab eller triamcinolon med laser ved diabetisk makulaødem. Endepunktet er makulaødem, ikke NPDR-sværhedsgrad. |
| [NCT03452657](https://clinicaltrials.gov/study/NCT03452657) | Fase 3 | Ukendt | 118 | Intravitreal ranibizumab versus sham-injektioner til forebyggelse af højrisiko diabetisk retinopati. |
| [NCT02834663](https://clinicaltrials.gov/study/NCT02834663) | Fase 4 | Afsluttet | 25 | Lille enkeltcenterstudie af ranibizumab ved makulaødem med NPDR, med fokus på mikroaneurismer og non-perfunderet retinaareal. |
| [NCT05222633](https://clinicaltrials.gov/study/NCT05222633) | Ikke relevant | Ukendt | 1000 | Observationsstudie af anti-VEGF i den virkelige verden (bl.a. eksudativ AMD). Begrænset relevans for NPDR. |

---

## Litteraturevidens

| PMID | År | Type | Tidsskrift | Hovedresultater |
|------|-----|------|------|---------|
| [40048178](https://pubmed.ncbi.nlm.nih.gov/40048178/) | 2025 | RCT | JAMA Ophthalmology | PAVILION: Port Delivery System med ranibizumab versus observation ved NPDR uden makulaødem. Afprøver kontinuerlig frigivelse med sjældnere behandling. |
| [32606578](https://pubmed.ncbi.nlm.nih.gov/32606578/) | 2020 | Post hoc RCT-analyse | Clinical Ophthalmology | Prædiktorer for tidlig forbedring af diabetisk retinopati med ranibizumab i RIDE/RISE. |
| [36161830](https://pubmed.ncbi.nlm.nih.gov/36161830/) | 2022 | Post hoc RCT-analyse | BMJ Open Ophthalmology | Ændringer i DRSS-score ved mindre hyppig ranibizumab efter induktion (RIDE/RISE-forlængelse). |
| [28448655](https://pubmed.ncbi.nlm.nih.gov/28448655/) | 2017 | Sekundær RCT-analyse | JAMA Ophthalmology | Ændring i diabetisk retinopati over 2 år ved aflibercept, bevacizumab og ranibizumab. |
| [30234859](https://pubmed.ncbi.nlm.nih.gov/30234859/) | 2018 | Sekundær RCT-analyse | Retina | DRCR Protocol I, 5-årsrapport: ændringer i retinopatiens sværhedsgrad under ranibizumab. |
| [39673354](https://pubmed.ncbi.nlm.nih.gov/39673354/) | 2024 | Systematisk review og metaanalyse | Health Technology Assessment | Anti-VEGF sammenlignet med laserfotokoagulation ved diabetisk retinopati. |
| [40347224](https://pubmed.ncbi.nlm.nih.gov/40347224/) | 2025 | Systematisk review og økonomisk analyse | Health Technology Assessment | Anti-VEGF versus laser ved diabetisk retinopati, inkl. økonomisk vurdering. |
| [33966556](https://pubmed.ncbi.nlm.nih.gov/33966556/) | 2021 | Review | Expert Opinion on Biological Therapy | Gennemgang af ranibizumab ved diabetisk retinopati. |
| [36580154](https://pubmed.ncbi.nlm.nih.gov/36580154/) | 2023 | Biomarkørstudie | International Ophthalmology | Serum- og glaslegeme-VEGF ved diabetisk retinopati samt effekt af intravitreale injektioner. |
| [37278412](https://pubmed.ncbi.nlm.nih.gov/37278412/) | 2023 | Simulation/modellering | BMJ Open Ophthalmology | Langtidseffekt af proaktiv anti-VEGF-behandling af svær NPDR versus behandling ved udvikling af PDR. |

---

## Markedsinformation for Danmark

| Markedsføringstilladelse | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28106507820 | Byooviz (Samsung Bioepis NL B.V.) | Injektionsvæske, opløsning | Ikke angivet i data |

---

## Sikkerhedsovervejelser

Der er ingen tilgængelige data om advarsler, kontraindikationer eller lægemiddelinteraktioner i evidenspakken. Der blev ikke fundet interaktioner i opslaget. Se det godkendte produktresumé (SmPC) for sikkerhedsinformation.

---

## Konklusion og næste skridt

**Beslutning: Proceed with Guardrails**

**Begrundelse:**
- Der er et direkte fase 3-forsøg med ranibizumab ved NPDR (PAVILION), en RCT-publikation fra 2025 og omfattende RIDE/RISE-data. Dertil kommer klasseevidens fra DRCR Protocol W og systematiske reviews.
- Evidensniveau L1 bør læses med forbehold. De afsluttede fase 3-forsøg gælder enten aflibercept (Protocol W) eller makulaødem (Protocol I), mens det mest direkte forsøg (NCT04503551) endnu ikke er afsluttet.
- Øvrige forudsagte indikationer (bl.a. forskellige katarakttyper) har ingen plausibel mekanisme eller kun modelbaseret støtte og vurderes som **Hold**.

**For at komme videre kræves:**
- Verifikation af den nuværende godkendte indikation i produktresuméet fra Lægemiddelstyrelsen, da indikationsteksten mangler.
- Sikkerhedsoplysninger (advarsler, kontraindikationer, interaktioner) fra produktresuméet.
- Data om virkningsmekanisme fra DrugBank.
- Afklaring af, om Port Delivery System er tilgængeligt i Danmark, da lægemiddelformen i den danske registrering er injektionsvæske.
- Endelige resultater og regulatorisk status for NCT04503551.
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

