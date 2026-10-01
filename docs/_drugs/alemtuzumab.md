---
layout: default
title: Alemtuzumab
parent: Kun modelforudsigelse (L5)
nav_order: 22
evidence_level: L5
indication_count: 10
---

# Alemtuzumab
{: .fs-9 }

Evidensniveau: **L5** | Forudsagte indikationer: **10** stk.
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

# Alemtuzumab: Fra oprindelig indikation (ikke angivet i data) til hepatisk infarkt

## Resumé i én sætning

Alemtuzumab er et anti-CD52-antistof, som i Danmark er markedsført under navnet Lemtrada. Datapakken angiver ikke lægemidlets oprindelige indikation.
TxGNN-modellen forudsiger, at det kan have effekt ved **hepatisk infarkt** (leverinfarkt), men **der er ingen kliniske forsøg og ingen publikationer**, der understøtter denne forudsigelse. Forudsigelsen vurderes sandsynligvis at være en artefakt i vidensgrafen.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Ikke angivet i datapakken (indikationsteksten for godkendelsen er tom). Skal verificeres i produktresuméet (SmPC) |
| Forudsagt ny indikation | Hepatisk infarkt |
| TxGNN-forudsigelsesscore | 94,4 % |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført |
| Antal markedsføringstilladelser | 1 |
| Anbefalet beslutning | Hold |

---

## Hvorfor er denne forudsigelse (ikke) rimelig?

Der foreligger på nuværende tidspunkt ingen detaljerede data om virkningsmekanismen (MOA) i datapakken. Alemtuzumab er et anti-CD52-antistof, der nedbryder lymfocytter (T- og B-celler).

Hepatisk infarkt skyldes normalt iskæmi eller vaskulær okklusion i leveren. Der er ikke noget kendt biologisk led mellem lymfocytdepletion via CD52 og forebyggelse eller behandling af iskæmisk eller vaskulær leverskade. Forudsigelsen bygger udelukkende på modellens score og er ikke understøttet af kliniske eller mekanistiske data.

Den høje score skal derfor tolkes med forsigtighed. Den kan afspejle tilfældige forbindelser i vidensgrafen frem for en reel farmakologisk sammenhæng.

---

## Kliniske forsøg

Der er i øjeblikket ingen relaterede kliniske forsøg registreret for hepatisk infarkt.

---

## Litteratur

Der er i øjeblikket ingen relateret litteratur tilgængelig for hepatisk infarkt.

---

## Øvrige forudsagte indikationer

Datapakken indeholder yderligere forudsigelser. De er slået sammen, fordi hver optrådte to gange i inputtet.

| Forudsagt indikation | TxGNN-score | Evidensniveau | Anbefaling |
|------|------|------|------|
| Syndrom med kombineret immundefekt | 93,7 % | L3 | Forskningsspørgsmål |
| Hepatisk veno-okklusiv sygdom | 93,1 % | L4 | Hold |
| Sarkomatoid overgangscellekarcinom i nyrebækkenet | 93,1 % | L5 | Hold |
| Infiltrerende sarkomatoid variant af urotelialt blærekarcinom | 92,9 % | L5 | Hold |

**Syndrom med kombineret immundefekt** har den stærkeste evidens. Alemtuzumab bruges som serumterapi (lymfocytdepletion) i konditioneringsregimer med reduceret intensitet før allogen stamcelletransplantation. Det kan understøtte engraftment og reducere risikoen for graft-versus-host-sygdom. Alemtuzumab er her en hjælpebehandling, der muliggør kurativ transplantation. Det behandler ikke selve immundefekten. Der er ingen fase 3-forsøg eller randomiserede data.

**Hepatisk veno-okklusiv sygdom** er en konditioneringsrelateret komplikation efter stamcelletransplantation. Alemtuzumab indgår i de samme regimer, fx busulfan/fludarabin/alemtuzumab. Sammenhængen er derfor sandsynligvis samtidig forekomst i transplantationsprotokoller og ikke behandling eller forebyggelse. De to øvrige indikationer (urotelial og nyrebækken) er alene modelforudsigelser uden forsøg eller litteratur, og CD52 er ikke et etableret target i disse tumorer.

### Udvalgte forsøg ved kombineret immundefekt

| Forsøgsnummer | Fase | Status | Antal deltagere | Hovedpunkter |
|---------|------|------|------|---------|
| [NCT00579137](https://clinicaltrials.gov/study/NCT00579137) | Fase 1/2 | Afsluttet før tid | 3 | CD45-antistof plus alemtuzumab og fludarabin som konditionering ved SCID og andre primære immundefekter. Kun 3 patienter, så meget begrænset information om effekt |
| [NCT01182675](https://clinicaltrials.gov/study/NCT01182675) | Fase 2 | Afsluttet før tid | 7 | Stamcelletransplantation ved SCID hos børn med alemtuzumab og mobilisering med plerixafor og filgrastim, uden klassisk kemoterapi |
| [NCT05463133](https://clinicaltrials.gov/study/NCT05463133) | Fase 1/2 | Rekrutterer | 50 | Allogen transplantation ved kronisk granulomatøs sygdom med alemtuzumab-, busulfan- og TBI-baseret konditionering plus IL-6-antagonister |
| [NCT04528355](https://clinicaltrials.gov/study/NCT04528355) | Ikke relevant | Rekrutterer | 50 | Prospektivt dataindsamlingsstudie af konditionering med reduceret intensitet og alemtuzumab-dosering ved ikke-maligne sygdomme |
| [NCT01962415](https://clinicaltrials.gov/study/NCT01962415) | Fase 2 | Rekrutterer | 100 | Konditionering med reduceret intensitet før stamcelletransplantation ved ikke-maligne sygdomme. Alemtuzumabs rolle er ikke bekræftet ud fra de foreliggende oplysninger |
| [NCT01821781](https://clinicaltrials.gov/study/NCT01821781) | Fase 2 | Aktiv, rekrutterer ikke | 20 | Transplantation ved immunfunktionsforstyrrelser med reduceret intensitet. Alemtuzumabs rolle er ikke bekræftet |

### Udvalgt litteratur ved kombineret immundefekt

| PMID | År | Type | Tidsskrift | Hovedpunkter |
|------|-----|------|------|---------|
| [27543157](https://pubmed.ncbi.nlm.nih.gov/27543157/) | 2016 | Kohorte | Biol Blood Marrow Transplant | Alemtuzumab, fludarabin og melphalan (reduceret intensitet, 4 patienter) sammenlignet med myeloablativ konditionering (14 patienter) ved kronisk granulomatøs sygdom |
| [21325599](https://pubmed.ncbi.nlm.nih.gov/21325599/) | 2011 | Kohorte | Blood | Treosulfan-baseret konditionering hos 70 børn med primær immundefekt, med alemtuzumab |
| [23131490](https://pubmed.ncbi.nlm.nih.gov/23131490/) | 2013 | Survey | Blood | Transplantation ved XIAP-mangel (19 patienter). Dårlige resultater. 11 fik konditionering med reduceret intensitet, overvejende med alemtuzumab |
| [18940685](https://pubmed.ncbi.nlm.nih.gov/18940685/) | 2008 | Ikke klassificeret | Biol Blood Marrow Transplant | Alemtuzumab (Campath-1H) og fludarabin ved graftsvigt hos 12 børn efter stamcelletransplantation |
| [29155317](https://pubmed.ncbi.nlm.nih.gov/29155317/) | 2018 | Kohorte | Biol Blood Marrow Transplant | Treosulfan og fludarabin hos 160 børn med primær immundefekt |
| [15590388](https://pubmed.ncbi.nlm.nih.gov/15590388/) | 2004 | Oversigtsartikel | Haematologica | Infektiøs toksicitet ved brug af alemtuzumab |

---

## Information om markedet i Danmark

| Markedsføringstilladelsesnummer | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28105091212 | Lemtrada (Sanofi Belgium) | Koncentrat til infusionsvæske, opløsning | Ikke angivet i data |

---

## Sikkerhedsovervejelser

Der er ingen registrerede lægemiddelinteraktioner i datapakken. Læs i øvrigt det godkendte produktresumé (SmPC) for sikkerhedsoplysninger. Litteraturen peger desuden på infektionsrisiko ved alemtuzumab (se PMID 15590388 ovenfor). Alemtuzumab nedbryder lymfocytter, og det bør indgå i enhver risikovurdering.

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelsen om hepatisk infarkt bygger udelukkende på modelscoren (evidensniveau L5). Der er hverken kliniske forsøg, litteratur eller en plausibel mekanisme. Den mest støttede af de øvrige forudsigelser er kombineret immundefekt (L3), hvor alemtuzumab har en rolle som konditioneringsmiddel og ikke som direkte behandling.

**For at komme videre kræves:**
- Sikkerhedsoplysninger (advarsler og kontraindikationer) fra det danske produktresumé hos Lægemiddelstyrelsen
- Data om virkningsmekanisme (MOA) fra DrugBank
- Bekræftelse af den oprindelige godkendte indikation
- For kombineret immundefekt: bekræftelse af alemtuzumabs faktiske rolle i de enkelte transplantationsprotokoller og data fra kontrollerede studier

*Resultaterne er kun til forskningsbrug og udgør ikke lægefaglig rådgivning. Forudsigelserne kræver klinisk validering, før de kan anvendes i praksis.*
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

