---
layout: default
title: Ifosfamide
parent: Kun modelforudsigelse (L5)
nav_order: 425
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-28
description: "Ifosfamide: forudsagt ny indikation Kvindelig brystkarcinom (female breast carcinoma) (evidensniveau L5). Oprindelig indikation: Ikke angivet i de indsamlede data (godkendelsesteksten for Holoxan er…"
monitor_inn: "ifosfamide"
predicted_indications: ["female breast carcinoma", "unclassified myelodysplastic syndrome", "partial deletion of the long arm of chromosome 5", "refractory cytopenia of childhood", "severe congenital hypochromic anemia with ringed sideroblasts", "aregenerative anemia", "rhabdomyosarcoma (disease)", "myelodysplastic syndrome", "monocytic leukemia", "botryoid-type embryonal rhabdomyosarcoma of the vagina"]
---

# Ifosfamide
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

## Ifosfamid: Fra [oprindelig indikation ikke angivet] til Kvindelig brystkræft
{: .text-alpha }

## Opsummering i en enkelt sætning

Ifosfamid er et alkylerende cytostatikum (prodrug), som i Danmark er markedsført som Holoxan. De data, der er indsamlet til denne rapport, indeholder ingen tekst om den godkendte indikation. TxGNN-modellen forudsiger flere nye indikationer. Den bedst understøttede er **rhabdomyosarkom** med **16 kliniske forsøg** og **20 publikationer**, herunder flere fase 3-forsøg i bløddelssarkom. Den højest scorende forudsigelse er dog **kvindelig brystkarcinom**, som kun har fase 2-evidens.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Ikke angivet i de indsamlede data (godkendelsesteksten for Holoxan er tom) |
| Forudsagt ny indikation (højeste score) | Kvindelig brystkarcinom (female breast carcinoma) |
| TxGNN-forudsigelsesscore | 0,9991 |
| Evidensniveau | L5 for brystkarcinom (fase 2-forsøg, ingen fase 3). Til sammenligning: L1 for rhabdomyosarkom |
| Markedsstatus i Danmark | Markedsført (gyldige tilladelser: 1 af 1) |
| Antal markedsføringstilladelser | 1 (gyldige: 1) |
| Anbefalet beslutning | Brystkarcinom: Hold (forskningsspørgsmål). Rhabdomyosarkom: Proceed with Guardrails |

> **Bemærk:** Den højest rangerede forudsigelse er brystkarcinom. Rhabdomyosarkom (rang 7, score 0,9967) har dog markant stærkere evidens. Rapporten fokuserer primært på brystkarcinom og beskriver rhabdomyosarkom som sammenligning. Øvrige forudsigelser omtales kort nedenfor.

---

## Hvorfor er denne forudsigelse rimelig?

Ifosfamid er et alkylerende stof og et prodrug, som aktiveres i leveren af cytokrom P450-enzymer (især CYP3A4 og CYP2B6) til isofosforamid-sennep. Denne aktive metabolit krydsbinder DNA og udløser apoptose i hurtigt delende tumorceller. Der foreligger ikke detaljerede mekanismedata i de indsamlede data, så beskrivelsen bygger på almindeligt kendt farmakologi.

Mekanismen er plausibel for brystkarcinom. Fase 2-forsøg med ifosfamidholdige regimer (f.eks. docetaxel-ifosfamid og højdosisregimer) og flere publikationer om ifosfamid ved fremskreden brystkræft, metaplastisk brystkræft og phyllodes-tumorer understøtter dette. Der er imidlertid ikke registreret noget fase 3-forsøg i brystkræft, og fase 2-forsøgene har status ukendt eller afsluttet i utide.

For rhabdomyosarkom er sammenhængen stærkere. Ifosfamid er en etableret del af sarkomregimer (ifosfamid/etoposid og IVA) og anvendes ved recidiverende eller refraktær sygdom. Flere fase 3-forsøg i bløddelssarkom inkluderer ifosfamid, men de fleste omfatter voksne bløddelssarkomer eller blandede populationer frem for rhabdomyosarkom specifikt.

---

## Klinisk forsøgsevidens

### Brystkarcinom (rang 1)

| Forsøgsnummer | Fase | Status | Antal deltagere | Hovedresultater |
|---------|------|------|------|---------|
| [NCT00026078](https://clinicaltrials.gov/study/NCT00026078) | Fase 2 | Ukendt | 42 | Docetaxel + ifosfamid som førstelinjebehandling ved metastatisk brystkræft. Tester direkte ifosfamid, men uden randomisering |
| [NCT00012311](https://clinicaltrials.gov/study/NCT00012311) | Fase 2 | Ukendt | Ikke oplyst | Randomiseret sammenligning af højdosis- og optimeret konventionel kemoterapi ved metastatisk brystkræft. Ifosfamids rolle er sandsynlig, men ikke bekræftet |
| [NCT00006032](https://clinicaltrials.gov/study/NCT00006032) | Fase 2 | Afsluttet i utide | Ikke oplyst | Højdosis topotecan, ifosfamid/mesna og etoposid med autolog stamcellestøtte. Begrænset fortolkning |
| [NCT00002854](https://clinicaltrials.gov/study/NCT00002854) | Fase 1 | Afsluttet | 33 | Sekventiel højdosis cisplatin, cyclophosphamid, etoposid og ifosfamid med stamcellestøtte (gennemførlighed/sikkerhed) |
| [NCT00003086](https://clinicaltrials.gov/study/NCT00003086) | Fase 1/2 | Afsluttet i utide | 12 | Samarium-153 ved dobbelt autolog transplantation. Ifosfamid er sandsynligvis kun baggrundsstof |
| [NCT00020722](https://clinicaltrials.gov/study/NCT00020722) | Fase 2 | Afsluttet i utide | 7 | Aktiverede T-celler efter stamcelletransplantation. Ifosfamid er ikke det undersøgte stof |

### Rhabdomyosarkom og relateret sarkom (rang 7) – de mest relevante

| Forsøgsnummer | Fase | Status | Antal deltagere | Hovedresultater |
|---------|------|------|------|---------|
| [NCT00003212](https://clinicaltrials.gov/study/NCT00003212) | Fase 3 | Afsluttet | 780 | To ifosfamid-skemaer vs. standarddosis doxorubicin ved fremskreden bløddelssarkom |
| [NCT00061984](https://clinicaltrials.gov/study/NCT00061984) | Fase 3 | Afsluttet | 455 | Doxorubicin alene vs. doxorubicin + ifosfamid som førstelinje ved bløddelssarkom |
| [NCT00003052](https://clinicaltrials.gov/study/NCT00003052) | Fase 3 | Afsluttet | 340 | Neoadjuverende etoposid + ifosfamid + doxorubicin med eller uden regional hypertermi ved højrisiko bløddelssarkom |
| [NCT00002641](https://clinicaltrials.gov/study/NCT00002641) | Fase 3 | Afsluttet | 350 | Adjuverende højdosis doxorubicin + ifosfamid + lenograstim ved højgradigt bløddelssarkom |
| [NCT00346164](https://clinicaltrials.gov/study/NCT00346164) | Fase 3 | Afsluttet | 588 | Risikobaseret behandling af non-rhabdomyosarkom bløddelssarkom hos patienter under 30 år |
| [NCT00025363](https://clinicaltrials.gov/study/NCT00025363) | Fase 2 | Afsluttet | 150 | Randomiseret vindues-studie ved recidiverende rhabdomyosarkom. Ifosfamids involvering bør verificeres |
| [NCT00025441](https://clinicaltrials.gov/study/NCT00025441) | Fase 2 | Afsluttet | Ikke oplyst | MMT 98: kombinationskemoterapi ved metastatisk rhabdomyosarkom hos børn |
| [NCT06277154](https://clinicaltrials.gov/study/NCT06277154) | Fase 2 | Rekrutterer | 148 | MASCT-I + doxorubicin og ifosfamid som førstelinje ved fremskreden bløddelssarkom |
| [NCT06239272](https://clinicaltrials.gov/study/NCT06239272) | Fase 1/2 | Rekrutterer | 139 | Risikotilpasset studie ved non-rhabdomyosarkom med pazopanib-vedligeholdelse; ifosfamid sandsynligvis del af kemoterapi |
| [NCT00003292](https://clinicaltrials.gov/study/NCT00003292) | Fase 2 | Afsluttet i utide | 7 | Ifosfamid ved aggressive meningeale tumorer |

---

## Litteraturevidens

### Brystkarcinom

| PMID | År | Type | Tidsskrift | Hovedresultater |
|------|-----|------|------|---------|
| [8918497](https://pubmed.ncbi.nlm.nih.gov/8918497/) | 1996 | Fase 2-forsøg | J Clin Oncol | Ifosfamid + vinorelbin som førstelinje ved metastatisk brystkræft |
| [8445421](https://pubmed.ncbi.nlm.nih.gov/8445421/) | 1993 | Fase 2-forsøg | J Clin Oncol | Ifosfamid + mitoxantron som førstelinje ved metastatisk brystkræft |
| [11932893](https://pubmed.ncbi.nlm.nih.gov/11932893/) | 2002 | Fase 2-forsøg | Cancer | Paclitaxel (24-timers infusion) + ifosfamid ved antracyklinresistent metastatisk brystkræft |
| [14586149](https://pubmed.ncbi.nlm.nih.gov/14586149/) | 2003 | Oversigtsartikel | Oncology | Ifosfamid ved fremskreden brystkræft: responsrater 7-30 % som monoterapi ved forbehandlede patienter, højere i kombinationer; mesna reducerer urotoksicitet |
| [39306877](https://pubmed.ncbi.nlm.nih.gov/39306877/) | 2024 | Kohorte | Curr Probl Cancer | Erfaringer med ifosfamidbaseret kemoterapi ved metaplastisk brystkræft |
| [2112056](https://pubmed.ncbi.nlm.nih.gov/2112056/) | 1990 | Klinisk studie | Cancer Chemother Pharmacol | Ifosfamid/etoposid og mesna ved fremskreden brystkræft (44 patienter) |
| [2347057](https://pubmed.ncbi.nlm.nih.gov/2347057/) | 1990 | Klinisk studie | Cancer Chemother Pharmacol | Ifosfamid, methotrexat og 5-FU ved resistent brystkræft (25 patienter) |
| [1390313](https://pubmed.ncbi.nlm.nih.gov/1390313/) | 1992 | Oversigtsartikel | Ann Oncol | Brug af ifosfamid ved brystkræft; ca. 20 % objektiv respons som monoterapi |
| [1720382](https://pubmed.ncbi.nlm.nih.gov/1720382/) | 1991 | Oversigtsartikel | Drugs | Ifosfamid/mesna: antineoplastisk aktivitet, farmakokinetik og effekt |
| [39074497](https://pubmed.ncbi.nlm.nih.gov/39074497/) | 2024 | Kohorte | J Natl Compr Canc Netw | Adjuverende kemoterapi ved maligne phyllodes-tumorer i brystet |

### Rhabdomyosarkom (udvalgt)

| PMID | År | Type | Tidsskrift | Hovedresultater |
|------|-----|------|------|---------|
| [11846301](https://pubmed.ncbi.nlm.nih.gov/11846301/) | 2001 | Klinisk studie | J Pediatr Hematol Oncol | Ifosfamid + etoposid var bedre end vincristin + melphalan ved metastatisk rhabdomyosarkom hos børn |
| [31786124](https://pubmed.ncbi.nlm.nih.gov/31786124/) | 2020 | Prospektiv kohorte | Lancet Oncol | Risikobaseret behandlingsstrategi ved non-rhabdomyosarkom bløddelssarkom (ARST0332) |
| [19770626](https://pubmed.ncbi.nlm.nih.gov/19770626/) | 2010 | Oversigt | Am J Clin Oncol | Behandling af rhabdomyosarkom hos voksne med doxorubicin, ifosfamid og vincristin |
| [9849484](https://pubmed.ncbi.nlm.nih.gov/9849484/) | 1998 | Klinisk studie | Eur J Cancer | Mellemrisiko-rhabdomyosarkom med alternerende VDC og etoposid/ifosfamid |

---

## Information om markedet i Danmark

| Markedsføringstilladelsesnummer | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28101091881 | Holoxan (Baxter A/S) | Pulver til injektions-/infusionsvæske, opløsning | Indikationstekst ikke angivet i de indsamlede data |

---

## Cytotoksicitet

| Punkt | Indhold |
|------|------|
| Cytotoksicitetsklassifikation | Konventionelt cytotoksisk (alkylerende middel, oxazaphosphorin) |
| Risiko for myelosuppression | Høj (leukopeni, trombocytopeni og anæmi er nævnt som kontraindikationsrelaterede tilstande i vidensgrafen) |
| Emetogenicitetsklassifikation | Se produktresuméet (SmPC) |
| Monitorering | Fuld blodtælling med differentialtælling, lever- og nyrefunktion, elektrolytter (især kalium), urinundersøgelse |
| Håndteringsbeskyttelse | Skal håndteres i henhold til gældende regler for cytotoksiske lægemidler |

---

## Sikkerhedsovervejelser

Produktresuméets advarsler og kontraindikationer er ikke tilgængelige i de indsamlede data. Følgende er baseret på øvrige data:

- **Tilstande med kontraindikationssignal (fra vidensgraf, ikke produkttekst):** nyresygdom, leversygdom, galdeblæresygdom, trombocytopeni, leukopeni, anæmi, kaliummangel, hyperbilirubinæmi (inkl. Gilberts syndrom), renal tubulær acidose og Fanconis syndrom.
- **Forsigtighedspunkter nævnt i evidensgrundlaget:** nefrotoksicitet, neurotoksicitet, myelosuppression, hæmoragisk cystitis (mesna er påkrævet), sekundær malignitet (inkl. terapirelateret MDS/leukæmi) og en høj interaktionsbyrde.
- **Lægemiddelinteraktioner:** 616 registrerede interaktioner. Eksempler på moderate interaktioner: amphotericin B, bupropion, aprepitant, morfin, metoclopramid, scopolamin, dronabinol, nabilon, aminoglykosider (kanamycin, neomycin) samt sulfonylurinstoffer og glinider (glimepirid, glipizid, glibenclamid, chlorpropamid, tolazamid, acetohexamid, nateglinid, repaglinid). Levofloxacin er en mindre interaktion.

Se i øvrigt det godkendte produktresumé (SmPC) for fuldstændige sikkerhedsoplysninger.

---

## Øvrige forudsigelser (kort)

| Forudsagt indikation | Score | Evidensniveau | Vurdering |
|------|------|------|------|
| Uklassificeret myelodysplastisk syndrom | 0,9971 | L5 | Hold. Ingen forsøg eller litteratur; ifosfamid er selv forbundet med terapirelaterede myeloide neoplasmer |
| Partiel deletion af kromosom 5q | 0,9970 | L5 | Hold. Cytogenetisk afvigelse, ikke en klinisk indikation |
| Refraktær cytopeni hos børn | 0,9970 | L5 | Hold. Eneste forsøg undersøger understøttende behandling, ikke ifosfamid |
| Medfødt hypokrom anæmi med ringsideroblaster | 0,9968 | L5 | Hold. Ingen mekanistisk rationale |
| Aregenerativ anæmi | 0,9968 | L5 | Hold. Litteraturen handler om andre sygdomme (formodede fejlassociationer) |
| Myelodysplastisk syndrom | 0,9966 | L4 | Hold. Litteraturen beskriver MDS som bivirkning, ikke effekt |
| Monocytær leukæmi | 0,9964 | L5 | Hold. Kun sekundær leukæmi som bivirkning |
| Botryoid embryonalt rhabdomyosarkom i vagina | 0,9957 | L5 | Forskningsspørgsmål. Kun en enkelt case-rapport; støtte er indirekte via rhabdomyosarkom |

---

## Konklusion og næste skridt

**Beslutning: Hold (forskningsspørgsmål) for brystkarcinom. Proceed with Guardrails for rhabdomyosarkom.**

**Begrundelse:**
- For brystkarcinom (højeste TxGNN-score) findes kun fase 2-forsøg med ukendt eller afbrudt status og ingen fase 3-forsøg. Evidensen er L2 og egner sig til videre forskning frem for klinisk implementering.
- For rhabdomyosarkom er evidensen L1 med flere afsluttede fase 3-forsøg i bløddelssarkom og en veletableret rolle for ifosfamid i sarkomregimer. De fleste fase 3-forsøg omfatter dog bløddelssarkom generelt, ikke rhabdomyosarkom specifikt.

**For at komme videre kræves følgende:**
- Hentning af produktresuméet for Holoxan fra Lægemiddelstyrelsen for at få den godkendte indikation, advarsler og kontraindikationer (kritisk datahul, der blokerer sikkerhedsscreening).
- Detaljerede data om virkningsmekanisme (MOA) fra DrugBank.
- For brystkarcinom: randomiserede forsøg med moderne standardbehandling som komparator.
- For rhabdomyosarkom: verifikation af ifosfamids rolle i de nævnte forsøg og undergruppeanalyser for rhabdomyosarkom.
- Monitoreringsplan for nefrotoksicitet, neurotoksicitet, myelosuppression og urotoksicitet (mesna), samt gennemgang af lægemiddelinteraktioner.
- Vurdering af, om forskellen mellem godkendt og forudsagt indikation kræver en ny ansøgning eller off-label-anvendelse.
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

