---
layout: default
title: Pegvaliase
parent: Kun modelforudsigelse (L5)
nav_order: 640
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-28
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
| Markedsstatus i Danmark | Markedsført (gyldige tilladelser: 1 af 1) |
| Antal markedsføringstilladelser | 1 (gyldige: 1) |
| Anbefalet beslutning | Hold |

## Hvorfor er denne forudsigelse (ikke) rimelig?

Detaljerede data om virkningsmekanismen er ikke tilgængelige i de indsamlede data. Pegvaliase er et PEGyleret phenylalanin-ammoniak-lyase, som omdanner phenylalanin og dermed sænker koncentrationen i blodet. Det er baggrunden for brugen ved phenylketonuri.

Diabetisk retinopati er en mikrovaskulær komplikation til langvarig hyperglykæmi og involverer blandt andet VEGF-signalering, inflammation, tab af pericytter og retinal iskæmi. De foreliggende data viser ingen plausibel mekanistisk forbindelse mellem phenylalaninnedbrydning og disse processer. Den høje score (0.9917) stammer fra TxGNN-modellen (deep learning) og kan afspejle ligheder, modellen har lært mellem beslægtede sygdomme, ikke biologisk evidens.

Modellen foreslår også beslægtede øjenlidelser: svær non-proliferativ diabetisk retinopati (score 0.9916, en undertype af ovenstående og sandsynligvis en redundant forudsigelse) og diabetisk katarakt (0.9911). Ingen af dem har understøttende forsøg eller litteratur.

## Klinisk evidens

Der er for øjeblikket ingen relaterede kliniske forsøg registreret.

## Litteraturevidens

Der er for øjeblikket ingen relateret litteratur tilgængelig.

## Information om det danske marked

| Markedsføringstilladelsesnr. | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28106089818 | Palynziq (BioMarin International Limited) | Injektionsvæske, opløsning i fyldt injektionssprøjte | Indikationstekst ikke tilgængelig i de indsamlede data |

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
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

