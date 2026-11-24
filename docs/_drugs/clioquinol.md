---
layout: default
title: Clioquinol
parent: Kun modelforudsigelse (L5)
nav_order: 206
evidence_level: L5
indication_count: 2
monitor_inn: "clioquinol"
predicted_indications: ["ectothrix infectious disease", "endothrix infectious disease"]
last_modified_at: 2026-11-24
description: "Clioquinol: forudsagt ny indikation Ektotrix-infektionssygdom (ectothrix infectious disease) (evidensniveau L5). I Danmark, markedsføringstilladelser: 1 (gyldige: 1)"
---

# Clioquinol
{: .fs-9 }

Evidensniveau: **L5** | Forudsagte indikationer: **2** stk.
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

## Clioquinol: halogeneret hydroxyquinolin med antimykotisk virkning → ektotrix-infektionssygdom (ectothrix infectious disease)
{: .text-alpha }

## Kort resumé

Clioquinol er et halogeneret hydroxyquinolin med antifungal og antibakteriel virkning. Det er i Danmark markedsført som ørdråber. TxGNN-modellen forudsiger, at lægemidlet kan have effekt mod **ektotrix-infektionssygdom (ectothrix infectious disease)**, men der er i de indsamlede data **ingen kliniske forsøg og ingen publikationer**, som understøtter forudsigelsen.

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Ikke registreret i de lokale data |
| Forudsagt ny indikation | Ektotrix-infektionssygdom (ectothrix infectious disease) |
| TxGNN-forudsigelsesscore | 0,9926 |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført (gyldige tilladelser: 1 af 1) |
| Antal markedsføringstilladelser | 1 (gyldige: 1) |
| Anbefalet beslutning | Hold |

## Hvorfor er forudsigelsen rimelig?

Ektotrix-infektion er en dermatofytinfektion i hårskaftet, hvor svampens artrokonidier dannes på hårets yderside. Clioquinol er et halogeneret hydroxyquinolin, hvis antifungale og antibakterielle virkning formodes at hænge sammen med chelering af metalioner. Ifølge ChEMBL (EMBL-EBI) er den registrerede virkningsmekanisme for Clioquinol (uofficiel oversættelse): »Zinkchelerende middel; Kobberchelerende middel; Jernchelerende middel«. Engelsk originaltekst: "Zinc chelating agent; Copper chelating agent; Iron chelating agent" ([ChEMBL CHEMBL497 (clioquinol): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL497), CC BY-SA 3.0; hentet 2026-11-19).

Den høje score er alene en beregningsmæssig forudsigelse. Den afspejler sandsynligvis, at de forårsagende organismer (dermatofytter som *Microsporum* og *Trichophyton*) er de samme som ved andre dermatofytinfektioner i huden, hvor clioquinol er kendt.

Der er en vigtig begrænsning: Hårskaftsinfektioner behandles normalt med systemisk antimykotisk behandling, fordi lokalbehandling trænger dårligt ind i hårfolliklen. Det svækker den translationelle begrundelse. Det eneste markedsførte produkt i Danmark er desuden ørdråber, hvilket ikke er en formulering til hårbærende hud.

## Klinisk evidens

Der er for tiden ingen relaterede kliniske forsøg registreret.

## Litteraturevidens

Der er for tiden ingen relateret litteratur tilgængelig.

## Markedsinformation i Danmark

<!-- licenses:begin -->

| Markedsføringstilladelsesnummer | Produktnavn | Lægemiddelform | Aktive stoffer | Status |
|---------|------|------|------|------|
| 28100540268 | Locacorten-Vioform | øredråber, opløsning | Clioquinol, Flumetasonpivalat | Gyldig |

Tabellen viser den eneste markedsføringstilladelse til et humant lægemiddel med dette aktive stof i Lægemiddelstyrelsens lister over godkendte og afregistrerede lægemidler.

<!-- licenses:end -->

Tilladelsen er gyldig og omfatter et kombinationspræparat (indehaver: Amdipharm Limited).

<!-- review:begin dk-lic-20261112-clioquinol-1 -->

> **Rettelse ved gennemgang (2026-11-12)**: Oprindeligt stod der: "omfatter et enkeltstofpræparat (indehaver: Amdipharm Limited)" Ifølge Lægemiddelstyrelsens liste over godkendte lægemidler (data fra 2026-11-05, feltet AktiveSubstanser): Locacorten-Vioform indeholder flumetason og clioquinol. Kilde: [Lægemiddelstyrelsen: liste over godkendte lægemidler](https://laegemiddelstyrelsen.dk/en/sideeffects/find-medicines/lists-with-information-about-medicines/).

<!-- review:end dk-lic-20261112-clioquinol-1 -->

## Sikkerhedsovervejelser

Der er ikke fundet oplysninger om interaktioner i de indsamlede data. Der foreligger ingen fuldstændige data om advarsler og kontraindikationer. Se det godkendte produktresumé (SmPC) for sikkerhedsoplysninger.

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelsen bygger udelukkende på modellen (evidensniveau L5), uden kliniske forsøg eller publikationer for sygdommen. Dertil kommer, at lokalbehandling formodes at have dårlig penetration til hårskaftet, og at det eneste danske præparat er ørdråber.

**For at komme videre kræves følgende:**
- Data om virkningsmekanisme (MOA) og in vitro-data for antifungal aktivitet mod ektotrix-forårsagende dermatofytter
- Gennemgang af produktresuméets advarsler og kontraindikationer (nødvendigt før sikkerhedsvurdering)
- Vurdering af, om en lokal formulering kan nå effektive koncentrationer i hårskaftet, sammenlignet med standard systemisk behandling
- Registrerede kliniske forsøg eller publicerede studier, der direkte undersøger ektotrix-infektion

<!-- review:begin log -->

## Gennemgangslog

Nedenfor er gennemgangsloggen for denne side: udsagn kontrolleret mod Lægemiddelstyrelsens liste over godkendte lægemidler. Rettelser er begrænset til grundlæggende faktuelle udsagn; modelforudsigelser, evidensniveauer og konklusioner er ikke omskrevet. Sætningen om, at data om virkningsmekanismen ikke var tilgængelige, er erstattet med et uddrag fra den angivne officielle produktinformation (med uofficiel oversættelse).

| Gennemgået | Punkt | Handling | Kilde |
|------|------|------|------|
| 2026-11-12 | Enkeltstof/kombination rettet | Rettet | [Lægemiddelstyrelsen: liste over godkendte lægemidler](https://laegemiddelstyrelsen.dk/en/sideeffects/find-medicines/lists-with-information-about-medicines/) |
| 2026-11-19 | Sætningen »data om virkningsmekanismen er ikke tilgængelige« erstattet med uddrag fra den amerikanske produktinformation | Sætning om manglende data om virkningsmekanismen erstattet med et uddrag med kilde (revideret 2026-11-20; tidligere version gemt i loggen) | [ChEMBL CHEMBL497 (clioquinol): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL497) |

<!-- review:end log -->

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

