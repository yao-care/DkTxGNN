---
layout: default
title: Glucagon
parent: Kun modelforudsigelse (L5)
nav_order: 210
evidence_level: L5
indication_count: 2
---

# Glucagon
{: .fs-9 }

Evidensniveau: **L5** | Forudsagte indikationer: **2** stk.
{: .fs-6 .fw-300 }

---

## Indholdsfortegnelse
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Farmaceutens vurderingsrapport

</div>

# Glucagon: Fra godkendt anvendelse til irritabel tarm-syndrom

## Resumé

Glucagon er et peptidhormon, som i Danmark er markedsført som Baqsimi (næsepulver i enkeltdosisbeholder). Godkendelsesteksten for den oprindelige indikation indgår ikke i datagrundlaget.
TxGNN-modellen forudsiger, at glucagon kan være virksomt ved **irritabel tarm-syndrom (IBS)**, men der findes **ingen kliniske studier af glucagon selv** ved IBS.
Det kliniske signal stammer fra GLP-1-receptoragonister (ROSE-010, liraglutid), og der er **1 klinisk studie (fase 1/2) med direkte IBS-relevans** samt **1 systematisk oversigtsartikel** om GLP-1-agonister ved IBS.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Ikke angivet i datagrundlaget |
| Forudsagt ny indikation | Irritabel tarm-syndrom (IBS) |
| TxGNN-forudsigelsesscore | 99,24 % |
| Evidensniveau | L4 (præklinisk/mekanistisk evidens og studier af beslægtede stoffer; ingen glucagon-studier) |
| Markedsstatus i Danmark | Markedsført |
| Antal markedsføringstilladelser | 1 |
| Anbefalet beslutning | Hold |

*Note: Inputtet indeholdt to identiske IBS-poster, som er slået sammen til én.*

---

## Hvorfor er forudsigelsen rimelig?

Der foreligger på nuværende tidspunkt ikke detaljerede data om glucagons virkningsmekanisme i datagrundlaget. Glucagon og GLP-1 er begge afledt af proglucagon. Glucagon afslapper desuden glat muskulatur i mave-tarmkanalen og bruges i den forbindelse som spasmolytikum ved radiologisk undersøgelse. Det er biologisk plausibelt i forhold til IBS-symptomer som smerte og motilitetsforstyrrelser.

Den kliniske retning understøttes primært af GLP-1-receptoragonister. GLP-1 og analogen ROSE-010 hæmmer det migrerende motoriske kompleks og nedsætter tarmmotiliteten. ROSE-010 har vist lovende smertelindring under IBS-anfald. Koblingen til glucagon er derfor **indirekte**.

Den høje TxGNN-score er en modelforudsigelse og dokumenterer ikke effekt. Glucagons markedsførte status og kendte sikkerhedsprofil kan understøtte en indledende sikkerhedsvurdering, men ikke effekt ved IBS.

---

## Klinisk evidens fra studier

Der er søgt 11 studier. De fleste er kun løst relateret via søgeord (kost, mikrobiota, motion mv.) og ingen undersøger glucagon. Nedenfor er de seks mest relevante vist; de øvrige fem er udeladt, fordi de ikke har relevans for glucagon eller IBS-behandling (NCT04111263, NCT06333717, NCT06113146, NCT04230655, NCT00802971).

| Studienummer | Fase | Status | Antal deltagere | Hovedpunkter |
|---------|------|------|------|---------|
| [NCT01056107](https://clinicaltrials.gov/study/NCT01056107) | Fase 1/2 | Afsluttet | 52 | ROSE-010 (GLP-1-analog) og mave-tarm-motilitet hos kvinder med IBS med forstoppelse. Mest sygdomsspecifikke studie, men stoffet er ikke glucagon. |
| [NCT02731664](https://clinicaltrials.gov/study/NCT02731664) | Fase 1 | Afsluttet | 12 | Nativ GLP-1 versus ROSE-010: hæmning af motilitet i mavesæk, duodenum og jejunum. Understøtter mekanismen, men ikke IBS-population. |
| [NCT04763564](https://clinicaltrials.gov/study/NCT04763564) | Fase 2 | Afbrudt | 8 | Liraglutid ved ileal pouch-analanastomose og hyppig afføring. Afbrudt tidligt, ringe evidensvægt, ikke IBS. |
| [NCT06408610](https://clinicaltrials.gov/study/NCT06408610) | Ikke relevant (NA) | Afsluttet | 66 | Træningsintervention og GLP-1 som målt udfald hos patienter med IBS. GLP-1 er ikke intervention. |
| [NCT05249023](https://clinicaltrials.gov/study/NCT05249023) | Ikke relevant (NA) | Afsluttet | 37 | Butyrats virkning i human tyktarm. Kun løs kobling til IBS. |
| [NCT03256266](https://clinicaltrials.gov/study/NCT03256266) | Ikke relevant (N/A) | Aktiv, rekrutterer ikke | 375 | Organoider fra tyndtarm og næringsantigener. Ingen glucagon- eller IBS-behandlingsdata. |

---

## Litteraturevidens

| PMID | År | Type | Tidsskrift | Hovedpunkter |
|------|-----|------|------|---------|
| [40134805](https://pubmed.ncbi.nlm.nih.gov/40134805/) | 2025 | Systematisk oversigt og meta-analyse | Front Endocrinol | GLP-1-agonister ved IBS. GLP-1 og ROSE-010 hæmmer det migrerende motoriske kompleks og nedsætter tarmmotiliteten hos IBS-patienter. |
| [35234561](https://pubmed.ncbi.nlm.nih.gov/35234561/) | 2022 | Post hoc-analyse af RCT | Scand J Gastroenterol | ROSE-010 reducerede smerte under IBS-anfald. Krydsanalyse for at identificere den bedst egnede undergruppe. |
| [30444291](https://pubmed.ncbi.nlm.nih.gov/30444291/) | 2019 | Oversigtsartikel | Exp Physiol | GLP-1-udskillende L-celler og deres mulige rolle i IBS-patofysiologi. |
| [25427821](https://pubmed.ncbi.nlm.nih.gov/25427821/) | 2015 | Oversigtsartikel | Adv Exp Med Biol | Aerosoliseret GLP-1 til behandling af diabetes og IBS. |
| [26765585](https://pubmed.ncbi.nlm.nih.gov/26765585/) | 2016 | Oversigtsartikel | Expert Opin Investig Drugs | Nye lægemidler under udvikling til IBS med forstoppelse. |
| [21694813](https://pubmed.ncbi.nlm.nih.gov/21694813/) | 2011 | Oversigtsartikel | Ther Adv Gastroenterol | IBS-behandling ud over fibre og spasmolytika. |
| [40697433](https://pubmed.ncbi.nlm.nih.gov/40697433/) | 2025 | Kohortestudie | Ann Gastroenterol | Mønstre for ordination og seponering af GLP-1-agonister hos IBS-patienter (bivirkninger i mave-tarmkanalen). |
| [28215540](https://pubmed.ncbi.nlm.nih.gov/28215540/) | 2017 | Patientstudie (ikke klassificeret) | Clin Res Hepatol Gastroenterol | Lavere serum-GLP-1 hænger sammen med mavesmerter ved IBS med forstoppelse. |
| [31602785](https://pubmed.ncbi.nlm.nih.gov/31602785/) | 2020 | Dyreforsøg | Neurogastroenterol Motil | GLP-1-agonisten exendin-4 forbedrede mave-tarm-dysfunktion i en rottemodel for IBS. |
| [31311066](https://pubmed.ncbi.nlm.nih.gov/31311066/) | 2019 | Dyreforsøg | Neurogastroenterol Motil | Ghrelin-agonist sensibiliserer neuroner i rottetyktarm over for exendin-4. |

---

## Information om markedet i Danmark

| Markedsføringstilladelse | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28106149818 | Baqsimi | Nasal pulver i enkeltdosisbeholder | Ikke angivet i datagrundlaget |

Producent: Amphastar France Pharmaceuticals Usine Saint-Charles.

---

## Sikkerhedsovervejelser

Se det godkendte produktresumé (SmPC) fra Lægemiddelstyrelsen for sikkerhedsoplysninger.

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Der findes ingen kliniske studier af glucagon ved IBS. Den kliniske støtte stammer fra GLP-1-receptoragonister, og koblingen til glucagon er indirekte. Den høje TxGNN-score er en ren modelforudsigelse. Sagen bør behandles som et forskningsspørgsmål (evidensniveau L4).

**For at komme videre kræves:**
- Produktresumé fra Lægemiddelstyrelsen med advarsler og kontraindikationer (blokerende for sikkerhedsscreening)
- Data om virkningsmekanisme fra DrugBank til at vurdere den mekanistiske kobling
- Godkendt indikationstekst for Baqsimi
- Præklinisk eller klinisk evidens for glucagon selv ved IBS, herunder en vurdering af, om administrationsvejen (næsepulver) er egnet til IBS

*Resultaterne er alene til forskningsbrug og udgør ikke medicinsk rådgivning. Lægemiddelkandidater til nye anvendelser kræver klinisk validering, før de kan anvendes.*
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

