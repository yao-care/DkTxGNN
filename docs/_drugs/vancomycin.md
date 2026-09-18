---
layout: default
title: Vancomycin
parent: Kun modelforudsigelse (L5)
nav_order: 464
evidence_level: L5
indication_count: 10
---

# Vancomycin
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

# Vancomycin: Fra Gram-positive bakterielle infektioner til diffus skleroderm

## Sammenfattelse på én linje

Vancomycin er et glykopeptidantibiotikim, der klinisk bruges til alvorlige Gram-positive infektioner (f.eks. MRSA, *C. difficile*). TxGNN-modellen forudsiger et muligt link til **Diffus skleroderm**, men denne retning er i øjeblikket understøttet af **0 kliniske forsøg** og kun **1 casusrapport**, og casusrapporten selv beskriver en mistænkt *bivirkning*, ikke en terapeutisk effekt.

## Hurtigt overblik

| Element | Indhold |
|---------|---------|
| Oprindelig indikation | Gram-positive bakterielle infektioner (udledt fra lægemiddelklasse; ingen Danmark-specifik godkendt indikationstekst på fil) |
| Forudsagt ny indikation | Diffus skleroderm |
| TxGNN-forudsigelsesscore | 99.92% |
| Evidensniveau | L5 |
| Status på det danske marked | Ikke markedsført |
| Antal markedsføringstilladelser | 0 |
| Anbefalet beslutning | Hold |

## Hvorfor er denne forudsigelse rimelig?

Detaljerede data om virkningsmåde for denne kandidat er ikke tilgængelige i bevispacken (virkningsmåde-felt er markeret som et blokerende datagab). Baseret på almene farmakologiske data, som fremgår af bevispacken selv, virker vancomycin ved at hæmme D-Ala-D-Ala-cellevægssyntese i Gram-positive bakterier — en mekanisme uden kendt relevans for diffus skleroderm, som er en autoimmun fibrotisk sygdom kendetegnet ved fibroblastaktivering, TGF-β-signalering og mikrovaskulær skade.

Den eneste understøttende litteratur (PMID 31541072) er en casusrapport fra 2019 om en patient med diffust eksfoliativt udslæt, sepsis og eosinofili efter antibiotikabehandling — dette beskriver en *mistænkt hudbivirkning*, ikke en terapeutisk fordel ved skleroderm. Der er ingen bevis fra kliniske forsøg, ingen præklinisk mekanistisk undersøgelse, og ingen etableret farmakologisk begrundelse, der forbinder en antibakteriell cellevægsinhibitor med en autoimmun fibrotisk sygdom.

I betragtning af dette afspejler den høje TxGNN-score mest sandsynligt sparsomme eller konfunderede associationer i den underliggende videnskraf snarere end et ægte repurposeringsignal. Det samme mønster gælder for de andre kandidater i denne batch (paratyfoid feber, salmonellose) — begge er forårsaget af Gram-negative organismer, som vancomycin ikke kan trænge ind i, hvilket gør disse forudsigelser mekanistisk usandsynlige såvel.

## Bevis fra kliniske forsøg

Der er i øjeblikket ingen registrerede relevante kliniske forsøg.

## Litteraturbevis

| PMID | År | Type | Tidsskrift | Vigtigste resultater |
|------|-----|------|--------|---------|
| [31541072](https://pubmed.ncbi.nlm.nih.gov/31541072/) | 2019 | Casusrapport | The American Journal of Case Reports | Beskriver en patient med diffust eksfoliativt udslæt, sepsis og eosinofili efter antibiotikabehandling (herunder midler i vancomycin-lægemiddelklassen) — en mistænkt hudbivirkning, ikke bevis for terapeutisk brug ved skleroderm |

## Oplysninger om det danske marked

Vancomycin er i øjeblikket ikke markedsført i Danmark i henhold til denne bevispacke, og der er ingen markedsføringstilladelelsesregistre på fil (0 licenser).

## Sikkerhedshensyn

Se venligst det godkendte produktinformationsdokument (SmPC) for sikkerhedsinformationer. Ingen lægemiddelinteraktionsregistre blev fundet i den forespurgte database.

## Konklusion og næste trin

**Beslutning: Hold**

**Begrundelse:**
TxGNN-scoren er høj, men der er ingen mekanistisk begrundelse, ingen bevis fra kliniske forsøg, og den enkelte litteraturreference beskriver faktisk en hudbivirkning snarere end en behandlingseffekt. Evidensniveau L5 (kun modelforudsigelse) understøtter ikke fremme af denne kandidat.

**For at komme videre er følgende nødvendigt:**
- Bekræftet data om virkningsmåde for vancomycin (i øjeblikket et blokerende datagab, DG002)
- TFDA/SmPC-advarsler og kontraindikationer (i øjeblikket et blokerende datagab, DG001), før nogen sikkerhedsforscreening (S1) kan påbegyndes
- Prækliniske eller mekanistiske undersøgelser, der specifikt forbinder glykopeptidantibiotikaer til fibrotisk/autoimmun patologier, hvis denne kandidat skal revurderes
- Uafhængig genvurdering af TxGNN-signalet, givet at de 10 bedst rangerede kandidater for dette lægemiddel (herunder paratyfoid feber og salmonellose, begge Gram-negative indikationer) viser det samme mønster af høj score kombineret med usandsynlig mekanisme

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

