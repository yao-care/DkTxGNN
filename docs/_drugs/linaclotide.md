---
layout: default
title: Linaclotide
parent: Kun modelforudsigelse (L5)
nav_order: 266
evidence_level: L5
indication_count: 6
---

# Linaclotide
{: .fs-9 }

Evidensniveau: **L5** | Forudsagte indikationer: **6** stk.
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

# Linaclotid: Fra forstoppelsesrelaterede mave-tarmlidelser til Cauda equina-syndrom

## Resumé

Linaclotid er en guanylatcyklase-C-agonist, der virker lokalt i tarmen. Lægemidlet er markedsført i Danmark som Constella, men den registrerede indikationstekst indgår ikke i datagrundlaget. TxGNN-modellen forudsiger, at det kan have effekt ved **cauda equina-syndrom**, men der er **0 kliniske forsøg** og **0 publikationer**, der understøtter forudsigelsen. Den høje score skyldes sandsynligvis en artefakt i vidensgrafen.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Ikke angivet i den danske registrering. Anvendelsen er typisk IBS med forstoppelse eller kronisk forstoppelse |
| Forudsagt ny indikation | Cauda equina-syndrom |
| TxGNN-forudsigelsesscore | 99,96 % |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført |
| Antal markedsføringstilladelser | 1 |
| Anbefalet beslutning | Hold |

---

## Hvorfor er denne forudsigelse rimelig?

Der foreligger i øjeblikket ingen detaljerede data om virkningsmekanismen i kildedataene. Linaclotid er en guanylatcyklase-C-agonist, der øger cGMP i tarmen og kun absorberes minimalt systemisk. Virkningen er veldokumenteret ved forstoppelsesrelaterede tarmlidelser, men ikke ved nervesygdomme.

Der kan være en svag, indirekte sammenhæng. Cauda equina-syndrom medfører ofte neurogen tarmdysfunktion og forstoppelse, og linaclotid kunne i teorien lindre disse symptomer. Det er dog ikke sandsynligt, at lægemidlet påvirker den underliggende årsag, nemlig kompression af nerverødder. Tilstanden er et kirurgisk akutområde. Den høje modelscore bør derfor tolkes med stor forsigtighed.

**Øvrige forudsigelser (sammenlagt, da hver optrådte to gange i input):**

| Forudsagt indikation | TxGNN-score | Evidensniveau | Vurdering |
|------|------|------|------|
| Neurogen blære (markeret som forældet term i ontologien) | 99,89 % | L5 | Spekulativ. Sandsynligvis en artefakt i begrebsmapningen |
| Søvnløshed | 99,51 % | L5 | Ingen troværdig mekanistisk vej. Højst en indirekte effekt via bedre mave-tarmsymptomer |

---

## Klinisk evidens

Der er i øjeblikket ikke registreret nogen relaterede kliniske forsøg.

---

## Litteraturevidens

Der er i øjeblikket ingen relateret litteratur tilgængelig.

---

## Markedsinformation for Danmark

| Markedsføringstilladelse | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28104989611 | Constella (AbbVie Deutschland GmbH & Co. KG) | Kapsler, hårde | Ikke angivet i datagrundlaget |

---

## Sikkerhedsovervejelser

Der er ingen tilgængelige sikkerhedsdata i kildedataene, og interaktionssøgningen gav ingen resultater. Se det godkendte produktresumé (SmPC) for sikkerhedsoplysninger.

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelsen bygger udelukkende på modellen (L5) uden forsøg eller litteratur. Linaclotid har desuden minimal systemisk absorption, og der er ingen plausibel effekt på årsagen til cauda equina-syndrom. Sikkerhedsdata mangler helt.

**For at komme videre kræves følgende:**
- Download og gennemgang af produktresuméet fra Lægemiddelstyrelsen med advarsler og kontraindikationer
- Data om virkningsmekanisme (MOA), fx fra DrugBank
- Bekræftelse af den godkendte indikation for Constella i Danmark
- En klinisk vurdering af, om symptomlindring af neurogen tarmdysfunktion er et relevant og afgrænset mål, adskilt fra behandlingen af selve cauda equina-syndromet
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

