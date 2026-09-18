---
layout: default
title: Abatacept
parent: Høj evidens (L1-L2)
nav_order: 11
evidence_level: L2
indication_count: 10
---

# Abatacept
{: .fs-9 }

Evidensniveau: **L2** | Forudsagte indikationer: **10** stk.
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

# Rapport om lægemiddelnyi anvendelse af evidens: Abatacept (DB01281)

**Kandidat-ID**: TW-DB01281-multi
**Rapportversion**: v4
**Dato for genereringen**: 2026-04-03
**Datoskæring**: 2026-04-03
**Udarbejdet til**: Lægemiddelstyrelsen (Danish Medicines Agency) Kontekst

---

## 1. Ledelsessammenfatning

| Felt | Detalje |
|------|---------|
| **Lægemiddel (INN)** | Abatacept |
| **DrugBank ID** | DB01281 |
| **Handelsnavn** | Orencia (Bristol-Myers Squibb) |
| **Antal forudsagte indikatorer** | 5 (unikke sygdomme) |
| **Højeste evidensniveau opnået** | **L1** — Inflammatorisk spondyloartropatologi (psoriasis-artritis subtype) |
| **Topanbefaling** | **Fortsæt med sikringsmekanismer** (inflammatorisk spondyloartropatologi / PsA) |

**Sammenfatning af vigtigste fund:**

Abatacept, en selektiv T-celle co-stimulation modulator (CTLA-4-Ig fusionprotein), blev evalueret af TxGNN vidensgrafodelens model på tværs af fem forudsagte sygdomsindikatorer. Analysen afdækker et spektrum af evidensmodning:

1. **Inflammatorisk spondyloartropatologi** (specifikt psoriasis-artritis [PsA] subtype): **L1 evidens** — understøttet af en afsluttet fase 3 RCT (NCT01860976, n=489), ACR/NPF 2018 guideline-inclusion og store post-marketing sikkerhedsdata, herunder en **Danmark-specifik DANBIO-registerstudie** (NCT05421442, n=38,396). Abatacept er allerede godkendt af EMA/FDA for PsA. **Anbefaling: Fortsæt med sikringsmekanismer.**
2. **Ankiloserende spondylitis (AS)**: **L2 evidens** — en fase 2 open-label pilot (NCT00558506, n=30; PMID 21415053) demonstrerede **begrænset effektivitet**, i overensstemmelse med et mekanistisk mismatch (AS primært drevet af IL-17/IL-23-aksen i stedet for T-celle co-stimulation). **Anbefaling: Hold pause.**
3. **Reumatoid vaskulitis**: **L4 evidens** — case reports viser **modstridende signaler** (både terapeutisk fordel og nyt-opstart vaskulitis under abatacept-terapi). Ingen kliniske forsøg. **Anbefaling: Forskningsspørgsmål.**
4. **Hypermobilitet af os coccygis**: **L5 evidens** — kun AI-forudsigelse. Ingen biologisk plausibilitet. **Anbefaling: Hold pause.**
5. **Kümmels sygdom**: **L5 evidens** — kun AI-forudsigelse. Ingen biologisk plausibilitet. **Anbefaling: Hold pause.**

> **Identificerede datagab**: Lægemiddelstyrlsens produktresumé advarsler/kontraindikationer og detaljerede virkningsmekanisme-data kræver supplementering fra DrugBank API og det danske produktresumé (produktresumé).

---

## 2. Lægemiddeloversigt

### 2.1 Godkendte indikatorer

#### Danmark (Lægemiddelstyrelsen / EMA Centraliseret Autorisation)

Abatacept (Orencia) holder en centraliseret EMA markedsføringstilladelse gyldig i Danmark for:

| Indikator | Population | Vej |
|-----------|-----------|-----|
| Leddegigt (RA) | Voksne med moderat til svær aktiv RA med utilstrækkelig respons på DMARD'er, herunder methotrexat eller en TNF-inhibitor | IV infusion / subkutan injektion |
| Polyartikulær juvenil idiopatisk artritis (pJIA) | Pediatriske patienter ≥2 år | IV / subkutan |
| Psoriasis-artritis (PsA) | Voksne med aktiv PsA med utilstrækkelig respons på DMARD'er | Subkutan injektion |

> **Bemærk**: Evidenspakken angiver taiwansk regulatorisk status som "Ikke markedsført" (ikke markedsført). I modsætning hertil er abatacept **godkendt og markedsført i Danmark** under EMA-centraliseringsproceduren.

#### FDA (Amerikanske Forenede Stater)

FDA-godkendte indikatorer svarer til EMA-godkendelser: RA (voksne), pJIA (≥2 år), PsA (voksne) og derudover forebyggelse af akut graft-versus-host-sygdom (aGVHD) i kombination med en calcineurin-inhibitor og methotrexat.

### 2.2 Virkningsmekanisme

Abatacept er et opløseligt fusionsprotein bestående af det ekstracellulære domæne af humant cytotoksisk T-lymfocyt-associeret antigen 4 (CTLA-4) bundet til den modificerede Fc-portion af humant immunoglobulin G1 (IgG1). Det virker som en selektiv co-stimulation modulator ved at:

1. **Binde CD80/CD86** på antigen-præsenterende celler (APC'er), og dermed blokere interaktion med CD28 på T-celler
2. **Hæmme "Signal 2"-co-stimulationsvejledningen** påkrævet for fuld T-celleaktivering
3. **Præferativt undertrykke naïve T-celleaktivering**, mens der er mindre effekt på hukommelsesT-celler
4. **Nedstrøms reduktion** af pro-inflammatoriske cytokiner (TNF-α, IL-6, IL-2) og autoantistof-produktion

> ⚠️ **Datagab (DG002)**: Fuldstændig MOA-karakterisering fra DrugBank API blev flagget som ufuldstændig i evidenspakken. Ovenstående er rekonstrueret fra publiceret litteratur.

### 2.3 Farmakokinetisk profil

| Parameter | IV-formulering | Subkutan formulering |
|-----------|---------------|----------------------|
| **Biotilgængelighed** | 100% (reference) | ~78.6% (subkutan vs IV) |
| **T_max** | End af infusion | ~7 dage (subkutan) |
| **Half-life (t½)** | ~13 dage (område 8–25 dage) | ~14.3 dage |
| **Steady-state** | Ved uge 8 (med loading) | Ved uge 12–13 |
| **Clearance** | ~0.22 mL/h/kg | Lignende |
| **Volumen af distribution (Vss)** | ~0.07 L/kg | — |
| **Dosering (IV)** | Vægtbaseret: <60 kg: 500 mg; 60–100 kg: 750 mg; >100 kg: 1000 mg; Dag 1, 15, 29, derefter hver 4. uge | — |
| **Dosering (subkutan)** | — | 125 mg ugentlig (med eller uden IV loading-dosis) |
| **Stofskifte** | Proteolytisk nedbrydning (ikke CYP-medieret) | Samme |
| **Immunogenicitet** | Lav dannelse af anti-stof (~2–3%) | Lignende |

---

## 3. Evidensanalyse

### Oversigt: Sammenfatning af forudsagte indikatorer

| Rang | Sygdom | TxGNN Score | Evidensniveau | Beslutningsstadium | Anbefaling |
|------|--------|-------------|---------------|-------------------|------------|
| 1 | Reumatoid vaskulitis | 0.999 | **L4** | S1 | Forskningsspørgsmål |
| 2 | Ankiloserende spondylitis | 0.999 | **L2** | S1 | Hold pause |
| 3 | Hypermobilitet af os coccygis | 0.999 | **L5** | S0 | Hold pause |
| 4 | Inflammatorisk spondyloartropatologi | 0.998 | **L1** | S3 | **Fortsæt med sikringsmekanismer** |
| 5 | Kümmels sygdom | 0.998 | **L5** | S0 | Hold pause |

---

### 3.1 Inflammatorisk spondyloartropatologi (psoriasis-artritis subtype)

**Evidensniveau: L1 | Beslutningsstadium: S3 | Anbefaling: Fortsæt med sikringsmekanismer**

Dette er den **stærkeste kandidat**, der er identificeret. Inflammatorisk spondyloartropatologi omfatter psoriasis-artritis (PsA), for hvilken abatacept allerede er godkendt globalt. Evidensgrundlaget er robust.

#### 3.1.1 Kliniske forsøg

| NCT ID | Titel | Fase | Status | N | Vigtigste fund |
|--------|-------|------|--------|---|---------------|
| **NCT01860976** | Fase 3 RCT: Abatacept subkutan i aktiv PsA | **Fase 3** | **Afsluttet** | 489 | Pivotal-forsøg: abatacept subkutan vs placebo i PsA; primært endepunkt nået. Førte til regulatorisk godkendelse. |
| **NCT00534313** | Fase 2b RCT: Abatacept vs placebo i PsA | Fase 2b | Afsluttet | 191 | Dosis-finding-studie; etablerede optimal dosering for PsA. |
| **NCT05421442** | Post-marketing sikkerhed: DANBIO-register (Danmark) | Post-marketing | **Afsluttet** | **38,396** | **Danmark-specifik**: landsomfattende post-marketing-overvågning af abatacept i RA- og PsA-patienter via DANBIO. |
| **NCT05413044** | Post-marketing sikkerhed: SRQ-register (Sverige) | Post-marketing | Afsluttet | 140,706 | Svensk landsomfattende sikkerhedsovervågning; malignitets-incidensdata. |
| **NCT03419143** | ALTEA: Virkelig verden PsA (Tyskland) | Observationel | Afsluttet | 190 | Langsigtet virkelig verden effektivitet og sikkerhed i PsA. |
| **NCT04106804** | ABEPSA: Knoglbiomarkører i PsA | Fase 4 | Ukendt | 20 | Abatacept knogleffekter i PsA via MRI og biomarkører. |
| **NCT00558506** | Pilot: Abatacept i AS | Fase 2 | Ukendt | 30 | Relevant til kun AS subtype; begrænset effektivitet rapporteret. |
| **NCT05080218** | COVER: COVID-19-vaccine respons | Fase 4 | Afsluttet | 841 | Sikkerhedsdata på vaccine-respons i patienter på abatacept. |

#### 3.1.2 Publiceret litteratur

**Tier 1 (retningslinjer / metaanalyser):**

- **PMID 30499246** — *ACR/NPF 2018 Guideline for the Treatment of PsA* (Arthritis & Rheumatology, 2019): Abatacept er inkluderet som en anbefalet biologisk DMARD-option for PsA-patienter med utilstrækkelig respons på csDMARD'er. Dette er en **klinisk praksis-guideline** fra de to ledende faglige organer.
- **PMID 39992258** — *Abatacept and the risk of malignancy: a meta-analysis across disease indications* (Rheumatology, 2025): Tværindikation metaanalyse, der vurderer malignitetsrisiko; giver vigtige sikkerhedsdata relevant for langsigtet brug i spondyloartritis.

**Tier 2 (systematiske reviews / vigtige reviews):**

- **PMID 28612180** — Systematisk review af immunogenicitet af biologika på tværs af inflammatoriske sygdomme.
- **PMID 38331098** — Vaccinations-retningslinjer for patienter på biologika, herunder abatacept.
- **PMID 38499181** — Perioperativ management-retningslinjer for abatacept i PsA-patienter.
- **PMID 29737909** — Review af biologiske og kliniske profiler af PsA-respondenter på abatacept; bemærker differentiel effektivitet på tværs af PsA-domæner (effektiv for perifer artritis, mindre for aksial sygdom og hud).
- **PMID 31171316** — Kommende behandlingsmuligheder for SpA; placerer abatacept inden for det terapeutiske landskab.
- **PMID 38639758** — Lægemiddelterapi i juvenil spondyloartritis; reviewerer abatacept-evidens i pædiatrisk JSpA.

#### 3.1.3 Mekanistisk begrundelse

Inflammatorisk spondyloartropatologi omfatter tilstande drevet af adaptiv immunologisk dysregulering, især PsA. Abatacepts hæmning af T-celle co-stimulation modulerer effektivt den adaptive immune respons i PsA, særligt for perifere leddmanifestationer. ACR/NPF 2018-retningslinjerne betinget anbefaler abatacept for behandlings-naïve PsA-patienter og dem med utilstrækkelig respons på TNF-inhibitorer.

**Vigtig tilføjelse**: Abatacept viser **begrænset effektivitet for aksial sygdom** inden for spondyloartritispektret. Dens godkendelse og guideline-anbefalinger er begrænset til perifere PsA-manifestationer, ikke aksial spondyloartritis (herunder AS).

#### 3.1.4 Danmark-specifik evidens

**DANBIO-registerstudien (NCT05421442)** er af særlig relevans:
- **Design**: Landsomfattende post-marketing-overvågning med det danske DANBIO biologika-register
- **Stikprøve**: 38,396 deltagere med RA eller PsA behandlet med abatacept
- **Status**: Afsluttet (2019–2025)
- **Formål**: Udvidet post-marketing-overvågning af abatacept-sikkerhed
- Dette studie giver **sikkerhedsdata fra virkelig verden på dansk befolkingsniveau**, direkte relevant for Lægemiddelstyrlsens beslutningstagning.

---

### 3.2 Ankiloserende spondylitis

**Evidensniveau: L2 | Beslutningsstadium: S1 | Anbefaling: Hold pause**

#### 3.2.1 Kliniske forsøg

| NCT ID | Titel | Fase | Status | N | Vigtigste fund |
|--------|-------|------|--------|---|---------------|
| **NCT00558506** | Pilot Open-Label: Abatacept i AS | Fase 2 | Ukendt | 30 | **Kerneevidence**: 24-ugers open-label pilot demonstrerede **begrænset effektivitet** (PMID 21415053). |
| NCT04610476 | Fase 3 PsA-nedtrapning RCT | Fase 3 | Ukendt | 270 | PsA-fokuseret; tangentiel til AS. |

#### 3.2.2 Publiceret litteratur

**Vigtig publikation:**

- **PMID 21415053** — *Treatment of active ankylosing spondylitis with abatacept: an open-label, 24-week pilot study* (Song et al., Ann Rheum Dis, 2011): Dette er det **eneste direkte kliniske studie** af abatacept i AS. Resultater viste **begrænset klinisk effektivitet**, hvor størstedelen af patienter ikke opnåede ASAS20-respons. Studiet blev ikke videreført til fase 3.

**Understøttende reviews:**

- **PMID 27856659** — Sieper (Rheumatology, 2016): Udtrykkelig angivelse af, at "konventionelle DMARD'er og også ikke-TNF-blokker biologika, der targets IL-1, IL-6 og T-celler (abatacept) **er ikke effektive**" i axSpA.
- **PMID 22450391** — Kiltz et al. (Curr Opin Rheumatol, 2012): Reviewerer alternativer til TNF-refraktær AS; abatacept vurderet, men fundet utilstrækkeligt effektiv.
- **PMID 19822066** — Braun & Kalden (Clin Exp Rheumatol, 2009): Diskuterer patogene forskelle mellem RA og AS, som forklarer differential biologika-respons.

#### 3.2.3 Mekanistisk begrundelse

AS er primært drevet af HLA-B27/IL-17/IL-23-aksen, med medfødt immunitet, der spiller en overvejende rolle. T-celle co-stimulation-blokade via abatacept targets ikke effektivt denne vej. De kliniske data (PMID 21415053) bekræfter dette mekanistiske mismatch. **Denne indikation bør ikke forfølges yderligere.**

---

### 3.3 Reumatoid vaskulitis

**Evidensniveau: L4 | Beslutningsstadium: S1 | Anbefaling: Forskningsspørgsmål**

#### 3.3.1 Kliniske forsøg

Ingen kliniske forsøg, der direkte studerer abatacept for reumatoid vaskulitis, blev identificeret. Et tangentielt relateret forsøg (NCT07138898, immunosuppressiv management i skulderartroplaski) fik relevansgrad C.

#### 3.3.2 Publiceret litteratur

Evidensen består helt af **case reports med modstridende signaler**:

| PMID | Type | År | Vigtigste fund | Signalretning |
|------|------|-----|---------------|---------------|
| **22124545** | Case Report | 2012 | 38-årig kvinde med refraktær RV: abatacept producerede **hurtig klinisk forbedring** efter fiasko med steroider, plasmafærese og tocilizumab. | **Positiv** ✅ |
| **29930884** | Case Report/Serie | 2018 | Patient med RA + common variable immunodeficiency: abatacept brugt som alternativ til rituximab for kutanøs RV. | **Positiv** ✅ |
| **27052429** | Case Report | 2016 | **Nyt udbrud** af reumatoid vaskulitis udviklet **under** abatacept-terapi; efterfølgende forbedret med rituximab. | **Negativ** ⚠️ |
| **30119075** | Case Report | 2018 | RA-associeret orbitalvaskulitis præsenteret **mens på abatacept**. | **Negativ** ⚠️ |
| **36418100** | Case Report | 2023 | ANCA-associeret nefritis udviklet under abatacept + adalimumab-terapi. | **Negativ** ⚠️ |

#### 3.3.3 Mekanistisk begrundelse

Reumatoid vaskulitis (RV) er en alvorlig ekstraarticulær manifestation af RA, der involverer T-celle-medieret vaskulær væg-inflammation. Teoretisk set kunne abatacepts hæmning af T-celle co-stimulation undertrykke den opstrøms autoimmun-vaskulær inflammation. Men de offentliggjorte case reports præsenterer **modstridende evidens**:

- **For**: Cases af refraktær RV reagerende på abatacept (PMID 22124545, 29930884)
- **Mod**: Cases af nyt-opstart vaskulitis udviklet under abatacept-terapi (PMID 27052429, 30119075)

Denne diskordans antyder, at forholdet mellem CTLA-4-vejlednings-modulation og vaskulitis er kompleks og muligvis patient-subtype-afhængig.

---

### 3.4 Hypermobilitet af os coccygis

**Evidensniveau: L5 | Beslutningsstadium: S0 | Anbefaling: Hold pause**

Ingen kliniske forsøg, ingen litteratur, ingen mekanistisk plausibilitet. Coccygeal hypermobilitet er en mekanisk/strukturel tilstand, der involverer ligamentøs laksitet eller ledforstyring. Der er ingen immunmedieret komponent, der ville reagere på T-celle co-stimulation-blokade. Det høje TxGNN-score (0.999) afspejler sandsynligvis **grafnærhedsartefakt** inden for klusteren af muskuloskeletale sygdomme. **Dette betragtes som en falsk positiv.**

---

### 3.5 Kümmels sygdom

**Evidensniveau: L5 | Beslutningsstadium: S0 | Anbefaling: Hold pause**

Ingen kliniske forsøg, ingen litteratur, ingen mekanistisk plausibilitet. Kümmels sygdom (forsinket post-traumatisk vertebral body-kollaps / avaskular nekrose af vertebralkroppen) er en mekanisk/vaskulær tilstand. Der er ingen rationel basis for immunmodulatorisk terapi. **Dette betragtes som en falsk positiv.**

---

## 4. Sikkerhedshensyn

> ⚠️ **Datagab (DG001)**: Produktresumé-advarsler og kontraindikationer fra det danske/EMA produktresumé var ikke tilgængelige i evidenspakken. Følgende er baseret på EMA Summary of Product Characteristics (SmPC) for Orencia og publiceret litteratur.

### 4.1 Kendte bivirkninger

**Almindelige (≥1/100 til <1/10):**
- Øvre luftvejsinfektioner (nasopharyngitis, sinusitis)
- Urinvejsinfektioner
- Hovedpine
- Kvalme, diarré
- Injektionssted-reaktioner (subkutan formulering)
- Infusionsrelaterede reaktioner (IV formulering)

**Ualmindelige (≥1/1.000 til <1/100):**
- Herpes zoster
- Lungebetændelse
- Forhøjede transaminaser

**Sjælden, men alvorlig:**
- Alvorlige infektioner (herunder sepsis, tuberkulose, opportunistiske infektioner)
- Malignitet (metaanalyse PMID 39992258 fandt ingen signifikant øget risiko for malignitet ekskluderet NMSC)
- Overfølsomhed/anafylaxi
- Autoimmun-fænomener (paradoksal vaskulitis — se afsnit 3.3)

### 4.2 Lægemiddelinteraktioner

| Interaktion | Alvorlighed | Detalje |
|-------------|-----------|---------|
| **Andre biologika (TNF-inhibitorer, IL-6-inhibitorer, rituximab)** | **Kontraindikeret** | Samtidig brug øger alvorlig infektionsrisiko uden tilføjet effektivitet |
| **Live-vacciner** | **Kontraindikeret** | Live-vacciner bør ikke administreres samtidigt eller inden for 3 måneder efter seponering |
| **Methotrexat** | Tilladt | Almindeligt brugt i kombination; ingen signifikant PK-interaktion |
| **Kortikosteroider** | Tilladt | Ingen signifikant interaktion; standard ledsageende brug |
| **Ikke-live vacciner** | Forsigtighed | Immunrespons kan være svækket; timing-overvejelser gælder (se PMID 38331098) |

> **Bemærk**: DDI-søgning returnerede 0 resultater fra evidenspakkens database (forespørgselsstatus: not_found). Ovenstående er sammensat fra SmPC-data og publicerede retningslinjer.

### 4.3 Kontraindikationer

Baseret på EMA SmPC:
- Overfølsomhed over for abatacept eller nogen hjælpestof
- Alvorlig og ukontrolleret aktiv infektion (fx sepsis, opportunistiske infektioner, aktiv tuberkulose)
- Samtidig brug med andre biologiske DMARD'er

### 4.4 Særlige populationer

| Population | Anbefaling |
|-----------|-----------|
| **Graviditet** | Begrænsede data; kun brug hvis klart nødvendigt (PMID 40256995 — scoping review af DMARD'er i graviditet) |
| **Amning** | Abatacept påvist i modermælk; risiko-fordel vurdering nødvendig |
| **Tuberkulose-screening** | Obligatorisk før initiering (PMID 39963138) |
| **Hepatitis B/C** | Screen før initiering |
| **Ældre** | Ingen dosisændring; øget infektions-årvågenhed |

### 4.5 Post-marketing sikkerhedsdata (Danmark-specifik)

**DANBIO-registerstudien (NCT05421442)** giver store danske sikkerhedsdata:
- **38,396 deltagere** med RA eller PsA i Danmark
- Overvågningsperiode: 2019–2025 (afsluttet)
- Fokus: udvidet post-marketing-sikkerhed, herunder malignitet, infektioner og kardiovaskulære begivenheder

Det supplerende **svenske SRQ-registerstudie (NCT05413044)** includerede 140,706 deltagere, der giver yderligere nordisk virkelig verden sikkerhedsbenchmarking.

---

## 5. Regulatorisk status

### 5.1 Danmark (Lægemiddelstyrelsen)

| Parameter | Status |
|-----------|--------|
| **Produktnavn** | Orencia |
| **Markedsføringstilladelse** | **Godkendt** (EMA centraliseret procedure, gyldig i Danmark) |
| **Godkendte indikatorer** | RA (voksne), PsA (voksne), pJIA (≥2 år) |
| **Formuleringer** | IV infusion (frysetørret pulver 250 mg); subkutan injektion (125 mg/mL præfyldt sprøjte/pen) |
| **DANBIO-register** | Aktivt; abatacept inkluderet i national biologika-overvågning |
| **Post-marketing studie** | NCT05421442 afsluttet (n=38,396) |

### 5.2 EMA-status

| Parameter | Detalje |
|-----------|---------|
| **Første godkendelse** | 2007 (RA) |
| **PsA-extension** | 2017 |
| **Aktuel SmPC-version** | Regelmæssigt opdateret |
| **PASS-krav** | Igangværende post-autoriserings sikkerhedsstudier (herunder NCT05421442, NCT05413044) |

### 5.3 FDA-status

| Parameter | Detalje |
|-----------|---------|
| **Første godkendelse** | 2005 (RA) |
| **PsA-godkendelse** | 2017 |
| **aGVHD-forebyggelse** | 2021 (unik til FDA, ikke EMA-godkendt herfor) |
| **Formuleringer** | IV og subkutan (samme som EMA) |

### 5.4 Regulatorisk status-sammenfatning for forudsagte indikatorer

| Forudsagt indikator | Danmark/EMA | FDA | Status |
|-------------------|-------------|-----|--------|
| Inflammatorisk spondyloartropatologi (PsA subtype) | **Godkendt** | **Godkendt** | Allerede autoriseret |
| Ankiloserende spondylitis | Ikke godkendt | Ikke godkendt | Fase 2 mislykkedes; usandsynligt at gennemføres |
| Reumatoid vaskulitis | Ikke godkendt | Ikke godkendt | Kun case reports |
| Hypermobilitet af os coccygis | Ikke godkendt | Ikke godkendt | Ingen evidens |
| Kümmels sygdom | Ikke godkendt | Ikke godkendt | Ingen evidens |

---

## 6. Konklusion og anbefalinger

### 6.1 Samlet vurdering

| Indikator | Evidensniveau | Konklusion | Handlemulighed |
|-----------|---------------|-----------|-----------------|
| **Inflammatorisk spondyloartropatologi (PsA)** | L1 | ✅ Allerede godkendt | Ingen repurposing nødvendig; sikre fuld udnyttelse i dansk klinisk praksis |
| **Ankiloserende spondylitis** | L2 | ❌ Negativ evidens | Forfølg ikke; mekanistisk mismatch bekræftet klinisk |
| **Reumatoid vaskulitis** | L4 | ⚠️ Modstridende signaler | Kun akademisk forskningsinteresse; ingen klinisk vej berettiget |
| **Hypermobilitet af os coccygis** | L5 | ❌ Falsk positiv | Forkast; ingen biologisk plausibilitet |
| **Kümmels sygdom** | L5 | ❌ Falsk positiv | Forkast; ingen biologisk plausibilitet |

### 6.2 Evidensgab

| Gab-ID | Punkt | Alvorlighed | Anbefalet afhjælpning |
|--------|-------|-----------|----------------------|
| DG001 | Lægemiddelstyrlsens produktresumé advarsler/kontraindikationer | Blokerende | Download og parse det danske-sproget SmPC fra Lægemiddelstyrlsens/EMA produktdatabase |
| DG002 | Detaljerede MOA-data fra DrugBank | Høj | Query DrugBank API for komplet target/enzym/transporter-profiler |
| — | Rute-kompatibilitet-vurdering | Medium | Krydstjek tilgængelige danske formuleringer med påkrævede administrationsveje for hver indikator |
| — | Sygdoms-mapping fuldstændighed | Lav | Flere litteraturposter har "pending"-klassifikation; fuldend relevans-gradning |
| — | Duplikatposter i evidenspakke | Lav | Ranger 1/2, 3/4, 5/6, 7/8, 9/10 virker dublerede; deduplikér i fremtidige pipeline-kørsler |

### 6.3 Foreslåede næste trin

#### For inflammatorisk spondyloartropatologi (PsA):
1. **Ingen repurposing-handling påkrævet** — abatacept er allerede EMA-godkendt for PsA og tilgængeligt i Danmark
2. **Udnyt DANBIO-data** (NCT05421442) til at informere Lægemiddelstyrlsens post-marketing-overvågningsrapportering
3. Overvej et **udnyttelses-studie** via DANBIO for at vurdere real-world optagelse og behandlingssekvensering af abatacept i danske PsA-patienter

#### For reumatoid vaskulitis:
1. **Formoder som forskningsspørgsmål** for akademisk undersøgelse
2. Gennemfør et **systematisk review af alle publicerede cases** af abatacept-brug i RV (både terapeutisk og paradoksal)
3. Overvej et **nationalt case series** via danske reumatologi-centre for at identificere eventuelt off-label brugs-mønstre
4. **Anbefal ikke klinisk brug** uden for et formelt forskningsprotokol givet modstridende sikkerhedssignaler

#### For ankiloserende spondylitis:
1. **Ingen videre handling** — negativ fase 2 data og mekanistisk mismatch
2. Arkivér evidens til reference

#### For hypermobilitet af os coccygis og Kümmels sygdom:
1. **Flag som TxGNN falsk positive** for modelkalibrering
2. Disse afspejler sandsynligvis vidensgrafs-node-nærhedsartefakter i klusteren af muskuloskeletale sygdomme

### 6.4 Pipeline-kvalitets-noter

Evidenspakken indeholdt **duplikatposter** (ranger 1/2, 3/4, 5/6, 7/8, 9/10 er identiske sygdomspar). Dette bør adresseres i datapipeline for at undgå oppustede kandidattællinger. Efter deduplikering er der **5 unikke forudsagte indikationer** snarere end 10.

---

## Tillæg A: Datakildre forespurgt

| Kilde | Forespørgsler kørt | Fund fundet |
|-------|------------------|-----------|
| DrugBank | 1 | 1 (lægemiddel-profil) |
| ClinicalTrials.gov | 10 | 32 forsøg (på tværs af alle indikatorer) |
| ICTRP | 10 | 0 |
| PubMed | 10 | 97 publikationer (på tværs af alle indikatorer) |
| DDI-database | 1 | 0 (ikke fundet) |

## Tillæg B: Vigtige referencer

1. Song I-H et al. Treatment of active ankylosing spondylitis with abatacept: an open-label, 24-week pilot study. *Ann Rheum Dis*. 2011;70(6):1108-1110. PMID: 21415053
2. Singh JA et al. 2018 ACR/NPF Guideline for the Treatment of Psoriatic Arthritis. *Arthritis Rheumatol*. 2019;71(1):5-32. PMID: 30499246
3. Zuckerman BP et al. Abatacept and the risk of malignancy: a meta-analysis across disease indications. *Rheumatology*. 2025. PMID: 39992258
4. Fujii W et al. The rapid efficacy of abatacept in a patient with rheumatoid vasculitis. *Mod Rheumatol*. 2012;22(3):440-443. PMID: 22124545
5. Carvajal Alegria G et al. New onset of rheumatoid vasculitis during abatacept therapy. *Joint Bone Spine*. 2016;83(5):589-590. PMID: 27052429
6. Al Attar L, Shaver T. Abatacept as a Therapeutic Option for Rheumatoid Vasculitis. *Cureus*. 2018;10(6):e2793. PMID: 29930884
7. Zizzo G et al. Abatacept in the treatment of psoriatic arthritis: biological and clinical profiles of the responders. *Immunotherapy*. 2018;10(6):465-478. PMID: 29737909
8. Sieper J. New treatment targets for axial spondyloarthritis. *Rheumatology*. 2016;55(suppl_2):ii38-ii42. PMID: 27856659

---

> **Disclaimer**: Denne rapport er genereret til **kun forskningsmæssige formål** og udgør ikke medicinske råd. Alle lægemiddelnyi anvendelse-kandidater kræver **klinisk validering** før terapeutisk anvendelse. Lægemiddelnyi anvendelse-forudsigelser er baseret på computational modeller (TxGNN videnskabelig graf) og kræver uafhængig verifikation. Konsultér altid sundhedspersonale og det aktuelle Lægemiddelstyrlsens godkendt produktresumé før træffer behandlingsbeslutninger.
>
> *Rapport genereret: 2026-04-03 | Dataskæring: 2026-04-03 | Pipeline-version: v4*

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

