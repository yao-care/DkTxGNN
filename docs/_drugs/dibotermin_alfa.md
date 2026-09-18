---
layout: default
title: Dibotermin Alfa
parent: Kun modelforudsigelse (L5)
nav_order: 141
evidence_level: L5
indication_count: 10
---

# Dibotermin Alfa
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

# Dibotermin alfa: Fra knoglereparation til Esotropi

## Sammenfatning i én sætning

Dibotermin alfa er et rekombinant humant knoglemorfogenetisk protein-2 (rhBMP-2), et biologisk lægemiddel, der bruges i ortopædisk kirurgi til at stimulere knogledannelse ved spinale fusioner og knoglebrudbehandling.
TxGNN-modellen forudsiger, at det kan være effektivt mod **Esotropi** (indadvendt konvergent skeløje), med en forudsigelsesscore på **99.97%**.
Der findes imidlertid **ingen kliniske forsøg og ingen understøttende litteratur** for denne indikation, og den interne mekanistiske vurdering klassificerer denne forudsigelse som en artefakt i vidensgraftopologien uden demonstrerbar biologisk plausibilitet.

---

## Hurtigt overblik

| Element | Indhold |
|---------|---------|
| Oprindelig indikation | Knoglereparation og spinale fusioner (centralt godkendt af EMA; ikke registreret i Danmark) |
| Forudsagt ny indikation | Esotropi |
| TxGNN-forudsigelsesscore | 99.97% |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Ikke markedsført |
| Antal markedsgodkendelser | 0 |
| Anbefalet beslutning | Afvente |

---

## Hvorfor er denne forudsigelse rimelig?

Detaljerede data om virkningsmekanisme er ikke tilgængelige i det aktuelle bevisemne. Baseret på kendt farmakologi er dibotermin alfa en rekombinant form af humant knoglemorfogenetisk protein-2 (BMP-2). Det binder sig til BMP-receptorer på celleoverfladen og aktiverer den intracelluløre SMAD1/5/8-signalvej, som forpligter mesenchymale stamceller til osteogen (knogledannende) differentiering. Ved klinisk brug leveres proteinet lokalt — indlejret i en resorberbar kollagensværm — direkte på det kirurgiske område, hvor det fremskynder og øger ny knoglevækst under spinal fusion eller reparation af lange knogler.

Esotropi er en form for konvergent strabismus, hvor det ene eller begge øjne vender indad, forårsaget af ubalance i spændingen og neuromuskulær koordination af de ekstrakkulære muskler. Den underliggende patofysiologi involverer udvikling af okulomotoriske neuroner, proprioceptive feedback-løkker og akkommodativ-konvergens-reflekser — hvoraf ingen styres af BMP-2/SMAD-signalvejen. Der er ingen etableret biologisk rolle for BMP-2-signalering i ekstrakkulær muskeltonus eller den neurale kontrol af øjnenes opstilling.

Den mekanistiske vurdering, der er indlejret i bevisemnet, konkluderer eksplicit, at der er en **fuldstændig mangel på biologisk plausibilitet** for denne forudsigelse. Den meget høje TxGNN-score (0.9997) tillægges en **topologieffekt i vidensgraf**: de to enheder er tætte naboer i den underliggende netværksstruktur, men denne nærhed afspejler delt grafkonnektivitet snarere end nogen farmakologisk relation. Denne forudsigelse bør behandles som en modelartefakt snarere end som en ægte terapeutisk hypotese.

---

## Bevis fra kliniske forsøg

Der er i øjeblikket ingen relaterede kliniske forsøg registreret.

---

## Litteraturbevis

Der er i øjeblikket ingen relateret litteratur tilgængelig.

---

## Markedsinformation for Danmark

Dibotermin alfa er **ikke i øjeblikket markedsført i Danmark**. Lægemiddelstyrelsen har ikke udstedt nationale markedsgodkendelser for dette produkt, og det fremgår ikke af det danske marked. Som reference er produktet kendt internationalt under mærkenavnet **InductOS®** og har en centraliseret EMA-markedsgodkendelse for Den Europæiske Union for ortopædiske indikationer; dette betyder imidlertid ikke, at der er aktiv markedstilgængelighed i Danmark.

---

## Sikkerhedsovervejelser

Se venligst det godkendte produktresumé (SmPC) for sikkerhedsinformationer.

---

## Konklusion og næste trin

**Beslutning: Afvente**

**Begrundelse:**
Der er ingen kliniske forsøg, ingen relevant litteratur, og ingen plausibel mekanistisk forbindelse mellem dibotermin alfa og esotropi. TxGNN-modellens høje konfidensscore (99.97%) vurderes som en vidensgraftopologiartefakt, ikke som et farmakologisk signal. Der er intet grundlag for at indlede et genbrugsprogram for denne indikation.

**For at kunne fortsætte med yderligere evaluering, ville det følgende være nødvendigt:**

- En troværdig biologisk hypotese, der forbinder BMP-2/SMAD1/5/8-signalering med ekstrakkulær muskelfysiologi, udvikling af okulomotoriske neuroner eller strabismuspatagenese
- Præklinisk evidens (in vitro eller dyremodel), der demonstrerer BMP-2-aktivitet i øje- eller neuromuskulært væv relevant for øjnenes opstilling
- Hentning af det fuldstændige produktresumé (SmPC) og receptinformationer for at karakterisere lægemidlets sikkerhed, kontraindikationer og interaktionsprofil før yderligere genbrugsevaluering
- Præcisering af den/de officielt godkendte indikation(er) i de relevante jurisdiktioner, da det aktuelle bevisemne ikke indeholder bekræftede oprindelige indikationsdata

> **Ansvarsfraskrivelse:** Denne rapport er udelukkende til forskningsreference og udgør ikke medicinsk rådgivning. Kandidater til genbrugelse af lægemidler kræver klinisk validering før enhver anvendelse.

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

