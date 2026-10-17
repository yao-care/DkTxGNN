---
layout: default
title: Anidulafungin
parent: Kun modelforudsigelse (L5)
nav_order: 66
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Anidulafungin: forudsagt ny indikation Impetigo (evidensniveau L5). Oprindelig indikation: Esophageal candidiasis og candidaemi"
monitor_inn: "Anidulafungin"
predicted_indications: ["impetigo", "impetigo", "malignant pleural mesothelioma", "malignant pleural mesothelioma", "staphylococcal scalded skin syndrome", "staphylococcal scalded skin syndrome", "pleural empyema (disease)", "pleural empyema (disease)", "malignant visceral pleura tumor", "malignant visceral pleura tumor"]
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

<div id="pharmacist" markdown="1">

## Farmaceutens vurderingsrapport

</div>

# Anidulafungin: Fra esophageal candidiasis og candidaemi til impetigo

## Resumé i én sætning

Anidulafungin er et antimykotikum af echinocandin-klassen, som oprindeligt anvendes til behandling af esophageal candidiasis og candidaemi.
TxGNN-modellen forudsiger, at lægemidlet kan have effekt mod **impetigo**,
men der er **ingen kliniske forsøg** og **ingen publikationer** til at understøtte denne forudsigelse. Den vurderes sandsynligvis at være falsk positiv.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Esophageal candidiasis og candidaemi (de godkendte indikationstekster for det danske produkt er ikke tilgængelige i de indsamlede data) |
| Forudsagt ny indikation | Impetigo |
| TxGNN-forudsigelsesscore | 98,85 % |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført |
| Antal markedsføringstilladelser | 1 |
| Anbefalet beslutning | Hold |

---

## Hvorfor er denne forudsigelse rimelig?

Detaljerede data om virkningsmekanismen er ikke tilgængelige i de data, der er indsamlet til denne rapport. Anidulafungin tilhører echinocandin-klassen, som hæmmer enzymet beta-(1,3)-D-glucansyntase i svampes cellevæg. Denne virkning er veletableret ved invasive candida-infektioner.

Impetigo skyldes hovedsageligt *Staphylococcus aureus* og *Streptococcus pyogenes*. Det er bakterier, som ikke har beta-glucan i cellevæggen, og som derfor ikke har det target, anidulafungin virker på. Der er således ikke noget plausibelt mekanistisk link mellem den oprindelige og den forudsagte indikation.

Den høje score (0,989) afspejler formentlig kun nærhed i vidensgrafen (f.eks. til andre infektionssygdomme) og ikke biologisk rationale. Forudsigelsen bør derfor fortolkes med stor forsigtighed.

Modellen genererede også andre forudsigelser med tilsvarende høje scorer, som ligeledes savner støtte:
- **Malign pleuramesoteliom** (score 98,75 %) og **malign visceral pleuratumor** (98,45 %): anidulafungin har ingen kendt antineoplastisk mekanisme.
- **Staphylokok-skoldet hud-syndrom** (98,73 %): sygdommen er toksinmedieret og behandles med antibakterielle midler, som anidulafungin ikke har aktivitet som.
- **Pleuraempyem** (98,52 %): se afsnittet om litteratur nedenfor.

---

## Evidens fra kliniske forsøg

Der er for øjeblikket ingen relaterede kliniske forsøg registreret.

---

## Litteraturevidens

Der er ingen litteratur om anidulafungin ved impetigo. Den eneste relevante publikation findes for den sekundære forudsigelse pleuraempyem:

| PMID | År | Type | Tidsskrift | Hovedfund |
|------|-----|------|------|---------|
| [29439960](https://pubmed.ncbi.nlm.nih.gov/29439960/) | 2018 | Farmakokinetisk studie | Antimicrobial Agents and Chemotherapy | Hos 10 kritisk syge patienter nåede anidulafungin pleuraekssudat (0,32–2,02 µg/ml) og ascitesvæske (0,12–0,99 µg/ml) i koncentrationer under plasmaniveauet. Studiet viser vævspenetration, ikke klinisk effekt. |

---

## Information om markedet i Danmark

| Markedsføringstilladelsesnummer | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28105926717 | Anidulafungin "Accord" (Accord Healthcare B.V.) | Pulver til koncentrat til infusionsvæske, opløsning | Indikationstekst ikke tilgængelig i de indsamlede data |

Lægemidlet findes udelukkende som injektionsvæske (intravenøs infusion).

---

## Sikkerhedsmæssige overvejelser

- **Kontraindikationer fra vidensgrafen** (ikke fra produktresuméet): lever- og galdeblæresygdom. Dette er afledt af relationer i vidensgrafen og bør verificeres mod produktresuméet.
- **Lægemiddelinteraktioner**: Der er identificeret én interaktion, med **ciclosporin** (sværhedsgrad: mindre, kilde: DDInter).

Se i øvrigt det godkendte produktresumé (SPC) for fuldstændige oplysninger om advarsler og kontraindikationer.

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelsen bygger udelukkende på modelberegning (evidensniveau L5) uden kliniske forsøg eller litteratur. Anidulafungin har ingen aktivitet mod de bakterier, der forårsager impetigo, så forudsigelsen er sandsynligvis falsk positiv.

**For at komme videre kræves følgende:**
- Data om virkningsmekanismen (MOA), f.eks. fra DrugBank
- Advarsler og kontraindikationer fra produktresuméet hos Lægemiddelstyrelsen (afgørende for sikkerhedsscreening)
- Præklinisk evidens (f.eks. in vitro-aktivitet) for en eventuel antimikrobiel effekt, før yderligere vurdering overvejes
- Om ønsket: en separat vurdering af pleuraempyem begrænset til svampeetiologi, hvor farmakokinetiske data er i overensstemmelse med den godkendte virkning
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

