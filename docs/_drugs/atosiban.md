---
layout: default
title: Atosiban
parent: Kun modelforudsigelse (L5)
nav_order: 49
evidence_level: L5
indication_count: 10
---

# Atosiban
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

# Atosiban: Fra præterm arbejde til primær arvelig glaukom

---

## Sammenfatning i én sætning

Atosiban er en syntetisk peptid oxytocin/vasopressin-receptor (OXTR) antagonist, etableret i klinisk praksis som tokolitikum til hæmning af uterine kontraktioner og forsinkelse af præterm arbejde.
TxGNN-modellen forudsiger, at det kan være effektivt for **Primær arvelig glaukom** med en sikkerhedsgrad på **99,92 %**,
dog **nul kliniske forsøg og nul publicerede publikationer** understøtter denne retning i øjeblikket – hvilket placerer det på det laveste bevisniveau (L5) og rejser betydelige mekanistiske bekymringer omkring behandlingens retning.

---

## Hurtig oversigt

| Punkt | Indhold |
|-------|---------|
| Oprindelig indikation | Præterm arbejde (tokolitikum) |
| Forudsagt ny indikation | Primær arvelig glaukom |
| TxGNN forudsigelses score | 99,92 % |
| Bevisniveau | L5 |
| Markedsstatus i Danmark | Ikke markedsført |
| Antal markedsføringsautoriteter | 0 |
| Anbefalet beslutning | Afvent |

---

## Hvorfor er denne forudsigelse rimelig?

Detaljerede data om virkningsmekanisme er ikke tilgængelige i den aktuelle bevissamling. Baseret på etableret farmakologisk viden er Atosiban en konkurrerende antagonist på både oxytocin-receptorer (OXTR) og vasopressin V1a-receptorer. Dens etablerede kliniske rolle er inhibering af OXTR-medieret uterine glatte muskelkontraktioner til forsinkelse af præterm arbejde.

Den mekanistiske forbindelse, som TxGNN foreslår, hviler på kendt udtryk af OXTR i okulært væv – specifikt i det trabelkulære maskeværk og ciliarlegemet. Endogent oxytocin er blevet vist i nogle studier at sænke intraokulart tryk (IOP), plausibelt gennem prostaglandin-medierede veje, der forbedrer afstrømningen af kammervand. Fordi Atosiban *blokerer* denne receptor, er dets netto-farmakologiske effekt på IOP retningsusikker og kan faktisk øge IOP i stedet for at sænke det – det modsatte af hvad der er terapeutisk påkrævet i glaukombehandling.

Primær arvelig glaukom opstår fra mutationer i strukturelle og regulatoriske gener (MYOC, OPTN, WDR36), der øger modstanden for trabelkulær afstrømning. Der er ingen etableret patogenetisk forbindelse mellem disse genetiske drivere og oxytocin-OXTR-aksen. Den høje TxGNN-score afspejler sandsynligvis delte co-ekspression mønstre af gener i okulært væv, som blev fanget af det grafneurale netværk, snarere end en valideret terapeutisk mekanisme. Forudsigelsen bør fortolkes med betydelig forsigtighed: **Atosibans farmakologiske virkningsretning i glaukom er plausibelt kontraproduktiv**.

---

## Klinisk forsøgsbeviser

Aktuelt ingen relaterede kliniske forsøg registreret.

*(Systematiske søgninger på ClinicalTrials.gov og WHO ICTRP blev gennemført den 2026-03-10 for Atosiban på tværs af alle forudsagte indikationer – primær arvelig glaukom, åbenvinkel glaukom, alopeci, medfødt hypotrichiasis milia og simpel hypotrichiasis på hovedbunden – og returnerede nul resultater i alle tilfælde.)*

---

## Litteraturbeviser

Aktuelt ingen tilgængelig relateret litteratur.

*(PubMed-søgninger gennemført den 2026-03-10 for Atosiban på tværs af alle fem forudsagte indikationer returnerede nul publikationer.)*

---

## Danmarks markedsinformation

Atosiban er ikke i øjeblikket registreret eller markedsført i Danmark ifølge de data, der er tilgængelige i denne bevissamling. Ingen markedsføringsautoriteter fra Lægemiddelstyrelsen eller via EMA-centraliseret procedure er registreret.

> **Bemærk:** Dette datasæt kan være ufuldstændigt med hensyn til dansk/EMA-registreringsstatus. Uafhængig verifikation via Lægemiddelstyrelses produktdatabase og EMA-medicindatabasen anbefales stærkt, før der drages endelige konklusioner om tilgængelighed i Danmark.

---

## Sikkerhedshensyn

Se venligst det godkendte Produktkarakteristika Resumé (SmPC) for sikkerhedsinformation.

*(Ingen oplysninger om lægemiddelinteraktioner, vigtige advarsler eller kontraindikationer var tilgængelige i denne bevissamling. Hentning fra Lægemiddelstyrelses produktregistrering og DrugBank anbefales som et prioriteret afhjælpningstrin, før enhver yderligere evaluering.)*

---

## Konklusion og næste skridt

**Beslutning: Afvent**

**Begrundelse:**
Alle fem forudsagte indikationer i denne bevissamling hviler udelukkende på TxGNN-modelscores (L5-beviser), uden at der er identificeret nul understøttende kliniske forsøg eller fagfællebedømte publikationer. Mere kritisk er den førende forudsagte mekanisme – OXTR-blokade i okulært væv – farmakologisk kontraproduktiv for glaukom: Atosibans antagonistvirkning vil sandsynligvis *modvirke* den IOP-sænkende virkning af endogent oxytocin, ikke gengive den. Denne retningskonflikt udelukker den primære forudsigelse som en levedygtig kandidat til kort-sigtsgenbrug.

**For at fortsætte er følgende nødvendigt:**

- **Regulatorisk verifikation:** Bekræft Atosibans aktuelle autorisationsstatus i Danmark direkte via Lægemiddelstyrelses produktdatabase og EMA-medicindatabasen, da de regulatoriske data i denne pakke virker ufuldstændige
- **MOA datahentning:** Hent fulde virkningsmekanisme og farmakodynamiske data fra DrugBank (DB09059) og det godkendte SmPC for at muliggøre korrekt mekanistisk gennemgang
- **Sikkerhedsdatahentning:** Download og parse det fulde SmPC fra dansk/EMA-mærkning for at identificere kontraindikationer, vigtige advarsler og klinisk relevante lægemiddelinteraktioner
- **Prækliniske mekanistiske studier:** Bestil eller identificer studier, der direkte måler effekten af OXTR *antagonisme* (ikke agonisme) på intraokulart tryk i dyremodel eller celle-kultur glaukommodeller, før nogen klinisk hypotese kan dannes
- **Retnings-reevaluering:** Vurder, om en OXTR *agonist* (snarere end Atosiban som antagonist) ville være en mere farmakologisk sammenhængende kandidat til IOP-reduktion i glaukom – en begrebsmæssigt omvendt repurposing-retning
- **Klynge gennemgang:** De fem forudsagte indikationer grupperer sig i to biologiske klynger (okulær/glaukom og hårfollikel/alopeci); begge klynger deler samme fundamentale retningskonflikt for en OXTR-antagonist og bør gennemgås sammen i enhver efterfølgende mekanistisk analyse

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

