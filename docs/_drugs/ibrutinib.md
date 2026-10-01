---
layout: default
title: Ibrutinib
parent: Kun modelforudsigelse (L5)
nav_order: 219
evidence_level: L5
indication_count: 10
---

# Ibrutinib
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

# Ibrutinib: Fra uoplyst oprindelig indikation til polyklonal hypergammaglobulinæmi

## Resumé i én sætning

Ibrutinib er en BTK-hæmmer (Brutons tyrosinkinase), men den oprindelige indikation fremgår ikke af datagrundlaget. Modellen TxGNN forudsiger, at lægemidlet kan have effekt ved **polyklonal hypergammaglobulinæmi**, men der er **ingen kliniske forsøg og ingen publikationer** til at understøtte netop denne forudsigelse. Den bedst understøttede forudsigelse i pakken er i stedet **monoklonal paraproteinæmi** (Waldenströms makroglobulinæmi, WM), hvor der er **13 kliniske forsøg** og **20 publikationer**, heriblandt to afsluttede fase 3-forsøg.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Ikke oplyst i datagrundlaget (den danske tilladelse har ingen indikationstekst) |
| Forudsagt ny indikation | Polyklonal hypergammaglobulinæmi |
| TxGNN-forudsigelsesscore | 91,75 % |
| Evidensniveau | L5 (kun modelforudsigelse) |
| Status på det danske marked | Markedsført |
| Antal markedsføringstilladelser | 1 |
| Anbefalet beslutning | Hold |

---

## Hvorfor er forudsigelsen rimelig?

Detaljerede data om virkningsmekanisme (MOA) er ikke tilgængelige i datapakken. Ibrutinib er en BTK-hæmmer. BTK virker nedstrøms for B-cellereceptoren og MYD88/TLR-signalering, og hæmning kan i teorien dæmpe B-celle- og plasmacelleaktivitet og dermed immunglobulinniveauerne.

For **polyklonal hypergammaglobulinæmi** er det mekanistiske argument svagt. Tilstanden er mere et laboratoriefund eller en sekundær manifestation end en selvstændig sygdom, og ibrutinib forbindes oftere med *hypogammaglobulinæmi*. Den høje score (0,92) er derfor sandsynligvis et artefakt fra vidensgrafen.

Samlet overblik over de unikke forudsigelser (nogle optræder to gange i datapakken):

| Forudsagt indikation | Score | Evidensniveau | Anbefaling |
|------|------|------|------|
| Polyklonal hypergammaglobulinæmi | 91,75 % | L5 | Hold |
| Monoklonal paraproteinæmi (WM) | 91,16 % | L1 | Fortsæt med sikkerhedsforanstaltninger |
| MALT-lymfom i skjoldbruskkirtlen | 88,43 % | L5 | Hold |
| MALT-lymfom i tyndtarmen | 88,36 % | L3 | Forskningsspørgsmål |
| Burkitt-lymfom i tyndtarmen | 88,32 % | L4 | Hold |

Forudsigelsen om **monoklonal paraproteinæmi** er mekanistisk direkte. MYD88 L265P-drevet BTK-aktivering er central i WM-biologien. WM er sandsynligvis allerede en godkendt ibrutinib-indikation, og at feltet for oprindelige indikationer er tomt skyldes formentlig en datamangel. Der er altså formentlig ikke tale om et ægte repurposing-kandidatforløb.

For MALT-lymfom bygger rationalet på ibrutinibs kendte aktivitet ved marginalzonelymfom. Skjoldbruskkirtel-MALT behandles ofte lokalt med strålebehandling eller kirurgi, så behovet for en systemisk BTK-hæmmer er begrænset. For Burkitt-lymfom er BTK-hæmning mekanistisk svagere begrundet, da sygdommen er MYC-drevet.

---

## Evidens fra kliniske forsøg

**Polyklonal hypergammaglobulinæmi:** Der er i øjeblikket ingen relaterede kliniske forsøg registreret.

**Monoklonal paraproteinæmi (WM), den bedst understøttede forudsigelse:**

| Forsøgsnummer | Fase | Status | Antal deltagere | Hovedresultater |
|---------|------|------|------|---------|
| [NCT02165397](https://clinicaltrials.gov/study/NCT02165397) | Fase 3 | Afsluttet | 181 | iNNOVATE: randomiseret, dobbeltblindet, placebokontrolleret forsøg med ibrutinib + rituximab ved WM |
| [NCT03053440](https://clinicaltrials.gov/study/NCT03053440) | Fase 3 | Afsluttet | 201 | Zanubrutinib vs. ibrutinib ved MYD88-muteret WM (ASPEN); ibrutinib er aktiv komparator |
| [NCT04061512](https://clinicaltrials.gov/study/NCT04061512) | Fase 2/3 | Rekrutterer | 148 | Rituximab + ibrutinib vs. DRC som førstelinjebehandling ved WM (RAINBOW); resultater foreligger endnu ikke |
| [NCT03620903](https://clinicaltrials.gov/study/NCT03620903) | Fase 2 | Aktiv, ikke rekrutterende | 53 | Bortezomib, rituximab og ibrutinib hos behandlingsnaive WM-patienter |
| [NCT04062448](https://clinicaltrials.gov/study/NCT04062448) | Fase 2 | Afsluttet | 16 | Ibrutinib + rituximab hos japanske WM-patienter; primært endepunkt er samlet responsrate |
| [NCT04840602](https://clinicaltrials.gov/study/NCT04840602) | Fase 2 | Rekrutterer | 92 | BTK-hæmmere (ibrutinib + rituximab eller zanubrutinib) vs. venetoclax + rituximab ved ubehandlet WM/LPL |
| [NCT01479842](https://clinicaltrials.gov/study/NCT01479842) | Fase 1 | Aktiv, ikke rekrutterende | 48 | Dosiseskalering af rituximab og bendamustin med BTK-hæmmer ved recidiverende NHL; blandet B-cellepopulation, så WM-signalet er usikkert |
| [NCT07169565](https://clinicaltrials.gov/study/NCT07169565) | Fase 1 | Ikke rekrutterende endnu | 21 | Ibrutinib efterfulgt af bendamustin + rituximab som tidsbegrænset behandling ved WM; ingen data endnu |
| [NCT02950220](https://clinicaltrials.gov/study/NCT02950220) | Fase 1/1b | Afsluttet | 2 | Pembrolizumab + ibrutinib ved recidiverende/refraktær NHL; meget lille population |
| [NCT05099471](https://clinicaltrials.gov/study/NCT05099471) | Fase 2 | Rekrutterer | 80 | Venetoclax + rituximab ved WM; indeholder ikke ibrutinib og er kun relevant som komparatorlandskab |

Tre øvrige forsøg i pakken vurderes som irrelevante (COVID-19, pirtobrutinib ved CLL, pembrolizumab ved CLL) og er udeladt.

**MALT-lymfom i tyndtarmen og Burkitt-lymfom i tyndtarmen:** Det eneste tilknyttede forsøg er [NCT02109224](https://clinicaltrials.gov/study/NCT02109224), et afsluttet (terminated) fase 1/PK-forsøg med ibrutinib hos hiv-smittede patienter med recidiverende/refraktært B-celle-lymfom (72 deltagere). Evidensen er indirekte og ikke subtypespecifik.

---

## Evidens fra litteraturen

**Polyklonal hypergammaglobulinæmi:** Der findes i øjeblikket ingen relateret litteratur.

**Monoklonal paraproteinæmi (WM):**

| PMID | År | Type | Tidsskrift | Hovedresultater |
|---------|-----|------|------|---------|
| [32731259](https://pubmed.ncbi.nlm.nih.gov/32731259/) | 2020 | RCT | Blood | ASPEN: fase 3-sammenligning af zanubrutinib og ibrutinib ved symptomatisk WM med MYD88 L265P; primært endepunkt var andelen med komplet respons |
| [38315878](https://pubmed.ncbi.nlm.nih.gov/38315878/) | 2024 | Post hoc-analyse af RCT | Blood Advances | Biomarkøranalyse af ASPEN med sekventering af knoglemarv fra patienter behandlet med ibrutinib eller zanubrutinib |
| [39626287](https://pubmed.ncbi.nlm.nih.gov/39626287/) | 2025 | Ad hoc-analyse af RCT | Blood Advances | Perifer neuropati i ASPEN: effekt af zanubrutinib og ibrutinib på neuropatisymptomer |
| [32603202](https://pubmed.ncbi.nlm.nih.gov/32603202/) | 2020 | Review | Expert Opin Pharmacother | Evaluering af ibrutinibs rolle ved WM i lyset af nye genomiske og kliniske fund |
| [33297772](https://pubmed.ncbi.nlm.nih.gov/33297772/) | 2020 | Review | Expert Rev Hematol | Zanubrutinib ved WM; beskriver ibrutinibs etablerede toksicitetsprofil |
| [31591468](https://pubmed.ncbi.nlm.nih.gov/31591468/) | 2019 | Review | Leukemia | Nyt i behandlingen af WM; MYD88 L265P som diagnostisk kendetegn |
| [27825466](https://pubmed.ncbi.nlm.nih.gov/27825466/) | 2016 | Review | Best Pract Res Clin Haematol | Aktuelle behandlingsretningslinjer ved WM |
| [27825468](https://pubmed.ncbi.nlm.nih.gov/27825468/) | 2016 | Review | Best Pract Res Clin Haematol | Nye terapeutiske targets ved WM; fremhæver MYD88 L265P-signalering og ibrutinibs bemærkelsesværdige aktivitet |
| [34170207](https://pubmed.ncbi.nlm.nih.gov/34170207/) | 2021 | Review | Expert Rev Hematol | Håndtering af komplikationer sekundært til WM |
| [29169431](https://pubmed.ncbi.nlm.nih.gov/29169431/) | 2017 | Review | Dtsch Arztebl Int | Monoklonal IgM-gammopati og WM; differentialdiagnostik |

---

## Information om det danske marked

| Markedsføringstilladelsesnummer | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28105995017 | Imbruvica (Janssen-Cilag International NV) | Filmovertrukne tabletter | Ikke oplyst i datagrundlaget |

Administrationsvej: oral.

---

## Cytotoksicitet

| Punkt | Indhold |
|------|------|
| Cytotoksisk klassifikation | Målrettet behandling (BTK-hæmmer) |
| Risiko for myelosuppression | Se produktresuméet (SmPC) om advarsler og forsigtighedsregler |
| Emetogenicitetsklassifikation | Se produktresuméet (SmPC) |
| Monitoreringspunkter | Se produktresuméet (SmPC) |
| Håndteringsbeskyttelse | Se produktresuméet (SmPC) |

---

## Sikkerhedsovervejelser

Datagrundlaget indeholder ingen advarsler, kontraindikationer eller registrerede lægemiddelinteraktioner. Se det godkendte produktresumé (SmPC) for sikkerhedsoplysninger.

Som forholdsregel ved en eventuel videre vurdering for WM bør de BTK-klasserelaterede risici monitoreres: **atrieflimren, blødning og infektion**.

---

## Konklusion og næste skridt

**Beslutning: Hold** (for den primære forudsigelse, polyklonal hypergammaglobulinæmi)

**Begrundelse:**
- Forudsigelsen er kun modelbaseret (L5) uden forsøg eller litteratur, og mekanismen er svag, da ibrutinib oftere forbindes med hypogammaglobulinæmi.
- For **monoklonal paraproteinæmi (WM)** er evidensen stærk (L1, to afsluttede fase 3-forsøg, anbefaling: Fortsæt med sikkerhedsforanstaltninger). WM er dog sandsynligvis allerede en godkendt indikation, så det er næppe et reelt repurposing-spor.

**For at komme videre kræves følgende:**
- Indlæsning og gennemgang af den danske indlægsseddel/SmPC fra Lægemiddelstyrelsen (blokerende datamangel DG001), herunder advarsler og kontraindikationer
- Bekræftelse af den godkendte indikationsstatus i Danmark, herunder om WM allerede er omfattet
- Detaljerede MOA-data fra DrugBank (DG002)
- Afgrænsning til symptomatisk WM, ikke asymptomatisk MGUS/smoldering sygdom
- Overvågningsplan for atrieflimren, blødning og infektion

*Resultaterne er kun til forskningsformål og udgør ikke medicinsk rådgivning. Kandidater til lægemiddelomplacering kræver klinisk validering, før de kan anvendes.*
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

