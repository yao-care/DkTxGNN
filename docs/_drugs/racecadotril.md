---
layout: default
title: Racecadotril
parent: Kun modelforudsigelse (L5)
nav_order: 364
evidence_level: L5
indication_count: 10
---

# Racecadotril
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

# Racecadotril: Fra akut diarré til polyklonalt hyperviskositetssyndrom

## Resumé i få sætninger

Racecadotril er et lægemiddel med intestinal antisekretorisk virkning. Det er markedsført i Danmark som granulat til oral suspension (Hidrasec). Indikationsteksten mangler i registreringsdata, men den antisekretoriske virkning peger på diarré.
TxGNN-modellen forudsiger, at det kan have effekt på **polyklonalt hyperviskositetssyndrom**.
Der er **0 kliniske forsøg** og **0 publikationer** bag forudsigelsen, som kun er en modelforudsigelse (evidensniveau L5).

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Ikke angivet i de danske registreringsdata (den antisekretoriske virkning peger på diarré) |
| Forudsagt ny indikation | Polyklonalt hyperviskositetssyndrom |
| TxGNN-forudsigelsesscore | 97,72 % |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført |
| Antal markedsføringstilladelser | 1 |
| Anbefalet beslutning | Hold |

---

## Hvorfor er forudsigelsen (ikke) rimelig?

Racecadotril er et prodrug af thiorphan, en hæmmer af enkephalinase (neprilysin). Stoffet virker antisekretorisk i tarmen. Detaljerede mekanismedata (MOA) fra DrugBank er ikke tilgængelige i den foreliggende datapakke.

Der er **ingen tydelig mekanistisk forbindelse** mellem denne virkning og immunglobulin-drevet hyperviskositet i serum. Den høje score (0,977) er sandsynligvis en artefakt fra vidensgrafen og ikke et tegn på reel effekt.

TxGNN har yderligere fire forudsigelser. Inputtet indeholdt hver indikation to gange (dublerede poster), og de er her slået sammen. Ingen af dem har kliniske forsøg eller litteratur.

| Forudsagt indikation | TxGNN-score | Evidensniveau | Vurdering af mekanisme |
|------|------|------|------|
| Polyklonalt hyperviskositetssyndrom | 97,72 % | L5 | Ingen tydelig mekanistisk forbindelse |
| Hyperamylasæmi | 97,72 % | L5 | Laboratoriefund med mange årsager (pankreas, spytkirtler, nyrer). Der er ingen evidens for, at neprilysinhæmning påvirker den. |
| Kongenit analbuminæmi | 97,53 % | L5 | Sjælden genetisk syntesedefekt. En enkephalinasehæmmer kan ikke rette den. |
| Blodtypeinkompatibilitet | 96,88 % | L5 | Immunmedieret proces uden tilknytning til racecadotrils farmakologi |
| Præmalign hæmatologisk sygdom | 96,61 % | L5 | Neprilysin er undersøgt ved nogle maligniteter, men intet i data forbinder racecadotril med f.eks. MDS eller MGUS. |

---

## Klinisk evidens fra forsøg

Der er i øjeblikket ingen relaterede kliniske forsøg registreret.

---

## Litteraturevidens

Der er i øjeblikket ingen relateret litteratur tilgængelig.

---

## Information om markedet i Danmark

| Markedsføringstilladelsesnr. | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28104880911 | Hidrasec (Bioprojet Europe Ltd.) | Granulat til oral suspension | Ikke angivet i data |

Den eneste tilgængelige administrationsvej er oral.

---

## Sikkerhedsovervejelser

Der er ingen registrerede interaktioner i DrugBank-forespørgslen (0 fund). Data om advarsler og kontraindikationer mangler.
Se det godkendte produktresumé (SmPC) fra Lægemiddelstyrelsen for sikkerhedsoplysninger.

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Alle forudsigelser har kun modelstøtte (L5), uden kliniske forsøg eller publikationer og uden plausibel mekanistisk forbindelse. Sikkerhedsdata fra den danske produktinformation mangler desuden og blokerer videre sikkerhedsscreening.

**For at komme videre kræves:**
- Hentning og gennemgang af produktresuméet (SmPC) fra Lægemiddelstyrelsen for advarsler, kontraindikationer og den godkendte indikation
- Detaljerede data om virkningsmekanisme (MOA) fra DrugBank
- En systematisk litteratur- og forsøgssøgning for racecadotril og de forudsagte sygdomme
- En mekanistisk vurdering af, om neprilysinhæmning overhovedet kan have relevans for de forudsagte tilstande
- En vurdering af administrationsvej (oral granulat) i forhold til de forudsagte tilstande

*Resultaterne er kun til forskningsbrug og udgør ikke medicinsk rådgivning. Kandidater til lægemiddelrepurposing kræver klinisk validering, før de kan anvendes.*
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

