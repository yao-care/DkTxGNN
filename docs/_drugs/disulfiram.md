---
layout: default
title: Disulfiram
parent: Kun modelforudsigelse (L5)
nav_order: 144
evidence_level: L5
indication_count: 0
---

# Disulfiram
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

# Disulfiram (DB00822): Evaluering af lægemiddel-genudnyttelse — Ufuldstændig datapakke

> ⚠️ **Meddelelse:** Dette evidenspakke indeholder kritiske datahiater. TxGNN-modellen returnerede **ingen forudsagte indikationer**, og regulatoriske, sikkerhedsmæssige og virkningsmekanisme-data er fraværende fra pakken. Denne rapport dokumenterer aktuelle resultater og specificerer de afhjælpningstrin, der er nødvendige, før en fuldstændig evaluering af lægemiddel-genudnyttelse kan udføres.

---

## Sammenfatning i én sætning

Disulfiram (DrugBank: DB00822) er en velkendt aldehyd dehydrogenase (ALDH)-hæmmer, klassisk anvendt til alkoholmisbrug (aversionsbehandling).
Dog indeholder det aktuelle evidenspakke **ingen TxGNN-forudsagte indikationer**, **ingen godkendte produktregistreringer i Danmark**, og **ingen maskinlæsbare sikkerhedsdata**, hvilket gør en standardevaluering af lægemiddel-genudnyttelse umulig på nuværende tidspunkt.
En **Suspender**-beslutning anbefales, indtil de blokerende datahiater er løst.

---

## Hurtig oversigt

| Element | Indhold |
|---------|---------|
| Oprindelig indikation | Alkoholmisbrug (aversionsbehandling) — fra generel farmakologisk viden; ingen strukturerede indikationsdata i denne pakke |
| Forudsagt ny indikation | **Ikke tilgængelig** — TxGNN returnerede ingen forudsigelser for denne kandidat |
| TxGNN-forudsigelsesscore | Ikke tilgængelig |
| Evidensniveau | **L5** (kun modelforudsigelse — og selv denne er fraværende; effektivt urangeret) |
| Markedsstatus i Danmark | **Ikke markedsført** |
| Antal godkendelser til markedsføring | **0** |
| Anbefalet beslutning | **Suspender** |

---

## Hvorfor er denne forudsigelse rimelig?

Ingen forudsagt indikation er tilgængelig i dette evidenspakke, så ingen mekanistisk forbindelses-analyse kan udføres på nuværende tidspunkt.

Fra etableret farmakologisk viden hæmmer Disulfiram irreversibelt **aldehyd dehydrogenase (ALDH)**, hvilket forårsager ophobning af acetaldehyd, når ethanol indtages, som fremkaldes disulfiram-ethanol-reaktionen, der bruges terapeutisk ved alkoholaversionsbehandling. Uden for denne klassiske rolle har ALDH-hæmning og sekundær kobberkelat-aktivitet tiltrukket forskningsmæssig interesse inden for onkologi (særligt glioblastom og brystkræft) og infektionssygdoms-kontekster — imidlertid afspejles ingen af dette i det aktuelle evidenspakke, og **ingen strukturerede virkningsmekanisme-data (DB002 — høj alvorlighed)** er tilgængelige for formelt at understøtte sådan begrundelse her.

Når DrugBank API-forespørgslen er fuldført og `original_moa` er udfyldt, kan en mekanistisk analyse genereres.

---

## Klinisk forsøgsevidans

Ingen forudsagt indikation er til stede i dette evidenspakke; derfor kan ingen indikations-specifik klinisk forsøgsevidans ekstraheres eller tabuleres.

I øjeblikket ingen relaterede kliniske forsøg registreret under en TxGNN-forudsagt indikation.

---

## Litteraturevidans

I øjeblikket ingen relateret litteratur tilgængelig under en TxGNN-forudsagt indikation.

---

## Markedsinformationer for Danmark

Disulfiram har **ingen godkendelser til markedsføring** registreret i Danmark på tidspunktet for denne dataudtræk (2026-04-05).

| Godkendelsesnummer til markedsføring | Produktnavn | Doseringform | Godkendt indikation |
|-------------------------------|-------------|-------------|-------------------|
| — | — | — | Ingen godkendelser på registrering |

> **Bemærk:** Disulfiram (mærkenavn *Antabuse*) er registreret i flere EU-medlemsstater og har EMA-præcedens. En separat manuel søgning i Lægemiddelstyrelsens produktregister og EMA's centraliserede database anbefales for at bekræfte, om der eksisterer nogen parallelle imposter eller dispensations-baserede forsyninger.

---

## Sikkerhedsmæssige overvejelser

> Se venligst det godkendte produktresume (SmPC) for sikkerhedsinformationer.

Alle sikkerhedsfelter i dette evidenspakke bærer blokerande datahiater:

- **Vigtige advarsler**: Ikke tilgængelig (DG001 — blokeringssværhed). Kilde: Dansk SmPC / Lægemiddelstyrelsens produktmonografi.
- **Kontraindikationer**: Ikke tilgængelig (DG001 — blokeringssværhed).
- **Lægemiddel–lægemiddel-interaktioner**: Forespørgsel returnerede `not_found` (0 interaktioner). Dette afspejler sandsynligvis en forespørgselsfejl snarere end fraværet af interaktioner — Disulfiram er kendt for at interagere med warfarin, phenytoin, metronidazol og flere andre midler.

Indtil DG001 er løst, **bør der ikke træffes sikkerhedsbaserede ordinationsbeslutninger på grundlag af denne rapport**.

---

## Konklusion og næste trin

**Beslutning: Suspender**

**Begrundelse:**
Evidenspakken er strukturelt ufuldstændig — TxGNN-forudsigelsespipelineen returnerede ingen kandidatindikationer, og både de regulatoriske og sikkerhedsmæssige datalag er fraværende. Der er ingen handlingsdygtig genudnyttelses-signal at evaluere på nuværende tidspunkt.

**For at fortsætte kræves følgende:**

1. **[DG001 — Blokering]** Hent det danske SmPC (eller EMA SmPC hvis relevant) for Disulfiram; gennemgå advarsler, kontraindikationer og særlige forholdsregler. *Kilde: Lægemiddelstyrelsen / EMA produktmonografi PDF.*
2. **[DG002 — Høj]** Forespørg DrugBank API for DB00822 for at udfylde `original_moa`, farmakodynamik og toksicitetsfelter. *Kilde: DrugBank `https://go.drugbank.com/drugs/DB00822`.*
3. **[Forudsigelseshiatus — Kritisk]** Undersøg hvorfor `predicted_indications` er tom:
   - Bekræft at Disulfiram (DB00822) er til stede i TxGNN-videnskabsgrafen-nodelisten (`data/node.csv`).
   - Kør `scripts/run_kg_prediction.py` igen med eksplicit DrugBank ID-søgning for at bekræfte pipeline-færdiggørelse.
   - Hvis lægemidlet mangler fra KG'en, tilføj det som en seednode og forudsig igen.
4. **[DDI-hiatus — Høj]** Kør DDI-forespørgslen igen med alternative lægemiddelname-varianter (f.eks. "disulfiram", "tetraethylthiuram disulfide") og bekræft at `not_found`-status ikke er en normaliserings-fejl.
5. **[Markedsstatus]** Krydstjek med Lægemiddelstyrelsens online produktregister og EMA's EPAR-database for at bekræfte nul-godkendelsesstatus og identificere eventuelle compassionate-use- eller navngiven-patient-forsyningsveje, der i øjeblikket er aktive i Danmark.

---

*Denne rapport blev genereret fra evidenspakke `TW-DB00822-multi` (v4, datakutoff 2026-04-05). Resultaterne er udelukkende til forskningsmæssig reference og udgør ikke medicinsk rådgivning. Alle kandidater til genudnyttelse kræver klinisk validering før anvendelse.*

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

