---
layout: default
title: Inotersen
parent: Moderat evidens (L3-L4)
nav_order: 232
evidence_level: L4
indication_count: 10
---

# Inotersen
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

# Inotersen: Fra hereditær transthyretinmedieret amyloidose (hATTR) til akut intermitterende porfyri

## Oversigt i én sætning

Inotersen er et levertargeteret antisense-oligonukleotid (ASO), som er godkendt til hereditær transthyretinmedieret (hATTR) amyloidose, hvor det reducerer produktionen af amyloidogen transthyretinprotein (TTR). TxGNN forudsiger en mulig effekt ved **akut intermitterende porfyri (AIP)**, men dette signal understøttes i øjeblikket kun af **0 kliniske forsøg** og blot **1 indirekte litteraturreference** — og bevispakkens egen mekanistiske analyse markerer den biologiske forbindelse som implausibel.

---

## Hurtig oversigt

| Element | Indhold |
|------|------|
| Oprindelig indikation | Hereditær transthyretinmedieret (hATTR) amyloidose *(fra bevispakkens baggrundsoplysninger; ikke til stede i det formelle `original_indications` registreringsfeldt — se Datakløft DG002)* |
| Forudsagt ny indikation | Akut intermitterende porfyri |
| TxGNN-forudsigelsesscore | 99.92% |
| Bevisniveau | L4 |
| Markedsstatus i Danmark | Ikke markedsført |
| Antal markedsføringstilladelser | 0 |
| Anbefalet beslutning | Afvent |

---

## Hvorfor er denne forudsigelse rimelig?

Detaljerede virkningsmekanismedata er ikke tilgængelige i det strukturerede register (Datakløft DG002, høj alvorlighed). Baseret på baggrundsoplysninger i bevispakken er Inotersen et antisense-oligonukleotid, som binder TTR-mRNA i leveren, sænker cirkulerende TTR-protein og reducerer derved amyloidfibrilaflejring — grundlaget for dets godkendelse ved hATTR-amyloidose.

Bevispakkens egen mekanistiske begrundelse argumenterer dog **imod** en plausibel forbindelse til akut intermitterende porfyri. AIP skyldes dysregulering af hemebiosyntesevejen (ALAS1/PBGD-HMBS-mangel), hvilket fører til ophobning af δ-ALA og porfyrinpræcursorer. En terapi, som allerede eksisterer til netop denne mekanisme — Givosiran, et RNAi-lægemiddel, som specifikt stilner hepatisk ALAS1-mRNA. Inotersens målstof (TTR) har ingen kendt molekylær vej med hemebioinsynte eller porfyrinmetabolisme.

Begrundelsesteksten konkluderer, at den meget høje TxGNN-score højtformentlig afspejler **strukturel lighedsklyngedannelse i vidensgrafen** — "levertargeterede oligonukleotidterapier for sjælden arvelig metabolisk/neurologisk sygdom" — snarere end en ægte lægemiddel-target-sygdommekanistisk forbindelse. Den enkelt understøttende publikation (PMID 30847674) er en generel oversigt over terapeutiske fremskridt inden for genetiske neuromuskulære/perifere neuropati-sygdomme, som diskuterer ASO/RNAi-lægemidler brugt til hATTR-amyloidose bredt; den omhandler ikke Inotersens brug ved AIP specifikt, og klassificeres i bevispakken som indirekte, ikke-sygdomsspecifik bevis.

**Kort sagt: dette er et lavt-sikkerhedssignal, kun-model signal, som intern mekanistisk vurdering betragter som usandsynligt at afspejle ægte farmakologisk relevans.**

---

## Bevis fra kliniske forsøg

Der er i øjeblikket ingen relaterede kliniske forsøg registreret. (Søgninger i ClinicalTrials.gov og WHO ICTRP for Inotersen + Akut intermitterende porfyri gav begge 0 resultater, ifølge forespørgelseslog.)

---

## Litteraturbevis

| PMID | År | Type | Journal | Vigtige fund |
|------|-----|------|------|---------|
| [30847674](https://pubmed.ncbi.nlm.nih.gov/30847674/) | 2019 | Oversigt | Neurological Sciences | Generel oversigt over terapeutiske fremskridt inden for genetiske neuromuskulære/perifere neuropati-sygdomme, herunder ASO/RNAi-lægemidler brugt til hATTR-amyloidose; **diskuterer ikke** Inotersens brug ved akut intermitterende porfyri — klassificeret i bevispakken som indirekte, ikke-sygdomsspecifik bevis. |

---

## Markedsoplysninger for Danmark

Inotersen har i øjeblikket **ingen markedsføringstilladelse registreret** for Danmark (`market_status: Not marketed` / Ikke markedsført; `total_licenses: 0`). Ingen nationale (Lægemiddelstyrelsen) eller centraliserede (EMA) tilladelsesrecords var tilgængelige i denne bevispakke.

---

## Sikkerhedshensyn

Se venligst det godkendte Produktresumé (SmPC) for sikkerhedsoplysninger.

*Bemærk: Vigtige advarsler, kontraindikationer og data om lægemiddelinteraktioner var alle markeret som utilgængelige i denne bevispakke. Hentning af TFDA/SmPC-niveau advarsler og kontraindikationer er registreret som en **Blokerende datakløft (DG001)** — uden den kan denne kandidat ikke fortsætte til sikkerhedsforhåndsvurderingsfasen S1.*

---

## Konklusion og næste trin

**Beslutning: Afvent**

**Begrundelse:**
- Forudsigelsen hviler udelukkende på en TxGNN-lighedsresultat, med nul kliniske forsøg og kun én indirekte (ikke sygdomsspecifik) litteraturreference.
- Bevispakkens egen mekanistiske vurdering betragter TTR–AIP biologisk forbindelse som implausibel, og tillægger den høje score vidensgrafsstrukturel klyngedannelse snarere end et ægte farmakologisk forhold — en valideret, mekanisme-specifik RNAi-terapi (Givosiran/ALAS1) eksisterer allerede for AIP.
- Inotersen er i øjeblikket ikke markedsført i Danmark, og obligatoriske sikkerhedsdata (SmPC advarsler/kontraindikationer) mangler — en Blokerende datakløft (DG001), som forhindrer fremskridt ud over den nuværende S0-screeningfase.

**For at fortsætte kræves følgende:**
- Løs Blokering datakløft DG001: indhent TFDA/SmPC advarsler og kontraindikationer, før nogen sikkerhedsforhåndsvurdering (S1) kan påbegyndes
- Løs Høj-alvorlighed datakløft DG002: indhent bekræftede virkningsmekanismedata fra DrugBank/producent for at vurdere mekanistisk plausibilitet korrekt
- Uafhængig ekspertvurdering (hepatologi/porfyri-specialist) af, hvorvidt nogen indirekte TTR–heme-vejinteraktion kunne eksistere, givet at den nuværende mekanistiske vurdering argumenterer imod det
- Løbende overvågning for nogen fremtidig præ-klinisk eller klinisk bevis specifikt for Inotersen ved porfyri, før denne kandidat genovervejes
- Bekræftelse af dansk/EU regulatorisk vej og administrationsvej-kompatibilitet, hvis markedsstatus ændres

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

