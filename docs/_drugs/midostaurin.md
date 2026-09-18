---
layout: default
title: Midostaurin
parent: Kun modelforudsigelse (L5)
nav_order: 290
evidence_level: L5
indication_count: 0
---

# Midostaurin
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

# Midostaurin (DB06595): Vurdering af Lægemiddels Genanvendelse — TxGNN-forudsigelsesdata ikke tilgængelig

---

## Resumé på én sætning

Midostaurin (Rydapt®) er en multi-målrettet kinasehæmmer med etableret antineoplastisk aktivitet, navnlig godkendt i EU til FLT3-muteret akut myeloid leukæmi og avanceret systemisk mastocytose.
Den nuværende Evidenspakke indeholder **ingen TxGNN-genanvendelsesforudsigelser** for dette lægemiddel, og to kritiske datafelter — virkningsmekanisme og nationale forskrivningsoplysninger — mangler.
**En fuldstændig vurdering af lægemiddels genanvendelse kan ikke udføres på nuværende tidspunkt; en Hold-beslutning anbefales i afventning af datareparation.**

---

## Hurtig oversigt

| Punkt | Indhold |
|------|---------|
| Oprindelig indikation | FLT3-muteret AML; avanceret systemisk mastocytose *(stammer fra generelle farmaceutiske oplysninger — fraværende fra Evidenspakke)* |
| Forudsagt ny indikation | Ikke tilgængelig — TxGNN-pipeline'et returnerede ingen kandidater |
| TxGNN-forudsigelsesscore | Ikke tilgængelig |
| Bevisniveau | Kan ikke bestemmes |
| Markedsstatus i Danmark | Ikke fundet i Laegemiddelstyrelses nationale register |
| Antal markedsføringstilladelser | 0 (forespørgsel til nationalt register) |
| Anbefalet beslutning | **Hold** |

---

## Hvorfor ingen forudsigelse er tilgængelig

Evidenspakken til midostaurin (DB06595) indeholder en tom `predicted_indications` array, hvilket betyder, at TxGNN-pipeline'et ikke returnerede nogen genanvendelseskandidater på tidspunktet for dataafskæring (2026-04-04). To kritiske datagab tidligere i processen formentlig foranledigede denne fejl:

**Manglende virkningsmekanisme (MOA).** DrugBank-forespørgslen returnerede en resultatpost (forespørgsels-log-ID 2, status: succes), men feltet `original_moa` blev ikke udfyldt. Uden en farmakologisk mekanismeprofil mangler TxGNN-grafmodellen de nodekarakteristika, der er nødvendige for pålidelig scoring af lægemiddel–sygdoms-koblinger.

**Manglende regulatoriske forskrivningsoplysninger.** Forespørgslen til Laegemiddelstyrelses register returnerede nul tilladelser. Bemærkelsesværdigt holder midostaurin en EMA-centraliseret markedsføringstilladelse (Rydapt®, EU/1/17/1213, givet juni 2017) til brug i Danmark og andre EU-medlemsstater. Forespørgslen til det nationale register synes ikke at have erfasset denne centraliserede godkendelsesprocedure, hvilket efterlader indikationsvokabular ukoordineret. Dette begrænser direkte sygdoms-node-tilpasning i vidensgrafen og kan have undertrykt kandidatgenerering.

Indtil disse gab er lukket, ville enhver genanvendelseshypotese for midostaurin hvile udelukkende på modelens strukturelle grafinferens, uden farmakologisk eller regulatorisk kontekst — hvilket er utilstrækkeligt for en klinisk evaluering.

---

## Markedsoplysninger for Danmark

Evidenspakken rapporterer nul markedsføringstilladelser via Laegemiddelstyrelses nationale register. Baseret på offentligt tilgængelige farmaceutiske registre holder Rydapt® (midostaurin 25 mg hårde kapsler, Novartis) en EMA-centraliseret godkendelse, der er tilgængelig i Danmark; dette skal dog formelt verificeres før næste pipeline-køring.

| Bemærkning | Detail |
|------|--------|
| Resultat af nationale registerforespørgsel | 0 tilladelser hentet |
| Forventet EMA-godkendelse | EU/1/17/1213 (Rydapt® — kræver verificering) |
| Anbefalet handling | Forespørg EMA EPAR-database direkte; bekræft, at produktet er på den danske lægemiddelliste, og hent den godkendte indikationstekst til sygdommapping |

---

## Cytotoksicitet

Midostaurin klassificeres som et antineoplastisk middel på grundlag af dets godkendte indikationer (AML, systemisk mastocytose) og dets virkningsmekanisme som en multi-målrettet proteinkinasehæmmer. Afsnittet nedenfor er baseret på generelle farmaceutiske oplysninger, da Evidenspakken ikke leverede lægemiddelniveau-sikkerhedsdata; alle poster bør verificeres mod det aktuelle SmPC før klinisk brug.

| Punkt | Indhold |
|------|---------|
| Cytotoksicitet-klassifikation | Målrettet terapi — multi-målrettet proteinkinasehæmmer (FLT3, KIT, PDGFR, PKC-isoformer, VEGFR-2) |
| Myelosuppressionsrisiko | Høj, når den bruges i AML-induktionsregimener (febril neutropeni, anæmi, trombocytopeni er velkarakteriseret i kombination med cytarabin/daunorubicin) |
| Emetogenicitet-klassifikation | Lav til moderat |
| Overvågningspunkter | Fuldt blodtal med differential, leverfunktionsprøver (ALT/AST/bilirubin), nyrefunktion, QTc-interval, lungefunktion (risiko for interstitiel lungesygdom) |
| Håndteringsbeskyttelse | Skal følge regulering for håndtering af cytotoksiske lægemidler i henhold til lokale farmaceutiske retningslinjer |

---

## Sikkerhedshensyn

Evidenspakken indeholdt ikke sikkerhedsadvarsler, kontraindikationer eller lægemiddel-interaktionsdata for midostaurin. Se venligst det godkendte Produktresume (SmPC) for alle sikkerhedsoplysninger før enhver klinisk eller forskningsmæssig brug.

---

## Konklusion og næste trin

**Beslutning: Hold**

**Begrundelse:**
Evidenspakken er kritisk ufuldstændig — ingen TxGNN-genanvendelsesforudsigelser blev genereret, og de to datagab klassificeret som Blokerend/Høj alvorlighed (forskrivningsoplysninger og MOA) forhindrer direkte både forudsigelsespipeline'et i at fungere og sikkerhedsscreening i at fortsætte. At generere en genanvendelsesanbefaling under disse betingelser ville ikke være klinisk ansvarligt.

**For at fortsætte, er følgende nødvendigt:**

1. **Undersøg tomt forudsigelsesoutput** — Bestem, om pipeline'et fejlede stilfærdigt (f.eks. DrugBank ID DB06595 ikke matchet til en KG-node, eller alle scores under rapporteringsgrænsværdien). Gennemgå `run_kg_prediction.py` logge for midostaurin.
2. **Hent MOA-data (DG002)** — Forespørg DrugBank API til DB06595 farmakologi, virkningsmekanisme og lægemiddelkategorier. Forespørgselsloggen bekræfter, at et vellykket DrugBank hit findes; MOA-feltet skal ekstraheres og udfyldes.
3. **Hent nationale forskrivningsoplysninger (DG001)** — Download og parse Rydapt® SmPC fra enten EMA EPAR-databasen (EU/1/17/1213) eller Laegemiddelstyrelses produktportal til at udfylde advarsler, kontraindikationer og godkendt indikationstekst.
4. **Genjuster sygdomsvokabular** — Når først den godkendte indikationstekst er tilgængelig, kør sygdommapping igen for at sikre, at AML og mastocytose-noder er korrekt forbundet i vidensgrafen.
5. **Regenerer Evidenspakke** — Efter at have løst alle datagab, genudføre det fuldstændige pipeline til bevisindsamling, og regenerer denne rapport. En fuldstændig evaluering med TxGNN-forudsigelser, klinisk forsøgsbevis og sikkerhedsscreening bør derefter være mulig.

---

*Denne rapport er kun beregnet til forskningsmæssige formål og udgør ikke medicinsk rådgivning. Alle genanvendelseskandidater kræver klinisk validering før enhver terapeutisk brug.*

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

