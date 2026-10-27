---
layout: default
title: Vildagliptin
parent: Kun modelforudsigelse (L5)
nav_order: 886
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Vildagliptin: forudsagt ny indikation Klassisk stiff person-syndrom (evidensniveau L5). Oprindelig indikation: Type 2-diabetes mellitus"
monitor_inn: "VILDAGLIPTIN"
predicted_indications: ["classic stiff person syndrome", "focal stiff limb syndrome", "focal stiff limb syndrome", "classic stiff person syndrome", "thiamine-responsive dysfunction syndrome", "thiamine-responsive dysfunction syndrome", "opsismodysplasia", "opsismodysplasia", "drug-induced localized lipodystrophy", "drug-induced localized lipodystrophy"]
---

# Vildagliptin
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

## Vildagliptin: Fra type 2-diabetes til klassisk stiff person-syndrom
{: .text-alpha }

## Resumé i én sætning

Vildagliptin er et lægemiddel, der oprindeligt anvendes til behandling af type 2-diabetes mellitus. TxGNN-modellen forudsiger, at det kan have effekt på **klassisk stiff person-syndrom** (og den beslægtede variant fokalt stiff limb-syndrom), men der er **ingen registrerede kliniske forsøg** og **ingen publikationer**, der understøtter forudsigelsen. Den er derfor udelukkende baseret på modelberegning.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Type 2-diabetes mellitus (indikationsteksten i den danske godkendelse er ikke angivet i de indsamlede data) |
| Forudsagt ny indikation | Klassisk stiff person-syndrom |
| TxGNN-forudsigelsesscore | 99,88 % |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført |
| Antal markedsføringstilladelser | 1 |
| Anbefalet beslutning | Hold |

---

## Hvorfor kan forudsigelsen give mening?

De data, der er indsamlet til denne rapport, indeholder ingen oplysninger om lægemidlets virkningsmekanisme. Vildagliptin er kendt som en hæmmer af enzymet dipeptidylpeptidase-4 (DPP-4), og dette understøttes af farmakologidata, der også viser binding til DPP-8 og DPP-9 samt TRPV4. Hæmning af DPP-4 øger niveauet af inkretinhormoner og sænker dermed blodsukkeret ved type 2-diabetes.

Stiff person-syndrom er en sjælden autoimmun neurologisk lidelse, der er forbundet med forstyrret GABAerg signaloverførsel (typisk anti-GAD65-antistoffer). Der er ikke noget etableret mekanistisk led mellem DPP-4-hæmning eller inkretinsystemet og denne sygdom. En eventuel sammenhæng er derfor spekulativ. Fokalt stiff limb-syndrom betragtes som en variant inden for samme sygdomsspektrum og har samme spekulative begrundelse.

Den høje score (99,88 %) er et rent modelresultat og bør ikke tolkes som klinisk evidens.

**Øvrige forudsagte indikationer** (alle med samme score-niveau, evidensniveau L5 og ingen forsøg eller publikationer):

| Forudsagt indikation | TxGNN-score | Bemærkning |
|------|------|------|
| Fokalt stiff limb-syndrom | 99,88 % | Variant inden for stiff person-spektret |
| Thiaminresponsivt dysfunktionssyndrom | 99,87 % | Sjælden genetisk forstyrrelse af thiaminstofskiftet; ingen kendt forbindelse til vildagliptin |
| Opsismodysplasi | 99,86 % | Sjælden skeletdysplasi (INPPL1-mutationer, insulin/PI3K-signalering); en indirekte forbindelse er tænkelig, men ikke understøttet |
| Lægemiddelinduceret lokaliseret lipodystrofi | 99,79 % | Løs konceptuel forbindelse til stofskifteforstyrrelser; vildagliptins rolle er uklar |

---

## Evidens fra kliniske forsøg

Der er i øjeblikket ingen relaterede kliniske forsøg registreret.

---

## Litteraturevidens

Der foreligger i øjeblikket ingen relateret litteratur.

---

## Markedsinformation for Danmark

| Markedsføringstilladelse | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28103990706 | Galvus (Novartis Europharm Limited) | Tabletter | Indikationstekst ikke tilgængelig i de indsamlede data |

Produktet er et monopræparat med gyldig status og er til oral anvendelse.

---

## Sikkerhedsovervejelser

**Lægemiddelinteraktioner:** Interaktionsforespørgslen er gennemført. Der blev ikke fundet interaktioner med andre lægemidler, men farmakologidata viser følgende molekylære mål for vildagliptin:

- Dipeptidylpeptidase 4 (DPP-4), det primære terapeutiske mål
- Dipeptidylpeptidase 8 (DPP-8)
- Dipeptidylpeptidase 9 (DPP-9)
- TRPV4

Hæmning af DPP-8/DPP-9 og binding til TRPV4 er relevant at have in mente ved vurdering af eventuelle uventede virkninger i en ny patientgruppe.

Oplysninger om advarsler og kontraindikationer er ikke tilgængelige i de indsamlede data. Se det godkendte produktresumé (SmPC) for fuldstændige sikkerhedsoplysninger.

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelsen er udelukkende baseret på modelberegning (evidensniveau L5). Der findes hverken kliniske forsøg eller publikationer, og der er ingen plausibel, dokumenteret mekanistisk forbindelse mellem DPP-4-hæmning og stiff person-syndrom. Desuden mangler sikkerhedsoplysninger fra produktresuméet, hvilket udgør en blokerende datamangel for videre sikkerhedsscreening.

**For at komme videre kræves følgende:**
- Hentning og gennemgang af produktresuméet (SmPC) for Galvus med advarsler, kontraindikationer og godkendt indikationstekst
- Fuldstændige mekanismedata for vildagliptin (fx fra DrugBank)
- Litteratursøgning og søgning i forsøgsregistre efter sammenhæng mellem DPP-4-hæmning/inkretinveje og stiff person-syndrom (herunder autoimmunitet og GABAerg signalering)
- Prækliniske data eller mekanistiske studier, der kan understøtte hypotesen, før et klinisk forsøg overvejes
- Vurdering af, om forudsigelsen er biologisk meningsfuld, da modellen giver næsten ens høje scorer for flere indbyrdes uafhængige sjældne sygdomme
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

