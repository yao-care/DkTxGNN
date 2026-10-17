---
layout: default
title: Sucralfate
parent: Høj evidens (L1-L2)
nav_order: 776
evidence_level: L2
indication_count: 2
last_modified_at: 2026-10-14
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

# Sucralfat: Fra duodenalsår til duodenogastrisk refluks

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
| TxGNN-forudsigelsesscore | 99,37 % |
| Evidensniveau | L2 |
| Markedsstatus i Danmark | Markedsført |
| Antal markedsføringstilladelser | 1 |
| Anbefalet beslutning | Proceed with Guardrails (fortsæt med sikkerhedsforanstaltninger) |

---

## Hvorfor er denne forudsigelse rimelig?

Der foreligger ikke i øjeblikket detaljerede data om virkningsmekanismen i de data, der er indsamlet til denne rapport. Ud fra almen viden danner sucralfat en beskyttende, klæbende barriere over beskadiget slimhinde i mave og spiserør og binder galdesyrer og pepsin.

Ved alkalisk (galde-)refluksgastritis og -øsofagitis skyldes slimhindeskaden tilbagestrømmet galde og bugspytkirtelsekret og ikke kun mavesyre. Derfor er en slimhindebeskyttende og galdebindende effekt biologisk plausibel, og den høje TxGNN-score er i overensstemmelse hermed.

Bemærk, at koblingen bygger på sucralfats kendte egenskaber og ikke på en registreret mekanismepost. Modellen forudsagde også **duodenal obstruktion** (score 99,30 %), men her er der ingen troværdig mekanistisk kobling. Sucralfat kan ikke afhjælpe en mekanisk forsnævring, og scoren afspejler sandsynligvis nærheden til duodenalsår i vidensgrafen. Denne forudsigelse (evidensniveau L5) anbefales sat på pause (Hold) og behandles ikke videre i rapporten.

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

| Markedsføringstilladelse | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28101167883 | Antepsin (Orion Corporation) | Tabletter | Indikationstekst er ikke angivet i registreringen |

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
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

