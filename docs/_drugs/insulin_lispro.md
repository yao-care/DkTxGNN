---
layout: default
title: Insulin Lispro
parent: Kun modelforudsigelse (L5)
nav_order: 443
evidence_level: L5
indication_count: 9
monitor_inn: "INSULIN LISPRO"
predicted_indications: ["autoimmune oophoritis", "thiamine-responsive dysfunction syndrome", "classic stiff person syndrome", "focal stiff limb syndrome", "opsismodysplasia", "drug-induced localized lipodystrophy", "pancreatic agenesis", "centrifugal lipodystrophy", "pressure-induced localized lipoatrophy"]
last_modified_at: 2026-10-30
description: "Insulin Lispro: forudsagt ny indikation Autoimmun oophoritis (evidensniveau L5). Oprindelig indikation: Type 1- og type 2-diabetes mellitus samt diabetisk ketoacidose"
---

# Insulin Lispro
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

## Insulin lispro: Fra diabetes mellitus til autoimmun oophoritis
{: .text-alpha }

## Resumé i én sætning

Insulin lispro er et hurtigtvirkende insulinanalog, der oprindeligt anvendes til behandling af diabetes mellitus (type 1 og type 2). TxGNN-modellen forudsiger, at det kan have effekt ved **autoimmun oophoritis**, men der er **ingen kliniske forsøg og ingen publikationer** i de indsamlede data, som understøtter denne retning. Forudsigelsen er udelukkende beregningsbaseret.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Type 1- og type 2-diabetes mellitus samt diabetisk ketoacidose (relationer registreret i vidensgrafen; teksten for den danske godkendelse er ikke tilgængelig) |
| Forudsagt ny indikation | Autoimmun oophoritis |
| TxGNN-forudsigelsesscore | 0,9978 |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført (gyldige tilladelser: 1 af 1) |
| Antal markedsføringstilladelser | 1 (gyldige: 1) |
| Antal godkendelser | 1 national markedsføringstilladelse |
| Anbefalet beslutning | Hold |

---

## Hvorfor er denne forudsigelse (ikke) rimelig?

Der er på nuværende tidspunkt ikke tilgængelige detaljerede data om virkningsmekanismen. Ud fra kendt viden er insulin lispro et insulinanalog, hvis effekt på blodsukkerreguleringen ved diabetes er veletableret.

Den eneste mulige kobling i de foreliggende data er, at autoimmun oophoritis ofte optræder sammen med autoimmune polyendokrine syndromer, som også omfatter type 1-diabetes. Det afspejler en fælles sygdomskontekst og ikke en terapeutisk effekt af insulin lispro på autoimmunitet i æggestokkene. Den høje score bør derfor ikke tolkes som klinisk støtte.

**Øvrige forudsigelser i listen** (alle uden kliniske data, medmindre andet er nævnt):

| Rang | Sygdom | Score | Vurdering |
|---|---|---|---|
| 2 | Thiaminresponsivt dysfunktionssyndrom | 0,9937 | Insulin kan kun behandle den diabetiske komponent, ikke den underliggende defekt (SLC19A2) |
| 3 | Klassisk stiff person-syndrom | 0,9936 | Sandsynligvis drevet af komorbiditet med type 1-diabetes og anti-GAD-autoimmunitet |
| 4 | Fokalt stiff limb-syndrom | 0,9936 | Identisk score som rang 3; scoren kommer fra TxGNN-modellen (deep learning) og kan afspejle ligheder, modellen har lært mellem beslægtede sygdomme, ikke biologisk evidens |
| 5 | Opsismodysplasi | 0,9934 | Spekulativ forbindelse via INPPL1/SHIP2 i insulinsignalering |
| 6 | Lægemiddelinduceret lokaliseret lipodystrofi | 0,9909 | Sandsynligt falsk positivt signal, da insulin selv kan forårsage tilstanden |
| 7 | Pancreasagenesi | 0,9909 | Insulinerstatning er rationel, men overlapper med den kendte diabetesindikation |
| 8 | Centrifugal lipodystrofi | 0,9904 | Insulin kan højst håndtere hyperglykæmi, ikke lipodystrofien |
| 9 | Trykinduceret lokaliseret lipoatrofi | 0,9903 | Ingen støttende mekanisme og en potentiel sikkerhedsbekymring |

---

## Klinisk evidens

Der er for øjeblikket ingen relaterede kliniske forsøg registreret for autoimmun oophoritis.

---

## Litteraturevidens

Der er for øjeblikket ingen relateret litteratur for autoimmun oophoritis.

Til orientering er der for rang 7 (pancreasagenesi) fundet én artikel, som ikke omhandler den forudsagte sygdom direkte:

| PMID | År | Type | Tidsskrift | Hovedfund |
|------|-----|------|------|---------|
| [12150359](https://pubmed.ncbi.nlm.nih.gov/12150359/) | 2002 | Review | Journal of the American Pharmaceutical Association | Gennemgang af insulinbehandling ved type 2-diabetes og praktisk opstart; behandler ikke pancreasagenesi |

---

## Information om det danske marked

| Markedsføringstilladelse | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28101706394 | Humalog | Injektionsvæske | Indikationstekst ikke tilgængelig i de indsamlede data |

Antal godkendelser: 1 national tilladelse (enkeltstofpræparat), gyldig.

---

## Sikkerhedsovervejelser

**Lægemiddelinteraktioner** (100 registrerede interaktioner; et udvalg af de vigtigste nævnes):
- **Moderat:** fenylefrin, acebutolol, acetazolamid, formoterol, pseudoefedrin, doxycyclin, adrenalin, levonorgestrel, hydrokortison, albiglutid, salbutamol, ethanol, hydrochlorthiazid, alogliptin, metformin, østradiol, alpelisib, ethinylestradiol
- **Let:** topisk hydrokortison, topisk alclometason

Generelt kan flere af disse stoffer påvirke blodsukkeret og dermed insulinbehovet.

For øvrig sikkerhedsinformation (advarsler og kontraindikationer) henvises til det godkendte produktresumé (SmPC). Flere af de forudsagte indikationer vedrører desuden lipodystrofi, hvor injektionsstedsrelateret lipodystrofi er en kendt bivirkning ved insulin; det udgør en potentiel sikkerhedsbekymring.

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelsen om autoimmun oophoritis bygger udelukkende på en beregningsmæssig score uden kliniske forsøg eller publikationer, og den mulige kobling skyldes sandsynligvis fælles sygdomskontekst (autoimmune polyendokrine syndromer) snarere end en terapeutisk mekanisme. Evidensniveauet er L5.

**For at komme videre er følgende nødvendigt:**
- Data om virkningsmekanisme, der kan belyse en eventuel biologisk kobling til autoimmun oophoritis
- Litteratursøgning og prækliniske eller kliniske data, der direkte undersøger insulin lispro ved autoimmun oophoritis
- Gennemgang af godkendelsesteksten og produktresuméet for Humalog (advarsler og kontraindikationer)
- Vurdering af, om signalerne for lipodystrofi og diabetesrelaterede tilstande er falsk positive eller blot overlapper med den kendte diabetesindikation
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

