---
layout: default
title: Epoprostenol
parent: Kun modelforudsigelse (L5)
nav_order: 169
evidence_level: L5
indication_count: 0
---

# Epoprostenol
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

# Epoprostenol (DB01240): Pulmonary Arterial Hypertension — Evidenspakke ufuldstændig, vurdering afventer

---

## Sammenfatning på en sætning

Epoprostenol (prostacyclin, PGI₂) er et syntetisk vasodilatator og aggregationshæmmer for blodplader, klassisk brugt til behandling af pulmonal arteriel hypertension (PAH).
Imidlertid indeholder den nuværende Evidenspakke **ingen TxGNN-forudsigelsesoutput** og **ingen danske markedsautoriseringsregistre**, hvilket betyder, at en fuldstændig vurdering af lægemiddelomformål ikke kan gennemføres på nuværende tidspunkt.
Denne rapport dokumenterer de identificerede datakløfter og anbefaler en struktureret afhjælpelsessti, før man går videre.

---

## Hurtigt overblik

| Element | Indhold |
|---------|---------|
| Original indikation | Pulmonal arteriel hypertension (baseret på generel farmakologisk viden; ikke leveret i evidenspakke) |
| Forudsagt ny indikation | Ingen forudsigelsesdata tilgængelige |
| TxGNN-forudsigelsesscore | Ingen forudsigelsesdata tilgængelige |
| Evidensniveau | Ikke vurderbart |
| Markedsstatus i Danmark | Ikke registreret (0 licenser på fil — sandsynligvis en datakollektionsfejl; EU centraliserede autoriseringer eksisterer) |
| Antal markedsføringstilladelser | 0 (på fil) |
| Anbefalet beslutning | **Afvent** — kritiske datakløfter skal løses først |

---

## Hvorfor denne rapport ikke kan gennemføres endnu

TxGNN-modellens forudsigelsespipeline returnerede ikke nogle omformålskandidater for Epoprostenol i denne Evidenspakke (version v4, dataudklip 2026-04-05). To datakløfter med høj alvorlighed er blevet formelt registreret:

| Kløft-ID | Kategori | Manglende element | Alvorlighed | Indvirkning |
|----------|----------|------------------|------------|-------------|
| DG001 | Lægemiddelsniveau | Danish Medicines Agency (Lægemiddelstyrelsen) / EMA godkendte advarsler og kontraindikationer | **Blokerende** | Kan ikke fuldføre S1-sikkerhedsskrinning |
| DG002 | Lægemiddelsniveau | Virkningsmekanisme (MOA) | **Høj** | Kan ikke udføre mekanistisk plausibilitetsvurdering for nogen forudsagt indikation |

Indtil disse kløfter er løst, og TxGNN-pipelinen køres igen med komplette inputdata, kan en meningsfuld vurdering af lægemiddelomformål ikke genereres.

---

## Markedsinformation Danmark

Evidenspakken registrerer **nul markedsføringstilladelser** for Epoprostenol i Danmark. Dette er uoverensstemmelse med offentligt kendt myndighedsstatus: Epoprostenol er tilgængelig i EU under centraliserede EMA-procedurer (f.eks. *Flolan*, *Veletri*), som automatisk giver autorisation i alle EU/EEA-medlemsstater, herunder Danmark.

**Dette tyder stærkt på en datakollektionsfejl snarere end sand fravær fra det danske marked.**

| Forventet autorisation | Produktnavn | Doseringform | Bemærkning |
|------------------------|------------|-------------|-----------|
| EMA centraliseret (bekræft via EMA EPAR-database) | Flolan | Pulver og opløsningsmiddel til infusionsvæske | PAH — bekræft nuværende status på ema.europa.eu |
| EMA centraliseret (bekræft via EMA EPAR-database) | Veletri | Pulver til infusionsvæske | PAH — bekræft nuværende status på ema.europa.eu |

> **Påkrævet handling:** Forespørg [EMA Product Database](https://www.ema.europa.eu/en/medicines) og [Lægemiddelstyrelsens produktresumé-database](https://www.laegemiddelstyrelsen.dk/) for at hente aktuelle autorisationsnumre, SmPC og godkendte indikationer.

---

## Sikkerhedshensyn

Ingen sikkerhedsdata blev hentet til denne evidenspakke. Alle vigtige advarsels-, kontraindikations- og lægemiddelinteraktionsfelter mangler.

> Se venligst det godkendte produktresumé (SmPC) — tilgængelig via [EMA EPAR for Flolan](https://www.ema.europa.eu/en/medicines/human/EPAR/flolan) eller [Veletri](https://www.ema.europa.eu/en/medicines/human/EPAR/veletri) — for fuldstændig sikkerhedsinformation før nogen klinisk vurdering.

---

## Konklusion og næste trin

**Beslutning: Afvent**

**Begrundelse:**
Evidenspakken for Epoprostenol mangler både TxGNN-forudsigelsesoutput og sikkerhedsdata for Danmark/EMA, hvilket gør det umuligt at vurdere nogen omformålshypotese eller evaluere risiko–nytte på nuværende tidspunkt.

**For at fortsætte, kræves følgende:**

1. **Kør TxGNN-pipelinen igen** for DB01240 og bekræft, at `predicted_indications` er udfyldt med mindst ét kandidat, før der genereres en fuldstændig rapport.
2. **Hent MOA-data (DG002)** fra DrugBank API (DrugBank-ID: DB01240) — Epoprostenol forventes at virke via prostacyclinreceptor (IP-receptor) agonisme, hvilket fører til cAMP-medieret vasodilatation og hæmning af blodpladeaggregation; bekræft og udfyld `original_moa`.
3. **Hent SmPC-advarsler og kontraindikationer (DG001)** fra EMA EPAR-dokumenter for Flolan/Veletri; parse og udfyld `safety.key_warnings` og `safety.contraindications`.
4. **Korriger Danmarks myndighedsopslag** ved at forespørge EMA's centraliserede autorisationsdatabase og Lægemiddelstyrelsens produktresumé-register; opdater `taiwan_regulatory.market_status`, `total_licenses` og `licenses[]`.
5. **Gensend den udfyldte Evidenspakke** for at regenerere en fuldstændig evalueringsrapport med forudsagte indikationer, mekanistisk begrundelse, kliniske forsøgsevidens og en endelig Go / Proceed with Guardrails-anbefaling.

---

*Denne rapport er genereret til forskningsreference alene og udgør ikke medicinsk rådgivning. Alle lægemiddelomformålskandidater kræver klinisk validering før nogen terapeutisk anvendelse.*

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

