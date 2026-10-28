---
layout: default
title: Clozapine
parent: Kun modelforudsigelse (L5)
nav_order: 215
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Clozapine: forudsagt ny indikation Manisk bipolar lidelse (evidensniveau L2). Oprindelig indikation: Ikke oplyst i de sammenstillede data (den danske tilladelse har ingen…"
monitor_inn: "clozapine"
predicted_indications: ["manic bipolar affective disorder", "Tourette syndrome", "trichotillomania", "schizophreniform disorder", "bipolar disorder", "major affective disorder", "attention deficit-hyperactivity disorder", "attention deficit hyperactivity disorder, inattentive type", "psychotic disorder", "Malan overgrowth syndrome"]
---

# Clozapine
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

## Clozapin: Fra behandlingsresistent skizofreni til manisk bipolar lidelse
{: .text-alpha }

## Resumé

Clozapin er et atypisk antipsykotikum, som er markedsført i Danmark som tabletter. Det er kendt til behandling af psykotiske lidelser, men indikationsteksten i den danske registrering er ikke tilgængelig i de data, der er sammenstillet til denne rapport.
TxGNN-modellen forudsiger, at clozapin kan være effektivt ved **manisk bipolar lidelse**, og der er **1 klinisk forsøg** og **21 publikationer** for denne konkrete indikation (heriklusive en metaanalyse fra 2020).

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Ikke oplyst i de sammenstillede data (den danske tilladelse har ingen indikationstekst) |
| Forudsagt ny indikation | Manisk bipolar lidelse |
| TxGNN-forudsigelsesscore | 0,9995 |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført (gyldige tilladelser: 1 af 1) |
| Antal markedsføringstilladelser | 1 (gyldige: 1) |
| Anbefalet beslutning | Proceed with Guardrails (fortsæt med sikkerhedsforanstaltninger) |

---

## Hvorfor er denne forudsigelse rimelig?

Data om clozapins virkningsmekanisme er ikke tilgængelige i de sammenstillede oplysninger. Ud fra almen farmakologi har clozapin en bred receptorprofil med antagonisme på D2/D4-, 5-HT2A-, muskarine, alfa-adrenerge og histaminerge receptorer. Denne profil kan bidrage til en antimanisk og stemningsstabiliserende effekt ved behandlingsresistent mani.

Clozapin anvendes i praksis til behandlingsresistente psykotiske lidelser, og bipolar lidelse med mani deler symptomer og dele af den underliggende dopaminerge dysfunktion med dem. En systematisk oversigt og metaanalyse fra 2020 samt flere oversigtsartikler om behandlingsresistent bipolar lidelse understøtter anvendelsen.

Bemærk, at den foreliggende evidens for manisk bipolar lidelse består af ét lille fase 2-forsøg (42 deltagere). Evidensen er derfor mere begrænset end for den bredere diagnose "bipolar lidelse" (se nedenfor).

---

## Evidens fra kliniske forsøg

| Forsøgsnummer | Fase | Status | Deltagere | Hovedpunkter |
|---------|------|------|------|---------|
| [NCT00029458](https://clinicaltrials.gov/study/NCT00029458) | Fase 2 | Afsluttet | 42 | Dobbeltblindt forsøg med clozapins sikkerhed og effekt ved behandlingsresistent mani; resultater er ikke angivet i data |

**Supplerende evidens for den bredere diagnose bipolar lidelse** (rang 5 i forudsigelserne, TxGNN-score 0,9962, evidensniveau L1):

| Forsøgsnummer | Fase | Status | Deltagere | Hovedpunkter |
|---------|------|------|------|---------|
| [NCT00036582](https://clinicaltrials.gov/study/NCT00036582) | Fase 3 | Afsluttet | 116 | Clozapin vs. placebo ved behandlingsrefraktær bipolar lidelse hos børn og unge; resultater ikke angivet |
| [NCT02562287](https://clinicaltrials.gov/study/NCT02562287) | Fase 4 | Ukendt | 54 | Randomiseret sammenligning af clozapin med olanzapin, quetiapin eller risperidon ved behandlingsresistent bipolar lidelse |
| [NCT05603104](https://clinicaltrials.gov/study/NCT05603104) | Fase 3 | Rekrutterer | 1254 | Intensiveret farmakologisk behandling efter første behandlingssvigt ved skizofreni, depression og bipolar depression; resultater afventes |
| [NCT06011460](https://clinicaltrials.gov/study/NCT06011460) | Ikke angivet | Optager efter invitation | 30 | Register over bivirkninger ved clozapin ved bipolar lidelse |
| [NCT04580134](https://clinicaltrials.gov/study/NCT04580134) | Fase 4 | Rekrutterer | 524 | Clozapinrespons ved B-SNIP biotype 1-psykose; biomarkørorienteret, delvis relevans for bipolar lidelse |

---

## Litteraturevidens

| PMID | År | Type | Tidsskrift | Hovedpunkter |
|------|-----|------|------|---------|
| [32182485](https://pubmed.ncbi.nlm.nih.gov/32182485/) | 2020 | Metaanalyse | J Psychiatr Res | Systematisk oversigt og metaanalyse af clozapins effekt og bivirkninger ved bipolar lidelse |
| [41192460](https://pubmed.ncbi.nlm.nih.gov/41192460/) | 2025 | Kohorte | Lancet Psychiatry | Transdiagnostisk effekt og sikkerhed af clozapin sammenlignet med andre antipsykotika |
| [25346322](https://pubmed.ncbi.nlm.nih.gov/25346322/) | 2015 | Systematisk oversigt | Bipolar Disord | Effekt og sikkerhed af clozapin ved behandlingsresistent bipolar lidelse |
| [16432528](https://pubmed.ncbi.nlm.nih.gov/16432528/) | 2006 | Oversigtsartikel | Mol Psychiatry | Behandlingsresistent bipolar lidelse |
| [11280956](https://pubmed.ncbi.nlm.nih.gov/11280956/) | 2001 | Oversigtsartikel | Bull Menninger Clin | Behandlingsresistent bipolar lidelse; nyere behandlinger bygger mest på case-rapporter |
| [33460070](https://pubmed.ncbi.nlm.nih.gov/33460070/) | 2020 | Oversigtsartikel | Acta Psychiatr Scand | Evidensbaserede behandlingsmuligheder ved mani |
| [10682225](https://pubmed.ncbi.nlm.nih.gov/10682225/) | 2000 | Oversigtsartikel | Clin Neuropharmacol | 36 patienter behandlet med ECT og clozapin; 67 % havde gavn, bivirkninger hos 16,6 % |
| [41262335](https://pubmed.ncbi.nlm.nih.gov/41262335/) | 2025 | Ikke klassificeret | Drug Des Devel Ther | Lægemiddelinteraktioner og individualiseret dosering af clozapin ved bipolar lidelse |
| [33719158](https://pubmed.ncbi.nlm.nih.gov/33719158/) | 2021 | Ikke klassificeret | Bipolar Disord | Clozapin ved bipolar lidelse: hvad ved vi, og hvad nu? |

---

## Oplysninger om det danske marked

| Tilladelsesnummer | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28106883122 | Cloprinex (Nordic Prime ApS) | Tabletter | Indikationstekst ikke angivet |

---

## Sikkerhedsovervejelser

**Kontraindikationer/sygdomme, hvor clozapin er markeret som problematisk i vidensgrafen (TxGNN/PrimeKG, ikke produktresumé):** epilepsi, leversygdom, galdeblæresygdom, neutropeni, agranulocytose, leukopeni, hyperglykæmi, diabetes mellitus, diabetisk ketoacidose, hyperlipidæmi, koronar hjertesygdom, fedme, slagtilfælde og cerebrovaskulær sygdom, lungeemboli, pludseligt hjertestop, hjerteledningsforstyrrelser, ortostatisk hypotension, hypotension, respirationssvigt, snævervinklet glaukom, benign prostatahyperplasi, paralytisk ileus, multipel systematrofi og postural ortostatisk takykardisyndrom.

**Lægemiddelinteraktioner:** Der er registreret 468 interaktioner. Blandt de viste er følgende af alvorlig grad (Major): bupropion, morfin og kaliumcitrat. Moderate interaktioner omfatter bl.a. metformin, pioglitazon, acarbose, omeprazol, cimetidin, famotidin, atropin, glycopyrronium, hyoscyamin, loperamid og epinephrin.

**Supplerende sikkerhedsemner fra litteraturen:** agranulocytose, myokarditis, krampeanfald og metabolisk belastning (vægtøgning, diabetes). Se også produktresuméet for de gældende krav til blodprøvekontrol.

---

## Konklusion og næste skridt

**Beslutning: Proceed with Guardrails**

**Begrundelse:**
Der er et afsluttet fase 2-forsøg samt en metaanalyse fra 2020, der understøtter brug ved behandlingsresistent mani, og for den bredere diagnose bipolar lidelse findes også et afsluttet fase 3-forsøg (resultater ikke tilgængelige). Evidensen er dog begrænset i omfang, og clozapins alvorlige risici kræver tæt overvågning.

**For at komme videre kræves:**
- Hentning af produktresuméet fra Lægemiddelstyrelsen (advarsler, kontraindikationer og godkendt indikation mangler i de sammenstillede data)
- Oplysninger om virkningsmekanisme fra DrugBank
- Resultater fra NCT00029458 og NCT00036582 samt gennemgang af metaanalysen fra 2020
- Plan for hæmatologisk overvågning (agranulocytose/neutropeni), hjertemonitorering (myokarditis), vurdering af krampetærskel og metabolisk kontrol
- Vurdering af interaktioner med patientens øvrige medicin

---

## Andre forudsagte indikationer (kort overblik)

| Forudsagt indikation | TxGNN-score | Evidensniveau | Anbefaling |
|------|------|------|------|
| Tourettes syndrom | 0,9991 | L4 | Hold (kun case-rapporter, ingen forsøg) |
| Trikotillomani | 0,9990 | L5 | Hold |
| Skizofreniform lidelse | 0,9969 | L3 | Proceed with Guardrails |
| Bipolar lidelse | 0,9962 | L1 | Proceed with Guardrails |
| Større affektiv lidelse | 0,9948 | L2 | Proceed with Guardrails |
| ADHD | 0,9931 | L4 | Hold |
| ADHD, uopmærksom type | 0,9921 | L5 | Hold |
| Psykotisk lidelse | 0,9912 | L1 | Proceed with Guardrails (reelt allerede etableret anvendelse) |
| Malan overvækstsyndrom | 0,9902 | L5 | Hold |
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

