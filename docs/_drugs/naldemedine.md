---
layout: default
title: Naldemedine
parent: Kun modelforudsigelse (L5)
nav_order: 303
evidence_level: L5
indication_count: 0
---

# Naldemedine
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

# Naldemedine: Opioid-induceret obstipation — Ingen TxGNN-forudsigelser tilgængelige

## Resumé i én sætning

Naldemedine (DB11691) er en perifer myopioid-receptorantagonist (PAMORA) godkendt internationalt til behandling af opioid-induceret obstipation (OIC) hos voksne med kroniske ikke-kræftrelaterede smerter.
Den aktuelle Evidence Pack indeholder **ingen TxGNN-forudsagte nye indikationer**, da forudsigelsespipelinen ikke returnerede kandidatsygdomme for dette lægemiddel.
Med nul markedsføringstilladelser i Danmark og kritiske datahullter inden for sikkerhed, virkningsmekanisme og forudsigelsesoutput kan der ikke gennemføres nogen evaluering af omformål på dette tidspunkt.

---

## Hurtigt overblik

| Element | Indhold |
|---------|---------|
| Original indikation | Opioid-induceret obstipation (OIC) — kroniske ikke-kræftrelaterede smerter (baseret på internationale godkendelser; ikke registreret i Evidence Pack) |
| Forudsagt ny indikation | — (Ingen forudsigelser returneret) |
| TxGNN-forudsigelsesscore | — |
| Evidensniveau | L5 (Kun modelforudsigelse — intet output genereret) |
| Markedsstatus i Danmark | Ikke markedsført |
| Antal markedsføringstilladelser | 0 |
| Anbefalet beslutning | **Afvent** |

---

## Hvorfor er denne forudsigelse rimelig?

Der blev ikke returneret TxGNN-forudsigelser for Naldemedine i denne Evidence Pack (`predicted_indications: []`). En omformål-rationalet kan derfor ikke konstrueres fra modeloutput.

Som reference: Naldemedine er et derivat af naltrexon, som er konstrueret til at virke perifer ved at begrænse CNS-penetration. Det antagoniserer µ-, δ- og κ-opioid-receptorer i gastrointestinaltrakten, hvilket reverserer opioid-induceret reduktion af GI-motilitet uden at formindske central analgetisk effekt. Denne stærkt målrettede perifere mekanisme er snæver i omfang, hvilket kan delvist forklare, hvorfor TxGNN-grafgennemgang ikke identificerede stærke tværsygdoms-kandidater.

I øjeblikket er der ikke tilgængelige detaljerede mekanisme-af-virkning-data i Evidence Pack. Baseret på kendt farmakologi tilhører Naldemedine PAMORA-klassen; dets efficacy inden for opioid-induceret obstipation er blevet etableret i pivotale Phase 3-forsøg, og mekanistisk kan det være relevant for bredere motilitätsforstyrrelser i tarmen — men denne hypotese er ikke understøttet af den aktuelle forudsigelse og ville kræve en ny pipeline-kørsel med fuldstændige inputdata.

---

## Kliniske forsøgsdata

Ingen forudsagt indikation er tilgængelig; sygdomsspecifik forsøgsdata kan ikke defineeres.

For fuldstændighed omfatter Naledmedines pivotale OIC-forsøg (lægemidlets etablerede indikation):

| Forsøgsnummer | Fase | Status | Inkludering | Vigtigste resultater |
|-------------|-------|--------|------------|--------------|
| [NCT01965158](https://clinicaltrials.gov/study/NCT01965158) | Fase 3 | Afsluttet | 547 | COMPOSE-1: Naldemedine 0,2 mg vs placebo i OIC; mødte primært endpoint for responder-rate |
| [NCT01993940](https://clinicaltrials.gov/study/NCT01993940) | Fase 3 | Afsluttet | 553 | COMPOSE-2: Bekræftende forsøg; signifikant forbedring i frekvensen af spontane tarmtomninger |
| [NCT02117388](https://clinicaltrials.gov/study/NCT02117388) | Fase 3 | Afsluttet | 1.246 | COMPOSE-3: 52-ugers sikkerhed og efficacy; vedvarende respons opretholdt over langtidsforbrug |

> Disse forsøg relaterer sig til den **godkendte** indikation kun, ikke til noget omformål-target.

---

## Litteraturdata

Ingen omformål-targetindikation er tilgængelig; sygdomsspecifik litteratur kan ikke defineeres.

---

## Markedsinformation for Danmark

Naldemedine er **ikke godkendt til markedsføring i Danmark** ifølge denne Evidence Pack. Ingen nationale (Lægemiddelstyrelsen) eller centraliserede (EMA) markedsføringstilladelser er registreret.

> **Bemærk for undersøgere:** Naldemedine (Symproic®) har EMA-centraliseret markedsføringstilladelse (tildelt 2019) og FDA-godkendelse (2017) for OIC. Fraværet fra det danske marked kan afspejle kommercielle, ikke regulatoriske, årsager. Verifikation mod det aktuelle Lægemiddelstyrelsen-produktregister anbefales, før der drages konklusioner.

---

## Sikkerhedshensyn

Der er ingen sikkerhedsdata tilgængelige i denne Evidence Pack (vigtige advarsler, kontraindikationer og lægemiddelinteraktionsrecords mangler alle). De to kritiske datahullter, som pipelinen har markeret, er:

- **DG001 (Blokering):** TFDA SmPC-advarsler og kontraindikationer blev ikke hentet — forhindrer S1-sikkerhedskontrol.
- **DG002 (Høj):** Virkningsmekanisme-data blev ikke hentet fra DrugBank — forhindrer mekanistisk relevans-analyse.

> Se venligst den godkendte Produktinformationsoversigt (SmPC) — tilgængelig via EMA-produktsiden for Symproic® — for alle sikkerhedsoplysninger, herunder QT-interval-effekter, opioid-tilbagetrækningssymptomer og lægemiddelinteraktioner (især med stærke CYP3A4-inducere/inhibitorer, som kan ændre naldemedins plasmakoncentrationer).

---

## Konklusion og næste skridt

**Beslutning: Afvent**

**Rationalet:**
Evidence Pack er kritisk ufuldstændig — der blev ikke genereret TxGNN-forudsigelser, ingen sikkerhedsdata blev hentet, og der er ingen MOA-oplysninger tilgængelige. En meningsfuld omformål-evaluering kan ikke produceres fra det aktuelle datasæt.

**For at fortsætte er følgende nødvendigt:**

- [ ] **Kør TxGNN-forudsigelsespipelinen igen** med et fuldstændigt inputsæt for at generere omformål-kandidater (`predicted_indications`)
- [ ] **Hent MOA-data fra DrugBank** (DB11691) for at muliggøre mekanistisk plausibilitet-analyse (afhjælpning af DG002)
- [ ] **Download og parse SmPC / receptåt-information** (EMA Symproic® EPAR eller TFDA-produktmonografi) for at udfylde sikkerhedsadvarsler, kontraindikationer og lægemiddelinteraktioner (afhjælpning af DG001)
- [ ] **Bekræft Danmark/EMA-markedsstatus** direkte fra Lægemiddelstyrelsen-produktregisteret, da det EMA-godkendte Symproic® kan allerede være tilgængeligt via den centraliserede procedure
- [ ] Når forudsigelser er tilgængelige, genudsted denne rapport under standard v5-formatet med fulde evidenstabeller

---

> ⚠️ *Denne rapport er genereret til forskningsmæssige formål udelukkende og udgør ikke medicinsk rådgivning. Enhver lægemiddel-omformål-kandidat kræver klinisk validering før terapeutisk anvendelse.*

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

