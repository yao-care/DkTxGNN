---
layout: default
title: Metyrapone
parent: Kun modelforudsigelse (L5)
nav_order: 546
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Metyrapone: forudsagt ny indikation Udøvelsesudløst malign hypertermi (evidensniveau L5). Oprindelig indikation: Ikke oplyst i de indsamlede data (godkendt indikationstekst er tom)"
monitor_inn: "metyrapone"
predicted_indications: ["exercise-induced malignant hyperthermia", "malignant hyperthermia, susceptibility to", "King-Denborough syndrome", "central core myopathy", "moderate multiminicore disease with hand involvement", "congenital multicore myopathy with external ophthalmoplegia", "myopathy, centronuclear", "familial periodic paralysis", "renal tubular acidosis", "malignant hyperthermia of anesthesia"]
---

# Metyrapone
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

## Metyrapon: Fra hæmning af binyrebarkens kortisolsyntese til udøvelsesudløst malign hypertermi
{: .text-alpha }

## Opsummering

Metyrapon (Metopirone) hæmmer enzymet 11-beta-hydroxylase og dermed dannelsen af kortisol. Lægemidlet er markedsført i Danmark, men den godkendte indikationstekst er ikke tilgængelig i de data, der er indsamlet til denne rapport.
TxGNN-modellen forudsiger, at metyrapon kan have effekt ved **udøvelsesudløst malign hypertermi**, men der findes **0 kliniske forsøg** og **0 publikationer** for denne indikation. Forudsigelsen bygger alene på modellen og er mekanistisk ikke understøttet.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Ikke oplyst i de indsamlede data (godkendt indikationstekst er tom) |
| Forudsagt ny indikation | Udøvelsesudløst malign hypertermi |
| TxGNN-forudsigelsesscore | 99,95 % |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført |
| Antal markedsføringstilladelser | 1 |
| Anbefalet beslutning | Hold |

---

## Hvorfor er denne forudsigelse (ikke) rimelig?

Der foreligger ingen detaljerede data om virkningsmekanismen i de indsamlede data. Metyrapon er dog kendt som en hæmmer af 11-beta-hydroxylase (CYP11B1), som sænker kortisolsyntesen i binyrerne.

Malign hypertermi skyldes primært forstyrret calciumfrigivelse i skeletmuskulatur, ofte forbundet med varianter i generne RYR1 eller CACNA1S. Der er ingen kendt biologisk forbindelse mellem hæmning af kortisolsyntese og denne patofysiologi. Den høje modelscore skyldes sandsynligvis tilfældige associationer i vidensgrafen og ikke et reelt biologisk forhold. Dantrolen er den etablerede mekanismebaserede behandling.

De øvrige forudsigelser i top 10 (bl.a. malign hypertermi-modtagelighed, King-Denboroughs syndrom, central core-myopati, multiminicore-sygdom, centronuklear myopati og renal tubulær acidose) ligger overvejende inden for gruppen af kongenitte myopatier og savner ligeledes mekanistisk og klinisk støtte. Ved renal tubulær acidose kan metyrapon teoretisk set forværre tilstanden, da det kan øge deoxykortikosteron med mineralokortikoid aktivitet. Den eneste forudsigelse med en publikation er familiær periodisk paralyse (evidensniveau L4), som er omtalt i afsnittet om litteratur.

---

## Klinisk forsøgsevidens

Der er i øjeblikket ikke registreret relaterede kliniske forsøg.

---

## Litteraturevidens

Der er ingen litteratur for den primære forudsigelse (udøvelsesudløst malign hypertermi). Den eneste fundne publikation vedrører en anden forudsagt indikation, familiær periodisk paralyse:

| PMID | År | Type | Tidsskrift | Hovedfund |
|------|-----|------|------|---------|
| [4322666](https://pubmed.ncbi.nlm.nih.gov/4322666/) | 1971 | Fysiologisk studie (design ikke bekræftet) | The Journal of Clinical Investigation | Hos en 19-årig mand med familiær hyperkalæmisk periodisk paralyse blev anfald udløst af kaliumklorid, kortikotropin og flere glukokortikoider, men ikke af mineralokortikoider eller af ACTH kombineret med metyrapon. Forbindelsen til metyrapon er indirekte og spekulativ. |

---

## Information om markedet i Danmark

| Markedsføringstilladelsesnr. | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28105336213 | Metopirone (Esteve Pharmaceuticals S.A.) | Kapsler, bløde | Ikke oplyst |

---

## Sikkerhedsovervejelser

- **Kontraindikationer ifølge vidensgrafen (ikke præparatomtale):** Tilstande med nedsat binyrefunktion, herunder Addisons sygdom, kronisk primær binyrebarkinsufficiens, binyrebarkinsufficiens, medfødt binyrehyperplasi, familiær glukokortikoidmangel, X-bundet medfødt binyrehypoplasi og arvelig isoleret binyrebarkinsufficiens som følge af delvis CYP11A1-mangel.
- **Lægemiddelinteraktioner:** 12 interaktioner af moderat sværhedsgrad er registreret, bl.a. med østrogener (ethinylestradiol, østradiol, konjugerede østrogener, mestranol, veresterede østrogener, østronsulfat, også topikale former) og cyproheptadin.

For fuldstændige oplysninger om advarsler og kontraindikationer henvises til den godkendte produktresumé (SmPC).

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelsen hviler udelukkende på modellen (evidensniveau L5) uden kliniske forsøg eller litteratur og uden plausibel biologisk forbindelse mellem kortisolsyntesehæmning og calciumdysregulering i muskulaturen. Der findes desuden en etableret behandling (dantrolen).

**For at komme videre kræves:**
- Data om virkningsmekanismen (MOA) fra DrugBank
- Produktresumé med advarsler og kontraindikationer fra Lægemiddelstyrelsen, da sikkerhedsscreening ikke kan gennemføres uden dem
- Oplysninger om godkendt indikation for Metopirone
- Prækliniske data eller en veldokumenteret mekanistisk hypotese, før yderligere vurdering overvejes
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

