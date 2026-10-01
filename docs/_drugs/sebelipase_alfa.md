---
layout: default
title: Sebelipase Alfa
parent: Kun modelforudsigelse (L5)
nav_order: 395
evidence_level: L5
indication_count: 10
---

# Sebelipase Alfa
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

# Sebelipase alfa: Fra LAL-mangel (Kanuma) til forudsagte indikationer

## Resumé

Sebelipase alfa er et rekombinant humant lysosomalt syrelipase-enzym (Kanuma), som bruges som enzymerstatningsterapi. Det oprindelige godkendte indikationsfelt er ikke registreret i det danske datagrundlag.
TxGNN-modellen forudsiger fem sygdomme, og de ti poster i evidenspakken svarer til disse fem, fordi hver forekommer to gange. Kun de to LAL-D-relaterede forudsigelser, **kolesterylesterlagringssygdom** og **Wolmans sygdom**, er biologisk plausible. De understøttes af **8 kliniske forsøg** og **19 publikationer** (kolesterylesterlagringssygdom). Disse to er i praksis allerede godkendte indikationer og ikke ægte repurposing. De tre øvrige forudsigelser (Scheies syndrom, Hurlers syndrom og en STAT5B-relateret sygdom) er sandsynligvis artefakter i vidensgrafen.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Ikke angivet i de danske licensdata. Præparatet er markedsført som enzymerstatning ved lysosomal syrelipase-mangel (LAL-D) |
| Forudsagt ny indikation (højeste score) | Scheies syndrom |
| TxGNN-forudsigelsesscore | 99,80 % (Scheies syndrom) |
| Evidensniveau | L5 for Scheies syndrom. Bedst understøttede forudsigelse: L1 (kolesterylesterlagringssygdom) |
| Status på det danske marked | Markedsført |
| Antal markedsføringstilladelser | 1 |
| Anbefalet beslutning | Hold for Scheies syndrom. Proceed with Guardrails for de LAL-D-relaterede forudsigelser |

### Oversigt over de unikke forudsigelser

| Forudsagt sygdom | Score | Evidensniveau | Anbefaling |
|------|------|------|------|
| Scheies syndrom | 99,80 % | L5 | Hold |
| Hurlers syndrom | 99,79 % | L4 | Hold |
| Væksthormoninsensitivitetssyndrom med immundysregulering 2 (autosomal dominant) | 99,75 % | L5 | Hold |
| Kolesterylesterlagringssygdom | 99,72 % | L1 | Proceed with Guardrails |
| Wolmans sygdom (med hypolipoproteinæmi og akantocytose) | 99,72 % | L3 | Proceed with Guardrails |

---

## Hvorfor er forudsigelsen rimelig?

Der foreligger i øjeblikket ingen detaljerede data om virkningsmekanismen i evidenspakken. Sebelipase alfa er dog rekombinant humant lysosomalt syrelipase (LAL). Enzymet erstatter det manglende enzym og nedbryder kolesterylestere og triglycerider, som ophobes i lysosomerne ved LAL-D.

**Kolesterylesterlagringssygdom og Wolmans sygdom** er henholdsvis den senere debuterende og den svære spædbarnsform af LAL-D. Mekanismen er direkte enzymerstatning, og lægemidlet er markedsført til netop denne sygdom. At indikationen mangler i feltet for oprindelige indikationer skyldes et datahul, ikke et reelt repurposing-fund. Wolman-noden hedder "med hypolipoproteinæmi og akantocytose", hvilket kan være en ontologivariant. Koblingen til klassisk Wolmans sygdom bør derfor kontrolleres.

**Scheies og Hurlers syndrom** skyldes mangel på alfa-L-iduronidase (IDUA) ved MPS I. Sebelipase alfa har ingen aktivitet på glykosaminoglykan-substrater. Den høje score afspejler formentlig, at sygdommene ligger tæt på hinanden i grafen som lysosomale lagringssygdomme med enzymerstatning, ikke reel biologi.

**Væksthormoninsensitivitetssyndromet** er en STAT5B-relateret forstyrrelse af væksthormonsignalering og immunregulering. Den har ingen biologisk relation til lysosomal syrelipase og er sandsynligvis en artefakt i vidensgrafen.

---

## Evidens fra kliniske forsøg

Tabellen viser forsøg knyttet til kolesterylesterlagringssygdom, den bedst understøttede forudsigelse. Ingen EudraCT-identifikatorer er tilgængelige i datagrundlaget.

| Forsøgsnummer | Fase | Status | Antal deltagere | Hovedresultater |
|---------|------|------|------|---------|
| [NCT01757184](https://clinicaltrials.gov/study/NCT01757184) | Fase 3 | Afsluttet | 66 | Randomiseret, placebokontrolleret forsøg med sebelipase alfa 1 mg/kg i.v. hver 2. uge ved sent debuterende LAL-D. Direkte pivotal evidens |
| [NCT02112994](https://clinicaltrials.gov/study/NCT02112994) | Fase 2 | Afsluttet | 31 | Åbent forsøg med sikkerhed og effekt i en bred LAL-D-population |
| [NCT01371825](https://clinicaltrials.gov/study/NCT01371825) | Fase 2/3 | Afsluttet | 9 | Dosiseskalering hos børn med væksthæmning pga. LAL-D |
| [NCT01307098](https://clinicaltrials.gov/study/NCT01307098) | Fase 1/2 | Afsluttet | 9 | Første kliniske studie af sebelipase alfa (SBC-102) hos voksne med leverpåvirkning. Sikkerhed og farmakokinetik |
| [NCT01488097](https://clinicaltrials.gov/study/NCT01488097) | Fase 2 | Afsluttet | 8 | Forlængelsesstudie af NCT01307098 med langtidssikkerhed og -effekt |
| [NCT02193867](https://clinicaltrials.gov/study/NCT02193867) | Fase 2 | Afsluttet før tid | 10 | Åbent forsøg hos spædbørn med hurtigt progredierende LAL-D (Wolman-fænotype) |
| [NCT04532047](https://clinicaltrials.gov/study/NCT04532047) | Fase 1 | Rekrutterer | 10 | Prænatal enzymerstatning ved lysosomale lagringssygdomme, herunder LAL-mangel. Tidlig fase og lille |
| [NCT02376751](https://clinicaltrials.gov/study/NCT02376751) | Ikke angivet | Ikke længere tilgængelig | Ikke angivet | Udvidet adgangsprotokol (USA). Viser klinisk brug, men er ikke effektevidens |
| [NCT02926872](https://clinicaltrials.gov/study/NCT02926872) | Ikke angivet | Afsluttet før tid | 22 | Observationelt screeningsstudie for LAL-D ved leverskade hos børn. Diagnostisk, ikke behandling |

For **Hurlers syndrom** er kun NCT04532047 knyttet til forudsigelsen. Forsøget er en prænatal enzymerstatningsplatform for flere sygdomme. Sebelipase alfa ville kun anvendes i LAL-D-armen, ikke ved MPS I, så forsøget giver ikke direkte evidens for Hurlers syndrom. For Scheies syndrom og den STAT5B-relaterede sygdom findes ingen forsøg.

---

## Litteraturevidens

Tabellen viser de 10 mest relevante publikationer for LAL-D (kolesterylesterlagringssygdom og Wolmans sygdom).

| PMID | År | Type | Tidsskrift | Hovedresultater |
|---------|-----|------|------|---------|
| [34774639](https://pubmed.ncbi.nlm.nih.gov/34774639/) | 2022 | RCT | J Hepatol | Endelige resultater fra fase 3-studiet ARISE med sebelipase alfa hos børn (≥4 år) og voksne med LAL-D |
| [29628368](https://pubmed.ncbi.nlm.nih.gov/29628368/) | 2018 | RCT (post hoc) | J Clin Lipidol | Forbedring af aterogene biomarkører op til 52 uger i fase 3-studiet |
| [35442238](https://pubmed.ncbi.nlm.nih.gov/35442238/) | 2022 | Kohorte (enkeltarmet, åben) | J Pediatr Gastroenterol Nutr | Langtidsbehandling af børn og voksne med LAL-D (NCT02112994) |
| [32657505](https://pubmed.ncbi.nlm.nih.gov/32657505/) | 2020 | Åbent forlængelsesstudie | Liver Int | 5 års behandlingserfaring. Efter 1 år var transaminaser og leverfedt reduceret, og lipidprofilen forbedret |
| [24993530](https://pubmed.ncbi.nlm.nih.gov/24993530/) | 2014 | Åbent forlængelsesstudie | J Hepatol | 52 uger reducerede transaminaser og levervolumen og forbedrede serumlipider |
| [23348766](https://pubmed.ncbi.nlm.nih.gov/23348766/) | 2013 | Første humane studie | Hepatology | Klinisk effekt og sikkerhedsprofil hos 9 patienter med kolesterylesterlagringssygdom |
| [28179030](https://pubmed.ncbi.nlm.nih.gov/28179030/) | 2017 | Åbent dosiseskaleringsstudie | Orphanet J Rare Dis | Overlevelse hos spædbørn med LAL-D behandlet med sebelipase alfa |
| [34906190](https://pubmed.ncbi.nlm.nih.gov/34906190/) | 2021 | Kohorte | Orphanet J Rare Dis | Landsdækkende kohorte ved Wolmans sygdom med op til ti års opfølgning |
| [38918870](https://pubmed.ncbi.nlm.nih.gov/38918870/) | 2024 | Case series | Orphanet J Rare Dis | Dosering to gange ugentligt (5 mg/kg) hos svært syge spædbørn med Wolmans sygdom |
| [40781810](https://pubmed.ncbi.nlm.nih.gov/40781810/) | 2025 | Registerdata | Liver Int | Aminotransferaseniveauer hos behandlede og ubehandlede LAL-D-patienter |

Derudover findes retningslinjer og oversigtsartikler, bl.a. [39770929](https://pubmed.ncbi.nlm.nih.gov/39770929/) (praktiske anbefalinger med fokus på Wolmans sygdom, 2024). Et case report beskriver desto-sensibilisering ved overfølsomhed over for sebelipase alfa: [38572778](https://pubmed.ncbi.nlm.nih.gov/38572778/). Der er ingen litteratur for Scheies syndrom, Hurlers syndrom eller den STAT5B-relaterede sygdom.

---

## Information om det danske marked

| Markedsføringstilladelse | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28105545614 | Kanuma (Alexion Europe) | Koncentrat til infusionsvæske, opløsning | Indikationsteksten er ikke angivet i datagrundlaget |

---

## Sikkerhedsovervejelser

Der foreligger ikke strukturerede data om advarsler, kontraindikationer eller interaktioner (en interaktionssøgning gav ingen fund). Se det godkendte produktresumé (SmPC) for sikkerhedsoplysninger.

Evidenspakkens forbehold for de LAL-D-relaterede forudsigelser er overvågning for infusionsrelaterede reaktioner, overfølsomhed og anti-lægemiddelantistoffer. Hos spædbørn med Wolmans sygdom anbefales behandling på et specialiseret center.

---

## Konklusion og næste skridt

**Beslutning: Proceed with Guardrails** (kolesterylesterlagringssygdom og Wolmans sygdom). **Hold** for Scheies syndrom, Hurlers syndrom og den STAT5B-relaterede sygdom.

**Begrundelse:**
- Sebelipase alfa erstatter direkte det manglende enzym ved LAL-D. Der foreligger et fase 3-RCT, flere fase 2-studier og omfattende kohortedata, og lægemidlet er markedsført. Forudsigelserne for kolesterylesterlagringssygdom og Wolmans sygdom er derfor i praksis allerede godkendte indikationer.
- De øvrige tre forudsigelser mangler både mekanistisk grundlag og klinisk evidens.

**For at komme videre kræves:**
- Produktresuméet fra Lægemiddelstyrelsen (advarsler og kontraindikationer) (datahul DG001)
- Data om virkningsmekanisme fra DrugBank (datahul DG002)
- Den godkendte indikationstekst for Kanuma i Danmark
- Kontrol af, om Wolman-noden svarer til klassisk Wolmans sygdom
- Bekræftet LAL-D-diagnose ved enzymaktivitet eller genotype, samt et overvågningsprogram for overfølsomhed og anti-lægemiddelantistoffer

*Resultaterne er kun til forskningsbrug og udgør ikke lægefaglig rådgivning. Forudsigelser fra modellen kræver klinisk validering.*
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

