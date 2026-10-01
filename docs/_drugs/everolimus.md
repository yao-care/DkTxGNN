---
layout: default
title: Everolimus
parent: Kun modelforudsigelse (L5)
nav_order: 183
evidence_level: L5
indication_count: 10
---

# Everolimus
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

# Everolimus: Fra oprindelig indikation til liposarkom

## Resumé i én sætning

Everolimus er en oral mTOR-hæmmer, der er markedsført i Danmark som Afinitor. Den oprindelige godkendte indikation fremgår ikke af de foreliggende data. TxGNN-modellen forudsiger, at lægemidlet kan have effekt ved **liposarkom** (især dedifferentieret liposarkom). Evidensen er begrænset: **1 klinisk fase 2-forsøg** (kombination med ribociclib) og **4 publikationer**, hvoraf kun 1 er en klinisk rapport.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Ikke angivet i den tilgængelige danske registreringsdata |
| Forudsagt ny indikation | Liposarkom |
| TxGNN-forudsigelsesscore | 99,88 % |
| Evidensniveau | L2 (nærmeste niveau, se bemærkning nedenfor) |
| Status på det danske marked | Markedsført |
| Antal markedsføringstilladelser | 1 |
| Anbefalet beslutning | Hold |

**Bemærkning om evidensniveau:** Det eneste kliniske forsøg er et enkeltarmet fase 2-forsøg, der ikke er afsluttet, og som kombinerer everolimus med ribociclib. Det opfylder derfor ikke strengt kriteriet for L2 (ét afsluttet randomiseret fase 2/3-forsøg). L2 er det nærmeste niveau.

---

## Hvorfor er forudsigelsen rimelig?

Detaljerede data om virkningsmekanismen (MOA) er ikke tilgængelige i Evidence Pack. Everolimus er dog kendt som en hæmmer af mTORC1, en central regulator af cellevækst og proteinsyntese.

Dedifferentieret liposarkom viser aktivering af Akt-mTOR- og MAPK-signalvejene. Dette er beskrevet i en undersøgelse af 99 tumorprøver (PMID 26518767), og sygdommen er desuden kendetegnet ved CDK4-amplifikation. Det biologiske rationale er en dobbelt blokade af CDK4/6 (ribociclib) og mTOR (everolimus), så kompensatorisk PI3K/mTOR-signalering begrænses. Prækliniske modeller har vist synergistisk væksthæmning ved denne kombination.

Den høje TxGNN-score (0,9988) stemmer overens med denne signalvejsforbindelse. Evidensen vedrører dog kombinationen med ribociclib, så everolimus' selvstændige bidrag kan ikke udledes.

**Øvrige forudsigelser fra modellen** (kun beregningsmæssig støtte, ingen forsøg eller litteratur om everolimus):

| Forudsagt indikation | TxGNN-score | Evidensniveau | Anbefaling |
|------|------|------|------|
| Ovarielt myxoidt liposarkom | 99,84 % | L5 | Hold |
| Dermatofibrosarcoma protuberans | 99,82 % | L5 | Hold |
| Parameningeal embryonalt rhabdomyosarkom | 99,77 % | L5 | Hold |
| Botryoid embryonalt rhabdomyosarkom i vagina | 99,76 % | L5 | Hold |

For dermatofibrosarcoma protuberans vedrører den fundne litteratur imatinib og ikke everolimus.

---

## Klinisk evidens fra forsøg

| Forsøgsnummer | Fase | Status | Antal deltagere | Hovedfund |
|---------|------|------|------|---------|
| [NCT03114527](https://clinicaltrials.gov/study/NCT03114527) | Fase 2 | Aktivt, rekrutterer ikke | 48 | Ribociclib + everolimus ved fremskreden dedifferentieret liposarkom (arm A) og leiomyosarkom (arm B) efter mindst 1 tidligere systemisk behandling. Formålet er at bestemme den antitumorale aktivitet. Forventet afslutning: december 2025. |

Der er ikke fundet EudraCT-numre eller ICTRP-forsøg.

---

## Litteraturevidens

| PMID | År | Type | Tidsskrift | Hovedfund |
|------|-----|------|------|---------|
| [37967116](https://pubmed.ncbi.nlm.nih.gov/37967116/) | 2024 | Klinisk fase 2-rapport | Clin Cancer Res | Rapport fra fase 2-forsøget med ribociclib + everolimus ved dedifferentieret liposarkom og leiomyosarkom. Kombinationen er biologisk interessant på grund af synergistisk væksthæmning i tumormodeller. |
| [26518767](https://pubmed.ncbi.nlm.nih.gov/26518767/) | 2016 | Translationel vævsundersøgelse | Tumour Biol | Akt-mTOR- og MAPK-signalvejene er aktiveret i dedifferentieret liposarkom (99 prøver). Supplerende in vitro-studie af en mTOR-hæmmer. |
| [36003796](https://pubmed.ncbi.nlm.nih.gov/36003796/) | 2022 | Review (prækliniske modeller) | Front Oncol | PDOX-musemodeller til at identificere kombinationsbehandlinger med CDK-hæmmeren palbociclib ved sarkomer. Ikke everolimus-specifik. |
| [29848686](https://pubmed.ncbi.nlm.nih.gov/29848686/) | 2018 | Præklinisk | Anticancer Res | Eribulin i kombination med andre kræftlægemidler. Ikke everolimus-specifik; begrænset direkte relevans. |

---

## Information om det danske marked

| Markedsføringstilladelse | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28104388708 | Afinitor (Novartis Europharm Limited) | Tabletter | Ikke angivet i de tilgængelige data |

---

## Cytotoksicitet

| Punkt | Indhold |
|------|------|
| Cytotoksicitetsklassifikation | Målrettet behandling (mTOR-hæmmer), ikke konventionel cytostatika |
| Risiko for myelosuppression | Se produktresuméet (SmPC) |
| Emetogenicitetsklassifikation | Generelt lav; se produktresuméet (SmPC) |
| Monitoreringspunkter | Blodtal med differentialtælling, lever- og nyrefunktion, blodsukker og lipider (generel anbefaling; bekræft i SmPC) |
| Håndteringsbeskyttelse | Følg gældende regler for håndtering af antineoplastiske lægemidler; se produktresuméet (SmPC) |

Der foreligger ikke toksicitetsdata i Evidence Pack. Se advarsler og forsigtighedsregler i produktresuméet (SmPC).

---

## Sikkerhedsovervejelser

Der er ikke fundet interaktioner i den forespurgte interaktionsdatabase. Se det godkendte produktresumé (SmPC) for sikkerhedsoplysninger, herunder advarsler og kontraindikationer.

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
- Den eneste kliniske støtte er et enkeltarmet fase 2-forsøg med en kombination (ribociclib + everolimus), som ikke kan isolere everolimus' effekt. Øvrige forudsigelser støttes kun af modelberegninger.
- Lægemiddelstyrelsens indlægsseddel-/produktresumédata mangler (blokerende datahul), så sikkerhedsscreening kan ikke gennemføres.

**For at komme videre kræves:**
- Publicerede endelige resultater fra NCT03114527 (responsrate, progressionsfri overlevelse, sikkerhed)
- Data fra randomiserede forsøg eller everolimus-monoterapi ved liposarkom
- Download og analyse af produktresuméet fra Lægemiddelstyrelsen (advarsler, kontraindikationer, interaktioner)
- Detaljerede data om virkningsmekanisme fra DrugBank
- Oplysning om den godkendte indikation for Afinitor i Danmark og vurdering af administrationsvejens kompatibilitet

*Resultaterne er kun til forskningsbrug og udgør ikke medicinsk rådgivning. Lægemiddelkandidater til nye anvendelser kræver klinisk validering, før de kan anvendes.*
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

