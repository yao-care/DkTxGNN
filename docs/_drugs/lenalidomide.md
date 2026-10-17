---
layout: default
title: Lenalidomide
parent: Kun modelforudsigelse (L5)
nav_order: 488
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-14
description: "Lenalidomide: forudsagt ny indikation Myeloid leukæmi (evidensniveau L5). Oprindelig indikation: Plasmacellemyelom, mantlecellelymfom, B-celleneoplasi…"
monitor_inn: "lenalidomide"
predicted_indications: ["myeloid leukemia", "refractory cytopenia of childhood", "aregenerative anemia", "severe congenital hypochromic anemia with ringed sideroblasts", "partial deletion of the long arm of chromosome 5"]
---

# Lenalidomide
{: .fs-9 }

Evidensniveau: **L5** | Forudsagte indikationer: **6** stk.
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

# Lenalidomid: Fra myelomatose og myelodysplastisk syndrom til myeloid leukæmi

## Resumé i én sætning

Lenalidomid er et immunmodulerende lægemiddel, der oprindeligt anvendes til behandling af plasmacellemyelom (myelomatose), mantlecellelymfom og myelodysplastisk syndrom (MDS).
TxGNN-modellen forudsiger, at det kan have effekt ved **myeloid leukæmi**,
og der er i de indsamlede data identificeret **47 kliniske forsøg** og **19 publikationer** for denne retning. Evidensen består dog overvejende af små fase 1/2-forsøg uden randomiseret sammenligning for lenalidomid alene.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Plasmacellemyelom, mantlecellelymfom, B-celleneoplasi, lymfosarkom og myelodysplastisk syndrom (indikationsteksten i den danske autorisation er ikke angivet) |
| Forudsagt ny indikation | Myeloid leukæmi |
| TxGNN-forudsigelsesscore | 99,49 % |
| Evidensniveau | L2 (ingen afsluttede fase 3-RCT'er; afsluttede fase 2-forsøg findes, men de er hovedsageligt enkeltarmede) |
| Markedsstatus i Danmark | Markedsført |
| Antal markedsføringstilladelser | 1 |
| Anbefalet beslutning | Proceed with Guardrails |

---

## Hvorfor er forudsigelsen rimelig?

Detaljerede data om virkningsmekanismen for den oprindelige indikation er ikke tilgængelige i de data, der er indsamlet til denne rapport. Følgende bygger derfor på almen viden og ikke på de leverede data.

Lenalidomid binder cereblon (CRBN) og omdirigerer E3-ligasekomplekset CRL4-CRBN, så proteinerne IKZF1, IKZF3 og CK1alpha nedbrydes. Nedbrydningen af CK1alpha er central for responset ved MDS med del(5q). Derudover har stoffet immunmodulerende virkning (aktivering af T- og NK-celler), som kan understøtte vedligeholdelsesbehandling efter remission eller efter transplantation.

MDS og akut myeloid leukæmi (AML) er tæt beslægtede myeloide sygdomme, og en tredjedel af MDS-patienter udvikler AML. Det gør det biologisk plausibelt, at et lægemiddel, der virker ved MDS, også kan have effekt ved myeloid leukæmi. Aktiviteten ved AML uden del(5q) er dog beskeden og inkonsistent, og de fleste forsøg testede lenalidomid i kombination med anden behandling.

---

## Evidens fra kliniske forsøg

Tabellen viser de 10 mest relevante forsøg (ud af 47 identificerede). Der er ikke angivet EudraCT-numre i de indsamlede data.

| Forsøgsnummer | Fase | Status | Antal deltagere | Hovedresultater |
|---------|------|------|------|---------|
| [NCT02126553](https://clinicaltrials.gov/study/NCT02126553) | Fase 2 | Afsluttet | 29 | Lenalidomid som vedligeholdelse ved højrisiko-AML i remission; enkeltarmet og lille |
| [NCT00360672](https://clinicaltrials.gov/study/NCT00360672) | Fase 2 | Afsluttet | 27 | Lenalidomid alene ved recidiverende/refraktær AML eller højrisiko-MDS med kromosom 5-abnormiteter |
| [NCT00352365](https://clinicaltrials.gov/study/NCT00352365) | Fase 2 | Afsluttet | 41 | Lenalidomid ved ubehandlet AML med del(5q) hos patienter ≥ 60 år, der afslog induktionskemoterapi |
| [NCT00546897](https://clinicaltrials.gov/study/NCT00546897) | Fase 2 | Afsluttet | 48 | Lenalidomid hos ældre (> 60 år) med ubehandlet AML uden 5q-abnormiteter |
| [NCT01358734](https://clinicaltrials.gov/study/NCT01358734) | Fase 2 | Afsluttet | 88 | Randomiseret: lenalidomid, azacitidin efterfulgt af lenalidomid, eller azacitidin alene hos ≥ 65-årige med nydiagnosticeret AML |
| [NCT01301820](https://clinicaltrials.gov/study/NCT01301820) | Fase 2 | Afsluttet | 120 | Vedligeholdelse med skiftevis lenalidomid og azacitidin efter LIA-induktion hos ældre med AML |
| [NCT00352001](https://clinicaltrials.gov/study/NCT00352001) | Fase 1/2 | Afsluttet | 37 | Lenalidomid plus azacitidin ved avanceret MDS; bidraget fra lenalidomid kan ikke isoleres |
| [NCT01038635](https://clinicaltrials.gov/study/NCT01038635) | Fase 1/2 | Afsluttet | 94 | Azacitidin plus lenalidomid ved højrisiko-MDS og AML |
| [NCT00843882](https://clinicaltrials.gov/study/NCT00843882) | Fase 3 | Aktiv, rekrutterer ikke | 247 | Lenalidomid med eller uden epoetin alfa ved lav-/intermediær-1-risiko MDS med symptomatisk anæmi |
| [NCT04490707](https://clinicaltrials.gov/study/NCT04490707) | Fase 3 | Ukendt | 60 | Azacitidin plus lenalidomid som MRD-styret vedligeholdelse hos ældre eller skrøbelige AML-patienter |

Øvrige forsøg omfatter bl.a. fase 1-forsøg med lenalidomid efter allogen transplantation og i kombination med kemoterapi (f.eks. NCT01254578, NCT01681537, NCT01132586) samt et pædiatrisk fase 2-forsøg (NCT02538965).

---

## Litteraturevidens

Størstedelen af de identificerede publikationer er oversigtsartikler, og der er ingen randomiserede forsøg med lenalidomid specifikt ved AML blandt dem. Tabellen viser de mest relevante.

| PMID | År | Type | Tidsskrift | Hovedresultater |
|------|-----|------|------|---------|
| [23316859](https://pubmed.ncbi.nlm.nih.gov/23316859/) | 2013 | Oversigtsartikel | Expert Opin Investig Drugs | Lenalidomid som ny behandling af AML; godkendt til del(5q)-MDS og myelomatose, forsøg i højrisiko-MDS og AML |
| [32899586](https://pubmed.ncbi.nlm.nih.gov/32899586/) | 2020 | Oversigtsartikel | Cancers | Immunmodulerende lægemidler (IMiD'er) i AML-behandling; immunmodulerende, antiangiogene og pro-apoptotiske egenskaber |
| [39881283](https://pubmed.ncbi.nlm.nih.gov/39881283/) | 2025 | Præklinisk studie | Cell Mol Biol Lett | KDM5C øger AML-cellers følsomhed over for lenalidomid ved at stabilisere cereblon |
| [37288607](https://pubmed.ncbi.nlm.nih.gov/37288607/) | 2023 | Oversigtsartikel | Am J Hematol | Opdatering om diagnostik, risikostratificering og behandling af MDS |
| [37874917](https://pubmed.ncbi.nlm.nih.gov/37874917/) | 2023 | Oversigtsartikel | Blood | Klinisk beslutningstagning og behandling af MDS |
| [29795386](https://pubmed.ncbi.nlm.nih.gov/29795386/) | 2018 | Oversigtsartikel | Blood Cancer J | Behandlingsalgoritme for MDS |
| [41348013](https://pubmed.ncbi.nlm.nih.gov/41348013/) | 2025 | Oversigtsartikel | Hematology ASH Educ Program | Opdatering om lav-/intermediær-risiko MDS |
| [38066862](https://pubmed.ncbi.nlm.nih.gov/38066862/) | 2023 | Oversigtsartikel | Hematology ASH Educ Program | Nye behandlinger til lavrisiko-MDS |
| [24656536](https://pubmed.ncbi.nlm.nih.gov/24656536/) | 2014 | Oversigtsartikel | Lancet | Oversigt over myelodysplastiske syndromer |
| [17488990](https://pubmed.ncbi.nlm.nih.gov/17488990/) | 2007 | Oversigtsartikel | J Clin Oncol | AML og MDS hos ældre patienter |

---

## Markedsinformation for Danmark

| Markedsføringstilladelsesnummer | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28106555220 | Ferulinor (STADA Nordic ApS) | Kapsler, hårde | Indikationstekst er ikke angivet i de indsamlede data |

---

## Cytotoksicitet

| Punkt | Indhold |
|------|------|
| Cytotoksicitetsklassifikation | Immunmodulerende kræftlægemiddel (thalidomid-analog) |
| Myelosuppressionsrisiko | Høj (trombocytopeni og neutropeni indgår blandt de kontraindikerede tilstande i videnbasen) |
| Emetogenicitetsklassifikation | Se produktresuméet (SmPC) |
| Overvågningspunkter | Fuldt blodbillede med differentialtælling, lever- og nyrefunktion; se i øvrigt SmPC |
| Håndteringsbeskyttelse | Se produktresuméet (SmPC) vedrørende håndtering og beskyttelse; stoffet er et thalidomid-analog med teratogent potentiale |

---

## Sikkerhedsovervejelser

- **Tilstande registreret som kontraindikationer i videnbasen (ikke produkttekst):** trombocytopeni, neutropeni, agranulocytose, lungeemboli, nedsat nyrefunktion, cancer og embryom. Disse stammer fra TxGNN-videnbasen og ikke fra den godkendte produktinformation, og de skal ses i lyset af, at lenalidomid netop anvendes ved kræft.
- **Lægemiddelinteraktioner:** 460 interaktioner er registreret. Blandt de vigtigste er **alvorlige (Major)** interaktioner med rosuvastatin og simvastatin samt moderate interaktioner med eliglustat og naltrexon.

Se i øvrigt det godkendte produktresumé (SmPC) for fuldstændige oplysninger om advarsler og kontraindikationer.

---

## Konklusion og næste skridt

**Beslutning: Proceed with Guardrails**

**Begrundelse:**
Der foreligger en række afsluttede fase 2-forsøg ved AML og højrisiko-MDS, og mekanismen (CRBN-medieret nedbrydning, immunmodulation) er biologisk plausibel. Evidensen er dog overvejende enkeltarmet, småskala og i kombinationsregimer, og der findes ingen afsluttet fase 3-RCT ved AML. Forudsigelsen bør derfor behandles som et forskningsspørgsmål og ikke som grundlag for rutinemæssig anvendelse.

**For at komme videre kræves:**
- Gennemgang af produktresuméet for Ferulinor (advarsler, kontraindikationer og godkendt indikation), da disse data mangler
- Data om virkningsmekanismen fra DrugBank til at underbygge den mekanistiske sammenhæng
- Randomiserede data, der isolerer lenalidomids bidrag, samt afklaring af effekten i undergrupper (del(5q) versus ikke-del(5q))
- Plan for sikkerhedsovervågning (blodtal, tromboserisiko, teratogenicitet og interaktioner med statiner)
- Afklaring af, om forslagene om del(5q) og uklassificeret MDS reelt blot er delmængder af den allerede godkendte MDS-indikation
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

