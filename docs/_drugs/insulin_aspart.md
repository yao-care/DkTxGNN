---
layout: default
title: Insulin Aspart
parent: Kun modelforudsigelse (L5)
nav_order: 234
evidence_level: L5
indication_count: 10
---

# Insulin Aspart
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

# Insulinaspart: Etableret brug i type 1-diabetes mellitus (datakløft markeret, ikke en kandidat til ny medicinsk anvendelse)

## Sammenfatning i én sætning

> Insulinaspart (DrugBank DB01306) er et hurtigt virkende humaninsulin-analog. Fordi originalindikationens felt i denne evidenspakke er tomt, har modellen opstillet **type 1-diabetes mellitus** — insulinasparts egen velkendte kerneindikation — som topindikation med "forudsigelse", understøttet af **>50 kliniske forsøg** og **20 publikationer**. Dette er **ikke et ægte signal for medicinsk genudnyttelse**; det afspejler en datakløft-artefakt og bør læses som en mekanisme-/evidensbekræftelsesøvelse frem for et forslag til ny indikation.

---

## Hurtigoversigt

| Element | Indhold |
|---------|---------|
| Originalindikation | Ikke tilgængelig i denne evidenspakke (datakløft — `original_indications` er tomt, og der findes ingen dansk licenstekst at udtrække fra) |
| Forudsagt ny indikation | Type 1-diabetes mellitus *(se forbehold nedenfor — dette er lægemidlets kendte etablerede indikation, ikke en kandidat til ny brug)* |
| TxGNN-forudsigelsesscore | 99,95% |
| Bevisniveau | L1 (≥2 afsluttede fase 3-randomiserede kontrollerede forsøg identificeret) |
| Danmark-markedsstatus | Ikke markedsført |
| Antal markedsføringstilladelser | 0 |
| Anbefalet beslutning | Fortsæt med forholdsregler *(til bekræftende/markedsindtradeningsformål — se Konklusion)* |

---

## Hvorfor er denne forudsigelse rimelig?

Detaljeret tekst om virkningsmekanisme er ikke tilgængelig i denne evidenspakke (`original_moa: [Datakløft]`). Baseret på de oplysninger, der er tilgængelige, er insulinaspart et hurtigt virkende humaninsulin-analog, hvor prolin ved position B28 er erstattet med asparaginsyre, hvilket accelererer subkutan absorption i forhold til regulært humaninsulin. Som alle insulinprodukter virker det ved at binde insulinreceptoren og aktivere PI3K/Akt- og MAPK-signaleringskaskadern, hvilket fremmer cellulær glucoseoptagelse, hepatisk glykogensyntese og undertrykkelse af hepatisk gluconeogenese.

Type 1-diabetes mellitus forårsages af autoimmun ødelæggelse af pankreatiske β-celler, hvilket resulterer i absolut insulinmangel. Insulinaspart erstatter direkte dette manglende hormon — den mekanistiske forbindelse er direkte og velafklaret, ikke slutningbaseret.

**Vigtigt forbehold:** Bevispackeens egen begrundelse for genudnyttelse markerer eksplicit, at dette *ikke* er en kandidat til genudnyttelse: "此項並非'老藥新用'候選，而是藥物已確立之核心適應症，資料庫因 `original_indications` 欄位缺失而將其列為預測項目" (dette element er ikke en kandidat til medicinsk genudnyttelse, men lægemidlets allerede etablerede kerneindikation; det blev kun anført som en "forudsigelse", fordi feltet `original_indications` er tomt). Den store mængde fase 3-evidens nedenfor bekræfter derfor en allerede kendt brug snarere end validerer en ny. Da insulinaspart **ikke er markedsført i Danmark**, er den praktiske værdi af denne evidens at understøtte en potentiel **markedsføringstilladelse**, ikke en genudnyttelsesvej.

For fuldstændigheds skyld returnerede modellen også flere lavere-rangerede kandidater (autoimmun ooforitis, opsismodysplasi, thiaminresponsiv dysfunktion-syndrom, permanent neonatal diabetes mellitus) med høje råscorer men lidt eller ingen direkte klinisk eller mekanistisk støtte i denne pakke; disse er ikke uddybet yderligere her pr. rapporteringsomfang, men bør ikke forveksles med validerede genudnyttelsesledere.

---

## Klinisk forsøgsevidenes

| Forsøgsnummer | Fase | Status | Tilmelding | Vigtige resultater |
|---------|------|------|------|---------|
| [NCT01486940](https://clinicaltrials.gov/study/NCT01486940) | Fase 3 | Afsluttet | 598 | Multinationalt randomiseret kontrolleret forsøg sammenlignende insulindetemir + insulinaspart vs. NPH + humaninsulin i basal-bolus-regime for type 1-diabetes |
| [NCT01513473](https://clinicaltrials.gov/study/NCT01513473) | Fase 3 | Afsluttet | 350 | 26-ugers + 26-ugers udvidelsesrandomiseret kontrolleret forsøg af degludec vs. detemir med insulinaspart som bolus hos børn/adolescenter med type 1-diabetes (BEGIN Young 1) |
| [NCT02670915](https://clinicaltrials.gov/study/NCT02670915) | Fase 3 | Afsluttet | 834 | Globalt randomiseret kontrolleret forsøg af hurtigere virkendeultrakorte insulinaspart vs. NovoRapid, begge kombineret med degludec, hos børn/adolescenter med type 1-diabetes |
| [NCT01134107](https://clinicaltrials.gov/study/NCT01134107) | Fase 3 | Afsluttet | 133 | Blindet cross-over randomiseret kontrolleret forsøg af insulinlispro vs. insulinaspart i CSII-pumpekartucher for type 1-diabetes |
| [NCT00046150](https://clinicaltrials.gov/study/NCT00046150) | Fase 3 | Afsluttet | 59 | Randomiseret kontrolleret forsøg sammenlignende sikkerhed for HMR1964 vs. insulinaspart i kontinuerlig subkutan insulininfusion (CSII) for type 1-diabetes |
| [NCT01513590](https://clinicaltrials.gov/study/NCT01513590) | Fase 3 | Afsluttet | 394 | 26-ugers randomiseret kontrolleret forsøg af insulindegludec/aspart (IDegAsp) vs. BIAsp 30, begge med metformin, hos insulinnaïf type 2-diabetes |
| [NCT04196231](https://clinicaltrials.gov/study/NCT04196231) | Fase 4 | Afsluttet | 258 | Randomiseret kontrolleret forsøg (BEYOND) evaluering af varighed af glykæmisk kontrol med basalinsulin/GLP-1-agonist eller SGLT-2-hæmmer vs. basal-bolus-regime hos type 2-diabetes |
| [NCT06199505](https://clinicaltrials.gov/study/NCT06199505) | Fase 2 | Afsluttet | 153 | Randomiseret kontrolleret forsøg sammenlignende GZR101 vs. insulindegludec/aspart hos type 2-diabetes utilstrækkeligt kontrolleret med orale midler |
| [NCT00675493](https://clinicaltrials.gov/study/NCT00675493) | I.a. (observationelt) | Afsluttet | 942 | 24-ugers observationelt studie af NovoMix 30 (bifasisk insulinaspart 30) for type 1-diabetes/type 2-diabetes glykæmisk kontrol (Rumænien) |
| [NCT00700648](https://clinicaltrials.gov/study/NCT00700648) | I.a. (observationelt) | Afsluttet | 3024 | Multicenterstudie af intravenøs insulinaspart (NovoRapid) sikkerhed/effektivitet hos hospitaliserede patienter (Asien) |

---

## Litteraturbevis

| PMID | År | Type | Journal | Vigtige resultater |
|------|-----|------|------|---------|
| [37863084](https://pubmed.ncbi.nlm.nih.gov/37863084/) | 2023 | Randomiseret kontrolleret forsøg | Lancet | ONWARDS 6: en gang ugentlig insulinicodec vs. en gang daglig degludec som del af basal-bolus-regime (med aspart som bolus) hos type 1-diabetes |
| [36623517](https://pubmed.ncbi.nlm.nih.gov/36623517/) | 2023 | Randomiseret kontrolleret forsøg | Lancet Diabetes & Endocrinology | EXPECT-forsøg: degludec vs. detemir, begge kombineret med insulinaspart, hos gravide kvinder med type 1-diabetes |
| [21333580](https://pubmed.ncbi.nlm.nih.gov/21333580/) | 2011 | Randomiseret kontrolleret forsøg/systematisk oversigt | Diabetes & Metabolism | Systematisk oversigt bekræftende effektivitet/sikkerhed for hurtigtvirkende insulinaspart vs. regulært humaninsulin hos type 1-diabetes og type 2-diabetes |
| [41697686](https://pubmed.ncbi.nlm.nih.gov/41697686/) | 2026 | Oversigt | JAMA | Oversigt over type 1-diabetes patofysiologi (autoimmun β-celleødelæggelse) og epidemiologi, som understøtter insulinerstattingsrationale |
| [37290466](https://pubmed.ncbi.nlm.nih.gov/37290466/) | 2023 | Oversigt | Lancet Diabetes & Endocrinology | Behandling af type 1-diabetes under graviditet, inklusiv brug af insulinanaloger og glykæmiske målværdier |
| [15871555](https://pubmed.ncbi.nlm.nih.gov/15871555/) | 2003 | Oversigt | Treatments in Endocrinology | Insulinaspart sænker HbA1c vs. regulært humaninsulin hos type 1-diabetes/type 2-diabetes randomiserede kontrollerede forsøg |
| [12215068](https://pubmed.ncbi.nlm.nih.gov/12215068/) | 2002 | Oversigt | Drugs | Oversigt over insulinasparts effektivitet/sikkerhed hos type 1-diabetes og type 2-diabetes behandling |
| [25143741](https://pubmed.ncbi.nlm.nih.gov/25143741/) | 2014 | Oversigt | Vascular Health and Risk Management | Insulindegludec/aspart-kombination til type 1-diabetes og type 2-diabetes behandling |
| [30789066](https://pubmed.ncbi.nlm.nih.gov/30789066/) | 2019 | Oversigt | Expert Opinion on Drug Metabolism & Toxicology | Oversigt over brug af degludec/aspart-premixinsulin hos type 1-diabetes |
| [18710361](https://pubmed.ncbi.nlm.nih.gov/18710361/) | 2008 | Kohortestudie | Expert Opinion on Pharmacotherapy | Evidensbaseret oversigt over bifasisk insulinaspart 30 til type 1-diabetes behandling |

---

## Danmark-markedsinformation

Insulinaspart har i øjeblikket **ingen markedsføringstilladelser registreret i Danmark** (markedsstatus: Ikke markedsført; 0 licenser). Ingen Lægemiddelstyrelsen eller centraliserede EMA-autoritetsdata er tilgængelige i denne evidenspakke.

---

## Sikkerhedshensyn

Se venligst den godkendte Produktinformationstekst (SmPC) for sikkerhedsinformation. Der var ingen vigtige advarsler, kontraindikationer eller lægemiddel-lægemiddel-interaktionsdata tilgængelige til ekstrahering fra denne evidenspakke (DDI-forespørgselsstatus: ikke fundet).

---

## Konklusion og næste trin

**Beslutning: Fortsæt med forholdsregler**

**Begrundelse:**
- Det kliniske forsøgs- og litteraturgrundlag for insulinaspart hos type 1-diabetes mellitus er omfattende og modent (flere afsluttede fase 3-randomiserede kontrollerede forsøg, årtiers publiceret evidens), men denne evidens bekræfter en **allerede etableret indikation**, ikke en ny genudnyttelsesmulighed — "forudsigelsen" opstod fra en datakløft i feltet `original_indications`, ikke en ægte modelbaseret hypotese.
- Fordi produktet **ikke er markedsført i Danmark**, er den praktiske værdi af denne evidenspakke, at den understøtter, om man skal forfølge dansk markedsføringstilladelse for et insulinprodukt med en velkendt international sikkerhed- og effektivitetsrekord — ikke en genudnyttelsesevaluering.

**For at fortsætte er følgende nødvendigt:**
- TFDA/SmPC-ækvivalent dansk eller EU-mærkat-data (advarsler, kontraindikationer, forholdsregler) — i øjeblikket et **blokerende** datakløft, der forhindrer enhver S1-sikkerhedsforberedende vurdering
- Bekræftet virkningsmekanisme-dokumentation fra DrugBank (i øjeblikket et **høj**-alvorlighed datakløft)
- Korrektion af feltet `original_indications`, så fremtidige TxGNN-kørsler ikke gensurfacer lægemidlets egen kerneindikation som en "forudsagt ny indikation"
- Hvis dansk markedsindtræden er det egentlige mål, en formel gennemgang af EMA/centraliseret tilladelsestatus for insulinaspart-produkter (f.eks. NovoRapid, Fiasp) og anvendelighed for det danske marked

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

