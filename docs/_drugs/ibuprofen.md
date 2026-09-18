---
layout: default
title: Ibuprofen
parent: Kun modelforudsigelse (L5)
nav_order: 219
evidence_level: L5
indication_count: 10
---

# Ibuprofen
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

# Ibuprofen: Fra smerter og betændelse til akromesomelik dysplasi, Hunter-Thompson type

## Sammenfatning på én sætning

Ibuprofen er et velkendt non-steroidt antiinflammatorisk lægemiddel (NSAID), der er bredt anvendt til behandling af smerter, feber og betændelsestilstande. TxGNN-modellen forudsiger, at det kan have aktivitet ved **Acromesomelic Dysplasia, Hunter-Thompson Type** — en sjælden medfødt skeletal dysplasi forårsaget af mutationer i CDMP1/GDF5-genet. Denne prognose understøttes af **ingen kliniske forsøg og ingen offentliggjort litteratur**, og repræsenterer alene modelbaseret spekulation (evidensniveau L5).

---

## Hurtig oversigt

| Punkt | Indhold |
|-------|---------|
| Original indikation | Smerter, feber og betændelsestilstande (etableret NSAID) |
| Forudsagt ny indikation | Acromesomelic Dysplasia, Hunter-Thompson Type |
| TxGNN-prognosescore | 99.74% |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Danske regulatoriske data blev ikke hentet i denne evidenspakke |
| Antal markedsgodkendelser | Danske regulatoriske data blev ikke hentet i denne evidenspakke |
| Anbefalet afgørelse | Afvente |

---

## Hvorfor er denne prognose fornuftig?

Detaljerede data om mekanisme for lægemidlet blev ikke hentet i denne evidenspakke. Baseret på etableret farmakologi hæmmer ibuprofen cyklooxygenase-enzymer (COX-1 og COX-2), hvilket reducerer syntesen af prostaglandin E2 (PGE2). Dette danner grundlaget for dets velkarakteriserede antiinflammatoriske, analgetiske og antifebrile egenskaber på tværs af et bredt spektrum af betændelsestilstande og smertetilstande.

Acromesomelik dysplasi, Hunter-Thompson type, er en sjælden autosomalt recessiv skeletal dysplasi forårsaget af loss-of-function mutationer i CDMP1/GDF5-genet, som koder for et medlem af BMP-familien (knogleinduktive proteiner). Tilstanden er karakteriseret ved forkortelse af de midterste og distale segmenter af ekstremiteterne (acromesomelia) som opstår under embryonal skeletudvikling, uden nogen etableret betændelsesdriver for sygdomsprogression.

Det foreslåede mekanistiske link — at COX-hæmning og reduceret PGE2 indirekte kan modulere BMP/GDF-signalering og osteoblast-aktivitet — er biologisk spekulativ og ikke understøttet af eksperimentelle eller kliniske data. PGE2 deltager ganske vist i benremodellering, men dens relevans til en medfødt strukturel defekt drevet af GDF5-haploinsufficienci er ikke etableret. Den høje TxGNN-prognosescore afspejler mest sandsynligt topologisk nærhed mellem ibuprofen-knuden og sjælden knogledysplasi-knuder inden for vidensgrafen, snarere end en ægte biologisk forbindelse. Denne fortolkning er i overensstemmelse med fraværet af kliniske forsøg eller publikationer, der understøtter dette.

---

## Evidens fra kliniske forsøg

Der er i øjeblikket ingen registrerede relaterede kliniske forsøg.

---

## Litteraturbevis

Der er i øjeblikket ingen tilgængelig relateret litteratur.

---

## Markedsinformation for Danmark

Danske regulatoriske data (Lægemiddelstyrelsen) blev ikke hentet med succes i denne evidenspakke — kun DrugBank-data blev indsat. Ibuprofen (DB01050) er et længe etableret NSAID med udbredt brug på tværs af europæiske markeder, og danske godkendelser forventes at eksistere under flere mærkenavne og doseringsformer. Sundhedsfagfolk bør konsultere Lægemiddelstyrelses produktregister direkte for aktuel godkendelsestatus, godkendte indikationer og produktinformation (SmPC).

| Godkendelsesnummer | Produktnavn | Doseringsform | Godkendt indikation |
|------|---------|-------------|---------------------|
| — | Data blev ikke hentet | — | Se Lægemiddelstyrelses register |

---

## Sikkerhedsovervejelser

Se venligst produktinformationen (SmPC) for sikkerhedsinformation.

---

## Konklusion og næste trin

**Afgørelse: Afvente**

**Begrundelse:**
Alle toprangerede TxGNN-prognoser for ibuprofen kortlægges udelukkende til sjældne medfødte skeletal dysplasier (acromesomelik dysplasi, brachyolmia-amelogenesis imperfecta-syndrom, myosclerosis, brachyolmia, brachydactyly-syndactyly-syndrom) — strukturelle udviklingsfejl uden betændelsesætiologi. Ibuprofen's COX-hæmmingsmekanisme har ingen rimelig sygdomsmodificerende begrundelse for disse tilstande, og ingen kliniske forsøg eller publikationer understøtter nogen af disse prognoser.

**For at fortsætte er følgende nødvendigt:**

- **Danske regulatoriske data** skal hentes fra Lægemiddelstyrelsen for at bekræfte aktuel godkendelsestatus, godkendte indikationer og produktinformation (SmPC)
- **Data om lægemidlets virkningsmekanisme** skal hentes fra DrugBank API (DG002) for at muliggøre formel mekanistisk tilknytningsanalyse
- **TFDA SmPC-sikkerhedsdata** (DG001) skal hentes, før nogen sikkerhedsvurdering kan fortsætte
- Disse TxGNN-prognoser bør markeres til **modelkvalitetsvurdering**: klyngen af sjældne skeletal dysplasier som toprangerede kandidater for et almindeligt NSAID tyder stærkt på et vidensgrafs topologi-artefakt (topologi-klynge-artefakt) snarere end ægte omdisponeringssignal
- Hvis fremtidig undersøgelse ønskes, bør en **specialist i sjældne sygdomme eller klinisk farmakolog** vurdere biologisk plausibilitet, før eventuelle yderligere udviklingsskrin overvejes

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

