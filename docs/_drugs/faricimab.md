---
layout: default
title: Faricimab
parent: Kun modelforudsigelse (L5)
nav_order: 186
evidence_level: L5
indication_count: 0
---

# Faricimab
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

# Faricimab: Vurdering af lægemiddelomformål

## Sammenfatning i en sætning

Faricimab er et bispecifikt monoklonalt antistof (rettet mod VEGF-A og Ang-2) godkendt internationalt til neovaskulariseret aldersrelateret makuladegeneration (nAMD) og diabetisk maculaødem (DME), markedsført som Vabysmo® af Roche.
TxGNN-modellen har **ingen forudsagte nye indikationer** for dette lægemiddel i øjeblikket, og bevisgrundlaget indeholder betydelige datahiatus, der forhindrer en fuld evaluering.

---

## Hurtig oversigt

| Emne | Indhold |
|------|---------|
| Oprindelig indikation | Ikke registreret i bevisgrundlaget (internationalt godkendt til nAMD og DME) |
| Forudsagt ny indikation | **Ingen** — ingen TxGNN-forudsigelser tilgængelige |
| TxGNN-forudsigelsesscore | N/A |
| Bevisniveau | **L5** (Ingen forudsigelse eller understøttende studier i dette datasæt) |
| Markedsstatus i Danmark | **Ikke markedsført** |
| Antal markedsføringstilladelser | 0 |
| Anbefalet beslutning | **Afvent** |

> **Bemærk:** Faricimab (Vabysmo®) har en centraliseret EMA-markedsføringstilladelse (EU/1/22/1683) til nAMD og DME. Bevisgrundlagets registreringer af Danmark-specifikke licenser viser 0 poster, hvilket kan afspejle en ufuldstændig dataindportning snarere end ægte fravær fra det danske marked. Dette bør verificeres mod Laegemiddelstyrelsenss og EMA-registre.

---

## Hvorfor er denne forudsigelse rimelig?

Der eksisterer i øjeblikket **ingen TxGNN-forudsagt ny indikation** for Faricimab, så en vurdering af mekanistisk plausibilitet kan ikke udføres.

Som baggrund: Faricimab er det første bispecifikke antistof godkendt til intraokulær brug. Det hæmmer samtidigt vaskulær endotelial vækstfaktor A (VEGF-A) og angiopoietin-2 (Ang-2), to vigtige drivere af patologisk angiogenese og vaskulær ustabilitet. Ved at målrette begge veje sigter det mod at opnå større vaskulær stabilisering end anti-VEGF-monterapi alene. Dets mekanisme-af-handling-data blev markeret som et datahiatus (DG002) i dette bevisgrundlag og bør hentes fra DrugBank til enhver fremtidig evalueringsrunde.

Indtil TxGNN-vidensgrafens genererer kandidatindikationer for Faricimab, og understøttende beviser indsamles, kan der ikke etableres en mekanistisk forbindelse til en ny indikation.

---

## Klinisk forsøgsbeviser

I øjeblikket eksisterer der ingen TxGNN-forudsagt indikation for Faricimab; derfor blev der ikke udført nogen indikationsspecifik klinisk forsøgssøgning.

---

## Litteraturbeviser

I øjeblikket eksisterer der ingen TxGNN-forudsagt indikation for Faricimab; derfor blev der ikke udført nogen indikationsspecifik litteratursøgning.

---

## Markedsinformation for Danmark

Ingen markedsføringstilladelser blev registreret i bevisgrundlaget.

> **Verificering anbefalet:** Faricimab (Vabysmo®) modtog en centraliseret EMA-markedsføringstilladelse (EU/1/22/1683) i september 2022 til nAMD og DME. Dansk tilgængelighed bør bekræftes via Laegemiddelstyrelsenss medicindatabase eller EMA Union Register.

---

## Sikkerhedshensyn

Se den godkendte Sammenfatning af produktkarakteristika (SmPC) for sikkerhedsinformation.

> Bevisgrundlaget markerede følgende blokering af datahiatus:
> - **DG001 (Blokering):** Etiketadvarsler og kontraindikationer er ikke endnu tilgængelige — disse skal hentes fra SmPC før nogen fase 1-sikkerhedsvurdering kan fortsætte.
> - **DG002 (Høj):** Detaljer om handlingsmekanisme mangler — skal forespørges fra DrugBank.
>
> Ingen lægemiddel-lægemiddel-interaktioner blev identificeret i DDI-databasesøgningen (forespørgselsdato: 2026-03-26). Dette kan afspejle den intravitreale administrationsvej, som generelt resulterer i minimal systemisk eksponering.

---

## Konklusion og næste trin

**Beslutning: Afvent**

**Begrundelse:**
Der eksisterer ingen TxGNN-forudsagte nye indikationer for Faricimab, og flere kritiske datahiatus (SmPC-sikkerhedsdata, handlingsmekanisme) forbliver uløst. Der foreligger utilstrækkelig information til at evaluere en eventuel omorienterings-mulighed på dette tidspunkt.

**For at fortsætte kræves følgende:**
- **Løs DG001:** Hent den fulde SmPC (advarsler, kontraindikationer, særlige populationer) fra EMA eller Laegemiddelstyrelsen — dette er en blokerende forudsætning for fase 1-sikkerhedsvurdering
- **Løs DG002:** Forespørg DrugBank API for detaljerede oplysninger om handlingsmekanisme, farmakodynamik og målproteiner
- **Verificer markedsstatus for Danmark:** Bekræft, om den centraliserede EMA-tilladelse (EU/1/22/1683) giver dansk markedsadgang, og opdater licenseregistreringerne i overensstemmelse hermed
- **Kør TxGNN-forudsigelsespipeline igen:** Når lægemidlet er korrekt kortlagt i vidensgrafens med komplette DrugBank-data, kør KG- og DL-forudsigelsesmodellerne igen for at generere kandidatindikationer
- **Udfyld oprindelige indikationer:** Registrer de EMA-godkendte indikationer (nAMD, DME) i bevisgrundlaget for at muliggøre fremtidige mekanistiske koblingsanalyser

---

*Denne rapport er til forskningsformål og udgør ikke medicinsk rådgivning. Alle omorienterings-kandidater kræver klinisk validering før anvendelse.*

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

