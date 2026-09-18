---
layout: default
title: Miglustat
parent: Kun modelforudsigelse (L5)
nav_order: 293
evidence_level: L5
indication_count: 10
---

# Miglustat
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

# Miglustat: Fra Gauchers sygdom til autosomal ichthyosis-syndrom med fatal sygdomsforløb

## Sammenfatning i en sætning

Miglustat (Zavesca®) er en glukosylceramidsyntase (GCS)-hæmmer godkendt i EU til Gauchers sygdom type 1 og Niemann-Pick-sygdom type C (NPC), der virker via substratreduktionsterapi (SRT) for at begrænse ophobning af toksiske glykosfingolipi­der.
TxGNN-modellen forudsiger, at det kan være effektivt til **autosomal ichthyosis-syndrom med fatal sygdomsforløb** med en forudsigelsesscore på **99.83%**; imidlertid er der **ikke identificeret kliniske forsøg eller understøttende publikationer** for denne indikation, og det mekanistiske rationale anses for svagt.
Dette er en multi-indikations-evidenspakke (TW-DB00419-multi), der også dækker kolesterylesterlageringssygdom, Krabbe-sygdom, metakromatisk leukodystrofi og Wolman-sygdom — hvoraf **metakromatisk leukodystrofi har det stærkeste mekanistiske rationale** og anbefales til aktivt opfølgning.

---

## Hurtig oversigt

| Emne | Indhold |
|------|---------|
| Oprindelig indikation | Gauchers sygdom type 1; Niemann-Pick-sygdom type C (NPC) |
| Forudsagt ny indikation (Top Rank) | Autosomal ichthyosis-syndrom med fatal sygdomsforløb |
| TxGNN-forudsigelsesscore | 99.83% |
| Evidensniveau | L5 — modelforudsigelse alene; ingen kliniske forsøg eller litteratur identificeret |
| Markedsstatus i Danmark | Ikke fundet i database — se note nedenfor |
| Antal markedsføringstilladelser | 0 (databasepost) |
| Anbefalet beslutning | **Vent** (topforudsigelse); **Fortsæt med sikkerhed** (metakromatisk leukodystrofi, rank 4) |

> **⚠️ Registreringsmærke:** Miglustat (Zavesca®) har en centraliseret EU-markedsføringstilladelse (EU/1/02/237) tildelt af Det Europæiske Lægemiddelagentur (EMA), som er gyldig i alle EU-medlemsstater, herunder Danmark. Fraværet af registreringer i den aktuelle database afspejler sandsynligvis et hul i dataindsamlingen snarere end et egentligt manglende autorisation. Sundhedsfagfolk bør konsultere EMA-produktsiden og det aktuelle danske produktinformationsblad (SmPC) for pålidelig registreringsstatus, før de drager nogen lovmæssige konklusioner.

---

## Oversigt over multi-indikations-forudsigelse

Denne evidenspakke indeholder fem unikke forudsagte indikationer (duplikerede poster i rank 1–10 er blevet deduplikeret). Alle er inden for området lysosomal lagringssygdom / sfingolipidmetabolisme-sygdom — i overensstemmelse med miglustat's kendt virkemåde.

| Rank | Forudsagt indikation | TxGNN-score | Evidensniveau | Anbefaling |
|------|---------------------|-------------|----------------|------------|
| 1 | Autosomal ichthyosis-syndrom med fatal sygdomsforløb | 99.83% | L5 | Vent |
| 2 | Kolesterylesterlageringssygdom (CESD) | 99.82% | L5 | Forskningsspørgsmål |
| 3 | Krabbe-sygdom | 99.78% | L4 | Forskningsspørgsmål |
| **4** | **Metakromatisk leukodystrofi (MLD)** | **99.77%** | **L4** | **Fortsæt med sikkerhed** |
| 5 | Wolman-sygdom med hypolipoproteinæmi og acanthocytose | 99.76% | L5 | Vent |

> **Redaktionel note:** Selvom TxGNN-scorerne er næsten identiske på tværs af alle fem indikationer (forskel < 0.1%), varierer kvaliteten af det mekanistiske rationale væsentligt. Metakromatisk leukodystrofi (rank 4) har den klareste forbindelse på stofvejsniveauet til miglustat og den højeste brugbare anbefaling i dette sæt.

---

## Hvorfor er denne forudsigelse rimelig?

Detaljerede data om virkningsmekanisme blev ikke hentet fra DrugBank i denne evidenspakke (datahul DG002). Baseret på etableret farmakologisk viden er miglustat en **iminosukker og konkurrencedygtigt inhibitor af glukosylceramidsyntase (GCS)** — enzymet ansvarlig for det første forpligtende trin i glykosfingolipi­dsyntesen. Ved at reducere substrattransporten til GSL-syntesevejenen sænker miglustat ophobningen af glukocerebrosider og nedstrøms sfingolipider, der ellers ville overbelaste defekt lysosomal enzymer. Kritisk set har miglustat demonstreret **blod-hjerne-barrieregennemtrængning (BBB)**, hvilket gør det unikt relevant for CNS-manifestationer af lysosomal lagringssygdomme.

**Hvorfor topforudsigelsen (autosomal ichthyosis-syndrom) er mekanistisk svag:** Nogle medfødte ichthyoser — især Sjögren-Larsson-syndrom — involverer lipidmetabolisme­abnormiteter (ALDH3A2-mutationer, der påvirker fedtaldehydafbygning). Imidlertid krydser denne metaboliske vej kun tangentielt med miglustat's GCS-inhibitionsvej og uden et delt enzymatisk trin. Betegnelsen »fatal sygdomsforløb« indikerer yderligere et ekstremt fænotype, hvor substratreduktionsterapi ikke tilbyder nogen etableret begrundelse.

**Hvorfor andre indikationer i denne pakke viser stærkere begrundelse:** Metakromatisk leukodystrofi (MLD, ARSA-mangel) forårsager sulfatidophobning via den samme glykosfingolipi­dsyntesevej, som miglustat direkte undertrykker — GCS-inhibition reducerer opstrøms galaktocerebrosid-substrat­tilgængelighed og begrænser således sulfatidproduktion. Miglustat's blod-hjerne-barrieregennemtrængning er en yderligere fordel for denne CNS-demyeliniserende sygdom, og konceptet er blevet udforsket i ARSA-knockout-musemodeller. Krabbe-sygdom (GALC-mangel, psychosin-ophobning) deler glykosfingolipi­dvej-nærhed med understøttende data fra Twitcher-musemodellen. Kolesterylesterlageringssygdom og Wolman-sygdom involverer lysosomal dysfunktion, der overlapper patologisk med NPC — miglustat's godkendt indikation — selvom den enzymatiske forbindelse gennem LAL/LIPA-vejene er indirekte.

---

## Bevis fra kliniske forsøg

Der er ikke identificeret kliniske forsøg for nogen af de fem forudsagte indikationer (autosomal ichthyosis-syndrom, kolesterylesterlageringssygdom, Krabbe-sygdom, metakromatisk leukodystrofi eller Wolman-sygdom med hypolipoproteinæmi og acanthocytose) i søgning i ClinicalTrials.gov, ICTRP eller relaterede registre udført på 2026-03-10.

> **Anbefaling:** En bredere litteratur- og forsøgssøgning ved hjælp af sygdomssynonymer (f.eks. »sulfatidlipidose« og »ARSA-mangel« for MLD; »globoid celle-leukodystrofi« for Krabbe-sygdom; »LAL-mangel« for CESD/Wolman) og udvidede søgeperioder anbefales, før man konkluderer, at der ikke findes nogen bevis.

---

## Litteraturbevis

Der er ikke identificeret relevant publikationer, der forbinder miglustat med nogen af de fem forudsagte indikationer i PubMed-søgningen udført på 2026-03-10.

> **Anbefaling:** Som ovenfor kan udvidede søgninger ved hjælp af MeSH-termer, sygdomssynonymer og bredere glykosfingolipi­d/SRT-relaterede forespørgsler give relevant præklinisk litteratur, især for MLD og Krabbe-sygdom.

---

## Markedsinformation for Danmark

Ingen markedsføringstilladelsesregistreringer for miglustat blev returneret fra Lægemiddelstyrelsens databasesøgning.

> Som nævnt ovenfor er dette sandsynligvis et hul i dataindsamlingen. Zavesca® (miglustat, 100 mg kapsler) har centraliseret EU-tilladelse EU/1/02/237 (Actelion/Janssen) til Gauchers sygdom type 1 og stabilisering af NPC-neurologiske manifestationer; denne tilladelse er direkte gyldig i Danmark. Læger bør verificere aktuel dansk produktinformation via EMA's produktside eller Lægemiddelstyrelsens Medicinprodukter-database.

---

## Sikkerhedshensyn

Ingen sikkerhedsdata (vigtige advarsler, kontraindikationer eller lægemiddelinteraktioner) blev hentet for miglustat under bevisindsamling for denne evidenspakke.

Se venligst det godkendt **Produktinformationsblad (SmPC) for Zavesca®** for fuldstændig sikkerhedsinformation før enhver klinisk eller forskningsmæssig brug.

---

## Konklusion og næste skridt

### Primær forudsigelse (Rank 1 — Autosomal ichthyosis-syndrom med fatal sygdomsforløb)

**Beslutning: Vent**

**Begrundelse:**
Det mekanistiske link mellem miglustat's GCS-inhibition og autosomal ichthyosis er fjernt og ikke understøttet af nogen klinisk forsøg eller publiceret litteratur (kun L5-bevis). Betegnelsen »fatal sygdomsforløb« og fraværet af et plausibelt SRT-interventionsrationale gør dette til en ugunstig kandidat for udvikling på dette tidspunkt.

---

### Prioriterings­opfølgnings­anbefaling — Metakromatisk leukodystrofi (MLD, Rank 4)

**Beslutning: Fortsæt med sikkerhed**

**Begrundelse:**
MLD er mekanistisk den mest overbevisende indikation i denne pakke. Miglustat's direkte undertrykkelse af opstrøms glykosfingolipi­dsubstrat og dets etablerede blod-hjerne-barrieregennemtrængning giver en biologisk kohærent begrundelse for MLD's CNS-demyeliniserende fænotype, understøttet af prækliniske dyremodels data (L4-bevis).

**For at fortsætte er følgende nødvendigt:**

- **Luk datahullerne:** Hent miglustat's DrugBank MOA-post (DG002) og den danske/EMA SmPC-sikkerhedsprofil (DG001)
- **Udvidet litteratursøgning:** Brug bredere MeSH-termer (»arylsulfatase A-mangel«, »sulfatidlipidose«, »SRT-leukodystrofi«) til at identificere publiceret prækliniske eller tidlig-fase data
- **Prøveregistrering-gensøgning:** Søg ClinicalTrials.gov med NCT-søgningstermer for "miglustat AND leukodystrophy" og "substrate reduction AND MLD"
- **Lovmæssig vejgennemgang:** Vurder, om MLD's designering som sjælden sygdom i EU (Forordning EF 141/2000) åbner accelererede lovmæssige veje for en ansøgning om godkendelse til ny indikation
- **Specialistconsultation:** Inddraging af danske eller nordiske specialister inden for lysosomal lagringssygdomme (f.eks. på Københavns Universitetshospital – Rigshospitalet) for at vurdere klinisk gennemførlighed og patientpopulationsstørrelse
- **Sammenlignende sammenhæng:** Gennemgang af arylsulfatase A-genterapi godkendelser (Libmeldy/atidarsagene autotemcel, EMA godkendt 2020) for at forstå nuværende behandlingsstandard og hvor oral SRT kan supplere eller tjene patienter, der ikke er berettigede til genterapi

---

*Denne rapport er genereret til forskningsreferenceformål alene og udgør ikke medicinske råd. Alle kandidater til lægemiddelhyldning kræver klinisk validering før enhver terapeutisk anvendelse.*
*Datakutoff: 2026-04-04 | Kandidat-id: TW-DB00419-multi | Evidenspakkeverision: v4*

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

