---
layout: default
title: Regadenoson
parent: Kun modelforudsigelse (L5)
nav_order: 368
evidence_level: L5
indication_count: 8
---

# Regadenoson
{: .fs-9 }

Evidensniveau: **L5** | Forudsagte indikationer: **8** stk.
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

# Regadenoson: Fra farmakologisk kardial stresstest til anafilaski

## Sammenfatning på én sætning

Regadenoson er en selektiv A2A-adenosinreceptoragonist, der klinisk bruges som farmakologisk stressmiddel til kardialperfusionsaftestning (ikke som behandling af en sygdomsindikation). TxGNN-modellen forudsiger, at det kan være effektivt for **anafilaski**, men dette understøttes kun af **1 klinisk forsøg** (som faktisk ikke tester denne anvendelse) og **0 publikationer** — og lægemidlets egen kendte bivirkningsprofil tyder på, at signalet sandsynligvis peger i den forkerte retning.

---

## Hurtig oversigt

| Punkt | Indhold |
|------|--------|
| Oprindelig indikation | Ikke en behandlet sygdom — bruges som farmakologisk stressmiddel til kardialperfusionsaftestning (ifølge mekanistiske noter i evidenspakken); lægemidlet er ikke markedsført i Danmark, så der findes ingen godkendt indikationstekst |
| Forudsagt ny indikation | Anafilaski |
| TxGNN Forudsigelsesscore | 99.85% |
| Bevisniveau | L5 |
| Markedsstatus i Danmark | Ikke markedsført |
| Antal markedsføringstilladelser | 0 |
| Anbefalet beslutning | Vent |

---

## Hvorfor er denne forudsigelse rimelig?

I øjeblikket er detaljerede mekanismedata for regadenosons virkningsmåde ikke tilgængelige i evidenspakken (markeret som et kritisk datahul). Baseret på de mekanistiske noter, der blev registreret, er regadenoson en selektiv **A2A-adenosinreceptoragonist**, der klinisk bruges til at inducere farmakologisk koronar vasodilatation under myokardialperfusionsstressaftestning — det er et diagnostisk værktøj, ikke et terapeutisk middel til en sygdomsindikation.

Kritisk nok kaster evidenspakkens egen analyse stærk tvivl over denne forudsigelse i stedet for at understøtte den. Regadenosons kendt bivirkningsprofil inkluderer rødmen, dyspnø og hypotension — pseudoallergiske (anafylaktoid) reaktioner medieret af A2A/A3-receptoraktivering på mastceller og basofiler. Disse er dokumenterede **risici ved lægemidlet**, ikke behandlingseffekter. Den mest plausible forklaring er, at TxGNN lærte et co-forekomstmønster mellem regadenoson og anafilaski-relaterede termer fra bivirkningsdata og fejlklassificerede dette som et terapeutisk forhold — hvilket betyder, at den forudsagte mekanisme sandsynligvis løber i den **modsatte retning** fra hvad der ville være nødvendigt for nybrug af lægemidlet.

Den samme forsigtighed gælder for de øvrige kandidatindikationer, der returneres for dette lægemiddel (mad-afhængig træningsudløst anafilaski, esotropi, pseudoallergi) — ingen af dem har nogen understøttende klinisk eller mekanistisk evidens, og to af dem deler samme "omvendt bivirkningssignal"-bekymring som anafilaski. Særskilt bemærk, at den rangerede kandidatliste indeholder nøjagtige duplicate-poster (rang 1–2, 3–4, 5–6, 7–8 er hver den samme sygdom med identiske score og evidens) — dette ser ud til at være en data-pipeline-kunstefakt og bør rettes, før der foretages yderligere gennemgang.

---

## Evidenz fra kliniske forsøg

| Forsøgsnummer | Fase | Status | Antal tilmeldte | Vigtige resultater |
|---------|------|------|------|---------|
| [NCT06854458](https://clinicaltrials.gov/study/NCT06854458) | N/A | Rekruttering | 1000 | Multicenterstudium af kardiak stress-MRI-perfusionsaftestning; regadenoson bruges kun som farmakologisk stressmiddel til at simulere træning til kardiakaftestning. Det evaluerer ikke regadenoson til behandling af anafilaski (relevans vurderet til **C — lav relevans** i evidenspakken). |

---

## Litteraturbevis

I øjeblikket ingen relateret litteratur tilgængelig.

---

## Information om det danske marked

Regadenoson er i øjeblikket **ikke markedsført** i Danmark — ingen nationale (Lægemiddelstyrelsen) eller centraliserede (EMA) markedsføringstilladelser blev fundet i evidenspakken (0 licenser på record).

---

## Sikkerhedshensyn

Se venligst det godkendte produktresume (SmPC) for detaljeret sikkerhedsinformation; strukturerede advarsel-, kontraindikations- og lægemiddelinteraktionsdata var ikke tilgængelige i denne evidenspakke (markeret som et blokerende datahul).

Et punkt værd at markere for klinisk gennemgang: lægemidlets kendt bivirkningsprofil (rødmen, dyspnø, hypotension og pseudoallergiske/anafylaktoid-reaktioner via A2A/A3-receptoraktivering) overlapper direkte med den forudsagte indikation selv (anafilaski), hvilket er grundlaget for at behandle denne forudsigelse med forsigtighed i stedet for som et ægte terapeutisk signal.

---

## Konklusion og næste skridt

**Beslutning: Vent**

**Begrundelse:**
- Bevisniveauet er L5 (kun modelforudsigelse) uden relevante kliniske forsøg eller litteratur; det eneste identificerede forsøg tester ikke regadenoson til anafilaski. Evidenspakkens egen mekanistiske analyse tyder på, at TxGNN-signalet sandsynligvis afspejler en omvendt bivirkningstilknytning i stedet for en ægte behandlingseffekt, og samme bekymring gælder for lægemidlets øvrige kandidatindikationer.

**For at fortsætte er følgende nødvendigt:**
- Regadenoson SmPC-advarsler/kontraindikationer (i øjeblikket et blokerende datahul)
- Verificeret virkningsmåde (MOA) data fra DrugBank eller anden primær kilde
- Uafhængig farmakologisk gennemgang for at bekræfte eller afvise hypotesen om "omvendt signal" før yderligere evaluering
- Korrektion af de duplicate-poster på listen over forudsagte indikationer på data-pipeline-niveau

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

