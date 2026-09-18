---
layout: default
title: Marbofloxacin
parent: Kun modelforudsigelse (L5)
nav_order: 278
evidence_level: L5
indication_count: 10
---

# Marbofloxacin
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

# Marbofloxacin: Fra bakterieinfektioner (veterinær) til interventrikulær septum aneurisme

## En-sætnings-sammenfatning

Marbofloxacin er et fluorokinolon-antibiotikum, der tilhører samme lægemiddelklasse som ciprofloxacin og levofloxacin; det er i øjeblikket godkendt udelukkende til **veterinær brug** (behandling af bakterieinfektioner hos hunde, katte og kvæg) og har ingen human markedsføringstilladelse i Danmark eller EU.

TxGNN-modellen tildeler sin højeste forudsigelsesscore til **interventrikulær septum aneurisme** (95,37%), efterfulgt af pulmonalklap-sygdom, orofaciale spalter syndrom, Laubry-Pezzi syndrom og Pierre Robin syndrom — alle strukturelle eller udviklingsbetingede tilstande.

Der er **ingen kliniske prøvebevis og ingen human litteratur** for nogen af disse forudsagte indikationer; den eneste indsamlede publikation er en veterinær reptilkasuistik, der beskriver marbofloxacins eksisterende antibakterielle brug, ikke en ny indikation.

---

## Hurtig oversigt

| Element | Indhold |
|---------|---------|
| Oprindelig indikation | Bakterieinfektioner hos dyr (kun veterinær brug; ingen godkendt human indikation) |
| Forudsagt ny indikation (Rang 1) | Interventrikulær septum aneurisme |
| TxGNN forudsigelsesscore | 95,37% |
| Bevisniveau | L5 |
| Status på det danske marked | Ikke markedsført |
| Antal markedsføringstilladelser | 0 |
| Anbefalet beslutning | **Afvent** |

---

## Hvorfor er denne forudsigelse rimelig?

Marbofloxacin er et fluorokinolon-antibiotikum af tredje generation. Som alle fluorokinoloner centrerer dets virkningsmekanisme sig omkring inhibering af bakteriel **DNA gyrase (topoisomerase II) og topoisomerase IV**, enzymer der er essentielle for bakteriel DNA-replikation og reparation. Denne antibakterielle virkningsmekanisme har ingen kendt biologisk skæringspunkt med patogenesen af hjertets strukturelle defekter.

I øjeblikket er detaljerede virkningsmekanisme-data specifikt for marbofloxacins farmakologi hos mennesker ikke tilgængelige i denne evidenspakke. Baseret på kendt information tilhører marbofloxacin fluorokinolon-klassen, dets antibakterielle effektivitet hos dyr er velkendt, og der er ingen mekanistisk begrundelse for, at topoisomerase-inhibering ville behandle — eller interagere med — hjertets strukturelle anomalier såsom interventrikulær septum aneurisme, som opstår fra embryonale udviklingsfejl eller postinfarktuel myokardiel remodellering.

De høje TxGNN-scores på tværs af alle topplacerede forudsigelser skyldes mest sandsynligt **ikke-specifik samtidig forekomst af "hjertesygdoms"-knuder inden for vidensgrafens**, snarere end sande årsags- eller mekanistiske forhold. Dette er en kendt begrænsning af grafbaserede forudsigelsesmodeller, når lægemiddel-knuder er sparsomt forbundne: delt naboskab forstørrer forudsagte scores uden at afspejle ægte farmakologisk plausibilitet. Alle fem forudsagte indikationer (hjertets strukturelle defekter og kranio-ansigtsudviklingssyndrome) er mekanistisk uoverensstemmende med et antibakterielt middel; en forudsigelse (orofaciale spalter) bærer den yderligere bekymring, at fluorokinoloner vides at være potentielt skadelige for udviklings-brusk under graviditet.

---

## Klinisk prøvebeviser

I øjeblikket ingen relaterede kliniske prøver registreret for nogen af de forudsagte indikationer.

---

## Litteraturbevis

| PMID | År | Type | Tidsskrift | Vigtigste resultater |
|------|-----|------|----------|----------------------|
| [25831585](https://pubmed.ncbi.nlm.nih.gov/25831585/) | 2015 | Veterinær kasuistik | *Journal of Zoo and Wildlife Medicine* | Argentinsk boa med bakteriel endokarditis (Ochrobactrum intermedium, Pseudomonas putida) og incidentel pulmonalklap-forandringer; marbofloxacin anvendt som **antibakteriell** agens — dette er en beskrivelse af lægemidlets oprindelige antibakterielle indikation hos et krybdyr, ikke bevis for ændret brug hos mennesker |

> **Bemærkning:** Denne eneste publikation udgør ikke bevis for nogen ny human indikation. Den beskriver marbofloxacins etablerede veterinære antibakterielle brug. Den bør ikke fortolkes som understøttelse af forudsigelsen om pulmonalklap-sygdom.

---

## Oplysninger om det danske marked

Marbofloxacin har **ingen markedsføringstilladelse** i Danmark (Lægemiddelstyrelsen) og har ingen centraliseret EMA-godkendelse til human brug. Det er registreret som et **veterinært lægemiddel** i EU under Det Europæiske Lægemiddelagenturs rammeværk for veterinære lægemidler.

Der er derfor ingen human-produkttilladelser at opregne.

---

## Sikkerhedshensyn

Detaljerede human sikkerhedsdata (advarsler, kontraindikationer, lægemiddelinteraktioner) er ikke tilgængelige i denne evidenspakke, da marbofloxacin ikke har nogen godkendt human indikation.

**Klasse-niveau-overvejelser, der gælder for alle fluorokinoloner** (baseret på etableret farmakologisk klasseviden):

- **Seneskader**: Fluorokinoloner er forbundet med tendinopati og seneruptur, især hos ældre patienter og dem på kortikosteroider. EMA har udstedt klasse-niveau-advarsler for human fluorokinoloner.
- **QT-forlængelse**: Klasse-niveau-kardial risiko; risiko for torsades de pointes, især i kombination med andre QT-forlængende midler.
- **Bruskskader og skeletal udvikling**: Kontraindikeret under graviditet og hos voksende børn for human fluorokinoloner; dyrestudier bekræfter ledbruskskader.
- **CNS-effekter**: Kramper, forvirring og perifer neuropati er klasse-niveau-bivirkninger.
- **Fotosensitivitet**.

Disse klasse-niveau-risici er især relevante her, fordi **de topforudsagte indikationer omfatter udviklingssyndrome (orofaciale spalter, Pierre Robin syndrom), hvor patienter kan omfatte gravide kvinder og nyfødte** — populationer med højest risiko for fluorokinolon-toksicitet.

For enhver human brugsvurdering skulle en fuldstændig human sikkerhedsvurdering (svarende til et Produktresumé) foretages fra første principper.

---

## Konklusion og næste trin

**Beslutning: Afvent**

**Begrundelse:**
Alle ti topplacerede TxGNN-forudsigelser for marbofloxacin er hjertets strukturelle defekter eller kranio-ansigtsudviklingssyndrome, ingen af hvilke har nogen etableret biologisk forbindelse til lægemidlets antibakterielle virkningsmekanisme. Bevisgrundlaget er ensartet på niveau L5 (kun modelforudsigelse), med nul kliniske prøver og nul relevant human litteratur på tværs af alle forudsagte indikationer. Desuden er marbofloxacin ikke godkendt til human brug i Danmark eller hvor som helst i EU, hvilket betyder, at den regulatoriske og kliniske udviklingsvej skulle begynde fra fase 0.

**For at fortsætte ville følgende være påkrævet minimum:**

- **Mekanistisk gen-evaluering**: Uafhængig biologisk vejanalyse for at identificere, om nogen plausibel mekanisme — ud over den antibakterielle handling — kunne forbinde marbofloxacin til nogen kardial eller udviklingsbetinget tilstand; nuværende evidens antyder stærkt, at dette er en vidensgraf-artefakt.
- **Human sikkerhedsdata**: Et komplet human farmakokinetisk, toksikologisk og sikkerhedsdossier ville være påkrævet før enhver klinisk undersøgelse; marbofloxacin har aldrig undergået formel human klinisk udvikling.
- **Regulatorisk præ-konsultation**: I betragtning af at dette er en veterinær-kun forbindelse, ville et møde før indsendelse med EMA eller Lægemiddelstyrelsen være nødvendigt for at bestemme gennemførligheden af et human udviklingsprogram.
- **TxGNN-model-revision**: Mønsteret af høje scores, der klumper sig omkring urelaterede strukturelle/udviklingsbetingede sygdomme, berettiger en gennemgang af vidensgraf-naboskabet for marbofloxacin-knuden for at udelukke systematiske grafarter, før yderligere ressourcer investeres.
- **Alternativ indikationshypotese-generering**: Hvis ændret brug af marbofloxacin er en prioritet, ville en infektionsrelateret indikation i human medicin (f.eks. resistente gram-negative infektioner, erhvervserhvervede luftvejsinfektioner) være mekanistisk langt mere forsvarlig og bør evalueres som en primær hypotese.

---

> ⚠️ **Ansvarsfraskrivelse**: Denne rapport er genereret til forskningsformål alene og udgør ikke medicinsk rådgivning. Ændret brug af lægemidler kræver klinisk validering før nogen terapeudisk anvendelse. Alt indhold bør gennemgås af kvalificerede sundhedsfaglige personer, før det informerer nogen klinisk eller regulatorisk beslutning.

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

