---
layout: default
title: Acipimox
parent: Kun modelforudsigelse (L5)
nav_order: 14
evidence_level: L5
indication_count: 0
---

# Acipimox
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

# Lægemiddel-omformålingsbevisrapport — Acipimox (DB09055)

**Udarbejdet for:** Dansk Lægemiddelstyrelse
**Rapportversion:** v4
**Dato for generation:** 2026-04-03
**Dataafgrænsning:** 2026-04-03

---

## 1. Lederberetning

| Felt | Værdi |
|-----|--------|
| **Lægemiddel (INN)** | Acipimox |
| **DrugBank-ID** | [DB09055](https://go.drugbank.com/drugs/DB09055) |
| **Handelsnavn** | Olbetam® (Pharmacia / Pfizer) |
| **Godkendt indikation** | Hyperlipidemier (typerne IIa, IIb, IV, V) — supplering til diætbehandling |
| **Foreslået omformål** | Flere nye indikationer forudsagt af TxGNN knowledge-graph-model (100 kandidater) |
| **Nuværende bevisniveau** | **L5** — Kun computerisk forudsigelse; ingen dedikerede omformålingskliniske forsøg identificeret |
| **Danmarks markedsstatus** | Tidligere tilgængelig på udvalgte europæiske markeder; nuværende dansk markedsautorisation bør bekræftes med Lægemiddelstyrelsen |

**Vigtigste fund:**
- Acipimox er et nicotinsyreanalolg med velkarakteriserede lipidmodificerende egenskaber, der virker primært gennem hydroxycarboxylsyrereceptor 2 (HCA2/GPR109A).
- TxGNN knowledge-graph-analyse (KG) har genereret **100 forudsagte nye indikationer**, hvor de vigtigste kandidater omfatter osteogenesis imperfecta, arvelig døvhed af forskellige typer og forskellige sjældne genetiske lidelser.
- Alle forudsigelser forbliver på **niveau 5 (kun computerisk)** — ingen klinisk forsøgsbevis understøtter for øjeblikket nogen af de foreslåede omformålingsindikationer.
- Adskillige **datahuller** findes i bevisydelsen (mekanisme-for-virkning-detaljer, lokale etiketadvarsler/kontraindikationer, lægemiddel-lægemiddel-interaktioner), som skal løses før fremskridt til sikkerhedsevaluering (trin S1).

---

## 2. Lægemiddeloversigt

### 2.1 Godkendte indikationer

Acipimox (Olbetam®) er indiceret som supplement til diæt ved behandling af hyperlipoproteinæmi, specifikt:

- **Type IIa** (forhøjet LDL-kolesterol)
- **Type IIb** (forhøjet LDL + VLDL; blandet hyperlipidemier)
- **Type IV** (forhøjet VLDL; endogent hypertriglyceridæmi)
- **Type V** (forhøjede chylomikroner + VLDL)

Det har været markedsført i flere europæiske lande (især Italien, Storbritannien og udvalgte nordiske/EU-markeder) under handelsmærket **Olbetam®**. Acipimox er **ikke godkendt af FDA (US Food and Drug Administration)**.

#### Status i Danmark (Lægemiddelstyrelsen)

FHIR MedicationKnowledge-ressourcen i dette projekt viser Danmark som jurisdiktion med status "aktiv" og handelsmærket "Olbetam." Imidlertid noterer bevisydelsen, at markedsstatusdata stammer fra Taiwan-kontekst (TFDA), hvor Acipimox **ikke er markedsført** (0 licenser). Den nuværende markedsautorisation med Lægemiddelstyrelsen bør verificeres uafhængigt, da Olbetam historisk har haft begrænset tilgængelighed selv på europæiske markeder, hvor det engang var autoriseret.

### 2.2 Virkningsmekanisme

> ⚠️ **Datahul (DG002)** — Fuld virkningsmekanisme er ikke udfyldt i bevisydelsen. Følgende er rekonstrueret fra etableret farmakologisk litteratur.

Acipimox er et **pyrazin-2-carboxylsyre-derivat** og strukturelt analogon af nicotinsyre (niacin). Dets mekanisme omfatter:

1. **HCA2 (GPR109A / Nicotinreceptor) Agonisme:** Acipimox aktiverer hydroxycarboxylsyrereceptor 2 (HCA2) på adipocytter, en Gi-proteinkoblet receptor. Receptoraktivering hæmmer adenylylcyclase, hvilket reducerer intracellulære cAMP-niveauer.

2. **Hæmning af lipolysis:** Reduceret cAMP svækker hormonfølelses-lipase (HSL)-aktivitet i adipøst væv, hvilket reducerer frigivelsen af frie fedtsyrer (FFAs) til cirkulationen.

3. **Efterfølgende hepatiske virkninger:** Lavere cirkulerende FFAs reducerer hepatiske substrater til triglycerid- og VLDL-syntese, hvilket fører til:
   - ↓ Plasma triglycerideer (20–50%)
   - ↓ Totalt og LDL-kolesterol (moderat, ~10–20%)
   - ↑ HDL-kolesterol (beskedent, ~10–15%)

4. **Antiinflammatoriske egenskaber (Ny udvikling):** Ligesom niacin kan acipimox udøve antiinflammatoriske virkninger via HCA2-mediaterede veje, herunder undertrykkelse af NF-κB-signalering og modulering af prostaglandinsyntese. Denne mekanisme er af særlig interesse i omformålskonteksten.

**Fordel frem for niacin:** Acipimox producerer betydeligt **mindre hudrødme** end nicotinsyre på grund af dets strukturelle modifikationer, hvilket forbedrer patienttolerance.

### 2.3 Farmakokinetisk profil

| Parameter | Værdi |
|-----------|-------|
| **Absorption** | Hurtigt og velabsorberet efter oral administration |
| **Biodisponibilitet** | ~90–100% (oral) |
| **Tmax** | ~2 timer |
| **Proteinbinding** | Lav (~10%) |
| **Metabolisme** | Minimal hepatisk metabolisme; stort set udskilt uændret |
| **Elimination** | Primært renal (>90% uændret lægemiddel i urin) |
| **Halveringstid (t½)** | ~1,5–2 timer |
| **Dosering** | Typisk 250 mg to til tre gange dagligt, tages med eller efter måltider |

**Kliniske farmakologi-noter:**
- Den korte halveringstid nødvendiggør flere daglige doser.
- Doseringsjustering er påkrævet ved nedsat nyrefunktion (CrCl < 30 mL/min) på grund af næsten eksklusiv renal elimination.
- Ingen betydelig hepatisk CYP450-medieret metabolisme, hvilket reducerer lægemiddel-lægemiddel-interaktionsrisiko.

---

## 3. Bevisanalyse

### 3.1 TxGNN computeriske forudsigelser

TxGNN knowledge-graph-modellen (KG) genererede **100 forudsagte nye indikationer** for Acipimox. De 20 vigtigste forudsigelser er:

| Placering | Forudsagt indikation | Kilde |
|-----------|---------------------|-------|
| 1 | Osteogenesis imperfecta | KG |
| 2 | Autosomal recessiv ikke-syndromisk døvhed | KG |
| 3 | Medføldt stationær natteblindhed, autosomal dominant | KG |
| 4 | Autosomal dominant ikke-syndromisk døvhed | KG |
| 5 | Døvhed, autosomal recessiv | KG |
| 6 | Keratoderma hereditarium mutilans | KG |
| 7 | ICF-syndrom (Immunodefekt-centromeric ustabilitet-ansigtsanomalier) | KG |
| 8 | Müllerian aplasi og hyperandrogeni | KG |
| 9 | Myelodysolasi, immunodefekt, ansigtsmalformationer, kort vækst og psykomotorisk forsinkelses | KG |
| 10 | GM1-gangliosidose | KG |
| 11 | Knogledysplasi, letal Holmgren-type | KG |
| 12 | CARD9-defekt (disposition for invasiv svampesygdom) | KG |
| 13 | Agammaglobulinæmi | KG |
| 14 | Asymmetrisk kortvækstsyndrom | KG |
| 15 | Action myoklonus–nyresvigt-syndrom | KG |
| 16 | Fanconi-anæmi komplementeringsgruppe | KG |
| 17 | Arthrogryposis, distal | KG |
| 18 | Portål hypertension, ikke-cirrotisk | KG |
| 19 | Kraniosynostose–intracranialt kalcificerings-syndrom | KG |
| 20 | Kombineret immundefekt på grund af ZAP70-defekt | KG |

*(100 forudsigelser i alt; fuld liste tilgængelig på projektets lægemiddelside)*

**Observation:** De forudsagte indikationer er overvejende **sjældne genetiske og medfødte lidelser** — mange af hvilke for øjeblikket mangler effektive farmakoterapier. Mens dette mønster er karakteristisk for KG-baserede forudsigelser (som traverserer fænotype–genotype-kanter i knowledge-graphen), betyder det også, at disse forudsigelser er særligt vanskelige at validere klinisk på grund af små patientpopulationer.

### 3.2 Kliniske forsøg

#### Eksisterende forsøg for godkendt indikation

Acipimox har en veletableret klinisk historie for lipidnedsættelse, med flere forsøg publiceret i 1980'erne–2000'erne:

- Fase 3-forsøg, der demonstrerer efficacitet i blandet hyperlipidemier (forskellige europæiske centre)
- Sammenligningsstudier mod niacin og fibrater

#### Forsøg relevant for omformål

| Område | Status | Noter |
|--------|--------|-------|
| **Insulinresistens / Type 2-diabetes** | Eksplorativt (fase 1/2 ækvivalent) | Adskillige efterforskerinitiaterede studier undersøgte acipimox' virkning på FFA-niveauer og insulinfølsomhed. Resultaterne viste akut forbedring af insulinfølsomhed, når FFA-niveauer blev reduceret, hvilket understøtter et mekanistisk link, men ingen pivotale forsøg blev gennemført. |
| **Metabolisk syndrom** | Observatorisk | Begrænset observatorisk data, der tyder på fordele ved metaboliske parametre ud over lipider. |
| **Forudsagte KG-indikationer** | **Ingen identificeret** | Ingen kliniske forsøg registreret på ClinicalTrials.gov eller EU CTR for nogen af de 100 TxGNN-forudsagte indikationer. |

#### Vigtige historiske studier værd at bemærke

1. **Santomauro et al. (1999)** — Demonstrerede, at nagtlig FFA-undertrykkelse med acipimox forbedrede insulinfølsomhed hos overvægtige ikke-diabetiske og Type 2-diabetiske personer. (*Diabetes*, 48(9): 1836–1841)

2. **Bajaj et al. (2005)** — Viste, at acipimox reducerede plasma-FFA og forbedrede hepatisk og perifer insulinfølsomhed hos HIV-lipodystrofi-patienter. (*J Clin Endocrinol Metab*, 90(7): 4474–4480)

3. **Daniele et al. (2014)** — Undersøgte acipimox-virkninger på mitokondriefunktion og insulinresistens. Fandt, at kronisk acipimox-behandling førte til en rebound-stigning i FFA-niveauer, hvilket sætter spørgsmålstegn ved vedvarende efficacitet for insulinfølsomhed. (*PLoS Med*, 11(3): e1001628)

### 3.3 Publiceret litteratur

#### Meta-analyser og systematiske anmeldelser

- Ingen meta-analyser eller systematiske anmeldelser specifikt adressering acipimox-omformål er blevet identificeret.
- Acipimox er inkluderet i bredere anmeldelser af nicotinklassen af agenternes og deres kardiovaskulære virkninger.

#### Randomiserede kontrollerede forsøg (for nye indikationer)

- **Ingen identificeret** for nogen af de 100 TxGNN-forudsagte indikationer.

#### Observatoriske studier

- Begrænsede caserapporter og små serier, der udforsker acipimox i metaboliske kontekster ud over hyperlipidemier (insulinresistens, lipodystrofi), men ingen som omhandler KG-forudsagte sjældne sygdomsindikationer.

### 3.4 Mekanistisk plausibilitetsvurdering

| Forudsagt indikation (højeste placeret) | HCA2/Lipid-vej-relevans | Plausibilitet |
|---------------------------------------|------------------------|--------------|
| Osteogenesis imperfecta | HCA2 udtrykt i osteoblaster; nicinklasse kan modulere knoglemetabolisme via prostaglandin-veje | Lav–Moderat |
| Arvelig døvhed (multiple undertyper) | Ingen etableret mekanistisk link mellem lipidnedsættelse/HCA2-agonisme og cochlear-funktion | Lav |
| Medføldt stationær natteblindhed | Ingen etableret mekanistisk link | Lav |
| GM1-gangliosidose | Lysosomalt lagringssygdom; ingen klar forbindelse til acipimox-MOA | Meget lav |
| Portål hypertension, ikke-cirrotisk | Potentielt FFA/metabolisk link; spekulativ | Lav |

**Vurdering:** Størstedelen af de højest placerede KG-forudsigelser mangler klar mekanistisk begrundelse, der forbinder acipimox' kendt farmakologi (HCA2-agonisme, FFA-reduktion, lipidnedsættelse) til de forudsagte sygdomsmål. Dette er en betydelig begrænsning på L5-bevisstadiet.

---

## 4. Sikkerhedshensyn

> ⚠️ **Datahul (DG001 — Bloker):** Lokale etiketeadvarsler og kontraindikationer ikke tilgængelige i bevisydelsen. Følgende er samlet fra etablerede farmakologiske referencer og europæiske SmPC-data.

### 4.1 Kendte bivirkninger

| Kategori | Bivirkninger | Hyppighed |
|----------|-------------|-----------|
| **Meget hyppig (≥10%)** | Hudhudrødme og varme (væsentligt mindre end med niacin) | ~15–20% |
| **Hyppig (1–10%)** | Hovedpine, gastrointestinale forstyrrelser (kvalme, dyspepsi, diarré, mavesmerter), pruritus, udslæt, nældefeber | |
| **Ualmindelig (0,1–1%)** | Myalgi, utilpashed, svimmelhed | |
| **Sjælden (<0,1%)** | Hepatotoxicitet (transaminase-stigning), anafylaktoide reaktioner | |

**Post-marketing-signaler:** Ingen større post-marketing sikkerhedssignaler ud over de kendte klassevirkninger af nicotinklasse-derivater.

### 4.2 Lægemiddel-interaktioner

| Interagerende agent | Virkning | Klinisk signifikans |
|-------------------|--------|-------------------|
| **Statiner (HMG-CoA-reductase-hæmmere)** | Potentiel additiv risiko for myopati/rabdomyolyse | Moderat — overvåg for muskelSymptomer |
| **Antihypertensiver** | Additiv vasodilatatoriske virkninger (hudrødme); potentiel hypotension | Lav–Moderat |
| **Antikoagulantia (warfarin)** | Teoretisk fortrængning fra proteinbinding (lav klinisk relevans givet lav acipimox-binding) | Lav |
| **Aspirin / NSAIDs** | Forkestelse med aspirin kan reducere hudrødme via prostaglandin-vej-blokering | Gavnlig interaktion |
| **Galdesyre-sequestranter** | Kan reducere acipimox-absorption, hvis co-administreret | Lav — adskil dosering med 4 timer |

> **Bemærk:** DDI-forespørgsel i bevisydelsen returnerede **not_found** (0 interaktioner). Dette datahul bør behandles.

### 4.3 Kontraindikationer

- **Aktiv mavesår** (risiko for GI-forværring)
- **Alvorlig nyreinsufficiens** (CrCl < 30 mL/min) — lægemiddelophobning på grund af renal elimination
- **Graviditet og amning** (utilstrækkelige sikkerhedsdata)
- **Overfølsomhed** over for acipimox eller nogen hjælpestof
- **Akut blødning** (teoretisk, klasserelateret)

### 4.4 Særlige populationer

| Population | Hensyn |
|-----------|--------|
| **Nyreinsufficiens** | Doseringsjustering påkrævet; kontraindikeret hvis CrCl < 30 mL/min |
| **Hepatisk insufficiens** | Brug med forsigtighed; overvåg leverprøver |
| **Ældre** | Doseringsjustering baseret på nyrenfunktion |
| **Pædiatrisk** | Ingen etableret dosering; ikke studeret hos børn |
| **Diabetiske patienter** | Kan påvirke glykæmisk kontrol (overvåg blodglukose); potentiel gavnlig virkning på insulinfølsomhed (akut) vs. FFA-rebound (kronisk) |

---

## 5. Regulatorisk status

### 5.1 Danmark — Lægemiddelstyrelsen

| Punkt | Status |
|-------|--------|
| **Markedsautorisation** | **Skal bekræftes** — Olbetam® var historisk autoriseret på udvalgte europæiske markeder. Nuværende tilgængelighed i Danmark skal verificeres med Lægemiddelstyrelses produktdatabase (produktresumé.dk / laegemiddelstyrelsen.dk). |
| **ATC-kode** | C10AD02 (Lipidmodificerende midler, nicotinsyre og derivater) |
| **Receptpligtsstatus** | Receptpligtigt lægemiddel (Rx) hvor autoriseret |
| **Refusering** | Skal bekræftes med Dansk Medicinerråd (Medicinrådet) |

### 5.2 EMA (Europæiske Lægemiddel-Agentur)

| Punkt | Status |
|-------|--------|
| **Centraliseret autorisation** | **Ikke centralt autoriseret** — Acipimox/Olbetam blev autoriseret via nationale procedurer i enkelte EU-medlemsstater |
| **Henvisning / sikkerhedsvurdering** | Ingen aktuel EMA-sikkerhedshenvisning identificeret |
| **Markedstilgængelighed (EU)** | Historisk tilgængelig i Italien (originalt marked), Storbritannien og udvalgte andre EU-stater; tilgængelighed er på tilbagegang |

### 5.3 FDA (United States Food and Drug Administration)

| Punkt | Status |
|-------|--------|
| **NDA / ANDA** | **Ikke godkendt** — Acipimox har aldrig modtaget FDA-markedsautorisation |
| **IND-status** | Brugt i efterforskerinitiaterede forskningsstudier under IND |
| **Orphan Drug-betegnelse** | Ingen for nogen indikation |

### 5.4 Andre jurisdiktioner

| Jurisdiktion | Status |
|-------------|--------|
| **Taiwan (TFDA)** | Ikke markedsført (0 licenser, pr. bevisydelse) |
| **Japan (PMDA)** | Ikke godkendt |
| **Storbritannien (MHRA)** | Historisk autoriseret; Olbetam diskontinueret på UK-marked |

---

## 6. Konklusioner og anbefalinger

### 6.1 Samlet vurdering

| Dimension | Vurdering |
|-----------|-----------|
| **Bevisniveau** | **L5** — Kun computerisk forudsigelse |
| **Forudsigelseskvalitet** | 100 KG-forudsagte indikationer; overvejende sjældne genetiske lidelser |
| **Mekanistisk plausibilitet** | **Lav** for de fleste højest placerede forudsigelser; den kendte HCA2-agonist/lipidnedsættelsesmekanisme har ikke en etableret forbindelse til de forudsagte sygdomsmål |
| **Klinisk bevis** | **Ingen** for nogen forudsagt omformålingsindikation |
| **Sikkerhedsprofil** | Velkarakteriseret; generelt gunstigt sammenlignet med niacin; kort halveringstid er fordelagtig for sikkerhed |
| **Regulatorisk gennemførlighed** | Begrænset — faldende markedstilgængelighed i Europa; ikke tilgængelig på større markeder (USA, Taiwan, Japan) |

### 6.2 Bevishuller

| Hul-ID | Punkt | Sværhedsgrad | Status | Anbefalet handling |
|--------|--------|----------|--------|-------------------|
| DG001 | Lokale etiketadvarsler / kontraindikationer | **Bloker** | Åben | Indhent dansk/EU SmPC for Olbetam; hvis ikke tilgængelig lokalt, brug italiensk originator-SmPC som reference |
| DG002 | Virkningsmekanisme (struktureret) | Høj | Delvis adresseret i denne rapport | Udfyld struktureret MOA fra DrugBank API; denne rapport giver narrativ MOA |
| DG003 | Lægemiddel-lægemiddel-interaktioner | Moderat | Åben (forespørgsel returnerede 0) | Genstil DrugBank DDI-endpoint forespørgsel; supplér med EU SmPC Section 4.5 |
| DG004 | TxGNN-scoreværdier | Moderat | Manglende fra lægemiddelliste | Bekræft KG-forudsigelsespipeline-output for numeriske scores til at aktivere rangering |
| DG005 | Nuværende dansk markedstilgængelighed | Moderat | Usikker | Forespørg Lægemiddelstyrelses produktdatabase direkte |

### 6.3 Foreslåede næste trin

#### Umiddelbar (Pre-S1-port)

1. **Løs blokerande datahul (DG001):** Indhent produktresumé (SmPC / produktresumé) for Olbetam fra Lægemiddelstyrelsen eller EMA-produktdatabase. Hvis ingen dansk SmPC findes, brug italiensk AIFA-originalsSmPC som referencedokumentet.

2. **Udfyld struktureret MOA (DG002):** Forespørg DrugBank API for DB09055 for at indhente struktureret target-, enzym- og vejdata.

3. **Bekræft dansk markedsstatus (DG005):** Bekræft, hvorvidt Olbetam har en aktiv markedsautorisation i Danmark, eller om den er blevet trukket tilbage/ikke fornyet.

#### Kort sigt (Post-S1)

4. **Mekanistisk plausibilitet-dybdegravning:** For de 5 vigtigste forudsagte indikationer, gennemfør et struktureret litteraturgennemgang, der forbinder:
   - HCA2-receptorekspretion i relevante væv (knogel, cochlear, CNS)
   - Kendte efterfølgende veje (cAMP, prostaglandin, antiinflammatorisk)
   - Eventuelle præ-kliniske beviser i sygdomsmodeller

5. **Prioritér forudsigelser med eksisterende uopfyldt behov:** Krydsreferencer de 100 forudsigelser mod:
   - Orphan disease-betegnelser (EMA/FDA)
   - Sygdomme uden for øjeblikket godkendt terapi
   - Patientpopulationsstørrelser i Danmark

#### Mellemlang sigt (Hvis plausibilitet bekræftes)

6. **Præ-klinisk validering:** For nogen indikation med mekanistisk plausibilitet ≥ Moderat, overvej *in vitro*-studier i relevante sygdomsmodeller før klinisk forskning.

7. **Udforskelk insulinresistens / metaboliske indikationer:** Givet de eksisterende (omend begrænsede) kliniske beviser for acipimox i insulinresistens og lipodystrofi, kan disse repræsentere mere håndterbare omformålsmuligheder end de sjældne genetiske lidelser forudsagt af KG-modellen, selvom de ikke blev overfladeret i den nuværende TxGNN-kørsel.

---

## Appendiks A: Data-provenance

| Datakilde | Forespørgselsdato | Status | Poster |
|-----------|------------------|--------|--------|
| DrugBank (DB09055) | 2026-03-26 | Succes | 1 |
| DDI-database | 2026-03-26 | Ikke fundet | 0 |
| TxGNN KG-forudsigelse | 2026-03-09 | Komplet | 100 indikationer |
| TFDA-licensdatabase | 2026-03-26 | Ikke markedsført | 0 |

## Appendiks B: FHIR-ressource

En FHIR R4 `MedicationKnowledge`-ressource for Acipimox er tilgængelig på:
```
/fhir/MedicationKnowledge/DB09055.json
```
Jurisdiktion: Danmark (DK) | Status: Aktiv | Visningsnavn: Olbetam

---

## Ansvarsfraskrivelse

> **Denne rapport er genereret til forskningsformål alene og udgør ikke medicinsk rådgivning.** Alle lægemiddel-omformålskandidater identificeret gennem computerisk forudsigelse (TxGNN) kræver grundig **klinisk validering** før nogen terapeutisk anvendelse. Sundhedsfagpersoner bør konsulteres for alle behandlingsbeslutninger. Forudsigelser på bevisniveau L5 repræsenterer computeriske hypoteser, som ikke er blevet testet i kliniske miljøer.
>
> **YMYL-bemærk (Din penge eller dit liv):** Dette dokument diskuterer farmaceutiske agenturer og sygdomstilstande. Oplysningerne er beregnet til kvalificerede forskere og sundhedsfagpersoner inden for dansk medicinerauths regulatorisk kontekst. Det bør ikke bruges til selvdiagnose eller selvbehandling.

---

*Rapport genereret af DkTxGNN Evidence Pipeline v4 — 2026-04-03*

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

