---
layout: default
title: Gabapentin
parent: Kun modelforudsigelse (L5)
nav_order: 198
evidence_level: L5
indication_count: 0
---

# Gabapentin
{: .fs-9 }

Evidensniveau: **L5** | Forudsagte indikationer: **0** stk.
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

# Gabapentin: Evidenspakke ufuldstændig — Vurdering af genanvendelse afventer

## Opsummering i én sætning

Gabapentin (DB00996) er et lægemiddel med bekræftede DrugBank-poster, men denne evidenspakke indeholder **ingen TxGNN-forudsagte indikationer**, hvilket gør en standard vurdering af genanvendelse umulig på nuværende tidspunkt.
Vigtige datakløfter — herunder oprindelige indikationer, virkningsmekanisme, markedsstatus i Danmark og sikkerhedsdata — skal løses, før nogen vurdering kan finde sted.
En **Hold**-beslutning anbefales, indtil pipelinen korrigeres, og prognoser genereres.

---

## Hurtig oversigt

| Punkt | Indhold |
|-------|---------|
| Oprindelig indikation | Ikke registreret i denne evidenspakke |
| Forudsagt ny indikation | Ingen prognoser genereret |
| TxGNN prognose-score | Ikke tilgængelig |
| Evidensniveau | Ikke vurderbart |
| Markedsstatus i Danmark | Ikke tilgængelig (pipelinefejl mistænkt) |
| Antal markedsføringstilladelser | 0 (sandsynligvis ufuldstændig — se nedenfor) |
| Anbefalet beslutning | **Hold** |

---

## Hvorfor denne vurdering ikke kan gennemføres

Evidenspakken for Gabapentin (DB00996) mangler tre datakategorier, som hver enkelt er tilstrækkelig til at blokere vurderingen:

**1. Ingen TxGNN-forudsagte indikationer**
`predicted_indications`-arrayet er tomt. En vurdering af genanvendelse kræver mindst én prognose-destination. Uden den er der ingen sygdomskontekst, som kliniske forsøg eller litteratur kan vurderes imod. Dette er den mest kritiske blokkering.

**2. Oprindelig indikation og virkningsmekanisme utilgængelige**
Både `original_indications` og `original_moa` mangler fra denne evidenspakke. Datapipelinen markerede MOA som et højt-sværhedsgrads-gap (DG002) og anbefalede hentning fra DrugBank — bemærkelsesværdigt returnerede DrugBank-forespørgslen den 26. marts 2026 status `success` med 1 resultat, hvilket tyder på, at dataene eksisterer i DrugBank, men ikke blev overført til denne evidenspakke.

**3. Markedsstatus i Danmark ser ud til at være en pipelinefejl**
Evidenspakken rapporterer `market_status: "Not marketed"` (ikke markedsført) med 0 licenser. Gabapentin er blevet godkendt i EU i mange år; et resultat på nul licenser antyder kraftigt en forbindelsesfejl til Lægemiddelstyrelsen eller EMA's datakilde snarere end et ægte fravær af godkendelser. Dette skal verificeres, før nogen lovgivningsmæssig vurdering foretages.

---

## Markedinformation for Danmark

Der blev ikke hentet markedsføringstilladelsesposter i denne evidenspakke. Manuel verifikation med Lægemiddelstyrelsen eller EMA's produktdatabase er påkrævet, før dette felt kan udfyldes.

---

## Sikkerhedshensyn

Se venligst det godkendte Produktresumé (SmPC) for sikkerhedsinformation.

---

## Konklusion og næste trin

**Beslutning: Hold**

**Begrundelse:**
Evidenspakken mangler sit væsentligste input — TxGNN-forudsagte indikationer — og kan ikke understøtte nogen struktureret vurdering af genanvendelse. Alle efterfølgende afsnit (bevis for kliniske forsøg, litteraturbevis, mekanismeanalyse, sikkerhedsgennemgang) afhænger af, at der foreligger et prognose-mål.

**For at fortsætte er følgende nødvendig:**

- **Genud køring af TxGNN-prognose-pipeline** for Gabapentin (DB00996) for at generere `predicted_indications`; bekræft, om det tomme resultat afspejler et ægte modeloutput eller en pipelineudførselsfejl
- **Hentning af MOA og oprindelige indikationer fra DrugBank** — DrugBank-forespørgslen fra 26. marts 2026 returnerede success; dataene bør ekstraheres og udfyldes i evidenspakken
- **Verifikation af danske lovgivningsdata** — kontrollér Lægemiddelstyrelse / EMA-dataforbindelsen; resultatet "0 licenser" er inkonsistent med kendt EU-lovgivningshistorik for dette lægemiddel
- **Løsning af DG001 (TFDA-advarsler/kontraindikationer)** — download og parse det relevante SmPC-PDF for at udfylde sikkerhedsfelter før nogen klinisk vurdering

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

