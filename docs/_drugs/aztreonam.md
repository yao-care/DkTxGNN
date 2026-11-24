---
layout: default
title: Aztreonam
parent: Kun modelforudsigelse (L5)
nav_order: 94
evidence_level: L5
indication_count: 10
monitor_inn: "aztreonam"
predicted_indications: ["hyperamylasemia", "polyclonal hyperviscosity syndrome", "congenital analbuminemia", "gonococcal urethritis", "Ureaplasma urethritis", "blood group incompatibility", "premalignant hematological system disease", "epiglottitis", "monoclonal gammopathy", "xanthogranulomatous pyelonephritis"]
last_modified_at: 2026-11-24
description: "Aztreonam: forudsagt ny indikation Hyperamylasæmi (hyperamylasemia) (evidensniveau L5). I Danmark, markedsføringstilladelser: 2 (gyldige: 2)"
---

# Aztreonam
{: .fs-9 }

Evidensniveau: **L5** | Forudsagte indikationer: **10** stk.
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

## Aztreonam: monobactam-antibiotikum (hæmmer bakteriel cellevægssyntese) → Hyperamylasæmi (hyperamylasemia)
{: .text-alpha }

## Resumé i én sætning

Aztreonam er et antibiotikum af monobactam-typen, som virker mod gramnegative bakterier. Ifølge TxGNN-modellen forudsiges det at kunne have effekt ved **hyperamylasæmi (hyperamylasemia)**, men der er **ingen kliniske forsøg** og **ingen publikationer** i de data, der er indsamlet til denne rapport. Forudsigelsen hviler dermed udelukkende på modellen.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Ikke registreret i de lokale data |
| Forudsagt ny indikation | Hyperamylasæmi (hyperamylasemia) |
| TxGNN-forudsigelsesscore | 0,9973 |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført (gyldige tilladelser: 2 af 2) |
| Antal markedsføringstilladelser | 2 (gyldige: 2) |
| Anbefalet beslutning | Hold |

---

## Hvorfor er denne forudsigelse (ikke) rimelig?

Aztreonam hæmmer bakteriel cellevægssyntese ved binding til penicillinbindende protein 3 (PBP3) hos gramnegative aerobe bakterier. Ifølge afsnittet »Mechanism of Action« i den produktinformation, som den amerikanske FDA har godkendt (Prescribing Information), for Aztreonam (uofficiel oversættelse): »Aztreonam er et baktericidt middel, der virker ved at hæmme syntesen af bakteriernes cellevæg. Aztreonam har aktivitet i tilstedeværelse af visse beta-lactamaser, både penicillinaser og cefalosporinaser, fra gramnegative og grampositive bakterier.« Engelsk originaltekst: "Aztreonam is a bactericidal agent that acts by inhibition of bacterial cell wall synthesis. Aztreonam has activity in the presence of some beta-lactamases, both penicillinases and cephalosporinases, of Gram-negative and Gram-positive bacteria." ([DailyMed: aztreonam prescribing information, Hospira, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=d4500795-3b07-4a7d-b432-73cafbb3dbc6), version af 2024-06-03; hentet 2026-11-20).

Hyperamylasæmi er et laboratoriefund (forhøjet amylase i blodet) og ikke en bakteriel infektion. Der er ingen plausibel mekanistisk forbindelse mellem en antibakteriel virkning og normalisering af amylaseniveauet. Den høje score skyldes sandsynligvis en artefakt i modellens netværksstruktur og ikke en reel farmakologisk sammenhæng.

---

## Evidens fra kliniske forsøg

Der er i øjeblikket ingen relaterede kliniske forsøg registreret.

---

## Litteraturevidens

Der er i øjeblikket ingen relateret litteratur tilgængelig.

---

## Information om markedet i Danmark

<!-- licenses:begin -->

| Markedsføringstilladelsesnummer | Produktnavn | Lægemiddelform | Aktive stoffer | Status |
|---------|------|------|------|------|
| 28107028323 | Emblaveo | pulver til koncentrat til infusionsvæske, opløsning | Avibactamnatrium, AZTREONAM | Gyldig |

Tabellen viser 1 af 2 markedsføringstilladelser til humane lægemidler med dette aktive stof i Lægemiddelstyrelsens lister over godkendte og afregistrerede lægemidler; gyldige tilladelser står først.

<!-- licenses:end -->

Emblaveo er en nationalt registreret, gyldig tilladelse (Pfizer Europe MA EEIG).

---

## Sikkerhedsovervejelser

**Lægemiddelinteraktioner:** Der er fundet i alt 37 registrerede interaktioner. Blandt de oplyste er følgende klassificeret som moderate:
- Picosulfursyre
- Dicoumarol
- Warfarin

Øvrige registrerede interaktioner (bl.a. protonpumpehæmmere, vancomycin, metronidazol, kortikosteroider, amphotericin B, acetylsalicylsyre og heparin) har uafklaret alvorlighedsgrad.

Se i øvrigt det godkendte produktresumé (SmPC) for fuldstændige sikkerhedsoplysninger.

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Der er ingen kliniske forsøg eller publikationer, der undersøger aztreonam ved hyperamylasæmi, og der er ingen plausibel mekanisme. Evidensniveauet er L5 (kun modelforudsigelse).

**Hvis man alligevel ønsker at gå videre, kræves følgende:**
- En biologisk begrundelse for, hvorfor en antibakteriel substans skulle påvirke serumamylase
- Systematisk litteratursøgning og eventuelle prækliniske data, der direkte omhandler hyperamylasæmi
- Mekanismedata (MOA) for aztreonam
- Gennemgang af produktresuméet med hensyn til advarsler og kontraindikationer

<!-- review:begin log -->

## Gennemgangslog

Nedenfor er gennemgangsloggen for denne side. Sætningen om, at data om virkningsmekanismen ikke var tilgængelige, er erstattet med et uddrag fra den angivne officielle produktinformation (med uofficiel oversættelse); modelforudsigelser, evidensniveauer og konklusioner er ikke omskrevet.

| Gennemgået | Punkt | Handling | Kilde |
|------|------|------|------|
| 2026-11-20 | Sætningen »data om virkningsmekanismen er ikke tilgængelige« erstattet med uddrag fra den amerikanske produktinformation | Sætning om manglende data om virkningsmekanismen erstattet med et uddrag med kilde | [DailyMed: aztreonam prescribing information, Hospira, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=d4500795-3b07-4a7d-b432-73cafbb3dbc6) |

<!-- review:end log -->

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

