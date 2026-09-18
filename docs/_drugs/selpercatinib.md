---
layout: default
title: Selpercatinib
parent: Moderat evidens (L3-L4)
nav_order: 397
evidence_level: L4
indication_count: 10
---

# Selpercatinib
{: .fs-9 }

Evidensniveau: **L4** | Forudsagte indikationer: **10** stk.
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

# Selpercatinib: Fra RET-fusions-positiv cancer til lungehypertension

## Resumé på én linje

Selpercatinib er en selektiv RET-kinaseinhibitor, hvis etablerede indikation – ifølge litteraturen i denne evidenspakke – er i RET-fusions-positiv ikke-småcellet lungecancer og relaterede RET-ændret kræft. TxGNN-modellens topforudsigelse er **Lungehypertension** (score 99.18%), men de eneste to understøttende publikationer beskriver behandlingsrelateret *systemisk* hypertension som en bivirkning, ikke virning mod lungehypertension som sygdom – med **0 kliniske forsøg** og ingen litteratur om virning, der i øjeblikket bakker denne retning op.

---

## Hurtig oversigt

| Punkt | Indhold |
|------|---------|
| Original indikation | Ikke dokumenteret i denne evidenspakke (ingen dansk licensering på fil); litteraturkontekst indikerer RET-fusions-positiv NSCLC/RET-ændret kræft |
| Forudsagt ny indikation | Lungehypertension |
| TxGNN Forudsigelsesscore | 99.18% |
| Evidensniveau | L4 |
| Markedsstatus i Danmark | Ikke markedsført |
| Antal markedsføringstilladelser | 0 |
| Anbefalet beslutning | Standsning |

---

## Hvorfor er denne forudsigelse rimelig?

Detaljerede mekanisme-of-action-data er ikke tilgængelig i denne evidenspakke (markeret som et høj-alvorlighed data gap). Baseret på den understøttende litteratur er Selpercatinib en meget selektiv RET-kinaseinhibitor, og behandlingsrelateret hypertension (forhøjet blodtryk) er en dokumenteret bivirkning af RET-inhibitor-terapi.

Imidlertid er dette et lægemiddelsikkerhedssignal for *systemisk* hypertension, ikke mekanistisk evidens for behandling af *lungehypertension* som sygdom. Ingen af de to understøttende publikationer undersøger Selpercatinib's virning mod lungehypertension: den ene er en farmakovigilans-sammenligning af bivirkningsmønstre mellem pralsetinib og selpercatinib (FDA FAERS-data), og den anden er en praksis-analyse af selpercatinib i RET-fusions-positiv ikke-småcellet lungecancer (SIREN-program). Den mest sandsynlige forklaring er, at TxGNN's embedding-rum har blandet "hypertension" (bivirkningsterminus) med "lungehypertension" (det forudsagte sygdomsmål) – en termoverbinding-artefakt snarere end et ægt repurposing-signal.

De resterende forudsagte indikationer i denne evidenspakke (migræne, migræne med hjernestammeaura, kyfoskoliotisk hjertesygdom) er bedømt L5 (modelforudsigelse alene) og er baseret på enten rent teoretisk GDNF-RET-vejsignalforskning uden understøttende studier, eller litteratur, der ikke er relevant til emnet (genetikforskning om epilepsi fundet via søgeord-overlap med "migræne/aura"), hvilket yderligere bekræfter, at denne kandidat endnu ikke er klar til at gå videre ud over en datadrevet hypotese.

---

## Klinisk forsøgsbevis

I øjeblikket ingen relaterede kliniske forsøg registreret.

---

## Litteraturbevis

| PMID | År | Type | Tidsskrift | Vigtigste resultater |
|------|-----|------|---------|----------|
| [39372206](https://pubmed.ncbi.nlm.nih.gov/39372206/) | 2024 | Kohort (praksis-farmakovigilans) | Frontiers in Pharmacology | Sammenligner bivirkningsmønstre af pralsetinib vs. selpercatinib ved hjælp af FDA FAERS-data; undersøger ikke virning mod lungehypertension |
| [34178121](https://pubmed.ncbi.nlm.nih.gov/34178121/) | 2021 | Kohort (retrospektiv) | Therapeutic Advances in Medical Oncology | Praksis-analyse (SIREN) af selpercatinib i RET-fusions-positiv ikke-småcellet lungecancer via et adgangssprogram; ikke relateret til lungehypertension |

---

## Markedsinformation for Danmark

I øjeblikket ingen danske markedsføringstilladelser på fil (markedsstatus: Ikke markedsført).

---

## Cytotoxicitet

Selpercatinib er et onkologi-indikeret målrettet lægemiddel (baseret på RET-fusions-positiv ikke-småcellet lungecancer-kontekst i litteraturen ovenfor), så dette afsnit gælder.

| Punkt | Indhold |
|------|---------|
| Cytotoxicitet klassificering | Målrettet terapi (selektiv RET-kinaseinhibitor) |
| Myelosuppressions risiko | Ingen myelosuppressions-data tilgængelige i denne evidenspakke – se venligst Produktresumé (SmPC) |
| Emetogenicitets klassificering | Ingen data tilgængelige i denne evidenspakke – se venligst Produktresumé (SmPC) |
| Overvågnings punkter | Blodtryk (behandlingsrelateret hypertension er en dokumenteret klasse-effekt bivirkning ifølge farmakovigilans-litteraturen ovenfor); leverøversigt; se venligst Produktresumé (SmPC) for et fuldstændigt overvågnings-panel |
| Håndterings beskyttelse | Ingen data tilgængelige i denne evidenspakke – se venligst Produktresumé (SmPC) og gældende håndterings regler for cytotoksiske/målrettede lægemidler |

---

## Sikkerhedsmæssige overvejelser

Se venligst det godkendte Produktresumé (SmPC) for sikkerhedsinformation. Bemærk: TFDA/Danske Produktresumé-advarsler og kontraindikationer er registreret som en **Blokerende** data gap (DG001) – dette skal løses, før nogen sikkerhedspre-screening (S1) kan fortsætte.

---

## Konklusion og næste trin

**Beslutning: Standsning**

**Begrundelse:**
- Toprangerede forudsigelse (Lungehypertension) understøttes kun af to praksis-/farmakovigilans-papirer, der ikke omhandler lungehypertension-virning – associationen afspejler højst sandsynligt en termoverbinding-artefakt (systemisk hypertension bivirkning vs. lungehypertension sygdom) snarere end et ægt mekanistisk signal. Der er ingen kliniske forsøg, og lægemidlet er ikke markedsført i Danmark. En blokerende data gap (manglende Produktresumé-advarsler/kontraindikationer) forhindrer også nogen sikkerhedspre-screening på dette stadium.

**For at gå videre, er følgende påkrævet:**
- TFDA/Danske Produktresumé-advarsler og kontraindikationer (DG001, Blokering)
- Bekræftet mekanisme-of-action-data fra DrugBank (DG002)
- En dedikeret mekanistisk eller preklinisk undersøgelse af RET-signalering i lungekar-omformning, for at skelne et ægt repurposing-signal fra termoverbinding-artefakten identificeret ovenfor
- Genbevaluering af lavere-rangerede kandidater (migræne, kyfoskoliotisk hjertesygdom) kun hvis uafhængig, relevant litteratur eller forsøgs-evidens fremkommer

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

