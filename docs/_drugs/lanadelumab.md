---
layout: default
title: Lanadelumab
parent: Kun modelforudsigelse (L5)
nav_order: 255
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

# Lanadelumab: Forudsagt indikation C1-inhibitormangel (hereditært angioødem)

## Resumé

Lanadelumab er et fuldt humant monoklonalt antistof, der hæmmer plasmakallikrein. Det markedsføres i Danmark som Takhzyro. Datapakken angiver ingen oprindelig indikation, men litteraturen beskriver stoffet som forebyggende behandling af anfald af hereditært angioødem (HAE).
TxGNN-modellen forudsiger **C1-inhibitormangel** som den højest rangerede indikation. Forudsigelsen understøttes af **22 kliniske forsøg** og **20 publikationer**, herunder et randomiseret, placebokontrolleret fase 3-forsøg. Der er derfor ikke tale om reel nyanvendelse, men om en dokumenteret og markedsført anvendelse.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Forudsagt ny indikation | C1-inhibitormangel (hereditært angioødem) |
| TxGNN-forudsigelsesscore | 99,996 % |
| Evidensniveau | L1 ifølge Evidence Pack (se note nedenfor) |
| Status på det danske marked | Markedsført |
| Antal markedsføringstilladelser | 1 |
| Anbefalet beslutning | Fortsæt med sikkerhedsforanstaltninger (Proceed with Guardrails) |

*Note om evidensniveau: Evidence Pack angiver L1. Der er dog kun identificeret ét randomiseret fase 3-forsøg (HELP). Efter strengt læst niveaudefinition (≥2 gennemførte fase 3-RCT'er) svarer det til L2. Den øvrige fase 3-evidens består af åbne forlængelses- og enkeltarmsstudier.*

---

## Hvorfor er forudsigelsen rimelig?

Detaljerede data om virkningsmekanisme (MOA) fra DrugBank foreligger ikke i datapakken. Ifølge litteraturen (bl.a. "Lanadelumab: First Global Approval") er lanadelumab et monoklonalt antistof, der hæmmer plasmakallikrein.

Ved C1-inhibitormangel (hereditært angioødem) er kallikrein-kinin-systemet ukontrolleret aktiveret. Det giver øget dannelse af bradykinin, en vasodilator, og dermed tilbagevendende hævelsesanfald i huden, mave-tarm-kanalen og de øvre luftveje. Når plasmakallikrein hæmmes, rammes sygdomsmekanismen direkte, hvilket gør forudsigelsen biologisk plausibel.

Forsøgsdataene bekræfter dette. Det pivotale HELP-forsøg (fase 3, randomiseret, dobbeltblindet, placebokontrolleret) undersøgte forebyggelse af anfald hos patienter med HAE type I og II. Forudsigelsen afspejler dermed en etableret og markedsført anvendelse.

---

## Evidens fra kliniske forsøg

Der er identificeret 22 forsøg. De 10 mest relevante er vist her.

| Forsøgsnummer | Fase | Status | Antal deltagere | Hovedpunkter |
|---------|------|------|------|---------|
| [NCT02586805](https://clinicaltrials.gov/study/NCT02586805) | Fase 3 | Gennemført | 125 | HELP: randomiseret, dobbeltblindet, placebokontrolleret forsøg med forebyggelse af anfald ved HAE type I/II |
| [NCT02741596](https://clinicaltrials.gov/study/NCT02741596) | Fase 3 | Gennemført | 212 | HELP-forlængelse: åbent langtidsstudie af sikkerhed og effekt i samme population |
| [NCT04070326](https://clinicaltrials.gov/study/NCT04070326) | Fase 3 | Gennemført | 21 | SPRING: åbent studie af sikkerhed, farmakokinetik og farmakodynamik hos børn på 2 til <12 år |
| [NCT04180163](https://clinicaltrials.gov/study/NCT04180163) | Fase 3 | Gennemført | 12 | Åbent studie af effekt og sikkerhed hos japanske HAE-patienter (type I/II) |
| [NCT05460325](https://clinicaltrials.gov/study/NCT05460325) | Fase 3 | Gennemført | 20 | Åbent studie af sikkerhed, farmakokinetik og effekt hos kinesiske HAE-patienter (26 ugers behandling) |
| [NCT04687137](https://clinicaltrials.gov/study/NCT04687137) | Fase 3 | Gennemført | 12 | Japansk udvidet adgangsprogram (expanded access) for HAE-patienter |
| [NCT04444895](https://clinicaltrials.gov/study/NCT04444895) | Fase 3 | Gennemført | 73 | Åbent langtidsstudie ved ikke-histaminerg angioødem med normal C1-inhibitor (anden population end C1-inhibitormangel) |
| [NCT04130191](https://clinicaltrials.gov/study/NCT04130191) | Ikke relevant | Gennemført | 140 | ENABLE: prospektivt observationelt studie af langtidseffekt i klinisk praksis |
| [NCT03845400](https://clinicaltrials.gov/study/NCT03845400) | Ikke relevant | Gennemført | 168 | EMPOWER: observationelt studie med sammenligning af anfaldsrate før og efter lanadelumab (USA og Canada) |
| [NCT04861090](https://clinicaltrials.gov/study/NCT04861090) | Ikke relevant | Gennemført | 207 | Retrospektivt journalstudie af klinisk effekt og behandlingsforløb i den virkelige verden |

---

## Litteraturevidens

| PMID | År | Type | Tidsskrift | Hovedpunkter |
|------|-----|------|------|---------|
| [30480729](https://pubmed.ncbi.nlm.nih.gov/30480729/) | 2018 | RCT | JAMA | Lanadelumab versus placebo til forebyggelse af HAE-anfald (HELP-forsøget) |
| [34287942](https://pubmed.ncbi.nlm.nih.gov/34287942/) | 2022 | Åben forlængelse | Allergy | HELP OLE: langtidseffekt og sikkerhed hos patienter ≥12 år med HAE type I/II |
| [39508959](https://pubmed.ncbi.nlm.nih.gov/39508959/) | 2024 | Systematisk review | Clin Rev Allergy Immunol | Gennembrudsanfald hos HAE-patienter i langtidsprofylakse |
| [40434599](https://pubmed.ncbi.nlm.nih.gov/40434599/) | 2025 | Netværksmetaanalyse | Drugs in R&D | Sammenligning af effekt, sikkerhed og livskvalitet for langtidsprofylakse ved HAE (bl.a. garadacimab, lanadelumab, berotralstat, subkutan C1INH) |
| [39701274](https://pubmed.ncbi.nlm.nih.gov/39701274/) | 2025 | Observationelt studie | J Allergy Clin Immunol Pract | INTEGRATED: multinational effektivitet i den virkelige verden |
| [39836016](https://pubmed.ncbi.nlm.nih.gov/39836016/) | 2025 | Indirekte sammenligning | J Comp Eff Res | Lanadelumab versus C1-esterasehæmmer hos børn med HAE under 12 år |
| [33556593](https://pubmed.ncbi.nlm.nih.gov/33556593/) | 2021 | Case-serie | J Allergy Clin Immunol Pract | Effekt af lanadelumab ved erhvervet angioødem med C1-inhibitormangel |
| [36379410](https://pubmed.ncbi.nlm.nih.gov/36379410/) | 2023 | Case-studie | J Allergy Clin Immunol Pract | Effekt af lanadelumab ved angioødem på grund af erhvervet C1-inhibitormangel |
| [32187470](https://pubmed.ncbi.nlm.nih.gov/32187470/) | 2020 | Review | N Engl J Med | Oversigt over hereditært angioødem |
| [30267321](https://pubmed.ncbi.nlm.nih.gov/30267321/) | 2018 | Review | Drugs | Lanadelumab: første globale godkendelse. Beskriver kallikrein-hæmning og forebyggelse af HAE-anfald |

---

## Information om det danske marked

| Markedsføringstilladelsesnummer | Produktnavn | Lægemiddelform | Indehaver |
|---------|------|------|-----------|
| 28106091818 | Takhzyro | Injektionsvæske, opløsning, hætteglas | Takeda Pharmaceuticals International AG Ireland Branch |

Indikationsteksten for tilladelsen er ikke tilgængelig i datapakken. Den godkendte indikation i Danmark bør derfor bekræftes i produktresuméet (SmPC).

---

## Sikkerhedsovervejelser

Se det godkendte produktresumé (SmPC) for sikkerhedsoplysninger. Der er ikke fundet registrerede lægemiddelinteraktioner i datapakken.

---

## Konklusion og næste skridt

**Beslutning: Fortsæt med sikkerhedsforanstaltninger (Proceed with Guardrails)**

**Begrundelse:**
Hovedforudsigelsen om C1-inhibitormangel understøttes af et randomiseret, placebokontrolleret fase 3-forsøg (HELP), flere åbne fase 3-studier og omfattende observationelle data. Lægemidlet er markedsført i Danmark. Der er derfor tale om en dokumenteret anvendelse snarere end nyanvendelse.

De øvrige forudsigelser har kun modelgrundlag (L5) og ingen forsøg eller litteratur. De anbefales sat på **Hold** (Hold):
- serpinopati med toksisk serpinpolymerisering
- pankreatitis
- pseudo-von Willebrands sygdom
- primær frigivelsesforstyrrelse af trombocytter

For de to blødningsforstyrrelser er der ingen plausibel mekanistisk sammenhæng med kallikrein-hæmning. De er sandsynligvis artefakter fra vidensgrafen.

**For at komme videre kræves:**
- Bekræftelse af den godkendte indikation og produktresuméet for Takhzyro hos Lægemiddelstyrelsen. Advarsler og kontraindikationer mangler i datapakken.
- Detaljerede data om virkningsmekanisme fra DrugBank.
- Forsigtig tolkning af evidensen for erhvervet C1-inhibitormangel, som kun består af case-niveau data.
- Særskilt sikkerhedsvurdering ved eventuel anvendelse hos patienter med blødningsforstyrrelser, da lanadelumab er kendt for at påvirke aPTT-analyser.

*Resultaterne er udelukkende til forskningsbrug og udgør ikke medicinsk rådgivning. Forudsigelser fra TxGNN skal valideres klinisk, før de kan anvendes.*
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

