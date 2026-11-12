---
layout: default
title: Tezacaftor
parent: Kun modelforudsigelse (L5)
nav_order: 818
evidence_level: L5
indication_count: 3
last_modified_at: 2026-11-06
description: "Tezacaftor: forudsagt ny indikation HIV-infektion (evidensniveau L5). Oprindelig indikation: Cystisk fibrose (de danske godkendelser indeholder ingen indikationst…"
monitor_inn: "tezacaftor"
predicted_indications: ["HIV infectious disease", "leprosy", "multiple endocrine neoplasia"]
---

# Tezacaftor
{: .fs-9 }

Evidensniveau: **L5** | Forudsagte indikationer: **3** stk.
{: .fs-6 .fw-300 }

---

## Indholdsfortegnelse
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Farmaceutens vurderingsrapport

</div>

## Tezacaftor: Fra cystisk fibrose til HIV-infektion
{: .text-alpha }

## Resumé

Tezacaftor er en CFTR-korrektor, som oprindeligt anvendes til behandling af **cystisk fibrose**, og som indgår i kombinationspræparater som Symkevi, Kaftrio og Alyftrek. TxGNN-modellen forudsiger, at stoffet kan have effekt mod **HIV-infektion**, men der er **0 kliniske forsøg** og **0 publikationer**, der understøtter denne forudsigelse. Forudsigelsen er udelukkende beregningsbaseret.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Cystisk fibrose (de danske godkendelser indeholder ingen indikationstekst) |
| Forudsagt ny indikation | HIV-infektion |
| TxGNN-forudsigelsesscore | 0,9924 |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført (gyldige tilladelser: 8 af 8) |
| Antal markedsføringstilladelser | 8 (gyldige: 8) |
| Anbefalet beslutning | Hold |

---

## Hvorfor er denne forudsigelse rimelig?

Detaljerede data om virkningsmekanismen er ikke tilgængelige i de data, der er indsamlet til denne rapport. Tezacaftor er kendt som en CFTR-korrektor, der forbedrer foldning og transport af det muterede F508del-CFTR-protein til cellemembranen. Stoffet bruges i kombination med andre CFTR-modulatorer til patienter med cystisk fibrose med specifikke genmutationer.

Der er ikke påvist nogen mekanistisk forbindelse mellem CFTR-korrektion og HIV-infektion. Der er ingen dokumenteret antiviral aktivitet mod HIV, og der er hverken kliniske forsøg eller litteratur, der kan danne grundlag for en hypotese. Den høje score (rang 8340) stammer fra TxGNN-modellen (deep learning) og kan afspejle ligheder, som modellen har lært mellem beslægtede sygdomme, ikke biologisk evidens, og bør ikke tolkes som klinisk evidens.

Modellen har også forudsagt to andre indikationer med samme manglende evidensgrundlag: **spedalskhed** (score 0,9914) og **multipel endokrin neoplasi** (score 0,9906). Heller ikke for disse er der understøttende forsøg, litteratur eller en dokumenteret mekanistisk forbindelse.

---

## Denmark-markedsinformation

| Tilladelsesnummer | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28105993917 | Symkevi | Filmovertrukne tabletter | Indikationstekst ikke tilgængelig |
| 28106594021 | Kaftrio | Filmovertrukne tabletter | Indikationstekst ikke tilgængelig |
| 28107176424 | Alyftrek | Filmovertrukne tabletter | Indikationstekst ikke tilgængelig |

Alle tre tilladelser er gyldige og indehaves af Vertex Pharmaceuticals (Ireland) Limited. Alle er kombinationspræparater, og alle er til oral anvendelse.

<!-- review:begin dk-lic-20261112-tezacaftor-1 -->

> **Rettelse ved gennemgang (2026-11-12)**: Oprindeligt stod der: "Alle er enkeltstofspræparater i de registrerede data" Ifølge Lægemiddelstyrelsens liste over godkendte lægemidler (data fra 2026-11-05, feltet AktiveSubstanser): Symkevi, Kaftrio og Alyftrek indeholder flere aktive stoffer. Kilde: [Lægemiddelstyrelsen: liste over godkendte lægemidler](https://laegemiddelstyrelsen.dk/en/sideeffects/find-medicines/lists-with-information-about-medicines/).

<!-- review:end dk-lic-20261112-tezacaftor-1 -->

---

## Sikkerhedsovervejelser

Der er ikke tilgængelige data om advarsler og kontraindikationer i de data, der er indsamlet til denne rapport. Den eneste registrerede interaktion er farmakologisk: tezacaftors målprotein er CFTR, og der er ikke identificeret interaktioner med andre lægemidler.

Se det godkendte produktresumé (SmPC) for sikkerhedsoplysninger.

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelsen om HIV-infektion er alene baseret på en beregningsmodel uden kliniske forsøg, litteratur eller en plausibel mekanistisk forbindelse (evidensniveau L5). Data om sikkerhed er desuden mangelfulde.

**For at komme videre kræves følgende:**
- Detaljerede data om virkningsmekanismen (MOA), f.eks. fra DrugBank
- Præklinisk dokumentation (f.eks. in vitro-studier af antiviral aktivitet mod HIV) som minimum for at hæve evidensniveauet til L4
- Hentning og gennemgang af produktresuméer fra Lægemiddelstyrelsen med advarsler og kontraindikationer, før der kan foretages en sikkerhedsscreening
- Systematisk litteratursøgning og søgning i forsøgsregistre efter eventuelle relevante data
- Vurdering af, om de to øvrige forudsagte indikationer (spedalskhed og multipel endokrin neoplasi) bør prioriteres, hvis der fremkommer evidens

<!-- review:begin log -->

## Gennemgangslog

Nedenfor er gennemgangsloggen for denne side: udsagn kontrolleret mod Lægemiddelstyrelsens liste over godkendte lægemidler. Rettelser er begrænset til grundlæggende faktuelle udsagn; modelforudsigelser, evidensniveauer og konklusioner er ikke omskrevet.

| Gennemgået | Punkt | Handling | Kilde |
|------|------|------|------|
| 2026-11-12 | Enkeltstof/kombination rettet | Rettet | [Lægemiddelstyrelsen: liste over godkendte lægemidler](https://laegemiddelstyrelsen.dk/en/sideeffects/find-medicines/lists-with-information-about-medicines/) |

<!-- review:end log -->

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

