---
layout: default
title: Pazopanib
parent: Kun modelforudsigelse (L5)
nav_order: 634
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Pazopanib: forudsagt ny indikation Liposarkom (evidensniveau L5). Oprindelig indikation: Nyrecellekarcinom og bløddelssarkom"
monitor_inn: "Pazopanib"
predicted_indications: ["liposarcoma", "liposarcoma"]
---

# Pazopanib
{: .fs-9 }

Evidensniveau: **L5** | Forudsagte indikationer: **10** stk.
{: .fs-6 .fw-300 }

---

## Indholdsfortegnelse
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Farmaceutens vurderingsrapport

</div>

# Pazopanib: Fra nyrecellekarcinom og sarkom til liposarkom

## Resumé

Pazopanib er en tyrosinkinasehæmmer, der oprindeligt anvendes til behandling af nyrecellekarcinom og bløddelssarkom.
TxGNN-modellen forudsiger, at lægemidlet også kan være virksomt ved **liposarkom** (score 99,59 %),
og der foreligger **6 kliniske forsøg** (heraf 2 specifikt i liposarkom) og **20 publikationer** på området.
Det er den forudsigelse med den stærkeste evidens blandt de forudsagte indikationer i de data, der er sammenstillet til denne rapport.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Nyrecellekarcinom og bløddelssarkom (hentet fra videnbasen; indikationsteksten i den danske registrering er tom) |
| Forudsagt ny indikation | Liposarkom |
| TxGNN-forudsigelsesscore | 99,59 % |
| Evidensniveau | L2 (kun fase 2-studier; ingen fase 3 specifikt i liposarkom) |
| Markedsstatus i Danmark | Markedsført |
| Antal markedsføringstilladelser | 1 |
| Anbefalet beslutning | Proceed with Guardrails (fortsæt med forbehold) |

Bemærk: De øvrige forudsagte indikationer (subtyper af nyrecellekarcinom og pædiatrisk nyrecellekarcinom) har enten kun modelforudsigelse (L5, Hold) eller retrospektive data (L3, forskningsspørgsmål). De er kort omtalt til sidst.

---

## Hvorfor er forudsigelsen rimelig?

Data om lægemidlets virkningsmekanisme er ikke tilgængelige i de sammenstillede data. Ud fra almen viden er pazopanib en multi-målrettet hæmmer af VEGFR-1/2/3, PDGFR og c-Kit. Den hæmmer dermed nydannelse af blodkar (angiogenese) og tumorvækst. Lægemidlet har dokumenteret effekt ved nyrecellekarcinom og er allerede godkendt til visse bløddelssarkomer.

Liposarkom er en bløddelssarkom-type, og den antiangiogene mekanisme er derfor biologisk relevant. Der er dog en vigtig begrænsning: Liposarkom (den adipocytiske subtype) blev udelukket fra det afgørende fase 3-studie (PALETTE) på grund af begrænset aktivitet. Fase 2-data, herunder et liposarkomspecifikt studie (PMID 31010343), tyder på nogen aktivitet ved intermediær/højgradigt liposarkom, men resultaterne er beskedne og afhænger af histologisk undertype.

---

## Klinisk evidens

| Forsøgsnummer | Fase | Status | Antal deltagere | Hovedresultater |
|---------|------|------|------|---------|
| [NCT01506596](https://clinicaltrials.gov/study/NCT01506596) | Fase 2 | Afsluttet | 42 | Pazopanib alene ved ikke-opererbart eller metastatisk liposarkom (direkte på indikation) |
| [NCT01692496](https://clinicaltrials.gov/study/NCT01692496) | Fase 2 | Afsluttet | 52 | Aktivitet og tolerabilitet ved fremskreden/metastatisk sarkom efter standardbehandling |
| [NCT02357810](https://clinicaltrials.gov/study/NCT02357810) | Fase 2 | Afsluttet | 178 | Pazopanib med oral topotecan ved metastatiske, ikke-opererbare bløddels- og knoglesarkomer |
| [NCT02180867](https://clinicaltrials.gov/study/NCT02180867) | Fase 2/3 | Afsluttet | 140 | Randomiseret præoperativ behandling (PAZNTIS) ved non-rhabdomyosarkom bløddelssarkom, strålebehandling ± pazopanib |
| [NCT01532687](https://clinicaltrials.gov/study/NCT01532687) | Fase 2 | Afsluttet | 54 | Randomiseret, dobbeltblindet: gemcitabin ± pazopanib ved refraktært bløddelssarkom |
| [NCT06239272](https://clinicaltrials.gov/study/NCT06239272) | Fase 1/2 | Rekrutterer | 139 | Risikotilpasset vedligeholdelsesbehandling med pazopanib ved non-rhabdomyosarkom bløddelssarkom (overvejende børn og unge voksne) |

Kun to af forsøgene (NCT01506596 og NCT01692496) er rettet mod liposarkom eller fremskredne sarkomer med liposarkom som mulig undergruppe. De øvrige er bredere bløddelssarkomstudier, hvor liposarkom muligvis indgår.

---

## Litteraturevidens

| PMID | År | Type | Tidsskrift | Hovedresultater |
|------|-----|------|------|---------|
| [31010343](https://pubmed.ncbi.nlm.nih.gov/31010343/) | 2019 | Fase 2-studie/oversigt | Expert Opin Investig Drugs | Pazopanib ved fremskredent intermediært eller højgradigt liposarkom |
| [28844815](https://pubmed.ncbi.nlm.nih.gov/28844815/) | 2017 | Kommentar | Lancet Oncol | Pazopanib ved fremskredent liposarkom |
| [34050255](https://pubmed.ncbi.nlm.nih.gov/34050255/) | 2021 | Fase 2 | Br J Cancer | Pazopanib med oral topotecan ved metastatiske, ikke-opererbare sarkomer |
| [32026050](https://pubmed.ncbi.nlm.nih.gov/32026050/) | 2020 | Oversigtsartikel | Curr Treat Options Oncol | Systemiske behandlingsmuligheder ved dedifferentieret liposarkom |
| [35609512](https://pubmed.ncbi.nlm.nih.gov/35609512/) | 2022 | Oversigtsartikel | Oncol Res Treat | Etablerede og eksperimentelle behandlinger ved fremskredent liposarkom |
| [37298520](https://pubmed.ncbi.nlm.nih.gov/37298520/) | 2023 | Oversigtsartikel | Int J Mol Sci | Behandling af dedifferentieret liposarkom i immunterapiens tidsalder |
| [28547734](https://pubmed.ncbi.nlm.nih.gov/28547734/) | 2017 | Oversigtsartikel | Adv Ther | Optimal brug af pazopanib, trabectedin og eribulin ved bløddelssarkom |
| [30060824](https://pubmed.ncbi.nlm.nih.gov/30060824/) | 2018 | Præklinisk | Tissue Cell | Pleomorft liposarkom med PDGFRA-amplifikation regredierede på pazopanib i musemodel |
| [36890471](https://pubmed.ncbi.nlm.nih.gov/36890471/) | 2023 | Protokol | BMC Cancer | Randomiseret fase 2-studie (JCOG1802) af trabectedin, eribulin og pazopanib som andenlinjebehandling |
| [27434055](https://pubmed.ncbi.nlm.nih.gov/27434055/) | 2016 | Oversigtsartikel | Cancer | Kemoterapi ved bløddelssarkom |

---

## Markedsinformation i Danmark

| Markedsføringstilladelse | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28106801522 | Pazopanib "Accord" (Accord Healthcare B.V.) | Filmovertrukne tabletter (oral) | Indikationstekst foreligger ikke i de sammenstillede data |

---

## Cytotoksicitet

| Punkt | Indhold |
|------|------|
| Klassifikation | Målrettet behandling (tyrosinkinasehæmmer), ikke konventionel cytotoksisk kemoterapi |
| Myelosuppressionsrisiko | Se produktresuméet (SmPC) |
| Emetogenicitet | Se produktresuméet (SmPC) |
| Monitoreringspunkter | Se produktresuméet (SmPC). Leverfunktion og blodtryk er relevante ud fra den vurdering, der ligger til grund for forbeholdene (se nedenfor) |
| Håndteringsbeskyttelse | Se produktresuméet (SmPC) |

---

## Sikkerhedsovervejelser

Der foreligger ingen produkttekst om advarsler og kontraindikationer i de sammenstillede data. Der henvises til det godkendte produktresumé (SmPC).

**Kontraindikationer fra videnbasen (ikke produkttekst):** Videnbasen angiver bl.a. følgende sygdomme som kontraindikationer eller områder med forsigtighed: hypertension, langt QT-syndrom og torsades de pointes, leversvigt og lægemiddelinduceret leverskade, hyperbilirubinæmi (inkl. Gilberts syndrom), hypothyroidisme, myokardieinfarkt, intracerebral blødning, aktivt mavesår, pancreatitis, proteinuri og diarré. Disse oplysninger bør verificeres mod SmPC.

**Lægemiddelinteraktioner** (100 registreret i alt; udvalgte vist):
- **Alvorlige (Major):** famotidin, ranitidin, cimetidin, omeprazol, esomeprazol, rabeprazol, dexlansoprazol (syrehæmmere kan nedsætte optagelsen), clarithromycin, dolasetron
- **Moderate:** pioglitazon, loperamid, aprepitant, dexamethason, budesonid, bisacodyl, magnesiumoxid, polyethylenglycol, saxagliptin, eliglustat

---

## Konklusion og næste skridt

**Beslutning: Proceed with Guardrails**

**Begrundelse:**
Liposarkom har den stærkeste evidens blandt de forudsagte indikationer (L2, afsluttede fase 2-studier, heriblandt to liposarkomspecifikke). Aktiviteten er dog beskeden og afhænger af undertype, og liposarkom blev udeladt fra det afgørende fase 3-studie.

**For at komme videre kræves:**
- Histologiinformeret patientudvælgelse (fx ikke-dedifferentieret eller ikke-adipocytisk kontekst) og sammenligning med etablerede behandlinger
- Monitorering af levertoksicitet og hypertension
- Gennemgang af resultaterne fra NCT01506596 og NCT01692496 samt indhentning af SmPC for advarsler, kontraindikationer og indikationstekst
- Data om virkningsmekanisme (MOA) fra DrugBank
- Gennemgang af interaktioner, især med syrehæmmere og CYP3A4-hæmmere

---

## Øvrige forudsagte indikationer (kort)

| Forudsagt indikation | TxGNN-score | Evidensniveau | Anbefaling |
|------|------|------|------|
| Ikke-klassificeret nyrecellekarcinom | 99,63 % | L3 | Forskningsspørgsmål: retrospektive kohorter, real-world data og ét enkeltarmet fase 2-studie ved non-clear-cell RCC (fx [PMID 28546525](https://pubmed.ncbi.nlm.nih.gov/28546525/), [PMID 28108284](https://pubmed.ncbi.nlm.nih.gov/28108284/)); ingen randomiserede studier |
| Nyrecellekarcinom med neuroblastom | 99,63 % | L5 | Hold: kun modelforudsigelse |
| Nyrecellekarcinom med Xp11.2/TFE3-fusion | 99,63 % | L5 | Hold: kun modelforudsigelse |
| Nyrecellekarcinom hos børn | 99,54 % | L5 | Hold: kun modelforudsigelse; pædiatrisk sikkerhed og dosering er ikke belyst |

Flere af disse forudsigelser optrådte to gange med identisk indhold i de sammenstillede data og er her kun opført én gang.
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

