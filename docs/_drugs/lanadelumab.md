---
layout: default
title: Lanadelumab
parent: Kun modelforudsigelse (L5)
nav_order: 254
evidence_level: L5
indication_count: 10
---

# Lanadelumab
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

# Lanadelumab: Fra arvelig angioødem til C1-inhibitor-mangel

## Sammenfatning på én sætning

Lanadelumab (Takhzyro®) er et monoklonalt antistof, der hæmmer plasma-kallikrein; de kliniske forsøgsoptegnelser i denne evidenspakke viser, at det er en allerede godkendt profylaktisk behandling for arvelig angioødem (HAE) i flere lande (f.eks. Japan, Kina, Sydkorea), selvom der ikke findes noget formelt indikations-/virkningsmekanisme-register for dette lægemiddel i den aktuelle evidenspakke, og det har i øjeblikket ingen markedsføringstilladelse i Danmark.

TxGNN-modellens topforudsigelse, **C1-inhibitor-mangel**, er den patofysiologiske betegnelse for Type I/II HAE — dvs. i det væsentlige den samme sygdom, som Lanadelumab allerede bruges til andre steder.

Dette understøttes af **22 kliniske forsøg** og **20 publikationer**, men bør læses som en *bekræftelse* af en eksisterende global indikation snarere end et nyt repurposing-signal.

---

## Kort oversigt

| Element | Indhold |
|---------|---------|
| Original-indikation | Arvelig angioødem (HAE) — udledt fra kliniske forsøgsdata i denne pakke; ingen formelt indikations-/virkningsmekanisme-register er til rådighed for dette lægemiddel |
| Forudsagt ny indikation | C1-inhibitor-mangel (klinisk ensbetydende med HAE Type I/II) |
| TxGNN-forudsigelsesscore | 99,996% |
| Bevisniveau | L2 (1 afsluttet Phase 3 RCT: HELP Study, NCT02586805) |
| Markedsstatus i Danmark | Ikke markedsført |
| Antal markedsføringstilladelser | 0 |
| Anbefalet afgørelse | Afvent |

---

## Hvorfor er denne forudsigelse rimelig?

Detaljerede virkningsmekanisme-data er ikke formelt registreret for dette lægemiddel i evidenspakken (original_moa: Datakløft). Imidlertid beskriver litteraturbeviserne, der er indsamlet sammen med forudsigelsen (PMID 30267321), Lanadelumab som "et fuldt human monoklonalt antistof, der hæmmer plasma-kallikrein," udviklet til at forhindre angioødem-anfald ved arvelig angioødem (HAE) forvoldt af mutationer i *SERPING1*, som fører til C1-inhibitor-mangel eller -dysfunktion, hvilket resulterer i ukontrolleret plasma-kallikrein-aktivitet og overdreven bradykinin-produktion.

Vigtigt er det, at "C1-inhibitor-mangel" — TxGNN-topforudsigelsen — ikke er en særskilt ny sygdom i forhold til HAE; det er den underliggende biokemiske klassificering af HAE Type I/II, den tilstand Lanadelumab oprindeligt blev udviklet til og allerede er godkendt for i flere jurisdiktioner (forsøgsoptegnelser i denne pakke henviser til godkendelsestatus i Japan, Kina og Sydkorea). Dette betyder, at modellen i det væsentlige har genidentificeret lægemidlets kendte indikation snarere end at have blotlagt en egentlig repurposing-kandidat. Den forudsagte score er meget høj (99,996%) præcis fordi lægemiddel-sygdoms-associationen allerede er velbegrundet i den underliggende vidensgrafs.

Tre andre TxGNN-forudsigelser i denne evidenspakke (serpinopati med giftig serpin-polymerisering, pankreatitis, pseudo-von Willebrand-sygdom, primær udgivelsesforstyrrelse af blodplader) scorede højt, men har ingen understøttende kliniske forsøg eller litteratur og blev scoret L5/Afvent — disse diskuteres ikke videre her, da de mangler bevisgrundlag.

---

## Kliniske forsøg

| Forsøgsnummer | Fase | Status | Deltagerantal | Vigtige resultater |
|---------|------|------|------|---------|
| [NCT02586805](https://clinicaltrials.gov/study/NCT02586805) | Fase 3 | Afsluttet | 125 | HELP Study — randomiseret, dobbeltblindet, placebo-kontrolleret forsøg bekræftende virkning/sikkerhed for Lanadelumab (DX-2930) til langtids-HAE-profylakse |
| [NCT02741596](https://clinicaltrials.gov/study/NCT02741596) | Fase 3 | Afsluttet | 212 | HELP Study Extension — åben-label langtids-sikkerhed og virkning opfølgning |
| [NCT04070326](https://clinicaltrials.gov/study/NCT04070326) | Fase 3 | Afsluttet | 21 | SPRING Study — sikkerhed, PK/PD hos børn med HAE 2 til <12 år |
| [NCT04180163](https://clinicaltrials.gov/study/NCT04180163) | Fase 3 | Afsluttet | 12 | Virkning og sikkerhed hos japanske HAE Type I/II-patienter |
| [NCT05460325](https://clinicaltrials.gov/study/NCT05460325) | Fase 3 | Afsluttet | 20 | Sikkerhed, PK og virkning hos kinesiske HAE-patienter over 26 uger |
| [NCT04444895](https://clinicaltrials.gov/study/NCT04444895) | Fase 3 | Afsluttet | 73 | Langtids-sikkerhed/virkning hos ikke-histamin-formidlet angioødem med normal C1-INH |
| [NCT04130191](https://clinicaltrials.gov/study/NCT04130191) | N/A | Afsluttet | 140 | ENABLE — 3-år real-world-effektivitetstudium |
| [NCT03845400](https://clinicaltrials.gov/study/NCT03845400) | N/A | Afsluttet | 168 | EMPOWER — observationelt HAE-anfaldrate-studium, USA/Canada |
| [NCT02093923](https://clinicaltrials.gov/study/NCT02093923) | Fase 1 | Afsluttet | 38 | Multipel stigende dosis sikkerhed/tolerabilitet/PK-studium hos HAE-forsøgspersoner |
| [NCT01923207](https://clinicaltrials.gov/study/NCT01923207) | Fase 1 | Afsluttet | 32 | First-in-human enkelt stigende dosis sikkerhed/tolerabilitet-studium hos sunde personer |

Der var ingen EudraCT-identifikatorer til stede i evidenspakken.

---

## Litteraturbevis

| PMID | År | Type | Journal | Vigtige resultater |
|------|-----|------|------|---------|
| [30480729](https://pubmed.ncbi.nlm.nih.gov/30480729/) | 2018 | RCT | JAMA | Lanadelumab vs. placebo reducerer signifikant HAE-anfaldrate (HELP Study primær publikation) |
| [40434599](https://pubmed.ncbi.nlm.nih.gov/40434599/) | 2025 | Netværks meta-analyse | Drugs in R&D | Sammenlignende virkning/sikkerhed for Lanadelumab vs. garadacimab, C1-INH, berotralstat for HAE-profylakse |
| [39508959](https://pubmed.ncbi.nlm.nih.gov/39508959/) | 2024 | Systematisk gennemgang | Clinical Reviews in Allergy & Immunology | Karakteriserer gennembrudsfald hos HAE-patienter på langtids-profylakse |
| [39836016](https://pubmed.ncbi.nlm.nih.gov/39836016/) | 2025 | Indirekte behandlingssammenligning | J Comp Eff Res | Sammenligner Lanadelumab vs. C1-INH hos børn med HAE (<12 år) |
| [34287942](https://pubmed.ncbi.nlm.nih.gov/34287942/) | 2022 | Åben-label extension | Allergy | HELP OLE Study — langtids-effektivitet og sikkerhed bekræftet |
| [30267321](https://pubmed.ncbi.nlm.nih.gov/30267321/) | 2018 | Oversigt | Drugs | "Lanadelumab: First Global Approval" — virkningsmekanisme- og udviklings-sammenfatning |
| [32187470](https://pubmed.ncbi.nlm.nih.gov/32187470/) | 2020 | Oversigt | NEJM | Generel oversigt over arvelig angioødem patofysiologi og behandling |
| [30539362](https://pubmed.ncbi.nlm.nih.gov/30539362/) | 2019 | Oversigt | BioDrugs | Præ-kliniske og Fase I data-oversigt for Lanadelumab i C1-INH-mangel |
| [37898409](https://pubmed.ncbi.nlm.nih.gov/37898409/) | 2024 | Oversigt | J Allergy Clin Immunol | Sygdomsbyrde af HAE pga. C1-inhibitor-mangel i Asien-Stillehavs-regionen |
| [39701274](https://pubmed.ncbi.nlm.nih.gov/39701274/) | 2025 | Observationelt | J Allergy Clin Immunol Pract | INTEGRATED multi-lands real-world-effektivitetstudium |

---

## Markedsinformation for Danmark

Lanadelumab har i øjeblikket **ingen markedsføringstilladelse** i Danmark (0 licenser på fil; markedsstatus: ikke markedsført). Der er ingen nationale (Lægemiddelstyrelsen) eller centraliserede (EMA) godkendelsesoptegnelser tilgængelige i denne evidenspakke.

---

## Sikkerhedshensyn

Se venligst det godkendte produktresumé (SmPC) for sikkerhedsinformation.

---

## Konklusion og næste trin

**Afgørelse: Afvent**

**Begrundelse:**
- En blokkerende datakløft findes (DG001: ingen TFDA/SmPC-advarsler eller kontraindikationer på fil), hvilket forhindrer afslutningen af den indledende sikkerhedsscreening (S1), som kræves før enhver anbefaling om at fortsætte. Dette gælder selv om den underliggende indikation ikke er ny — Lanadelumab er allerede en godkendt HAE-terapi andre steder, understøttet af ét afsluttet placebo-kontrolleret Fase 3 RCT (L2) og omfattende real-world-bevis.

**For at fortsætte, kræves følgende:**
- Officielt SmPC / produktetiket med advarsler, forsigtighedsregler og kontraindikationer (kilde: TFDA eller tilsvarende regulator)
- Formelt virkningsmekanisme-register (MOA) fra DrugBank eller fabrikantmærkning
- Lægemiddel-lægemiddel-vekselvirkning (DDI) data (nuværende forespørgsel returnerede ingen resultater)
- Hvis dansk markedsindgang overvejes: en formelt markedsføringstilladelsesansøgning, da der i øjeblikket ikke findes nogen licens i Danmark
- Afklaring af, at "C1-inhibitor-mangel" afspejler lægemidlets eksisterende godkendte indikation snarere end et nyt repurposing-mål, for at undgå fejltolkning af dette som en ny opdagelse

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

