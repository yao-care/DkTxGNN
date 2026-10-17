---
layout: default
title: Delamanid
parent: Høj evidens (L1-L2)
nav_order: 248
evidence_level: L2
indication_count: 10
last_modified_at: 2026-10-14
description: "Delamanid: forudsagt ny indikation Inaktiv tuberkulose (evidensniveau L2). Oprindelig indikation: Multiresistent tuberkulose"
---

# Delamanid
{: .fs-9 }

Evidensniveau: **L2** | Forudsagte indikationer: **10** stk.
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

# Delamanid: Fra multiresistent tuberkulose til inaktiv tuberkulose

## Resumé i én sætning

Delamanid er et antibakterielt middel mod tuberkulose, oprindeligt anvendt til behandling af **multiresistent tuberkulose (MDR-TB)**. TxGNN-modellen forudsiger, at lægemidlet også kan være virksomt mod **inaktiv tuberkulose**, og forudsigelsen understøttes af **1 klinisk fase 2/3-forsøg** og **20 publikationer** (hovedsageligt oversigtsartikler).

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Multiresistent tuberkulose |
| Forudsagt ny indikation | Inaktiv tuberkulose |
| TxGNN-forudsigelsesscore | 99,91 % |
| Evidensniveau | L2 |
| Markedsstatus i Danmark | Markedsført |
| Antal markedsføringstilladelser | 1 |
| Anbefalet beslutning | Proceed with Guardrails (fortsæt med sikkerhedsforanstaltninger) |

Bemærk: Den oprindelige indikation er hentet fra den vidensgraf, som TxGNN bygger på, da den danske tilladelse ikke indeholder en indikationstekst.

---

## Hvorfor er forudsigelsen rimelig?

Delamanid er et nitroimidazol-prodrug. Det aktiveres af et enzym i *Mycobacterium tuberculosis* (deazaflavin-afhængig nitroreduktase, Ddn, F420-afhængig). Den aktive metabolit hæmmer syntesen af mykolsyrer (methoxy- og keto-mykolsyrer) og svækker dermed bakteriens cellevæg. Oplysninger om virkningsmekanisme manglede i de data, der er indsamlet til denne rapport, men mekanismen er velbeskrevet i litteraturen.

MDR-TB og inaktiv tuberkulose skyldes samme bakterie. Forsøget CRUSH-TB (NCT05766267) undersøger kortere regimer, hvor delamanid indgår som en af to mulige komponenter, ved lungetuberkulose. Det er en tæt, men ikke fuldstændig overensstemmelse med den forudsagte indikation.

**Forbehold:** Inaktiv (latent eller ikke-replikerende) tuberkulose adskiller sig fra den aktive lungesygdom, der studeres i forsøget. Delamanids aktivitet mod ikke-replikerende bakterier og brugen ved latent TB (fx kontakter til MDR-TB-patienter) understøttes kun indirekte af de foreliggende data.

**Øvrige forudsigelser:** Modellen angiver også andre tuberkuloserelaterede sygdomme med næsten samme score. Evidensen for disse er svagere:
- **Bovin tuberkulose** (L4): Kun ét molekylært epidemiologisk studie af *M. bovis*-isolater. Delamanids følsomhed er ikke påvist.
- **Tuberkuloma** (L4): Kun en generel oversigtsartikel om neurotuberkulose. Delamanids penetration til centralnervesystemet er ikke belyst.
- **Tuberkuløs ascites** (L5): Kun modelforudsigelse.
- **Aviær tuberkulose** (L5): Forårsages af *M. avium*, hvor aktivering via Ddn/F420 ikke er påvist. Mekanismen er tvivlsom.

---

## Klinisk evidens

| Forsøgsnummer | Fase | Status | Antal deltagere | Hovedresultater |
|---------|------|------|------|---------|
| [NCT05766267](https://clinicaltrials.gov/study/NCT05766267) | Fase 2/3 | Aktiv, ikke rekrutterende | 288 | CRUSH-TB: undersøger, om 17-ugers regimer med bedaquilin, moxifloxacin og pyrazinamid plus enten rifabutin eller delamanid er lige så effektive som standardbehandling over seks måneder ved lungetuberkulose. Forventet afslutning: 31. december 2027. Resultater foreligger endnu ikke. |

---

## Litteraturevidens

Det er alene oversigtsartikler og prækliniske arbejder, og ingen af dem er randomiserede forsøg. Nedenfor er de mest relevante.

| PMID | År | Type | Tidsskrift | Hovedresultater |
|------|-----|------|------|---------|
| [38003836](https://pubmed.ncbi.nlm.nih.gov/38003836/) | 2023 | Oversigtsartikel | Pathogens | Nyere lægemidler som bedaquilin og delamanid har styrket behandlingen af lægemiddelresistent TB hos børn. |
| [36982277](https://pubmed.ncbi.nlm.nih.gov/36982277/) | 2023 | Oversigtsartikel | Int J Mol Sci | Patogenese, nuværende behandlingsregimer og nye lægemiddelmål ved tuberkulose. |
| [33837535](https://pubmed.ncbi.nlm.nih.gov/33837535/) | 2021 | Oversigtsartikel | Clin Pharmacol Ther | Behandling af latent og aktiv TB samt lægemidlers bakteriedræbende og sterilisende virkning. |
| [33319660](https://pubmed.ncbi.nlm.nih.gov/33319660/) | 2021 | Oversigtsartikel | Curr Top Med Chem | Opdatering om resistensmekanismer, nyere anti-TB-lægemidler og behandlingsregimer. |
| [36915977](https://pubmed.ncbi.nlm.nih.gov/36915977/) | 2022 | Oversigtsartikel | J Zhejiang Univ Med Sci | Fremskridt i diagnostik og behandling af latent tuberkuloseinfektion. |
| [29580819](https://pubmed.ncbi.nlm.nih.gov/29580819/) | 2018 | Oversigtsartikel | Lancet Infect Dis | Udvikling af nye lægemidler og kortere behandlingsregimer mod TB. |
| [24100880](https://pubmed.ncbi.nlm.nih.gov/24100880/) | 2013 | Oversigtsartikel | Curr Opin HIV AIDS | Nye kombinationsregimer til TB-sygdom og latent TB-infektion. |
| [32372202](https://pubmed.ncbi.nlm.nih.gov/32372202/) | 2020 | Oversigtsartikel | Appl Microbiol Biotechnol | Undersøgelsesstoffer og lægemidler med genanvendelsespotentiale i TB-behandling. |
| [41696339](https://pubmed.ncbi.nlm.nih.gov/41696339/) | 2026 | Præklinisk | ACS Omega | Delamanid og pretomanid er godkendt til TB. Nye akirale 4-nitroimidazoler testet in vitro. |
| [27151308](https://pubmed.ncbi.nlm.nih.gov/27151308/) | 2016 | Oversigtsartikel | Adv Drug Deliv Rev | Nye lægemiddelklasser mod MDR-TB. |

---

## Markedsinformation i Danmark

| Markedsføringstilladelse | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28106493520 | Deltyba (Otsuka Novel Products GmbH) | Dispergible tabletter | Indikationstekst ikke angivet i de indsamlede data |

---

## Cytotoksicitet

Delamanid er et antibakterielt middel og ikke et antineoplastisk lægemiddel. Afsnittet er derfor udeladt.

---

## Sikkerhedsovervejelser

Der blev ikke fundet interaktioner i de indsamlede data. Der foreligger ingen øvrige sikkerhedsdata. Se det godkendte produktresumé (SmPC) for oplysninger om advarsler, kontraindikationer og interaktioner.

---

## Konklusion og næste skridt

**Beslutning: Proceed with Guardrails**

**Begrundelse:**
Et fase 2/3-forsøg (CRUSH-TB) undersøger delamanid i kortere regimer ved lungetuberkulose, og mekanismen er i overensstemmelse med den godkendte brug ved MDR-TB. Forsøget er endnu ikke afsluttet og omfatter aktiv sygdom, ikke inaktiv/latent TB, så evidensen er kun delvis. De øvrige forudsagte indikationer (bovin tuberkulose, tuberkuloma, tuberkuløs ascites, aviær tuberkulose) bør betragtes som forskningsspørgsmål eller afventes (Hold).

**For at komme videre kræves:**
- Resultater fra CRUSH-TB (forventet 2027) og data, der specifikt belyser delamanids rolle i regimet
- Data om delamanids aktivitet mod ikke-replikerende bakterier og om anvendelse ved latent/inaktiv TB
- Gennemgang af produktresuméet (SmPC) for advarsler, kontraindikationer og interaktioner, da disse data manglede
- Oplysninger om virkningsmekanisme fra DrugBank til formel dokumentation
- Ved tuberkuloma: data om delamanids penetration til centralnervesystemet
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

