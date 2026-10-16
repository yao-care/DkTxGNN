---
layout: default
title: Memantine
parent: Kun modelforudsigelse (L5)
nav_order: 528
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-14
description: "Memantine: forudsagt ny indikation Migræne (migraine disorder) (evidensniveau L5). Oprindelig indikation: Ikke angivet i de indsamlede data (almen viden: Alzheimers demens…"
monitor_inn: "memantine"
predicted_indications: ["pulmonary hypertension", "migraine disorder", "kyphoscoliotic heart disease", "migraine with brainstem aura"]
---

# Memantine
{: .fs-9 }

Evidensniveau: **L5** | Forudsagte indikationer: **4** stk.
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

# Memantin: Fra demens (Alzheimers sygdom) til migræne

## Resumé i én sætning

Memantin er en NMDA-receptorantagonist, som i Danmark er godkendt som filmovertrukne tabletter (Axura). Godkendelsesteksten for indikationen indgår ikke i de data, der er indsamlet til denne rapport. TxGNN-modellen forudsiger, at memantin kan have effekt ved **migræne** (rang 2 blandt forudsigelserne), og forudsigelsen understøttes af **1 fase 3-studie** og **19 publikationer**, herunder metaanalyser af randomiserede forsøg.

*Bemærkning: Memantins oprindelige indikation fremgår ikke af de indsamlede data. Titlen og den oprindelige indikation i oversigten bygger derfor på almen faglig viden (moderat til svær Alzheimers demens) og bør verificeres mod produktresuméet.*

Forudsigelsen med højest score er pulmonal hypertension (99,5 %), men den er kun modelbaseret og uden understøttende studier. Rapporten fokuserer derfor på migræne, som har den stærkeste evidens.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Ikke angivet i de indsamlede data (almen viden: Alzheimers demens, skal verificeres) |
| Forudsagt ny indikation | Migræne (migraine disorder) |
| TxGNN-forudsigelsesscore | 99,52 % |
| Evidensniveau | L1 (et gennemført fase 3-RCT samt metaanalyser; styrken er begrænset af lille stikprøve) |
| Markedsstatus i Danmark | Markedsført |
| Antal markedsføringstilladelser | 1 |
| Anbefalet beslutning | Proceed with Guardrails |

---

## Hvorfor er denne forudsigelse rimelig?

Detaljerede data om virkningsmekanisme er ikke tilgængelige i de indsamlede data. Memantin er imidlertid kendt som en NMDA-receptorantagonist, der dæmper glutamaterg signalering.

Glutamat og NMDA-receptorer spiller en rolle i migrænens patofysiologi, herunder kortikal spreading depression og central sensitisering. Hos migrænepatienter er glutamatniveauerne forhøjede i hjernen og muligvis i blodet, især under anfald. Blokade af NMDA-receptorer kan derfor teoretisk reducere kortikal hyperexcitabilitet og smertefølsomhed.

Evidensen er dog ikke entydig. En kommentar i tidsskriftet *Headache* beskriver evidensen som "stort løfte, men lidt evidens". Studiernes størrelse og placebokontrol bør derfor vurderes kritisk.

Til sammenligning har forudsigelsen om pulmonal hypertension ikke noget dokumenteret mekanistisk grundlag i de fundne data, og forudsigelsen om kyfoskoliotisk hjertesygdom er sandsynligvis en modelartefakt. Forudsigelsen om migræne med hjernestammeaura støttes kun indirekte af et placebokontrolleret studie i migræne uden aura.

---

## Klinisk evidens

| Forsøgsnummer | Fase | Status | Antal deltagere | Hovedresultater |
|---------|------|------|------|---------|
| [NCT04698525](https://clinicaltrials.gov/study/NCT04698525) | Fase 3 | Afsluttet | 33 | Memantin sammenlignet med natriumvalproat som forebyggende behandling af episodisk migræne. Direkte relevant, men lille og med aktivt sammenligningsstof frem for placebo. |

---

## Litteraturevidens

| PMID | År | Type | Tidsskrift | Hovedresultater |
|------|-----|------|------|---------|
| [33961371](https://pubmed.ncbi.nlm.nih.gov/33961371/) | 2021 | Metaanalyse af RCT'er | Clin Neuropharmacol | Vurderer memantin versus placebo hos migrænepatienter; effekten betegnes som omdiskuteret |
| [26638119](https://pubmed.ncbi.nlm.nih.gov/26638119/) | 2016 | RCT (placebokontrolleret) | Headache | Memantin som forebyggelse af migræne uden aura |
| [34352118](https://pubmed.ncbi.nlm.nih.gov/34352118/) | 2021 | Systematisk review | Headache | Effekt og sikkerhed af memantin som forebyggende behandling af episodisk migræne |
| [40978493](https://pubmed.ncbi.nlm.nih.gov/40978493/) | 2025 | Netværksmetaanalyse | Front Pharmacol | Sammenligning af orale forebyggende migrænemidler hos voksne (18-65 år) |
| [36869904](https://pubmed.ncbi.nlm.nih.gov/36869904/) | 2023 | Review | Naunyn-Schmiedebergs Arch Pharmacol | Memantin og ketamin som potentielle anti-migrænemidler |
| [25159002](https://pubmed.ncbi.nlm.nih.gov/25159002/) | 2014 | Review | Ann Pharmacother | Data om effekt og sikkerhed af memantin til forebyggelse af primære hovedpinelidelser |
| [34510445](https://pubmed.ncbi.nlm.nih.gov/34510445/) | 2021 | Kommentar | Headache | "Stort løfte, men lidt evidens" |
| [17901918](https://pubmed.ncbi.nlm.nih.gov/17901918/) | 2007 | Retrospektiv undersøgelse (60 tilfælde) | J Headache Pain | Retrospektiv vurdering af memantin som forebyggende behandling ved hyppig migræne |
| [39467289](https://pubmed.ncbi.nlm.nih.gov/39467289/) | 2024 | Klinisk retningslinje | Ann Intern Med | VA/DoD-retningslinje for behandling og forebyggelse af migræne og spændingshovedpine |
| [29508147](https://pubmed.ncbi.nlm.nih.gov/29508147/) | 2018 | Review | Neurotherapeutics | Glutamat og dets receptorer som terapeutiske mål ved migræne |

---

## Information om markedet i Danmark

| Markedsføringstilladelsesnummer | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28103161800 | Axura (Merz Pharma GmbH & Co. KGaA) | Filmovertrukne tabletter (oral) | Indikationstekst ikke tilgængelig i de indsamlede data |

---

## Sikkerhedsovervejelser

- **Kontraindikationer fra vidensgraf (ikke produkttekst):** TxGNN-vidensgrafen angiver kontraindikation-relationer med leversygdom, galdeblæresygdom og nedsat nyrefunktion. Disse stammer ikke fra produktresuméet og skal verificeres.
- **Lægemiddelinteraktioner:** Der er registreret 122 interaktioner. Blandt de fremhævede er følgende af moderat grad, hovedsageligt antikolinerge midler: hyoscyamin, atropin, glycopyrronium, clidinium, dicyclomin, methscopolamin, propantelin, scopolamin, trospium og mepenzolat. Mindre interaktioner omfatter ranitidin, metformin, cimetidin og kaliumcitrat.

Se i øvrigt det godkendte produktresumé (SmPC) for fuldstændige oplysninger om advarsler og kontraindikationer.

---

## Konklusion og næste skridt

**Beslutning: Proceed with Guardrails** (for migræne)

**Begrundelse:**
Der foreligger et afsluttet fase 3-RCT, et placebokontrolleret RCT i migræne uden aura samt flere metaanalyser, hvilket giver et rimeligt grundlag for yderligere vurdering. Det direkte fase 3-studie er dog lille (n=33) med aktivt sammenligningsstof, og evidensen beskrives i litteraturen som begrænset. Forudsigelserne om pulmonal hypertension og kyfoskoliotisk hjertesygdom bør afvente (Hold), da de ikke understøttes af data.

**For at komme videre kræves:**
- Hentning og gennemgang af produktresuméet (advarsler, kontraindikationer og godkendt indikation), da disse data mangler
- Data om virkningsmekanisme fra DrugBank
- Gennemgang af effektstørrelser i metaanalyserne (de indsamlede data indeholder ikke resultattal)
- Større placebokontrollerede forsøg for at bekræfte effekt og dosering ved migræne
- Subtypespecifik bekræftelse, hvis migræne med hjernestammeaura skal vurderes
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

