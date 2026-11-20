---
layout: default
title: Cabotegravir
parent: Kun modelforudsigelse (L5)
nav_order: 145
evidence_level: L5
indication_count: 5
last_modified_at: 2026-11-06
monitor_inn: "Cabotegravir"
predicted_indications: ["rheumatoid arthritis", "sclerosing cholangitis", "bronchitis", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "severe nonproliferative diabetic retinopathy"]
description: "Cabotegravir: forudsagt ny indikation Reumatoid artritis (rheumatoid arthritis) (evidensniveau L5). I Danmark, markedsføringstilladelser: 5 (gyldige: 5)"
---

# Cabotegravir
{: .fs-9 }

Evidensniveau: **L5** | Forudsagte indikationer: **5** stk.
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

## Cabotegravir: Reumatoid artritis (rheumatoid arthritis)
{: .text-alpha }

## Opsummering i én sætning

Cabotegravir er en HIV-1-integrasehæmmer, som er markedsført i Danmark som depotinjektionsvæske (Vocabria). Den oprindelige indikationstekst er ikke tilgængelig i de data, der er indsamlet til denne rapport.
TxGNN-modellen forudsiger, at lægemidlet kan have effekt på **reumatoid artritis**, men der er **0 kliniske forsøg** og **0 publikationer**, der understøtter forudsigelsen.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Ikke registreret i de lokale data |
| Forudsagt ny indikation | Reumatoid artritis (rheumatoid arthritis) |
| TxGNN-forudsigelsesscore | 0.9945 |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført (gyldige tilladelser: 5 af 5) |
| Antal markedsføringstilladelser | 5 (gyldige: 5) |
| Anbefalet beslutning | Hold |

---

## Hvorfor er denne forudsigelse (ikke) rimelig?

Ifølge afsnittene »Mechanism of Action« og »Microbiology« i den produktinformation, som den amerikanske FDA har godkendt (Prescribing Information), for Cabotegravir (uofficiel oversættelse): »Cabotegravir er et antiretroviralt lægemiddel mod HIV-1. […] Cabotegravir hæmmer HIV-integrase ved at binde sig til integrasens aktive sted og blokere strengoverførselstrinnet i integrationen af retroviral deoxyribonukleinsyre (DNA), som er essentielt for HIV's replikationscyklus. Den gennemsnitlige 50 % hæmmende koncentration (IC 50 ) for cabotegravir i et strengoverførselsassay med oprenset rekombinant HIV-1-integrase var 3,0 nM.« Engelsk originaltekst: "Cabotegravir is an HIV-1 antiretroviral drug. […] Cabotegravir inhibits HIV integrase by binding to the integrase active site and blocking the strand transfer step of retroviral deoxyribonucleic acid (DNA) integration that is essential for the HIV replication cycle. The mean 50% inhibitory concentration (IC 50 ) value of cabotegravir in a strand transfer assay using purified recombinant HIV-1 integrase was 3.0 nM." ([DailyMed: Vocabria (cabotegravir sodium) prescribing information, ViiV Healthcare Company](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=66d450fb-cca4-476c-b0c7-c0730e3e4cf3), version af 2025-04-11; hentet 2026-11-19). Ud fra almen viden er cabotegravir en integrase-strengoverførselshæmmer (INSTI), der blokerer HIV-1-integrase, et viralt enzym uden kendt humant homolog.

Der er ikke påvist nogen mekanistisk sammenhæng mellem denne virkning og reumatoid artritis. Cabotegravir har ingen kendt immunmodulerende aktivitet i de centrale sygdomsveje (TNF, IL-6, JAK/STAT, B-celle- eller T-cellesignalering). Den høje score kommer fra TxGNN-modellen (deep learning) og kan afspejle ligheder, som modellen har lært mellem beslægtede sygdomme, ikke biologisk evidens.

Bemærk, at forudsigelsen optræder to gange i de modtagne data, hvilket tyder på en fejl i databehandlingen.

**Øvrige forudsigelser med samme evidensniveau (L5, Hold):** Modellen foreslår også skleroserende kolangitis (0.9922), bronkitis (0.9919), colobomatøs mikroftalmi-rhizomelisk dysplasi-syndrom (0.9916) og svær ikke-proliferativ diabetisk retinopati (0.9903). Ingen af dem har kliniske forsøg, litteratur eller en plausibel mekanisme.

---

## Klinisk forsøgsevidens

Der er i øjeblikket ingen relaterede kliniske forsøg registreret.

---

## Litteraturevidens

Der er i øjeblikket ingen relateret litteratur tilgængelig.

---

## Information om det danske marked

| Markedsføringstilladelsesnummer | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28106313319 | Vocabria (ViiV Healthcare BV) | Depotinjektionsvæske, suspension | Ikke angivet i de tilgængelige data |

---

## Sikkerhedsovervejelser

**Lægemiddelinteraktioner:** Der er identificeret 7 interaktioner af moderat grad, alle med antacida og mineralpræparater:

- Calciumcarbonat
- Aluminiumhydroxid
- Magnesiumcarbonat
- Magnesiumhydroxid
- Magnesiumoxid
- Natriumbicarbonat
- Natriumcitrat

For yderligere sikkerhedsoplysninger (advarsler og kontraindikationer) henvises til det godkendte produktresumé (SmPC).

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelsen bygger udelukkende på en modelscore uden kliniske forsøg, litteratur eller en plausibel virkningsmekanisme. Evidensniveauet er L5, og der er ingen mekanistisk forbindelse mellem HIV-integrasehæmning og reumatoid artritis.

**For at komme videre kræves følgende:**
- Data om virkningsmekanisme (MOA) og en eventuel mekanistisk hypotese for reumatoid artritis
- Prækliniske data, der kan understøtte en immunmodulerende effekt
- Oplysninger om godkendt indikation, advarsler og kontraindikationer fra produktresuméet
- Kontrol og oprydning af dublerede forudsigelser i datagrundlaget
- Vurdering af administrationsvej og formulering, hvis forudsigelsen skal forfølges

<!-- review:begin log -->

## Gennemgangslog

Nedenfor er gennemgangsloggen for denne side. Sætningen om, at data om virkningsmekanismen ikke var tilgængelige, er erstattet med et uddrag fra den angivne officielle produktinformation (med uofficiel oversættelse); modelforudsigelser, evidensniveauer og konklusioner er ikke omskrevet.

| Gennemgået | Punkt | Handling | Kilde |
|------|------|------|------|
| 2026-11-19 | Sætningen »data om virkningsmekanismen er ikke tilgængelige« erstattet med uddrag fra den amerikanske produktinformation | Sætning om manglende data om virkningsmekanismen erstattet med et uddrag med kilde | [DailyMed: Vocabria (cabotegravir sodium) prescribing information, ViiV Healthcare Company](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=66d450fb-cca4-476c-b0c7-c0730e3e4cf3) |

<!-- review:end log -->

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

