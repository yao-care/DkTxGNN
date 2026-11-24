---
layout: default
title: Roxadustat
parent: Kun modelforudsigelse (L5)
nav_order: 738
evidence_level: L5
indication_count: 4
last_modified_at: 2026-11-24
description: "Roxadustat: forudsagt ny indikation Tørre øjne (dry eye syndrome) (evidensniveau L5). Oprindelig indikation: Refraktær anæmi"
monitor_inn: "Roxadustat"
predicted_indications: ["dry eye syndrome", "bone Paget disease", "dentinogenesis imperfecta", "squamous cell carcinoma"]
---

# Roxadustat
{: .fs-9 }

Evidensniveau: **L5** | Forudsagte indikationer: **4** stk.
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

## Roxadustat: Fra refraktær anæmi til tørre øjne (dry eye syndrome)
{: .text-alpha }

## Resumé i én sætning

Roxadustat er en HIF-prolylhydroxylasehæmmer, som oprindeligt anvendes til behandling af refraktær anæmi (i EU godkendt til anæmi ved kronisk nyresvigt).
TxGNN-modellen forudsiger, at lægemidlet kan have effekt på **tørre øjne (dry eye syndrome)**.
Forudsigelsen er rent beregningsbaseret: der er **0 kliniske forsøg** og **0 publikationer**, som understøtter den i de data, der er indsamlet til rapporten.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Refraktær anæmi (godkendelsesteksten for indikationen er ikke angivet i de danske registerdata) |
| Foreslået ny indikation | Tørre øjne (dry eye syndrome) |
| TxGNN-forudsigelsesscore | 0,9951 |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført (gyldige tilladelser: 5 af 5) |
| Antal markedsføringstilladelser | 5 (gyldige: 5) |
| Anbefalet beslutning | Hold |

---

## Hvorfor er denne forudsigelse rimelig?

Ifølge ChEMBL (EMBL-EBI) er den registrerede virkningsmekanisme for Roxadustat (uofficiel oversættelse): »Hæmmer af hypoxi-inducerbar faktor-prolylhydroxylase«. Engelsk originaltekst: "Hypoxia-inducible factor prolyl hydroxylase inhibitor" ([ChEMBL CHEMBL2338329 (roxadustat): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL2338329), CC BY-SA 3.0; hentet 2026-11-19). Roxadustat er dog kendt som en hæmmer af HIF-prolylhydroxylase (EGLN-enzymer). Hæmningen stabiliserer HIF (hypoxia-inducible factor) og øger bl.a. erythropoietin, hvilket er grundlaget for effekten ved anæmi.

HIF-signalering påvirker cellernes respons på iltmangel, inflammation og vævsreparation. Det kan hypotetisk have betydning for hornhindens og øjenoverfladens epitelreparation og inflammation ved tørre øjne. Koblingen er dog **hypotetisk**: den oprindelige indikation (anæmi) og tørre øjne har ikke et oplagt patofysiologisk slægtskab, og der er hverken kliniske forsøg eller litteratur, der underbygger den. Den høje score er alene en beregningsmæssig forudsigelse. Ruteforenlighed er heller ikke vurderet: roxadustat findes kun som oral tablet, og en okulær anvendelse ville sandsynligvis kræve en anden formulering.

**Andre forudsigelser fra modellen** (samme evidensniveau L5, alle med anbefalingen Hold):

| Forudsagt indikation | TxGNN-score | Kommentar |
|------|------|------|

---

## Klinisk evidens fra forsøg

Der er i øjeblikket ikke registreret relevante kliniske forsøg.

---

## Litteraturevidens

Der foreligger i øjeblikket ingen relevant litteratur.

---

## Markedsinformation for Danmark

<!-- licenses:begin -->

| Markedsføringstilladelsesnummer | Produktnavn | Lægemiddelform | Aktive stoffer | Status |
|---------|------|------|------|------|
| 28106434120 | Evrenzo | filmovertrukne tabletter | Roxadustat | Gyldig |
| 28106434220 | Evrenzo | filmovertrukne tabletter | Roxadustat | Gyldig |
| 28106433820 | Evrenzo | filmovertrukne tabletter | Roxadustat | Gyldig |
| 28106433920 | Evrenzo | filmovertrukne tabletter | Roxadustat | Gyldig |
| 28106434020 | Evrenzo | filmovertrukne tabletter | Roxadustat | Gyldig |

Tabellen viser alle 5 markedsføringstilladelser til humane lægemidler med dette aktive stof i Lægemiddelstyrelsens lister over godkendte og afregistrerede lægemidler; gyldige tilladelser står først.

<!-- licenses:end -->

---

## Sikkerhedsovervejelser

- **Lægemiddelinteraktioner**: Der er registreret én farmakologisk interaktion, nemlig roxadustats hæmning af målproteinet EGLN2 (egl-9 family hypoxia inducible factor 2). Dette er lægemidlets tilsigtede virkningsmekanisme og ikke en klinisk interaktion med et andet lægemiddel. Der er ikke angivet noget interaktionsniveau.
- **Særligt forbehold ved kræft**: Da HIF-stabilisering er involveret i tumorbiologi (tilpasning til iltmangel, angiogenese, stofskifte), kan brug ved pladecellekarcinom potentielt være tumorfremmende.

For øvrige advarsler og kontraindikationer henvises til det godkendte produktresumé (SmPC), da disse oplysninger ikke indgår i de data, der er indsamlet til rapporten.

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelsen om tørre øjne bygger udelukkende på en modelscore (0,9951) uden understøttende kliniske forsøg eller litteratur (evidensniveau L5). Den mekanistiske kobling er hypotetisk, og lægemidlet findes kun som oral tablet.

**For at komme videre kræves følgende:**
- Data om virkningsmekanisme (MOA) til en egentlig mekanistisk analyse
- Gennemgang af produktresuméet for advarsler og kontraindikationer (nødvendig før sikkerhedsscreening)
- Prækliniske studier eller litteraturgennemgang af HIF-stabilisering ved øjenoverfladen
- Vurdering af, om en okulær formulering er nødvendig, samt af systemisk versus lokal sikkerhed
- Registrering af eventuelle kliniske forsøg, før en egentlig vurdering kan påbegyndes

<!-- review:begin log -->

## Gennemgangslog

Nedenfor er gennemgangsloggen for denne side. Sætningen om, at data om virkningsmekanismen ikke var tilgængelige, er erstattet med et uddrag fra den angivne officielle produktinformation (med uofficiel oversættelse); modelforudsigelser, evidensniveauer og konklusioner er ikke omskrevet.

| Gennemgået | Punkt | Handling | Kilde |
|------|------|------|------|
| 2026-11-19 | Sætningen »data om virkningsmekanismen er ikke tilgængelige« erstattet med uddrag fra den amerikanske produktinformation | Sætning om manglende data om virkningsmekanismen erstattet med et uddrag med kilde (revideret 2026-11-20; tidligere version gemt i loggen) | [ChEMBL CHEMBL2338329 (roxadustat): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL2338329) |

<!-- review:end log -->

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

