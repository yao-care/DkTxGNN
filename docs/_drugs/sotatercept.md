---
layout: default
title: Sotatercept
parent: Kun modelforudsigelse (L5)
nav_order: 771
evidence_level: L5
indication_count: 10
monitor_inn: "Sotatercept"
predicted_indications: ["acute lymphoblastic leukemia (disease)", "severe nonproliferative diabetic retinopathy", "diabetic retinopathy", "drug-induced osteoporosis", "diabetic cataract", "HER2 positive breast carcinoma", "transitional cell carcinoma", "prostatic urethra urothelial carcinoma", "kidney pelvis sarcomatoid transitional cell carcinoma", "infiltrating bladder urothelial carcinoma sarcomatoid variant"]
last_modified_at: 2026-10-23
description: "Sotatercept: forudsagt ny indikation Akut lymfatisk leukæmi (evidensniveau L5). Oprindelig indikation: Ikke angivet i de indsamlede data"
---

# Sotatercept
{: .fs-9 }

Evidensniveau: **L5** | Forudsagte indikationer: **10** stk.
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

## Sotatercept: Fra en ikke-angivet godkendt anvendelse til akut lymfatisk leukæmi
{: .text-alpha }

## Resumé

Sotatercept markedsføres i Danmark som Winrevair, men de data, der er indsamlet til denne rapport, indeholder ingen godkendt indikationstekst. TxGNN-modellen forudsiger, at lægemidlet kan have effekt ved **akut lymfatisk leukæmi**. Der er **ingen kliniske forsøg og ingen publikationer** i datagrundlaget, så forudsigelsen er udelukkende modelbaseret.

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Ikke angivet i de indsamlede data (indikationsteksten i licensen er tom) |
| Forudsagt ny indikation | Akut lymfatisk leukæmi |
| TxGNN-forudsigelsesscore | 0,9978 |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført (gyldige tilladelser: 1 af 1) |
| Antal markedsføringstilladelser | 1 (gyldige: 1) |
| Antal godkendelser | 1 markedsføringstilladelse |
| Anbefalet beslutning | Hold |

## Hvorfor kan forudsigelsen give mening?

Data om lægemidlets oprindelige virkningsmekanisme er ikke tilgængelige i det indsamlede materiale. Ud fra almen viden er sotatercept et fusionsprotein med aktivin-receptor type IIA, der virker som "ligandfælde" for aktivin og vækstdifferentieringsfaktorer (GDF'er) og dermed genbalancerer BMP/aktivin-signalering.

Aktivin/TGF-beta-signalering påvirker bloddannelsen, men der er ingen direkte mekanistisk eller klinisk evidens for en rolle ved akut lymfatisk leukæmi. Koblingen er derfor spekulativ, og scoren er alene et modelresultat. Da der ikke findes en kendt godkendt indikation i datagrundlaget, kan der heller ikke redegøres for sammenhængen mellem oprindelig og ny indikation.

## Klinisk evidens

Der er for øjeblikket ingen relaterede kliniske forsøg registreret.

## Litteraturevidens

Der er for øjeblikket ingen relateret litteratur tilgængelig.

## Information om det danske marked

| Markedsføringstilladelse | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28107063623 | Winrevair (Merck Sharp & Dohme B.V.) | Pulver og solvens til injektionsvæske, opløsning | Ikke angivet i de indsamlede data |

## Sikkerhedsovervejelser

Der foreligger ingen sikkerhedsdata i det indsamlede materiale. Der henvises til det godkendte produktresumé (SmPC) for sikkerhedsinformation.

## Andre forudsagte indikationer

TxGNN har også rangeret nedenstående indikationer. Ingen af dem har kliniske forsøg eller litteratur, og alle har evidensniveau L5 og anbefalingen Hold.

| Rang | Sygdom | Score | Kommentar |
|------|------|------|------|
| 2 | Svær non-proliferativ diabetisk retinopati | 0,9977 | Løs biologisk rationale i retinal karremodellering; mulige okulære sikkerhedsspørgsmål (telangiektasi, blødning) |
| 3 | Diabetisk retinopati | 0,9972 | Samme rationale som rang 2; relaterede termer er ikke uafhængig evidens |
| 4 | Lægemiddelinduceret osteoporose | 0,9965 | Aktivin hæmmer knogledannelse, og beslægtede aktivinfælder har vist knogleopbyggende effekt i dyremodeller; ingen data for sotatercept |
| 5 | Diabetisk grå stær | 0,9949 | Ingen klar mekanistisk kobling; scoren stammer fra TxGNN-modellen (deep learning) og kan afspejle ligheder, som modellen har lært mellem beslægtede sygdomme, ikke biologisk evidens |
| 6 | HER2-positiv brystkræft | 0,9943 | TGF-beta/aktivin har kontekstafhængig rolle; effekten kan være skadelig |
| 7 | Overgangscellekarcinom | 0,9939 | Ingen direkte kobling; sandsynligvis grafnærhed |
| 8 | Urothelkarcinom i prostatisk urinrør | 0,9936 | Overlapper med øvrige urothelkarcinomer |
| 9 | Sarkomatoid overgangscellekarcinom i nyrebækken | 0,9936 | Mulig EMT-relation; effekt (gavn/skade) ukendt |
| 10 | Infiltrerende blæreurothelkarcinom, sarkomatoid variant | 0,9934 | Spekulativ; overlapper med øvrige urothelkarcinomer |

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelsen for akut lymfatisk leukæmi bygger kun på en modelscore uden kliniske forsøg, litteratur eller dokumenteret mekanistisk kobling (evidensniveau L5). Sikkerhedsdata og virkningsmekanisme mangler desuden i datagrundlaget.

**For at komme videre er følgende nødvendigt:**
- Hentning af produktresuméet (SmPC) fra Lægemiddelstyrelsen med godkendt indikation, advarsler og kontraindikationer
- Data om virkningsmekanisme (MOA) fra DrugBank
- Præklinisk evidens for effekt af aktivin-ligandfangst ved akut lymfatisk leukæmi
- En systematisk søgning efter kliniske forsøg og litteratur for den forudsagte sygdom
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

