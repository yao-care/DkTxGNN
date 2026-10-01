---
layout: default
title: Orlistat
parent: Kun modelforudsigelse (L5)
nav_order: 323
evidence_level: L5
indication_count: 2
---

# Orlistat
{: .fs-9 }

Evidensniveau: **L5** | Forudsagte indikationer: **2** stk.
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

# Orlistat: Fra lipasehæmmer til hypervitaminose

## Resumé

Orlistat er en hæmmer af mave- og bugspytkirtellipaser, som nedsætter optagelsen af fedt fra kosten med ca. 30 %. TxGNN-modellen forudsiger, at lægemidlet kan have effekt ved **hypervitaminose**. Der er dog **ingen kliniske studier og ingen publikationer**, som understøtter forudsigelsen. Evidensniveauet er L5 (kun modelforudsigelse).

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Forudsagt ny indikation | Hypervitaminose |
| TxGNN-forudsigelsesscore | 99,42 % |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført |
| Antal markedsføringstilladelser | 1 |
| Anbefalet beslutning | Hold |

---

## Hvorfor er forudsigelsen (ikke) rimelig?

Orlistat hæmmer mave- og bugspytkirtellipaser og reducerer dermed fedtoptagelsen med ca. 30 %. Det nedsætter også optagelsen af de fedtopløselige vitaminer (A, D, E og K), og mærkningen advarer netop om mangel på disse vitaminer.

Der findes en hypotetisk begrundelse for forudsigelsen. Ved hypervitaminose med et fedtopløseligt vitamin (A eller D) kunne en lavere tarmoptagelse eller mindre enterohepatisk recirkulation teoretisk set mindske vitaminbelastningen.

Der er flere grunde til at være tilbageholdende:

- Scoren på 0,994 skyldes sandsynligvis en artefakt i vidensgrafen.
- Orlistats kendte vitaminrelaterede effekt er mangel, ikke overskud.
- "Hypervitaminose" er en bred betegnelse, som ikke angiver, hvilket vitamin der er tale om.
- Hypervitaminose behandles normalt ved at stoppe tilskuddet, så der er intet tydeligt uopfyldt behov, som en lipasehæmmer kunne dække.
- Detaljerede data om virkningsmekanisme og oprindelige indikationer er ikke tilgængelige, så forudsigelsen kan ikke krydstjekkes mod kuraterede lægemiddel-target-data.

Modellen returnerede den samme forudsigelse to gange (rang 1 og 2). Den er kun medtaget én gang her.

---

## Kliniske forsøg

Der er i øjeblikket ingen relaterede kliniske forsøg registreret.

---

## Litteraturevidens

Der er i øjeblikket ingen relateret litteratur tilgængelig.

---

## Markedsinformation for Danmark

| Markedsføringstilladelsesnummer | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28104222107 | alli (Glaxo Group Ltd) | Kapsler, hårde | Ikke angivet i data |

---

## Sikkerhedsovervejelser

- **Lægemiddelinteraktioner:** Der blev ikke fundet interaktionsdata i søgningen.
- **Vitaminoptagelse:** Ifølge mekanismen kan orlistat nedsætte optagelsen af fedtopløselige vitaminer (A, D, E, K), og mærkningen advarer om mangel.

Se i øvrigt det godkendte produktresumé (SmPC) for fuldstændige oplysninger om sikkerhed.

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelsen hviler udelukkende på en modelscore uden kliniske forsøg eller litteratur. Den kendte farmakologiske effekt (nedsat vitaminoptagelse) giver heller ikke et klart klinisk behov for orlistat ved hypervitaminose.

**For at komme videre kræves:**
- Produktresumé fra Lægemiddelstyrelsen med advarsler og kontraindikationer, da sikkerhedsscreening ikke kan gennemføres uden disse data
- Data om virkningsmekanisme (f.eks. via DrugBank API)
- Præcisering af, hvilken hypervitaminose (A, D eller andet) der menes
- Prækliniske eller mekanistiske studier, der kan understøtte hypotesen
- En litteratur- og forsøgssøgning målrettet de specifikke vitaminer

*Resultaterne er udelukkende til forskningsbrug og udgør ikke lægefaglig rådgivning. Kandidater til lægemiddelomplacering skal valideres klinisk, før de kan anvendes.*
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

