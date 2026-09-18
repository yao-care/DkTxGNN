---
layout: default
title: Melatonin
parent: Kun modelforudsigelse (L5)
nav_order: 281
evidence_level: L5
indication_count: 0
---

# Melatonin
{: .fs-9 }

Evidensniveau: **L5** | Forudsagte indikationer: **0** stk.
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

# Melatonin: Evaluering af medicingenforbrug — Ingen TxGNN-forudsigelsesdata tilgængelige

---

## Sammenfatning i en sætning

Melatonin (DB01065) er et endogent neurohormom, der primært er forbundet med regulering af circadiske rytmer og søvn-vågen-cyclus. Den aktuelle Evidenspakke indeholder **ingen TxGNN-forudsagte indikationer** og har to uløste datakløfter — hvoraf den ene er klassificeret som Blocking — hvilket betyder, at en formel evalueringen af medicingenforbrug ikke kan gennemføres på nuværende tidspunkt. Denne rapport dokumenterer den aktuelle status for beviser og skitserer de trin, der er nødvendige før nogen beslutning om medicingenforbrug kan træffes.

---

## Hurtig oversigt

| Emne | Indhold |
|------|---------|
| Oprindelig indikation | Ikke specificeret i Evidenspakke |
| Forudsagt ny indikation | Ingen forudsigelser tilgængelige |
| TxGNN-forudsigelsesscore | N/A |
| Bevisniveau | N/A — pipeline har ikke produceret output |
| Danmark markedsstatus | Ikke markedsført |
| Antal markedsføringstilladelser | 0 |
| Anbefalet beslutning | **Vent** |

---

## Hvorfor er denne forudsigelse fornuftig?

Der er ikke genereret nogen TxGNN-forudsigelse for dette lægemiddel i den aktuelle Evidenspakke, så ingen mekanistisk begrundelse for en ny indikation kan formelt præsenteres.

For almen kontekst: Melatonin (N-acetyl-5-methoxytryptamin) er et endogent hormon, der primært syntetiseres af epifysen. Baseret på offentligt tilgængelig farmakologisk viden virker det på G-proteinkoblede melatoninreceptorer MT1 og MT2 og medierer tilpasning af circadiske rytmer og søvn-vågen-overgange. Det anerkendes også for at have antioxidative egenskaber. Evidenspakken markerer mekanismen dog som en **datakløft med høj alvorlighed** (DG002), hvilket betyder, at formel MOA-dokumentation endnu ikke er hentet fra DrugBank.

Indtil TxGNN-pipeline køres igen og producerer kandidatindikationer, vil denne sektion forblive ufuldstændig.

---

## Klinisk forsøgsbevis

Der er ikke genereret nogen TxGNN-forudsigelse for dette lægemiddel. Der er ikke præsenteret sygdomsspecifikke kliniske forsøgsbevis i denne Evidenspakke.

> I øjeblikket ingen relaterede kliniske forsøg registreret i Evidenspakke.

---

## Litteraturbevis

Der er ikke genereret nogen TxGNN-forudsigelse for dette lægemiddel. Der er ikke præsenteret sygdomsspecifikke litteraturbevis i denne Evidenspakke.

> I øjeblikket ingen relateret litteratur tilgængelig i Evidenspakke.

---

## Danmarks markedsinformation

Melatonin er ikke registreret som markedsført i Danmark inden for denne Evidenspakke. Der er ingen markedsføringstilladelser fra Det Danske Lægemiddelstyrelse på fil.

| Emne | Detalje |
|------|---------|
| Markedsstatus | Ikke markedsført i Danmark (ifølge Evidenspakke) |
| Samlede tilladelser | 0 |

> **Bemærkning for anmeldere:** Melatonin er godkendt i Den Europæiske Union under mærkenavnet **Circadin® 2 mg depoteret tablet** (EMA centraliseret procedure) til korttidsbehandling af primær søvnløshed hos patienter på 55 år og derover. Denne godkendelse fremgår ikke af den aktuelle Evidenspakke, hvilket kan indikere en dataindsamlingskløft snarere end en sand fravær af godkendelse. Verifikation mod Det Danske Lægemiddelstyrelses produktdatabase anbefales, før man konkluderer, at melatonin er helt uregistreret i Danmark.

---

## Sikkerhedsovervejelser

Alle sikkerhedsfelter i denne Evidenspakke er markeret som datakløfter og kan ikke rapporteres.

> Se venligst den godkendt produktinformations-sammenfattelse (SmPC) — for eksempel den EMA-godkendt Circadin SmPC — for aktuelle sikkerhedsoplysninger, herunder advarsler, kontraindikationer og lægemiddelinteraktioner.

**Udestående datakløfter, der forhindrer sikkerhedsvurdering:**

| Datakløft-ID | Manglende emne | Alvorlighed | Indflydelse | Foreslået afhjælpning |
|--------|---------------|-----------|-----------|----------------------|
| DG001 | Regulatoriske advarsler og kontraindikationer | **Blokerend** | Kan ikke gennemføre sikkerhedsforscreening (S1 gate) | Download og parse SmPC PDF fra Det Danske Lægemiddelstyrelse eller EMA-websted |
| DG002 | Mekanisme for virkning (MOA) | Høj | Mekanistisk linkanalyse kan ikke udføres | Forespørg DrugBank API for DB01065 |

---

## Konklusion og næste trin

**Beslutning: Vent**

**Begrundelse:**
TxGNN-pipeline har ikke produceret nogen forudsagte indikationer for melatonin i denne Evidenspakke-version (v4, datasnit 2026-04-04), og en Blocking datakløft (DG001 — manglende regulatoriske advarsler og kontraindikationer) forhindrer selv foreløbig sikkerhedsscreening. Ingen evalueringen af medicingenforbrug kan fortsætte, før disse problemer løses.

**For at fortsætte, følgende er nødvendig:**

- **[Blokerend]** Løs DG001: Hent aktuelle SmPC advarsler og kontraindikationer fra Det Danske Lægemiddelstyrelse eller EMA produktdatabasen
- **[Høj]** Løs DG002: Forespørg DrugBank API for DB01065 for at få formel MOA-dokumentation
- **Kør TxGNN-pipeline igen** efter datakløfter er løst for at generere kandidatindikationer
- **Verificer Danmarks registreringsstatus**: Dobbelttjek, om Circadin® eller nogen melatoninprodukt i øjeblikket har en national eller centraliseret godkendelse, der er gyldig i Danmark, da 0-licensantal i denne Evidenspakke kan afspejle et dataindsamlingsproblem
- **Opdater Evidenspakken** til version v5, når de ovenstående trin er fuldført, og genindlæg til formel evaluering

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

