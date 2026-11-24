---
layout: default
title: Sucralfate
parent: Høj evidens (L1-L2)
nav_order: 776
evidence_level: L2
indication_count: 2
last_modified_at: 2026-11-24
description: "Sucralfate: forudsagt ny indikation Duodenogastrisk refluks (evidensniveau L2). Oprindelig indikation: Duodenalsår"
monitor_inn: "sucralfate"
predicted_indications: ["duodenogastric reflux", "duodenal obstruction"]
---

# Sucralfate
{: .fs-9 }

Evidensniveau: **L2** | Forudsagte indikationer: **2** stk.
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

## Sucralfat: Fra duodenalsår til duodenogastrisk refluks
{: .text-alpha }

## Resumé i én sætning

Sucralfat er et mavebeskyttende lægemiddel, som oprindeligt bruges til behandling af duodenalsår.
TxGNN-modellen forudsiger, at det kan have effekt på **duodenogastrisk refluks** (tilbageløb af galde og tarmindhold til mavesækken).
Der er **ingen registrerede kliniske forsøg**, men **10 publikationer** (heriblandt 2 randomiserede forsøg) peger i denne retning.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Duodenalsår (ifølge den viden, der er brugt i modellen; indikationsteksten i den danske registrering er tom) |
| Forudsagt ny indikation | Duodenogastrisk refluks |
| TxGNN-forudsigelsesscore | 0,9937 |
| Evidensniveau | L2 |
| Markedsstatus i Danmark | Markedsført (gyldige tilladelser: 3 af 3) |
| Antal markedsføringstilladelser | 3 (gyldige: 3) |
| Anbefalet beslutning | Proceed with Guardrails (fortsæt med sikkerhedsforanstaltninger) |

---

## Hvorfor er denne forudsigelse rimelig?

Ifølge afsnittet »Clinical Pharmacology« i den produktinformation, som den amerikanske FDA har godkendt (Prescribing Information), for Sucralfate (uofficiel oversættelse): »Selvom mekanismen bag sucralfats evne til at fremskynde helingen af duodenalsår endnu ikke er fuldt klarlagt, vides det, at det udøver sin virkning gennem en lokal snarere end systemisk virkning. Følgende observationer synes også relevante: 1.« Engelsk originaltekst: "Although the mechanism of sucralfate's ability to accelerate healing of duodenal ulcers remains to be fully defined, it is known that it exerts its effect through a local, rather than systemic, action. The following observations also appear pertinent: 1." ([DailyMed: Sucralfate Oral Suspension (sucralfate) prescribing information, Glenmark Pharmaceuticals Inc., USA](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=1e595c2a-edd0-43f7-a2db-69553b9557d9), version af 2026-01-06; hentet 2026-11-19). Ud fra almen viden danner sucralfat en beskyttende, klæbende barriere over beskadiget slimhinde i mave og spiserør og binder galdesyrer og pepsin.

Ved alkalisk (galde-)refluksgastritis og -øsofagitis skyldes slimhindeskaden tilbagestrømmet galde og bugspytkirtelsekret og ikke kun mavesyre. Derfor er en slimhindebeskyttende og galdebindende effekt biologisk plausibel, og den høje TxGNN-score er i overensstemmelse hermed.

Bemærk, at koblingen bygger på sucralfats kendte egenskaber og ikke på en registreret mekanismepost. Modellen forudsagde også **duodenal obstruktion** (score 0,9930), men her er der ingen troværdig mekanistisk kobling. Sucralfat kan ikke afhjælpe en mekanisk forsnævring, og scoren stammer fra TxGNN-modellen (deep learning) og afspejler muligvis ligheder, som modellen har lært mellem beslægtede sygdomme, ikke biologisk evidens. Denne forudsigelse (evidensniveau L5) anbefales sat på pause (Hold) og behandles ikke videre i rapporten.

---

## Evidens fra kliniske forsøg

Der er i øjeblikket ingen relaterede kliniske forsøg registreret.

---

## Evidens fra litteraturen

| PMID | År | Type | Tidsskrift | Hovedfund |
|------|-----|------|------|---------|
| [3839973](https://pubmed.ncbi.nlm.nih.gov/3839973/) | 1985 | RCT | Am J Med | Dobbeltblindet forsøg med 23 patienter med symptomer på alkalisk refluksgastritis efter mavekirurgi; sucralfat 6 g/dag mod placebo i 6 uger, derefter 6 ugers åben sucralfat |
| [12923369](https://pubmed.ncbi.nlm.nih.gov/12923369/) | 2003 | RCT | Eur J Gastroenterol Hepatol | Sucralfat sammenlignet med rabeprazol eller ingen behandling ved alkalisk reaktiv gastritis efter galdeblæreoperation |
| [1391144](https://pubmed.ncbi.nlm.nih.gov/1391144/) | 1992 | Klinisk studie | Minerva Gastroenterol Dietol | 18 patienter med dyspepsi ved duodenogastrisk refluksgastritis; cisaprid (prokinetikum) mod sucralfat (4 g/dag) i 2 måneder |
| [3616071](https://pubmed.ncbi.nlm.nih.gov/3616071/) | 1987 | Kohorte | Rev Esp Enferm Apar Dig | 50 tilfælde af gastritis efter galdereflukspostoperativt behandlet med sucralfat |
| [3475771](https://pubmed.ncbi.nlm.nih.gov/3475771/) | 1987 | Randomiseret forsøg/oversigt | Scand J Gastroenterol Suppl | Sucralfat mod placebo ved gastritis med sammenligning af gastroøsofageal og duodenogastrisk refluks |
| [14723838](https://pubmed.ncbi.nlm.nih.gov/14723838/) | 2004 | Review | Curr Treat Options Gastroenterol | Duodenogastrisk refluks-induceret øsofagitis; protonpumpehæmmere er bedste medicinske behandling |
| [6372664](https://pubmed.ncbi.nlm.nih.gov/6372664/) | 1984 | Review | Annu Rev Med | Alkalisk refluksgastritis og -øsofagitis: symptomer, patofysiologi og behandling |
| [12836018](https://pubmed.ncbi.nlm.nih.gov/12836018/) | 2003 | Kohorte | Eur J Pediatr | Primær duodenogastrisk refluks hos 6 børn og unge med atypiske refluxsymptomer |
| [3838414](https://pubmed.ncbi.nlm.nih.gov/3838414/) | 1985 | Oversigt | Am J Gastroenterol | Sucralfats anvendelse uden for sårsygdom er lovende, men ikke klart fastlagt |
| [10228771](https://pubmed.ncbi.nlm.nih.gov/10228771/) | 1999 | Kirurgisk serie | Hepatogastroenterology | Duodenal switch-operation ved patologisk duodenogastrisk refluks (ikke lægemiddelrelateret) |

---

## Oplysninger om det danske marked

<!-- licenses:begin -->

| Markedsføringstilladelsesnummer | Produktnavn | Lægemiddelform | Aktive stoffer | Status |
|---------|------|------|------|------|
| 28101167883 | Antepsin | tabletter | SUCRALFAT | Gyldig |
| 28106661021 | Antepsin | tabletter | SUCRALFAT | Gyldig |
| 28106740522 | Peptonorm | tabletter | SUCRALFAT | Gyldig |

Tabellen viser alle 3 markedsføringstilladelser til humane lægemidler med dette aktive stof i Lægemiddelstyrelsens lister over godkendte og afregistrerede lægemidler; gyldige tilladelser står først.

<!-- licenses:end -->

---

## Sikkerhedsovervejelser

- **Kontraindikationer ifølge vidensgrafen (ikke produktresuméets tekst):** hyperglykæmi, kronisk nyresygdom, kronisk nyresvigt og terminal nyresvigt.
- **Lægemiddelinteraktioner:** 549 interaktioner er registreret. Blandt de viste er de vigtigste:
  - **Alvorlige (Major):** dolutegravir, bictegravir.
  - **Moderate:** bl.a. doxycyclin, tetracyclin, alendronsyre, risedronsyre, ibandronat, pioglitazon, acarbose, alogliptin, albiglutid, allopurinol, askorbinsyre, baloxegavir marboxil og calcifediol.
  - **Milde (Minor):** bl.a. acebutolol, atenolol, betaxolol, bisoprolol og anagrelid.

Se i øvrigt det godkendte produktresumé (SmPC) for fuldstændige oplysninger om advarsler og kontraindikationer.

---

## Konklusion og næste skridt

**Beslutning: Proceed with Guardrails**

**Begrundelse:**
To randomiserede forsøg (1985 og 2003) og flere mindre studier undersøger sucralfat ved alkalisk refluksgastritis, og mekanismen er plausibel. Forsøgene er dog små, gamle og ikke registrerede kliniske forsøg, og et enkelt review peger på protonpumpehæmmere som bedste behandling. Evidensen er derfor lovende, men ikke afgørende.

**For at komme videre kræves:**
- Data om virkningsmekanismen (MOA) fra DrugBank
- Advarsler og kontraindikationer fra det danske produktresumé (manglende, blokerende datahul for sikkerhedsvurdering)
- Det godkendte indikationsområde for Antepsin i Danmark
- Et moderne, velkontrolleret forsøg, der sammenligner sucralfat med protonpumpehæmmere
- Særlig forsigtighed hos patienter med nedsat nyrefunktion og ved samtidig brug af lægemidler med relevante interaktioner (fx dolutegravir, bictegravir, tetracykliner og bisfosfonater)

<!-- review:begin log -->

## Gennemgangslog

Nedenfor er gennemgangsloggen for denne side. Sætningen om, at data om virkningsmekanismen ikke var tilgængelige, er erstattet med et uddrag fra den angivne officielle produktinformation (med uofficiel oversættelse); modelforudsigelser, evidensniveauer og konklusioner er ikke omskrevet.

| Gennemgået | Punkt | Handling | Kilde |
|------|------|------|------|
| 2026-11-19 | Sætningen »data om virkningsmekanismen er ikke tilgængelige« erstattet med uddrag fra den amerikanske produktinformation | Sætning om manglende data om virkningsmekanismen erstattet med et uddrag med kilde | [DailyMed: Sucralfate Oral Suspension (sucralfate) prescribing information, Glenmark Pharmaceuticals Inc., USA](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=1e595c2a-edd0-43f7-a2db-69553b9557d9) |

<!-- review:end log -->

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

