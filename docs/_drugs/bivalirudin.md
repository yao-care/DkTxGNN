---
layout: default
title: Bivalirudin
parent: Kun modelforudsigelse (L5)
nav_order: 69
evidence_level: L5
indication_count: 0
---

# Bivalirudin
{: .fs-9 }

Evidensniveau: **L5** | Forudsagte indikationer: **0** stk.
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

# Bivalirudin: Ingen gendestinationsbestemmelseskandidater identificeret af TxGNN

## Resumé på en sætning

Bivalirudin er en syntetisk direkte trombin-inhibitor (DTI), der anvendes som antikoagulant, og er bedst kendt for sin anvendelse under perkutan koronar intervention (PCI) og hos patienter med eller i risiko for heparin-induceret trombocytopeni (HIT).
Den aktuelle TxGNN-analyse **genererede ingen gendestinationsbestemmelsesprediktioner** for denne forbindelse.
Denne evaluering er **ufuldstændig** på grund af to kritiske datahuller — manglende MOA-data og fraværende danske regulatoriske posteringer — og en gendestinationsbestemmelsesanbefaling kan ikke udstedes på dette stadium.

---

## Hurtig oversigt

| Element | Indhold |
|---------|---------|
| Original indikation | Antikoagulation under PCI; heparin-induceret trombocytopeni *(baseret på etableret farmakologisk viden; ingen formel indikationstekst hentet fra Evidence Pack)* |
| Forudsagt ny indikation | Ingen identificeret |
| TxGNN-forudsigelsesscore | Ikke tilgængelig |
| Bevisniveau | Ikke evalueret |
| Markeds tilstand i Danmark | Ikke markedsført (0 godkendelser på register) |
| Antal markedsføringstilladelser | 0 |
| Anbefalet afgørelse | **Afvente** |

---

## Hvorfor der ikke blev genereret en forudsigelse

Bivalirudin (DrugBank ID: DB00006) er et 20-aminosyre-syntetisk peptid, der reversibelt og direkte inhiberer trombin — både frit og bundne i blodpropper — ved at binde samtidigt til det aktive katalytiske sted og anionbindingssteder I. Denne bivalente bindingsprofil adskiller det fra heparin og danner grundlaget for dets antikoagulante anvendelse i kardiovaskulære indstillinger.

Trods denne velkarakteriserede farmakologiske profil returnerede TxGNN vidensgraf-pipelinen **ingen gendestinationsbestemmelseskandidater** i denne kørsel. To faktorer er sandsynligvis ansvarlige:

1. **Manglende MOA-data i Evidence Pack.** Feltet `original_moa` er markeret som et datahul (alvorlighed: Høj). Uden en struktureret mekanisme-for-handling-registrering forbundet til vidensgrafen, kan TxGNN's vidensgraf-gennemgange og sygdomsligheds-moduler ikke forankre lægemidlet til nedstrøms biologiske mål og veje, som ellers ville bringe nye indikationer til overfladen.

2. **Ingen dansk regulatorisk forbindelse.** Evidence Pack indeholder nul godkendte indikationer og nul markedsføringstilladelser for Danmark. De lægemiddel-indikation-kanter, der normalt starter TxGNN's scoring, er derfor fraværende, hvilket yderligere begrænser prognose-dækningen.

> **Bemærk:** Bivalirudin er centralt godkendt i Europa under handelsnavn **Angiox** (EMA/H/C/000562). Fraværet af danske nationale posteringer i dette Evidence Pack kan afspejle et dataindsamlings-hul snarere end en virkelig mangel på tilgængelighed. Dette bør verificeres mod EMA-produktdatabasen og Lægemiddelstyrelsen's register, før man konkluderer, at produktet virkelig er utilgængeligt i Danmark.

---

## Sikkerhedshensyn

Alle sikkerhedsfelter (vigtige advarsler, kontraindikationer, lægemiddel-lægemiddel-interaktioner) mangler i det aktuelle Evidence Pack.

> Se venligst det godkendte Produktresumé (SmPC) for Angiox — tilgængeligt via [EMA-produktsiden](https://www.ema.europa.eu/en/medicines/human/EPAR/angiox) — for fuldstændige sikkerhedsoplysninger, herunder blødningsrisiko, nyre-dosistilpasninger og interaktioner med andre antikoagulanter eller antitrombocytmidler.

---

## Konklusion og næste trin

**Afgørelse: Afvente**

**Begrundelse:**
TxGNN-modellen producerede ingen gendestinationsbestemmelsesprediktioner for Bivalirudin i denne evalueringscyklus, og to blokkerende eller høj-alvorligheds-datahuller forhindrer en meningsfuld mekanistisk eller regulatorisk vurdering i at blive gennemført. Ingen bevisevaluering kan udføres uden en målindikation til at forankre det.

**For at fortsætte er følgende nødvendig:**

- **Løse DG002 (Høj) — MOA-data:** Forespørg DrugBank API for DB00006 for at hente struktureret mekanisme-for-handling, mål- og vejlederdata. Dette er væsentligt for TxGNN grafbaseret scoring og for mekanisme-begrundelsessektion.
- **Løse DG001 (Blokkering) — danske regulatoriske / SmPC-data:** Krydscheck EMA-databasen for centralt godkendte autorisationer og Lægemiddelstyrelsen's produktregister for Bivalirudin / Angiox. Hent det aktuelle SmPC PDF for at udtrække godkendte indikationer, advarsler og kontraindikationer.
- **Kør TxGNN-pipelinen igen:** Når MOA- og indikationsdata er udfyldt, skal vidensgraf-forudsigelse-trinnet køres igen. Med bivalent trombin-inhibering som kernemekanisme, kan kandidatindikationer i trombotiske, inflammatoriske eller komplementvej-lidelser komme til overfladen.
- **Verificer Danmarks markedstilgængelighed:** Bekræft, om Angiox er kommercielt tilgængeligt via EMA centralt godkendt autorisering og om det er refunderet under den danske nationale formulær, uafhængigt af et nationalt MA-nummer.

---

*Denne rapport genereres til forskningsformål alene og udgør ikke medicinsk rådgivning. Alle gendestinationsbestemmelseskandidater kræver klinisk validering før enhver terapeutisk anvendelse.*

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

