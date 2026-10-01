---
layout: default
title: Toripalimab
parent: Kun modelforudsigelse (L5)
nav_order: 444
evidence_level: L5
indication_count: 10
---

# Toripalimab
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

# Toripalimab: Fra PD-1-hæmmer til blandet type autoimmun hæmolytisk anæmi

## Resumé

Toripalimab er et monoklonalt antistof, der blokerer PD-1 (en immun-checkpoint-hæmmer). I Danmark markedsføres det som LOQTORZI.
TxGNN-modellen forudsiger, at det kan have effekt ved **blandet type autoimmun hæmolytisk anæmi**, men der er **0 kliniske forsøg** og **0 publikationer**, der understøtter forudsigelsen.
Den biologiske logik peger desuden i modsat retning: PD-1-blokade kan udløse eller forværre netop denne type autoimmun sygdom.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Forudsagt ny indikation | Blandet type autoimmun hæmolytisk anæmi |
| TxGNN-prediktionsscore | 93,76 % |
| Evidensniveau | L5 (kun modelforudsigelse) |
| Status på det danske marked | Markedsført |
| Antal markedsføringstilladelser | 1 |
| Anbefalet beslutning | Hold |

---

## Hvorfor er denne forudsigelse (ikke) rimelig?

Detaljerede data om virkningsmekanismen (MOA) er ikke tilgængelige i evidenspakken. Toripalimab er dog en PD-1-blokerende antistofbehandling. PD-1-blokade ophæver T-cellernes tolerance og forventes derfor at *forværre* antistofmedieret autoimmunitet i stedet for at behandle den.

Autoimmun hæmolytisk anæmi er en kendt immunrelateret bivirkning ved PD-1/PD-L1-hæmmere. Den høje score (0,938) er ikke understøttet af forsøg eller litteratur. Den afspejler sandsynligvis en association i vidensgrafen, hvor virkningsretningen er ukendt eller omvendt. Sikkerhedssignalet vejer sandsynligvis tungere end et eventuelt terapeutisk argument.

Modellen foreslår også andre indikationer med lignende score. De har samme problem:

| Forudsagt indikation | Score | Vurdering af mekanistisk sammenhæng |
|------|------|------|
| Idiopatisk aplastisk anæmi | 93,76 % | Sygdommen drives af autoreaktive T-celler mod knoglemarvens stamceller. Checkpoint-blokade forventes at forstærke processen, og aplastisk anæmi er rapporteret som en sjælden immunrelateret bivirkning. |
| Dermatitis | 93,69 % | Udslæt og dermatitis er blandt de hyppigste immunrelaterede bivirkninger ved PD-1-hæmmere. Effektretningen er skade, ikke gavn. |
| Paroksysmal nattlig hæmoglobinuri (PNH) | 93,67 % | PNH er en komplementmedieret hæmolytisk sygdom. PD-1-blokade har ingen direkte kobling til komplementregulering. |
| Lægemiddelinduceret autoimmun hæmolytisk anæmi | 93,67 % | Tilstanden er udløst af lægemidler. PD-1-hæmmere er en mulig årsag, så sammenhængen er snarere kausal end terapeutisk. |

---

## Evidens fra kliniske forsøg

Der er i øjeblikket ingen relaterede kliniske forsøg registreret.

---

## Litteraturevidens

Der er i øjeblikket ingen relateret litteratur tilgængelig.

---

## Information om det danske marked

| Markedsføringstilladelsesnummer | Produktnavn | Lægemiddelform | Indehaver |
|---------|------|------|-----------|
| 28106870222 | LOQTORZI | Koncentrat til infusionsvæske, opløsning | Topalliance Biosciences Europe Limited |

---

## Cytotoksicitet

| Punkt | Indhold |
|------|------|
| Klassifikation | Immunterapi (PD-1 checkpoint-hæmmer), ikke konventionelt cytotoksisk middel |
| Øvrige oplysninger (myelosuppression, emetogenicitet, monitorering, håndtering) | Se advarsler og forsigtighedsregler i produktresuméet (SmPC) |

---

## Sikkerhedsovervejelser

- **Immunrelaterede bivirkninger, der overlapper med de forudsagte indikationer:** autoimmun hæmolytisk anæmi, aplastisk anæmi (sjælden) og udslæt/dermatitis er rapporteret ved PD-1-hæmmere. Det er et alvorligt sikkerhedssignal mod brug til disse tilstande.

Der foreligger ingen registrerede lægemiddelinteraktioner i evidenspakken. For øvrige advarsler og kontraindikationer henvises til det godkendte produktresumé (SmPC).

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelsen er kun modelbaseret (L5) og har ingen støtte fra kliniske forsøg eller litteratur. Den kendte virkningsretning for PD-1-blokade er snarere skade end gavn ved alle de forudsagte tilstande.

**For at komme videre kræves følgende:**
- Hentning og gennemgang af produktresuméet fra Lægemiddelstyrelsen (advarsler, kontraindikationer og godkendte indikationer), da sikkerhedsscreening ikke kan gennemføres uden
- Detaljerede data om virkningsmekanismen fra DrugBank
- Afklaring af virkningsretningen bag TxGNN-associationen (behandling eller bivirkning)
- Systematisk litteratursøgning efter case reports og immunrelaterede bivirkninger ved disse tilstande, før yderligere vurdering

*Resultaterne er udelukkende til forskningsbrug og udgør ikke medicinsk rådgivning. Kandidater til lægemiddelrepurposing skal valideres klinisk, før de kan anvendes.*
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

