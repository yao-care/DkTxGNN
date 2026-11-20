---
layout: default
title: Lamotrigine
parent: Høj evidens (L1-L2)
nav_order: 476
evidence_level: L2
indication_count: 2
last_modified_at: 2026-11-06
monitor_inn: "lamotrigine"
predicted_indications: ["trigeminal nerve neoplasm", "trigeminal neuralgia"]
description: "Lamotrigine: forudsagt ny indikation Trigeminal nerve neoplasm (evidensniveau L2). I Danmark, markedsføringstilladelser: mindst 20"
---

# Lamotrigine
{: .fs-9 }

Evidensniveau: **L2** | Forudsagte indikationer: **2** stk.
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

## Lamotrigine: Trigeminal nerve neoplasm
{: .text-alpha }

## Resumé i én sætning

Lamotrigin er et antiepileptikum, der oprindeligt anvendes til behandling af epilepsi, partiel epilepsi og Lennox-Gastaut-syndrom.
TxGNN-modellen forudsiger, at det også kan have effekt ved **trigeminusneuralgi**. Den højest rangerede forudsigelse i modellen er dog *trigeminusnervetumor*, som ikke understøttes af evidens (se nedenfor). Trigeminusneuralgi understøttes af **2 afsluttede kliniske forsøg** (begge små) og **18 publikationer**, herunder en europæisk retningslinje (EAN 2019).

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Ikke registreret i de lokale data |
| Forudsagt ny indikation | Trigeminal nerve neoplasm |
| TxGNN-forudsigelsesscore | 0.9997 |
| Evidensniveau | L2 (trigeminusneuralgi) |
| Markedsstatus i Danmark | Markedsført (gyldige tilladelser: mindst 20) |
| Antal markedsføringstilladelser | mindst 20 |
| Anbefalet beslutning | Proceed with Guardrails (trigeminusneuralgi) |

---

## Hvorfor er forudsigelsen rimelig?

Ifølge afsnittet »Mechanism of Action« i den produktinformation, som den amerikanske FDA har godkendt (Prescribing Information), for Lamotrigine (uofficiel oversættelse): »Den eller de præcise mekanismer, hvorved lamotrigin udøver sin antikonvulsive virkning, er ukendte. I dyremodeller designet til at påvise antikonvulsiv aktivitet var lamotrigin effektivt til at forhindre spredning af anfald i maksimalt elektroshock (MES)- og pentylentetrazol (scMet)-testene og forhindrede anfald i testene for visuelt og elektrisk fremkaldt efterudladning (EEAD) for antiepileptisk aktivitet.« Engelsk originaltekst: "The precise mechanism(s) by which lamotrigine exerts its anticonvulsant action are unknown. In animal models designed to detect anticonvulsant activity, lamotrigine was effective in preventing seizure spread in the maximum electroshock (MES) and pentylenetetrazol (scMet) tests, and prevented seizures in the visually and electrically evoked after-discharge (EEAD) tests for antiepileptic activity." ([DailyMed: Lamotrigine Kit (lamotrigine) prescribing information, OWP Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=474fb321-575c-4b97-9dbe-080061652ee4), version af 2026-10-12; hentet 2026-11-19). Lamotrigin er dog kendt som en blokker af spændingsafhængige natriumkanaler, der dæmper frigørelsen af glutamat. Denne vurdering bygger på den generelle farmakologiske viden og de mekanistiske vurderinger i datagrundlaget.

Trigeminusneuralgi opstår typisk ved karkompression af trigeminusnervens rod, hvilket giver fokal demyelinisering og unormale, højfrekvente udladninger. Det er den samme type overeksciterbarhed, som natriumkanalblokkere som carbamazepin og oxcarbazepin dæmper. Da lamotrigin virker via en tilsvarende mekanisme, og da det allerede er etableret ved epilepsi, er det mekanistisk plausibelt ved denne lidelse. EAN-retningslinjen fra 2019 nævner lamotrigin som tillægs- eller andenlinjemulighed.

**Bemærk om den højest scorende forudsigelse:** Den høje score for trigeminusnervetumor skyldes sandsynligvis nærhed til trigeminusneuralgi i videnskabsgrafen. Den fundne litteratur handler om neuralgi, ikke tumorbehandling, og der er ingen evidens for en antitumoreffekt.

---

## Kliniske forsøg

| Forsøgsnummer | Fase | Status | Antal deltagere | Hovedresultater |
|---------|------|------|------|---------|
| [NCT00913107](https://clinicaltrials.gov/study/NCT00913107) | Fase 2/3 | Afsluttet | 21 | Lamotrigin sammenlignet med carbamazepin ved trigeminusneuralgi (effekt og sikkerhed). Direkte relevant, men lille stikprøve |
| [NCT00203229](https://clinicaltrials.gov/study/NCT00203229) | Ikke angivet (NA) | Afsluttet | 20 | Dobbeltblindet, placebokontrolleret tillægsundersøgelse af lamotrigin ved trigeminusneuralgi. Passende design, men lav styrke |

Der er ikke registreret kliniske forsøg for de øvrige forudsagte indikationer (trigeminusnervetumor, reflekspræget anfald m.fl.).

---

## Litteratur

Et udvalg af de mest relevante publikationer for trigeminusneuralgi:

| PMID | År | Type | Tidsskrift | Hovedresultater |
|------|-----|------|------|---------|
| [30860637](https://pubmed.ncbi.nlm.nih.gov/30860637/) | 2019 | Retningslinje | Eur J Neurol | Europæisk retningslinje for behandling af trigeminusneuralgi |
| [37892981](https://pubmed.ncbi.nlm.nih.gov/37892981/) | 2023 | Systematisk review | Biomedicines | Paraplyreview over lægemidler til trigeminusneuralgi, effekt og bivirkninger |
| [34108244](https://pubmed.ncbi.nlm.nih.gov/34108244/) | 2021 | Review | Pract Neurol | Praktisk vejledning om diagnostik og behandling |
| [31908187](https://pubmed.ncbi.nlm.nih.gov/31908187/) | 2020 | Review | Mol Pain | Overblik fra patofysiologi til farmakologisk behandling |
| [38870050](https://pubmed.ncbi.nlm.nih.gov/38870050/) | 2024 | Review | Expert Rev Neurother | Opdatering om farmakoterapi; carbamazepin/oxcarbazepin er førstevalg, tredjegenerationsantiepileptika kan være adjuvans |
| [38246671](https://pubmed.ncbi.nlm.nih.gov/38246671/) | 2024 | Review | No Shinkei Geka | Lamotrigin nævnt som off-label alternativ til carbamazepin |
| [30178160](https://pubmed.ncbi.nlm.nih.gov/30178160/) | 2018 | Review | Drugs | Aktuelle og nye farmakologiske muligheder ved typisk og atypisk trigeminusneuralgi |
| [11903537](https://pubmed.ncbi.nlm.nih.gov/11903537/) | 2001 | Review | Headache | Antiepileptika ved clusterhovedpine og trigeminusneuralgi |
| [39365662](https://pubmed.ncbi.nlm.nih.gov/39365662/) | 2025 | Registerstudie | Pain | Komorbiditeter ved trigeminusneuralgi i det danske landspatientregister |
| [25299564](https://pubmed.ncbi.nlm.nih.gov/25299564/) | 2014 | Review | BMJ Clin Evid | Oversigt over behandling af trigeminusneuralgi |

**Øvrige forudsagte indikationer (kort):** For startle-epilepsi findes små kasuistiske serier med lamotrigin som tillægsbehandling ([10512780](https://pubmed.ncbi.nlm.nih.gov/10512780/), 1999; [21896426](https://pubmed.ncbi.nlm.nih.gov/21896426/), 2011, hvor 3 af 6 patienter blev markant bedre). For audiogene anfald er evidensen udelukkende prækliniske dyrestudier (fx [26876275](https://pubmed.ncbi.nlm.nih.gov/26876275/)). For de øvrige reflekspræget anfaldstyper (orgasme-, vandladnings-, spise-, tanke- og læseanfald) er der ingen relevant direkte evidens.

---

## Markedsinformation i Danmark

| Markedsføringstilladelsesnummer | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28101390489 | Lamictal (GlaxoSmithKline Pharma A/S) | Tabletter | Indikationstekst ikke tilgængelig i de indsamlede data |

---

## Sikkerhedsovervejelser

Kun punkter med data er medtaget.

- **Kontraindikationer/risikotilstande fra videnskabsgrafen** (ikke fra produktresuméet): angstlidelse, neurotisk lidelse, dysthymi, leversygdom, galdeblæresygdom, trombocytopeni, neutropeni, agranulocytose, anæmi (inkl. makrocytær), pancytopeni, aplastisk anæmi og ikke-infektiøs meningitis.
- **Lægemiddelinteraktioner:** 190 registrerede interaktioner i alt. Blandt de angivne er flere af moderat grad (morfin, dronabinol, nabilon, metoclopramid, opium, orlistat); metformin er mindre betydelig. Valproat og østrogenholdige p-piller bør især gennemgås, da de påvirker lamotrigins niveau.
- **Udslæt:** Langsom optitrering anbefales for at begrænse risikoen for alvorligt udslæt (Stevens-Johnson syndrom).

Advarsler og kontraindikationer fra det godkendte produktresumé (SmPC) mangler i datagrundlaget og skal indhentes fra Lægemiddelstyrelsen.

---

## Konklusion og næste skridt

**Beslutning: Proceed with Guardrails** (for trigeminusneuralgi)

**Begrundelse:**
Lamotrigin har plausibel mekanisme, er nævnt i europæisk retningslinje og er undersøgt i to afsluttede, men små forsøg (n=20 og n=21). Evidensen er ikke tilstrækkelig til førstevalg. For trigeminusnervetumor, orgasme-, vandladnings-, spise-, tanke- og læseanfald anbefales *Hold* (evidensniveau L5). Startle-epilepsi og audiogene anfald er forskningsspørgsmål (L4).

**For at komme videre kræves:**
- Hent og gennemgå produktresuméet (SmPC) for advarsler, kontraindikationer og godkendt indikation (blokerende datahul)
- Detaljerede data om virkningsmekanisme (fx fra DrugBank)
- Større, veldesignede randomiserede forsøg ved trigeminusneuralgi
- Anvendelse som tillægsbehandling eller ved intolerance over for førstelinjemidler, med langsom optitrering
- Gennemgang af relevante interaktioner (især valproat og østrogenholdige p-piller) og overvågning af blodbillede og leverfunktion
- Yderligere observationelle data for startle-epilepsi før en anbefaling kan overvejes

<!-- review:begin log -->

## Gennemgangslog

Nedenfor er gennemgangsloggen for denne side. Sætningen om, at data om virkningsmekanismen ikke var tilgængelige, er erstattet med et uddrag fra den angivne officielle produktinformation (med uofficiel oversættelse); modelforudsigelser, evidensniveauer og konklusioner er ikke omskrevet.

| Gennemgået | Punkt | Handling | Kilde |
|------|------|------|------|
| 2026-11-19 | Sætningen »data om virkningsmekanismen er ikke tilgængelige« erstattet med uddrag fra den amerikanske produktinformation | Sætning om manglende data om virkningsmekanismen erstattet med et uddrag med kilde | [DailyMed: Lamotrigine Kit (lamotrigine) prescribing information, OWP Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=474fb321-575c-4b97-9dbe-080061652ee4) |

<!-- review:end log -->

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

