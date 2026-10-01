---
layout: default
title: Ravulizumab
parent: Kun modelforudsigelse (L5)
nav_order: 368
evidence_level: L5
indication_count: 10
---

# Ravulizumab
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

# Ravulizumab: Fra komplementhæmning til alvorlig medfødt neutropeni (G6PC3-mangel)

## Resumé

Ravulizumab er et langtidsvirkende monoklonalt antistof mod komplementfaktor C5. Det er markedsført i Danmark som Ultomiris. TxGNN-modellen forudsiger, at det kan have effekt ved **autosomal recessiv svær medfødt neutropeni pga. G6PC3-mangel**. Der er dog **ingen kliniske forsøg og ingen publikationer**, der understøtter forudsigelsen, og der er ikke identificeret nogen plausibel biologisk sammenhæng.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Ikke angivet i de tilgængelige data (godkendelsesteksten er tom) |
| Forudsagt ny indikation | Autosomal recessiv svær medfødt neutropeni pga. G6PC3-mangel |
| TxGNN-forudsigelsesscore | 99,96 % |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført |
| Antal markedsføringstilladelser | 1 |
| Anbefalet beslutning | Hold |

---

## Hvorfor er forudsigelsen (ikke) rimelig?

Detaljerede data om virkningsmekanismen (MOA) er ikke tilgængelige i datagrundlaget. Ravulizumab er et anti-C5-antistof, der blokerer den terminale komplementaktivering.

G6PC3-mangel giver neutropeni via nedsat glukose-6-phosphatase-aktivitet, metabolisk stress i neutrofile granulocytter og øget apoptose. Denne mekanisme involverer ikke komplement C5. Den meget høje score (0,9996) afspejler sandsynligvis grafens topologi, f.eks. fælles naboknuder knyttet til neutropeni, og ikke en biologisk begrundelse.

De øvrige forudsigelser i top 10 er vurderet på samme måde:

- **Cyklisk hæmatopoese (cyklisk neutropeni):** Skyldes typisk ELANE-mutationer, som påvirker neutrofil elastase og myeloid modning. Det er uafhængigt af terminal komplementhæmning.
- **Svær medfødt neutropeni:** Skyldes genetiske defekter i granulopoiesen (f.eks. ELANE, HAX1, G6PC3). Standardbehandling er G-CSF og allogen stamcelletransplantation. Komplementhæmning adresserer ikke den underliggende defekt.
- **Autosomal recessiv svær medfødt neutropeni pga. CXCR2-mangel:** CXCR2-mangel forstyrrer neutrofil kemotaksi og frigivelse fra knoglemarven. C5-hæmning genopretter ikke denne signalvej, og C5a-signalering via C5aR1 er en separat akse.
- **Primær hyperoxaluri:** Her er forbindelsen svag og indirekte. Calciumoxalatkrystaller kan udløse inflammation (f.eks. NLRP3-inflammasomaktivering) og muligvis involvere komplement ved nyreskade. Sygdommen drives dog af defekter i leverens glyoxylatmetabolisme (AGXT, GRHPR, HOGA1) og behandles med substratreduktion (RNAi mod HAO1 eller LDHA) og hydrering. Der er ingen data, så det forbliver en ren hypotese.

---

## Evidens fra kliniske forsøg

Der er i øjeblikket ingen relaterede kliniske forsøg registreret.

---

## Litteraturevidens

Der er i øjeblikket ingen relateret litteratur tilgængelig.

---

## Markedsinformation for Danmark

| Markedsføringstilladelsesnr. | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28106375119 | Ultomiris (Alexion Europe SAS) | Koncentrat til infusionsvæske, opløsning | Ikke angivet i data |

---

## Sikkerhedsovervejelser

Der er ikke fundet interaktionsdata for ravulizumab i den anvendte kilde. For advarsler, kontraindikationer og interaktioner henvises til det godkendte produktresumé (SmPC).

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelsen hviler udelukkende på modellen (L5). Der er ingen kliniske forsøg eller publikationer, og der er ingen plausibel mekanistisk sammenhæng mellem C5-hæmning og de forudsagte neutropeni-sygdomme. Den høje score skyldes sandsynligvis en artefakt i vidensgrafen.

**For at komme videre kræves følgende:**
- Hentning og gennemgang af produktresumé (SmPC) fra Lægemiddelstyrelsen, som er en forudsætning for sikkerhedsscreening
- Data om virkningsmekanisme (MOA) fra DrugBank
- Præklinisk eller mekanistisk evidens for en rolle for komplement C5 ved de forudsagte sygdomme
- En litteratur- og forsøgssøgning målrettet de forudsagte indikationer, hvis forudsigelsen skal undersøges videre

*Disse resultater er kun til forskningsbrug og udgør ikke medicinsk rådgivning. Forudsigelser skal valideres klinisk, før de kan anvendes.*
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

