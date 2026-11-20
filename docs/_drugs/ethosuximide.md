---
layout: default
title: Ethosuximide
parent: Kun modelforudsigelse (L5)
nav_order: 333
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-20
description: "Ethosuximide: forudsagt ny indikation Nefrogent syndrom med uhensigtsmæssig antidiurese (NSIAD) (evidensniveau L5). Oprindelig indikation: Absence-epilepsi (iht. videnbasen i TxGNN"
monitor_inn: "ethosuximide"
predicted_indications: ["nephrogenic syndrome of inappropriate antidiuresis"]
---

# Ethosuximide
{: .fs-9 }

Evidensniveau: **L5** | Forudsagte indikationer: **1** stk.
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

## Ethosuximid: Fra absence-epilepsi til nefrogent syndrom med uhensigtsmæssig antidiurese (NSIAD)
{: .text-alpha }

## Opsummering i én sætning

Ethosuximid er et antiepileptikum, som oprindeligt anvendes til behandling af absence-epilepsi.
TxGNN-modellen forudsiger, at det kan have effekt ved **nefrogent syndrom med uhensigtsmæssig antidiurese (NSIAD)**,
men der er på nuværende tidspunkt **ingen kliniske forsøg** og **ingen publikationer**, der understøtter denne retning. Forudsigelsen hviler alene på modellens score.

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Absence-epilepsi (iht. videnbasen i TxGNN; den danske godkendelsestekst er ikke angivet) |
| Forudsagt ny indikation | Nefrogent syndrom med uhensigtsmæssig antidiurese (NSIAD) |
| TxGNN-forudsigelsesscore | 0,9991 |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført (gyldige tilladelser: 9 af 9) |
| Antal markedsføringstilladelser | 9 (gyldige: 9) |
| Anbefalet beslutning | Hold |

## Hvorfor er denne forudsigelse rimelig?

Ifølge afsnittet »Clinical Pharmacology« i den produktinformation, som den amerikanske FDA har godkendt (Prescribing Information), for Ethosuximide (uofficiel oversættelse): »Ethosuximid undertrykker den paroksystiske spike-wave-aktivitet med tre cykler pr. sekund, der er forbundet med bevidsthedssvigt, og som er almindelig ved absence-anfald (petit mal). Hyppigheden af epileptiforme anfald nedsættes, tilsyneladende ved hæmning af den motoriske cortex og forhøjelse af centralnervesystemets tærskel for krampefremkaldende stimuli.« Engelsk originaltekst: "Ethosuximide suppresses the paroxysmal three cycle per second spike and wave activity associated with lapses of consciousness which is common in absence (petit mal) seizures. The frequency of epileptiform attacks is reduced, apparently by depression of the motor cortex and elevation of the threshold of the central nervous system to convulsive stimuli." ([DailyMed: Zarontin (ethosuximide) prescribing information, Parke-Davis Div of Pfizer Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=0e008f33-70a1-4bc6-b3a0-d45214418ab6), version af 2026-05-25; hentet 2026-11-19). Det er generelt beskrevet, at ethosuximid blokerer T-type-calciumkanaler i thalamiske neuroner, hvilket forklarer virkningen ved absence-epilepsi.

Der er ikke noget etableret biologisk link mellem denne mekanisme og NSIAD. NSIAD skyldes aktiverende mutationer i vasopressin V2-receptoren (AVPR2) eller i nogle tilfælde GNAS-relateret signalering og medfører vandretention og hyponatriæmi. En sammenhæng kunne tænkes via indirekte effekter på calciumsignalering eller nedstrøms regulering af aquaporin-2, men det er spekulativt og ikke understøttet af data.

Den meget høje score kommer fra TxGNN-modellen (deep learning) og kan afspejle ligheder, som modellen har lært mellem beslægtede sygdomme, snarere end biologisk evidens. Forudsigelsen bør derfor betragtes som en hypotese, ikke som et evidensbaseret fund.

## Kliniske forsøg

Der er på nuværende tidspunkt ingen relaterede kliniske forsøg registreret.

## Litteraturevidens

Der er på nuværende tidspunkt ingen relateret litteratur tilgængelig.

## Markedsinformation for Danmark

| Markedsføringstilladelsesnummer | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28107149824 | Ethonor (Nordic Prime ApS) | Kapsler, bløde | Indikationstekst ikke angivet i de indsamlede data |

## Sikkerhedsovervejelser

**Kontraindikationer/risikotilstande fra vidensgrafen (ikke fra produktresuméets tekst):** Vidensgrafen peger på følgende sygdomme, hvor brug af ethosuximid er forbundet med kontraindikation:
- Angstlidelse, neurotisk lidelse og dysthymi
- Nyresygdom og pyoureter
- Hæmatologiske sygdomme, herunder neutropeni og agranulocytose
- Leversygdom og galdeblæresygdom
- Systemisk lupus erythematosus (herunder pædiatrisk form)
- Akut intermitterende porfyri

Disse oplysninger skal verificeres mod det godkendte produktresumé.

**Lægemiddelinteraktioner:** Der er identificeret 101 interaktioner, hvoraf de 20 viste alle er af moderat sværhedsgrad. Blandt de vigtigste er:
- Opioider og beslægtede midler: morfin (også liposomal), opium
- Centralt dæmpende eller antiemetiske midler: promethazin, metoclopramid, aprepitant, dronabinol, nabilon
- Alkohol (ethanol)
- Folinsyre, leucovorin og levoleucovorin
- Malariamidler/antireumatika: chloroquin, hydroxychloroquin, mefloquin
- Øvrige: sibutramin, cobicistat, deferasirox, fostamatinib

Derudover foreligger der ikke oplysninger om advarsler og kontraindikationer fra produktresuméet. Se det godkendte produktresumé for fuldstændige sikkerhedsoplysninger.

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelsen understøttes udelukkende af en høj modelscore (evidensniveau L5). Der findes ingen kliniske forsøg eller publikationer, virkningsmekanismen er ikke tilgængelig i de indsamlede data, og der er ikke noget kendt biologisk link til NSIAD.

**For at komme videre kræves følgende:**
- Detaljerede data om virkningsmekanisme (MOA), f.eks. fra DrugBank
- Hentning og gennemgang af produktresuméet fra Lægemiddelstyrelsen (advarsler, kontraindikationer og godkendt indikationstekst)
- Præklinisk eller mekanistisk evidens for en effekt på AVPR2-/GNAS-signalering eller aquaporin-2-regulering
- Systematisk litteratur- og forsøgssøgning efter eventuelle relevante data
- Vurdering af administrationsvej og formulering (kapsler, bløde) i forhold til den nye indikation, samt sikkerhedsprofil i patientgruppen

<!-- review:begin log -->

## Gennemgangslog

Nedenfor er gennemgangsloggen for denne side. Sætningen om, at data om virkningsmekanismen ikke var tilgængelige, er erstattet med et uddrag fra den angivne officielle produktinformation (med uofficiel oversættelse); modelforudsigelser, evidensniveauer og konklusioner er ikke omskrevet.

| Gennemgået | Punkt | Handling | Kilde |
|------|------|------|------|
| 2026-11-19 | Sætningen »data om virkningsmekanismen er ikke tilgængelige« erstattet med uddrag fra den amerikanske produktinformation | Sætning om manglende data om virkningsmekanismen erstattet med et uddrag med kilde | [DailyMed: Zarontin (ethosuximide) prescribing information, Parke-Davis Div of Pfizer Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=0e008f33-70a1-4bc6-b3a0-d45214418ab6) |

<!-- review:end log -->

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

