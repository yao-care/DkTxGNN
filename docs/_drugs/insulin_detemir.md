---
layout: default
title: Insulin Detemir
parent: Høj evidens (L1-L2)
nav_order: 236
evidence_level: L1
indication_count: 10
---

# Insulin Detemir
{: .fs-9 }

Evidensniveau: **L1** | Forudsagte indikationer: **10** stk.
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

# Insulin detemir: Fra en udokumenteret oprindelig indikation til type 1-diabetes mellitus (sandsynligvis eksisterende indikation)

## Sammenfatning i én sætning

Insulin detimirs oprindelige indikation er ikke registreret i denne bevissamling (datakløft), men lægemidlet er generelt kendt som et langtidsvirkende basal-insulinanalog. TxGNN-modellen forudsiger, at det kan være effektivt for **type 1-diabetes mellitus**, med **dusin af kliniske forsøg** (mange afsluttede fase 3-RCT'er) og **betydelig litteratur** til støtte for denne retning — imidlertid er dette meget sandsynligt en **allerede godkendt eksisterende indikation** snarere end et ægte nyt omformålingstilfælde, og dette skal verificeres, før der fremsættes påstande om "ny indikation".

---

## Hurtig oversigt

| Punkt | Indhold |
|------|---------|
| Oprindelig indikation | Ikke registreret i dette datasæt — insulin detemir er generelt et langtidsvirkende basal-insulin, så dette er sandsynligvis en eksisterende (ikke ny) indikation; kræver verifikation |
| Forudsagt ny indikation | Type 1-diabetes mellitus |
| TxGNN-forudsigelsesscore | 99,77% |
| Bevisniveau | L1 |
| Markedsstatus i Danmark | Ikke markedsført (ifølge dette datasæt — se varsel nedenfor) |
| Antal markedsføringstilladelser | 0 |
| Anbefalet afgørelse | Tilbageholdelse |

---

## Hvorfor er denne forudsigelse rimelig?

Detaljerede data om virkningsmekanisme er ikke tilgængelige i denne bevissamling (datakløft DG002, alvorlighed: Høj). Generelt er insulin detemir et rekombinant human-insulinanalog, der er modificeret ved B29-lysine-residuen med en C14 (myristinsyre) fedtsyrukæde, hvilket tillader reversibel binding til serumalbumin. Dette bremser subkutan absorption og producerer en udvidet, relativt flad tidsvirknerprofil sammenlignet med NPH-insulin — det farmakologiske grundlag for dets brug som et én- eller todaglig basal-insulin. Dette er det samme aktivt stof, der markedsføres internationalt under mærkenavnet Levemir®.

Fordi feltet `original_indications` i dette datasæt er tomt, kunne systemet ikke automatisk bekræfte, hvorvidt "type 1-diabetes mellitus" allerede er lægemidlets godkendt indikation snarere end en ny. Langtidsvirkende basal-insulinanaloger i denne klasse er efter design og efter regulatorisk historie angivet for basal glykæmisk kontrol i både type 1 og type 2-diabetes. Den ekstremt høje TxGNN-score (99,77%) kombineret med en meget stor mængde afsluttede fase 3-randomiserede kontrollerede forsøg afspejler mest sandsynligt et stærkt, allerede etableret lægemiddel-sygdoms-forhold i vidensgrafen — **ikke** en ny mekanistisk hypotese.

Bevissamlingens egen omformålingsreference flag dette direkte: *"此案例的決策重點在於『引進/上市可行性』而非機轉新穎性…建議人工核實後移除或標註為『既有適應症之市場引進』而非典型 repurposing 候選"* (afgørelsens fokus her er markedsadgangenes gennemførlig, ikke mekanistisk nyhed; manuel gennemgang bør omklassificere dette som "markedsintroduktion af en eksisterende indikation" snarere end en typisk omformålingskandidat). Dette varsel bør løses — ved at hente lægemidlets dokumenteret oprindelige indikation fra TFDA/DrugBank/SmPC — før denne kandidat behandles som en ægte mulighed for gammel-lækemiddel-nye-bruger.

---

## Klinisk forsøgsbeviser

| Forsøgsnummer | Fase | Status | Antal deltagere | Vigtige fund |
|---------|------|------|------|---------|
| [NCT03220425](https://clinicaltrials.gov/study/NCT03220425) | Fase 3 | Afsluttet | 752 | 6-måneders effektivitets-/sikkerhedssammenligning af insulin detemir vs NPH-insulin i T1DM basal-bolus-regimen; stort direkte bevisgrundlag |
| [NCT01486940](https://clinicaltrials.gov/study/NCT01486940) | Fase 3 | Afsluttet | 598 | Multinational RCT sammenlignende detemir+aspart vs NPH+human solubel insulin i T1DM basal-bolus-terapi |
| [NCT01513473](https://clinicaltrials.gov/study/NCT01513473) | Fase 3 | Afsluttet | 350 | BEGIN™ Young 1: 26-ugers (+26-ugers forlængelse) sammenligning af insulin degludec vs detemir hos børn/ungdomme med T1DM |
| [NCT00447382](https://clinicaltrials.gov/study/NCT00447382) | Fase 3 | Afsluttet | 330 | 12-måneders dobbelblind sikkerhedssammenligning af to insulindetemir-fremstillingsprocesser i T1DM basal-bolus-regimen |
| [NCT01709929](https://clinicaltrials.gov/study/NCT01709929) | Fase 3 | Afsluttet | 2287 | Stort multi-center ikke-randomiseret sikkerhedsstudie af insulin detemir i T1DM og T2DM |
| [NCT01461616](https://clinicaltrials.gov/study/NCT01461616) | Fase 3 | Afsluttet | 19 | Åben-label tredobbelt cross-over-forsøg sammenlignende NPH, detemir og glargine på IGFBP-1/IGF-I i T1DM |
| [NCT00738153](https://clinicaltrials.gov/study/NCT00738153) | N/A (observationelt) | Afsluttet | 798 | Observationelt studie (Afrika) evaluering af effektivitet og alvorlige uønskede bivirkninger med Levemir® i T1DM og T2DM |
| [NCT00687284](https://clinicaltrials.gov/study/NCT00687284) | N/A (observationelt) | Afsluttet | 2188 | Stort europæisk observationelt studie af glykæmisk kontrol med Levemir® som initierings-terapi |
| [NCT01271517](https://clinicaltrials.gov/study/NCT01271517) | Fase 4 | Ukendt | 120 | RCT hos nydiagnosticerede ungdomme sammenlignende NPH, glargine og detemir på metabolisk kontrol og GH/IGF-I-aksen |
| [NCT00595374](https://clinicaltrials.gov/study/NCT00595374) | Fase 3 | Afsluttet | 114 | Europæisk RCT sammenlignende detemir+aspart vs NPH+aspart hos voksne med T1DM |

*Bemærk: dusin yderligere fase 1–4-forsøg (både RCT'er og observationelle studier) findes i bevissamlingen ud over dette top-10-udvalg; det fulde sæt omfatter graviditet, pæditrisk og komparator-populationer (glargine/degludec).*

---

## Litteraturbeviser

| PMID | År | Type | Journal | Vigtige fund |
|------|-----|------|------|---------|
| [36623517](https://pubmed.ncbi.nlm.nih.gov/36623517/) | 2023 | RCT | Lancet Diabetes Endocrinol | EXPECT-forsøg: åben-label, multinational ikke-underlegenhedsforsøg af degludec vs detemir (begge + aspart) hos gravide kvinder med T1DM |
| [36763996](https://pubmed.ncbi.nlm.nih.gov/36763996/) | 2022 | Systematisk gennemgang/Meta-analyse | Clin Ther | Effektivitet/tolerabilitet af degludec vs andre langtidsvirkende basal-analoger (inkl. detemir) i T1DM/T2DM |
| [29477399](https://pubmed.ncbi.nlm.nih.gov/29477399/) | 2018 | Systematisk gennemgang/Netværks-meta-analyse | Value Health | Komparativ effektivitet og sikkerhed af basal insulin-regimener hos voksne med T1DM |
| [23110609](https://pubmed.ncbi.nlm.nih.gov/23110609/) | 2012 | Gennemgang | Drugs | Omfattende gennemgang af insulin detimirs rolle som basal-terapi i T1DM og T2DM |
| [21878861](https://pubmed.ncbi.nlm.nih.gov/21878861/) | 2011 | Systematisk gennemgang/Meta-analyse | Pol Arch Med Wewn | Detemir vs NPH-insulin i T1DM — glykæmisk kontrol-resultater |
| [17326333](https://pubmed.ncbi.nlm.nih.gov/17326333/) | 2006 | Gennemgang | Vasc Health Risk Manag | Mekanisme og klinisk brug af detemir i T1DM og T2DM, inkl. reduceret hypoglykæmi-risiko |
| [15516157](https://pubmed.ncbi.nlm.nih.gov/15516157/) | 2004 | Gennemgang | Drugs | Tidlig omfattende gennemgang af detimirs farmakologi og brug i T1DM/T2DM |
| [20539842](https://pubmed.ncbi.nlm.nih.gov/20539842/) | 2010 | Gennemgang | Vasc Health Risk Manag | Opdateret behandlingsgennemgang, der positionerer detemir blandt basal-insulin-analoger |
| [36896906](https://pubmed.ncbi.nlm.nih.gov/36896906/) | 2024 | Gennemgang | Curr Diabetes Rev | To-dekader gennemgang af glargine i T1DM, med detemir som vigtig komparator |
| [18454569](https://pubmed.ncbi.nlm.nih.gov/18454569/) | 2008 | Gennemgang | Paediatr Drugs | Gennemgang af insulin-analog-præparater, inkl. detemir, hos børn/ungdomme med T1DM |

---

## Markedsinformation for Danmark

Ingen markedsføringstilladelser for insulin detemir er registreret i dette datasæt (markedsstatus: **Ikke markedsført**, 0 licenser på fil).

**Vigtig varsel:** Insulin detemir (Levemir®) er et internationalt markedsført EMA-centraliseret produkt. Et resultat på "0 licenser / ikke markedsført" i denne bevissamling er uforenelig med dets kendte globale regulatoriske status og skal behandles som et sandsynligt **datakløft** snarere end bekræftelse af sand fravær fra det danske marked. Dette skal verificeres direkte mod Lægemiddelstyrelses register og EMA's centraliserede proceduretatabase, før en eventuel markedsadgangsbeslutning finaliseres.

---

## Sikkerhedshensyn

Se venligst det godkendt produktresumé (SmPC) for sikkerhedsinformation.

**Kritisk udestående kløft:** Advarslerne og kontraindikationer for TFDA/SmPC-etiketten kunne ikke hentes til denne evaluering (datakløft DG001, alvorlighed: **Blokerende**). Ifølge bevissamlingen betyder dette kløft, at kandidaten **ikke kan fortsætte til S1-sikkerhedsinitialevaluerings-stadiet**, indtil etikettdata er tilgængelige. Dette alene er tilstrækkeligt grund til at tilbageholde sagen, uanset styrken af effektivitetsbeviserne ovenfor.

---

## Konklusion og næste trin

**Afgørelse: Tilbageholdelse**

**Begrundelse:**
- Et **Blokerende**-alvorligheds datakløft (manglende TFDA/SmPC-advarsler og kontraindikationer) forhindrer enhver sikkerhedsinitialevaluering (S1), uafhængigt af hvor stærk effektivitetsbeviserne er.
- Den forudsagt "nye" indikation (type 1-diabetes mellitus) er meget sandsynligt en **allerede godkendt, eksisterende brug** af insulin detemir snarere end en ægte omformålingskandidat; sagen skal omklassificeres, når lægemidlets dokumenteret oprindelige indikation bekræftes.
- Separat er modelens andre forudsigelser for dette lægemiddel (autoimmun ooforit, opsismodysplasi, thiamin-responsiv dysfunktionssyndrom, klassisk/fokal stiv-person-syndrom) alle bevisniveau L5 uden understøttende forsøg eller litteratur, og er allerede korrekt flag "Tilbageholdelse" — disse afspejler mest sandsynligt indirekte vidensgraps-stier (delt autoimmun/komorbidit eller insulin-signalerings-knudepunkter) snarere end plausible kliniske hypoteser.

**For at fortsætte kræves følgende:**
- Hent TFDA/Lægemiddelstyrelses SmPC-etiket (advarsler, kontraindikationer) for at lukke det blokerende datakløft og muliggøre S1-sikkerhedsevaluering
- Hent bekræftet virkningsmekanisme og **oprindelig godkendt indikation(er)** fra DrugBank/regulatoriske kilder for at fastslå, hvorvidt "type 1-diabetes mellitus" er ægte nyhed eller en eksisterende brug
- Verificer faktisk dansk/EU markedsføringstilladelse for insulin detemir (Levemir®), da "0 licenser / ikke markedsført" synes uforenelig med dets kendte EMA-centraliseret godkendelse
- Hvis omklassificeret som en eksisterende indikation, omdirigér denne bevissamling mod en markedsadgang-/prisevaluering snarere end en omformålsevaluering
- Hvis nogle af de lavere-rangerede sjælden-sygdoms-forudsigelser er særskilt interessant, skal målrettet litteratur-/mekanistiske søgninger tages i betragtning, før yderligere handling, da ingen har i øjeblikket nogen understøttende beviser

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

