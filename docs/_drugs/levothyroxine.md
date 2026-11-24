---
layout: default
title: Levothyroxine
parent: Kun modelforudsigelse (L5)
nav_order: 497
evidence_level: L5
indication_count: 4
monitor_inn: "levothyroxine"
predicted_indications: ["renal hypodysplasia/aplasia", "bilateral renal agenesis", "Potter sequence", "Carney complex"]
last_modified_at: 2026-11-24
description: "Levothyroxine: forudsagt ny indikation Renal hypodysplasi/aplasi (evidensniveau L5). Oprindelig indikation: Hypothyreose"
---

# Levothyroxine
{: .fs-9 }

Evidensniveau: **L5** | Forudsagte indikationer: **4** stk.
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

## Levothyroxin: Fra hypothyreose til renal hypodysplasi/aplasi
{: .text-alpha }

## Resumé i én sætning

Levothyroxin er et skjoldbruskkirtelhormon, der i videnskabsgrafen er knyttet til behandling af bl.a. hypothyreose, struma og skjoldbruskkirtelkræft.
TxGNN-modellen forudsiger, at lægemidlet kan have effekt ved **renal hypodysplasi/aplasi**, men der er **0 kliniske forsøg** og **0 publikationer**, der understøtter dette. Forudsigelsen er alene modelbaseret.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Hypothyreose (relation registreret i videnskabsgrafen; den danske markedsføringstilladelse indeholder ingen indikationstekst i de data, der er indsamlet til rapporten) |
| Forudsagt ny indikation | Renal hypodysplasi/aplasi |
| TxGNN-forudsigelsesscore | 0,9967 |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført (gyldige tilladelser: mindst 20) |
| Antal markedsføringstilladelser | mindst 20 |
| Anbefalet beslutning | Hold |

---

## Hvorfor er forudsigelsen (ikke) rimelig?

Ifølge afsnittet »Mechanism of Action« i den produktinformation, som den amerikanske FDA har godkendt (Prescribing Information), for Levothyroxine (uofficiel oversættelse): »Thyroideahormoner udøver deres fysiologiske virkninger gennem kontrol af DNA-transkription og proteinsyntese. Triiodthyronin (T3) og L-thyroxin (T4) diffunderer ind i cellekernen og bindes til thyroideareceptorproteiner, der er bundet til DNA.« Engelsk originaltekst: "Thyroid hormones exert their physiologic actions through control of DNA transcription and protein synthesis. Triiodothyronine (T3) and L-thyroxine (T4) diffuse into the cell nucleus and bind to thyroid receptor proteins attached to DNA." ([DailyMed: Levoxyl (levothyroxine sodium) prescribing information, Pfizer Laboratories Div Pfizer Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=758588c3-c63e-491b-0aa2-4f50d80cb174), version af 2026-11-06; hentet 2026-11-19). Levothyroxin er syntetisk skjoldbruskkirtelhormon, og i videnskabsgrafen er det knyttet til tilstande som hypothyreose, myxødem, struma, Hashimotos thyroiditis og skjoldbruskkirtelkræft.

Skjoldbruskkirtelhormon spiller generelt en rolle i nyrernes udvikling og modning. Det er dog ikke et bevis for, at levothyroxin kan behandle eller omvende strukturelle nyremisdannelser, som opstår under fosterlivet. Der er ingen direkte mekanistisk sammenhæng understøttet af de foreliggende data. Den høje score kan afspejle nærhed i netværket, f.eks. fælles tilknytning til medfødte eller udviklingsrelaterede sygdomme, snarere end en reel terapeutisk sammenhæng.

De øvrige forudsigelser i modellen er ligeledes uden klinisk støtte:
- **Bilateral nyreagenesi** (score 0,9960): Fuldstændig fravær af begge nyrer forventes ikke at reagere på hormonsubstitution.
- **Potter-sekvens** (score 0,9933): Skyldes oligohydramnion, typisk som følge af nyreagenesi eller svær nyredysplasi. Der er ingen oplagt grund til postnatal levothyroxin.
- **Carney-kompleks** (score 0,9918): Syndromet omfatter endokrine tumorer, herunder skjoldbruskkirtelknuder, så der er en vis indirekte overlapning med skjoldbruskkirtelsygdom. Brug (f.eks. TSH-suppression ved knuder) ville dog være en udvidelse af eksisterende skjoldbrusktirtelindikationer og ikke en valideret behandling af syndromet.

---

## Evidens fra kliniske forsøg

Der er i øjeblikket ingen relaterede kliniske forsøg registreret.

---

## Litteraturevidens

Der er i øjeblikket ingen relateret litteratur tilgængelig.

---

## Information om det danske marked

<!-- licenses:begin -->

| Markedsføringstilladelsesnummer | Produktnavn | Lægemiddelform | Aktive stoffer | Status |
|---------|------|------|------|------|
| 28100020455 | Eltroxin | tabletter | LEVOTHYROXINNATRIUM | Gyldig |
| 28105398114 | Eltroxin | tabletter | LEVOTHYROXINNATRIUM | Gyldig |
| 28101006679 | Eltroxin | tabletter | LEVOTHYROXINNATRIUM | Gyldig |
| 28103222601 | Euthyrox | tabletter | LEVOTHYROXINNATRIUM | Gyldig |
| 28107128924 | Euthyrox | tabletter | LEVOTHYROXINNATRIUM | Gyldig |

Tabellen viser 5 af mindst 20 markedsføringstilladelser til humane lægemidler med dette aktive stof i Lægemiddelstyrelsens lister over godkendte og afregistrerede lægemidler; gyldige tilladelser står først. Dataene i denne rapport omfatter kun en del af tilladelserne.

Dataene indeholder desuden 15 tilladelser til veterinærlægemidler (ATC-kode Q eller »Vet.« i navnet), som ikke er medtaget i tabellen eller i antallet ovenfor.

<!-- licenses:end -->

---

## Sikkerhedsovervejelser

**Kontraindikationer registreret i videnskabsgrafen** (relationer i grafen, ikke teksten fra produktresuméet): hypertension, hypopituitarisme og andre former for hypofysemangel (herunder Sheehans syndrom og isoleret væksthormonmangel), hypogonadotrop hypogonadisme/Kallmanns syndrom, tymussygdom, osteoporose (inkl. postmenopausal), diabetes mellitus og diabetisk ketoacidose, koronararteriesygdom og myokardieinfarkt.

**Lægemiddelinteraktioner**: Der er identificeret 1.017 mulige interaktioner. Blandt de anførte er størstedelen af moderat sværhedsgrad, bl.a.:
- Antidiabetika: acarbose, metformin, pioglitazon, alogliptin, albiglutid, dulaglutid, canagliflozin, dapagliflozin, empagliflozin, chlorpropamid
- Syrehæmmere: omeprazol, rabeprazol, dexlansoprazol (cimetidin: lav grad)
- Mineraler/antacida: calciumphosphat, calciumacetat, magnesiumoxid
- Sympatomimetika: epinephrin, isometheptén, diethylpropion

For yderligere sikkerhedsinformation henvises til det godkendte produktresumé (SmPC).

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelserne er alene modelbaserede (evidensniveau L5) uden kliniske forsøg eller publikationer, og der er ingen plausibel mekanisme for, at levothyroxin kan behandle strukturelle nyremisdannelser eller deres følger.

**For at komme videre kræves følgende:**
- Data om virkningsmekanisme (MOA)
- Advarsler og kontraindikationer fra det godkendte produktresumé (SmPC) fra Lægemiddelstyrelsen
- Præklinisk eller klinisk evidens, der direkte undersøger levothyroxin ved den forudsagte sygdom
- For Carney-kompleks: en særskilt vurdering af, om brug ved skjoldbruskkirtelknuder er relevant

<!-- review:begin log -->

## Gennemgangslog

Nedenfor er gennemgangsloggen for denne side. Sætningen om, at data om virkningsmekanismen ikke var tilgængelige, er erstattet med et uddrag fra den angivne officielle produktinformation (med uofficiel oversættelse); modelforudsigelser, evidensniveauer og konklusioner er ikke omskrevet.

| Gennemgået | Punkt | Handling | Kilde |
|------|------|------|------|
| 2026-11-19 | Sætningen »data om virkningsmekanismen er ikke tilgængelige« erstattet med uddrag fra den amerikanske produktinformation | Sætning om manglende data om virkningsmekanismen erstattet med et uddrag med kilde | [DailyMed: Levoxyl (levothyroxine sodium) prescribing information, Pfizer Laboratories Div Pfizer Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=758588c3-c63e-491b-0aa2-4f50d80cb174) |

<!-- review:end log -->

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

