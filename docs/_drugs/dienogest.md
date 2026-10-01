---
layout: default
title: Dienogest
parent: Moderat evidens (L3-L4)
nav_order: 143
evidence_level: L4
indication_count: 10
---

# Dienogest
{: .fs-9 }

Evidensniveau: **L4** | Forudsagte indikationer: **10** stk.
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

# Dienogest: Fra endometriose-behandling til amenorré (Hold)

## Resumé i få linjer

Dienogest er et gestagen i tabletform, og kliniske studier bruger det primært mod endometriose. Godkendelsesdata for det danske præparat oplyser dog ikke en indikationstekst. TxGNN-modellen forudsiger, at det kan have effekt ved **amenorré**, men der er **ingen kliniske studier med amenorré som behandlingsmål**, og de 4 registrerede studier handler alle om endometriose. Amenorré er sandsynligvis en kendt *virkning* af dienogest og ikke en sygdom, det behandler. Forudsigelsen er derfor sandsynligvis en artefakt i vidensgrafen.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Ikke angivet i godkendelsesdata (de kliniske studier omhandler endometriose) |
| Forudsagt ny indikation | Amenorré |
| TxGNN-score | 99,71 % |
| Evidensniveau | L4 |
| Status på det danske marked | Markedsført |
| Antal markedsføringstilladelser | 1 |
| Anbefalet beslutning | Hold |

---

## Hvorfor er forudsigelsen (ikke) rimelig?

Detaljerede data om virkningsmekanisme er ikke tilgængelige i datagrundlaget. Dienogest er et progestin, der hæmmer ovulation og giver decidualisering og atrofi af endometriet. Det er velkendt, at behandlingen kan give amenorré eller blødningsforandringer.

Netop derfor er koblingen tvivlsom. Amenorré er en *effekt* af lægemidlet og ikke et behandlingsmål. Vidensgrafen har sandsynligvis opfanget et lægemiddelinduceret fænotypetræk frem for en egentlig terapeutisk sammenhæng. Da lægemidlets oprindelige virkningsmekanisme mangler i input, har koblingen ikke kunnet kontrolleres mod den.

---

## Evidens fra kliniske studier

| Studienummer | Fase | Status | Antal deltagere | Hovedpunkter |
|---------|------|------|------|---------|
| [NCT07164183](https://clinicaltrials.gov/study/NCT07164183) | Fase 3 | Rekrutterer | 290 | Åbent, randomiseret non-inferioritetsstudie: Indinol Forto 200 mg vs. Visanne 2 mg ved endometriose. Indirekte evidens. |
| [NCT02425462](https://clinicaltrials.gov/study/NCT02425462) | Ikke angivet | Afsluttet | 895 | Observationel kohorte: livskvalitet og langtidssikkerhed ved dienogest hos asiatiske kvinder med endometriose. |
| [NCT04495855](https://clinicaltrials.gov/study/NCT04495855) | Ikke angivet | Afsluttet | 968 | Observationelt "real-world"-studie af dienogest ved endometriose. Amenorré indgår højst som blødningsmønster. |
| [NCT07204093](https://clinicaltrials.gov/study/NCT07204093) | Ikke angivet | Aktivt, rekrutterer ikke | 138 | Transdermal østradiol sammen med dienogest vs. drospirenon ved endometriose. Handler ikke om behandling af amenorré. |

Ingen af studierne undersøger amenorré som sygdom.

---

## Litteraturevidens

| PMID | År | Type | Tidsskrift | Hovedpunkter |
|------|-----|------|------|---------|
| [39090694](https://pubmed.ncbi.nlm.nih.gov/39090694/) | 2024 | Systematisk review/meta-analyse | BMC Pharmacol Toxicol | Bayesiansk oversigt over bivirkninger ved dienogest ved endometriose og adenomyose. |
| [34405378](https://pubmed.ncbi.nlm.nih.gov/34405378/) | 2022 | Review | Rev Endocr Metab Disord | Endokrin baggrund for hormonbehandling af endometriose. |
| [29161960](https://pubmed.ncbi.nlm.nih.gov/29161960/) | 2018 | Kohortestudie | Reprod Sci | Retrospektiv kohorte (514 kvinder) om langtidseffekt og sikkerhed af dienogest ved ovarie-endometriom. |
| [41329046](https://pubmed.ncbi.nlm.nih.gov/41329046/) | 2026 | Klinisk/farmakodynamisk studie | Eur J Contracept Reprod Health Care | Høj hæmningsratio og transformationsindeks for 2 mg dienogest. Amenorré nævnes som mål for hormonbehandling af endometriose. |
| [40543564](https://pubmed.ncbi.nlm.nih.gov/40543564/) | 2025 | Review | J Pediatr Adolesc Gynecol | Avanceret visualisering af müllerske anomalier. Kun løst relateret. |
| [34918698](https://pubmed.ncbi.nlm.nih.gov/34918698/) | 2021 | Case report | Medicine | Granulosacelletumor hos patient med PCOS. Kun løst relateret. |

Ingen publikationer viser, at dienogest behandler amenorré.

---

## Øvrige forudsagte indikationer

| Forudsagt indikation | TxGNN-score | Evidensniveau | Vurdering |
|------|------|------|------|
| Primær ovariel insufficiens | 99,69 % | L4 | Ingen troværdig mekanisme. Dienogest sænker østradiol og hæmmer hypothalamus-hypofyse-ovarie-aksen, så hypoøstrogenismen kan forværres. Det eneste studie ([NCT04306276](https://clinicaltrials.gov/study/NCT04306276), 140 deltagere) er forbehandling før IVF ved endometriose. |
| Fibrocystisk brystsygdom | 99,60 % | L4 | Biologisk plausibelt (gestagener er antiproliferative i brystvæv). Kun en narrativ oversigt fra 2009 ([PMID 19499407](https://pubmed.ncbi.nlm.nih.gov/19499407/)) med en pilotobservation hos 21 kvinder, og ingen klinisk studie. |
| Isoleret væksthormonmangel | 99,53 % | L5 | Ingen mekanistisk begrundelse, kun modelprædiktion. |
| Symptomatisk fragilt X-syndrom hos kvindelig bærer | 99,46 % | L5 | Ingen direkte begrundelse. Kun en mulig indirekte kobling via ovariel dysfunktion hos FMR1-præmutationsbærere, uden støtte i data. |

---

## Information om det danske marked

| Markedsføringstilladelse | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28106335019 | Dienogest "Besins" (Laboratoires Besins Int. S.A.S.) | Tabletter (oral) | Ikke angivet i data |

---

## Sikkerhedsovervejelser

Se det godkendte produktresumé (SmPC) for sikkerhedsoplysninger. Der er ikke fundet oplysninger om interaktioner i datagrundlaget.

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
- Der er ingen direkte evidens for dienogest som behandling af amenorré, og alle studier handler om endometriose. Amenorré er sandsynligvis en kendt virkning af lægemidlet, og forudsigelsen er sandsynligvis en vidensgraf-artefakt.
- Evidensniveauet er L4 (de øvrige forudsigelser L4–L5), og sikkerhedsscreening kan ikke gennemføres uden produktresuméet.

**For at komme videre kræves:**
- Hentning og gennemgang af produktresuméet fra Lægemiddelstyrelsen (advarsler og kontraindikationer).
- Data om virkningsmekanisme, f.eks. fra DrugBank.
- Afklaring af, om amenorré her er en bivirkning/effekt eller et reelt behandlingsmål. Der skal i givet fald være direkte kliniske studier med amenorré som endepunkt.
- Særskilt sikkerhedsvurdering (risiko for forværret hypoøstrogenisme) før en eventuel videre vurdering af primær ovariel insufficiens.

*Resultaterne er kun til forskningsbrug og udgør ikke medicinsk rådgivning. Forudsigelserne kræver klinisk validering.*
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

