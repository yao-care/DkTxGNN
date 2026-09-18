---
layout: default
title: Bisacodyl
parent: Kun modelforudsigelse (L5)
nav_order: 67
evidence_level: L5
indication_count: 0
---

# Bisacodyl
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

# Bisacodyl: Utilfuldstændig Evidence Pack — Ingen TxGNN Drug Repurposing-forudsigelser tilgængelige

## Sammenfattelse i en sætning

Bisacodyl (DB09020) er et stimulerande afføringsmiddel etableret i klinisk praksis til kortvarig behandling af forstoppelse og tarmforberedelse før koloskopi eller operation. Det aktuelle Evidence Pack indeholder **ingen TxGNN-forudsagte nye indikatorer**, og tre kritiske datakategorier — virkningsmekanisme, danske regulatoriske optegnelser og sikkerhedsprofil — mangler. Denne rapport dokumenterer datatilstanden fra 2026-04-04 og kan ikke gå videre til en fuldstændig drug repurposing-evaluering uden afhjælpning af de identificerede mangler.

---

## Hurtig oversigt

| Element | Indhold |
|---------|---------|
| Oprindelig indikation | Ikke tilgængelig — ingen danske markeringsgodkendelsesoptegnelser i aktuelle datasæt |
| Forudsagt ny indikation | Ingen — TxGNN-forudsigelser mangler fra dette Evidence Pack |
| TxGNN-forudsigelsesscore | N/A |
| Evidensniveau | N/A |
| Markedsstatus i Danmark | Ikke markedsført (per aktuelle data; sandsynligvis en datakollektionsmangel — se bemærkning nedenfor) |
| Antal markeringsgodkendelser | 0 |
| Anbefalet beslutning | **Hold** |

---

## Hvorfor er denne forudsigelse rimelig?

Denne sektion kan ikke udfyldes, da `predicted_indications`-arrayet i Evidence Packen er tomt. Der er ingen TxGNN drug repurposing-kandidat genereret for Bisacodyl i denne pipeline-kørsel. De mest sandsynlige årsager er: (1) Bisacodyl blev ikke succesfuldt mappet til en DrugBank-knude i TxGNN-vidensgrafen, (2) forudsigelsestrinnet blev ikke udført for denne forbindelse, eller (3) Bisacodyl falder under modellens scoringsgrænse for alle sygdomsknuder.

Detaljerede virkningsmekanisme-data er ikke tilgængelige i dette Evidence Pack (Datamangel DG002). Baseret på etableret farmakologisk viden er Bisacodyl en diphenylmethan-derivat, der virker direkte på kolonslimhinden: det stimulerer entale nervebindinger, accelererer peristaltik og fremmer luminal væskeophobning ved at ændre elektrolyttransport i kolonocytter. Denne lokalt virkende mekanisme er forskellig fra systemiske lægemiddelkombinationsmål, der almindeligvis udforskes i drug repurposing-forskning, hvilket kan begrænse TxGNNs evne til at generere vidensgrafordede forudsigelser.

For at låse op for en drug repurposing-evaluering skal DrugBank-rekorden for DB09020 hentes for at udfylde MOA- og farmakologiske målfelter, og TxGNN-forudsigelsespipelinen skal køres igen med en bekræftet DrugBank-knudmapping.

---

## Markedsinformation i Danmark

Ingen markeringsgodkendelser er i øjeblikket registreret i datasættet for Bisacodyl. Dette afspejler næsten helt sikkert en **datakollektionsmangel** snarere end ægte fravær fra det danske marked: Bisacodyl er et bredt tilgængeligt køb uden recept (OTC) afføringsmiddel solgt på tværs af EU og ville normalt optræde i Lægemiddelstyrelsens register. Følgende afstemmingstrin er påkrævet før markedsstatus kan rapporteres:

- Forespørg Lægemiddelstyrelsen-produktregisteret direkte efter Bisacodyl og dets brandækvivalenter (f.eks. *Dulcolax*, *Toilax*)
- Tjek EMA-centraliseringsgodkendelses-databasen, idet Bisacodyl er et receptfrit produkt og kan være registreret nationalt snarere end centralt
- Opdater `taiwan_regulatory` (danske regulatoriske) felter tilsvarende før gen-kørsel af dette Evidence Pack

---

## Sikkerhedshensyn

Venligst henvises til den godkendte Produktsammenfattelse (SmPC) for sikkerhedsinformation.

> **Bemærk:** Sikkerhedsdata — herunder vigtige advarsler, kontraindikationer og lægemiddelinteraktionsdata — mangler fra dette Evidence Pack (Datamangel DG001, alvorlighed: Blokerende). Den danske SmPC-PDF skal hentes fra Lægemiddelstyrelsens hjemmeside og analyseres før enhver klinisk eller regulatorisk beslutning træffes.

---

## Konklusion og næste trin

**Beslutning: Hold**

**Argumentation:**
Evidence Packen for Bisacodyl (DB09020) er kritisk utilfuldstændig på tværs af alle tre evalueringspiller — forudsigelse, regulatorisk og sikkerhed — hvilket gør en drug repurposing-evaluering umulig på dette stadium. At fortsætte uden afhjælpning ville producere en rapport uden handlingsdygtig indhold for sundhedspersonale.

**For at fortsætte, er følgende nødvendigt:**

- **Kør TxGNN-forudsigelser igen** for DB09020 efter bekræftelse af den korrekte DrugBank-knudmapping; bekræft, at Bisacodyl optræder i `data/external/drugbank_vocab.csv`
- **Hent DrugBank-rekord** via DrugBank API for at udfylde virkningsmekanisme, farmakologiske mål og toksicitetsdata (Datamangel DG002 — alvorlighed: Høj)
- **Hent dansk SmPC** fra Lægemiddelstyrelsen for at få godkendte indikatorer, boksadvarsler, kontraindikationer og lægemiddelinteraktioner (Datamangel DG001 — alvorlighed: Blokerende)
- **Afstemt markedsstatus** mod Lægemiddelstyrelsens nationale produktregister og EMA-database; opdater `total_licenses` og `licenses[]` tilsvarende
- **Gengener Evidence Pack** (målrettet version v5) når alle blokerende mangler er løst, og udløs derefter den fulde rapportpipeline igen

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

