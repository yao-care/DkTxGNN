---
layout: default
title: Anidulafungin
parent: Kun modelforudsigelse (L5)
nav_order: 40
evidence_level: L5
indication_count: 10
---

# Anidulafungin
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

# Anidulafungin: Fra invasiv candidiasis til impetigo

## Resumé i én sætning

Anidulafungin er et svampemiddel af echinocandin-klassen. Evidenspakken angiver ikke en original indikation, men klassen anvendes til invasive Candida-infektioner. TxGNN-modellen forudsiger, at lægemidlet kan have effekt mod **impetigo**, men der er **0 kliniske forsøg** og **0 publikationer** til støtte for denne retning, og der er ingen understøttet mekanistisk forbindelse.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Original indikation | Ikke angivet i Lægemiddelstyrelsens data (klassens kendte anvendelse: invasiv candidiasis) |
| Forudsagt ny indikation | Impetigo |
| TxGNN-forudsigelsesscore | 98,85 % |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført |
| Antal markedsføringstilladelser | 1 |
| Anbefalet beslutning | Hold |

---

## Hvorfor er denne forudsigelse rimelig?

Der er i øjeblikket ingen detaljerede data om virkningsmekanisme i evidenspakken. Anidulafungin tilhører echinocandin-klassen, som hæmmer svampenes enzym beta-1,3-D-glukansyntase og dermed opbygningen af cellevæggen.

Impetigo er en hudinfektion, der skyldes bakterier, typisk *Staphylococcus aureus* eller *Streptococcus pyogenes*. Bakterier har ikke dette målenzym, og der forventes derfor ikke antibakteriel virkning. Den høje modelscore (0,989) er en ren grafbaseret forudsigelse uden klinisk eller litteraturmæssig opbakning.

**Vurdering:** Forudsigelsen har ingen understøttet mekanistisk forklaring og bør betragtes som et modelartefakt, indtil andet er påvist.

---

## Kliniske forsøg

Der er i øjeblikket ingen relaterede kliniske forsøg registreret.

---

## Litteratur

Der er i øjeblikket ingen relateret litteratur for impetigo.

---

## Øvrige forudsagte indikationer

Evidenspakken indeholder yderligere forudsigelser med tilsvarende høje scorer. Rækkerne er dubletter i kilden og vises her kun én gang.

| Forudsagt indikation | TxGNN-score | Evidensniveau | Kommentar |
|------|------|------|------|
| Malign pleural mesoteliom | 98,75 % | L5 | Ingen understøttet mekanistisk forbindelse; humane tumorceller udtrykker ikke svampens glukansyntase |
| Staphylococcal scalded skin syndrome | 98,73 % | L5 | Toksinmedieret sygdom (eksfoliative toksiner); anidulafungin har ingen antibakteriel eller antitoksin-virkning |
| Pleuraempyem | 98,52 % | L4 | Indirekte og begrænset understøttelse, se nedenfor |
| Malign visceral pleuratumor | 98,45 % | L5 | Som ved mesoteliom er målstrukturen fraværende |

**Pleuraempyem:** Et farmakokinetisk studie fra 2018 ([PMID 29439960](https://pubmed.ncbi.nlm.nih.gov/29439960/), *Antimicrobial Agents and Chemotherapy*) målte anidulafungin i ascitesvæske og pleuraeffusion hos 10 kritisk syge voksne. Koncentrationerne i pleuraeffusion (0,32-2,02 µg/ml) var lavere end i plasma (2,48-13,36 µg/ml), men viser en vis eksponering i pleurarummet. Studiet vurderer ikke effekt ved empyem, og de fleste empyemer er bakterielle. Fundet er kun relevant for den svampeforårsagede del.

---

## Markedsinformation i Danmark

| Markedsføringstilladelse | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28105926717 | Anidulafungin "Accord" (Accord Healthcare B.V.) | Pulver til koncentrat til infusionsvæske, opløsning | Ikke angivet i data |

---

## Sikkerhedsovervejelser

Se det godkendte produktresumé (SmPC) for sikkerhedsoplysninger.

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelsen for impetigo hviler alene på en grafbaseret modelscore. Der er hverken kliniske forsøg eller publikationer, og virkningsmekanismen (hæmning af svampens glukansyntase) passer ikke til en bakteriel infektion. Evidensniveauet er L5.

**For at komme videre kræves følgende:**
- Data om virkningsmekanisme (MOA) fra DrugBank
- Oplysninger om advarsler og kontraindikationer fra Lægemiddelstyrelsens produktresumé, som er forudsætning for sikkerhedsscreening
- Den godkendte indikationstekst for den danske markedsføringstilladelse
- Enhver ny hypotese bør først belyses med præklinisk eller mekanistisk evidens. Pleuraempyem (fungal delmængde) er den eneste forudsigelse med indirekte støtte og kan overvejes som et forskningsspørgsmål.

*Resultaterne er udelukkende til forskningsbrug og udgør ikke medicinsk rådgivning. Kandidater til lægemiddelrepositionering kræver klinisk validering, før de kan anvendes.*
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

