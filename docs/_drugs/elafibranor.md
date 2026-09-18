---
layout: default
title: Elafibranor
parent: Kun modelforudsigelse (L5)
nav_order: 158
evidence_level: L5
indication_count: 10
---

# Elafibranor
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

# Elafibranor: Fra metabolisk leversygdom til amenoré

## Sammenfatning i en sætning

Elafibranor er en dual PPARα/δ-agonist, som undersøges primært for metaboliske leversygdomme, herunder Non-Alcoholic Steatohepatitis (NASH) og Primary Biliary Cholangitis (PBC), men har i øjeblikket ingen markedsføringsgodkendelse i Danmark.
TxGNN-modellen forudsiger, at det kan være effektivt mod **Amenoré** (højest rangeret forudsigelse, score 99.86%), men der blev identificeret **ingen kliniske forsøg** og **ingen publikationer**, som understøtter denne specifikke omplaceringsretning.
Alle fem forudsagte indikationer er på evidensniveau **L5 — modelforudsigelse alene** — og den overordnede anbefaling er **Hold** afventende grundlæggende mekanistiske og sikkerhedsdata.

---

## Hurtig oversigt

| Post | Indhold |
|------|---------|
| Original indikation | Ingen godkendt indikation i Danmark; undersøgt for NASH og Primary Biliary Cholangitis |
| Forudsagt ny indikation | Amenoré (rang 1) |
| TxGNN-forudsigelsesscore | 99.86% |
| Evidensniveau | L5 — modelforudsigelse alene; ingen kliniske forsøg eller publikationer fundet |
| Danmark-markedsstatus | Ikke markedsført |
| Antal markedsføringsgodkendelser | 0 |
| Anbefalet beslutning | **Hold** |

---

## Hvorfor er denne forudsigelse rimelig?

I øjeblikket er detaljerede mekanismedata ikke tilgængelige i denne Evidence Pack. Baseret på kendt information er elafibranor en dual PPARα/δ (peroxisome proliferator-activated receptor alfa/delta) agonist. Dens undersøgte efficacy er blevet studeret i sammenhæng med hepatisk metabolisk sygdom — specifikt NASH og PBC — hvor den modulerer fedtsyres β-oxidation, lipidmetabolisme og hepatisk inflammation.

Det foreslåede mekanistiske link til amenoré baserer sig på hypotesen om, at PPARα/δ-drevet forbedring af energisubstratudbygning kan indirekte påvirke hypotalamisk GnRH-pulsatil sekretion. Denne vej er konceptuelt relevant for **funktionel hypotalamisk amenoré** udløst af negativt energibalance (f.eks. træningsudløst eller ernærings-deficit-amenoré). Imidlertid er denne ræsonnering stort set ekstrapoleret fra PPARγ-forskning; der er i øjeblikket **ingen publiceret evidens** for, at PPARα eller PPARδ-agonisme direkte modulerer aksen hypotalamus-hypofyse-ovarier (HPO).

Den interne mekanistiske relevanskarakterisering for denne parring er ekstremt svag (2/10). Det er derfor sandsynligt, at den høje TxGNN-score afspejler delt strukturel topologi i det biovidenskabelige vidensdiagram snarere end et meningsfuldt biologisk signal. Dette fund er konsistent på tværs af alle fem forudsagte indikationer, hvoraf ingen har bekræftende klinisk eller præ-klinisk litteraturunderstøttelse.

---

## Klinisk forsøgsevidence

I øjeblikket er der ingen relaterede kliniske forsøg registreret for elafibranor inden for amenoré.

---

## Litteraturevidence

I øjeblikket er der ingen relateret litteratur tilgængelig for elafibranor inden for amenoré.

---

## Danmark-markedsinformation

Elafibranor har i øjeblikket **ingen markedsføringsgodkendelser** i Danmark. Lægemidlet er ikke registreret hos Lægemiddelstyrelsen og er ikke tilgængeligt på det danske marked i nogen doseringsform eller indikation.

| Markedsføringsgodkendelsesnummer | Produktnavn | Doseringsform | Godkendt indikation |
|-------------------------------|-------------|-------------|---------------------|
| — | — | — | Ingen godkendelse på protokol |

---

## Sikkerhedshensyn

Se venligst den godkendte Resumé af produktkarakteristika (SmPC) for sikkerhedsinformation. Lægemiddelinteraktionsdata, vigtige advarsler og kontraindikationer kunne ikke indhentes på tidspunktet for denne vurdering.

---

## Konklusion og næste trin

**Beslutning: Hold**

**Begrundelse:**
Alle fem TxGNN-forudsagte indikationer for elafibranor — amenoré, non-syndromisk spiserørsmalformation, knogles Pagets sygdom, dentinogenesis imperfecta og pladecellekarcinom — er på evidensniveau L5, understøttet af modelforudsigelse alene og ingen bekræftende kliniske forsøg eller publiceret litteratur. Mekanistisk relevans spænder fra ekstremt svag (amenoré, 2/10) til fraværende (non-syndromisk spiserørsmalformation og dentinogenesis imperfecta, 0/10), og en forudsigelse (pladecellekarcinom) medfører en aktiv **sikkerhedsbekymring**: PPARδ-agonisme er associeret med pro-tumorigene effekter i pladecelleepitelier, hvilket gør elafibranor potentielt kontraindikeret snarere end terapeutisk i denne sammenhæng. Lægemidlet er desuden i øjeblikket ikke godkendt i Danmark, hvilket betyder, at den regulatoriske vej ville kræve initiering fra bunden.

**For at fortsætte er følgende nødvendigt:**

- **SmPC og sikkerhedsdata**: Hent det fulde Resumé af produktkarakteristika (herunder advarsler, kontraindikationer og interaktioner) fra EMA-produktsiden eller det oprindelige firma for at muliggøre en ordentlig sikkerhedsscreening (Stage S1)
- **MOA-bekræftelse**: Indhent komplet PPARα/δ-agonismeprofil fra DrugBank eller primær farmakologilitteratur, herunder vævspecifik receptoraktivitet og eventuelle kendte endokrine effekter
- **Præ-klinisk litteraturgennemgang**: Gennemfør en målrettet søgning (PubMed, Embase) specifikt for PPARα/δ-agonister og reproduktiv endokrinologi eller hypotalamisk funktion for at vurdere, hvorvidt nogen biologisk basis for amenoré-forudsigelsen eksisterer, før der fortsættes
- **Indikationsprioriteringsgennemgang**: I betragtning af at den højest rangerede indikation har en mekanistisk score på 2/10, bør man overveje, hvorvidt et anderledes terapiområde (f.eks. knoglemetabolisme via PPARδ, bedømt 4/10) repræsenterer et stærkere udgangspunkt for yderligere undersøgelse
- **Regulatorisk landskabskortlægning**: Præciser elafibranors nuværende globale godkendelsestatus (herunder EMA centraliseret procedure for PBC) og fastlæg, hvorvidt nogen eksisterende godkendelse kan understøtte en etiketudvidelsevej inden for EU/Danmark

---

*Denne rapport er genereret til forskningsmæssige formål alene og udgør ikke medicinsk rådgivning. Alle omplaceringsmuligheder kræver klinisk validering før eventuel terapeutisk anvendelse.*

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

