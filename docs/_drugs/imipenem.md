---
layout: default
title: Imipenem
parent: Kun modelforudsigelse (L5)
nav_order: 430
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-24
monitor_inn: "imipenem"
predicted_indications: ["diffuse scleroderma", "paratyphoid fever", "salmonellosis", "sinusitis", "chronic rhinosinusitis", "typhoid fever", "chronic ethmoidal sinusitis", "paranasal sinus neoplasm (disease)", "eosinophilia-myalgia syndrome"]
description: "Imipenem: forudsagt ny indikation Diffus sklerodermi (diffuse scleroderma) (evidensniveau L5). I Danmark, markedsføringstilladelser: 3 (gyldige: 3)"
---

# Imipenem
{: .fs-9 }

Evidensniveau: **L5** | Forudsagte indikationer: **9** stk.
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

## Imipenem: Diffus sklerodermi (diffuse scleroderma)
{: .text-alpha }

## Resumé i én sætning

Imipenem er et bredspektret carbapenem-antibiotikum, der hæmmer bakteriens cellevægssyntese.
TxGNN-modellen forudsiger, at det kan have effekt ved **diffus sklerodermi (diffuse scleroderma)**,
men der er **ingen registrerede kliniske forsøg** og **ingen publikationer** til at understøtte denne forudsigelse.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Ikke registreret i de lokale data |
| Forudsagt ny indikation | Diffus sklerodermi (diffuse scleroderma) |
| TxGNN-forudsigelsesscore | 0.9999 |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført (gyldige tilladelser: 3 af 3) |
| Antal markedsføringstilladelser | 3 (gyldige: 3) |
| Anbefalet beslutning | Hold |

---

## Hvorfor er forudsigelsen rimelig?

Ifølge ChEMBL (EMBL-EBI) er den registrerede virkningsmekanisme for Imipenem (uofficiel oversættelse): »Hæmmer af bakterielt penicillinbindende protein«. Engelsk originaltekst: "Bacterial penicillin-binding protein inhibitor" ([ChEMBL CHEMBL43708 (imipenem): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL43708), CC BY-SA 3.0; hentet 2026-11-19). Imipenem er et carbapenem, der binder til penicillinbindende proteiner og dermed hæmmer bakteriens cellevægssyntese.

Diffus sklerodermi er derimod en autoimmun, fibrotisk sygdom. Der er ingen kendt biologisk forbindelse mellem en antibakteriel virkningsmekanisme og sygdommens kerneprocesser, fibrose og autoimmunitet. Carbapenemer er ikke kendt for at påvirke disse processer. Den høje score skal derfor betragtes som en ren modelbaseret forudsigelse uden mekanistisk eller klinisk støtte, og den bør tolkes med stor forsigtighed.

---

## Evidens fra kliniske forsøg

Der er for tiden ingen relaterede kliniske forsøg registreret.

---

## Litteraturevidens

Der foreligger for tiden ingen relateret litteratur.

---

## Markedsinformation for Danmark

<!-- licenses:begin -->

| Markedsføringstilladelsesnummer | Produktnavn | Lægemiddelform | Aktive stoffer | Status |
|---------|------|------|------|------|
| 28106430220 | Andatin | pulver til infusionsvæske, opløsning | Cilastatinnatrium, Imipenemmonohydrat | Gyldig |
| 28107312425 | Imipenem/Cilastatin "Noridem" | pulver til infusionsvæske, opløsning | Cilastatinnatrium, Imipenemmonohydrat | Gyldig |
| 28106192418 | Recarbrio | pulver til infusionsvæske, opløsning | Cilastatinnatrium, Imipenemmonohydrat, Relebactammonohydrat | Gyldig |

Tabellen viser alle 3 markedsføringstilladelser til humane lægemidler med dette aktive stof i Lægemiddelstyrelsens lister over godkendte og afregistrerede lægemidler; gyldige tilladelser står først.

<!-- licenses:end -->

---

## Sikkerhedsovervejelser

**Lægemiddelinteraktioner** (15 registrerede interaktioner i de indsamlede data), blandt andet:
- **Alvorlige (Major):** bupropion, iohexol, iopamidol
- **Moderate:** warfarin, dicoumarol, theophyllin, aminophyllin, dyphyllin, oxtriphyllin, ciclosporin, mycophenolsyre, pemetrexed, ethinylestradiol, lindan, polyethylenglycol (3350 med elektrolytter)

For øvrig sikkerhedsinformation henvises til det godkendte produktresumé (SmPC).

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelsen om diffus sklerodermi hviler udelukkende på en modelscore uden kliniske forsøg, uden litteratur og uden en plausibel mekanistisk forbindelse mellem et antibakterielt carbapenem og en autoimmun, fibrotisk sygdom. Evidensniveauet er derfor L5.

**For at komme videre kræves følgende:**
- Detaljerede data om virkningsmekanisme og en egentlig biologisk hypotese for effekt ved diffus sklerodermi
- Prækliniske data, der kan understøtte en effekt på fibrose eller autoimmunitet
- Gennemgang af sikkerhedsoplysninger i produktresuméet, da der ikke foreligger data om advarsler og kontraindikationer i de indsamlede data

<!-- review:begin log -->

## Gennemgangslog

Nedenfor er gennemgangsloggen for denne side. Sætningen om, at data om virkningsmekanismen ikke var tilgængelige, er erstattet med et uddrag fra den angivne officielle produktinformation (med uofficiel oversættelse); modelforudsigelser, evidensniveauer og konklusioner er ikke omskrevet.

| Gennemgået | Punkt | Handling | Kilde |
|------|------|------|------|
| 2026-11-19 | Sætningen »data om virkningsmekanismen er ikke tilgængelige« erstattet med uddrag fra den amerikanske produktinformation | Sætning om manglende data om virkningsmekanismen erstattet med et uddrag med kilde (revideret 2026-11-20; tidligere version gemt i loggen) | [ChEMBL CHEMBL43708 (imipenem): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL43708) |

<!-- review:end log -->

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

