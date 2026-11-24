---
layout: default
title: Pegvaliase
parent: Kun modelforudsigelse (L5)
nav_order: 640
evidence_level: L5
indication_count: 3
last_modified_at: 2026-11-24
description: "Pegvaliase: forudsagt ny indikation diabetic retinopathy (evidensniveau L5). Oprindelig indikation: Godkendt indikationstekst er ikke tilgængelig i de indsamlede data. I…"
monitor_inn: "Pegvaliase"
predicted_indications: ["diabetic retinopathy", "severe nonproliferative diabetic retinopathy", "diabetic cataract"]
---

# Pegvaliase
{: .fs-9 }

Evidensniveau: **L5** | Forudsagte indikationer: **3** stk.
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

## Pegvaliase: Fra phenylketonuri til diabetic retinopathy
{: .text-alpha }

## Resumé i én sætning

Pegvaliase (markedsført som Palynziq) er et PEGyleret enzym, som nedbryder phenylalanin, og som er godkendt til behandling af phenylketonuri. TxGNN-modellen forudsiger, at det kan have effekt på **diabetisk retinopati**, men forudsigelsen er alene beregningsbaseret: der er **0 kliniske forsøg** og **0 publikationer**, som understøtter den.

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Godkendt indikationstekst er ikke tilgængelig i de indsamlede data. Ifølge produktets kendte profil er det phenylketonuri (PKU). |
| Foreslået ny indikation | Diabetisk retinopati |
| TxGNN-forudsigelsesscore | 0.9917 |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført (gyldige tilladelser: 3 af 3) |
| Antal markedsføringstilladelser | 3 (gyldige: 3) |
| Anbefalet beslutning | Hold |

## Hvorfor er denne forudsigelse (ikke) rimelig?

Ifølge afsnittet »Mechanism of Action« i den produktinformation, som den amerikanske FDA har godkendt (Prescribing Information), for Pegvaliase (uofficiel oversættelse): »Pegvaliase-pqpz er et PEGyleret phenylalanin-ammoniaklyase (PAL)-enzym, der omdanner phenylalanin til ammoniak og trans -kanelsyre. Det erstatter den manglende aktivitet af enzymet phenylalaninhydroxylase (PAH) hos patienter med PKU og nedsætter koncentrationen af phenylalanin i blodet.« Engelsk originaltekst: "Pegvaliase-pqpz is a PEGylated phenylalanine ammonia lyase (PAL) enzyme that converts phenylalanine to ammonia and trans -cinnamic acid. It substitutes for the deficient phenylalanine hydroxylase (PAH) enzyme activity in patients with PKU and reduces blood phenylalanine concentrations." ([DailyMed: Palynziq (pegvaliase-pqpz) prescribing information, BioMarin Pharmaceutical Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=6dba844a-db02-44f8-8593-ce497ed9406c), version af 2026-03-02; hentet 2026-11-19). Pegvaliase er et PEGyleret phenylalanin-ammoniak-lyase, som omdanner phenylalanin og dermed sænker koncentrationen i blodet. Det er baggrunden for brugen ved phenylketonuri.

Diabetisk retinopati er en mikrovaskulær komplikation til langvarig hyperglykæmi og involverer blandt andet VEGF-signalering, inflammation, tab af pericytter og retinal iskæmi. De foreliggende data viser ingen plausibel mekanistisk forbindelse mellem phenylalaninnedbrydning og disse processer. Den høje score (0.9917) stammer fra TxGNN-modellen (deep learning) og kan afspejle ligheder, modellen har lært mellem beslægtede sygdomme, ikke biologisk evidens.

Modellen foreslår også beslægtede øjenlidelser: svær non-proliferativ diabetisk retinopati (score 0.9916, en undertype af ovenstående og sandsynligvis en redundant forudsigelse) og diabetisk katarakt (0.9911). Ingen af dem har understøttende forsøg eller litteratur.

## Klinisk evidens

Der er for øjeblikket ingen relaterede kliniske forsøg registreret.

## Litteraturevidens

Der er for øjeblikket ingen relateret litteratur tilgængelig.

## Information om det danske marked

<!-- licenses:begin -->

| Markedsføringstilladelsesnummer | Produktnavn | Lægemiddelform | Aktive stoffer | Status |
|---------|------|------|------|------|
| 28106089818 | Palynziq | injektionsvæske, opløsning i fyldt injektionssprøjte | Pegvaliase | Gyldig |
| 28106089918 | Palynziq | injektionsvæske, opløsning i fyldt injektionssprøjte | Pegvaliase | Gyldig |
| 28106089718 | Palynziq | injektionsvæske, opløsning i fyldt injektionssprøjte | Pegvaliase | Gyldig |

Tabellen viser alle 3 markedsføringstilladelser til humane lægemidler med dette aktive stof i Lægemiddelstyrelsens lister over godkendte og afregistrerede lægemidler; gyldige tilladelser står først.

<!-- licenses:end -->

## Sikkerhedsovervejelser

**Lægemiddelinteraktioner:** Der er identificeret 16 interaktioner af moderat sværhedsgrad (kilde: DDInter). Interaktionerne vedrører primært andre PEGylerede eller pegylerede produkter og enkelte øvrige stoffer:

- Pegylerede biologiske lægemidler: pegloticase, pegaspargase, pegfilgrastim, peginesatid, peginterferon alfa-2a, alfa-2b og beta-1a, pegvisomant, pegademase, pegaptanib (oftalmisk), certolizumab pegol
- Koagulationsfaktorer: rekombinant antihæmofilifaktor og human koagulationsfaktor IX
- Øvrige: liposomal doxorubicin, medroxyprogesteronacetat, naloxegol

Se i øvrigt det godkendte produktresumé (SmPC) for fuldstændige oplysninger om advarsler og kontraindikationer.

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelsen bygger udelukkende på en modelscore uden kliniske forsøg, litteratur eller en plausibel mekanistisk forbindelse (evidensniveau L5). Flere af de foreslåede indikationer er desuden dubletter eller undertyper af hinanden.

**For at komme videre kræves følgende:**
- Hentning og gennemgang af produktresuméet (SmPC) for advarsler, kontraindikationer og den godkendte indikationstekst
- Data om virkningsmekanisme (MOA) fra DrugBank
- Præklinisk eller mekanistisk dokumentation for en sammenhæng mellem phenylalaninmetabolisme og retinal patologi
- Vurdering af administrationsvej: pegvaliase gives som subkutan injektion, og det er uafklaret, om dette er foreneligt med behandling af øjensygdomme
- En systematisk litteratur- og forsøgsgennemgang, før der overvejes yderligere evaluering

<!-- review:begin log -->

## Gennemgangslog

Nedenfor er gennemgangsloggen for denne side. Sætningen om, at data om virkningsmekanismen ikke var tilgængelige, er erstattet med et uddrag fra den angivne officielle produktinformation (med uofficiel oversættelse); modelforudsigelser, evidensniveauer og konklusioner er ikke omskrevet.

| Gennemgået | Punkt | Handling | Kilde |
|------|------|------|------|
| 2026-11-19 | Sætningen »data om virkningsmekanismen er ikke tilgængelige« erstattet med uddrag fra den amerikanske produktinformation | Sætning om manglende data om virkningsmekanismen erstattet med et uddrag med kilde | [DailyMed: Palynziq (pegvaliase-pqpz) prescribing information, BioMarin Pharmaceutical Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=6dba844a-db02-44f8-8593-ce497ed9406c) |

<!-- review:end log -->

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

