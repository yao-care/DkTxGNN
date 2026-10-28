---
layout: default
title: Rasburicase
parent: Kun modelforudsigelse (L5)
nav_order: 705
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Rasburicase: forudsagt ny indikation Renal hypourikæmi (evidensniveau L5). Oprindelig indikation: Hyperurikæmi"
monitor_inn: "rasburicase"
predicted_indications: ["hypouricemia, renal", "hypoxanthine guanine phosphoribosyltransferase partial deficiency", "hepatic porphyria", "idiopathic copper-associated cirrhosis", "early-onset familial noncirrhotic portal hypertension", "primitive portal vein thrombosis", "hepatopulmonary syndrome", "hepatoportal sclerosis", "renal tubular acidosis", "disorder of phenylalanine metabolism"]
---

# Rasburicase
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

## Rasburicase: Fra hyperurikæmi til renal hypourikæmi
{: .text-alpha }

## Resumé i en sætning

Rasburicase er et rekombinant urat-oxidaseenzym, som oprindeligt blev brugt til at sænke urinsyre ved hyperurikæmi. TxGNN-modellen forudsiger, at lægemidlet kan have effekt ved **renal hypourikæmi**, men der er **ingen registrerede kliniske forsøg og ingen publikationer**, der understøtter forudsigelsen. Forudsigelsen er desuden mekanistisk modstridende (se nedenfor).

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Hyperurikæmi (fra videnbasen; der er ingen godkendt indikationstekst i de danske data) |
| Forudsagt ny indikation | Renal hypourikæmi |
| TxGNN-forudsigelsesscore | 0.9999 |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført (gyldige tilladelser: 1 af 1) |
| Antal markedsføringstilladelser | 1 (gyldige: 1) |
| Anbefalet beslutning | Hold |

## Hvorfor er forudsigelsen (ikke) rimelig?

Data om detaljeret virkningsmekanisme er ikke tilgængelige i de data, der er indsamlet til denne rapport. Rasburicase er dog kendt som et rekombinant urat-oxidaseenzym, der omdanner urinsyre til allantoin og dermed sænker serum-urat.

Renal hypourikæmi er en tilstand, hvor serum-urat allerede er for lavt, typisk på grund af funktionstabsmutationer i transportørerne URAT1 eller GLUT9. Yderligere urat-sænkning er mekanistisk kontraproduktiv og vil ikke behandle tilstanden. Det kan øge risikoen for skade, f.eks. træningsudløst akut nyreskade. Den høje TxGNN-score (0.9999) stammer fra TxGNN-modellen (deep learning) og kan afspejle ligheder, som modellen har lært mellem beslægtede sygdomme, ikke biologisk evidens.

Blandt de øvrige forudsigelser (rang 2-10) er det kun delvis HGPRT-mangel, der har en biologisk forbindelse via urat-endepunktet. Rasburicase er dog et intravenøst, immunogent enzym til korte kure og adresserer ikke det underliggende enzymdefekt. Kronisk behandling varetages bedre af xanthinoxidasehæmmere. Hepatisk porfyri, idiopatisk kobberassocieret cirrose, familiær non-cirrotisk portal hypertension, primær portalvenetrombose, hepatopulmonalt syndrom, hepatoportal sklerose, renal tubulær acidose og forstyrrelser i fenylalaninstofskiftet har ingen identificeret mekanistisk sammenhæng og fremstår som netværksartefakter.

## Evidens fra kliniske forsøg

Der er aktuelt ingen relaterede kliniske forsøg registreret.

## Litteraturevidens

Der er aktuelt ingen relateret litteratur tilgængelig.

## Markedsinformation for Danmark

| Markedsføringstilladelsesnummer | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28103081899 | Fasturtec (Sanofi Winthrop Industrie) | Pulver og solvens til koncentrat til infusionsvæske, opløsning | Indikationstekst er ikke angivet i de indsamlede data |

## Sikkerhedsovervejelser

**Lægemiddelinteraktioner:** Der blev fundet 26 registrerede interaktioner (kilde: DDInter). De væsentligste:
- **Større (Major):** prilocain og nitrit (salpetersyrling)
- **Moderate:** lokalbedøvelsesmidler og lignende (tetracain, lidocain, benzocain, cocain, proparacain, oxybuprocain, cinchocain; i topikale, oftalmiske og nasale former) samt idelalisib

Der er desuden risiko for hæmolyse og methæmoglobinæmi ved brug af rasburicase, hvilket er særligt relevant ved syre-base-forstyrrelser. For komplette advarsler og kontraindikationer henvises til det godkendte produktresumé (SmPC), da disse ikke indgår i de indsamlede data.

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Alle forudsigelser er på evidensniveau L5 uden kliniske forsøg eller litteratur. For den højest rangerede forudsigelse (renal hypourikæmi) er den forventede virkning modsat det ønskede, og der er en potentiel skaderisiko.

**For at komme videre kræves følgende:**
- Gennemgang af produktresuméet for advarsler og kontraindikationer (blokerende datamangel)
- Data om virkningsmekanisme (MOA) fra DrugBank
- Hvis man alligevel vil udforske en snæver anvendelse (f.eks. akut svær hyperurikæmi ved delvis HGPRT-mangel), kræves først prækliniske eller kliniske data
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

