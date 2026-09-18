---
layout: default
title: Anidulafungin
parent: Kun modelforudsigelse (L5)
nav_order: 39
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

## Resumé på en sætning

Anidulafungin er et echinocandin-antifungalt middel, der bruges på andre markeder til invasiv candidiasis og kandidæmi, men det er **ikke for øjeblikket registreret i Danmark**. TxGNN-modellen tildeler sin højeste forudsigelsesscore til **Impetigo** (98.85%), men mekanistisk analyse identificerer dette som en sandsynlig **falsk positiv** drevet af vidensgrafs topologi — medicinen har ingen relevant antibakteriel aktivitet mod denne indikation, og **0 kliniske forsøg** og **0 publikationer** understøtter denne retning. Det mest klinisk kredible sekundære signal på tværs af alle forudsigelser er **Pleural empyem** (rang 7), understøttet af kun et enkelt farmakokinetisk studie, der demonstrerer målelig pleural penetration.

---

## Hurtig oversigt

| Element | Indhold |
|---------|---------|
| Oprindelig indikation | Invasiv candidiasis, kandidæmi (ikke registreret i Danmark; ingen licensdata tilgængelig) |
| Forudsagt ny indikation | Impetigo |
| TxGNN forudsigelsesscore | 98.85% |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Ikke markedsført |
| Antal markedsføringstilladelser | 0 |
| Anbefalet beslutning | Hold |

---

## Hvorfor er denne forudsigelse rimelig?

Anidulafungin tilhører echinocandin-klassen af antifungale midler. Selvom detaljerede data om virkningsmekanisme ikke er tilgængelige i denne Evidence Pack, er medicinen veletableret som en **ikke-konkurrencepræget hæmmer af β-1,3-glukan synthase** — det enzym, der er ansvarligt for at syntetisere β-1,3-glukan, en kritisk strukturel komponent af svampecellvæggen. Fordi dette enzym er fuldstændigt fraværende i både pattedyrceller og bakterielle celler, har anidulafungin **ingen antibakteriel aktivitet af nogen art**.

Impetigo er en overfladisk bakteriel hudinfektion forårsaget af *Staphylococcus aureus* eller *Streptococcus pyogenes*. Ingen af disse patogener besidder et β-1,3-glukan synthase-mål, og der er ingen etableret farmakologisk grundlag for at forudsige anidulafungin-effektivitet mod dem. Den høje TxGNN-score (98.85%) afspejler sandsynligvis en **topologisk artefakt i vidensgrafen**: "hudinfektions"-nodegruppen sidder i tæt nærhed til antifungale stofnoder inden for grafen, hvilket genererer en spurios høj-scorende association uden nogen ægte mekanistisk forbindelse. Denne forudsigelse vurderes som en **falsk positiv**.

Det er værd at bemærke, at en sekundær forudsigelse — **Pleural empyem** (rang 7, score 98.52%, evidensniveau L4) — repræsenterer en marginalt mere plausibel, selvom stadig meget tidlig-stadium, hypotese. Svampe-betinget pleural empyem forårsaget af *Candida* eller *Aspergillus* spp. forekommer hos kritisk syge og immunokomprimiterede patienter og har høj mortalitet. En PK/PD-observationsstudie (PMID 29439960) bekræfter, at anidulafungin når målelige koncentrationer i pleural væske (cirka 40–60% af samtidige plasma-niveauer), hvilket etablerer, at stofpenetration til pleural-kompartmentet er opnåelig. Dette udgør ikke effektivitetsbevis, men det er det eneste datapunkt på tværs af alle forudsigelser, der bærer nogen klinisk tolkbar signal.

---

## Bevis fra kliniske forsøg

Der er i øjeblikket ingen relaterede kliniske forsøg registreret.

---

## Litteraturbevis

Der er i øjeblikket ingen relevant litteratur tilgængelig for impetigo-indikationen.

**Sekundært signal — Pleural empyem (rang 7):** Et farmakokinetisk studie er tilgængeligt og inkluderet nedenfor som reference, da det repræsenterer det eneste offentliggjorte bevis identificeret på tværs af alle forudsigelser i denne Evidence Pack.

| PMID | År | Type | Journal | Vigtige fund |
|------|-----|------|---------|-------------|
| [29439960](https://pubmed.ncbi.nlm.nih.gov/29439960/) | 2018 | PK/PD-observationsstudie | *Antimicrobial Agents and Chemotherapy* | Hos 10 kritisk syge patienter var anidulafungin-koncentrationer i pleural væske (0,32–2,02 µg/ml) og ascites-væske (0,12–0,99 µg/ml) målelige, men konsistent lavere end samtidige plasma-niveauer (2,48–13,36 µg/ml), hvilket bekræfter stofpenetration til både pleural og abdominalt kompartment ved klinisk relevante koncentrationer |

---

## Markedsinformation for Danmark

Anidulafungin er **ikke registreret i Danmark**. Ingen markedsføringstilladelser er udstedt af Lægemiddelstyrelsen, og ingen centraliseret EMA-markedsføringstilladelse gælder for det danske marked.

> **Adgangsoversigt:** Anidulafungin er godkendt i EU under varemærket **Ecalta** (EMA-centraliseret procedure) til behandling af invasiv candidiasis hos ikke-neutropene voksne. Klinisk brug i Danmark ville kræve adgang via en patientimport- eller compassioneret-brug-vej gennem Lægemiddelstyrelsen.

---

## Sikkerhedshensyn

Se venligst det godkendte produktresumé (SmPC) for sikkerhedsinformation.

---

## Konklusion og næste trin

**Beslutning: Hold**

**Begrundelse:**
Den toprangerede TxGNN-forudsigelse (impetigo, rang 1) har ingen mekanistisk grundlag og ingen understøttende klinisk eller præ-klinisk bevis; den vurderes som en vidensgrafs falsk positiv, der opstår fra topologisk nærhed af hudinfektions-knuder. Alle resterende L5-klassificerede forudsigelser (ondartet pleural mesotheliom, staphylokok-skaldet hudsyndrom, ondartet visceral pleura-tumor) mangler ligeledes understøttelse. Det eneste fund med nogen form for bevis (pleural empyem, rang 7, L4) er begrænset til stofpenetrations-data og udgør ikke et effektivitets-signal, der er tilstrækkeligt til at gå videre med ud over et forskningsspørgsmål.

**For at fortsætte er følgende nødvendigt:**

- Hentelse af det fuldstændige **Ecalta EU-produktresumé** for at fuldende sikkerhedsprofil-vurderingen (advarsler, kontraindikationer, stofinteraktioner)
- Præcisering af den **danske patientimport-vej** (Lægemiddelstyrelsen §29), hvis compassioneret klinisk brug er påkrævet
- Hvis det pleural empyem sekundære signal skal udforskes videre: en **dedikeret litteratur-søgning** for kasuistikker og kasusserier af anidulafungin-brug i bekræftet *svampe*pleural empyem, sammen med vurdering af MIC-data mod relevante *Candida*/*Aspergillus*-isolater
- Ingen yderligere investering i impetigo-, ondartet pleural mesotheliom-, staphylokok-skaldet hudsyndrom-, eller ondartet visceral pleura-tumor-forudsigelserne er berettiget på nuværende tidspunkt

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

