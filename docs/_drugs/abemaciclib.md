---
layout: default
title: Abemaciclib
parent: Moderat evidens (L3-L4)
nav_order: 12
evidence_level: L4
indication_count: 10
---

# Abemaciclib
{: .fs-9 }

Evidensniveau: **L4** | Forudsagte indikationer: **10** stk.
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

# Medicinalstoffers nyformål - Bevisrapport

## Abemaciclib (DB12001) — Analyse af flere indikationer

**Rapport-ID**: TW-DB12001-multi | **Version**: v4
**Dato**: 2026-04-03 | **Dataudsnit**: 2026-04-03
**Udarbejdet for**: Lægemiddelstyrelsen – Dansk kontekst

---

## 1. Ledelsesoversigt

| Felt | Detail |
|------|--------|
| **Medicinalstof** | Abemaciclib (INN); DrugBank ID: DB12001 |
| **Handelsnavn** | Verzenio™ (Eli Lilly) |
| **Foreslåede indikationer** | 5 unikke kandidater til medicinalstoffers nyformål identificeret af TxGNN-prognosemodel |
| **Højeste bevisniveau** | **L4** (Præklnisk/mekanistisk) — Multipel endokrin neoplasi |
| **Samlet anbefaling** | **Hold / Forskningsspørgsmål** — Ingen kandidater har direkte klinisk forsøgsbeviser for de foreslåede indikationer |

### Opsummering af topforeslåede indikationer

| Rangering | Sygdom | TxGNN-score | Bevisniveau | Anbefaling |
|-----------|--------|-------------|-------------|-----------|
| 1 | Reumatoid artritis | 0.973 | L5 | Hold |
| 2 | Hypertyreoidisme | 0.972 | L5 | Hold |
| 3 | **Multipel endokrin neoplasi** | 0.971 | **L4** | **Forskningsspørgsmål** |
| 4 | Resistens over for thyroidhormon (RTHβ) | 0.969 | L5 | Hold |
| 5 | Homozygot familial hyperkolesterolæmi | 0.966 | L5 | Hold |

**Vigtigste resultater**: Af de fem foreslåede sygdomsmål når kun **multipel endokrin neoplasi (MEN)** L4-bevisniveau baseret på en plausibel mekanistisk begrundelse, der forbinder CDK4/6-vej-dysregulering til endokrin tumorbrist. Ingen kliniske forsøg undersøger dog direkte abemaciclib for nogen af de fem foreslåede indikationer. De øvrige fire kandidater mangler både kliniske beviser og en troværdig mekanistisk forbindelse og klassificeres som L5 (kun AI-prognose). Væsentlige datahuller eksisterer for sikkerhedsmærkning og mekanisme-for-virkningsgranskelse inden for det danske regulatoriske miljø.

---

## 2. Medicinalstoffers oversigt

### 2.1 Godkendte indikationer

#### Internationale godkendelser (EMA/FDA)

Abemaciclib er godkendt som en selektiv hæmmer af cyclin-afhængige kinaser 4 og 6 (CDK4/6) til behandling af:

- **HR+/HER2− avanceret eller metastatisk brystcancer** i kombination med en aromatasehæmmer eller fulvestrant som initial eller påfølgende hormonbaseret terapi
- **HR+/HER2− tidligtstadium-brystcancer** med høj tilbagefaldrisiko, i kombination med hormonterapi (adjuvant indstilling; FDA: monarchE-indikation)

#### Danmark (Lægemiddelstyrelsen) / EMA-status

Abemaciclib (Verzenio) modtog **EMA-markedsføringstilladelse** og er tilgængelig i Danmark til de godkendte brystcancer-indikationer. Det er anført i den danske nationale farmakopé under onkologi-terapeutika. Medicinrådet har udstedt anbefalinger vedrørende dets anvendelse i specifikke brystcancer-subpopulationer.

> **Bemærk**: Bevispakningen stammer fra en taiwansk (TFDA) regulatorisk kontekst, hvor abemaciclib registreres som "Ikke markedsført". I Danmark er lægemidlet **tilgængeligt** gennem EMA centraliseret godkendelse.

### 2.2 Virkningsmekanisme

| Parameter | Detail |
|-----------|--------|
| **Medicinalstofklasse** | Selektiv CDK4/6-hæmmer |
| **Primære mål** | Cyclin-afhængig kinase 4 (CDK4) og cyclin-afhængig kinase 6 (CDK6) |
| **Molekylær mekanisme** | Hæmmer CDK4/6-medieret fosforylering af retinoblastoma-proteinet (Rb) og forhindrer G1→S-cellecyklus-transition og standsning af tumorcellproliferation |
| **Selektivitet** | Blandt CDK4/6-hæmmere viser abemaciclib den højeste CDK4-selektivitet (CDK4 IC₅₀ ~2 nM mod CDK6 IC₅₀ ~10 nM), med yderligere aktivitet mod CDK9 |
| **Distingueringsfunktion** | Evne til at krydse blod-hjerne-barrieren (demonstreret i NCT02308020) |

> ⚠️ **Datahul (DG002)**: Detaljeret MOA-dokumentation fra DrugBank-kilden blev markeret som ufuldstændig i bevispakningen. Ovenstående er suppleret fra EMA's evalueringsrapport (EPAR) og publiceret farmakologi-litteratur.

### 2.3 Farmakokinetisk profil

| Parameter | Værdi |
|-----------|-------|
| **Administrationsvej** | Oral (filmovertrukne tabletter: 50 mg, 100 mg, 150 mg, 200 mg) |
| **Biodisponibilitet** | ~45% (absolut) |
| **T_max** | 8 timer (median) |
| **Proteinbinding** | ~96,3% (albumin) |
| **Metabolisme** | Hepatisk via CYP3A4 (primær); aktive metabolitter M2 (N-desethylabemaciclib), M20, M18 |
| **Halveringstid** | 18,3 timer (abemaciclib); 56,4 timer (M2 aktiv metabolit) |
| **Eliminering** | Fækalt (81%); renalt (3,4%) |
| **CNS-penetration** | Ja — CSF:plasma-forhold demonstreret i kliniske forsøg |
| **Dosering** | 150 mg to gange dagligt (kombination); 200 mg to gange dagligt (monoterapi) — kontinuerlig skema |

---

## 3. Bevisanalyse

### 3.1 Indikation 1: Reumatoid artritis (TxGNN-score: 0.973)

**Bevisniveau: L5 — Kun AI-prognose**

#### Kliniske forsøg
- **Direkte forsøg**: Ingen identificeret (0 resultater på ClinicalTrials.gov; 0 på ICTRP)
- Ingen registrerede kliniske forsøg undersøger abemaciclib til reumatoid artritis eller nogen inflammatorisk arthropati

#### Publiceret litteratur
En indirekte relevant publikation blev identificeret:

| PMID | Citation | Relevans |
|------|----------|----------|
| 40504547 | Jacobs F, et al. *The Oncologist* (2025). "Præ-eksisterende og nye immun-medierede sygdomme hos patienter med brystcancer under CDK4/6-hæmmere og hormonterapi." | **Indirekte** — Denne observationsstudie undersøger autoimmun sygdoms-fremkomst (herunder RA) som en *uønsket bivirkning* hos brystcancer-patienter under CDK4/6-hæmmere, snarere end som en terapeutisk fordel. |

#### Mekanistisk vurdering
**Svag og potentielt modstridende**. Selvom CDK4/6 regulerer T-celle-proliferation (teoretisk kunne hæmning undertrykke autoreaktiv T-celle-ekspansion), indikerer kliniske beviser, at CDK4/6-hæmmere oftere *udløser* immun-relaterede uønskede hændelser (interstitiel pneumonitis, hepatitis, autoimmunfænomener) snarere end at udøve immunsuppressive terapeutiske effekter. Ingen præklnisk data støtter antirheumatoid-effektivitet.

#### Konklusion
❌ **Ikke anbefalet til yderligere forfølgelse.** Den mekanistiske forbindelse er indirekte og modsagt af kliniske sikkerhedssignaler, der foreslår immunaktivering snarere end undertrykkelse.

---

### 3.2 Indikation 2: Hypertyreoidisme (TxGNN-score: 0.972)

**Bevisniveau: L5 — Kun AI-prognose**

#### Kliniske forsøg
- **Direkte forsøg**: Ingen identificeret (0 resultater på tværs af alle registre)

#### Publiceret litteratur
- Ingen relevante publikationer identificeret (0 PubMed-resultater)

#### Mekanistisk vurdering
**Ingen troværdig forbindelse.** Hypertyreoidisme er primært drevet af TSH-receptor-autoantistoffer (Graves' sygdom) eller autonom thyroidea-nodule-sekretion. CDK4/6-Rb-vejen styrer cellecyklus-progression og har ingen direkte forbindelse til thyreoidea-hormon-syntese, sekretion eller autoantistof-produktion. Selvom CDK4/6-hæmning teoretisk kunne reducere thyreocyt-proliferation, adresserer det ikke thyreoidea-hormon-overprodukering.

#### Konklusion
❌ **Ikke anbefalet til yderligere forfølgelse.** Ingen mekanistisk, præklnisk eller klinisk grundlag eksisterer.

---

### 3.3 Indikation 3: Multipel endokrin neoplasi (TxGNN-score: 0.971)

**Bevisniveau: L4 — Præklnisk/mekanistisk beviser**

> ⭐ **Højest rangeret kandidat efter bevisstyrke**

#### Kliniske forsøg

22 kliniske forsøg blev hentet fra ClinicalTrials.gov. Ved ekspertgennemsyn undersøger **ingen dog direkte abemaciclib til MEN-syndrom**. Alle hentede forsøg relaterer til abemaciclib-brug til brystcancer eller andre solide tumorer. Vigtigste gennemgåede forsøg:

| NCT ID | Fase | Status | N | Sygdom | Relevans til MEN |
|--------|------|--------|---|--------|-------------------|
| NCT02107703 (MONARCH 2) | Fase 3 | Aktiv | 669 | HR+/HER2− avanceret eller metastatisk brystcancer | **C** — Sikkerhed/effektivitets-profil referencering kun |
| NCT02308020 | Fase 2 | Gennemført | 162 | Hjernemetastaser (bryst, NSCLC, melanom) | **C** — Demonstrerer CNS-penetration; potentielt relevant til MEN1-associeret pituitær-tumorer |
| NCT02981342 | Fase 2 | Gennemført | 106 | Metastatisk pankreascancer | **C** — Pankreastumorer deler træk med MEN1-associerede pNETs |
| NCT03675893 (RESOLVE) | Fase 2 | Rekrutterer | 180 | Endometrial/ovarial cancer | **C** — Hormonafhængig tumor-kontekst |
| NCT04931342 | Fase 2 | Aktiv | 176 | Sjældne epithelial ovarialtumorer | **C** — Biomarkør-drevet platform; proof-of-concept til sjældne tumortyper |

#### Publiceret litteratur
- Ingen MEN-specifikke publikationer identificeret (0 PubMed-resultater)

#### Mekanistisk vurdering
**Moderat plausibel.** Flere molekylære forbindelser støtter undersøgelse:

1. **MEN1/Menin–Cyclin D-akse**: Tab af menin-protein (MEN1-genmutationer) fører til opregulering af Cyclin D1, en direkte aktivator af CDK4/6. CDK4/6-hæmning kunne derfor adressere nedstrøms-følger af menin-tab.
2. **Pankreatisk NET'er (pNET'er)**: MEN1-associerede pNET'er viser afhængighed af cellecyklus-progression-veje. Tidlige-fase-studier af CDK4/6-hæmmere i pNET'er eksisterer i det bredere litteratur.
3. **CDK4-amplifikation**: Nogle endokrine tumorer (især veldifferentierede NET'er) bærer CDK4-gensamplifikation eller Rb-vej-alterationer.
4. **CNS-penetration**: Abemaciclibs evne til at krydse blod-hjerne-barrieren er relevant for MEN1-associerede pituitær-adenomer.

**Begrænsninger**: MEN er et hereditært syndrom med multi-organ tumor-manifestationer; enkelt-mål-terapi vil sandsynligvis ikke give omfattende sygdomskontrol. Ingen direkte kliniske forsøgsdata eksisterer.

#### Konklusion
🔬 **Forskningsspørgsmål** — Berettiget til yderligere præklnisk undersøgelse, især i MEN1-associerede pNET-celllinjer og menin-deficiente tumor-modeller. En basket-forsøg eller casuserie i MEN1-patienter med progressive tumorer kunne overvejes.

---

### 3.4 Indikation 4: Resistens over for thyroidhormon (RTHβ) (TxGNN-score: 0.969)

**Bevisniveau: L5 — Kun AI-prognose**

#### Kliniske forsøg
- **Direkte forsøg**: Ingen identificeret (0 resultater på tværs af alle registre)

#### Publiceret litteratur
- Ingen relevante publikationer identificeret (0 PubMed-resultater)

#### Mekanistisk vurdering
**Ingen troværdig forbindelse.** RTHβ skyldes mutationer i THRB-genet, der koder for thyroidea-hormon-receptor beta, hvilket forårsager forringet receptor-signalering. Dette er en nukleær-receptor/transskriptions-faktor-defekt uden skæring med CDK4/6-medieret cellecyklus-kontrol. CDK4/6-hæmning kan ikke korrigere en mutant hormonreceptor.

#### Konklusion
❌ **Ikke anbefalet til yderligere forfølgelse.** Grundlæggende vej-mismatch.

---

### 3.5 Indikation 5: Homozygot familial hyperkolesterolæmi (TxGNN-score: 0.966)

**Bevisniveau: L5 — Kun AI-prognose**

#### Kliniske forsøg
- **Direkte forsøg**: Ingen identificeret (0 resultater på tværs af alle registre)

#### Publiceret litteratur
- Ingen relevante publikationer identificeret (0 PubMed-resultater)

#### Mekanistisk vurdering
**Ingen troværdig forbindelse.** HoFH skyldes homozygote mutationer i LDLR-, APOB- eller PCSK9-gener, hvilket fører til alvorlig forringet LDL-clearance. Kolesterol-metabolisme og LDL-receptor-biologi opererer gennem veje helt adskilt fra CDK4/6 cellecyklus-regulering. Selvom tangential forskning eksisterer, der forbinder celloproliferation med lipid-metabolisme, udgør dette ikke en levedygtig terapeutisk hypotese for CDK4/6-hæmning i hyperkolesterolæmi.

#### Konklusion
❌ **Ikke anbefalet til yderligere forfølgelse.** Ingen biologisk plausibilitet.

---

## 4. Sikkerhedshensyn

> ⚠️ **Datahul (DG001)**: Lokal regulatorisk mærkning (TFDA 仿單) var ikke tilgængelig. Følgende sikkerhedsinformationer er afledt fra EMA's sammenfatning af produktkarakteristika (SmPC) til Verzenio og publicerede kliniske forsøgsdata.

### 4.1 Kendte uønskede virknigner

| Kategori | Almindelig (≥10%) | Alvorlige / Bemærkelsesværdige |
|----------|-------------------|--------------------------------|
| **Gastrointestinal** | Diarré (81–86%), kvalme (45%), opkastning (26%), mavesmerter (20%) | Grad 3-4 diarré (13%); kræver dosistilpasning |
| **Hæmatologisk** | Neutropeni (41–46%), anæmi (29%), trombocytopeni (16%), leukopeni (21%) | Grad 3-4 neutropeni (24%); febril neutropeni sjælden (~1%) |
| **Hepatisk** | ALT-stigning (13%), AST-stigning (11%) | Grad 3-4 hepatotoxicitet (~4%); hepatisk svigt (sjælden) |
| **Infektioner** | Infektioner (31%) | Sepsis, lungebetændelse |
| **Tromboembolisk** | Venøs tromboembolisme (2–5%) | Lungeembolisme, dybde venøs trombose |
| **Pulmonær** | — | Interstitiel lungesygdom/pneumonitis (~3%; nogle dødelige) |
| **Nyre** | Serum-kreatinin-stigning (98%) | Hæmning af tubulær-sekretion-transportører (OCT2, MATE); reflekterer ikke GFR-ændring |
| **Generel** | Træthed (40%), nedsat appetit (24%) | — |

### 4.2 Medicinalstof-interaktioner

| Interaktionstype | Agent | Effekt | Klinisk betydning |
|------------------|-------|--------|-------------------|
| **CYP3A4-hæmmere** (stærk) | Ketokonazol, klarithromycin, itrakonazol | ↑ Abemaciclib-eksponering (AUC +16-fold med ketokonazol) | **Kontraindikeret eller dosisstigning påkrævet** |
| **CYP3A4-inducere** (stærk) | Rifampicin, phenytoin, carbamazepin | ↓ Abemaciclib-eksponering (AUC −90% med rifampicin) | **Undgå samlinjing** |
| **CYP3A4-substrater** (følsomme) | Midazolam, simvastatin | ↑ Substrat-eksponering | Overvåg; overvej dosisjustering |
| **Transportør-substrater** | Metformin (OCT2/MATE) | ↑ Metformin-eksponering | Overvåg nyrfunktion |

> ⚠️ **DDI-forespørgselsstatus**: Bevispakningen DDI-søgning returnerede 0 resultater, hvilket indikerer et datahul. Ovenstående er suppleret fra EMA SmPC.

### 4.3 Kontraindikationer

- Overfølsomhed over for abemaciclib eller nogen hjælpestof
- Co-administration med stærke CYP3A4-hæmmere bør undgås eller håndteres med dosisstigning
- Alvorlig hepatisk svigt (Child-Pugh C) — ikke anbefalet på grund af øget eksponering

### 4.4 Særlige hensyn til medicinalstoffers nyformål

For de foreslåede non-onkologi-indikationer er følgende sikkerhedsbetingelser især relevante:

| Betingelse | Indflydelse på nyformål |
|-----------|------------------------|
| **Myeloundertrykkelse** | Uacceptabel risiko-fordel til ikke-maligne tilstande (RA, hypertyreoidisme, HoFH) |
| **Diarré-alvorlighed** | Livskvalitets-påvirkning sandsynligvis uacceptabel til kronisk non-onkologi-brug |
| **Immunmodulering** | Paradoksalt kan *forværre* autoimmune tilstande |
| **Teratogenicitet** | Embryo-føtal-toksicitet demonstreret i dyreforsøg; kontraindikeret i graviditet |
| **Omkostninger** | Cirka DKK 25.000–30.000/måned; ikke begrundet for uprøvede indikationer |

---

## 5. Regulatorisk status

### 5.1 Danmark (Lægemiddelstyrelsen)

| Parameter | Status |
|-----------|--------|
| **Markedsføringstilladelse** | ✅ Godkendt via EMA centraliseret procedure |
| **Handelsnavn** | Verzenio (Eli Lilly) |
| **Godkendt indikation** | HR+/HER2− brystcancer (avanceret/metastatisk og adjuvant) |
| **Refusion** | Underlagt Medicinrådets anbefaling; tilgængelig gennem hospital-baseret onkologi |
| **Nyformål-status** | Ingen ansøgninger eller compassionate use-programmer til nogen foreslået indikation |

### 5.2 Det Europæiske Lægemiddelagentur (EMA)

| Parameter | Status |
|-----------|--------|
| **Initial godkendelse** | 27. september 2018 (EU/1/18/1307) |
| **Indikations-udvidelser** | Adjuvant brystcancer (2022) |
| **Orphan-betegnelse** | Ingen til nogen foreslået indikation |
| **PRIME-betegnelse** | Ikke relevant til foreslåede indikationer |
| **Pediatrisk undersøgelsesplan** | Gennemført til godkendt indikation |

### 5.3 US FDA

| Parameter | Status |
|-----------|--------|
| **Godkendelsesdato** | 28. september 2017 (accelereret); 12. oktober 2021 (adjuvant) |
| **Godkendte indikationer** | HR+/HER2− avanceret/metastatisk brystcancer; højrisiko tidligtstadium brystcancer (adjuvant) |
| **Breakthrough Therapy** | Ikke til foreslåede indikationer |

### 5.4 Taiwan (TFDA) — Kildedata

| Parameter | Status |
|-----------|--------|
| **Markeds-status** | Ikke markedsført |
| **Samlede licenser** | 0 |

---

## 6. Konklusion og anbefalinger

### 6.1 Samlet vurdering

| Indikation | Beviser | Mekanistisk forbindelse | Sikkerhedsmulighed | Samlet |
|-----------|---------|------------------------|--------------------|--------|
| **Multipel endokrin neoplasi** | L4 | Moderat | Acceptabel (onkologi-kontekst) | 🔬 Forskningsspørgsmål |
| Reumatoid artritis | L5 | Svag/modstridende | Dårlig (giftighedsprofil) | ❌ Hold |
| Hypertyreoidisme | L5 | Ingen | Dårlig | ❌ Hold |
| RTHβ | L5 | Ingen | Dårlig | ❌ Hold |
| HoFH | L5 | Ingen | Dårlig | ❌ Hold |

**Kun en kandidat — Multipel endokrin neoplasi — demonstrerer tilstrækkelig videnskabelig begrundelse til yderligere undersøgelse.** De øvrige fire indikationer mangler både biologisk plausibilitet og kliniske beviser, og abemaciclibs giftighedsprofil (myeloundertrykkelse, alvorlig diarré, hepatotoxicitet) gør det uegnet til ikke-onkologiske, kroniske-sygdoms-applikationer.

### 6.2 Bevishuller

| Hul-ID | Beskrivelse | Alvorlighed | Anbefalet handling |
|--------|-----------|------------|------------------|
| DG001 | Lokal regulatorisk mærkning (sikkerhedsadvarsler/kontraindikationer) | Blokerer | Indhent EMA SmPC og dansk national mærkning |
| DG002 | Mekanisme-for-virknings-dokumentation i bevispakning | Høj | Forespørg DrugBank API; supplér fra EMA EPAR |
| — | Ingen direkte kliniske forsøg til nogen foreslået indikation | Høj | Litteratur-overvågning; overvåg ClinicalTrials.gov |
| — | Ingen MEN-specifik præklnisk data i pakning | Mellem | Systematisk PubMed-søgning for "CDK4/6 hæmmer" AND "MEN1" eller "neuroendokrin tumor" |
| — | Duplikat-indlæg i prognoseoutput (rækker 1/2, 3/4, 5/6, 7/8, 9/10) | Lav | Deduplikér TxGNN output-pipeline |

### 6.3 Foreslåede næste trin

#### For Multipel endokrin neoplasi (prioritet-kandidat)

1. **Målrettet litteraturgennemgang**: Gennemfør systematisk søgning for CDK4/6-hæmmere (abemaciclib, palbociclib, ribociclib) i neuroendokrine tumorer, MEN1-associerede pNET'er og pituitær-adenomer
2. **Præklnisk validering**: Vurder abemaciclib-effektivitet i menin-deficiente cellinje-modeller (f.eks. BON-1, QGP-1 pankreatisk NET-linjer)
3. **Klinisk signal-minedrift**: Forespørg EMA EudraVigilance og FAERS-databaser for MEN-patienter, som modtog CDK4/6-hæmmere til samtidig brystcancer — vurder eventuel incidental tumor-reaktion
4. **Samarbejde**: Engagér danske ENETS (European Neuroendocrine Tumor Society) centre til potentiel casusserie eller basket-forsøg design
5. **Regulatorisk vej**: Overvej EMA orphan medicinal product-betegnelse til MEN1-associerede progressive NET'er hvis præklnisk data er supportivt

#### For alle øvrige kandidater

6. **Ingen yderligere handling anbefalet** på nuværende tidspunkt til reumatoid artritis, hypertyreoidisme, RTHβ eller HoFH
7. **Pipeline-forbedring**: Løs duplikat-indlæg i TxGNN-output; rekalibrér prognose-model til at indarbejde mekanisme-for-virkning-vej-kompatibilitet som filter-kriterium

#### Datahul-afhjælpning

8. Løs **DG001** (Blokerer): Indhent komplet EMA SmPC til dansk regulatorisk kontekst
9. Løs **DG002** (Høj): Gennemfør DrugBank API-forespørgsel til omfattende MOA-data

---

## Bilag A: Datakilde-kildesporinger

| Kilde | Forespørgsler | Resultater fundet |
|-------|---------------|------------------|
| ClinicalTrials.gov | 10 sygdoms-specifikke forespørgsler | 22 (MEN-relateret nøgleord-match; ingen direkte relevant) |
| WHO ICTRP | 10 sygdoms-specifikke forespørgsler | 0 |
| PubMed | 10 sygdoms-specifikke forespørgsler | 1 (indirekte; RA-relateret) |
| DrugBank | 1 medicinalstof-forespørgsel | 1 |
| DDI-database | 1 medicinalstof-forespørgsel | 0 (datahul) |

## Bilag B: TxGNN-model-bemærkning

TxGNN-viden-graf-prognose-modellen genererede høje konfidensscorer (0.966–0.973) til alle fem kandidat-indikationer. Disse scorer reflekterer dog topologisk nærhed inden for den biomedikale viden-graf og **indarbejder ikke mekanisme-for-virkning-kompatibilitet, sikkerhedsmulighed eller klinisk translatabilitet-vurderinger**. Den høje falsk-positiv-rate observeret (4 af 5 kandidater mangler biologisk plausibilitet) foreslår, at post-prognose mekanistisk filtrering er væsentlig til denne medicinalstof-klasse.

---

> **Fraskrivelse**: Denne rapport er genereret til forskningsformål alene og udgør ikke lægeligt råd. Alle medicinalstoffers nyformål-kandidater kræver stringent klinisk validering før nogen terapeutisk applikation. Denne analyse er ikke blevet gennemgået eller godkendt af Lægemiddelstyrelsen, EMA eller nogen regulatorisk myndighed. Sundhedspersonale bør konsulteres før enhver behandlingsbeslutning.
>
> *Rapport genereret: 2026-04-03 | Bevispakning version: v4 | Kandidat ID: TW-DB12001-multi*

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

