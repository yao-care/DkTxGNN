---
layout: default
title: Sotalol
parent: Kun modelforudsigelse (L5)
nav_order: 770
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-28
description: "Sotalol: forudsagt ny indikation sick sinus syndrome 2, autosomal dominant (evidensniveau L5). Oprindelig indikation: Atrieflimren (fra videnbasen"
monitor_inn: "sotalol"
predicted_indications: ["sick sinus syndrome 2, autosomal dominant", "Wildervanck syndrome", "sarcoglycanopathy", "stroke disorder", "manic bipolar affective disorder", "macrocephaly, dysmorphic facies, and psychomotor retardation"]
---

# Sotalol
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

## Sotalol: Fra atrieflimren til sick sinus syndrome 2, autosomal dominant
{: .text-alpha }

## Sammenfatning i én sætning

Sotalol er et antiarytmisk lægemiddel med betablokerende og klasse III-virkning, som oprindeligt anvendes til atrieflimren. TxGNN-modellen forudsiger, at det kan være virksomt ved **sick sinus-syndrom 2 (autosomal dominant)**, men der er **ingen kliniske forsøg og ingen publikationer** for denne forudsigelse, og den mekanistiske vurdering peger på, at lægemidlet snarere kan forværre tilstanden.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Atrieflimren (fra videnbasen; produktets godkendte indikationstekst er ikke tilgængelig) |
| Foreslået ny indikation | Sick sinus-syndrom 2, autosomal dominant |
| TxGNN-forudsigelsesscore | 0,9976 |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført (gyldige tilladelser: 1 af 1) |
| Antal markedsføringstilladelser | 1 (gyldige: 1) |
| Anbefalet beslutning | Hold |

---

## Hvorfor er denne forudsigelse (ikke) rimelig?

Der foreligger på nuværende tidspunkt ikke detaljerede data om virkningsmekanismen i de data, der er indsamlet til denne rapport. Sotalol er dog kendt som en betablokker med klasse III-antiarytmisk aktivitet (blokade af kaliumkanaler), som nedsætter sinusfrekvensen og forsinker AV-overledningen.

Sick sinus-syndrom 2 er knyttet til tab af funktion i HCN4-genet, som giver sinusbradykardi. Sotalol må forventes at forværre sinusknudedysfunktion og bradykardi. Den mekaniske retning er derfor kontraindiceret frem for terapeutisk. Den høje score skyldes sandsynligvis en artefakt i grafens nærhedsstruktur (fælles knudepunkter for hjerterytmeforstyrrelser). Dette underbygges af, at sick sinus-syndrom og AV-blok optræder blandt sotalols kontraindikationer i videnbasen.

---

## Evidens fra kliniske forsøg

Der er for øjeblikket ingen relaterede kliniske forsøg registreret for sick sinus-syndrom 2.

---

## Litteraturevidens

Der er for øjeblikket ingen relateret litteratur for denne forudsigelse.

---

## Information om det danske marked

| Markedsføringstilladelsesnummer | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28107077823 | Sotalol "Nordic Prime" (Nordic Prime ApS) | Tabletter | Indikationstekst ikke angivet |

---

## Sikkerhedsovervejelser

- **Kontraindikationer/sygdomme med forhøjet risiko (fra videnbasen, ikke produktresumétekst):** langt QT-syndrom (også familiært), torsades de pointes, astma (inkl. intrinsisk og allergisk), bronkial sygdom, kaliummangel, diabetes mellitus, diabetisk ketoacidose, hypotension, nedsat nyrefunktion, atrioventrikulær blok, sick sinus-syndrom (også familiært) og anafylaksi.
- **Lægemiddelinteraktioner:** 328 interaktioner er registreret. Blandt dem er der flere af alvorlig (major) grad, bl.a. **adrenalin**, **clarithromycin**, **picosulfat** og **polyethylenglycol (3350 med elektrolytter)**. Mange er af moderat grad, fx med famotidin, loperamid, bupropion, morfin, atropin, cimetidin, canagliflozin og dapagliflozin. Acetylsalicylsyre er registreret som mindre (minor).
- Litteraturen for andre forudsigelser fremhæver risiko for additiv QT-forlængelse ved kombination med antipsykotika samt proarytmisk risiko (QT-forlængelse, torsades de pointes), som kræver opstart under indlæggelse og dosisjustering ved nedsat nyrefunktion.

For fuldstændig sikkerhedsinformation henvises til det godkendte produktresumé (SmPC), da advarsler og kontraindikationer fra produktresuméet ikke indgik i de indsamlede data.

---

## Øvrige forudsigelser (til information)

| Rang | Sygdom | Score | Evidensniveau | Vurdering |
|---|---|---|---|---|
| 2 | Wildervanck-syndrom | 0,9965 | L5 | Ingen plausibel mekanistisk sammenhæng; Hold |
| 3 | Sarkoglykanopati | 0,9964 | L5 | Påvirker ikke den underliggende defekt; Hold |
| 4 | Slagtilfælde | 0,9944 | L4 | Indirekte via atrieflimren; i praksis den oprindelige indikation; 1 fase 3-forsøg ([NCT00007605](https://clinicaltrials.gov/study/NCT00007605), afsluttet, 706 deltagere, amiodaron og sotalol ved vedligeholdelse af sinusrytme ved atrieflimren) og primært reviews; forskningsspørgsmål |
| 5 | Manisk bipolar lidelse | 0,9943 | L5 | Kun sikkerhedssignaler (QT); Hold |
| 6 | Makrocefali, dysmorfe ansigtstræk og psykomotorisk retardering | 0,9942 | L5 | Ingen sammenhæng; Hold |

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelsen for sick sinus-syndrom 2 bygger udelukkende på modellen (L5), uden forsøg eller litteratur. Sotalols virkning (nedsat sinusfrekvens og AV-overledning) peger i modsat retning af et terapeutisk formål, og sick sinus-syndrom er desuden anført blandt kontraindikationerne.

**For at komme videre kræves følgende:**
- Gennemgang af produktresuméet (advarsler og kontraindikationer) fra Lægemiddelstyrelsen, som er en blokerende datamangel for sikkerhedsvurderingen
- Detaljerede data om virkningsmekanismen (fx fra DrugBank)
- Ingen yderligere udredning af sick sinus-syndrom 2 anbefales, medmindre der fremkommer ny evidens, som modsiger den mekanistiske vurdering
- Hvis en forskningsretning ønskes, er forudsigelsen om slagtilfælde den eneste med indirekte evidens, men den er i praksis den oprindelige atrieflimren-indikation
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

