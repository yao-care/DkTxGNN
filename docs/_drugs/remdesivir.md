---
layout: default
title: Remdesivir
parent: Kun modelforudsigelse (L5)
nav_order: 711
evidence_level: L5
indication_count: 6
monitor_inn: "Remdesivir"
predicted_indications: ["multiple endocrine neoplasia", "HIV infectious disease", "feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "homozygous familial hypercholesterolemia"]
last_modified_at: 2026-10-23
description: "Remdesivir: forudsagt ny indikation Multipel endokrin neoplasi (evidensniveau L5). Oprindelig indikation: Ikke angivet i den danske godkendelsestekst"
---

# Remdesivir
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

## Remdesivir: Fra COVID-19 til multipel endokrin neoplasi
{: .text-alpha }

## Resumé

Remdesivir er et antiviralt middel (nukleotidanalog), som i Danmark er markedsført som Veklury, en koncentrat til infusionsvæske. Den lokale godkendelsestekst indeholder ikke en angivet indikation i de data, der er samlet til denne rapport.
TxGNN-modellen forudsiger, at lægemidlet kan have effekt ved **multipel endokrin neoplasi**, men der er **0 kliniske forsøg** og **0 publikationer**, som direkte undersøger denne sygdom. Forudsigelsen er derfor udelukkende modelbaseret.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Ikke angivet i den danske godkendelsestekst |
| Forudsagt ny indikation | Multipel endokrin neoplasi |
| TxGNN-forudsigelsesscore | 0,9950 |
| Evidensniveau | L5 |
| Status på det danske marked | Markedsført (gyldige tilladelser: 1 af 1) |
| Antal markedsføringstilladelser | 1 (gyldige: 1) |
| Anbefalet beslutning | Hold |

---

## Hvorfor er denne forudsigelse (ikke) rimelig?

Der foreligger ikke detaljerede data om virkningsmekanisme i de data, der er samlet til denne rapport. Remdesivir er dog kendt som en nukleotidanalog-prodrug, som hæmmer viral RNA-afhængig RNA-polymerase.

Multipel endokrin neoplasi er et arveligt tumorsyndrom (fx MEN1- og RET-mutationer) uden viral drivkraft. Der kan derfor ikke identificeres nogen mekanistisk sammenhæng mellem remdesivirs antivirale virkning og sygdommens patofysiologi. Den høje score (0,9950) stammer fra TxGNN-modellen (deep learning) og afspejler sandsynligvis ligheder, modellen har lært mellem beslægtede sygdomme, ikke biologisk evidens. Den understøttes ikke af kliniske data eller litteratur.

Til sammenligning har de øvrige forudsigelser i analysen heller ikke solid støtte. Den næstbedst scorende, HIV-infektion (score 0,9932), er mekanistisk mere plausibel på klasseniveau, da HIV er en RNA-virus. HIV bruger dog revers transkriptase, hvilket adskiller sig fra remdesivirs RdRp-hæmning. De fundne forsøg og artikler handler om COVID-19, ikke HIV-behandling.

---

## Dokumentation fra kliniske forsøg

Der er for øjeblikket ingen relaterede kliniske forsøg registreret for multipel endokrin neoplasi.

---

## Dokumentation fra litteraturen

Der er for øjeblikket ingen relateret litteratur om remdesivir ved multipel endokrin neoplasi.

---

## Information om det danske marked

| Markedsføringstilladelsesnummer | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28106444820 | Veklury (Gilead Sciences Ireland UC) | Koncentrat til infusionsvæske, opløsning | Ikke angivet i de tilgængelige data |

Antal tilladelser: 1 (enkeltstofpræparat, gyldig).

---

## Sikkerhedsovervejelser

- **Lægemiddelinteraktioner**: Der er registreret 100 potentielle interaktioner. De først anførte er alle af moderat grad, bl.a. acarbose, doxycyclin, pioglitazon, amphotericin B, bupropion, mesalazin, clarithromycin, minocyclin, tetracyclin, vancomycin, kanamycin, naltrexon, levofloxacin og neomycin.

Se i øvrigt det godkendte produktresumé (SmPC) for fuldstændige oplysninger om advarsler og kontraindikationer.

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelsen bygger kun på en score fra TxGNN-modellen (deep learning) uden kliniske forsøg, litteratur eller en plausibel mekanisme. Evidensniveauet er L5, og der er stor sandsynlighed for, at scoren blot afspejler ligheder, modellen har lært mellem beslægtede sygdomme, og ikke biologisk evidens.

**For at komme videre kræves følgende:**
- Data om virkningsmekanisme (MOA) fra DrugBank
- Produktresumé fra Lægemiddelstyrelsen med advarsler og kontraindikationer
- Præklinisk evidens (fx cellelinjer for MEN-relaterede tumorer), før klinisk overvejelse er relevant
- Eventuelt en mere gennemarbejdet vurdering af HIV-forudsigelsen, hvis man ønsker et mere plausibelt spor
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

