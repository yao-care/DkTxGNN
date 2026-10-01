---
layout: default
title: Idarucizumab
parent: Kun modelforudsigelse (L5)
nav_order: 223
evidence_level: L5
indication_count: 10
---

# Idarucizumab
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

# Idarucizumab: Fra dabigatran-reversering til hæmoglobinopati

## Resumé i én sætning

Idarucizumab (Praxbind) er et humaniseret Fab-fragment, der binder dabigatran og neutraliserer dets antikoagulerende effekt.
TxGNN-modellen forudsiger, at det kan have effekt ved **hæmoglobinopati**, men der er **ingen kliniske forsøg og ingen publikationer**, der understøtter forudsigelsen.
Forudsigelsen vurderes som sandsynligvis et artefakt i vidensgrafen og ikke som et reelt lægemiddelrepositioneringsspor.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Reversering af dabigatrans antikoagulerende effekt (ud fra mekanismebeskrivelsen; indikationsteksten er ikke angivet i de danske registerdata) |
| Forudsagt ny indikation | Hæmoglobinopati |
| TxGNN-forudsigelsesscore | 95,7 % |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført |
| Antal markedsføringstilladelser | 1 |
| Anbefalet beslutning | Hold |

Øvrige forudsigelser har tilsvarende høje scorer, men samme evidensgrundlag (L5, ingen studier):

| Forudsagt indikation | TxGNN-score |
|------|------|
| Reumatoid arthritis | 95,5 % |
| Partiel deletion af den korte arm af kromosom 16 | 95,0 % |
| Beta-thalassæmi med andre manifestationer | 95,0 % |
| Pyruvatkinasemangel i røde blodlegemer | 94,8 % |

Posterne optrådte to gange i inputtet og er slået sammen i denne rapport.

---

## Hvorfor er forudsigelsen rimelig?

Der foreligger i øjeblikket ingen detaljerede data om virkningsmekanismen i Evidence Pack. Ud fra kendt information er idarucizumab et målrettet antistoffragment, der binder dabigatran med høj affinitet og ophæver dets effekt. Lægemidlet har ingen kendt virkning på globinsyntese, hæmoglobinstabilitet, erytropoiese eller røde blodlegemers stofskifte.

Der er derfor ikke identificeret nogen plausibel mekanistisk forbindelse mellem den oprindelige indikation og de forudsagte sygdomme:

- **Hæmoglobinopati og beta-thalassæmi:** skyldes nedsat eller manglende globinkædesyntese. Idarucizumab påvirker hverken globinekspression eller jernhåndtering.
- **Pyruvatkinasemangel:** er en arvelig enzymdefekt i erytrocytternes glykolyse. Idarucizumab har ingen kendt effekt på PKLR-enzymfunktionen.
- **Reumatoid arthritis:** idarucizumab har ingen kendt immunmodulerende eller antiinflammatorisk aktivitet og ingen rationale for at påvirke TNF-, IL-6- eller andre RA-signalveje.
- **Partiel deletion af kromosom 16p:** er en kromosomal strukturel forstyrrelse. Et lægemiddel, der neutraliserer dabigatran, kan ikke korrigere tab af gendosis.

De høje scorer afspejler sandsynligvis nærhed i vidensgrafen via hæmatologiske knudepunkter (fx alfa-globingener på 16p) og ikke et farmakologisk grundlag.

---

## Klinisk evidens

Der er i øjeblikket ingen relaterede kliniske forsøg registreret.

---

## Litteraturevidens

Der er i øjeblikket ingen relateret litteratur tilgængelig.

---

## Markedsinformation i Danmark

| Markedsføringstilladelsesnr. | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28105566415 | Praxbind (Boehringer Ingelheim Int. GmbH) | Injektions-/infusionsvæske, opløsning | Ikke angivet i registerdata |

---

## Sikkerhedsovervejelser

Se det godkendte produktresumé (SmPC) for sikkerhedsoplysninger. Der er ikke fundet data om interaktioner i Evidence Pack.

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelserne bygger udelukkende på modelscorer (L5) uden kliniske forsøg eller litteratur, og der er ikke identificeret nogen plausibel mekanistisk forbindelse. Det skønnes, at de høje scorer er artefakter i vidensgrafen.

**For at komme videre kræves:**
- Hentning og gennemgang af produktresumeet fra Lægemiddelstyrelsen (advarsler og kontraindikationer er ikke tilgængelige, hvilket blokerer sikkerhedsscreeningen)
- Detaljerede data om virkningsmekanisme (MOA), fx fra DrugBank
- Et konkret biologisk rationale og prækliniske data, før et repositioneringsspor kan genovervejes
- Bekræftelse af den godkendte indikationstekst for Praxbind i Danmark

*Resultaterne er kun til forskningsbrug og udgør ikke medicinsk rådgivning. Forudsigelserne kræver klinisk validering, før de kan anvendes.*
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

