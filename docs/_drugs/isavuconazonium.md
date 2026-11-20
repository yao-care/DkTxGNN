---
layout: default
title: Isavuconazonium
parent: Kun modelforudsigelse (L5)
nav_order: 454
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-06
description: "Isavuconazonium: forudsagt ny indikation Pneumocystose (rang 1) og mycetom (rang 2) (evidensniveau L5). Oprindelig indikation: Aspergillose, zygomycose, coccidioidomycose, histoplasmose…"
monitor_inn: "isavuconazonium"
predicted_indications: ["pneumocystosis", "mycetoma"]
---

# Isavuconazonium
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

## Isavuconazonium: Fra aspergillose til pneumocystose
{: .text-alpha }

## Resumé i en sætning

Isavuconazonium er et forstadie (prodrug) til isavuconazol, et bredspektret svampemiddel, som oprindeligt anvendes til behandling af svampeinfektioner som aspergillose og zygomycose. TxGNN-modellen forudsiger, at lægemidlet også kan have effekt på **mycetom** (rang 2 blandt de forudsagte indikationer), men der er **ingen registrerede kliniske forsøg** og kun **1 indirekte publikation** til at understøtte retningen. Den højest scorende forudsigelse, pneumocystose, vurderes som biologisk usandsynlig.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Aspergillose, zygomycose, coccidioidomycose, histoplasmose, sporotrikose, hvid og sort piedra (fra TxGNN-videnграfen; der er ikke angivet indikationstekst i den danske registrering) |
| Forudsagt ny indikation | Pneumocystose (rang 1) og mycetom (rang 2); rapporten fokuserer på begge |
| TxGNN-forudsigelsesscore | Pneumocystose: 0,9956; mycetom: 0,9934 |
| Evidensniveau | Pneumocystose: L5; mycetom: L4 |
| Markedsstatus i Danmark | Markedsført (gyldige tilladelser: 3 af 3) |
| Antal markedsføringstilladelser | 3 (gyldige: 3) |
| Anbefalet beslutning | Hold (for begge forudsigelser) |

---

## Hvorfor er forudsigelsen rimelig?

Ifølge afsnittene »Mechanism of Action« og »Microbiology« i den produktinformation, som den amerikanske FDA har godkendt (Prescribing Information), for Isavuconazonium (uofficiel oversættelse): »Isavuconazoniumsulfat er prodrug for isavuconazol, et azol-antimykotikum. […] Isavuconazoniumsulfat er prodrug for isavuconazol, et antimykotisk lægemiddel af azoltypen. Isavuconazol hæmmer syntesen af ergosterol, en central bestanddel af svampecellemembranen, gennem hæmning af det cytokrom P-450-afhængige enzym lanosterol-14-alfa-demethylase.« Engelsk originaltekst: "Isavuconazonium sulfate is the prodrug of isavuconazole, an azole antifungal. […] Isavuconazonium sulfate is the prodrug of isavuconazole, an azole antifungal drug. Isavuconazole inhibits the synthesis of ergosterol, a key component of the fungal cell membrane, through the inhibition of cytochrome P-450 dependent enzyme lanosterol 14-alpha-demethylase." ([DailyMed: Cresemba (isavuconazonium sulfate) prescribing information, Astellas Pharma US, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=8f7f73b8-586a-4df0-935f-fecd4696c16c), version af 2025-04-25; hentet 2026-11-19). Ud fra kendt viden er isavuconazonium et prodrug af isavuconazol, som hæmmer svampens enzym lanosterol 14-alfa-demethylase (CYP51) og dermed blokerer syntesen af ergosterol, en nødvendig komponent i svampens cellemembran.

**Mycetom:** Eumycetom (den svampeforårsagede form, fx *Madurella mycetomatis*) skyldes svampe med ergosterol i cellemembranen, som generelt er følsomme over for azoler. Mekanismen er derfor plausibel. Itraconazol er nuværende standardbehandling, og fosravuconazol, et andet azol-prodrug, har vist gavnlig effekt i et fase 2-forsøg. Isavuconazol er et beslægtet triazol, hvilket giver indirekte støtte. Actinomycetom er derimod bakteriel og forventes ikke at responderere på et svampemiddel.

**Pneumocystose:** Forudsigelsen er svagt funderet. *Pneumocystis jirovecii* mangler ergosterol i cellemembranen og bruger kolesterol og beslægtede steroler, så azolernes mål er biologisk svagt. Azoler er ikke standardbehandling (trimethoprim-sulfamethoxazol er førstevalg). Den høje score afspejler sandsynligvis lægemidlets generelle antifungale profil frem for reel mekanistisk eller klinisk evidens.

---

## Evidens fra kliniske forsøg

Der er på nuværende tidspunkt ingen relaterede kliniske forsøg registreret, hverken for mycetom eller pneumocystose.

---

## Litteraturevidens

Kun mycetom har en publikation. For pneumocystose foreligger der ingen litteratur.

| PMID | År | Type | Tidsskrift | Hovedresultater |
|------|-----|------|------|---------|
| [37907954](https://pubmed.ncbi.nlm.nih.gov/37907954/) | 2023 | Review | Parasites & Vectors | Oversigt over pipelinen for orale anti-infektiva og kombinationer til off-label brug mod oversete tropesygdomme (NTD'er). Indirekte evidens, ikke specifik for isavuconazonium ved mycetom. |

---

## Information om det danske marked

| Markedsføringstilladelse | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28105475714 | Cresemba (Basilea Pharmaceutica Deutschland GmbH) | Kapsler, hårde | Indikationstekst er ikke angivet i de indsamlede data |

---

## Sikkerhedsovervejelser

- **Lægemiddelinteraktioner:** Der er identificeret 207 mulige interaktioner. Blandt de fremhævede er der flere af **alvorlig (major)** grad, bl.a. med **clarithromycin**, **eliglustat** og **cisaprid**. Mange er af moderat grad, bl.a. hydrocortison, dexamethason, betamethason, triamcinolon, budesonid, metformin, pioglitazon, saxagliptin, linagliptin, empagliflozin, loperamid, bupropion, aprepitant, cimetidin og clotrimazol. Fidaxomicin er angivet som mindre (minor). Interaktionsbyrden hænger sammen med CYP3A4-involvering.
- **Praktiske forhold:** Mycetom kræver typisk langvarig behandling, hvilket øger betydningen af interaktioner og monitorering.

Se i øvrigt det godkendte produktresumé (SmPC) for fuldstændige oplysninger om advarsler og kontraindikationer.

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
- Mycetom er mekanistisk plausibelt for eumycetom (azol-følsomme svampe), men evidensen er kun indirekte (én oversigtsartikel) uden forsøg med isavuconazonium. Pneumocystose er biologisk usandsynlig trods den høje modelscore og bør ikke prioriteres.

**For at komme videre kræves følgende:**
- Gennemgang af produktresuméet for advarsler og kontraindikationer (disse data mangler og blokerer sikkerhedsscreeningen)
- Data om virkningsmekanisme (MOA), fx fra DrugBank
- Prækliniske data (in vitro-følsomhed af *Madurella mycetomatis* over for isavuconazol) og kliniske data eller case-serier for mycetom
- Afklaring af sygdomsform (eumycetom vs. actinomycetom) og vurdering af dosering, behandlingsvarighed og interaktionsstyring
- Afklaring af, hvilke indikationer der er godkendt for Cresemba i Danmark

<!-- review:begin log -->

## Gennemgangslog

Nedenfor er gennemgangsloggen for denne side. Sætningen om, at data om virkningsmekanismen ikke var tilgængelige, er erstattet med et uddrag fra den angivne officielle produktinformation (med uofficiel oversættelse); modelforudsigelser, evidensniveauer og konklusioner er ikke omskrevet.

| Gennemgået | Punkt | Handling | Kilde |
|------|------|------|------|
| 2026-11-19 | Sætningen »data om virkningsmekanismen er ikke tilgængelige« erstattet med uddrag fra den amerikanske produktinformation | Sætning om manglende data om virkningsmekanismen erstattet med et uddrag med kilde | [DailyMed: Cresemba (isavuconazonium sulfate) prescribing information, Astellas Pharma US, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=8f7f73b8-586a-4df0-935f-fecd4696c16c) |

<!-- review:end log -->

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

