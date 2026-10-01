---
layout: default
title: Caplacizumab
parent: Kun modelforudsigelse (L5)
nav_order: 89
evidence_level: L5
indication_count: 10
---

# Caplacizumab
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

# Caplacizumab: Fra markedsført anvendelse til forudsagt ny indikation, primær frigivelsesforstyrrelse i blodplader

## Resumé i få sætninger

Caplacizumab er en anti-vWF-nanobody (Cablivi), der er markedsført i Danmark. Det oprindelige godkendte indikationsområde fremgår ikke af datagrundlaget.

TxGNN-modellen rangerer **primær frigivelsesforstyrrelse i blodplader** højest (99,9998 %), men der er **0 kliniske forsøg** og **0 publikationer** for denne forudsigelse. Mekanismen taler desuden imod effekt, fordi caplacizumab kan forværre en blødningsforstyrrelse.

Den eneste forudsagte indikation med solid evidens er **trombotisk trombocytopenisk purpura (TTP)** med **13 kliniske forsøg** og **20 publikationer**. Det er dog en godkendt og retningslinjeanbefalet anvendelse, ikke egentlig lægemiddelomplacering.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Forudsagt ny indikation (rang 1) | Primær frigivelsesforstyrrelse i blodplader |
| TxGNN-forudsigelsesscore | 99,9998 % |
| Evidensniveau (rang 1) | L5 |
| Markedsstatus i Danmark | Markedsført |
| Antal markedsføringstilladelser | 1 |
| Anbefalet beslutning (rang 1) | Hold |
| Evidensniveau for TTP (rang 9) | L1 (iflg. evidence pack) |
| Anbefalet beslutning for TTP | Fortsæt med sikkerhedsforanstaltninger (Proceed with Guardrails) |

De øvrige forudsagte indikationer er pseudo-von Willebrand-sygdom, Glanzmanns trombasteni og Scotts syndrom. Alle har evidensniveau L5 og anbefalingen Hold.

---

## Hvorfor er denne forudsigelse rimelig?

Caplacizumab er et humaniseret nanobody-fragment, der binder vWF's A1-domæne og blokerer vWF's binding til blodpladernes GPIb-receptor. Detaljerede mekanismedata (MOA) er ikke tilgængelige i datagrundlaget. Beskrivelsen her bygger på den mekanistiske vurdering i evidence pack.

**De højest rangerede forudsigelser er mekanistisk problematiske.** Primær frigivelsesforstyrrelse i blodplader, Glanzmanns trombasteni og Scotts syndrom er blødningsforstyrrelser med nedsat blodpladefunktion eller nedsat prokoagulant aktivitet. Caplacizumab hæmmer vWF-medieret blodpladeadhæsion og ville derfor lægge sig oven i den hæmostatiske defekt i stedet for at rette den.

Ved pseudo-von Willebrand-sygdom (blodplade-type VWD) skyldes sygdommen gain-of-function-varianter i GPIb, der øger vWF-binding. Blokade af vWF's A1-domæne er derfor teoretisk plausibel. Men sygdommen præsenterer sig som en blødningstilstand med tab af højmolekylære vWF-multimerer, og caplacizumab medfører selv blødningsrisiko. Den høje score skyldes sandsynligvis netværksnærhed i vidensgrafen mellem blodplade- og vWF-veje (graf-artefakt) og ikke en reel terapeutisk sammenhæng.

**TTP er derimod mekanistisk direkte.** Ved erhvervet TTP efterlader ADAMTS13-mangel ultrastore vWF-multimerer, som driver mikrovaskulær blodpladeaggregation. Caplacizumab blokerer netop denne interaktion.

---

## Kliniske forsøg for den højest rangerede forudsigelse

Der er i øjeblikket ingen relaterede kliniske forsøg registreret for primær frigivelsesforstyrrelse i blodplader.

## Litteratur for den højest rangerede forudsigelse

Der er i øjeblikket ingen relateret litteratur tilgængelig.

---

## Supplerende evidens: Trombotisk trombocytopenisk purpura (TTP, rang 9)

### Kliniske forsøg

| Forsøgsnummer | Fase | Status | Antal deltagere | Hovedpunkter |
|---------|------|------|------|---------|
| [NCT02553317](https://clinicaltrials.gov/study/NCT02553317) | Fase 3 | Afsluttet | 145 | HERCULES: dobbeltblindet, randomiseret, placebokontrolleret forsøg af caplacizumab ved erhvervet TTP |
| [NCT01151423](https://clinicaltrials.gov/study/NCT01151423) | Fase 2 | Afsluttet | 75 | Enkeltblindet, randomiseret, placebokontrolleret forsøg af anti-vWF-nanobody som tillæg til plasmaudskiftning |
| [NCT02878603](https://clinicaltrials.gov/study/NCT02878603) | Fase 3 | Afsluttet | 104 | Post-HERCULES: langtidsopfølgning af sikkerhed og effekt, inkl. gentagen brug |
| [NCT05468320](https://clinicaltrials.gov/study/NCT05468320) | Fase 3 | Afsluttet | 51 | Åbent enkeltarmet forsøg: caplacizumab og immunsuppression uden førstelinje-plasmaudskiftning ved iTTP |
| [NCT04074187](https://clinicaltrials.gov/study/NCT04074187) | Fase 2/3 | Afsluttet | 21 | Åbent forsøg hos japanske patienter; primært mål er forebyggelse af TTP-recidiv |
| [NCT04720261](https://clinicaltrials.gov/study/NCT04720261) | Fase 2 | Afbrudt | 58 | Personaliseret caplacizumab-regime styret af ADAMTS13-aktivitet; begrænset evidens pga. afbrydelse |
| [NCT06291025](https://clinicaltrials.gov/study/NCT06291025) | Ikke angivet | Rekrutterer | 131 | Immunsuppression, caplacizumab og plasmainfusion uden plasmaudskiftning; ingen resultater endnu |
| [NCT05876221](https://clinicaltrials.gov/study/NCT05876221) | Ikke relevant | Afsluttet | 223 | Observationel undersøgelse af blodpladerespons på caplacizumab i klinisk praksis |
| [NCT04985318](https://clinicaltrials.gov/study/NCT04985318) | Ikke relevant | Rekrutterer | 350 | REACT-2020: tysk observationel undersøgelse af effekt i klinisk praksis |
| [NCT05262881](https://clinicaltrials.gov/study/NCT05262881) | Ikke relevant | Ukendt | 50 | ROSCAPLI: italiensk retrospektiv undersøgelse af caplacizumab med plasmaudskiftning og immunsuppression |

Yderligere registrerede forsøg omfatter blandt andet et pædiatrisk retrospektivt studie (NCT05263193, n=4) og flere registre (NCT07205861, NCT06376786).

### Litteratur

| PMID | År | Type | Tidsskrift | Hovedpunkter |
|------|-----|------|------|---------|
| [26863353](https://pubmed.ncbi.nlm.nih.gov/26863353/) | 2016 | RCT | N Engl J Med | Caplacizumab ved erhvervet TTP; adresserer den fortsatte sygelighed trods plasmaudskiftning og immunsuppression |
| [30625070](https://pubmed.ncbi.nlm.nih.gov/30625070/) | 2019 | RCT | N Engl J Med | Behandling af erhvervet TTP med caplacizumab, en anti-vWF-nanobody |
| [32914526](https://pubmed.ncbi.nlm.nih.gov/32914526/) | 2020 | Retningslinje | J Thromb Haemost | ISTH-retningslinjer for behandling af TTP |
| [40533296](https://pubmed.ncbi.nlm.nih.gov/40533296/) | 2025 | Retningslinje (opdatering) | J Thromb Haemost | Fokuseret opdatering 2025 af ISTH-retningslinjerne, omfatter iTTP og kongenit TTP |
| [37045600](https://pubmed.ncbi.nlm.nih.gov/37045600/) | 2023 | Systematisk review og metaanalyse | Expert Rev Hematol | Effekt og sikkerhed af caplacizumab ved TTP; effekten i forskellige populationer er omdiskuteret |
| [40235949](https://pubmed.ncbi.nlm.nih.gov/40235949/) | 2025 | Retrospektiv kohorte | EClinicalMedicine | Capla 1000+: international multicenterkohorte om brug og optimal opstartstidspunkt |
| [38838300](https://pubmed.ncbi.nlm.nih.gov/38838300/) | 2024 | Retrospektiv kohorte | Blood | Behandling af iTTP uden plasmaudskiftning (42 tilfælde, Østrig og Tyskland) |
| [40388146](https://pubmed.ncbi.nlm.nih.gov/40388146/) | 2025 | Review | JAMA | Oversigt over immun-TTP |
| [33540569](https://pubmed.ncbi.nlm.nih.gov/33540569/) | 2021 | Review | J Clin Med | Patofysiologi, diagnostik og behandling af TTP |
| [37689812](https://pubmed.ncbi.nlm.nih.gov/37689812/) | 2023 | Retningslinje | Int J Hematol | Japanske retningslinjer for diagnostik og behandling af TTP 2023 |

---

## Information om det danske marked

| Markedsføringstilladelse | Produktnavn | Lægemiddelform | Producent |
|---------|------|------|-----------|
| 28105912417 | Cablivi | Pulver og solvens til injektionsvæske, opløsning | Ablynx NV |

Godkendt indikationstekst er ikke tilgængelig i datagrundlaget.

---

## Sikkerhedsovervejelser

- **Blødningsrisiko:** Caplacizumab hæmmer vWF-medieret blodpladeadhæsion og medfører blødningsrisiko. Dette er et centralt sikkerhedsaspekt, især ved blødningsforstyrrelser i blodpladerne.
- **Lægemiddelinteraktioner:** Der blev ikke fundet interaktionsdata i datagrundlaget.

Se i øvrigt det godkendte produktresumé (SmPC) for fuldstændige oplysninger om sikkerhed, kontraindikationer og advarsler.

---

## Konklusion og næste skridt

**Beslutning for de højest rangerede forudsigelser (primær frigivelsesforstyrrelse i blodplader, pseudo-von Willebrand-sygdom, Glanzmanns trombasteni, Scotts syndrom): Hold**

**Begrundelse:**
- Forudsigelserne har kun modelgrundlag (L5) uden kliniske forsøg eller litteratur.
- Mekanismen taler imod terapeutisk nytte og rejser en sikkerhedsbekymring, fordi caplacizumab kan forværre blødningsfænotypen.

**Beslutning for TTP: Fortsæt med sikkerhedsforanstaltninger (Proceed with Guardrails)**

**Begrundelse:**
- Evidensen er stærk, herunder et fase 3 RCT (HERCULES), langtidsopfølgning og internationale retningslinjer. Anvendelsen er dog allerede godkendt og retningslinjeanbefalet og udgør derfor ikke egentlig omplacering.
- Sikkerhedsforanstaltninger: overvågning af blødningsrisiko samt anvendelse sammen med plasmaudskiftning og immunsuppression under ADAMTS13-monitorering.

**For at komme videre kræves følgende:**
- Indhentning af produktresumé og indlægsseddel fra Lægemiddelstyrelsen (advarsler, kontraindikationer), da sikkerhedsdata mangler.
- Detaljerede data om virkningsmekanisme (MOA), f.eks. fra DrugBank.
- Afklaring af det oprindelige godkendte indikationsområde, som mangler i datagrundlaget.

*Resultaterne er udelukkende til forskningsbrug og udgør ikke medicinsk rådgivning. Forudsagte indikationer kræver klinisk validering, før de kan anvendes.*
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

