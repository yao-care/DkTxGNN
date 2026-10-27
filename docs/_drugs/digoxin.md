---
layout: default
title: Digoxin
parent: Kun modelforudsigelse (L5)
nav_order: 263
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Digoxin: forudsagt ny indikation Prinzmetal angina (evidensniveau L5). Oprindelig indikation: Atrieflimren og digitalisforgiftning"
monitor_inn: "DIGOXIN"
predicted_indications: ["Prinzmetal angina", "Prinzmetal angina", "duodenal obstruction", "duodenal obstruction", "duodenal ulcer (disease)", "duodenal ulcer (disease)", "duodenogastric reflux", "duodenogastric reflux", "obsolete susceptibility to ischemic stroke", "obsolete susceptibility to ischemic stroke"]
---

# Digoxin
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

## Digoxin: Fra atrieflimren til Prinzmetal angina
{: .text-alpha }

## Resumé i én sætning

Digoxin er et hjerteglykosid, der oprindeligt anvendes til behandling af atrieflimren og digitalisforgiftning. TxGNN-modellen forudsiger, at lægemidlet kan have effekt ved **Prinzmetal angina**, men der er **ingen kliniske forsøg** og kun **1 publikation** (en generel oversigtsartikel uden direkte relevans for digoxin), så forudsigelsen er i praksis uden klinisk understøttelse.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Atrieflimren og digitalisforgiftning (fra TxGNN-vidensgrafen; indikationsteksten i den danske registrering er ikke tilgængelig) |
| Forudsagt ny indikation | Prinzmetal angina |
| TxGNN-forudsigelsesscore | 99,81 % |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført |
| Antal markedsføringstilladelser | 1 |
| Anbefalet beslutning | Hold |

---

## Hvorfor er denne forudsigelse (ikke) rimelig?

Der foreligger ikke detaljerede data om digoxins virkningsmekanisme i de data, der er indsamlet til denne rapport. Digoxin er kendt som en hæmmer af Na⁺/K⁺-ATPase med positivt inotrop og vagomimetisk effekt. Dette er effektivt til frekvenskontrol ved atrieflimren, men det adresserer ikke koronar vasospasme, som er kernen i Prinzmetal angina.

Prinzmetal angina behandles typisk med calciumkanalblokkere og nitrater. Digoxin kan tværtimod øge karrenes tonus og kan teoretisk forværre vasospasme. Der er derfor ikke etableret en troværdig mekanistisk sammenhæng mellem den oprindelige og den forudsagte indikation. Den høje modelscore (0,998) er alene en modelforudsigelse og er ikke bekræftet af kliniske data.

Øvrige forudsagte indikationer med høje scorer (duodenal obstruktion 99,70 %, duodenalsår 99,59 %, duodenogastrisk reflux 99,53 % samt en forældet ontologipost om modtagelighed for iskæmisk apopleksi 99,29 %) har heller ingen kliniske forsøg eller relevant litteratur og ingen plausibel mekanistisk rationale. Digoxins gastrointestinale bivirkninger (kvalme, opkastning) taler snarere imod anvendelse ved de gastrointestinale tilstande.

---

## Klinisk forsøgsevidens

Der er i øjeblikket ingen relaterede kliniske forsøg registreret.

---

## Litteraturevidens

| PMID | År | Type | Tidsskrift | Hovedresultater |
|------|-----|------|------|---------|
| [10736610](https://pubmed.ncbi.nlm.nih.gov/10736610/) | 1999 | Oversigtsartikel | Acta physiologica et pharmacologica Bulgarica | Generel gennemgang af kronofarmakologi og antihypertensiv behandling; omhandler ikke digoxin ved Prinzmetal angina direkte |

---

## Markedsinformation for Danmark

| Markedsføringstilladelse | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28100709876 | Digoxin "DAK" (Orifarm Healthcare A/S) | Tabletter (oral) | Indikationstekst ikke tilgængelig |

---

## Sikkerhedsovvejelser

**Kontraindikationer ifølge vidensgrafen (TxGNN/PrimeKG, ikke produktresumétekst):**
Vidensgrafen angiver kontraindikation ved bl.a.:
- Hjerterelaterede tilstande: myokardieinfarkt, koronar trombose, ventrikelflimren, Wolff-Parkinson-White-syndrom, sick sinus-syndrom, atrioventrikulært blok, hypertrofisk og restriktiv kardiomyopati, cor pulmonale, myokarditis, konstriktiv perikarditis
- Elektrolyt- og stofskiftetilstande: kaliummangel, hyperkalcæmi, nefrokalcinose, forstyrrelser i fosforstofskiftet
- Øvrige: nyresygdom, pyouretær, hæmoglobinopati, myxødem, hypothyreose (inkl. medfødt)

**Lægemiddelinteraktioner (100 registreret; udvalgte eksempler):**
- Moderate: acarbose, rabeprazol, doxycyclin, adrenalin, hydrocortison, cholecalciferol, metformin, amphotericin B, bupropion, triamcinolon, acetylsalicylsyre, dexamethason, betamethason, tetracyclin, calciumphosphat
- Milde: albiglutid, hyoscyamin, atropin, glycopyrronium

Oplysninger om advarsler og kontraindikationer fra produktresuméet mangler. Se det godkendte produktresumé (SmPC) for fuldstændige sikkerhedsoplysninger.

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelsen er alene baseret på en modelscore (evidensniveau L5), uden kliniske forsøg og uden relevant litteratur. Der er ingen troværdig mekanistisk sammenhæng, og digoxin kan teoretisk forværre koronar vasospasme.

**For at komme videre kræves følgende:**
- Hentning og gennemgang af produktresuméet fra Lægemiddelstyrelsen (advarsler og kontraindikationer), da manglende sikkerhedsdata er en blokerende mangel
- Data om virkningsmekanisme (f.eks. fra DrugBank)
- Præklinisk eller klinisk evidens, der understøtter en effekt ved koronar vasospasme, samt en vurdering af risikoen for forværring
- Målrettet litteratursøgning, der direkte omhandler digoxin og den forudsagte indikation
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

