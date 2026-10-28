---
layout: default
title: Zanamivir
parent: Kun modelforudsigelse (L5)
nav_order: 899
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-28
description: "Zanamivir: forudsagt ny indikation Pyelonefritis (evidensniveau L5). Oprindelig indikation: Influenza"
monitor_inn: "Zanamivir"
predicted_indications: ["pyelonephritis", "disorder of tyrosine metabolism"]
---

# Zanamivir
{: .fs-9 }

Evidensniveau: **L5** | Forudsagte indikationer: **2** stk.
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

## Zanamivir: Fra influenza til pyelonefritis
{: .text-alpha }

## Resumé i én sætning

Zanamivir er en neuraminidasehæmmer, som oprindeligt bruges til behandling af influenza. TxGNN-modellen forudsiger, at lægemidlet kan have effekt mod **pyelonefritis**, men der er **ingen registrerede kliniske forsøg** og **ingen publikationer**, der understøtter denne forudsigelse. Forudsigelsen er udelukkende beregningsbaseret.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Influenza (godkendt indikationstekst for det danske produkt er ikke angivet i de indsamlede data) |
| Forudsagt ny indikation | Pyelonefritis |
| TxGNN-forudsigelsesscore | 0,9984 |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført (gyldige tilladelser: 1 af 1) |
| Antal markedsføringstilladelser | 1 (gyldige: 1) |
| Anbefalet beslutning | Hold |

---

## Hvorfor er denne forudsigelse (ikke) rimelig?

Der foreligger på nuværende tidspunkt ingen detaljerede data om virkningsmekanismen. Zanamivir er kendt som en hæmmer af viralt neuraminidase, et enzym influenzavirus bruger til at frigive nye viruspartikler fra inficerede celler. Lægemidlets effekt ved influenza er veldokumenteret.

Pyelonefritis er derimod typisk en bakteriel infektion i nyren. Der er ingen klar mekanistisk forbindelse mellem hæmning af viralt neuraminidase og behandling af en bakteriel nyreinfektion. Mennesker har egne neuraminidaser (NEU1-4), men der er intet, der tyder på, at hæmning af dem er relevant for pyelonefritis.

Den høje score (0,9984) stammer fra TxGNN-modellen (deep learning) og kan afspejle ligheder, som modellen har lært mellem beslægtede sygdomme, og ikke biologisk evidens. Forudsigelsen bør derfor betragtes som en hypotese uden understøttende evidens.

---

## Klinisk evidens fra forsøg

Der er på nuværende tidspunkt ingen relaterede kliniske forsøg registreret.

---

## Litteraturevidens

Der er på nuværende tidspunkt ingen relateret litteratur for pyelonefritis.

---

## Markedsinformation for Danmark

| Markedsføringstilladelsesnummer | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28106043117 | Dectova (GlaxoSmithKline Trading Services) | Infusionsvæske, opløsning | Indikationstekst ikke angivet i de indsamlede data |

---

## Sikkerhedsovervejelser

- **Lægemiddelinteraktioner** (8 registrerede i de indsamlede data):
  - Insulin humant (inhaleret, hurtigtvirkende): moderat
  - Clarithromycin, loratadin, montelukast, ketotifen, fexofenadin, ibuprofen og diclofenac: sværhedsgrad ikke klassificeret
- **Sygdomme, der i vidensgrafen er knyttet til kontraindikation** (ikke hentet fra produktresuméet): epilepsi, kronisk obstruktiv lungesygdom (KOL), bronkial sygdom og delirium.

Se i øvrigt det godkendte produktresumé (SmPC) for fuldstændige sikkerhedsoplysninger.

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelsen for pyelonefritis bygger udelukkende på en modelscore uden kliniske forsøg, uden litteratur og uden en plausibel mekanistisk sammenhæng mellem en viral neuraminidasehæmmer og en bakteriel nyreinfektion. Der findes desuden allerede etablerede antibiotiske behandlinger.

**For at komme videre kræves følgende:**
- Data om virkningsmekanisme (MOA) fra DrugBank
- Produktresumé for Dectova fra Lægemiddelstyrelsen med advarsler og kontraindikationer
- Prækliniske eller mekanistiske data, der kan underbygge en eventuel rolle i pyelonefritis
- Gennemgang af de øvrige forudsigelser (fx forstyrrelser i tyrosin- og phenylalaninstofskiftet og Pierre Robin-syndrom), som heller ikke har mekanistisk eller klinisk støtte og ligeledes har evidensniveau L5
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

