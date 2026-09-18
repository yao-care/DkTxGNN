---
layout: default
title: Reteplase
parent: Moderat evidens (L3-L4)
nav_order: 373
evidence_level: L4
indication_count: 10
---

# Reteplase
{: .fs-9 }

Evidensniveau: **L4** | Forudsagte indikationer: **10** stk.
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

# Reteplase: Fra Akut Myokardieinfarkt (STEMI) til Posteroinferior Myokardieinfarkt

## Et-linjers sammenfatning

Reteplase er en rekombinant vævsplasminogenaktivator (r-tPA-variant) brugt som trombolitisk terapi til akut ST-elevation myokardieinfarkt (STEMI). TxGNN-modellens højest rangerede forudsigelse, **Posteroinferior Myokardieinfarkt**, markeres af bevisemballagen selv som en anatomisk subtype af reteplases *eksisterende* MI-indikation snarere end en ægte ny indikation, og den understøttes af **0 kliniske forsøg** og **0 publikationer**. Et mere væsentligt signal findes længere nede på kandidatlisten — **Septal Myokardieinfarkt** (rang 5–6) er bakket op af et afsluttet fase 3 RCT (n=2,461).

---

## Hurtig oversigt

| Emne | Indhold |
|------|--------|
| Oprindelig indikation | Akut myokardieinfarkt (STEMI) — trombolitisk terapi (ifølge repurposing-rationale-teksten i bevisemballagen; ikke bekræftet mod et dansk produktresumé, da produktet i øjeblikket ikke har dansk markedsføringstilladelse) |
| Forudsagt ny indikation | Posteroinferior Myokardieinfarkt *(anatomisk subtype af den eksisterende indikation — se forbehold nedenfor)* |
| TxGNN-forudsigelsesscore | 99.90% |
| Bevisniveau | L4 |
| Markedsstatus i Danmark | Ikke markedsført |
| Antal markedsføringstilladelser | 0 |
| Anbefalet beslutning | Afventer |

---

## Hvorfor er denne forudsigelse rimelig?

Data om mekanisme for virkemåde (MOA) for reteplase er i øjeblikket ikke tilgængelig i denne bevisemballage [DG002]. Baseret på kendt farmakologi er reteplase en tredje-generations rekombinant plasminogenaktivator (en konstrueret tPA-variant), der katalyserer omdannelse af plasminogen til plasmin, hvilket opløser fibrinkoagler i tillukkede koronararterier — grundlaget for dets godkendte brug ved akut MI/STEMI.

**Vigtigt forbehold vedrørende den højest rangerede kandidat:** bevisemballagen selv angiver, at "posteroinferior myokardieinfarkt" ikke er en ægte ny indikation. TxGNN's næsten identiske scores på tværs af ranger 1–4 (posteroinferior MI, posterolateral MI) afspejler semantisk overlap i vidensgrafen mellem MI-anatomiske subtyper og MI generelt, ikke et nyt mekanistisk link. Ingen uafhængige forsøg eller litteratur blev fundet for disse subtype-mærkede termer. Dette bør behandles som en **ontologiartefakt** — en udvidelse af den eksisterende indikation snarere end en repurposing-kandidat.

Et mere ægte signal fremgår af rang 5–6, **Septal Myokardieinfarkt**, understøttet af et afsluttet multiceentralt, dobbelt-blindet, placebo-kontrolleret fase 3 RCT (NCT00046228, n=2,461), der evaluerer reteplase plus abciximab ved akut MI — direkte på mekanisme, og evalueret ved beslutningsstadium S3 med en anbefaling om "Fortsæt med sikkerhedsbetingelser". Ranger 9–10 (**koronarstenose**) er på samme måde understøttet af flere observationelle/kohort-studier (GUSTO-V, SPEED/GUSTO-4 pilot) i overensstemmelse med reteplases kernefibrinolytiske mekanisme, selvom ingen forsøg er registreret under det præcise sygdomslabel.

---

## Bevis fra kliniske forsøg

I øjeblikket er der ingen relaterede kliniske forsøg registreret for **Posteroinferior Myokardieinfarkt** (den nr. 1-rangerede kandidat).

*Som reference vedrører de vigtigste forsøgsbeviser i denne bevisemballage Septal Myokardieinfarkt (rang 5–6):*

| Forsøgsnummer | Fase | Status | Tilmelding | Vigtige resultater |
|---------|------|------|------|---------|
| [NCT00046228](https://clinicaltrials.gov/study/NCT00046228) | Fase 3 | Afsluttet | 2,461 | Multiceentralt, randomiseret, dobbelt-blindet, placebo-kontrolleret forsøg, der sammenligner reteplase + abciximab-kombinationsterapi mod abciximab alene før primær PCI ved akut MI. |

---

## Litteraturbevis

I øjeblikket er der ingen relateret litteratur tilgængelig for **Posteroinferior Myokardieinfarkt** (den nr. 1-rangerede kandidat).

---

## Markedsinformation for Danmark

Reteplase har i øjeblikket **0 markedsføringstilladelser** i Danmark (`market_status: Not marketed / Not marketed`). Der er ingen Laegemiddelstyrelsen-nationale eller EMA-centraliserede licensregistreringer til stede i denne bevisemballage.

---

## Sikkerhedsmæssige overvejelser

Venligst se det godkendte Produktresumé (SmPC) for sikkerhedsinformation. Vigtige advarsler, kontraindikationer og data om lægemiddelinteraktioner var ikke tilgængelige i denne bevisemballage [DG001 — Blokering: TFDA/SmPC-mærkat ikke endnu hentet].

---

## Konklusion og næste trin

**Beslutning: Afventer**

**Begrundelse:**
Den højest rangerede kandidat (Posteroinferior Myokardieinfarkt) er en anatomisk subtype af reteplases eksisterende godkendt indikation snarere end et nyt repurposing-signal, har ingen understøttende forsøg eller litteratur, og markeres eksplicit i bevisemballagen som en vidensgrafs ontologiartefakt. Kombineret med den blokerende mangel på dansk etiket/sikkerhedsdata (DG001) og manglende MOA-bekræftelse (DG002), kan denne kandidat ikke fortsætte forbi indledende screening.

**For at fortsætte er følgende nødvendig:**
- Dansk SmPC / lovgivningsmæssig mærkat (advarsler, kontraindikationer, DDI) — blokerer i øjeblikket (DG001)
- Bekræftet mekanisme for virkemådedata fra DrugBank (DG002)
- En beslutning om hvorvidt MI-anatomiske-subtype-forudsigelser (ranger 1–4, 7–8) skal udelukkes fra kandidatpipelinen som ontologiduplikater, eller gen-scores mod den overordnede "myokardieinfarkt"-indikation
- Hvis du forfølger en bevisunderbygget kandidat i stedet, **Septal Myokardieinfarkt** (L1-bevis, fase 3 RCT, "Fortsæt med sikkerhedsbetingelser") og **Koronarstenose** (L3-bevis, flere kohort-studier) berettiger til separat evaluering som de mere væsentlige repurposing-signaler i denne bevisemballage

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

