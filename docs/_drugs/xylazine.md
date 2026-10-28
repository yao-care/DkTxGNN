---
layout: default
title: Xylazine
parent: Kun modelforudsigelse (L5)
nav_order: 897
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-28
description: "Xylazine: forudsagt ny indikation Migræne (migraine disorder) (evidensniveau L5). Oprindelig indikation: Ikke angivet i de tilgængelige data (kun veterinære præparater)"
monitor_inn: "xylazine"
predicted_indications: ["migraine disorder", "open-angle glaucoma", "migraine with brainstem aura", "primary hereditary glaucoma"]
---

# Xylazine
{: .fs-9 }

Evidensniveau: **L5** | Forudsagte indikationer: **4** stk.
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

## Xylazin: Fra dyrlægemiddel (ingen godkendt human indikation) til migræne
{: .text-alpha }

## Resumé

Xylazin er en alfa-2-adrenerg agonist, som i Danmark kun er godkendt som dyrlægemiddel (Rompun Vet. og Nerfasin Vet.). Der er ingen registreret original indikationstekst i de data, der er sammenstillet til denne rapport. TxGNN-modellen forudsiger, at xylazin kan være virksomt mod **migræne**, men der er **0 kliniske forsøg** og kun **1 publikation** (et præklinisk dyrestudie, hvor xylazin sandsynligvis kun indgår som anæstetikum). Evidensen er derfor meget svag.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Ikke angivet i de tilgængelige data (kun veterinære præparater) |
| Forudsagt ny indikation | Migræne (migraine disorder) |
| TxGNN-forudsigelsesscore | 0,9964 |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført (gyldige tilladelser: 2 af 2) |
| Antal markedsføringstilladelser | 2 (gyldige: 2) |
| Anbefalet beslutning | Hold |

---

## Hvorfor er forudsigelsen rimelig (eller ikke)?

Der foreligger ingen detaljerede data om virkningsmekanisme i de sammenstillede data. Xylazin er kendt som alfa-2-adrenerg agonist med sedativ, analgetisk og muskelafslappende effekt i veterinærmedicin. Det er ikke godkendt til human brug.

Den eneste publikation (PMID 27122032) undersøger, hvor modtagelig den primære sensoriske cortex er for spredende depolarisationer, en mekanisme der er relevant for migrænearua. Der er tale om et præklinisk neurofysiologisk studie i mus og elektrokortikografi hos mennesker, og xylazin indgår sandsynligvis som en del af anæstesiprotokollen og ikke som en testet behandling. Forbindelsen til migræne er derfor indirekte og spekulativ.

Forudsigelsen hviler dermed næsten udelukkende på TxGNN-grafscoren.

### Øvrige forudsagte indikationer

| Rang | Sygdom | TxGNN-score | Evidens | Bemærkning |
|---|---|---|---|---|
| 2 | Åbenvinklet glaukom | 0,9955 | L5 | Alfa-2-agonister (fx brimonidin) sænker det intraokulære tryk, men xylazins systemiske hypotension og bradykardi kan sænke okulært perfusionstryk. Eneste artikel (PMID 22359566) er et dyrestudie. |
| 3 | Migræne med hjernestammeaura | 0,9954 | L5 | Samme enkeltartikel som for migræne (PMID 27122032). |
| 4 | Primært arveligt glaukom | 0,9953 | L5 | Ingen forsøg eller litteratur. |

---

## Klinisk forsøgsevidens

Der er i øjeblikket ingen relaterede kliniske forsøg registreret.

---

## Litteraturevidens

| PMID | År | Type | Tidsskrift | Hovedresultater |
|------|-----|------|------|---------|
| [27122032](https://pubmed.ncbi.nlm.nih.gov/27122032/) | 2016 | Præklinisk dyrestudie | J Neurosci | Undersøger modtageligheden af den primære sensoriske cortex for spredende depolarisationer (relevant for migrænearua) hos mus og mennesker. Xylazin er sandsynligvis kun del af anæstesien. |

---

## Markedsinformation i Danmark

| Markedsføringstilladelse | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28100566969 | Rompun Vet. (Elanco Animal Health GmbH) | Injektionsvæske, opløsning | Ikke angivet i data (veterinært præparat) |
| 28104812410 | Nerfasin Vet. (Le Vet B.V.) | Injektionsvæske, opløsning | Ikke angivet i data (veterinært præparat) |

---

## Sikkerhedsovervejelser

Der foreligger ingen produktresuméoplysninger om advarsler, kontraindikationer eller interaktioner i de sammenstillede data. Ud fra den tilgængelige vurdering er der dog alvorlige sikkerhedsbekymringer ved human brug:

- **Systemiske virkninger:** Kraftig sedation, respirationsdepression, bradykardi og hypotension.
- **Hudskader:** Alvorlige nekrotiske hudsår er set ved brug i forurenede opioider.
- **Glaukom:** Hypotension kan yderligere reducere okulært perfusionstryk.
- **Regulatorisk status:** Xylazin er ikke godkendt til human brug.

Se i øvrigt de godkendte produktresuméer (SmPC) for de veterinære præparater.

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelsen understøttes kun af en høj TxGNN-score og en enkelt præklinisk artikel, hvor xylazin sandsynligvis ikke er det undersøgte middel (evidensniveau L5). Kombineret med xylazins ugunstige sikkerhedsprofil hos mennesker og manglende godkendelse til human brug er der ikke grundlag for at gå videre.

**For at komme videre kræves:**
- Data om virkningsmekanisme (MOA) fra DrugBank
- Produktresumé med advarsler og kontraindikationer fra Lægemiddelstyrelsen (blokerende datahul)
- Præklinisk og klinisk evidens, hvor xylazin selv er det undersøgte middel
- Vurdering af, om etablerede alfa-2-agonister med human godkendelse er mere hensigtsmæssige kandidater
- Fuld toksikologisk og sikkerhedsmæssig vurdering til human brug
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

