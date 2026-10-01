---
layout: default
title: Alirocumab
parent: Kun modelforudsigelse (L5)
nav_order: 25
evidence_level: L5
indication_count: 10
---

# Alirocumab
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

# Alirocumab: Fra hyperkolesterolæmi til X-bundet ichthyosis

## Resumé

Alirocumab er et PCSK9-hæmmende monoklonalt antistof, som anvendes til sænkning af LDL-kolesterol. Indikationsteksten er ikke oplyst i datagrundlaget, så den originale indikation er udledt af lægemiddelklassen.
TxGNN-modellen forudsiger, at det kan have effekt ved **X-bundet ichthyosis uden steroidsulfatasemangel**, men der er **0 kliniske forsøg** og **0 publikationer**, der understøtter denne retning. Forudsigelsen vurderes som et artefakt fra vidensgrafen og ikke som et biologisk signal.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Original indikation | Hyperkolesterolæmi/dyslipidæmi (udledt af lægemiddelklassen, ikke angivet i Lægemiddelstyrelsens data) |
| Forudsagt ny indikation | X-bundet ichthyosis uden steroidsulfatasemangel |
| TxGNN-forudsigelsesscore | 99,43 % |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført |
| Antal markedsføringstilladelser | 1 |
| Anbefalet beslutning | Hold |

---

## Hvorfor er forudsigelsen rimelig?

Detaljerede data om virkningsmekanisme foreligger ikke i datapakken. Alirocumab er dog et PCSK9-hæmmende antistof. Det øger tilgængeligheden af LDL-receptorer og sænker dermed cirkulerende LDL-kolesterol.

Der er ingen troværdig mekanistisk forbindelse mellem PCSK9-hæmning og denne ichthyosis-fænotype. Ingen kendt signalvej forbinder de to. Den høje score på 0,994 skyldes sandsynligvis nærhed i vidensgrafen og ikke et reelt biologisk grundlag. Forudsigelsen bør derfor ikke danne grundlag for kliniske overvejelser.

**Øvrige forudsagte kandidater** (samme lægemiddel, højere evidens):

- **Xanthomatose (score 99,37 %, evidensniveau L4, "Forskningsspørgsmål"):** Der er en plausibel indirekte sammenhæng. Xanthomer er kolesterolaflejringer sekundært til svær hyperkolesterolæmi, og alirocumab sænker LDL-kolesterol. De to fundne artikler er casebeskrivelser (kombineret dyslipidæmi og sitosterolæmi med senexanthomer behandlet med ezetimib og alirocumab). Ingen af dem tester alirocumab som behandling til regression af xanthomer. Ved sitosterolæmi (ABCG5/ABCG8) er den primære defekt en anden, så effekten af en PCSK9-hæmmer er usikker.
- **Sygdom i kolesterolkatabolisme (score 99,36 %, evidensniveau L1, "Proceed with Guardrails"):** Sammenhængen er stærk og direkte, men kategorien ligger tæt på alirocumabs eksisterende anvendelsesområde. Der er tale om udvidet anvendelse i en afgrænset population snarere end egentlig repurposing.
- **Sygdom i andre vitaminer og kofaktorer (score 99,41 %, L5, Hold)** og **46,XY-udviklingsforstyrrelse i den bagvedliggende DHT-syntesevej (score 99,37 %, L5, Hold):** Begge mangler et troværdigt mekanistisk grundlag.

---

## Klinisk evidens

For den primære kandidat (X-bundet ichthyosis) er der på nuværende tidspunkt ingen relaterede kliniske forsøg registreret.

Til orientering er der for kandidaten "sygdom i kolesterolkatabolisme" fundet ét forsøg:

| Forsøgsnummer | Fase | Status | Antal deltagere | Hovedfund |
|---------|------|------|------|---------|
| [NCT03207945](https://clinicaltrials.gov/study/NCT03207945) | Fase 3 | Afsluttet | 118 | EPIC-HIV: effekt af PCSK9-hæmning på kardiovaskulær risiko ved behandlet HIV-infektion, vurderet med non-invasiv billeddiagnostik. Relevans B, fordi populationen er HIV-specifik. Primært endepunkt og design er ikke oplyst og bør verificeres. |

---

## Litteraturevidens

For den primære kandidat (X-bundet ichthyosis) er der på nuværende tidspunkt ingen relateret litteratur.

Til orientering er der for kandidaten xanthomatose fundet to casebeskrivelser:

| PMID | År | Type | Tidsskrift | Hovedfund |
|------|-----|------|------|---------|
| [32713907](https://pubmed.ncbi.nlm.nih.gov/32713907/) | 2020 | Casebeskrivelse | Internal Medicine | Sitosterolæmi med svær hyperkolesterolæmi og senexanthomer (ABCG5-mutationer), behandlet med ezetimib og alirocumab |
| [31538826](https://pubmed.ncbi.nlm.nih.gov/31538826/) | 2019 | Casebeskrivelse | J Investig Med High Impact Case Rep | Svær kombineret dyslipidæmi med kompleks genetisk baggrund og xanthomer |

---

## Markedsinformation for Danmark

| Markedsføringstilladelse | Produktnavn | Lægemiddelform | Producent |
|---------|------|------|-----------|
| 28105680115 | Praluent | Injektionsvæske, opløsning i fyldt injektionssprøjte | Sanofi Winthrop Industrie |

---

## Sikkerhedsovervejelser

Der er ikke fundet registrerede lægemiddelinteraktioner i datagrundlaget. Ellers henvises til det godkendte produktresumé (SmPC) for sikkerhedsoplysninger, herunder advarsler og kontraindikationer.

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Den primære forudsigelse (X-bundet ichthyosis) har kun evidensniveau L5 uden forsøg eller litteratur og uden troværdig biologisk forbindelse. Den høje TxGNN-score afspejler sandsynligvis nærhed i vidensgrafen.

**For at komme videre kræves følgende:**
- Indhentning af produktresuméets advarsler og kontraindikationer fra Lægemiddelstyrelsen (blokerende datahul for sikkerhedsscreening)
- Indhentning af data om virkningsmekanisme fra DrugBank
- Hvis der ønskes et videre spor, bør fokus flyttes til xanthomatose (forskningsspørgsmål) eller til udvidet anvendelse ved sygdomme i kolesterolmetabolismen. Her bør endepunkter og design for NCT03207945 verificeres først.

*Resultaterne er udelukkende til forskningsbrug og udgør ikke medicinsk rådgivning. Repurposing-kandidater kræver klinisk validering, før de kan anvendes.*
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

