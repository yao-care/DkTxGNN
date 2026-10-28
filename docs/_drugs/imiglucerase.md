---
layout: default
title: Imiglucerase
parent: Kun modelforudsigelse (L5)
nav_order: 429
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-28
description: "Imiglucerase: forudsagt ny indikation Hurlers syndrom (evidensniveau L4). Oprindelig indikation: Gauchers sygdom"
monitor_inn: "Imiglucerase"
predicted_indications: ["Hurler syndrome", "Scheie syndrome", "benign neoplasm of adrenal gland", "autosomal ichthyosis syndrome with fatal disease course", "cholesteryl ester storage disease"]
---

# Imiglucerase
{: .fs-9 }

Evidensniveau: **L5** | Forudsagte indikationer: **5** stk.
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

## Imiglucerase: Fra Gauchers sygdom til Hurlers syndrom
{: .text-alpha }

## Resumé i én sætning

Imiglucerase er et rekombinant enzym (beta-glucocerebrosidase), som oprindeligt anvendes som enzymerstatningsbehandling ved Gauchers sygdom.
TxGNN-modellen forudsiger, at det kan være virksomt ved **Hurlers syndrom** (MPS I), men der findes **ingen registrerede kliniske forsøg** og kun **1 generel oversigtsartikel**, som ikke dokumenterer effekt af imiglucerase ved denne sygdom.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Gauchers sygdom |
| Forudsagt ny indikation | Hurlers syndrom |
| TxGNN-forudsigelsesscore | 0,9952 |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført (gyldige tilladelser: 1 af 1) |
| Antal markedsføringstilladelser | 1 (gyldige: 1) |
| Anbefalet beslutning | Hold |

---

## Hvorfor er forudsigelsen (ikke) rimelig?

Detaljerede data om virkningsmekanismen er ikke tilgængelige i de data, der er indsamlet til denne rapport. Imiglucerase erstatter det manglende enzym glucocerebrosidase (GBA) ved Gauchers sygdom og nedbryder dermed glucosylceramid.

Hurlers syndrom (MPS I) skyldes mangel på enzymet alfa-L-iduronidase, hvilket medfører ophobning af glykosaminoglykaner (dermatan- og heparansulfat). Begge sygdomme er lysosomale lagringssygdomme, der behandles med enzymerstatning, men forbindelsen er kun konceptuel (fælles behandlingsklasse). Imiglucerase har en anden substratspecificitet og kan ikke erstatte alfa-L-iduronidase. Den høje score kommer fra TxGNN-modellen (deep learning) og kan afspejle ligheder, modellen har lært mellem beslægtede sygdomme, ikke biologisk evidens. Laronidase er den specifikke, godkendte enzymerstatning ved MPS I.

Tilsvarende vurderes den forudsagte indikation **Scheies syndrom** (den mildere form af MPS I, score 0,9929) at være uden direkte mekanistisk grundlag.

### Øvrige forudsigelser i modellen

| Forudsagt indikation | Score | Evidensniveau | Vurdering |
|------|------|------|------|
| Scheies syndrom | 0,9929 | L5 | Samme begrundelse som for Hurlers syndrom; kun en generel oversigtsartikel |
| Godartet binyretumor | 0,9928 | L5 | Ingen evidens og ingen plausibel mekanisme |
| Autosomal ichthyosis-syndrom med dødeligt forløb | 0,9924 | L5 | Spekulativt link via ceramidmetabolisme i huden; intravenøst enzym har dårlig hudpenetration |
| Kolesterylester-lagringssygdom | 0,9912 | L5 | Mangel på lysosomal sur lipase; andet substrat, ingen krydsaktivitet forventet; sebelipase alfa er den specifikke behandling |

---

## Evidens fra kliniske forsøg

Der er i øjeblikket ingen relaterede kliniske forsøg registreret.

---

## Litteraturevidens

| PMID | År | Type | Tidsskrift | Hovedresultater |
|------|-----|------|------|---------|
| [21211680](https://pubmed.ncbi.nlm.nih.gov/21211680/) | 2010 | Oversigtsartikel | La Revue de médecine interne | Generel gennemgang af enzymerstatningsbehandling ved lysosomale lagringssygdomme, herunder imiglucerase ved Gauchers sygdom. Ingen evidens for imiglucerase ved MPS I. |

---

## Markedsinformation i Danmark

| Markedsføringstilladelse | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28103138400 | Cerezyme (Sanofi B.V.) | Pulver til infusionsvæske, opløsning | Indikationstekst ikke tilgængelig |

---

## Sikkerhedsovervejelser

- **Lægemiddelinteraktioner**: Miglustat (moderat niveau, kilde: DDInter).

For øvrige sikkerhedsoplysninger henvises til det godkendte produktresumé (SmPC).

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelsen bygger alene på modelnærhed mellem lysosomale lagringssygdomme. Der er ingen kliniske forsøg, og imiglucerase kan mekanistisk ikke erstatte alfa-L-iduronidase. Specifik og godkendt behandling findes allerede (laronidase).

**For at gå videre kræves:**
- Data om virkningsmekanisme (MOA) og præklinisk dokumentation for enhver aktivitet mod glykosaminoglykan-ophobning
- Gennemgang af produktresumé (warnings og kontraindikationer), som mangler i datagrundlaget
- Kliniske eller prækliniske data, der understøtter en reel fordel frem for eksisterende enzymerstatning
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

