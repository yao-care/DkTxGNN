---
layout: default
title: Obinutuzumab
parent: Høj evidens (L1-L2)
nav_order: 316
evidence_level: L1
indication_count: 6
---

# Obinutuzumab
{: .fs-9 }

Evidensniveau: **L1** | Forudsagte indikationer: **6** stk.
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

# Obinutuzumab: Fra CD20+ B-cellemalignitet til follikulært lymfom

## Sammenfatning i én sætning

Obinutuzumab (DrugBank DB08935) er et type II anti-CD20 monoklonalt antistof; Danmark-specifikke oprindelige indikationer og etiketdata er ikke tilgængelige i dette datasæt (datakløft). TxGNN-modellens bevisbaserede lede kandidat i denne pakke er **Follikulært lymfom**, understøttet af **>40 matchede kliniske studier (10 højest relevante vist)** — herunder to afsluttede fase 3-RCT'er — og **19 publikationer**, hvilket giver det det stærkeste bevisniveau (L1) blandt alle evaluerede kandidater.

> **Bemærkning om ranking**: TxGNN's højest scorede forudsigelser (rang 1–4) er snævert navngivne CLL/SLL molekylære undertyper (f.eks. "pregerminal center CLL/SLL"), som returnerede **nul** matchende forsøg eller litteratur — pakkens egen analyse tilskriver dette sygdomsnavn-granularitet, ikke en sand mangel på bevis, og anbefaler gensorgering med bredere CLL/SLL-betingelser. Fordi Follikulært lymfom (rang 5, score 99.18%, i hovedsagen bundet med rang 1's 99.21%) er den eneste kandidat i dette datasæt med faktisk hentbar bevis, bruges det som lede kandidat for denne rapport.

## Hurtig oversigt

| Element | Indhold |
|------|------|
| Oprindelig indikation | Ikke tilgængelig — lægemidlet er ikke registreret i Danmark; ingen lokale etiket-/indikationstekster på fil (datakløft DG001/DG002) |
| Forudsagt ny indikation | Follikulært lymfom |
| TxGNN-forudsigelse score | 99.18% |
| Bevisniveau | L1 |
| Danmark markedsstatus | Ikke markedsført |
| Antal markedsføringstilladelser | 0 |
| Anbefalet beslutning | Fortsæt med sikkerhedsforanstaltninger |

## Hvorfor er denne forudsigelse rimelig?

Obinutuzumab er et glykoengineret, humaniseret type II anti-CD20 monoklonalt antistof. Det bindes til CD20 på overfladen af B-celler og inducerer celledød gennem en kombination af antistof-afhængig cellulær cytotoxicitet (ADCC), antistof-afhængig cellulær fagocytose (ADCP) og direkte (ikke-apoptotisk) celledød — en mekanisme der er forskellig fra og generelt mere potent end type I anti-CD20 antistoffer såsom rituximab.

Follikulært lymfom-tumorceller er karakteristisk CD20-positive, hvilket gør dem til en direkte farmakologisk match for obinutuzumabs mål. Dette er ikke et spekulativt mekanistisk spring: obinutuzumab (Gazyva/Gazyvaro) er allerede en godkendt terapi for follikulært lymfom i flere andre jurisdiktioner (både først-linje og rituximab-refraktær/recidivering indstillinger), og datasættets eget kliniske forsøg og litteraturrecord for FL er omfattende og modent — herunder det pivotale fase 3-forsøg GALLIUM (NCT01332968, n=1,401) sammenlignet obinutuzumab-kemoterapi med rituximab-kemoterapi.

De andre højt scorede forudsigelser i denne pakke (pregerminal-center og IGHV-mutation-definerede CLL/SLL-undertyper) er mekanistisk lige så plausible — CD20-ekspression er uafhængig af disse molekylære subtypeskemaer — men dette datasæt kunne ikke hente forsøgs- eller litteraturbevis for disse nøjagtige subtype-navne. Dette er højst sandsynligt et søge-granularitets-artefakt snarere end en ægte mangel på understøttende data, og garanterer en opfølgende forespørgsel ved hjælp af det bredere begreb "kronisk lymfocytært leukæmi/lille lymfocytært lymfom" før disse kandidater scoreres eller afvises.

## Klinisk forsøgbevis

| Forsøgsnummer | Fase | Status | Tilmelding | Nøglefund |
|---------|------|------|------|---------|
| [NCT01332968](https://clinicaltrials.gov/study/NCT01332968) | Fase 3 | Afsluttet | 1401 | GALLIUM-forsøg: obinutuzumab + kemoterapi mod rituximab + kemoterapi hos tidligere ubehandlet avanceret indolent NHL (hovedsageligt FL) |
| [NCT01059630](https://clinicaltrials.gov/study/NCT01059630) | Fase 3 | Afsluttet | 413 | Bendamustin alene mod bendamustin + obinutuzumab hos rituximab-refraktør indolent NHL |
| [NCT03332017](https://clinicaltrials.gov/study/NCT03332017) | Fase 2 | Afsluttet | 217 | ROSEWOOD: zanubrutinib + obinutuzumab mod obinutuzumab monaterapi hos recidivering/refraktør FL (Grad A — nøgle-komparatortest) |
| [NCT01691898](https://clinicaltrials.gov/study/NCT01691898) | Fase 1/2 | Afsluttet | 231 | Randomiseret evaluering af obinutuzumab-baserede kombinationsregimer hos recidivering/refraktør FL (Grad A) |
| [NCT02611323](https://clinicaltrials.gov/study/NCT02611323) | Fase 1b/2 | Afsluttet | 133 | Obinutuzumab + polatuzumab vedotin + venetoclax hos recidivering/refraktør FL (Grad A) |
| [NCT06191744](https://clinicaltrials.gov/study/NCT06191744) | Fase 3 | Rekrutterer | 1095 | EPCORE™FL-2: epcoritamab + R² mod kemoimmunoterapi hos tidligere ubehandlet FL |
| [NCT05100862](https://clinicaltrials.gov/study/NCT05100862) | Fase 3 | Rekrutterer | 780 | Zanubrutinib + anti-CD20-antistoffer mod lenalidomid + rituximab hos recidivering/refraktør FL/MZL |
| [NCT05929222](https://clinicaltrials.gov/study/NCT05929222) | Fase 3 | Rekrutterer | 190 | GAZEBO: strålebethandling alene mod strålebethandling + obinutuzumab hos tidlig-stadie FL |
| [NCT03980171](https://clinicaltrials.gov/study/NCT03980171) | Fase 1b/2 | Aktiv, ikke rekrutterer | 50 | Lenalidomid + venetoclax + obinutuzumab hos behandlingsnaiv FL (Grad B) |
| [NCT01680991](https://clinicaltrials.gov/study/NCT01680991) | Fase 1 | Afsluttet | 48 | Farmakokinetik/sikkerhed af obinutuzumab hos kinesiske patienter med CD20+ malignitet (Grad B — doseringsbasis) |

## Litteraturbevis

| PMID | År | Type | Tidsskrift | Nøglefund |
|------|-----|------|------|---------|
| [28976863](https://pubmed.ncbi.nlm.nih.gov/28976863/) | 2017 | RCT | New England Journal of Medicine | GALLIUM: obinutuzumab-baseret mod rituximab-baseret kemoterapi til først-linje FL |
| [29856692](https://pubmed.ncbi.nlm.nih.gov/29856692/) | 2018 | RCT | Journal of Clinical Oncology | GALLIUM underanalyse: indflydelse af kemoterapibasis på efficacy/sikkerhed |
| [37404773](https://pubmed.ncbi.nlm.nih.gov/37404773/) | 2023 | RCT | HemaSphere | GALLIUM slutanalyse: obinutuzumab mod rituximab immunokemoterapi hos ubehandlet iNHL |
| [37506346](https://pubmed.ncbi.nlm.nih.gov/37506346/) | 2023 | RCT | Journal of Clinical Oncology | ROSEWOOD: zanubrutinib + obinutuzumab mod obinutuzumab monaterapi hos recidivering/refraktør FL |
| [31296423](https://pubmed.ncbi.nlm.nih.gov/31296423/) | 2019 | RCT | The Lancet Haematology | GALEN: obinutuzumab + lenalidomid hos recidivering/refraktør FL |
| [31360086](https://pubmed.ncbi.nlm.nih.gov/31360086/) | 2017 | Review | Blood and Lymphatic Cancer: Targets and Therapy | Indflydelse af obinutuzumab alene og i kombination for FL |
| [38660754](https://pubmed.ncbi.nlm.nih.gov/38660754/) | 2024 | Review | Turkish Journal of Haematology | Omfattende oversigt over FL-ledelse, herunder obinutuzumab-baserede regimer |
| [39830356](https://pubmed.ncbi.nlm.nih.gov/39830356/) | 2024 | Review/HTA | Frontiers in Pharmacology | Efficacy, sikkerhed og cost-effectiveness af obinutuzumab i FL |
| [35180337](https://pubmed.ncbi.nlm.nih.gov/35180337/) | 2022 | Review | Oncology (Williston Park) | Nuværende og nye terapier for FL |
| [28324270](https://pubmed.ncbi.nlm.nih.gov/28324270/) | 2017 | Review | Targeted Oncology | Obinutuzumab hos rituximab-refraktør/recidivering FL |

## Danmarks markedsinformation

Obinutuzumab er i øjeblikket ikke markedsført i Danmark, og ingen markedsføringstilladelser (nationale Lægemiddelstyrelsen eller centraliserede EMA) er på fil i dette datasæt.

## Cytotoxicitet

Obinutuzumab er et antineoplastisk middel (målrettet immunoterapiklasse, brugt på tværs af CD20+ B-cellemaligniter herunder den forudsagt FL-indikation).

| Element | Indhold |
|------|------|
| Cytotoxicitets klassifikation | Målrettet terapi / immunoterapi (anti-CD20 monoklonalt antistof) — ikke en konventionel cytotoksisk kemoterapibethandling |
| Myelosuppression risiko | Lav–Moderat; anti-CD20-antistoffer som en klasse er forbundet med neutropeni (herunder forsinket-debut) og B-celle-depletion; ingen lægemiddelspecifik cytotoxicitets-data tilgængelig i dette datasæt |
| Emetogenicitets klassifikation | Lav; monoklonale antistoffer er generelt minimalt emetogene, selvom infusionsrelaterede reaktioner er almindelige ved første infusioner |
| Overvågningselementer | CBC med differentialcelleantal (neutropeni), hepatitis B screening/overvågning (anti-CD20 reaktiveringsrisiko), infusionsrelateret reaktion overvågning under administration |
| Håndteringsbeskyttelse | Standard biologiske infusionsprocedurer gælder; kræver ikke håndteringsprotokoller for cytotoksiske lægemidler, men præmedikaion og infusionsovervågning efter klassemarkeringen anbefales — venligst se SmPC for præcis vejledning |

## Sikkerhedsovervejelser

Se venligst det godkendte produktresumé (SmPC) for sikkerhedsinformationer. Ingen lægemiddelinteraktions-, kontraindikations- eller advarselsdata specifikt for obinutuzumab var genkrævelig i dette datasæt (DDI-forespørgsel: ikke fundet).

## Konklusion og næste skridt

**Beslutning: Fortsæt med sikkerhedsforanstaltninger**

**Begrundelse:**
- Follikulært lymfom-indikationen er understøttet af L1-niveau-bevis, herunder to afsluttede fase 3-RCT'er (GALLIUM og bendamustin ± obinutuzumab-forsøget) og en modent litteraturbase på 19 publikationer, og afspejler godkendelser, der allerede er givet i andre jurisdiktioner.
- Imidlertid er lægemidlet i øjeblikket uregistreret i Danmark, og både etiket-niveau sikkerhedsdata (DG001, Blokering) og formel virkningsmekanisme-dokumentation (DG002, Høj) er datakløfter, der skal lukkes, før en S1-sikkerhedsgennemgang kan fortsætte.

**For at fortsætte er følgende nødvendigt:**
- TFDA/Danmarks SmPC-advarsler, kontraindikationer og DDI-data (DG001)
- Verificeret virkningsmekanisme-dokumentation (DG002)
- Bekræftelse af EU/EMA centraliseret markedsføringstilladelsestatus for obinutuzumab i Danmark
- En opfølgende bevisesøgning ved hjælp af det bredere begreb "kronisk lymfocytært leukæmi/lille lymfocytært lymfom" for korrekt at evaluere rang 1–4 molekylære undertype-forudsigelser, som i øjeblikket viser nul bevis sandsynligvis på grund af for specifikt sygdomsnavn

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

