---
layout: default
title: Ceftaroline Fosamil
parent: Kun modelforudsigelse (L5)
nav_order: 98
evidence_level: L5
indication_count: 10
---

# Ceftaroline Fosamil
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

# Ceftaroline fosamil: Fra bakterielle infektioner til reumatoid artritis

## Sammenfatning på en sætning

Ceftaroline fosamil (handelsnavn Zinforo) er en femte-generations cephalosporin-antibiotikum, godkendt i EU til akutte bakterielle hud- og hudbindevevsinfektioner (ABSSSI) og samfundserhvervede bakterielle pneumonier (CABP).
TxGNN-modellen forudsiger, at det kan være effektivt mod **reumatoid artritis**, med en høj modelsikkerhedsscore på **98.20%**.
Denne forudsigelse understøttes imidlertid i øjeblikket af **0 kliniske forsøg** og **0 relevante publikationer** — og analysen af mekanismen tyder stærkt på, at dette er en falsk positiv inden for vidensgrafs topologi snarere end en ægte genbrugsmulighed.

---

## Hurtigt overblik

| Parameter | Værdi |
|-----------|-------|
| Original indikation | Akutte bakterielle hud- og hudbindevevsinfektioner (ABSSSI); samfundserhvervede bakterielle pneumonier (CABP) |
| Forudsagt ny indikation | Reumatoid artritis |
| TxGNN-forudsigelsesscore | 98.20% |
| Bevisniveau | L5 |
| Markedsstatus i Danmark | Ikke markedsført |
| Antal markedsføringstilladelser | 0 |
| Anbefalet beslutning | Afvent |

---

## Hvorfor er denne forudsigelse rimelig?

I øjeblikket er detaljerede mekanistiske data ikke tilgængelige i denne evidenspakke. Baseret på kendt farmakologi er ceftaroline fosamil et β-lactam-antibiotikum, hvis mekanisme centrerer sig omkring hæmning af bakteriel cellevægssyntese via binding til penicillin-bindende proteiner (PBP'er) — især PBP2a fra MRSA — hvorved det opnår bred-spektrum baktericidal aktivitet mod Gram-positive og udvalgte Gram-negative patogener.

Reumatoid artritis (RA) er en autoimmun lidelse drevet af dysreguleret T- og B-celle-aktivering, synovial hyperplasi og en pro-inflammatorisk cytokinkaskade domineret af TNF-α og IL-6. Der er ingen kendt farmakologisk vej, hvorigennem PBP-binding eller cellevægssyntesehæmning ville modulere autoimmun inflammation. I modsætning til tetracykliner eller makrolider — som har pleiotrope anti-inflammatoriske egenskaber uafhængigt af deres antimikrobielle virkninger — har β-lactam-antibiotika ingen etableret immunomodul-mekanisme relevant for RA-patofysiologi.

Den mest plausible forklaring på denne høje TxGNN-score er en indirekte vidensgrafs-forbindelse (KG): ceftaroline-knuder knyttet til "behandling af septisk artritis" eller "ledinfektion" er topologisk tæt på RA-knuder inden for grafen, hvilket producerer en artifaktuelt høj-konfidensforudsigelse. Dette er en kendt begrænsning ved grafbaserede modeller, når infektionssygdomsknuder deler strukturel nærhed med inflammatoriske ledsygdomsknuder. Forudsigelsen bør behandles som en **topologi-baseret falsk positiv** i afventning af modsatrettede eksperimentelle beviser.

---

## Bevis fra kliniske forsøg

Der er i øjeblikket ingen relaterede kliniske forsøg registreret for ceftaroline fosamil ved reumatoid artritis.

---

## Litteraturbevis

Der er i øjeblikket ingen relateret litteratur tilgængelig for ceftaroline fosamil ved reumatoid artritis.

---

## Markedsinformation for Danmark

Ceftaroline fosamil har i øjeblikket ingen markedsføringstilladelse aktiv på det danske marked. Lægemidlet har en centraliseret EMA-godkendelse (Zinforo, EU/1/12/787/001-004), der er gyldig på tværs af EU/EØS; det er imidlertid ikke kommercielt distribueret i Danmark på tidspunktet for denne rapport.

| Markedsføringstilladelsesnummer | Produktnavn | Doseringsform | Godkendt indikation |
|------|------|------|------|
| EU/1/12/787 (EMA — ikke aktivt markedsført i DK) | Zinforo | Pulver til koncentrat til infusion (600 mg) | Akutte bakterielle hud- og hudbindevevsinfektioner; samfundserhvervede bakterielle pneumonier hos voksne |

---

## Sikkerhedsovervejelser

Detaljerede dansk/TFDA-SmPC-advarsler og kontraindikationer var ikke tilgængelige i denne evidenspakke. Se venligst det godkendte produktresumé (SmPC) for Zinforo — tilgængeligt via [EMA-produktsiden](https://www.ema.europa.eu/en/medicines/human/EPAR/zinforo) — for fuldstændig sikkerhedsinformation, herunder overfølsomhedsreaktioner, *Clostridioides difficile*-associeret diarré, hæmatologiske virkninger (hæmolytisk anæmi, neutropeni) og krav til nyrerelateret dosistilpasning.

---

## Konklusion og næste trin

**Beslutning: Afvent**

**Begrundelse:**
TxGNN-modellen tildeler en høj numerisk score (98.20%), men dette er næsten sikkert en vidensgrafs-topologi-artefakt drevet af nærhed mellem infektiøs artritis og inflammatorisk artritis-knuder — ikke et ægt farmakologisk signal. Ceftaroline fosamil har ingen kendt mekanisme relevant for autoimmun eller degenerativ ledsygdom, og den fuldstændige mangel på understøttende kliniske forsøg eller peer-reviewed litteratur bekræfter denne vurdering. Fremskridt ville ikke opfylde nogen videnskabelig eller regulatorisk standard for et genbrugsprogram.

**For at gå videre fra Afvent ville følgende være nødvendigt:**

- **Mekanistisk bevis**: Identifikation af en plausibel biologisk mekanisme, der forbinder PBP-binding (eller enhver off-target-virkning af ceftaroline) til RA-patofysiologi — i øjeblikket findes ingen i den udgivne litteratur.
- **Eksperimentelle in vitro/in vivo-data**: Demonstration af anti-inflammatorisk aktivitet i validerede RA-modeller (f.eks. CIA-musemodel, synoviacyt-assays).
- **KG-revision**: Gennemgang af kantestien i vidensgrafen, der genererer denne forudsigelse, for at bekræfte eller afvise den formodede falske-positive topologi.
- **Sikkerhedsdata**: Hentning og gennemgang af det fulde Zinforo-SmPC, herunder immunologiske virkninger og eventuelle signaler efter markedsføring relevant for inflammatoriske tilstande.
- **Præcisering af klinisk kontekst**: De 2 PubMed-publikationer hentet (PMID'er [27530754](https://pubmed.ncbi.nlm.nih.gov/27530754/) og [23312602](https://pubmed.ncbi.nlm.nih.gov/23312602/)) vedrører *osteoartikulær infektions*-behandling — ikke RA eller degenerativ ledsygdom — og udgør ikke bevis for nogen af de forudsagte ikke-infektiøse indikationer i denne pakke.

> **Ansvarsfraskrivelse**: Denne rapport er udelukkende til forskningsmæssig reference og udgør ikke medicinsk rådgivning. Alle lægemiddelgenbrugskandidater kræver klinisk validering før anvendelse.

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

