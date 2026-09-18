---
layout: default
title: Glucarpidase
parent: Kun modelforudsigelse (L5)
nav_order: 210
evidence_level: L5
indication_count: 10
---

# Glucarpidase
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

## Glucarpidase: Fra metotrexattoksicitetsredning til diabetisk katarakt

## Ét-sætningsresumé

Glucarpidase er et carboxypeptidase-enzym, der bruges som redningsstof ved akut metotrexat (MTX)-overdosis, og virker ved hurtigt at hydrolyse cirkulerende MTX til inaktive metabolitter.
TxGNN-modellen forudsiger, at det kan være effektivt til **Diabetisk katarakt**,
dog **ingen kliniske forsøg og ingen publikationer** understøtter på nuværende tidspunkt denne retning – forudsigelsen er udelukkende baseret på vidensgrafs-inferens.

---

## Hurtig oversigt

| Emne | Indhold |
|------|---------|
| Oprindelig indikation | Metotrexat-overdosis / redning fra toksiske MTX-plasma-niveauer |
| Forudsagt ny indikation | Diabetisk katarakt |
| TxGNN-forudsigelsesscore | 99.85% |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Ikke markedsført |
| Antal markedsføringstilladelser | 0 |
| Anbefalet beslutning | Tilbageholde |

---

## Hvorfor er denne forudsigelse rimelig?

Glucarpidase (også kendt som carboxypeptidase G2) er et rekombinant bakterielt enzym, der spalter glutamathalen af metotrexat og dets giftige polyglutamat-metabolitter, hvilket hurtigt reducerer plasma-MTX-niveauer. Det er godkendt som en nødredningsterapi hos patienter med forsinket MTX-clearance på grund af nyresvigt, hvor toksiske MTX-niveauer medfører risiko for alvorlig myelosuppression, mucositis og organskade.

Det foreslåede link til diabetisk katarakt er mekanistisk indirekte. Diabetisk katarakt drives af aktivering af polyolvejen (aldose-reduktase), ophobning af advanced glycation end-produkter (AGE'er) og oxidativ stress – ingen af disse involverer MTX-metabolisme eller carboxypeptidase-aktivitet. TxGNN-modellen har sandsynligvis genereret denne høje score gennem en multi-hop-sti i vidensgrafen: **folatmetabolisme → forhøjet homocystein → vaskulær og metabolisk skade → diabetiske okulære komplikationer**. Selvom hyperhomocysteinæmi er en etableret risikofaktor for diabetisk mikroangiopati, er Glucarpidase et akut-redningsenzym, ikke et folattilskud eller et homocysteinnedsættende middel, således at denne grafsti ikke udgør en valid terapeutisk rationale.

Det er værd at bemærke, at de 10 vigtigste forudsigelser er domineret af flere katarakt-subtyper med identiske scores (0.998330), hvilket er en anerkendt klynge-artefakt i vidensgrafs-modeller – knudepunkter tilhørende samme sygdomsklynge modtager ensartede høje scores uanset lægemiddel-specifik mekanistisk relevans. Dette reducerer yderligere tilliden til den biologiske plausibilitet af forudsigelsen.

---

## Klinisk forsøgsevidence

Der er i øjeblikket ingen relaterede kliniske forsøg registreret.

---

## Litteraturevidence

Der er i øjeblikket ingen relateret litteratur til rådighed.

---

## Markedsinformation for Danmark

Glucarpidase er ikke registreret hos Lægemiddelstyrelsen og har ingen national eller centraliseret (EMA) markedsføringstilladelse i Danmark. Ingen produktliste er tilgængelig.

---

## Sikkerhedsovervejelser

Se venligst det godkendte produktresumé (SmPC) for sikkerhedsinformation.

---

## Konklusion og næste trin

**Beslutning: Tilbageholde**

**Begrundelse:**
TxGNN-forudsigelsesscore er høj (99.85%), men dette ser ud til at afspejle en vidensgrafs-klynge-artefakt snarere end en ægte farmakologisk hypotese – der er ingen mekanistisk forbindelse mellem Glucarpidase' MTX-hydrolyseaktivitet og patofysiologien af diabetisk katarakt. Med nul understøttende kliniske forsøg, nul publikationer, ingen dansk markedsføringstilladelse og ingen tilgængelige sikkerhedsdata, er der i øjeblikket intet grundlag for at avancere denne kandidat.

**For at fortsætte er følgende påkrævet:**

- Bekræftelse af en plausibel mekanistisk hypotese, der forbinder Glucarpidase (eller MTX-vejmodulering) til beskyttelse af linseepitelceller under hyperglykæmiske forhold
- Uafhængig litteraturgennemgang for at bestemme, om en forbindelse mellem folatcyklus–homocystein–linseglåhed er blevet udforsket eksperimentelt
- Fuld mekanisme-for-handling (MOA)-data fra DrugBank for at muliggøre en stringent mekanistisk analyse
- Sikkerhedsprofil og kontraindikationdata (TFDA/EMA SmPC) før enhver yderligere evaluering
- Genundersøgelse af, hvorvidt den høje forudsigelsesscore afspejler ægte signal eller vidensgrafs-klynge-støj (dedublicering og score-rekalibrering anbefalet)

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

