---
layout: default
title: Catridecacog
parent: Kun modelforudsigelse (L5)
nav_order: 96
evidence_level: L5
indication_count: 10
---

# Catridecacog
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

# Catridecacog: Fra medfødt Factor XIII mangel til primær frigivelsesforstyrrelse af blodplader

## Resumé på én sætning

Catridecacog (NovoThirteen®) er en rekombinant humant Factor XIII A-subunit godkendt af EMA og FDA til profylakse af blødning ved medfødt Factor XIII A-subunit mangel, men er i øjeblikket ikke registreret i Danmark.
TxGNN-modellens højest rangerede forudsigelse er virkning ved **primær frigivelsesforstyrrelse af blodplader** (score 99.29%), understøttet alene af mekanistisk ræsonnement uden **nogen kliniske forsøg eller publikationer** der er tilgængelig for denne indikation.
Vigtigt er det, at modellen også uafhængigt identificerer **medfødt Factor XIII mangel** som en forudsigelse med høj sikkerhed (score 98.79%, rang 7), understøttet af **9 kliniske forsøg** og **3 publikationer** — både validering af modellen og fremhævelse af et betydeligt regulatorisk tilgangsproblem for danske patienter med denne sjældne blødningsforstyrrelse.

---

## Hurtig oversigt

| Element | Indhold |
|---------|---------|
| Original indikation | Medfødt Factor XIII A-subunit mangel (EMA/FDA godkendt; ikke registreret i Danmark) |
| Foreslået ny indikation | Primær frigivelsesforstyrrelse af blodplader |
| TxGNN forudsigelsesscore | 99.29% |
| Evidensniveau | L5 |
| Markeds status Danmark | Ikke markedsført |
| Antal markedsføringstilladelser | 0 |
| Anbefalet afgørelse | Indholder |

---

## Hvorfor er denne forudsigelse rimelig?

I øjeblikket er detaljerede data om virkningsmekanisme ikke tilgængelig i denne evidenspakke. Baseret på kendt farmakologisk information er catridecacog en rekombinant humant koagulationsfaktor XIII A-subunit (rFXIII-A). Når det administreres intravenøst, rekonstituerer det funktionel Factor XIII ved at kombinere med den endogene cirkulerende B-subunit. Ved aktivering af thrombin i nærvær af kalciumioner katalyserer aktivt FXIIIa dannelsen af kovalente ε-(γ-glutamyl)lysin tværbindinger mellem fibrin γ-γ og α-α kæder, hvilket producerer en mekanisk stabil og fibrinolysisresistent blodprop — det sidste stabiliseringstrin i sekundær hemostase-kaskaden.

Det biologiske rationale for forudsigelsen i **primær frigivelsesforstyrrelse af blodplader** hviler på det faktum, at blodplader lagrer Factor XIII i deres α-granula og frigiver det ved aktivering. Hos patienter med α-granula frigivelsesdefekter eller tæthed granulumangel svigter blodpladeaktivering til at frigive ADP, ATP, serotonin og α-granula-lagrede indhold, herunder blodplade-bundet Factor XIII korrekt. Eksomt rFXIII kunne teoretisk kompensere for dette frigivelsesafhængige funktionelt FXIII deficit ved at styrke downstream fibrin blodpropdannelse. Imidlertid bevarer patienter med primær blodplade-frigivelsesforstyrrelse typisk væsentligt cirkulerende plasma FXIII (plasmapoolen tegner sig for den dominerende andel af systemisk FXIII aktivitet), så det funktionelle deficit er langt mindre alvorligt end ved medfødt FXIII mangel, og det kliniske gavn-tærskel for supplementering er usikker.

TxGNN forudsigelsesscore på 0.9929 hidrør højst sandsynligt fra den biologiske sammenhæng mellem blodplade α-granula og Factor XIII indlejret i vidensgrafen — en mekanistisk gyldig forbindelse — snarere end fra nogen direkte klinisk evidens. Denne forudsigelse bør behandles som et hypotesegenererende signal alene, der kræver prospektiv undersøgelse før klinisk anvendelse.

---

## Evidens fra kliniske forsøg

I øjeblikket ingen relaterede kliniske forsøg registreret for catridecacog ved primær frigivelsesforstyrrelse af blodplader.

---

> **Kontekstuel note — medfødt Factor XIII mangel (TxGNN rang 7, score 98.79%, evidensniveau L1)**
>
> Selvom medfødt Factor XIII mangel er catridecacogs globalt godkendte indikation snarere end et nyt gentilføringsmål, har det ingen markedsføringstilladelse i Danmark. Forsøgene nedenfor er direkte relevante for danske læger, der søger tilgang for berettigede patienter, og fungerer som intern modelvalidering, der demonstrerer, at TxGNN korrekt gendanner medicinerets etablerede indikation.

| Forsøgsnummer | Fase | Status | Tilmelding | Vigtigste resultater |
|-------------|------|--------|------------|-------------|
| [NCT00713648](https://clinicaltrials.gov/study/NCT00713648) | Fase 3 | Afsluttet | 41 | MENTOR1: Afgørende multi-center åbent label enkeltarm forsøg af månedlig profylaktisk rFXIII substitution hos voksne med medfødt FXIII mangel; primært grundlag for EMA/FDA godkendelse |
| [NCT00978380](https://clinicaltrials.gov/study/NCT00978380) | Fase 3 | Afsluttet | 63 | MENTOR2: Langtid sikkerhedsudvidelsesstudie med op til 36 måneder månedlig profylakse; største fase 3 datasæt for denne indikation |
| [NCT01862367](https://clinicaltrials.gov/study/NCT01862367) | Observationelt | Afsluttet | 30 | Prospektivt multi-center real-world studie af NovoThirteen® hos EU-patienter; overvågning af FXIII antibiotikaformation, allergiske reaktioner og tromboemboliske hændelser |
| [NCT01253811](https://clinicaltrials.gov/study/NCT01253811) | Fase 3 | Afsluttet | 6 | Pædiatrisk sikkerhedsudvidelse (alderen 1–6 år); langtid månedlig profylakse data hos små børn med medfødt FXIII A-subunit mangel |
| [NCT01230021](https://clinicaltrials.gov/study/NCT01230021) | Fase 3b | Afsluttet | 6 | MENTOR4: PK og sikkerhedsprofil for enkelt IV dosis rFXIII hos pædiatriske patienter (alderen 1–6); grundlag for pædiatrisk dosisekstrapolation |
| [NCT00056589](https://clinicaltrials.gov/study/NCT00056589) | Fase 1 | Afsluttet | 11 | Første patient dosestigning studie ved medfødt FXIII mangel; etablerede sikkerhed og PK profil i målpopulationen |
| [NCT01082406](https://clinicaltrials.gov/study/NCT01082406) | Fase 1 | Afsluttet | 51 | Bioækvivalens krydsover studie, der sammenligner rFXIII fra to producenter (Novo Nordisk mod Avecia) hos raske frivillige |
| [NCT01848002](https://clinicaltrials.gov/study/NCT01848002) | Fase 1 | Afsluttet | 24 | Multi-dose sikkerhed og PK randomiseret dobbelt-blind placebo-kontrolleret studie hos raske frivillige; karakteriserede dosisakkumulering og gentagen-dose sikkerhed |
| [NCT01847989](https://clinicaltrials.gov/study/NCT01847989) | Fase 1 | Afsluttet | 50 | Enkelt-dose eskalering sikkerhed og PK randomiseret dobbelt-blind placebo-kontrolleret studie hos raske frivillige; etablerede dosis-eksponerings forhold |

---

## Litteraturbevis

I øjeblikket ingen relateret litteratur tilgængelig for catridecacog ved primær frigivelsesforstyrrelse af blodplader.

---

> **Kontekstuel litteratur — medfødt Factor XIII mangel**

| PMID | År | Type | Tidsskrift | Vigtigste resultater |
|------|-----|------|-----------|-------------|
| [36580025](https://pubmed.ncbi.nlm.nih.gov/36580025/) | 2023 | Kohort | Blood Transfusion | Italiensk FXIII-studie: Multi-center real-world vurdering af catridecacog virkning og sikkerhed hos FXIII-deficiente patienter; dækker PK fra MENTOR2 forsøg til klinisk praksis |
| [30915205](https://pubmed.ncbi.nlm.nih.gov/30915205/) | 2019 | Casusrapport | Hematology Reports | Vellykket perioperativ ledelse ved hjælp af catridecacog profylakse (35 IU/kg hver 28. dag) hos en patient med alvorlig FXIII mangel, der gennemgår lyskebrokkirurgi |
| [25031548](https://pubmed.ncbi.nlm.nih.gov/25031548/) | 2014 | Oversigt | Journal of Blood Medicine | Omfattende oversigt over catridecacog som gennembrudsbehandling for medfødt FXIII A-subunit mangel; dækker klinisk præsentation, diagnostik og det centrale kliniske evidensgrundlag |

---

## Danmark markedsinformation

Catridecacog er ikke registreret hos Lægemiddelstyrelsen og har ingen aktuelle markedsføringstilladelser i Danmark.

Produktet markedsføres som **NovoThirteen®** (Novo Nordisk A/S) under en centraliseret EMA markedsføringstilladelse for medfødt Factor XIII A-subunit mangel. Danske patienter med bekræftet medfødt FXIII mangel kan være berettigede til adgang gennem en individuel patiencimp (*særlig tilladelse*) eller navnepatient program via Lægemiddelstyrelsen.

---

## Sikkerhedshensyn

Se venligst den godkendte produktinformations (SmPC) for sikkerhedsinformation.

---

## Konklusion og næste skridt

### Afgørelse A: Indholder — primær frigivelsesforstyrrelse af blodplader (TxGNN rang 1, L5)

**Begrundelse:**
TxGNN's toprangerede forudsigelse for primær frigivelsesforstyrrelse af blodplader hviler alene på den biologiske sammenhæng mellem blodplade α-granula og Factor XIII indhold. Der er ingen kliniske forsøg, observationsstudier eller casusrapporter, der understøtter denne indikation. Selvom det mekanistiske hypotese er sammenhængende, forbliver plasma FXIII pools stort set intakte hos patienter med blodplade frigivelsesforstyrrelse, hvilket gør det kliniske gavn ved supplementering usikkert.

**For at fortsætte, kræves følgende:**
- Måling af funktionel FXIII aktivitetsniveauer hos patienter med primær blodplade frigivelsesforstyrrelse for at karakterisere den faktiske grad af mangel
- Udforskende pilotstudie eller prospektiv casusserie hos patienter med dokumenteret blødningsfænotype og bekræftet frigivelsesforstyrrelse
- Hentning af fuld MOA data fra DrugBank (DrugBank ID: DB09310) for at styrke det mekanistiske rationale
- Fuld SmPC gennemgang (TFDA/EMA) for kontraindikationer, advarsler og dossvejledning relevant for denne ikke-godkendte population

---

### Afgørelse B: Fortsæt med sikkerhedssystemer — medfødt Factor XIII mangel (TxGNN rang 7, L1)

**Begrundelse:**
Catridecacog har gennemført to centrale fase 3 forsøg (MENTOR1 og MENTOR2) og har en centraliseret EMA markedsføringstilladelse for medfødt Factor XIII A-subunit mangel — en af de sjældneste koagulationssygdomme globalt (estimeret incidens 1 på 2 millioner). Medicinen er ikke registreret i Danmark, hvilket skaber en direkte adgangsbarriere for danske patienter med denne potentielt livstruende sjælden blødningsforstyrrelse. Evidensgrundlaget er robust givet sygdommens sjældenhed.

**For at fortsætte, kræves følgende:**
- Engagement med Lægemiddelstyrelsen vedrørende *særlig tilladelse* (særlig importtilladelse) for individuelle patienter med bekræftet medfødt FXIII A-subunit mangel
- Kortlægning af hæmatologicentre for at identificere danske patienter med denne diagnose, der kan gavne adgang
- Koordinering med Novo Nordisk Danmark vedrørende navnepatient eller managed access program tilgængelighed
- Fuld SmPC gennemgang og lokal farmakovigilance plan før klinisk brug

---

> ⚠️ **Ansvarsfraskrivelse:** Denne rapport er til forskningsreferenceformål kun og udgør ikke medicinsk rådgivning. Lægemiddel-gentilføringskandidat kræver klinisk validering før anvendelse. Alle resultater bør fortolkes af kvalificerede sundhedspersonale i sammenhæng med godkendt produktinformation.

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

