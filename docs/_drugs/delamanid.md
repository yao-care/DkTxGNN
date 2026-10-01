---
layout: default
title: Delamanid
parent: Moderat evidens (L3-L4)
nav_order: 136
evidence_level: L4
indication_count: 10
---

# Delamanid
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

# Delamanid: Fra multiresistent tuberkulose til bovin tuberkulose

## Resumé

Delamanid er et tuberkulosemiddel, der markedsføres i Danmark som Deltyba og ifølge evidensgrundlaget bruges mod aktiv multiresistent tuberkulose (MDR-TB).
TxGNN-modellen forudsiger, at det kan virke mod **bovin tuberkulose** (*Mycobacterium bovis*), men der er kun **1 publikation** og **ingen kliniske forsøg** for netop denne indikation.
Den bedst understøttede forudsigelse i samme pakke er **inaktiv (latent) tuberkulose**, hvor et fase 3-forsøg med 5.832 deltagere er i gang.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Aktiv multiresistent tuberkulose (fra evidensgrundlaget; indikationsteksten i den danske registrering er ikke oplyst) |
| Forudsagt ny indikation | Tuberkulose, bovin (*M. bovis*) |
| TxGNN-forudsigelsesscore | 99,91 % |
| Evidensniveau | L4 (bovin TB). Til sammenligning: L1 for inaktiv tuberkulose |
| Status på det danske marked | Markedsført |
| Antal markedsføringstilladelser | 1 |
| Anbefalet beslutning | Hold (bovin TB). Proceed with Guardrails for inaktiv tuberkulose |

**Øvrige forudsigelser i samme pakke:**

| Forudsagt indikation | Evidensniveau | Anbefaling |
|------|------|------|
| Inaktiv tuberkulose (latent TB-infektion) | L1 | Proceed with Guardrails |
| Tuberkulom | L4 | Hold |
| Tuberkuløs ascites | L5 | Hold |
| Aviær tuberkulose | L5 | Hold |

---

## Hvorfor er forudsigelsen rimelig?

Der foreligger ikke detaljerede mekanismedata i Evidence Pack. Ud fra almen farmakologi er delamanid et nitroimidazooxazol-prodrug, der aktiveres af det F420-afhængige enzym Ddn i *Mycobacterium tuberculosis*. Når det er aktiveret, hæmmer det syntesen af methoxy- og keto-mykolsyrer, som er vigtige for bakteriens cellevæg.

*M. bovis* tilhører samme kompleks som *M. tuberculosis*. Zoonotisk tuberkulose hos mennesker forventes derfor at være følsom over for delamanid via samme aktiveringsvej. *M. bovis* er desuden naturligt resistent over for pyrazinamid, hvilket gør alternative midler interessante. Der er dog ingen delamanid-specifikke følsomheds- eller kliniske data, så sammenhængen er indtil videre kun teoretisk.

For inaktiv tuberkulose er mekanismen den samme. Ved forebyggende behandling af kontakter til MDR-TB-patienter forventes isoniazid og rifamyciner at svigte, og delamanid kan være et alternativ. Det er en indikationsudvidelse (forebyggelse), ikke en ny mekanisme.

Forudsigelserne for tuberkuløs ascites og tuberkulom hviler på samme mekanisme, men uden egne data. For tuberkulom afhænger virkningen desuden af tilstrækkelig penetration til centralnervesystemet, som ikke er dokumenteret. Aviær tuberkulose skyldes *M. avium*-komplekset, som generelt ikke er følsomt over for delamanid, så koblingen er svag.

---

## Evidens fra kliniske forsøg

For bovin tuberkulose er der aktuelt ingen relaterede kliniske forsøg registreret.

Følgende forsøg er registreret under den bedst understøttede forudsigelse, inaktiv tuberkulose:

| Forsøgsnummer | Fase | Status | Deltagere | Hovedpunkter |
|---------|------|------|------|---------|
| [NCT03568383](https://clinicaltrials.gov/study/NCT03568383) | Fase 3 | Aktiv, rekrutterer ikke | 5.832 | PHOENIx MDR-TB: 26 ugers delamanid sammenlignet med isoniazid til forebyggelse af aktiv TB hos højrisiko-husstandskontakter til MDR-TB-patienter. Slutdato forventes januar 2027. Der foreligger endnu ingen bekræftede effektresultater. |
| [NCT05766267](https://clinicaltrials.gov/study/NCT05766267) | Fase 2/3 | Aktiv, rekrutterer ikke | 288 | CRUSH-TB: 17 ugers regimer med bedaquilin, moxifloxacin og pyrazinamid plus rifabutin eller delamanid sammenlignet med standardbehandling i 6 måneder ved lungetuberkulose. Det er indirekte evidens, da populationen har aktiv sygdom. |

---

## Litteraturevidens

| PMID | År | Type | Tidsskrift | Hovedpunkter |
|------|-----|------|------|---------|
| [39487429](https://pubmed.ncbi.nlm.nih.gov/39487429/) | 2024 | Kohorte | BMC Genomics | Helgenomsekventering af *M. bovis*-isolater fra zoonotisk TB: genetisk diversitet og lægemiddelresistens. Ingen delamanid-specifikke data. (Bovin TB) |
| [38003836](https://pubmed.ncbi.nlm.nih.gov/38003836/) | 2023 | Review | Pathogens | Behandling og forebyggelse af lægemiddelresistent TB hos børn. Nævner delamanid og bedaquilin. (Inaktiv TB) |
| [36915977](https://pubmed.ncbi.nlm.nih.gov/36915977/) | 2022 | Review | J Zhejiang Univ Med Sci | Fremskridt i diagnostik og behandling af latent tuberkuloseinfektion. (Inaktiv TB) |
| [33837535](https://pubmed.ncbi.nlm.nih.gov/33837535/) | 2021 | Review | Clin Pharmacol Ther | Behandling af latent og aktiv TB. (Inaktiv TB) |
| [29580819](https://pubmed.ncbi.nlm.nih.gov/29580819/) | 2018 | Review | Lancet Infect Dis | Nye lægemidler, behandlingsregimer og værtsrettet terapi ved TB. (Inaktiv TB) |
| [24100880](https://pubmed.ncbi.nlm.nih.gov/24100880/) | 2013 | Review | Curr Opin HIV AIDS | Pipeline for TB-lægemidler, herunder regimer til latent TB-infektion. (Inaktiv TB) |
| [33400226](https://pubmed.ncbi.nlm.nih.gov/33400226/) | 2021 | Review | Acta Neurol Belg | Opdatering om neurotuberkulose. Ingen delamanid-specifikke data. (Tuberkulom) |

Litteraturen består udelukkende af kohortestudier og reviews. Der er ingen randomiserede studier med delamanid ved bovin TB.

---

## Oplysninger om det danske marked

| Markedsføringstilladelsesnummer | Produktnavn | Lægemiddelform | Indehaver |
|---------|------|------|-----------|
| 28106493520 | Deltyba | Dispergible tabletter (oral) | Otsuka Novel Products GmbH |

Den godkendte indikationstekst er ikke tilgængelig i de leverede data.

---

## Sikkerhedsovervejelser

Der er ikke leveret data om advarsler og kontraindikationer fra Lægemiddelstyrelsen. Se det godkendte produktresumé (SmPC) for sikkerhedsoplysninger.

- **Lægemiddelinteraktioner**: Ingen interaktioner fundet i de leverede data.
- **QT-forlængelse**: Forsøgsvurderingen af PHOENIx peger på QT-forlængelse som et centralt sikkerhedsspørgsmål, især ved samtidig brug af andre QT-aktive lægemidler.

---

## Konklusion og næste skridt

**Beslutning: Hold (bovin tuberkulose)**

**Begrundelse:**
- Forudsigelsen for bovin TB er biologisk plausibel, men understøttes kun af en genomisk kohorteundersøgelse uden delamanid-data (L4). Scoren på 99,91 % er ikke i sig selv klinisk evidens.
- Inaktiv tuberkulose (L1, Proceed with Guardrails) har et fase 3-forsøg (NCT03568383), men uden bekræftede resultater endnu. Det bør derfor følges, indtil resultaterne foreligger (forventet 2027).

**For at komme videre kræves:**
- Mekanismedata (MOA) fra DrugBank.
- Advarsler og kontraindikationer fra Lægemiddelstyrelsens produktresumé (blokerende mangel for sikkerhedsscreening).
- Delamanid-specifikke *in vitro*-følsomhedsdata for *M. bovis*.
- Resultater fra PHOENIx MDR-TB (NCT03568383) og en QT-overvågningsplan for samtidig brug af QT-aktive lægemidler.
- Data om penetration til centralnervesystemet, hvis tuberkulom skal vurderes videre.

*Resultaterne er kun til forskningsbrug og udgør ikke medicinsk rådgivning. Kandidater til lægemiddelomdefinering kræver klinisk validering, før de kan anvendes.*
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

