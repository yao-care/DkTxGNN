---
layout: default
title: Riociguat
parent: Kun modelforudsigelse (L5)
nav_order: 379
evidence_level: L5
indication_count: 10
---

# Riociguat
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

# Riociguat: Fra Pulmonal Arteriel Hypertension til Ambras Type Hypertrichosis Universalis Congenita

## En Sætning Sammenfatning

Riociguat er en opløseligt guanylat cyclase (sGC)-stimulator, der er refereret i denne bevisspakkes egne mekanistiske annotationer som værende brugt til pulmonal arteriel hypertension (PAH) og kronisk tromboembolisk pulmonal hypertension (CTEPH) — selvom dette ikke kan formelt bekræftes, da lægemidlets oprindelige indikation og virkningsmekanisme er flagget som datahuller i denne bevisspakke. TxGNN-modellens topforudsigelse er **Ambras Type Hypertrichosis Universalis Congenita**, et sjældet medfødt hårvækstsynd rom, men denne forudsigelse understøttes i øjeblikket af **0 kliniske forsøg** og **0 publikationer**.

## Hurtig Oversigt

| Emne | Indhold |
|------|---------|
| Oprindelig Indikation | Ikke bekræftet i denne bevisspakke (refereret kun uformelt som PAH/CTEPH i interne begrundelsesnoter — se Datahuller) |
| Forudsagt Ny Indikation | Ambras Type Hypertrichosis Universalis Congenita |
| TxGNN-forudsigelsesscore | 94.92% |
| Bevisniveau | L5 |
| Markedsstatus i Danmark | Ikke markedsført |
| Antal Markedsføringstilladelser | 0 |
| Anbefalet Beslutning | Aflyst |

## Hvorfor er Denne Forudsigelse Rimelig?

Detaljerede virkningsmekanisme-data for Riociguat er ikke tilgængelige i denne bevisspakke (flagget som et alvorligt datahul, DG002). Interne begrundelsesannotationer knyttet til lavere-rangerede kandidater i denne samme bevisspakke noterer, at Riociguat farmakologisk er kendt som en sGC-stimulator, der øger intracellulær cGMP, hvilket frembringer slappelse af vaskulær glat muskulatur — grundlaget for dets etablerede anvendelse i PAH/CTEPH. Denne information er ubekræftet, afventende formel MOA-bekræftelse via DrugBank-API.

For den toprangerede forudsigelse, Ambras-type hypertrichosis universalis congenita, er der ingen plausibel patofysiologisk forbindelse til denne vaskulære sGC/cGMP-mekanisme. Dette er et sjældet medfødt hårvæktsyndrom med et genetisk grundlag uden forbindelse til vaskulær glat muskulatur-signalering. Forudsigelsen afspejler kun en høj TxGNN-model-score, uden bekræftende mekanistisk, klinisk eller litteratur-signal.

Det er også værd at bemærke, at de ti forudsagte indikationer returneret i denne bevisspakke kollapser til fem unikke sygdomme, hver dubleret. Alle fem (hypertrichosis-type lidelser, et tanddannelses- og/eller parodontalt malformationssyndrom, og Dandy-Walker malformationssyndrom) er sjældne medfødte eller strukturelle syndromer uden etableret forbindelse til vaskulær sGC/cGMP farmakologi, og alle er scoret L5/Aflyst i de underliggende data.

## Bevis fra Kliniske Forsøg

I øjeblikket ingen relaterede kliniske forsøg registreret.

## Litteraturbevis

I øjeblikket ingen relateret litteratur tilgængelig.

*Bemærk: En lavere-rangeret kandidat i denne samme bevisspakke ("malformationssyndrom med tanddannelses- og/eller parodontal komponent," rangering 3–4) returnerede 20 PubMed-hits, men manuel gennemgang fandt disse at være generelle parodontologi-artikler uden omtale af Riociguat eller sGC-stimulatorer — vurderet som søgeordsamfald-støj snarere end lægemiddelspecifikt bevis, og tælles ikke mod den toprangerede kandidat ovenfor.*

## Markedsinformation i Danmark

Ingen markedsføringstilladelser for Riociguat er i øjeblikket registreret i denne bevisspakke. Markedsstatus: Ikke markedsført (0 licenser på fil).

## Sikkerhedshensyn

Venligst se det godkendt sammendrag af produktkarakteristika (SmPC) for sikkerhedsoplysninger.

## Konklusion og Næste Trin

**Beslutning: Aflyst**

**Begrundelse:**
Den toprangerede forudsagte indikation har ingen mekanistisk begrundelse, ingen bevis fra kliniske forsøg og ingen litteraturstøtte — kun en rå TxGNN-model-score. Kombineret med et uløst blokerend datahul (produktetiket/advarsler, DG001) og en ubekræftet virkningsmekanisme (DG002), opfylder denne kandidat ikke tærsklen for at komme videre forbi initial screening.

**For at fortsætte, kræves følgende:**
- Dansk/EU SmPC eller produktetiketoplysninger (advarsler, kontraindikationer) — blokerer i øjeblikket (DG001)
- MOA-verifikation via DrugBank-API — høj-prioritets gab i øjeblikket (DG002)
- Bekræftelse af Riociguat's oprindelige godkendt indikation og regulatorisk status i Danmark/EU
- Hvis det forfølges yderligere, en målrettet litteratur- og mekanisme-søgning specifik for hypertrichosis-patofysiologi, snarere end at stole på automatiseret model-score alene

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

