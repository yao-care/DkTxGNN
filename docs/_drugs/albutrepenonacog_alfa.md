---
layout: default
title: Albutrepenonacog Alfa
parent: Kun modelforudsigelse (L5)
nav_order: 20
evidence_level: L5
indication_count: 10
---

# Albutrepenonacog Alfa
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

# Albutrepenonacog Alfa: Fra Hæmofili B til Pseudo-von Willebrand-sygdom

## Resumé i én sætning

Albutrepenonacog alfa (Idelvion®) er et rekombinant Faktor IX-albumin-fusionsprotein, der oprindeligt blev udviklet til profylakse og behandling af blødninger i Hæmofili B (medfødt Faktor IX-mangel).
TxGNN-modellen forudsiger, at det kan være effektivt for **Pseudo-von Willebrand-sygdom (blodpladetype VWD)** med en forudsigelsesscore på **99,94%**; dog **er der i øjeblikket ingen kliniske forsøg og ingen offentliggjort litteratur**, der understøtter denne retning, og mekanistisk analyse indikerer en fundamental uoverensstemmelse mellem lægemidlets virkningsmekanisme og patofysiologien for den forudsagte indikation.

---

## Hurtig oversigt

| Element | Indhold |
|---------|---------|
| Original indikation | Hæmofili B — profylakse og behandling af blødningstilfælde på grund af medfødt Faktor IX-mangel |
| Forudsagt ny indikation | Pseudo-von Willebrand-sygdom (blodpladetype VWD) |
| TxGNN-forudsigelsesscore | 99,94% |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Ikke markedsført |
| Antal markedsføringstilladelser | 0 |
| Anbefalet beslutning | Afvent |

---

## Hvorfor er denne forudsigelse rimelig?

Albutrepenonacog alfa er et rekombinant humant koagulationsfaktor IX (FIX) fusioneret med humant albumin (rFIX-FP). Albuminsfusionen forlænger væsentligt plasmaets halveringstid for FIX sammenlignet med standard Faktor IX-koncentrater. Dets farmakologiske virkning ligger helt inden for den **indre koagulationsvej**: når det først er aktiveret til FIXa, sammensætter det det indre tenase-kompleks (FIXa–FVIIIa) på phospholipid-membranflader, driver Faktor Xa-generering, trombindannelse og i sidste ende fibrinkoagel-stabilisering. Denne mekanisme er specifik for korrektion af den sekundære hemostase-defekt, der findes i Hæmofili B.

Pseudo-von Willebrand-sygdom (også kendt som blodpladetype VWD eller GP1BA-relateret VWD) repræsenterer en fuldstændig anden patofysiologi. Det er forårsaget af en funktionsøgende mutation i blodpladeglykoproteinet **GPIbα**, som resulterer i spontan, abnorm binding af GPIbα til von Willebrand-faktor (vWF). Dette udtømmer cirkulerende vWF-multimerer og blodplader, hvilket forringer primær hemostase. Den etablerede behandling er **blodpladeltransfusion** (for at levere normal GPIbα), ikke koagulationsfaktorerstatning. Faktor IX-supplement spiller ingen rolle i at genskabe vWF-niveauer, normalisere blodpladetal eller korrigere GPIbα-receptorfunktion.

TxGNN-modellens høje forudsigelsesscore afspejler højst sandsynligt **topologisk lighed inden for det underliggende vidensnetværk** — både Hæmofili B og pseudo-von Willebrand-sygdom deler "blødningsforstyrelse" og "koagulationsforstyrelse"-noder — snarere end nogen ægte mekanistisk eller terapeutisk forbindelse. Denne sag illustrerer en anerkendt begrænsning af grafordede forudsigelsesmodeller: fænotypisk klyngning kan øge forudsigelsesscore uden at fange sygdomsspecifik molekylær patofysiologi. Forudsigelsen bør tolkes med betydelig forsigtighed.

---

## Beviser fra kliniske forsøg

Der er i øjeblikket ingen relaterede kliniske forsøg registreret.

*Systematiske søgninger i ClinicalTrials.gov og WHO ICTRP udført den 26. marts 2026 gav ingen resultater for albutrepenonacog alfa i pseudo-von Willebrand-sygdom.*

---

## Litteraturbeviser

Der er i øjeblikket ingen relateret litteratur tilgængelig.

*PubMed-søgninger udført den 26. marts 2026 gav ingen publikationer, der knytter albutrepenonacog alfa til pseudo-von Willebrand-sygdom.*

---

## Sikkerhedsovervejelser

Se venligst det godkendte produktresumé (SmPC) for sikkerhedsinformation.

---

## Konklusion og næste skridt

**Beslutning: Afvent**

**Begrundelse:**
TxGNN-forudsigelsen er drevet af vidensnetværkets topologisk nærhed inden for "blødningsforstyrelse"-fænotypeklyngen snarere end ved mekanistisk relevans; pseudo-von Willebrand-sygdom er en primær hemostase-forstyrelse, der kræver blodpladeltransfusion, og Faktor IX-erstatning har ingen teoretisk grundlag, ingen klinisk præcedens og ingen understøttende beviser i denne tilstand.

**Oversigt over alle TxGNN-forudsagte indikationer for Albutrepenonacog Alfa:**

| Rangering | Forudsagt sygdom | TxGNN-score | Mekanistisk vurdering | Beslutning |
|-----------|-----------------|------------|---------------------|-----------|
| 1 | Pseudo-von Willebrand-sygdom | 99,94% | **Uoverensstemmelse** — GPIbα funktionsøgende blodpladessygdom; FIX har ingen mekanistisk rolle | Afvent |
| 2 | Primær frisættelsesforstyrelse af blodplader | 99,94% | **Uoverensstemmelse** — Defekt i tætte/α-granula-sekretion; koagulationsfaktor-supplement har ingen grundlag | Afvent |
| 3 | Glanzmann Thrombasthenia | 99,92% | **Svag** — Bypass-terapikoncept forkert anvendt; rFVIIa (ikke FIX) er den etablerede bypass-agent for GPIIb/IIIa-mangel | Afvent |
| 4 | Scott-syndrom | 99,63% | **Delvis plausibilitet** — FIX-komplekssamling teoretisk forringet; dog eksisterer der ingen klinisk evidens, og sygdommen påvirker færre end 30 patienter globalt | Afvent |
| 5 | Blødningsdiathesis på grund af kollageneceptor-defekt | 99,28% | **Uoverensstemmelse** — Primær hemostase-defekt (GPVI/α2β1); koagulationsfaktorer kan ikke korrigere blodplade-kollagen-adhæsionssvigt | Afvent |

**For at fortsætte med nogen genvurdering ville følgende være påkrævet:**

- Detaljeret virkningsmekanisme-data og farmakodynamisk profil fra DrugBank og primærlitteratur
- Bekræftelse af dansk markedsføringstilladelsers status (bemærk: Idelvion® har EMA's centraliserede tilladelse EU/1/16/1073 for Hæmofili B; lokal tilgængelighed og refusionsstatus i Danmark bør verificeres med Laegemiddelstyrelsen separat)
- For **Scott-syndrom** specifikt — den mest mekanistisk diskutabel blandt de fem forudsigelser — ekspert-hæmatologi-holdning og en målrettet litteraturgennemmaling af FIX-aktivitet i phosphatidylserin-eksternaliseringsdefekter ville være minimumsprærequistit før eventuelle yderligere skridt
- Præklinisk eller case-report-niveau evidens, der demonstrerer FIX-aktivitet i blodplade-blødningsmodeller (i øjeblikket helt fraværende på tværs af alle fem forudsagte indikationer)

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

