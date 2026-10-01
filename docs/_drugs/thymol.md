---
layout: default
title: Thymol
parent: Kun modelforudsigelse (L5)
nav_order: 432
evidence_level: L5
indication_count: 10
---

# Thymol
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

# Thymol: Fra veterinærlægemiddel (Apiguard Vet.) til interventrikulær septumaneurisme

## Resumé i få sætninger

Thymol er registreret i Danmark som aktivt stof i veterinærlægemidlet Apiguard Vet. (gel). Der er ikke registreret en godkendt indikationstekst i datagrundlaget.
TxGNN-modellen forudsiger, at stoffet kan have effekt ved **interventrikulær septumaneurisme**, men der findes **0 kliniske forsøg** og **0 publikationer**, der understøtter forudsigelsen. Den hviler udelukkende på en modelscore.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Ikke angivet i datagrundlaget (produktet er et veterinærlægemiddel) |
| Forudsagt ny indikation | Interventrikulær septumaneurisme |
| TxGNN-forudsigelsesscore | 99,25 % |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført |
| Antal markedsføringstilladelser | 1 |
| Anbefalet beslutning | Hold |

---

## Hvorfor er forudsigelsen (ikke) rimelig?

Der foreligger ingen detaljerede data om thymols virkningsmekanisme. Thymol er et monoterpen-phenol, og i prækliniske studier er der beskrevet antimikrobielle, antioxidative og antiinflammatoriske egenskaber. Der er dog ikke dokumenteret nogen sammenhæng mellem disse egenskaber og de forudsagte hjertesygdomme.

Interventrikulær septumaneurisme er en strukturel hjertemisdannelse. Der er ingen kendt thymol-relateret mekanisme, som kan påvirke den. Den høje score (0,992) er en forudsigelse fra vidensgrafen og ikke et farmakologisk fund.

De fem unikke forudsagte indikationer er alle medfødte strukturelle eller udviklingsmæssige tilstande med næsten identiske scorer. Det tyder på en artefakt i vidensgrafens naboskab frem for fem uafhængige signaler. Datagrundlaget indeholder hver indikation to gange (dublerede poster); tabellen viser dem kun én gang.

| Forudsagt indikation | TxGNN-score | Evidensniveau | Beslutning |
|------|------|------|------|
| Interventrikulær septumaneurisme | 99,25 % | L5 | Hold |
| Pulmonalklapsygdom | 99,17 % | L5 | Hold |
| Laubry-Pezzi syndrom | 99,17 % | L5 | Hold |
| Genetisk syndromisk Pierre Robin-syndrom | 99,15 % | L5 | Hold |
| Orofacialt kløftsyndrom | 99,15 % | L5 | Hold |

---

## Klinisk evidens

Der er for øjeblikket ingen relaterede kliniske forsøg registreret.

---

## Litteraturevidens

Der er for øjeblikket ingen relateret litteratur tilgængelig.

---

## Information om markedet i Danmark

| Markedsføringstilladelse | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28103399802 | Apiguard Vet. (Vita Bee Health Ltd.) | Gel | Ikke angivet i datagrundlaget |

---

## Sikkerhedsovervejelser

Se det godkendte produktresumé (SmPC) for sikkerhedsoplysninger. Der er ikke fundet registrerede lægemiddelinteraktioner i datagrundlaget.

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelsen er rent modelbaseret (L5), uden kliniske forsøg, litteratur eller en plausibel mekanistisk forbindelse. Det eneste markedsførte produkt er et veterinærlægemiddel, og de forudsagte indikationer er strukturelle hjertemisdannelser, som thymol ikke forventes at kunne påvirke.

**For at komme videre kræves følgende:**
- Sikkerhedsoplysninger (advarsler og kontraindikationer) fra Lægemiddelstyrelsens produktresumé; denne mangel blokerer den videre sikkerhedsscreening
- Data om virkningsmekanisme (MOA) fra DrugBank
- Prækliniske eller mekanistiske data, der kan forbinde thymol med de forudsagte tilstande
- Afklaring af, om en human formulering overhovedet er relevant, da det eneste danske produkt er til veterinær brug

*Resultaterne er udelukkende til forskningsformål og udgør ikke medicinsk rådgivning. Forudsigelserne kræver klinisk validering, før de kan anvendes.*
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

