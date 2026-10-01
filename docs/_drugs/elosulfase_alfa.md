---
layout: default
title: Elosulfase Alfa
parent: Kun modelforudsigelse (L5)
nav_order: 160
evidence_level: L5
indication_count: 10
---

# Elosulfase Alfa
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

# Elosulfase alfa: Fra Morquio A-syndrom (MPS IVA) til Scheie syndrom

## Resumé i få sætninger

Elosulfase alfa (Vimizim) er en rekombinant enzymerstatningsterapi (GALNS), som er udviklet til behandling af Morquio A-syndrom (MPS IVA). TxGNN-modellen forudsiger, at lægemidlet kan have effekt ved **Scheie syndrom** (mild form af MPS I). Der er dog **ingen kliniske forsøg** og **ingen publikationer med data om elosulfase alfa** ved denne sygdom, og modellens høje score skyldes sandsynligvis blot nærheden mellem MPS-sygdommene i vidensgrafen.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Ikke angivet i de danske licensdata. Ifølge litteraturen er det Morquio A-syndrom (MPS IVA) |
| Forudsagt ny indikation | Scheie syndrom |
| TxGNN-forudsigelsesscore | 99,90 % |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført |
| Antal markedsføringstilladelser | 1 |
| Anbefalet beslutning | Hold |

---

## Hvorfor er forudsigelsen (ikke) rimelig?

Der foreligger på nuværende tidspunkt ingen detaljerede data om virkningsmekanisme. Elosulfase alfa er rekombinant N-acetylgalactosamin-6-sulfatase (GALNS), som nedbryder keratansulfat og chondroitin-6-sulfat. Enzymet erstatter den manglende funktion ved Morquio A-syndrom.

Scheie syndrom skyldes mangel på enzymet IDUA (alfa-L-iduronidase). Derfor ophobes dermatansulfat og heparansulfat. Disse substrater overlapper ikke med GALNS' substrater, så der er **ingen plausibel enzymatisk begrundelse** for, at elosulfase alfa kan erstatte det manglende enzym. Den høje score afspejler formentlig, at begge sygdomme ligger tæt på hinanden i vidensgrafen (MPS og lysosomale lagringssygdomme).

De øvrige forudsigelser i evidenspakken understøtter den samme vurdering:

- **Lysosomal lagringssygdom med skeletinvolvering** (score 99,59 %): Kategorien er for bred og omfatter Morquio A, som er lægemidlets godkendte indikation. Signalet er derfor sandsynligvis genfinding af den eksisterende indikation og ikke reel ny anvendelse. Evidens bør tilskrives den specifikke sygdom, MPS IVA.
- **Hurler syndrom** (score 99,43 %): Det er den svære form af MPS I (IDUA-mangel). GALNS-erstatning adresserer ikke den primære defekt. Det eneste forsøg, NCT04532047 (PEARL), er et fase 1-platformsstudie af prænatal enzymerstatning ved flere lysosomale lagringssygdomme uden bekræftelse af, at elosulfase alfa anvendes.
- **Sanfilippo syndrom** (score 99,42 %): Sygdommen involverer nedbrydning af heparansulfat og overvejende CNS-sygdom. GALNS er ikke involveret, og intravenøs enzymerstatning forventes ikke at passere blod-hjerne-barrieren. De 19 tilknyttede publikationer, herunder fase 3-RCT'en (PMID 24810369), handler alle om Morquio A og må ikke tilskrives Sanfilippo.
- **Camptodactyly, myopia og fibrose af den mediale rectusmuskel** (score 99,09 %): Der er hverken mekanistisk sammenhæng, forsøg eller litteratur.

---

## Evidens fra kliniske forsøg

Der er på nuværende tidspunkt ingen registrerede kliniske forsøg for Scheie syndrom.

---

## Litteraturevidens

| PMID | År | Type | Tidsskrift | Hovedfund |
|------|-----|------|------|---------|
| [35005816](https://pubmed.ncbi.nlm.nih.gov/35005816/) | 2022 | Kohorte | Human Mutation | Molekylær karakterisering af 302 iranske MPS-patienter. Ingen data om elosulfase alfa |
| [18584975](https://pubmed.ncbi.nlm.nih.gov/18584975/) | 2009 | Kohorte | Pathologie-biologie | Kliniske træk og konsanguinitet ved MPS I og IVA i Tunesien. Ingen data om elosulfase alfa |

Begge artikler beskriver sygdommen, ikke behandling med elosulfase alfa.

---

## Information om det danske marked

| Markedsføringstilladelse | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28105295813 | Vimizim (BioMarin International Limited) | Koncentrat til infusionsvæske, opløsning | Indikationstekst ikke angivet i de tilgængelige data |

---

## Sikkerhedsovervejelser

Se det godkendte produktresumé (SmPC) for sikkerhedsoplysninger.

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelsen for Scheie syndrom hviler udelukkende på modellen (L5). Der er ingen forsøg og ingen data om elosulfase alfa, og der er ingen enzymatisk sammenhæng, da GALNS-substrater og IDUA-substrater ikke overlapper. Evidensen for lægemidlet gælder kun den godkendte indikation, Morquio A.

**For at komme videre kræves:**
- Produktresumé (advarsler og kontraindikationer) fra Lægemiddelstyrelsen, så sikkerhedsscreening kan gennemføres
- Data om virkningsmekanisme fra DrugBank
- Prækliniske data eller andet, der kan understøtte en biologisk sammenhæng med IDUA-mangel, før der overvejes yderligere vurdering
- Kortlægning af den brede kategori "lysosomal lagringssygdom med skeletinvolvering" til en specifik sygdom (MPS IVA), så eksisterende evidens tilskrives korrekt

*Resultaterne er kun til forskningsbrug og udgør ikke lægefaglig rådgivning. Kandidater til lægemiddelomplacering kræver klinisk validering, før de kan anvendes.*
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

