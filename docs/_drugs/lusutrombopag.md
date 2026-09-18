---
layout: default
title: Lusutrombopag
parent: Kun modelforudsigelse (L5)
nav_order: 273
evidence_level: L5
indication_count: 10
---

# Lusutrombopag
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

# Lusutrombopag: Fra [oprindelig indikation ikke tilgængelig] til arveligt trombocytopeni med normale blodplader

## Sammenfatning på én sætning

Lusutrombopag (DrugBank DB13125) er en thrombopoietin (TPO)-receptor (MPL) agonist; dens oprindeligt godkendte indikation er ikke registreret i denne bevissamling, og medicinen er ikke aktuelt markedsført i Danmark. TxGNN-modellen forudsiger en mulig sammenhæng med **arveligt trombocytopeni med normale blodplader**, men denne forudsigelse understøttes af **0 kliniske forsøg** og **0 publikationer**, og det underliggende mekanistiske rationale selv flags som en sandsynlig mismatch (se nedenfor).

---

## Hurtig oversigt

| Punkt | Indhold |
|------|---------|
| Oprindelig indikation | Ikke tilgængelig i bevissamlingen (ingen dansk licenstekst; `original_moa` er også flagget som datakløft) |
| Forudsagt ny indikation | Arveligt trombocytopeni med normale blodplader |
| TxGNN-forudsigelsesscore | 99.995% |
| Bevisniveau | L5 |
| Markedsstatus i Danmark | Ikke markedsført |
| Antal markedsføringstilladelser | 0 |
| Anbefalet afgørelse | Vent |

---

## Hvorfor er denne forudsigelse rimelig?

Detaljerede oplysninger om oprindelig indikation og formale MOA-data er ikke udfyldt i denne bevissamling (flagget som datakløfter DG001 og DG002). Baseret på den mekanistiske beskrivelse fanget i modellens eget begrundelsestekst er Lusutrombopag en **thrombopoietin (TPO)-receptor (MPL) agonist**: det stimulerer proliferation og differentiering af benmarvsmegarcarycytter for at øge cirkulerende blodplade-**antal**. Denne klasse medicin bruges typisk når trombocytopeni skyldes utilstrækkelig blodplade-produktion.

Den forudsagte indikation, "arveligt trombocytopeni med normale blodplader," er problematisk i sig selv — sygdomsnavnet specificerer selv **normale blodplade-antal**, hvilket betyder at den underliggende patologi ikke skyldes utilstrækkelig blodplade-produktion, men snarere en arvelig blodplade-funktionel/strukturel abnormitet. En TPO-RA's mekanisme for *øget blodplade-antal* har ingen klar modpart i en tilstand hvor blodplade-antal allerede er normalt, så det mekanistiske link er svagt.

Den samme forsigtighed gælder for de andre top-rankede kandidater i denne bevissamling: "macrothrombocytopeni med mitralklap-insufficiens," "dense granule-sygdom," og "blodplade-lagringspulje-defekt" er alle funktionelle/strukturelle blodplade-lidelser snarere end produktionsforstyrrelser, og "forbigående neonatal trombocytopeni" er en selvbegrænsende tilstand uden etablerede pædiatriske sikkerhedsdata for denne medicin. Alle blev scoret L5/Vent internt, konsistent med høje TxGNN-lighedsscore men lav biologisk plausibilitet — sandsynligvis afspejlende videngraf-sammentræf (delt "blodplade" og "trombocytopeni" terminologi) snarere end kausal mekanisme.

---

## Bevis fra kliniske forsøg

Der er i øjeblikket ingen relaterede kliniske forsøg registreret.

---

## Bevis fra litteratur

Der er i øjeblikket ingen relateret litteratur tilgængelig.

---

## Markedsoplysninger for Danmark

Lusutrombopag er ikke aktuelt markedsført i Danmark (0 markedsføringstilladelser registreret; markedsstatus: "Ikke markedsført" / ikke markedsført).

---

## Sikkerhedsovervejelser

Venligst se det godkendte Produktresumé (SmPC) for sikkerhedsinformation. Ingen vigtige advarsler, kontraindikationer eller medicin-medicin interaktionsdata er aktuelt tilgængelige i bevissamlingen (DDI-søgning returnerede "ikke fundet").

---

## Konklusion og næste skridt

**Afgørelse: Vent**

**Begrundelse:**
- Den forudsagte indikations egen definition (normalt blodplade-antal) er mekanistisk uforenelig med en thrombopoietin-receptor agonists blodplade-antal-forhøjende virkning, og dette mønster gentager sig blandt de andre top-rankede kandidater i denne bevissamling.
- Der er nul kliniske forsøg eller litteraturunderstøttelse (L5 — modelforudsigelse alene), medicinen er ikke markedsført i Danmark, og sikkerhedsdata (advarsler, kontraindikationer, DDI) er helt utilgængelige — inklusiv et Blocking-alvorligheds-kløft (DG001) som forhindrer enhver S1 sikkerhedsvurdering.

**For at fortsætte kræves følgende:**
- Danske/EU SmPC-advarsler og kontraindikationer (DG001, Blocking)
- Bekræftet virkningsmåde via DrugBank eller primærlitteratur (DG002, High)
- Klinisk/hæmatologisk specialistvurdering af det mekanistiske mismatch mellem TPO-RA-virkning og de blodplade-funktionelle (ikke produktions-) lidelser forudsagt her
- Original godkendt indikationstekst, for ordentligt at ramme medicin-kandidat-sammenlignelighed
- Hvis dette skal forfølges videre kræves målrettet litteratur- og registreringssøgning specifikt for TPO-RA-brug ved arvelig blodplade-funktionelle lidelser, da standard kliniske forsøg/PubMed-søgninger ikke gav noget resultat

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

