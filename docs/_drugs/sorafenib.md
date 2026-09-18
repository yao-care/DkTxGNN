---
layout: default
title: Sorafenib
parent: Høj evidens (L1-L2)
nav_order: 405
evidence_level: L2
indication_count: 10
---

# Sorafenib
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

# Sorafenib: Fra nyrcellekarcinon til liposarkom

*Bemærk: `original_indications` og `original_moa` er tomme/datakløft i denne bevissamling (DG002). "Renal Cell Carcinoma" bruges her kun, fordi det refereres som en allerede godkendt sorafenib-indikation i bevisamlingens egen omformåling (rank 9–10 entries) — dette er ikke uafhængigt verificeret mod et formelt label/SmPC og bør bekræftes før brug.*

## Resumé på en sætning

Sorafenib er en multi-kinase-hæmmer med en godkendt onkologisk indikation ved nyrcellekarcinon (jf. intern reference i denne bevissamling). TxGNN-modellens højest rangerede forudsigelse er **liposarkom**, understøttet af **1 direkte relevant afsluttet fase 2-forsøg** og **8 publikationer**, selv om beviserne forbliver foreløbige og stort set præ-kliniske/indirekte. Ni yderligere kandidatindikationer for sorafenib blev også vurderet i denne samling på lavere evidensniveauer.

## Hurtig oversigt

| Element | Indhold |
|------|------|
| Original indikation | Nyrcellekarcinon (udledt fra intern begrundelse alene — ikke uafhængigt bekræftet; se bemærkning ovenfor) |
| Forudsagt ny indikation | Liposarkom |
| TxGNN-forudsigelsesscore | 99.82% |
| Evidensniveau | L2 |
| Markedsstatus i Danmark | Ikke markedsført |
| Antal markedsføringstilladelser | 0 |
| Anbefalet beslutning | Gå videre med forholdsregler |

## Hvorfor er denne forudsigelse rimelig?

Formelle mekanisme-for-virkning-data for sorafenib er markeret som et datakløft i denne samling (DG002). Den genbrugsbegrundelse, der er knyttet til forudsigelsen, beskriver dog sorafenib som en multi-rettet kinase-hæmmer, der virker på VEGFR-1/2/3, PDGFR-β og RAF/MEK/ERK-signalvejen — dvs. en anti-angiogenetisk og anti-proliferativ mekanisme snarere end en formelt dokumenteret læbelmårkering for virkningsmåde.

Liposarkom og andre bløddelsarkomater afhænger af angiogen og RAS-RAF-MAPK-signalering. Præ-klinisk arbejde inkluderet i denne samling viser, at sorafenib undertrykker MAPK-signalering i dedifferentieret liposarkom- og maligne perifer nerve-sheath tumor-cellelinier (PMID 18413802), og en relateret xenograft-undersøgelse identificerer PTEN-nedjustering som en malignt signatur i dedifferentieret liposarkom forbundet med PI3K-signalvejes-følsomhed (PMID 23416162) — en signalvej, der er mekanistisk tilstødende, men ikke identisk med sorafenibs primære mål.

De stærkeste direkte kliniske beviser er et afsluttet fase 2-forsøg med sorafenib selv (udviklingskode BAY-9006/NSC #724772, NCT00217620) ved avanceret bløddelssarkom, og et separat SWOG-ledet fase 2-enkeltarms-forsøg (PMID 21751200) i samme population. Intet forsøg var begrænset til eller designet specifikt for liposarkom, så det mekanistiske link til denne specifikke histologiske subtype forbliver indirekte snarere end subtypspecifik.

## Klinisk forsøgsbeviser

| Forsøgsnummer | Fase | Status | Rekruttering | Vigtige fund |
|---------|------|------|------|---------|
| [NCT00217620](https://clinicaltrials.gov/study/NCT00217620) | Fase 2 | Afsluttet | 51 | Direkte beviser (Relevansgradé A): testede sorafenib selv (udviklingskode BAY-9006) ved avanceret bløddelssarkom, herunder liposarkom-subtyper. |
| [NCT02048371](https://clinicaltrials.gov/study/NCT02048371) | Fase 2 | Afsluttet | 131 | Indirekte beviser (Relevansgradé C): SARC024 testede regorafenib, ikke sorafenib — samme Bayer multi-kinase-hæmmerklasse, mekanisme-analogi kun, ikke direkte sorafenib-data. |

## Litteraturbeviser

| PMID | År | Type | Journal | Vigtige fund |
|------|-----|------|------|---------|
| [21751200](https://pubmed.ncbi.nlm.nih.gov/21751200/) | 2012 | Fase 2-forsøg (SWOG S0505) | Cancer | Sorafenib evalueret ved avanceret bløddelssarkom, en population med begrænsede terapeutiske muligheder. |
| [24554062](https://pubmed.ncbi.nlm.nih.gov/24554062/) | 2014 | Fase 1-forsøg | Annals of Surgical Oncology | Neoadjuvant konformalt strålebehandling plus sorafenib ved lokalt avanceret ekstremitetsbløddelssarkom. |
| [36003796](https://pubmed.ncbi.nlm.nih.gov/36003796/) | 2022 | Oversigt | Frontiers in Oncology | PDOX-musemodeller af sarkom identificerer effektive kombinationsterapier med CDK-hæmmeren palbociclib. |
| [24712007](https://pubmed.ncbi.nlm.nih.gov/24712007/) | 2014 | Oversigt | Magyar Onkologia | Medicinsk behandling af bløddelsarkomater efter histologisk subtype. |
| [22987955](https://pubmed.ncbi.nlm.nih.gov/22987955/) | 2012 | Oversigt | Annals of Oncology | Histologi- og ikke-histologi-drevet terapi for bløddelsarkomater, herunder liposarkom. |
| [18413802](https://pubmed.ncbi.nlm.nih.gov/18413802/) | 2008 | Præ-klinisk (in vitro/in vivo) | Molecular Cancer Therapeutics | Sorafenib hæmmer MAPK-signalering i MPNST og dedifferentieret liposarkom-cellelinier. |
| [23416162](https://pubmed.ncbi.nlm.nih.gov/23416162/) | 2013 | Præ-klinisk (xenograft) | American Journal of Pathology | Dedifferentieret liposarkom-xenograft-modeller viser PTEN-nedjustering; respons på PI3K-signalvejes-inhibering (ikke direkte sorafenib). |
| [25075796](https://pubmed.ncbi.nlm.nih.gov/25075796/) | 2014 | Casusrapport | Anti-Cancer Drugs | Respons på trabectedin (et andet lægemiddel) ved synovial sarkom med lungemetastaser — begrænset direkte relevans for sorafenib. |

## Markedsinformation for Danmark

Der er ingen markedsføringstilladelsesregistre til stede i denne bevissamling — markedsstatus er registreret som "Ikke markedsført" med i alt 0 licenser.

## Cytotoxicitet

Sorafenib er et antineoplastisk lægemiddel, og dets forudsagte nye indikationer er udelukkende onkologidiagnoser, derfor gælder dette afsnit.

| Element | Indhold |
|------|------|
| Cytotoxicitetsklassifikation | Målrettet terapi (multi-kinase-hæmmer: VEGFR-1/2/3, PDGFR-β, RAF/MEK/ERK — jf. denne samlings begrundelse) |
| Myelosuppression-risiko | Se venligst Produktinformation (SmPC) for advarsler og forsigtighedsregler |
| Emetogenitetsklassifikation | Se venligst Produktinformation (SmPC) for advarsler og forsigtighedsregler |
| Overvågningspunkter | Se venligst Produktinformation (SmPC) for advarsler og forsigtighedsregler |
| Håndteringsbeskyttelse | Se venligst Produktinformation (SmPC) for advarsler og forsigtighedsregler |

## Sikkerhedshensyn

Se venligst den godkendte Produktinformation (SmPC) for sikkerhedsinformation.

## Konklusion og næste trin

**Beslutning: Gå videre med forholdsregler**

**Begrundelse:**
Ét direkte relevant, afsluttet fase 2-forsøg med sorafenib selv ved avanceret bløddelssarkom (herunder liposarkom) plus et andet uafhængigt fase 2-enkeltarms-forsøg giver L2-niveau kliniske beviser, men intet forsøg var specifikt designet til liposarkom-histologi, og det meste af den understøttende litteratur er præ-klinisk eller af en anden tumorsubtype.

**For at gå videre er følgende nødvendigt:**
- Sikkerhedsdata fra SmPC/produktinformation (advarsler, kontraindikationer) — i øjeblikket et blokerende datakløft (DG001)
- Bekræftet virkningsmåde og oprindelige godkendt(e) indikation(er) fra DrugBank/regulatorisk kilde — i øjeblikket et alvorligt datakløft (DG002)
- Liposarkom-subtypespecifik forsøgsdata eller post-hoc subgruppeanalyse fra de eksisterende STS-forsøg
- Lægemiddelinteraktionsdata (DDI) — nuværende forespørgsel gav ingen resultater

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

