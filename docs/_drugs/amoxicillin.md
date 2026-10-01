---
layout: default
title: Amoxicillin
parent: Kun modelforudsigelse (L5)
nav_order: 35
evidence_level: L5
indication_count: 10
---

# Amoxicillin
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

# Amoxicillin: Fra bakterielle infektioner til polyklonalt hyperviskositetssyndrom

## Resumé i få sætninger

Amoxicillin er et beta-lactam-antibiotikum, der bruges til behandling af bakterielle infektioner.
TxGNN-modellen forudsiger, at det kan have effekt ved **polyklonalt hyperviskositetssyndrom**, men der findes **ingen kliniske forsøg** og **ingen publikationer**, der understøtter forudsigelsen.
Den høje modelscore skyldes sandsynligvis en artefakt i vidensgrafens struktur og ikke reel farmakologi.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Ikke angivet i den danske registrering (indikationsteksten er tom) |
| Forudsagt ny indikation | Polyklonalt hyperviskositetssyndrom |
| TxGNN-prædiktionsscore | 99,63 % |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført |
| Antal markedsføringstilladelser | 1 |
| Anbefalet beslutning | Hold |

---

## Hvorfor er denne forudsigelse (ikke) rimelig?

Der foreligger ingen detaljerede data om virkningsmekanismen i evidenspakken. Amoxicillin er et beta-lactam-antibiotikum, der hæmmer bakteriers cellevægssyntese. Dets effekt ved bakterielle infektioner er veldokumenteret.

Polyklonalt hyperviskositetssyndrom skyldes for meget immunglobulin eller for mange plasmaproteiner i blodet. En antibakteriel virkning på cellevæggen har ingen kendt sammenhæng med denne tilstand, og der er ikke identificeret nogen plausibel mekanistisk forbindelse. Den høje score (0,996) kan derfor ikke kontrolleres mod kendt farmakologi.

Modellen giver også høje scorer for andre tilstande, som heller ikke har nogen identificeret mekanistisk eller klinisk støtte:

| Forudsagt indikation | Score | Vurdering |
|------|------|------|
| Hyperamylasæmi | 99,63 % | Et laboratoriefund med mange årsager. Antibiotika kan højst behandle en underliggende infektion. |
| Medfødt analbuminæmi | 99,59 % | Sjælden genetisk syntesedefekt. Et antibakterielt middel påvirker hverken albuminekspression eller proteinerstatning. |
| Blodtypeinkompatibilitet | 99,40 % | Immunmedieret hæmolyse. Amoxicillin har ingen immunmodulerende virkning her. |
| Præmaligne hæmatologiske sygdomme | 99,29 % | Klonale abnormaliteter. Amoxicillin har ingen kendt antiproliferativ aktivitet. |

Dubletter i prædiktionslisten er slået sammen.

---

## Klinisk evidens

Der er på nuværende tidspunkt ikke registreret nogen relaterede kliniske forsøg.

---

## Litteraturevidens

Der findes på nuværende tidspunkt ingen relateret litteratur.

---

## Markedsinformation for Danmark

| Markedsføringstilladelsesnr. | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28106096118 | Trymox Vet. | Injektionsvæske, suspension | Ikke angivet |

Den eneste registrerede tilladelse er et **veterinærlægemiddel** (Trymox Vet., Univet Limited). Der er ikke identificeret nogen human godkendelse i datagrundlaget. Den eneste tilgængelige administrationsvej er injektion, og kompatibilitet med den forudsagte indikation er ikke vurderet.

---

## Sikkerhedsovervejelser

Data om advarsler, kontraindikationer og interaktioner mangler. Der henvises til det godkendte produktresumé (SmPC) for sikkerhedsoplysninger.

Én relevant observation fra vurderingen: Beta-lactamer kan forårsage lægemiddelinduceret immunmedieret hæmolytisk anæmi. Ved den forudsagte indikation "blodtypeinkompatibilitet" er det derfor en sikkerhedsbekymring og ikke en terapeutisk begrundelse.

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelsen hviler alene på en modelscore (evidensniveau L5). Der er ingen kliniske forsøg, ingen litteratur og ingen plausibel mekanistisk forbindelse. Sikkerhedsscreeningen kan heller ikke gennemføres, fordi advarsler og kontraindikationer fra Lægemiddelstyrelsen mangler.

**Før et eventuelt videre arbejde kræves:**
- Produktresumé med advarsler og kontraindikationer fra Lægemiddelstyrelsen (blokerende hul)
- Data om virkningsmekanisme (MOA) fra DrugBank
- Afklaring af, om der findes en human amoxicillin-registrering i Danmark, da den eneste fundne tilladelse er veterinær
- En biologisk begrundelse for, hvorfor et antibiotikum skulle påvirke immunglobulin- eller plasmaproteinniveauer, før der overvejes prækliniske studier

*Resultaterne er kun til forskningsbrug og udgør ikke medicinsk rådgivning. Kandidater til lægemiddelomplacering kræver klinisk validering, før de kan anvendes.*
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

