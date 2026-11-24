---
layout: default
title: Evolocumab
parent: Kun modelforudsigelse (L5)
nav_order: 342
evidence_level: L5
indication_count: 6
monitor_inn: "Evolocumab"
predicted_indications: ["symptomatic form of hemophilia in female carriers", "familial apolipoprotein C-II deficiency", "thrombocytopenic purpura", "factor XI deficiency", "hemophilia A with vascular abnormality", "disease of catalytic activity"]
last_modified_at: 2026-11-24
description: "Evolocumab: forudsagt ny indikation Symptomatisk hæmofili hos kvindelige bærere (evidensniveau L5). Oprindelig indikation: Homozygot familiær hyperkolesterolæmi og syndromisk dyslipidæmi"
---

# Evolocumab
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

## Evolocumab: Fra homozygot familiær hyperkolesterolæmi til symptomatisk hæmofili hos kvindelige bærere
{: .text-alpha }

## Resumé i en sætning

Evolocumab er et monoklonalt antistof mod PCSK9, som i videnbasen (knowledge graph) er registreret i relation til homozygot familiær hyperkolesterolæmi og syndromisk dyslipidæmi.
TxGNN-modellen forudsiger, at lægemidlet kan have effekt ved **symptomatisk hæmofili hos kvindelige bærere**, men der er **0 kliniske forsøg** og **0 publikationer**, der understøtter denne retning. Forudsigelsen er kun modelbaseret.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Homozygot familiær hyperkolesterolæmi og syndromisk dyslipidæmi (relation registreret i videnbasen; godkendelsesteksten i den danske registrering er ikke tilgængelig) |
| Forudsagt ny indikation | Symptomatisk hæmofili hos kvindelige bærere |
| TxGNN-forudsigelsesscore | 0,9982 |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført (gyldige tilladelser: 3 af 3) |
| Antal markedsføringstilladelser | 3 (gyldige: 3) |
| Anbefalet beslutning | Hold |

---

## Hvorfor er denne forudsigelse (ikke) rimelig?

Evolocumab er et antistof, der binder PCSK9 og blokerer dets virkning uden for cellen. Dermed bevares flere LDL-receptorer på leverceller, og LDL-kolesterol i blodet falder. Ifølge afsnittet »Mechanism of Action« i den produktinformation, som den amerikanske FDA har godkendt (Prescribing Information), for Evolocumab (uofficiel oversættelse): »Evolocumab er et humant monoklonalt IgG2 rettet mod human proproteinkonvertase subtilisin/kexin type 9 (PCSK9). PCSK9 bindes til low-density lipoprotein-receptoren (LDLR) på overfladen af hepatocytter og fremmer nedbrydningen af LDLR i leveren.« Engelsk originaltekst: "Evolocumab is a human monoclonal IgG2 directed against human proprotein convertase subtilisin kexin type 9 (PCSK9). PCSK9 binds to the low-density lipoprotein receptor (LDLR) on the surface of hepatocytes to promote LDLR degradation within the liver." ([DailyMed: Repatha (evolocumab) prescribing information, Amgen USA Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=cd61e902-166d-4aa6-9f3c-a18c1008d07e), version af 2026-10-12; hentet 2026-11-19).

Der er ikke identificeret nogen plausibel biologisk sammenhæng mellem denne mekanisme og den forudsagte sygdom. Symptomatisk hæmofili hos kvindelige bærere skyldes nedsat aktivitet af faktor VIII eller IX som følge af X-bundne varianter og skæv X-inaktivering. PCSK9-hæmning påvirker ikke koagulationsfaktorer.

Den høje score (0,9982) er en grafbaseret forudsigelse uden understøttende kliniske data eller litteratur og afspejler sandsynligvis nærhed i netværket frem for biologi.

Øvrige forudsagte indikationer i de indsamlede data er heller ikke understøttet af studier. Den mest biologisk nærliggende er familiær apolipoprotein C-II-mangel (score 0,9950), men her er rationalet svagt: sygdommen skyldes defekt aktivering af lipoproteinlipase med svær hypertriglyceridæmi, mens PCSK9-hæmning primært sænker LDL-kolesterol.

---

## Klinisk evidens fra forsøg

Der er ingen relaterede kliniske forsøg registreret.

## Litteraturevidens

Der er ingen relateret litteratur tilgængelig.

---

## Information om det danske marked

<!-- licenses:begin -->

| Markedsføringstilladelsesnummer | Produktnavn | Lægemiddelform | Aktive stoffer | Status |
|---------|------|------|------|------|
| 28105697715 | Repatha | injektionsvæske, opløsning i cylinderampul | Evolocumab | Gyldig |
| 28105504414 | Repatha | injektionsvæske, opløsning i fyldt injektionssprøjte | Evolocumab | Gyldig |
| 28105504514 | Repatha | injektionsvæske, opløsning i fyldt pen | Evolocumab | Gyldig |

Tabellen viser alle 3 markedsføringstilladelser til humane lægemidler med dette aktive stof i Lægemiddelstyrelsens lister over godkendte og afregistrerede lægemidler; gyldige tilladelser står først.

<!-- licenses:end -->

---

## Sikkerhedsovervejelser

- **Lægemiddelinteraktioner**: Der er kun registreret en farmakologisk målrelation (PCSK9), ikke interaktioner med andre lægemidler af klinisk betydning.

Se i øvrigt det godkendte produktresumé (SmPC) for oplysninger om advarsler og kontraindikationer.

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelsen bygger udelukkende på en grafbaseret model uden kliniske forsøg eller publikationer, og der er ingen plausibel mekanistisk forbindelse mellem PCSK9-hæmning og hæmofili hos kvindelige bærere. Evidensniveauet er L5.

**For at komme videre kræves følgende:**
- Hentning og gennemgang af produktresuméet (SmPC) fra Lægemiddelstyrelsen, herunder godkendt indikation, advarsler og kontraindikationer
- Detaljerede data om virkningsmekanisme
- Prækliniske eller kliniske data, der direkte undersøger evolocumab ved den forudsagte sygdom, før en videre vurdering er meningsfuld
- Overvejelse af, om andre kandidater (fx familiær apolipoprotein C-II-mangel) fortjener en separat, målrettet vurdering

<!-- review:begin log -->

## Gennemgangslog

Nedenfor er gennemgangsloggen for denne side. Sætningen om, at data om virkningsmekanismen ikke var tilgængelige, er erstattet med et uddrag fra den angivne officielle produktinformation (med uofficiel oversættelse); modelforudsigelser, evidensniveauer og konklusioner er ikke omskrevet.

| Gennemgået | Punkt | Handling | Kilde |
|------|------|------|------|
| 2026-11-19 | Sætningen »data om virkningsmekanismen er ikke tilgængelige« erstattet med uddrag fra den amerikanske produktinformation | Sætning om manglende data om virkningsmekanismen erstattet med et uddrag med kilde | [DailyMed: Repatha (evolocumab) prescribing information, Amgen USA Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=cd61e902-166d-4aa6-9f3c-a18c1008d07e) |

<!-- review:end log -->

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

