---
layout: default
title: Belimumab
parent: Kun modelforudsigelse (L5)
nav_order: 60
evidence_level: L5
indication_count: 10
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

# Belimumab: Fra BLyS-hæmmende B-celle-behandling til primær frigørelsesforstyrrelse af blodplader

## Resumé i få sætninger

Belimumab er et lægemiddel, der hæmmer det opløselige BLyS-protein (BAFF) og dermed nedsætter B-cellers overlevelse og produktionen af autoantistoffer. Original indikation fremgår ikke af de tilgængelige data.
TxGNN-modellen forudsiger, at belimumab kan have effekt ved **primær frigørelsesforstyrrelse af blodplader** (primary release disorder of platelets).
Forudsigelsen understøttes af **0 relevante kliniske forsøg** og **0 publikationer**. Det eneste identificerede forsøg omhandler en anden sygdom.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Original indikation | Ikke angivet (indikationsteksten i den danske godkendelse er tom) |
| Forudsagt ny indikation | Primær frigørelsesforstyrrelse af blodplader |
| TxGNN-forudsigelsesscore | 99,96 % |
| Evidensniveau | L5 (kun modelforudsigelse) |
| Markedsstatus i Danmark | Markedsført |
| Antal markedsføringstilladelser | 1 |
| Anbefalet beslutning | Hold |

---

## Hvorfor er denne forudsigelse (ikke) rimelig?

Der foreligger ingen detaljerede mekanismedata fra DrugBank. Ud fra kendt viden hæmmer belimumab BLyS (BAFF) og nedsætter dermed B-cellers overlevelse og produktionen af autoantistoffer.

Primære frigørelsesforstyrrelser af blodplader skyldes typisk medfødte defekter i blodpladernes granula eller signalering. De er ikke drevet af B-celler eller antistoffer. Der er derfor ikke noget troværdigt mekanistisk link mellem belimumabs virkemåde og denne sygdom. Den høje TxGNN-score (ca. 0,9996) ligner et artefakt fra nærhed i vidensgrafen og ikke en biologisk understøttet sammenhæng.

### Øvrige forudsagte indikationer (dubletter fjernet)

| Forudsagt indikation | Score | Vurdering | Anbefaling |
|------|------|------|------|
| Pseudo-von Willebrands sygdom | 99,96 % | Genetisk defekt i GP1BA (trombocytreceptor), ikke immunmedieret. BLyS-hæmning har intet rationelt mål. | Hold |
| Glanzmanns trombastheni | 99,88 % | Arvelig αIIbβ3-defekt, som belimumab ikke kan korrigere. Kun en spinkel hypotese om alloantistofdannelse efter blodpladetransfusion. | Hold |
| Føtal og neonatal alloimmun trombocytopeni (FNAIT) | 99,59 % | Den mest biologisk sammenhængende forudsigelse. Sygdommen er drevet af maternelle IgG-alloantistoffer (især anti-HPA-1a), så B-cellemodulation er konceptuelt relevant. Der foreligger dog ingen kliniske data, og graviditetssikkerhedsdata for belimumab er begrænsede. Desuden virker belimumab mere på B-cellers overlevelse end på etableret plasmacelle-antistofproduktion. IVIG og FcRn-blokade passer mekanistisk bedre. | Forskningsspørgsmål |
| Svær nonproliferativ diabetisk retinopati | 99,05 % | Mikrovaskulær sygdom drevet af hyperglykæmi, VEGF og inflammation. BLyS/BAFF-hæmning er ikke en etableret behandlingsakse. | Hold |

---

## Klinisk evidens

| Forsøgsnummer | Fase | Status | Antal deltagere | Vigtigste fund |
|---------|------|------|------|---------|
| [NCT01610492](https://clinicaltrials.gov/study/NCT01610492) | Fase 2 | Afsluttet | 14 | Åbent mekanistisk forsøg med belimumab ved idiopatisk membranøs glomerulonefropati (anti-PLA2R-positiv). Forsøget undersøger ikke blodpladefunktionsforstyrrelser og giver hverken direkte eller indirekte evidens for den forudsagte indikation (relevans: C). |

---

## Litteraturevidens

Der er i øjeblikket ingen relateret litteratur.

---

## Information om det danske marked

| Markedsføringstilladelsesnummer | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28105851916 | Benlysta (GlaxoSmithKline (Ireland) Limited) | Injektionsvæske, opløsning i fyldt injektionssprøjte | Ikke angivet i data |

---

## Sikkerhedsovervejelser

Sikkerhedsoplysninger fra Lægemiddelstyrelsen er ikke tilgængelige, og der er ikke fundet interaktionsdata. Se den godkendte produktresumé (SmPC) for sikkerhedsoplysninger.

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelserne bygger udelukkende på modelscore (evidensniveau L5), og der er ingen relevante kliniske forsøg eller publikationer. For flere af de forudsagte sygdomme er der desuden et klart mekanistisk misforhold. Den høje score ser ud til at være et grafartefakt. Kun FNAIT fortjener at blive fulgt som et hypotese- eller prækliniskt forskningsspørgsmål.

**For at komme videre kræves:**
- Sikkerhedsdata (advarsler og kontraindikationer) fra produktresuméet i Lægemiddelstyrelsen, som i dag blokerer sikkerhedsscreeningen
- Mekanismedata (MOA) fra DrugBank
- Bekræftelse af den godkendte indikationstekst for Benlysta i Danmark
- For FNAIT: prækliniske data eller litteraturgennemgang samt en vurdering af graviditetssikkerhed og sammenligning med IVIG og FcRn-blokade

*Resultaterne er kun til forskningsbrug og udgør ikke medicinsk rådgivning. Forudsigelserne kræver klinisk validering, før de kan anvendes.*
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

