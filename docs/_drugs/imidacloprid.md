---
layout: default
title: Imidacloprid
parent: Kun modelforudsigelse (L5)
nav_order: 427
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Imidacloprid: forudsagt ny indikation Cauda equina-syndrom (evidensniveau L5). Oprindelig indikation: Ikke angivet i godkendelsesteksten (veterinært produkt til hund)"
---

# Imidacloprid
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

# Imidacloprid: Fra et veterinært lægemiddel til hund til cauda equina-syndrom

## Resumé i en sætning

Imidacloprid er et insektmiddel af neonikotinoid-typen. I Danmark er det markedsført som veterinært lægemiddel til hund (Advantage Vet.), og et originalt humant indikationsområde er ikke angivet i de data, der er indsamlet til denne rapport.
TxGNN-modellen forudsiger, at stoffet kan have effekt på **cauda equina-syndrom**, men der er **0 kliniske forsøg** og **0 relevante publikationer** til støtte for dette.
Forudsigelsen er udelukkende baseret på en grafmodel og bør betragtes som spekulativ.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Ikke angivet i godkendelsesteksten (veterinært produkt til hund) |
| Forudsagt ny indikation | Cauda equina-syndrom |
| TxGNN-forudsigelsesscore | 99,99 % |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført |
| Antal markedsføringstilladelser | 1 |
| Anbefalet beslutning | Hold |

---

## Hvorfor er forudsigelsen (ikke) rimelig?

Data om lægemidlets virkningsmekanisme var ikke tilgængelige i de indsamlede data. Imidacloprid er dog kendt som et neonikotinoid, der virker som agonist på insekters nikotinerge acetylcholinreceptorer (nAChR). Stoffet har langt højere affinitet for insekters end for pattedyrs receptorer, hvilket er grunden til, at det anvendes som insekticid.

Cauda equina-syndrom er en kompressionsrelateret neurologisk tilstand, som typisk behandles kirurgisk. Der er ikke påvist nogen plausibel mekanistisk sammenhæng mellem en nAChR-agonist rettet mod insekter og behandling af denne tilstand. Den høje score afspejler sandsynligvis mønstre i vidensgrafen snarere end biologisk sandsynlighed.

Andre forudsagte indikationer i datasættet har samme begrænsninger:
- **Neurogen blære** (betegnelsen er markeret som forældet i ontologien): en teoretisk kolinerg forbindelse, men spekulativ og uden støtte.
- **Irritabel tarm-syndrom**: enterisk nikotinerg signalering påvirker tarmmotilitet, men imidaclopridens selektivitet og neurotoksicitetssignaler hos pattedyr gør sammenhængen spekulativ.
- **Medfødt misdannelse af spiserøret**: strukturelle udviklingsafvigelser kan ikke forventes at kunne behandles farmakologisk.
- **Spiserørssygdom**: se litteraturafsnittet nedenfor.

---

## Evidens fra kliniske forsøg

Der er i øjeblikket ingen relaterede kliniske forsøg registreret.

---

## Litteraturevidens

Der er ingen litteratur, som direkte omhandler cauda equina-syndrom. Den eneste fundne publikation vedrører en anden forudsagt indikation (spiserørssygdom):

| PMID | År | Type | Tidsskrift | Hovedfund |
|------|-----|------|------|---------|
| [29506575](https://pubmed.ncbi.nlm.nih.gov/29506575/) | 2018 | Veterinært klinisk forsøg (dobbeltblindet, placebokontrolleret) | Parasites & Vectors | Spot-on-præparat med imidacloprid og moxidectin (Advocate®) sammenlignet med injicerbart doramectin ved spirocercose i spiserøret hos hunde. Den antiparasitære effekt tilskrives moxidectin, og studiet understøtter ikke human anvendelse. |

---

## Markedsinformation for Danmark

| Markedsføringstilladelsesnr. | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28101891197 | Advantage Vet. til hund (Elanco Animal Health GmbH) | Kutanopløsning | Ikke angivet |

---

## Sikkerhedsovervejelser

Der foreligger ikke sikkerhedsdata i de indsamlede data. Der blev ikke fundet oplysninger om lægemiddelinteraktioner. Se det godkendte produktresumé (SmPC) for sikkerhedsoplysninger.

Det bemærkes, at imidacloprid er et veterinært/landbrugsprodukt, og at der er toksikologiske bekymringer vedrørende neurotoksicitet hos pattedyr. Stoffet er ikke etableret som humant lægemiddel.

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelsen hviler udelukkende på en grafbaseret score uden kliniske forsøg eller relevant litteratur, og der er ingen plausibel mekanistisk sammenhæng. Stoffet er et veterinært produkt uden etableret human terapeutisk anvendelse.

**For at gå videre kræves følgende:**
- Data om virkningsmekanisme (MOA) fra DrugBank
- Indlægsseddel/produktresumé med advarsler og kontraindikationer fra Lægemiddelstyrelsen (sikkerhedsscreening kan ikke gennemføres uden)
- Præklinisk dokumentation for en biologisk sammenhæng mellem stoffet og den forudsagte indikation
- Vurdering af toksikologi og pattedyrsselektivitet samt administrationsvej (kompatibilitet er ikke afklaret)
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

