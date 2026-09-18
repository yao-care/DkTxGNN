---
layout: default
title: Daratumumab
parent: Kun modelforudsigelse (L5)
nav_order: 129
evidence_level: L5
indication_count: 0
---

# Daratumumab
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

# Daratumumab: Ingen genbrugsprognose genereret — Evaluering afventer

## Sammenfatning på én sætning

Daratumumab (DB09331) er et CD38-målrettet monoklonalt antistof, der anvendes til behandling af multipel myelomatose, og er registreret af EMA under handelsnavn Darzalex.
TxGNN-prognoseprocessen **genererede ingen genbrugsprognose** for dette lægemiddel i den aktuelle evalueringscyklus, da kritiske inputdata — herunder virkningsmekanisme og oprindelige indikationsfelter — manglede i Evidence Pack.
**Ingen kliniske forsøgs- eller litteraturbevis kunne derfor indsamles eller vurderes**, og en formel genbrugsevaluering kan ikke gennemføres på dette stadium.

---

## Hurtig oversigt

| Punkt | Indhold |
|-------|---------|
| Oprindelig indikation | Ikke registreret i Evidence Pack |
| Forudsagt ny indikation | Ingen genereret |
| TxGNN-prognosescore | Ikke tilgængelig |
| Bevisniveau | Ikke vurderbar (L5-niveau ikke nået — ingen prognoseoutput) |
| Markedsstatus i Danmark | Ikke registreret per Evidence Pack-data |
| Antal markedsføringstilladelser | 0 (per Evidence Pack) |
| Anbefalet beslutning | **Afvent** |

> ⚠️ **Dataintegritetsnote:** Evidence Pack registrerer 0 danske markedsføringstilladelser og status "ikke markedsført". Dette er inkonsistent med den offentligt kendte centraliserede EMA-tilladelse for Darzalex (daratumumab) til multipel myelomatose, som er gyldig i alle EU/EØS-medlemsstater, herunder Danmark. Reguleringskilden bør verificeres, før denne feltværdi stoles på.

---

## Hvorfor der ikke blev genereret prognoser

TxGNN-modellen kræver to input for at generere genbrugskandidater: (1) en valideret DrugBank-ID matchet til vidensgraph, og (2) mindst én mapset godkendt indikation, hvorfra modellen udleder mekanistisk lighed. For daratumumab (DB09331) bekræfter Evidence Pack et vellykket DrugBank-søgning, men registrerer **ingen oprindelige indikationer** i feltet `original_indications`. Uden en kilde-indikationnode kan modellen ikke gennemløbe vidensgraphen for at identificere målsygdomskandidater, og ingen prognosescore outputtes.

Derudover mangler virkningsmekanisme-feltet (MOA). MOA-data bruges efterfølgende til at kontekstualisere og prioritere kandidater; dets fravær betyder, at selv manuel prioritering af ethvert fremtidigt modeloutput ville være forsvækket.

Fra generel farmakologisk viden binder daratumumab CD38 — et glykoprotein, der udtrykkes højt på plasmacelleår — og inducerer tumorceldød gennem antistof-afhængig cellulær cytotoxicitet (ADCC), komplementafhængig cytotoxicitet (CDC) og apoptose. Dets godkendt brug ved multipel myelomatose er veletableret og biologisk sammenhængende. Når Evidence Pack er rettificeret (se Næste trin), kan TxGNN-modellen generere prognoser for hæmatologiske malignniteter og potentielt andre CD38-udtrykkende tilstande, såsom systemisk lupus erythematosus eller AL-amyloidose — begge områder af aktiv klinisk forskning globalt.

---

## Cytotoxicitet

Daratumumab klassificeres som et antineoplastisk lægemiddel (målrettet immunoterapi / monoklonalt antistof) baseret på dets godkendt terapeutisk brug ved multipel myelomatose.

| Punkt | Indhold |
|-------|---------|
| Cytotoxicitet-klassificering | Målrettet immunoterapi — anti-CD38 IgG1κ monoklonalt antistof (ikke konventionel cytotoxisk) |
| Myelosuppressionrisiko | Moderat til høj — infusionsrelaterede reaktioner, neutropeni, trombocytopeni og anæmi rapporteres almindeligt i produktinformation |
| Emetogenicitet-klassificering | Lav (monoklonale antistoffer har minimalt direkte emetogent potentiale) |
| Kontrolpunkter | Komplet blodtal (CBC med differencial) før hver cyklus; nyrefunktion; immunoglobulin-niveauer; hepatitis B-screening før initiering |
| Håndteringsbeskyttelse | Standard aseptisk håndtering af parenterale biologiske lægemidler; ingen klassificering som særligt affald for cytotoxiske lægemidler påkrævet, men institutionelle biofareprotokol for monoklonale antistoffer gælder |

> Se venligst det godkendt SmPC for Darzalex for fuldstændig forordning, håndtering og kontrolvejledning.

---

## Sikkerhedshensyn

Se venligst det godkendt Produktinformation (SmPC) for Darzalex for fuldstændig sikkerhedsinformation, herunder styring af infusionsrelaterede reaktioner, immuniseringspræcautioner og interferens med serum-proteinelektroforeseassays (daratumumab er en kendt kilde til falsk-positive M-protein-resultater).

---

## Konklusion og næste trin

**Beslutning: Afvent**

**Begrundelse:**
Evidence Pack for daratumumab (DB09331) er kritisk ufuldstændig — ingen oprindelige indikationsdata, ingen virkningsmekanisme, og ingen TxGNN-genbrugsprognose blev genereret. En meningsfuld genbrugsevaluering kan ikke gennemføres på grundlag af tilgængelige data alene, og at gå videre til klinisk gennemførlighedsvurdering ville være for tidligt.

**For at fortsætte er følgende nødvendigt:**

- **[Blokerer — DG001]** Hent SmPC / produktinformation for Darzalex fra EMA's produktdatabase eller Lægemiddelstyrelsen for at udtrække godkendt indikationer, vigtige advarsler og kontraindikationer
- **[Høj — DG002]** Søg DrugBank-API'et for DB09331 for at udfylde MOA-feltet; dette er påkrævet for vidensgraph-prognosesteget og for mekanistisk plausibilitetsvurdering
- **Kør TxGNN-pipeline igen** når `original_indications` og `original_moa` er udfyldt i Evidence Pack
- **Ret reguleringsdata** — verificer Danmark / EMA markedsføringstilladelsestatus mod EMA EPAR-databasen (Darzalex EU/1/16/1101); det nuværende "ikke markedsført"-flag ser ud til at afspejle en datakildekløft snarere end faktisk markedsfravær
- **Supplementært søgning** — når prognoser er genereret, indsaml kliniske forsøgsdata fra ClinicalTrials.gov og EudraCT / EU Clinical Trials Register for enhver ny indikation (f.eks. AL-amyloidose, POEMS-syndrom, lupusnefrit) for at vurdere bevisniveauet

---

*Denne rapport er genereret til forskningsmæssige formål alene og udgør ikke medicinsk rådgivning. Alle genbrugskandidater kræver klinisk validering før enhver terapeutisk anvendelse. Rapport genereret: 2026-04-05 | Evidence Pack-version: v4 | Kandidat-ID: TW-DB09331-multi.*

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

