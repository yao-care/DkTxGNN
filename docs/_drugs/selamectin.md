---
layout: default
title: Selamectin
parent: Kun modelforudsigelse (L5)
nav_order: 394
evidence_level: L5
indication_count: 10
---

# Selamectin
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

# Selamectin: Fra veterinær antiparasitisk brug til Candidiasis

## Sammenfattelse på en sætning

Selamectin er en avermectin-klasse macrocyclisk lacton godkendt udelukkende som et veterinært antiparasiticum (lopper, mider, hjertemark-forebyggelse hos hunde og katte) — det har ingen godkendt humant indicæ og ingen markedsføringstilladelse i Danmark. TxGNN-modellen forudsiger potentiel effektivitet for **Candidiasis**, men denne forudsigelse understøttes i øjeblikket af **0 kliniske forsøg** og **0 publikationer**, og er baseret udelukkende på knowledge-graph topologi snarere end nogen kendt antifungal mekanisme.

---

## Hurtigt overblik

| Emne | Indhold |
|------|---------|
| Original indicæ | Ikke etableret til humant brug — godkendt kun som veterinært antiparasiticum (ekto-/endoparasit-kontrol hos selskasbsdyr); ingen humane indicæ-data tilgængelige |
| Forudsagt ny indicæ | Candidiasis |
| TxGNN forudsigelsesscore | 98.43% |
| Bevisgrad | L5 |
| Markedsstatus i Danmark | Ikke markedsført |
| Antal markedsføringstilladelser | 0 |
| Anbefalet beslutning | Afvent |

---

## Hvorfor er denne forudsigelse rimelig?

Detaljerede data om virkningsmekanisme er ikke tilgængelige (MOA markeret som datamangel). Baseret på de tilgængelige informationer er Selamectin en avermectin-klasse macrocyclisk lacton, hvis kendt farmakologi aktiverer invertebrat glutamat-styrede chloridkanaler — en mekanisme specifik for arthropod- og nematodenervesystemer. Det har ingen dokumenteret antifungal aktivitetsvej.

Der er ingen etableret mekanistisk eller klinisk sammenhæng mellem Selamectins godkendte veterinære antiparasitiske brug og menneskelig candidiasis (en svampeinfektion). Bevisepakkets egen rationale er eksplicit på dette punkt: den høje TxGNN-score (0.984) afspejler graph-topologisk lighed inden for knowledge graph snarere end nogen farmakologisk plausibilitet.

Fordi Selamectin aldrig er blevet undersøgt hos mennesker — det har ingen humane PK/PD-data, ingen human sikkerhedsdatabase, og toksikologi er begrænset til veterinær-/dyreforsøg — kan mekanistisk ekstrapolation til candidiasis i øjeblikket ikke understøttes.

---

## Bevis fra kliniske forsøg

I øjeblikket ingen relaterede kliniske forsøg registreret.

---

## Litteraturbevis

I øjeblikket ingen relateret litteratur tilgængelig.

---

## Informationer om det danske marked

Selamectin har ingen markedsføringstilladelse i Danmark (0 licenser på fil); produktet er i øjeblikket ikke registreret hos Lægemiddelstyrelsen eller centralt gennem EMA.

---

## Sikkerhedsovervejelser

Se venligst det godkendte produktresumé (SmPC) for sikkerhedsinformationer. Ingen vigtige advarsler, kontraindikationer eller lægemiddelinteraktionsdata er i øjeblikket tilgængelige for denne kandidat.

---

## Konklusion og næste trin

**Beslutning: Afvent**

**Rationale:**
- Candidiasis-forudsigelsen har nul understøttende kliniske forsøg eller litteratur, ingen plausibel virkningsmekanisme, ingen humane sikkerhedsdata, og lægemidlet er ikke registreret i Danmark — beviserne er utilstrækkelige til at fortsætte ud over model-forudsigelse-stadiet (L5/S0).

**For at fortsætte er følgende nødvendigt:**
- Bekræftede data om virkningsmekanisme (MOA) fra DrugBank eller primær litteratur
- Eventuelle prækliniske (in vitro/in vivo) antifungal aktivitetsdata for Selamectin
- Humane farmakokinetiske og sikkerhed/toksikologi-data, givet at lægemidlet ikke har tidligere eksponeringshistorie hos mennesker
- Advarsler og kontraindikationer på TFDA/EMA/SmPC-niveau før der kan påbegyndes S1 sikkerhedsscreening

**Notat om datakvalitet:** Blandt de øvrige TxGNN-kandidater i denne pakke understøttes forudsigelsen "hjertesygdom" (rang 9–10, L4) kun af veterinær litteratur om *hjertemark-sygdom* (Dirofilaria immitis infektion) — en tilsyneladende keyword-matching artefakt ("hjertemark-sygdom" → "hjertesygdom"), ikke bevis for aktivitet mod menneskelig hjertesygdom. Dette bør ikke læses som understøttende bevis for en kardiovaskulær indicæ.

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

