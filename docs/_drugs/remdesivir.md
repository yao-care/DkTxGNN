---
layout: default
title: Remdesivir
parent: Kun modelforudsigelse (L5)
nav_order: 711
evidence_level: L5
indication_count: 6
monitor_inn: "Remdesivir"
predicted_indications: ["multiple endocrine neoplasia", "HIV infectious disease", "feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "homozygous familial hypercholesterolemia"]
last_modified_at: 2026-11-24
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
| Markedsstatus i Danmark | Markedsført (gyldige tilladelser: 2 af 2) |
| Antal markedsføringstilladelser | 2 (gyldige: 2) |
| Anbefalet beslutning | Hold |

---

## Hvorfor er denne forudsigelse (ikke) rimelig?

Ifølge afsnittene »Mechanism of Action« og »Microbiology« i den produktinformation, som den amerikanske FDA har godkendt (Prescribing Information), for Remdesivir (uofficiel oversættelse): »Remdesivir er et antiviralt lægemiddel med aktivitet mod svær akut respiratorisk syndrom-coronavirus 2 (SARS-CoV-2). […] Remdesivir er en hæmmer af SARS-CoV-2's RNA-afhængige RNA-polymerase (RdRp), som er essentiel for viral replikation. Remdesivir er et adenosinnukleotid-prodrug, der fordeles ind i celler, hvor det metaboliseres til et nukleosidmonofosfat-intermediat af carboxyesterase 1 og/eller cathepsin A, afhængigt af celletypen.« Engelsk originaltekst: "Remdesivir is an antiviral drug with activity against severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2). […] Remdesivir is an inhibitor of the SARS-CoV-2 RNA-dependent RNA polymerase (RdRp), which is essential for viral replication. Remdesivir is an adenosine nucleotide prodrug that distributes into cells where it is metabolized to a nucleoside monophosphate intermediate by carboxyesterase 1 and/or cathepsin A, depending upon the cell type." ([DailyMed: Veklury (remdesivir) prescribing information, Gilead Sciences, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=c0978fa8-53ff-4ca2-82a7-567fd3e958ca), version af 2026-07-29; hentet 2026-11-19). Remdesivir er dog kendt som en nukleotidanalog-prodrug, som hæmmer viral RNA-afhængig RNA-polymerase.

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

<!-- licenses:begin -->

| Markedsføringstilladelsesnummer | Produktnavn | Lægemiddelform | Aktive stoffer | Status |
|---------|------|------|------|------|
| 28106444820 | Veklury | koncentrat til infusionsvæske, opløsning | Remdesivir | Gyldig |
| 28106485920 | Veklury | pulver til koncentrat til infusionsvæske, opløsning | Remdesivir | Gyldig |

Tabellen viser alle 2 markedsføringstilladelser til humane lægemidler med dette aktive stof i Lægemiddelstyrelsens lister over godkendte og afregistrerede lægemidler; gyldige tilladelser står først.

<!-- licenses:end -->

Tilladelserne gælder enkeltstofpræparatet Veklury (antal og status: se Hurtigt overblik og tabellen ovenfor).

<!-- review:begin dk-lic-20261124b-remdesivir-1 -->

> **Rettelse ved gennemgang (2026-11-24)**: Oprindeligt stod der: "Antal tilladelser: 1 (enkeltstofpræparat, gyldig)." Rettet efter Lægemiddelstyrelsens liste over godkendte lægemidler (data fra 2026-11-05): Listen har tilladelser til Veklury både som koncentrat og som pulver, ikke én. Antal og status for tilladelserne vedligeholdes af programmet i Hurtigt overblik og i tabellen under markedsinformationen. Kilde: [Lægemiddelstyrelsen: liste over godkendte lægemidler](https://laegemiddelstyrelsen.dk/en/sideeffects/find-medicines/lists-with-information-about-medicines/).

<!-- review:end dk-lic-20261124b-remdesivir-1 -->

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

<!-- review:begin log -->

## Gennemgangslog

Nedenfor er gennemgangsloggen for denne side: udsagn kontrolleret mod Lægemiddelstyrelsens liste over godkendte lægemidler. Rettelser er begrænset til grundlæggende faktuelle udsagn; modelforudsigelser, evidensniveauer og konklusioner er ikke omskrevet. Sætningen om, at data om virkningsmekanismen ikke var tilgængelige, er erstattet med et uddrag fra den angivne officielle produktinformation (med uofficiel oversættelse).

| Gennemgået | Punkt | Handling | Kilde |
|------|------|------|------|
| 2026-11-19 | Sætningen »data om virkningsmekanismen er ikke tilgængelige« erstattet med uddrag fra den amerikanske produktinformation | Sætning om manglende data om virkningsmekanismen erstattet med et uddrag med kilde | [DailyMed: Veklury (remdesivir) prescribing information, Gilead Sciences, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=c0978fa8-53ff-4ca2-82a7-567fd3e958ca) |
| 2026-11-24 | Antal tilladelser: 1 (enkeltstofpræparat, gyldig). | Rettet | [Lægemiddelstyrelsen: liste over godkendte lægemidler](https://laegemiddelstyrelsen.dk/en/sideeffects/find-medicines/lists-with-information-about-medicines/) |

<!-- review:end log -->

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

