---
layout: default
title: Hydroxocobalamin
parent: Kun modelforudsigelse (L5)
nav_order: 413
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-06
monitor_inn: "hydroxocobalamin"
predicted_indications: ["esophageal varices without bleeding", "esophageal varices with bleeding"]
description: "Hydroxocobalamin: forudsagt ny indikation Esophageal varices without bleeding (evidensniveau L5). I Danmark, markedsføringstilladelser: 4 (gyldige: 4)"
---

# Hydroxocobalamin
{: .fs-9 }

Evidensniveau: **L5** | Forudsagte indikationer: **2** stk.
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

## Hydroxocobalamin: Esophageal varices without bleeding
{: .text-alpha }

## Resumé i én sætning

Hydroxocobalamin er en form for vitamin B12, som oprindeligt anvendes til behandling af vitamin B12-mangel, perniciøs anæmi og cyanidforgiftning.
TxGNN-modellen forudsiger, at lægemidlet kan have effekt ved **esophageal varices uden blødning** (åreknuder i spiserøret), men der er **0 kliniske forsøg** og **0 publikationer**, som støtter denne retning. Forudsigelsen er udelukkende baseret på en model.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Ikke registreret i de lokale data |
| Forudsagt ny indikation | Esophageal varices without bleeding |
| TxGNN-prædiktionsscore | 0.9923 |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført (gyldige tilladelser: 4 af 4) |
| Antal markedsføringstilladelser | 4 (gyldige: 4) |
| Anbefalet beslutning | Hold |

---

## Hvorfor er denne forudsigelse rimelig?

Ifølge afsnittet »Mechanism of Action« i den produktinformation, som den amerikanske FDA har godkendt (Prescribing Information), for Hydroxocobalamin (uofficiel oversættelse): »Cyanid er en ekstremt toksisk gift. Uden hurtig og tilstrækkelig behandling kan eksponering for en høj dosis cyanid medføre død inden for minutter på grund af hæmning af cytokromoxidase, hvilket resulterer i ophør af cellulær respiration. […] Hvert hydroxocobalaminmolekyle kan binde én cyanidion ved at erstatte hydroxoliganden, der er bundet til den trivalente koboltion, med denne, hvorved der dannes cyanocobalamin, som derefter udskilles i urinen.« Engelsk originaltekst: "Cyanide is an extremely toxic poison. In the absence of rapid and adequate treatment, exposure to a high dose of cyanide can result in death within minutes due to the inhibition of cytochrome oxidase resulting in arrest of cellular respiration. […] Each hydroxocobalamin molecule can bind one cyanide ion by substituting it for the hydroxo ligand linked to the trivalent cobalt ion, to form cyanocobalamin, which is then excreted in the urine." ([DailyMed: Cyanokit (hydroxocobalamin) prescribing information, BTG INTERNATIONAL INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=d56fcc8d-bd64-46ab-b0c0-2124bd745a6b), version af 2023-04-27; hentet 2026-11-19). Hydroxocobalamin er en cobalamin (vitamin B12-form), hvis effekt ved B12-mangel og cyanidforgiftning er veletableret. Den kan binde cyanid, og det er desuden kendt, at den kan binde nitrogenoxid (NO) og hydrogensulfid.

Teoretisk kunne en binding af NO påvirke karudvidelse i mave-tarm-området og i portalkredsløbet, som spiller en rolle ved portal hypertension og åreknuder i spiserøret. Dette er imidlertid spekulativt, og der er ikke fremlagt data, som understøtter en egentlig mekanistisk sammenhæng mellem de oprindelige indikationer og esophageal varices.

Den høje score (0,9923) er en ren modelforudsigelse fra TxGNN-modellen (deep learning) og kan ikke erstatte klinisk evidens eller litteratur. Scoren kan afspejle ligheder, som modellen har lært mellem beslægtede sygdomme, og er ikke biologisk evidens. Det samme gælder den relaterede forudsigelse **esophageal varices med blødning** (samme score, 0,9923, evidensniveau L5). Akut variceblødning behandles med etablerede metoder (vasoaktive stoffer, endoskopisk båndligering og antibiotikaprofylakse), og der er ingen evidens for, at hydroxocobalamin har en rolle.

---

## Klinisk evidens

Der er for tiden ingen relaterede kliniske forsøg registreret.

---

## Litteraturevidens

Der er for tiden ingen relateret litteratur tilgængelig.

---

## Markedsinformation for Danmark

| Markedsføringstilladelse | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28104060406 | Cyanokit (SERB S.A.) | Pulver til infusionsvæske, opløsning | Indikationsteksten er ikke angivet i de indsamlede data |

Lægemidlet findes kun som injicerbar formulering (infusion).

---

## Sikkerhedsovervejelser

- **Kontraindikationer fra vidensgrafen** (ikke fra produktresumeet): Hypertension og hypertensive tilstande er i vidensgrafen registreret som kontraindikation. Det bør vurderes nøje, da patienter med portal hypertension ofte har komplekse hæmodynamiske forhold.
- **Lægemiddelinteraktioner**: I alt 83 mulige interaktioner er identificeret. De fleste har ukendt alvorlighedsgrad. Interaktioner med **moderat** alvorlighed omfatter:
  - Arsentrioxid
  - Chloramphenicol
  - Iodid I-131
  - Iodid I-123

  Blandt de øvrige ses bl.a. omeprazol, lansoprazol, simvastatin, prednisolon, acetylsalicylsyre, valsartan, ramipril og citalopram (alvorlighed ukendt).

Se i øvrigt det godkendte produktresumé (SmPC) for fuldstændige sikkerhedsoplysninger.

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelsen bygger kun på en computermodel (L5) uden kliniske forsøg, uden litteratur og uden en dokumenteret mekanistisk sammenhæng. Der findes desuden etablerede behandlinger til indikationen.

**For at komme videre kræves følgende:**
- Data om virkningsmekanisme (MOA), f.eks. fra DrugBank
- Gennemgang af produktresumeet fra Lægemiddelstyrelsen (advarsler og kontraindikationer) og den godkendte indikationstekst
- Systematisk litteratursøgning og prækliniske studier af NO-binding og portalt tryk
- Vurdering af ruteegnethed og sikkerhed ved hypertension/portal hypertension, før der overvejes kliniske forsøg

<!-- review:begin log -->

## Gennemgangslog

Nedenfor er gennemgangsloggen for denne side. Sætningen om, at data om virkningsmekanismen ikke var tilgængelige, er erstattet med et uddrag fra den angivne officielle produktinformation (med uofficiel oversættelse); modelforudsigelser, evidensniveauer og konklusioner er ikke omskrevet.

| Gennemgået | Punkt | Handling | Kilde |
|------|------|------|------|
| 2026-11-19 | Sætningen »data om virkningsmekanismen er ikke tilgængelige« erstattet med uddrag fra den amerikanske produktinformation | Sætning om manglende data om virkningsmekanismen erstattet med et uddrag med kilde | [DailyMed: Cyanokit (hydroxocobalamin) prescribing information, BTG INTERNATIONAL INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=d56fcc8d-bd64-46ab-b0c0-2124bd745a6b) |

<!-- review:end log -->

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

