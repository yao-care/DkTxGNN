---
layout: default
title: Belimumab
parent: Kun modelforudsigelse (L5)
nav_order: 100
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Belimumab: forudsagt ny indikation Primær frigivelsesforstyrrelse af blodplader (evidensniveau L5). Oprindelig indikation: Systemisk lupus erythematosus (SLE) og pædiatrisk SLE"
---

# Belimumab
{: .fs-9 }

Evidensniveau: **L5** | Forudsagte indikationer: **10** stk.
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

# Belimumab: Fra systemisk lupus erythematosus til primær frigivelsesforstyrrelse af blodplader

## Resumé i én sætning

Belimumab er et monoklonalt antistof, der oprindeligt anvendes til behandling af systemisk lupus erythematosus (SLE), herunder pædiatrisk SLE.
TxGNN-modellen forudsiger, at det kan have effekt ved **primær frigivelsesforstyrrelse af blodplader**,
men der er **ingen kliniske forsøg** og **ingen publikationer** i de indsamlede data, der understøtter denne retning. Forudsigelsen er udelukkende modelbaseret.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Systemisk lupus erythematosus (SLE) og pædiatrisk SLE |
| Forudsagt ny indikation | Primær frigivelsesforstyrrelse af blodplader |
| TxGNN-forudsigelsesscore | 99,96 % |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført |
| Antal markedsføringstilladelser | 1 |
| Anbefalet beslutning | Hold |

---

## Hvorfor er denne forudsigelse rimelig?

Der foreligger i øjeblikket ingen detaljerede data om virkningsmekanismen i de indsamlede data. Belimumab er dog kendt som et antistof, der neutraliserer BLyS (BAFF). Det nedsætter B-cellers overlevelse og dermed produktionen af autoantistoffer, hvilket er grundlaget for effekten ved SLE.

Den forudsagte indikation har **ingen klar mekanistisk forbindelse** til den oprindelige. Primære frigivelsesforstyrrelser af blodplader er typisk arvelige eller iboende defekter i trombocytfunktionen (granulesekretion eller signalering) og er ikke drevet af B-celler eller autoantistoffer. Den høje score er alene en beregningsmæssig forudsigelse og understøttes ikke af forsøg eller litteratur.

### Øvrige forudsagte indikationer

Modellen forudsagde også følgende indikationer, alle med evidensniveau L5 og anbefalingen Hold:

| Forudsagt indikation | TxGNN-score | Vurdering af mekanistisk sammenhæng |
|------|------|------|
| Pseudo-von Willebrands sygdom | 99,96 % | Ingen plausibel sammenhæng. Sygdommen skyldes en genetisk gain-of-function-defekt i trombocyt-GPIbα og er ikke immunmedieret. |
| Glanzmanns trombasteni | 99,88 % | Svag og indirekte. Sygdommen skyldes arvelig mangel på integrin αIIbβ3. Teoretisk relevans kun ved alloantistoffer efter trombocyttransfusion, hvilket er spekulativt. |
| Føtal og neonatal alloimmun trombocytopeni (FNAIT) | 99,59 % | Biologisk den mest plausible, men uunderbygget. Reduceret antistofproduktion er konceptuelt sammenhængende, men belimumab (IgG1) passerer placenta, data om graviditetssikkerhed er begrænsede, og effekten på allerede etablerede plasmaceller er usikker. Nuværende behandling er IVIG med eller uden kortikosteroider. |
| Svær non-proliferativ diabetisk retinopati | 99,05 % | Ingen direkte sammenhæng. Sygdommen er primært drevet af hyperglykæmi-induceret mikrovaskulær skade og VEGF. Immunsuppression ville give infektionsrisiko uden understøttende rationale. |

---

## Klinisk evidens fra forsøg

Der er i øjeblikket ingen relaterede kliniske forsøg registreret.

---

## Litteraturevidens

Der er i øjeblikket ingen relateret litteratur tilgængelig.

---

## Information om det danske marked

| Markedsføringstilladelsesnummer | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28105851916 | Benlysta (GlaxoSmithKline (Ireland) Limited) | Injektionsvæske, opløsning i fyldt injektionssprøjte | Indikationstekst ikke tilgængelig i de indsamlede data |

---

## Sikkerhedsovervejelser

**Lægemiddelinteraktioner:** Der blev fundet i alt 69 registrerede interaktioner. Blandt de interaktioner, der indgår i de indsamlede data, er de vigtigste:

- **Alvorlig (Major):** adalimumab, baricitinib, certolizumab pegol samt levende BCG-vaccine (Bacillus Calmette-Guérin).
- **Moderat:** blandt andet roflumilast, azathioprin, anakinra, canakinumab, alemtuzumab, alefacept, tetanustoksoid samt flere vacciner (bl.a. miltbrand, adenovirus, kolera og *Candida albicans*-antigen).
- **Mindre (Minor):** zinkforbindelser (acetat, gluconat, sulfat og chlorid).

Generelt gælder, at kombination med andre immunsuppressiva eller biologiske lægemidler samt levende vacciner kræver særlig opmærksomhed.

For advarsler og kontraindikationer henvises til det godkendte produktresumé (SmPC), da disse data ikke var tilgængelige.

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelsen hviler udelukkende på modelscoren (evidensniveau L5). Der er ingen kliniske forsøg eller publikationer, og der er ingen klar mekanistisk forbindelse mellem BLyS-hæmning og primære frigivelsesforstyrrelser af blodplader.

**For at komme videre kræves:**
- Data om virkningsmekanisme (MOA) fra DrugBank
- Advarsler og kontraindikationer fra produktresuméet hos Lægemiddelstyrelsen (afgørende for sikkerhedsscreening)
- Præklinisk eller mekanistisk dokumentation for en rolle for B-celler/BLyS i den forudsagte sygdom
- Hvis der ønskes en prioritering, bør FNAIT undersøges først som den biologisk mest plausible kandidat, med særlig vægt på graviditetssikkerhed
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

