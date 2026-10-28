---
layout: default
title: Brodalumab
parent: Kun modelforudsigelse (L5)
nav_order: 133
evidence_level: L5
indication_count: 10
monitor_inn: "Brodalumab"
predicted_indications: ["strongyloidiasis", "eye disease", "vitamin deficiency disorder", "von Hippel anomaly", "isolated optic neuritis", "recurrent idiopathic neuroretinitis", "chronic relapsing inflammatory optic neuropathy", "optic perineuritis", "episcleritis periodica fugax", "nodular episcleritis"]
last_modified_at: 2026-10-23
description: "Brodalumab: forudsagt ny indikation Strongyloidiasis (evidensniveau L5). Oprindelig indikation: Ikke angivet i de indsamlede data"
---

# Brodalumab
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

## Brodalumab: Fra den oprindelige anvendelse til strongyloidiasis (forudsagt ny indikation)
{: .text-alpha }

## Resumé i én sætning

Brodalumab er et lægemiddel, der er markedsført i Danmark under navnet Kyntheum, men de data, der er indsamlet til denne rapport, indeholder ingen godkendt indikationstekst. TxGNN-modellen forudsiger, at lægemidlet kan have effekt mod **strongyloidiasis**, men der er **0 kliniske forsøg** og **0 publikationer** om netop denne sygdom, så forudsigelsen er rent beregningsbaseret.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Ikke angivet i de indsamlede data (licensen indeholder ingen indikationstekst) |
| Forudsagt ny indikation | Strongyloidiasis |
| TxGNN-forudsigelsesscore | 0,9984 |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført (gyldige tilladelser: 1 af 1) |
| Antal markedsføringstilladelser | 1 (gyldige: 1) |
| Anbefalet beslutning | Hold |

---

## Hvorfor er denne forudsigelse (ikke) rimelig?

Der foreligger ingen detaljerede data om virkningsmekanismen i de data, der er indsamlet til denne rapport. Brodalumab er kendt som en antagonist af IL-17-receptor A (IL-17RA), og det er den mekanisme, der er grundlaget for den følgende vurdering.

Der er ikke noget klart mekanistisk led mellem IL-17RA-blokade og strongyloidiasis. Immunforsvaret mod orme er overvejende drevet af Th2-celler. Blokade af IL-17-signalering kan i teorien forværre snarere end forbedre infektionskontrollen. Den høje TxGNN-score er derfor en beregningsmæssig forudsigelse uden støtte i kliniske data eller litteratur.

Hverken lighed med den oprindelige indikation eller administrationsvejens egnethed er vurderet, da de relevante data mangler.

---

## Klinisk forsøgsevidens

Der er i øjeblikket ingen relaterede kliniske forsøg registreret for strongyloidiasis.

---

## Litteraturevidens

Der er i øjeblikket ingen relateret litteratur for strongyloidiasis.

---

## Markedsinformation for Danmark

| Markedsføringstilladelse | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28105697815 | Kyntheum (LEO Pharma A/S) | Injektionsvæske, opløsning i fyldt injektionssprøjte | Ikke angivet i de indsamlede data |

Der er tale om 1 gyldig tilladelse til et enkeltstofpræparat.

---

## Sikkerhedsovervejelser

- **Kontraindikationer i vidensgrafen (ikke mærkningstekst):** Vidensgrafen registrerer relationer til Crohns sygdom, inflammatorisk tarmsygdom og Crohns colitis. Det er relationer fra en model, ikke bekræftede kontraindikationer fra produktresuméet.
- **Lægemiddelinteraktioner:** Der er fundet 68 interaktioner. Et udvalg:
  - **Alvorlige (Major):** adalimumab, baricitinib, certolizumab pegol, levende BCG-vaccine (Bacillus Calmette-Guérin).
  - **Moderate:** roflumilast, anakinra, canakinumab, alefacept, alemtuzumab, tetanustoksoid samt flere vacciner og levende mikroorganismer (fx anthraxvaccine, koleravaccine, adenovirusvaccine, Candida albicans, Bifidobacterium longum infantis).
  - **Mindre alvorlige (Minor):** zinksalte (acetat, gluconat, sulfat, chlorid).
- Oplysninger om advarsler og kontraindikationer fra produktresuméet er ikke tilgængelige. Se det godkendte produktresumé (SmPC) for fuldstændige sikkerhedsoplysninger, herunder eventuelle advarsler om selvmordstanker og -adfærd.

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelsen for strongyloidiasis hviler udelukkende på en modelscore uden kliniske forsøg, litteratur eller plausibel mekanisme. Evidensniveauet er L5, og blokade af IL-17 kan i teorien være ufordelagtig ved ormeinfektioner.

**For at komme videre kræves følgende:**
- Hent og gennemgå produktresuméet for Kyntheum (indikationer, advarsler, kontraindikationer) hos Lægemiddelstyrelsen.
- Indhent data om virkningsmekanisme fra DrugBank.
- Præklinisk eller mekanistisk dokumentation for en rolle af IL-17RA i værtsforsvaret mod *Strongyloides*.

---

## Øvrige forudsagte indikationer (kort)

Ingen af de øvrige forudsigelser har kliniske forsøg. Alle har anbefalingen Hold.

| Rang | Sygdom | Score | Evidensniveau | Bemærkning |
|---|---|---|---|---|
| 2 | Øjensygdom (eye disease) | 0,9982 | L5 | Biologisk plausibelt via IL-17, men litteraturen omhandler ikke effekt mod øjensygdom: en parodontitismodel, en case-rapport om Behçets sygdom opstået efter brodalumab-start og en farmakovigilansanalyse af uveitis som bivirkning. Kategorien er for bred til at vurdere som én indikation. |
| 3 | Vitaminmangeltilstand | 0,9980 | L5 | Ingen plausibel mekanisme. |
| 4 | Von Hippel-anomali | 0,9977 | L5 | Ingen etableret IL-17-drevet patologi. |
| 5–8 | Optikusneuritis og beslægtede optiske neuropatier (isoleret optikusneuritis, recidiverende idiopatisk neuroretinitis, kronisk recidiverende inflammatorisk optikusneuropati, optisk perineuritis) | 0,9976 | L5 | Kun svag, indirekte plausibilitet; de identiske scorer kommer fra TxGNN-modellen (deep learning) og kan afspejle ligheder, modellen har lært mellem beslægtede sygdomme, ikke biologisk evidens. |
| 9–10 | Episcleritis periodica fugax og nodulær episcleritis | 0,9976 | L5 | Ofte selvbegrænsende; ugunstig nytte-risiko-balance for et biologisk lægemiddel. |

Bemærk: Rang 2 (øjensygdom) er i grundlaget angivet som L4, men da ingen af de citerede studier direkte undersøger brodalumab ved øjensygdom, er evidensniveauet her sat til L5.
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

