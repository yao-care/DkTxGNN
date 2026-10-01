---
layout: default
title: Inotersen
parent: Kun modelforudsigelse (L5)
nav_order: 233
evidence_level: L5
indication_count: 10
---

# Inotersen
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

# Inotersen: Fra hereditær transthyretin-amyloidose til akut intermitterende porfyri

## Resumé i få sætninger

Inotersen (handelsnavn Tegsedi) er et antisense-oligonukleotid, der nedsætter produktionen af transthyretin (TTR) i leveren. Der er ikke angivet en godkendt indikation i de danske registreringsdata. Konteksten i datagrundlaget peger på TTR-relateret sygdom, som den litteratur, der er knyttet til forudsigelsen, også beskriver.
TxGNN-modellen forudsiger, at lægemidlet kan have effekt ved **akut intermitterende porfyri (AIP)**. Der er **0 kliniske forsøg** og kun **1 publikation** (en generel oversigtsartikel), så evidensen er meget svag.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Ikke angivet i de danske registreringsdata |
| Forudsagt ny indikation | Akut intermitterende porfyri |
| TxGNN-forudsigelsesscore | 99,92 % |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført |
| Antal markedsføringstilladelser | 1 |
| Anbefalet beslutning | Hold |

---

## Hvorfor er denne forudsigelse rimelig?

Der foreligger ingen detaljerede data om virkningsmekanismen i evidenspakken. Inotersen er et antisense-oligonukleotid, der reducerer TTR-mRNA i leveren og dermed dannelsen af TTR-protein.

AIP skyldes derimod en øget aktivitet af ALAS1 i leveren og en mangel på enzymet HMBS i hæmsyntesen. Der er altså ingen kendt mekanistisk sammenhæng mellem TTR-nedregulering og AIP. Den høje score (0,999) er sandsynligvis en graf-baseret forudsigelse, der skyldes fælles naboer i vidensgrafen, fx neuropati og oligonukleotidbaserede behandlinger. Den har ikke noget klinisk grundlag.

Modellen har også peget på andre sygdomme, men heller ikke her er der evidens eller kendt mekanistisk sammenhæng:

| Forudsagt sygdom | Score | Bemærkning |
|------|------|------|
| Blindtarmsbetændelse (appendicitis) | 99,91 % | Ingen mekanistisk sammenhæng, ingen forsøg eller litteratur |
| IgG4-relateret pachymeningitis | 99,90 % | TTR-hæmning har ingen plausibel rolle. Sikkerhedsprofilen (trombocytopeni, glomerulonefritis) er en ulempe ved immunmedierede sygdomme |
| IgG4-relateret retroperitoneal fibrose | 99,88 % | Nyrepåvirkning kan forværre risikoen for glomerulonefritis |
| Ikke-infektiøs meningitis | 99,86 % | TTR dannes i plexus choroideus, men inotersen virker primært på TTR i leveren |

---

## Evidens fra kliniske forsøg

Der er i øjeblikket ingen relaterede kliniske forsøg registreret.

---

## Evidens fra litteraturen

| PMID | År | Type | Tidsskrift | Hovedresultater |
|------|-----|------|------|---------|
| [30847674](https://pubmed.ncbi.nlm.nih.gov/30847674/) | 2019 | Oversigtsartikel | Neurological Sciences | Generel oversigt over nye behandlinger af arvelige perifere neuropatier, herunder hATTR. Artiklen undersøger ikke inotersen ved AIP, og de to nævnes sandsynligvis som separate eksempler på oligonukleotidbaseret behandling |

---

## Markedsinformation for Danmark

| Markedsføringstilladelse | Produktnavn | Lægemiddelform | Producent |
|---------|------|------|-----------|
| 28106032117 | Tegsedi | Injektionsvæske, opløsning i fyldt injektionssprøjte | Akcea Therapeutics Ireland Ltd |

---

## Sikkerhedsovervejelser

- **Boksede advarsler:** Ifølge vurderingen i evidenspakken har inotersen boksede advarsler om trombocytopeni og glomerulonefritis/nyretoksicitet. Det er særligt relevant, hvis lægemidlet overvejes til sygdomme med immunmedieret aktivitet eller nyrepåvirkning.
- **Interaktioner:** Der blev ikke fundet registrerede lægemiddelinteraktioner i den forespurgte kilde.

Konsulter det godkendte produktresumé (SmPC) for fuldstændige oplysninger om advarsler, kontraindikationer og interaktioner. Produktresuméet fra Lægemiddelstyrelsen er endnu ikke indhentet.

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelsen bygger kun på modellens score. Der er ingen kliniske forsøg, ingen mekanistisk sammenhæng mellem TTR-nedregulering og AIP og kun én generel oversigtsartikel. Lægemidlets boksede advarsler øger desuden den potentielle risiko.

**For at komme videre kræves følgende:**
- Hentning og gennemgang af produktresuméet fra Lægemiddelstyrelsen (advarsler, kontraindikationer), som er en blokerende datamangel
- Mekanistiske data (MOA) fra DrugBank til at vurdere en eventuel biologisk kobling til AIP
- Præklinisk eller mekanistisk evidens for en sammenhæng mellem TTR-hæmning og hæmsyntesen ved AIP
- En målrettet litteratursøgning efter studier, der direkte undersøger inotersen ved AIP
- Afklaring af den oprindelige godkendte indikation, da indikationsteksten mangler i de danske registreringsdata

*Resultaterne er kun til forskningsbrug og udgør ikke medicinsk rådgivning. Forudsigelser om gentænkning af lægemidler (drug repurposing) skal valideres klinisk, før de kan anvendes.*
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

