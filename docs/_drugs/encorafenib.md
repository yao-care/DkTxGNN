---
layout: default
title: Encorafenib
parent: Kun modelforudsigelse (L5)
nav_order: 163
evidence_level: L5
indication_count: 0
---

# Encorafenib
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

# Encorafenib: Evaluering ufuldstændig — der blev ikke genereret præpositioneringsforudsigelser

## Sammenfatning i én sætning

Encorafenib (DB11718) er en selektiv BRAF-kinase-inhibitor, der bruges inden for onkologi.
Denne bevispakke **kunne ikke generere præpositioneringsforudsigelser**, da kritiske input — herunder den oprindeligt godkendte indikation, virkningsmekanisme og danske regulatoriske registre — ikke blev hentet med succes.
Denne rapport dokumenterer de aktuelle datahuller og skitserer de afhjælpningsskridt, der kræves, før en fuldstændig evaluering kan gennemføres.

---

## Hurtig oversigt

| Element | Indhold |
|---------|---------|
| Oprindelig indikation | Ikke hentet i denne bevispakke |
| Forudsagt ny indikation | Ingen — TxGNN gav intet resultat |
| TxGNN-forudsigelsesscore | N/A |
| Evidensniveau | Kan ikke vurderes |
| Markeds status i Danmark | Ikke markedsført (baseret på hentet data) |
| Antal markedsføringstilladelser | 0 |
| Anbefalet afgørelse | **Aflyst** |

---

## Kontekst: Hvorfor blev der ikke genereret nogen forudsigelse

Der blev ikke genereret nogen præpositioneringsforudsigelse for Encorafenib i denne bevispakke. Matrixen `predicted_indications` er tom, og både den oprindelige indikation og virkningsmekanisme blev markeret som datahuller — de to vigtigste input til TxGNN-forudsigelsespipelinen.

Fra offentligt tilgængelige kilder er det kendt, at Encorafenib er en selektiv **klasse VI BRAF-kinase-inhibitor** (varemærke Braftovi), godkendt kombineret med binimetinib til BRAF V600E/K-mutant uoperabel eller metastatisk melanom, og kombineret med cetuximab til BRAF V600E-mutant metastatisk colorectal kræft. Disse detaljer blev ikke registreret i bevispakken og kunne derfor ikke tjene som TxGNN-input. Indtil `original_indications` og `original_moa` er udfyldt, har modellen utilstrækkelig kontekst til at vurdere og rangordne præpositioneringskandidater.

To datahuller blokerer i øjeblikket fremskridtet:

| Huller-ID | Element | Alvorlighed | Påvirkning |
|-----------|---------|-------------|-----------|
| DG001 | Regulatoriske advarsler og kontraindikationer (SmPC) | **Blokerend** | Forhindrer sikkerhedspresscreening |
| DG002 | Virkningsmekanisme (MOA) | **Høj** | Forhindrer analyse af mekanistisk relevans og TxGNN-input |

---

## Markedsinformation for Danmark

Der blev ikke hentet markedsføringstilladelser for Encorafenib fra den danske regulatoriske database.

> **Vigtig note:** Encorafenib (Braftovi) har en centraliseret EMA-markedsføringstilladelse (EU/1/18/1314), der er gyldig i alle EU/EØS-medlemsstater, herunder Danmark. Det aktuelle `market_status: Not marketed` afspejler sandsynligvis et **henteproblem i bevispakkens pipeline** snarere end en faktisk fraværelse fra det danske marked. Det anbefales stærkt at bekræfte den aktuelle status direkte via [EMA-produktdatabasen](https://www.ema.europa.eu/en/medicines/human/EPAR/braftovi) eller Laegemiddelstyrelsen, inden der drages nogle regulatoriske konklusioner.

---

## Cytotoksicitet

Encorafenib er et antineoplastisk middel. Følgende er baseret på offentligt tilgængelige produktoplysninger, da der ikke blev inkluderet DrugBank-toksicitetsdata i denne bevispakke.

| Element | Indhold |
|---------|---------|
| Cytotoksicitetsklassifikation | Målrettet terapi — selektiv BRAF-kinase-inhibitor (klasse VI RAF-inhibitor) |
| Risiko for myelosuppression | Lav til moderat; anæmi og neutropeni er blevet rapporteret, men hæmatologisk toksicitet er mindre udtalt end ved konventionel cytotoksisk kemoterapy |
| Emetogenicitetsklassifikation | Lav til moderat (oral målrettet terapi) |
| Overvågningselementer | Fuldt blodtal (CBC med differential), leverfunktion (ALT, AST, bilirubin), nyrefunktion, dermatologisk vurdering (risiko for planocellulart carcinom), EKG (QTc-interval), oftalmologisk vurdering |
| Håndteringsbeskyttelse | Se venligst SmPC — standard oral cytotoksisk håndteringsprocedurer gælder; undgå at knuse eller dele kapsler |

---

## Sikkerhedshensyn

Se venligst det godkendte produktresumé (SmPC) for fuldstændige sikkerhedsoplysninger.

Der blev ikke hentet sikkerhedsdata (advarsler, kontraindikationer eller lægemiddelinteraktioner) i denne bevispakke. Huller DG001 er klassificeret som **blokerend** og skal løses, før nogen sikkerhedspresscreening kan gennemføres.

---

## Konklusion og næste trin

**Afgørelse: Aflyst**

**Begrundelse:**
Bevispakken for Encorafenib er ufuldstændig — der blev ikke hentet oprindelige indikationer, virkningsmekanisme, præpositioneringsforudsigelser eller sikkerhedsdata. En meningsfuld evaluering af præpositionering af lægemidler kan ikke gennemføres i den nuværende tilstand.

**For at fortsætte kræves følgende:**

- **Løs DG001 (blokerend):** Hent regulatoriske advarsler og kontraindikationer fra det godkendte SmPC — adgang via [EMA EPAR for Braftovi](https://www.ema.europa.eu/en/medicines/human/EPAR/braftovi) eller Laegemiddelstyrelsen
- **Løs DG002 (høj):** Søg i DrugBank API for DB11718 for at hente virkningsmekanismen
- **Udfyld `original_indications`:** Tilføj bekræftede godkendte indikationer (BRAF V600-mutant melanom; BRAF V600E-mutant metastatisk colorectal kræft) for at aktivere TxGNN-inputmapping
- **Genudgør TxGNN-forudsigelsespipelinen** når alle input er fuldstændige
- **Bekræft dansk markeds status:** Bekræft EMA-centraliseret autorisationsdækning — resultatet `market_status: Not marketed` er sandsynligvis et pipeline-henteproblem

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

