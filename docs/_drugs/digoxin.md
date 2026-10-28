---
layout: default
title: Digoxin
parent: Kun modelforudsigelse (L5)
nav_order: 263
evidence_level: L5
indication_count: 5
monitor_inn: "DIGOXIN"
predicted_indications: ["Prinzmetal angina", "duodenal obstruction", "duodenal ulcer (disease)", "duodenogastric reflux", "hypoalphalipoproteinemia"]
last_modified_at: 2026-10-28
description: "Digoxin: forudsagt ny indikation Prinzmetal angina (evidensniveau L5). Oprindelig indikation: Atrieflimren og digitalisforgiftning"
---

# Digoxin
{: .fs-9 }

Evidensniveau: **L5** | Forudsagte indikationer: **5** stk.
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

## Digoxin: Fra atrieflimren til Prinzmetal angina
{: .text-alpha }

## Resumé i én sætning

Digoxin er en hjerteglykosid, som i videnbasen (knowledge graph) er registreret i relation til atrieflimren og digitalisforgiftning. TxGNN-modellen forudsiger, at lægemidlet kan have effekt ved **Prinzmetal angina**, men der er **0 kliniske forsøg** og kun **1 publikation** med en meget fjern forbindelse til denne retning. Forudsigelsen bygger reelt kun på modellen.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Atrieflimren og digitalisforgiftning (relationer registreret i videnbasen; ikke angivet i godkendelsesteksten, som er tom) |
| Forudsagt ny indikation | Prinzmetal angina |
| TxGNN-forudsigelsesscore | 0,9981 |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført (gyldige tilladelser: 1 af 1) |
| Antal markedsføringstilladelser | 1 (gyldige: 1) |
| Anbefalet beslutning | Hold |

---

## Hvorfor er forudsigelsen (ikke) rimelig?

De data, der er indsamlet til denne rapport, indeholder ingen detaljerede oplysninger om virkningsmekanismen. Digoxin er kendt som hæmmer af Na⁺/K⁺-ATPase, hvilket øger den intracellulære calciumkoncentration. Det styrker hjertets kontraktilitet og bremser overledningen i AV-knuden, hvilket forklarer den kendte brug ved atrieflimren.

Prinzmetal angina skyldes koronar vasospasme og behandles normalt med vasodilatorer (calciumkanalblokkere og nitrater). Den øgede intracellulære calciumkoncentration kan tværtimod øge den vaskulære tonus, så digoxin er mekanistisk modsatrettet. Der er derfor ikke noget klart mekanistisk bindeled mellem de oprindelige relationer og den nye forudsagte indikation.

Den høje modelscore er en ren grafbaseret forudsigelse. Den eneste tilknyttede publikation handler om kronofarmakologi ved antihypertensiv behandling og omhandler ikke digoxin ved vasospastisk angina.

---

## Klinisk evidens

Der er for øjeblikket ingen relaterede kliniske forsøg registreret.

---

## Litteraturevidens

| PMID | År | Type | Tidsskrift | Hovedresultater |
|------|-----|------|------|---------|
| [10736610](https://pubmed.ncbi.nlm.nih.gov/10736610/) | 1999 | Review | Acta physiologica et pharmacologica Bulgarica | Gennemgang af kronofarmakologi og betydningen for antihypertensiv behandling; omhandler ikke digoxin ved Prinzmetal angina |

---

## Markedsinformation for Danmark

| Markedsføringstilladelsesnummer | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28100709876 | Digoxin "DAK" (Orifarm Healthcare A/S) | Tabletter (oral) | Indikationsteksten er ikke angivet i de indsamlede data |

---

## Sikkerhedsovervejelser

**Kontraindikationer registreret i videnbasen** (ikke fra produktresuméet, og skal derfor ikke læses som officielle kontraindikationer): nyresygdom, kaliummangel, hyperkalcæmi, nefrokalcinose, forstyrrelser i fosformetabolismen, myokardieinfarkt, koronar trombose, hæmoglobinopati, cor pulmonale, Wolff-Parkinson-White syndrom, sick sinus syndrom (herunder familiær form), ventrikelflimren, hypertrofisk kardiomyopati (herunder familiær form), restriktiv kardiomyopati, atrioventrikulær blok, myxødem, hypothyroidisme (herunder kongenit), myokarditis, konstriktiv perikarditis og pyoureter.

**Lægemiddelinteraktioner:** 100 interaktioner er identificeret i alt; de vigtigste fra den viste liste:
- Moderate: acarbose, rabeprazol, doxycyclin, adrenalin, hydrocortison, colecalciferol, metformin, amphotericin B (inkl. lipidkompleks), bupropion, triamcinolon, acetylsalicylsyre, dexamethason, betamethason, tetracyclin, calciumphosphat
- Mindre: albiglutid, hyoscyamin, atropin, glycopyrronium

Se desuden det godkendte produktresumé (SmPC) for fuldstændige oplysninger om advarsler og kontraindikationer.

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelsen om Prinzmetal angina bygger kun på modellen (evidensniveau L5). Der er ingen kliniske forsøg og ingen publikationer, der undersøger digoxin ved denne sygdom, og mekanismen peger snarere mod, at digoxin er uhensigtsmæssig ved koronar vasospasme.

**For at komme videre kræves følgende:**
- Detaljerede data om virkningsmekanisme (MOA)
- Gennemgang af produktresuméet (SmPC) for advarsler og kontraindikationer
- Præklinisk eller klinisk evidens, der direkte undersøger digoxin ved Prinzmetal angina
- Vurdering af, om forudsigelsen er en artefakt i videnbasen
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

