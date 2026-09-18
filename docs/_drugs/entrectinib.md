---
layout: default
title: Entrectinib
parent: Moderat evidens (L3-L4)
nav_order: 168
evidence_level: L4
indication_count: 10
---

# Entrectinib
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

# Entrectinib: Fra NTRK Fusionspositive Solide Tumorer til Multiple Endokrin Neoplasi

## Resumé på en sætning

Entrectinib (Rozlytrek) er en CNS-aktiv multikinase-hemmer godkendt til NTRK fusionspositive solide tumorer og ROS1-positive non-småcellet lungekræft, virkende ved at blokere aberrant receptor-tyrosinkinase-signalering som driver tumorvækst og overlevelse.
TxGNN-modellen forudsiger, at det kan være effektivt mod **Multiple Endokrin Neoplasi (MEN)**, med **2 kliniske forsøg** og **1 publikation** der i øjeblikket giver indirekte understøttende beviser for denne retning.
Den mekanistiske forbindelse er plausibel, men forbliver uvalideret, og yderligere biomarker-drevet forskning er nødvendig før klinisk translation.

---

## Hurtig oversigt

| Punkt | Indhold |
|-------|---------|
| Oprindelig indikation | NTRK fusionspositive solide tumorer (vævsuafhængig); ROS1-positive non-småcellet lungekræft (baseret på kendt regulatoriske godkendelser; felt tomt i datakilden) |
| Forudsagt ny indikation | Multiple Endokrin Neoplasi (MEN) |
| TxGNN-forudsigelsesscore | 98.58% |
| Bevisniveau | L4 |
| Danmarks markedsstatus | Ikke markedsført (ingen national markedsføringstilladelse registreret) |
| Antal markedsføringstilladelser | 0 nationale tilladelser i arkivet — bemærk: EMA centraliseret tilladelse (Rozlytrek, EU/1/20/1467) er gyldig på tværs af EØS inklusive Danmark |
| Anbefalet beslutning | Hold |

---

## Hvorfor er denne forudsigelse rimelig?

Entrectinib er en potent, CNS-penetrant hemmer af tre receptor-tyrosinkinase-familier: TRKA, TRKB og TRKC (kodet af *NTRK1*, *NTRK2* og *NTRK3*), ROS1 og ALK. Når disse kinaser bærer onkogene genfusioner, bliver de konstitutivt aktive og driver tumorproliferation via downstream RAS/MAPK, PI3K/AKT og PLCγ signalveje. Entrectinib konkurrerer om binding til ATP-bindingslommen på disse kinaser, hvilket slukker det onkogene signal uanset tumorens vævsoprindelse — en vævsuafhængig mekanisme.

Multiple Endokrin Neoplasi (MEN) er en gruppe af arvelige syndromer karakteriseret ved tumorer i flere endokrine kirtler. MEN2A og MEN2B drives af aktiverende mutationer i *RET* proto-onkogenet, manifesterende sig primært som medullært thyroideakarcinom (MTC), fæokromocytom og, i MEN2A, primær hyperparathyroidisme. MEN1 opstår fra tab-af-funktion-mutationer i *MEN1* tumorsupresor, producerende parathyreoid-adenomer, hypofyse-tumorer og pancreatico-neuroendokrine tumorer (pNETs). Den indirekte forbindelse til entrectinib hviler på to observationer: (1) NTRK-genfusioner er blevet identificeret i en delmængde af thyroideakræft og neuroendokrine tumorer — præcis de tumortyper som karakteriserer MEN-syndromerne; (2) den understøttende litteratur (PMID 38438731) dokumenterer en patient med MTC (den karakteristiske MEN2-cancer) som udvikler off-target-resistens over for den selektive RET-hemmer selpercatinib via alternative onkogene drivere, hvilket rejser hypotesen om at NTRK/ROS1-inhibering potentielt kunne adressere bypass-mekanismer i RET-drevne endokrine tumorer.

Det er vigtigt at bemærke, at mutant RET — den primære onkogene driver i MEN2 — **ikke** er et direkte mål for entrectinib. Den høje TxGNN-score (98.58%) afspejler mest sandsynligt knowledge-graph co-occurrence mønstre som linker NTRK/ROS1-hemmere til endokrin tumorbiologi snarere end en direkte valideret mekanisme. Forudsigelsen bør derfor behandles som hypotese-genererende og tolkes med forsigtighed, afventende dedikeret mekanistisk og klinisk validering.

---

## Klinisk forsøgsbeviser

| Forsøgsnummer | Fase | Status | Indskrivning | Vigtigste fund |
|---------|------|------|------|---------|
| [NCT04551495](https://clinicaltrials.gov/study/NCT04551495) | Fase 2 | Aktiv, ikke rekrutterende | 65 | Neoadjuvant ROS1-inhibering (entrectinib) kombineret med endokrin terapi ved invasivt lobulært brystkræft (ILBC) med CDH1-tab. Baseret på et præklinisk fund at ROS1 er en syntetisk letal partner af CDH1-inaktivering. Ikke MEN-specifik, men validerer princippet om entrectinib-aktivitet i en endokrin-sensitiv, hormonreceptor-positiv tumor-kontekst. |
| [NCT03878524](https://clinicaltrials.gov/study/NCT03878524) | Fase 1 | Termineret | 2 | Basket-forsøg (SMMART PRIME) testende personaliserede lægemiddelkombinationer guidet af individuel tumor-molekylær profilering til at overvinde lægemiddelresistens. Termineret tidligt på grund af dårlig rekruttering. Ingen MEN-specifikke data tilgængelige og ingen efficacy-konklusioner kan drages. |

---

## Litteraturbeviser

| PMID | År | Type | Journal | Vigtigste fund |
|------|------|------|---------|---------|
| [38438731](https://pubmed.ncbi.nlm.nih.gov/38438731/) | 2024 | Kasuistik / Molekylær analyse | NPJ Precision Oncology | Beskriver adaptiv off-target-resistens over for den selektive RET-hemmer selpercatinib hos en patient med metastatisk medullært thyroideakarcinom (MTC) bærende en RET D898_E901del activation-loop-mutation. Resistensen opstod gennem alternative onkogene mekanismer snarere end sekundære RET-mutationer. Fremhæver den kliniske udfordring med alternative pathway bypass i RET-drevne MEN2-tumorer, og understøtter indirekte udforskningen af multi-kinase-strategier — inklusive NTRK/ROS1-hemmere såsom entrectinib — til behandlings-refraktær MEN2-associeret MTC. |

---

## Cytotoxicitet

Entrectinib er en antineoplastisk målrettet terapi godkendt til onkologiske indikationer (NTRK fusionspositive solide tumorer; ROS1-positive NSCLC).

| Punkt | Indhold |
|-------|---------|
| Cytotoxicitet-klassifikation | Målrettet terapi — Multikinase-hemmer (NTRK1/2/3, ROS1, ALK); ikke et konventionelt cytotoxisk middel |
| Myelosuppressionrisiko | Lav til moderat — anæmi er den hyppigst rapporterede hæmatologiske bivirkning; neutropeni og trombocytopeni forekommer men er mindre almindelig end ved konventionel cytotoxisk kemoterapy |
| Emetogenicitet-klassifikation | Lav — kvalme rapporteres men er typisk mild til moderat i sværhedsgrad for orale målrettede midler af denne klasse |
| Overvågningspunkter | Fuldt blodtal (CBC med differential), leverfunction (ALT, AST, total bilirubin), nyrefunktion, hjertemonitorering (ECG for QTc-forlængelse, vurdering for kongestiv hjerteinsufficiens) og neurologisk vurdering (kognitive effekter, svimmelhed, humørændringer og søvnforstyrrelser er klasse-relaterede CNS-effekter) |
| Håndteringsbeskyttelse | Standard cytotoxisk oral lægemiddelhåndtering-forholdsregler gælder; følg institutionelle retningslinjer for klargøring, dispensering og bortskaffelse af orale antineoplastiske midler |

---

## Sikkerhedshensyn

Detaljerede advarselserklæringer, kontraindikationer og lægemiddelinteraktionsdata er ikke tilgængelige i det aktuelle bevismateriell.

> Se venligst godkendelsessammendraget af produktkarakteristika (SmPC) for Rozlytrek (entrectinib) — tilgængeligt via EMA produktsiden — for komplet sikkerhedsinformation. Vigtige områder at gennemgå omfatter kardiel toksicitet (kongestiv hjerteinsufficiens, QTc-forlængelse), CNS-effekter (kognitiv svækkelse, humørforstyrrelser, søvnforstyrrelser), hepatotoksicitet, embryo-fetal toksicitet og farmakokinetiske interaktioner med stærke CYP3A4-inducere og inhibitorer.

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
På trods af en høj TxGNN-forudsigelsesscore (98.58%), er de tilgængelige beviser for entrectinib specifikt ved Multiple Endokrin Neoplasi indirekte og utilstrækkelige til at understøtte klinisk brug eller et formelt repurposing-program på dette tidspunkt. Hverken identificeret klinisk forsøg er designet til eller inkluderer MEN-patienter, det eneste litteraturbevises vedrører resistensmekanismer i RET-drevet MTC snarere end direkte NTRK/ROS1-målrettet anti-tumor-efficacy ved MEN, og entrectinib har ingen registreret national markedsføringstilladelse i Danmark for nogen indikation.

**For at fortsætte, er følgende nødvendigt:**

- **Biomarker-screening**: Systematisk molekylær profilering af MEN-associerede tumor-kohorter (MTC, pNETs, fæokromocytom) til at bestemme prævalensen af NTRK-genfusioner, ROS1-omlokalisering eller ALK-alterationer som ville indikere on-target-aktivitet af entrectinib
- **Præklinisk validering**: Cell line og patient-derived xenograft-studier i MEN tumor-modeller til at demonstrere meningsfuld anti-tumor-aktivitet af entrectinib
- **Dedikeret klinisk beviser**: Prospektive basket-forsøgsdata eller registerbaserede observationelle beviser specifikt inklusive MEN-patienter med NTRK/ROS1/ALK-positive tumorer
- **Komplet sikkerhedsvurdering**: Formaliseret gennemgang af Rozlytrek SmPC, inklusive evaluering af lægemiddelinteraktioner relevante for MEN-behandlingskonteksten (f.eks. samtidig brug af somatostatin-analoger, protonpumpehemmere, antihypertensive midler)
- **Regulatorisk præcisering**: Bekræftelse af EMA centraliseret tilladelsestatus for Rozlytrek i Danmark og vurdering af gennemførligheden af et off-label-brugsprogram eller udvidet indikationsansøgning via EMA's Type II variation-vej

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

