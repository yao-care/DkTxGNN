---
layout: default
title: Allopurinol
parent: Kun modelforudsigelse (L5)
nav_order: 27
evidence_level: L5
indication_count: 10
---

# Allopurinol
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

# Allopurinol: Fra gigt/hyperurikæmi til hepatisk porfyri

## Resumé

Allopurinol er en xanthinoxidasehæmmer, som er markedsført i Danmark som tabletter. Evidence Pack indeholder ingen godkendt indikationstekst, og den almindelige anvendelse mod gigt og hyperurikæmi er derfor ikke dokumenteret i grunddata.
TxGNN-modellen forudsiger, at allopurinol kan have effekt ved **hepatisk porfyri**, men der er **0 kliniske forsøg** og kun **2 publikationer**. Ingen af dem nævner allopurinol, så evidensen er meget svag.

---

## Hurtig oversigt

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Ikke angivet i den danske registrering (indikationsteksten er tom) |
| Foreslået ny indikation | Hepatisk porfyri |
| TxGNN-prædiktionsscore | 99,95 % |
| Evidensniveau | L4 (kun præklinisk/hypotese, ingen direkte data for allopurinol) |
| Status på det danske marked | Markedsført |
| Antal markedsføringstilladelser | 1 |
| Anbefalet beslutning | Hold |

---

## Hvorfor kan forudsigelsen give mening?

Der foreligger ingen detaljerede data om virkningsmekanismen. Allopurinol er en xanthinoxidasehæmmer, men Evidence Pack indeholder ingen dokumenteret sammenhæng med hepatisk porfyri.

De to fundne artikler handler om hæmbiosyntese, herunder regulering af 5-aminolevulinatsyntase (ALAS1) og carbamazepins effekt på hæmmetabolismen i rottelever. Ingen af titlerne nævner allopurinol, så koblingen er uverificeret.

Der er også en sikkerhedsmæssig bekymring. Allopurinol er kendt for at påvirke leverens hæm- og cytokrom P450-metabolisme, og det kan forværre porfyri i stedet for at forbedre den. Om effekten er gavnlig eller skadelig, er uafklaret og kræver manuel gennemgang, før der tages yderligere skridt.

Den høje score (0,9995) er ikke forklaret af de leverede data.

---

## Klinisk evidens

Der er på nuværende tidspunkt ingen relaterede kliniske forsøg registreret.

---

## Litteraturevidens

| PMID | År | Type | Tidsskrift | Hovedfund |
|------|-----|------|------|---------|
| [31443750](https://pubmed.ncbi.nlm.nih.gov/31443750/) | 2019 | Hypotese/review | Medical Hypotheses | Foreslår metabolisk målretning af 5-ALAS via tryptophan eller hæmning af hæmforbrug ved tryptophan-2,3-dioxygenase som mulig behandling af akutte hepatiske porfyrier. Nævner ikke allopurinol i titlen. |
| [1567472](https://pubmed.ncbi.nlm.nih.gov/1567472/) | 1992 | Præklinisk (rotte) | Biochemical Pharmacology | Carbamazepin i lav dosis forværrede tab af hæm i rottelever og virkede som porfyri-eksacerbator. Nævner ikke allopurinol i titlen. |

---

## Information om det danske marked

| Markedsføringstilladelsesnummer | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28106017917 | Allopurinol "Accord" (Accord Healthcare B.V.) | Tabletter | Ikke angivet |

Administrationsvej: oral.

---

## Sikkerhedsovervejelser

Der er ingen tilgængelige data om advarsler, kontraindikationer eller interaktioner (interaktionssøgningen gav ingen resultater). Se det godkendte produktresumé (SmPC) for sikkerhedsoplysninger.

Specifikt for den foreslåede indikation kan allopurinols påvirkning af hepatisk hæm- og CYP450-metabolisme potentielt forværre porfyri. Det skal afklares, før noget forsøg overvejes.

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Trods en meget høj modelscore findes ingen kliniske forsøg og ingen litteratur, der direkte omhandler allopurinol ved hepatisk porfyri. Retningen af effekten er uafklaret, og der er risiko for forværring.

De øvrige forudsigelser (hepatoportal sklerose, primær portalveretrombose, tidligt debuterende familiær ikke-cirrotisk portal hypertension, hepatopulmonalt syndrom og idiopatisk kobberassocieret cirrose) har alle evidensniveau L5. Deres identiske scores (0,99943) tyder på en artefakt fra grafens nabolag snarere end et indikationsspecifikt signal, og de bør heller ikke forfølges på nuværende grundlag.

**For at komme videre kræves:**
- Manuel gennemgang af, hvorfor videngrafen kobler allopurinol til hepatisk porfyri, og i hvilken retning effekten går
- Gennemgang af produktresuméet fra Lægemiddelstyrelsen (advarsler, kontraindikationer, godkendt indikation)
- Data om virkningsmekanisme fra DrugBank
- Målrettet litteratursøgning på allopurinol og porfyri, herunder rapporter om forværring
- Vurdering af administrationsvej og ligheden mellem den oprindelige og den foreslåede indikation

---

*Resultaterne er kun til forskningsbrug og udgør ikke medicinsk rådgivning. Kandidater til lægemiddelrepurposing kræver klinisk validering, før de kan anvendes.*
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

