---
layout: default
title: Isavuconazonium
parent: Kun modelforudsigelse (L5)
nav_order: 454
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-14
description: "Isavuconazonium: forudsagt ny indikation Pneumocystose (rang 1) og mycetom (rang 2) (evidensniveau L5). Oprindelig indikation: Aspergillose, zygomycose, coccidioidomycose, histoplasmose…"
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

<div id="pharmacist">

## Farmaceutens vurderingsrapport

</div>

# Isavuconazonium: Fra aspergillose til mycetom

## Resumé i en sætning

Isavuconazonium er et forstadie (prodrug) til isavuconazol, et bredspektret svampemiddel, som oprindeligt anvendes til behandling af svampeinfektioner som aspergillose og zygomycose. TxGNN-modellen forudsiger, at lægemidlet også kan have effekt på **mycetom** (rang 2 blandt de forudsagte indikationer), men der er **ingen registrerede kliniske forsøg** og kun **1 indirekte publikation** til at understøtte retningen. Den højest scorende forudsigelse, pneumocystose, vurderes som biologisk usandsynlig.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Aspergillose, zygomycose, coccidioidomycose, histoplasmose, sporotrikose, hvid og sort piedra (fra TxGNN-videnграfen; der er ikke angivet indikationstekst i den danske registrering) |
| Forudsagt ny indikation | Pneumocystose (rang 1) og mycetom (rang 2); rapporten fokuserer på begge |
| TxGNN-forudsigelsesscore | Pneumocystose: 99,56 %; mycetom: 99,34 % |
| Evidensniveau | Pneumocystose: L5; mycetom: L4 |
| Markedsstatus i Danmark | Markedsført |
| Antal markedsføringstilladelser | 1 |
| Anbefalet beslutning | Hold (for begge forudsigelser) |

---

## Hvorfor er forudsigelsen rimelig?

Detaljerede data om virkningsmekanisme (MOA) er ikke tilgængelige i de data, der er indsamlet til denne rapport. Ud fra kendt viden er isavuconazonium et prodrug af isavuconazol, som hæmmer svampens enzym lanosterol 14-alfa-demethylase (CYP51) og dermed blokerer syntesen af ergosterol, en nødvendig komponent i svampens cellemembran.

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
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

