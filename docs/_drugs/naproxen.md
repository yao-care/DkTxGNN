---
layout: default
title: Naproxen
parent: Kun modelforudsigelse (L5)
nav_order: 304
evidence_level: L5
indication_count: 8
---

# Naproxen
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

# Naproxen: Fra smertelindring og inflammationskontrol til brachydaktyli-syndaktyli-syndrom

## Resumé på én sætning

Naproxen er et velkendt non-steroid antiinflammatorisk lægemiddel (NSAID), der er meget brugt til smertelindring, feber og inflammatoriske tilstande såsom arthritis og dysmenorrhoe.
TxGNN-modellen forudsiger, at det kan være effektivt mod **brachydaktyli-syndaktyli-syndrom**, en sjælden medfødt skeletal-malformationssygdom.
Der er imidlertid **ingen kliniske forsøg og ingen publiceret litteratur**, der i øjeblikket understøtter denne indikation, og det mekanistiske link anses for biologisk svagt — denne forudsigelse er højst sandsynligt en artefakt fra knowledge graph.

---

## Hurtigt overblik

| Punkt | Indhold |
|-------|---------|
| Original indikation | Smerte, feber og inflammation (velkendt NSAID; ingen danske regulatoriske data tilgængelige i denne datapakke) |
| Forudsagt ny indikation | Brachydaktyli-syndaktyli-syndrom |
| TxGNN-forudsigelsesscore | 99.35% |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Ikke på markedet (ifølge aktuelle data; ingen markedsføringstilladelser registreret) |
| Antal markedsføringstilladelser | 0 |
| Anbefalet beslutning | Vent |

---

## Hvorfor er denne forudsigelse rimelig?

Naproxen er en propionsyreafledning NSAID, hvis primære mekanisme er hæmning af cyclooxygenase-enzymer (COX-1 og COX-2), hvilket reducerer prostaglandinsyntes. Dette danner det farmakologiske grundlag for dets antiinflammatoriske, analgetiske og antipyretiske effekter. Detaljerede data om virkningsmekanisme var ikke tilgængelige i den aktuelle datapakke; ovenstående er baseret på velkendt farmakologisk viden.

Brachydaktyli-syndaktyli-syndrom er en sjælden, genetisk betinget medfødt malformation karakteriseret ved unormalt korte fingre (brachydaktyli) og sammenvoksede fingre (syndaktyli). Disse er faste strukturelle defekter etableret under fosterudviklingen — fundamentalt forskellige fra de erhvervede inflammatoriske processer, som Naproxen retter sig imod. Der er ingen anerkendt klinisk begrundelse for, at COX-hæmning skal kunne korrigere eller afhjælpe allerede eksisterende skeletal-strukturelle anomalier.

Den spekulative mekanistiske vej, som modellen foreslår — COX-2-hæmning → reduceret PGE2 → forstyrret knogleremodelleringssignalering → indirekte vekselvirkning med BMP/GDF-udviklingsveje — er ikke understøttet af klinisk eller præklinikal evidens for dette specifikke syndrom. Den høje TxGNN-forudsigelsesscore afspejler næsten sikkert en **knowledge graph-falsk positiv**: både Naproxen og skeletale dysplasier deler "skeletal"-kategorinoder i den underliggende graf, hvilket skaber en falsk strukturel forbindelse. Denne forudsigelse bør tolkes med betydelig skepsis.

---

## Bevis fra kliniske forsøg

I øjeblikket ingen relaterede kliniske forsøg registreret.

---

## Bevis fra litteratur

I øjeblikket ingen relateret litteratur tilgængelig.

---

## Sikkerhedshensyn

Se godkendt produktinformation (SmPC) for sikkerhedsinformation.

---

## Konklusion og næste skridt

**Beslutning: Vent**

**Begrundelse:**
Trods en tilsyneladende høj TxGNN-forudsigelsesscore (99.35%) har denne kandidat ingen understøttende evidens fra kliniske forsøg eller litteratur (Evidensniveau L5), og det foreslåede mekanistiske link mellem COX-hæmning og en genetisk betinget medfødt skeletal-strukturel defekt er biologisk usandsynligt. Forudsigelsen afspejler højst sandsynligt en strukturel bias i knowledge graph snarere end en genuin terapeutisk mulighed.

**For at fortsætte er følgende nødvendigt:**
- **Biologisk plausibilitetsvurdering:** Uafhængig ekspertvurdering af, hvorvidt COX/prostaglandin-hæmning kunne have nogen meningsfuld terapeutisk effekt på en genetisk betinget medfødt skeletal-malformation
- **Knowledge graph-revision:** Undersøgelse af, hvorvidt delte "skeletal"-kategorinoder i TxGNN-grafen genererer systematiske falske positiver for Naproxen på tværs af sjældne skeletal-/udviklingssyndrom (bemærk: rang 3–8 i denne pakke er alle sjældne skeletal-/udviklingssyndrom, hvilket tyder på et mønster)
- **MOA-datahentning:** Indhentelse af fuld farmakologisk profil fra DrugBank (DB00788) for at understøtte eller afvise enhver mekanistisk hypotese
- **Sikkerhedsdatahentning:** Download og parsering af SmPC fra Lægemiddelstyrelsen for at fuldende sikkerhedsprofilen, herunder advarsler, kontraindikationer og lægemiddelinteraktioner
- **Verificering af danske regulatoriske data:** Bekræftelse af aktuelle markedsføringstilladelsesstatuser for naproxen-holdige produkter hos Lægemiddelstyrelsen; fraværet af tilladelsesposter i denne datapakke afspejler sandsynligvis et datahul, da naproxen er et langvarigt etableret NSAID

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

