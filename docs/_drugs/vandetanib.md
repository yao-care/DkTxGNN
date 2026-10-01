---
layout: default
title: Vandetanib
parent: Moderat evidens (L3-L4)
nav_order: 467
evidence_level: L3
indication_count: 10
---

# Vandetanib
{: .fs-9 }

Evidensniveau: **L3** | Forudsagte indikationer: **10** stk.
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

# Vandetanib: Fra medullær thyreoideacancer til nyrecellekarcinom

## Resumé i en sætning

Vandetanib er en oral tyrosinkinasehæmmer, som ifølge litteraturen i evidenspakken er godkendt til avanceret medullær thyreoideacancer.
TxGNN-modellen forudsiger, at lægemidlet kan have effekt ved **nyrecellekarcinom (renal cell carcinoma)**.
Støtten er begrænset: **4 kliniske forsøg** (kun 3 direkte relevante, hvoraf 2 blev afsluttet for tidligt) og **6 publikationer** (ingen med vandetanib-specifikke resultater for nyrecellekarcinom).

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Ikke angivet i de danske registerdata. Litteraturen i evidenspakken nævner medullær thyreoideacancer |
| Forudsagt ny indikation | Nyrecellekarcinom (renal cell carcinoma) |
| TxGNN-prædiktionsscore | 99,92 % |
| Evidensniveau | L3 |
| Markedsstatus i Danmark | Markedsført |
| Antal markedsføringstilladelser | 1 |
| Anbefalet beslutning | Hold (afvent) |

---

## Hvorfor er forudsigelsen rimelig?

Vandetanib hæmmer VEGFR2, EGFR og RET. DrugBank-data om virkningsmekanisme (MOA) er ikke tilgængelige i evidenspakken. Oplysningen om målstrukturerne stammer fra evidensvurderingen.

Ved klarcellet nyrecellekarcinom fører tab af VHL-genet til aktivering af HIF og øget VEGF-signalering. Hæmning af VEGFR er derfor biologisk plausibel. Andre VEGFR-rettede tyrosinkinasehæmmere (f.eks. cabozantinib) omtales i litteraturen om nyrecellekarcinom. Det er også en mekanistisk forbindelse til den oprindelige kræftindikation, hvor vandetanib virker via RET-hæmning.

TxGNN-scoren er meget høj, men den er kun en modelforudsigelse. Den kliniske støtte består af små eller for tidligt afsluttede fase 2-forsøg uden publicerede effektresultater i de leverede data. Evidensen er derfor vurderet til L3 og ikke L2, fordi ingen af de nyrespecifikke fase 2-forsøg er randomiserede.

Modellen forudsiger også en række sjældne subtyper (uklassificeret nyrecellekarcinom, Xp11.2/TFE3-translokation, nyrecellekarcinom associeret med neuroblastom). For disse findes hverken forsøg eller litteratur. Scoren afspejler sandsynligvis nærhed til moderknuden "nyrecellekarcinom" i vidensgrafen og ikke subtypespecifik biologi. De vurderes som L5 med anbefalingen Hold.

Karcinom i nyrebækkenet (renal pelvis carcinoma) har score 99,88 % og et randomiseret fase 2-forsøg (NCT01191892). Det er tentativt vurderet som L2, se nedenfor.

---

## Klinisk evidens

| Forsøgsnummer | Fase | Status | Antal deltagere | Hovedpunkter |
|---------|------|------|------|---------|
| [NCT00566995](https://clinicaltrials.gov/study/NCT00566995) | Fase 2 | Afsluttet | 37 | Vandetanib ved von Hippel-Lindau-sygdom med nyretumorer. Direkte relevant population, men ikke randomiseret, og der er ikke leveret effektresultater |
| [NCT02495103](https://clinicaltrials.gov/study/NCT02495103) | Fase 1/2 | Afbrudt | 7 | Vandetanib + metformin ved HLRCC- eller SDH-associeret nyrekræft og sporadisk papillært nyrecellekarcinom. Sjældne arvelige subtyper, få patienter |
| [NCT01372813](https://clinicaltrials.gov/study/NCT01372813) | Fase 2 | Afbrudt | 3 | Vandetanib ved avanceret klarcellet nyrecellekarcinom. Direkte relevant, men kun 3 patienter, så reelt uinformativt for effekt |
| [NCT01191892](https://clinicaltrials.gov/study/NCT01191892) | Fase 2 (randomiseret) | Afsluttet | 82 | Carboplatin + gemcitabin med eller uden vandetanib som førstelinjebehandling ved avanceret urotelcancer hos patienter uegnede til cisplatin. Indirekte for nyrecellekarcinom. Relevant for nyrebækkenkarcinom, men populationen bør verificeres, og effektresultater er ikke leveret |

---

## Litteraturevidens

| PMID | År | Type | Tidsskrift | Hovedpunkter |
|------|-----|------|------|---------|
| [40779213](https://pubmed.ncbi.nlm.nih.gov/40779213/) | 2025 | Præklinisk/translationel (ikke verificeret ud fra titel) | Clinical & Experimental Metastasis | Målrettet behandling af metabolisk og epigenetisk omprogrammering ved metastatisk fumarathydratase-mangelfuldt nyrecellekarcinom. Ingen standardbehandling, flere fase 2-forsøg undersøger kombinationer |
| [36302175](https://pubmed.ncbi.nlm.nih.gov/36302175/) | 2023 | Fase 2-forsøg (guadecitabin, ikke vandetanib) | Clinical Cancer Research | Indirekte: guadecitabin ved SDH-mangelfulde tumorer, bl.a. HLRCC-associeret nyrecellekarcinom |
| [31043488](https://pubmed.ncbi.nlm.nih.gov/31043488/) | 2019 | Præklinisk (musemodel) | Molecular Cancer Research | TFE3 Xp11.2-translokations-nyrecellekarcinom: musemodel, nye terapeutiske targets og GPNMB som diagnostisk markør |
| [28477875](https://pubmed.ncbi.nlm.nih.gov/28477875/) | 2017 | Oversigtsartikel | Bulletin du Cancer | Cabozantinib (VEGFR2, c-MET, RET): virkningsmekanisme og indikationer. Bruges som mekanistisk sammenligning |
| [26677336](https://pubmed.ncbi.nlm.nih.gov/26677336/) | 2015 | Oversigtsartikel | OncoTargets and Therapy | Nintedanib ved solide tumorer. Nævner vandetanib blandt antiangiogene midler |
| [24451769](https://pubmed.ncbi.nlm.nih.gov/24451769/) | 2012 | Oversigtsartikel | ASCO Educational Book | Systemisk behandling af avanceret thyreoideacancer. Vandetanib som RET-hæmmer ved medullær thyreoideacancer |

Ingen af publikationerne rapporterer effektresultater for vandetanib ved nyrecellekarcinom.

---

## Information om markedet i Danmark

| Markedsføringstilladelsesnummer | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28104777710 | Caprelsa (Sanofi B.V.) | Filmovertrukne tabletter (oral) | Ikke angivet i registerdata |

---

## Cytotoksicitet

| Punkt | Indhold |
|------|------|
| Cytotoksicitetsklassifikation | Målrettet behandling (tyrosinkinasehæmmer mod VEGFR2, EGFR og RET) |
| Risiko for myelosuppression | Se produktresuméet (SmPC) for advarsler og forsigtighedsregler |
| Emetogenicitetsklassifikation | Se produktresuméet (SmPC) |
| Monitoreringspunkter | Se produktresuméet (SmPC) |
| Beskyttelse ved håndtering | Følg gældende regler for håndtering af antineoplastiske lægemidler, og se SmPC |

---

## Sikkerhedsovervejelser

Der er ingen tilgængelige data om advarsler, kontraindikationer eller interaktioner i evidenspakken. Der blev ikke fundet registrerede lægemiddelinteraktioner i den anvendte kilde. Det er ikke ensbetydende med, at der ikke findes interaktioner.

Se det godkendte produktresumé (SmPC) for sikkerhedsoplysninger.

---

## Konklusion og næste skridt

**Beslutning: Hold (afvent)**

**Begrundelse:**
- Modelscoren er meget høj (99,92 %), men den kliniske støtte ved nyrecellekarcinom består kun af små, ikke-randomiserede eller for tidligt afbrudte fase 2-forsøg (3, 7 og 37 patienter) uden leverede effektresultater.
- Sikkerhedsoplysninger fra det danske produktresumé mangler (blokerende datahul), så sikkerhedsscreening kan ikke gennemføres. Anbefalingen er derfor et forskningsspørgsmål og ikke en klinisk anbefaling.

**For at komme videre kræves:**
- Hent og gennemgå produktresuméet fra Lægemiddelstyrelsen (advarsler, kontraindikationer, interaktioner).
- Indhent DrugBank-data om virkningsmekanisme.
- Skaf publicerede eller registrerede resultater fra NCT00566995, NCT01372813 og NCT02495103.
- Verificér, om NCT01191892 inkluderede patienter med nyrebækkenkarcinom, og hent forsøgets effektresultater.
- Vurder først efterfølgende, om de sjældne subtyper (rang 3-8) fortjener selvstændig undersøgelse. I dag er de kun modelforudsigelser.

*Resultaterne er udelukkende til forskningsbrug og udgør ikke medicinsk rådgivning. Kandidater til lægemiddelomplacering skal valideres klinisk, før de kan anvendes.*
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

