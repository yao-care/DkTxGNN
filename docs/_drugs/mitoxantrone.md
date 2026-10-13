---
layout: default
title: Mitoxantrone
parent: Kun modelforudsigelse (L5)
nav_order: 563
evidence_level: L5
indication_count: 8
---

# Mitoxantrone
{: .fs-9 }

Evidensniveau: **L5** | Forudsagte indikationer: **8** stk.
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

# Mitoxantron: Fra akut myeloid leukæmi til hoved- og halskræft

## Resumé i én sætning

Mitoxantron er et kemoterapeutisk middel (topoisomerase II-hæmmer), der oprindeligt anvendes til behandling af akut myeloid leukæmi.
TxGNN-modellen forudsiger, at det kan have effekt på **øvre luftvejs- og fordøjelseskanalstumorer** (højeste modelscore), men den bedst understøttede forudsigelse er **hoved- og halskræft**, hvor der findes **6 kliniske forsøg** og **20 publikationer**. Evidensen er hovedsageligt ældre fase II-studier samt nyere studier med den liposomale formulering, som ikke er markedsført i Danmark.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Akut myeloid leukæmi (indikationstekst i dansk markedsføringstilladelse er ikke angivet i de indsamlede data) |
| Forudsagt ny indikation | Øvre luftvejs- og fordøjelseskanalstumor (modellens førstevalg); hoved- og halskræft er den bedst understøttede kandidat |
| TxGNN-forudsigelsesscore | 99,78 % (øvre luftvejs- og fordøjelseskanalstumor); 99,31 % (hoved- og halskræft) |
| Evidensniveau | L3 for øvre luftvejs- og fordøjelseskanalstumor; L2 for hoved- og halskræft |
| Markedsstatus i Danmark | Markedsført |
| Antal markedsføringstilladelser | 1 |
| Anbefalet beslutning | Hold for øvre luftvejs- og fordøjelseskanalstumor (rangeret som forskningsspørgsmål); Proceed with Guardrails for hoved- og halskræft |

---

## Hvorfor er forudsigelsen rimelig?

De indsamlede data indeholder ikke detaljerede mekanismedata fra DrugBank. Ud fra kendt viden er mitoxantron et antracendion-derivat, der virker som topoisomerase II-hæmmer og DNA-interkalator. Det er cytotoksisk over for hurtigt delende celler. Effekten ved akut myeloid leukæmi er dokumenteret, og mekanismen kan principielt også være relevant for solide tumorer.

Ældre fase II-studier har vist beskeden aktivitet i planocellulært karcinom og adenoid cystisk karcinom i hoved- og halsområdet, og i nasopharyngealt karcinom. Resultaterne har dog været blandede: nogle studier (f.eks. Southwest Oncology Group) fandt ingen betydelig antitumoraktivitet. Nyere arbejde med liposomalt mitoxantron (fase Ib og fase II) giver fornyet interesse, især ved nasopharyngealt karcinom.

Bemærk, at evidensen for "øvre luftvejs- og fordøjelseskanalstumor" i høj grad overlapper med evidensen for hoved- og halskræft.

---

## Dokumentation fra kliniske forsøg

De kliniske forsøg nedenfor er knyttet til hoved- og halskræft (den bedst understøttede forudsigelse). Der er ingen registrerede forsøg knyttet direkte til "øvre luftvejs- og fordøjelseskanalstumor".

| Forsøgsnummer | Fase | Status | Antal deltagere | Hovedresultater |
|---------|------|------|------|---------|
| [NCT04902027](https://clinicaltrials.gov/study/NCT04902027) | Fase 1b | Afsluttet | 45 | Liposomalt mitoxantron ved recidiverende/metastatisk hoved- og halskræft; direkte data om sikkerhed og effekt |
| [NCT05717764](https://clinicaltrials.gov/study/NCT05717764) | Fase 3 | Endnu ikke rekrutterende | 500 | Liposomalt mitoxantron + capecitabin vs. capecitabin alene ved recidiverende/metastatisk nasopharyngealt karcinom efter platinbehandling; ingen resultater endnu |
| [NCT06472713](https://clinicaltrials.gov/study/NCT06472713) | Fase 2 | Rekrutterer | 32 | Liposomalt mitoxantron + PD-1-blokade ved forbehandlet nasopharyngealt karcinom |
| [NCT06892431](https://clinicaltrials.gov/study/NCT06892431) | Fase 2 | Endnu ikke rekrutterende | 150 | JMT101 + liposomalt mitoxantron ved nasopharyngealt karcinom efter mindst to tidligere behandlinger |
| [NCT07070479](https://clinicaltrials.gov/study/NCT07070479) | Fase 2 | Rekrutterer | 208 | Bayesiansk adaptivt forsøg med fire regimer ved PD-1-resistent nasopharyngealt karcinom; mitoxantron er ikke det centrale middel |
| [NCT07354698](https://clinicaltrials.gov/study/NCT07354698) | Fase 4 | Endnu ikke rekrutterende | 114 | Mitoxantron som sporstof til lymfeknudeafbildning ved thyreoideakirurgi (billeddannelse, ikke antitumorbehandling) |

---

## Litteraturevidens

| PMID | År | Type | Tidsskrift | Hovedresultater |
|------|-----|------|------|---------|
| [39952083](https://pubmed.ncbi.nlm.nih.gov/39952083/) | 2025 | Fase 1b-studie | Oral Oncology | Liposomalt mitoxantron (PLM60) ved recidiverende/metastatisk planocellulært hoved- og halskarcinom |
| [8922205](https://pubmed.ncbi.nlm.nih.gov/8922205/) | 1996 | Fase II | Annals of Oncology | EORTC-studie af mitoxantron ved adenoid cystisk karcinom i hoved og hals |
| [11290867](https://pubmed.ncbi.nlm.nih.gov/11290867/) | 2001 | Fase II | Anti-Cancer Drugs | Ifosfamid + mitoxantron ved recidiverende/metastatisk planocellulært hoved- og halskarcinom |
| [12045460](https://pubmed.ncbi.nlm.nih.gov/12045460/) | 2002 | Fase II | Anti-Cancer Drugs | Mitoxantron + cisplatin ved recidiverende/metastatiske spytkirtelmaligniteter (14 patienter) |
| [1650529](https://pubmed.ncbi.nlm.nih.gov/1650529/) | 1991 | Fase II | Am J Clin Oncol | Mitoxantron ved hoved- og halskarcinom (19 patienter) |
| [8418245](https://pubmed.ncbi.nlm.nih.gov/8418245/) | 1993 | Fase II | J Clin Oncol | Multicenterstudie af mitoxantron ved fremskredent nasopharyngealt karcinom i Sydøstasien |
| [6511243](https://pubmed.ncbi.nlm.nih.gov/6511243/) | 1984 | Fase II | Investigational New Drugs | Southwest Oncology Group: ingen betydelig antitumoraktivitet ved planocellulært hoved- og halskarcinom |
| [34659878](https://pubmed.ncbi.nlm.nih.gov/34659878/) | 2021 | Review | Am J Cancer Res | Systemiske behandlinger af adenoid cystisk karcinom i spytkirtler |
| [31324333](https://pubmed.ncbi.nlm.nih.gov/31324333/) | 2019 | Systematisk review | Bulletin du Cancer | Systemisk behandling af metastatisk/lokalt recidiverende adenoid cystisk karcinom i hoved og hals |
| [3512224](https://pubmed.ncbi.nlm.nih.gov/3512224/) | 1986 | Review | Drug Intell Clin Pharm | Generel oversigt over mitoxantron; en vis aktivitet ved hoved- og halskræft |

---

## Information om markedet i Danmark

| Markedsføringstilladelsesnummer | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28103041098 | Mitoxantron "Ebewe" | Koncentrat til infusionsvæske, opløsning | Indikationstekst ikke angivet i de indsamlede data |

Der er i alt 1 gyldig markedsføringstilladelse (enkeltstof). Lægemiddelformen er injicerbar. Den liposomale formulering, som er anvendt i de nyere studier, fremgår ikke af de danske tilladelser.

---

## Cytotoksicitet

| Punkt | Indhold |
|------|------|
| Cytotoksicitetsklassifikation | Konventionelt cytotoksisk middel (antracendion, topoisomerase II-hæmmer) |
| Risiko for myelosuppression | Høj (leukopeni og trombocytopeni er de væsentligste toksiciteter i fase II-studierne) |
| Emetogenicitetsklassifikation | Lav til moderat |
| Monitoreringsparametre | Fuldt blodbillede med differentialtælling, lever- og nyrefunktion; hjertefunktion (LVEF) på grund af kardiotoksicitet |
| Håndteringsbeskyttelse | Skal håndteres efter gældende regler for cytostatika |

Se i øvrigt produktresuméet (SmPC) for advarsler og forsigtighedsregler.

---

## Sikkerhedsovervejelser

- **Sygdomme med kontraindikationsforbindelse i vidensgrafen** (ikke fra produktteksten): leversvigt, leversygdom, galdeblæresygdom, epilepsi, trombocytopeni, neutropeni, agranulocytose, anæmi (herunder makrocytær), leukopeni, hjertesvigt, infektionssygdomme (herunder svampeinfektion og dermatofytose). Disse skal verificeres mod produktresuméet.
- **Lægemiddelinteraktioner:** 446 interaktioner er registreret. Blandt de viste er dolasetron klassificeret som **større** (Major); clarithromycin, eliglustat og rolapitant som **moderate**; levofloxacin som **mindre**. Flere øvrige (f.eks. metformin, lansoprazol, amphotericin B, hydrocortison, morphin, omeprazol) har uklassificeret niveau.

Advarsler og kontraindikationer fra godkendt produktresumé er ikke tilgængelige i de indsamlede data. Se det godkendte produktresumé (SmPC) for fuldstændige sikkerhedsoplysninger.

---

## Konklusion og næste skridt

**Beslutning:**
- **Øvre luftvejs- og fordøjelseskanalstumor (modellens førstevalg): Hold** – kun forskningsspørgsmål, ingen registrerede forsøg, og evidensen overlapper med hoved- og halskræft.
- **Hoved- og halskræft: Proceed with Guardrails**

**Begrundelse:**
- Der findes ældre fase II-data med blandede resultater samt nyere fase Ib/II-data med liposomalt mitoxantron. Et fase 3-forsøg (NCT05717764) er planlagt, men ikke startet. Evidensen er konsistent, men ikke bekræftet af afsluttede randomiserede data.
- De øvrige forudsigelser har svagere støtte: småcellet lungekarcinom (Hold, kun præklinisk), primært pulmonalt lymfom (begrænset retrospektiv erfaring), kronisk myeloid leukæmi (relevant kun ved blastkrise) samt fire forudsigelser uden evidens eller med usandsynlig rationale (bl.a. blæreekstrofi, der sandsynligvis er en falsk grafbaseret forudsigelse).

**For at komme videre kræves:**
- Resultater fra det planlagte fase 3-forsøg (NCT05717764) eller andre randomiserede data
- Afklaring af, om resultater med liposomalt mitoxantron kan overføres til den konventionelle formulering, der er markedsført i Danmark
- Detaljerede mekanismedata (MOA) fra DrugBank
- Advarsler og kontraindikationer fra produktresuméet hos Lægemiddelstyrelsen
- Plan for hæmatologisk og kardiel monitorering (inkl. kumulativ dosisgrænse)
- Vurdering af interaktionsrisici ved samtidig medicinering
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

