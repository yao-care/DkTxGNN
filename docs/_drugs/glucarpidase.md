---
layout: default
title: Glucarpidase
parent: Kun modelforudsigelse (L5)
nav_order: 396
evidence_level: L5
indication_count: 10
monitor_inn: "Glucarpidase"
predicted_indications: ["diabetic cataract", "diabetic retinopathy", "craniostenosis cataract", "immature cataract", "mature cataract", "diabetes mellitus type 2 associated cataract", "tetanic cataract", "nuclear senile cataract", "cortical cataract", "senile cataract"]
last_modified_at: 2026-11-24
description: "Glucarpidase: forudsagt ny indikation Diabetisk katarakt (evidensniveau L5). Oprindelig indikation: Ikke angivet i de data…"
---

# Glucarpidase
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

## Glucarpidase: Fra metotrexat-toksicitet til diabetisk katarakt
{: .text-alpha }

## Resumé i én sætning

Glucarpidase er et rekombinant enzym, som nedbryder metotrexat i blodet, og som markedsføres i Danmark som Voraxaze. TxGNN-modellen forudsiger, at lægemidlet kan have effekt på **diabetisk katarakt**, men der er **0 kliniske forsøg** og **0 publikationer** i de data, der er indsamlet til denne rapport. Forudsigelsen er rent beregningsbaseret og har ingen mekanistisk understøttelse.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Ikke angivet i de data, der er indsamlet til rapporten (godkendelsens indikationstekst er tom) |
| Forudsagt ny indikation | Diabetisk katarakt |
| TxGNN-forudsigelsesscore | 0,9985 |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført (gyldige tilladelser: 1 af 1) |
| Antal markedsføringstilladelser | 1 (gyldige: 1) |
| Anbefalet beslutning | Hold (afvent) |

---

## Hvorfor er forudsigelsen (ikke) rimelig?

Ifølge afsnittet »Mechanism of Action« i den produktinformation, som den amerikanske FDA har godkendt (Prescribing Information), for Glucarpidase (uofficiel oversættelse): »Glucarpidase er et rekombinant bakterielt enzym, der hydrolyserer den carboxyl-terminale glutamatrest fra folinsyre og klassiske antifolater såsom methotrexat. Glucarpidase omdanner methotrexat til dets inaktive metabolitter 4-deoxy-4-amino-N 10 -methylpteroinsyre (DAMPA) og glutamat.« Engelsk originaltekst: "Glucarpidase is a recombinant bacterial enzyme that hydrolyzes the carboxyl- terminal glutamate residue from folic acid and classical antifolates such as methotrexate. Glucarpidase converts methotrexate to its inactive metabolites 4-deoxy-4-amino-N 10 - methylpteroic acid (DAMPA) and glutamate." ([DailyMed: Voraxaze (glucarpidase) prescribing information, BTG International Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=acaef5a6-b740-40e3-8ffe-74a75c74745c), version af 2024-11-27; hentet 2026-11-19). Ud fra almindelig farmakologisk viden er glucarpidase en rekombinant bakteriel carboxypeptidase G2, som hydrolyserer ekstracellulært metotrexat og andre folater til inaktive metabolitter. Det er et stort protein, som holder sig i det ekstracellulære rum.

Diabetisk katarakt skyldes primært polyolvejen (aldosereduktase), glykering af linseproteiner og oxidativ stress. Glucarpidase påvirker ingen af disse processer, og det er ikke sandsynligt, at et så stort protein når ind i linsen.

Den høje score fra TxGNN-modellen (deep learning) på 0,9985 kan afspejle ligheder, som modellen har lært mellem beslægtede sygdomme, og ikke biologisk evidens. Flere kataraktundertyper har identiske scorer, hvilket tyder på redundans mellem termerne frem for uafhængige signaler. Forudsigelsen bør derfor betragtes som en beregningsmæssig artefakt og ikke som et klinisk holdepunkt.

Øvrige forudsagte indikationer i rangeringen (bl.a. diabetisk retinopati, craniostenose-katarakt, umoden og moden katarakt, senil katarakt, nuklear og kortikal katarakt) har samme karakter: ingen studier og ingen plausibel mekanisme.

---

## Evidens fra kliniske forsøg

Der er i øjeblikket ingen relaterede kliniske forsøg registreret.

---

## Evidens fra litteraturen

Der er i øjeblikket ingen relateret litteratur tilgængelig.

---

## Information om det danske marked

<!-- licenses:begin -->

| Markedsføringstilladelsesnummer | Produktnavn | Lægemiddelform | Aktive stoffer | Status |
|---------|------|------|------|------|
| 28106459820 | Voraxaze | pulver til injektionsvæske, opløsning | Glucarpidase | Gyldig |

Tabellen viser den eneste markedsføringstilladelse til et humant lægemiddel med dette aktive stof i Lægemiddelstyrelsens lister over godkendte og afregistrerede lægemidler.

<!-- licenses:end -->

---

## Sikkerhedsmæssige overvejelser

**Lægemiddelinteraktioner:** Der er identificeret 8 interaktioner af moderat sværhedsgrad (kilde: DDInter):
- Proguanil
- Trimethoprim
- Levoleucovorin
- Pemetrexed
- Pralatrexat
- Pyrimethamin
- Leucovorin
- Trimetrexat

Det bemærkes, at flere af disse er folatrelaterede stoffer, hvilket er i tråd med glucarpidases folatnedbrydende virkning.

For advarsler og kontraindikationer henvises til det godkendte produktresumé (SmPC).

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelsen bygger udelukkende på en modelscore uden kliniske forsøg, publikationer eller plausibel mekanisme. Glucarpidase er et ekstracellulært folatnedbrydende enzym uden kendt effekt på de processer, der driver katarakt, og det er usandsynligt, at det når linsen eller nethinden.

**For at gå videre kræves følgende:**
- Data om virkningsmekanisme (MOA) og godkendt indikationstekst fra produktresuméet
- Prækliniske data, der viser en biologisk sammenhæng mellem folat-/metotrexatnedbrydning og linsepatologi
- Dokumentation for, at lægemidlet kan nå målvævet (linse/nethinde)
- Gennemgang af produktresuméets advarsler og kontraindikationer

<!-- review:begin log -->

## Gennemgangslog

Nedenfor er gennemgangsloggen for denne side. Sætningen om, at data om virkningsmekanismen ikke var tilgængelige, er erstattet med et uddrag fra den angivne officielle produktinformation (med uofficiel oversættelse); modelforudsigelser, evidensniveauer og konklusioner er ikke omskrevet.

| Gennemgået | Punkt | Handling | Kilde |
|------|------|------|------|
| 2026-11-19 | Sætningen »data om virkningsmekanismen er ikke tilgængelige« erstattet med uddrag fra den amerikanske produktinformation | Sætning om manglende data om virkningsmekanismen erstattet med et uddrag med kilde | [DailyMed: Voraxaze (glucarpidase) prescribing information, BTG International Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=acaef5a6-b740-40e3-8ffe-74a75c74745c) |

<!-- review:end log -->

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

