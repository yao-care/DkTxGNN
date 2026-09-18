---
layout: default
title: Escitalopram
parent: Kun modelforudsigelse (L5)
nav_order: 175
evidence_level: L5
indication_count: 0
---

# Escitalopram
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

# Escitalopram: Vurdering af lægemidlet til ny brug — Utilstrækkelige data til forudsigelse

## Sammenfatning på en sætning

Escitalopram er et veletableret selektivt serotoningjenoptagelseshemmer (SSRI), der bruges bredt internationalt til behandling af major depressiv lidelse og generaliseret angstlidelse. TxGNN-modellen har **ikke genereret nogen forudsigelser om nye indikationer** for denne forbindelse, og evidenspakken indeholder **intet klinisk forsøgs- eller litteraturbevis** for nye indikationer. Denne rapport dokumenterer de aktuelle datakløfter, som skal lukkes, før en vurdering af lægemidlet til ny brug kan gennemføres.

---

## Hurtig oversigt

| Element | Indhold |
|---------|---------|
| Original indikation | Ikke registreret i denne evidenspakke (se note nedenfor) |
| Forudsagt ny indikation | **Ingen** — ingen TxGNN-forudsigelser tilgængelige |
| TxGNN forudsigelsesscore | N/A |
| Evidensniveau | **L5** (Ingen forudsigelser eller understøttende studier) |
| Status på dansk marked | Ikke markedsført (Ikke markedsført) |
| Antal markedsføringstilladelser | 0 |
| Anbefalet beslutning | **Påbegynd ikke** |

> **Note om original indikation:** Selv om evidenspakken ikke angiver oprindelige indikationer, er escitalopram internationalt anerkendt som et SSRI godkendt til behandling af major depressiv lidelse (MDD) og generaliseret angstlidelse (GAD). I EU er escitalopram godkendt gennem flere nationale markedsføringstilladelser (f.eks. Cipralex®) til depression, panikklidelse, social angstlidelse, generaliseret angstlidelse og tvangslidelse.

---

## Hvorfor er denne forudsigelse rimelig?

Ingen TxGNN-forudsigelse om ny brug er blevet genereret for escitalopram. Derfor kan en mekanistisk rationalisering for en ny indikation ikke vurderes på nuværende tidspunkt.

For øjeblikket er detaljerede data om virkningsmekanisme ikke tilgængelige i denne evidenspakke. Baseret på offentligt kendt information er escitalopram S-enantiomeren af citalopram og fungerer som et meget selektivt serotoningjenoptagelseshemmer (SSRI). Det blokerer serotoningjenoptagelsestransporteren (SERT), hvilket øger serotoninutveksling i nervesystemet. Denne mekanisme er grundlaget for dets etablerede virkning ved depressive og angstlidelser.

Fraværet af TxGNN-forudsigelser kan indikere, at escitaloprams DrugBank ID (DB01175) ikke blev succesfuldt kortlagt til vidensgrafen, eller at modellen ikke identificerede nogle nye sygdomsassociationer, der scorede over relevansgrænsen. Yderligere undersøgelse af kortlægningspipelinen anbefales.

---

## Evidens fra kliniske forsøg

For øjeblikket eksisterer der ingen forudsagte indikationer, og derfor er der ikke identificeret relaterede kliniske forsøg i en kontekst vedrørende ny brug.

---

## Litteraturbevis

For øjeblikket eksisterer der ingen forudsagte indikationer, og derfor er der ikke identificeret relateret litteratur i en kontekst vedrørende ny brug.

---

## Markedsinformation for Danmark

Ingen markedsføringstilladelser for escitalopram blev fundet i det aktuelle datasæt.

> **Note:** Dette afspejler sandsynligvis en datakløft snarere end faktisk fravær. Escitalopram er bredt tilgængeligt på tværs af EU. Cipralex® (escitalopram oxalat) er godkendt gennem nationale procedurer i Danmark via Lægemiddelstyrelsen, og generiske formuleringer er også tilgængelige. Evidenspakkens regulatoriske datamodul kan have behov for opdatering med danske eller EMA-markedsføringstilladelser.

---

## Sikkerhedshensyn

> Venligst henvises til det godkendte produktresumé (SmPC) for sikkerhedsinformation.
>
> For danske ordinerende læger er SmPC'et for Cipralex® (escitalopram) tilgængeligt via Lægemiddelstyrelsens produktdatabase eller EMA-webstedet. Vigtige sikkerhedshensyn for escitalopram omfatter generelt:
> - QT-forlængelsesrisiko (dosisafhængig)
> - Risiko for serotoninsyndrom ved kombination med andre serotoninantierne agenter
> - Selvmordsrisiko hos unge voksne (sort boks-advarsel i nogle jurisdiktioner)
> - Abstinenser ved pludselig seponering

---

## Konklusion og næste trin

**Beslutning: Påbegynd ikke**

**Begrundelse:**
Evidenspakken indeholder ingen TxGNN-forudsigelser, ingen regulatoriske data for Danmark og ingen sikkerhedsinformation. Uden en forudsagt ny indikation er der intet grundlag for at vurdere en mulighed for ny brug. Denne kandidat kan ikke avancere, indtil grundlæggende datakløfter er lukket.

**For at fortsætte er følgende nødvendig:**

1. **Løs DrugBank/vidensgrafs kortlægningsproblem** — Bekræft, at DB01175 (escitalopram) er korrekt kortlagt til TxGNN-vidensgrafen, og at forudsigelser kan genereres
2. **Udfyld danske regulatoriske data** — Importer markedsføringstilladelser fra Lægemiddelstyrelsen og/eller EMA's centraliserede proceduredatabase (escitalopram er vidt godkendt i Danmark)
3. **Indhent mekanisme-for-virkning-data (MOA)** — Forespørg DrugBank API'et for komplet farmakologisk profil (DG002)
4. **Indhent SmPC-sikkerhedsdata** — Uddrag advarsler, kontraindikationer og lægemiddelinteraktioner fra det danske godkendte SmPC (DG001)
5. **Kør TxGNN-forudsigelsespipelinen igen** når ovenstående datakløfter er udfyldt, og regenerer evidenspakken

---

*Denne rapport er til forskningsformål og udgør ikke medicinsk rådgivning. Alle lægemiddelkandidater til ny brug kræver klinisk validering før anvendelse.*

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

