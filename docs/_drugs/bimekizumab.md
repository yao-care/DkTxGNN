---
layout: default
title: Bimekizumab
parent: Kun modelforudsigelse (L5)
nav_order: 65
evidence_level: L5
indication_count: 10
---

# Bimekizumab
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

# Bimekizumab: Fra inflammatorisk sygdom til diabetisk katarakt

## Et-linie sammendrag

Bimekizumab (Bimzelx) er et humaniseret monoklonalt antistof, der dobbelt hæmmer både IL-17A og IL-17F, indiceret for immunmedierede inflammatoriske tilstande såsom moderat til svær plakatpsoaisis og aksial spondyloartritis.
TxGNN-modellen forudsiger, at det kan være effektivt til **diabetisk katarakt**, med **0 kliniske forsøg** og **0 publikationer**, der i øjeblikket understøtter denne retning.
Denne forudsigelse er klassificeret som et **L5**-signal — kun modelbaseret — og mekanistisk rationale for, at en IL-17A/F-hæmmer virker på linsestofskiftet, er i øjeblikket fraværende; denne rapport anbefaler **Hold** i afventning af vurdering af biologisk plausibilitet.

---

## Hurtig oversigt

| Emne | Indhold |
|------|---------|
| Oprindelig indikation | Inflammatoriske tilstande (plakatpsoaisis / aksial spondyloartritis); ingen dansk MA fundet i dette datasæt |
| Forudsagt ny indikation | Diabetisk katarakt |
| TxGNN-forudsigelsesscore | 98,23% |
| Evidensniveau | L5 |
| Status på det danske marked | Ikke markedsført (ingen godkendelse fundet i dette datasæt) |
| Antal markedsføringstilladelser | 0 |
| Anbefalet beslutning | **Hold** |

> ⚠️ **Datanotat**: Det regulatoriske datasæt, der blev søgt i, returnerede 0 danske markedsføringstilladelser for bimekizumab. Bimekizumab (handelsnavn **Bimzelx**) modtog imidlertid en centraliseret EMA-markedsføringstilladelse i 2023, der dækker alle EU/EØS-medlemsstater, herunder Danmark. En genforespørgsel mod EMA-produktdatabasen anbefales for at udfylde dette hul, før endelige lovgivningsmæssige konklusioner drages.

---

## Hvorfor er denne forudsigelse rimelig?

Bimekizumab er et humaniseret IgG1-monoklonalt antistof, der selektivt binder og neutraliserer både **IL-17A og IL-17F**, to relaterede pro-inflammatoriske cytokiner fra Th17-signalvejen. Ved at blokere begge isoformer samtidigt reducerer bimekizumab downstream inflammatorisk signalering mere fuldstændigt end midler, der målretter sig mod IL-17A alene. Dets etablerede kliniske nytte er inden for immunmedierede inflammatoriske tilstande — især plakatpsoaisis, psoriasis arthritis og aksial spondyloartritis — hvor Th17-drevet inflammation er en central patologisk drivkraft.

Diabetisk katarakt er derimod primært en **metabolisk sygdom i det okulære linse**. De dominerende patofysiologiske mekanismer omfatter ophobning af sorbitol gennem polyolstien, non-enzymatisk glycering af krystallinproteiner og oxidativt stress, der fører til progressiv linseopaquitet. Selvom systemisk lavgradig inflammation ved type 2-diabetes (inklusive Th17-celleaktivering og forhøjede cirkulerende IL-17) bidrager til endeorganskader bredt, er der **ingen etableret mekanistisk forbindelse** mellem IL-17A/F-signalering og de lokale intraokulære metaboliske ændringer, der driver linseforurening.

Bemærkelsesværdigt klynges alle de 10 vigtigste TxGNN-forudsigelser for bimekizumab eksklusivt omkring **kataraktsubtyper** (diabetisk, modnet, umenlig, tetanisk, kraniostenose-associeret) med næsten identiske forudsigelsesscore (0,9812–0,9823). Dette mønster er stærkt konsistent med en **klyngeartefakt i vidensgrafen** — modellen kan have identificeret indirekte sygdomsontologi-linkages i stedet for et sandt farmakologisk signal. De mekanistiske vurderinger, der er indlejret i denne Evidenspakke, markerer konsekvent disse forudsigelser som sandsynlige falske positiver. Formel validering gennem vejanalyse eller vejledende laboratoriestudier ville være nødvendige for at hæve signalet over L5.

---

## Evidens fra kliniske forsøg

Der er i øjeblikket ingen relaterede kliniske forsøg registreret.

---

## Litteratur evidens

Der er i øjeblikket ingen relateret litteratur tilgængelig.

---

## Markeds- og regulatoriske informationer for Danmark

Ingen markedsføringstilladelser blev returneret af det regulatoriske datasæt for denne forespørgsel. Baseret på offentligt tilgængelig information er følgende godkendelse kendt som relevant:

| Markedsføringstilladelsesnummer | Produktnavn | Doseringsform | Godkendt indikation |
|-------------------------------|-------------|-------------|-------------------|
| EU/1/23/1743 *(EMA — verifikation mod aktuel register anbefales)* | Bimzelx | Opløsning til injektion (fyldt pen/sprøjte) | Moderat til svær plakatpsoaisis hos voksne; aktiv psoriasis arthritis; aktiv aksial spondyloartritis (nr-axSpA og AS) |

> En direkte genforespørgsel af [EMA-produktdatabasen](https://www.ema.europa.eu/en/medicines/human/EPAR/bimzelx) og Lægemiddelstyrelsens [produktresumé-database](https://laegemiddelstyrelsen.dk/) er påkrævet for at bekræfte aktuel status og fuldt indikationsomfang.

---

## Sikkerhedshensyn

Detaljerede sikkerhedsoplysninger (vigtige advarsler, kontraindikationer og lægemiddelinteraktioner) blev ikke hentet i denne Evidenspakke. Se venligst produktresuméet (SmPC) for Bimzelx for fuldstændige sikkerhedsoplysninger, tilgængeligt via [EMA EPAR-siden](https://www.ema.europa.eu/en/medicines/human/EPAR/bimzelx) og Lægemiddelstyrelsens produktdatabase.

Kendte klassemæssige hensyn for IL-17-hæmmere omfatter:
- Risiko for alvorlige infektioner (herunder Candida-infektioner)
- Inflammatorisk tarmsygdom (nyopdukket eller forværring)
- Overfølsomhedsreaktioner
- Brug under graviditet og amning kræver vurdering

---

## Konklusion og næste trin

**Beslutning: Hold**

**Rationale:**
TxGNN-forudsigelsen af bimekizumab til diabetisk katarakt understøttes i øjeblikket af **ingen kliniske forsøg og ingen publiceret litteratur**, og den mekanistiske forbindelse mellem IL-17A/F-hæmning og linsestofskifte er **ikke etableret** — klyngningen af alle katarakttyper på tværs af alle 10 forudsagte indikationer tyder stærkt på en vidensgrafs falsk positiv snarere end et ægte omformål-signal.

**For at fortsætte er følgende nødvendigt:**

- **Biologisk plausibilitetsvurdering**: En struktureret litteratursøgning, der specifikt undersøger enhver IL-17/Th17-akse-involvering i linse-stofskifte, polyolsti-regulering eller krystallin-glycering — for at afgøre, om den indirekte inflammatoriske vej plausibelt kunne forbindes til linsebeskyttelse
- **KG-artefaktundersøgelse**: Undersøg TxGNN-vidensgrafen undergraf, der forbinder bimekizumab-knuder til kataraktysygdomsknuder for at identificere, om den høje score afspejler delte opstrømsmetabolske knuder (f.eks. diabetes-relaterede) snarere end en direkte farmakologisk relation
- **Re-query af regulatoriske data**: Genafvikl den danske markedsføringstilladelsessøgning mod EMA-databasen for centralisering for korrekt at registrere Bimzelx's eksisterende tilladelse og fuldt godkendte indikationer
- **MOA-datahentning**: Hent den komplette DrugBank-mekanisme for handlings-post for bimekizumab (DB12917) for at muliggøre formel mekanistisk gapanalyse
- **Sikkerhedsdatahentning**: Download og parse Bimzelx SmPC/EPAR-sikkerhedsdataene for at muliggøre en fuldstændig S1-sikkerhedsvurdering før nogle yderligere udviklingsstrin overvejes

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

