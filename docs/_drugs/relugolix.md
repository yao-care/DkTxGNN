---
layout: default
title: Relugolix
parent: Kun modelforudsigelse (L5)
nav_order: 370
evidence_level: L5
indication_count: 10
---

# Relugolix
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

# Relugolix: Fra avanceret prostatakræft til nefrogen syndrom med upassende antidiurese

## En-linjers sammenfatning

Relugolix (DrugBank DB11853) er en oral GnRH-receptorantagonist, hvis etablerede anvendelse er i hormon-sensitive tilstande såsom avanceret prostatakræft og uterusknopler/endometriose. TxGNN-modellen forudsiger, at det kan være effektivt for **nefrogen syndrom med upassende antidiurese (NSIAD)**, men denne forudsigelse understøttes i øjeblikket af **ingen registrerede kliniske forsøg og ingen publiceret litteratur** — det er et signal baseret kun på modellen.

---

## Hurtigt overblik

| Punkt | Indhold |
|-------|---------|
| Original indikation | Ikke dokumenteret i denne bevisspakke (ingen licens på fil); eksternt kendt klasseanvendelse er avanceret prostatakræft og hormonafhængige gynækologiske tilstande |
| Forudsagt ny indikation | Nefrogen syndrom med upassende antidiurese |
| TxGNN-forudsigelsesscore | 96.13% |
| Bevisniveau | L5 |
| Status på det danske marked | Ikke markedsført |
| Antal markedsføringstilladelser | 0 |
| Anbefalet beslutning | Afhold |

---

## Hvorfor er denne forudsigelse rimelig?

I øjeblikket er detaljerede mekanismedata for Relugolix ikke tilgængelige i denne bevisspakke. Baseret på kendt farmakologi er Relugolix en oral **GnRH-receptorantagonist (gonadotropin-releasing hormon)** — den samme lægemiddelklasse som refereret andre steder i dette datasæts mekanistiske begrundelse for andre kandidatindikationer (f.eks. dets undertrykkelse af den gonadale hormonakse). Dens etablerede effektivitet er bygget på undertrykkelse af kønshormonproduktion, som er mekanistisk adskilt fra patofysiologien af NSIAD.

NSIAD er en sjælden, typisk medfødt lidelse forårsaget af **gain-of-function-mutationer i vasopressin V2-receptoren**, hvilket fører til upassende ferskvandsretention uafhængigt af gonadale hormonsignalering. Ingen direkte eller indirekte mekanistisk vej, der forbinder GnRH-receptorantagonisme til V2-receptor-drevet vandretention, er dokumenteret i denne bevisspakke — `repurposing_rationale.mechanistic_link`-feltet for denne indikation er eksplicit markeret som endnu ikke analyseret ("pending").

I betragtning af fraværet af en underbygget mekanistisk forbindelse, understøttende forsøg eller litteratur, bør denne forudsigelse behandles som en tidlig-fase hypotese genereret udelukkende fra TxGNN-kendskabsgraf-embeddings, ikke som et farmakologisk valideret signal.

---

## Evidens fra kliniske forsøg

I øjeblikket ingen relaterede kliniske forsøg registreret.

*(Forespørgelseslog bekræfter, at ClinicalTrials.gov og ICTRP-søgninger efter "Relugolix" + "nefrogen syndrom med upassende antidiurese" returnerede nul resultater pr. 2026-03-24.)*

---

## Litteraturbevis

I øjeblikket ingen relateret litteratur tilgængelig.

*(PubMed-søgning efter "Relugolix" + "nefrogen syndrom med upassende antidiurese" returnerede nul resultater pr. 2026-03-24.)*

---

## Oplysninger om det danske marked

Relugolix har i øjeblikket ingen markedsføringstilladelse i Danmark (0 licenser på fil; markedsstatus: Ikke markedsført). Ingen nationale (Lægemiddelstyrelsen) eller centraliserede (EMA) autoriseringsdata er tilgængelige i denne bevisspakke.

---

## Sikkerhedshensyn

Se venligst den godkendte produktinformationsbog (SmPC) for sikkerhedsinformation.

*(Bemærk: vigtige advarsler, kontraindikationer og lægemiddelinteraktionsdata er alle uregistreret i denne bevisspakke. Dette er markeret som en blokerende datamanko — se Konklusion nedenfor.)*

---

## Konklusion og næste trin

**Beslutning: Afhold**

**Begrundelse:**
- Forudsigelsen hviler kun på TxGNN-modeloutput (Bevisniveau L5), med nul kliniske forsøg, nul litteratur og ingen dokumenteret mekanistisk vej, der forbinder GnRH-antagonisme med NSIAD-patofysiologi.
- Relugolix er ikke markedsført i Danmark og har ingen sikkerhed/etiket-data på fil, så ingen sikkerhedsbaseline eksisterer for at understøtte selv eksplorativ brug.

**For at fortsætte er følgende påkrævet:**
- SmPC-advarsler, kontraindikationer og interaktionsdata (Blokerende datamanko — påkrævet før ethvert S1-sikkerhedsscreening kan finde sted)
- Mekanisme-af-virkning (MOA) dokumentation fra DrugBank eller tilsvarende kilde
- En farmakologisk eller preklinisk begrundelse, der specifikt forbinder GnRH-receptorantagonisme med vasopressin V2-receptor-medieret vandretention
- Bekræftelse af oprindelig godkendt indikation(er) og eksisterende erfaringer med sikkerhed fra virkeligheden, da ingen oprindelige indikationsdata i øjeblikket er på fil

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

